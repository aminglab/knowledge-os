"""Small CEDV object-loading helpers for protocol checkers.

This module is intentionally scoped to current CEDV example objects.
It is not a repository-wide object registry and should not grow into one by
accident.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Any

from scripts.lib.protocol_constants import CEDV_OBJECT_TYPES
from scripts.lib.simple_yaml import parse_simple_yaml


def load_cedv_objects(
    paths: Iterable[Path],
    errors: list[str],
    root: Path,
) -> dict[str, dict[str, Any]]:
    """Load CEDV example objects from paths into an id-keyed dictionary.

    Errors are appended rather than raised so checkers can report all failures
    in one pass.
    """
    objects: dict[str, dict[str, Any]] = {}

    for path in paths:
        display_path = path.relative_to(root) if path.is_absolute() or path.exists() else path
        if not path.exists():
            errors.append(f'Missing CEDV object file: {display_path}')
            continue

        parsed = parse_simple_yaml(path.read_text(encoding='utf-8'))
        object_id = parsed.get('id')
        if not isinstance(object_id, str):
            errors.append(f'{display_path} missing id')
            continue
        if object_id in objects:
            errors.append(f'duplicate object id: {object_id}')

        object_type = parsed.get('object_type')
        if object_type not in CEDV_OBJECT_TYPES:
            errors.append(f'{object_id}: object_type is not a CEDV type: {object_type}')

        objects[object_id] = parsed

    return objects
