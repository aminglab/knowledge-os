# H. pylori first-consistency-pass-v1

## Status

Completed first consistency pass.

## Function

This document records the first shell-internal consistency pass for the second case:

- after explicit second-case authorization,
- before any broader multi-case generalization,
- and before a harder public-layer release pass.

Its job is not to pretend the second case is already mature.
Its job is to tighten the shell that now exists.

---

## Scope checked in this pass

This pass checked four adjacent surfaces:

1. `references-metadata-v1.md` against current object frontmatter usage
2. `claims/` and `snapshots/snapshot-v0.md` against the current verdict arc
3. `README.md`, `references.md`, and `sources/README.md` against the real stage of the source layer
4. activation wording around shell-copy discipline

---

## Findings

### 1. Activation status was real but under-signposted

The activation chain already existed:

- `second-case-authorization-v1.md` explicitly authorized the second case,
- and the existing seam documents already governed shell reuse.

But the checklist itself still read too much like a future-condition note.
This pass therefore records that gap explicitly.

### 2. Source metadata usage had drifted from object frontmatter

Several canonical source entries had object-usage lists that no longer matched the current object layer exactly.

The drift was not catastrophic, but it was real.
Examples included:

- early publication sources used by dissent objects without that usage being recorded,
- consensus and guidance sources whose usage lists lagged behind current claim or dissent references.

This pass treats that as a real consistency defect rather than as harmless slack.

### 3. The source layer was real, but still too thin

Before this pass, the second case had:

- a thin source entrypoint,
- a stable metadata layer,
- and only a source-pack index.

That was enough for a first object skeleton, but not yet enough for a first governed public-facing source surface.

This pass therefore opens the first actual source-page seed surfaces.

### 4. The core case arc was already coherent

The main line remained consistent across:

- object files,
- claim pages,
- snapshot seed,
- and timeline.

The second case still reads as:

> false rejection moving toward stabilization,
> with later narrowing into a more careful descendant public path.

That core arc did not need rewriting in this pass.

---

## Output of this pass

This pass produces two concrete outcomes immediately and identifies one still-open cleanup item:

1. first actual source-page seed surfaces now exist for the second case
2. the consistency defects around source-metadata usage are now explicitly documented
3. activation back-reference and metadata-floor tightening should still be written directly into the existing shell documents in a follow-up edit

---

## Current verdict

Current verdict:

> The second case remains in seed-stage form,
> but its shell is now tighter than the original object-skeleton drop.
>
> The main remaining weakness is no longer whether the case exists.
> It is how far the source layer and later snapshot/page surfaces should now be hardened.

---

## Next natural step

The next natural step is:

> use the now-real source-page seed layer as the base for a first H. pylori public-layer hardening pass,
> rather than continuing to expand the second case by adding more raw objects.
