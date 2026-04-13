# Public-Layer Verification Atlas v1

This file records the current **public-layer verification atlas v1** for the `power-posing` pilot.

Its purpose is narrower than a full repository-wide check atlas.
It does not try to describe every validation path in the repo.
It does something more immediately useful:

> it makes the current public-layer rule stack legible,
> shows which checker protects which public surface,
> clarifies what kind of drift each checker is meant to catch,
> and names the public-layer gaps that are still intentionally uncovered.

This atlas now sits **alongside** `check-atlas-v1.md`.

- `check-atlas-v1.md` remains the broader case-scoped validation map.
- `public-layer-verification-atlas-v1.md` is the narrower atlas for the current claim/source/snapshot/page public-layer ecology.
- [`atlas-authority-boundary-ruling-v1.md`](./atlas-authority-boundary-ruling-v1.md) is the formal ruling that explains why both atlases currently coexist and why they should not be merged yet.

The two atlases should be treated as adjacent rather than contradictory, and this ruling is now the authoritative boundary note for that split.

---

## One-sentence ruling

Current ruling:

> **The public layer is no longer one page and one generator.**
> **It is now a small ecology of coordinated public surfaces, and it now has an explicit public-layer orchestration boundary.**

---

## Entry surface

The current explicit public-layer entrypoints are:

### Make targets
- `make check-public-layer`
- `make power-posing-public-layer`

### GitHub Actions workflow
- `check-power-posing-public-layer.yml`

### Orchestrator script
- `scripts/check_power_posing_public_layer.py`

This means the earlier gap note about the absence of a unified public-layer orchestrator is no longer true for the current `power-posing` case.

---

## Current public-layer stack

The current `power-posing` public layer can now be read as eight adjacent surfaces.

1. **protocol consistency floor**
2. **object-envelope floor**
3. **judgment wording bridge**
4. **claim page public layer**
5. **source page public layer**
6. **snapshot release-view layer**
7. **page emission layer**
8. **public-layer orchestration boundary**

The orchestration boundary is now explicit rather than only implied by scattered scripts.

---

## Orchestrator-facing layer order

To keep the single-check output, the orchestrator summary, and this atlas from drifting apart, the current orchestrator-facing layer order should stay pinned to the stack above.

The current layer-to-check grouping is:

1. **protocol consistency floor**
   - `check_protocol_record_consistency.py`
2. **object-envelope floor**
   - `check_power_posing_object_envelope.py`
3. **judgment wording bridge**
   - `check_power_posing_verdict_grammar.py`
   - `check_power_posing_status_legend.py`
4. **claim page public layer**
   - `check_power_posing_claim_page_layering.py`
   - `check_power_posing_claim_page_pressure_coverage.py`
5. **source page public layer**
   - `check_power_posing_source_page_layering.py`
   - `check_power_posing_source_page_role_anchors.py`
   - `check_power_posing_reference_metadata.py`
6. **snapshot release-view layer**
   - `check_power_posing_snapshot_section_layering.py`
   - `check_power_posing_snapshot_subsection_semantics.py`
   - `check_power_posing_snapshot_consistency.py`
7. **page emission layer**
   - `check_power_posing_public_surface.py`
   - `page/generate_page_data.py --check`
8. **public-layer orchestration boundary**
   - `check_power_posing_public_layer_atlas.py`
   - `check_power_posing_public_layer.py` as the suite entry surface

This grouping is not a new checker taxonomy.
It is a small naming and ordering discipline that keeps the public-layer stack readable when the suite emits a compact verdict table.

---

## Current checker atlas

The public-layer subset currently includes at least the following named checks:

1. `check_protocol_record_consistency.py`
2. `check_power_posing_object_envelope.py`
3. `check_power_posing_verdict_grammar.py`
4. `check_power_posing_status_legend.py`
5. `check_power_posing_claim_page_layering.py`
6. `check_power_posing_claim_page_pressure_coverage.py`
7. `check_power_posing_source_page_layering.py`
8. `check_power_posing_source_page_role_anchors.py`
9. `check_power_posing_snapshot_section_layering.py`
10. `check_power_posing_snapshot_subsection_semantics.py`
11. `check_power_posing_snapshot_consistency.py`
12. `check_power_posing_reference_metadata.py`
13. `check_power_posing_public_surface.py`
14. `check_power_posing_public_layer_atlas.py`
15. `page/generate_page_data.py --check`
16. `check_power_posing_public_layer.py` as the suite entrypoint

`check_power_posing_public_layer_atlas.py` now reports atlas governance in two views:

- **boundary view** — whether the current dual-atlas structure, README exposure, and authority ruling remain intact
- **threshold view** — whether the future merge-threshold object remains properly exposed and expressed

The important current fact is not just that these checks exist.
It is that the public layer now has a **named operational boundary** for running the subset as a suite.

---

## Boundary note: this atlas vs `check-atlas-v1.md`

These two atlas files are now adjacent but not identical.

- **`check-atlas-v1.md`** is the broader case-scoped validation map.
- **`public-layer-verification-atlas-v1.md`** is the narrower public-layer-specific atlas.
- **`atlas-authority-boundary-ruling-v1.md`** is the formal authority note that explains which one is broader, which one is narrower, when to read which one first, and why they should not be merged yet.

The first helps keep the whole case validation topology legible.
The second helps keep the public-layer rule stack legible.
The third keeps the split itself governed rather than implicit.

---

## Current public-layer gaps

This atlas should also say what is **not** yet covered.

### 1. No single merged atlas yet
The current stage still uses a governed dual-atlas structure rather than a single consolidated atlas.
That is now intentional rather than accidental.

### 2. No repository-wide public-layer orchestrator yet
The current orchestrator is still explicitly case-scoped to `power-posing`.
That is correct for the current stage.
It also means the repository does not yet have a generic multi-case public-layer suite.

---

## Practical verdict

So the practical verdict is:

- **the `power-posing` public layer now has a real multi-surface verification network**
- **claim pages, source pages, snapshot structure, judgment wording, source metadata, navigation surface, page emission, public-layer orchestration, and public-layer atlas governance are no longer being treated as one undifferentiated surface**
- **the main remaining work is no longer “add checks blindly,” but decide which currently named gaps deserve the next hardening step**
