# COCKPIT3-B-A Review Boundary Prototype v1

## Status

Drafted for current threshold.

## Function

This file defines the first bounded review-boundary prototype for COCKPIT3-B-A.
Its purpose is to show, inside the cockpit surface, what a lawful review posture would need to expose before any future surface could honestly be discussed as `operator_review_required`.

---

## Governing principle

A review-boundary prototype is lawful only when it makes review posture more explicit, not more powerful.

The prototype may show:

- `review_trigger`
- `review_scope`
- `review_act`
- retained anti-execution holds

The prototype may not silently upgrade a governed result surface into execution authority.

---

## Minimum visible review-boundary fields

The first prototype should visibly expose at least:

1. `review_trigger`
2. `review_scope`
3. `review_act`
4. `retained_holds`

At the current threshold, the lawful defaults still remain:

- `execution_boundary_class: draft_only`
- `action_posture: surface_only`
- `current_default_status: non-executable at current stage`

---

## Boundary honesty sentence

The prototype must explicitly say:

> operator review is still not execution authority.

---

## Current lawful reading

The right reading is:

> the cockpit can now show what a lawful review posture would have to contain.

The wrong reading is:

> the cockpit may now escalate any current result surface into review or execution just because a human is present.
