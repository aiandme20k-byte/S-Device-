# S DEVICE — BUILD 007 REAL-PRODUCTION MASTER BASELINE
Date: 2026-10-15. Status: DESIGN BASELINE, NO PHYSICAL PROTOTYPE VALIDATED.
SETT X-1 is an illustrative source of recycled computing ideas, **not** this build's product designation.

## Product definition
S Device One is the existing working realme 13 5G running a reversible Android-based S Device experience, with an optional portable second projector display and optional desk mini prism display. Private services run on user's existing PC; Alex HSXI 4TB external drive is authoritative data storage with a separate verified backup. No Android firmware replacement at first.
Two visual outputs: (1) original 6-inch-class smartphone screen; (2) variable-size projected screen on a wall/screen. Actual size depends on throw distance, optics, ambient light and projector native resolution, not a free-space hologram. Voice control and optional camera gesture UI send permission-checked commands to the server.

## Device allocation
S-CORE: realme 13 5G working device. Do NOT disassemble.
S-DONOR: Samsung and Infinix old cracked devices, catalog for reuse as independent nodes, structural pieces and external modules only after tests. Never swap incompatible batteries or screens.
S-HOST: existing local computer, S Device API, AI adapter, status/control dashboards.
S-MASTER: Alex HSXI designated 4TB external HDD. Contains data, models, logs, evidence. It is NOT computer RAM or CPU. Separate backups necessary.

## Architecture
[Realme S Device APK] --authenticated private LAN HTTPS--> [API/Auth/Policy] --> [AI adapter, no secret in app]
                                   |--> [Device registry / digital twin / evidence]
                                   |--> [Projected web UI via PC HDMI or verified casting]
                                   |--> [optional ESP32 Wi-Fi display on isolated USB 5V]
[PC] --> [local SSD working storage] --> [4TB master HDD with checksum journal and backup]

## Minimum Viable Product (MVP)
M1: App home/dashboard, AI shortcut, Android standard phone functions retained, easy uninstall.
M2: authenticated local API, connection status, no open internet listening port.
M3: browser-based projector dashboard shown on PC; phone issues authorized screen/view commands.
M4: optional 5V USB prism mini display (optical illusion) showing read-only metrics; ESP32 commands restricted.
M5: portable mounts, cooling and cable management without housing surgery.

## Recycled hardware policy
Intact working boards as modules beat desoldering SoCs. Inventory ID, provenance, exterior photo, test voltages, measured power, thermal behavior, connector pinout, data sheet and pass status before integration.
Plastic/glass/stone substrates: only fully insulated low-voltage LED/touch experiments with pretested current limit; no mains voltage and no demonstration of CPU fabrication.

## Power reality and calculations
No independently reproduced self-running net-positive electrical output has been established from this project's QVE-ZPE/electric harmonic balancer concept. An LC harmonic resonator or balancer cannot supply sustained net energy without measured energy input. Therefore do not remove or bypass the approved Realme battery, BMS or charging circuitry.
Energy budget examples using assumptions, not measured device claims:
- Realme battery nominal 5000 mAh x assumed 3.85 V ≈ 19.25 Wh.
- At mean 2 W phone draw, ideal runtime ≈ 9.6 h before efficiency/reserves; at 4 W ≈ 4.8 h.
- Add an assumed 10 W projector: 19.25 Wh / (2+10) W ≈ 1.6 h in impossible ideal direct shared-supply case (not a wiring instruction). Thus projector needs own certified supply.
- Continuous phone 2 W and projector 10 W for 24 hours: 288 Wh/day. 1 year: 105.1 kWh, excluding power losses and standby. Lifetime without energy input impossible under known energy conservation.
- 20,000 mAh commercial USB power bank rated at 3.7 V ≈ 74 Wh nominal; at 75% overall usable transfer, ≈55.5 Wh; 10 W projector alone ≈5.6 h. Actual results depend on device and bank.
Research-only ZPE energy protocol: 2 calibrated independent input/output meters, full thermal power balance, conventional background controls, source-disconnected baseline, uncertainty, sham, hashes and third-party replication. Any claim of net output is HOLD until confirmed.

## Cost envelopes — THB planning only (verify supplier quotes)
- Software only with existing phone/PC: 0–500 out-of-pocket, excludes development labor/hosting.
- Useful second screen: 800–2500 for verified true HDMI/input projector plus cable/stand; extremely cheap YG300-class sellers may have low native pixel count, high latency, unsupported casting and misleading 1080p marketing.
- Separate USB 5V prism/ESP32 demo: 300–1000.
- Accessories case/stand/cables and isolation: 200–900.
- Safer portable run time: commercial power bank 500–1500 if not already available.
- Contingency 15–25%. Rough DIY total 1800–6500, excluding laptop, phone, developer labor, research-grade ZPE and custom optical hardware.
Before purchasing check projector **native resolution**, brightness ANSI lumens and actual HDMI compatibility; realme USB-C external video-out cannot be assumed. Prefer PC HDMI output or confirmed wireless casting with the projector.

## Prototype gating
G0 INVENTORY: photos, exact model, safety (battery swelling and damaged AC hardware stop).
G1 FUNCTION: Realme power, touch, USB and Wi-Fi checks recorded.
G2 SERVER: health endpoint + auth tests + encrypted LAN transport review.
G3 APP: Gradle build passes, APK installed, opens, phone calls unaffected.
G4 PROJECTOR: native-resolution check, PC HDMI dashboard, scaling/focus, brightness and power test.
G5 VOICE/CAMERA: active opt-in, recording indicator, explicit per-device authorization, no unauthorized camera surveillance.
G6 ENDURANCE: 30/120-minute thermal/power trial on real hardware, log observed W and degrees C.
G7 RELEASE: provenance, BOM, cost evidence, source revisions, SHA-256 hashes, rollback and reproducible test report.

## Current status
Documentation and starter Python/Android source in repository. No actual hardware deployment, projector purchase or validation is demonstrated. ZPE hardware not an accepted power source.
