"""Shared protocol constants for Knowledge OS checkers.

This module keeps compact working-set vocabularies in one place so individual
checkers do not silently drift from the protocol docs.
"""

from __future__ import annotations

CANONICAL_RELATION_TYPES = {
    "supports",
    "challenges",
    "cites",
    "depends_on",
    "descends_from",
    "supersedes",
    "pinned_in_snapshot",
}

LEGACY_RELATION_ALIASES = {
    "supported_by",
    "weakens",
    "attacks",
    "attacked_by",
    "responds_to",
    "rules_on",
    "ruled_on",
    "splits_from",
    "splits_to",
    "published_as",
    "derived_from",
    "based_on",
    "cited_by",
    "coexists_with",
}

SELF_RELATION_TYPES = {
    "descends_from",
    "supersedes",
    "splits_from",
    "splits_to",
}

LIFECYCLE_STATES = {
    "draft",
    "active",
    "paused",
    "superseded",
    "withdrawn",
    "archived",
    "linked",
}

VISIBILITY_LEVELS = {
    "private",
    "team",
    "public",
}

EPISTEMIC_STATUS_VALUES = {
    "under_evaluation",
    "supported",
    "contested",
    "weakened",
    "rejected",
    "split",
    "stabilized",
}

VERDICT_LEVELS = {
    "local",
    "provisional",
    "supported",
    "contested",
    "weakened",
    "stabilized",
    "rejected",
    "split",
    "unresolved",
}

DISSENT_KINDS = {
    "empirical",
    "methodological",
    "logical",
    "definitional",
    "procedural",
    "scope",
    "interpretive",
}

SEVERITY_LEVELS = {
    "low",
    "medium",
    "high",
    "critical",
}

ID_PREFIXES = {
    "claim": "C-",
    "evidence": "E-",
    "dissent": "D-",
    "verdict": "V-",
}

CEDV_OBJECT_TYPES = {
    "claim",
    "evidence",
    "dissent",
    "verdict",
}
