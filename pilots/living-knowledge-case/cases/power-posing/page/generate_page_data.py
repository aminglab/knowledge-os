#!/usr/bin/env python3
"""Generate page-data.js for the power-posing page prototype.

This script is intentionally small and case-scoped.
It is the first automation step between:

- governed markdown object files,
- snapshot markdown,
- and the public page prototype.

It does not attempt to be a universal Knowledge OS compiler.
It only proves that page data can be derived from the current case layer
rather than written entirely by hand.

Usage:
    python generate_page_data.py
    python generate_page_data.py --check
    python generate_page_data.py --json-summary
    python generate_page_data.py --check --json-summary

It rewrites:
    ./page-data.js
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
CASE_ROOT = ROOT.parent
OBJECTS_ROOT = CASE_ROOT / "objects"
CLAIMS_ROOT = CASE_ROOT / "claims"
SOURCES_ROOT = CASE_ROOT / "sources"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
TIMELINE_PATH = CASE_ROOT / "timeline" / "events.md"
REFERENCES_PATH = CASE_ROOT / "references-metadata-v1.md"
OUTPUT_PATH = ROOT / "page-data.js"
SCHEMA_NAME = "power_posing_json_summary"
SCHEMA_VERSION = "v2"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

REQUIRED_FIELDS = {
    "*": ["id", "object_type", "title", "lifecycle_state", "visibility", "links"],
    "claim": ["epistemic_status"],
    "dissent": ["dissent_kind", "severity"],
    "verdict": ["verdict_level"],
}


class ValidationError(Exception):
    """Raised when the current case layer fails generator validation."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate or validate page-data.js for the power-posing page prototype."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate and summarize the current release surface without writing page-data.js.",
    )
    parser.add_argument(
        "--json-summary",
        action="store_true",
        help="Emit a machine-readable JSON summary instead of human-readable terminal output.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_frontmatter_and_body(text: str) -> tuple[list[str], str]:
    if not text.startswith("---\n"):
        return [], text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return [], text
    frontmatter = parts[0].splitlines()[1:]
    body = parts[1]
    return frontmatter, body


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


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

        block = [b for b in block if b.strip()]
        if not block:
            data[key] = None
            continue

        if all(b.startswith("  - ") and not re.search(r":\s", b[4:]) for b in block):
            data[key] = [parse_scalar(b[4:]) for b in block]
            continue

        if all(b.startswith("  ") and not b.startswith("  - ") for b in block):
            mapping: dict[str, Any] = {}
            for b in block:
                m = re.match(r"^  ([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", b)
                if m:
                    mapping[m.group(1)] = parse_scalar(m.group(2))
            data[key] = mapping
            continue

        if all(b.startswith("  - ") or b.startswith("    ") for b in block):
            items: list[dict[str, Any]] = []
            current: dict[str, Any] | None = None
            for b in block:
                first = re.match(r"^  - ([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", b)
                nested = re.match(r"^    ([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", b)
                if first:
                    current = {first.group(1): parse_scalar(first.group(2))}
                    items.append(current)
                elif nested and current is not None:
                    current[nested.group(1)] = parse_scalar(nested.group(2))
            data[key] = items
            continue

        data[key] = [b.strip() for b in block]

    return data


def extract_summary(body: str) -> str:
    match = re.search(r"## Summary\n\n(.+?)(?:\n\n## |\Z)", body, re.S)
    if match:
        return " ".join(line.strip() for line in match.group(1).strip().splitlines())
    paragraphs = [p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith("#")]
    return paragraphs[0] if paragraphs else ""


def load_objects() -> dict[str, dict[str, Any]]:
    objects: dict[str, dict[str, Any]] = {}
    for object_type, directory in OBJECT_DIRS.items():
        for path in sorted(directory.glob("*.md")):
            text = read_text(path)
            frontmatter_lines, body = extract_frontmatter_and_body(text)
            meta = parse_frontmatter(frontmatter_lines)
            meta["object_type"] = meta.get("object_type", object_type)
            meta["summary"] = extract_summary(body)
            rel_path = path.relative_to(CASE_ROOT).as_posix()
            meta["href"] = f"../{rel_path}"
            object_id = str(meta.get("id", path.stem))
            objects[object_id] = meta
    return objects


def section_text(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    if not match:
        return ""
    return "\n\n".join(chunk.strip() for chunk in match.group(1).strip().split("\n\n") if chunk.strip())


def section_intro(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n### |\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    if not match:
        return ""
    block = match.group(1).strip()
    paragraphs = []
    for chunk in block.split("\n\n"):
        chunk = chunk.strip()
        if not chunk or chunk.startswith("- "):
            break
        if "\n- " in chunk:
            chunk = chunk.split("\n- ", 1)[0].strip()
        paragraphs.append(" ".join(chunk.splitlines()))
    return " ".join(paragraphs).strip()


def extract_snapshot_title(markdown: str) -> str:
    match = re.search(r"\*\*(.+?)\*\*", markdown)
    return match.group(1) if match else "Power Posing"


def extract_state_block(markdown: str, label: str) -> tuple[str, str]:
    pattern = rf"### {re.escape(label)}\n\*\*Current state:\*\* (.+?)\n\n(.+?)(?:\n### |\n---\n|\Z)"
    match = re.search(pattern, markdown, re.S)
    if not match:
        fallback = re.search(rf"### {re.escape(label)}\n\*\*Status:\*\* (.+?)\n\n(.+?)(?:\n### |\n---\n|\Z)", markdown, re.S)
        if fallback:
            return fallback.group(1).strip(), " ".join(fallback.group(2).strip().splitlines())
        return "", ""
    status = match.group(1).strip()
    summary = " ".join(match.group(2).strip().splitlines())
    return status, summary


def source_anchor(source_id: str) -> str:
    anchor = source_id.strip().lower()
    anchor = anchor.replace("`", "")
    anchor = re.sub(r"\s+", "-", anchor)
    anchor = re.sub(r"[^a-z0-9_\-]", "", anchor)
    return anchor


def clean_inline_markdown(text: str) -> str:
    text = text.strip()
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)
    return text


def extract_metadata_value(block: str, label: str) -> str:
    match = re.search(rf"- {re.escape(label)}: (.+)", block)
    return clean_inline_markdown(match.group(1)) if match else ""


def claim_page_path(claim_id: str) -> Path:
    return CLAIMS_ROOT / f"{claim_id}.md"


def claim_page_href(claim_id: str) -> str:
    return f"../claims/{claim_id}.md"


def source_page_path(source_id: str) -> Path:
    return SOURCES_ROOT / f"{source_id}.md"


def source_page_href(source_id: str) -> str:
    return f"../sources/{source_id}.md"


def parse_references(markdown: str) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    parts = re.split(r"\n### `([^`]+)`\n", markdown)
    for i in range(1, len(parts), 2):
        source_id = parts[i]
        block = parts[i + 1]
        usage = extract_metadata_value(block, "Object usage")
        usage_ids = re.findall(r"`([^`]+)`", block)
        entries.append(
            {
                "id": source_id,
                "source_type": extract_metadata_value(block, "Source type"),
                "title": extract_metadata_value(block, "Title"),
                "year": extract_metadata_value(block, "Year"),
                "locator": extract_metadata_value(block, "Canonical locator"),
                "role": extract_metadata_value(block, "Role in case"),
                "usage": usage,
                "usage_ids": usage_ids,
                "href": f"../references-metadata-v1.md#{source_anchor(source_id)}",
                "page_href": source_page_href(source_id),
            }
        )
    return entries


def parse_timeline(markdown: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    heading_pattern = re.compile(r"^### (.+)$", re.M)
    matches = list(heading_pattern.finditer(markdown))

    for index, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        block = markdown[start:end]
        bullets = [line[2:].strip() for line in block.splitlines() if line.startswith("- ")]
        body = " ".join(bullets)

        if " — " in heading:
            year, title = heading.split(" — ", 1)
        else:
            year, title = "", heading

        items.append({"year": year.strip(), "title": title.strip(), "body": body})
    return items


def make_link(label: str, href: str) -> dict[str, str]:
    return {"label": label, "href": href}


def canonical_source_ids(reference_entries: list[dict[str, Any]]) -> set[str]:
    return {entry["id"] for entry in reference_entries if entry.get("id")}


def count_objects_by_type(objects: dict[str, dict[str, Any]]) -> dict[str, int]:
    counts = {"claim": 0, "evidence": 0, "dissent": 0, "verdict": 0}
    for obj in objects.values():
        object_type = str(obj.get("object_type", "unknown"))
        counts[object_type] = counts.get(object_type, 0) + 1
    return counts


def validate_objects(objects: dict[str, dict[str, Any]], source_ids: set[str]) -> None:
    errors: list[str] = []

    for object_id, obj in sorted(objects.items()):
        object_type = str(obj.get("object_type", ""))
        required_fields = REQUIRED_FIELDS["*"] + REQUIRED_FIELDS.get(object_type, [])

        for field in required_fields:
            value = obj.get(field)
            missing = value is None or value == "" or value == []
            if missing:
                errors.append(f"{object_id}: missing required field `{field}`")

        for source_ref in obj.get("source_refs", []):
            if source_ref not in source_ids:
                errors.append(f"{object_id}: undefined source_ref `{source_ref}`")

        for basis_ref in obj.get("basis_refs", []):
            if basis_ref not in objects:
                errors.append(f"{object_id}: basis_ref `{basis_ref}` points to a missing object")

        links = obj.get("links", [])
        if isinstance(links, list):
            for position, link in enumerate(links, start=1):
                link_type = link.get("type") if isinstance(link, dict) else None
                target = link.get("target") if isinstance(link, dict) else None
                if not link_type:
                    errors.append(f"{object_id}: link #{position} is missing `type`")
                if not target:
                    errors.append(f"{object_id}: link #{position} is missing `target`")
                elif target not in objects:
                    errors.append(f"{object_id}: link #{position} points to missing target `{target}`")
        else:
            errors.append(f"{object_id}: `links` must be a list")

    if errors:
        raise ValidationError("\n".join(errors))


def validate_snapshot_contract(snapshot_text: str) -> None:
    required_headings = [
        "## What this page is",
        "## Current visible judgment",
        "### Original claim",
        "### Descendant claim",
        "## Why this case matters",
    ]
    missing = [heading for heading in required_headings if heading not in snapshot_text]
    if missing:
        formatted = ", ".join(missing)
        raise ValidationError(f"snapshot-v2.md is missing required section(s): {formatted}")


def validate_public_seed_layers(objects: dict[str, dict[str, Any]], reference_entries: list[dict[str, Any]]) -> None:
    errors: list[str] = []

    if not (CLAIMS_ROOT / "README.md").exists():
        errors.append("claims/README.md is missing")
    if not (SOURCES_ROOT / "README.md").exists():
        errors.append("sources/README.md is missing")

    for object_id, obj in sorted(objects.items()):
        if obj.get("object_type") == "claim":
            path = claim_page_path(object_id)
            if not path.exists():
                errors.append(f"{object_id}: missing public claim page `{path.relative_to(CASE_ROOT).as_posix()}`")

    for entry in reference_entries:
        source_id = entry["id"]
        path = source_page_path(source_id)
        if not path.exists():
            errors.append(f"{source_id}: missing public source page `{path.relative_to(CASE_ROOT).as_posix()}`")

    if errors:
        raise ValidationError("\n".join(errors))


def build_status_cards(objects: dict[str, dict[str, Any]], snapshot_text: str) -> list[dict[str, Any]]:
    original_status, original_summary = extract_state_block(snapshot_text, "Original claim")
    descendant_status, descendant_summary = extract_state_block(snapshot_text, "Descendant claim")

    c1 = objects["C-0001"]
    v1 = objects["V-0001"]
    e1 = objects["E-0001"]
    c2 = objects["C-0002"]
    v2 = objects["V-0002"]

    return [
        {
            "title": "Original claim",
            "status": original_status,
            "summary": original_summary,
            "badges": ["claim", c1["id"], v1["id"]],
            "links": [
                make_link(f"Open claim page {c1['id']}", claim_page_href(c1["id"])),
                make_link(f"Open verdict {v1['id']}", v1["href"]),
                make_link(f"Open evidence {e1['id']}", e1["href"]),
            ],
        },
        {
            "title": "Descendant claim",
            "status": descendant_status,
            "summary": descendant_summary,
            "badges": ["claim", c2["id"], v2["id"]],
            "links": [
                make_link(f"Open claim page {c2['id']}", claim_page_href(c2["id"])),
                make_link(f"Open verdict {v2['id']}", v2["href"]),
            ],
        },
    ]


def build_neighborhood_cards(objects: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    ids = ["E-0001", "D-0001", "D-0002", "D-0003", "C-0002", "V-0001", "V-0002"]
    cards: list[dict[str, Any]] = []
    for object_id in ids:
        obj = objects[object_id]
        kind = "dissent" if obj["object_type"] == "dissent" else "status"
        if obj["object_type"] == "evidence":
            kind = "support"
        badges = [obj["id"]]
        if "source_refs" in obj:
            badges.extend(obj["source_refs"][:2])

        object_link_href = claim_page_href(object_id) if obj["object_type"] == "claim" else obj["href"]
        label_prefix = "Open claim page" if obj["object_type"] == "claim" else "Open"

        cards.append(
            {
                "title": obj["title"],
                "kind": kind,
                "body": obj["summary"],
                "badges": badges,
                "links": [make_link(f"{label_prefix} {obj['id']}", object_link_href)],
            }
        )
    return cards


def build_public_route_cards(objects: dict[str, dict[str, Any]], reference_entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    claim_count = sum(1 for obj in objects.values() if obj.get("object_type") == "claim")
    source_count = len(reference_entries)
    return [
        {
            "title": "Claim pages",
            "kind": "status",
            "body": "The case now has public claim pages for both the original strong-form claim and the weaker descendant claim. These pages localize standing, support, challenge, and lineage without turning the case page into a full graph browser.",
            "badges": ["claims", f"{claim_count} public claim pages"],
            "links": [
                make_link("Open claim index", "../claims/README.md"),
                make_link("Open claim C-0001", claim_page_href("C-0001")),
                make_link("Open claim C-0002", claim_page_href("C-0002")),
            ],
        },
        {
            "title": "Source pages",
            "kind": "support",
            "body": "The case now has a first public source-page layer. It makes canonical sources readable as participants in the living case rather than leaving source grounding trapped inside metadata and case cards.",
            "badges": ["sources", f"{source_count} public source pages"],
            "links": [
                make_link("Open source index", "../sources/README.md"),
                make_link("Open source Carney_Cuddy_Yap_2010", source_page_href("Carney_Cuddy_Yap_2010")),
                make_link("Open source Dana_Carney_2016_statement", source_page_href("Dana_Carney_2016_statement")),
            ],
        },
    ]


def build_source_cards(reference_entries: list[dict[str, Any]], objects: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for entry in reference_entries:
        usage_links = []
        for object_id in entry.get("usage_ids", []):
            if object_id not in objects:
                continue
            obj = objects[object_id]
            href = claim_page_href(object_id) if obj.get("object_type") == "claim" else obj["href"]
            label = f"Open claim page {object_id}" if obj.get("object_type") == "claim" else f"Open {object_id}"
            usage_links.append(make_link(label, href))

        links = [
            make_link("Open source page", entry["page_href"]),
            make_link("Open source metadata", entry["href"]),
        ]
        links.extend(usage_links)
        badges = [entry["id"]]
        if entry.get("source_type"):
            badges.append(entry["source_type"])
        if entry.get("year"):
            badges.append(entry["year"])

        cards.append(
            {
                "id": entry["id"],
                "title": entry.get("title", ""),
                "role": entry.get("role", ""),
                "locator": entry.get("locator", ""),
                "usage": entry.get("usage", ""),
                "badges": badges,
                "links": links,
            }
        )
    return cards


def build_page_data() -> tuple[dict[str, Any], dict[str, dict[str, Any]], list[dict[str, Any]]]:
    snapshot_text = read_text(SNAPSHOT_PATH)
    references_text = read_text(REFERENCES_PATH)
    timeline_text = read_text(TIMELINE_PATH)
    reference_entries = parse_references(references_text)
    source_ids = canonical_source_ids(reference_entries)
    objects = load_objects()

    validate_snapshot_contract(snapshot_text)
    validate_objects(objects, source_ids)
    validate_public_seed_layers(objects, reference_entries)

    title = extract_snapshot_title(snapshot_text)
    what_this_page_is_intro = section_intro(snapshot_text, "What this page is")
    why_case_matters = section_text(snapshot_text, "Why this case matters")
    current_visible_judgment_intro = section_intro(snapshot_text, "Current visible judgment")

    data = {
        "title": title,
        "shortTitle": "Power Posing",
        "description": what_this_page_is_intro,
        "links": [
            make_link("Snapshot v2", "../snapshots/snapshot-v2.md"),
            make_link("Claim pages", "../claims/README.md"),
            make_link("Source pages", "../sources/README.md"),
            make_link("Case overview", "../case.md"),
            make_link("References", "../references.md"),
            make_link("Timeline", "../timeline/events.md"),
        ],
        "judgmentIntro": current_visible_judgment_intro,
        "judgmentLinks": [
            make_link("Status legend", "../status-legend-v1.md"),
            make_link("Verdict grammar", "../verdict-grammar-v1.md"),
        ],
        "statusCards": build_status_cards(objects, snapshot_text),
        "sections": [
            {
                "title": "Why this case matters",
                "intro": " ".join(why_case_matters.splitlines()),
                "cards": [
                    {
                        "title": "The structural problem",
                        "kind": "status",
                        "body": "The publication persists, but the knowledge status changed. A living knowledge system should keep those changes attached to the claim lineage itself.",
                    },
                    {
                        "title": "Object neighborhoods",
                        "kind": "support",
                        "body": "This page keeps the object model visible instead of flattening the case into anonymous prose.",
                    },
                ],
            },
            {
                "title": "Current object neighborhoods",
                "intro": "These cards are derived from current object frontmatter plus each object's summary section.",
                "cards": build_neighborhood_cards(objects),
            },
            {
                "title": "Public claim and source routes",
                "intro": "The page now sits inside a richer public-layer ecology. These cards route into the seeded claim-page and source-page layers without replacing Snapshot v2 as the fuller release view.",
                "cards": build_public_route_cards(objects, reference_entries),
            },
        ],
        "timeline": parse_timeline(timeline_text),
        "sources": build_source_cards(reference_entries, objects),
        "readingPathIntro": "This page keeps a deliberately thinner downstream reading path than snapshot-v2. Start with Snapshot v2 if you want the fuller governance-backed route; use the links below for the shortest path into the seeded claim-page and source-page layers, verdicts, timeline, and references.",
        "readingPath": [
            make_link("Snapshot v2", "../snapshots/snapshot-v2.md"),
            make_link("Claim pages", "../claims/README.md"),
            make_link("Claim C-0001", claim_page_href("C-0001")),
            make_link("Claim C-0002", claim_page_href("C-0002")),
            make_link("Source pages", "../sources/README.md"),
            make_link("Verdict V-0001", objects["V-0001"]["href"]),
            make_link("Verdict V-0002", objects["V-0002"]["href"]),
            make_link("Timeline", "../timeline/events.md"),
            make_link("References", "../references.md"),
        ],
        "footer": {
            "eyebrow": "Knowledge OS · First live case page",
            "title": "A governed public case page carried in main",
            "body": "This page is the first live public case page currently carried in the repository main line. It stays downstream of Snapshot v2, and it now acknowledges the seeded claim-page and source-page layers growing around the case rather than treating the case as one flat surface.",
            "badges": [
                "first live case page",
                "snapshot-v2 upstream",
                "downstream release surface",
                "claims+sources integrated",
            ],
            "links": [
                make_link("Open Snapshot v2", "../snapshots/snapshot-v2.md"),
                make_link("Open claim pages", "../claims/README.md"),
                make_link("Open source pages", "../sources/README.md"),
                make_link("Open references", "../references.md"),
            ],
        },
    }
    return data, objects, reference_entries


def write_output(data: dict[str, Any]) -> None:
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    content = (
        "// This file is generated by generate_page_data.py.\n"
        "// Edit object files, snapshot-v2.md, or references-metadata-v1.md, then re-run the generator.\n"
        "// The generator now performs minimal validation before writing this file.\n\n"
        f"window.POWER_POSING_PAGE_DATA = {payload};\n"
    )
    OUTPUT_PATH.write_text(content, encoding="utf-8")


def build_release_summary(objects: dict[str, dict[str, Any]], reference_entries: list[dict[str, Any]], data: dict[str, Any]) -> dict[str, Any]:
    counts = count_objects_by_type(objects)
    neighborhood_cards = 0
    public_route_cards = 0
    for section in data.get("sections", []):
        if section.get("title") == "Current object neighborhoods":
            neighborhood_cards = len(section.get("cards", []))
        if section.get("title") == "Public claim and source routes":
            public_route_cards = len(section.get("cards", []))

    return {
        "objects_total": len(objects),
        "claims": counts.get("claim", 0),
        "evidence_objects": counts.get("evidence", 0),
        "dissents": counts.get("dissent", 0),
        "verdicts": counts.get("verdict", 0),
        "canonical_source_ids": len(reference_entries),
        "claim_page_count": counts.get("claim", 0),
        "source_page_count": len(reference_entries),
        "status_cards": len(data.get("statusCards", [])),
        "neighborhood_cards": neighborhood_cards,
        "public_route_cards": public_route_cards,
        "timeline_entries": len(data.get("timeline", [])),
        "reading_path_links": len(data.get("readingPath", [])),
    }


def build_json_summary_base(check_mode: bool) -> dict[str, Any]:
    return {
        "schema_name": SCHEMA_NAME,
        "schema_version": SCHEMA_VERSION,
        "check_mode": check_mode,
    }


def print_validation_passed() -> None:
    print("Validation passed.")


def print_release_summary(summary: dict[str, Any]) -> None:
    print("Release summary:")
    print(f"- objects: {summary['objects_total']} total")
    print(f"- claims: {summary['claims']}")
    print(f"- evidence objects: {summary['evidence_objects']}")
    print(f"- dissents: {summary['dissents']}")
    print(f"- verdicts: {summary['verdicts']}")
    print(f"- canonical source ids: {summary['canonical_source_ids']}")
    print(f"- claim pages: {summary['claim_page_count']}")
    print(f"- source pages: {summary['source_page_count']}")
    print(f"- status cards: {summary['status_cards']}")
    print(f"- neighborhood cards: {summary['neighborhood_cards']}")
    print(f"- public-route cards: {summary['public_route_cards']}")
    print(f"- timeline entries: {summary['timeline_entries']}")
    print(f"- reading-path links: {summary['reading_path_links']}")


def print_write_status(check_mode: bool) -> None:
    if check_mode:
        print("Write skipped (--check).")
    else:
        print(f"Write completed: {OUTPUT_PATH}")


def emit_json_summary(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def main() -> None:
    args = parse_args()

    try:
        data, objects, reference_entries = build_page_data()
        if not args.check:
            write_output(data)
    except ValidationError as exc:
        errors = [line for line in str(exc).splitlines() if line.strip()]
        failure_payload = {
            **build_json_summary_base(args.check),
            "validation_status": "failed",
            "write_status": "skipped_due_to_validation_failure",
            "output_path": None,
            "errors": errors,
        }
        if args.json_summary:
            emit_json_summary(failure_payload)
        else:
            print("Validation failed.", file=sys.stderr)
            print(file=sys.stderr)
            for line in errors:
                print(line, file=sys.stderr)
            print(file=sys.stderr)
            print("Write skipped due to validation failure.", file=sys.stderr)
        raise SystemExit(1) from exc

    release_summary = build_release_summary(objects, reference_entries, data)
    output_path = None if args.check else str(OUTPUT_PATH)
    success_payload = {
        **build_json_summary_base(args.check),
        "validation_status": "passed",
        "write_status": "skipped" if args.check else "completed",
        "output_path": output_path,
        "release_summary": release_summary,
    }

    if args.json_summary:
        emit_json_summary(success_payload)
    else:
        print_validation_passed()
        print()
        print_release_summary(release_summary)
        print()
        print_write_status(args.check)


if __name__ == "__main__":
    main()
