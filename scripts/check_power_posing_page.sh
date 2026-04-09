#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GENERATOR="$REPO_ROOT/pilots/living-knowledge-case/cases/power-posing/page/generate_page_data.py"
PYTHON_BIN="${PYTHON:-python3}"

exec "$PYTHON_BIN" "$GENERATOR" --check
