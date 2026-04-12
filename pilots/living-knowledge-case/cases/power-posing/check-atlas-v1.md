# Check Atlas v1

This file is the current **check atlas v1** for the power-posing pilot.

Its purpose is not to add another validation layer.
Its purpose is to make the existing validation network legible:

- what each checker protects,
- what files it reads,
- what a failure means,
- where two checkers are adjacent,
- and where they are intentionally distinct.

This atlas is case-scoped.
It does **not** claim to be a repository-wide validation constitution.

For the narrower atlas that focuses only on the current public-layer ecology, see:

- [`public-layer-verification-atlas-v1.md`](./public-layer-verification-atlas-v1.md)

For the formal authority note that explains why the two atlas files currently coexist and why they should not be merged yet, see:

- [`atlas-authority-boundary-ruling-v1.md`](./atlas-authority-boundary-ruling-v1.md)

For the lighter future-threshold note that names when a merge could later become admissible, see:

- [`atlas-merge-threshold-v1.md`](./atlas-merge-threshold-v1.md)

That ruling governs the present boundary.
That threshold note governs the future merge condition.
This file remains the broader case-scoped map.

---

## Authority note

Current authority note:

- `check-atlas-v1.md` remains the broader case-scoped validation map,
- `public-layer-verification-atlas-v1.md` remains the narrower public-layer atlas,
- `atlas-authority-boundary-ruling-v1.md` governs the current dual-atlas boundary,
- `atlas-merge-threshold-v1.md` governs the future admissibility threshold for a possible merge,
- and no atlas merge is currently authorized.

---

## Why this atlas exists

The power-posing case is no longer held together by one generator script and one snapshot.
It now has a small but real validation network.

Without an atlas, two bad things become likely:

1. later work starts to confuse neighboring checks with duplicate checks,
2. future refactors lose the distinction between object-envelope consistency, narrative consistency, reader-facing surface consistency, and template-seam governance exposure.

This file exists to prevent that drift.

---

## Current layer map

The current case can be read as seven adjacent layers:

1. **Object layer**
   - claim, evidence, dissent, and verdict objects under `objects/`
2. **Reference metadata layer**
   - `references-metadata-v1.md`
3. **Verdict grammar layer**
   - `verdict-grammar-v1.md`
4. **Status legend layer**
   - `status-legend-v1.md`
5. **Snapshot layer**
   - `snapshots/snapshot-v2.md`
6. **Reader-facing surface layer**
   - `references.md`, `README.md` public reading paths, snapshot reading paths, and page prototype entrypoints
7. **Template-seam governance surface layer**
   - `case-template-boundary-v1.md`, `case-template-extraction-checklist-v1.md`, `template-seam-summary-v1.md` as exposed through README developer / governance paths

The checks below are distributed across these layers rather than collapsed into one monolithic validator.

---

## Entry surface

The current explicit validation entrypoints are:

### Make targets
- `make check-page`
- `make check-page-json`
- `make check-public-layer`
- `make power-posing-public-layer`

These call either the page generator in validation mode or the public-layer orchestrator entrypoint.

### GitHub Actions workflows
- `check-power-posing-page.yml`
- `check-power-posing-object-envelope.yml`
- `check-power-posing-snapshot-consistency.yml`
- `check-power-posing-reference-metadata.yml`
- `check-power-posing-verdict-grammar.yml`
- `check-power-posing-status-legend.yml`
- `check-power-posing-public-surface.yml`
- `check-power-posing-template-seam-readme.yml`
- `check-power-posing-public-layer.yml`

These workflows together form the current CI surface for the case.

### Atlas governance notes
- [`atlas-authority-boundary-ruling-v1.md`](./atlas-authority-boundary-ruling-v1.md) — current authority boundary for the dual-atlas structure
- [`atlas-merge-threshold-v1.md`](./atlas-merge-threshold-v1.md) — future admissibility threshold for a possible atlas merge

These are not entrypoints for running validation.
They are entrypoints for interpreting the current atlas structure correctly.
The current atlas governance checker now reports this layer in two views: a **boundary view** for the present dual-atlas structure and a **threshold view** for future merge admissibility.

---

## Current checker atlas

### 1. Page validation surface
- **Primary script:** `page/generate_page_data.py`
- **Repository entrypoints:** `make check-page`, `make check-page-json`
- **Protected layer:** release-generation layer between governed objects and the public page prototype
- **Reads:** object files, `snapshot-v2.md`, `timeline/events.md`, `references-metadata-v1.md`
- **Checks:** required frontmatter fields, source ref coverage, basis refs, link targets, snapshot required sections, release-summary construction
- **Failure meaning:** the current case layer can no longer be safely emitted into the page prototype contract
- **Why it stays distinct:** it is the only checker that validates the page-data generation contract itself rather than only the markdown surface

### 2. Object envelope conformance
- **Primary script:** `scripts/check_power_posing_object_envelope.py`
- **Protected layer:** object frontmatter conformance to the current working protocol envelope
- **Reads:** all object files, `protocol/object-envelope.md`, `protocol/enums.md`, `protocol/link-types.md`, `references-metadata-v1.md`
- **Checks:** object family ↔ file path agreement, required frontmatter fields, enum conformance, allowed top-level fields, source ref coverage, basis ref coverage, and link structure / target validity
- **Failure meaning:** object frontmatter has drifted away from the working envelope strongly enough that the pilot can no longer treat the object layer as a stable protocol floor
- **Why it stays distinct:** it protects the protocol floor of the object layer itself, rather than the snapshot, source metadata, or public wording built on top of it

### 3. Snapshot consistency
- **Primary script:** `scripts/check_power_posing_snapshot_consistency.py`
- **Protected layer:** snapshot narrative consistency
- **Reads:** `snapshot-v2.md`, `references-metadata-v1.md`, all object files
- **Checks:** included object coverage, reading-path object ids, object-link path validity, canonical source id coverage against object frontmatter
- **Failure meaning:** the public snapshot has drifted away from the current object / reference reality
- **Why it stays distinct:** it protects the snapshot as a governed narrative object, not the broader public reading surface

### 4. Reference metadata consistency
- **Primary script:** `scripts/check_power_posing_reference_metadata.py`
- **Protected layer:** source metadata layer
- **Reads:** `references-metadata-v1.md`, all object files
- **Checks:** source id coverage, required metadata fields, declared object usage versus object frontmatter usage
- **Failure meaning:** the stable source metadata layer no longer faithfully describes current object grounding
- **Why it stays distinct:** it governs the source layer, not the snapshot or verdict language

### 5. Verdict grammar consistency
- **Primary script:** `scripts/check_power_posing_verdict_grammar.py`
- **Protected layer:** bridge between snapshot status wording and verdict / claim judgment fields
- **Reads:** `verdict-grammar-v1.md`, `snapshot-v2.md`, claim objects, verdict objects
- **Checks:** snapshot current-state wording, required claim epistemic status, required verdict level, required verdict-body anchor terms
- **Failure meaning:** public-facing judgment wording and object-layer verdict semantics have drifted apart
- **Why it stays distinct:** it is the canonical bridge between human-readable status wording and object-layer judgment fields

### 6. Status legend consistency
- **Primary script:** `scripts/check_power_posing_status_legend.py`
- **Protected layer:** reader-facing explanation of status wording
- **Reads:** `status-legend-v1.md`, `verdict-grammar-v1.md`, `snapshot-v2.md`
- **Checks:** public wording alignment, snapshot label alignment, claim / verdict id alignment, governing status and verdict-level alignment against grammar
- **Failure meaning:** the reader-facing explanation of status language is no longer synchronized with the grammar that governs it
- **Why it stays distinct:** it validates the explanatory legend layer rather than the underlying grammar layer itself

### 7. Public surface consistency
- **Primary script:** `scripts/check_power_posing_public_surface.py`
- **Protected layer:** reader-facing path and link surface
- **Reads:** `snapshot-v2.md`, `README.md`
- **Checks:** required reader-facing links in `Public reading path` to `snapshot-v2.md`, `references.md`, `case.md`, and `timeline/events.md`, plus required governance links in the snapshot itself
- **Failure meaning:** the public-facing navigation surface no longer exposes the minimum path needed to read the case as a public artifact
- **Why it stays distinct:** it checks what the outside reader can visibly navigate first, not whether the underlying semantics are true

### 8. README template seam audit
- **Primary script:** `scripts/check_power_posing_template_seam_readme.py`
- **Protected layer:** template-seam governance surface as exposed through README paths
- **Reads:** `README.md`
- **Checks:** required README exposure of `case-template-boundary-v1.md`, `case-template-extraction-checklist-v1.md`, and `template-seam-summary-v1.md` in both `Developer / governance path` and `Folder guide`
- **Failure meaning:** the README no longer exposes the documents that govern seam boundary, extraction discipline, and consolidated seam judgment
- **Why it stays distinct:** it does not validate general public navigation; it validates continued exposure of the case’s reusable-seam governance documents

---

## Adjacency and boundary notes

### Object envelope conformance vs reference metadata consistency
These two are adjacent but not identical.

- **Object envelope conformance** asks whether the object files still satisfy the current protocol floor.
- **Reference metadata consistency** asks whether the stable metadata layer still truthfully reflects current object grounding.

One protects object structure.
The other protects source-layer description.

They should not be treated as duplicate merely because both touch `source_refs`.

### Snapshot consistency vs public surface consistency
These two are adjacent but not identical.

- **Snapshot consistency** asks whether the snapshot still truthfully points to the current object/reference world.
- **Public surface consistency** asks whether the reader-facing navigation path still exposes the minimum path a public reader now needs.

A future refactor might merge them, but they should not be treated as already redundant.

### Public surface consistency vs README template seam audit
These two are also adjacent but not identical.

- **Public surface consistency** checks whether the public reading surface still exposes the minimum entry path for reading the case.
- **README template seam audit** checks whether the README still exposes the documents that govern seam reuse discipline.

One protects public reading navigation.
The other protects developer-facing seam governance exposure.

They should not be treated as duplicate merely because both read `README.md`.

### Verdict grammar vs status legend
These two are also adjacent but not identical.

- **Verdict grammar** is the governing bridge from snapshot wording to claim/verdict state fields.
- **Status legend** is the reader-facing explanation of how to read those governed phrases.

If one changes without the other, that is not a harmless editorial difference; it is exactly the drift these checks are meant to catch.

### Page validation vs all other checks
The generator check is special.
It is not just another markdown consistency pass.
It is the only check that proves the current case layer can still be emitted into a stable page-data contract.

That is why it should remain explicit even if other markdown-layer checks are later consolidated.

---

## Failure interpretation guide

When a check fails, the safest first interpretation is:

- **page validation failed** → release emission contract broken
- **object envelope failed** → object frontmatter drifted from the current protocol floor
- **snapshot consistency failed** → snapshot narrative drifted from governed objects/references
- **reference metadata failed** → source layer drifted from object grounding
- **verdict grammar failed** → judgment wording drifted from claim/verdict semantics
- **status legend failed** → reader-facing explanation drifted from governing grammar
- **public surface failed** → public reading path no longer exposes the minimum reader-facing path the pilot now depends on
- **README template seam audit failed** → README no longer exposes the documents that govern seam boundary and seam reuse discipline

The point of the network is not only to reject bad states.
It is also to localize what kind of bad state has appeared.

---

## Current non-goals

This atlas does **not** claim that the current validation network is final.
In particular, it does not yet do all of the following:

- generic multi-case validation,
- repository-wide verdict grammar governance,
- cross-case source doctrine enforcement,
- unified check orchestration beyond the current explicit entrypoints,
- or automatic contraction of adjacent checks into a single canonical validator.

Those are future design questions, not current facts.

---

## Natural next-step directions

Once this atlas exists, the next moves become clearer:

1. decide whether object-envelope conformance should remain case-scoped or later lift into a broader pilot-level envelope checker,
2. decide whether `snapshot consistency` and `public surface consistency` should remain adjacent or later be partially merged,
3. decide whether `public surface consistency` and `README template seam audit` should remain separate or later share a small utility layer while preserving distinct failure meanings,
4. decide whether `verdict grammar` and `status legend` should remain separate artifacts or later be represented as one layered document with two validation views,
5. and decide whether the current power-posing validation network is mature enough to be used as the template for a second case.

Until then, the safest discipline is simple:

- do not remove a checker merely because it looks similar to a neighbor,
- and do not merge layers before their boundary has first been documented here.
