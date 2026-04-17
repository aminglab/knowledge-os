# COCKPIT3 Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for COCKPIT3.
It does not falsely claim that the cockpit has already gained execution authority.
It records what must be true before a lawful `PASS_EXECUTION_BOUNDARY_FLOOR` verdict can be issued.

---

## Primary verdict set

- `PASS_EXECUTION_BOUNDARY_FLOOR`
- `PASS_RESULT_SURFACE_GOVERNANCE_OBJECT`
- `HOLD_EXECUTION_BOUNDARY_NOT_YET_COHERENT`
- `FAIL_EXECUTION_BOUNDARY_OBJECT_NOT_FORMED`

---

## Required acceptance checks

### 1. Boundary-class formation check

The cockpit must visibly define lawful boundary classes that distinguish at least:

- draft-only
- operator-review-required or review-candidate posture
- execution-forbidden posture

Failure mode:
- the cockpit still has structured result cards but no explicit governance object for action boundary classes

### 2. Governance-surface honesty check

The result-surface governance object must visibly declare how current result surfaces are classified and must not blur draft outputs into executable action objects.

Failure mode:
- result-surface governance language drifts into implicit authority claims

### 3. Escalation-grammar coherence check

The action-escalation grammar must remain a governance grammar and not masquerade as an execution pipeline.

Failure mode:
- escalation words imply that execution is already lawful at the current stage

### 4. Boundary honesty check

The execution-boundary floor must not masquerade as:

- runtime execution authority
- governed mutation authority
- team workflow execution control
- publication authority
- production cockpit behavior

### 5. Retained-holds continuity check

The current core cockpit holds must remain explicit and unchanged while the new execution-boundary floor is introduced.

---

## Pass condition

`PASS_EXECUTION_BOUNDARY_FLOOR` is lawful only if all five required checks pass.

`PASS_RESULT_SURFACE_GOVERNANCE_OBJECT` is lawful only if the floor passes and the result-surface governance object clearly classifies current result surfaces without implying current execution authority.

---

## Retained holds during evaluation

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`
