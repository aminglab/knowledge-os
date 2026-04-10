# case-index-seed-surface-v1

## Status

Seed-surface note v1.

## Function

This document defines the first **Case Index seed surface** for the public layer of Knowledge OS.

It follows the current Phase 3 chain:

- `phase-3-direction-decision-v1.md`
- `public-layer-foundation-v1.md`
- `public-layer-ia-v1.md`
- `public-layer-seeding-order-v1.md`
- `home-seed-surface-v1.md`

That chain has already established:

1. the public layer now exists in seed form,
2. the minimum public-layer page universe is larger than one case page,
3. the seeding order begins with **Home**, then **Case Index**,
4. and Home is responsible for system-level public entry rather than case-level identity.

This document therefore answers the next practical question:

> What is the smallest honest Case Index surface that should exist after Home?

This is not a final product listing spec.
It is the minimum credible listing surface for public cases.

---

## Why Case Index must follow Home

At the current repository stage, one real public case already exists:

- `power-posing`

That is enough to prove that a public case can be made real.
But it also creates a structural distortion.

Without a Case Index surface, the public layer risks reading as if:

- the first case is the whole public layer,
- or the public layer is simply one featured page plus some repository files.

That is a transitional convenience, not a good information architecture.

Once Home exists as the public front door, the next structural need is a listing layer that says:

- public cases are a category,
- this first case is one member of that category,
- and the public layer is a growing ecology of cases rather than one isolated artifact.

So the Case Index seed is not busywork.
It is the first explicit surface that makes the public layer plural, even while it is still small.

---

## Core definition

The **Case Index seed** is the smallest public listing surface that presents public cases as a real category inside Knowledge OS rather than as one accidental page.

A short definition is:

> Case Index is the minimum public listing surface that situates the first public case as the first member of a broader case layer.

---

## What Case Index should accomplish

The Case Index seed should accomplish five things.

### 1. Establish public cases as a first-class category

A reader should immediately understand that a public case is a specific kind of public-layer artifact.

### 2. Stop the first case from being mistaken for the whole public layer

The index should make it structurally obvious that the first case is featured because it is first, not because it exhausts the system.

### 3. Bridge Home to Case Page

Home should not route straight from system identity into a single case without any intermediate case-layer structure.
Case Index provides that bridge.

### 4. Introduce what a case card is

The Case Index should define the minimum representation of a public case as a listable object.
That matters for later multi-case growth.

### 5. Stay honest about stage

The Case Index should not pretend there are many mature public cases already.
A one-card index is still structurally valid if it is honest.

---

## What Case Index should not try to do

The Case Index seed should remain small on purpose.
It should not try to become any of the following.

### 1. Not a search product

This is not yet the stage for search-first public discovery.

### 2. Not a filter-heavy explorer

The index should not pretend to have a rich taxonomy, query system, or faceted browsing layer before there is enough public material to justify it.

### 3. Not a public governance dashboard

The Case Index is not where public readers should see every unresolved dissent, deep object graph, or internal workflow signal.

### 4. Not a marketing showcase grid

The goal is not to create the visual impression of scale before the public layer has actually earned it.

### 5. Not a replacement for the case page itself

The index should help a reader choose and enter a case.
It should not absorb the actual reading surface of the case.

---

## Minimum Case Index structure

The Case Index seed should contain four blocks.

### Block 1. Index identity block

Purpose:

- establish what this page is.

Minimum contents:

- page title,
- short sentence explaining what a public case is inside Knowledge OS,
- and a short note that this is an early public-layer listing surface.

This block should orient the reader before any case card appears.

---

### Block 2. Case-layer explanation block

Purpose:

- explain why cases exist as a public-layer form.

Minimum contents:

- a case is not just an article,
- it is a public release view over governed knowledge objects,
- it exposes current judgment, source traceability, and lineage in reader-facing form.

This block should stay shorter than the Home explanation block.
Its job is to define the category, not re-explain the whole system.

---

### Block 3. Case card block

Purpose:

- present one or more public cases.

At the current stage, one case card is enough.
But the card format must already be conceived as a repeatable page object.

Each case card should minimally expose:

- case title,
- one-paragraph synopsis,
- current visible judgment summary,
- why this case matters,
- and route into the case page.

Optional but useful fields:

- case type,
- release identity,
- current public layer status,
- whether it is the first public case or a later addition.

---

### Block 4. Current-stage honesty block

Purpose:

- keep the index from overclaiming scale.

Minimum contents:

- a sentence that this is the first public case index,
- that the current public layer is still early,
- and that the first case is the first seeded case surface, not evidence of a fully populated public catalog.

This is important because the Case Index will otherwise tempt the project to perform scale rather than state reality.

---

## Minimum case card contract

The Case Index seed should also define the minimum contract of a public case card.
That contract matters even before multiple cases exist.

A public case card should answer six questions at a glance:

1. What is the case called?
2. What kind of dispute or knowledge surface is it?
3. What is the current visible judgment?
4. Why does this case matter?
5. What kind of public artifact will I enter if I click?
6. Why is this case here now?

At the current stage, the `power-posing` card should therefore expose:

- title,
- dispute type,
- current visible judgment in compressed form,
- significance sentence,
- and route into the case page.

This is enough for a seed.

---

## Relationship to the current repository

The Case Index seed should not be written from abstraction alone.
It should be built from current repository reality.

### System-level public framing
Already grounded by:

- `README.md`
- `FOUNDING.md`
- `home-seed-surface-v1.md`

### Public case meaning
Already grounded by:

- `public-layer-foundation-v1.md`
- `public-layer-ia-v1.md`

### First case card source
Already grounded by:

- `snapshots/snapshot-v2.md`
- current `power-posing` page
- `phase-2-closeout-v1.md`

### Current-stage honesty
Already grounded by:

- `phase-3-direction-decision-v1.md`
- `public-layer-seeding-order-v1.md`

This means the Case Index seed should be treated as a compositional and IA task, not as a new strategy task.

---

## Case Index versus Home

This boundary matters.

### Home

Home answers:

- what this system is,
- why the public layer exists,
- and where public reading begins.

### Case Index

Case Index answers:

- what a public case is,
- what public cases currently exist,
- and which case the reader should enter.

So Case Index should not re-expand into full system explanation.
It should sit one level below Home.

---

## Case Index versus Case Page

This boundary matters just as much.

### Case Index

Case Index is:

- selection surface,
- category surface,
- and public listing surface.

### Case Page

Case Page is:

- reading surface,
- judgment surface,
- and narrative-plus-traceability surface.

So the Case Index should summarize and route.
It should not attempt to reproduce full case reading.

---

## Engineering consequence

From an engineering point of view, the Case Index seed does three useful things.

### 1. It turns the first case into a listable object

That is important because public-layer growth later depends not only on more pages, but on stable listable page objects.

### 2. It gives Home a proper downstream handoff

Without Case Index, Home either routes too directly into the first case or becomes awkwardly abstract.

### 3. It creates a stable insertion point for later cases

Once the Case Index exists, later public cases can be added to a known surface instead of forcing another restructuring of public entry.

That is exactly the sort of early structural win that prevents later ad hoc growth.

---

## Current implementation stance

The Case Index seed does not need a complex frontend build or deep data model before it can be defined.

At the current stage, the honest implementation posture is:

- define the seed contract first,
- keep the first index small,
- allow one real case card,
- and prioritize structural clarity over feature richness.

That means the next practical build step after this note would likely be a small public listing surface, not a search platform.

---

## Current stage verdict

Current verdict:

> The public layer now needs a Case Index seed surface directly after Home.
>
> That surface should not pretend to offer scale, search, or rich discovery.
>
> It should simply establish public cases as a real category, situate `power-posing` as the first public case, and create a stable bridge from Home into case-level reading.

That is the current Case Index seed ruling.

---

## Immediate next step

If this document is accepted, the next natural continuation is:

- `source-page-seed-surface-v1.md`

The seeding-order ruling already placed Source Page before Claim Page.
That means the next step after Case Index should be to define how the already-partial source surface becomes a first-class public page type.

---

## Consolidated closing sentence

Case Index is the first listing surface of the public layer.
Its job is not to simulate scale.
Its job is to make the first public case readable as the first member of a broader category, so that the public layer stops looking like one accidental page and starts looking like a real, if still small, public system.
