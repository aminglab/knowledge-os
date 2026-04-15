#!/usr/bin/env python3
"""Lightweight semantic checker for COCKPIT2-A interactive prototype."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT2-A" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"

REQUIRED_HTML_SNIPPETS = [
    'id="state-nav"',
    'id="object-nav"',
    'id="lens-nav"',
    'id="trigger-panel"',
    'id="sidecar-content"',
    'src="./app.js"',
    'href="./styles.css"',
]

REQUIRED_LENSES = ["focus", "pressure", "route", "boundary"]
REQUIRED_STATES = ["landing", "hpClaim", "hpVerdict", "ppDissent", "ppRoute"]
REQUIRED_TRIGGERS = [
    "scan missing evidence",
    "draft dissent response",
    "check upgrade conditions",
    "suggest canonical continuation",
    "prepare progress summary",
]
REQUIRED_APP_SNIPPETS = [
    "HOLD_NO_LIVE_RUNTIME_COCKPIT",
    "HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND",
    "Output class remains draft-only / suggestion-layer.",
    "Lens switched to",
    "Object anchor switched to",
]
REQUIRED_CSS_SNIPPETS = [
    ".lens-nav",
    ".lens-button.active",
    ".object-button.active",
    ".trigger-button",
    ".audit-card",
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
            errors.append(f"app.js missing bound state fixture: {state}")

    for lens in REQUIRED_LENSES:
        if f"{lens}: {{" not in js:
            errors.append(f"app.js missing lens fixture: {lens}")

    for trigger in REQUIRED_TRIGGERS:
        if trigger not in js:
            errors.append(f"app.js missing trigger fixture: {trigger}")

    for snippet in REQUIRED_APP_SNIPPETS:
        if snippet not in js:
            errors.append(f"app.js missing semantic snippet: {snippet}")

    object_anchor_match = re.search(r"objects:\s*\[", js)
    if not object_anchor_match:
        errors.append("app.js missing object anchor arrays")

    if "renderObjects()" not in js or "renderLenses()" not in js or "renderTriggers()" not in js:
        errors.append("app.js missing one of the bounded interactive render passes")

    if errors:
        print("COCKPIT2-A interactive prototype semantic check: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("COCKPIT2-A interactive prototype semantic check: PASS")
    print("- required files present")
    print("- bounded state fixtures present")
    print("- bounded lens fixtures present")
    print("- bounded trigger fixtures present")
    print("- object-browse and audit-log wiring present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
