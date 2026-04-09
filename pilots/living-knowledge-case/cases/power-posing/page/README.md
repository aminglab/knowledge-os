# Power Posing Page Prototype

This directory contains the **first simple renderer prototype** for the `power-posing` living knowledge case.

It is intentionally small.
It is still a zero-build prototype.
But it no longer treats `page-data.js` as a hand-maintained bridge.

The current page stack now has a small publishing pipeline:

- governed markdown object files,
- snapshot markdown,
- a case-scoped page-data generator,
- generated page data,
- and a reader-facing page shell.

That is enough for the current stage.

---

## What is here

- `index.html` — the page shell
- `styles.css` — the current visual layer
- `generate_page_data.py` — the case-scoped generator that derives page data from the current case layer, validates the release surface, and prints a small release summary
- `page-data.js` — generated page data consumed by the browser renderer
- `render.js` — the script that turns the generated data into a page

---

## Current scope

This renderer prototype is designed to prove five things:

1. the case can be rendered as a page rather than only as a markdown tree,
2. object ids can remain visible at the UI layer,
3. the page can point back to source objects and the reference map,
4. the snapshot can become a navigable public reading surface,
5. and the page layer can now grow from the governed object layer through a minimal generation step.

---

## How it works now

The current intended flow is:

1. edit object files, `snapshot-v2.md`, `references.md`, or `timeline/events.md`
2. run `generate_page_data.py`
3. let the generator validate the current case layer
4. review the printed release summary
5. open `index.html`

That means `page-data.js` should now be treated as a **generated artifact**, not as the canonical place to edit case content.

---

## Current validation floor

The generator now performs a small but useful validation pass before writing `page-data.js`.
It currently checks for:

- undefined `source_refs`,
- missing required frontmatter fields,
- and links or internal references that point to missing objects.

This is not yet a full protocol validator.
But it gives the publishing pipeline its first real teeth.

---

## Current release feedback

When generation succeeds, the script now prints a compact release summary including:

- total object count,
- object counts by family,
- canonical source id count,
- neighborhood card count,
- timeline entry count,
- and reading-path link count.

This is still lightweight.
But it means the pipeline now tells you what it just published instead of only saying that it wrote a file.

---

## Important honesty note

This is still a **case-scoped prototype**.
It does not yet implement:

- a universal markdown/frontmatter parser for all cases,
- a generic case renderer pipeline,
- live snapshot selection,
- search,
- filters,
- object graph visualization,
- formal routing,
- or multi-case publishing automation.

Those should come later.

For now, the renderer is intentionally simple and honest:

- the knowledge model still lives in the case objects,
- the snapshot still acts as a public release layer,
- the generator creates a thin browser-ready data bridge,
- validates a small set of high-value invariants,
- prints a readable release summary,
- and the page is a presentation surface over that bridge.

---

## Why this matters

The repository already proved that the case can exist as governed files.
The first renderer prototype proved that the case could begin to look like a product surface.

This step proves the next thing:

> the public page no longer depends entirely on hand-written page data.

And the pipeline can now fail early when the case layer drifts in obvious ways.

That is the beginning of a real publishing pipeline.

---

## Next natural upgrades

Later iterations may:

- make the generator more generic across cases,
- derive richer cards from object fields and body sections,
- validate more protocol constraints,
- support multiple snapshots,
- and eventually merge into a broader public layer renderer.
