A2 — Energy Meter Selection**

**SolThrive Monitoring V1 — Enhanced Engineering Edition**

---

## **1. Purpose**

This document defines the engineering requirements and selection criteria for the **3-channel Modbus energy meter** used in SolThrive Monitoring V1.

This meter performs all electrical measurement functions:

* Reads **current** from 3 CTs
* Measures **voltage** on L1 and L2
* Calculates **power** and **energy**
* Provides all data over **Modbus RTU (RS-485)** to the Raspberry Pi

Choosing the correct meter ensures accurate readings, safe operation, and compatibility with the SolThrive V1 software stack.

---

## **2. Functional Requirements**

The meter must support:

### ✔ **1. Split-phase 120/240V Residential Power**

* L1 and L2 voltage measurement
* Single-phase, 3-channel current monitoring

### ✔ **2. Three Independent CT Inputs**

For reading:

* **Main L1**
* **Main L2**
* **PV backfeed breaker**

Each CT channel must accept:

* 20–200A CTs
* CTs **with burden resistors built in**
* 1% accuracy or better

### ✔ **3. RS-485 / Modbus RTU Support**

Required features:

* Modbus RTU (function codes 0x03, 0x04)
* Configurable baud rate (9600 recommended for V1)
* Stable polling at 1–5 seconds

### ✔ **4. Provides Specific Mandatory Registers**

The meter **must** expose registers for:

* Voltage L1/L2
* Current CT1/CT2/CT3
* Active power (total + per phase)
* Import kWh
* Export kWh

(See **A4 — Modbus Register Map** for details.)

### ✔ **5. DIN-Rail Mountable**

To ensure safe installation and clean wiring layout.

---

## **3. Recommended Meter Models (Validated for V1)**

SolThrive V1 uses compact, affordable industrial meters that meet the above requirements.

### **Primary Recommendation**

#### **Acrel ADL400-CT**

* 3-channel CT inputs
* Split-phase compatible
* 1% accuracy
* Native RS-485
* DIN-rail enclosure
* Widely used in residential and light commercial monitoring

Reliable, accurate, and easy to integrate with Modbus.

### **Alternate Options**

#### **Eastron SDM230 / SDM630 Series**

* Strong Modbus support
* Good accuracy
* DIN-rail
* Slightly more expensive
* Multi-phase variants available for future V2

#### **DTSU666 / DDSU666 (Huawei-style)**

* Good Modbus implementation
* Usually tied to OEM systems
* Documentation varies by vendor

---

## **4. CT Compatibility Requirements**

Any meter selected **must support external CTs** with:

* **1% accuracy**
* **20–200A range** depending on channel
* **Built-in burden resistors**
* **Split-core mechanical design**

This ensures correct pairing with A1 CT specifications.

---

## **5. Electrical Requirements**

### **Voltage Input**

* 120/240V split-phase
* Direct voltage sensing terminals
* Category III rated

### **Current Channels**

* 3 independent channels
* Accept CTs via screw terminals
* Must support correct scaling (Amps × 100, etc.)

### **Isolation**

* Optical or galvanic RS-485 isolation preferred
* Reduces noise and ground loop issues

---

## **6. Modbus Requirements**

The meter must provide a **minimal register set** required by the SolThrive V1 poller:

| Category         | Needed Registers        |
| ---------------- | ----------------------- |
| **Voltage**      | L1, L2                  |
| **Current**      | CT1, CT2, CT3           |
| **Active Power** | Total, L1, L2, PV       |
| **Energy**       | Import kWh, Export kWh  |
| **Optional**     | Power factor, frequency |

SolThrive software expects:

* 16-bit and 32-bit numeric registers
* Integer scaling (÷10, ÷100)
* Stable response within 100–200ms

(Full details in **A4 — Modbus Register Map**.)

---

## **7. Installation & Physical Requirements**

### **DIN-Rail Mountable**

The meter must:

* Fit standard 35mm rail
* Support field wiring access
* Provide front panel display (optional)

### **Terminals**

* Screw terminals capable of secure ferrule connections
* Clearly labeled:

  * A / B RS-485
  * L1 / L2 voltage
  * CT1 / CT2 / CT3

### **Enclosure Considerations**

Meter must be installed in:

* A dedicated auxiliary enclosure **or**
* Equipment room backboard
* **Not** inside the main panel

---

## **8. Meter Selection Decision Tree**

```
Is the system split-phase 120/240V?
   │
   ├── No → Choose multi-phase meter (V2/V3)
   │
   └── Yes
         │
         ├── Do you need three CT channels?
         │       │
         │       ├── No → 1-channel meter inappropriate for SolThrive
         │       └── Yes
         │
         ├── Does meter support Modbus RTU via RS-485?
         │       │
         │       └── No → Reject
         │
         ├── Does meter expose required registers?
         │       │
         │       └── No → Reject
         │
         └── Acceptable (Acrel ADL400-CT recommended)
```

---

## **9. Why the Acrel ADL400-CT Fits SolThrive V1**

* Compact DIN-rail format
* 3 channel CT measurement
* Stable Modbus RTU protocol
* Proven accuracy in residential loads
* Strong compatibility with RS-485 → USB adapters
* Known register mapping (A4)

This meter provides the best mix of cost, accuracy, and developer friendliness.

---

## **10. Summary (A2 Complete)**

To qualify for SolThrive V1:

✔ 3 CT channels (main L1, main L2, PV)
✔ Split-phase 120/240V support
✔ True RMS measurement
✔ RS-485 Modbus RTU
✔ Integer-scaled voltage/current/power registers
✔ DIN-rail mount
✔ Works with CTs defined in **A1**

**Recommended Model: Acrel ADL400-CT**
Reliable, accurate, and perfectly aligned with all other V1 hardware and software components.

---
