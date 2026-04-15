# COCKPIT2-A Prototype

## Status

Bounded interactive prototype lift.

## Function

This directory contains the first **COCKPIT2-A interactive prototype shell**.
It exists to prove a stronger cockpit interaction floor than COCKPIT1-B while preserving the current anti-runtime and anti-mutation boundaries.

This prototype currently demonstrates:

- the five bound cockpit screen states carried forward from COCKPIT1-B
- a bounded four-lens switch (`focus`, `pressure`, `route`, `boundary`)
- a bounded object-browse surface with named anchors per state
- a suggestion-layer trigger panel
- a sidecar audit log that stays draft-only and non-authoritative

---

## Boundary

This prototype does **not**:

- open live runtime behavior
- write governed objects from the frontend
- replace the public layer
- claim production readiness

It is a bounded interactive lift only.

---

## Files

- `index.html` — bounded interactive shell
- `styles.css` — cockpit styling for the COCKPIT2-A lift
- `app.js` — state, lens, object-browse, trigger, and audit-log wiring

---

## Reading note

The correct reading is:

> stronger interaction under stricter honesty.

The incorrect reading is:

> the cockpit has now become a live governed application.
