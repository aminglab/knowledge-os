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
    VERDICT_LEVELS,
)

ENUMS = ROOT / 'protocol' / 'enums.md'
LINK_TYPES = ROOT / 'protocol' / 'link-types.md'
CEDV_SCHEMA = ROOT / 'protocol' / 'cedv' / 'canonical-object-schema-v1.md'

REQ_ENUMS = [
    '## verdict_level',
    'Current working values for verdict objects:',
    'verdict_level is distinct from claim-like `epistemic_status`',
    'scripts/lib/protocol_constants.py',
]
REQ_SCHEMA = [
    'Enum vocabularies are owned by `protocol/enums.md`',
    'Canonical relation names are owned by `protocol/link-types.md`',
    'verdict_level: <see protocol/enums.md>',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def main() -> int:
    errors: list[str] = []
    enums = read(ENUMS, errors)
    link_types = read(LINK_TYPES, errors)
    schema = read(CEDV_SCHEMA, errors)

    for snippet in REQ_ENUMS:
        if snippet not in enums:
            errors.append(f'enums.md missing snippet: {snippet}')
    for snippet in REQ_SCHEMA:
        if snippet not in schema:
            errors.append(f'canonical CEDV schema missing snippet: {snippet}')

    for value in sorted(VERDICT_LEVELS):
        if f'`{value}`' not in enums:
            errors.append(f'enums.md missing verdict_level value: {value}')

    for relation in sorted(CANONICAL_RELATION_TYPES):
        if f'`{relation}`' not in link_types:
            errors.append(f'link-types.md missing canonical relation: {relation}')

    if errors:
        print('Protocol constants drift check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('Protocol constants drift check: PASS')
    print('- verdict_level working set is documented in protocol/enums.md')
    print('- canonical relation working set is documented in protocol/link-types.md')
    print('- CEDV schema references enum/link owners rather than redefining them')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
