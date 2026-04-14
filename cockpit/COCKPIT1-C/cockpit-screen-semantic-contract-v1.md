# COCKPIT1-C Screen Semantic Contract v1

## Status

Drafted for prototype hardening.

## Function

This file defines the minimum semantic contract for the COCKPIT1-B static prototype screens.

---

## One-sentence contract ruling

> **A cockpit screen is not identified by visual style alone. It is identified by the bounded semantic state it exposes.**

---

## Required screen semantics

### 1. `landing_state`
Must expose:

- both bound cases
- shared cockpit frame
- phase-1 demo scope reminder

### 2. `claim_focus_state`
Must expose:

- focused claim title
- current judgment / verdict phrase
- next actions
- at least one direct pressure grouping

### 3. `verdict_boundary_state`
Must expose:

- current verdict floor
- retained holds or current non-upgrade boundary
- lawful movement constraint

### 4. `dissent_pressure_state`
Must expose:

- current dissent cluster
- pressure on a claim neighborhood
- at least one candidate next action

### 5. `route_map_state`
Must expose:

- route or map identity
- multiple object entry surfaces or route points
- current cockpit role for that case

---

## Semantic honesty rule

A screen must not reuse a label while silently dropping the semantic content that makes that label lawful.

Examples:

- a `claim_focus_state` without a current judgment phrase is not lawful
- a `verdict_boundary_state` without retained holds or non-upgrade wording is not lawful
- a `route_map_state` without visible route identity is not lawful

---

## Final contract block

- required states: 5
- label without semantic payload: forbidden
- current contract scope: static prototype only
