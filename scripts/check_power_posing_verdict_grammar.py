#!/usr/bin/env python3
"""Validate verdict grammar consistency for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
GRAMMAR_PATH = CASE_ROOT / "verdict-grammar-v1.md"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"
OBJECTS_ROOT = CASE_ROOT / "objects"

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")
REQUIRED_FIELDS = [
    "Claim id",
    "Verdict id",
    "Snapshot label",
    "Snapshot current state",
    "Required claim epistemic status",
    "Required verdict level",
    "Required verdict anchors",
]


class VerdictGrammarError(Exception):
    """Raised when verdict grammar drifts from the current case layer."""


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


def load_markdown_object(path: Path) -> tuple[dict[str, Any], str]:
    text = read_text(path)
    frontmatter = parse_frontmatter(extract_frontmatter(text))
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    return frontmatter, body


def parse_entries(markdown: str) -> dict[str, dict[str, str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, dict[str, str]] = {}
    for i in range(1, len(parts), 2):
        entry_id = parts[i]
        block = parts[i + 1]
        fields: dict[str, str] = {}
        for field in REQUIRED_FIELDS:
            match = re.search(rf"^- {re.escape(field)}: (.+)$", block, re.M)
            if match:
                fields[field] = match.group(1).strip()
        entries[entry_id] = fields
    return entries


def extract_snapshot_state(snapshot_text: str, label: str) -> str:
    pattern = rf"### {re.escape(label)}\n\*\*Current state:\*\* (.+?)\n"
    match = re.search(pattern, snapshot_text)
    return match.group(1).strip() if match else ""


def parse_anchor_list(value: str) -> list[str]:
    return [part.strip().strip('`') for part in value.split(",") if part.strip()]


def validate() -> dict[str, int]:
    grammar_text = read_text(GRAMMAR_PATH)
    snapshot_text = read_text(SNAPSHOT_PATH)
    entries = parse_entries(grammar_text)

    errors: list[str] = []

    if not entries:
        errors.append("verdict-grammar-v1.md contains no parseable grammar entries")

    for entry_id, fields in sorted(entries.items()):
        for field in REQUIRED_FIELDS:
            if not fields.get(field):
                errors.append(f"{entry_id}: missing required field `{field}`")

        claim_id = re.search(r"`([A-Z]-\d{4})`", fields.get("Claim id", "") or "")
        verdict_id = re.search(r"`([A-Z]-\d{4})`", fields.get("Verdict id", "") or "")
        snapshot_label = fields.get("Snapshot label", "")
        snapshot_state = fields.get("Snapshot current state", "")
        required_claim_status = re.search(r"`([^`]+)`", fields.get("Required claim epistemic status", "") or "")
        required_verdict_level = re.search(r"`([^`]+)`", fields.get("Required verdict level", "") or "")
        anchors = parse_anchor_list(fields.get("Required verdict anchors", ""))

        if not claim_id or not verdict_id or not required_claim_status or not required_verdict_level:
            continue

        claim_path = CASE_ROOT / "objects" / "claims" / f"{claim_id.group(1)}.md"
        verdict_path = CASE_ROOT / "objects" / "verdicts" / f"{verdict_id.group(1)}.md"
        if not claim_path.exists():
            errors.append(f"{entry_id}: missing claim object `{claim_id.group(1)}`")
            continue
        if not verdict_path.exists():
            errors.append(f"{entry_id}: missing verdict object `{verdict_id.group(1)}`")
            continue

        claim_meta, _ = load_markdown_object(claim_path)
        verdict_meta, verdict_body = load_markdown_object(verdict_path)

        actual_snapshot_state = extract_snapshot_state(snapshot_text, snapshot_label)
        if actual_snapshot_state != snapshot_state:
            errors.append(
                f"{entry_id}: snapshot state mismatch for `{snapshot_label}`; found `{actual_snapshot_state}` but expected `{snapshot_state}`"
            )

        if claim_meta.get("epistemic_status") != required_claim_status.group(1):
            errors.append(
                f"{entry_id}: claim `{claim_id.group(1)}` has epistemic_status `{claim_meta.get('epistemic_status')}` but expected `{required_claim_status.group(1)}`"
            )

        if verdict_meta.get("verdict_level") != required_verdict_level.group(1):
            errors.append(
                f"{entry_id}: verdict `{verdict_id.group(1)}` has verdict_level `{verdict_meta.get('verdict_level')}` but expected `{required_verdict_level.group(1)}`"
            )

        verdict_text_lower = verdict_body.lower()
        for anchor in anchors:
            if anchor.lower() not in verdict_text_lower:
                errors.append(
                    f"{entry_id}: verdict `{verdict_id.group(1)}` body is missing required anchor `{anchor}`"
                )

    if errors:
        raise VerdictGrammarError("\n".join(errors))

    return {
        "grammar_entries": len(entries),
        "snapshot_states_checked": len(entries),
    }


def main() -> None:
    try:
        summary = validate()
    except VerdictGrammarError as exc:
        print("Verdict grammar consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Verdict grammar consistency passed.")
    print()
    print(f"- grammar entries: {summary['grammar_entries']}")
    print(f"- snapshot states checked: {summary['snapshot_states_checked']}")


if __name__ == "__main__":
    main()
