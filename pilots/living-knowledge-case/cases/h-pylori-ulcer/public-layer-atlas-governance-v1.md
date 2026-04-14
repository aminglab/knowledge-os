# Public-Layer Atlas Governance v1

This note records the current **public-layer atlas governance rule v1** for the `h-pylori-ulcer` case.

Its purpose is narrow:

- keep the second-case public-layer atlas, acceptance record, README entry surface, and suite entrypoint from drifting out of sync,
- define the minimum governance facts those surfaces should continue to agree on,
- and justify a small self-check now that the second-case public-layer stack is no longer tiny.

This note is case-scoped.
It does **not** claim to define a repository-wide atlas doctrine.

---

## Why this layer exists

The second case now has more than one public-layer governance surface:

- the suite entrypoint
- the verification atlas
- the acceptance pass record
- the case README governance path

That is already enough for a new failure mode:

> the checker network can move forward,
> while the atlas, acceptance record, or README still describe an older stack.

That drift is no longer hypothetical.
It has already happened once on the snapshot side.

This file exists so the next stage does not depend on memory and manual cleanup.

---

## One-sentence ruling

Current ruling:

> **The suite entrypoint, verification atlas, acceptance record, and case README should continue to agree on the current second-case public-layer stack at the level of named checks, current hardening lifts, and retained holds.**

Do not let the stack become operationally stronger while its governance surfaces describe an earlier stage.

---

## Current minimum governance facts

At the current stage, the following facts should remain aligned across the atlas-governed surfaces.

### 1. Current suite composition

The current suite should continue to expose these named checks:

- `check_h_pylori_claim_page_layering.py`
- `check_h_pylori_claim_page_pressure_coverage.py`
- `check_h_pylori_source_page_layering.py`
- `check_h_pylori_source_page_role_anchors.py`
- `check_h_pylori_snapshot_section_layering.py`
- `check_h_pylori_snapshot_subsection_semantics.py`
- `check_h_pylori_snapshot_consistency.py`

### 2. Current richer hardening lifts

The current second-case stack should continue to describe these harder lifts:

- claim-page direct pressure coverage
- source-page role anchors
- snapshot subsection semantic anchors
- fuller snapshot consistency checking

### 3. Current retained holds

The current second-case stack should continue to retain at least:

- `HOLD_NO_FULL_PUBLIC_RELEASE`
- `HOLD_NO_PAGE_EMISSION_LAYER`
- `HOLD_NO_LARGER_PUBLIC_LAYER_ORCHESTRATION_BOUNDARY`
- `HOLD_NO_REPOSITORY_WIDE_PUBLIC_LAYER_GENERALIZATION`

### 4. README governance visibility

The case README should continue to expose the current public-layer governance path rather than stopping at an older stage.

---

## What this note does not require

This note does **not** require:

- a repository-wide governance registry,
- a first-case-equivalent orchestration boundary,
- or a full atlas self-auditing subframework.

The goal is not to overbuild.
The goal is to stop obvious second-case governance drift.

---

## Practical verdict

So the practical verdict is:

- **the second-case stack is now large enough to justify a small atlas-governance self-check**
- **that self-check should stay narrow and factual**
- **its job is to keep suite, atlas, acceptance, and README in the same stage of reality**
