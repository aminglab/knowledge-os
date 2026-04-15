# COCKPIT1-F Operator Note v1

## Status

Drafted for use.

## Function

This file defines the minimum operator note for using the COCKPIT1-B static prototype through the current preview route.

---

## One-sentence operator ruling

> **Use the cockpit prototype as a bounded demonstration surface, not as a writable working application.**

---

## Minimum operator sequence

### 1. Enter the prototype directory

```bash
cd cockpit/COCKPIT1-B/prototype
```

### 2. Start the preview helper

```bash
python preview_cockpit.py
```

Optional:

```bash
python preview_cockpit.py --port 8010 --no-browser
```

### 3. Confirm the preview surface

The operator should confirm that the screen visibly contains:

- left-rail state navigation
- main-panel title and subtitle
- right-rail pressure/verdict/activity stack
- sidecar discipline block

### 4. Run the standard demo sequence

The operator should move through the five required screen states in the standard order rather than jumping randomly.

### 5. Exit honestly

When the demo ends, the operator should describe the surface as:

- a zero-build static cockpit skeleton
- a bounded prototype
- not a production frontend

---

## Operator prohibitions

The operator should not present the prototype as:

- a live runtime
- a team-layer workspace
- a write-capable object editor
- a replacement for the public-case entry chain

---

## Final operator block

- entry command: `python preview_cockpit.py`
- standard order: required
- bounded-prototype honesty: mandatory
