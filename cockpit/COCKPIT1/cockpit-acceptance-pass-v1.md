# COCKPIT1 Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for COCKPIT1.
It does not falsely claim that the cockpit has already been implemented.
It records what must be true before a lawful `PASS_PRIVATE_COCKPIT_FLOOR` verdict can be issued.

---

## Primary verdict set

- `PASS_PRIVATE_COCKPIT_FLOOR`
- `PASS_PRIVATE_COCKPIT_MINIMAL_FRONTEND`
- `HOLD_PRIVATE_COCKPIT_NOT_YET_COHERENT`
- `FAIL_OBJECT_FRONTEND_NOT_FORMED`

---

## Required acceptance checks

### 1. Object-centered layout check
The cockpit must visibly center:

- project map
- current focus object
- dissent/verdict/activity stack

Failure mode:
- chat window still behaves as the real center

### 2. Object-view coverage check
The cockpit must support at least:

- claim view
- evidence tree view
- dissent ledger view
- verdict state view
- project map view

### 3. Action anchoring check
Every exposed cockpit action must have:

- named object anchor
- read scope
- write scope
- audit trace

### 4. Transition-route check
There must be a lawful visible route from founding/structuring outputs into cockpit mode.

### 5. Boundary honesty check
The cockpit must not masquerade as:

- team layer
- public release layer
- page emission layer
- repository-wide generic cockpit

---

## Pass condition

`PASS_PRIVATE_COCKPIT_FLOOR` is lawful only if all five required checks pass.

`PASS_PRIVATE_COCKPIT_MINIMAL_FRONTEND` is lawful only if the floor passes and at least one real case can be navigated end-to-end through the cockpit.

---

## Retained holds during evaluation

- `HOLD_NO_TEAM_LAYER_EXPANSION`
- `HOLD_NO_PUBLIC_LAYER_SUBSTITUTION`
- `HOLD_NO_PAGE_EMISSION_UPGRADE`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
