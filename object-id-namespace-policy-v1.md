# Object ID namespace policy v1

This note records the **current namespace policy** for Knowledge OS object ids.

It is intentionally conservative.
It does **not** rename existing objects.
It does **not** force project-prefixed ids prematurely.
It does something smaller and more useful:

> it explains why the current repo-local object id style still holds,
> and it defines the threshold at which explicit project-prefixed ids become necessary.

---

## One-sentence ruling

Current ruling:

> **Repo-local object ids remain valid at the current stage.**
> **Project-prefixed ids become necessary only when object identity must stay unambiguous across more than one active project namespace.**

That is the whole policy.

---

## Why this note exists now

The current repository already uses governed object ids such as:

- `C-0001`
- `C-0002`

That style is currently readable, compact, and sufficient inside the present scope.

The problem is not that these ids are already wrong.
The problem is that without an explicit namespace policy, later growth could trigger confused, reactive renaming.

This note exists so future upgrades happen deliberately rather than under pressure.

---

## Current accepted object-id model

At the current stage, object ids are treated as:

> **repo-local governed identifiers inside the current active project environment**

That means current ids such as:

- `C-0001`
- `E-0007`
- `D-0012`
- `V-0003`

are acceptable **as long as** all of the following remain true:

1. the repository is still functioning as one active governed project environment,
2. object routing and interpretation remain unambiguous inside that environment,
3. public case rendering does not require cross-project id disambiguation,
4. and no second active project namespace is forcing id collision risk.

Under those conditions, short ids are not a weakness.
They are an appropriate early-stage compression.

---

## Why current repo-local ids are still lawful

### 1. current scope is still narrow enough

There is not yet a broad multi-project object browser inside this repository.
The current usage remains close enough to one governed project environment that repo-local ids still resolve cleanly.

### 2. object meaning is carried by more than the raw id string

The current system also carries:

- object type,
- project context,
- file location,
- snapshot context,
- and link structure.

So the id string does not bear the whole identity burden by itself.

### 3. premature prefixing would create churn without corresponding benefit

Immediate renaming of current ids into forms such as:

- `sguft-C-0001`
- `knowledgeos-C-0001`

would currently create:

- file churn,
- link churn,
- snapshot churn,
- renderer churn,
- and historical diff noise,

without solving a pressing present collision problem.

That is the wrong trade right now.

---

## When project-prefixed ids become necessary

Project-prefixed ids become necessary when **any** of the following conditions becomes true.

### Trigger 1. more than one active project namespace shares the same working repository or object plane

If the repository begins to host multiple live governed projects whose object families could collide, repo-local ids stop being sufficient.

### Trigger 2. cross-project object routing becomes first-class

If the system starts supporting:

- cross-project search,
- cross-project object resolution,
- multi-project public browsing,
- or cross-project snapshot composition,

then object identity must become explicit across namespaces.

### Trigger 3. public release surfaces expose multiple projects side by side

If public-facing routes begin to show objects from multiple governed projects in one user-facing surface, implicit repo-local disambiguation is no longer enough.

### Trigger 4. downstream automation needs globally stable object addressing

If exports, APIs, or sync workflows begin to depend on stronger portable identity semantics, project-prefixed ids become much more justified.

---

## Preferred upgrade path when the threshold is crossed

When the threshold is crossed, the preferred upgrade path is:

```text
<project_key>-<object_family>-<serial>
```

Examples:

- `sguft-C-0001`
- `lkc-C-0001`
- `cosfit-E-0012`

Where:

- `project_key` is short, stable, and governance-backed,
- `object_family` remains human-readable,
- `serial` remains monotonically assigned within that project/object family scope.

This keeps ids compact while making namespace explicit.

---

## What should happen before any future migration

Before migrating to project-prefixed ids, the repository should first define:

1. the stable list of project keys,
2. the canonical migration scope,
3. how historical ids remain traceable,
4. whether old ids remain aliases,
5. and whether snapshots pin old ids, new ids, or both.

This matters because namespace migration is not only a naming operation.
It is a continuity operation.

---

## What should not happen now

This note explicitly rules out the following premature move:

> bulk-renaming current object ids only because future multi-project growth is imaginable.

Imagined future scale is not yet sufficient reason.
The upgrade should be threshold-driven, not anxiety-driven.

---

## Practical verdict

So the practical verdict is:

- **current repo-local ids remain lawful**
- **no immediate rename is justified**
- **project-prefixed ids are a future threshold upgrade, not a present obligation**
- **the correct current move is policy clarity, not migration churn**

That is the right namespace rule for the current stage.
