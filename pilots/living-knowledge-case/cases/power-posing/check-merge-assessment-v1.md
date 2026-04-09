# Check Merge Assessment v1

This file is the current **check merge assessment v1** for the power-posing pilot.

Its scope is intentionally narrow:

- `scripts/check_power_posing_snapshot_consistency.py`
- `scripts/check_power_posing_public_surface.py`

The question is not whether these two scripts are adjacent.
They obviously are.
The question is whether they should now be partially merged, fully merged, or deliberately kept separate.

---

## Current question

Both scripts read `snapshot-v2.md`.
Both protect a public-facing layer of the case.
That makes them look mergeable at first glance.

But they do **not** currently protect the same thing.
This assessment therefore distinguishes:

- shared input surface,
- overlapping validation mechanics,
- and actual governance target.

---

## Script A: snapshot consistency

### Current purpose
`check_power_posing_snapshot_consistency.py` protects the snapshot as a governed narrative object.

### Current reads
- `snapshots/snapshot-v2.md`
- `references-metadata-v1.md`
- all object files

### Current failure semantics
A failure here means the snapshot has drifted away from the current object/reference reality.

### Canonical responsibilities
- included object coverage
- reading-path object id validity
- object link path validity
- canonical source id coverage against object frontmatter

This script answers the question:

> Is the snapshot still a truthful governed release view over the current object and reference layer?

---

## Script B: public surface consistency

### Current purpose
`check_power_posing_public_surface.py` protects the reader-facing navigation surface.

### Current reads
- `snapshots/snapshot-v2.md`
- `README.md`

### Current failure semantics
A failure here means the reader-facing path no longer exposes the governance layers the case now depends on.

### Canonical responsibilities
- required status-layer links in `Current visible judgment`
- required reader-path links in `Snapshot reading path`
- required developer/reader-path links in `README.md`

This script answers the question:

> Can a reader still visibly reach the governance layers that explain the snapshot?

---

## Actual overlap

The real overlap is smaller than it first appears.

### Shared elements
The two scripts share:

- `snapshot-v2.md` as an input file
- section extraction logic
- markdown-link parsing style
- a broad concern with public-facing coherence

### Non-shared elements
They diverge on the most important point: what counts as truth failure.

- **Snapshot consistency** treats broken object/reference grounding as failure.
- **Public surface consistency** treats missing reader-visible navigation to governance layers as failure.

That is not a cosmetic distinction.
It is a different failure class.

---

## Merge options

### Option 1: full merge now
Put both scripts into one canonical `snapshot_and_surface_consistency.py` checker.

#### Benefits
- fewer files
- fewer workflows
- one place for markdown-section utilities

#### Costs
- failure reports become less local
- object/reference-truth failures and reader-path failures get mixed together
- the resulting script begins to protect two governance targets at once

#### Assessment
Not recommended now.
The reduction in file count is real but small.
The loss of semantic locality is more important.

---

### Option 2: partial merge at the utility layer
Keep two scripts, but later share helper functions such as:

- section extraction
- markdown link parsing
- snapshot path normalization

#### Benefits
- reduces duplicate parsing logic
- preserves distinct failure semantics
- lowers maintenance burden without collapsing governance targets

#### Costs
- introduces a shared helper surface that must itself be versioned carefully
- mild risk that later refactors over-generalize too early

#### Assessment
This is the most plausible future merge route.
It captures most of the engineering gain while preserving current checker boundaries.

---

### Option 3: keep fully separate for now
Leave both scripts independent.

#### Benefits
- clean failure localization
- no premature abstraction
- easy to reason about during ongoing pilot hardening

#### Costs
- small duplication in markdown parsing and section extraction
- one more workflow to monitor

#### Assessment
This is the correct current choice.
The current pilot is still young enough that semantic clarity matters more than small deduplication wins.

---

## Current verdict

### Verdict
**Do not merge the two scripts now.**

### More precise ruling
- **Full merge:** reject for now
- **Partial utility-layer merge later:** admissible and likely useful
- **Keep semantic checker boundaries separate now:** recommended

### Reason
The two scripts are adjacent but not redundant.
They protect different failure classes:

- governed snapshot truthfulness
- reader-facing governance visibility

That boundary is currently still worth preserving in explicit form.

---

## What would justify a later partial merge

A later partial merge becomes attractive if all three conditions are met:

1. the power-posing pilot stabilizes and stops changing its public-layer structure frequently,
2. a second case appears and repeats the same section-extraction / link-parsing patterns,
3. duplicated helper logic becomes a real maintenance burden rather than a theoretical one.

If those conditions are not met, early consolidation is more likely to create confusion than value.

---

## Recommended next engineering move

Do **not** rewrite checker boundaries yet.
Instead, the natural next step after this assessment is:

- add a tiny note in `check-atlas-v1.md` or a future atlas revision that the current merge ruling is:
  - full merge rejected for now,
  - utility-layer sharing admissible later,
  - semantic boundary preservation recommended now.

That keeps the decision explicit without forcing a refactor before the pilot actually needs one.

---

## Current closing note

This assessment should be read as a staging verdict, not a forever verdict.

The point is not to defend file count.
The point is to avoid collapsing two different kinds of failure into one checker before the pilot has earned that contraction.
