# COCKPIT3-B-C Emitted Review Family Labels v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum emitted-label surface for COCKPIT3-B-C.
Its purpose is to connect the review-family grammar from COCKPIT3-B-B back into the bounded COCKPIT3-B-A prototype so that review families become visible labels rather than hidden interpretive assumptions.

---

## Governing principle

An emitted family label is a **classification surface**, not an authority surface.
It answers:

> which review family is currently being emitted here?

It does **not** answer:

> what stronger action is now authorized?

---

## Minimum emitted fields

The minimum emitted-label floor should support at least:

1. `review_trigger_family`
2. `review_scope_family`

At the current bounded prototype threshold, these labels may be emitted as single primary labels for the active draft card.
They do not need to express exhaustive multi-family coverage yet.

---

## Current bounded mapping floor

The current prototype may lawfully emit at least the following primary mappings:

### `summary_review`
- `review_trigger_family: export_surface_pressure`
- `review_scope_family: export_only`

### `continuation_review`
- `review_trigger_family: routing_handoff_pressure`
- `review_scope_family: routing_only`

These mappings remain review-only classifications.
They do not lawfully upgrade the current result surface into `operator_review_required`.

---

## Boundary honesty clause

The emitted labels must remain accompanied by:

- `execution_boundary_class: draft_only`
- `action_posture: surface_only`
- `current_default_status: non-executable at current stage`
- the explicit clause that no current governed result surface is yet lawfully classified as `operator_review_required`
