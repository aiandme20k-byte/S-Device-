# BUILD 012 — Android APK Build and Realme Field Test
**Precondition:** Read BUILD-010-MASTER-CHECKPOINT.md, BUILD-011-SIM-AND-CROSS-PLATFORM.md, CURRENT_STATE.md and recent CI logs. No assumption that test code means deployed OS.

1. Check GitHub Actions Android workflow conclusion; on failure read first relevant job log, correct build issues and rerun.
2. If debug APK artifact exists, verify APK version/name and hash; do NOT label it a signed consumer release.
3. Test Android app on Realme 13 5G without disassembly, backup first, enable developer options/USB debugging only during controlled install.
4. Test SIM state, Wi-Fi vs mobile data, Android-validated network, original dialer and SMS; compare Android Settings independently. No real calls or SMS sent without explicit user action.
5. Confirm permission manifest contains only ACCESS_NETWORK_STATE (no phone metadata, camera, mic or SMS read permissions).
6. Test app uninstall and recovery of normal Realme UI.
7. Keep cross-platform web app PC-only until approved HTTPS pairing; plan security Build 014.
8. Collect device-private PASS/HOLD checklist, measured values and SHA-256; do not publish IMEI, phone number or carrier account.
9. Update Current State and GitHub Build 012 report. Preserve prior checkpoint. Audit all at Build 020.
