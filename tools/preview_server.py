#!/usr/bin/env python3
"""Stable local preview server for the Spank The Monkey static site.

Why this exists:
- `python3 -m http.server` can terminate/noise out when Chrome drops media
  connections and triggers BrokenPipeError/ConnectionResetError during review.
- This server uses ThreadingHTTPServer, suppresses noisy request logs, and treats
  dropped browser connections as normal preview behavior.

Usage:
  python3 tools/preview_server.py
  python3 tools/preview_server.py --port 8769
"""

from __future__ import annotations

import argparse
import functools
import http.server
import os
import socket
import socketserver
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"


class QuietStaticHandler(http.server.SimpleHTTPRequestHandler):
    """Static handler that ignores normal browser disconnect noise."""

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        return

    def log_error(self, format: str, *args: object) -> None:  # noqa: A002 - stdlib signature
        return

    def handle_one_request(self) -> None:
        try:
            super().handle_one_request()
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            self.close_connection = True

    def copyfile(self, source, outputfile) -> None:  # type: ignore[no-untyped-def]
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            self.close_connection = True


class ReusableThreadingHTTPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def server_bind(self) -> None:
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, "SO_REUSEPORT"):
            try:
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            except OSError:
                pass
        super().server_bind()


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve the Spank static site for local review.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8768")))
    args = parser.parse_args()

    if not SRC.exists():
        raise SystemExit(f"Missing static source directory: {SRC}")

    handler = functools.partial(QuietStaticHandler, directory=str(SRC))
    with ReusableThreadingHTTPServer((args.host, args.port), handler) as httpd:
        print(f"Serving Spank preview at http://{args.host}:{args.port}/ from {SRC}", flush=True)
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
