# S Device One — QVE HNS Future Technology
**Current implementation: BUILD 011 (2026-10-18). Latest 10-build checkpoint: BUILD 010.**

Working realme 13 5G stays the primary cellular Android phone (SIM, calls, SMS and drivers remain on stock Android). S Device is a custom Android OS **experience** and local-first platform, not a new flashed ROM. For iPhone/iPad, S Device shares the interface through a future securely hosted Safari PWA; no iOS kernel replacement. Projector is a separate future hardware output. The Samsung and Infinix cracked devices are experimental donors, not approved battery donors. SETT X-1 is a research example, not this product's name.

## Mandatory continuity at every Next
Read [Build 010 master checkpoint](docs/BUILD-010-MASTER-CHECKPOINT.md), [Current State](docs/CURRENT_STATE.md), [Next Build](docs/NEXT-BUILD.md) and the most recent implementation report. At Builds 020, 030, 040... audit all completed builds, changed hardware decisions, GitHub code, tests, costs and real verification evidence.

## Build 011 — Platform
- [Engineering implementation and SIM/iOS constraints](docs/BUILD-011-SIM-AND-CROSS-PLATFORM.md)
- [Android native app](android/) — QVE theme, read-only SIM/mobile data status, original dialer/SMS intents, **CI debug APK build PASS, physical Realme field test pending**.
- [Cross-platform browser interface](web/) — static QVE-branded Home/Network/AI/Devices PWA shell. On localhost PC; trusted HTTPS mobile deployment not done.
- [Local-only Python server](server/) — protected API, serves [PC dashboard](dashboard/) and web app; no LAN exposure.
- [Server CI](https://github.com/aiandme20k-byte/S-Device-/actions/workflows/server-tests.yml) and [Android CI](https://github.com/aiandme20k-byte/S-Device-/actions/workflows/android-build.yml).

**CI evidence (Build 011):** [Python server PASS](https://github.com/aiandme20k-byte/S-Device-/actions/runs/39076662664) · [Android debug APK build PASS](https://github.com/aiandme20k-byte/S-Device-/actions/runs/39077274157). Debug APK artifact is attached to the Android run and expires 2026-10-24 UTC. Not a production signing certificate or completed installation.\n\n## Engineering baseline
[Build 007 Production Master](docs/BUILD-007-PRODUCTION-MASTER.md) · [BOM](docs/BUILD-007-BOM-REGISTER.csv) · [Acceptance Gates](docs/BUILD-007-ACCEPTANCE.csv) · [Shopping & DIY](docs/BUILD-007-SHOP-AND-DIY.md) · [Roadmap 010–030](docs/ROADMAP-010-030.md).

## Validation truths
Source code and CI are not final product verification. Unverified: user's Realme install, SIM/4G/5G performance, iOS deployment, model inference, projector, external ESP32, 4TB drive integration, commercial compliance and ZPE power production. QVE-ZPE indefinite energy is experimental/unverified; the phone must retain original certified battery and safely powered accessories.

**Privacy:** No secrets, IMEI, SIM identifiers, personal pictures, raw mic/camera footage or phone numbers in public GitHub. Do not expose server port; approved remote cellular services need HTTPS plus explicit pairing. Preserve SHA-256 evidence and STOP/HOLD on safety issues.
