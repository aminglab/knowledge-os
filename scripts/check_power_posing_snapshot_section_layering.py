#!/usr/bin/env python3
"""Validate snapshot section layering for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
OBJECTS_ROOT = CASE_ROOT / "objects"

REQUIRED_SECTIONS = [
    "Title",
    "What this page is",
    "Current visible judgment",
    "Why this case matters",
    "Original claim neighborhood",
    "What changed later",
    "Snapshot reading path",
    "Included objects",
]

EXPECTED_INCLUDED_OBJECTS = [
    "C-0001",
    "C-0002",
    "E-0001",
    "D-0001",
    "D-0002",
    "D-0003",
    "V-0001",
    "V-0002",
]


class SnapshotSectionLayeringError(Exception):
    """Raised when the snapshot release view loses required structure."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section_present(markdown: str, title: str) -> bool:
    return re.search(rf"^## {re.escape(title)}$", markdown, re.M) is not None


def validate_current_visible_judgment(markdown: str, errors: list[str]) -> None:
    if "../status-legend-v1.md" not in markdown:
        errors.append("snapshot-v2: current visible judgment section must link to status-legend-v1.md")
    if "../verdict-grammar-v1.md" not in markdown:
        errors.append("snapshot-v2: current visible judgment section must link to verdict-grammar-v1.md")

    if not re.search(r"### Original claim\n\*\*Current state:\*\* (.+)", markdown):
        errors.append("snapshot-v2: missing Original claim current-state block in current visible judgment section")
    if not re.search(r"### Descendant claim\n\*\*Current state:\*\* (.+)", markdown):
        errors.append("snapshot-v2: missing Descendant claim current-state block in current visible judgment section")


def validate_reading_path(markdown: str, errors: list[str]) -> None:
    reading_path_match = re.search(
        r"## Snapshot reading path\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S
    )
    if not reading_path_match:
        errors.append("snapshot-v2: missing Snapshot reading path section body")
        return

    body = reading_path_match.group(1)
    if "status-legend-v1.md" not in body and "verdict-grammar-v1.md" not in body:
        errors.append("snapshot-v2: reading path must include status legend or verdict grammar route")
    if "../claims/" not in body:
        errors.append("snapshot-v2: reading path must include claim page route")
    if "../objects/" not in body and "timeline/events.md" not in body:
        errors.append("snapshot-v2: reading path must include object-layer or timeline route")
    if "../sources/" not in body and "../references" not in body:
        errors.append("snapshot-v2: reading path must include source or references route")


def validate_included_objects(markdown: str, errors: list[str]) -> None:
    included_match = re.search(r"## Included objects\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S)
    if not included_match:
        errors.append("snapshot-v2: missing Included objects section body")
        return

    body = included_match.group(1)
    for object_id in EXPECTED_INCLUDED_OBJECTS:
        if f"[`{object_id}`]" not in body:
            errors.append(f"snapshot-v2: included objects section is missing `{object_id}`")

        object_family = {
            "C": "claims",
            "E": "evidence",
            "D": "dissents",
            "V": "verdicts",
        }[object_id[0]]
        object_path = OBJECTS_ROOT / object_family / f"{object_id}.md"
        if not object_path.exists():
            errors.append(f"snapshot-v2: governed object file for `{object_id}` does not exist")


def validate() -> dict[str, int]:
    markdown = read_text(SNAPSHOT_PATH)
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if not section_present(markdown, section):
            errors.append(f"snapshot-v2: missing required section `## {section}`")

    validate_current_visible_judgment(markdown, errors)
    validate_reading_path(markdown, errors)
    validate_included_objects(markdown, errors)

    if errors:
        raise SnapshotSectionLayeringError("\n".join(errors))

    return {
        "required_sections": len(REQUIRED_SECTIONS),
        "included_objects": len(EXPECTED_INCLUDED_OBJECTS),
    }


def main() -> None:
    try:
        summary = validate()
    except SnapshotSectionLayeringError as exc:
        print("Snapshot section layering failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Snapshot section layering passed.")
    print()
    print(f"- required sections checked: {summary['required_sections']}")
    print(f"- included objects checked: {summary['included_objects']}")


if __name__ == "__main__":
    main()
