# COCKPIT2-A Interactive Fixtures v1

## Status

Drafted for current threshold.

## Function

This file records the bounded fixture set for the first COCKPIT2-A interactive prototype lift.
The purpose of these fixtures is to prove stronger interaction without opening runtime mutation.

---

## Fixture scope

COCKPIT2-A is intentionally limited to one stronger prototype shell with:

- two bound pilot cases
- the existing five cockpit screen states
- four bounded lenses
- named object anchors per state
- five suggestion-layer action triggers
- one audit-style sidecar log

---

## Required screen-state continuity

The prototype must still retain the five bound states already proven by COCKPIT1-B:

- `landing`
- `hpClaim`
- `hpVerdict`
- `ppDissent`
- `ppRoute`

COCKPIT2-A does not replace these fixtures.
It adds a stronger interaction layer over them.

---

## Required lens fixtures

The prototype must expose at least four bounded lenses:

- `focus`
- `pressure`
- `route`
- `boundary`

These lenses may change foreground emphasis.
They may not change governed object state.

---

## Required object-browse fixtures

Each bound state must expose at least two named object anchors.
At least one case must expose three or more anchors.

Examples of lawful anchor kinds include:

- claim anchor
- evidence anchor
- dissent anchor
- verdict anchor
- route anchor
- source anchor

---

## Required trigger fixtures

The prototype must expose at least the following five bounded triggers:

- `scan missing evidence`
- `draft dissent response`
- `check upgrade conditions`
- `suggest canonical continuation`
- `prepare progress summary`

All trigger fixtures must remain suggestion-layer only.

---

## Required sidecar honesty

The sidecar may display:

- temporary audit notes
- local operator hints
- draft-only trigger outputs

The sidecar must not masquerade as a write-capable command center.
