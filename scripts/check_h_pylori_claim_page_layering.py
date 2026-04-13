#!/usr/bin/env python3
"""Validate claim-page layering for the h-pylori-ulcer pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
CLAIMS_ROOT = CASE_ROOT / "claims"
OBJECT_CLAIMS_ROOT = CASE_ROOT / "objects" / "claims"
OBJECT_VERDICTS_ROOT = CASE_ROOT / "objects" / "verdicts"

CLAIM_PAGE_SECTIONS = [
    "Claim identity",
    "Current visible judgment",
    "Support surface",
    "Challenge surface",
    "Lineage placement",
]


class ClaimPageLayeringError(Exception):
    """Raised when a claim page loses required neighborhood-summary structure."""


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


def load_frontmatter(path: Path) -> dict[str, Any]:
    return parse_frontmatter(extract_frontmatter(read_text(path)))


def section_present(markdown: str, title: str) -> bool:
    return re.search(rf"^## {re.escape(title)}$", markdown, re.M) is not None


def extract_linked_verdict(markdown: str) -> str | None:
    match = re.search(r"\*\*Linked verdict:\*\* \[`(V-\d{4})`\]", markdown)
    return match.group(1) if match else None


def extract_claim_id(markdown: str) -> str | None:
    match = re.search(r"\*\*Claim id:\*\* `(C-\d{4})`", markdown)
    return match.group(1) if match else None


def validate() -> dict[str, int]:
    claim_pages = sorted(path for path in CLAIMS_ROOT.glob("C-*.md") if path.is_file())
    errors: list[str] = []

    for claim_page_path in claim_pages:
        markdown = read_text(claim_page_path)
        claim_id = claim_page_path.stem

        for section in CLAIM_PAGE_SECTIONS:
            if not section_present(markdown, section):
                errors.append(f"{claim_id}: missing required section `## {section}`")

        page_claim_id = extract_claim_id(markdown)
        if page_claim_id != claim_id:
            errors.append(f"{claim_id}: page claim id marker is `{page_claim_id}` but filename requires `{claim_id}`")

        linked_verdict_id = extract_linked_verdict(markdown)
        if not linked_verdict_id:
            errors.append(f"{claim_id}: missing `Linked verdict` reference in current visible judgment section")
            continue

        verdict_path = OBJECT_VERDICTS_ROOT / f"{linked_verdict_id}.md"
        if not verdict_path.exists():
            errors.append(f"{claim_id}: linked verdict `{linked_verdict_id}` does not exist")
            continue

        verdict_meta = load_frontmatter(verdict_path)
        target_claim_id = verdict_meta.get("target_claim_id")
        if target_claim_id != claim_id:
            errors.append(
                f"{claim_id}: linked verdict `{linked_verdict_id}` targets `{target_claim_id}` instead of `{claim_id}`"
            )

        claim_obj_path = OBJECT_CLAIMS_ROOT / f"{claim_id}.md"
        if not claim_obj_path.exists():
            errors.append(f"{claim_id}: missing governed claim object `{claim_id}.md`")
            continue

        if "## Support surface" in markdown and not re.search(r"- \[`E-\d{4}`\]", markdown):
            errors.append(f"{claim_id}: support surface contains no linked evidence objects")

        if "## Challenge surface" in markdown and not re.search(r"- \[`D-\d{4}`\]", markdown):
            errors.append(f"{claim_id}: challenge surface contains no linked dissent objects")

        lineage_section = re.search(r"## Lineage placement\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S)
        if not lineage_section or not re.search(r"\[`C-\d{4}`\]", lineage_section.group(1)):
            errors.append(f"{claim_id}: lineage placement contains no linked claim route")

    if errors:
        raise ClaimPageLayeringError("\n".join(errors))

    return {
        "claim_pages": len(claim_pages),
        "required_sections_per_page": len(CLAIM_PAGE_SECTIONS),
    }


def main() -> None:
    try:
        summary = validate()
    except ClaimPageLayeringError as exc:
        print("H. pylori claim page layering failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori claim page layering passed.")
    print()
    print(f"- claim pages checked: {summary['claim_pages']}")
    print(f"- required sections per page: {summary['required_sections_per_page']}")


if __name__ == "__main__":
    main()
