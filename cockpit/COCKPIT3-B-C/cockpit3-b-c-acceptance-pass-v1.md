# COCKPIT3-B-C Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT3-B-C / Emitted Review Family Labels Lift v1**.
It does not claim that emitted family labels open stronger authority.
It records what must become true before a lawful emitted-label lift verdict can be issued.

---

## Primary verdict set

- `PASS_REVIEW_FAMILY_LABELS_EMITTED`
- `PASS_REVIEW_FAMILY_LABELS_CHECKER_VISIBLE`
- `HOLD_EMITTED_FAMILY_LABELS_NOT_YET_COHERENT`
- `FAIL_EMITTED_FAMILY_LABELS_NOT_FORMED`

---

## Required acceptance checks

### 1. Trigger-family emission check

The bounded prototype must visibly emit a `review_trigger_family` label.

### 2. Scope-family emission check

The bounded prototype must visibly emit a `review_scope_family` label.

### 3. Family-floor legality check

Emitted labels must come from the lawful COCKPIT3-B-B family floor rather than ad hoc or authority-heavy labels.

### 4. Checker-surface visibility check

The emitted labels must be part of the checker-visible prototype surface rather than buried only in prose.

### 5. Boundary-honesty continuity check

The emitted labels must remain accompanied by the current non-upgrade clause and all current anti-execution posture markers.

---

## Pass condition

`PASS_REVIEW_FAMILY_LABELS_EMITTED` is lawful only if checks 1, 2, 3, and 5 pass.

`PASS_REVIEW_FAMILY_LABELS_CHECKER_VISIBLE` is lawful only if all five required checks pass together.
