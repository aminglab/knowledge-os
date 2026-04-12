# Public-Layer Verification Atlas v1

This file records the current **public-layer verification atlas v1** for the `power-posing` pilot.

Its purpose is narrower than a full repository-wide check atlas.
It does not try to describe every validation path in the repo.
It does something more immediately useful:

> it makes the current public-layer rule stack legible,
> shows which checker protects which public surface,
> clarifies what kind of drift each checker is meant to catch,
> and names the public-layer gaps that are still intentionally uncovered.

---

## One-sentence ruling

Current ruling:

> **The public layer is no longer one page and one generator.**
> **It is now a small ecology of coordinated public surfaces, and each major surface needs its own explicit verification boundary.**

That is the whole point of this atlas.

---

## Why this atlas exists now

The current pilot now has multiple public-facing layers with different jobs:

- the main snapshot release view,
- claim pages,
- source pages,
- status legend,
- verdict grammar,
- and the page-emission surface.

At the same time, the protocol layer has tightened:

- relation naming is now canonicalized,
- verdict levels have been compressed toward a compact floor,
- verdict targets are now explicit,
- and protocol record consistency is now checked at a system-facing layer.

That is good progress.
But it also means one new risk appears:

> people can see many green checks without understanding what those checks are actually protecting.

This atlas exists to stop that confusion.

---

## Current public-layer stack

The current `power-posing` public layer can now be read as seven adjacent surfaces.

### 1. protocol consistency floor
This is not itself a reader-facing surface, but it now constrains what public surfaces can safely sit on top of.

Core artifacts:

- `record-consistency-check-floor-v1.md`
- `scripts/check_protocol_record_consistency.py`

### 2. object-envelope floor for this pilot
This protects the pilot’s governed object shape.

Core artifacts:

- `protocol/object-envelope.md`
- `scripts/check_power_posing_object_envelope.py`

### 3. judgment wording bridge
This holds together status wording, verdict levels, and the claim / verdict object layer.

Core artifacts:

- `verdict-grammar-v1.md`
- `status-legend-v1.md`
- `scripts/check_power_posing_verdict_grammar.py`
- `scripts/check_power_posing_status_legend.py`

### 4. claim page public layer
This is the first human-readable neighborhood-summary layer for claims.

Core artifacts:

- `claims/*.md`
- `claim-page-layering-v1.md`
- `scripts/check_power_posing_claim_page_layering.py`
- `scripts/check_power_posing_claim_page_pressure_coverage.py`

### 5. source page public layer
This is the first human-readable case-participation layer for sources.

Core artifacts:

- `sources/*.md`
- `source-page-layering-v1.md`
- `source-page-role-anchors-v1.md`
- `scripts/check_power_posing_source_page_layering.py`
- `scripts/check_power_posing_source_page_role_anchors.py`

### 6. snapshot release-view layer
This is the whole-case public homepage surface.

Core artifacts:

- `snapshots/snapshot-v2.md`
- `snapshot-section-layering-v1.md`
- `scripts/check_power_posing_snapshot_section_layering.py`
- `scripts/check_power_posing_snapshot_consistency.py`

### 7. page emission layer
This is the public page prototype contract and downstream renderer surface.

Core artifacts:

- `page/generate_page_data.py`
- `renderer-primitives.js`
- `render.js`
- `preview_page.py`
- page-related CI checks

---

## Current checker atlas

Below is the current public-layer verification network, ordered from lower substrate checks to higher public presentation checks.

### 1. Protocol record consistency
- **Primary script:** `scripts/check_protocol_record_consistency.py`
- **Protected layer:** protocol-facing record floor under the public layer
- **Reads:** all `power-posing` objects
- **Main job:** ensure that the public layer is no longer sitting on legacy relation aliases, floating verdict targets, or non-canonical verdict levels
- **Typical drift caught:**
  - legacy relation aliases reappearing,
  - missing `target_claim_id`,
  - verdict levels outside the compact verdict floor,
  - dangling object targets
- **Failure meaning:** the governed record floor has drifted enough that public-layer semantics can no longer be trusted to be canonical

### 2. Object envelope conformance
- **Primary script:** `scripts/check_power_posing_object_envelope.py`
- **Protected layer:** current pilot object-envelope floor
- **Reads:** all object files, `protocol/object-envelope.md`, `protocol/enums.md`, `protocol/link-types.md`, `references-metadata-v1.md`
- **Main job:** ensure that public surfaces are still backed by object files that satisfy the current working envelope
- **Typical drift caught:**
  - unsupported frontmatter fields,
  - enum drift,
  - invalid source refs,
  - invalid basis refs,
  - invalid link structure
- **Failure meaning:** the pilot’s object layer has drifted away from the current protocol floor

### 3. Verdict grammar consistency
- **Primary script:** `scripts/check_power_posing_verdict_grammar.py`
- **Protected layer:** bridge from public status wording to object-layer judgment semantics
- **Reads:** `verdict-grammar-v1.md`, `snapshot-v2.md`, claim objects, verdict objects
- **Main job:** keep public judgment wording aligned with claim status, verdict level, and required verdict-body anchors
- **Typical drift caught:**
  - snapshot wording changing while verdict grammar does not,
  - claim status drift,
  - verdict-level drift,
  - verdict-body anchor drift
- **Failure meaning:** public judgment language and object-layer judgment state have drifted apart

### 4. Status legend consistency
- **Primary script:** `scripts/check_power_posing_status_legend.py`
- **Protected layer:** reader-facing explanation of current public status wording
- **Reads:** `status-legend-v1.md`, `verdict-grammar-v1.md`, `snapshot-v2.md`
- **Main job:** keep the explanatory legend synchronized with the governing grammar layer and current snapshot wording
- **Typical drift caught:**
  - old verdict levels lingering in the legend,
  - label mismatch,
  - public wording mismatch,
  - id mismatch
- **Failure meaning:** the public explanation layer no longer matches the governing status bridge

### 5. Claim page layering
- **Primary script:** `scripts/check_power_posing_claim_page_layering.py`
- **Protected layer:** claim-page public readability layer
- **Reads:** `claims/*.md`, `objects/claims/*.md`, `objects/verdicts/*.md`
- **Main job:** ensure that stricter canonical frontmatter is compensated by visible public claim structure
- **Typical drift caught:**
  - missing `Current visible judgment`,
  - missing `Support surface`,
  - missing `Challenge surface`,
  - missing `Lineage placement`,
  - linked verdict targeting the wrong claim,
  - claim-page title drift from the governed object title
- **Failure meaning:** claim pages are no longer doing their job as the human-readable neighborhood summary layer

### 6. Claim page pressure coverage
- **Primary script:** `scripts/check_power_posing_claim_page_pressure_coverage.py`
- **Protected layer:** claim-page support/challenge fidelity to direct object-side pressure-bearing relations
- **Reads:** `claims/*.md`, all object files
- **Main job:** ensure that every direct inbound `supports` or `challenges` relation targeting a claim is actually surfaced in the appropriate public claim-page section
- **Typical drift caught:**
  - a direct supporting object disappearing from `Support surface`,
  - a direct challenging object disappearing from `Challenge surface`
- **Failure meaning:** the claim page still has the right section headings, but it is no longer faithfully summarizing the direct pressure-bearing neighborhood of the governed claim

### 7. Source page layering
- **Primary script:** `scripts/check_power_posing_source_page_layering.py`
- **Protected layer:** source-page public readability layer
- **Reads:** `sources/*.md`, `references-metadata-v1.md`
- **Main job:** ensure that source pages remain more than duplicated metadata or vague prose pages
- **Typical drift caught:**
  - missing `Source identity`,
  - missing `Source role in the case`,
  - missing `Case usage`,
  - missing `Object usage`,
  - source-page id drift,
  - source-page title drift from metadata,
  - object-usage section without actual governed object links
- **Failure meaning:** source pages are no longer acting as the public case-participation layer for sources

### 8. Source page role anchors
- **Primary script:** `scripts/check_power_posing_source_page_role_anchors.py`
- **Protected layer:** source-page role fidelity inside the public source layer
- **Reads:** `sources/*.md`, `source-page-role-anchors-v1.md`
- **Main job:** ensure that each source page keeps the minimal role phrases that make its case function legible
- **Typical drift caught:**
  - a source page keeping its headings but losing the role phrases that identify it as foundational source, empirical challenge, internal withdrawal, methodological attack, amplification surface, or retreat-and-reframing surface
- **Failure meaning:** the source page still looks structurally complete, but its actual case role has drifted into generic prose

### 9. Snapshot section layering
- **Primary script:** `scripts/check_power_posing_snapshot_section_layering.py`
- **Protected layer:** snapshot release-view structure
- **Reads:** `snapshots/snapshot-v2.md`, current object set, status legend and verdict grammar paths
- **Main job:** ensure that the snapshot remains a structured public homepage rather than drifting into an unstructured narrative page
- **Typical drift caught:**
  - missing major release-view sections,
  - missing original/descendant current-state blocks,
  - missing reading-path routes,
  - missing included-object exposure
- **Failure meaning:** the snapshot has started to lose its release-view structure

### 10. Snapshot consistency
- **Primary script:** `scripts/check_power_posing_snapshot_consistency.py`
- **Protected layer:** snapshot narrative fidelity to current governed objects and source ids
- **Reads:** `snapshot-v2.md`, `references-metadata-v1.md`, all object files
- **Main job:** keep the snapshot honest relative to the object / reference world it is describing
- **Typical drift caught:**
  - included-object coverage errors,
  - reading-path object drift,
  - object-link path errors,
  - canonical source id coverage drift
- **Failure meaning:** the snapshot still has structure, but no longer truthfully points to the current governed layer

### 11. Reference metadata consistency
- **Primary script:** `scripts/check_power_posing_reference_metadata.py`
- **Protected layer:** stable source metadata floor
- **Reads:** `references-metadata-v1.md`, all object files
- **Main job:** keep metadata claims about source usage aligned with actual object grounding
- **Typical drift caught:**
  - missing source ids,
  - missing metadata fields,
  - object usage declarations that no longer match object frontmatter
- **Failure meaning:** public source pages and snapshot source routes are sitting on stale source metadata

### 12. Public surface consistency
- **Primary script:** `scripts/check_power_posing_public_surface.py`
- **Protected layer:** reader-facing navigation entry surface
- **Reads:** `snapshot-v2.md`, `README.md`
- **Main job:** ensure that the reader can still find the minimum outward-facing path through the case
- **Typical drift caught:**
  - missing public reading path links,
  - missing required snapshot / references / timeline / case-entry routes
- **Failure meaning:** the public layer is still internally coherent, but the outside reader can no longer navigate it properly

### 13. Page emission validation
- **Primary surface:** `page/generate_page_data.py` in validation mode, plus page-related CI entrypoints
- **Protected layer:** downstream page-data contract and page prototype emission layer
- **Reads:** object files, snapshot, timeline, references metadata, page stack
- **Main job:** ensure that the current public ecology can still be emitted into the page layer
- **Typical drift caught:**
  - release-summary construction breakage,
  - required field omissions that block page emission,
  - source-ref or basis-ref issues that break page-data generation
- **Failure meaning:** the public markdown ecology may still read fine locally, but it can no longer be safely emitted into the case page prototype

---

## Boundary notes

### Protocol consistency vs object envelope
These are adjacent but not duplicate.

- **Protocol consistency** protects canonical semantic floor and relation/verdict hardening.
- **Object envelope** protects the broader working frontmatter shape for this pilot.

One asks whether the pilot is still canonical enough.
The other asks whether the pilot is still structurally well-formed enough.

### Verdict grammar vs status legend
These are adjacent but not duplicate.

- **Verdict grammar** is the governing bridge.
- **Status legend** is the reader-facing explanation layer.

If one changes without the other, the public layer becomes confusing even if the objects remain untouched.

### Claim/source/snapshot layering checks
These three are parallel, not hierarchical.

- **Claim page layering** protects object-neighborhood public readability.
- **Source page layering** protects source-participation public readability.
- **Snapshot section layering** protects whole-case release-view readability.

Each is a different compensation layer for a different public surface.

### Claim page layering vs claim page pressure coverage
These are adjacent but not duplicate.

- **Claim page layering** checks whether the claim page still has the required public sections and correct linked-verdict routing.
- **Claim page pressure coverage** checks whether those sections still faithfully expose the direct pressure-bearing support/challenge neighborhood from the governed object layer.

A page can keep all the right section headings and still quietly omit the actual objects that matter.
These two checks catch different failure modes.

### Source page layering vs source page role anchors
These are adjacent but not duplicate.

- **Source page layering** checks whether the source page still has the required public sections and metadata-aligned identity surface.
- **Source page role anchors** checks whether the source page still preserves the minimal role phrases that identify why this source matters in the case.

A page can keep all the right headings and still quietly lose the role language that makes it case-specific.
These two checks catch different failure modes.

### Snapshot section layering vs snapshot consistency
These are adjacent but not duplicate.

- **Snapshot section layering** asks whether the snapshot still has the right public release-view structure.
- **Snapshot consistency** asks whether that structured page still truthfully points to the current governed layer.

A snapshot can be structurally beautiful and still factually stale.
These two checks catch different failure modes.

### Public surface consistency vs page emission validation
These are also adjacent but not duplicate.

- **Public surface consistency** checks visible navigation exposure.
- **Page emission validation** checks downstream page-contract emission.

One protects reader navigation.
The other protects renderer-facing viability.

---

## Current public-layer gaps

This atlas should also say what is **not** yet covered.

### 1. No unified public-layer orchestrator yet
The checks now form a real network, but there is not yet a single explicit `public-layer check orchestrator` that runs only the public-layer subset as one named command.

### 2. No snapshot subsection semantic checker yet
The current snapshot layering checker validates section presence and major route surfaces.
It does not yet deeply validate subsection-by-subsection semantic content inside `What changed later` or `Original claim neighborhood`.

### 3. No public-layer atlas checker yet
This atlas itself is currently documentary, not checked.
It can still drift unless later given a small audit companion.

These are not hidden failures.
They are simply the current edge of the verification surface.

---

## Practical reading guide

If a new failure appears, the safest first interpretation is:

- **protocol consistency failed** → canonical floor drifted
- **object envelope failed** → frontmatter structure drifted
- **verdict grammar failed** → public judgment wording drifted from claim/verdict semantics
- **status legend failed** → reader explanation drifted from governing judgment bridge
- **claim page layering failed** → claim pages stopped compensating for machine-layer strictness
- **claim page pressure coverage failed** → claim pages stopped faithfully surfacing direct support/challenge pressure from the object layer
- **source page layering failed** → source pages stopped compensating for metadata-layer strictness
- **source page role anchors failed** → source pages kept their structure but lost the role language that makes them case-specific
- **snapshot section layering failed** → public homepage structure drifted
- **snapshot consistency failed** → homepage content drifted from current governed reality
- **reference metadata failed** → source metadata drifted from object grounding
- **public surface failed** → public navigation drifted
- **page emission failed** → page prototype contract drifted

This is the real practical value of the atlas:

> not just to say that there are many checks,
> but to say what kind of drift each one localizes.

---

## Practical verdict

So the practical verdict is:

- **the `power-posing` public layer now has a real multi-surface verification network**
- **claim pages, source pages, snapshot structure, judgment wording, source metadata, navigation surface, and page emission are no longer being treated as one undifferentiated surface**
- **the main remaining work is no longer “add checks blindly,” but decide which currently named gaps deserve the next hardening step**

That is the right reading of the current stage.
