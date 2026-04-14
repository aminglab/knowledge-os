#!/usr/bin/env python3
"""Validate that snapshot-v0 remains consistent with the current H. pylori case layer."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "h-pylori-ulcer"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v0.md"
REFERENCES_PATH = CASE_ROOT / "references-metadata-v1.md"
OBJECTS_ROOT = CASE_ROOT / "objects"
SOURCES_ROOT = CASE_ROOT / "sources"
CLAIMS_ROOT = CASE_ROOT / "claims"
TIMELINE_PATH = CASE_ROOT / "timeline" / "events.md"
CASE_ENTRY_PATH = CASE_ROOT / "README.md"
CLAIMS_INDEX_PATH = CASE_ROOT / "claims" / "README.md"
REFERENCES_ENTRY_PATH = CASE_ROOT / "references.md"
SOURCES_INDEX_PATH = CASE_ROOT / "sources" / "README.md"

OBJECT_DIRS = {
    "claim": OBJECTS_ROOT / "claims",
    "evidence": OBJECTS_ROOT / "evidence",
    "dissent": OBJECTS_ROOT / "dissents",
    "verdict": OBJECTS_ROOT / "verdicts",
}

SECTION_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REFERENCE_HEADING_RE = re.compile(r"^### `([^`]+)`$", re.M)


class SnapshotConsistencyError(Exception):
    """Raised when snapshot-v0 drifts from the current case layer."""


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
        if all(b.startswith("  - ") and not re.search(r":\s", b[4:]) for b in block):
            data[key] = [parse_scalar(b[4:]) for b in block]
        else:
            data[key] = None
    return data


def load_verdict_levels() -> dict[str, str]:
    verdict_levels: dict[str, str] = {}
    for path in sorted((OBJECTS_ROOT / "verdicts").glob("V-*.md")):
        meta = parse_frontmatter(extract_frontmatter(read_text(path)))
        target_claim_id = str(meta.get("target_claim_id"))
        verdict_level = str(meta.get("verdict_level"))
        verdict_levels[target_claim_id] = verdict_level
    return verdict_levels


def extract_section(markdown: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n\n(.+?)(?:\n---\n|\n## |\Z)"
    match = re.search(pattern, markdown, re.S)
    return match.group(1).strip() if match else ""


def parse_reference_ids(markdown: str) -> set[str]:
    return {match.group(1) for match in REFERENCE_HEADING_RE.finditer(markdown)}


def parse_count(section_text: str, noun: str) -> int | None:
    match = re.search(rf"- (\d+) {re.escape(noun)}", section_text)
    return int(match.group(1)) if match else None


def validate() -> dict[str, int]:
    snapshot_text = read_text(SNAPSHOT_PATH)
    references_text = read_text(REFERENCES_PATH)
    verdict_levels = load_verdict_levels()
    errors: list[str] = []

    current_visible_judgment = extract_section(snapshot_text, "Current visible judgment")
    if verdict_levels.get("C-0001") and verdict_levels["C-0001"] not in current_visible_judgment:
        errors.append(
            f"snapshot-v0: current visible judgment is missing verdict level `{verdict_levels['C-0001']}` for C-0001"
        )
    if verdict_levels.get("C-0002") and verdict_levels["C-0002"] not in current_visible_judgment:
        errors.append(
            f"snapshot-v0: current visible judgment is missing verdict level `{verdict_levels['C-0002']}` for C-0002"
        )

    core_claim = extract_section(snapshot_text, "Core claim neighborhood")
    for claim_id in ["C-0001", "C-0002"]:
        expected_rel = f"../claims/{claim_id}.md"
        if f"[`{claim_id}`]({expected_rel})" not in core_claim:
            errors.append(f"snapshot-v0: core claim neighborhood is missing `{claim_id}` route `{expected_rel}`")
        if not (CLAIMS_ROOT / f"{claim_id}.md").exists():
            errors.append(f"snapshot-v0: expected claim page `{claim_id}.md` does not exist")

    included = extract_section(snapshot_text, "Included objects")
    actual_counts = {
        "claims": len(list((OBJECTS_ROOT / "claims").glob("*.md"))),
        "evidence objects": len(list((OBJECTS_ROOT / "evidence").glob("*.md"))),
        "dissent objects": len(list((OBJECTS_ROOT / "dissents").glob("*.md"))),
        "verdict objects": len(list((OBJECTS_ROOT / "verdicts").glob("*.md"))),
    }
    for noun, actual in actual_counts.items():
        parsed = parse_count(included, noun)
        if parsed is None:
            errors.append(f"snapshot-v0: included objects section is missing count for `{noun}`")
        elif parsed != actual:
            errors.append(f"snapshot-v0: included objects says `{parsed} {noun}` but current case has `{actual}`")

    reading_path = extract_section(snapshot_text, "Snapshot reading path")
    expected_routes = [
        ("../README.md", CASE_ENTRY_PATH),
        ("../claims/README.md", CLAIMS_INDEX_PATH),
        ("../references.md", REFERENCES_ENTRY_PATH),
        ("../sources/README.md", SOURCES_INDEX_PATH),
        ("../timeline/events.md", TIMELINE_PATH),
    ]
    found_routes = set(SECTION_LINK_RE.findall(reading_path))
    if len(found_routes) != len(SECTION_LINK_RE.findall(reading_path)):
        errors.append("snapshot-v0: snapshot reading path contains duplicate links")
    for rel, target in expected_routes:
        if rel not in found_routes:
            errors.append(f"snapshot-v0: snapshot reading path is missing `{rel}`")
        if not target.exists():
            errors.append(f"snapshot-v0: expected reading-path target `{rel}` does not exist")

    honesty = extract_section(snapshot_text, "Current-stage honesty note")
    for phrase in ["stable metadata floor", "source-page index", "first written source pages"]:
        if phrase not in honesty:
            errors.append(f"snapshot-v0: honesty note is missing `{phrase}`")

    reference_ids = parse_reference_ids(references_text)
    source_page_ids = {
        path.stem for path in SOURCES_ROOT.glob("*.md") if path.name != "README.md"
    }
    if reference_ids != source_page_ids:
        missing = sorted(reference_ids - source_page_ids)
        extra = sorted(source_page_ids - reference_ids)
        if missing:
            errors.append("snapshot-v0: canonical source ids without source pages: " + ", ".join(missing))
        if extra:
            errors.append("snapshot-v0: source pages without canonical metadata entries: " + ", ".join(extra))

    if errors:
        raise SnapshotConsistencyError("\n".join(errors))

    return {
        "reading_routes": len(found_routes),
        "claims_in_core_neighborhood": 2,
        "canonical_source_ids": len(reference_ids),
        "source_pages": len(source_page_ids),
    }


def main() -> None:
    try:
        summary = validate()
    except SnapshotConsistencyError as exc:
        print("H. pylori snapshot consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("H. pylori snapshot consistency passed.")
    print()
    print(f"- reading routes checked: {summary['reading_routes']}")
    print(f"- core claim routes checked: {summary['claims_in_core_neighborhood']}")
    print(f"- canonical source ids: {summary['canonical_source_ids']}")
    print(f"- source pages: {summary['source_pages']}")


if __name__ == "__main__":
    main()
