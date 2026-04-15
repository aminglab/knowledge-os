# COCKPIT2 Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for COCKPIT2.
It does not falsely claim that the stronger interactive cockpit has already been implemented.
It records what must be true before a lawful `PASS_INTERACTIVE_COCKPIT_PROTOTYPE_FLOOR` verdict can be issued.

---

## Primary verdict set

- `PASS_INTERACTIVE_COCKPIT_PROTOTYPE_FLOOR`
- `PASS_INTERACTIVE_COCKPIT_CASE_NAVIGATION`
- `HOLD_INTERACTIVE_COCKPIT_NOT_YET_COHERENT`
- `FAIL_INTERACTION_GRAMMAR_NOT_FORMED`

---

## Required acceptance checks

### 1. Stronger interaction check
The cockpit must visibly support stronger interaction than the COCKPIT1 static floor, including at least:

- focus switching
- bounded browse transitions
- one lawful lens switch
- one lawful action-trigger exposure

Failure mode:
- the prototype is still only a static page set with no meaningful interaction grammar

### 2. Object-browse integrity check
Every stronger interactive surface must remain anchored in named governed objects.

Failure mode:
- the frontend invents floating semantics that do not trace back to current case objects

### 3. Trigger honesty check
Every exposed trigger must remain suggestion-layer only and must not masquerade as direct mutation.

Failure mode:
- the UI implies that a governed change has already been committed

### 4. Boundary honesty check
The interactive prototype must not masquerade as:

- live runtime cockpit
- write-capable cockpit surface
- team layer
- production frontend
- repository-wide cockpit

### 5. Case-binding continuity check
The stronger interactive prototype must still be demonstrable against the currently bound pilot cases.
At least one case must support a meaningful end-to-end navigation path under the stronger interaction grammar.

---

## Pass condition

`PASS_INTERACTIVE_COCKPIT_PROTOTYPE_FLOOR` is lawful only if all five required checks pass.

`PASS_INTERACTIVE_COCKPIT_CASE_NAVIGATION` is lawful only if the floor passes and at least one real bound case supports a coherent end-to-end interactive navigation path.

---

## Retained holds during evaluation

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`
