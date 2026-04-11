#!/usr/bin/env python3
"""Check minimal protocol record consistency against live pilot records."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
OBJECTS_ROOT = CASE_ROOT / "objects"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

ID_PREFIXES = {
    "claim": "C-",
    "evidence": "E-",
    "dissent": "D-",
    "verdict": "V-",
}

REQUIRED_FIELDS = {
    "id",
    "object_type",
    "title",
    "lifecycle_state",
    "visibility",
    "links",
}

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

CANONICAL_VERDICT_LEVELS = {
    "under_evaluation",
    "supported",
    "contested",
    "weakened",
    "rejected",
    "stabilized",
}

PILOT_LOCAL_VERDICT_LEVELS = {
    "original_claim_contested_and_weakened",
    "descendant_claim_contested_but_surviving",
}

RESOLVING_VERDICT_LINK_TYPES = {"rules_on"}


class ProtocolRecordConsistencyError(Exception):
    """Raised when hard-fail consistency violations are present."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter(text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return []
    return parts[0].splitlines()[1:]


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    return value


def parse_indented_block(lines: list[str]) -> Any:
    block = [line for line in lines if line.strip()]
    if not block:
        return None

    if block[0].startswith("  - "):
        items: list[Any] = []
        i = 0
        while i < len(block):
            line = block[i]
            if not line.startswith("  - "):
                i += 1
                continue

            item_head = line[4:]
            item: Any
            dict_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", item_head)
            if dict_match:
                item = {dict_match.group(1): parse_scalar(dict_match.group(2))}
            else:
                item = parse_scalar(item_head)

            i += 1
            while i < len(block) and block[i].startswith("    "):
                nested = block[i][4:]
                nested_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", nested)
                if isinstance(item, dict) and nested_match:
                    item[nested_match.group(1)] = parse_scalar(nested_match.group(2))
                i += 1

            items.append(item)
        return items

    mapping: dict[str, Any] = {}
    for line in block:
        if not line.startswith("  "):
            continue
        nested = line[2:]
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", nested)
        if match:
            mapping[match.group(1)] = parse_scalar(match.group(2))
    return mapping if mapping else None


def parse_frontmatter(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        top_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$", line)
        if not top_match:
            i += 1
            continue

        key = top_match.group(1)
        value = top_match.group(2)
        if value:
            data[key] = parse_scalar(value)
            i += 1
            continue

        i += 1
        block: list[str] = []
        while i < len(lines):
            nxt = lines[i]
            if nxt.startswith("  ") or not nxt.strip():
                block.append(nxt)
                i += 1
            else:
                break

        data[key] = parse_indented_block(block)

    return data


def load_objects() -> dict[str, dict[str, Any]]:
    objects: dict[str, dict[str, Any]] = {}
    for object_type, directory in OBJECT_DIRS.items():
        for path in sorted(directory.glob("*.md")):
            frontmatter = parse_frontmatter(extract_frontmatter(read_text(path)))
            object_id = str(frontmatter.get("id", path.stem))
            objects[object_id] = {
                "id": object_id,
                "object_type": object_type,
                "path": path,
                "file_stem": path.stem,
                "frontmatter": frontmatter,
            }
    return objects


def ensure_string_list(value: Any, field_name: str, record_id: str, hard_failures: list[str]) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        hard_failures.append(f"{record_id}: `{field_name}` must be a list of non-empty strings")
        return []
    return [item.strip() for item in value]


def validate_core_fields(
    object_id: str,
    object_type: str,
    file_stem: str,
    frontmatter: dict[str, Any],
    hard_failures: list[str],
) -> None:
    missing = sorted(field for field in REQUIRED_FIELDS if field not in frontmatter)
    if missing:
        hard_failures.append(f"{object_id}: missing required fields: {', '.join(missing)}")

    if frontmatter.get("id") != file_stem:
        hard_failures.append(f"{object_id}: `id` must match filename stem `{file_stem}`")

    if frontmatter.get("object_type") != object_type:
        hard_failures.append(
            f"{object_id}: `object_type` is `{frontmatter.get('object_type')}` but file path requires `{object_type}`"
        )

    prefix = ID_PREFIXES[object_type]
    if not file_stem.startswith(prefix):
        hard_failures.append(f"{object_id}: filename stem `{file_stem}` does not match object family `{object_type}`")

    title = frontmatter.get("title")
    if not isinstance(title, str) or not title.strip():
        hard_failures.append(f"{object_id}: missing non-empty `title`")


def validate_links(
    object_id: str,
    links: Any,
    object_ids: set[str],
    hard_failures: list[str],
    warnings: list[str],
) -> tuple[int, int]:
    if not isinstance(links, list) or not links:
        hard_failures.append(f"{object_id}: `links` must be a non-empty list")
        return 0, 0

    checked = 0
    legacy = 0

    for idx, item in enumerate(links, start=1):
        if not isinstance(item, dict):
            hard_failures.append(f"{object_id}: link #{idx} must be a mapping with `type` and `target`")
            continue

        link_type = item.get("type")
        target = item.get("target")

        if not isinstance(link_type, str) or not link_type.strip():
            hard_failures.append(f"{object_id}: link #{idx} is missing a valid `type`")
            continue
        if not isinstance(target, str) or not target.strip():
            hard_failures.append(f"{object_id}: link #{idx} is missing a valid `target`")
            continue
        if target not in object_ids:
            hard_failures.append(f"{object_id}: link #{idx} points to missing object `{target}`")
            continue

        if link_type in CANONICAL_RELATION_TYPES:
            pass
        elif link_type in LEGACY_RELATION_ALIASES:
            legacy += 1
            warnings.append(
                f"{object_id}: link #{idx} uses legacy relation alias `{link_type}`; migrate toward canonical relation grammar"
            )
        else:
            hard_failures.append(f"{object_id}: link #{idx} uses unknown relation type `{link_type}`")
            continue

        if link_type in SELF_RELATION_TYPES and target == object_id:
            hard_failures.append(f"{object_id}: `{link_type}` cannot target the same object `{object_id}`")

        checked += 1

    return checked, legacy


def resolve_verdict_target(
    object_id: str,
    frontmatter: dict[str, Any],
    object_map: dict[str, dict[str, Any]],
    hard_failures: list[str],
    warnings: list[str],
) -> str | None:
    explicit = frontmatter.get("target_claim_id")
    links = frontmatter.get("links")
    legacy_targets: list[str] = []

    if isinstance(links, list):
        for item in links:
            if isinstance(item, dict) and item.get("type") in RESOLVING_VERDICT_LINK_TYPES:
                target = item.get("target")
                if isinstance(target, str) and target.strip():
                    legacy_targets.append(target.strip())

    if explicit is not None:
        if not isinstance(explicit, str) or not explicit.strip():
            hard_failures.append(f"{object_id}: `target_claim_id` must be a non-empty string when present")
            return None
        target_claim_id = explicit.strip()
        if legacy_targets:
            if len(legacy_targets) != 1 or legacy_targets[0] != target_claim_id:
                hard_failures.append(
                    f"{object_id}: `target_claim_id` and legacy `rules_on` link disagree on verdict target"
                )
            else:
                warnings.append(
                    f"{object_id}: retains legacy `rules_on` link even though `target_claim_id` is present"
                )
    else:
        if not legacy_targets:
            hard_failures.append(f"{object_id}: verdict must declare `target_claim_id` or a temporary resolving `rules_on` link")
            return None
        unique_targets = sorted(set(legacy_targets))
        if len(unique_targets) != 1:
            hard_failures.append(f"{object_id}: verdict resolves to multiple legacy `rules_on` targets: {', '.join(unique_targets)}")
            return None
        target_claim_id = unique_targets[0]
        warnings.append(
            f"{object_id}: verdict target currently inferred through legacy `rules_on` relation; add explicit `target_claim_id`"
        )

    target_obj = object_map.get(target_claim_id)
    if target_obj is None:
        hard_failures.append(f"{object_id}: verdict target `{target_claim_id}` does not resolve to a real object")
        return None
    if target_obj["object_type"] != "claim":
        hard_failures.append(
            f"{object_id}: verdict target `{target_claim_id}` resolves to `{target_obj['object_type']}`, not `claim`"
        )
        return None

    return target_claim_id


def validate_verdict_record(
    object_id: str,
    frontmatter: dict[str, Any],
    object_map: dict[str, dict[str, Any]],
    hard_failures: list[str],
    warnings: list[str],
) -> None:
    verdict_level = frontmatter.get("verdict_level")
    if not isinstance(verdict_level, str) or not verdict_level.strip():
        hard_failures.append(f"{object_id}: missing non-empty `verdict_level`")
        verdict_level = None
    else:
        verdict_level = verdict_level.strip()
        if verdict_level in CANONICAL_VERDICT_LEVELS:
            pass
        elif verdict_level in PILOT_LOCAL_VERDICT_LEVELS:
            warnings.append(
                f"{object_id}: uses pilot-local verdict level `{verdict_level}`; migrate or formally declare extension against compact verdict floor"
            )
        else:
            hard_failures.append(f"{object_id}: unknown `verdict_level` `{verdict_level}`")

    resolve_verdict_target(object_id, frontmatter, object_map, hard_failures, warnings)

    basis_refs = ensure_string_list(frontmatter.get("basis_refs"), "basis_refs", object_id, hard_failures)
    if verdict_level != "under_evaluation" and not basis_refs:
        hard_failures.append(f"{object_id}: nontrivial verdict must declare non-empty `basis_refs`")

    basis_types: list[str] = []
    for basis_id in basis_refs:
        basis_obj = object_map.get(basis_id)
        if basis_obj is None:
            hard_failures.append(f"{object_id}: `basis_refs` points to missing object `{basis_id}`")
            continue
        basis_type = basis_obj["object_type"]
        basis_types.append(basis_type)
        if basis_type not in {"claim", "evidence", "dissent", "verdict"}:
            hard_failures.append(f"{object_id}: `basis_refs` target `{basis_id}` has unsupported type `{basis_type}`")

    if basis_refs and all(basis_type == "verdict" for basis_type in basis_types):
        warnings.append(
            f"{object_id}: verdict basis currently points only to other verdict objects; verify that publication or judgment summaries are not impersonating direct basis"
        )


def validate_records() -> dict[str, int]:
    object_map = load_objects()
    object_ids = set(object_map)

    hard_failures: list[str] = []
    warnings: list[str] = []

    checked_relations = 0
    legacy_relations = 0
    checked_verdicts = 0

    for object_id, obj in sorted(object_map.items()):
        object_type = obj["object_type"]
        frontmatter = obj["frontmatter"]
        file_stem = obj["file_stem"]

        validate_core_fields(object_id, object_type, file_stem, frontmatter, hard_failures)

        relation_count, legacy_count = validate_links(
            object_id,
            frontmatter.get("links"),
            object_ids,
            hard_failures,
            warnings,
        )
        checked_relations += relation_count
        legacy_relations += legacy_count

        if object_type == "verdict":
            checked_verdicts += 1
            validate_verdict_record(object_id, frontmatter, object_map, hard_failures, warnings)

    if hard_failures:
        raise ProtocolRecordConsistencyError("\n".join(hard_failures))

    return {
        "objects_total": len(object_map),
        "claims": sum(1 for obj in object_map.values() if obj["object_type"] == "claim"),
        "evidence": sum(1 for obj in object_map.values() if obj["object_type"] == "evidence"),
        "dissents": sum(1 for obj in object_map.values() if obj["object_type"] == "dissent"),
        "verdicts": checked_verdicts,
        "checked_relations": checked_relations,
        "legacy_relations": legacy_relations,
        "warnings": len(warnings),
        "warning_messages": warnings,
    }


def main() -> None:
    try:
        summary = validate_records()
    except ProtocolRecordConsistencyError as exc:
        print("Protocol record consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    if summary["warning_messages"]:
        print("Protocol record consistency passed with warnings.")
    else:
        print("Protocol record consistency passed.")
    print()
    print(f"- objects total: {summary['objects_total']}")
    print(f"- claims: {summary['claims']}")
    print(f"- evidence: {summary['evidence']}")
    print(f"- dissents: {summary['dissents']}")
    print(f"- verdicts: {summary['verdicts']}")
    print(f"- checked relations: {summary['checked_relations']}")
    print(f"- legacy relations still authored directly: {summary['legacy_relations']}")
    print(f"- warnings: {summary['warnings']}")

    if summary["warning_messages"]:
        print()
        print("Warnings:")
        for warning in summary["warning_messages"]:
            print(f"- {warning}")


if __name__ == "__main__":
    main()
