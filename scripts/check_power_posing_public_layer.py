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
        "name": "protocol_record_consistency",
        "label": "Protocol consistency",
        "layer": "protocol consistency floor",
        "cmd": [PYTHON, "scripts/check_protocol_record_consistency.py"],
    },
    {
        "name": "object_envelope",
        "label": "Object envelope",
        "layer": "object-envelope floor",
        "cmd": [PYTHON, "scripts/check_power_posing_object_envelope.py"],
    },
    {
        "name": "verdict_grammar",
        "label": "Verdict grammar",
        "layer": "judgment wording bridge",
        "cmd": [PYTHON, "scripts/check_power_posing_verdict_grammar.py"],
    },
    {
        "name": "status_legend",
        "label": "Status legend",
        "layer": "judgment wording bridge",
        "cmd": [PYTHON, "scripts/check_power_posing_status_legend.py"],
    },
    {
        "name": "claim_page_layering",
        "label": "Claim page layering",
        "layer": "claim page public layer",
        "cmd": [PYTHON, "scripts/check_power_posing_claim_page_layering.py"],
    },
    {
        "name": "claim_page_pressure_coverage",
        "label": "Claim pressure coverage",
        "layer": "claim page public layer",
        "cmd": [PYTHON, "scripts/check_power_posing_claim_page_pressure_coverage.py"],
    },
    {
        "name": "source_page_layering",
        "label": "Source page layering",
        "layer": "source page public layer",
        "cmd": [PYTHON, "scripts/check_power_posing_source_page_layering.py"],
    },
    {
        "name": "source_page_role_anchors",
        "label": "Source role anchors",
        "layer": "source page public layer",
        "cmd": [PYTHON, "scripts/check_power_posing_source_page_role_anchors.py"],
    },
    {
        "name": "reference_metadata",
        "label": "Reference metadata",
        "layer": "source page public layer",
        "cmd": [PYTHON, "scripts/check_power_posing_reference_metadata.py"],
    },
    {
        "name": "snapshot_section_layering",
        "label": "Snapshot section layering",
        "layer": "snapshot release-view layer",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_section_layering.py"],
    },
    {
        "name": "snapshot_subsection_semantics",
        "label": "Snapshot semantics",
        "layer": "snapshot release-view layer",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_subsection_semantics.py"],
    },
    {
        "name": "snapshot_consistency",
        "label": "Snapshot consistency",
        "layer": "snapshot release-view layer",
        "cmd": [PYTHON, "scripts/check_power_posing_snapshot_consistency.py"],
    },
    {
        "name": "public_surface",
        "label": "Public surface",
        "layer": "page emission layer",
        "cmd": [PYTHON, "scripts/check_power_posing_public_surface.py"],
    },
    {
        "name": "page_emission_validation",
        "label": "Page emission",
        "layer": "page emission layer",
        "cmd": [PYTHON, str(PAGE_GENERATOR), "--check"],
    },
    {
        "name": "public_layer_atlas",
        "label": "Public-layer orchestration boundary",
        "layer": "public-layer orchestration boundary",
        "cmd": [PYTHON, "scripts/check_power_posing_public_layer_atlas.py"],
        "hint": "atlas governance (boundary + threshold views)",
        "summary_label": "public-layer orchestration boundary",
    },
]

LAYER_ORDER = [
    "protocol consistency floor",
    "object-envelope floor",
    "judgment wording bridge",
    "claim page public layer",
    "source page public layer",
    "snapshot release-view layer",
    "page emission layer",
    "public-layer orchestration boundary",
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


def build_layer_summary(results: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[str, dict[str, int]] = {
        layer: {"total": 0, "failed": 0} for layer in LAYER_ORDER
    }

    for result in results:
        layer = result["layer"]
        grouped.setdefault(layer, {"total": 0, "failed": 0})
        grouped[layer]["total"] += 1
        if result["status"] == "FAIL":
            grouped[layer]["failed"] += 1

    summary: list[dict[str, object]] = []
    for layer in LAYER_ORDER:
        if grouped[layer]["total"] == 0:
            continue
        failed = grouped[layer]["failed"]
        total = grouped[layer]["total"]
        summary.append(
            {
                "layer": layer,
                "status": "FAIL" if failed else "PASS",
                "failed": failed,
                "passed": total - failed,
                "total": total,
            }
        )
    return summary


def emit_layer_summary(layer_summary: list[dict[str, object]]) -> None:
    if not layer_summary:
        return

    print("- layer verdicts:")
    for entry in layer_summary:
        layer = str(entry["layer"])
        status = str(entry["status"])
        passed = int(entry["passed"])
        total = int(entry["total"])
        print(f"  - {layer}: {status} ({passed}/{total})")


def emit_failure_focus(
    failures: list[dict[str, str]],
    layer_summary: list[dict[str, object]],
) -> None:
    if not failures:
        return

    governance_failures = [
        f for f in failures if f.get("summary_label") == "public-layer orchestration boundary"
    ]
    other_failures = [
        f for f in failures if f.get("summary_label") != "public-layer orchestration boundary"
    ]
    failing_layers = [
        str(entry["layer"])
        for entry in layer_summary
        if str(entry["status"]) == "FAIL"
        and str(entry["layer"]) != "public-layer orchestration boundary"
    ]

    print()
    print("Failure focus")

    if governance_failures:
        failure = governance_failures[0]
        line = "- public-layer orchestration boundary: FAIL"
        hint = failure.get("hint", "")
        if hint:
            line += f" ({hint})"
        print(line)
        print("  see above: boundary / threshold details")

    if failing_layers:
        print(f"- failing layers ({len(failing_layers)}): {', '.join(failing_layers)}")

    if other_failures:
        other_labels = ", ".join(failure["label"] for failure in other_failures)
        print(f"- other failed checks ({len(other_failures)}): {other_labels}")


def main() -> None:
    failures: list[dict[str, str]] = []
    results: list[dict[str, str]] = []
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
        label = str(check.get("label", name))
        layer = str(check.get("layer", "uncategorized"))

        results.append({"name": name, "status": status, "layer": layer})

        if ok:
            passes += 1
        else:
            failures.append(
                {
                    "name": name,
                    "label": label,
                    "output": output,
                    "hint": hint,
                    "summary_label": str(summary_label or ""),
                    "layer": layer,
                }
            )

        if isinstance(summary_label, str) and summary_label:
            governance_summary = (status, hint)

    layer_summary = build_layer_summary(results)
    overall_status = "FAIL" if failures else "PASS"

    print("Summary")
    print(f"- overall public-layer verdict: {overall_status}")
    print(f"- checks run: {len(PUBLIC_LAYER_CHECKS)}")
    print(f"- passed: {passes}")
    print(f"- failed: {len(failures)}")
    if governance_summary is not None:
        governance_status, governance_hint = governance_summary
        summary_line = f"- public-layer orchestration boundary: {governance_status}"
        if governance_hint:
            summary_line += f" ({governance_hint})"
        print(summary_line)
    emit_layer_summary(layer_summary)

    emit_failure_focus(failures, layer_summary)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
