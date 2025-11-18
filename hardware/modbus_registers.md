A4 — Modbus Register Map

---

## **1. Purpose**

This document defines the **exact Modbus RTU registers** required for SolThrive Monitoring V1. These registers are accessed by the Raspberry Pi to read:

* Voltage
* Current
* Power
* Energy import/export
* Optional metrics (PF, frequency)

This is *not* the full manufacturer register list — only the **minimal required set** used by V1 software (poller.py, logger.py, local API).

---

## **2. What Modbus RTU Is (Plain English)**

Modbus RTU is a simple request–reply protocol over RS-485.

Think of it like:

> **“Pi asks the meter for a number → meter replies with that number.”**

Each data point (voltage, current, etc.) lives in a **register** — an address that stores a numeric value.

Registers can be:

* **16-bit** (single register)
* **32-bit** (two registers combined)

SolThrive V1 uses both.

---

## **3. Required Registers for SolThrive V1**

Below is the **minimal stable register set** required by the V1 software.
These addresses match common layouts for Acrel ADL300/ADL400 series meters.

---

### **3.1 Voltage Registers**

| Measurement    | Register | Type   | Scaling | Notes                |
| -------------- | -------- | ------ | ------- | -------------------- |
| **Voltage L1** | `0x0000` | 16-bit | ÷10     | e.g., 2415 → 241.5 V |
| **Voltage L2** | `0x0001` | 16-bit | ÷10     | e.g., 2397 → 239.7 V |

---

### **3.2 Current Registers (CT Inputs)**

| Channel              | Register | Type   | Scaling | Notes          |
| -------------------- | -------- | ------ | ------- | -------------- |
| **CT1 (Main L1)**    | `0x0006` | 16-bit | ÷100    | Amps (L1)      |
| **CT2 (Main L2)**    | `0x0007` | 16-bit | ÷100    | Amps (L2)      |
| **CT3 (PV Breaker)** | `0x0008` | 16-bit | ÷100    | Solar backfeed |

---

### **3.3 Active Power Registers**

| Measurement     | Register | Type   | Scaling | Notes                         |
| --------------- | -------- | ------ | ------- | ----------------------------- |
| **Total Power** | `0x000C` | 16-bit | raw W   | Net consumption/import/export |
| **L1 Power**    | `0x000D` | 16-bit | raw W   |                               |
| **L2 Power**    | `0x000E` | 16-bit | raw W   |                               |
| **PV Power**    | `0x000F` | 16-bit | raw W   | Solar output                  |

---

### **3.4 Energy Registers**

These values accumulate over time.

| Energy Type    | Register | Type   | Notes                 |
| -------------- | -------- | ------ | --------------------- |
| **Import kWh** | `0x0100` | 32-bit | Total energy imported |
| **Export kWh** | `0x0101` | 32-bit | Total energy exported |

These are essential for long-term savings reports and dashboard analytics.

---

### **3.5 Optional: Power Factor**

| Measurement  | Register | Type   | Scaling          |
| ------------ | -------- | ------ | ---------------- |
| **PF Total** | `0x0030` | 16-bit | unitless (0–1.0) |

Not required for V1, but useful for power-quality diagnostics.

---

## **4. Scaling Factors (Critical)**

Meters rarely return “real numbers.”
They return integers with built-in scaling factors.

### **Voltage Example**

* Raw value: **2415**
* Scaling: ÷10
* Actual: **241.5 V**

### **Current Example**

* Raw value: **1532**
* Scaling: ÷100
* Actual: **15.32 A**

### Why Scaling Exists

* Ensures precision
* Avoids floating-point issues
* Keeps communication stable over slow RS-485 lines

**SolThrive software applies all scaling in poller.py.**

---

## **5. Recommended Polling Settings**

| Parameter                | Value                        |
| ------------------------ | ---------------------------- |
| **Polling Interval**     | 1–2 seconds (real-time feel) |
| **Alternative Interval** | 5 seconds (low-load logging) |
| **Timeout**              | 100–200 ms                   |
| **Retries**              | 2                            |

Modbus is extremely efficient — even fast polling is low overhead.

---

## **6. Example Modbus Interaction (Plain English)**

When the Pi wants to read CT1 current:

**Pi sends:**

> “Meter, give me register **0x0006**.”

**Meter replies:**

> “Here’s the value: **1532**.”

**Pi converts:**
1532 ÷ 100 = **15.32 A**

**logger.py** then writes the result to JSONL/CSV.

---

## **7. ASCII Register Map Overview**

A quick visual lookup:

```
0x0000  Voltage L1
0x0001  Voltage L2

0x0006  Current CT1 (Main L1)
0x0007  Current CT2 (Main L2)
0x0008  Current CT3 (PV)

0x000C  Total Active Power
0x000D  Power L1
0x000E  Power L2
0x000F  Power PV

0x0100  Import kWh (32-bit)
0x0101  Export kWh (32-bit)

0x0030  Power Factor (optional)
```

These registers provide all essential readings for consumption, solar production, and net flow.

---

## **8. What poller.py Expects**

The poller:

1. Connects to `/dev/ttyUSB0`
2. Reads all required registers in a batch
3. Applies scaling
4. Produces a JSON snapshot like:

```
{
  "timestamp": "2025-01-03T14:22:10Z",
  "voltage_l1": 241.2,
  "voltage_l2": 239.9,
  "current_l1": 12.53,
  "current_l2": 10.11,
  "current_pv": -4.75,
  "power_total": 1580,
  "energy_import": 852.1,
  "energy_export": 445.8
}
```

---

## **9. Future-Proofing for V2/V3**

The V1 register set supports:

* Full consumption monitoring
* Solar PV measurement
* Import/export tracking
* Net metering analytics
* Dashboard visualizations

Future expansions may include:

* THD (harmonics)
* Frequency
* Neutral current
* Reactive/VAR metrics
* Multi-inverter systems
* Commercial 3-phase support

The A4 register map is intentionally minimal to keep V1 simple and stable.

---

## **10. Summary (A4 Complete)**

SolThrive V1 uses ~12 registers to compute:

* Home consumption
* Solar production
* Grid import/export
* Total instantaneous power
* Long-term energy flows

These registers provide all data required by:

* **poller.py**
* **logger.py**
* **local API (web.py)**
* Future dashboards

This register map is the backbone of the SolThrive monitoring system.

---
