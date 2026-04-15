# COCKPIT2-B Trigger Output Grammar v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum output grammar for COCKPIT2-B trigger results.
It exists to make trigger outputs more structured without crossing into governed writes.

---

## Governing principle

The cockpit may expose richer output grammar only if the output remains:

- draft-only
- bounded by output class
- tied to a named anchor
- visibly narrower than mutation

---

## Minimum lawful output classes

The current output grammar should remain limited to five classes aligned with the current trigger set:

### 1. `scan_result`
For gap scans and missing-evidence surfaces.

### 2. `draft_response`
For draft dissent-response surfaces.

### 3. `condition_check`
For upgrade-condition or threshold checks.

### 4. `continuation_suggestion`
For next-step or route-ordering suggestions.

### 5. `summary_draft`
For bounded progress-summary or export-summary drafts.

---

## Required output structure

A lawful structured trigger output should support at least the following sections when relevant:

- current anchor
- output class
- main result body
- basis or evidence note
- unresolved remainder
- next-step hint

Not every output needs every field.
But the output grammar must remain visibly structured enough that it can be distinguished from loose chat prose.

---

## Forbidden output postures

The current output grammar must not drift into result language such as:

- `committed`
- `upgraded`
- `resolved`
- `published`
- `executed`

Those are not lawful current output classes for COCKPIT2-B.

---

## Alignment rule

The trigger-output grammar should remain aligned with:

- the current trigger set from COCKPIT2-A
- the current anti-runtime and anti-mutation holds
- the current result-card contract

If the project later widens the trigger universe, the output grammar may widen then.
It should not widen in advance by imagination alone.
