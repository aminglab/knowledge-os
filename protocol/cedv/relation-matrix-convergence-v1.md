# CEDV-F / Relation Matrix Convergence v1

## Status

Protocol relation-admissibility matrix pass.

## Function

This file records the first CEDV relation-matrix convergence pass.

The goal is narrow:

> move the current CEDV source/target relation admissibility rules out of imperative checker code and into a small explicit relation-admissibility matrix.

This does not change relation semantics.
It makes the existing semantics visible and checkable.

---

## Entry context

Before this pass, CEDV already had:

- schema floor;
- relation and basis validation floor;
- shared constant-authority layer;
- canonical example registry;
- expanded enum drift coverage;
- protocol-facing checker import convergence;
- shared simple YAML parser.

But one hidden protocol surface remained in `scripts/check_cedv_relation_basis_validation.py`:

- `relation_allowed()` encoded source/target admissibility in imperative Python conditionals.

That was acceptable for the first graph validator.
It became less acceptable once CEDV was moving toward explicit protocol surfaces.

---

## Matrix added

This pass adds:

- `protocol/cedv/relation-admissibility-matrix-v1.json`.

The matrix declares:

- `schema_name`;
- `schema_version`;
- `relation_rules`;
- `external_target_rules`.

It covers the current CEDV relation-admissibility subset for:

- Claim;
- Evidence;
- Dissent;
- Verdict.

---

## Utility added

This pass adds:

- `scripts/lib/relation_matrix.py`.

It provides:

- `load_relation_matrix(path)`;
- `validate_relation_matrix(matrix)`;
- `relation_allowed_by_matrix(matrix, source_type, relation, target, target_type)`.

The utility validates that matrix rules use:

- shared canonical relation names;
- shared CEDV object types;
- explicit external target prefixes where needed.

---

## Checker change

`script/check_cedv_relation_basis_validation.py` is now matrix-driven.

It no longer keeps an imperative `relation_allowed()` function as the primary source of admissibility law.

Instead, it:

1. loads `relation-admissibility-matrix-v1.json`;
2. validates the matrix shape and vocabulary;
3. uses `relation_allowed_by_matrix()` for each object link.

---

## Current matrix semantics

Current internal CEDV object-target rules include:

- Claim `depends_on` Claim;
- Claim `descends_from` Claim;
- Claim `supersedes` Claim or Verdict;
- Evidence `supports` Claim or Verdict;
- Evidence `challenges` Claim or Verdict;
- Dissent `challenges` any CEDV object family;
- Verdict `depends_on` any CEDV object family;
- Verdict `supersedes` Verdict.

Current external target rules include:

- any CEDV object may `cites` an external target;
- Verdict may `pinned_in_snapshot` targets beginning with `public-candidate:` or `snapshot:`.

---

## Acceptance result

CEDV-F / RELMATRIX1 is accepted at the following level:

> `PASS_FIRST_RELATION_ADMISSIBILITY_MATRIX`

Meaning:

- relation source/target admissibility is no longer hidden only in checker conditionals;
- the matrix is explicit and versioned;
- the relation-basis checker validates and consumes the matrix;
- matrix vocabulary is checked against shared constants;
- current relation semantics are preserved.

---

## Retained holds

This pass does **not** claim:

- full graph ontology;
- final relation grammar freeze;
- all repository relations are governed by this matrix;
- public-layer link rendering is governed by this matrix;
- case-specific narrative links must be rewritten;
- relation semantics are complete for every future domain.

The current matrix is the first CEDV protocol example relation-admissibility floor.

---

## Boundary rule

Use the matrix for protocol-facing CEDV object relation admissibility.

Do not use it as a universal replacement for:

- UI route links;
- page reading paths;
- source cards;
- README exposure links;
- case-local public-layer navigation.

Those are presentation or public-layer routes, not necessarily CEDV graph relations.

---

## Remaining debt

Likely future pressure points:

1. The matrix may later need to express whether targets must resolve internally, may be external, or must have special prefixes.
2. The matrix may later need named rationales for each admissible relation.
3. Example registry and relation-basis validation may eventually share a CEDV object loader.
4. A later schema layer may need JSON Schema or typed validation for the matrix itself.

---

## Next recommended move

The natural continuation is:

> `CEDV-G / OBJECTLOAD1`

Purpose:

> introduce a small shared CEDV object loader used by example-registry and relation-basis validation checkers, if repeated object-loading logic remains concentrated after the parser and matrix passes.

Do not proceed if the loader would only save a few lines while hiding checker intent.
