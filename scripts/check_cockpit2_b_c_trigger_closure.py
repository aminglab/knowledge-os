#!/usr/bin/env python3
"""Lightweight semantic checker for the COCKPIT2-B-C final trigger-closure lift."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT2-B-C" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"
README = PROTO / "README.md"
SCOPE = ROOT / "cockpit" / "COCKPIT2-B-C" / "cockpit2-b-c-closure-scope-v1.md"

REQUIRED_HTML_SNIPPETS = [
    'id="app"',
    'src="./app.js"',
    'href="./styles.css"',
]
REQUIRED_APP_SNIPPETS = [
    'scan missing evidence',
    'draft dissent response',
    'check upgrade conditions',
    'suggest canonical continuation',
    'prepare progress summary',
    'scan_result',
    'draft_response',
    'condition_check',
    'continuation_suggestion',
    'summary_draft',
    'Full current trigger-set structured coverage',
    'The current trigger set is now fully covered.',
    'Draft-only',
    'Output class: ${resultCard.outputClass}',
    'Anchor: ${resultCard.anchor}',
    'HOLD_NO_LIVE_RUNTIME_COCKPIT',
    'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND',
]
REQUIRED_README_SNIPPETS = [
    'bring suggest canonical continuation into the structured draft result-card pattern',
    'complete structured result-card coverage for the current trigger set',
]
REQUIRED_SCOPE_SNIPPETS = [
    '`suggest canonical continuation`',
    '`scan missing evidence`',
    '`draft dissent response`',
    '`check upgrade conditions`',
    '`prepare progress summary`',
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
        print('COCKPIT2-B-C trigger-closure semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT2-B-C trigger-closure semantic check: PASS')
    print('- prototype shell present')
    print('- full current trigger-set coverage present')
    print('- continuation_suggestion result card present')
    print('- draft-only honesty preserved')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
