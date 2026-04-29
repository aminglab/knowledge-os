# Protocol Enums (Working Set)

This file defines the current working enum-style vocabularies used across early pilots.
It is not a final protocol freeze.

The purpose is simple:

> prevent silent vocabulary drift while the language is still young.

---

## lifecycle_state

Current working values:

- `draft`
- `active`
- `paused`
- `superseded`
- `withdrawn`
- `archived`
- `linked`

Notes:

- `linked` is currently used for evidence objects that are already attached into a claim neighborhood.
- not every object family will use every value.

---

## epistemic_status

Current working values for claim-like knowledge standing:

- `under_evaluation`
- `supported`
- `contested`
- `weakened`
- `rejected`
- `split`
- `stabilized`

Notes:

- these values are intentionally provisional,
- but pilots should not invent new ones casually.

---

## visibility

Current working values:

- `private`
- `team`
- `public`

---

## dissent_kind

Current working values:

- `empirical`
- `methodological`
- `logical`
- `definitional`
- `procedural`
- `scope`
- `interpretive`

---

## severity

Current working values:

- `low`
- `medium`
- `high`
- `critical`

---

## verdict_level

Current working values for verdict objects:

- `local`
- `provisional`
- `supported`
- `stabilized`
- `rejected`
- `split`
- `unresolved`

Notes:

- `verdict_level` is distinct from claim-like `epistemic_status`.
- older pilot materials may still use claim-status words such as `under_evaluation`, `contested`, or `weakened`; those should be migrated deliberately rather than silently mixed into new verdict objects.
- this working set is mirrored in `scripts/lib/protocol_constants.py` so checkers have one shared source for current protocol constants.
