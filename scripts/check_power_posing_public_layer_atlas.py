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
ATLAS_AUTHORITY_RULING_PATH = CASE_ROOT / "atlas-authority-boundary-ruling-v1.md"
ATLAS_MERGE_THRESHOLD_PATH = CASE_ROOT / "atlas-merge-threshold-v1.md"

PUBLIC_LAYER_ATLAS_LINK = "./public-layer-verification-atlas-v1.md"
CHECK_ATLAS_LINK = "./check-atlas-v1.md"
ATLAS_AUTHORITY_RULING_LINK = "./atlas-authority-boundary-ruling-v1.md"
ATLAS_MERGE_THRESHOLD_LINK = "./atlas-merge-threshold-v1.md"

REQUIRED_ATLAS_TOKENS = [
    "make check-public-layer",
    "make power-posing-public-layer",
    "check-power-posing-public-layer.yml",
    "scripts/check_power_posing_public_layer.py",
    "check_power_posing_public_layer_atlas.py",
]
FORBIDDEN_PUBLIC_LAYER_ATLAS_TOKENS = [
    "No unified public-layer orchestrator yet",
    "No public-layer atlas checker yet",
]
REQUIRED_RULING_TOKENS = [
    "check-atlas-v1.md",
    "public-layer-verification-atlas-v1.md",
    "Do not merge them yet.",
    "atlas-merge-threshold-v1.md",
]
REQUIRED_THRESHOLD_TOKENS = [
    "HOLD_NO_ATLAS_MERGE",
    "check-atlas-v1.md",
    "public-layer-verification-atlas-v1.md",
    "atlas-authority-boundary-ruling-v1.md",
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
    authority_ruling_text = read_text(ATLAS_AUTHORITY_RULING_PATH)
    merge_threshold_text = read_text(ATLAS_MERGE_THRESHOLD_PATH)

    developer_governance_path = extract_section(readme_text, "Developer / governance path")
    folder_guide = extract_section(readme_text, "Folder guide")

    errors: list[str] = []

    developer_links = find_markdown_links(developer_governance_path)
    folder_links = find_markdown_links(folder_guide)

    for link_name, link_target in [
        ("public-layer atlas", PUBLIC_LAYER_ATLAS_LINK),
        ("check atlas", CHECK_ATLAS_LINK),
        ("atlas authority ruling", ATLAS_AUTHORITY_RULING_LINK),
        ("atlas merge threshold", ATLAS_MERGE_THRESHOLD_LINK),
    ]:
        if link_target not in developer_links:
            errors.append(
                f"README developer / governance path is missing required {link_name} link `{link_target}`"
            )
        if link_target not in folder_links:
            errors.append(
                f"README folder guide is missing required {link_name} link `{link_target}`"
            )

    if ATLAS_AUTHORITY_RULING_LINK not in check_atlas_text:
        errors.append("check-atlas-v1.md no longer points to atlas-authority-boundary-ruling-v1.md")
    if ATLAS_MERGE_THRESHOLD_LINK not in check_atlas_text:
        errors.append("check-atlas-v1.md no longer points to atlas-merge-threshold-v1.md")

    if ATLAS_AUTHORITY_RULING_LINK not in public_layer_atlas_text:
        errors.append("public-layer-verification-atlas-v1.md no longer points to atlas-authority-boundary-ruling-v1.md")

    for token in REQUIRED_ATLAS_TOKENS:
        if token not in public_layer_atlas_text:
            errors.append(f"public-layer atlas is missing required current-state token `{token}`")

    for token in FORBIDDEN_PUBLIC_LAYER_ATLAS_TOKENS:
        if token in public_layer_atlas_text:
            errors.append(f"public-layer atlas still contains retired token `{token}`")

    for token in REQUIRED_RULING_TOKENS:
        if token not in authority_ruling_text:
            errors.append(f"atlas authority ruling is missing required token `{token}`")

    for token in REQUIRED_THRESHOLD_TOKENS:
        if token not in merge_threshold_text:
            errors.append(f"atlas merge threshold is missing required token `{token}`")

    if errors:
        raise PublicLayerAtlasError("\n".join(errors))

    return {
        "developer_governance_path_links": len(developer_links),
        "folder_guide_links": len(folder_links),
        "required_public_layer_atlas_tokens": len(REQUIRED_ATLAS_TOKENS),
        "required_authority_ruling_tokens": len(REQUIRED_RULING_TOKENS),
        "required_merge_threshold_tokens": len(REQUIRED_THRESHOLD_TOKENS),
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
    print(f"- required public-layer atlas tokens: {summary['required_public_layer_atlas_tokens']}")
    print(f"- required authority ruling tokens: {summary['required_authority_ruling_tokens']}")
    print(f"- required merge threshold tokens: {summary['required_merge_threshold_tokens']}")


if __name__ == "__main__":
    main()
