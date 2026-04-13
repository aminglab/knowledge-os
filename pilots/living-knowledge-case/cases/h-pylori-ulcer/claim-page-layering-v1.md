# Claim Page Layering v1

This note records the current **claim page layering rule** for the `h-pylori-ulcer` case.

It exists because the second case has now crossed a real threshold:

- claim objects remain the governed machine layer,
- claim pages now act as public-facing surfaces,
- and the public claim surface should no longer be allowed to drift silently.

That is especially important here because this is a health-related case.
The public layer should stay readable without collapsing back into loose prose.

---

## One-sentence ruling

Current ruling:

> **Claim object frontmatter is the governed machine layer.**
> **Claim pages are the human-readable neighborhood summary layer.**

Do not collapse these jobs back into one file format.

---

## Why this note exists now

The second case already has two public claim pages.
Those pages are doing work that raw object files should not be forced to do alone.

A reader should be able to see, without parsing frontmatter:

- what the current judgment is,
- what supports the claim,
- what challenges it,
- and how it sits inside a lineage.

That readability is a public-layer job.
It is not a reason to loosen the governed object layer.

---

## Layer split

### Layer A. governed object frontmatter

This layer is for:

- machine-legible identity,
- canonical relations,
- minimal governed metadata,
- and reliable checking.

### Layer B. claim page neighborhood summary

This layer is for:

- visible judgment,
- support surface,
- challenge surface,
- lineage placement,
- and public reading routes.

This layer does not replace the governed graph.
It makes the governed graph publicly readable.

---

## Current minimum claim-page obligations

At the current stage, each public claim page should expose at least the following sections:

### 1. `Claim identity`

Minimum expectations:

- visible claim id,
- visible title or public formulation,
- visible claim type.

### 2. `Current visible judgment`

Minimum expectations:

- a visible current state phrase,
- a linked verdict object.

### 3. `Support surface`

Minimum expectations:

- at least one linked support object,
- enough prose to explain why that support matters.

### 4. `Challenge surface`

Minimum expectations:

- at least one linked dissent or challenge object where applicable,
- enough prose to explain why that pressure matters.

### 5. `Lineage placement`

Minimum expectations:

- whether the claim is stronger-form, narrower descendant, or otherwise lineage-bearing,
- and at least one visible lineage route where lineage is part of the case.

These are not ornamental sections.
They are the minimum public compensation layer for the stricter object graph.

---

## What this note does **not** require

This note does **not** require that claim pages:

- duplicate every object field,
- mirror raw object titles word-for-word,
- become full graph explorers,
- or reproduce every edge in the case.

The goal is not maximal duplication.
The goal is structured public readability.

---

## Practical verdict

So the practical verdict is:

- **claim objects remain the machine-governed layer**
- **claim pages remain the human-readable neighborhood layer**
- **the second case should stabilize this split rather than slide back into mixed responsibilities**
