#!/usr/bin/env python3
"""Semantic checker for the COCKPIT4-A-B public-candidate index floor."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'cockpit' / 'COCKPIT4-A-B'
ENTRY = BASE / 'cockpit4-a-b-entry-decision-v1.md'
OBJECT_NOTE = BASE / 'cockpit4-a-b-public-candidate-index-v1.md'
ACCEPT = BASE / 'cockpit4-a-b-acceptance-pass-v1.md'
INDEX = BASE / 'public-candidate-index-v1.json'

REQ_TEXT = [
    (ENTRY, [
        'ENTER_COCKPIT4_A_B_PUBLIC_CANDIDATE_INDEX_FLOOR',
        'does not create publication authority',
    ]),
    (OBJECT_NOTE, [
        'public-candidate:h-pylori-ulcer-summary:v1',
        'object_id',
        'candidate_stage',
        'source_object_kind',
        'candidate_file',
        'dissent_residue_status_class',
        'snapshot_id',
        'registry_status',
        'publication authority',
        'public-truth status',
    ]),
    (ACCEPT, [
        'PASS_PUBLIC_CANDIDATE_INDEX_FLOOR',
        'PASS_PUBLIC_CANDIDATE_REGISTRY_CONSISTENT',
        'HOLD_PUBLIC_CANDIDATE_INDEX_NOT_YET_CONSISTENT',
        'FAIL_PUBLIC_CANDIDATE_INDEX_NOT_FORMED',
        'candidate_count',
        'candidate_file',
        'publication authority',
        'verdict finalization',
        'governed mutation authority',
        'public-truth status',
    ]),
]
REQ_INDEX_TOP = [
    'index_type',
    'index_id',
    'stage',
    'status',
    'candidate_count',
    'non_publication_clause',
    'entries',
]
REQ_ENTRY_KEYS = [
    'object_id',
    'candidate_stage',
    'source_object_kind',
    'candidate_file',
    'dissent_residue_status_class',
    'snapshot_id',
    'registry_status',
]
NON_UPGRADE_SNIPPETS = [
    'publication authority',
    'verdict finalization',
    'governed mutation authority',
    'public-truth status',
]


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def require_snippets(path: Path, snippets: list[str], errors: list[str]) -> None:
    text = read_text(path, errors)
    for snippet in snippets:
        if snippet not in text:
            errors.append(f'{path.relative_to(ROOT)} missing snippet: {snippet}')


def require_keys(obj: dict, keys: list[str], label: str, errors: list[str]) -> None:
    for key in keys:
        if key not in obj:
            errors.append(f'{label} missing key: {key}')


def load_json(path: Path, label: str, errors: list[str]) -> dict:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return {}
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        errors.append(f'{label} JSON is invalid: {exc}')
        return {}
    if not isinstance(data, dict):
        errors.append(f'{label} JSON root must be an object')
        return {}
    return data


def main() -> int:
    errors: list[str] = []

    for path, snippets in REQ_TEXT:
        require_snippets(path, snippets, errors)

    index = load_json(INDEX, 'index', errors)
    require_keys(index, REQ_INDEX_TOP, 'index', errors)

    if index.get('index_type') != 'public_candidate_index':
        errors.append('index.index_type must be public_candidate_index')

    entries = index.get('entries', [])
    if not isinstance(entries, list) or not entries:
        errors.append('index.entries must be a non-empty list')
        entries = []

    if index.get('candidate_count') != len(entries):
        errors.append('index.candidate_count must equal len(entries)')

    clause = index.get('non_publication_clause', '')
    for snippet in NON_UPGRADE_SNIPPETS:
        if snippet not in clause:
            errors.append(f'index.non_publication_clause missing snippet: {snippet}')

    for i, entry in enumerate(entries):
        label = f'entry[{i}]'
        if not isinstance(entry, dict):
            errors.append(f'{label} must be an object')
            continue
        require_keys(entry, REQ_ENTRY_KEYS, label, errors)
        candidate_file = entry.get('candidate_file')
        if candidate_file:
            path = ROOT / candidate_file
            candidate = load_json(path, f'{label}.candidate_file', errors)
            if candidate and candidate.get('object_id') != entry.get('object_id'):
                errors.append(f'{label}.object_id does not match candidate file object_id')
            candidate_dissent = candidate.get('dissent_residue_status', {}) if candidate else {}
            if isinstance(candidate_dissent, dict):
                if candidate_dissent.get('status_class') != entry.get('dissent_residue_status_class'):
                    errors.append(f'{label}.dissent_residue_status_class does not match candidate file')
            boundary = candidate.get('export_snapshot_boundary', {}) if candidate else {}
            if isinstance(boundary, dict):
                if boundary.get('snapshot_id') != entry.get('snapshot_id'):
                    errors.append(f'{label}.snapshot_id does not match candidate file')
        if entry.get('registry_status') != 'indexed_candidate_not_published':
            errors.append(f'{label}.registry_status must be indexed_candidate_not_published')

    if errors:
        print('COCKPIT4-A-B public candidate index check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT4-A-B public candidate index check: PASS')
    print('- public candidate index exists')
    print('- candidate_count matches entries')
    print('- registry entry is complete')
    print('- registry entry matches candidate JSON')
    print('- indexing remains non-publication')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
