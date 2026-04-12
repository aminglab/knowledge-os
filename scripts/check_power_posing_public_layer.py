#!/usr/bin/env python3
"""Run the current public-layer verification subset for the power-posing pilot."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable
PAGE_GENERATOR = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing" / "page" / "generate_page_data.py"

PUBLIC_LAYER_CHECKS = [
    ("verdict_grammar", [PYTHON, "scripts/check_power_posing_verdict_grammar.py"]),
    ("status_legend", [PYTHON, "scripts/check_power_posing_status_legend.py"]),
    ("claim_page_layering", [PYTHON, "scripts/check_power_posing_claim_page_layering.py"]),
    ("claim_page_pressure_coverage", [PYTHON, "scripts/check_power_posing_claim_page_pressure_coverage.py"]),
    ("source_page_layering", [PYTHON, "scripts/check_power_posing_source_page_layering.py"]),
    ("source_page_role_anchors", [PYTHON, "scripts/check_power_posing_source_page_role_anchors.py"]),
    ("snapshot_section_layering", [PYTHON, "scripts/check_power_posing_snapshot_section_layering.py"]),
    ("snapshot_subsection_semantics", [PYTHON, "scripts/check_power_posing_snapshot_subsection_semantics.py"]),
    ("snapshot_consistency", [PYTHON, "scripts/check_power_posing_snapshot_consistency.py"]),
    ("reference_metadata", [PYTHON, "scripts/check_power_posing_reference_metadata.py"]),
    ("public_surface", [PYTHON, "scripts/check_power_posing_public_surface.py"]),
    ("public_layer_atlas", [PYTHON, "scripts/check_power_posing_public_layer_atlas.py"]),
    ("page_emission_validation", [PYTHON, str(PAGE_GENERATOR), "--check"]),
]


class PublicLayerCheckError(Exception):
    """Raised when one or more public-layer checks fail."""


def run_check(name: str, cmd: list[str]) -> tuple[bool, str]:
    result = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode == 0, output.strip()


def main() -> None:
    failures: list[tuple[str, str]] = []
    passes = 0

    print("Power-posing public-layer orchestrator")
    print()

    for name, cmd in PUBLIC_LAYER_CHECKS:
        ok, output = run_check(name, cmd)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}")
        if output:
            for line in output.splitlines():
                print(f"  {line}")
        print()
        if ok:
            passes += 1
        else:
            failures.append((name, output))

    print("Summary")
    print(f"- checks run: {len(PUBLIC_LAYER_CHECKS)}")
    print(f"- passed: {passes}")
    print(f"- failed: {len(failures)}")

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
