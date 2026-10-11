# BUILD 005 — S Device One: two donor phones, one finished handset

Decision (user, 2026-10-11): S-01 cracked Samsung and S-03 cracked Infinix are DONORS for ONE completed S Device handset. Realme 13 5G stays intact as software test/reference phone.

## Architectural choice
- Pick a single working, known-model phone mainboard with its OWN exact compatible display, battery, charging circuit, cameras, radios, buttons and antennas.
- Other donor can provide universal external accessories or cosmetically reusable materials after mechanical/electrical fit checks.
- NEVER splice Li-ion cells, connect dissimilar battery packs in parallel, interchange unknown screen FPCs, combine high-speed motherboard traces or graft unrelated charging circuitry.
- If both phones run, a second full phone may act as a separate Wi-Fi node, but that is not one motherboard or combined RAM/CPU and greatly increases thickness/complexity. Not chosen for budget v1.
- Reversible Android app/launcher for S Device UI, initially deployed on Realme test handset.
- Optional 5V independent ESP32 microdisplay and passive optical accessory after core device works.

## Component purchase gate
Do NOT order LCD/OLED, replacement glass, battery, flex parts or frame until exact Samsung SM model and Infinix X-model confirmed; Note 2 is only user guess.
Check boot/screen/touch, whether cracked *glass* vs failed display, whether display can be reused, battery safety and backups. Get all-side and About Phone model photos, redacting IMEI/serial.

## Shop/DIY delineation
DIY: non-invasive diagnosis, backup, app development/test, case sketches, low-voltage standalone display, assembly of non-battery accessories.
Specialist: glass-only LOCA/OCA delamination/lamination, precision display bonding, severely damaged Li-ion batteries or unknown adhesive/glass work.

## Build gates
005A Identify and choose main board
005B Confirm all needed replacement parts and exact compatibility
005C Function test at bench in safe original frame
005D Run S Device launcher on Realme then target
005E Mechanically mount in custom enclosure with antenna/thermal clearance
005F Verify calls, charge, radios, touch, cameras, temperatures, battery, user data security

This is a design plan, not evidence of working hardware.
