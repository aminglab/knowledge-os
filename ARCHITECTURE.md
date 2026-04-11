# Architecture v0.2

Working draft.
Not a frozen specification.

## 1. First principle

Knowledge OS is a system for managing the **lifecycle of knowledge objects**.

Its minimal public language is built around four object families:

- **Claim**
- **Evidence**
- **Dissent**
- **Verdict**

Documents remain important, but they are downstream artifacts.
A paper, memo, appendix, or white paper is a **snapshot** over a deeper object graph.

## 2. Product surfaces

### Private Cockpit
The workspace where a person or small team drafts, maps, argues, and governs a project.

### Team Layer
The layer where permissions, review, assignment, and audit become explicit.

### Public Layer
The layer where selected objects become public snapshots, living pages, or public cases.

These are not three separate products.
They are three surfaces over the same evolving object graph.

## 3. Design principles

- **Object-first, document-second**
- **Lifecycle-first, not storage-first**
- **Governance over generation**
- **Protocol grows from use**
- **Private by default, public by deliberate release**
- **Model-agnostic by design**
- **Solo-founder buildability**

## 4. Canonical vocabulary

- **Claim** — a formally stated proposition under governance
- **Evidence** — a supporting or weakening artifact
- **Dissent** — a structured challenge, reservation, attack, or unresolved concern
- **Verdict** — the current institutional judgment on a target claim
- **Snapshot** — a frozen publication package derived from live objects
- **Lineage** — ancestry and descent relations between claims or snapshots
- **Actor** — a human or agent that creates, transforms, or reviews objects
- **Action** — a governed operation performed on an object

## 5. Core architectural stack

1. **Object Protocol Layer**
2. **Knowledge Graph / Storage Layer**
3. **Action + Governance Layer**
4. **Skill Runtime Layer**
5. **Product Surfaces** (Private / Team / Public)

```text
┌──────────────────────────────────────────────────────┐
│                  Public Surface                      │
│   snapshots · living pages · public dissent input   │
├──────────────────────────────────────────────────────┤
│                   Team Surface                       │
│   review · assignment · audit · permissions          │
├──────────────────────────────────────────────────────┤
│                 Private Cockpit                      │
│   drafting · mapping · triage · exploration          │
├──────────────────────────────────────────────────────┤
│                  Skill Runtime                       │
│   extraction · scanning · challenge · export         │
├──────────────────────────────────────────────────────┤
│             Action + Governance Layer                │
│   state transition · logging · validation            │
├──────────────────────────────────────────────────────┤
│          Object Protocol + Graph Storage             │
│   claims · evidence · dissent · verdicts · links     │
└──────────────────────────────────────────────────────┘
```

## 6. Core object envelope

```ts
BaseObject {
  id: string
  object_type: "claim" | "evidence" | "dissent" | "verdict"
  project_id: string
  title: string
  summary: string
  body: RichContent
  created_at: ISODateTime
  updated_at: ISODateTime
  created_by: ActorRef
  updated_by: ActorRef
  visibility: "private" | "team" | "public"
  labels: string[]
  links: Link[]
  revisions: RevisionRef[]
  lifecycle_state: string
}
```

### 6.1 Revision model (compact rule)

The `revisions` field is not only an audit convenience.
It is the semantic history of the object.

Current compact rule:

- every substantive object change creates a new revision state,
- new objects begin at version `1.0`,
- revisions use a simple `MAJOR.MINOR` model,
- minor means the same governed object with the same semantic identity, now clarified or enriched,
- major means the same governed object but a materially changed governed semantic state,
- lineage remains distinct from revision history,
- snapshots should pin exact revisions rather than only floating object ids.

Use the detailed companion note for the current working rule:

- `revision-model-v1.md`

### 6.2 Object id namespace rule (compact rule)

The `id` field is currently repo-local and project-contextual rather than globally prefixed.

Current compact rule:

- repo-local object ids remain lawful while the repository still functions as one active governed project environment,
- short ids such as `C-0001` remain acceptable while routing stays unambiguous inside that scope,
- explicit project-prefixed ids become necessary only when multiple active project namespaces or cross-project routing make current ids collision-prone,
- migration to prefixed ids should be threshold-driven, not anticipatory churn.

Use the detailed companion note for the current working rule:

- `object-id-namespace-policy-v1.md`

## 7. Crucial modeling decision: two axes

Do **not** collapse object lifecycle and epistemic standing into one status field.

### A. Lifecycle state
This is about the operational state of the object inside the system.
Examples: `draft`, `active`, `paused`, `superseded`, `withdrawn`, `archived`.

### B. Epistemic / institutional status
This is about how the claim currently stands as knowledge.
Examples: `under_evaluation`, `supported`, `contested`, `weakened`, `rejected`, `split`, `stabilized`.

A claim can be:

- `active` and `contested`,
- `archived` and historically `rejected`,
- `superseded` because it split into descendants, not because it was false.

## 8. Graph philosophy

Knowledge OS should not treat the whole object universe as a DAG.
That will become false in real use.

Use a **general directed graph**.
Some validated subgraphs may obey stricter constraints:

- dependency graphs may be DAG-like,
- lineage graphs may be partially ordered,
- response and publication graphs may form cycles at the broader system level.

## 9. Object families

### Claim
A formally introduced proposition with boundaries, assumptions, dependencies, and a target verdict level.

### Evidence
An accountable support object with links to claims, source references, artifacts, reproducibility notes, and custody.

### Dissent
A first-class governance object for attack, reservation, methodological challenge, boundary concern, or unresolved objection.

### Verdict
An institutional judgment about a claim, with a current level, rationale, supporting basis, and conditions for upgrade or downgrade.

## 10. Actions, not chats

The front-end interaction model should be organized around actions on objects, not generic prompting.

Examples:

- create claim
- attach evidence
- raise dissent
- request verdict update
- scan for missing support
- scan for unresolved dissent
- export snapshot
- split claim
- supersede claim

AI enters through governed actions, not as the center of the interface.

### 10.1 Action grammar (compact rule)

The current action model distinguishes six compact families:

- object creation
- object revision
- relation
- lifecycle
- epistemic / institutional
- publication
- skill-run

Current compact rule:

- actions must not collapse lifecycle change, epistemic change, relation change, and publication change into one undifferentiated event,
- object revision is distinct from graph mutation,
- lifecycle change is distinct from epistemic standing,
- publication actions are distinct from object semantic history,
- skill-run outputs must remain governed rather than self-authorizing.

Use the detailed companion note for the current working rule:

- `action-governance-grammar-v1.md`

## 11. Minimal skill runtime for V1

### Object Extractor
Turn raw notes, transcripts, or paper excerpts into candidate objects.

### Gap Scanner
Analyze a claim neighborhood for unsupported assumptions, missing evidence, unresolved dissent, and blocked verdict upgrades.

### Counterposition Generator
Generate candidate dissent objects rather than freeform criticism prose.

### Snapshot Composer
Build a publication-ready snapshot from selected objects.

### Case Renderer
Render a public living knowledge page from a snapshot or claim lineage.

All skill calls must create audit records.

## 12. Honest implementation stance

For V1, the realistic approach is **hosted-first with strong exportability**, not full local-first.

That means:

- server-hosted app is acceptable,
- project export must be easy,
- snapshot export must be durable,
- the object graph must remain portable,
- protocol artifacts must not be trapped in a black box.

Do not claim local-first unless the implementation truly supports offline-authoritative workflows.

## 13. Recommended V1 stack

- **Frontend:** Next.js + React
- **Styling:** Tailwind CSS
- **Backend:** Next.js route handlers / server actions
- **Database:** PostgreSQL
- **ORM:** Prisma or Drizzle
- **Auth:** NextAuth or Clerk
- **Storage:** S3-compatible object storage
- **AI orchestration:** Vercel AI SDK or equivalent model-agnostic layer
- **Deployment:** Vercel or equivalent simple deployment platform

## 14. Data model strategy for V1

Start with a relational core and explicit link tables.
Do not over-engineer a graph database in V1.

Suggested core tables:

- `projects`
- `objects`
- `object_links`
- `revisions`
- `actors`
- `skill_runs`
- `snapshots`
- `snapshot_objects`
- `actions`

The key is not storage purity.
The key is preserving object identity, history, links, and governed operations.

The `revisions` table should hold append-only semantic revision history rather than acting as a loose edit-log catchall.
Operational logging may be richer than revision history, but revision history itself should stay accountable and interpretable.

The `id` field should not be prematurely globalized.
Namespace upgrades should occur only when the repository crosses from repo-local project context into genuinely multi-project identity pressure.

The `actions` table should preserve governed action history rather than collapsing every object event into an untyped audit stream.

## 15. What must not happen

- Do not become a glorified note app.
- Do not become a generic chat wrapper.
- Do not pretend to be local-first when it is not.
- Do not freeze the protocol before real use.
- Do not confuse publication with truth.
