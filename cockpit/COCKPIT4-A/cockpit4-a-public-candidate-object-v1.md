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

### 3. `current_verdict_posture`
A clear statement of the current private-stage verdict posture carried by the object.
The candidate may not pretend to be verdict-free.

### 4. `dissent_residue_status`
A clear statement of whether dissent has been cleared, narrowed, carried forward, or remains explicitly unresolved.
A public candidate may not conceal unresolved dissent residue.

### 5. `audit_fingerprint`
A stable audit-facing identifier or snapshot fingerprint tying the candidate back to a concrete governed object state.

### 6. `export_snapshot_boundary`
A clear boundary statement describing what snapshot is being presented and what is not being upgraded by that presentation.

---

## Unlawful candidate shortcuts

The following remain unlawful at this stage:

- candidate objects with no provenance trace
- candidate objects with hidden dissent residue
- candidate objects framed as already published
- candidate objects framed as already team-approved
- candidate objects framed as already final truth

---

## Current lawful reading

The right reading is:

> a public candidate is a governed export-admission object that remains visibly provisional.

The wrong reading is:

> once a private object is well formed, it is basically public already.
