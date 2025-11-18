# SolThrive Edge S1 — Wiring & Enclosure Layout  
**Version:** Draft v1.0  
**Device:** SolThrive Edge S1  
**Platform:** SolThrive Monitoring V1  

---

# 📦 1. Overview

This document defines the **physical hardware layout**, **wiring structure**, and **recommended enclosure design** for the SolThrive Edge S1 device.

The goal:

- Clean DIN-rail layout  
- Safe + installer-friendly wiring  
- Minimal noise/interference  
- Secure mounting inside an electrical environment  
- Realistic path toward a manufacturable S2/S3 enclosure  

---

# 🔌 2. Component List (S1 Hardware Stack)

| Component | Function | Mount | Notes |
|----------|----------|--------|-------|
| Acrel ADL200/300/400 | Energy meter | DIN rail | CT + voltage inputs |
| Raspberry Pi 4 | Edge compute | DIN rail base plate | Route USB downward |
| USB→RS485 Adapter | Modbus interface | USB port | Connects Pi ↔ meter |
| 2–3 CTs | Current sensing | Service panel | Routed to meter CT ports |
| Low-voltage wiring | Meter → Pi | DIN rail trunk | Twisted pair recommended |
| Surge Protector (optional) | Device protection | DIN rail | Strongly recommended |

---

# 🧩 3. High-Level Wiring Diagram

   ┌───────────────────────────────────┐
   │         Service Entrance Panel     │
   │                                     │
   │   L1  ────────┐                     │
   │                ├─── CT1 ──────────┐ │
   │   L2  ────────┘                   │ │
   │                                    │ │
   │    PV Feed ───── CT2 ─────────────┘ │
   └─────────────────────────────────────┘

                   ↓  CT Leads
                   ↓

    ┌────────────────────────────────────┐
    │         Acrel ADL-Series Meter     │
    │------------------------------------│
    │  CT1 → I1+/I1-                     │
    │  CT2 → I2+/I2-                     │
    │  (Optional CT3 for subload)        │
    │                                    │
    │  L1/L2 Voltage Sense Inputs        │
    │                                    │
    │  RS-485 A/B/GND                    │
    └────────────────────────────────────┘
                   |
                   |  RS-485 (A/B/GND)
                   v
    ┌────────────────────────────────────┐
    │         Raspberry Pi 4             │
    │------------------------------------│
    │ USB Port → USB↔RS485 Adapter       │
    │ Runs SolThrive Monitoring V1       │
    └────────────────────────────────────┘

# 🪛 4. DIN-Rail Layout (Recommended)

┌──────────────────────────────────────┐
│ Enclosure │
│ │
│ ┌───────────────────────────────┐ │
│ │ Acrel ADL Meter │ │
│ └───────────────────────────────┘ │
│ │
│ ┌───────────────────────────────┐ │
│ │ Raspberry Pi 4 │ │
│ │ + RS-485 USB Adapter │ │
│ └───────────────────────────────┘ │
│ │
│ ┌───────────────────────────────┐ │
│ │ Optional Surge Protector │ │
│ └───────────────────────────────┘ │
│ │
└──────────────────────────────────────┘

---

# 🔧 5. RS-485 Wiring (Meter ↔ Pi)

| Meter Terminal | Pi Connection |
|----------------|----------------|
| **A** | USB-RS485 A |
| **B** | USB-RS485 B |
| **GND** | USB-RS485 GND |

**Important notes:**

- Use **twisted pair** for A/B  
- Keep RS-485 lines away from AC power conductors  
- Keep cable ≤ 3 meters if possible  
- Avoid sharp bends  
- Add ferrite if electrical noise is present  

---

# ⚡ 6. CT Wiring (Panel → Meter)

### **CT Orientation**
- **Arrow → Load direction**  
- If reversed, readings flip sign (import/export swap)

### **Lead Polarity (if applicable):**
- White = I+  
- Black = I−  
- (Some CTs have non-polarity pairs — refer to CT spec sheet)

### **Routing Rules**
- Keep CT lead wires twisted  
- Keep away from high-voltage AC runs  
- Do not run CT wires parallel to 240V conductors  
- Tie-down CT wires inside panel  
- Use grommets if passing into the enclosure  

---

# 🧲 7. Enclosure Recommendation (S1)

### **Minimum requirements:**
- **DIN-rail carrier** (180–250mm recommended)
- **UL94-V0 plastic or metal enclosure**
- **Cable glands** for CT + RS485 entry
- **Ventilation slots** (because Pi generates heat)
- **Mounting flange** or wall-mount brackets
- **Strain relief** for low-voltage wires

### **Target Internal Dimensions (Draft)**

- Height: 180–250 mm
- Width: 120–180 mm
- Depth: 70–100 mm


This allows:

- 1 × Acrel meter  
- 1 × Raspberry Pi  
- RS485 adapter  
- Surge protector  
- Cable management space  
- Future expansion (LTE, PCB, etc.)

---

# 🛠 8. Safety Restrictions

- CT work must be done with **main power off**  
- Meter L1/L2 wiring should only be performed by a licensed electrician  
- Low-voltage RS-485 must be separated from high-voltage cabling  
- Use double-insulated conductors  
- All components should be UL-listed or equivalent  

---

# 📝 9. Installation Workflow (S1)

1. Mount DIN rail inside enclosure  
2. Snap-in Acrel meter  
3. Mount Raspberry Pi on DIN baseplate  
4. Install surge protector (optional but recommended)  
5. Terminate CT wiring inside the panel  
6. Route CT leads into enclosure  
7. Terminate CTs on I+/I− terminals  
8. Wire L1/L2 for voltage sense  
9. Connect RS-485 A/B/GND → USB adapter  
10. Power the Pi  
11. Run bench test procedure  
12. Run field test procedure  
13. Seal enclosure  

---

# 📎 10. Future Additions (for S2/S3)

- Custom PCB  
- Integrated RS-485 transceiver  
- Dedicated CT input block  
- Thermal management  
- Injection-molded enclosure  
- External LTE/WiFi antennas  
- Cable routing channels  
- Tool-free installation  

---

# ✔️ End of Document
