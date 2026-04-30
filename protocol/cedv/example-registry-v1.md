# CEDV-B / Example Registry v1

## Status

Protocol example-registry floor.

## Function

This file defines the first registry rule for CEDV canonical examples.

The goal is not to add more example objects.
The goal is to make the existing examples discoverable, named, and checkable as a set.

Before this step, `protocol/cedv/examples/` already contained one minimal object for each canonical CEDV family:

- Claim;
- Evidence;
- Dissent;
- Verdict.

But the directory itself had no registry object.
That meant a future edit could add, remove, rename, or desynchronize examples without a single surface saying what the canonical example set is supposed to be.

This file closes that gap.

---

## Registry object

The current registry object is:

- `protocol/cedv/examples/index-v1.json`

It is a protocol-local example registry, not a public release index.

It should answer:

1. Which example files belong to the current canonical CEDV example set?
2. Which object family does each file exercise?
3. Which ids and titles should be found in those files?
4. Which minimal graph expectations should remain true across the set?

---

## Required registry duties

The example registry must declare at least:

- `schema_name`;
- `schema_version`;
- `registry_scope`;
- `examples`;
- `graph_expectations`.

Each example entry must declare at least:

- `id`;
- `object_type`;
- `path`;
- `role`;
- `expected_title`.

The registry is invalid if:

- a registered file is missing;
- an example YAML file exists but is not registered;
- a registered id does not match the YAML `id`;
- a registered object type does not match the YAML `object_type`;
- required object families are missing;
- required graph edges are absent;
- required verdict basis refs are absent;
- relation names in required edges drift outside the canonical relation floor.

---

## Current canonical example set

Current required object-family coverage:

- one Claim example;
- one Evidence example;
- one Dissent example;
- one Verdict example.

Current examples:

- `C-0001` — Claim example;
- `E-0001` — Evidence example;
- `D-0001` — Dissent example;
- `V-0001` — Verdict example.

Current minimal graph expectations:

- `E-0001 supports C-0001`;
- `D-0001 challenges C-0001`;
- `V-0001 depends_on C-0001`;
- `V-0001 pinned_in_snapshot public-candidate:h-pylori-ulcer-summary:v1`;
- `V-0001 basis_refs: C-0001, E-0001, D-0001`.

---

## Checker

The current checker is:

- `scripts/check_cedv_example_registry.py`

The current workflow is:

- `.github/workflows/check-cedv-example-registry.yml`

This checker is intentionally small.
It does not replace:

- `scripts/check_cedv_canonical_schema.py`;
- `scripts/check_cedv_relation_basis_validation.py`;
- `scripts/check_protocol_constants.py`.

It only checks that the canonical example set is registered, discoverable, and aligned with the minimal expected graph.

---

## Acceptance result

CEDV-B / EXAMPLEREG1 is accepted at the following level:

> `PASS_CANONICAL_EXAMPLE_REGISTRY_FLOOR`

Meaning:

- the CEDV example set now has a registry;
- all current example YAML files are expected to be registered;
- object-family coverage is explicit;
- minimal graph expectations are explicit;
- a checker can fail when examples drift from the registry.

---

## Retained holds

This registry does **not** claim:

- full fixture-generation support;
- full JSON Schema validation;
- repository-wide object indexing;
- public release indexing;
- cross-case registry authority;
- automatic example synthesis;
- final protocol freeze.

It is a local canonical example registry for the current CEDV protocol floor.

---

## Next recommended move

After this step, the natural continuation is not to add many examples.

The next useful move is:

> `CEDV-C / ENUMCOVER1`

Purpose:

> extend protocol drift checking beyond `verdict_level` so lifecycle, visibility, epistemic status, dissent kind, severity, relation types, and checker mirrors are covered more uniformly.

The example registry gives CEDV a stable sample set.
The next protocol pressure should be stronger enum coverage, not example sprawl.
