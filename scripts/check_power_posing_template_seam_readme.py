#!/usr/bin/env python3
"""Validate that template seam documents remain exposed in the power-posing README."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
README_PATH = CASE_ROOT / "README.md"

REQUIRED_TEMPLATE_SEAM_LINKS = {
    "./case-template-boundary-v1.md": "boundary ruling",
    "./case-template-extraction-checklist-v1.md": "copy discipline",
    "./template-seam-summary-v1.md": "consolidated seam ruling",
}


class TemplateSeamReadmeError(Exception):
    """Raised when README drift hides required template seam documents."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def find_markdown_links_with_lines(markdown: str) -> list[tuple[str, str, str]]:
    results: list[tuple[str, str, str]] = []
    for line in markdown.splitlines():
        for label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", line):
            results.append((label, target, line.strip()))
    return results


def validate() -> dict[str, int]:
    readme_text = read_text(README_PATH)

    reader_path = extract_section(readme_text, "Reader path")
    folder_guide = extract_section(readme_text, "Folder guide")

    errors: list[str] = []

    reader_links = {target: (label, line) for label, target, line in find_markdown_links_with_lines(reader_path)}
    folder_links = {target: (label, line) for label, target, line in find_markdown_links_with_lines(folder_guide)}

    for target, meaning in REQUIRED_TEMPLATE_SEAM_LINKS.items():
        if target not in reader_links:
            errors.append(f"README reader path is missing required template seam link `{target}` ({meaning})")
        if target not in folder_links:
            errors.append(f"README folder guide is missing required template seam link `{target}` ({meaning})")

    if errors:
        raise TemplateSeamReadmeError("\n".join(errors))

    return {
        "reader_path_links": len(reader_links),
        "folder_guide_links": len(folder_links),
        "required_template_seam_links": len(REQUIRED_TEMPLATE_SEAM_LINKS),
    }


def main() -> None:
    try:
        summary = validate()
    except TemplateSeamReadmeError as exc:
        print("README template seam audit failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("README template seam audit passed.")
    print()
    print(f"- reader path links: {summary['reader_path_links']}")
    print(f"- folder guide links: {summary['folder_guide_links']}")
    print(f"- required template seam links: {summary['required_template_seam_links']}")


if __name__ == "__main__":
    main()
