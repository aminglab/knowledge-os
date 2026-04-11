#!/usr/bin/env python3
"""Local preview helper for the power-posing page prototype.

This script optionally refreshes page-data.js via generate_page_data.py,
then serves the current page directory over a tiny local HTTP server.
"""

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
import subprocess
import sys
import threading
import time
import webbrowser
from pathlib import Path

PAGE_DIR = Path(__file__).resolve().parent
GENERATOR = PAGE_DIR / "generate_page_data.py"
DEFAULT_PORT = 4173


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def run_generator(check_only: bool = False) -> int:
    cmd = [sys.executable, str(GENERATOR)]
    if check_only:
        cmd.append("--check")

    completed = subprocess.run(cmd, cwd=PAGE_DIR)
    return completed.returncode


def serve_directory(port: int, open_browser: bool) -> int:
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(PAGE_DIR)

    with ReusableTCPServer(("127.0.0.1", port), handler) as httpd:
        url = f"http://127.0.0.1:{port}/index.html"
        print(f"Serving power-posing page preview at {url}")
        print("Press Ctrl+C to stop.")

        if open_browser:
            def _open_browser() -> None:
                time.sleep(0.4)
                webbrowser.open(url)

            threading.Thread(target=_open_browser, daemon=True).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")
            return 0

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh and locally preview the power-posing living page."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_PORT,
        help=f"Local preview port. Default: {DEFAULT_PORT}",
    )
    parser.add_argument(
        "--no-refresh",
        action="store_true",
        help="Skip generate_page_data.py before serving.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run generate_page_data.py --check before serving instead of rewriting page-data.js.",
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Do not automatically open the preview in a browser.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.no_refresh:
        if not GENERATOR.exists():
            print(f"Missing generator: {GENERATOR}", file=sys.stderr)
            return 1

        exit_code = run_generator(check_only=args.check_only)
        if exit_code != 0:
            print("Page-data refresh/check failed. Preview not started.", file=sys.stderr)
            return exit_code

    return serve_directory(port=args.port, open_browser=not args.no_open)


if __name__ == "__main__":
    raise SystemExit(main())
