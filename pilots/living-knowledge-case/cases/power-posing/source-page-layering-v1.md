# Source Page Layering v1

This note records the current **source page layering rule** for the `power-posing` pilot.

It exists because the pilot now has three distinct source-facing layers:

- `references.md` as a thin reader entrypoint,
- `references-metadata-v1.md` as the stable metadata layer,
- and `sources/*.md` as the first public source-page surfaces.

That split is good.
But it only works if the jobs remain distinct.

> metadata should remain machine-stable and reusable,
> while source pages should make each source publicly legible as a participant in the case.

---

## One-sentence ruling

Current ruling:

> **References metadata is the machine-stable source layer.**
> **Source pages are the human-readable case-participation layer.**

Do not collapse these jobs back into one page format.

---

## Why this note exists now

The current pilot has already grown beyond a bare references list.
That is valuable because a living case needs to show not only *what* was cited, but *how* a source functions inside the case.

A source page should therefore do more than restate bibliographic metadata.
It should make a reader able to answer questions like:

- why is this source here,
- what role does it play,
- which governed objects use it,
- and how should I continue reading from it.

Without this layer, the public source surface becomes either:

- a duplicate of metadata,
- or a loose prose page with no stable grounding.

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
- and other machine-checkable stable metadata.

In the current pilot, this is the job of `references-metadata-v1.md`.

### Layer B. source page public layer

This layer is for:

- making the source readable inside the living case,
- explaining its role in the case,
- surfacing the governed objects that use it,
- and giving public reading routes.

This layer is not replacing metadata.
It is making metadata and case participation publicly legible.

---

## Current minimum source-page obligations

At the current stage, each public source page should expose at least the following sections:

### 1. `Source identity`

This section gives the reader a visible source identity surface.

Minimum expectations:

- title,
- canonical source id,
- source type,
- year,
- venue or host,
- canonical locator.

### 2. `Source role in the case`

This section explains why the source matters in this case.

Minimum expectations:

- a short explanation of role,
- enough prose to show how the source participates in the case rather than only existing in a bibliography.

### 3. `Case usage`

This section explains where the source fits in the current case reading.

Minimum expectations:

- the case name,
- a short “why it matters here” explanation,
- visible public reading routes.

### 4. `Object usage`

This section exposes which governed objects currently use the source.

Minimum expectations:

- at least one linked object usage route where the source is currently in play.

### 5. `Public reading routes`

This section gives the reader a way back into the larger public surface.

Minimum expectations:

- at least one route into snapshot, references, metadata, source index, or case entry.

These are not ornamental sections.
They are the human-readable compensation layer for the tighter source metadata stack.

---

## What this note does **not** require

This note does **not** require that source pages:

- reproduce every metadata field verbatim,
- become full literature reviews,
- carry every quoted passage,
- or replace the metadata layer.

The goal is not maximal duplication.
The goal is structured public readability.

---

## Current design rule

When there is tension between:

- keeping source identity stable at the metadata layer,
- and making a single source page publicly intelligible,

the preferred move is:

1. keep the metadata layer stable,
2. then improve the source page explanation layer.

Do **not** overload the metadata layer merely to recover public readability.
That readability belongs in the source page layer.

---

## Practical verdict

So the practical verdict is:

- **source metadata should remain the stable machine layer**
- **source pages should remain the public case-participation layer**
- **the current pilot should stabilize this split rather than regress into either metadata duplication or vague source prose**

That is the right architecture for the current stage.
