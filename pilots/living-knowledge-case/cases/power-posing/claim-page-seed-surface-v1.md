# claim-page-seed-surface-v1

## Status

Seed-surface note v1.

## Function

This document defines the first **Claim Page seed surface** for the public layer of Knowledge OS.

It follows the current Phase 3 chain:

- `phase-3-direction-decision-v1.md`
- `public-layer-foundation-v1.md`
- `public-layer-ia-v1.md`
- `public-layer-seeding-order-v1.md`
- `home-seed-surface-v1.md`
- `case-index-seed-surface-v1.md`
- `source-page-seed-surface-v1.md`

That chain has already established:

1. the public layer now exists in seed form,
2. the minimum public-layer page universe is larger than one case page,
3. the seeding order is currently **Home → Case Index → Source Page → Claim Page**,
4. and Claim Page comes last in this first seeding pass because it is the most judgment-heavy and object-facing public page type in the current public-layer universe.

This document therefore answers the next practical question:

> What is the smallest honest Claim Page surface that should exist after Home, Case Index, and Source Page?

This is not a final object-browser spec.
It is the minimum credible claim-centered public page for the current stage.

---

## Why Claim Page comes now, and not earlier

Claim Page has always mattered.
But it was correctly not seeded first.

That was the right order for three reasons.

### 1. Because system-level entry had to be clarified first

Before Claim Page could become a first-class public page type, the public layer needed:

- a system entry,
- a public case listing surface,
- and a stronger source-grounding surface.

Without those earlier surfaces, a Claim Page would have landed into a public layer with weak framing and too much burden on one page type.

### 2. Because Claim Page is the first deeply object-facing public page type

Case Page is still partly narrative.
Source Page is grounding-oriented.
Claim Page is where the public layer starts to expose the object model more directly.

That makes it valuable.
It also makes it dangerous to rush.

### 3. Because Claim Page carries the heaviest judgment burden

A Source Page can explain source role and usage.
A Claim Page must do more:

- expose the claim itself,
- expose current visible judgment,
- expose support and attack relations,
- and place the claim inside a lineage without drowning the reader.

That is why Claim Page comes last in this first seeding cycle.

---

## Core definition

The **Claim Page seed** is the smallest public-facing surface that lets a reader understand what a claim is, how it currently stands, what supports it, what challenges it, and how it sits inside a larger claim lineage.

A short definition is:

> Claim Page is the minimum public surface that turns a claim from a sentence in a case narrative into a traceable governed object with visible standing.

This is the moment where the public layer most clearly stops looking like a set of pages and starts looking like an object-aware public system.

---

## What Claim Page should accomplish

The Claim Page seed should accomplish six things.

### 1. Establish claim identity

A reader should know exactly what the claim is, not only what the case is about in general.

### 2. Expose current visible judgment

The claim’s current public standing should be legible immediately.
This is one of the core reasons the page exists.

### 3. Expose support surface

A reader should be able to see what evidence or basis currently supports the claim.

### 4. Expose challenge surface

A reader should be able to see what dissent, attack, weakness, or unresolved objection currently bears on the claim.

### 5. Place the claim in lineage

A reader should understand whether the claim is:

- original,
- descendant,
- narrowed,
- split,
- or otherwise positioned relative to neighboring claims.

### 6. Stay readable

Even though Claim Page is the most object-facing page type in this seeding round, it should still remain public-facing and readable.
It should not become a wall of object references and jargon.

---

## What Claim Page should not try to do

The Claim Page seed should stay narrow on purpose.
It should not try to become any of the following.

### 1. Not a full graph explorer

The page should not attempt to show the whole object graph at once.
That would turn the public layer into a maze.

### 2. Not a raw object dump

Claim Page should not simply reproduce full markdown object files with minimal translation.

### 3. Not a theorem-style dossier

The page should remain a public reading surface, not a maximal technical case file.

### 4. Not a universal public judgment console

The page can expose current visible judgment.
It should not pretend to provide every internal governance state or every unresolved workflow detail.

### 5. Not a replacement for the case page

Claim Page should deepen and localize reading.
It should not replace the case page’s role as the main narrative entry to a case.

---

## Minimum Claim Page structure

The Claim Page seed should contain seven blocks.

### Block 1. Claim identity block

Purpose:

- establish what the claim is.

Minimum contents:

- claim title,
- claim id,
- short claim statement,
- and a short type or role label if useful.

This block should let a reader identify the claim at once.

---

### Block 2. Current visible judgment block

Purpose:

- expose the claim’s current public standing.

Minimum contents:

- visible status phrase,
- linked verdict surface,
- and a short explanation of what that status means in this case.

This block should remain visibly tied to the current verdict grammar and status legend discipline already earned by the case.

---

### Block 3. Why this claim matters block

Purpose:

- explain why this claim matters inside the case.

Minimum contents:

- one short paragraph explaining the claim’s role,
- whether it is the original headline claim, a narrower descendant, or another important route.

This block prevents the page from feeling like a sterile claim record.

---

### Block 4. Support surface block

Purpose:

- show the current support-bearing objects or evidence routes.

Minimum contents:

- supporting evidence objects,
- source links where useful,
- and short explanation of what kind of support is being claimed.

This block should stay selective.
It is not a full evidence warehouse.

---

### Block 5. Challenge surface block

Purpose:

- show the strongest current challenge-bearing objects.

Minimum contents:

- dissent objects,
- challenge types if useful,
- and a short explanation of what kind of pressure they create.

This block matters because a living claim without visible challenge is just a polished summary wearing a fake mustache.

---

### Block 6. Lineage placement block

Purpose:

- place the claim inside the larger case lineage.

Minimum contents:

- whether this is the original claim or a descendant,
- relation to adjacent claims,
- and route back into the case-level lineage path.

This block is especially important in cases like `power-posing`, where the weaker descendant claim is not just a rewording but a lineage event.

---

### Block 7. Public reading routes block

Purpose:

- route the reader back into the larger public-layer ecology.

Minimum contents:

- route to Case Page,
- route to Source Page where useful,
- route to Case Index,
- and route to the current public homepage.

The Claim Page should always feel like a node in a readable system, not a dead-end leaf.

---

## Minimum claim card contract

The Claim Page seed should also stabilize the minimum contract of a claim as a public-facing page object.

A claim page or claim card should answer at least seven questions:

1. What is this claim?
2. What is its current visible judgment?
3. Why does this claim matter in the case?
4. What currently supports it?
5. What currently challenges it?
6. Where does it sit in lineage?
7. Where should I go next?

That is enough to make the page useful without overbuilding it.

---

## Relationship to the current repository

The Claim Page seed should be built from current repository reality rather than imported from theory alone.

### Current claim identity source
Already grounded by:

- claim object files under `objects/claims/`
- `snapshot-v2.md`
- current case page routes

### Current visible judgment source
Already grounded by:

- verdict objects,
- `verdict-grammar-v1.md`,
- `status-legend-v1.md`,
- and the current snapshot judgment surface.

### Current support and challenge source
Already grounded by:

- evidence objects,
- dissent objects,
- source refs,
- and current case-level reading paths.

### Current lineage source
Already grounded by:

- `C-0001` / `C-0002` relation in the current case,
- snapshot discussion of original and descendant claim,
- and timeline support.

This means Claim Page is not a new metaphysical ambition.
It is the public-page elevation of already-governed claim structure.

---

## Claim Page versus Case Page

This boundary matters.

### Case Page

Case Page is:

- primary narrative entry,
- case-level reading surface,
- and public homepage for the case.

### Claim Page

Claim Page is:

- localized object-facing reading,
- claim-level standing surface,
- and route into support / challenge / lineage for one claim.

So Claim Page should deepen the case.
It should not replace the case page’s role as the main public entry to the case.

---

## Claim Page versus Source Page

This boundary matters just as much.

### Source Page

Source Page asks:

- what is this source,
- why does it matter,
- where is it used,
- and where do I go next?

### Claim Page

Claim Page asks:

- what is this claim,
- what is its standing,
- what supports it,
- what challenges it,
- and where does it sit in lineage?

The two pages should cross-link, but not collapse into each other.
One is grounding-centered.
The other is claim-centered.

---

## Claim Page versus raw claim object file

This boundary is the one most likely to go wrong.

### Raw claim object file

The raw claim object file is:

- internal working object,
- governance-bearing,
- and not written first for public reading ease.

### Claim Page

Claim Page should be:

- public-facing,
- compressed,
- route-rich,
- and visibly tied to governed standing without exposing every internal detail.

So the Claim Page should not simply mirror the markdown object file line by line.
It should translate it into a public page contract.

---

## Engineering consequence

From an engineering point of view, the Claim Page seed does three useful things.

### 1. It completes the first public-layer seeding order

Once Claim Page is defined, the current seeding cycle becomes complete:

- Home,
- Case Index,
- Source Page,
- Claim Page.

### 2. It makes the public layer genuinely object-aware

This is the page type where the public layer most clearly begins to expose governed object identity as public reading structure.

### 3. It creates the cleanest bridge toward later richer public interaction

If the project later wants richer claim navigation, filtered evidence routes, or lineage-centered views, Claim Page is the most natural stepping stone.

That is why it is worth defining carefully now instead of improvising later.

---

## Current implementation stance

The Claim Page seed does not yet require a graph UI, route engine, or full object-browser shell.

The honest current implementation posture is:

- keep the first Claim Page small,
- make judgment legible first,
- expose only the strongest support and challenge routes,
- and let lineage remain understandable without rendering the whole graph.

In practice, the first Claim Page could be represented as a light public page per public claim, derived from current claim objects, verdict objects, and already-established support/challenge relations.

That is enough for a seed.

---

## Current stage verdict

Current verdict:

> The next and final page type in the current public-layer seeding round should be a true Claim Page surface.
>
> That surface should not become a graph explorer, a raw object dump, or a maximal case dossier.
>
> It should become the smallest honest public page that makes claim identity, current visible judgment, support, challenge, and lineage all visible in one place.

That is the current Claim Page seed ruling.

---

## Immediate consequence

With this document in place, the current first seeding order is now fully defined.

That means the next natural work after this is no longer another seed-surface note by default.
It becomes one of two things:

1. begin mapping one or more of these seed surfaces into real repository-visible public artifacts,
2. or decide which seed should next receive a concrete implementation pass beyond documentation.

At the current repository stage, the most natural implementation-minded next step would be to choose whether:

- Source Page,
- or Claim Page,

is the next public-layer seed to receive a real repository-visible surface beyond note form.

---

## Consolidated closing sentence

Claim Page is the most object-facing page type in the current first public-layer seeding round.
That is why it was seeded last, not because it matters least, but because it requires the clearest boundaries. Its job is to make governed claim standing publicly readable without turning the public layer into a graph labyrinth.
