#!/usr/bin/env python3
"""Validate direct support/challenge coverage on H. pylori claim pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
CLAIMS_ROOT = CASE_ROOT / "claims"
OBJECTS_ROOT = CASE_ROOT / "objects"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

PRESSURE_TYPES = {"supports", "challenges"}


class ClaimPagePressureCoverageError(Exception):
    """Raised when a claim page omits direct pressure-bearing object coverage."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return []
    return parts[0].splitlines()[1:]


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def parse_indented_block(lines: list[str]) -> Any:
    block = [line for line in lines if line.strip()]
    if not block:
        return None

    if block[0].startswith("  - "):
        items: list[Any] = []
        i = 0
        while i < len(block):
            line = block[i]
            if not line.startswith("  - "):
                i += 1
                continue

            item_head = line[4:]
            dict_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", item_head)
            if dict_match:
                item: Any = {dict_match.group(1): parse_scalar(dict_match.group(2))}
            else:
                item = parse_scalar(item_head)

            i += 1
            while i < len(block) and block[i].startswith("    "):
                nested = block[i][4:]
                nested_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", nested)
                if isinstance(item, dict) and nested_match:
                    item[nested_match.group(1)] = parse_scalar(nested_match.group(2))
                i += 1

            items.append(item)
        return items

    mapping: dict[str, Any] = {}
    for line in block:
        if not line.startswith("  "):
            continue
        nested = line[2:]
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", nested)
        if match:
            mapping[match.group(1)] = parse_scalar(match.group(2))
    return mapping if mapping else None


def parse_frontmatter(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        top_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$", line)
        if not top_match:
            i += 1
            continue

        key = top_match.group(1)
        value = top_match.group(2)
        if value:
            data[key] = parse_scalar(value)
            i += 1
            continue

        i += 1
        block: list[str] = []
        while i < len(lines):
            nxt = lines[i]
            if nxt.startswith("  ") or not nxt.strip():
                block.append(nxt)
                i += 1
            else:
                break

        data[key] = parse_indented_block(block)

    return data


def load_objects() -> dict[str, dict[str, Any]]:
    objects: dict[str, dict[str, Any]] = {}
    for object_type, directory in OBJECT_DIRS.items():
        for path in sorted(directory.glob("*.md")):
            frontmatter = parse_frontmatter(extract_frontmatter(read_text(path)))
            object_id = str(frontmatter.get("id", path.stem))
            objects[object_id] = {
                "id": object_id,
                "object_type": object_type,
                "path": path,
                "frontmatter": frontmatter,
            }
    return objects


def extract_section(markdown: str, title: str) -> str:
    pattern = rf"## {re.escape(title)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1) if match else ""


def linked_object_ids(markdown: str) -> set[str]:
    return set(re.findall(r"\[`([A-Z]-\d{4})`\]", markdown))


def collect_inbound_pressure(objects: dict[str, dict[str, Any]]) -> dict[str, dict[str, list[str]]]:
    inbound: dict[str, dict[str, list[str]]] = {}
    for object_id, obj in objects.items():
        links = obj["frontmatter"].get("links")
        if not isinstance(links, list):
            continue
        for item in links:
            if not isinstance(item, dict):
                continue
            relation_type = item.get("type")
            target = item.get("target")
            if relation_type not in PRESSURE_TYPES:
                continue
            if not isinstance(target, str) or target not in objects:
                continue
            if objects[target]["object_type"] != "claim":
                continue
            inbound.setdefault(target, {"supports": [], "challenges": []})
            inbound[target][relation_type].append(object_id)

    for target_id in inbound:
        for relation_type in PRESSURE_TYPES:
            inbound[target_id][relation_type] = sorted(set(inbound[target_id][relation_type]))
    return inbound


def validate() -> dict[str, int]:
    objects = load_objects()
    inbound = collect_inbound_pressure(objects)
    claim_pages = sorted(path for path in CLAIMS_ROOT.glob("C-*.md") if path.is_file())
    errors: list[str] = []
    pressure_links_checked = 0

    for claim_page_path in claim_pages:
        claim_id = claim_page_path.stem
        markdown = read_text(claim_page_path)
        support_section = extract_section(markdown, "Support surface")
        challenge_section = extract_section(markdown, "Challenge surface")

        support_ids = linked_object_ids(support_section)
        challenge_ids = linked_object_ids(challenge_section)

        required_supports = inbound.get(claim_id, {}).get("supports", [])
        required_challenges = inbound.get(claim_id, {}).get("challenges", [])

        for support_id in required_supports:
            pressure_links_checked += 1
            if support_id not in support_ids:
                errors.append(
                    f"{claim_id}: support surface is missing direct supporting object `{support_id}`"
                )

        for challenge_id in required_challenges:
            pressure_links_checked += 1
            if challenge_id not in challenge_ids:
                errors.append(
                    f"{claim_id}: challenge surface is missing direct challenging object `{challenge_id}`"
                )

    if errors:
        raise ClaimPagePressureCoverageError("\n".join(errors))

    return {
        "claim_pages": len(claim_pages),
        "claims_with_direct_pressure": sum(1 for claim_id in [p.stem for p in claim_pages] if inbound.get(claim_id)),
        "direct_pressure_links_checked": pressure_links_checked,
    }


def main() -> None:
    try:
        summary = validate()
    except ClaimPagePressureCoverageError as exc:
        print("H. pylori claim page pressure coverage failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori claim page pressure coverage passed.")
    print()
    print(f"- claim pages checked: {summary['claim_pages']}")
    print(f"- claims with direct pressure-bearing objects: {summary['claims_with_direct_pressure']}")
    print(f"- direct pressure links checked: {summary['direct_pressure_links_checked']}")


if __name__ == "__main__":
    main()
