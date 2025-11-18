# SolThrive Monitoring V1 — Raspberry Pi Wiring & Mounting Guide

## 1. Purpose of This Document
This guide explains how to wire, mount, and power the Raspberry Pi used in the SolThrive Monitoring V1 prototype.

The Pi acts as:
- The Modbus data poller  
- The local API server  
- The logging engine  
- The dashboard host (optional for V1)  

---

## 2. Hardware Used in V1 Prototype

### Raspberry Pi
Recommended models:
- Raspberry Pi 4 (best performance)
- Raspberry Pi 3B+ (fully compatible)
- Raspberry Pi Zero 2W (only for ultra-low cost build)

V1 Target: **Raspberry Pi 4 Model B (2GB or 4GB)**

### Required Accessories
- 5V → 3A USB-C power supply (official or high-quality)
- MicroSD card 16–64GB (Class 10 or better)
- RS-485 → USB adapter
- Ethernet cable (recommended for stability)
- DIN-rail mountable Pi case (optional but ideal for field installs)

---

## 3. Communication Interface (RS-485 → USB)

The Pi communicates with the energy meter using **Modbus RTU (RS-485)** via a USB adapter.

### Recommended RS-485 Adapters
- Waveshare USB-to-RS485  
- DSD TECH SH-U10  
- FTDI-based industrial adapters (most reliable)

### Wiring to the Energy Meter
Energy Meter RS-485 terminals:
- **A** (sometimes “D+”)
- **B** (sometimes “D–”)
- **GND** (optional but recommended)

Adapter wires:
- A → A  
- B → B  
- GND → GND  

Keep RS-485 cable twisted pair (CAT5/CAT6 works great).

Maximum recommended length for V1: **10–50 ft**  
Up to 1000 ft is possible, but not needed here.

---

## 4. Network Connectivity

### Preferred Order
1. **Ethernet (best)**  
   - Most stable  
   - No Wi-Fi dropouts  
   - Ideal for monitoring reliability  

2. **Wi-Fi (acceptable)**  
   Use if Ethernet isn’t available near the panel.

3. **Hotspot / Cellular (future V2/V3)**  
   Only needed for remote commercial installs.

---

## 5. Power Considerations

The Pi MUST have:
- Clean, stable 5V
- At least 2.5A available (3A recommended)

Avoid:
- Cheap Amazon wall plugs  
- USB ports on inverters  
- Weak Wi-Fi distance causing brownouts  

If powering near a panel:
- Use a **dedicated receptacle**
- Or a **UL-listed DIN-rail USB PSU** (MeanWell HDR-15-5 recommended)

---

## 6. Physical Mounting Options

### Option 1 — DIN-Rail Case (Recommended)
Advantages:
- Clean install next to the energy meter  
- Mechanical stability  
- Easier field servicing  
- Professional appearance  

DIN-rail Pi cases to consider:
- GeeekPi DIN-Rail Raspberry Pi 4 Enclosure  
- Waveshare Industrial Pi Case  

### Option 2 — Standard Pi Case (Budget)
Advantages:
- Cheap  
- Easy  

Disadvantages:
- Not panel-friendly  
- No mounting tabs  
- Can vibrate loose  

### Option 3 — Pi Mounted to Backboard (Simple V1)
- Use plastic standoffs  
- Screw into plywood backer board  
- Avoid conductive surfaces  
- Keep away from bus bars  

---

## 7. Recommended Mounting Location

Ideal:
- **Inside an electrical equipment room**, on a backboard  
- Next to the router or Ethernet switch  
- Away from high-voltage lugs  
- Not inside the main service panel (unsafe & code issues)

Allowed (if careful):
- Inside an auxiliary enclosure  
- With proper ventilation  

Avoid:
- Inside inverter housing  
- Inside the main panel  
- Anywhere moisture can enter  

---

## 8. Field Wiring Diagram (ASCII)

### Pi + RS-485 + Meter Wiring Overview

          ┌──────────────────────────┐
          │      Raspberry Pi        │
          │                          │
          │  USB Port ───────────────┼─── USB-RS485 Adapter
          └──────────────────────────┘
                      │
                      │  RS-485 Twisted Pair (CAT5/6)
                      ▼
          ┌──────────────────────────┐
          │   Energy Meter (Acrel)   │
          │                          │
          │   A  ────────────────────┘
          │   B  ────────────────────┘
          │  GND ────────────────────┘
          └──────────────────────────┘

CTs → Meter  
Meter → Pi  
Pi → SolThrive Dashboard  

---

## 9. SD Card Setup Notes (For Later Software Section)

Image to install:
- Raspberry Pi OS Lite (recommended)
- No desktop environment needed for V1

Basic preparation:
- Flash via Raspberry Pi Imager
- Enable SSH
- Set hostname: `solthrive-monitor-v1`
- Pre-configure Wi-Fi if needed

---

## 10. Summary (A3 Complete)

For SolThrive Monitoring V1:
- Use Raspberry Pi 4  
- Use USB-RS485 adapter  
- Use Ethernet when possible  
- Install in a clean, ventilated, panel-adjacent enclosure  
- Keep wiring simple and safe  
- Follow orientation + polarity rules  

The Pi is the “brain” of the V1 system — it polls the meter, logs values, and serves the API.

