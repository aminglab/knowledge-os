# COCKPIT2-B Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for COCKPIT2-B.
It does not falsely claim that the stronger structured suggestion surface has already been implemented.
It records what must be true before a lawful `PASS_STRUCTURED_SUGGESTION_SURFACE` verdict can be issued.

---

## Primary verdict set

- `PASS_STRUCTURED_SUGGESTION_SURFACE`
- `PASS_TRIGGER_RESULT_CARD_SURFACE`
- `HOLD_STRUCTURED_SUGGESTION_SURFACE_NOT_YET_COHERENT`
- `FAIL_RESULT_SURFACE_NOT_FORMED`

---

## Required acceptance checks

### 1. Result-surface formation check

The cockpit must visibly expose stronger trigger results than an audit-log note alone.
At least one trigger path must produce a cockpit-native structured result surface.

Failure mode:
- trigger activation still only writes a thin audit note and no richer result surface exists

### 2. Result-card honesty check

Every structured result surface must visibly declare:

- output class
- anchor reference
- draft-only posture

Failure mode:
- the result card looks like a committed change rather than a draft-only cockpit result

### 3. Output-grammar coherence check

The structured output classes must remain aligned with the current trigger universe and current result-card contract.

Failure mode:
- output categories drift into ad hoc prose or unauthorized action language

### 4. Boundary honesty check

The structured suggestion surface must not masquerade as:

- runtime execution
- governed object mutation
- team workflow control
- public publishing authority
- production cockpit behavior

### 5. Case-binding continuity check

The stronger result surface must still remain visibly tied to the currently bound pilot cases and their named anchors.
It must not become a floating global result feed detached from current case semantics.

---

## Pass condition

`PASS_STRUCTURED_SUGGESTION_SURFACE` is lawful only if all five required checks pass.

`PASS_TRIGGER_RESULT_CARD_SURFACE` is lawful only if the floor passes and at least one bounded trigger path produces a coherent structured result card.

---

## Retained holds during evaluation

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`
