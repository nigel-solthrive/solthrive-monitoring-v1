Field Test Procedure — SolThrive Monitoring V1

---

## **1. Purpose**

This Field Test Procedure validates the complete SolThrive Monitoring V1 system **inside a real electrical panel** after the bench test has fully passed.

It confirms:

* CT orientation is correct
* PV and mains channels measure accurately
* Voltage matches meter readings
* Import/export polarity is correct
* Power flows are sensible and stable
* Real-time and logged data match physical conditions
* The Pi, meter, and wiring behave as a unified monitoring appliance

This must be completed before labeling the system “commissioned.”

---

## **2. Safety Requirements (Critical)**

Working inside a live electrical panel is dangerous.
Follow NEC and electrical-safety practices:

* Wear insulated gloves
* Stand on non-conductive surface
* Avoid touching bus bars or lugs
* Never place hands near main breaker stabs
* Use the **one-hand rule** when probing
* Shut off the main breaker if unsure
* Only clamp CTs around **one conductor**
* Never clamp hot + neutral together

If you are not comfortable with energized work — **STOP** and call a licensed electrician.

---

## **3. Required Equipment**

| Item                              | Purpose                                            |
| --------------------------------- | -------------------------------------------------- |
| Raspberry Pi (fully bench-tested) | Controller                                         |
| Energy meter (powered)            | Measurement device                                 |
| (3) CTs                           | Mains L1, mains L2, PV                             |
| Smartphone/tablet/laptop          | For API testing                                    |
| Multimeter                        | Voltage checks                                     |
| Reference load                    | To simulate consumption (space heater, hair dryer) |
| Optional: clamp meter             | Extra current validation                           |

---

## **4. Pre-Field Checklist**

Before opening the panel:

✔ Bench test fully passed
✔ Pi boots automatically into SolThrive services
✔ API responding
✔ Meter already wired to L1/L2 inside subpanel or external enclosure
✔ RS-485 connected and verified
✔ CTs physically accessible
✔ Installer understands CT polarity arrows

Do **not** proceed if any item above is missing.

---

# **5. Field Installation Procedure**

---

## **5.1 Mount the Pi (if not already mounted)**

Choose one:

### ◎ DIN-rail enclosure (recommended)

Mount near the panel in an auxiliary enclosure.

### ◎ Backboard mounting

Use standoffs and zip-tie lateral strain relief.

### ◎ Adjacent equipment room

Mount the Pi near the router or network switch.

**Avoid** mounting Pi inside the main electrical panel.

---

## **5.2 Verify Meter Power**

Using a multimeter:

* L1 → neutral: ~120V
* L2 → neutral: ~120V
* L1 → L2: ~240V

If the meter display is active and stable, continue.

---

## **5.3 Install CTs on Conductors**

### ✔ **CT1 — Main L1**

Clamp the CT around the conductor feeding one pole of the main breaker.

Arrow direction:
**Toward the home / loads**
(Arrow points AWAY from the utility.)

### ✔ **CT2 — Main L2**

Same procedure for the second hot leg.

Arrow direction:
**Toward the home / loads**

### ✔ **CT3 — PV Backfeed**

Clamp around the inverter’s backfeed hot conductor.

Arrow direction:
**Toward the inverter (source)**

### CT Installation Notes

* Ensure the CT is fully closed; latch must click.
* Keep CTs away from metal surfaces when possible.
* Do not clamp CT around both hot legs — must be 1 conductor only.

---

## **5.4 Connect CT Leads to Meter**

Match channels:

```
CT1 → I1+ / I1–
CT2 → I2+ / I2–
CT3 → I3+ / I3–
```

Color consistency:

* White = +
* Black = –

---

# **6. Live Validation Tests**

This is the core of field commissioning.

---

## **6.1 Validate Voltage Readings**

Open browser:

```
http://<pi-ip>:8080/api/latest
```

Check:

* `voltage_l1` ≈ 118–125V
* `voltage_l2` ≈ 118–125V

Compare to multimeter:

```
Meter reading should be within ±2–3 V.
```

If voltage offsets are large → check meter wiring.

---

## **6.2 Validate No-Load Readings**

Turn off major appliances.

Expected:

* `current_l1` < 1.0 A
* `current_l2` < 1.0 A
* `current_pv` near zero (if solar idle)

If values > 1A, re-check CT closure or placement.

---

## **6.3 Validate Load Response (Main CTs)**

Turn on a known high-power load (space heater, microwave, etc).

Expected behavior:

* **CT1 and CT2 increase sharply**
* `power_total` increases
* Import power becomes **positive** (grid → home)

Example:

```
Load: 1500 W space heater
Expected: power_total ≈ 1350–1600 W
```

If readings are negative → CT orientation is reversed.

---

## **6.4 Validate Solar PV Readings (CT3)**

When solar is producing:

* `current_pv` should be **positive** (toward inverter)
* `power_pv` should be positive
* If PV arrow is reversed → PV may show negative

Fix by:

* Reversing CT
  **or**
* Changing sign in software (less ideal)

---

## **6.5 Import / Export Polarity Test**

### **Step 1 — Load ON**

* Turn on a heavy load
* Solar minimal
  **Expected:**
  `power_total` **positive** (importing)

### **Step 2 — Solar producing**

* Ensure PV producing more than home uses
* Turn off the load
  **Expected:**
  `power_total` **negative** (exporting to grid)

This confirms all polarity conventions are correct.

---

## **6.6 Verify Real-Time Stability**

Watch API updates for 60 seconds:

```
/api/latest
```

Confirm:

* Readings update every 1–2 seconds
* No zeros or NANs
* No drops in voltage
* No wild CT swings

If unstable → check RS-485 shielding and A/B wiring.

---

## **6.7 Logging Verification**

Check minute logs:

```
/var/solthrive/logs/daily/<today>.csv
```

Check raw logs:

```
tail /var/solthrive/data/history.jsonl
```

Values should match API readings.

---

## **6.8 Final API Check**

Verify all endpoints:

```
/api/latest
/api/powerflow
/api/history?hours=1
/api/system
```

All should respond instantly.

---

# **7. Commissioning Checklist**

| Item                       | Pass/Fail |
| -------------------------- | --------- |
| Meter powered correctly    | ☐         |
| Voltage readings correct   | ☐         |
| CT1/L1 orientation correct | ☐         |
| CT2/L2 orientation correct | ☐         |
| CT3/PV orientation correct | ☐         |
| Import → positive power    | ☐         |
| Export → negative power    | ☐         |
| PV measured correctly      | ☐         |
| No-load baseline < 1A      | ☐         |
| Load test matches expected | ☐         |
| API stable                 | ☐         |
| Logs writing properly      | ☐         |
| System auto-starts on boot | ☐         |

---

# **8. Field Test Complete**

Once all tests pass, the monitoring system is considered **commissioned**, and the installation is ready for:

* Ongoing monitoring
* Dashboard integration
* V2 local UI development
* V3 cloud sync expansion

---
