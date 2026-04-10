# public-layer-ia-v1

## Status

IA note v1.

## Function

This document defines the current **minimum information architecture** for the public layer at the start of Phase 3.

It follows `public-layer-foundation-v1.md`.
That earlier document answers:

- what the public layer is,
- why it exists,
- what role it plays,
- and what does and does not belong inside it.

This document answers the next question:

> if the public layer now exists in seed form, what is the minimum page universe it should grow into?

This is not a final product spec.
It is a first coherent IA boundary.

---

## IA principle

The public layer should not be modeled as one page plus optional extras.

It should be modeled as a small but coherent page universe.
That page universe must be large enough to support:

- public entry,
- public case reading,
- public source traceability,
- public claim navigation,
- and visible release continuity.

But it must also remain small enough that the project does not pretend to have already built a full public product shell.

So the governing IA rule is:

> define the minimum page universe that lets public living knowledge be entered, read, traced, and situated.

---

## Current IA center of gravity

At the current stage, the repository already contains one real public-layer seed:

- `power-posing` as first public case,
- `snapshots/snapshot-v2.md` as current public homepage for that case,
- and the current page renderer as a downstream public case page.

That means the public layer is no longer purely hypothetical.
But it is still anchored in one validated seed.

So this IA should be read as:

- grounded in what the current seed already proves,
- open to later expansion,
- but not yet generic in a full product sense.

---

## Minimum public-layer page universe

The minimum page universe should currently contain six page types.

### 1. Home

The public entry point for Knowledge OS as a system.

### 2. Case Index

The public listing surface for available or published cases.

### 3. Case Page

The main public reading surface for a single case.

### 4. Claim Page

A more atomic public reading surface centered on an individual claim.

### 5. Source Page

A public-facing source surface that exposes how a source participates in one or more cases.

### 6. Reading / Lineage Layer

A public path layer that lets a reader move through related claims, verdicts, sources, and release views over time.

These are the minimum page types because together they answer six different reader needs:

- Where am I?
- What cases exist?
- What is this case saying now?
- What is this claim?
- What grounds this?
- How did this get here?

---

## Page type 1: Home

### Function

Home is the public entry point into Knowledge OS as a public system.
It should tell a new reader:

- what this system is,
- what kind of objects or artifacts they are looking at,
- why this public layer exists,
- and where to start reading.

### It is not

Home is not:

- the private cockpit,
- a manifesto-only page,
- a developer README clone,
- or a dashboard pretending the whole product already exists.

### Minimum contents

Home should minimally contain:

- system one-sentence definition,
- short explanation of living knowledge vs static publication,
- public entry explanation,
- first public case entry card,
- and a path into the case index.

### Current implementation status

Not yet implemented as a distinct public page type.
Currently only implied by repository entry docs and the first case surface.

---

## Page type 2: Case Index

### Function

Case Index is the public listing surface for published or public-facing cases.

It should answer:

- what public cases exist,
- what state they are in,
- what kind of dispute or knowledge object they represent,
- and which one the reader should enter first.

### Why it matters now

Even though only one case is currently present, the page type should still be defined now.
Otherwise the project risks treating the first case as if it were the whole public layer.

### Minimum contents

A case card should expose at least:

- case title,
- short synopsis,
- visible current judgment summary,
- why the case matters,
- and link to case page.

### Current implementation status

Not yet implemented as a distinct page.
Currently represented implicitly by the repository and the single `power-posing` case.

---

## Page type 3: Case Page

### Function

Case Page is the main public reading surface for a single living case.

It should let a reader understand:

- what the case is,
- why it matters,
- what the current judgment is,
- what changed over time,
- and where to go deeper.

### Current seed implementation

The existing `power-posing` page is the first seed implementation of this page type.

But its upstream public release source remains `snapshots/snapshot-v2.md`.
The current page is downstream presentation, not the primary editorial authority.

### Minimum contents

A case page should minimally expose:

- case title,
- case identity,
- current visible judgment,
- why this case matters,
- key claim neighborhood,
- what changed later,
- source surface entry,
- reading path,
- and clear route into claims, verdicts, timeline, and sources.

### IA discipline

The case page should remain thinner than the fuller snapshot release path if needed.
Its role is public readability and navigation, not full governance duplication.

---

## Page type 4: Claim Page

### Function

Claim Page is the atomic public page type centered on one claim.

It should let a reader understand:

- what the claim is,
- how it is currently judged,
- what it depends on,
- what supports it,
- what attacks it,
- and how it relates to stronger or weaker descendants.

### Why this page type matters

Without a claim page, the public layer risks remaining case-only.
That would keep the public surface too coarse and too tied to narrative summary.

Claim Page is the first page type that begins to make the public layer feel object-aware rather than merely article-aware.

### Minimum contents

A claim page should minimally contain:

- claim title,
- current visible judgment,
- short claim statement,
- lineage placement,
- supporting evidence links,
- dissent links,
- linked verdicts,
- and source usage surface.

### Current implementation status

Not yet implemented as a distinct page.
Currently only reachable indirectly through markdown object files and case reading paths.

---

## Page type 5: Source Page

### Function

Source Page is the public-facing surface for a canonical source and its participation in living knowledge.

It should answer:

- what this source is,
- what role it plays,
- which objects use it,
- which cases use it,
- and how it contributes to the current public release surface.

### Why this page type matters

The current public surface already proved that source usability matters.
A reader needs more than a source id.
They need a way to understand source role, location, and usage.

### Minimum contents

A source page should minimally expose:

- source title,
- canonical locator,
- short role description,
- object usage,
- case usage,
- and link back into claims or case surfaces.

### Current implementation status

Partially seeded through `references.md` and `references-metadata-v1.md`, but not yet implemented as a first-class public page type.

---

## Page type 6: Reading / Lineage Layer

### Function

This is not necessarily one page.
It is the public path layer that helps a reader move through:

- case,
- claim,
- source,
- verdict,
- timeline,
- and release continuity.

It answers the question:

- how should a public reader move through this knowledge surface without getting lost?

### Why it matters

The public layer is not just a set of pages.
It is also a set of paths.
If the paths are missing, the page universe exists only formally.

### Minimum capabilities

The reading / lineage layer should let a reader do at least four things:

1. enter through a case,
2. go one layer deeper into claims and verdicts,
3. trace outward into sources,
4. move through time or lineage rather than only through prose order.

### Current implementation status

Already partially present through:

- `snapshot-v2.md` reading path,
- `README.md` public reading path,
- timeline surface,
- explicit object links,
- and source surface routes.

So unlike several other page types, the reading / lineage layer already exists in primitive but real form.

---

## Current reader journeys

The minimum IA should support at least three reader journeys.

### Journey A: first-time public reader

Question:

- What is this system?
- What kind of thing am I looking at?
- Where should I start?

Path:

- Home → Case Index → Case Page

### Journey B: case-first reader

Question:

- What is this case about?
- What is the current judgment?
- Why does it matter?
- Where do I go deeper?

Path:

- Case Page → Claim Page / Verdict-linked object route → Source Page / Timeline

### Journey C: source- or claim-driven reader

Question:

- I care about this claim or this source; where does it sit in the larger living knowledge surface?

Path:

- Claim Page or Source Page → Case Page → Reading / Lineage Layer

These journeys are enough for the current stage.
They do not require a full navigation shell yet.

---

## Current page-type implementation matrix

### Already real in seed form

- Case Page
- Reading / Lineage Layer

### Partially real but not first-class yet

- Source Page

### Not yet implemented as distinct public page types

- Home
- Case Index
- Claim Page

This matrix matters because it keeps the IA honest.
The project has more than zero.
But it has not yet built the whole universe.

---

## IA boundary rules

The public-layer IA should obey the following rules.

### 1. Do not confuse page types with internal tools

A public page type should describe a public release function, not an internal workspace surface.

### 2. Do not let page richness outrun release identity

If a public page becomes more interactive, it must still remain clear what the reader is seeing.

### 3. Do not collapse snapshot and page into one undefined surface

Snapshot remains the release authority.
Page remains downstream public rendering.
The IA should preserve that distinction.

### 4. Do not model everything as a case page

Claim-centered and source-centered public navigation should eventually become first-class.

### 5. Do not force genericity too early

The IA should define a page universe now without pretending the whole multi-case product shell already exists.

---

## What this IA does not do yet

This document does not yet specify:

- visual design system,
- routing implementation details,
- URL schema,
- exact component library,
- graph interaction model,
- filtering system,
- search surface,
- or authenticated reader states.

Those belong to later design and implementation passes.

This document only defines the minimum public-layer page universe and the logic that connects its parts.

---

## Relationship to current repository files

At the current stage, the page universe maps onto repository reality like this.

### System-level public entry

Currently approximated by:

- `README.md`
- `FOUNDING.md`

But not yet represented as a true public Home page.

### Current case page seed

Currently represented by:

- `pilots/living-knowledge-case/cases/power-posing/page/`
- with `snapshots/snapshot-v2.md` as release authority upstream.

### Current source surface seed

Currently represented by:

- `references.md`
- `references-metadata-v1.md`

### Current lineage / reading layer seed

Currently represented by:

- snapshot reading path,
- README public reading path,
- timeline,
- explicit object routes.

This mapping shows that the IA is not fantasy. It is an interpretation and ordering of real repository surfaces.

---

## Current IA verdict

Current verdict:

> The public layer now requires a minimum page universe rather than a single successful page.
>
> That page universe should currently be defined as:
> Home, Case Index, Case Page, Claim Page, Source Page, and Reading / Lineage Layer.
>
> Of these, the Case Page and Reading / Lineage Layer already exist in seed form, Source Page exists partially, and the remaining page types are defined but not yet implemented.

That is enough to guide the next product-thinking step without pretending the whole public-layer system is already complete.

---

## Immediate consequence

If this document is accepted, the next natural work is no longer another abstract phase note.
It becomes one of two things:

1. a light public-identity implementation pass that begins to separate system-level public entry from case-level entry,
2. or a small public-layer planning pass that decides which of the not-yet-first-class page types should be seeded next.

At the current repository stage, the most natural order would be:

- first clarify public entry identity,
- then decide whether to seed Home / Case Index,
- and only after that consider whether Claim Page or Source Page should become the next concrete implementation target.

---

## Consolidated closing sentence

The public layer should now be understood not as one public page, but as a minimum page universe.
The first `power-posing` case page proved that the layer can exist.
This IA note defines the smallest coherent public structure that can grow from that proof without overclaiming system maturity.
