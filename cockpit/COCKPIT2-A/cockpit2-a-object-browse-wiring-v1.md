# COCKPIT2-A Object Browse Wiring v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum object-browse wiring for the COCKPIT2-A prototype.
Its purpose is to ensure that stronger interaction still reads as object-centered cockpit navigation rather than generic interface movement.

---

## Governing principle

Every stronger interactive surface in COCKPIT2-A must be reachable through named object anchors.
Object browsing is lawful only when the frontend remains visibly downstream of the governed case layer.

---

## Required browse wiring

### 1. State to anchor wiring
Each screen state must expose a bounded anchor list.
The active state must visibly determine the available object anchors.

### 2. Anchor to main-panel wiring
Selecting an object anchor must visibly update the main panel around that anchor.
The main panel may show:

- object identity
- bounded neighborhood
- lens-specific interpretation
- visible action-trigger posture

### 3. Anchor continuity across lenses
Switching lenses must preserve the active object anchor unless the user explicitly changes it.

### 4. Case continuity
Switching screen states across cases must visibly replace the anchor list with the correct case-scoped objects.
The prototype must not flatten both cases into one anonymous object list.

---

## Required anchor families

Across the bounded prototype, the visible anchor universe must include at least:

- one claim anchor
- one evidence anchor
- one dissent anchor
- one verdict anchor
- one route anchor

The first lift does not need to expose all possible object kinds.
It only needs enough anchor diversity to prove lawful browse structure.

---

## Forbidden browse shortcuts

COCKPIT2-A object browse becomes unlawful if:

- the active object is not named
- the visible neighborhood no longer traces to case semantics
- the object list becomes repo-wide instead of bounded
- the prototype hides current holds when boundary reading is selected

---

## Acceptance note

The goal is not to build a complete object browser.
The goal is to prove that a stronger cockpit can browse governed objects without collapsing back into blank chat or forward into uncontrolled runtime.
