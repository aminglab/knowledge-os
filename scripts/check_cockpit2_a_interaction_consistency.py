#!/usr/bin/env python3
"""Lightweight consistency check for COCKPIT2-A interaction and preview surfaces."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROTO_DIR = ROOT / "cockpit" / "COCKPIT2-A" / "prototype"
APP = PROTO_DIR / "app.js"
README = PROTO_DIR / "README.md"
PREVIEW_HELPER = PROTO_DIR / "preview_cockpit2_a.py"
PREVIEW_ROUTE = ROOT / "cockpit" / "COCKPIT2-A" / "cockpit2-a-preview-route-v1.md"
SMOKE = ROOT / "cockpit" / "COCKPIT2-A" / "cockpit2-a-preview-smoke-checklist-v1.md"
LENS_DOC = ROOT / "cockpit" / "COCKPIT2-A" / "cockpit2-a-bounded-lens-switch-v1.md"
BROWSE_DOC = ROOT / "cockpit" / "COCKPIT2-A" / "cockpit2-a-object-browse-wiring-v1.md"


def read_or_fail(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    app = read_or_fail(APP, errors)
    readme = read_or_fail(README, errors)
    helper = read_or_fail(PREVIEW_HELPER, errors)
    preview_route = read_or_fail(PREVIEW_ROUTE, errors)
    smoke = read_or_fail(SMOKE, errors)
    lens_doc = read_or_fail(LENS_DOC, errors)
    browse_doc = read_or_fail(BROWSE_DOC, errors)

    helper_required = [
        "COCKPIT2-A local preview",
        "bounded interactive prototype only",
        "no live runtime / no frontend mutation",
    ]
    for snippet in helper_required:
        if snippet not in helper:
            errors.append(f"preview helper missing snippet: {snippet}")

    readme_required = [
        "bounded four-lens switch (`focus`, `pressure`, `route`, `boundary`)",
        "bounded object-browse surface with named anchors per state",
        "suggestion-layer trigger panel",
    ]
    for snippet in readme_required:
        if snippet not in readme:
            errors.append(f"prototype README missing snippet: {snippet}")

    preview_required = [
        "preview_cockpit2_a.py",
        "local preview of a bounded interactive cockpit lift",
        "does not claim live runtime behavior",
        "cockpit2-a-preview-smoke-checklist-v1.md",
    ]
    for snippet in preview_required:
        if snippet not in preview_route:
            errors.append(f"preview route doc missing snippet: {snippet}")

    smoke_required = [
        "python preview_cockpit2_a.py",
        "Switch the active lens to `pressure`",
        "the active object anchor remains preserved",
        "sidecar audit log records a draft-only trigger note",
        "retained holds remain visible",
    ]
    for snippet in smoke_required:
        if snippet not in smoke:
            errors.append(f"smoke checklist missing snippet: {snippet}")

    lens_required = [
        "`focus`",
        "`pressure`",
        "`route`",
        "`boundary`",
    ]
    for snippet in lens_required:
        if snippet not in lens_doc:
            errors.append(f"lens doc missing snippet: {snippet}")
        if snippet.replace("`", "") + ": {" not in app and snippet not in app:
            # app uses object keys like focus: { ... }
            raw = snippet.replace("`", "") + ": {"
            if raw not in app:
                errors.append(f"app.js missing lens fixture matching {snippet}")

    browse_required = [
        "state must expose a bounded anchor list",
        "Selecting an object anchor must visibly update the main panel",
        "Switching lenses must preserve the active object anchor",
    ]
    for snippet in browse_required:
        if snippet not in browse_doc:
            errors.append(f"browse wiring doc missing snippet: {snippet}")

    app_required = [
        "Object anchor switched to",
        "Lens switched to",
        "Output class remains draft-only / suggestion-layer.",
        "HOLD_NO_LIVE_RUNTIME_COCKPIT",
        "HOLD_NO_OBJECT_MUTATION_FROM_FRONTEND",
    ]
    for snippet in app_required:
        if snippet not in app:
            errors.append(f"app.js missing interaction snippet: {snippet}")

    if errors:
        print("COCKPIT2-A interaction consistency check: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("COCKPIT2-A interaction consistency check: PASS")
    print("- preview helper present")
    print("- preview route and smoke checklist aligned")
    print("- lens grammar remains aligned")
    print("- object-browse wiring remains aligned")
    print("- suggestion-layer honesty preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
