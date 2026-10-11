"""S Device local-first starter API. Standard-library only. Python 3.10+.
Private by default: binds 127.0.0.1 unless explicitly configured.
Never expose to the internet without TLS, firewall and authentication gateway.
"""
import json
import os
import secrets
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.environ.get("SDEVICE_HOST", "127.0.0.1")
PORT = int(os.environ.get("SDEVICE_PORT", "8765"))
TOKEN = os.environ.get("SDEVICE_TOKEN", "")

class Handler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            return self._send(200, {"service": "s-device", "status": "ok", "time_utc": datetime.now(timezone.utc).isoformat()})
        if not TOKEN or not secrets.compare_digest(self.headers.get("Authorization", ""), "Bearer " + TOKEN):
            return self._send(401, {"error": "unauthorized"})
        if self.path == "/api/v1/device":
            return self._send(200, {"product": "S Device One", "os": "Android-based S Device UX", "phase": "foundation", "features": ["launcher", "local-service", "future-ai"]})
        return self._send(404, {"error": "not_found"})

    def do_POST(self):
        return self._send(501, {"error": "not_implemented"})

if __name__ == "__main__":
    if not TOKEN or len(TOKEN) < 24:
        raise SystemExit("Set SDEVICE_TOKEN to a random secret of at least 24 characters before startup")
    print(f"S Device local API listening on http://{HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
