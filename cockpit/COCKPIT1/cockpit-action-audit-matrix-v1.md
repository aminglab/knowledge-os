# COCKPIT1 Action Audit Matrix v1

## Status

Drafted for construction.

## Matrix

| Action | Anchor object | Default write scope | Human sign-off required | Minimum audit trace |
|---|---|---:|---:|---|
| `scan_missing_evidence` | claim / route | read_only | no | actor, anchor, model, timestamp, output |
| `draft_dissent_response` | dissent | draft_only | no | actor, anchor, model, timestamp, draft location |
| `check_upgrade_conditions` | claim / verdict | read_only | no | actor, anchor, model, timestamp, assessment |
| `export_progress_summary` | project / route / claim | draft_only | no | actor, anchor, template, timestamp, export path |
| `generate_canonical_continuation` | project / route | read_only | no | actor, anchor, model, timestamp, ranked options |
| `freeze_object_revision` | object | draft_plus_commit | yes | actor, anchor, revision id, commit ref, timestamp |

## Matrix rules

1. No action may write a verdict directly by default.
2. Any object-freezing action must leave a revision or commit trace.
3. Any future higher-risk action must be added here before becoming a cockpit primitive.

## Current floor

This matrix is the minimum permission-and-audit floor for COCKPIT1.
It is intentionally narrower than a team-layer workflow matrix.
