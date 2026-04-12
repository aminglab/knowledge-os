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

The two files should be treated as adjacent rather than contradictory.

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

This means the old sentence:

> `No unified public-layer orchestrator yet`

is no longer true for the current `power-posing` case.

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
14. `page/generate_page_data.py --check`
15. `check_power_posing_public_layer.py` as the suite entrypoint

The important current fact is not just that these checks exist.
It is that the public layer now has a **named operational boundary** for running the subset as a suite.

---

## Boundary note: this atlas vs `check-atlas-v1.md`

These two atlas files are now adjacent but not identical.

- **`check-atlas-v1.md`** is the broader case-scoped validation map.
- **`public-layer-verification-atlas-v1.md`** is the narrower public-layer-specific atlas.

The first helps keep the whole case validation topology legible.
The second helps keep the public-layer rule stack legible.

The split is manageable as long as they remain clearly distinguished and do not contradict each other.

---

## Current public-layer gaps

This atlas should also say what is **not** yet covered.

### 1. No public-layer atlas checker yet
This atlas itself is still documentary rather than checked.

### 2. Atlas authority is still split across two adjacent documents
The atlas language still lives across:

- `check-atlas-v1.md`
- `public-layer-verification-atlas-v1.md`

That split is now visible rather than hidden, but it is still a governance edge.

### 3. No repository-wide public-layer orchestrator yet
The current orchestrator is still explicitly case-scoped to `power-posing`.
That is correct for the current stage.
It also means the repository does not yet have a generic multi-case public-layer suite.

---

## Practical verdict

So the practical verdict is:

- **the `power-posing` public layer now has a real multi-surface verification network**
- **claim pages, source pages, snapshot structure, judgment wording, source metadata, navigation surface, page emission, and public-layer orchestration are no longer being treated as one undifferentiated surface**
- **the main remaining work is no longer “add checks blindly,” but decide which currently named gaps deserve the next hardening step**
