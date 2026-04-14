# COCKPIT1-C Slot Contract v1

## Status

Drafted for prototype hardening.

## Function

This file defines the minimum slot contract for the static cockpit frame.

---

## One-sentence slot ruling

> **The cockpit frame is lawful only if each visible region continues to serve its bounded role.**

---

## Required slots

### `left_rail`
Must own:

- state navigation
- case visibility
- route or screen switching affordance

Must not pretend to be:

- the main object surface
- the sidecar console

### `main_panel`
Must own:

- current screen title
- current semantic subtitle
- status line
- primary object/state cards

This remains the cockpit center.

### `right_rail`
Must own:

- pressure stack
- verdict stack
- activity or attention stack

It may summarize judgment pressure but must not replace the main panel.

### `sidecar`
Must own:

- temporary analysis hints
- drafting posture
- bounded exploratory guidance

It must remain explicitly subordinate to the object-centered frame.

---

## Slot drift failures

The following count as failures:

- missing `main_panel` title/subtitle
- missing visible sidecar discipline cue
- right rail disappearing entirely
- left rail no longer exposing state navigation

---

## Final slot block

- required slots: 4
- cockpit center: `main_panel`
- subordinate slot: `sidecar`
