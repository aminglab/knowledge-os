# COCKPIT3-B-A Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT3-B-A / Review Boundary Prototype Lift v1**.
It does not claim that `operator_review_required` has already been lawfully opened.
It records what must be true before a lawful `PASS_REVIEW_BOUNDARY_PROTOTYPE_LIFT` verdict can be issued.

---

## Primary verdict set

- `PASS_REVIEW_BOUNDARY_PROTOTYPE_LIFT`
- `PASS_REVIEW_TRIGGER_SCOPE_ACT_VISIBLE`
- `HOLD_REVIEW_BOUNDARY_PROTOTYPE_NOT_YET_COHERENT`
- `FAIL_REVIEW_BOUNDARY_PROTOTYPE_NOT_FORMED`

---

## Required acceptance checks

### 1. Review-field formation check

The prototype must visibly expose all minimum review-boundary fields:

- `review_trigger`
- `review_scope`
- `review_act`
- `retained_holds`

### 2. Boundary-default continuity check

The prototype must still visibly preserve the current defaults:

- `execution_boundary_class: draft_only`
- `action_posture: surface_only`
- `current_default_status: non-executable at current stage`

It must also explicitly preserve the non-upgrade clause:

- no current governed result surface is yet lawfully classified as `operator_review_required`

### 3. Boundary-honesty sentence check

The prototype must explicitly say that operator review is still not execution authority.

### 4. Anti-mutation continuity check

The prototype must preserve the core anti-runtime and anti-mutation holds.

### 5. Prototype-boundedness check

The prototype may not present review posture as a general runtime capability, a team-layer control, or a production-ready workflow.

---

## Pass condition

`PASS_REVIEW_BOUNDARY_PROTOTYPE_LIFT` is lawful only if all five required checks pass.

`PASS_REVIEW_TRIGGER_SCOPE_ACT_VISIBLE` is lawful only if the prototype exposes review trigger, scope, and act as visible governance fields without collapsing them into execution authority.

---

## Retained holds during evaluation

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`
