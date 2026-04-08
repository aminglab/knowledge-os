# Knowledge OS

**Knowledge OS** is a protocol and product direction for governing the lifecycle of knowledge objects.

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

## Design constraints

Knowledge OS must not:

- collapse into a glorified note app,
- collapse into a generic chat shell,
- pretend to be local-first when it is not,
- freeze the protocol before real use,
- or confuse publication with truth.

## One-sentence definition

**Knowledge OS is a public protocol layer for organizing collaboration between humans and intelligent agents around claims, evidence, dissent, and verdicts.**
