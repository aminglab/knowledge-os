# COCKPIT3-A Governance Sidecar v1

## Status

Drafted for current threshold.

## Function

This file defines the first governance sidecar lift for COCKPIT3-A.
Its purpose is to make execution-boundary governance visible next to current cockpit result surfaces without granting execution authority.

---

## Governing principle

A governance sidecar is lawful only when it makes action boundaries more visible, not more permissive.
The sidecar may display:

- current execution-boundary class
- current action posture
- future classes not opened yet

The sidecar may not silently upgrade result surfaces into executable actions.

---

## Minimum visible governance fields

The first sidecar should visibly expose at least:

1. `execution_boundary_class`
2. `action_posture`
3. `current_default_status`
4. `future_classes_not_opened_yet`

At the current threshold, the lawful default remains:

- execution boundary class: `draft_only`
- action posture: `surface_only`
- current default status: `non-executable at current stage`

---

## Sidecar reading

The right reading is:

> the cockpit can now show why a result surface is non-executable.

The wrong reading is:

> the cockpit is now one click away from execution.
