#!/usr/bin/env python3
"""Validate the H. pylori public-layer orchestration boundary remains exposed and synchronized."""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
README_PATH = CASE_ROOT / "README.md"
PUBLIC_LAYER_ATLAS_PATH = CASE_ROOT / "public-layer-verification-atlas-v1.md"
ATLAS_GOVERNANCE_PATH = CASE_ROOT / "public-layer-atlas-governance-v1.md"
BOUNDARY_PATH = CASE_ROOT / "public-layer-orchestration-boundary-v1.md"
THRESHOLD_PATH = CASE_ROOT / "public-layer-orchestration-threshold-v1.md"

PUBLIC_LAYER_ATLAS_LINK = "./public-layer-verification-atlas-v1.md"
ATLAS_GOVERNANCE_LINK = "./public-layer-atlas-governance-v1.md"
BOUNDARY_LINK = "./public-layer-orchestration-boundary-v1.md"
THRESHOLD_LINK = "./public-layer-orchestration-threshold-v1.md"

REQUIRED_BOUNDARY_TOKENS = [
    "scripts/check_h_pylori_public_layer.py",
    "check-h-pylori-public-layer.yml",
    "public-layer-verification-atlas-v1.md",
    "public-layer-atlas-governance-v1.md",
    "Do not open a larger orchestration expansion yet",
]
REQUIRED_THRESHOLD_TOKENS = [
    "HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY",
    "check_h_pylori_public_layer.py",
    "public-layer-orchestration-boundary-v1.md",
    "page-emission layer",
]


class PublicLayerBoundaryError(Exception):
    """Raised when public-layer orchestration boundary surfaces drift."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.casefold()
    text = re.sub(r"[`*_]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def contains_token(text: str, token: str) -> bool:
    return normalize_text(token) in normalize_text(text)


def find_markdown_links(markdown: str) -> set[str]:
    return {target for _label, target in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", markdown)}


def validate() -> dict[str, int]:
    readme_text = read_text(README_PATH)
    atlas_text = read_text(PUBLIC_LAYER_ATLAS_PATH)
    boundary_text = read_text(BOUNDARY_PATH)
    threshold_text = read_text(THRESHOLD_PATH)
    developer_links = find_markdown_links(extract_section(readme_text, "Developer / governance path"))
    folder_links = find_markdown_links(extract_section(readme_text, "Folder guide"))
    errors: list[str] = []

    for link_name, link_target in [
        ("public-layer atlas", PUBLIC_LAYER_ATLAS_LINK),
        ("atlas governance", ATLAS_GOVERNANCE_LINK),
        ("orchestration boundary", BOUNDARY_LINK),
        ("orchestration threshold", THRESHOLD_LINK),
    ]:
        if link_target not in developer_links:
            errors.append(f"README developer / governance path is missing required {link_name} link `{link_target}`")
        if link_target not in folder_links:
            errors.append(f"README folder guide is missing required {link_name} link `{link_target}`")

    if BOUNDARY_LINK not in atlas_text:
        errors.append("public-layer-verification-atlas-v1.md no longer points to public-layer-orchestration-boundary-v1.md")
    if THRESHOLD_LINK not in atlas_text:
        errors.append("public-layer-verification-atlas-v1.md no longer points to public-layer-orchestration-threshold-v1.md")
    if THRESHOLD_LINK not in boundary_text:
        errors.append("public-layer-orchestration-boundary-v1.md no longer points to public-layer-orchestration-threshold-v1.md")

    for token in REQUIRED_BOUNDARY_TOKENS:
        if not contains_token(boundary_text, token):
            errors.append(f"public-layer orchestration boundary is missing required token `{token}`")

    for token in REQUIRED_THRESHOLD_TOKENS:
        if not contains_token(threshold_text, token):
            errors.append(f"public-layer orchestration threshold is missing required token `{token}`")

    if errors:
        raise PublicLayerBoundaryError("\n".join(errors))

    return {
        "developer_governance_path_links": len(developer_links),
        "folder_guide_links": len(folder_links),
        "required_boundary_tokens": len(REQUIRED_BOUNDARY_TOKENS),
        "required_threshold_tokens": len(REQUIRED_THRESHOLD_TOKENS),
    }


def main() -> None:
    try:
        summary = validate()
    except PublicLayerBoundaryError as exc:
        print("H. pylori public-layer orchestration boundary failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori public-layer orchestration boundary passed.")
    print()
    print(f"- developer / governance path links: {summary['developer_governance_path_links']}")
    print(f"- folder guide links: {summary['folder_guide_links']}")
    print(f"- required boundary tokens: {summary['required_boundary_tokens']}")
    print(f"- required threshold tokens: {summary['required_threshold_tokens']}")


if __name__ == "__main__":
    main()
