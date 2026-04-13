# case-template-extraction-checklist-v1

## Status

Working extraction checklist v1.

## Function

This document turns the ruling in `case-template-boundary-v1.md` into an operational checklist.

Its job is narrow:

- identify what a future second case may copy directly,
- identify what must be rewritten immediately,
- identify what must **not** yet be assumed generic,
- and reduce the chance of fake template reuse.

This is **not** a second-case launch document.
It becomes active only after a second case is explicitly authorized.

---

## Activation condition

Use this checklist only when all of the following are true:

- `phase-transition-decision-v1.md` is no longer the blocking authority against second-case expansion,
- the project has explicitly decided to open a second case,
- the new case has its own domain payload ready to replace `power-posing` content,
- the team is copying a shell, not cloning a controversy.

If those conditions are not met, stop here.

## Current activation status

Those conditions are now met for the currently authorized second case.

The activating authority object is:

- [`../../second-case-authorization-v1.md`](../../second-case-authorization-v1.md)

That file does not replace this checklist.
It explicitly activates the shell-copy discipline for `cases/h-pylori-ulcer/`.

---

## Core rule

The governing rule is:

> Copy the shell. Rewrite the payload. Do not pretend the current implementation is already generic.

---

## Direct-copy checklist

The following items may be copied **as structural starting points** for a future case.

### A. Structural directories and layer expectations

- [ ] Create explicit object directories for claims, evidence, dissents, and verdicts.
- [ ] Preserve the expectation that the case line exposes distinct layers:
  - object layer
  - reference layer
  - governance wording layer
  - snapshot layer
  - reader-facing surface layer
  - publishing layer
  - checking layer
  - CI layer
  - meta-governance layer

### B. Reference shell

- [ ] Copy the dual-reference pattern:
  - thin reader-facing `references.md`
  - stable machine-facing metadata file
- [ ] Preserve the rule that reader navigation and machine validation are separate jobs.

### C. Governance wording shell

- [ ] Copy the existence of an explicit `status-legend` document.
- [ ] Copy the existence of an explicit `verdict-grammar` document.
- [ ] Preserve the rule that public wording must remain tethered to governance wording objects.

### D. Snapshot shell

- [ ] Copy the expectation that the public-facing snapshot is not pure free prose.
- [ ] Preserve visible linkage from snapshot to governance wording documents.

### E. Publishing shell

- [ ] Preserve the expectation that a case-level publishing tool may expose:
  - validation
  - check-only mode
  - summary output
  - machine-readable summary
  - schema identity
  - documented contract

### F. Checker-network shell

- [ ] Preserve checker specialization instead of collapsing everything into one mega-checker.
- [ ] Preserve explicit checker-boundary reasoning.
- [ ] Preserve the principle that adjacent checks may remain separate when their failure meanings differ.

### G. CI shell

- [ ] Copy workflow-level enforcement for the case checks.
- [ ] Preserve the principle that CI belongs to a hardened case shell.

### H. Meta-governance shell

- [ ] Copy the practice of documenting checker topology when the case line becomes nontrivial.
- [ ] Copy the practice of writing explicit merge or separation rulings when adjacent checks appear similar.
- [ ] Copy the practice of writing phase-transition rulings before expansion.

---

## Rewrite-immediately checklist

The following items must be rewritten immediately for a new case.
Do **not** copy them forward as if they were reusable content.

### A. Object payload

- [ ] Rewrite every claim object.
- [ ] Rewrite every evidence object.
- [ ] Rewrite every dissent object.
- [ ] Rewrite every verdict object.
- [ ] Rewrite lineage relations so they reflect the new case rather than the `power-posing` arc.

### B. Reference payload

- [ ] Replace all source ids.
- [ ] Replace all bibliographic metadata.
- [ ] Replace all case-bound source mappings.
- [ ] Rebuild the metadata file around the new case’s sources.

### C. Snapshot payload

- [ ] Rewrite the public-facing snapshot prose.
- [ ] Rewrite the controversy narrative.
- [ ] Rewrite the status explanations so they match the new case.
- [ ] Rewrite any explanatory wording tied to the `power-posing` replication story.

### D. README payload

- [ ] Rewrite the reader path sequence if the new case requires a different entry flow.
- [ ] Rewrite case motivation and overview language.
- [ ] Rewrite folder guidance where file roles or reading order differ.

### E. Governance payload

- [ ] Rewrite status wording if the new case needs different public phrasing.
- [ ] Rewrite verdict grammar payload if the new case has different judgment patterns.

### F. Checker assumptions

- [ ] Rewrite checks that depend on current section names.
- [ ] Rewrite checks that depend on current public wording.
- [ ] Rewrite checks that depend on `power-posing`-specific narrative or release assumptions.

---

## Mixed-layer caution checklist

The following items contain reusable value, but only as shell + rule.
Treat them carefully.

### A. Generator

- [ ] Reuse the idea of a case-scoped publishing tool.
- [ ] Do **not** assume the current `generate_page_data.py` is already multi-case.
- [ ] Inspect path assumptions before reuse.
- [ ] Inspect expected sections before reuse.
- [ ] Inspect release-surface assumptions before reuse.

### B. Checker suite

- [ ] Reuse checker roles where they still make sense.
- [ ] Do **not** assume current checker bodies apply without change.
- [ ] Inspect whether failure meaning remains the same in the new case.

### C. README surface pattern

- [ ] Reuse the distinction between reader-facing and developer-facing navigation.
- [ ] Do **not** assume the current reading order transfers unchanged.

---

## Do-not-assume checklist

The following assumptions remain unauthorized.

- [ ] Do **not** assume one generator now compiles all cases.
- [ ] Do **not** assume one schema now fits all cases.
- [ ] Do **not** assume all future cases need the exact same filenames.
- [ ] Do **not** assume the current checker network is the final global architecture.
- [ ] Do **not** assume `power-posing` public wording is template wording.
- [ ] Do **not** assume that because a shell exists, a second case should open immediately.

---

## Pre-copy verification gate

Before copying anything into a second case, verify all of the following:

- [ ] The new case has a clearly bounded controversy or knowledge-pressure surface.
- [ ] The new case can support explicit claims, evidence, dissents, and verdicts.
- [ ] The team knows which existing files are shell and which are payload.
- [ ] The team has named what must be rewritten before first commit.
- [ ] The team is not using the shell as an excuse to skip case-specific thinking.

If any box remains unchecked, do not copy yet.

---

## Minimum extraction package

If a future second case is opened, the minimum reusable package that may be extracted from `power-posing` is:

- directory and layer expectations,
- dual-reference pattern,
- governance wording split,
- snapshot-to-governance linkage rule,
- publishing-contract pattern,
- checker-network pattern,
- CI expectation,
- meta-governance discipline.

Everything else must justify itself again inside the new case.

---

## Failure modes this checklist is meant to prevent

This checklist exists to prevent the following mistakes:

1. **Clone-the-content failure**  
   Copying `power-posing` substance instead of copying reusable shell.

2. **Fake-generic failure**  
   Treating one hardened case as if a universal framework has already been earned.

3. **Section-name coupling failure**  
   Reusing checks whose logic is secretly tied to current wording or section structure.

4. **Payload leakage failure**  
   Allowing old source ids, verdict phrases, or snapshot logic to leak into a new case.

5. **Premature expansion failure**  
   Opening a second case before the first seam is understood.

---

## Verdict

Current verdict:

> A future second case may reuse the `power-posing` shell only under disciplined extraction.
>
> The shell is reusable in part.
>
> The payload is not.
>
> Genericity remains partial, local, and earned only at the seam level.
