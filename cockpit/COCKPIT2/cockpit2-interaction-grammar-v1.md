# COCKPIT2 Interaction Grammar v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum lawful interaction grammar for COCKPIT2.
It upgrades the cockpit from a bounded static prototype to a bounded interactive prototype without crossing into runtime mutation or production claims.

---

## Governing principle

COCKPIT2 interaction is lawful only when interaction remains:

- object-centered
- read-dominant
- auditable
- bounded by the current cockpit holds

The purpose of interaction is not to let the frontend improvise.
It is to let users navigate the governed object space more powerfully without breaking the current boundaries.

---

## Minimum interaction families

### 1. Focus switching
The cockpit may support bounded switching between:

- landing overview
- claim focus
- evidence adjacency
- dissent pressure
- verdict boundary
- route view

The focus target must always be a named cockpit object or named route view.

### 2. Rail expansion and collapse
The cockpit may support:

- left-rail tree expansion/collapse
- right-rail panel expansion/collapse
- bounded section folding inside the main panel

These are lawful only when they reveal or hide already-governed surfaces.
They must not manufacture new semantics.

### 3. Lens switching
The cockpit may expose multiple bounded reading lenses, including:

- `focus`
- `pressure`
- `route`
- `boundary`

A lens changes what is foregrounded.
It does not change the governed object state.

### 4. Cross-case switching
The cockpit may support bounded switching between the currently bound pilot cases.
Case switching must preserve:

- one shared cockpit frame
- one shared slot grammar
- one visible case identity

Cross-case switching does not yet imply repository-wide cockpit genericity.

### 5. Action-trigger exposure
The cockpit may expose bounded action triggers in the UI.
These triggers must remain suggestion-layer triggers only.
They do not directly mutate governed objects.

---

## Forbidden interaction classes at this stage

COCKPIT2 interaction does **not** yet include:

- freeform object mutation from the frontend
- verdict rewriting from the frontend
- evidence upload workflows
- team-layer collaboration mechanics
- public-layer publishing from the cockpit
- persistent runtime task orchestration

---

## Lawful reading of “interactive”

For COCKPIT2, “interactive” means:

> the bounded cockpit prototype may now change focus, reveal governed neighborhoods, switch reading lenses, and expose suggestion-layer triggers.

It does **not** mean:

> the cockpit has become a live runtime or a write-capable research application.
