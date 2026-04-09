#!/usr/bin/env python3
"""Validate status legend consistency for the power-posing pilot."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CASE_ROOT = REPO_ROOT / "pilots" / "living-knowledge-case" / "cases" / "power-posing"
LEGEND_PATH = CASE_ROOT / "status-legend-v1.md"
GRAMMAR_PATH = CASE_ROOT / "verdict-grammar-v1.md"
SNAPSHOT_PATH = CASE_ROOT / "snapshots" / "snapshot-v2.md"

ENTRY_RE = re.compile(r"\n### `([^`]+)`\n")
LEGEND_REQUIRED_FIELDS = [
    "Public wording",
    "Snapshot label",
    "Claim id",
    "Verdict id",
    "Governing verdict level",
    "Governing claim epistemic status",
    "Reader meaning",
]
GRAMMAR_REQUIRED_FIELDS = [
    "Claim id",
    "Verdict id",
    "Snapshot label",
    "Snapshot current state",
    "Required claim epistemic status",
    "Required verdict level",
    "Required verdict anchors",
]


class StatusLegendError(Exception):
    """Raised when the public status legend drifts from the current case layer."""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_entries(markdown: str, required_fields: list[str]) -> dict[str, dict[str, str]]:
    parts = ENTRY_RE.split("\n" + markdown)
    entries: dict[str, dict[str, str]] = {}
    for i in range(1, len(parts), 2):
        entry_id = parts[i]
        block = parts[i + 1]
        fields: dict[str, str] = {}
        for field in required_fields:
            match = re.search(rf"^- {re.escape(field)}: (.+)$", block, re.M)
            if match:
                fields[field] = match.group(1).strip()
        entries[entry_id] = fields
    return entries


def extract_snapshot_state(snapshot_text: str, label: str) -> str:
    pattern = rf"### {re.escape(label)}\n\*\*Current state:\*\* (.+?)\n"
    match = re.search(pattern, snapshot_text)
    return match.group(1).strip() if match else ""


def lookup_grammar_entry(grammar_entries: dict[str, dict[str, str]], label: str) -> tuple[str, dict[str, str]] | tuple[None, None]:
    for entry_id, fields in grammar_entries.items():
        if fields.get("Snapshot label", "") == f"`{label}`":
            return entry_id, fields
    return None, None


def validate() -> dict[str, int]:
    legend_text = read_text(LEGEND_PATH)
    grammar_text = read_text(GRAMMAR_PATH)
    snapshot_text = read_text(SNAPSHOT_PATH)

    legend_entries = parse_entries(legend_text, LEGEND_REQUIRED_FIELDS)
    grammar_entries = parse_entries(grammar_text, GRAMMAR_REQUIRED_FIELDS)

    errors: list[str] = []

    if not legend_entries:
        errors.append("status-legend-v1.md contains no parseable status entries")

    for entry_id, fields in sorted(legend_entries.items()):
        for field in LEGEND_REQUIRED_FIELDS:
            if not fields.get(field):
                errors.append(f"{entry_id}: missing required field `{field}`")

        public_wording = re.search(r"`([^`]+)`", fields.get("Public wording", "") or "")
        snapshot_label = re.search(r"`([^`]+)`", fields.get("Snapshot label", "") or "")
        claim_id = re.search(r"`([A-Z]-\d{4})`", fields.get("Claim id", "") or "")
        verdict_id = re.search(r"`([A-Z]-\d{4})`", fields.get("Verdict id", "") or "")
        verdict_level = re.search(r"`([^`]+)`", fields.get("Governing verdict level", "") or "")
        claim_status = re.search(r"`([^`]+)`", fields.get("Governing claim epistemic status", "") or "")

        if not public_wording or not snapshot_label or not claim_id or not verdict_id or not verdict_level or not claim_status:
            continue

        actual_snapshot_state = extract_snapshot_state(snapshot_text, snapshot_label.group(1))
        if actual_snapshot_state != public_wording.group(1):
            errors.append(
                f"{entry_id}: snapshot wording mismatch for `{snapshot_label.group(1)}`; found `{actual_snapshot_state}` but expected `{public_wording.group(1)}`"
            )

        grammar_entry_id, grammar_fields = lookup_grammar_entry(grammar_entries, snapshot_label.group(1))
        if not grammar_fields:
            errors.append(f"{entry_id}: no grammar entry found for snapshot label `{snapshot_label.group(1)}`")
            continue

        expected_snapshot_state = re.search(r"`([^`]+)`", grammar_fields.get("Snapshot current state", "") or "")
        expected_claim_id = re.search(r"`([A-Z]-\d{4})`", grammar_fields.get("Claim id", "") or "")
        expected_verdict_id = re.search(r"`([A-Z]-\d{4})`", grammar_fields.get("Verdict id", "") or "")
        expected_claim_status = re.search(r"`([^`]+)`", grammar_fields.get("Required claim epistemic status", "") or "")
        expected_verdict_level = re.search(r"`([^`]+)`", grammar_fields.get("Required verdict level", "") or "")

        if expected_snapshot_state and expected_snapshot_state.group(1) != public_wording.group(1):
            errors.append(
                f"{entry_id}: public wording `{public_wording.group(1)}` does not match grammar entry `{grammar_entry_id}` snapshot state `{expected_snapshot_state.group(1)}`"
            )
        if expected_claim_id and expected_claim_id.group(1) != claim_id.group(1):
            errors.append(
                f"{entry_id}: claim id `{claim_id.group(1)}` does not match grammar entry `{grammar_entry_id}` claim id `{expected_claim_id.group(1)}`"
            )
        if expected_verdict_id and expected_verdict_id.group(1) != verdict_id.group(1):
            errors.append(
                f"{entry_id}: verdict id `{verdict_id.group(1)}` does not match grammar entry `{grammar_entry_id}` verdict id `{expected_verdict_id.group(1)}`"
            )
        if expected_claim_status and expected_claim_status.group(1) != claim_status.group(1):
            errors.append(
                f"{entry_id}: claim status `{claim_status.group(1)}` does not match grammar entry `{grammar_entry_id}` claim status `{expected_claim_status.group(1)}`"
            )
        if expected_verdict_level and expected_verdict_level.group(1) != verdict_level.group(1):
            errors.append(
                f"{entry_id}: verdict level `{verdict_level.group(1)}` does not match grammar entry `{grammar_entry_id}` verdict level `{expected_verdict_level.group(1)}`"
            )

    if errors:
        raise StatusLegendError("\n".join(errors))

    return {
        "legend_entries": len(legend_entries),
        "grammar_entries": len(grammar_entries),
    }


def main() -> None:
    try:
        summary = validate()
    except StatusLegendError as exc:
        print("Status legend consistency failed.", file=sys.stderr)
        print(file=sys.stderr)
        for line in str(exc).splitlines():
            if line.strip():
                print(line, file=sys.stderr)
        raise SystemExit(1) from exc

    print("Status legend consistency passed.")
    print()
    print(f"- legend entries: {summary['legend_entries']}")
    print(f"- grammar entries: {summary['grammar_entries']}")


if __name__ == "__main__":
    main()
