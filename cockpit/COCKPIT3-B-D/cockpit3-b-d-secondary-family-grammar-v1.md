# COCKPIT3-B-D Secondary Family Grammar v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum grammar floor for secondary family labels and any future multi-family representation inside COCKPIT3-B-D.
Its purpose is to answer a narrow governance question:

> when is a single primary family label enough, and when would a secondary family label become lawful rather than noisy?

---

## Governing principle

Primary family labels are the current default because they maximize compactness, checker visibility, and boundedness.
A secondary label is lawful only when it adds real governance information that cannot be honestly preserved inside the primary label plus prose explanation.

Multi-family grammar is therefore not the default.
It is an exception that must justify itself.

---

## Current default discipline

At the current stage, the lawful default remains:

- one primary `review_trigger_family`
- one primary `review_scope_family`
- no required secondary family labels
- no required multi-family arrays

This default should remain in force unless a stronger grammar object proves otherwise.

---

## Minimum admissibility tests for secondary labels

A secondary family label should not be admitted unless all of the following are true:

### 1. Non-redundancy test
The secondary label adds governance information that the primary label plus ordinary prose cannot already carry.

### 2. Checker-clarity test
The secondary label can remain machine-checkable without making the checker surface ambiguous or noisy.

### 3. Boundary-honesty test
The secondary label does not smuggle in stronger authority or make a bounded prototype sound less bounded.

### 4. Compactness test
The gain from the secondary label is greater than the cost in emitted-surface complexity.

---

## Unlawful early moves

The following remain unlawful at this stage:

- mandatory multi-family emission for every current card
- authority-heavy secondary labels
- secondary labels used as a substitute for execution, approval, or mutation posture
- sidecar arrays that make the bounded prototype look like a runtime classifier

---

## Current lawful reading

The right reading is:

> secondary labels are not forbidden forever, but they must earn their existence.

The wrong reading is:

> once families exist, the prototype should immediately emit as many as possible.
