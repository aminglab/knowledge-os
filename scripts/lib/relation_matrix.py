"""Relation-admissibility matrix helpers for CEDV protocol checkers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from scripts.lib.protocol_constants import CANONICAL_RELATION_TYPES, CEDV_OBJECT_TYPES


def load_relation_matrix(path: Path) -> dict[str, Any]:
    """Load a relation matrix JSON file."""
    return json.loads(path.read_text(encoding='utf-8'))


def validate_relation_matrix(matrix: dict[str, Any]) -> list[str]:
    """Return validation errors for the relation matrix shape and vocabulary."""
    errors: list[str] = []
    if matrix.get('schema_name') != 'cedv_relation_admissibility_matrix':
        errors.append('relation matrix schema_name must be cedv_relation_admissibility_matrix')
    if matrix.get('schema_version') != 'v1':
        errors.append('relation matrix schema_version must be v1')

    relation_rules = matrix.get('relation_rules')
    if not isinstance(relation_rules, list) or not relation_rules:
        errors.append('relation matrix relation_rules must be a non-empty list')
        relation_rules = []
    for index, rule in enumerate(relation_rules):
        if not isinstance(rule, dict):
            errors.append(f'relation_rules[{index}] must be an object')
            continue
        source_type = rule.get('source_type')
        relation = rule.get('relation')
        target_types = rule.get('target_types')
        if source_type not in CEDV_OBJECT_TYPES:
            errors.append(f'relation_rules[{index}] source_type is not a CEDV type: {source_type}')
        if relation not in CANONICAL_RELATION_TYPES:
            errors.append(f'relation_rules[{index}] relation is not canonical: {relation}')
        if not isinstance(target_types, list) or not target_types:
            errors.append(f'relation_rules[{index}] target_types must be a non-empty list')
            continue
        for target_type in target_types:
            if target_type not in CEDV_OBJECT_TYPES:
                errors.append(f'relation_rules[{index}] target_type is not a CEDV type: {target_type}')

    external_rules = matrix.get('external_target_rules')
    if not isinstance(external_rules, list):
        errors.append('relation matrix external_target_rules must be a list')
        external_rules = []
    for index, rule in enumerate(external_rules):
        if not isinstance(rule, dict):
            errors.append(f'external_target_rules[{index}] must be an object')
            continue
        source_type = rule.get('source_type')
        relation = rule.get('relation')
        target_prefixes = rule.get('target_prefixes')
        if source_type not in CEDV_OBJECT_TYPES:
            errors.append(f'external_target_rules[{index}] source_type is not a CEDV type: {source_type}')
        if relation not in CANONICAL_RELATION_TYPES:
            errors.append(f'external_target_rules[{index}] relation is not canonical: {relation}')
        if rule.get('allowed') is not True:
            errors.append(f'external_target_rules[{index}] allowed must be true')
        if not isinstance(target_prefixes, list) or not target_prefixes:
            errors.append(f'external_target_rules[{index}] target_prefixes must be a non-empty list')

    return errors


def relation_allowed_by_matrix(
    matrix: dict[str, Any],
    source_type: str,
    relation: str,
    target: str,
    target_type: str | None,
) -> bool:
    """Return whether a relation is admissible under a CEDV relation matrix."""
    if target_type:
        for rule in matrix.get('relation_rules', []):
            if (
                isinstance(rule, dict)
                and rule.get('source_type') == source_type
                and rule.get('relation') == relation
                and target_type in rule.get('target_types', [])
            ):
                return True
        return False

    for rule in matrix.get('external_target_rules', []):
        if not isinstance(rule, dict):
            continue
        if rule.get('source_type') != source_type or rule.get('relation') != relation:
            continue
        prefixes = rule.get('target_prefixes', [])
        if '*' in prefixes:
            return True
        if any(isinstance(prefix, str) and target.startswith(prefix) for prefix in prefixes):
            return True
    return False
