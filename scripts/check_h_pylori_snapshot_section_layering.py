#!/usr/bin/env python3
"""Validate snapshot section layering for the h-pylori-ulcer pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v0.md"

REQUIRED_SECTIONS = [
    "Title",
    "What this page is",
    "Current visible judgment",
    "Why this case matters",
    "Core claim neighborhood",
    "What changed later",
    "Snapshot reading path",
    "Included objects",
]


class SnapshotSectionLayeringError(Exception):
    """Raised when the snapshot release view loses required structure."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section_present(markdown: str, title: str) -> bool:
    return re.search(rf"^## {re.escape(title)}$", markdown, re.M) is not None


def validate_current_visible_judgment(markdown: str, errors: list[str]) -> None:
    if "**stabilized**" not in markdown:
        errors.append("snapshot-v0: current visible judgment must surface the stabilized stronger claim state")
    if "**supported**" not in markdown:
        errors.append("snapshot-v0: current visible judgment must surface the supported descendant-claim state")


def validate_claim_neighborhood(markdown: str, errors: list[str]) -> None:
    section = re.search(r"## Core claim neighborhood\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S)
    if not section:
        errors.append("snapshot-v0: missing Core claim neighborhood section body")
        return

    body = section.group(1)
    if "../claims/C-0001.md" not in body:
        errors.append("snapshot-v0: core claim neighborhood must route to C-0001 claim page")
    if "../claims/C-0002.md" not in body:
        errors.append("snapshot-v0: core claim neighborhood must route to C-0002 claim page")


def validate_reading_path(markdown: str, errors: list[str]) -> None:
    section = re.search(r"## Snapshot reading path\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S)
    if not section:
        errors.append("snapshot-v0: missing Snapshot reading path section body")
        return

    body = section.group(1)
    if "../claims/README.md" not in body:
        errors.append("snapshot-v0: reading path must include claim-page route")
    if "../sources/README.md" not in body and "../references.md" not in body:
        errors.append("snapshot-v0: reading path must include source or references route")
    if "../timeline/events.md" not in body and "../README.md" not in body:
        errors.append("snapshot-v0: reading path must include timeline or case-entry route")


def validate_included_objects(markdown: str, errors: list[str]) -> None:
    section = re.search(r"## Included objects\n\n(.+?)(?:\n---\n|\Z)", markdown, re.S)
    if not section:
        errors.append("snapshot-v0: missing Included objects section body")
        return

    body = section.group(1)
    for phrase in ["2 claims", "3 evidence objects", "3 dissent objects", "2 verdict objects"]:
        if phrase not in body:
            errors.append(f"snapshot-v0: included objects section is missing `{phrase}`")


def validate() -> dict[str, int]:
    markdown = read_text(SNAPSHOT_PATH)
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
        if not section_present(markdown, section):
            errors.append(f"snapshot-v0: missing required section `## {section}`")

    validate_current_visible_judgment(markdown, errors)
    validate_claim_neighborhood(markdown, errors)
    validate_reading_path(markdown, errors)
    validate_included_objects(markdown, errors)

    if errors:
        raise SnapshotSectionLayeringError("\n".join(errors))

    return {
        "required_sections": len(REQUIRED_SECTIONS),
    }


def main() -> None:
    try:
        summary = validate()
    except SnapshotSectionLayeringError as exc:
        print("H. pylori snapshot section layering failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori snapshot section layering passed.")
    print()
    print(f"- required sections checked: {summary['required_sections']}")


if __name__ == "__main__":
    main()
