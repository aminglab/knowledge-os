#!/usr/bin/env python3
"""Validate snapshot subsection semantic anchors for the power-posing pilot."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
ANCHORS_PATH = CASE_ROOT / "snapshot-subsection-semantic-anchors-v1.md"

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")


class SnapshotSubsectionSemanticError(Exception):
    """Raised when a snapshot subsection loses required semantic anchors."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(markdown: str, title: str) -> str:
    pattern = rf"## {re.escape(title)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1) if match else ""


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    text = re.sub(r"[`*_]", "", text)
    text = text.replace("/", " ")
    text = text.replace("-", " ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_anchor_entries(markdown: str) -> dict[str, list[str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, list[str]] = {}
    for i in range(1, len(parts), 2):
        block = parts[i + 1]
        section_match = re.search(r"^- Section: `([^`]+)`$", block, re.M)
        anchors_match = re.search(r"^- Required anchors:\n((?:  - `.*`\n?)+)", block, re.M)
        if not section_match or not anchors_match:
            continue
        section_title = section_match.group(1)
        anchors = re.findall(r"  - `([^`]+)`", anchors_match.group(1))
        entries[section_title] = anchors
    return entries


def validate() -> dict[str, int]:
    snapshot_markdown = read_text(SNAPSHOT_PATH)
    anchor_entries = parse_anchor_entries(read_text(ANCHORS_PATH))
    errors: list[str] = []
    anchors_checked = 0

    for section_title, anchors in sorted(anchor_entries.items()):
        section_body = extract_section(snapshot_markdown, section_title)
        if not section_body:
            errors.append(f"snapshot-v2: missing section body for `{section_title}`")
            continue

        normalized_section = normalize_text(section_body)
        for anchor in anchors:
            anchors_checked += 1
            if normalize_text(anchor) not in normalized_section:
                errors.append(
                    f"snapshot-v2: section `{section_title}` is missing required anchor `{anchor}`"
                )

    if errors:
        raise SnapshotSubsectionSemanticError("\n".join(errors))

    return {
        "sections_checked": len(anchor_entries),
        "anchors_checked": anchors_checked,
    }


def main() -> None:
    try:
        summary = validate()
    except SnapshotSubsectionSemanticError as exc:
        print("Snapshot subsection semantic anchors failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Snapshot subsection semantic anchors passed.")
    print()
    print(f"- sections checked: {summary['sections_checked']}")
    print(f"- anchors checked: {summary['anchors_checked']}")


if __name__ == "__main__":
    main()
