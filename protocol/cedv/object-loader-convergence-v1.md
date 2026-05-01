# CEDV-G / Object Loader Convergence v1

## Status

Protocol checker object-loading convergence pass.

## Function

This file records the first CEDV object-loader convergence pass.

The goal is narrow:

> introduce a small shared loader for current CEDV example objects so protocol-facing checkers do not each reimplement object-file loading and id-keyed assembly.

This is not a repository-wide object registry.
It is not a public release index.
It is a small utility for current CEDV example objects.

---

## Entry context

Before this pass, CEDV already had:

- schema floor;
- relation and basis validation floor;
- shared constant-authority layer;
- canonical example registry;
- expanded enum drift coverage;
- protocol-facing checker import convergence;
- shared simple YAML parser;
- relation-admissibility matrix.

After the parse utility pass, two protocol-facing checkers still independently performed the same object-loading pattern:

1. read example YAML file;
2. parse tiny YAML subset;
3. check `id`;
4. check duplicate ids;
5. assemble an id-keyed `objects` dictionary.

That repeated loading path was small, but it had become the next likely utility drift surface.

---

## Utility added

This pass adds:

- `scripts/lib/cedv_objects.py`.

It currently exports:

- `load_cedv_objects(paths, errors, root)`.

The loader:

- reads current CEDV example object files;
- parses them through `scripts/lib/simple_yaml.py`;
- checks missing files;
- checks missing ids;
- checks duplicate ids;
- checks object types against `CEDV_OBJECT_TYPES`;
- returns an id-keyed object dictionary.

---

## Checker changes

### `scripts/check_cedv_relation_basis_validation.py`

Now imports:

- `load_cedv_objects` from `scripts.lib.cedv_objects`.

It no longer performs its own file-read / parse / id assembly loop.

### `scripts/check_cedv_example_registry.py`

Now imports:

- `load_cedv_objects` from `scripts.lib.cedv_objects`.

It still retains registry-specific checks such as:

- path is registered;
- expected title matches;
- graph expectations are satisfied.

But object loading itself is shared.

---

## Workflow updates

This pass also updates:

- `.github/workflows/check-cedv-relation-basis-validation.yml`;
- `.github/workflows/check-cedv-example-registry.yml`.

The workflows now wake when shared loader or related helper files change.

---

## Acceptance result

CEDV-G / OBJECTLOAD1 is accepted at the following level:

> `PASS_FIRST_CEDV_OBJECT_LOADER_CONVERGENCE`

Meaning:

- current CEDV example object loading is shared by the two protocol-facing checkers that need it;
- object loading uses the existing tiny YAML parser utility;
- object-type checking uses shared constants;
- relation-basis and example-registry checkers no longer maintain parallel object-loading loops;
- the result remains intentionally scoped to CEDV examples.

---

## Retained holds

This pass does **not** claim:

- repository-wide object registry;
- public candidate indexing;
- case object indexing;
- markdown frontmatter loading across all pilots;
- full YAML parsing;
- schema validation;
- automatic graph construction;
- production API object loading.

The loader is a utility, not a platform subsystem.

---

## Boundary rule

Use `scripts/lib/cedv_objects.py` when a protocol-facing CEDV checker needs to load current CEDV example YAML objects.

Do not use it as a shortcut for:

- public-layer page data;
- source pages;
- claim pages;
- case-specific object stores;
- future runtime object databases.

Those may eventually need their own loaders, but this file does not authorize that expansion.

---

## Remaining debt

Likely future pressure points:

1. Registry loading remains local to `check_cedv_example_registry.py`.
2. External target rules in relation matrix may need richer validation later.
3. A future CEDV fixture suite may require a stronger object loader, but only after the fixture model exists.
4. Current object loading remains example-scoped; broader object loading should be justified by repeated use, not anticipation.

---

## Next recommended move

The natural continuation is:

> `CEDV-H / REGLOAD1`

Purpose:

> consider whether the example registry JSON loading and validation shape should be extracted into a tiny shared helper, but only if another protocol checker starts consuming the registry.

For now, avoid over-abstracting. The current loader closes the repeated object-loading loop; that is enough.
