# S DEVICE BUILD 010 — MASTER CHECKPOINT / SOURCE OF TRUTH
Checkpoint created 2026-10-15. Next mandatory reviews: 020, 030, 040 ... every 10 builds.
Purpose: read the full project context before each Next; never confuse an aspiration with a verified feature.

## 1. Mission and product identity
Build ONE S DEVICE initially using the user's working realme 13 5G with Android retained for core driver, calling and security support. S Device is a local-first Android UX + owned private services + AI and dual-screen Vision Control experience. SETT X-1 is a recycled technology example, NOT the product name.
The product should be useful to budget users: reuse spare materials before ordering anything. The user prefers actual design, code, installation instructions and photo → build → test → PASS/HOLD evidence, not generic speculation.

## 2. Devices, materials, storage
- Core phone: working realme 13 5G, shown in About screen (Dimensity 6300, 12 GB RAM plus virtual expansion, 256 GB storage, system-reported 5000 mAh typical battery; do not treat as measured power).
- Samsung blue broken glass and Infinix cracked phone: candidate recycled components / optional intact network nodes. Infinix was formerly planned as mainboard in Build 005 but was superseded by realme-primary decision in Builds 006–007. Do not use Build 005 as current hardware authority.
- Existing PC: local server and AI processing host.
- Windows desired root: F:\SETT_UNI, not remotely verified.
- Alex HSXI red 4 TB external HDD: designated master persistent knowledge/evidence storage, NOT compute. Require second backup and restore test.
- Images illustrate old phone boards, fans, USB tools, storage, chargers, cracked phones, and QVE concepts. Identify/test physical pieces before powering them.

## 3. What the user ultimately wants
A. S Device OS **experience** comparable in usability to Android/iOS, built as reversible launcher and apps before any firmware work. Android core stays until independently supported firmware can be proven.
B. Private services/API, local voice AI, screen/control dashboard, device registry/digital twin and memory link to Alex HSXI.
C. TWO outputs: the realme's existing touch display plus scalable projector image on wall/screen. Optional ESP32 + LCD + acrylic prism optical status display; no true free-space hologram claim.
D. JARVIS-inspired futuristic controls, opt-in camera gesture and voice, local security, action approvals for significant device operations.
E. QVE-HNS Future Technology brand, official logo where permission and image assets permit, dark navy / cyan / metallic gold, tagline QUANTUM • VISION • EXPLORATION, Authorized By SETT, footer EXPLORE • ENGINEER • CREATE • A BETTER TOMORROW; user photos never auto-published.
F. Distinct R&D: low-voltage transparent conductive glass, copper on plastic and stone substrates, recycled mechanical modules. Do not claim homemade dense CPU fabrication.
G. Aspirational long-life / batteryless QVE ZPE electricity: UNVERIFIED, not a power design or accepted production supply. Normal battery and separately protected USB/projector supply mandatory until reproducible calorimetric power evidence exists.

## 4. Build chronology and audit outcome
001: safety/diagnostic plan; documentation only.
002: chat-based DIY staging; no hardware demonstration.
003: phone roles documentation; superseded by realme-main decision.
004: multi-device identification and inventory.
005: Infinix mainboard donor project; SUPERSEDED for current MVP.
006: Python private API source and Android static Kotlin app skeleton; source uploaded, installation unverified.
007: realme-centered dual-output production master, BOM, cost/energy estimates, test gates; design not bench-validated.
008: local projector browser dashboard, updated server, tests and CI workflow; code staged, results unconfirmed.
009: QVE-brand text and colors in dashboard and Kotlin app, branding document; original binary logo not yet integrated.
010: present checkpoint and explicit 10-build audit process; no claim of device completion.

## 5. What exists vs what does NOT
EXISTS: GitHub source paths android/, server/, dashboard/, docs/; static Android starter app; local-only HTTP API and fullscreen web UI; test source; GitHub CI workflow definition.
NOT VERIFIED: successful Android Gradle build/APK on user's PC, realme install, API runtime on user's PC, projector purchase/output, encrypted LAN pairing, AI inference/voice/gesture, 4TB data link, proprietary logo asset integration, environmental endurance tests, ZPE output.
At each Next, log precise changed files, unit results, physical tests, open blockers. A source-code upload is NOT production PASS.

## 6. Safety, security, evidence
- Don't tap/swap cross-model batteries or screen connectors; do not use salvage power adapters without safety rating. No lithium DIY charging circuits. Do not expose the unfinished API to an external LAN.
- User explicitly authorizes their OWN systems and assets; never infer permission to read strangers' cameras. Require explicit consent and visual recording indicator.
- Do not put personal photos, raw camera footage, IMEI, tokens, credentials or phone numbers in the public repository.
- Ensure tests, exact measurements, provenance, SHA-256 evidence and acceptance gates. Use HOLD / UNKNOWN when physical proof is absent.
- Price estimates are rough Thai baht planning, not confirmed quotes.

## 7. Backlog Build 011–020 (planned not done)
011: verify Python server tests and CI, fix blockers, record outputs.
012: compile Android app using Gradle & SDK; unit/build logs; obtain signed debug APK.
013: create actual S Device home/launcher UI with reversible HOME selector and Android package queries limited to need.
014: private API HTTPS pairing and scoped credentials without repo secrets.
015: QVE asset catalog, hash/authorization of official emblem, optional private theme photos.
016: browser projection UI model and phone-to-PC authorized display control.
017: local AI voice opt-in MVP, failure states and privacy indicators.
018: optional gesture input prototype with bounded commands, permission test and no autonomous third-party camera access.
019: optional independent 5V USB ESP32 status cube + compatibility BOM (defer purchase until test).
020: complete 001–020 checkpoint: code/build/test/acceptance matrix, cost and power recomputation, risk register, update next 021–030.

## 8. Mandatory checkpoint after EVERY 10 builds
At build 010/020/030/...:
1. Read README, this master checkpoint, latest production master, previous checkpoint, roadmap, tests, GitHub code, and user decision log.
2. Resolve conflicts; newest confirmed user decision wins, archive old alternatives as superseded (never silently erase history).
3. Reconcile BOM, wiring, runtime architecture, 4TB storage path, permissions, safety, estimates and proof.
4. Run available local tests and fetch CI status; label PASS only with evidence.
5. Write CHECKPOINT-0NN.md, update CURRENT_STATE.md, NEXT-BUILD.md, ROADMAP.md and README.
6. Include what was intended / implemented / verified / failed / deferred, hashes and links.
7. Break release on missing critical evidence; report HOLD instead of claiming done.
This is a repository workflow requirement, not proof of automated background execution.
