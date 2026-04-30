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

4. `examples/`
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
- drift checking for the first protocol constant set.

Current verdict:

> `PASS_CEDV_PROTOCOL_CORE_STARTED_WITH_WORKING_AUTHORITY_LAYER`

---

## Boundaries

This directory does not yet provide:

- final protocol freeze;
- full JSON Schema or OpenAPI contract;
- complete repository-wide object migration;
- production runtime semantics;
- public release semantics by itself.

Public candidates and cockpit surfaces may consume CEDV objects, but they do not replace CEDV.

---

## Next likely work

The next useful work is:

> `CEDV-B / EXAMPLEREG1`

Expected purpose:

> create a small canonical example registry so the current example set is discoverable, checkable as a set, and easier to keep aligned with the schema and validation floor.
