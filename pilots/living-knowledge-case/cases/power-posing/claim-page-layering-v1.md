# Claim Page Layering v1

This note records the current **claim page layering rule** for the `power-posing` pilot.

It exists because the pilot has now crossed a real structural threshold:

- the governed object layer is being normalized toward a compact canonical relation floor,
- relation direction is now intentionally one-way,
- and raw object frontmatter is no longer trying to be both machine-safe protocol and human-friendly neighborhood map at the same time.

That is the right architectural move.
But it creates an obligation:

> if machine-layer relation semantics become stricter and more one-directional,
> the public claim surface must deliberately compensate by making support, challenge, and lineage legible to human readers.

---

## One-sentence ruling

Current ruling:

> **Claim object frontmatter is the machine-governed relation layer.**
> **Claim pages are the human-readable neighborhood summary layer.**

Do not collapse these jobs back into one file format.

---

## Why this note exists now

After the current relation migration, claim object frontmatter now prefers canonical directed relations such as:

- `supports`
- `challenges`
- `cites`
- `descends_from`

That improves protocol clarity.
It reduces synonym drift.
It makes agent-authored graph updates much safer.

But it also means a claim object like `C-0001` may now carry several `cites` links in frontmatter where an older pilot might have used reverse labels such as:

- `supported_by`
- `attacked_by`
- `ruled_on`
- `splits_to`

That loss of reverse convenience is acceptable at the machine layer.
It should **not** be left uncompensated at the public reading layer.

---

## Layer split

### Layer A. governed object frontmatter

This layer is for:

- machine-legible object identity,
- canonical directed relation semantics,
- minimal governed metadata,
- and reliable protocol checking.

This layer should prefer compact canonical relation naming.
It should not be stretched into a reader-optimized neighborhood atlas.

### Layer B. claim page neighborhood summary

This layer is for:

- visible judgment,
- support surface,
- challenge surface,
- lineage placement,
- and public reading routes.

This layer is where the pilot restores quick human intelligibility.
It is not replacing the governed graph.
It is making the governed graph readable.

---

## Current minimum claim-page obligations

At the current stage, each public claim page should expose at least the following sections:

### 1. `Current visible judgment`

This section gives the reader a direct answer to:

- what is the current public reading of this claim,
- and which verdict object currently governs that reading.

Minimum expectations:

- a visible current state phrase,
- a linked verdict object.

### 2. `Support surface`

This section makes positive grounding legible.

Minimum expectations:

- at least one support or grounding object, source, or support-context route where applicable,
- enough prose to explain why the support surface matters.

### 3. `Challenge surface`

This section makes negative pressure legible.

Minimum expectations:

- the main empirical, methodological, procedural, or interpretive pressures where applicable,
- enough prose to explain why those pressures matter.

### 4. `Lineage placement`

This section makes ancestry or descendant position legible.

Minimum expectations:

- whether the claim is original, descendant, successor, or otherwise lineage-bearing,
- and at least one visible lineage route when lineage is part of the case.

These are not ornamental sections.
They are the human-readable compensation layer for the stricter protocol graph.

---

## What this note does **not** require

This note does **not** require that claim pages:

- reproduce every graph edge,
- become full graph explorers,
- duplicate every object body,
- or mirror every frontmatter field one-to-one.

The goal is not maximal duplication.
The goal is structured public readability.

---

## Current design rule

When there is tension between:

- keeping the object graph canonical and directionally clean,
- and keeping a single object file self-explanatory to a casual reader,

the preferred move is:

1. keep the object graph canonical,
2. then improve the claim page summary layer.

Do **not** reintroduce reverse relation names such as `attacked_by` into frontmatter merely to recover human convenience.
That convenience belongs in the public summary layer.

---

## Practical verdict

So the practical verdict is:

- **canonical one-direction relation semantics should remain at the machine layer**
- **human-readable support/challenge/lineage context should remain a public claim-page responsibility**
- **the current pilot should stabilize this split rather than relapse into mixed graph vocabulary**

That is the right architecture for the current stage.
