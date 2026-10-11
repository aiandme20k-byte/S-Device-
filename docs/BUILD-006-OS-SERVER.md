# BUILD 006 — S Device OS + Private Server

## What is being built
Version 0.1: Android-based S Device user experience (launcher/app) connected to a private Python API service.
This is **not** a new kernel/ROM or an iOS installation. Stock Android remains responsible for telephony, radios, OTA security, drivers and app compatibility.

## Roles
- Realme 13 5G: Android test handset; do not root or flash.
- Infinix (model unconfirmed): possible future custom physical device.
- Local PC/SSD: service runtime and primary project data path. F:\\SETT_UNI is a Windows target path previously requested; not verified to exist in this runtime.
- Alex HSXI master storage: 4 TB external drive is designated as the authoritative long-term store by project policy; verify physical connection and backup before writing.
- GitHub: source/version control, not a secure database for secrets.

## System flow
Realme Android S Device app -> trusted LAN (later HTTPS) -> S Device API -> authorized AI adapters and Alex HSXI services -> SSD/master storage.

## Starter service
The minimal Python server exposes:
- GET /health: public on bind interface (no sensitive data).
- GET /api/v1/device: bearer-token restricted info.
No device management, personal-data collection, shell execution, AI inference, voice capture or cloud synchronization yet.

## Run on PC (PowerShell)
```powershell
cd F:\SETT_UNI\S-Device-\server
$env:SDEVICE_TOKEN = [Convert]::ToHexString([Security.Cryptography.RandomNumberGenerator]::GetBytes(24))
python .\sdevice_server.py
```
For older PowerShell/.NET environments, generate a random secret with Python instead:
```powershell
$env:SDEVICE_TOKEN = (python -c "import secrets; print(secrets.token_urlsafe(32))")
```
Check from same PC: http://127.0.0.1:8765/health

## Android connectivity later
The default bind 127.0.0.1 is *not* reachable from the Realme. Do not expose on 0.0.0.0 until local LAN address, router isolation, firewall, token storage and a secure HTTPS transport are specified and reviewed.
The Android client should never hardcode tokens into repository or APK.

## Security / evidence gates
1. Service starts locally and health check passes.
2. Incorrect/missing token returns HTTP 401.
3. Authorized device endpoint responds.
4. Android app build is signed for testing and manually installed.
5. After security review, allow authenticated access over protected LAN HTTPS.
6. No firmware flashing until exact-device driver and recovery validation.

## Test
```bash
python -m unittest discover -s server -p 'test_*.py'
```
Tests are supplied, not yet proven to have run on the user's computer.
