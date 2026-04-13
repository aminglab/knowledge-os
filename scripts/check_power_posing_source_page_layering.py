#!/usr/bin/env python3
"""Validate source-page layering for the power-posing pilot."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
SOURCES_ROOT = CASE_ROOT / "sources"
METADATA_PATH = CASE_ROOT / "references-metadata-v1.md"

SOURCE_PAGE_SECTIONS = [
    "Source identity",
    "Source role in the case",
    "Case usage",
    "Object usage",
    "Public reading routes",
]

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")


class SourcePageLayeringError(Exception):
    """Raised when a source page loses required public-layer structure."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section_present(markdown: str, title: str) -> bool:
    return re.search(rf"^## {re.escape(title)}$", markdown, re.M) is not None


def extract_canonical_source_id(markdown: str) -> str | None:
    match = re.search(r"\*\*Canonical source id:\*\* `(.*?)`", markdown)
    return match.group(1) if match else None


def extract_title(markdown: str) -> str | None:
    match = re.search(r"\*\*Title:\*\* (.+?)\s{2,}$", markdown, re.M)
    return match.group(1).strip() if match else None


def normalize_text(text: str | None) -> str:
    if not text:
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.casefold()


def parse_metadata_entries(markdown: str) -> dict[str, dict[str, str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, dict[str, str]] = {}
    for i in range(1, len(parts), 2):
        entry_id = parts[i]
        block = parts[i + 1]
        fields: dict[str, str] = {}
        for field in ["Title", "Role in case", "Object usage"]:
            match = re.search(rf"^- {re.escape(field)}: (.+)$", block, re.M)
            if match:
                fields[field] = match.group(1).strip()
        entries[entry_id] = fields
    return entries


def validate() -> dict[str, int]:
    metadata_entries = parse_metadata_entries(read_text(METADATA_PATH))
    source_pages = sorted(path for path in SOURCES_ROOT.glob("*.md") if path.name != "README.md")
    errors: list[str] = []

    for source_page_path in source_pages:
        markdown = read_text(source_page_path)
        source_id = source_page_path.stem

        for section in SOURCE_PAGE_SECTIONS:
            if not section_present(markdown, section):
                errors.append(f"{source_id}: missing required section `## {section}`")

        page_source_id = extract_canonical_source_id(markdown)
        if page_source_id != source_id:
            errors.append(
                f"{source_id}: page canonical source id is `{page_source_id}` but filename requires `{source_id}`"
            )

        metadata = metadata_entries.get(source_id)
        if not metadata:
            errors.append(f"{source_id}: no metadata entry found in references-metadata-v1.md")
            continue

        page_title = extract_title(markdown)
        metadata_title = metadata.get("Title")
        if normalize_text(page_title) != normalize_text(metadata_title):
            errors.append(
                f"{source_id}: page title `{page_title}` does not match metadata title `{metadata_title}`"
            )

        if "## Object usage" in markdown and not re.search(r"- \[`[A-Z]-\d{4}`\]", markdown):
            errors.append(f"{source_id}: object usage section contains no linked governed objects")

    if errors:
        raise SourcePageLayeringError("\n".join(errors))

    return {
        "source_pages": len(source_pages),
        "required_sections_per_page": len(SOURCE_PAGE_SECTIONS),
        "metadata_entries_seen": len(metadata_entries),
    }


def main() -> None:
    try:
        summary = validate()
    except SourcePageLayeringError as exc:
        print("Source page layering failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Source page layering passed.")
    print()
    print(f"- source pages checked: {summary['source_pages']}")
    print(f"- required sections per page: {summary['required_sections_per_page']}")
    print(f"- metadata entries seen: {summary['metadata_entries_seen']}")


if __name__ == "__main__":
    main()
