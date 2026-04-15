# COCKPIT1-E Preview Check Pass v1

## Status

Drafted for evaluation.

## Function

This file records the minimum pass grammar for cockpit preview-route consistency.

---

## Current verdict grammar

- `PASS_COCKPIT_PREVIEW_ROUTE_CONSISTENCY`
- `HOLD_COCKPIT_PREVIEW_ROUTE_NEEDS_REALIGNMENT`
- `FAIL_COCKPIT_PREVIEW_ROUTE_DRIFT`

---

## Minimum pass checks

### 1. Helper existence check
`preview_cockpit.py` must exist.

### 2. Prototype README exposure check
The prototype README must expose the helper and show a usable preview command.

### 3. Root README exposure check
The root README must expose the cockpit preview route as a modest local preview path.

### 4. PUBLIC-ENTRY exposure check
`PUBLIC-ENTRY.md` must expose the cockpit preview route as additive and non-replacing.

### 5. Honesty wording check
The exposed route must retain prototype honesty rather than drifting into production-shell language.

---

## Pass rule

`PASS_COCKPIT_PREVIEW_ROUTE_CONSISTENCY` is lawful only if all five minimum pass checks pass.

---

## Final pass block

- pass checks: 5
- required full pass: yes
- route drift tolerance: none
