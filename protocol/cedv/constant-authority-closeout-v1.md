# CEDV-A / Constant Authority Closeout v1

## Status

Stage closeout after PR #56.

## Function

This file closes the first constant-authority pass for the CEDV protocol line.

The goal of this pass is not to freeze the final Knowledge OS protocol.
The goal is narrower:

> make the current CEDV working vocabulary explicit, shared, and checkable so individual checkers no longer define private protocol law.

---

## Entry context

Before this closeout, the project already had:

- `protocol/cedv/canonical-object-schema-v1.md` as the first CEDV schema floor;
- `protocol/cedv/relation-basis-validation-v1.md` as the first CEDV graph-validity implementation subset;
- `scripts/check_cedv_canonical_schema.py`;
- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_protocol_record_consistency.py`.

However, a drift risk remained:

1. relation constants were duplicated across checkers;
2. `verdict_level` was not yet documented as a working enum;
3. individual checkers were beginning to carry their own private protocol vocabularies.

That risk was acceptable during early prototyping.
It is no longer acceptable after CEDV became the protocol core.

---

## What PR #56 closed

PR #56 established the first shared constant-authority layer by adding:

- `scripts/lib/protocol_constants.py`;
- `scripts/lib/__init__.py`;
- `scripts/check_protocol_constants.py`;
- `.github/workflows/check-protocol-constants.yml`.

It also updated:

- `protocol/enums.md`;
- `protocol/cedv/canonical-object-schema-v1.md`;
- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_protocol_record_consistency.py`.

The resulting structure is now:

- `protocol/enums.md` owns current enum-style vocabulary;
- `protocol/link-types.md` owns canonical relation language;
- `scripts/lib/protocol_constants.py` mirrors the working set for checkers;
- `scripts/check_protocol_constants.py` checks for silent drift between docs and checker constants;
- CEDV schema now points to vocabulary owners instead of re-listing private enum sets.

---

## Current authority chain

### Enum authority

Current working enum vocabularies are documented in:

- `protocol/enums.md`

This includes:

- `lifecycle_state`;
- `epistemic_status`;
- `visibility`;
- `dissent_kind`;
- `severity`;
- `verdict_level`.

### Relation authority

Canonical relation names are documented in:

- `protocol/link-types.md`

Current canonical floor:

- `supports`;
- `challenges`;
- `cites`;
- `depends_on`;
- `descends_from`;
- `supersedes`;
- `pinned_in_snapshot`.

### Checker mirror

Current checker-facing working sets are mirrored in:

- `scripts/lib/protocol_constants.py`

This file is not the public doctrine.
It is the checker-facing mirror of the public doctrine.

### Drift check

Current drift is checked by:

- `scripts/check_protocol_constants.py`
- `.github/workflows/check-protocol-constants.yml`

This checker does not prove the protocol is final.
It only ensures that the current docs and checker constants do not silently diverge.

---

## Acceptance result

CEDV-A / CONSTANTAUTH1 is accepted at the following level:

> `PASS_WORKING_CONSTANT_AUTHORITY_LAYER`

Meaning:

- shared constants now exist;
- CEDV schema delegates enum and relation ownership to protocol-level files;
- relation and verdict constants are no longer independently redefined inside the updated checkers;
- a drift checker exists and is wired into CI;
- the current working enum set preserves live-pilot compatibility instead of breaking existing records silently.

---

## Retained holds

This closeout does **not** claim any of the following:

- no final protocol freeze;
- no full schema language;
- no repository-wide object migration completion;
- no proof that every checker has already been refactored into shared utilities;
- no guarantee that `contested` and `weakened` will remain verdict levels permanently;
- no team/public runtime execution semantics;
- no production API contract.

The current result is a working authority layer, not a constitutional freeze.

---

## Remaining debt

The next useful debt classes are:

1. **Enum coverage expansion**
   - make drift checking cover more enum families, not only `verdict_level`.

2. **Checker import convergence**
   - gradually move remaining checkers away from private hardcoded protocol constants.

3. **CEDV example registry**
   - expose canonical examples through a small index so examples are discoverable and checkable as a set.

4. **Live-pilot migration audit**
   - identify remaining legacy relation vocabulary in pilot records and public surfaces.

5. **Verdict ladder cleanup**
   - later decide whether `contested` and `weakened` belong permanently in `verdict_level`, or should migrate back into claim-like `epistemic_status` with explicit transition rules.

---

## Next recommended move

The next move should not be another cockpit expansion.

The natural continuation is:

> `CEDV-B / EXAMPLEREG1`

Purpose:

> create a small CEDV example registry and make the canonical example set discoverable, checkable, and harder to accidentally desynchronize from the schema and relation-basis validation floor.

This is the right next step because CEDV now has:

- schema floor;
- graph-validation floor;
- constant-authority layer.

What it lacks next is a clear example-set registry.

---

## Closing verdict

CEDV has now crossed from:

> fields and sample objects

into:

> fields, sample objects, graph validation, and shared vocabulary authority.

That is a real protocol step.
It should be treated as the close of the first CEDV constant-authority pass, not as another draft note.
