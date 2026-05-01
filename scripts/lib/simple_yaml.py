"""Tiny YAML subset parser shared by protocol checkers.

This is intentionally not a general YAML implementation.
It only supports the small frontmatter-like subset used by current protocol
example objects:

- top-level scalar keys;
- top-level list keys;
- list values that are either scalars or simple one-level maps.

If repository data grows beyond this subset, replace this utility with a real
YAML parser deliberately rather than silently expanding it into a half-parser.
"""

from __future__ import annotations

from typing import Any

LIST_KEYS = {'source_refs', 'basis_refs', 'links'}


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the tiny YAML subset used by current protocol examples."""
    data: dict[str, Any] = {}
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
                data[key] = [] if key in LIST_KEYS else {}
                current_list_key = key if key in LIST_KEYS else None
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
                data[current_list_key].append(current_map)
                current_map_key = current_list_key
            else:
                data[current_list_key].append(value)
            continue

        if current_map_key == 'links' and current_map is not None and ':' in stripped:
            k, v = stripped.split(':', 1)
            current_map[k.strip()] = v.strip()
            continue

    return data
