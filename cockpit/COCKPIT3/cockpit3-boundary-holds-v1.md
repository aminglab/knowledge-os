# COCKPIT3 Boundary Holds v1

## Status

Active at current threshold.

## Function

This file records the retained holds for COCKPIT3.
It exists to prevent the execution-boundary floor from being misread as an execution authorization object.

---

## Retained core holds

The following holds remain active throughout COCKPIT3 evaluation:

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`

---

## COCKPIT3-specific reading

COCKPIT3 allows stronger governance language about action boundaries.
It does not allow stronger action authority.

That means the cockpit may now define:

- draft-only surfaces
- review-candidate posture
- execution-forbidden classes

But it still may not cross into:

- governed mutation
- runtime execution
- verdict resolution
- publication authority
- team-layer execution control

---

## Stage reading

The right reading of COCKPIT3 is:

> action-boundary governance under the same honesty boundary.

The wrong reading is:

> the cockpit can now do things to governed objects.
