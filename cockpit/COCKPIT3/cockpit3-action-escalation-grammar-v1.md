# COCKPIT3 Action Escalation Grammar v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum escalation grammar for actions that could ever sit downstream of cockpit result surfaces.
It does not authorize execution.
It only defines the governance language that later objects would have to satisfy.

---

## Governing principle

The current cockpit line already supports structured result surfaces.
A later system may wish to act on some of those surfaces.
Before that ever becomes lawful, the system needs a grammar for the escalation path itself.

---

## Minimum escalation steps

The escalation grammar should at minimum distinguish:

### 1. `surface_only`
The result exists only as a visible cockpit surface.
No action is implied.

### 2. `review_candidate`
The result may be considered by a human operator for a later stronger threshold object.
The current layer still does not authorize action.

### 3. `forbidden_at_current_stage`
The result belongs to a class that may not be escalated further at the current stage.

---

## Current lawful reading

At the current threshold, the cockpit may classify and stage escalation posture, but it may not itself authorize escalation into execution.

This means the escalation grammar is a governance grammar, not an execution pipeline.

---

## Anti-overclaim rule

The system must not let words like:

- execute
- commit
- apply
- resolve
- publish

appear as lawful current cockpit action postures unless a later stronger object explicitly makes them lawful.
