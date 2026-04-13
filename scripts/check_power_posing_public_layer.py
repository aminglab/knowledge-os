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
    {
        "name": "verdict_grammar",
        "cmd": [PYTHON, "scripts/check_power_posing_verdict_grammar.py"],
    },
    {
        "name": "status_legend",
        "cmd": [PYTHON, "scripts/check_power_posing_status_legend.py"],
    },
    {
        "name": "claim_page_layering",
        "cmd": [PYTHON, "scripts/check_power_posing_claim_page_layering.py"],
    },
    {
        "name": "claim_page_pressure_coverage",
        "cmd": [PYTHON, "scripts/check_power_posing_claim_page_pressure_coverage.py"],
    },
    {
        "name": "source_page_layering",
        "cmd": [PYTHON, "scripts/check_power_posing_source_page_layering.py"],
    },
    {
        "name": "source_page_role_anchors",
        "cmd": [PYTHON, "scripts/check_power_posing_source_page_role_anchors.py"],
    },
    {
        "name": "snapshot_section_layering",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_section_layering.py"],
    },
    {
        "name": "snapshot_subsection_semantics",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_subsection_semantics.py"],
    },
    {
        "name": "snapshot_consistency",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_consistency.py"],
    },
    {
        "name": "reference_metadata",
        "cmd": [PYTHON, "scripts/check_power_posing_reference_metadata.py"],
    },
    {
        "name": "public_surface",
        "cmd": [PYTHON, "scripts/check_power_posing_public_surface.py"],
    },
    {
        "name": "public_layer_atlas",
        "cmd": [PYTHON, "scripts/check_power_posing_public_layer_atlas.py"],
        "hint": "atlas governance (boundary + threshold views)",
        "summary_label": "atlas governance",
    },
    {
        "name": "page_emission_validation",
        "cmd": [PYTHON, str(PAGE_GENERATOR), "--check"],
    },
]

ATLAS_GOVERNANCE_HEADERS = {"Boundary view", "Threshold view"}


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


def format_check_title(check: dict[str, object], status: str) -> str:
    title = f"[{status}] {check['name']}"
    hint = check.get("hint")
    if hint:
        title += f" — {hint}"
    return title


def emit_check_output(name: str, output: str) -> None:
    if not output:
        return

    for line in output.splitlines():
        stripped = line.strip()
        if name == "public_layer_atlas" and stripped in ATLAS_GOVERNANCE_HEADERS:
            print(f"  > {stripped}")
            continue
        print(f"  {line}")


def emit_failure_focus(failures: list[dict[str, str]]) -> None:
    if not failures:
        return

    governance_failures = [f for f in failures if f.get("summary_label") == "atlas governance"]
    other_failures = [f for f in failures if f.get("summary_label") != "atlas governance"]

    print()
    print("Failure focus")

    if governance_failures:
        failure = governance_failures[0]
        line = "- atlas governance: FAIL"
        hint = failure.get("hint", "")
        if hint:
            line += f" ({hint})"
        print(line)
        print("  see above: boundary / threshold details")

    if other_failures:
        print("- other failed checks:")
        for failure in other_failures:
            print(f"  - {failure['name']}")


def main() -> None:
    failures: list[dict[str, str]] = []
    passes = 0
    governance_summary: tuple[str, str] | None = None

    print("Power-posing public-layer orchestrator")
    print()

    for check in PUBLIC_LAYER_CHECKS:
        name = str(check["name"])
        cmd = list(check["cmd"])
        ok, output = run_check(name, cmd)
        status = "PASS" if ok else "FAIL"
        print(format_check_title(check, status))
        emit_check_output(name, output)
        print()
        hint = str(check.get("hint", ""))
        summary_label = check.get("summary_label")

        if ok:
            passes += 1
        else:
            failures.append(
                {
                    "name": name,
                    "output": output,
                    "hint": hint,
                    "summary_label": str(summary_label or ""),
                }
            )

        if isinstance(summary_label, str) and summary_label:
            governance_summary = (status, hint)

    print("Summary")
    print(f"- checks run: {len(PUBLIC_LAYER_CHECKS)}")
    print(f"- passed: {passes}")
    print(f"- failed: {len(failures)}")
    if governance_summary is not None:
        governance_status, governance_hint = governance_summary
        summary_line = f"- atlas governance: {governance_status}"
        if governance_hint:
            summary_line += f" ({governance_hint})"
        print(summary_line)

    emit_failure_focus(failures)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
