# source-page-seed-surface-v1

## Status

Seed-surface note v1.

## Function

This document defines the first **Source Page seed surface** for the public layer of Knowledge OS.

It follows the current Phase 3 chain:

- `phase-3-direction-decision-v1.md`
- `public-layer-foundation-v1.md`
- `public-layer-ia-v1.md`
- `public-layer-seeding-order-v1.md`
- `home-seed-surface-v1.md`
- `case-index-seed-surface-v1.md`

That chain has already established:

1. the public layer now exists in seed form,
2. the minimum public-layer page universe is larger than one case page,
3. the seeding order is currently **Home → Case Index → Source Page → Claim Page**,
4. and Source Page should be seeded before Claim Page because the repository already contains a stronger partial source surface than a public claim-page surface.

This document therefore answers the next practical question:

> What is the smallest honest Source Page surface that should exist after Home and Case Index?

This is not a final source-system spec.
It is the minimum credible public source surface for the current stage.

---

## Why Source Page should be seeded now

The repository already proved something important during Phase 2:

- source visibility is not enough,
- source usability matters.

That lesson already appears in the current public case line.
The public reader can already see:

- canonical source ids,
- source titles,
- metadata entries,
- and the objects that use them.

So Source Page is not a speculative new direction.
It is the formalization of a value the repository has already earned.

At the current stage, Source Page should come now for three reasons.

### 1. Because source surfaces are already partially real

The repository already contains:

- `references.md`
- `references-metadata-v1.md`
- source references inside object files
- source cards and routes in the public case surface

That means Source Page does not start from zero.

### 2. Because public traceability is one of the strongest real values of the current case

The current `power-posing` case is already stronger because a reader can move from public narrative into source grounding.
That should now become a first-class page type rather than remain only a cluster of adjacent files and links.

### 3. Because Source Page is structurally lighter than Claim Page

Claim Page requires deeper public decisions about claim-level judgment, grouping, lineage rendering, and object-level reading burden.
Source Page is more immediately ready because the current public layer already has a clear source vocabulary and a partially structured source surface.

So Source Page is the correct next seed.

---

## Core definition

The **Source Page seed** is the smallest public-facing surface that lets a reader understand what a source is, why it matters, and how it participates in one or more living knowledge cases.

A short definition is:

> Source Page is the minimum public surface that turns a source from a reference entry into a traceable participant in living knowledge.

That last phrase matters.
The Source Page is not just bibliographic storage.
It is a public-facing participation surface for a source inside the knowledge graph.

---

## What Source Page should accomplish

The Source Page seed should accomplish five things.

### 1. Establish source identity

A reader should be able to see what this source is without guessing from a raw id.

### 2. Explain source role

A source should not appear only as a title and a link.
The reader should understand why this source matters inside the case.

### 3. Expose object usage

A reader should be able to see which governed objects use the source.
That is what begins to make the source surface feel like part of living knowledge rather than part of a static bibliography.

### 4. Expose case usage

A reader should be able to tell which public case or cases the source participates in.
At the current stage this may only mean one case.
That is acceptable.

### 5. Stay honest about scope

The Source Page seed should not pretend to be a global literature browser, scholarly search engine, or universal citation explorer.
Its job is narrower:

- make public source participation legible,
- make source grounding navigable,
- and make source role visible in public living cases.

---

## What Source Page should not try to do

The Source Page seed should remain small on purpose.
It should not try to become any of the following.

### 1. Not a full bibliography manager

The Source Page is not meant to replicate a full citation-management system.

### 2. Not a global search engine

This is not yet the stage for advanced cross-source search or discovery tooling.

### 3. Not a giant metadata wall

The seed should not dump every possible metadata field onto the page just because they exist.
The page should stay public-facing and intelligible.

### 4. Not a replacement for object pages
nA Source Page can show which objects use a source. It should not try to reproduce full object content.

### 5. Not a general public library catalog

The Source Page should remain attached to the logic of living knowledge cases.
It is not just a catalog of papers floating in abstraction.

---

## Minimum Source Page structure

The Source Page seed should contain six blocks.

### Block 1. Source identity block

Purpose:

- establish what source this is.

Minimum contents:

- source title,
- canonical source id,
- canonical locator when available,
- and a short type label if useful.

This block should make the source legible at one glance.

---

### Block 2. Source role block

Purpose:

- explain why this source matters inside the case.

Minimum contents:

- short role statement,
- whether the source is foundational, dissenting, methodological, corrective, amplifying, or otherwise relevant,
- and a compact note on how it enters the case.

This block is one of the most important ones, because it shifts the page from bibliography to public reasoning surface.

---

### Block 3. Case usage block

Purpose:

- show which public case or cases use the source.

Minimum contents:

- case name,
- short usage note,
- and route back into the case page or current public homepage.

At the current stage, one case is enough.
The page type should still be designed as repeatable.

---

### Block 4. Object usage block

Purpose:

- expose which governed objects use the source.

Minimum contents:

- object ids,
- object titles if useful,
- object family labels,
- and route into the relevant object or public case surface.

This is the block that most strongly distinguishes a Source Page from a plain bibliography entry.

---

### Block 5. Public reading route block

Purpose:

- help a reader move from the source back into the public-layer ecology.

Minimum contents:

- route to case page,
- route to current public homepage,
- route to case index or public entry,
- and optionally route to related sources later if that becomes useful.

The Source Page should always feel connected to a larger public reading system.

---

### Block 6. Current-stage honesty block

Purpose:

- keep the Source Page seed honest about maturity.

Minimum contents:

- this is an early first-class public source surface,
- it is not yet a general source explorer,
- and it exists to strengthen traceability inside the first seeded public-layer ecology.

---

## Minimum source card contract

The Source Page seed should also stabilize the minimum contract of a source as a public-facing page object.

A source card or source page should answer at least six questions:

1. What is this source?
2. Where does it live canonically?
3. Why is it relevant here?
4. Which case uses it?
5. Which objects use it?
6. Where should the reader go next?

At the current stage, that is enough to turn the source surface into a real part of the public layer.

---

## Relationship to the current repository

The Source Page seed should be built from current repository reality rather than invented from scratch.

### Current thin reader-facing source entry
Already grounded by:

- `references.md`

### Current stable source metadata layer
Already grounded by:

- `references-metadata-v1.md`

### Current governed usage source
Already grounded by:

- object `source_refs`
- snapshot source references
- page-level source cards

### Current public traceability source
Already grounded by:

- `snapshot-v2.md`
- current `power-posing` page
- Phase 2 source-surface hardening already recorded in repository closeout notes

This means the Source Page seed is not a theory-first artifact.
It is an extraction and elevation of a source surface that already exists in partial form.

---

## Source Page versus references.md

This boundary matters.

### `references.md`

The current `references.md` is:

- reader-facing,
- thin,
- and entry-oriented.

It is useful as a compact source map.

### Source Page

The Source Page should be:

- public-facing,
- role-aware,
- usage-aware,
- and route-rich.

It should still be readable.
But it should go beyond a flat reference list.

So the Source Page should not replace `references.md` immediately.
It should grow from it.

---

## Source Page versus references-metadata-v1.md

This boundary matters just as much.

### `references-metadata-v1.md`

That file is:

- stable metadata layer,
- machine- and governance-friendly,
- and part of the internal release-support structure.

### Source Page

The Source Page should be:

- public-facing,
- interpretive only where the current case has already earned interpretation,
- and centered on public role and usage.

So the Source Page is not a prettier version of `references-metadata-v1.md`.
It is a different surface with a different reader contract.

---

## Source Page versus Claim Page

This boundary is the reason Source Page is seeded first.

### Source Page

Source Page asks:

- what is this source,
- why does it matter,
- where is it used,
- and where do I go next?

### Claim Page

Claim Page asks:

- what is this claim,
- what is its current judgment,
- what supports it,
- what attacks it,
- and how does it sit in lineage?

Claim Page is more judgment-heavy and more structurally demanding.
That is why Source Page comes first.

---

## Engineering consequence

From an engineering point of view, the Source Page seed does three useful things.

### 1. It turns existing source surfaces into a first-class public page type

That reduces the gap between current source metadata and future public source experience.

### 2. It strengthens public traceability without requiring deeper public object rendering first

This is a high-value move because the current case is already strongest where it is most traceable.

### 3. It creates a stable bridge between case-level reading and later claim-level public navigation

Once Source Page exists, the public layer will have a more balanced ecology:

- system entry,
- case listing,
- case reading,
- source grounding.

That makes Claim Page easier to seed later into a cleaner structure.

---

## Current implementation stance

The Source Page seed does not yet require a complex app shell or a new search system.

The honest current implementation posture is:

- treat the existing source metadata and source routes as raw material,
- keep the first Source Page small,
- keep it case-aware,
- and prefer clear role + usage + routing over large metadata display.

In practical terms, the first Source Page could be represented as a light public page per canonical source id, derived from current metadata plus object usage and case links.

That is enough for a seed.

---

## Current stage verdict

Current verdict:

> The next public-layer seed after Home and Case Index should be a true Source Page surface.
>
> That surface should not try to become a literature browser or metadata warehouse.
>
> It should become the smallest honest public page that makes source identity, source role, object usage, and case participation visibly traceable.

That is the current Source Page seed ruling.

---

## Immediate next step

If this document is accepted, the next natural continuation is:

- `claim-page-seed-surface-v1.md`

That would complete the current public-layer seeding order already set by the repository.

---

## Consolidated closing sentence

The current repository has already proved that sources should be visible and usable.
The Source Page seed is the next step that turns that proof into a first-class public page type.
Its job is not to become a giant bibliography product. Its job is to make public grounding feel real.
