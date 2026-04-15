#!/usr/bin/env python3
"""Small local preview helper for the COCKPIT2-A interactive prototype."""

from __future__ import annotations

import argparse
import http.server
import os
import socketserver
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_PORT = 8011


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Preview the COCKPIT2-A interactive prototype locally.")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"Port to serve on (default: {DEFAULT_PORT})")
    parser.add_argument("--no-browser", action="store_true", help="Do not auto-open a browser tab")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    os.chdir(ROOT)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        url = f"http://localhost:{args.port}/"
        print("COCKPIT2-A local preview")
        print(f"- root: {ROOT}")
        print(f"- url:  {url}")
        print("- bounded interactive prototype only")
        print("- no live runtime / no frontend mutation")
        print("- press Ctrl+C to stop")
        if not args.no_browser:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping preview server.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
