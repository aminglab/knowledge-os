#!/usr/bin/env python3
"""Validate the stable source metadata layer for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
METADATA_PATH = CASE_ROOT / "references-metadata-v1.md"
OBJECTS_ROOT = CASE_ROOT / "objects"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")
REQUIRED_FIELDS = [
    "Source type",
    "Authors",
    "Year",
    "Title",
    "Venue / host",
    "Canonical locator",
    "Role in case",
    "Object usage",
    "Notes",
]


class MetadataError(Exception):
    """Raised when reference metadata drifts from the current case layer."""


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
                "source_refs": list(frontmatter.get("source_refs", [])),
            }
    return objects


def parse_entries(markdown: str) -> dict[str, dict[str, str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, dict[str, str]] = {}
    for i in range(1, len(parts), 2):
        source_id = parts[i]
        block = parts[i + 1]
        fields: dict[str, str] = {}
        for field in REQUIRED_FIELDS:
            match = re.search(rf"^- {re.escape(field)}: (.+)$", block, re.M)
            if match:
                fields[field] = match.group(1).strip()
        entries[source_id] = fields
    return entries


def parse_object_usage(value: str) -> list[str]:
    return re.findall(r"`([A-Z]-\d{4})`", value)


def validate_metadata() -> dict[str, int]:
    objects = load_objects()
    markdown = read_text(METADATA_PATH)
    entries = parse_entries(markdown)

    object_source_ids = {
        source_id
        for obj in objects.values()
        for source_id in obj.get("source_refs", [])
    }

    errors: list[str] = []

    if set(entries) != object_source_ids:
        missing = sorted(object_source_ids - set(entries))
        extra = sorted(set(entries) - object_source_ids)
        if missing:
            errors.append("metadata layer is missing canonical source ids used by objects: " + ", ".join(missing))
        if extra:
            errors.append("metadata layer declares canonical source ids not used by current objects: " + ", ".join(extra))

    reverse_usage: dict[str, list[str]] = {}
    for object_id, obj in objects.items():
        for source_id in obj.get("source_refs", []):
            reverse_usage.setdefault(source_id, []).append(object_id)

    for source_id, fields in sorted(entries.items()):
        for field in REQUIRED_FIELDS:
            if not fields.get(field):
                errors.append(f"{source_id}: missing required field `{field}`")

        declared_usage = parse_object_usage(fields.get("Object usage", ""))
        expected_usage = sorted(reverse_usage.get(source_id, []))
        if sorted(declared_usage) != expected_usage:
            errors.append(
                f"{source_id}: object usage mismatch; declared {declared_usage or []} but expected {expected_usage}"
            )

        if len(declared_usage) != len(set(declared_usage)):
            errors.append(f"{source_id}: object usage contains duplicate object ids")

    if errors:
        raise MetadataError("\n".join(errors))

    return {
        "source_ids": len(entries),
        "objects_total": len(objects),
        "object_source_links": sum(len(obj.get("source_refs", [])) for obj in objects.values()),
    }


def main() -> None:
    try:
        summary = validate_metadata()
    except MetadataError as exc:
        print("Reference metadata consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Reference metadata consistency passed.")
    print()
    print(f"- source ids: {summary['source_ids']}")
    print(f"- objects total: {summary['objects_total']}")
    print(f"- object-source links: {summary['object_source_links']}")


if __name__ == "__main__":
    main()
