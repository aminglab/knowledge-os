#!/usr/bin/env python3
"""Validate the reader-facing public surface for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
README_PATH = CASE_ROOT / "README.md"

REQUIRED_SNAPSHOT_CURRENT_VISIBLE_JUDGMENT_LINKS = {
    "../status-legend-v1.md": "public wording note for current status phrases",
    "../verdict-grammar-v1.md": "case-scoped bridge between snapshot wording and object-layer judgment fields",
}

REQUIRED_SNAPSHOT_READING_PATH_LINKS = [
    "../status-legend-v1.md",
    "../verdict-grammar-v1.md",
    "../references.md",
    "../references-metadata-v1.md",
]

REQUIRED_README_READER_PATH_LINKS = [
    "./references.md",
    "./references-metadata-v1.md",
    "./status-legend-v1.md",
    "./verdict-grammar-v1.md",
]


class PublicSurfaceError(Exception):
    """Raised when the reader-facing public surface drifts from the current case design."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def find_markdown_links(markdown: str) -> list[tuple[str, str]]:
    return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", markdown)


def validate() -> dict[str, int]:
    snapshot_text = read_text(SNAPSHOT_PATH)
    readme_text = read_text(README_PATH)

    snapshot_judgment_section = extract_section(snapshot_text, "Current visible judgment")
    snapshot_reading_path = extract_section(snapshot_text, "Snapshot reading path")
    readme_reader_path = extract_section(readme_text, "Reader path")

    errors: list[str] = []

    judgment_links = {target: label for label, target in find_markdown_links(snapshot_judgment_section)}
    for target, expected_label_fragment in REQUIRED_SNAPSHOT_CURRENT_VISIBLE_JUDGMENT_LINKS.items():
        if target not in judgment_links:
            errors.append(f"snapshot current visible judgment is missing required link `{target}`")
        elif expected_label_fragment not in judgment_links[target]:
            errors.append(
                f"snapshot current visible judgment link `{target}` has label `{judgment_links[target]}` which does not contain `{expected_label_fragment}`"
            )

    snapshot_reading_path_targets = [target for _, target in find_markdown_links(snapshot_reading_path)]
    for target in REQUIRED_SNAPSHOT_READING_PATH_LINKS:
        if target not in snapshot_reading_path_targets:
            errors.append(f"snapshot reading path is missing required link `{target}`")

    readme_reader_path_targets = [target for _, target in find_markdown_links(readme_reader_path)]
    for target in REQUIRED_README_READER_PATH_LINKS:
        if target not in readme_reader_path_targets:
            errors.append(f"README reader path is missing required link `{target}`")

    if errors:
        raise PublicSurfaceError("\n".join(errors))

    return {
        "snapshot_current_visible_judgment_links": len(judgment_links),
        "snapshot_reading_path_links": len(snapshot_reading_path_targets),
        "readme_reader_path_links": len(readme_reader_path_targets),
    }


def main() -> None:
    try:
        summary = validate()
    except PublicSurfaceError as exc:
        print("Public surface consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Public surface consistency passed.")
    print()
    print(f"- snapshot current visible judgment links: {summary['snapshot_current_visible_judgment_links']}")
    print(f"- snapshot reading path links: {summary['snapshot_reading_path_links']}")
    print(f"- README reader path links: {summary['readme_reader_path_links']}")


if __name__ == "__main__":
    main()
