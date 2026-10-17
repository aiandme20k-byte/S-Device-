"""S Device Build 011 local-only API, projector and cross-platform UI. Python 3.10+."""
import json
import os
import secrets
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = os.environ.get("SDEVICE_HOST", "127.0.0.1")
PORT = int(os.environ.get("SDEVICE_PORT", "8765"))
TOKEN = os.environ.get("SDEVICE_TOKEN", "")
DASHBOARD = Path(__file__).resolve().parent.parent / "dashboard" / "index.html"
WEB = Path(__file__).resolve().parent.parent / "web"
WEB_ROUTES = {
    "/app": ("index.html", "text/html; charset=utf-8"),
    "/app/": ("index.html", "text/html; charset=utf-8"),
    "/app/sw.js": ("sw.js", "application/javascript; charset=utf-8"),
    "/app/manifest.webmanifest": ("manifest.webmanifest", "application/manifest+json; charset=utf-8"),
    "/app/icon.svg": ("icon.svg", "image/svg+xml"),
}

class Handler(BaseHTTPRequestHandler):
    def _headers(self, status, typ, size):
        self.send_response(status)
        self.send_header("Content-Type", typ)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'unsafe-inline' 'self'; script-src 'unsafe-inline' 'self'; connect-src 'self'; object-src 'none'; frame-ancestors 'none'")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Length", str(size))
        self.end_headers()

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self._headers(status, "application/json; charset=utf-8", len(body))
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            return self._json(200, {"service": "s-device", "status": "ok", "time_utc": datetime.now(timezone.utc).isoformat()})
        if self.path in ("/", "/dashboard"):
            body = DASHBOARD.read_bytes()
            self._headers(200, "text/html; charset=utf-8", len(body))
            return self.wfile.write(body)
        if self.path in WEB_ROUTES:
            filename, mime = WEB_ROUTES[self.path]
            body = (WEB / filename).read_bytes()
            self._headers(200, mime, len(body))
            return self.wfile.write(body)
        if not TOKEN or not secrets.compare_digest(self.headers.get("Authorization", ""), "Bearer " + TOKEN):
            return self._json(401, {"error": "unauthorized"})
        if self.path == "/api/v1/device":
            return self._json(200, {"product": "S Device One", "os": "Android-based S Device UX", "phase": "Build 011", "features": ["launcher-foundation", "local-api", "projector-dashboard"]})
        return self._json(404, {"error": "not_found"})

    def do_POST(self):
        if not TOKEN or not secrets.compare_digest(self.headers.get("Authorization", ""), "Bearer " + TOKEN):
            return self._json(401, {"error": "unauthorized"})
        return self._json(501, {"error": "not_implemented"})

if __name__ == "__main__":
    if not TOKEN or len(TOKEN) < 24:
        raise SystemExit("Set SDEVICE_TOKEN to a random secret of at least 24 characters")
    if HOST not in ("127.0.0.1", "localhost", "::1"):
        raise SystemExit("Build 008 is local-only. Do not expose before authenticated HTTPS LAN design.")
    print(f"S Device PC-only UI: http://{HOST}:{PORT}/app/ (projector: /dashboard)", flush=True)
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
