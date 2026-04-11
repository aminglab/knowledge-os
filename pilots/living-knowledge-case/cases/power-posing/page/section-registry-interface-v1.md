# Section registry interface v1

This note records the **smallest lawful section-registry interface** implied by the current `power-posing` page line.

It is intentionally narrow.
It does **not** declare a generic multi-case section system.
It records only the smallest interface that now exists between:

- the extracted renderer primitive layer,
- and the still case-scoped page composer.

---

## One-sentence ruling

Current ruling:

> **A section registry may now be described at the level of section-shape interface.**
> **It may not yet be described at the level of cross-case semantic registry.**

In plain language:

- yes, we can now describe the minimal shape a section entry must provide to the page composer,
- no, we cannot yet pretend that section names, section meanings, or section taxonomies are already generic across cases.

---

## Why this note exists now

Two things are already true.

### 1. renderer primitives have been extracted in code

The page stack now contains a real primitive layer in `renderer-primitives.js`.
It already carries section shells, cards, lineage rail, source items, source groups, timeline items, and footer cards.

### 2. `render.js` is now more clearly a composer than a primitive warehouse

That means the next boundary is no longer:

- “what is a primitive?”

It is now:

- “what is the smallest lawful interface between the primitive layer and the case composer?”

This note answers only that smaller question.

---

## The current minimal section-shape interface

At the current stage, a section entry in the composer may be described by the following minimal interface:

```text
section_entry := {
  title: string,
  intro: string,
  options?: {
    id?: string,
    tone?: string,
    kicker?: string,
    navLabel?: string,
  },
  body_renderer: case-scoped render step,
}
```

That is the whole point.

The interface is deliberately small:

- `title` gives the visible section title,
- `intro` gives the visible section intro,
- `options` carries section-shell hints,
- `body_renderer` remains a case-scoped rendering step that decides what kind of content gets mounted inside the section shell.

This is enough to describe the current seam without lying.

---

## What is inside the interface now

The following fields are now lawful to describe as interface-level.

### 1. shell-facing fields

These now clearly belong to the interface rather than the case content itself:

- `title`
- `intro`
- `options.id`
- `options.tone`
- `options.kicker`
- `options.navLabel`

These are section-shape properties.
They tell the renderer how to frame a section.
They do not yet tell it what a case means.

### 2. body mounting boundary

The interface may also lawfully name one more thing:

- `body_renderer`

This does **not** mean a generic content grammar exists.
It only means the section shell can now receive a case-scoped content renderer as its mounted body.

That is a real seam.
But it is still only a seam.

---

## What is explicitly outside the interface

The following things remain outside this minimal registry interface.

### 1. section semantics

Still case-scoped:

- `Why this case matters`
- `Current object neighborhoods`
- `Public claim and source routes`
- `Canonical source ids`
- `Reading path`

Those are current `power-posing` section meanings.
They are **not** yet generic section categories.

### 2. section ordering law

The current section order is still part of the case composer.

This note does **not** claim that there is already a general section-order grammar for:

- all living cases,
- all public pages,
- or all future public-layer products.

### 3. content grammar inside sections

Still case-scoped:

- which sections use status cards,
- which use route cards,
- which use source groups,
- which use timeline items,
- which use reading-path links.

The interface only says:

> a section shell may receive a body renderer.

It does **not** yet say that body renderers already form a generic registry.

### 4. source taxonomy and lineage taxonomy

Still case-scoped:

- source grouping into scientific record vs public circulation / retreat,
- lineage interpretation of original vs descendant claim,
- current emphasis choices around this case.

These should not be smuggled into a fake neutral registry.

---

## The lawful use of this interface right now

The current lawful use is narrow:

1. keep `render.js` as the case composer,
2. let section creation flow through a small section-shape interface,
3. continue extracting display primitives only when they stop depending on case wording,
4. avoid claiming that the section registry is already semantic or cross-case stable.

That is enough.

Anything bigger would be theater.

---

## The next lawful upgrade after this note

Once there is a second real case, the next lawful question becomes:

> do two case composers share enough section-shape and body-mount structure to justify a tiny registry schema beyond this one?

That question is not available yet.

Right now the honest move is simply:

- protect this minimal interface,
- keep semantics case-scoped,
- and wait for another real case before promoting it.

---

## Short practical consequence

So the practical consequence is:

- **yes** to a minimal section-shape registry interface,
- **yes** to naming the body-mount boundary,
- **no** to generic section semantics,
- **no** to generic section ordering law,
- **no** to pretending that one case has already proven a multi-case registry.

This is the smallest lawful registry note.
It should be treated as a **composer-to-primitive interface note**, not as the birth certificate of a general page system.
