#!/usr/bin/env python3
"""Lightweight semantic checker for COCKPIT1-B static prototype."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT1-B" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"

REQUIRED_HTML_SNIPPETS = [
    'id="state-nav"',
    'id="screen-title"',
    'id="screen-subtitle"',
    'id="main-content"',
    'id="right-content"',
    'id="sidecar-content"',
    'src="./app.js"',
    'href="./styles.css"',
]

REQUIRED_STATES = ["landing", "hpClaim", "hpVerdict", "ppDissent", "ppRoute"]
REQUIRED_LABELS = [
    "Landing",
    "H. pylori / Claim focus",
    "H. pylori / Verdict boundary",
    "Power posing / Dissent pressure",
    "Power posing / Route map",
]
REQUIRED_CASE_STRINGS = ["power-posing", "h-pylori-ulcer"]
REQUIRED_APP_SNIPPETS = [
    "Two bound cases visible",
    "HOLD_NO_FULL_PUBLIC_RELEASE",
    "replication failure and null effect pressure",
    "snapshot-v2 public homepage",
    "Sidecar discipline",
]
REQUIRED_CSS_SNIPPETS = [
    ".cockpit-grid",
    ".left-rail",
    ".main-panel",
    ".right-rail",
    ".sidecar",
    ".state-button.active",
]


def require_file(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    html = require_file(INDEX, errors)
    css = require_file(STYLES, errors)
    js = require_file(APP, errors)

    for snippet in REQUIRED_HTML_SNIPPETS:
        if snippet not in html:
            errors.append(f"index.html missing snippet: {snippet}")

    for snippet in REQUIRED_CSS_SNIPPETS:
        if snippet not in css:
            errors.append(f"styles.css missing snippet: {snippet}")

    for state in REQUIRED_STATES:
        if f"{state}: {{" not in js:
            errors.append(f"app.js missing state fixture: {state}")

    order_match = re.search(r"stateOrder\s*=\s*\[(.*?)\]", js, re.DOTALL)
    if not order_match:
        errors.append("app.js missing stateOrder declaration")
    else:
        for state in REQUIRED_STATES:
            if f"'{state}'" not in order_match.group(1):
                errors.append(f"stateOrder missing state: {state}")

    for label in REQUIRED_LABELS:
        if label not in js:
            errors.append(f"app.js missing label: {label}")

    for case_text in REQUIRED_CASE_STRINGS:
        if case_text not in js and case_text not in html:
            errors.append(f"prototype missing bound case string: {case_text}")

    for snippet in REQUIRED_APP_SNIPPETS:
        if snippet not in js:
            errors.append(f"app.js missing semantic snippet: {snippet}")

    if errors:
        print("COCKPIT1-B static prototype semantic check: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("COCKPIT1-B static prototype semantic check: PASS")
    print("- required files present")
    print("- required slots and ids present")
    print("- five required state fixtures present")
    print("- two bound case strings present")
    print("- key semantic snippets present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
