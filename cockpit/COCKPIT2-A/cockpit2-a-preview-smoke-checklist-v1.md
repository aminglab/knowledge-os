# COCKPIT2-A Preview Smoke Checklist v1

## Status

Drafted for current threshold.

## Function

This file defines one minimal smoke route for the COCKPIT2-A interactive prototype.
It is not a production QA matrix.
It only proves that the bounded interactive lift can be previewed locally and read honestly.

---

## Preview command

From `cockpit/COCKPIT2-A/prototype/` run:

```bash
python preview_cockpit2_a.py
```

Optional:

```bash
python preview_cockpit2_a.py --no-browser
python preview_cockpit2_a.py --port 8012
```

---

## Minimum smoke route

### 1. Open the landing state
Check that the shell visibly presents:

- the five bound state families
- object anchors in the left rail
- lens buttons in the main-panel header
- suggestion-layer triggers in the right rail
- a sidecar audit log at the bottom

### 2. Switch from `landing` to `hpClaim`
Check that:

- the screen title changes
- the active object anchor resets to the first case-scoped object
- the sidecar audit log records a state switch note

### 3. Switch the active lens to `pressure`
Check that:

- the active object anchor remains preserved
- the main panel foreground changes from focus reading to pressure reading
- the UI does not imply any governed object mutation

### 4. Switch the active object anchor inside `hpClaim`
Check that:

- the active object card changes
- the lens remains preserved
- the sidecar audit log records an object-anchor switch

### 5. Run one bounded trigger
Trigger `draft dissent response` or `prepare progress summary`.
Check that:

- the sidecar audit log records a draft-only trigger note
- the UI still reads as suggestion-layer only
- nothing on screen implies a committed verdict, object write, or publication event

### 6. Switch to `boundary` lens on `hpVerdict`
Check that:

- retained holds remain visible
- the current boundary reading is foregrounded
- the prototype does not drift into runtime-control language

---

## Smoke pass reading

The smoke route passes only if the preview proves:

- stronger interaction than COCKPIT1-B
- preserved object-centered reading
- preserved anti-runtime honesty
- preserved anti-mutation honesty

If the preview reads like a live governed application, the smoke route has failed.
