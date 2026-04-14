# COCKPIT1 Surface Grammar v1

## Status

Drafted for construction.

## Function

This file defines the minimum **surface grammar** for COCKPIT1.
The cockpit is not a general chat shell.
It is the first private object-centered frontend.

---

## One-sentence surface ruling

> **The cockpit front surface must be object-centered, route-aware, and action-bearing.**
>
> **Conversation may exist only as a sidecar workbench, not as the primary center of the screen.**

---

## Minimum layout grammar

COCKPIT1 should expose four regions.

### A. Left rail — project and route navigation
Must support:

- project selection
- route tree / project map
- object index by type
- current focus pointer

### B. Main panel — current focus object
Must support at least:

- object title and type
- current verdict / lifecycle visibility
- dependencies and direct pressure surfaces
- current notes and next-step hooks

### C. Right rail — dissent / verdict / activity stack
Must support:

- open dissent queue
- current verdict state
- recent object-changing activity
- unresolved attention items

### D. Sidecar console — conversation / analysis workbench
May support:

- founding-style exploration
- temporary analysis
- prompt debugging
- note drafting

But it must remain subordinate to the object-centered screen.

---

## Required object views

COCKPIT1 must natively support these views:

- `project_map_view`
- `claim_view`
- `evidence_tree_view`
- `dissent_ledger_view`
- `verdict_state_view`

Optional in COCKPIT1 but not required:

- `snapshot_preview_view`
- `export_preview_view`

---

## Surface prohibitions

COCKPIT1 should not present itself as:

- a blank chat homepage
- a document browser pretending to be a cockpit
- a team dashboard
- a public publishing page

---

## Final grammar block

- cockpit center: object-focused
- sidecar status: subordinate
- required views: 5
- forbidden substitution: chat shell for cockpit
