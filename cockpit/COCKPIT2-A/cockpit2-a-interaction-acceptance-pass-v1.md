# COCKPIT2-A Interaction Acceptance Pass v1

## Status

Passed at current threshold.

## Function

This file records a narrower acceptance verdict for the **current COCKPIT2-A interactive prototype**.
It does not evaluate an imagined future cockpit.
It only evaluates the currently implemented bounded lift together with its current preview and consistency surfaces.

---

## One-sentence acceptance verdict

Current acceptance verdict:

> **The current COCKPIT2-A prototype lawfully passes as a bounded interactive cockpit lift.**
>
> **It now demonstrates stronger interaction than the COCKPIT1 static floor through a bounded lens switch, bounded object-browse wiring, bounded suggestion-layer triggers, a local preview path, a smoke route, and interaction-consistency checks, while remaining narrower than runtime, team-layer, write-capable, or production frontend claims.**

---

## Evaluation target

The current acceptance target is not the whole COCKPIT2 program.
It is the current COCKPIT2-A prototype as represented by:

- `cockpit/COCKPIT2-A/prototype/index.html`
- `cockpit/COCKPIT2-A/prototype/styles.css`
- `cockpit/COCKPIT2-A/prototype/app.js`
- `cockpit/COCKPIT2-A/prototype/README.md`
- `cockpit/COCKPIT2-A/prototype/preview_cockpit2_a.py`
- `cockpit/COCKPIT2-A/cockpit2-a-preview-route-v1.md`
- `cockpit/COCKPIT2-A/cockpit2-a-preview-smoke-checklist-v1.md`
- `scripts/check_cockpit2_a_interactive_prototype.py`
- `scripts/check_cockpit2_a_interaction_consistency.py`
- the two corresponding workflows

---

## Detailed acceptance checks

### 1. Stronger interaction check — PASS

The current prototype visibly exceeds the COCKPIT1 static floor by exposing:

- five bound state surfaces
- four bounded lenses (`focus`, `pressure`, `route`, `boundary`)
- a bounded object-anchor surface in the left rail
- a suggestion-layer trigger surface in the right rail
- an audit-style sidecar log that records interaction events

This is enough to treat the current lift as genuinely interactive rather than only static.

### 2. Object-browse integrity check — PASS

The current prototype remains anchored in named case-scoped objects.
The active state controls the available anchors, and the active anchor controls the main-panel foreground.
Switching lenses preserves the current anchor unless the user explicitly changes it.

This is a lawful object-browse surface rather than floating graph drift.

### 3. Trigger honesty check — PASS

The current trigger surface remains suggestion-layer only.
The visible posture stays within:

- `scan`
- `draft`
- `check`
- `suggest`
- `prepare`

The current prototype does not claim:

- committed verdict mutation
- governed object writes
- publication events
- runtime task execution

### 4. Boundary honesty check — PASS

The current prototype still visibly preserves the core holds:

- `HOLD_NO_LIVE_RUNTIME_COCKPIT`
- `HOLD_NO_WRITE_CAPABLE_COCKPIT_SURFACE`
- `HOLD_NO_TEAM_LAYER_COCKPIT`
- `HOLD_NO_PRODUCTION_FRONTEND_CLAIM`
- `HOLD_NO_REPOSITORY_WIDE_COCKPIT_GENERALIZATION`
- `HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND`

The prototype reads as a bounded interactive lift rather than a live governed application.

### 5. Case-binding continuity check — PASS

The currently bound pilot cases remain visible and distinct.
At least one meaningful end-to-end route is now explicit for `h-pylori-ulcer`:

- landing
- `hpClaim`
- `pressure` lens
- object-anchor switch
- bounded trigger run
- `hpVerdict`
- `boundary` lens

This is enough to count as a lawful interactive case-navigation path at the current threshold.

---

## Current pass verdicts now lawful

The following verdicts are now lawful for the current COCKPIT2-A prototype:

- `PASS_INTERACTIVE_COCKPIT_PROTOTYPE_FLOOR`
- `PASS_INTERACTIVE_COCKPIT_CASE_NAVIGATION`

The following verdicts are not warranted by this file:

- runtime cockpit pass
- write-capable cockpit pass
- team-layer cockpit pass
- production frontend pass

---

## Final acceptance block

- evaluated object: `COCKPIT2-A bounded interactive prototype`
- interaction verdict: `PASS_INTERACTIVE_COCKPIT_PROTOTYPE_FLOOR`
- navigation verdict: `PASS_INTERACTIVE_COCKPIT_CASE_NAVIGATION`
- retained holds: unchanged
