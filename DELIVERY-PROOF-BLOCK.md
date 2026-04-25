# Delivery Proof Block Template

## Status

Required template for remotely verifiable coding deliveries.

## Purpose

This template gives a copyable proof block for coding agents and reviewers.
It exists to prevent reports that are true only in a local working directory from being accepted as GitHub-delivered work.

---

## Copyable proof block

```text
owner/repo:
branch or PR:
latest commit SHA:
changed file paths:
- 
```

---

## Field rules

### `owner/repo`

Must be the exact GitHub repository, for example:

```text
owner/repo: aminglab/knowledge-os
```

### `branch or PR`

Must be a GitHub-visible branch or pull request.
Local-only branch names do not count.

Examples:

```text
branch or PR: codex/delivery-proof-checklist-v1
branch or PR: https://github.com/aminglab/knowledge-os/pull/<number>
```

### `latest commit SHA`

Must be the GitHub-visible head SHA for the named branch or PR.
A local-only SHA is not sufficient.

### `changed file paths`

Must list every changed file path that the reviewer should inspect.
Each listed path must exist in the named repository at the named branch, PR, or SHA.

---

## Non-acceptance examples

The following proof blocks are not acceptable:

```text
owner/repo: unknown
branch or PR: work
latest commit SHA: local only
changed file paths:
- file.md
```

```text
owner/repo: aminglab/knowledge-os
branch or PR: local branch, push failed
latest commit SHA: 1234567
changed file paths:
- file.md
```

---

## Acceptance sentence

Use this sentence only after remote verification succeeds:

> This delivery is accepted because the owner/repo, branch or PR, latest commit SHA, and changed file paths are all visible on GitHub and mutually consistent.
