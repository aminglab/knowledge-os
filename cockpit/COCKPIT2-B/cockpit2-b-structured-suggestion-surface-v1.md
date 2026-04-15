# COCKPIT2-B Structured Suggestion Surface v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum lawful structured suggestion surface for COCKPIT2-B.
Its purpose is to upgrade the current trigger result posture from audit-log notes alone toward a more cockpit-native draft result surface.

---

## Governing principle

A structured suggestion surface is lawful only when all of the following remain true:

- every result remains draft-only
- every result remains anchored in a named object or route
- every result states its output class honestly
- every result remains narrower than governed mutation

The cockpit may display richer outputs.
It may not silently convert those outputs into authoritative object state.

---

## Why this lift is now needed

COCKPIT2-A already proves that bounded triggers can be exposed lawfully.
However, its current result posture is still thinner than the rest of the cockpit.
The next natural strengthening is to let the cockpit show structured trigger outputs as first-class draft surfaces rather than only as sidecar audit notes.

---

## Minimum lawful result-surface families

### 1. Draft result card
A trigger may produce one or more draft result cards.
Each card must visibly declare that it is a draft-only output.

### 2. Output-class badge
A result surface must expose its output class using bounded language such as:

- `scan result`
- `draft response`
- `condition check`
- `continuation suggestion`
- `summary draft`

### 3. Anchor reference
A result surface must visibly state the current object or route anchor that it belongs to.

### 4. Basis / unresolved remainder surface
A result surface may include:

- current basis hints
- missing basis hints
- unresolved remainder
- next-step hints

These remain guidance surfaces, not governed commitments.

### 5. Audit trace link
A result surface must still preserve an audit trace posture.
The richer result card does not replace audit visibility.
It supplements it.

---

## Forbidden drift

The structured suggestion surface becomes unlawful if it starts behaving like:

- a hidden object editor
- a hidden verdict editor
- a publication surface
- a task runner with runtime persistence
- a team workflow board

---

## Stage reading

The right reading of COCKPIT2-B is:

> stronger cockpit-native draft outputs.

The wrong reading is:

> cockpit actions now commit governed changes.
