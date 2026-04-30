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

5. `examples/index-v1.json`
   - Registers the current canonical example objects and their minimal graph expectations.

6. `examples/`
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
- drift checking for the first protocol constant set;
- canonical example registry;
- example-registry checker and workflow.

Current verdict:

> `PASS_CEDV_PROTOCOL_CORE_WITH_WORKING_AUTHORITY_AND_EXAMPLE_REGISTRY`

---

## Current checker surfaces

Current CEDV-facing checkers include:

- `scripts/check_cedv_canonical_schema.py`;
- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_cedv_example_registry.py`;
- `scripts/check_protocol_constants.py`.

The example-registry checker does not replace schema or graph validation.
It only checks that the canonical example set is registered, discoverable, and aligned with its minimal expected graph.

---

## Boundaries

This directory does not yet provide:

- final protocol freeze;
- full JSON Schema or OpenAPI contract;
- complete repository-wide object migration;
- production runtime semantics;
- public release semantics by itself;
- repository-wide object registry.

Public candidates and cockpit surfaces may consume CEDV objects, but they do not replace CEDV.

---

## Next likely work

The next useful work is:

> `CEDV-C / ENUMCOVER1`

Expected purpose:

> extend protocol drift checking beyond `verdict_level` so lifecycle, visibility, epistemic status, dissent kind, severity, relation types, and checker mirrors are covered more uniformly.
