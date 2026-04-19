#!/usr/bin/env python3
"""Lightweight semantic checker for the COCKPIT3-B-A review-boundary prototype lift."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO = ROOT / 'cockpit' / 'COCKPIT3-B-A' / 'prototype'
INDEX = PROTO / 'index.html'
APP = PROTO / 'app.js'
README = PROTO / 'README.md'
ENTRY = ROOT / 'cockpit' / 'COCKPIT3-B-A' / 'cockpit3-b-a-entry-decision-v1.md'
OBJECT = ROOT / 'cockpit' / 'COCKPIT3-B-A' / 'cockpit3-b-a-review-boundary-prototype-v1.md'
ACCEPT = ROOT / 'cockpit' / 'COCKPIT3-B-A' / 'cockpit3-b-a-acceptance-pass-v1.md'
SMOKE = ROOT / 'cockpit' / 'COCKPIT3-B-A' / 'cockpit3-b-a-smoke-closeout-v1.md'

REQ_INDEX = ['id="app"', 'src="./app.js"']
REQ_APP = [
    'data-governed-result="true"',
    'data-review-boundary-sidecar="true"',
    'review_trigger',
    'review_scope',
    'review_act',
    'retained_holds',
    'review_trigger_family',
    'review_scope_family',
    'export_surface_pressure',
    'export_only',
    'routing_handoff_pressure',
    'routing_only',
    'execution_boundary_class: draft_only',
    'action_posture: surface_only',
    'non-executable at current stage',
    'operator review is still not execution authority.',
    'No current governed result surface is yet lawfully classified as operator_review_required.',
    'HOLD_NO_LIVE_RUNTIME_COCKPIT',
    'HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE',
    'HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND',
]
REQ_README = [
    'show review trigger, review scope, and review act next to the result surface',
    'emit `review_trigger_family` and `review_scope_family` as checker-visible labels',
    'keep all current result surfaces draft_only and non-executable',
    'operator review is still not execution authority',
    'no current governed result surface is yet lawfully classified as operator_review_required',
]
REQ_OBJECT = [
    'review_trigger',
    'review_scope',
    'review_act',
    'retained_holds',
    'operator review is still not execution authority.',
    'No current governed result surface is yet lawfully classified as `operator_review_required`.',
]
REQ_ACCEPT = [
    'PASS_REVIEW_BOUNDARY_PROTOTYPE_LIFT',
    'PASS_REVIEW_TRIGGER_SCOPE_ACT_VISIBLE',
    'HOLD_REVIEW_BOUNDARY_PROTOTYPE_NOT_YET_COHERENT',
]
REQ_SMOKE = [
    'review_trigger',
    'review_scope',
    'review_act',
    'operator review is still not execution authority',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def main() -> int:
    errors: list[str] = []
    index = read(INDEX, errors)
    app = read(APP, errors)
    readme = read(README, errors)
    entry = read(ENTRY, errors)
    obj = read(OBJECT, errors)
    accept = read(ACCEPT, errors)
    smoke = read(SMOKE, errors)

    for s in REQ_INDEX:
        if s not in index:
            errors.append(f'index.html missing snippet: {s}')
    for s in REQ_APP:
        if s not in app:
            errors.append(f'app.js missing snippet: {s}')
    for s in REQ_README:
        if s not in readme:
            errors.append(f'README missing snippet: {s}')
    if 'ENTER_COCKPIT3_B_A_REVIEW_BOUNDARY_PROTOTYPE_LIFT' not in entry:
        errors.append('entry decision missing prototype-lift verdict')
    for s in REQ_OBJECT:
        if s not in obj:
            errors.append(f'prototype object doc missing snippet: {s}')
    for s in REQ_ACCEPT:
        if s not in accept:
            errors.append(f'acceptance pass missing snippet: {s}')
    for s in REQ_SMOKE:
        if s not in smoke:
            errors.append(f'smoke closeout missing snippet: {s}')

    if errors:
        print('COCKPIT3-B-A review boundary semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT3-B-A review boundary semantic check: PASS')
    print('- governed result surface present')
    print('- review boundary sidecar present')
    print('- review_trigger / review_scope / review_act / retained_holds explicit')
    print('- review family labels emitted and checker-visible')
    print('- draft_only / surface_only posture preserved')
    print('- operator review remains non-executional')
    print('- no current surface is overclaimed as operator_review_required')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
