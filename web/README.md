# S Device Web Shell
Build 011 code is an offline-capable app-shell demo. Run it only via Python localhost server on the same PC (`http://127.0.0.1:8765/app/`). For mobile/iOS installation use a later user-approved secure HTTPS host, HTTPS authentication and privacy audit. There is NO SIM API in the browser. Browser navigator.onLine is only an approximate indication of connectivity. Projector dashboard is `/dashboard`.
For a local PC test (Python 3.10+):
```powershell
$env:SDEVICE_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
python -m unittest discover -s server -p "test_*.py" -v
python server/sdevice_server.py
```
Do not expose 8765 on your LAN or internet; the server is deliberately loopback-only. No AI model, calls/SMS, phone permissions or private server pairing are active.
