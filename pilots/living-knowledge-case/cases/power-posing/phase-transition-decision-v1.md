# Phase Transition Decision v1

This file is the current **phase transition decision v1** for the power-posing pilot.

Its question is simple:

- should the project open a second case now,
- or should it first extract a small reusable template layer from the current power-posing system?

This decision is scoped to the current pilot stage.
It is not a permanent repository-wide doctrine.

---

## Current situation

The power-posing case is no longer only a one-off markdown example.
It now includes:

- a public snapshot layer,
- a source metadata layer,
- a verdict grammar layer,
- a status legend layer,
- a page-generation entry surface,
- and a multi-check validation network with explicit CI workflows.

That means the repository has crossed a threshold.
The next move should no longer be chosen only by narrative interest.
It should be chosen by what makes the structure more reusable without prematurely abstracting away the first real case.

---

## Option A: open a second case now

### Benefits
- tests whether the current design can survive a second real example
- exposes hidden assumptions that only become visible cross-case
- reduces the risk that power-posing bakes in an accidental pseudo-standard

### Costs
- duplicates current case-specific scaffolding before the reusable seam is clear
- risks copying current naming and file conventions without deciding which parts are genuinely canonical
- increases maintenance load while the first case is still the only mature source of truth

### Current assessment
This option is attractive, but it is still slightly early.

The current pilot has only just reached the point where its validation network is legible enough to assess.
Opening a second case immediately would test breadth before the first case has yielded its first reusable template boundary.

---

## Option B: extract a small reusable template layer first

### Benefits
- clarifies which parts of power-posing are genuinely case-agnostic
- turns current hardening work into a reusable asset rather than a one-case monument
- makes the eventual second case cheaper and more diagnostic
- avoids premature full abstraction while still reducing accidental one-off structure

### Costs
- can drift into over-abstraction if not kept deliberately small
- delays the second case slightly
- requires explicit discipline about what is and is not being templated

### Current assessment
This is the better next move.

The key is that the extraction should be **small**.
The project should not try to build a generic Knowledge OS compiler now.
It should only extract the first obvious reusable seam.

---

## Current verdict

### Verdict
**Do not open a second case yet.**

### Recommended next phase
**Extract a small reusable template layer from power-posing first.**

### Why
The first case is now mature enough to reveal reusable structure, but not yet so stable that a broad second-case expansion is cheaper than a narrow template extraction.

The right move is therefore not:

- freeze everything into a generic framework,
- nor duplicate the whole structure into a second case immediately.

The right move is:

- identify one narrow reusable seam,
- extract it cleanly,
- then use that seam to make the eventual second case diagnostically stronger.

---

## What “small reusable template layer” means here

At the current stage, a sensible half-step abstraction would likely cover only things such as:

- a canonical case folder skeleton,
- a minimal reader-path skeleton,
- shared validation utility conventions,
- and a short definition of which layers are expected in a public living case.

It should **not** yet attempt all of the following:

- a fully generic multi-case generator,
- repository-wide verdict doctrine,
- universal source ontology,
- or a final cross-case rendering architecture.

Those would be premature.

---

## Suggested immediate target

The most natural immediate target is to define a first reusable scaffold such as:

- `case-template-boundary-v1.md`
- or an equivalent small document that says which files and layers in power-posing are currently considered reusable

That document should separate:

- case-specific content,
- from reusable pilot structure.

Only after that boundary is explicit does a second case become maximally informative.

---

## Closing note

This decision should be read as a **staging verdict**.

It does not say that the project should avoid a second case.
It says that the project should earn the second case by first extracting one clean reusable seam from the first one.
