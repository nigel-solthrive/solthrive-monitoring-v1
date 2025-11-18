SolThrive Monitoring V1 — Current Transformer (CT) Specifications

# #️⃣ **1. What CTs Actually Do**

A Current Transformer (CT) measures electrical current by detecting the magnetic field around a conductor.
It does **not** interrupt the wire — it simply clamps around it and outputs a small, safe signal for the meter to read.

Think of it as:

> **A stethoscope for electricity.**

---

# #️⃣ **2. Why CTs Matter in Solar Monitoring**

To measure real-world behavior, CTs provide:

* **Solar production** (PV backfeed breaker)
* **Home consumption** (main service legs L1 & L2)
* **Grid import/export** (computed from PV + consumption)

Without CTs, you only know inverter output — not full system behavior.

---

# #️⃣ **3. Split-Core vs Solid-Core CTs**

### ✔️ **Split-Core CTs (Recommended for V1)**

* Clamp-on design (no disconnecting conductors)
* Faster + safer for retrofit installs
* Slightly lower accuracy but perfect for home monitoring
* Ideal for SolThrive V1

### ✔️ **Solid-Core CTs**

* Wire must be removed and re-fed through
* High accuracy (0.1%)
* Not recommended for retrofits or field installs

**V1 Choice:** *Split-core CTs for all channels.*

---

# #️⃣ **4. CT Amp Ratings**

CTs must match the size of the conductor they clamp onto.

### **Recommended Ratings**

| Location       | Rating   | Purpose                 |
| -------------- | -------- | ----------------------- |
| **Main L1**    | 100–200A | Entire home load        |
| **Main L2**    | 100–200A | Same as above           |
| **PV Circuit** | 20–50A   | Solar inverter backfeed |

These support typical U.S. residential electrical systems.

---

# #️⃣ **5. CT Polarity**

CTs have direction indicators:

* Arrow, dot, or “K” marking
* Indicates the “source → load” direction

### **Correct Orientation**

* **Main CTs:** arrow **toward the panel loads**
* **PV CT:** arrow **toward the inverter**

If reversed, readings invert (export ↔ import).
We *can* fix this in software, but proper orientation is preferred.

---

# #️⃣ **6. CT Wiring (Leads → Meter Terminals)**

Most split-core CTs include two leads:

* **White = Positive (+)**
* **Black = Negative (–)**

### Typical meter terminal mapping:

* CT1 → `I1+ / I1−`
* CT2 → `I2+ / I2−`
* CT3 → `I3+ / I3−`

Your specific meter will list exact terminals.

---

# #️⃣ **7. Accuracy Class**

CT accuracy affects measurement quality.

Common classes:

* **1%** (standard, very good)
* **0.5%** (premium)
* **3%** (low-end; avoid)

**V1 Target Accuracy:**
✔️ **1% CTs** for all three channels

This meets professional monitoring standards.

---

# #️⃣ **8. CT Burden Resistors**

CTs require a “burden resistor” to convert current into a readable voltage.

### For V1:

**Use CTs with built-in burden resistors.**

Benefits:

* Safer
* Simpler wiring
* Compatible with most Modbus meters
* Zero risk of overvoltage

This is the industry standard for home monitoring.

---

# #️⃣ **9. CT Safety Notes**

Important installation guidelines:

* Clamp around **one** conductor only (L1 or L2 or PV hot)
* Never clamp around **hot + neutral together** (it cancels out)
* Keep hands/tools clear of live lugs
* If unsure: shut off main breaker
* Treat panels as energized even when “off”

Split-core CTs greatly reduce installation risk.

---

# #️⃣ **10. CT Placement (ASCII Diagrams)**

### **Main Service Conductors**

```
        [Utility Service]
               ↓
   ┌─────────────────────────┐
   │     Main Breaker        │
   │                         │
   │   L1 —— [ CT1 ] ——→     │ → Meter Channel 1
   │   L2 —— [ CT2 ] ——→     │ → Meter Channel 2
   └─────────────────────────┘
               ↓
           House Loads
```

### **PV Backfeed Breaker**

```
Inverter → Backfeed Breaker → —— [ CT3 ] ——→ Meter Channel 3
```

These will be recreated as real diagrams in Figma later.

---

# #️⃣ **11. Recommended CT Models (V1 Prototype)**

### **Main (100–200A):**

* Magnelab SCT-1250
* CCS AccuCT CTBL series
* YHDC SCT-013-000 (budget option)

### **PV (20–50A):**

* Magnelab SCT-0750
* Echun ECS series
* YHDC SCT-013-030

All include burden resistors.
All compatible with standard home energy monitors.

---

# #️⃣ **12. Summary**

SolThrive V1 requires:
* **Two 100–200A split-core CTs** for mains
* **One 20–50A split-core CT** for PV
* ~1% accuracy
* Built-in burden resistors
* Correct orientation toward load/source
* Clean wiring into meter channels

This ensures:
* Accurate consumption
* Accurate PV production
* Accurate grid flow
* Reliable long-term field performance
