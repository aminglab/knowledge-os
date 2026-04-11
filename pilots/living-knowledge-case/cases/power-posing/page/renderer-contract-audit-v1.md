# Renderer contract audit v1

This note records a **small renderer-side contract audit** for the current `power-posing` public page stack.

Scope is intentionally narrow.
It audits only the current relationship between:

- `page-data.js`
- `renderer-primitives.js`
- `render.js`

It does **not** attempt a generator-seam redesign.
It only asks:

> do these three current layers still fit together honestly,
> and where are the first drift risks starting to appear?

---

## Executive ruling

Current ruling:

> **The current renderer contract still holds.**
> **But several composer-side assumptions are still implicit rather than machine-readable.**

So the page is not in contract failure.
But it is now mature enough that the first drift risks can be named precisely.

---

## The current contract, compressed

At the current stage, the page line works because the following unwritten agreement still holds.

### 1. `page-data.js` provides the public content payload

It currently provides:

- hero fields
- judgment links and status cards
- generic `sections[]`
- timeline entries
- source entries
- reading-path links
- footer fields

### 2. `renderer-primitives.js` provides reusable display units

It currently provides:

- shell primitives
- card primitives
- lineage primitive
- timeline primitive
- source display primitives
- footer primitive

### 3. `render.js` composes this specific case

It currently decides:

- which section title maps to which section options
- which section body uses which primitive family
- which source ids belong to which grouped source surface
- which source tone class is applied
- which link collection is mounted where

That composer contract still works.
But it works partly by implication rather than by explicit machine-readable hints.

---

## Contract areas that currently look healthy

The following parts currently look stable enough.

### A. primitive mounting boundary

The primitive layer now cleanly accepts content objects and returns DOM nodes.
`render.js` consumes those primitives without redefining them inline.

That boundary is healthier than before.

### B. section shell interface

The minimal section-shape interface named in `section-registry-interface-v1.md` is consistent with the current composer behavior.

That means:

- section shell,
- options,
- and mounted body

currently line up without contradiction.

### C. footer / timeline / card mounting

The second-wave primitive extraction reduced duplication in a real way.
Those display surfaces now look less likely to drift independently.

---

## First visible drift risks

The following are the first concrete drift risks.

### 1. title-driven section dispatch

`render.js` still uses current section titles as part of its composition logic.

Examples of current risk shape:

- route-section behavior is keyed off the current route-section title
- section options are keyed by current visible section title strings

That is acceptable right now.
But it means a future rename of section titles could silently change composition behavior if the note and the data drift apart.

This is not yet failure.
It is a **rename-coupling risk**.

### 2. label-driven source-link splitting

The source layer still splits link meaning by checking whether a link label begins with `Open source`.

That means current semantics partly depend on display wording.
If a future wording pass changes link labels while keeping the same structural intent, the source-route / object-touch split could drift.

This is the clearest current **presentation-text coupling risk**.

### 3. id-driven source grouping

The grouped source surface is still composed by current hard-coded source-id sets.

That is lawful inside one case.
But it means the composer is still carrying source-group semantics in local logic rather than receiving them from a machine-readable payload field.

This is a **case-local taxonomy coupling risk**.

### 4. card-shape divergence inside `page-data.js`

Not all cards in `page-data.js` share the same body fields.

Examples:

- status cards use `summary`
- standard / route cards use `body`

This is not necessarily wrong.
But it means the page-data card family is already plural, while the contract is still only lightly named.

This is a **card-family naming risk**, not yet a rendering failure.

### 5. composer hints are still implicit

The current page-data payload does not yet carry explicit composer hints such as:

- section kind
- card renderer family
- source link role
- source group key

So `render.js` must still infer more than it is told.

Again: not yet failure.
But it is the main reason this audit exists.

---

## What this audit does **not** conclude

This audit does **not** conclude that the contract is broken.
It also does **not** conclude that we should immediately push those meanings upstream into the generator.

That would be too early.

The current honest conclusion is smaller:

> the renderer contract still works,
> but the current composer depends on several implicit assumptions that are now visible enough to audit.

---

## Current recommended handling

Current handling should remain conservative.

### Keep as-is for now

For now it is still lawful to keep:

- title-driven section option lookup
- id-driven source grouping
- local tone classification
- current card-family split

because this is still a single real case.

### But treat the following as protected audit targets

The next time this page line changes materially, re-check these four areas first:

1. section title changes
2. source link label wording changes
3. source id set changes
4. page-data card-field shape changes

That is the real use of this audit.

---

## The next lawful upgrade, if later needed

If drift pressure increases later, the first lawful upgrade should still be **small**.

Not a generator redesign.
Not a fake generic renderer schema.

The first lawful upgrade would instead be one or more tiny machine-readable hints such as:

- `section_kind`
- `card_family`
- `source_link_role`
- `source_group_key`

But that upgrade should happen only when the current implicit coupling starts causing real friction.

Right now the audit does **not** claim that threshold has been crossed.

---

## Practical verdict

So the practical verdict is:

- **contract still passes**
- **no immediate renderer-seam rewrite needed**
- **implicit composer assumptions now formally identified**
- **future drift most likely to appear first in title / label / source-id coupling**

That is enough for the current stage.
