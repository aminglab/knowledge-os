# Public-Layer Orchestration Boundary v1

This note records the current **public-layer orchestration boundary v1** for the `h-pylori-ulcer` case.

Its purpose is narrow:

- define what currently counts as the second case's public-layer orchestrator,
- make the relationship between the suite entrypoint, workflow entrypoint, atlas, and atlas-governance self-check explicit,
- and explain why the current stage still stops short of a larger orchestration expansion.

This note is case-scoped.
It does **not** claim to define a repository-wide orchestration doctrine.

---

## One-sentence ruling

Current ruling:

> **The current second-case public-layer orchestrator is the existing suite entrypoint plus its workflow and atlas-governed boundary surfaces.**
> **Do not open a larger orchestration expansion yet.**

---

## Current authority split

### 1. `scripts/check_h_pylori_public_layer.py`
This remains the operational suite entrypoint.

It is the right first surface when the question is:

- what public-layer checks currently run together,
- how claim/source/snapshot/public-entry checks are grouped,
- and what the current overall public-layer verdict is.

### 2. `check-h-pylori-public-layer.yml`
This remains the workflow entrypoint.

It is the right first surface when the question is:

- how the public-layer suite is triggered,
- which path changes currently rerun it,
- and what currently counts as workflow-level enforcement.

### 3. `public-layer-verification-atlas-v1.md`
This remains the current public-layer sub-map.

It is the right first surface when the question is:

- which checks currently protect which public surface,
- what the current subset topology is,
- and what public-layer-specific gaps remain.

### 4. `public-layer-atlas-governance-v1.md`
This remains the self-check note that keeps suite, atlas, acceptance, and README aligned.

It is the right first surface when the question is:

- whether the current governance surfaces still describe the same stack,
- and whether narrative drift has reappeared.

---

## Why this is now a real boundary

The current second-case public layer is no longer small enough to treat all of the following as one accidental pile:

- suite entrypoint
- workflow entrypoint
- atlas
- atlas-governance self-check

These now form a real operational boundary.

That does **not** mean the second case has reached first-case maturity.
It means the current boundary is no longer implicit.

---

## Why the boundary should not expand further yet

The current non-expansion ruling is not timidity.
It follows from the current stack shape.

### 1. No page-emission layer yet
The second case still does not have a page-emission layer comparable to the first case.
So a larger orchestration expansion would currently be wider in naming than in substance.

### 2. One suite entrypoint is still enough
The current second-case public layer still routes cleanly through one suite entrypoint and one main workflow entrypoint.
That means a stronger hidden-checks or multi-entry orchestration structure is not yet forced.

### 3. The current self-check now covers the recent drift class
The most recent real failure mode was atlas / acceptance / README drift.
That is now covered by the atlas-governance self-check.
There is no need to pretend a much larger orchestrator is required before the current smaller one has been fully absorbed.

---

## Practical reading order

Use the following rule.

### Read `scripts/check_h_pylori_public_layer.py` first when:
- you want the current public-layer verdict,
- you are changing a current public-layer checker,
- or you need the current grouped suite entrypoint.

### Read `public-layer-verification-atlas-v1.md` first when:
- you are reasoning about which checks protect which public surfaces,
- you are changing the current layer topology,
- or you need the current public-layer map.

### Read `public-layer-atlas-governance-v1.md` first when:
- you are worried the current governance surfaces may have drifted,
- or you need to verify suite / atlas / acceptance / README alignment.

### Read this note first when:
- you are asking whether the second case already has a real orchestration boundary,
- you are tempted to open a larger boundary immediately,
- or you need the current do-not-expand-yet judgment in one place.

### Read `public-layer-orchestration-threshold-v1.md` when:
- you are asking what would justify a later orchestration expansion,
- or you need threshold language rather than a present-boundary ruling.

---

## README exposure rule

The `h-pylori-ulcer/README.md` should expose all four of the following in the developer / governance path and in the folder guide:

- `public-layer-verification-atlas-v1.md`
- `public-layer-atlas-governance-v1.md`
- `public-layer-orchestration-boundary-v1.md`
- `public-layer-orchestration-threshold-v1.md`

That is the minimum exposure rule for keeping the current boundary legible rather than implicit.

---

## Practical verdict

So the practical verdict is:

- the second case now has an explicit public-layer orchestration boundary,
- that boundary is still intentionally smaller than the first case's broader public-layer ecology,
- the current stage favors naming and checking the boundary,
- and the larger-expansion question now belongs to an explicit threshold note rather than to memory or guesswork.
