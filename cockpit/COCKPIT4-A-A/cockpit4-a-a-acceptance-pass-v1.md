# COCKPIT4-A-A Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT4-A-A / Public Candidate Emission Prototype v1**.
It does not claim that publication authority has been opened.
It records what must become true before a lawful public-candidate emission prototype verdict can be issued.

---

## Primary verdict set

- `PASS_PUBLIC_CANDIDATE_EMISSION_PROTOTYPE`
- `PASS_PUBLIC_CANDIDATE_FIELDS_CHECKER_VISIBLE`
- `HOLD_PUBLIC_CANDIDATE_SAMPLE_NOT_YET_AUDITABLE`
- `FAIL_PUBLIC_CANDIDATE_SAMPLE_NOT_FORMED`

---

## Required acceptance checks

### 1. Six-field emission check

The sample must visibly carry all six COCKPIT4-A fields:

- `source_object_kind`
- `provenance_trace`
- `current_verdict_posture`
- `dissent_residue_status`
- `audit_fingerprint`
- `export_snapshot_boundary`

### 2. Dissent-status legality check

The sample must use one lawful `dissent_residue_status.status_class` value.

### 3. Snapshot-boundary structure check

The sample must include `snapshot_id`, `included_object_set`, `excluded_object_set`, `frozen_snapshot_reference`, and `non_upgrade_clause`.

### 4. Non-upgrade continuity check

The sample must explicitly preserve that candidate admission does not create publication authority, verdict finalization, governed mutation authority, or public-truth status.

### 5. Prototype-boundedness check

The sample may not generalize itself into a full public-layer release or automatic candidate emitter.

---

## Pass condition

`PASS_PUBLIC_CANDIDATE_EMISSION_PROTOTYPE` is lawful only if all five required checks pass.

`PASS_PUBLIC_CANDIDATE_FIELDS_CHECKER_VISIBLE` is lawful only if the sample exposes all six fields in a machine-checkable form.
