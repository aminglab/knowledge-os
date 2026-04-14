# COCKPIT1-B Prototype README

## Purpose

This directory contains the first **zero-build static cockpit skeleton** for COCKPIT1-B.

It is intentionally narrow.
It exists to prove that the cockpit can:

- center on real governed objects
- switch across five required screen states
- bind two distinct pilot cases into one shared cockpit frame
- keep the sidecar visibly subordinate

## Files

- `index.html` — static prototype shell
- `styles.css` — prototype layout and visual hierarchy
- `app.js` — hardcoded state fixtures and screen switching logic

## Preview

Open `index.html` directly in a browser, or serve the directory with a simple static server.

Example:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/cockpit/COCKPIT1-B/prototype/
```

## Boundary

This prototype does **not** claim:

- live backend behavior
- live model routing
- write-capable object actions
- team-layer functionality
- production UI polish

It is a bounded static skeleton only.
