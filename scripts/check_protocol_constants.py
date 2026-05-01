#!/usr/bin/env python3
"""Check that protocol docs and shared constants do not drift silently."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lib.protocol_constants import (  # noqa: E402
    CANONICAL_RELATION_TYPES,
    DISSENT_KINDS,
    EPISTEMIC_STATUS_VALUES,
    LIFECYCLE_STATES,
    SEVERITY_LEVELS,
    VERDICT_LEVELS,
    VISIBILITY_LEVELS,
)

ENUMS = ROOT / 'protocol' / 'enums.md'
LINK_TYPES = ROOT / 'protocol' / 'link-types.md'
CEDV_SCHEMA = ROOT / 'protocol' / 'cedv' / 'canonical-object-schema-v1.md'
CEDV_ENUM_COVERAGE = ROOT / 'protocol' / 'cedv' / 'enum-coverage-v1.md'

ENUM_SECTIONS = {
    'lifecycle_state': LIFECYCLE_STATES,
    'epistemic_status': EPISTEMIC_STATUS_VALUES,
    'visibility': VISIBILITY_LEVELS,
    'dissent_kind': DISSENT_KINDS,
    'severity': SEVERITY_LEVELS,
    'verdict_level': VERDICT_LEVELS,
}

REQ_ENUMS = [
    '# Protocol Enums (Working Set)',
    'prevent silent vocabulary drift while the language is still young',
    'scripts/lib/protocol_constants.py',
]
REQ_SCHEMA = [
    'Enum vocabularies are owned by `protocol/enums.md`',
    'Canonical relation names are owned by `protocol/link-types.md`',
    'lifecycle_state: <see protocol/enums.md>',
    'visibility: <see protocol/enums.md>',
    'verdict_level: <see protocol/enums.md>',
]
REQ_ENUM_COVERAGE = [
    'CEDV-C / Enum Coverage v1',
    'PASS_WORKING_ENUM_COVERAGE_LAYER',
    'lifecycle_state',
    'epistemic_status',
    'visibility',
    'dissent_kind',
    'severity',
    'verdict_level',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def section_text(markdown: str, heading: str) -> str:
    marker = f'## {heading}'
    start = markdown.find(marker)
    if start == -1:
        return ''
    next_heading = markdown.find('\n## ', start + len(marker))
    if next_heading == -1:
        return markdown[start:]
    return markdown[start:next_heading]


def main() -> int:
    errors: list[str] = []
    enums = read(ENUMS, errors)
    link_types = read(LINK_TYPES, errors)
    schema = read(CEDV_SCHEMA, errors)
    enum_coverage = read(CEDV_ENUM_COVERAGE, errors)

    for snippet in REQ_ENUMS:
        if snippet not in enums:
            errors.append(f'enums.md missing snippet: {snippet}')
    for snippet in REQ_SCHEMA:
        if snippet not in schema:
            errors.append(f'canonical CEDV schema missing snippet: {snippet}')
    for snippet in REQ_ENUM_COVERAGE:
        if snippet not in enum_coverage:
            errors.append(f'enum-coverage-v1.md missing snippet: {snippet}')

    for enum_name, values in ENUM_SECTIONS.items():
        section = section_text(enums, enum_name)
        if not section:
            errors.append(f'enums.md missing enum section: {enum_name}')
            continue
        for value in sorted(values):
            if f'`{value}`' not in section:
                errors.append(f'enums.md missing {enum_name} value: {value}')

    for relation in sorted(CANONICAL_RELATION_TYPES):
        if f'`{relation}`' not in link_types:
            errors.append(f'link-types.md missing canonical relation: {relation}')

    if errors:
        print('Protocol constants drift check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('Protocol constants drift check: PASS')
    print('- lifecycle_state working set is documented in protocol/enums.md')
    print('- epistemic_status working set is documented in protocol/enums.md')
    print('- visibility working set is documented in protocol/enums.md')
    print('- dissent_kind working set is documented in protocol/enums.md')
    print('- severity working set is documented in protocol/enums.md')
    print('- verdict_level working set is documented in protocol/enums.md')
    print('- canonical relation working set is documented in protocol/link-types.md')
    print('- CEDV schema references enum/link owners rather than redefining them')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
