#!/usr/bin/env python3
"""Lightweight semantic checker for the COCKPIT2-B-A result-card lift."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT2-B-A" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"
README = PROTO / "README.md"

REQUIRED_HTML_SNIPPETS = [
    'id="app"',
    'src="./app.js"',
    'href="./styles.css"',
]

REQUIRED_APP_SNIPPETS = [
    'Draft Result Surface',
    'check upgrade conditions',
    'prepare progress summary',
    'condition_check',
    'summary_draft',
    'Output class: ${resultCard.outputClass}',
    'Anchor: ${resultCard.anchor}',
    'Draft-only',
    'data-result-card="true"',
    'No structured draft result yet.',
    'Output class remains draft-only / suggestion-layer.',
    'HOLD_NO_LIVE_RUNTIME_COCKPIT',
    'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND',
]

REQUIRED_README_SNIPPETS = [
    'first structured draft result-card lift',
    'upgrade at least one trigger to a structured draft result card',
    'anti-runtime and anti-mutation holds',
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

    if errors:
        print('COCKPIT2-B-A result-surface semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT2-B-A result-surface semantic check: PASS')
    print('- prototype shell present')
    print('- first structured result-card lift present')
    print('- draft-only output classes present')
    print('- anchor and honesty markers present')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
