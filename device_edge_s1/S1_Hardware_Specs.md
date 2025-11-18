# SolThrive Edge S1 — Hardware Specifications

## 🧩 Hardware Architecture

The SolThrive Edge S1 is composed of:

- Raspberry Pi 4 Model B (recommended)
- USB → RS-485 adapter
- Acrel ADL200/300/400-series energy meter
- 2–3 split-core CTs
- DIN-rail mount components
- Low-voltage wiring harness
- Surge protection (optional)

---

## 🔌 Electrical Requirements

### **Input Power**
- 5V DC for Raspberry Pi  
- Typical: 3A minimum  
- Clean power strongly recommended

### **Meter Power**
- 100–240V AC depending on model  
- Provided directly from the panel

---

## 🔗 Interfaces

| Component | Interface | Purpose |
|----------|-----------|---------|
| Raspberry Pi | USB | RS-485 communication |
| Acrel Meter | RS-485 (Modbus RTU) | Real-time energy data |
| CTs | Dedicated meter CT ports | Current measurement |

---

## 🧭 Supported Sensors (CTs)

- Split-core  
- 100A–200A  
- 26mm–36mm opening  
- 333mV or meter-native type

(Aligned with `/docs/A1_CT_Specs.md`)

---

## 📐 Physical Layout (Draft)

**DIN Rail Layout:**

┌─────────────────────────────┐
│ Acrel Meter (ADL-series)    │
├─────────────────────────────┤
│ Raspberry Pi + RS485 Module │
├─────────────────────────────┤
│ Cable Mgmt / Power          │
└─────────────────────────────┘


A full enclosure diagram will be added during S1 mechanical design.

---

## 🧪 Bench Test Compatibility

Compatible with:

- `/test/bench_test_procedure.md`
- `/test/field_test_procedure.md`

Testing includes:
- CT orientation validation  
- Voltage + current scaling  
- Real-time polling stability  
- API verification  

