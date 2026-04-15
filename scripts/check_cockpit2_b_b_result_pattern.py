#!/usr/bin/env python3
"""Lightweight semantic checker for the COCKPIT2-B-B result-pattern expansion lift."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT2-B-B" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"
README = PROTO / "README.md"
SCOPE = ROOT / "cockpit" / "COCKPIT2-B-B" / "cockpit2-b-b-expansion-scope-v1.md"

REQUIRED_HTML_SNIPPETS = [
    'id="app"',
    'src="./app.js"',
    'href="./styles.css"',
]
REQUIRED_APP_SNIPPETS = [
    'scan missing evidence',
    'draft dissent response',
    'check upgrade conditions',
    'prepare progress summary',
    'scan_result',
    'draft_response',
    'condition_check',
    'summary_draft',
    'suggest canonical continuation',
    'outside current structured-card coverage',
    'Draft-only',
    'Output class: ${resultCard.outputClass}',
    'Anchor: ${resultCard.anchor}',
    'HOLD_NO_LIVE_RUNTIME_COCKPIT',
    'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND',
]
REQUIRED_README_SNIPPETS = [
    'widen structured draft result cards to four bounded triggers',
    'keep at least one trigger outside the current card-coverage boundary',
]
REQUIRED_SCOPE_SNIPPETS = [
    '`scan missing evidence`',
    '`draft dissent response`',
    '`check upgrade conditions`',
    '`prepare progress summary`',
    '`suggest canonical continuation`',
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
    readme = require_file(README, errors)
    scope = require_file(SCOPE, errors)

    for snippet in REQUIRED_HTML_SNIPPETS:
        if snippet not in html:
            errors.append(f"index.html missing snippet: {snippet}")

    if 'injected by app.js' not in css:
        errors.append('styles.css missing injected-by-app marker')

    for snippet in REQUIRED_APP_SNIPPETS:
        if snippet not in js:
            errors.append(f"app.js missing snippet: {snippet}")

    for snippet in REQUIRED_README_SNIPPETS:
        if snippet not in readme:
            errors.append(f"prototype README missing snippet: {snippet}")

    for snippet in REQUIRED_SCOPE_SNIPPETS:
        if snippet not in scope:
            errors.append(f"scope doc missing snippet: {snippet}")

    if errors:
        print('COCKPIT2-B-B result-pattern semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT2-B-B result-pattern semantic check: PASS')
    print('- prototype shell present')
    print('- four structured result classes present')
    print('- one trigger intentionally left outside coverage')
    print('- draft-only honesty preserved')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
