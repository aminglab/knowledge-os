# COCKPIT4-A Public Candidate Object v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum object grammar for a `public_candidate_object` inside COCKPIT4-A.
Its purpose is to answer a narrow governance question:

> what minimum controlled object must exist before a private governed result can even be discussed as a candidate for public presentation?

---

## Governing principle

A `public_candidate_object` is a **candidate-layer object**, not a publication-layer object.
It may make a possible public-facing package legible.
It may not silently upgrade that package into a published, finalized, or institutionally approved result.

The candidate object therefore must carry its private-stage uncertainty forward rather than polishing it away.

---

## Minimum admissibility fields

A `public_candidate_object` should not be named unless it carries at least the following fields:

### 1. `source_object_kind`
A clear statement of what private governed object the candidate is derived from, such as:

- claim object
- evidence object
- dissent object
- verdict object
- bounded composite of the above

### 2. `provenance_trace`
A compact trace showing where the candidate came from in the private line.
This must not be omitted.

Minimum trace content:

- private source path or object id
- producing cockpit stage or route
- latest governed snapshot reference
- parent object relation if the candidate is composite

### 3. `current_verdict_posture`
A clear statement of the current private-stage verdict posture carried by the object.
The candidate may not pretend to be verdict-free.

Minimum posture content:

- current verdict label or hold label
- whether the verdict is local, provisional, supported, or unresolved
- whether the posture is inherited from a private object or newly summarized for admission

### 4. `dissent_residue_status`
A public candidate may not conceal unresolved dissent residue.
This field must be explicit and must use one of the following status classes:

- `none_remaining_documented`
- `narrowed_carried_forward`
- `unresolved_carried_forward`
- `not_yet_evaluated_hold`

A candidate may not use vague phrases such as "no major issues" or "basically settled" as a substitute for this field.

Minimum dissent residue content:

- status class
- linked dissent object ids or an explicit `none_linked` statement
- residue summary in bounded prose
- public-reader warning if unresolved or not yet evaluated residue remains

The status `none_remaining_documented` is lawful only when the provenance trace identifies where dissent was cleared or why no dissent object is linked.

### 5. `audit_fingerprint`
A stable audit-facing identifier or snapshot fingerprint tying the candidate back to a concrete governed object state.

Minimum fingerprint content:

- stable id or content hash
- snapshot-producing source
- timestamp, commit, or equivalent frozen reference when available

### 6. `export_snapshot_boundary`
A public candidate must declare what exact snapshot is being exported into the candidate layer and what remains outside that snapshot.
This field must not be a generic export note.

Minimum snapshot-boundary content:

- `snapshot_id`
- `included_object_set`
- `excluded_object_set`
- `frozen_snapshot_reference`
- `non_upgrade_clause`

The `non_upgrade_clause` must explicitly state that candidate admission does not create publication authority, verdict finalization, governed mutation authority, or public-truth status.

---

## Unlawful candidate shortcuts

The following remain unlawful at this stage:

- candidate objects with no provenance trace
- candidate objects with hidden dissent residue
- candidate objects using vague dissent phrases instead of a residue status class
- candidate objects with no explicit export snapshot boundary
- candidate objects whose export boundary does not name included and excluded object sets
- candidate objects framed as already published
- candidate objects framed as already team-approved
- candidate objects framed as already final truth

---

## Current lawful reading

The right reading is:

> a public candidate is a governed export-admission object that remains visibly provisional, provenance-bound, dissent-honest, and snapshot-bounded.

The wrong reading is:

> once a private object is well formed, it is basically public already.
