# Atlas Authority Boundary Ruling v1

This file records the current **atlas authority boundary ruling v1** for the `power-posing` pilot.

Its job is simple:

> make the authority relationship between `check-atlas-v1.md` and `public-layer-verification-atlas-v1.md` explicit,
> say which one is broader and which one is narrower,
> say which one to read first for which task,
> and state clearly why they should **not** be merged yet.

For the lighter future-threshold note that asks when a merge could later become admissible, see:

- [`atlas-merge-threshold-v1.md`](./atlas-merge-threshold-v1.md)

---

## One-sentence ruling

Current ruling:

> **Keep the two atlas files separate for now.**
> **`check-atlas-v1.md` remains the broader case-scoped validation map.**
> **`public-layer-verification-atlas-v1.md` remains the narrower public-layer atlas.**
> **Do not merge them yet.**

---

## Current authority split

### 1. `check-atlas-v1.md`
This remains the broader map.

It is the right first document when the question is:

- what validation layers currently exist across the case,
- how object, snapshot, reference, public surface, and seam governance checks relate,
- what kinds of failures different checkers localize,
- and how the broader case-scoped validation topology currently hangs together.

### 2. `public-layer-verification-atlas-v1.md`
This remains the narrower map.

It is the right first document when the question is:

- what the current public-layer subset is,
- which checks specifically protect claim/source/snapshot/page public surfaces,
- what the public-layer orchestration boundary currently is,
- and what the remaining public-layer-specific gaps are.

---

## Practical reading order

Use the following rule.

### Read `public-layer-verification-atlas-v1.md` first when:
- you are changing claim pages,
- source pages,
- snapshot public sections,
- page emission,
- or the public-layer orchestrator itself.

### Read `check-atlas-v1.md` first when:
- you are reasoning about the broader case validation map,
- you are comparing adjacent non-public-layer checks,
- you are touching object-envelope, reference metadata, or seam-governance validation,
- or you need the wider case-scoped topology before narrowing down.

### Read this ruling when:
- you are unsure which atlas is authoritative for the task in front of you,
- you are tempted to merge the two atlases,
- or you need the current boundary judgment in one place instead of reconstructing it from README notes and cross-links.

### Read `atlas-merge-threshold-v1.md` when:
- you are asking whether a future merge has become admissible,
- you want the current non-merge stance translated into threshold language,
- or you need a future-facing criterion rather than a present-boundary ruling.

---

## Why they should not be merged yet

The current non-merge ruling is not just conservatism.
It follows from a real scope difference.

### 1. Scope is still asymmetric
- `check-atlas-v1.md` is still the broader case-scoped validation map.
- `public-layer-verification-atlas-v1.md` is still the narrower public-layer atlas.

A merged file would either bloat the narrower atlas or thin out the broader one.

### 2. The public-layer stack now has its own operational boundary
The public layer now has:

- a named orchestrator,
- a named workflow,
- and its own narrower checker subset.

That makes the public-layer atlas more than a convenience note.
It has become a real sub-map.

### 3. The broader case map still contains non-public-layer boundary value
The broader atlas still helps explain:

- why page validation is distinct from markdown validation,
- why public surface consistency is distinct from template-seam exposure,
- and how adjacent case-scoped checks localize different failure classes.

That material still has value even when the task is not purely public-layer-facing.

### 4. Merge pressure should wait for a stronger threshold
A future merge could become sensible later.
But not before one of the following becomes true:

- the broader atlas contracts toward the public-layer subset,
- the public-layer atlas expands into the dominant case-scoped map,
- or a stronger multi-case / repo-wide atlas structure forces a clearer consolidation pass.

The explicit future-threshold object for that question now lives in:

- [`atlas-merge-threshold-v1.md`](./atlas-merge-threshold-v1.md)

Until then, the safer discipline is:

> **keep both, name their boundary, and stop pretending the split is accidental.**

---

## README exposure rule

The `power-posing/README.md` should expose all four of the following in the developer / governance route and in the folder guide:

- `public-layer-verification-atlas-v1.md`
- `check-atlas-v1.md`
- `atlas-authority-boundary-ruling-v1.md`
- `atlas-merge-threshold-v1.md`

That is the minimum exposure rule for keeping the split legible rather than hidden.

---

## Atlas cross-link rule

Both atlas files should point to this ruling.

That does not make this file the only atlas.
It makes this file the formal boundary note that explains why two adjacent atlases currently coexist.

---

## Practical verdict

So the practical verdict is:

- the atlas split is now intentional rather than accidental,
- the broader atlas and the narrower public-layer atlas now have explicit roles,
- the future merge question now has its own lighter threshold note,
- and the current stage still favors a governed dual-atlas structure over premature consolidation.
