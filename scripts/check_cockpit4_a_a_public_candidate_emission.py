#!/usr/bin/env python3
"""Semantic checker for the COCKPIT4-A-A public-candidate emission prototype."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'cockpit' / 'COCKPIT4-A-A'
ENTRY = BASE / 'cockpit4-a-a-entry-decision-v1.md'
OBJECT_NOTE = BASE / 'cockpit4-a-a-public-candidate-emission-v1.md'
ACCEPT = BASE / 'cockpit4-a-a-acceptance-pass-v1.md'
SAMPLE = BASE / 'public-candidates' / 'h-pylori-ulcer-summary-public-candidate-v1.json'

LAWFUL_DISSENT_STATUS = {
    'none_remaining_documented',
    'narrowed_carried_forward',
    'unresolved_carried_forward',
    'not_yet_evaluated_hold',
}

REQ_TEXT = [
    (ENTRY, [
        'ENTER_COCKPIT4_A_A_PUBLIC_CANDIDATE_EMISSION_PROTOTYPE',
        'does not create publication authority',
    ]),
    (OBJECT_NOTE, [
        'public-candidate:h-pylori-ulcer-summary:v1',
        'source_object_kind',
        'provenance_trace',
        'current_verdict_posture',
        'dissent_residue_status',
        'audit_fingerprint',
        'export_snapshot_boundary',
        'public-truth status',
    ]),
    (ACCEPT, [
        'PASS_PUBLIC_CANDIDATE_EMISSION_PROTOTYPE',
        'PASS_PUBLIC_CANDIDATE_FIELDS_CHECKER_VISIBLE',
        'HOLD_PUBLIC_CANDIDATE_SAMPLE_NOT_YET_AUDITABLE',
        'FAIL_PUBLIC_CANDIDATE_SAMPLE_NOT_FORMED',
        'snapshot_id',
        'included_object_set',
        'excluded_object_set',
        'frozen_snapshot_reference',
        'non_upgrade_clause',
    ]),
]

REQ_SAMPLE_TOP = [
    'object_type',
    'object_id',
    'candidate_stage',
    'source_object_kind',
    'provenance_trace',
    'current_verdict_posture',
    'dissent_residue_status',
    'audit_fingerprint',
    'export_snapshot_boundary',
]
REQ_PROVENANCE = [
    'private_source_path_or_object_id',
    'producing_cockpit_stage_or_route',
    'latest_governed_snapshot_reference',
    'parent_object_relation',
]
REQ_VERDICT = [
    'label',
    'posture_class',
    'inherited_or_summarized',
    'non_finalization_note',
]
REQ_DISSENT = [
    'status_class',
    'linked_dissent_object_ids',
    'residue_summary',
    'public_reader_warning',
]
REQ_AUDIT = [
    'stable_id',
    'snapshot_producing_source',
    'frozen_reference',
]
REQ_BOUNDARY = [
    'snapshot_id',
    'included_object_set',
    'excluded_object_set',
    'frozen_snapshot_reference',
    'non_upgrade_clause',
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


def main() -> int:
    errors: list[str] = []

    for path, snippets in REQ_TEXT:
        require_snippets(path, snippets, errors)

    if not SAMPLE.exists():
        errors.append(f'Missing file: {SAMPLE.relative_to(ROOT)}')
        sample = {}
    else:
        try:
            sample = json.loads(SAMPLE.read_text(encoding='utf-8'))
        except json.JSONDecodeError as exc:
            errors.append(f'Sample JSON is invalid: {exc}')
            sample = {}

    if isinstance(sample, dict):
        require_keys(sample, REQ_SAMPLE_TOP, 'sample', errors)
        if sample.get('object_type') != 'public_candidate_object':
            errors.append('sample.object_type must be public_candidate_object')

        provenance = sample.get('provenance_trace', {})
        verdict = sample.get('current_verdict_posture', {})
        dissent = sample.get('dissent_residue_status', {})
        audit = sample.get('audit_fingerprint', {})
        boundary = sample.get('export_snapshot_boundary', {})

        if isinstance(provenance, dict):
            require_keys(provenance, REQ_PROVENANCE, 'provenance_trace', errors)
        else:
            errors.append('provenance_trace must be an object')

        if isinstance(verdict, dict):
            require_keys(verdict, REQ_VERDICT, 'current_verdict_posture', errors)
        else:
            errors.append('current_verdict_posture must be an object')

        if isinstance(dissent, dict):
            require_keys(dissent, REQ_DISSENT, 'dissent_residue_status', errors)
            status = dissent.get('status_class')
            if status not in LAWFUL_DISSENT_STATUS:
                errors.append(f'dissent_residue_status.status_class is not lawful: {status}')
            linked = dissent.get('linked_dissent_object_ids')
            if not isinstance(linked, list) or not linked:
                errors.append('dissent_residue_status.linked_dissent_object_ids must be a non-empty list or explicit none_linked in future samples')
        else:
            errors.append('dissent_residue_status must be an object')

        if isinstance(audit, dict):
            require_keys(audit, REQ_AUDIT, 'audit_fingerprint', errors)
        else:
            errors.append('audit_fingerprint must be an object')

        if isinstance(boundary, dict):
            require_keys(boundary, REQ_BOUNDARY, 'export_snapshot_boundary', errors)
            included = boundary.get('included_object_set')
            excluded = boundary.get('excluded_object_set')
            if not isinstance(included, list) or not included:
                errors.append('export_snapshot_boundary.included_object_set must be a non-empty list')
            if not isinstance(excluded, list) or not excluded:
                errors.append('export_snapshot_boundary.excluded_object_set must be a non-empty list')
            clause = boundary.get('non_upgrade_clause', '')
            for snippet in NON_UPGRADE_SNIPPETS:
                if snippet not in clause:
                    errors.append(f'non_upgrade_clause missing snippet: {snippet}')
        else:
            errors.append('export_snapshot_boundary must be an object')
    else:
        errors.append('Sample JSON root must be an object')

    if errors:
        print('COCKPIT4-A-A public candidate emission check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT4-A-A public candidate emission check: PASS')
    print('- one concrete public_candidate_object sample emitted')
    print('- all six COCKPIT4-A fields are machine-checkable')
    print('- dissent residue status is lawful and explicit')
    print('- export snapshot boundary preserves non-upgrade discipline')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
