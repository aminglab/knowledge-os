# CEDV Protocol Index

## Function

This directory is the protocol home for the four canonical Knowledge OS object families:

- Claim
- Evidence
- Dissent
- Verdict

These four families are the core knowledge-object grammar of the project.
Cockpit surfaces, public candidates, pages, and release layers are operational layers around this core.

---

## Current reading order

1. `canonical-object-schema-v1.md`
   - Defines the first schema floor for Claim / Evidence / Dissent / Verdict.

2. `relation-basis-validation-v1.md`
   - Defines the first CEDV-specific implementation subset for graph validity under the broader record-consistency floor.

3. `constant-authority-closeout-v1.md`
   - Records the post-PR #56 constant-authority closeout and the current ownership chain for enums, relation names, and checker-facing mirrors.

4. `example-registry-v1.md`
   - Defines the first registry rule for the canonical CEDV example set.

5. `enum-coverage-v1.md`
   - Records the first expanded enum drift-coverage layer across the current working enum families.

6. `examples/index-v1.json`
   - Registers the current canonical example objects and their minimal graph expectations.

7. `examples/`
   - Holds the current canonical example objects used to exercise the CEDV schema and relation-basis validation surface.

---

## External authority files

CEDV does not privately own every vocabulary it uses.

The current authority chain is:

- `protocol/enums.md` owns working enum vocabularies.
- `protocol/link-types.md` owns canonical relation names.
- `protocol/object-envelope.md` owns the shared object envelope.
- `record-consistency-check-floor-v1.md` owns the broader repository consistency floor.
- `scripts/lib/protocol_constants.py` mirrors the current working set for checkers.

This means CEDV files should reference these authorities rather than silently copying private vocabularies.

---

## Current status

CEDV currently has:

- schema floor;
- canonical examples;
- relation and basis validation;
- shared constant-authority layer;
- expanded enum drift coverage;
- canonical example registry;
- example-registry checker and workflow.

Current verdict:

> `PASS_CEDV_PROTOCOL_CORE_WITH_AUTHORITY_EXAMPLE_REGISTRY_AND_ENUM_COVERAGE`

---

## Current checker surfaces

Current CEDV-facing checkers include:

- `scripts/check_cedv_canonical_schema.py`;
- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_cedv_example_registry.py`;
- `scripts/check_protocol_constants.py`.

The example-registry checker does not replace schema or graph validation.
It only checks that the canonical example set is registered, discoverable, and aligned with its minimal expected graph.

The protocol constants checker now covers the current working enum families as well as canonical relation names.

---

## Boundaries

This directory does not yet provide:

- final protocol freeze;
- full JSON Schema or OpenAPI contract;
- complete repository-wide object migration;
- production runtime semantics;
- public release semantics by itself;
- repository-wide object registry;
- proof that every checker has converged on shared constants.

Public candidates and cockpit surfaces may consume CEDV objects, but they do not replace CEDV.

---

## Next likely work

The next useful work is:

> `CEDV-D / CHECKERIMPORT1`

Expected purpose:

> audit remaining protocol-facing checkers for hardcoded CEDV vocabulary and progressively move them to shared constants where warranted.
