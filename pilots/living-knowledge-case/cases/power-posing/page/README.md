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
- a small extracted renderer-primitive layer,
- and a reader-facing page shell.

That is enough for the current stage.

---

## What is here

- `index.html` — the page shell
- `styles.css` — the current visual layer
- `generate_page_data.py` — the case-scoped generator that derives page data from the current case layer, validates the release surface, prints a small release summary, supports `--check`, and can emit machine-readable summaries with `--json-summary`
- `page-data.js` — generated page data consumed by the browser renderer
- `renderer-primitives.js` — the first extracted renderer primitive layer
- `render.js` — the case-scoped page composer that now assembles `power-posing` from the primitive layer rather than defining every primitive inline
- `generic-renderer-seam-v1.md` — the first renderer-seam judgment on what now looks extractable versus what still remains case-scoped

---

## Current scope

This renderer prototype is designed to prove eight things:

1. the case can be rendered as a page rather than only as a markdown tree,
2. object ids can remain visible at the UI layer,
3. the page can point back to source objects and the reference map,
4. the snapshot can become a navigable public reading surface,
5. the page layer can grow from the governed object layer through a minimal generation step,
6. the page can now begin to expose the seeded `claims/` and `sources/` layers without replacing the snapshot as the fuller release view,
7. the display layer can now make both claim lineage and grouped source participation more visible as page structure instead of leaving them implicit inside links alone,
8. and the first lawful renderer primitives can now be extracted without pretending the whole page stack is already generic.

---

## Current publication chain

The current public release chain should be read in one direction:

> object layer → `snapshot-v2.md` → page layer

More concretely:

1. the governed objects remain the deepest source of truth,
2. `snapshots/snapshot-v2.md` acts as the current **public homepage** for the case,
3. the generator derives `page-data.js` from that governed case layer,
4. the extracted primitive layer provides a small reusable renderer substrate,
5. and the case composer turns that generated data into the current `power-posing` page surface.

This means the page layer is **downstream** of the snapshot release layer, not a competing editorial surface.
It should not invent a second public storyline that diverges from `snapshot-v2.md`.

The same rule applies to the page reading path.
It is intentionally **thinner** than the fuller reading path exposed in `snapshot-v2.md`.
The page should provide the shortest downstream route back into verdicts, claims, timeline, and references,
while the snapshot remains the fuller governance-backed release path.

As of the current integration pass, that thinner route now acknowledges not only raw object links and references, but also the seeded public `claims/` and `sources/` layers that have grown around the case.

The current renderer pass also makes two more things visible at the display layer:

- the original claim and the weaker descendant claim now appear as an explicit lineage surface rather than only as two disconnected status cards,
- and the source layer now renders as grouped stacks with split subroutes (`Source routes` / `Touches objects`) rather than as one flat undifferentiated list.

That is still downstream of the governed case layer.
But it gives the page a more legible structure without turning it into a full graph browser.

---

## How it works now

The current intended flow is:

1. edit object files, `snapshot-v2.md`, `references.md`, or `timeline/events.md`
2. treat `snapshot-v2.md` as the current public homepage and release source for the case
3. run `generate_page_data.py`
4. let the generator validate the current case layer and seeded public page surfaces
5. review the printed release summary or emitted JSON summary
6. open `index.html`

That means `page-data.js` should now be treated as a **generated artifact**, not as the canonical place to edit case content.

If you want to validate the release surface without rewriting `page-data.js`, run:

```bash
python generate_page_data.py --check
```

If you want a machine-readable summary for automation, run:

```bash
python generate_page_data.py --json-summary
```

You can also combine both modes:

```bash
python generate_page_data.py --check --json-summary
```

That combined mode performs the same parsing and validation pass, builds the release data in memory, emits JSON, and exits without writing the output file.

---

## Current validation floor

The generator now performs a small but useful validation pass before writing `page-data.js`.
It currently checks for:

- undefined `source_refs`,
- missing required frontmatter fields,
- links or internal references that point to missing objects,
- missing public claim pages for current claim objects,
- and missing public source pages for current canonical source ids.

This is not yet a full protocol validator.
But it gives the publishing pipeline real teeth around the current richer page contract.

Adjacent to that generator-level floor, the repository now also carries a small README template seam audit:

- script: `scripts/check_power_posing_template_seam_readme.py`
- workflow: `.github/workflows/check-power-posing-template-seam-readme.yml`

That audit does **not** validate page-data emission.
It validates something narrower and neighboring:

> whether the case README continues to expose the template-seam governance documents that now define reusable-shell discipline.

In practical terms, it protects continued README exposure of:

- `case-template-boundary-v1.md`
- `case-template-extraction-checklist-v1.md`
- `template-seam-summary-v1.md`

So the current page/publishing line is no longer guarded only by object validation.
It is also guarded by a small adjacent README template seam audit that keeps seam-governance documents visible to later developers.

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
- `snapshot-v2.md` acts as the current public homepage and release layer,
- the generator creates a thin browser-ready data bridge downstream of that release layer,
- the extracted primitive layer now carries the first lawful reusable renderer units,
- `render.js` remains the `power-posing` page composer rather than pretending to be a generic renderer runtime,
- the page reading path is intentionally thinner than the snapshot reading path,
- the page can now acknowledge the seeded public `claims/` and `sources/` layers without pretending to be a full object browser,
- the renderer now makes the original-to-descendant claim relation visibly legible in the current judgment surface rather than leaving lineage implicit,
- the source layer now renders as grouped source stacks with explicit source-route and object-touch subroutes,
- the generator now validates that those seeded public layers actually exist for the current case,
- and the page is a presentation surface over that bridge.

If you want the explicit seam judgment for what may later be extracted into a broader renderer line, read:

- `generic-renderer-seam-v1.md`

---

## Why this matters

The repository already proved that the case can exist as governed files.
The first renderer prototype proved that the case could begin to look like a product surface.
The page-layer integration pass proved that the visible page could acknowledge a richer public ecology around the case.

This step proves the next thing:

> the first renderer seam can now be acted on in code without pretending that generic renderer closure has already happened.

That is exactly why the seam note now exists beside the extracted primitive layer itself.
