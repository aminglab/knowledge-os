# COCKPIT1-B Static Prototype Boundary v1

## Status

Drafted for prototype.

## Function

This file defines the admissible boundary for the first static cockpit prototype.

---

## One-sentence boundary ruling

> **The first cockpit prototype must prove layout, state transitions, and real case binding — not runtime completeness.**

---

## Required proof points

The prototype must prove:

- one shared cockpit frame
- five required screen states
- two distinct governed pilot cases
- object-centered main panel behavior
- visibly subordinate sidecar behavior

---

## Allowed simplifications

The prototype may:

- hardcode case data
- use static navigation buttons
- omit authentication
- omit persistence
- omit backend services
- omit model execution

---

## Forbidden overclaims

The prototype must not claim:

- working team-layer flows
- live verdict mutation
- live evidence ingestion
- public-layer replacement
- production implementation readiness

---

## Final boundary block

- prototype class: `low-fidelity static`
- dynamic runtime requirement: none
- implementation overclaim: forbidden
