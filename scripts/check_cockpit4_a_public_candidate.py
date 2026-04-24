#!/usr/bin/env python3
"""Semantic checker for the COCKPIT4-A public-candidate admission floor."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'cockpit' / 'COCKPIT4-A'
ENTRY = BASE / 'cockpit4-a-entry-decision-v1.md'
OBJECT = BASE / 'cockpit4-a-public-candidate-object-v1.md'
ACCEPT = BASE / 'cockpit4-a-acceptance-pass-v1.md'

REQ_ENTRY = [
    'ENTER_COCKPIT4_A_PUBLIC_CANDIDATE_ADMISSION_FLOOR',
    'without implying publication authority',
]
REQ_OBJECT = [
    'public_candidate_object',
    'source_object_kind',
    'provenance_trace',
    'current_verdict_posture',
    'dissent_residue_status',
    'audit_fingerprint',
    'export_snapshot_boundary',
    'none_remaining_documented',
    'narrowed_carried_forward',
    'unresolved_carried_forward',
    'not_yet_evaluated_hold',
    'none_linked',
    'snapshot_id',
    'included_object_set',
    'excluded_object_set',
    'frozen_snapshot_reference',
    'non_upgrade_clause',
    'candidate admission does not create publication authority',
    'verdict finalization',
    'governed mutation authority',
    'public-truth status',
]
REQ_ACCEPT = [
    'PASS_PUBLIC_CANDIDATE_OBJECT_FLOOR',
    'PASS_PUBLIC_CANDIDATE_ADMISSION_GRAMMAR',
    'HOLD_PUBLIC_CANDIDATE_NOT_YET_AUDITABLE',
    'FAIL_PUBLIC_CANDIDATE_OBJECT_NOT_FORMED',
    'none_remaining_documented',
    'narrowed_carried_forward',
    'unresolved_carried_forward',
    'not_yet_evaluated_hold',
    'snapshot_id',
    'included_object_set',
    'excluded_object_set',
    'frozen_snapshot_reference',
    'non_upgrade_clause',
    'dissent-honest',
    'snapshot-bounded',
    'non-published',
]
FORBIDDEN_OBJECT_PHRASES = [
    'no major issues',
    'basically settled',
    'basically public already',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def require(snippets: list[str], text: str, label: str, errors: list[str]) -> None:
    for snippet in snippets:
        if snippet not in text:
            errors.append(f'{label} missing snippet: {snippet}')


def main() -> int:
    errors: list[str] = []
    entry = read(ENTRY, errors)
    obj = read(OBJECT, errors)
    accept = read(ACCEPT, errors)

    require(REQ_ENTRY, entry, 'entry', errors)
    require(REQ_OBJECT, obj, 'public candidate object', errors)
    require(REQ_ACCEPT, accept, 'acceptance', errors)

    lowered_obj = obj.lower()
    for phrase in FORBIDDEN_OBJECT_PHRASES:
        if phrase in lowered_obj:
            errors.append(f'public candidate object contains forbidden vague phrase: {phrase}')

    if errors:
        print('COCKPIT4-A public candidate semantic check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('COCKPIT4-A public candidate semantic check: PASS')
    print('- public_candidate_object floor present')
    print('- dissent_residue_status uses explicit status classes')
    print('- export_snapshot_boundary is structured and non-upgrade preserving')
    print('- candidate admission remains non-publication and non-finalization')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
