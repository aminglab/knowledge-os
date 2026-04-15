# COCKPIT2 Boundary Holds v1

## Status

Active at current threshold.

## Function

This file records the retained holds for COCKPIT2.
It exists to prevent the stronger interactive prototype floor from being mistaken for runtime, team-layer, or production expansion.

---

## Retained core holds

The following holds remain active throughout COCKPIT2 evaluation:

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`

---

## Additional COCKPIT2-specific hold

The following hold is now added explicitly for the interactive stage:

- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`

This additional hold clarifies the exact point of current risk:
interaction may become stronger, but stronger interaction must not silently become object mutation.

---

## What these holds still allow

These holds do **not** forbid:

- stronger focus switching
- bounded browse modes
- rail expansion/collapse
- suggestion-layer action triggers
- richer preview and demo routes

They only forbid escalation beyond the current lawful threshold.

---

## What these holds still forbid

These holds still forbid:

- live backend task runtime
- object writes from cockpit controls
- verdict mutation from cockpit controls
- team-member collaboration surfaces
- public publishing from the cockpit
- production-readiness claims
- repository-wide cockpit generalization claims

---

## Stage reading

The right reading of COCKPIT2 is:

> stronger interaction under stricter honesty.

The wrong reading is:

> the cockpit has now become a live governed application.
