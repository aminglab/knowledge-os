#!/usr/bin/env python3
"""Run the current public-layer verification subset for the h-pylori-ulcer pilot."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable

PUBLIC_LAYER_CHECKS = [
    {
        "name": "claim_page_layering",
        "label": "Claim page layering",
        "layer": "claim page public layer",
        "cmd": [PYTHON, "scripts/check_h_pylori_claim_page_layering.py"],
    },
    {
        "name": "claim_page_pressure_coverage",
        "label": "Claim page pressure coverage",
        "layer": "claim page public layer",
        "cmd": [PYTHON, "scripts/check_h_pylori_claim_page_pressure_coverage.py"],
    },
    {
        "name": "source_page_layering",
        "label": "Source page layering",
        "layer": "source page public layer",
        "cmd": [PYTHON, "scripts/check_h_pylori_source_page_layering.py"],
    },
    {
        "name": "snapshot_section_layering",
        "label": "Snapshot section layering",
        "layer": "snapshot release-view layer",
        "cmd": [PYTHON, "scripts/check_h_pylori_snapshot_section_layering.py"],
    },
]

LAYER_ORDER = [
    "claim page public layer",
    "source page public layer",
    "snapshot release-view layer",
]


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


def main() -> None:
    failures: list[dict[str, str]] = []
    results: list[dict[str, str]] = []
    passes = 0

    print("H. pylori public-layer suite")
    print()

    for check in PUBLIC_LAYER_CHECKS:
        ok, output = run_check(str(check["name"]), list(check["cmd"]))
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {check['name']}")
        if output:
            for line in output.splitlines():
                print(f"  {line}")
        print()

        results.append(
            {
                "name": str(check["name"]),
                "status": status,
                "layer": str(check["layer"]),
            }
        )

        if ok:
            passes += 1
        else:
            failures.append(
                {
                    "name": str(check["name"]),
                    "label": str(check["label"]),
                    "layer": str(check["layer"]),
                }
            )

    layer_summary = build_layer_summary(results)
    overall_status = "FAIL" if failures else "PASS"

    print("Summary")
    print(f"- overall public-layer verdict: {overall_status}")
    print(f"- checks run: {len(PUBLIC_LAYER_CHECKS)}")
    print(f"- passed: {passes}")
    print(f"- failed: {len(failures)}")
    print("- layer verdicts:")
    for entry in layer_summary:
        print(f"  - {entry['layer']}: {entry['status']} ({entry['passed']}/{entry['total']})")

    if failures:
        print()
        print("Failure focus")
        print(f"- failing layers ({len(failures)}): {', '.join(f['layer'] for f in failures)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
