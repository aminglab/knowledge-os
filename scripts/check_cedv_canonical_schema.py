#!/usr/bin/env python3
"""Checker for the first CEDV canonical object schema floor."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / 'protocol' / 'cedv' / 'canonical-object-schema-v1.md'
EXAMPLES = ROOT / 'protocol' / 'cedv' / 'examples'

REQ_SCHEMA = [
    'Claim',
    'Evidence',
    'Dissent',
    'Verdict',
    'object_type: claim',
    'object_type: evidence',
    'object_type: dissent',
    'object_type: verdict',
    'A `public_candidate_object` is not a fifth CEDV family.',
    'cockpit objects and public-candidate objects are the core object families',
]
REQ_EXAMPLE_FILES = [
    'claim-C-0001.yaml',
    'evidence-E-0001.yaml',
    'dissent-D-0001.yaml',
    'verdict-V-0001.yaml',
]
REQ_COMMON = [
    'id:',
    'object_type:',
    'title:',
    'lifecycle_state:',
    'visibility:',
    'links:',
]
REQ_BY_TYPE = {
    'claim-C-0001.yaml': ['object_type: claim', 'epistemic_status:', 'source_refs:'],
    'evidence-E-0001.yaml': ['object_type: evidence', 'source_refs:', 'type: supports'],
    'dissent-D-0001.yaml': ['object_type: dissent', 'dissent_kind:', 'severity:', 'type: challenges'],
    'verdict-V-0001.yaml': ['object_type: verdict', 'verdict_level:', 'basis_refs:', 'type: pinned_in_snapshot'],
}


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def main() -> int:
    errors: list[str] = []
    schema = read(SCHEMA, errors)
    for snippet in REQ_SCHEMA:
        if snippet not in schema:
            errors.append(f'schema missing snippet: {snippet}')

    for filename in REQ_EXAMPLE_FILES:
        path = EXAMPLES / filename
        text = read(path, errors)
        for snippet in REQ_COMMON:
            if snippet not in text:
                errors.append(f'{filename} missing common snippet: {snippet}')
        for snippet in REQ_BY_TYPE[filename]:
            if snippet not in text:
                errors.append(f'{filename} missing type snippet: {snippet}')

    if errors:
        print('CEDV canonical schema check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('CEDV canonical schema check: PASS')
    print('- Claim / Evidence / Dissent / Verdict schema floor present')
    print('- examples for all four object families present')
    print('- public_candidate_object held as wrapper, not fifth CEDV family')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
