#!/usr/bin/env python3
"""Check the CEDV canonical example registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lib.protocol_constants import (  # noqa: E402
    CANONICAL_RELATION_TYPES,
    CEDV_OBJECT_TYPES,
)

BASE = ROOT / 'protocol' / 'cedv'
EXAMPLES = BASE / 'examples'
REGISTRY = EXAMPLES / 'index-v1.json'
DOC = BASE / 'example-registry-v1.md'

REQ_DOC = [
    'CEDV-B / Example Registry v1',
    'protocol/cedv/examples/index-v1.json',
    'PASS_CANONICAL_EXAMPLE_REGISTRY_FLOOR',
    'E-0001 supports C-0001',
    'D-0001 challenges C-0001',
    'V-0001 basis_refs: C-0001, E-0001, D-0001',
]


def read_text(path: Path, errors: list[str]) -> str:
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


def load_registry(errors: list[str]) -> dict:
    if not REGISTRY.exists():
        errors.append(f'Missing registry: {REGISTRY.relative_to(ROOT)}')
        return {}
    try:
        return json.loads(REGISTRY.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        errors.append(f'Registry is not valid JSON: {exc}')
        return {}


def main() -> int:
    errors: list[str] = []

    doc = read_text(DOC, errors)
    for snippet in REQ_DOC:
        if snippet not in doc:
            errors.append(f'example-registry-v1.md missing snippet: {snippet}')

    registry = load_registry(errors)
    if registry:
        if registry.get('schema_name') != 'cedv_canonical_example_registry':
            errors.append('registry schema_name must be cedv_canonical_example_registry')
        if registry.get('schema_version') != 'v1':
            errors.append('registry schema_version must be v1')
        if registry.get('registry_scope') != 'protocol/cedv/examples':
            errors.append('registry_scope must be protocol/cedv/examples')

    examples = registry.get('examples') if isinstance(registry, dict) else None
    if not isinstance(examples, list) or not examples:
        errors.append('registry examples must be a non-empty list')
        examples = []

    registered_paths = set()
    objects: dict[str, dict] = {}
    object_types_seen: set[str] = set()

    for entry in examples:
        if not isinstance(entry, dict):
            errors.append('registry example entry must be an object')
            continue
        object_id = entry.get('id')
        object_type = entry.get('object_type')
        path_value = entry.get('path')
        expected_title = entry.get('expected_title')
        if not isinstance(object_id, str):
            errors.append('registry example missing string id')
            continue
        if object_type not in CEDV_OBJECT_TYPES:
            errors.append(f'{object_id}: registry object_type is not a CEDV type: {object_type}')
        else:
            object_types_seen.add(object_type)
        if not isinstance(path_value, str):
            errors.append(f'{object_id}: registry path must be a string')
            continue
        if not path_value.startswith('protocol/cedv/examples/'):
            errors.append(f'{object_id}: registry path must stay under protocol/cedv/examples')
            continue
        registered_paths.add(path_value)
        path = ROOT / path_value
        text = read_text(path, errors)
        if not text:
            continue
        parsed = parse_simple_yaml(text)
        objects[object_id] = parsed
        if parsed.get('id') != object_id:
            errors.append(f'{object_id}: YAML id does not match registry id')
        if parsed.get('object_type') != object_type:
            errors.append(f'{object_id}: YAML object_type does not match registry object_type')
        if isinstance(expected_title, str) and parsed.get('title') != expected_title:
            errors.append(f'{object_id}: YAML title does not match registry expected_title')

    yaml_files = {str(path.relative_to(ROOT)) for path in EXAMPLES.glob('*.yaml')}
    unregistered_yaml = sorted(yaml_files - registered_paths)
    if unregistered_yaml:
        errors.append(f'unregistered CEDV example YAML files: {", ".join(unregistered_yaml)}')

    required_object_types = registry.get('required_object_types') if isinstance(registry, dict) else None
    if not isinstance(required_object_types, list):
        errors.append('registry required_object_types must be a list')
        required_object_types = []
    for required_type in required_object_types:
        if required_type not in CEDV_OBJECT_TYPES:
            errors.append(f'required_object_types includes non-CEDV type: {required_type}')
        if required_type not in object_types_seen:
            errors.append(f'required object type is not represented in examples: {required_type}')

    graph = registry.get('graph_expectations') if isinstance(registry, dict) else None
    if not isinstance(graph, dict):
        errors.append('registry graph_expectations must be an object')
        graph = {}

    required_links = graph.get('required_links')
    if not isinstance(required_links, list):
        errors.append('graph_expectations.required_links must be a list')
        required_links = []
    for link_req in required_links:
        if not isinstance(link_req, dict):
            errors.append('required_links entry must be an object')
            continue
        source = link_req.get('source')
        rel = link_req.get('type')
        target = link_req.get('target')
        if not isinstance(source, str) or source not in objects:
            errors.append(f'required link source does not resolve: {source}')
            continue
        if rel not in CANONICAL_RELATION_TYPES:
            errors.append(f'required link relation is not canonical: {rel}')
            continue
        links = objects[source].get('links')
        if not isinstance(links, list):
            errors.append(f'{source}: links must be a list to satisfy registry expectations')
            continue
        if not any(isinstance(link, dict) and link.get('type') == rel and link.get('target') == target for link in links):
            errors.append(f'missing required link: {source} {rel} {target}')

    required_basis = graph.get('required_basis_refs')
    if not isinstance(required_basis, dict):
        errors.append('graph_expectations.required_basis_refs must be an object')
        required_basis = {}
    for source, refs in required_basis.items():
        if source not in objects:
            errors.append(f'required basis source does not resolve: {source}')
            continue
        basis_refs = objects[source].get('basis_refs')
        if not isinstance(basis_refs, list):
            errors.append(f'{source}: basis_refs must be a list to satisfy registry expectations')
            continue
        if not isinstance(refs, list):
            errors.append(f'{source}: required basis refs must be a list')
            continue
        for ref in refs:
            if ref not in basis_refs:
                errors.append(f'{source}: missing required basis_ref: {ref}')

    if errors:
        print('CEDV example registry check: FAIL')
        for err in errors:
            print(f'- {err}')
        return 1

    print('CEDV example registry check: PASS')
    print('- canonical example registry is present')
    print('- all example YAML files are registered')
    print('- required CEDV object families are represented')
    print('- minimal required graph expectations are satisfied')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
