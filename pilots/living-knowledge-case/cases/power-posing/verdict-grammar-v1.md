# Verdict Grammar v1

This file defines the current **verdict grammar v1** for the power-posing pilot.

Its purpose is narrow:

- make the public-facing status wording in `snapshot-v2.md` explicit,
- tie that wording to concrete claim and verdict objects,
- and reduce silent drift between reader-facing language and object-layer judgment fields.

This is still case-scoped.
It does **not** claim to be a repository-wide verdict constitution.

---

## Why this layer exists

The current pilot already has three layers that can drift apart if left unchecked:

- public snapshot wording,
- claim object status fields,
- verdict object level fields and body language.

This file introduces a small canonical bridge between them.

---

## Entry surface

Each verdict grammar entry below is expected to expose at least:

- `Claim id`
- `Verdict id`
- `Snapshot label`
- `Snapshot current state`
- `Required claim epistemic status`
- `Required verdict level`
- `Required verdict anchors`

The anchor list is intentionally lightweight.
It does not try to freeze every sentence in a verdict body.
It only asserts the minimum wording anchors that should remain present if the public-facing status is still honest.

---

## Current entries

### `original_claim_status`
- Claim id: `C-0001`
- Verdict id: `V-0001`
- Snapshot label: `Original claim`
- Snapshot current state: `contested and significantly weakened`
- Required claim epistemic status: `contested`
- Required verdict level: `weakened`
- Required verdict anchors: `contested`, `weakened`, `split lineage`

### `descendant_claim_status`
- Claim id: `C-0002`
- Verdict id: `V-0002`
- Snapshot label: `Descendant claim`
- Snapshot current state: `contested but still surviving`
- Required claim epistemic status: `contested`
- Required verdict level: `contested`
- Required verdict anchors: `contested`, `surviving`, `weaker`

---

## Current note

This grammar layer is deliberately small.

If the pilot later changes its public-facing wording, that change should be reflected here explicitly rather than only drifting through snapshot prose or verdict bodies by accident.
