# COCKPIT1 Action Grammar v1

## Status

Drafted for construction.

## Function

This file defines the minimum **institutional action grammar** for COCKPIT1.
In the cockpit, users do not primarily ask an AI an open question.
They perform object-anchored institutional actions.

---

## One-sentence action ruling

> **Every cockpit action must name its object anchor, its read scope, its write scope, and its audit trace.**

---

## Minimum action set

### 1. `scan_missing_evidence`
- anchor: claim or route
- reads: target claim, current evidence tree, open dissents
- writes: no direct write by default
- output: structured gap report

### 2. `draft_dissent_response`
- anchor: dissent
- reads: dissent, target claim, linked evidence
- writes: response draft object or note
- output: answerable / unanswered / evidence-needed split

### 3. `check_upgrade_conditions`
- anchor: claim or verdict
- reads: target claim, evidence, dissents, prior verdict state
- writes: no direct verdict upgrade without human sign-off
- output: admissibility assessment

### 4. `export_progress_summary`
- anchor: project, route, or claim
- reads: recent changes and current state
- writes: export artifact only
- output: structured summary

### 5. `generate_canonical_continuation`
- anchor: project or route
- reads: open objects, holds, unresolved dissents
- writes: no direct route mutation by default
- output: ranked next-step continuation

### 6. `freeze_object_revision`
- anchor: object
- reads: current object state
- writes: yes, but only with explicit commit/audit record
- output: revision event

---

## Write-scope classes

- `read_only`
- `draft_only`
- `draft_plus_commit`
- `human_signoff_required`

COCKPIT1 should default to `read_only` or `draft_only` unless the action explicitly belongs to revision freezing.

---

## Audit floor

Every cockpit action must record at least:

- action name
- anchor object
- actor
- model/runtime used
- timestamp
- output location
- whether a write occurred

---

## Final grammar block

- minimum actions: 6
- direct verdict writes: forbidden by default
- audit requirement: mandatory
