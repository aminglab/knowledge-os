# Public-Layer Verification Atlas v1

This file records the current **public-layer verification atlas v1** for the `h-pylori-ulcer` case.

Its purpose is narrower than a full case atlas and much narrower than a repository-wide public-layer doctrine.
It does something more immediately useful:

> it makes the current second-case public-layer stack legible,
> shows which checker protects which public surface,
> clarifies what kind of drift each checker is meant to catch,
> and names the public-layer gaps that are still intentionally uncovered.

---

## One-sentence ruling

Current ruling:

> **The second case now has a real but still minimal governed public layer.**
> **Its current verification stack is claim-page structure, claim-page direct pressure coverage, source-page structure, source-page role anchors, snapshot release-view structure, snapshot subsection semantics, fuller snapshot consistency, and one small suite entrypoint that can run them together.**

---

## Entry surface

The current explicit public-layer entrypoints are:

### Script suite entrypoint
- `scripts/check_h_pylori_public_layer.py`

### GitHub Actions workflow
- `check-h-pylori-public-layer.yml`

This means the earlier state of “a few separate checks but no public-layer suite entrypoint” is no longer true for the current second case.

---

## Current public-layer stack

The current `h-pylori-ulcer` public layer should now be read as four adjacent surfaces.

1. **claim page public layer**
2. **source page public layer**
3. **snapshot release-view layer**
4. **public-layer verification entry surface**

This is intentionally smaller than the current `power-posing` stack.
That difference is a feature, not a defect.
The second case has not yet earned a larger public-layer ecology.

---

## Layer-to-check grouping

The current layer-to-check grouping is:

1. **claim page public layer**
   - `check_h_pylori_claim_page_layering.py`
   - `check_h_pylori_claim_page_pressure_coverage.py`
2. **source page public layer**
   - `check_h_pylori_source_page_layering.py`
   - `check_h_pylori_source_page_role_anchors.py`
3. **snapshot release-view layer**
   - `check_h_pylori_snapshot_section_layering.py`
   - `check_h_pylori_snapshot_subsection_semantics.py`
   - `check_h_pylori_snapshot_consistency.py`
4. **public-layer verification entry surface**
   - `check_h_pylori_public_layer.py`

This grouping is not a grand checker taxonomy.
It is a small naming and ordering discipline that keeps the second-case public layer readable and auditable.

---

## Current checker atlas

The current public-layer subset includes the following named checks:

1. `check_h_pylori_claim_page_layering.py`
2. `check_h_pylori_claim_page_pressure_coverage.py`
3. `check_h_pylori_source_page_layering.py`
4. `check_h_pylori_source_page_role_anchors.py`
5. `check_h_pylori_snapshot_section_layering.py`
6. `check_h_pylori_snapshot_subsection_semantics.py`
7. `check_h_pylori_snapshot_consistency.py`
8. `check_h_pylori_public_layer.py` as the suite entrypoint

The important current fact is not just that these checks exist.
It is that the second case now has a **named operational entry surface** for running them together.

---

## What this atlas does **not** yet include

This atlas should also say what is **not** yet covered.

### 1. No page emission layer yet
The current second case does not yet have a page-emission layer comparable to the first case.
That means there is nothing here like `generate_page_data.py --check`.

### 2. No public-layer atlas governance checker yet
The current second-case stack is still small enough that atlas self-governance does not yet need its own checker.

### 3. No hidden-checks orchestration boundary yet
The current second case does not yet need the stronger orchestration boundary used by the first case.

---

## Practical verdict

So the practical verdict is:

- **the `h-pylori-ulcer` public layer now has a real but compact verification network**
- **claim-page structure, claim-page direct pressure coverage, source-page structure, source-page role anchors, snapshot structure, snapshot subsection semantics, fuller snapshot consistency, and suite-level entry are no longer being treated as one undifferentiated surface**
- **the next hardening question is no longer whether the snapshot layer has a fuller consistency checker, but whether a larger public-layer orchestration boundary or atlas-governance checker is now justified**
