# BUILD 007 — Integrated SETT X-1 / S Device engineering baseline

Date: 2026-10-15. Status: DESIGN BASELINE — no fabricated prototype or validated experimental energy source.

## User requirements
- Salvage-first: identify/test available old equipment before purchasing.
- Main handset: working Realme 13 5G, Android-based S Device interface (no iOS binaries or unsafe ROM flashing).
- Separate desktop SETT X-1 recycled computing module and 4 TB Alex HSXI master storage.
- Dual display modes: original handset screen; adjustable projected big screen.
- Private local server, services, AI, voice, camera/gesture controls, digital twin, testing and evidence.
- Explore harmonic energy and QVE/ZPE as an experimentally unverified R&D track, **not** a power supply dependency.
- Accessibility and affordability, clear low-cost BOM, staged acceptance.

## Evidence observed from user photographs
- Realme About Device: Realme 13 5G, Dimensity 6300, 12 GB displayed RAM + expansion and 256 GB storage. Software and battery health not independently verified.
- Loose donor phone internals (at least two phones), 2-fan cooling stand, USB cables, red portable external drive marked Portable SSD, small red USB device, audio microphone, USB/power adapters, metal watch, soldering iron, optical concept pictures.
- Do not assume batteries are safe, USB storage capacity is exactly 4 TB, fans are electrically compatible, or adapters have known output ratings until read and measured.
- QVE Future Glass artwork and hologram photos are concepts/demonstrations, not validated free-space projection technology.

## Architecture
Realme Android S Device app <- WiFi / authenticated TLS -> SETT X-1 PC local service
SETT X-1 API <-> AI model provider/local inference, device registry, digital twin, telemetry and controlled work queue.
4 TB master drive stores versioned models, logs, evidence and user-owned files; use backups, integrity manifests and full disk encryption.
Projector: external independently powered HDMI/Wi-Fi unit driven by PC; alternatively Android supported casting. Confirm compatibility before purchase.
Mini optical prism display: separately powered 5 V ESP32 demonstration. No direct battery or display-flex interfacing.

## Power subsystem: no unsupported free energy claims
A phone battery rated 5000 mAh at nominal 3.85 V is roughly 19.25 Wh (illustrative, not measured).
At average 2 W -> approx 9.6 h; at 5 W -> approx 3.9 h, ignoring losses and degradation.
If a 5 W device must run 24h/day for 365 days, energy required = 43.8 kWh/year, before losses. A lifetime single-charge claim cannot be supported by harmonic balancing. Harmonic resonance/energy storage can condition energy, not generate net energy from nothing.
No ZPE converter is validated. Keep stock manufacturer battery/charging system and separately investigate any source via independently calibrated input/output energy, thermal balance, off/on/sham, blank/control, uncertainty and replication.
Never substitute experimental ZPE circuit for lithium battery or connect homemade mains power supply directly to smartphone.

## Build gates
G0: PHOTO INVENTORY / device and adapter label identification / lithium hazard screen.
G1: SAFETY + STORAGE: verify adapter specs, backup and drive health; distinguish HDD vs SSD and document measured capacity.
G2: SOFTWARE: local API tests, Android apk build/test on Realme, verified opt-in device access.
G3: DISPLAY A: native smartphone dashboard, touch, voice.
G4: DISPLAY B: PC-hosted full-screen projector dashboard; tune image size using distance/zoom, not claimed holography.
G5: ESP32 demo: optional USB-powered prism mini panel, off-phone.
G6: BENCH VALIDATION: usability, Wi-Fi reconnect, 30-min burn-in temperature logging, controlled permission tests, no unapproved access, evidence files.
G7: custom enclosure: mounting, antenna, airflow, strain relief, verified safe USB power, re-test.
G8: acceptance / controlled release (not mass-production certified).

## Provisional purchase budget (THB, not live quotations)
Core free reuse (existing phone+PC+drive): 0-300 consumables.
Basic projector/casting cables and mount: 700-2,000.
Optional mini ESP32 optical desk module: 350-1,000.
Enclosure/fasteners/straps/strain relief: 150-600.
Spare safe 5 V USB power adaptor/power bank: 200-700 when required.
Total staged DIY target: 1,400-4,600 incremental THB. Excludes skilled labor, faulty parts, AI usage, connectivity and full professional product certification.
Do not place orders until inventory and verified ports/rating review.

## PASS / HOLD rules
PASS requires exact model/part identity, safe power, repeatable operation and timestamped evidence.
HOLD if unknown mains wiring, swollen cells, hot smell, exposed contacts, adapter mismatch, input/output power data missing, unsafe internet access or unverifiable power claim.
Do not upload personal files, serials, IMEIs, credentials or private photos to a public repository.

## Next immediate actionable step
With all devices unplugged, photograph power-supply rating labels, USB/HDMI ports, and storage model label with serial masked. List existing multimeter, available monitor/projector and computer operating system. Then select a zero-purchase dashboard demo; no battery disassembly or mains opening.
