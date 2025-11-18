# SolThrive Edge S1 — Bill of Materials (BOM)
**Version:** Draft v1.0  
**Device:** SolThrive Edge S1  
**Platform:** SolThrive Monitoring V1  

This Bill of Materials (BOM) lists all components required to assemble the SolThrive Edge S1 hardware device for bench testing, field deployment, or early pilot installations.

---

# 📦 1. Core Components

| Item | Part / Model | Qty | Est. Cost | Notes |
|------|--------------|-----|-----------|-------|
| Raspberry Pi 4 Model B | 4GB or 8GB RAM | 1 | $55–$75 | Core compute module |
| MicroSD Card | 32–64 GB, Class 10 | 1 | $8–$15 | OS + firmware |
| RS-485 USB Adapter | FTDI/CH340/CP2102-based | 1 | $8–$18 | Pi ↔ meter communication |
| Acrel ADL-series Meter | ADL200 / ADL300 / ADL400 | 1 | $55–$90 | Modbus-enabled meter |
| Split-core CTs | 100A–200A, 26–36mm | 2–3 | $8–$20 each | Whole-home & PV CTs |

---

# 🔌 2. Wiring & Connectivity

| Item | Specification | Qty | Est. Cost | Notes |
|-------|---------------|-----|-----------|-------|
| RS-485 Cable | Twisted-pair, shielded | 1–2m | $4–$8 | A/B/GND wiring |
| Low-voltage wire | 18–22 AWG | As needed | $2–$5 | Meter ↔ Pi wiring |
| CT Cable Extensions | Shielded | Optional | $4–$12 | Depends on panel distance |
| Cable Glands | M16 / M20 | 2–3 | $2–$8 | Enclosure cable entry |
| Wire Ferrules | Assorted | 1 set | $5–$10 | For neat terminations |
| Heat Shrink Tubing | 2–4mm | Assorted | $3–$7 | Wire sealing & protection |

---

# 🛠 3. Enclosure & Mounting Hardware

| Item | Specification | Qty | Est. Cost | Notes |
|------|--------------|-----|-----------|-------|
| DIN Rail (35mm) | 150–250mm length | 1 | $4–$7 | Internal mounting |
| Enclosure | DIN-friendly, UL94-V0 rated | 1 | $18–$35 | Polycase, Bud, Hammond, etc. |
| Mounting Plate | For Pi & RS-485 | 1 | $5–$10 | Can be 3D printed |
| Standoffs (nylon/metal) | M2.5 (Pi), assorted for accessories | 8–12 | $3–$6 | Mounting Pi + extras |
| Ventilation Insert | Passive vent slots | Optional | $2–$5 | Helps Pi cooling |
| Adhesive Cable Clips | 3M backed | 4–6 | $3–$6 | Internal cable management |

---

# ⚡ 4. Power Components

| Item | Specification | Qty | Est. Cost | Notes |
|------|--------------|-----|-----------|-------|
| Raspberry Pi Power Supply | 5V, 3A USB-C | 1 | $8–$12 | Official recommended |
| Surge Protector | DIN mount | Optional | $10–$18 | For sensitive installs |
| Terminal Blocks | DIN terminal block | 2–3 | $3–$8 | For neat terminations |
| Grounding Lug | Panel ground | Optional | $2–$4 | Depending on jurisdiction |

---

# 🧪 5. Assembly Tools (Not included in BOM but required)

| Tool | Purpose |
|------|---------|
| Screwdrivers | Meter terminals, enclosure mounting |
| Wire stripper/cutter | Low-voltage prep |
| Ferrule crimper | Clean RS-485 + CT terminations |
| Drill + step bit | Cable gland openings |
| Multimeter | Basic verification |
| Laptop | Pi setup |

---

# 🧩 6. Device Variants (Future-Proofing)

### **S1 (current)**
- Pi-based  
- Acrel meter  
- External CTs  
- DIN rail + enclosure  

### **S2 (future target)**
- Custom PCB  
- Integrated RS-485  
- Direct CT inputs  
- Optional 4G/WiFi module  
- Thermal-optimized enclosure  

### **S3 (long-term)**
- Fully integrated device  
- Cloud-native gateway  
- Professional-grade exterior  
- Installer ecosystem support  

---

# 🎯 7. Estimated Cost Breakdown (S1 Prototype Build)

| Category | Estimated Cost |
|----------|----------------|
| Compute (Pi + SD + USB–RS485) | ~$75–$95 |
| Meter + CTs | ~$80–$120 |
| Enclosure + DIN hardware | ~$25–$45 |
| Wiring + accessories | ~$10–$25 |
| **Total Estimated Cost (Prototype)** | **$190–$285** |

Production costs drop significantly when moving to a custom PCB (S2).

---

# ✔️ End of Document

