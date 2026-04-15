#!/usr/bin/env python3
"""Lightweight consistency check for cockpit preview exposure surfaces."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PREVIEW_HELPER = ROOT / "cockpit" / "COCKPIT1-B" / "prototype" / "preview_cockpit.py"
PROTO_README = ROOT / "cockpit" / "COCKPIT1-B" / "prototype" / "README.md"
ROOT_README = ROOT / "README.md"
PUBLIC_ENTRY = ROOT / "PUBLIC-ENTRY.md"


def read_or_fail(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []

    helper = read_or_fail(PREVIEW_HELPER, errors)
    proto_readme = read_or_fail(PROTO_README, errors)
    root_readme = read_or_fail(ROOT_README, errors)
    public_entry = read_or_fail(PUBLIC_ENTRY, errors)

    if "COCKPIT1-B local preview" not in helper:
        errors.append("preview_cockpit.py missing local preview banner")
    if "static prototype" not in helper:
        errors.append("preview_cockpit.py missing static prototype honesty wording")

    proto_required = [
        "preview_cockpit.py",
        "python preview_cockpit.py",
        "zero-build static cockpit skeleton",
        "bounded static skeleton only",
    ]
    for snippet in proto_required:
        if snippet not in proto_readme:
            errors.append(f"prototype README missing snippet: {snippet}")

    root_required = [
        "Local preview of the first cockpit prototype",
        "COCKPIT1-B/prototype/README.md",
        "preview_cockpit.py",
        "zero-build static cockpit skeleton",
        "does not claim a production frontend",
    ]
    for snippet in root_required:
        if snippet not in root_readme:
            errors.append(f"README.md missing snippet: {snippet}")

    public_required = [
        "Preview the bounded cockpit prototype locally",
        "COCKPIT1-B/prototype/README.md",
        "preview_cockpit.py",
        "bounded local preview",
        "does not replace the current public-case entry chain",
    ]
    for snippet in public_required:
        if snippet not in public_entry:
            errors.append(f"PUBLIC-ENTRY.md missing snippet: {snippet}")

    if errors:
        print("Cockpit preview exposure consistency check: FAIL")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Cockpit preview exposure consistency check: PASS")
    print("- preview helper present")
    print("- prototype README route exposed")
    print("- root README route exposed")
    print("- PUBLIC-ENTRY route exposed")
    print("- prototype honesty wording preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
