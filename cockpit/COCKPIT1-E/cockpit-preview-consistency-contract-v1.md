# COCKPIT1-E Preview Consistency Contract v1

## Status

Drafted for governance.

## Function

This file defines the minimum consistency contract for the cockpit preview route across repository front-door and local-preview surfaces.

---

## One-sentence contract ruling

> **The cockpit preview route is lawful only if the same bounded truth is preserved across the helper, the prototype README, the root README, and the public-entry surface.**

---

## Required aligned surfaces

The following surfaces must stay aligned:

- `cockpit/COCKPIT1-B/prototype/preview_cockpit.py`
- `cockpit/COCKPIT1-B/prototype/README.md`
- root `README.md`
- `PUBLIC-ENTRY.md`

---

## Minimum consistency requirements

### 1. Preview helper presence
The repository must actually contain `preview_cockpit.py`.

### 2. Prototype README route presence
The prototype README must mention:

- `preview_cockpit.py`
- `python preview_cockpit.py`
- bounded static skeleton honesty

### 3. Root README exposure presence
The root README must expose:

- a local preview route for the cockpit prototype
- a link to the prototype README
- a link to `preview_cockpit.py`
- wording that the route is modest rather than production-grade

### 4. PUBLIC-ENTRY exposure presence
`PUBLIC-ENTRY.md` must expose:

- the cockpit preview route
- prototype honesty wording
- the fact that the cockpit route is additive rather than a replacement for the current public-case entry chain

### 5. Preview helper honesty
The helper script must clearly describe itself as a local preview helper for the static cockpit prototype.

---

## Final contract block

- aligned surfaces: 4
- required consistency checks: 5
- prototype-overclaim drift: forbidden
