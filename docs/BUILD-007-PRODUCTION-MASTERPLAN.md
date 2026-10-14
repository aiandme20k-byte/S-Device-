# BUILD 007 — S Device / SETT X-1 Recycled Future Computing Master Plan
Date: 2026-10-15. State: DESIGN BASELINE (NOT manufactured/verified).

## Requirements
- Keep working Realme 13 5G intact as the primary S Device Android UX/controller.
- Reuse broken Samsung/Infinix devices only after model, connector, thermal and battery safety verification; prefer complete devices as independent network nodes.
- SETT X-1 optional desktop recycled compute/sensor/display module, not equivalent to the smartphone.
- Alex HSXI 4 TB master disk: authoritative store for logs/models/research evidence, mounted and backed up on user's local PC; actual hardware paths not verified.
- Project visualization includes (A) native smartphone display (B) external projector with adjustable image size using throw distance/focus and compatible HDMI/casting.
- Voice assistant, on-device permissioned camera gesture detection, dashboard and independent manual override.
- Glass/plastic/stone conductive substrate projects limited to insulated **low-voltage research signal circuits**. Do not claim chip fabrication or conductive stone.

## Block diagram
Realme (Android S Device app/UI, mic/camera permissions) -- authenticated TLS on LAN --> S Device local API (PC) --> Alex HSXI adapters --> master drive and local AI.
PC browser dashboard -> HDMI projector or confirmed compatible wireless casting receiver.
Optional ESP32-S3 + LCD acrylic prism display -> independent protected 5V USB power -> authenticated status endpoint (no raw secrets stored in firmware).
QVE ZPE/QED experiment -> electrically isolated test bench/metrology; NO power connection to phone or existing hardware until net-energy claims pass evidence gate.

## Energy budget / physical limits
Energy conservation: continuously consuming electrical power requires an independently measured input or finite stored energy. Resonance/harmonic balancing does not create energy.
Example illustrative load: phone 2–6 W typical operation (device/workload-dependent), projector 10–60 W (model-dependent), ESP32+LCD 1–4 W, PC 30–150 W. For a hypothetical 20 W load for 24h = 480 Wh/day. 5000mAh at nominal 3.85V corresponds to ~19.25Wh nameplate, without aging/conversion losses. Actual battery life must be measured and will be shorter with major peripherals.
A tiny ZPE module capable of replacing batteries or indefinite operation has no verified basis. Never advertise lifetime charge as achieved.
Near-batteryless user experience possible when connected to a safe external USB-C PD adapter (device still uses its battery and designed power circuitry) or fixed mains-powered projector/PC. Solar harvesting requires sized photovoltaic cells, regulators and storage for intermittent supply and cannot guarantee always-on.
Energy acceptance: independently measure voltage/current/input power, stored-energy changes, instrument calibration, sham and source-disconnected baselines, calorimetry where appropriate, uncertainty analysis and independent replication; no overunity claim without reproducible measurements.

## Prototype stages
A: inventory photographs and power-off visual checks; log part IDs, condition, and provenance.
B: reversible Android app -> signed APK build -> Realme smoke tests.
C: local server health/auth tests -> secure LAN access -> video/dashboard in browser.
D: existing projector/borrowed projector compatibility test; define brightness/throw/input and beam safety (avoid eyes).
E: ESP32 LCD prism standalone 5V bench demo with independent supply and guards, no salvaged Li-ion direct wiring.
F: salvaged materials experiments (glass, plastic, stone) using 3.3V/5V current-limited supply, continuity/resistance, substrate isolation, no batteries as raw power sources.
G: digital twin and sensor health, serial IDs, evidence logs, SHA256 checksum of records, calibrated instruments.
H: integrated prototype acceptance report, thermal/charging/runtime/privacy verification.

## Minimum purchase gate
Buy NOTHING new initially. Inventory available phone/PC/4 TB disk, cables, USB supply, fan, multimeter access and monitor/TV first.
Optional later: protected 5V ESP32-S3 LCD, acrylic optical prism, HDMI mini projector with verifiable native resolution and compatible inputs, USB microphone/webcam only if existing Realme insufficient.

## Cost guidance (Thailand, very preliminary not a quote)
Reversible software/basic test: THB 0–500 excluding time/internet/electricity.
External DIY desk display/LED: THB 300–1200.
Projector/HDMI/casting: THB 800–4000+ depending on actual brightness/native resolution.
Full practical demo using existing phone/PC: THB 1500–7000+ excluding professional labor/cloud subscription.
True volumetric hologram or independent batteryless power module: not part of the above budget / not demonstrated.

## Distinct verification statuses
VERIFIED: user images of working Realme screen and old hardware materials; repository code uploaded.
NOT VERIFIED: runtime Android APK installation, server running on local PC, connected master disk, hardware function tests, energy tests, displays.
RESEARCH: glass/plastic/stone circuit substrates, QVE/ZPE; never sell unsupported performance claims.

## Next hands-on instruction
Photograph physical inventory arranged on a safe nonconductive surface with AC adapters unplugged; record Realme functioning and HDD/PC interfaces. Do not probe live phone battery or disassemble mains AC supplies. Mark inventory PASS/HOLD. Then run local API tests and first Android build.
