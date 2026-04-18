#!/usr/bin/env python3
"""Lightweight semantic checker for the COCKPIT3-A governance sidecar lift."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / "cockpit" / "COCKPIT3-A" / "prototype"
INDEX = PROTO / "index.html"
STYLES = PROTO / "styles.css"
APP = PROTO / "app.js"
README = PROTO / "README.md"
SIDECAR = ROOT / "cockpit" / "COCKPIT3-A" / "cockpit3-a-governance-sidecar-v1.md"

REQ_HTML = ['id="app"', 'src="./app.js"', 'href="./styles.css"']
REQ_APP = [
    'execution_boundary_class: draft_only',
    'action_posture: surface_only',
    'non-executable at current stage',
    'operator_review_required',
    'execution_forbidden',
    'data-governance-sidecar="true"',
    'data-governed-result="true"',
    'No execute, commit, apply, resolve, or publish authority is opened here.',
    'HOLD_NO_LIVE_RUNTIME_COCKPIT',
    'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND',
]
REQ_README = [
    'surface execution-boundary class and action posture next to result surfaces',
    'keep all current result surfaces draft_only and non-executable',
]
REQ_SIDECAR = [
    'execution_boundary_class',
    'action_posture',
    'draft_only',
    'surface_only',
    'future classes not opened yet',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding='utf-8')


def main() -> int:
    errors: list[str] = []
    html = read(INDEX, errors)
    css = read(STYLES, errors)
    js = read(APP, errors)
    readme = read(README, errors)
    sidecar = read(SIDECAR, errors)

    for s in REQ_HTML:
        if s not in html:
            errors.append(f"index.html missing snippet: {s}")
    if 'injected by app.js' not in css:
        errors.append('styles.css missing injected-by-app marker')
    for s in REQ_APP:
        if s not in js:
            errors.append(f"app.js missing snippet: {s}")
    for s in REQ_README:
        if s not in readme:
            errors.append(f"README missing snippet: {s}")
    for s in REQ_SIDECAR:
        if s not in sidecar:
            errors.append(f"sidecar doc missing snippet: {s}")

    if errors:
        print('COCKPIT3-A governance sidecar semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT3-A governance sidecar semantic check: PASS')
    print('- governed result surface present')
    print('- governance sidecar present')
    print('- draft_only / surface_only posture explicit')
    print('- future classes remain unopened')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
