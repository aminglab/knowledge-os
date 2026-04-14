#!/usr/bin/env python3
"""Validate that H. pylori public-layer governance surfaces remain aligned."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
SUITE_PATH = REPO_ROOT / "scripts" / "check_h_pylori_public_layer.py"
ATLAS_PATH = CASE_ROOT / "public-layer-verification-atlas-v1.md"
ACCEPTANCE_PATH = CASE_ROOT / "public-layer-acceptance-pass-v1.md"
README_PATH = CASE_ROOT / "README.md"

EXPECTED_CHECK_FILES = [
    "check_h_pylori_claim_page_layering.py",
    "check_h_pylori_claim_page_pressure_coverage.py",
    "check_h_pylori_source_page_layering.py",
    "check_h_pylori_source_page_role_anchors.py",
    "check_h_pylori_snapshot_section_layering.py",
    "check_h_pylori_snapshot_subsection_semantics.py",
    "check_h_pylori_snapshot_consistency.py",
]

EXPECTED_HARDENING_LIFTS = [
    "claim-page direct pressure coverage",
    "source-page role anchors",
    "snapshot subsection semantic anchors",
    "fuller snapshot consistency checking",
]

EXPECTED_HOLDS = [
    "HOLD_NO_FULL_PUBLIC_RELEASE",
    "HOLD_NO_PAGE_EMISSION_LAYER",
    "HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY",
    "HOLD_NO_REPOSITORY_WIDE_PUBLIC_LAYER_GENERALIZATION",
]

README_EXPECTED_DOCS = [
    "snapshot-consistency-v1.md",
    "public-layer-verification-atlas-v1.md",
    "public-layer-acceptance-pass-v1.md",
]


class PublicLayerAtlasGovernanceError(Exception):
    """Raised when public-layer governance surfaces drift out of sync."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate() -> dict[str, int]:
    suite_text = read_text(SUITE_PATH)
    atlas_text = read_text(ATLAS_PATH)
    acceptance_text = read_text(ACCEPTANCE_PATH)
    readme_text = read_text(README_PATH)
    errors: list[str] = []

    for check_file in EXPECTED_CHECK_FILES:
        if check_file not in suite_text:
            errors.append(f"suite: missing check file `{check_file}`")
        if check_file not in atlas_text:
            errors.append(f"atlas: missing check file `{check_file}`")

    for phrase in EXPECTED_HARDENING_LIFTS:
        if phrase not in acceptance_text:
            errors.append(f"acceptance: missing hardening lift `{phrase}`")
        if phrase not in readme_text:
            errors.append(f"README: missing hardening lift `{phrase}`")

    for hold in EXPECTED_HOLDS:
        if hold not in acceptance_text:
            errors.append(f"acceptance: missing retained hold `{hold}`")

    for doc_name in README_EXPECTED_DOCS:
        if doc_name not in readme_text:
            errors.append(f"README: missing governance-path document `{doc_name}`")

    if "atlas-governance self-check" not in atlas_text and "atlas-governance self-check" not in acceptance_text:
        errors.append("governance surfaces: missing explicit atlas-governance self-check wording")

    if errors:
        raise PublicLayerAtlasGovernanceError("\n".join(errors))

    return {
        "expected_checks": len(EXPECTED_CHECK_FILES),
        "expected_hardening_lifts": len(EXPECTED_HARDENING_LIFTS),
        "expected_holds": len(EXPECTED_HOLDS),
    }


def main() -> None:
    try:
        summary = validate()
    except PublicLayerAtlasGovernanceError as exc:
        print("H. pylori public-layer atlas governance failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori public-layer atlas governance passed.")
    print()
    print(f"- expected checks aligned: {summary['expected_checks']}")
    print(f"- expected hardening lifts aligned: {summary['expected_hardening_lifts']}")
    print(f"- expected retained holds aligned: {summary['expected_holds']}")


if __name__ == "__main__":
    main()
