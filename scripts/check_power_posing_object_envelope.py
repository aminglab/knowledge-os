#!/usr/bin/env python3
"""Validate object-envelope conformance for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
OBJECTS_ROOT = CASE_ROOT / "objects"
METADATA_PATH = CASE_ROOT / "references-metadata-v1.md"
ENUMS_PATH = REPO_ROOT / "protocol" / "enums.md"
LINK_TYPES_PATH = REPO_ROOT / "protocol" / "link-types.md"

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

COMMON_ALLOWED_FIELDS = {
    "id",
    "object_type",
    "title",
    "lifecycle_state",
    "epistemic_status",
    "visibility",
    "source_refs",
    "basis_refs",
    "key_facts",
    "links",
}

FAMILY_ALLOWED_FIELDS = {
    "claim": set(),
    "evidence": set(),
    "dissent": {"dissent_kind", "severity"},
    "verdict": {"verdict_level"},
}

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")


class ObjectEnvelopeError(Exception):
    """Raised when object frontmatter drifts from the current working envelope."""


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


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def parse_protocol_values(path: Path, heading: str) -> set[str]:
    section = extract_section(read_text(path), heading)
    return set(re.findall(r"- `([^`]+)`", section))


def parse_metadata_source_ids() -> set[str]:
    markdown = read_text(METADATA_PATH)
    return set(ENTRY_RE.findall("\n" + markdown))


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
                "frontmatter_keys": set(frontmatter),
            }
    return objects


def ensure_string_list(value: Any, field_name: str, object_id: str, errors: list[str]) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{object_id}: `{field_name}` must be a list of non-empty strings")
        return []
    return [item.strip() for item in value]


def validate_links(value: Any, object_id: str, object_ids: set[str], link_types: set[str], errors: list[str]) -> int:
    if not isinstance(value, list) or not value:
        errors.append(f"{object_id}: `links` must be a non-empty list")
        return 0

    count = 0
    for idx, item in enumerate(value, start=1):
        if not isinstance(item, dict):
            errors.append(f"{object_id}: link #{idx} must be a mapping with `type` and `target`")
            continue

        extra_keys = sorted(set(item) - {"type", "target"})
        if extra_keys:
            errors.append(f"{object_id}: link #{idx} contains unsupported keys: {', '.join(extra_keys)}")

        link_type = item.get("type")
        target = item.get("target")

        if not isinstance(link_type, str) or not link_type.strip():
            errors.append(f"{object_id}: link #{idx} is missing a valid `type`")
        elif link_type not in link_types:
            errors.append(f"{object_id}: link #{idx} uses unknown link type `{link_type}`")

        if not isinstance(target, str) or not target.strip():
            errors.append(f"{object_id}: link #{idx} is missing a valid `target`")
        elif target not in object_ids:
            errors.append(f"{object_id}: link #{idx} points to missing object `{target}`")

        count += 1

    return count


def validate_objects() -> dict[str, int]:
    enums = {
        "lifecycle_state": parse_protocol_values(ENUMS_PATH, "lifecycle_state"),
        "epistemic_status": parse_protocol_values(ENUMS_PATH, "epistemic_status"),
        "visibility": parse_protocol_values(ENUMS_PATH, "visibility"),
        "dissent_kind": parse_protocol_values(ENUMS_PATH, "dissent_kind"),
        "severity": parse_protocol_values(ENUMS_PATH, "severity"),
    }
    link_types = parse_protocol_values(LINK_TYPES_PATH, "Current working link types")
    metadata_source_ids = parse_metadata_source_ids()
    objects = load_objects()
    object_ids = set(objects)

    errors: list[str] = []
    source_ref_links = 0
    basis_ref_links = 0
    object_links = 0

    for object_id, obj in sorted(objects.items()):
        object_type = obj["object_type"]
        frontmatter = obj["frontmatter"]
        file_stem = obj["file_stem"]

        allowed_fields = COMMON_ALLOWED_FIELDS | FAMILY_ALLOWED_FIELDS[object_type]
        unknown_fields = sorted(obj["frontmatter_keys"] - allowed_fields)
        if unknown_fields:
            errors.append(f"{object_id}: unsupported frontmatter fields: {', '.join(unknown_fields)}")

        if frontmatter.get("id") != file_stem:
            errors.append(f"{object_id}: `id` must match filename stem `{file_stem}`")
        if not file_stem.startswith(ID_PREFIXES[object_type]):
            errors.append(f"{object_id}: filename stem `{file_stem}` does not match object family `{object_type}`")

        if frontmatter.get("object_type") != object_type:
            errors.append(
                f"{object_id}: `object_type` is `{frontmatter.get('object_type')}` but file path requires `{object_type}`"
            )

        title = frontmatter.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{object_id}: missing non-empty `title`")

        lifecycle_state = frontmatter.get("lifecycle_state")
        if lifecycle_state not in enums["lifecycle_state"]:
            errors.append(f"{object_id}: invalid `lifecycle_state` `{lifecycle_state}`")

        visibility = frontmatter.get("visibility")
        if visibility not in enums["visibility"]:
            errors.append(f"{object_id}: invalid `visibility` `{visibility}`")

        epistemic_status = frontmatter.get("epistemic_status")
        if object_type == "claim":
            if epistemic_status not in enums["epistemic_status"]:
                errors.append(f"{object_id}: invalid or missing `epistemic_status` `{epistemic_status}`")
        elif epistemic_status is not None and epistemic_status not in enums["epistemic_status"]:
            errors.append(f"{object_id}: invalid optional `epistemic_status` `{epistemic_status}`")

        if object_type == "dissent":
            dissent_kind = frontmatter.get("dissent_kind")
            severity = frontmatter.get("severity")
            if dissent_kind not in enums["dissent_kind"]:
                errors.append(f"{object_id}: invalid or missing `dissent_kind` `{dissent_kind}`")
            if severity not in enums["severity"]:
                errors.append(f"{object_id}: invalid or missing `severity` `{severity}`")

        if object_type == "verdict":
            verdict_level = frontmatter.get("verdict_level")
            if not isinstance(verdict_level, str) or not verdict_level.strip():
                errors.append(f"{object_id}: missing non-empty `verdict_level`")

        key_facts = frontmatter.get("key_facts")
        if key_facts is not None and not isinstance(key_facts, dict):
            errors.append(f"{object_id}: `key_facts` must be a mapping when present")

        source_refs = ensure_string_list(frontmatter.get("source_refs"), "source_refs", object_id, errors)
        if object_type in {"claim", "evidence", "dissent"} and not source_refs:
            errors.append(f"{object_id}: `{object_type}` objects must declare non-empty `source_refs` in the current pilot")
        if len(source_refs) != len(set(source_refs)):
            errors.append(f"{object_id}: `source_refs` contains duplicate source ids")
        for source_id in source_refs:
            if source_id not in metadata_source_ids:
                errors.append(f"{object_id}: `source_refs` contains undefined source id `{source_id}`")
        source_ref_links += len(source_refs)

        basis_refs = ensure_string_list(frontmatter.get("basis_refs"), "basis_refs", object_id, errors)
        if object_type == "verdict" and not basis_refs:
            errors.append(f"{object_id}: `verdict` objects must declare non-empty `basis_refs`")
        if len(basis_refs) != len(set(basis_refs)):
            errors.append(f"{object_id}: `basis_refs` contains duplicate object ids")
        for basis_id in basis_refs:
            if basis_id not in object_ids:
                errors.append(f"{object_id}: `basis_refs` points to missing object `{basis_id}`")
        basis_ref_links += len(basis_refs)

        object_links += validate_links(frontmatter.get("links"), object_id, object_ids, link_types, errors)

    if errors:
        raise ObjectEnvelopeError("\n".join(errors))

    return {
        "objects_total": len(objects),
        "claims": sum(1 for obj in objects.values() if obj["object_type"] == "claim"),
        "evidence": sum(1 for obj in objects.values() if obj["object_type"] == "evidence"),
        "dissents": sum(1 for obj in objects.values() if obj["object_type"] == "dissent"),
        "verdicts": sum(1 for obj in objects.values() if obj["object_type"] == "verdict"),
        "source_ref_links": source_ref_links,
        "basis_ref_links": basis_ref_links,
        "object_links": object_links,
    }


def main() -> None:
    try:
        summary = validate_objects()
    except ObjectEnvelopeError as exc:
        print("Object envelope conformance failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Object envelope conformance passed.")
    print()
    print(f"- objects total: {summary['objects_total']}")
    print(f"- claims: {summary['claims']}")
    print(f"- evidence: {summary['evidence']}")
    print(f"- dissents: {summary['dissents']}")
    print(f"- verdicts: {summary['verdicts']}")
    print(f"- source-ref links: {summary['source_ref_links']}")
    print(f"- basis-ref links: {summary['basis_ref_links']}")
    print(f"- object links: {summary['object_links']}")


if __name__ == "__main__":
    main()
