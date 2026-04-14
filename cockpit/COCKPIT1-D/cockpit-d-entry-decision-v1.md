# COCKPIT1-D Entry Decision v1

## Status

Entered at current threshold.

## Function

This file records the entry decision for **COCKPIT1-D / Cockpit Preview and Front-Door Exposure v1**.

COCKPIT1-C hardened the semantic floor of the static cockpit prototype.
The next lawful step is to make that prototype easier to preview locally and easier to discover from the repository front door.

---

## One-sentence entry verdict

Current entry verdict:

> **ENTER_COCKPIT1_D_PREVIEW_AND_EXPOSURE**
>
> The project may now expose the static cockpit prototype through a bounded preview route and a modest front-door link path, because the prototype already has case binding and semantic checks.

---

## Immediate purpose

COCKPIT1-D exists to do three things:

1. give the cockpit prototype a simple local preview helper;
2. expose the cockpit route from repository entry surfaces;
3. do so without overstating the cockpit as a production frontend.

---

## Boundary

COCKPIT1-D does **not**:

- claim production readiness
- replace public-layer front doors
- open team-layer routes
- promote the cockpit prototype above the current public cases

It only makes the bounded prototype easier to preview and easier to find.

---

## Final decision block

- entry verdict: `ENTER_COCKPIT1_D_PREVIEW_AND_EXPOSURE`
- proof target: `local preview path + front-door discoverability`
- overclaim: forbidden
