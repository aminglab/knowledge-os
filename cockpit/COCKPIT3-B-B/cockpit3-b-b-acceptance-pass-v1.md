# COCKPIT3-B-B Acceptance Pass v1

## Status

Not yet evaluated.

## Function

This file defines the acceptance grammar for **COCKPIT3-B-B / Review Trigger and Scope Families Floor v1**.
It does not claim that any current surface is already lawfully classified as `operator_review_required`.
It records what must become true before a lawful review-family floor verdict can be issued.

---

## Primary verdict set

- `PASS_REVIEW_TRIGGER_FAMILIES_FLOOR`
- `PASS_REVIEW_SCOPE_FAMILIES_FLOOR`
- `PASS_REVIEW_FAMILY_GRAMMAR_COHERENT`
- `HOLD_REVIEW_FAMILY_FLOOR_NOT_YET_COMPACT`
- `FAIL_REVIEW_FAMILY_GRAMMAR_NOT_FORMED`

---

## Required acceptance checks

### 1. Trigger-family compactness check

The trigger grammar must define a compact family floor without leaving every trigger as free prose.

### 2. Scope-family compactness check

The scope grammar must define a compact family floor without leaving every scope description as free prose.

### 3. Pressure-vs-authority distinction check

Trigger families must remain pressure classes and scope families must remain bounded object-of-review classes. Neither may masquerade as authority classes.

### 4. Unlawful-family exclusion check

The family grammar must explicitly exclude authority-heavy names such as execution, mutation, approval, publish, or team-control classes.

### 5. Retained-boundary honesty check

The family floor must explicitly preserve the current non-upgrade clause that no current surface is already lawfully classified as `operator_review_required`.

---

## Pass condition

`PASS_REVIEW_TRIGGER_FAMILIES_FLOOR` is lawful only if the trigger floor passes checks 1, 3, 4, and 5.

`PASS_REVIEW_SCOPE_FAMILIES_FLOOR` is lawful only if the scope floor passes checks 2, 3, 4, and 5.

`PASS_REVIEW_FAMILY_GRAMMAR_COHERENT` is lawful only if all five required checks pass together.
