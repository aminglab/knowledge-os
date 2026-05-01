# CEDV-D / Checker Import Convergence v1

## Status

Protocol-facing checker import convergence pass.

## Function

This file records the first CEDV checker-import convergence pass.

The goal is narrow:

> reduce private CEDV vocabulary inside protocol-facing checkers by moving appropriate object-family, relation, enum, and id-prefix knowledge into `scripts/lib/protocol_constants.py`.

This is not a full checker architecture rewrite.
It is the first cleanup pass after enum coverage made drift more visible.

---

## Entry context

Before this pass, CEDV already had:

- schema floor;
- relation and basis validation floor;
- shared constant-authority layer;
- canonical example registry;
- expanded enum drift coverage.

But some protocol-facing checkers still had local vocabulary fragments.
The highest-value remaining fragments were:

1. CEDV object-family lists inside `scripts/check_cedv_canonical_schema.py`;
2. CEDV id-prefix to object-family inference inside `scripts/check_cedv_relation_basis_validation.py`.

Those fragments were small, but strategically wrong: they allowed protocol-facing checkers to keep deciding CEDV family vocabulary locally.

---

## Shared constants added

This pass extends:

- `scripts/lib/protocol_constants.py`

with:

- `CEDV_ID_PREFIX_TO_OBJECT_TYPE`.

This derives id-prefix mapping from the existing `ID_PREFIXES` object:

- `C-` → `claim`;
- `E-` → `evidence`;
- `D-` → `dissent`;
- `V-` → `verdict`.

The point is not to introduce a new protocol concept.
The point is to stop repeating prefix/family law inside each checker.

---

## Checker changes

### `scripts/check_cedv_canonical_schema.py`

Now imports:

- `CEDV_OBJECT_TYPES`.

It uses the shared object-family set when checking the schema floor and example files.

### `scripts/check_cedv_relation_basis_validation.py`

Now imports:

- `CANONICAL_RELATION_TYPES`;
- `CEDV_ID_PREFIX_TO_OBJECT_TYPE`;
- `CEDV_OBJECT_TYPES`.

It uses shared constants for:

- relation vocabulary;
- object-family admissibility;
- id-prefix family inference.

---

## Acceptance result

CEDV-D / CHECKERIMPORT1 is accepted at the following level:

> `PASS_FIRST_PROTOCOL_CHECKER_IMPORT_CONVERGENCE`

Meaning:

- the most obvious CEDV family/prefix vocabulary duplication in protocol-facing CEDV checkers has been removed;
- relation validation continues to import canonical relation names from the shared constants module;
- canonical schema validation now imports shared CEDV object-family names;
- relation/basis validation now imports shared CEDV object-family and prefix mapping;
- this is a convergence pass, not a total rewrite.

---

## Retained holds

This pass does **not** claim:

- every checker in the repository imports shared constants;
- every case-specific checker should import shared constants;
- page-rendering checkers must become protocol checkers;
- protocol constants are final;
- the shared constants module is a complete type system;
- there is no remaining hardcoded vocabulary anywhere.

Case-specific public-layer checkers may continue to carry case-local phrases and surface obligations.
The target of this pass is protocol-facing CEDV checker drift, not every string literal in the repository.

---

## Boundary rule

Use shared constants when a checker is enforcing protocol vocabulary.

Do not force shared constants when a checker is enforcing:

- case-local source roles;
- page-section labels;
- narrative anchors;
- README exposure obligations;
- UI/preview wording;
- public-layer local acceptance phrases.

Otherwise the project will turn a useful constants layer into a bureaucratic octopus. Nobody needs an octopus in the protocol basement.

---

## Remaining debt

Likely future debt classes:

1. `scripts/check_protocol_record_consistency.py` already imports several shared constants, but may later benefit from more helper functions rather than only shared sets.
2. `scripts/check_cedv_example_registry.py` already imports relation and object-type constants, but could later share YAML parsing helpers.
3. Repeated `parse_simple_yaml` implementations remain utility duplication, not protocol vocabulary drift.
4. Some case-specific checkers may contain protocol-like words, but should be evaluated one by one rather than mass-refactored.

---

## Next recommended move

The natural continuation is:

> `CEDV-E / PARSEUTIL1`

Purpose:

> extract the repeated tiny YAML/frontmatter parsing helpers used by CEDV protocol checkers into a shared utility module, without changing protocol semantics.

This should be done only if the duplication remains concentrated in protocol-facing checkers.
Do not build a general parser empire unless the code actually demands it.
