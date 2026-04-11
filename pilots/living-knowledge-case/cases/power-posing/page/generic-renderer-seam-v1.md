# Generic renderer seam v1

This note records the **first serious renderer-seam judgment** for the current `power-posing` page line.

It does **not** claim that the renderer is already generic.
It records a narrower question:

> after the recent page-layer integration and component-level deepening work, which parts of the current renderer now look like lawful extraction candidates, and which parts remain clearly case-scoped?

---

## Current stage judgment

Current ruling:

> **Do not genericize the full page stack yet.**
> **Do identify and protect the first renderer seam.**

The page line is now stronger than a flat one-off prototype.
It has:

- a governed object layer,
- a snapshot-backed release layer,
- a validating page-data generator,
- a reader-facing page shell,
- a visible claim-lineage surface,
- grouped source stacks,
- and explicit public claim/source route cards.

That is enough to justify seam analysis.
It is **not** enough to justify pretending there is already a general multi-case renderer.

---

## Current implementation status

The seam is no longer only theoretical.
The current page stack now carries an extracted primitive layer in:

- `renderer-primitives.js`

At the current stage, that extracted layer now carries two waves of lawful units:

### First-wave primitives

- section shell primitive
- meta-row primitive
- links-block primitive
- lineage-rail primitive
- route-card primitive
- split source-link primitive
- source-link-block primitive

### Second-wave primitives

- standard-card primitive
- status-card primitive
- timeline-item primitive
- source-item primitive
- source-group primitive
- footer-card primitive

That extraction is still intentionally small.
But it is no longer symbolic.
It proves that primitive extraction can continue in code while the page composer remains case-scoped.

---

## What now looks like a plausible renderer seam

The following parts now look like the first plausible extraction candidates.

### 1. section shell primitives

These already behave more like reusable display primitives than case-specific prose:

- section shell
- section kicker
- section intro
- section nav label
- card grid shell
- footer shell

They are renderer-level framing elements, not `power-posing` facts.

### 2. route-card primitives

The current page now has a more legible public-layer route surface:

- claim-route card
- source-route card
- route-card tone classes
- chip/link grouping inside route cards

This looks like a real renderer seam because the pattern is not unique to this case, even though the current card copy still is.

### 3. lineage-rail primitive

The renderer now exposes a compact lineage rail for:

- original claim
narrowing into
- weaker descendant claim

The exact case semantics are still specific.
But the **display pattern** — ordered claim relation rendered as a rail rather than hidden in scattered links — now looks like a real reusable UI primitive.

### 4. grouped source-stack primitive

The source layer now renders as:

- grouped source stacks
- role-toned source cards
- split source subroutes (`Source routes` / `Touches objects`)

Again, the current grouping rules are still case-bound.
But the component pattern is no longer purely accidental.

### 5. status / timeline / footer display primitives

The current renderer now also exposes a second small cluster of reusable display units:

- judgment/status card surface
- standard section card surface
- timeline item surface
- footer card surface

These units still live inside a case-scoped page.
But they no longer need to be redefined inline for each section.

---

## What remains clearly case-scoped

The following parts should **not** yet be extracted as if they were generic.

### 1. generator assumptions

Still clearly case-bound:

- `snapshot-v2.md` as upstream release source
- `references-metadata-v1.md` as the canonical source metadata layer
- current file paths under `power-posing`
- current object-family assumptions
- the exact `window.POWER_POSING_PAGE_DATA` contract name and payload shape

### 2. section registry semantics

Still clearly case-bound:

- `Why this case matters`
- `Current object neighborhoods`
- `Public claim and source routes`
- `Canonical source ids`
- `Reading path`

These are not yet a neutral public-layer section grammar.
They are the current `power-posing` page composition.

### 3. source grouping rules

The present grouping between:

- core scientific record
- public circulation and retreat context

is a useful renderer move,
but it is currently driven by this case’s own source population.
That taxonomy must not be misdescribed as general literature ontology.

### 4. lineage cardinality assumptions

The current lineage rail implicitly assumes a short ordered chain.
That is appropriate here.
It is not yet a proof that the same renderer path can lawfully absorb broader claim-graph structures.

### 5. page composition logic

`render.js` still remains intentionally case-scoped.
It composes:

- this case’s section order,
- this case’s source grouping,
- this case’s reading-path logic,
- and this case’s current public-layer emphases.

That is still correct.
The extraction so far does **not** change that ruling.

---

## The lawful next extraction move

If a later phase wants to continue acting on this seam, the most lawful next move is:

> keep extracting **renderer primitives first**, not generator governance first.

Concretely, that means:

1. keep the generator case-scoped for now,
2. keep `render.js` as the case composer,
3. continue moving only display primitives that no longer depend on `power-posing` wording,
4. describe a tiny section-registry interface only after more than one case exists,
5. wait for a second case before claiming generic renderer closure.

This remains the key discipline:

> **primitive extraction before system-level genericization**

That avoids fake generality.

---

## What should not happen next

The following moves would still be premature:

- renaming the current page stack as a multi-case renderer
- pretending the generator is already a public-layer compiler
- replacing current case-earned wording with abstract generic placeholders
- extracting source taxonomy as if it were already cross-case stable
- claiming graph-browser capability from a short lineage rail
- collapsing the case composer into a fake universal runtime

That would be theater, not engineering.

---

## Short practical consequence

So the current practical consequence is:

- **yes** to renderer-component hardening,
- **yes** to seam identification,
- **yes** to first primitive extraction,
- **yes** to second-wave primitive extraction,
- **no** to fake generic closure,
- **no** to broad renderer extraction before a second case exists.

This is still the first renderer seam.
It should be treated as a **protected future extraction boundary**, not as a completed general renderer system.
