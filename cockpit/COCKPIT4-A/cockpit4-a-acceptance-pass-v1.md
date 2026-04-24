# COCKPIT4-A Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT4-A / Public Candidate Admission Floor v1**.
It does not claim that publication authority has already been lawfully opened.
It records what must become true before a lawful public-candidate admission verdict can be issued.

---

## Primary verdict set

- `PASS_PUBLIC_CANDIDATE_OBJECT_FLOOR`
- `PASS_PUBLIC_CANDIDATE_ADMISSION_GRAMMAR`
- `HOLD_PUBLIC_CANDIDATE_NOT_YET_AUDITABLE`
- `FAIL_PUBLIC_CANDIDATE_OBJECT_NOT_FORMED`

---

## Required acceptance checks

### 1. Source-object clarity check

The candidate grammar must clearly identify what private governed object kinds may lawfully feed a public candidate.

It must also prevent bounded composites from hiding their parent object relations.

### 2. Provenance-trace check

The candidate grammar must require provenance trace as a non-optional field.

The trace must include at least:

- private source path or object id
- producing cockpit stage or route
- latest governed snapshot reference
- parent object relation if the candidate is composite

### 3. Verdict-posture honesty check

The candidate grammar must require the current verdict posture to remain visible rather than implied away.

The posture must say whether it is local, provisional, supported, or unresolved, and whether it is inherited from a private object or newly summarized for admission.

### 4. Dissent-residue honesty check

The candidate grammar must require dissent residue status to remain explicit rather than concealed.

The status must use one of the lawful status classes:

- `none_remaining_documented`
- `narrowed_carried_forward`
- `unresolved_carried_forward`
- `not_yet_evaluated_hold`

The grammar must reject vague substitutes such as "no major issues" or "basically settled".

### 5. Audit-and-boundary check

The candidate grammar must require both an audit fingerprint and an export snapshot boundary, and it must preserve the distinction between candidate admission and publication authority.

The export boundary must include at least:

- `snapshot_id`
- `included_object_set`
- `excluded_object_set`
- `frozen_snapshot_reference`
- `non_upgrade_clause`

The `non_upgrade_clause` must explicitly preserve that candidate admission does not create publication authority, verdict finalization, governed mutation authority, or public-truth status.

---

## Pass condition

`PASS_PUBLIC_CANDIDATE_OBJECT_FLOOR` is lawful only if all five required checks pass.

`PASS_PUBLIC_CANDIDATE_ADMISSION_GRAMMAR` is lawful only if the candidate layer remains visibly provisional, auditable, dissent-honest, snapshot-bounded, and non-published.
