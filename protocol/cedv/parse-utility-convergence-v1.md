# CEDV-E / Parse Utility Convergence v1

## Status

Protocol checker utility convergence pass.

## Function

This file records the first CEDV parse-utility convergence pass.

The goal is narrow:

> extract the repeated tiny YAML parser used by protocol-facing CEDV checkers into a shared utility module, without changing protocol semantics.

This is not a general YAML framework.
It is a utility cleanup for the current protocol example subset.

---

## Entry context

Before this pass, repeated `parse_simple_yaml()` implementations existed in:

- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_cedv_example_registry.py`.

Those implementations were functionally similar and existed only because early protocol checkers were grown one at a time.

After CEDV-D, the remaining duplication was no longer primarily vocabulary drift.
It was small parser utility duplication.

---

## Utility added

This pass adds:

- `scripts/lib/simple_yaml.py`.

The utility exports:

- `parse_simple_yaml(text: str) -> dict[str, Any]`.

Supported subset:

- top-level scalar keys;
- top-level list keys;
- list values that are scalars;
- list values that are simple one-level maps, currently used for `links`.

This intentionally covers only the small frontmatter-like subset used by current CEDV protocol examples.

---

## Checker changes

### `scripts/check_cedv_relation_basis_validation.py`

Now imports:

- `parse_simple_yaml` from `scripts.lib.simple_yaml`.

### `scripts/check_cedv_example_registry.py`

Now imports:

- `parse_simple_yaml` from `scripts.lib.simple_yaml`.

The local parser copies were removed from both files.

---

## Acceptance result

CEDV-E / PARSEUTIL1 is accepted at the following level:

> `PASS_FIRST_PROTOCOL_PARSE_UTILITY_CONVERGENCE`

Meaning:

- repeated tiny YAML parser logic has been removed from the two current CEDV protocol-facing checkers that used it;
- parsing remains deliberately scoped to the present protocol example subset;
- protocol semantics are unchanged;
- no general YAML parsing framework has been introduced.

---

## Retained holds

This pass does **not** claim:

- full YAML compliance;
- frontmatter parsing for all repository documents;
- markdown body parsing;
- typed schema validation;
- replacement of proper YAML tooling if the data model grows;
- parser ownership over case-specific page or public-layer files.

The shared utility is allowed because the duplicated parser was already present in multiple protocol-facing CEDV checkers.
It should not be expanded casually into a half-parser empire.

---

## Boundary rule

Use `scripts/lib/simple_yaml.py` only for the current simple protocol object subset.

If CEDV examples start needing nested maps beyond one level, multiline scalars, anchors, comments with semantic meaning, or richer YAML behavior, the correct move is to deliberately adopt proper YAML parsing rather than quietly accreting features here.

---

## Remaining debt

Likely future pressure points:

1. A small protocol checker utility package may eventually group `read_text`, registry loading, and object loading helpers.
2. Relation admissibility rules remain embedded in `check_cedv_relation_basis_validation.py`; they may later deserve a declarative relation matrix.
3. Example registry and relation-basis validation still load objects separately; a shared CEDV object loader may become warranted if a third checker repeats the pattern.

---

## Next recommended move

The natural continuation is:

> `CEDV-F / RELMATRIX1`

Purpose:

> move the current relation source/target admissibility rules out of imperative checker code and into a small explicit relation-admissibility matrix, if the next audit confirms that relation rules are becoming the next hidden protocol surface.

Do not start this unless the matrix would simplify actual checker logic.
