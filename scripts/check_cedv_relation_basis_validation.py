#!/usr/bin/env python3
"""Checker for the CEDV implementation subset of the record-consistency floor."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lib.protocol_constants import CANONICAL_RELATION_TYPES  # noqa: E402

BASE = ROOT / 'protocol' / 'cedv'
DOC = BASE / 'relation-basis-validation-v1.md'
EXAMPLES = BASE / 'examples'

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


def parse_simple_yaml(text: str) -> dict:
    data: dict[str, object] = {}
    current_list_key: str | None = None
    current_map_key: str | None = None
    current_map: dict[str, str] | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip().startswith('#'):
            continue
        if not line.startswith(' ') and ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            current_map_key = None
            current_map = None
            if value == '':
                data[key] = [] if key in {'source_refs', 'basis_refs', 'links'} else {}
                current_list_key = key if key in {'source_refs', 'basis_refs', 'links'} else None
            else:
                data[key] = value
                current_list_key = None
            continue

        stripped = line.strip()
        if current_list_key and stripped.startswith('- '):
            value = stripped[2:].strip()
            if current_list_key == 'links' and ':' in value:
                k, v = value.split(':', 1)
                current_map = {k.strip(): v.strip()}
                data[current_list_key].append(current_map)  # type: ignore[index]
                current_map_key = current_list_key
            else:
                data[current_list_key].append(value)  # type: ignore[index]
            continue

        if current_map_key == 'links' and current_map is not None and ':' in stripped:
            k, v = stripped.split(':', 1)
            current_map[k.strip()] = v.strip()
            continue

    return data


def object_family(object_id: str) -> str | None:
    if object_id.startswith('C-'):
        return 'claim'
    if object_id.startswith('E-'):
        return 'evidence'
    if object_id.startswith('D-'):
        return 'dissent'
    if object_id.startswith('V-'):
        return 'verdict'
    return None


def relation_allowed(source_type: str, rel: str, target: str) -> bool:
    target_type = object_family(target)
    if rel == 'cites':
        return True
    if rel == 'pinned_in_snapshot':
        return source_type == 'verdict' and (target.startswith('public-candidate:') or target.startswith('snapshot:'))
    if not target_type:
        return False
    if source_type == 'claim':
        return (rel in {'depends_on', 'descends_from'} and target_type == 'claim') or (rel == 'supersedes' and target_type in {'claim', 'verdict'})
    if source_type == 'evidence':
        return rel in {'supports', 'challenges'} and target_type in {'claim', 'verdict'}
    if source_type == 'dissent':
        return rel == 'challenges' and target_type in {'claim', 'evidence', 'dissent', 'verdict'}
    if source_type == 'verdict':
        return (rel == 'depends_on' and target_type in {'claim', 'evidence', 'dissent', 'verdict'}) or (rel == 'supersedes' and target_type == 'verdict')
    return False


def main() -> int:
    errors: list[str] = []
    doc = read(DOC, errors)
    for snippet in REQ_DOC:
        if snippet not in doc:
            errors.append(f'doc missing snippet: {snippet}')

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
            if not relation_allowed(source_type, rel, target):
                errors.append(f'{object_id} relation not admissible: {source_type} {rel} {target}')
            if object_family(target) and target not in objects:
                errors.append(f'{object_id} link target does not resolve: {target}')

    if errors:
        print('CEDV relation and basis validation check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('CEDV relation and basis validation check: PASS')
    print('- object ids are unique')
    print('- CEDV link targets and basis_refs resolve')
    print('- relation source/target families are admissible')
    print('- evidence, dissent, and verdict objects do not float free')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
