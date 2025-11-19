````markdown
# SolThrive Edge S1 — Installer Manual  
**Version:** v1.0  
**Device:** SolThrive Edge S1  
**Platform:** SolThrive Monitoring V1  
**Audience:** Licensed Electricians & Qualified Installers  

---

# 🛑 1. Safety Instructions & Warnings

Installation of the SolThrive Edge S1 must be performed by a **licensed electrician**.

### ⚡ High Voltage

- CT installation requires **opening the electrical panel**.
- Voltage-sense wiring connects to **live conductors**.
- Follow NEC and local electrical code at all times.
- Always de-energize circuits before working on CTs or voltage taps.

### 🔧 Low-Voltage Wiring

- RS-485 cable must remain isolated from AC conductors.
- Use twisted-pair for A/B differential lines.
- Keep all low-voltage wiring inside the enclosure or approved conduit.

### 🏷 CT Orientation

Incorrect CT placement will cause **reversed import/export readings**.

### 🧯 General

- Do not install device outdoors without rated enclosure.
- Avoid excessive moisture or temperatures above 50°C.
- Wear PPE appropriate for panel work.

---

# 📦 2. System Overview

The **SolThrive Edge S1** is a DIN-rail-mounted energy monitoring device designed for:

- Whole-home load monitoring  
- Solar PV production measurement  
- Grid import/export visibility  
- Offline-first operation with local API  
- Raspberry Pi–based edge compute  

The system consists of:

- Acrel ADL-series Modbus energy meter  
- Raspberry Pi 4 running SolThrive Monitoring V1  
- USB → RS485 communications module  
- 2–3 split-core current transformers  
- S1 enclosure (pilot version)  

---

# 🔧 3. Hardware Components

### **Included with S1 Prototype**

- 1× Acrel ADL-series energy meter  
- 1× Raspberry Pi 4 (4GB/8GB)  
- 1× USB→RS485 adapter  
- 2–3× Split-core CTs (100–200A)  
- DIN rail + Pi mounting plate  
- Low-voltage wiring harness  

### **Installer-Supplied Items**

- Pi 5V 3A USB-C power supply  
- CT extensions (if needed)  
- Conduit, cable glands, or strain relief fittings  
- Enclosure screws, wall anchors  

---

# 📍 4. Pre-Installation Planning

Before installation:

### ✔ Verify Panel Type

- Main panel or subpanel  
- Split-phase 120/240V (US typical)  

### ✔ Confirm CT Access

- Clearance around mains L1/L2  
- PV breaker accessibility  

### ✔ Determine Enclosure Location

- Within **3 meters** of CTs  
- Dry indoor location  
- Not directly over high-heat sources  
- Vertical mounting recommended  

### ✔ Check Network Requirements

- Local API does **not require internet**  
- For remote access (future V3), LAN is recommended  

---

# 🪛 5. Mounting the S1 Enclosure

### Tools Required:

- Drill + step bit  
- Screwdrivers  
- Wire stripper  
- Ferrule crimper  
- Level  

### Mounting Steps:

1. Mark mounting holes on wall or backboard.  
2. Install anchors/screws appropriate for surface.  
3. Mount enclosure backplate.  
4. Install DIN rail inside enclosure.  
5. Mount Acrel meter to DIN rail.  
6. Mount Raspberry Pi + RS485 adapter below the meter.  

### Recommended Layout:

```
┌──────────────────────────────────────────┐
│               Enclosure                  │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │        Acrel ADL Meter             │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │ Raspberry Pi 4                     │  │
│  │ + RS-485 USB Adapter               │  │
│  └────────────────────────────────────┘  │
│                                          │
│  ┌────────────────────────────────────┐  │
│  │    Surge Protector (optional)      │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
````

---

# 🔌 6. Wiring Overview

### Installation Order

1. CT installation
2. CT routing
3. Voltage-sense wiring
4. RS-485 wiring
5. Pi power
6. Commissioning test

---

# 🔋 7. CT Installation (Critical Section)

### ⚠️ De-energize panel before installing CTs.

### Identify CT Locations:

* **CT1** → Main L1
* **CT2** → Main L2
* **CT3** → PV backfeed breaker (if solar present)

### CT Orientation:

**Arrow → toward the load (house)**

### CT Polarity:

(Some CTs have polarized leads)

* **White → I+**
* **Black → I−**

*(“I” stands for *current*, not the letter “L.”)*

### Meter Terminations:

| CT  | Terminals |
| --- | --------- |
| CT1 | I1+ / I1− |
| CT2 | I2+ / I2− |
| CT3 | I3+ / I3− |

### Routing Rules:

* Twist CT leads
* Keep away from AC mains
* Use grommets for panel → enclosure entry

---

# ⚡ 8. Voltage Sense Wiring

### Purpose:

Voltage sense allows the meter to compute:

* Real power (kW)
* Power factor
* Accurate kWh

### Wiring:

* **L1 → Phase A**
* **L2 → Phase B**
* **N → Neutral** (if required by meter model)

Verify with a multimeter before energizing.

---

# 🧵 9. RS-485 Wiring (Meter → Pi)

### Required Materials:

* Shielded twisted pair
* Ferrules
* RS-485 A/B/GND termination

### Wiring Table:

| Meter Terminal | RS-485 Adapter |
| -------------- | -------------- |
| A              | A              |
| B              | B              |
| GND            | GND            |

### Rules:

* Do not run parallel to AC conductors
* Keep runs short (< 3m)
* Use cable glands for entry
* Shield can be tied to GND at meter end only

---

# 🔌 10. Powering the Raspberry Pi

* Use **5V 3A USB-C supply**
* Confirm LEDs:

  * Red (power): solid
  * Green (SD activity): blinking

Ensure Pi cooling is not blocked.

---

# 🧪 11. Field Commissioning Procedure

Once wiring is complete:

### **Step 1 — Boot the Pi**

Wait 30–60 seconds for services to start.

### **Step 2 — Test Modbus Connectivity**

On the Pi:

```
python3 /opt/solthrive-monitoring-v1/software/poller.py --test
```

Expected:

* Current readings
* Voltage
* PF
* kWh

If **timeout** → check A/B polarity.

---

### **Step 3 — Verify CT Direction & Polarity**

Look for:

* Load increases when appliances turn on
* PV positive when producing
* Import/export transitions when grid usage changes

**If reversed:**
Flip CT direction **or** swap I+/I−.

---

### **Step 4 — Validate Voltage Sense**

Expected readings:

* 110–125V per leg
* Balanced legs (within ±5%)

---

### **Step 5 — Check Local API**

From a laptop:

```
curl http://<pi-ip>:8080/api/latest
```

Expected:

* JSON with voltage, current, watts, pf, energy
* No “NaN” or null values

---

# 🛠 12. Troubleshooting Guide

### **No RS-485 Communication**

* Swap A/B lines
* Check ferrules
* Shorten cable
* Ensure shield termination is correct

### **Negative Solar at Noon**

* CT reversed → flip direction
* Wrong CT assigned → check mapping

### **Voltage Missing**

* Check L1/L2 tap
* Loose neutral

### **Pi Not Booting**

* Bad SD card
* Insufficient power supply
* Wrong OS image

---

# 📎 13. Appendix A — Reference Wiring Diagram

```
Service Panel
 ┌──────────────────────────────────────────┐
 │   L1 ────────── CT1 → Meter I1+/I1−      │
 │   L2 ────────── CT2 → Meter I2+/I2−      │
 │   PV Breaker ── CT3 → Meter I3+/I3−      │
 └──────────────────────────────────────────┘

Meter → Pi
    Meter A  → RS485 A  
    Meter B  → RS485 B  
    Meter GND → RS485 GND

Raspberry Pi
    USB-C → Power  
    USB Port → RS485 Adapter  
```

---

# 📎 14. Appendix B — Specifications Summary

* Meter: Acrel ADL200/300/400
* Pi: Raspberry Pi 4
* CTs: 100–200A split-core
* RS-485: 9600 baud, 8N1
* Enclosure: UL94-V0 recommended

---

# 📞 SolThrive Support

SolThrive Renewables
[support@solthriverenewables.com](mailto:support@solthriverenewables.com)
solthriverenewables.com

---

# ✔️ End of Installer Manual

```

