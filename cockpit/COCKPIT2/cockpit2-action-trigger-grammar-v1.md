# COCKPIT2 Action Trigger Grammar v1

## Status

Drafted for current threshold.

## Function

This file defines which cockpit actions may be exposed as bounded triggers in COCKPIT2.
Its purpose is to strengthen the front-door action surface without opening direct frontend mutation of governed objects.

---

## Governing principle

Every COCKPIT2 action trigger must satisfy all of the following:

- named object anchor
- declared read scope
- declared output class
- audit trace expectation
- no direct governed-object mutation from the trigger itself

The cockpit may expose stronger action entry points.
It may not yet expose write-capable object governance from the frontend.

---

## Lawful trigger set

### 1. Missing-evidence scan
The cockpit may expose a trigger that asks for a bounded scan of missing evidence around a focus claim or route.

Expected output class:
- suggestion
- gap list
- priority hints

### 2. Dissent-response draft
The cockpit may expose a trigger that drafts a response posture for a bounded dissent object.

Expected output class:
- response draft
- unresolved remainder
- required new basis

### 3. Upgrade-condition check
The cockpit may expose a trigger that inspects whether a visible claim or verdict surface appears to satisfy its current upgrade boundary.

Expected output class:
- condition check
- unmet conditions
- guarded suggestion

### 4. Canonical continuation suggestion
The cockpit may expose a trigger that proposes the next bounded continuation for a visible route or focus object.

Expected output class:
- continuation suggestion
- route ordering hint
- risk note

### 5. Progress-summary export draft
The cockpit may expose a trigger that drafts a bounded progress summary from the currently visible governed surface.

Expected output class:
- export draft
- operator summary
- bounded case recap

---

## Trigger/output distinction

A trigger is not yet a write action.
For COCKPIT2, the trigger may ask the backend to produce:

- suggestion objects
- draft text
- bounded diagnostics
- export-ready summaries

The trigger may not directly:

- rewrite claim state
- rewrite verdict state
- create authoritative evidence objects
- publish to the public layer
- open runtime task persistence

---

## Required UI honesty

If a COCKPIT2 trigger is exposed in the prototype, the UI must not pretend that the action has already committed governed changes.
The visible posture must remain closer to:

- `suggest`
- `draft`
- `scan`
- `check`
- `prepare`

and must not drift into:

- `commit`
- `upgrade`
- `publish`
- `resolve`
- `freeze`

unless a later threshold explicitly makes those lawful.
