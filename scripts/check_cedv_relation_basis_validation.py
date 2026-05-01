#!/usr/bin/env python3
"""Checker for the CEDV implementation subset of the record-consistency floor."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lib.protocol_constants import (  # noqa: E402
    CANONICAL_RELATION_TYPES,
    CEDV_ID_PREFIX_TO_OBJECT_TYPE,
    CEDV_OBJECT_TYPES,
)
from scripts.lib.relation_matrix import (  # noqa: E402
    load_relation_matrix,
    relation_allowed_by_matrix,
    validate_relation_matrix,
)
from scripts.lib.simple_yaml import parse_simple_yaml  # noqa: E402

BASE = ROOT / 'protocol' / 'cedv'
DOC = BASE / 'relation-basis-validation-v1.md'
EXAMPLES = BASE / 'examples'
RELATION_MATRIX = BASE / 'relation-admissibility-matrix-v1.json'

REQ_DOC = [
    'object id uniqueness',
    'all link targets resolve',
    'all `basis_refs` resolve',
    'relation source and target families are admissible',
    'Evidence with no authored link',
    'Dissent with no authored challenge',
    'Verdict with empty `basis_refs`',
    'E-0001 supports C-0001',
    'D-0001 challenges C-0001',
    'V-0001 basis_refs: C-0001, E-0001, D-0001',
]
REQ_EXAMPLES = [
    'claim-C-0001.yaml',
    'evidence-E-0001.yaml',
    'dissent-D-0001.yaml',
    'verdict-V-0001.yaml',
]


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f'Missing file: {path.relative_to(ROOT)}')
        return ''
    return path.read_text(encoding='utf-8')


def object_family(object_id: str) -> str | None:
    for prefix, object_type in CEDV_ID_PREFIX_TO_OBJECT_TYPE.items():
        if object_id.startswith(prefix):
            return object_type
    return None


def main() -> int:
    errors: list[str] = []
    doc = read(DOC, errors)
    for snippet in REQ_DOC:
        if snippet not in doc:
            errors.append(f'doc missing snippet: {snippet}')

    if not RELATION_MATRIX.exists():
        errors.append(f'Missing relation matrix: {RELATION_MATRIX.relative_to(ROOT)}')
        relation_matrix = {}
    else:
        relation_matrix = load_relation_matrix(RELATION_MATRIX)
        errors.extend(validate_relation_matrix(relation_matrix))

    objects: dict[str, dict] = {}
    for filename in REQ_EXAMPLES:
        text = read(EXAMPLES / filename, errors)
        if not text:
            continue
        obj = parse_simple_yaml(text)
        object_id = obj.get('id')
        if not isinstance(object_id, str):
            errors.append(f'{filename} missing id')
            continue
        if object_id in objects:
            errors.append(f'duplicate object id: {object_id}')
        objects[object_id] = obj

    for object_id, obj in objects.items():
        source_type = obj.get('object_type')
        if not isinstance(source_type, str):
            errors.append(f'{object_id} missing object_type')
            continue
        if source_type not in CEDV_OBJECT_TYPES:
            errors.append(f'{object_id} object_type is not a shared CEDV type: {source_type}')
            continue
        links = obj.get('links')
        if not isinstance(links, list):
            errors.append(f'{object_id} links must be a list')
            links = []
        if source_type == 'evidence' and not links:
            errors.append(f'{object_id} evidence object must not float without links')
        if source_type == 'dissent' and not any(isinstance(l, dict) and l.get('type') == 'challenges' for l in links):
            errors.append(f'{object_id} dissent object must author at least one challenges link')
        if source_type == 'verdict':
            basis_refs = obj.get('basis_refs')
            if not isinstance(basis_refs, list) or not basis_refs:
                errors.append(f'{object_id} verdict must include non-empty basis_refs')
            else:
                for ref in basis_refs:
                    if ref not in objects:
                        errors.append(f'{object_id} basis_ref does not resolve: {ref}')

        for link in links:
            if not isinstance(link, dict):
                errors.append(f'{object_id} link must be an object')
                continue
            rel = link.get('type')
            target = link.get('target')
            if rel not in CANONICAL_RELATION_TYPES:
                errors.append(f'{object_id} link relation is not canonical: {rel}')
                continue
            if not isinstance(target, str):
                errors.append(f'{object_id} link target missing')
                continue
            target_type = object_family(target)
            if not relation_allowed_by_matrix(relation_matrix, source_type, rel, target, target_type):
                errors.append(f'{object_id} relation not admissible: {source_type} {rel} {target}')
            if target_type and target not in objects:
                errors.append(f'{object_id} link target does not resolve: {target}')

    if errors:
        print('CEDV relation and basis validation check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('CEDV relation and basis validation check: PASS')
    print('- object ids are unique')
    print('- CEDV link targets and basis_refs resolve')
    print('- relation source/target families are admissible through relation-admissibility-matrix-v1.json')
    print('- shared CEDV prefix and object-type constants are used by this checker')
    print('- shared simple YAML parser is used by this checker')
    print('- evidence, dissent, and verdict objects do not float free')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
