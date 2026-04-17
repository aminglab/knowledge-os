# COCKPIT3 Execution Boundary Floor v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum execution-boundary floor for COCKPIT3.
Its purpose is to make explicit the governance object that separates a lawful draft-only cockpit result from any future action class that would require stronger review or remain forbidden at the current stage.

---

## Governing principle

The cockpit may expose structured result surfaces before it exposes execution authority.
Therefore the system needs an object that answers:

- what always remains draft-only
- what may require explicit operator review
- what is execution-forbidden at the current threshold

The execution-boundary floor exists to answer those questions without falsely authorizing execution itself.

---

## Minimum lawful boundary classes

The execution-boundary floor should at minimum support these classes:

### 1. `draft_only`
The result surface may be shown, copied, exported as draft text, or used for later human review, but it may not trigger governed mutation or execution.

### 2. `operator_review_required`
The result surface may be considered for later action only after explicit operator review and a stronger threshold object. The current floor does not itself authorize that stronger action.

### 3. `execution_forbidden`
The result surface belongs to a class that must remain non-executable at the current stage, regardless of apparent convenience.

---

## Current lawful reading

At the current project stage, every existing cockpit result surface should still default to `draft_only` unless a later stronger governance object explicitly proves otherwise.

The existence of an execution-boundary class does not mean execution has been authorized.
It means the line between output and action is now being governed explicitly.

---

## Stage reading

The right reading of COCKPIT3 is:

> governance for future action boundaries.

The wrong reading is:

> the cockpit is now allowed to execute things.
