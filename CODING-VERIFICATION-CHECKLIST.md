# Coding Verification Checklist

## Status

Required for all coding-agent delivery claims.

## Purpose

This checklist prevents a local-only coding report from being mistaken for a GitHub-verifiable delivery.
A coding task is not considered delivered merely because commands passed in a local working tree.
It is considered delivered only when the changed repository, branch or pull request, latest remote commit SHA, and changed file paths can be independently inspected on GitHub.

---

## Mandatory delivery evidence block

Every coding-agent completion report must include the following block:

```text
owner/repo:
branch or PR:
latest commit SHA:
changed file paths:
- path/to/file
```

If any field is missing, ambiguous, local-only, or not remotely inspectable, the delivery is not accepted.

---

## Required verification steps

Before declaring completion, run and record the following checks:

1. Confirm the remote repository:

```bash
git remote -v
```

The remote must match the intended `owner/repo`.

2. Confirm the current branch:

```bash
git branch --show-current
```

The branch name must be specific to the work. Avoid generic branch names such as `work`, `temp`, or `changes`.

3. Confirm the local HEAD:

```bash
git rev-parse HEAD
```

4. Push to the intended remote branch:

```bash
git push -u <remote> <branch>
```

5. Create or update a pull request on GitHub.

6. Re-check that the GitHub-visible branch or PR head SHA matches the reported `latest commit SHA`.

7. Re-check that every path listed under `changed file paths` is visible on GitHub at that SHA or PR.

---

## Push-failure rule

If push fails because of authentication, network, proxy, missing remote, or permission problems, the report must explicitly say that the task is **not yet remotely delivered**.

A failed push may be logged as an attempted delivery, but it is not an accepted delivery.

---

## No local-only acceptance rule

The following evidence is insufficient by itself:

- local `git status`
- local `git rev-parse HEAD`
- local test output
- local file inspection commands
- screenshots of a local terminal
- a branch name that is not visible on GitHub

Local evidence may support a report, but it cannot replace the mandatory remote proof block.

---

## Acceptance sentence

A coding-agent delivery is acceptable only when this sentence is true:

> The named GitHub repository, branch or PR, latest commit SHA, and changed file paths are all remotely inspectable and mutually consistent.
