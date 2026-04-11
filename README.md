# Knowledge OS

*A protocol layer and operating environment for governing the lifecycle of knowledge objects.*

It is not a chat wrapper, not an automated paper factory, and not a generic note-taking tool.
It is a system for organizing collaboration between humans and intelligent agents around four core object families:

- **Claim**
- **Evidence**
- **Dissent**
- **Verdict**

## Why this exists

Humanity still manages dynamic knowledge through static publication artifacts.
A paper can be published, cited, indexed, and archived, but its core claims usually cannot be formally attacked in place, visibly downgraded, linked to new counter-evidence, or tracked through long-term status changes.

The result is a structural gap:

- claims become detached from their later fate,
- evidence chains drift or break,
- dissent evaporates into chat logs and review threads,
- verdicts remain implicit,
- and public documents continue to circulate after their knowledge status has changed.

Knowledge OS exists to replace the **publish-and-freeze** model with a **living governance model**.

## Core idea

The system treats important knowledge work as a graph of governed objects rather than a pile of documents.

A paper, memo, appendix, or white paper is therefore not the primary object. It is a **snapshot or publication view** over a deeper object graph.

## Product surfaces

Knowledge OS has three connected surfaces:

### 1. Private Cockpit
A workspace for drafting, decomposing, mapping, and governing a project from the inside.

### 2. Team Layer
A collaboration layer for review, assignment, permissions, audit, and shared responsibility.

### 3. Public Layer
A release layer for publishing selected snapshots, living knowledge pages, and public cases.

## Public entry

The repository now has a small but explicit public-layer entry chain.

Start here if you want the public-facing surface first rather than the repository documentation first:

- [`PUBLIC-ENTRY.md`](./PUBLIC-ENTRY.md) — the current system-level public entry seed
- [`PUBLIC-CASES.md`](./PUBLIC-CASES.md) — the current public case listing seed
- [`Power Posing`](./pilots/living-knowledge-case/cases/power-posing/snapshots/snapshot-v2.md) — the first public case homepage

## Preview and governance entry points

Two recently strengthened repo-level routes are now worth surfacing directly:

### Local preview of the first public case

If you want to locally preview the current living page rather than only read markdown surfaces, start here:

- [`power-posing/page/README.md`](./pilots/living-knowledge-case/cases/power-posing/page/README.md)
- [`preview_page.py`](./pilots/living-knowledge-case/cases/power-posing/page/preview_page.py)

The local preview helper can refresh `page-data.js` and start a tiny static server so a forked checkout can show the current page quickly.

### Revision governance

If you want the current semantic revision rule for governed objects, start here:

- [`revision-model-v1.md`](./revision-model-v1.md)
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)

The current rule now makes `revisions` a governed semantic history rather than a loose placeholder field.

### Object id namespace policy

If you want the current rule for why repo-local ids still hold and when project-prefixed ids become necessary, start here:

- [`object-id-namespace-policy-v1.md`](./object-id-namespace-policy-v1.md)
- [`ARCHITECTURE.md`](./ARCHITECTURE.md)

The current rule keeps repo-local ids lawful for now, while defining the threshold for future namespace upgrades.

## Current stance

This repository is building toward a system that is:

- **object-first** rather than document-first,
- **governance-first** rather than generation-first,
- **private by default** and selectively public,
- **model-agnostic** by design,
- and **protocol-shaped**, but not prematurely frozen.

## What happens here first

The early project does **not** begin by building federation, a marketplace, or a fully formalized global standard.
It begins by pressure-testing the language and the product in live pilots.

Current pilot directions:

1. **SGUFT cockpit pilot** — a real long-running research program modeled as Claim / Evidence / Dissent / Verdict.
2. **Living Knowledge Case pilot** — a public disputed scientific claim rendered as a living knowledge object.

## Repository guide

- [`FOUNDING.md`](./FOUNDING.md) — the short founding narrative
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — the current working architecture
- [`ROADMAP.md`](./ROADMAP.md) — staged build and validation plan
- [`repo-signal-closeout-v1.md`](./repo-signal-closeout-v1.md) — the current stage closeout for repo entry, preview, and revision-governance signal
- [`object-id-namespace-policy-v1.md`](./object-id-namespace-policy-v1.md) — the current namespace rule for governed object ids

## Design constraints

Knowledge OS must not:

- collapse into a glorified note app,
- collapse into a generic chat shell,
- pretend to be local-first when it is not,
- freeze the protocol before real use,
- or confuse publication with truth.

## One-sentence definition

**Knowledge OS is a protocol layer and operating environment for organizing collaboration around claims, evidence, dissent, and verdicts.**
