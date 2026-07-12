#!/usr/bin/env python3
"""Minimal static server for previewing the invoice app (sandbox-safe)."""
import functools
import http.server
import socketserver

DIRECTORY = "/Users/joseph/Documents/Project/Onnuri Church/allfj-invoice"
PORT = 8731

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"serving {DIRECTORY} at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
