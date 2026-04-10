# page-snapshot-alignment-audit-v1

## Status

Alignment audit note v1.

## Function

This document audits alignment between the current public homepage snapshot and the current page surface for the `power-posing` case.

It does **not** introduce a new protocol layer.
Its narrower purpose is to answer:

- whether the page is still downstream of the current snapshot release layer,
- whether the page has started to drift into a second public storyline,
- and which mismatches are now worth fixing first.

---

## Audited surfaces

This audit compares the following current files:

- `snapshots/snapshot-v2.md`
- `page/page-data.js`
- `page/render.js`
- `page/index.html`

These are the minimal files that together define the current public homepage layer and the downstream page presentation layer.

---

## High-level verdict

Current verdict:

> Alignment is **good enough to preserve the one-direction publication chain**, but not yet tight enough to call the page and snapshot fully synchronized public surfaces.
>
> There is **no major second-storyline break**.
>
> There are, however, several clear wording and hierarchy drifts that now deserve direct cleanup.

Operational reading:

- the page is still recognizably downstream of the snapshot,
- but it still carries some older or flatter release wording,
- and it currently underexpresses the snapshot's stronger homepage role.

---

## What is aligned

### 1. Core judgment direction is aligned

Both surfaces still present the same basic top-level judgment:

- original claim weakened and contested,
- descendant claim still surviving in weaker form.

This is the most important alignment point.
The page has not invented a rival judgment outcome.

### 2. The page still points back into governed objects

The current page keeps object ids, verdict links, evidence links, and source ids visible.
That means it still behaves like a release surface over the governed object layer rather than a detached summary article.

### 3. The page still depends on generated data from the governed case layer

The current page is not hand-maintained narrative HTML.
It is still downstream of the case-scoped generator and therefore remains structurally tied to the governed case layer.

### 4. The page still keeps the case chronology and source layer visible

The timeline and canonical source sections continue to express the same general case arc visible in the snapshot and object layer.

---

## Main alignment drifts

### Drift 1. The page hero still uses older, weaker homepage framing

`snapshot-v2.md` now explicitly behaves like the current **public homepage** for the case.
The first-screen wording was tightened in Phase 1 to make that role clearer.

But `page/page-data.js` still carries an older description string:

- it says the page is a “reader-facing release view” and “public snapshot of the current pilot reading,”
- but it does not carry the newer explicit homepage framing now present in the snapshot.

This is not a fatal break.
It is a release-surface lag.

### Drift 2. The page hero hierarchy underexpresses the snapshot title hierarchy

The current page hero uses:

- `title = "Power Posing"`
- `subtitle = "Power Posing: a living knowledge page for a disputed scientific claim"`

But `render.js` renders the short title as the `h1` and does not elevate the longer snapshot title into the main hero hierarchy.

As a result, the page still feels more like a generic prototype heading than a fully aligned public homepage.

### Drift 3. The status-card wording is close, but not exact

The page uses:

- `contested and significantly weakened`
- `contested but still surviving as a weaker path`

The snapshot now uses the tighter pair:

- `contested and significantly weakened`
- `contested but still surviving`

The extra phrase “as a weaker path” is not wrong, but it is one more example of the page carrying its own local paraphrase rather than staying maximally synchronized with the current snapshot release wording.

### Drift 4. The page section intro for “Current visible judgment” is not the same layer as the snapshot section intro

In the page, `render.js` uses `data.subtitle` as the intro line for the “Current visible judgment” section.
That means the intro under that heading is currently just the case subtitle.

In the snapshot, the same section instead explains:

- these status phrases are not narrative decoration,
- they are public renderings of governed judgment,
- and governance documents can be consulted if the reader wants to trace them back.

This is one of the clearest structural misalignments in the current page surface.
It makes the page section feel less governed and less informative than the snapshot section it is supposed to descend from.

### Drift 5. The page reading path is thinner than the snapshot reading path

The current page reading path omits:

- `status-legend-v1.md`
- `verdict-grammar-v1.md`
- direct links to the dissent objects
- the references metadata layer

This is not automatically a bug.
A downstream page surface may legitimately simplify.

But it should be treated as a conscious simplification rather than an unexamined default, because Phase 1 already made the snapshot the explicit public homepage and release source.

---

## Drift severity

These drifts are currently **minor to medium**, not severe.

Why they are not severe:

- they do not produce a contradictory verdict,
- they do not invert the claim lineage,
- they do not hide the object layer,
- and they do not create a fully separate editorial story.

Why they still matter:

- they weaken the homepage identity of the page,
- they allow older wording to persist after snapshot tightening,
- and they make the page feel more prototype-like than the current repository stage now deserves.

---

## Recommended first repair set

The first repair set should remain small.

### 1. Refresh page hero copy from the current snapshot homepage wording

Bring the page description and hero hierarchy into closer sync with the current homepage framing now present in `snapshot-v2.md`.

### 2. Stop using `subtitle` as the intro for the “Current visible judgment” section

Replace that intro with wording that better matches the snapshot's governance-backed explanation of status phrases.

### 3. Normalize status-card wording to match the current snapshot more closely

Especially for the descendant claim, reduce unnecessary local paraphrase where possible.

### 4. Make an explicit decision about page reading-path simplification

Either:

- keep the thinner page reading path and document it as intentional,
- or enrich it so it better reflects the snapshot reading path.

What should be avoided is accidental drift through silence.

---

## Audit verdict for Phase 2 entry

This audit supports the current Phase 2 entry decision.

It shows that:

- the public release surface is already worth improving,
- the page is not broken,
- but there is still clear value in tightening page/snapshot alignment before attempting broader protocol lifting.

That is exactly why public-surface hardening was the correct entry choice for Phase 2.
