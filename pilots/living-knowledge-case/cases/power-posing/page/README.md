# Power Posing Page Prototype

This directory contains the **first simple renderer prototype** for the `power-posing` living knowledge case.

It is intentionally small.
It does not yet parse the markdown object files automatically.
Instead, it creates a real page surface from a thin hand-maintained data bridge.

That is enough for the current stage.

The goal is not to pretend the full product already exists.
The goal is to cross an important threshold:

> move from a repository-readable case to a reader-facing page prototype.

---

## What is here

- `index.html` — the page shell
- `styles.css` — the current visual layer
- `page-data.js` — a small renderer data bridge derived from the current case objects and snapshot
- `render.js` — the script that turns the data bridge into a page

---

## Current scope

This renderer prototype is designed to prove four things:

1. the case can be rendered as a page rather than only as a markdown tree,
2. object ids can remain visible at the UI layer,
3. the page can point back to source objects and the reference map,
4. the snapshot can become a navigable public reading surface.

---

## Important honesty note

This is a **zero-build prototype**.
It does not yet implement:

- automatic markdown/frontmatter parsing,
- a generic case renderer pipeline,
- live snapshot selection,
- search,
- filters,
- object graph visualization,
- or formal routing.

Those should come later.

For now, the renderer is intentionally simple and honest:

- the knowledge model still lives in the case objects,
- the page is a presentation layer,
- and `page-data.js` is the temporary bridge between the two.

---

## Why this matters

The repository already proved that the case can exist as governed files.
This renderer prototype proves the next thing:

> the same case can begin to look like a product surface.

That shift matters because Knowledge OS is not only a protocol idea.
It also needs public-facing reading surfaces.

---

## Next natural upgrades

Later iterations may:

- generate `page-data.js` from object frontmatter,
- support multiple cases through one renderer shell,
- turn object references into richer cards,
- and eventually merge into a more general public layer renderer.
