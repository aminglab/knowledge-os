# CEDV-C / Enum Coverage v1

## Status

Protocol enum-coverage lift after CEDV-B.

## Function

This file records the first expanded enum drift-coverage layer for CEDV.

The goal is narrow:

> extend protocol constants drift checking beyond `verdict_level` so the current working enum vocabularies remain aligned between protocol docs and checker-facing constants.

This does not freeze the final enum doctrine.
It makes the current working vocabulary harder to silently fork.

---

## Entry context

Before this step, CEDV already had:

- schema floor;
- relation and basis validation floor;
- shared constant-authority layer;
- canonical example registry;
- example-registry checker and workflow.

However, the protocol constants checker still mainly exercised:

- `verdict_level`;
- canonical relation names.

Meanwhile `scripts/lib/protocol_constants.py` already carried additional enum families:

- `lifecycle_state`;
- `epistemic_status`;
- `visibility`;
- `dissent_kind`;
- `severity`.

That mismatch created a second-order drift risk: the constants module looked shared, but only part of its enum surface was checked against the public protocol document.

---

## Covered enum families

CEDV-C expands the drift checker over the current working enum families:

- `lifecycle_state`;
- `epistemic_status`;
- `visibility`;
- `dissent_kind`;
- `severity`;
- `verdict_level`.

Canonical relation names remain checked against:

- `protocol/link-types.md`.

---

## Checker change

The updated checker is:

- `scripts/check_protocol_constants.py`.

It now imports these working sets from:

- `scripts/lib/protocol_constants.py`.

And checks them against:

- `protocol/enums.md`;
- `protocol/link-types.md`;
- `protocol/cedv/canonical-object-schema-v1.md`;
- this file.

---

## Acceptance result

CEDV-C / ENUMCOVER1 is accepted at the following level:

> `PASS_WORKING_ENUM_COVERAGE_LAYER`

Meaning:

- all current enum families in the shared constants module are checked against `protocol/enums.md`;
- canonical relation names continue to be checked against `protocol/link-types.md`;
- the CEDV schema continues to delegate enum and link ownership to protocol-level authority files;
- this file records the reason the checker grew beyond `verdict_level`.

---

## Retained holds

This pass does **not** claim:

- final enum freeze;
- complete type-system validation;
- JSON Schema generation;
- full repository-wide enum migration;
- proof that every checker has stopped using private constants;
- permanent endorsement of every current enum value.

The current result is drift coverage for the present working set, not final vocabulary law.

---

## Known future pressure

Likely future pressure points:

1. `contested` and `weakened` may later migrate out of `verdict_level` into claim-like `epistemic_status` or transition grammar.
2. `linked` may later become evidence-specific rather than global `lifecycle_state`.
3. `severity` may need a richer scale or source-specific semantics.
4. `visibility` may need intermediate states between private/team/public.

Those are future explicit protocol moves.
They should not happen as silent checker drift.

---

## Next recommended move

The natural continuation is:

> `CEDV-D / CHECKERIMPORT1`

Purpose:

> audit remaining protocol-facing checkers for hardcoded CEDV vocabulary and progressively move them to shared constants where warranted.

Enum coverage makes drift visible.
Checker import convergence will reduce how many places can drift in the first place.
