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
- `generate_page_data.py` — the case-scoped generator that derives page data from the current case layer, validates the release surface, prints a small release summary, supports `--check`, and can emit machine-readable summaries with `--json-summary`
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

## Current publication chain

The current public release chain should be read in one direction:

> object layer → `snapshot-v2.md` → page layer

More concretely:

1. the governed objects remain the deepest source of truth,
2. `snapshots/snapshot-v2.md` acts as the current **public homepage** for the case,
3. the generator derives `page-data.js` from that governed case layer,
4. and the browser renderer turns that generated data into the current page surface.

This means the page layer is **downstream** of the snapshot release layer, not a competing editorial surface.
It should not invent a second public storyline that diverges from `snapshot-v2.md`.

The same rule applies to the page reading path.
It is intentionally **thinner** than the fuller reading path exposed in `snapshot-v2.md`.
The page should provide the shortest downstream route back into verdicts, claims, timeline, and references,
while the snapshot remains the fuller governance-backed release path.

---

## How it works now

The current intended flow is:

1. edit object files, `snapshot-v2.md`, `references.md`, or `timeline/events.md`
2. treat `snapshot-v2.md` as the current public homepage and release source for the case
3. run `generate_page_data.py`
4. let the generator validate the current case layer
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
- and links or internal references that point to missing objects.

This is not yet a full protocol validator.
But it gives the publishing pipeline its first real teeth.

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

So the current page/publishing line is no longer guarded only by generator validation.
It is also guarded by a small adjacent README template seam audit that keeps seam-governance documents visible to later developers.

---

## Current release feedback

When generation succeeds, the script now reports its result in three layers in human-readable mode:

1. `Validation passed.`
2. `Release summary:`
3. `Write completed: ...` or `Write skipped (--check).`

The release summary itself currently includes:

- total object count,
- object counts by family,
- canonical source id count,
- neighborhood card count,
- timeline entry count,
- and reading-path link count.

When `--json-summary` is used, the script instead emits a machine-readable JSON object containing:

- `schema_name`
- `schema_version`
- validation status,
- write status,
- whether `--check` was active,
- output path when relevant,
- and the same release-summary counts.

That means the payload now identifies its own contract instead of requiring downstream automation to infer it from repository docs alone.

---

## Exit-code discipline

The generator now follows a simple exit-code rule:

- `0` — validation passed and the requested action completed
- `1` — validation failed
- `2` — command-line usage error from `argparse`

That gives downstream automation a minimal but clear contract.

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
- the page reading path is intentionally thinner than the snapshot reading path,
- validates a small set of high-value invariants,
- prints a readable release summary,
- supports a non-writing `--check` mode,
- can emit machine-readable JSON,
- the README template seam audit keeps template-governance documents visibly attached to the case entry surface,
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
