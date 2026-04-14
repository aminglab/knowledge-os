# COCKPIT1-D Preview Route v1

## Status

Drafted for exposure.

## Function

This file defines the bounded local preview route for the static cockpit prototype.

---

## One-sentence route ruling

> **The cockpit prototype should be locally previewable in one short step, without pretending that it is already a full application runtime.**

---

## Required preview path

The repository should expose a small helper that:

1. starts a tiny static server from the prototype directory;
2. prints the local preview URL;
3. optionally opens the browser;
4. keeps the route scoped to `cockpit/COCKPIT1-B/prototype/`.

---

## Exposure rule

The preview route may be surfaced from:

- `cockpit/COCKPIT1-B/prototype/README.md`
- repository `README.md`
- `PUBLIC-ENTRY.md`

But it must be named honestly as a prototype preview route rather than a public product route.

---

## Final route block

- preview kind: `local static preview`
- live backend requirement: none
- public product overclaim: forbidden
