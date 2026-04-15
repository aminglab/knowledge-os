# COCKPIT2-B-A First Trigger Scope v1

## Status

Drafted for current threshold.

## Function

This file defines the first bounded trigger scope for COCKPIT2-B-A.
It exists to keep the first implementation small, readable, and honest.

---

## Scope rule

The first COCKPIT2-B-A implementation should not try to upgrade the whole trigger universe at once.
It should prove the result-card pattern on a narrow initial slice.

---

## Current first-scope recommendation

The most natural first-scope trigger is:

- `check upgrade conditions`

A lawful optional companion trigger is:

- `prepare progress summary`

These are good first candidates because they naturally produce bounded draft surfaces without implying immediate mutation.

---

## Why this scope is lawful

`check upgrade conditions` already reads as a bounded inspection trigger.
It can produce a structured `condition_check` result card without pretending that the underlying claim or verdict has already been changed.

`prepare progress summary` can likewise produce a `summary_draft` result card without implying publication or committed export.

---

## Current non-scope

The first lift should not yet attempt to turn every trigger into a full structured card surface.
That broader move may come later after the first card pattern proves coherent.
