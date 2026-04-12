#!/usr/bin/env python3
"""Validate that the public-layer atlas remains exposed and synchronized."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
README_PATH = CASE_ROOT / "README.md"
PUBLIC_LAYER_ATLAS_PATH = CASE_ROOT / "public-layer-verification-atlas-v1.md"
CHECK_ATLAS_PATH = CASE_ROOT / "check-atlas-v1.md"

PUBLIC_LAYER_ATLAS_LINK = "./public-layer-verification-atlas-v1.md"
REQUIRED_ATLAS_TOKENS = [
    "make check-public-layer",
    "make power-posing-public-layer",
    "check-power-posing-public-layer.yml",
    "scripts/check_power_posing_public_layer.py",
]
FORBIDDEN_ATLAS_TOKENS = [
    "No unified public-layer orchestrator yet",
]


class PublicLayerAtlasError(Exception):
    """Raised when atlas exposure or atlas sync drifts."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def find_markdown_links(markdown: str) -> set[str]:
    return {target for _label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", markdown)}


def validate() -> dict[str, int]:
    readme_text = read_text(README_PATH)
    public_layer_atlas_text = read_text(PUBLIC_LAYER_ATLAS_PATH)
    check_atlas_text = read_text(CHECK_ATLAS_PATH)

    developer_governance_path = extract_section(readme_text, "Developer / governance path")
    folder_guide = extract_section(readme_text, "Folder guide")

    errors: list[str] = []

    developer_links = find_markdown_links(developer_governance_path)
    folder_links = find_markdown_links(folder_guide)

    if PUBLIC_LAYER_ATLAS_LINK not in developer_links:
        errors.append(
            "README developer / governance path is missing required public-layer atlas link "
            f"`{PUBLIC_LAYER_ATLAS_LINK}`"
        )
    if PUBLIC_LAYER_ATLAS_LINK not in folder_links:
        errors.append(
            "README folder guide is missing required public-layer atlas link "
            f"`{PUBLIC_LAYER_ATLAS_LINK}`"
        )

    if PUBLIC_LAYER_ATLAS_LINK not in check_atlas_text:
        errors.append("check-atlas-v1.md no longer points to public-layer-verification-atlas-v1.md")

    for token in REQUIRED_ATLAS_TOKENS:
        if token not in public_layer_atlas_text:
            errors.append(f"public-layer atlas is missing required current-state token `{token}`")

    for token in FORBIDDEN_ATLAS_TOKENS:
        if token in public_layer_atlas_text:
            errors.append(f"public-layer atlas still contains retired token `{token}`")

    if errors:
        raise PublicLayerAtlasError("\n".join(errors))

    return {
        "developer_governance_path_links": len(developer_links),
        "folder_guide_links": len(folder_links),
        "required_atlas_tokens": len(REQUIRED_ATLAS_TOKENS),
    }


def main() -> None:
    try:
        summary = validate()
    except PublicLayerAtlasError as exc:
        print("Public-layer atlas check failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Public-layer atlas check passed.")
    print()
    print(f"- developer / governance path links: {summary['developer_governance_path_links']}")
    print(f"- folder guide links: {summary['folder_guide_links']}")
    print(f"- required atlas tokens: {summary['required_atlas_tokens']}")


if __name__ == "__main__":
    main()
