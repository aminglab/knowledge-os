#!/usr/bin/env python3
"""Validate that snapshot-v2 remains consistent with the current power-posing case layer.

This check is intentionally case-scoped.
It hardens the public-facing snapshot against drift from:

- the governed object set,
- the current references layer,
- and the linked object paths exposed to readers.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
REFERENCES_PATH = CASE_ROOT / "references-metadata-v1.md"
OBJECTS_ROOT = CASE_ROOT / "objects"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

OBJECT_LINK_RE = re.compile(r"\[`([A-Z]-\d{4})`\]\(([^)]+)\)")
REFERENCE_HEADING_RE = re.compile(r"^### `([^`]+)`$", re.M)


class ConsistencyError(Exception):
    """Raised when snapshot-v2 drifts from the current case layer."""


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

        block = [b for b in block if b.strip()]
        if all(b.startswith("  - ") and not re.search(r":\s", b[4:]) for b in block):
            data[key] = [parse_scalar(b[4:]) for b in block]
        else:
            data[key] = None

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
                "path": path.resolve(),
                "source_refs": list(frontmatter.get("source_refs", [])),
            }
    return objects


def parse_reference_ids(markdown: str) -> set[str]:
    return {match.group(1) for match in REFERENCE_HEADING_RE.finditer(markdown)}


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def parse_snapshot_object_links(markdown: str) -> list[tuple[str, str]]:
    return OBJECT_LINK_RE.findall(markdown)


def parse_included_object_ids(section_text: str) -> list[str]:
    return [object_id for object_id, _ in OBJECT_LINK_RE.findall(section_text)]


def parse_reading_path_object_ids(section_text: str) -> list[str]:
    return [object_id for object_id, _ in OBJECT_LINK_RE.findall(section_text)]


def parse_snapshot_source_ids(markdown: str, reference_ids: set[str]) -> set[str]:
    inline_codes = re.findall(r"`([^`]+)`", markdown)
    return {code for code in inline_codes if code in reference_ids}


def validate_consistency() -> dict[str, int]:
    snapshot_text = read_text(SNAPSHOT_PATH)
    references_text = read_text(REFERENCES_PATH)
    objects = load_objects()
    reference_ids = parse_reference_ids(references_text)

    linked_objects = parse_snapshot_object_links(snapshot_text)
    included_ids = parse_included_object_ids(extract_section(snapshot_text, "Included objects"))
    reading_path_ids = parse_reading_path_object_ids(extract_section(snapshot_text, "Snapshot reading path"))
    mentioned_source_ids = parse_snapshot_source_ids(snapshot_text, reference_ids)
    object_source_ids = {
        source_id
        for obj in objects.values()
        for source_id in obj.get("source_refs", [])
    }

    errors: list[str] = []

    if not included_ids:
        errors.append("snapshot-v2.md has no parseable object list in `## Included objects`")

    expected_object_ids = set(objects)
    included_set = set(included_ids)
    if included_set != expected_object_ids:
        missing = sorted(expected_object_ids - included_set)
        extra = sorted(included_set - expected_object_ids)
        if missing:
            errors.append("Included objects section is missing: " + ", ".join(missing))
        if extra:
            errors.append("Included objects section has unknown entries: " + ", ".join(extra))

    if len(included_ids) != len(included_set):
        errors.append("Included objects section contains duplicate object ids")

    if len(reading_path_ids) != len(set(reading_path_ids)):
        errors.append("Snapshot reading path contains duplicate object ids")

    unknown_reading_path_ids = sorted(set(reading_path_ids) - expected_object_ids)
    if unknown_reading_path_ids:
        errors.append("Snapshot reading path references unknown objects: " + ", ".join(unknown_reading_path_ids))

    if mentioned_source_ids != object_source_ids:
        missing = sorted(object_source_ids - mentioned_source_ids)
        extra = sorted(mentioned_source_ids - object_source_ids)
        if missing:
            errors.append("snapshot-v2.md is missing canonical source ids used by objects: " + ", ".join(missing))
        if extra:
            errors.append("snapshot-v2.md mentions canonical source ids not used by current objects: " + ", ".join(extra))

    for object_id, rel_target in linked_objects:
        if object_id not in objects:
            errors.append(f"snapshot-v2.md links unknown object `{object_id}`")
            continue
        resolved = (SNAPSHOT_PATH.parent / rel_target).resolve()
        expected = objects[object_id]["path"]
        if resolved != expected:
            errors.append(
                f"snapshot-v2.md links `{object_id}` to `{rel_target}`, but current object path is `{expected.relative_to(CASE_ROOT)}`"
            )

    if errors:
        raise ConsistencyError("\n".join(errors))

    return {
        "objects_total": len(objects),
        "included_objects": len(included_ids),
        "reading_path_objects": len(reading_path_ids),
        "linked_object_mentions": len(linked_objects),
        "canonical_source_ids": len(mentioned_source_ids),
    }


def main() -> None:
    try:
        summary = validate_consistency()
    except ConsistencyError as exc:
        print("Snapshot consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Snapshot consistency passed.")
    print()
    print(f"- objects total: {summary['objects_total']}")
    print(f"- included objects: {summary['included_objects']}")
    print(f"- reading path objects: {summary['reading_path_objects']}")
    print(f"- linked object mentions: {summary['linked_object_mentions']}")
    print(f"- canonical source ids: {summary['canonical_source_ids']}")


if __name__ == "__main__":
    main()
