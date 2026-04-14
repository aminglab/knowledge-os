#!/usr/bin/env python3
"""Validate source-page role-anchor coverage for the h-pylori-ulcer pilot."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
SOURCES_ROOT = CASE_ROOT / "sources"
ROLE_ANCHORS_PATH = CASE_ROOT / "source-page-role-anchors-v1.md"

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")


class SourcePageRoleAnchorError(Exception):
    """Raised when a source page loses required role anchors."""


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


def parse_role_anchor_entries(markdown: str) -> dict[str, list[str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, list[str]] = {}
    for i in range(1, len(parts), 2):
        entry_id = parts[i]
        block = parts[i + 1]
        source_match = re.search(r"^- Source id: `([^`]+)`$", block, re.M)
        anchors_match = re.search(r"^- Required role anchors:\n((?:  - `.*`\n?)+)", block, re.M)
        if not source_match or not anchors_match:
            entries[entry_id] = []
            continue
        source_id = source_match.group(1)
        anchors = re.findall(r"  - `([^`]+)`", anchors_match.group(1))
        entries[source_id] = anchors
    return entries


def validate() -> dict[str, int]:
    role_anchor_entries = parse_role_anchor_entries(read_text(ROLE_ANCHORS_PATH))
    errors: list[str] = []
    anchors_checked = 0

    for source_id, anchors in sorted(role_anchor_entries.items()):
        source_page_path = SOURCES_ROOT / f"{source_id}.md"
        if not source_page_path.exists():
            errors.append(f"{source_id}: source page does not exist")
            continue

        markdown = read_text(source_page_path)
        role_section = extract_section(markdown, "Source role in the case")
        if not role_section:
            errors.append(f"{source_id}: missing `Source role in the case` section body")
            continue

        normalized_role = normalize_text(role_section)
        for anchor in anchors:
            anchors_checked += 1
            if normalize_text(anchor) not in normalized_role:
                errors.append(f"{source_id}: source role section is missing required anchor `{anchor}`")

    if errors:
        raise SourcePageRoleAnchorError("\n".join(errors))

    return {
        "source_pages": len(role_anchor_entries),
        "anchors_checked": anchors_checked,
    }


def main() -> None:
    try:
        summary = validate()
    except SourcePageRoleAnchorError as exc:
        print("H. pylori source page role-anchor coverage failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori source page role-anchor coverage passed.")
    print()
    print(f"- source pages checked: {summary['source_pages']}")
    print(f"- role anchors checked: {summary['anchors_checked']}")


if __name__ == "__main__":
    main()
