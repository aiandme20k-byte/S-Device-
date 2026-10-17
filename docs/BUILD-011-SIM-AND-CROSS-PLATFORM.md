# S DEVICE — BUILD 011: SIM INTERNET + CROSS-PLATFORM EXPERIENCE
Date: 2026-10-18. Implemented in source; physical tests pending.

## Scope and rules
- Main phone remains working Realme 13 5G, with stock Realme Android modem, carrier SIM, Wi-Fi, Android telephony & secure boot in control. S Device is the application/launcher experience, **not** replacement Android firmware.
- iPhone/iPad must retain Apple iOS. S Device runs as web app/PWA on supported Safari via an approved HTTPS origin, and a future signed iOS app could be built. iOS telephony internals, calls/SMS APIs and home launcher replacement are not generally accessible to third-party apps.
- PC/Linux/Windows browser shows the same UI (local web server); projector via PC HDMI or tested supported casting. A real phone USB-C projector video-out is NOT assumed to work.
- No new GSM modem/antenna/SIM circuit is required in Realme; optional Raspberry Pi with Quectel/SIM7600 would be a **separate** product, requiring certified modem board/antenna, local bands, operator tests and voice/SMS support verification.

## Repository changes
- Android 0.2.0: MainActivity displays SIM ready/missing/locked state and observes ConnectivityManager active network (Wi-Fi, Cellular, Ethernet/other); shows Android-validated vs unvalidated connectivity. It launches stock Phone dialer and SMS client through safe Android Intent commands. Uses only ACCESS_NETWORK_STATE; does not read IMEI, SIM identifiers, phone numbers, message content or carrier secrets.
- Web: `web/index.html` responsive QVE-branded Home/Network/AI/Devices browser shell. `web/manifest.webmanifest`, `web/sw.js`, `web/icon.svg` provide a minimal PWA shell and offline fallback only for known static assets. No real AI inference or carrier modem control.
- Python: `/app/`, `/app/sw.js`, `/app/icon.svg`, `/app/manifest.webmanifest` served on local-only 127.0.0.1. Existing `/dashboard`, `/health` and bearer-secured API retained. Referrer, frame and Permissions-Policy response headers added.
- Server tests: health, dashboard, PWA files, auth status and POST rejection.
- Android CI: workflows include an SDK/Gradle compile attempt and debug APK artifact if successful. This is NOT an app-store release.

## How to validate in steps
1. On Realme, safely insert working carrier nano-SIM (do not force tray; confirm correct size/orientation), enable Mobile Data, confirm carrier subscription and coverage.
2. Verify **stock Android** can browse via cellular with Wi-Fi disabled; then try a call and SMS in its own apps. Avoid any private number in public screenshots.
3. Build S Device native APK with Android Studio or CI, install on Realme using normal developer/debug process, launch and verify SIM READY, CELLULAR DATA when used, and Android-validated connection. Restore Wi-Fi and verify it becomes WIFI. Note: simState readiness is NOT proof of active subscription, and active transport is not a certified 4G vs 5G radio-tech reading.
4. Run `python -m unittest discover -s server -p "test_*.py" -v`; set `SDEVICE_TOKEN` (24+ random characters), then `python server/sdevice_server.py`. Open `http://127.0.0.1:8765/app/` on SAME PC; projector console `/dashboard`. Do not change SDEVICE_HOST to a LAN/public interface.
5. The local URL will not open from your Realme/iPhone over cellular. Connecting remotely requires a future mutually authenticated HTTPS deployment/pairing, not simply port-forwarding.
6. After trusted HTTPS pairing is implemented, test S Device web app in Android Chrome and iOS Safari; iOS browser-only capabilities and Add to Home Screen depend on Safari/iOS versions and suitable app icons. Keep native call/SMS separate.

## Current gating
- Python GitHub CI: PASS confirmed (run 39076662664) after Build 011 routes and tests.
- Native Android debug APK compile: PASS at GitHub Actions run 39077274157, commit cdb631cacb9f034117be5665aa0e4ffe0d8fb348. Artifact `s-device-build011-debug-apk` uploaded (ID 12117139134, expires 2026-10-24 UTC). ZIP artifact sha256 from GitHub: `2f6047bb3aa1090bce81f0f0044d0d3f64e7e4a2dc0f55120ebddbd4ef4049eb` (ZIP digest, **not** verified standalone APK SHA-256). Initial Android CI failures resolved: obsolete `tools` SDK package in action defaults; then Java bytecode 1.8 vs Kotlin JVM 17 mismatch. Build success does NOT verify phone installation.
- SIM hardware/cellular/voice/SMS on the Realme: HOLD — no physical measurements.
- iOS Safari functional deployment: HOLD — no HTTPS hosting, app icon not optimized for iOS.
- Real-time AI data over SIM: HOLD — secure remote service not connected.
- Local AI model inference, projector, 4TB link, QVE pixel logo, custom holograms, batteryless ZPE: HOLD.
No automatic calls or texts, camera access, paid mobile data use, or unauthorized remote access performed.

## Next Build 012
Fix Android compile errors (if any), retrieve and install debug APK, compare SIM+cellular state to Android Settings; keep phone data private. Build HTTPS pairing separately at build 014.
