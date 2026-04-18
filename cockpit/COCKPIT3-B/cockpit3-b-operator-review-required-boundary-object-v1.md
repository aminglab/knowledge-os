# COCKPIT3-B Operator Review Required Boundary Object v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum lawful boundary object for `operator_review_required` inside COCKPIT3-B.
Its purpose is to answer a narrower question than COCKPIT3-A:

> what would need to become true before a cockpit result surface could honestly stop being only `draft_only`, yet still remain non-executable and subject to explicit human review?

---

## Governing principle

`operator_review_required` is not a soft synonym for execution readiness.
It is a stronger governance posture than `draft_only`, but it still belongs to the review layer rather than to the execution layer.

A lawful operator-review boundary object must therefore answer all three questions:

- what objective trigger moves a surface out of pure `draft_only`
- what explicit operator act is required before any stronger posture is acknowledged
- what holds keep the reviewed surface from masquerading as execution authority

---

## Minimum lawful ingredients

A future `operator_review_required` classification should not be named unless the boundary object can identify at least:

### 1. Review trigger object
A clearly stated trigger showing why the surface is no longer adequately described as pure `draft_only`.

### 2. Review scope object
A clearly stated description of what the operator is reviewing:

- wording only
- routing only
- export only
- bounded next-step suggestion only

The review scope may not be left implicit.

### 3. Review act object
A clearly stated operator act that remains review-only rather than executional.
Examples may include:

- acknowledge for manual follow-up
- mark as review candidate
- freeze for later handoff

None of these acts may mutate governed objects automatically.

### 4. Retained anti-execution holds
The reviewed surface must still explicitly preserve at least:

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`

### 5. Boundary honesty sentence
The object must explicitly say that operator review does not by itself create execution authority.

---

## Current lawful reading

At the current stage, existing cockpit result surfaces remain lawfully classified as:

- `draft_only`
- `surface_only`
- `non-executable at current stage`

COCKPIT3-B does not upgrade those defaults.
It only defines the minimum object that would be required before a future upgrade to `operator_review_required` could be discussed honestly.

---

## Wrong readings to block

The following readings are unlawful:

- "operator review means the cockpit may now execute after one click"
- "operator review is a UI synonym for approval"
- "operator review removes the retained anti-runtime holds"
- "operator review authorizes governed mutation so long as a human is present"

---

## Stage reading

The right reading of COCKPIT3-B is:

> a boundary object for naming review posture without collapsing review into execution.

The wrong reading is:

> the cockpit is now approaching live runtime authority.
