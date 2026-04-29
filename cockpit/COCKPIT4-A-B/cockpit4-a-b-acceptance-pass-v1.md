# COCKPIT4-A-B Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT4-A-B / Public Candidate Index and Registry Floor v1**.
It does not claim that indexing creates publication authority.
It records what must become true before a lawful public-candidate index verdict can be issued.

---

## Primary verdict set

- `PASS_PUBLIC_CANDIDATE_INDEX_FLOOR`
- `PASS_PUBLIC_CANDIDATE_REGISTRY_CONSISTENT`
- `HOLD_PUBLIC_CANDIDATE_INDEX_NOT_YET_CONSISTENT`
- `FAIL_PUBLIC_CANDIDATE_INDEX_NOT_FORMED`

---

## Required acceptance checks

### 1. Index-object formation check

The index must exist as a machine-readable JSON object with `index_type: public_candidate_index`.

### 2. Candidate-count check

The `candidate_count` field must equal the number of registry entries.

### 3. Entry-field completeness check

Each registry entry must expose:

- `object_id`
- `candidate_stage`
- `source_object_kind`
- `candidate_file`
- `dissent_residue_status_class`
- `snapshot_id`
- `registry_status`

### 4. Candidate-file consistency check

Each `candidate_file` must exist and its `object_id` must match the registry entry.

### 5. Non-publication continuity check

The index must explicitly preserve that indexing a public candidate does not create publication authority, verdict finalization, governed mutation authority, or public-truth status.

---

## Pass condition

`PASS_PUBLIC_CANDIDATE_INDEX_FLOOR` is lawful only if checks 1, 2, 3, and 5 pass.

`PASS_PUBLIC_CANDIDATE_REGISTRY_CONSISTENT` is lawful only if all five required checks pass together.
