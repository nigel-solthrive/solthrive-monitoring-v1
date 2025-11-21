A3 — Raspberry Pi Wiring & Mounting Guide

---

## **1. Purpose**

This document explains how to **wire, mount, power, and connect** the Raspberry Pi used in the SolThrive Monitoring V1 prototype.
The Pi is the central controller for:

* **Modbus polling** (via RS-485)
* **JSON snapshot generation**
* **Data logging**
* **Local API hosting**
* Optional **dashboard serving**

This guide ensures a clean, reliable field installation.

---

## **2. Raspberry Pi Hardware Requirements**

### ✔ Recommended Models

* **Raspberry Pi 4 Model B (2GB or 4GB)** → *Primary V1 standard*
* Raspberry Pi 3B+ → compatible
* Raspberry Pi Zero 2W → only for ultra-low-cost builds

### ✔ Required Accessories

* High-quality **5V 3A USB-C** power supply (official recommended)
* 16–64GB **Class 10 microSD card**
* **RS-485 → USB** adapter
* Ethernet cable (preferred)
* Optional: **DIN-rail Pi enclosure** for professional installs

---

## **3. RS-485 Communication Interface**

The Pi communicates with the energy meter via **Modbus RTU over RS-485**, using an RS-485 → USB adapter.

### Recommended Adapters

* Waveshare USB-RS485
* DSD TECH SH-U10
* FTDI-based industrial adapters (most reliable)

### Wiring RS-485 to the Meter

#### **Meter Terminals**

* **A** (a.k.a. D+)
* **B** (a.k.a. D–)
* **GND** (optional but recommended)

#### **Wiring Rules**

* Adapter **A → Meter A**
* Adapter **B → Meter B**
* Adapter **GND → Meter GND**
* Use **twisted-pair cable** (CAT5/6 works)

### Cable Length Guidelines

* V1 install: **10–50 ft** recommended
* RS-485 supports up to **1000 ft**, but not needed here
* Avoid running parallel to AC conductors for long distances

---

## **4. Network Connectivity**

### Preferred Order

1. **Ethernet (best)**

   * rock-solid
   * zero Wi-Fi dropouts
   * ideal for continuous monitoring

2. **Wi-Fi (acceptable)**

   * use only when Ethernet is not available

3. **Hotspot / Cellular (future V2/V3)**

   * for remote or off-grid deployments

The Pi needs stable connectivity for the API, logging, and optional dashboard.

---

## **5. Power Requirements (Critical)**

The Pi requires:

* Clean, stable **5V supply**
* At least **2.5A** available (3A recommended)

### Avoid:

* Random Amazon wall-warts
* Weak inverter USB ports
* Long, thin USB cables that cause voltage drop
* Outlets with questionable grounding

### Recommended Power Options Near Panel:

* Standard wall receptacle
* **DIN-rail 5V power supply** (e.g., MeanWell HDR-15-5)

---

## **6. Physical Mounting Options**

A clean install is essential.
These are the recommended options:

### **Option 1 — DIN-Rail Mounted Pi Case (Recommended)**

**Advantages:**

* Professional appearance
* Secure and vibration-resistant
* Keeps wiring organized
* Easier field servicing

**Suggested Models:**

* GeeekPi DIN-Rail Pi 4 Enclosure
* Waveshare Industrial Case

---

### **Option 2 — Standard Pi Case (Budget Option)**

**Advantages:**

* Cheap and widely available
* Fine for benchtop testing

**Disadvantages:**

* Not enclosure-friendly
* No mounting holes
* Easier to dislodge

---

### **Option 3 — Pi Mounted on a Backboard**

* Attach Pi using **plastic standoffs**
* Mount to a plywood/ABS backboard
* Keep a safe distance from energized components
* Avoid conductive surfaces

This is the simplest field-install option.

---

## **7. Recommended Mounting Location**

Ideal:

* Electrical equipment room
* Near router or Ethernet switch
* Good airflow
* Away from panel lugs and main breakers

Allowed (with care):

* Inside an auxiliary enclosure
* Dedicated Pi box with ventilation

Avoid:

* Inside main service panel
* Inside inverter housings
* Damp or unventilated locations

---

## **8. Wiring Diagram (Enhanced ASCII)**

Below is a clean, accurate diagram of the full communication chain.

```
          ┌─────────────────────┐
          │   Raspberry Pi      │
          │ (poller / logger /  │
          │   local API server) │
          └──────────┬──────────┘
                     │ USB
                     ▼
          ┌─────────────────────┐
          │ USB → RS-485 Adapter│
          └──────────┬──────────┘
                     │ Twisted Pair (A/B/GND)
                     ▼
          ┌─────────────────────┐
          │ Energy Meter (Acrel)│
          │   A  ◄──────────────┘
          │   B  ◄──────────────┘
          │  GND ◄──────────────┘
          └─────────────────────┘

CTs → Meter  
Meter → Pi (Modbus RTU)  
Pi → Dashboard/API  
```

This chain forms the backbone of SolThrive V1.

---

## **9. SD Card Image & First Boot Checklist**

### Recommended OS

* **Raspberry Pi OS Lite** (no desktop)

### Initial Setup Steps

1. Flash OS using Raspberry Pi Imager
2. Enable **SSH**
3. Set hostname:
   `solthrive-monitor-v1`
4. Configure Wi-Fi if needed
5. Install Python dependencies from `requirements.txt`
6. Create directories:

   ```
   /var/solthrive/data/
   /var/solthrive/logs/
   ```

This prepares the Pi for software deployment (A5).

---

## **10. Summary (A3 Complete)**

For SolThrive Monitoring V1, the Raspberry Pi must:

✔ Be a Pi 4 (preferred)
✔ Use a USB-RS485 adapter
✔ Connect via Ethernet if possible
✔ Mount cleanly in a DIN-rail case or backboard
✔ Be powered by a stable 5V/3A supply
✔ Use OS Lite + SSH + hostname configuration

The Pi is the **brain** of the monitoring system — responsible for reading the meter, storing data, and serving the API.

---
