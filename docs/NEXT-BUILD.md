# Next action: BUILD 011 — Test the baseline, do not add speculative features first
1. Fetch server/sdevice_server.py, dashboard/index.html, server/test_server.py and workflow definition.
2. Execute Python unittest and verify /health, dashboard, unauthorized 401, authenticated device data.
3. Inspect GitHub Actions latest run or state that it could not be verified.
4. Resolve broken relative file paths, Windows/PowerShell compatibility and network isolation.
5. Capture tool output and commit hash without exposing credentials.
6. Mark G2 PARTIAL until a real user-PC runtime test and HTTPS LAN implementation.
7. Update CURRENT_STATE.md and add BUILD-011 test report. Preserve 010 snapshot for continuity.
No hardware purchase or physical wiring at this stage.
