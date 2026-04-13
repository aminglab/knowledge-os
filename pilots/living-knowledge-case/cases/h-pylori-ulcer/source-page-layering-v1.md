# Source Page Layering v1

This note records the current **source page layering rule** for the `h-pylori-ulcer` case.

It exists because the second case now has four distinct source-facing layers:

- `references.md` as a thin reader entrypoint,
- `references-metadata-v1.md` as the stable metadata layer,
- `sources/README.md` as the source-page index,
- and `sources/*.md` as the first written public source pages.

That split is good.
But it only works if the jobs remain distinct.

---

## One-sentence ruling

Current ruling:

> **References metadata is the stable machine-facing source layer.**
> **Source pages are the human-readable case-participation layer.**

Do not collapse these jobs back into one page format.

---

## Why this note exists now

The second case has already grown beyond a bare references list.
That matters because a living case should show not only *what* was cited, but *how* a source participates in the case.

A source page should therefore let a reader answer questions like:

- why is this source here,
- what role does it play,
- which governed objects use it,
- and where should I continue reading from it.

Without this layer, the public source surface becomes either metadata duplication or vague explanatory prose.

---

## Layer split

### Layer A. source metadata layer

This layer is for:

- canonical source identity,
- source type,
- authors or host,
- year,
- title,
- canonical locator,
- role in case,
- object usage,
- and other stable metadata.

In the current second case, this is the job of `references-metadata-v1.md`.

### Layer B. source page public layer

This layer is for:

- making the source readable inside the case,
- explaining its role in the case,
- surfacing which objects use it,
- and giving public reading routes.

This layer is not replacing metadata.
It is making metadata and case participation publicly legible.

---

## Current minimum source-page obligations

At the current stage, each public source page should expose at least the following sections:

### 1. `Source identity`

Minimum expectations:

- title,
- canonical source id,
- source type,
- year,
- venue or host,
- canonical locator.

### 2. `Source role in the case`

Minimum expectations:

- a short explanation of role,
- enough prose to show how the source participates in the case rather than only existing in a bibliography.

### 3. `Case usage`

Minimum expectations:

- the case name,
- a short “why it matters here” explanation,
- visible public reading routes.

### 4. `Object usage`

Minimum expectations:

- at least one linked governed object where the source is currently in play.

### 5. `Public reading routes`

Minimum expectations:

- at least one route into snapshot, references, metadata, source index, or case entry.

These are not ornamental sections.
They are the minimum public compensation layer for the tighter source stack.

---

## What this note does **not** require

This note does **not** require that source pages:

- reproduce every metadata field verbatim,
- become full literature reviews,
- carry every quotation,
- or replace the metadata layer.

The goal is not maximal duplication.
The goal is structured public readability.

---

## Practical verdict

So the practical verdict is:

- **source metadata remains the stable layer**
- **source pages remain the public case-participation layer**
- **the second case should stabilize this split rather than regress into either metadata duplication or vague source prose**
