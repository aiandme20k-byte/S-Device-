# Build 008 — Dual-Screen Vision Console
Status: source committed; hardware and real-PC PASS pending.

## Result delivered
- dashboard/index.html: responsive dark/cyan fullscreen browser dashboard.
- server/sdevice_server.py: local-only standard library web server; /dashboard and /health, plus bearer-protected /api/v1/device.
- server/test_server.py and GitHub workflow: automated HTTP tests.

## Test on Windows PC
1. Install Python 3.10+; download/clone latest S-Device- repo.
2. Open PowerShell inside repository:
```powershell
$env:SDEVICE_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
python -m unittest discover -s server -p "test_*.py" -v
python server/sdevice_server.py
```
3. Open http://127.0.0.1:8765/dashboard in PC browser.
4. Click Fullscreen; choose external monitor or actual HDMI projector once available.
5. Observe LOCAL ONLINE and timestamp. Save non-private screenshot as evidence.

## Acceptance
- API tests GREEN on CI, Android app still needs independent APK build.
- Dashboard HTTP 200, status online.
- No internet exposure; cannot be accessed directly by Realme yet. Planned HTTPS pairing next.
- Device audio/hand gesture/AI and real projection are future work, not simulated PASS.
- Power remains Realme stock certified battery and separately protected projector supply.
- Do not buy a star/nebula light for text projection or assume YG300 native resolution.
