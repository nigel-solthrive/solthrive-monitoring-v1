Perfect — we're rolling with the **professional, real-world combo**:

✅ **2–3 Page Installer Quick-Start Guide**
✅ **Full Installer Manual (20+ pages)**

I’ll start by giving you the **Quick-Start Guide**, clean, tight, and GitHub-ready.
You’ll save it here:

```
device_edge_s1/S1_Installer_Quickstart.md
```

Once that’s complete, I’ll follow with the **Full Installer Manual** next.

---

# 🟩 **SolThrive Edge S1 — Installer Quick-Start Guide (v1.0)**

**Save as:** `device_edge_s1/S1_Installer_Quickstart.md`
**Length:** ~2.5 pages, fast for field use, includes micro-diagrams + safety.

---

```markdown
# SolThrive Edge S1 — Installer Quick-Start Guide  
**Version:** v1.0  
**Device:** SolThrive Edge S1  
**Platform:** SolThrive Monitoring V1  

This Quick-Start Guide provides the essential steps for mounting, wiring, powering, and verifying the SolThrive Edge S1 energy monitoring device.

For advanced details, refer to:  
**S1_Installer_Manual.md**

---

# ⚠️ 1. Safety Requirements

Installation must be performed by a **licensed electrician**.

- De-energize breakers before installing CTs or voltage wiring.  
- Follow NEC/local electrical code.  
- Keep low-voltage RS-485 wiring **separate** from AC conductors.  
- Verify CT orientation before closing the panel.  

**CT Rule:**  
**Arrow → toward the load**  
If reversed, import/export values will be inverted.

---

# 🧰 2. Required Tools

- Flathead + Phillips screwdrivers  
- Wire stripper / cutter  
- Ferrule crimp tool  
- Drill + step bit (for cable glands)  
- Multimeter  
- Laptop (for Pi setup)  

---

# 📦 3. Included Components (S1)

- Acrel ADL-series meter  
- Raspberry Pi 4 + USB→RS485 adapter  
- 2–3 split-core CTs  
- DIN rail + mounting plate  
- S1 enclosure (pilot)  
- Low-voltage wiring kit  

---

# 📍 4. Recommended Mounting Location

- Near service panel or subpanel  
- Dry indoor location  
- Within **3 meters** of CT anchoring point  
- Adequate ventilation for Pi  
- Mount enclosure vertically for best heat dissipation  

---

# 🪛 5. Mounting the Edge S1

1. Mount DIN rail inside enclosure.  
2. Snap in **Acrel ADL meter** (top).  
3. Mount **Raspberry Pi** on DIN baseplate (below the meter).  
4. Install **optional surge protector** if used.  
5. Install cable glands (CT + RS485 entries).  

```

[ Top ]
┌───────────────────┐
│  Acrel Meter       │
└───────────────────┘
│  Raspberry Pi 4    │
│  + RS485 Adapter   │
└───────────────────┘
[ Bottom ]

```

---

# 🔌 6. Wiring Sequence (Follow This Order)

## **Step 1 — CT Installation**

### ❗ Power Off Main Breaker  
Install CTs around:

- **Main L1**  
- **Main L2**  
- **PV backfeed** (if applicable)

### CT Orientation  
Arrow → **toward the load (house)**

### CT Polarity
If CT leads are polarized:

- **White → I+**  
- **Black → I−**

*(I+ and I− refer to the meter’s CT inputs; the “I” means current.)*

Terminate CT wires on the Acrel meter:

| CT | Meter Terminals |
|----|-----------------|
| CT1 (mains) | I1+ / I1− |
| CT2 (PV) | I2+ / I2− |
| CT3 (optional load) | I3+ / I3− |

---

## **Step 2 — Voltage Sense Wiring (Meter L1/L2)**

Wire the meter’s voltage sense terminals:

- **L1 → Phase A**  
- **L2 → Phase B**  
- **N → Neutral** (if required by meter model)

Verify connections with a multimeter before powering.

---

## **Step 3 — RS-485 Wiring (Meter → Pi)**

Connect the Acrel terminals to the USB→RS485 adapter:

| Meter Terminal | USB-RS485 |
|----------------|-----------|
| A | A |
| B | B |
| GND | GND |

**Use twisted-pair cable.**  
Avoid running alongside AC conductors.

---

## **Step 4 — Power the Pi**

Connect:

- 5V 3A USB-C power supply → Raspberry Pi  
- Confirm Pi boots (steady red LED, blinking green LED)

---

# 🧪 7. Commissioning Checklist

### **1. Meter Communication Test**
Run on the Pi:

```

python3 /opt/solthrive-monitoring-v1/software/poller.py --test

```

✔ Should return real-time kWh / kW values  
✖ If timeout → check RS485 polarity (A/B)

---

### **2. CT Verification**
Check values:

- Home load fluctuates with appliances  
- PV negative at night / positive in sunlight  
- Import/export signs correct  
- If reversed → flip CT direction or swap I+/I−

---

### **3. Voltage & Power Factor**
Expected values:

- 110–125 V per leg  
- PF: 0.95–1.00 typical  

---

### **4. API Test**
From laptop:

```

curl http://<pi-ip>:8080/api/latest

```

✔ JSON returns without errors  
✔ All channels show valid floats  

---

# 🧷 8. Final Steps

- Secure wiring with clips  
- Add ferrites if electrical noise  
- Close enclosure  
- Label device as “SolThrive Edge S1”  
- Date + Installer initials  

---

# 📞 Support

SolThrive Renewables  
support@solthriverenewables.com  
solthriverenewables.com  

---

# ✔️ End of Quick-Start Guide
```

---

# 🟦 **Next: The Full Installer Manual (20+ pages)**

Now that the Quick-Start Guide is done, your next document is:

```
device_edge_s1/S1_Installer_Manual.md
```

I’ll deliver that next — properly structured, professional, and modeled after the AlsoEnergy manual (but 100% your own).

Ready for it? Just say:

**“Let’s do the full manual.”**
