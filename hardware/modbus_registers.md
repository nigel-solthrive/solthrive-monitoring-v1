# SolThrive Monitoring V1 — Modbus Register Map Overview

## 1. Purpose of This Document
This document defines the essential Modbus RTU registers needed for SolThrive Monitoring V1 to read real-time data from the Acrel ADL400-CT (or similar 3-channel Modbus CT meter).

These registers are used by:
- poller.py  
- logger.py  
- dashboard API  
- validation/testing scripts  

This is NOT the full manufacturer register list — only the registers needed for V1.

---

## 2. Key Concepts (Plain English)

### What is Modbus RTU?
Modbus RTU is a simple communication protocol that sends and receives numeric registers over RS-485.

Think of it like:
> “Ask the meter what the current is → meter replies with a number.”

### What is a Register?
A register is just a memory slot holding a value:
- Voltage
- Current
- Power
- Energy
- Frequency

Each register has:
- An **address** (like a street number)
- A **data type** (16-bit or 32-bit)
- A **unit** (amps, volts, watts, etc.)

---

## 3. SolThrive V1 Needed Registers (Minimal Set)

Below is the minimal recommended register set for V1.

These are generic Acrel-style addresses commonly used across the ADL300/400 meter series.

### Voltage
| Measurement | Register | Type | Notes |
|-------------|----------|------|-------|
| Voltage L1  | 0x0000   | 16-bit | Volts × 10 |
| Voltage L2  | 0x0001   | 16-bit | Volts × 10 |

### Current (CT Inputs)
| CT Channel | Register | Type | Notes |
|------------|----------|------|-------|
| CT1 (Main L1) | 0x0006 | 16-bit | Amps × 100 |
| CT2 (Main L2) | 0x0007 | 16-bit | Amps × 100 |
| CT3 (PV Breaker) | 0x0008 | 16-bit | Amps × 100 |

### Active Power
| Power Measurement | Register | Type | Notes |
|-------------------|----------|------|-------|
| Total Active Power | 0x000C | 16-bit | W |
| L1 Active Power | 0x000D | 16-bit | W |
| L2 Active Power | 0x000E | 16-bit | W |
| PV Active Power | 0x000F | 16-bit | W |

### Energy Import/Export
| Energy | Register | Type | Notes |
|--------|----------|------|-------|
| Import kWh | 0x0100 | 32-bit | Accumulating |
| Export kWh | 0x0101 | 32-bit | Accumulating |

### Power Factor (Optional)
| Measurement | Register | Type |
|-------------|----------|------|
| PF Total    | 0x0030   | 16-bit |

---

## 4. Scaling Factors (IMPORTANT)

Meters do not usually return “real” numbers.  
They send scaled integers to preserve accuracy.

### Example Voltage
If register value = **2415**  
Scale = **÷10**  
Actual = **241.5 V**

### Example Current
If register value = **1532**  
Scale = **÷100**  
Actual = **15.32 A**

The software must apply these scalers.

---

## 5. Data Polling Recommendations

### Polling interval:
- **Every 1–2 seconds** → Real-time feeling  
- **Every 5 seconds** → For long-term logging stability

### Timeout:
- 100–200 ms

### Retries:
- 2 retries recommended

### Why?
RS-485 is extremely stable, so low polling cost.

---

## 6. Modbus Frames (Plain English)

When the Pi wants to read Current L1:

**Pi sends:**  
“Meter, what is register 0x0006?”

**Meter replies:**  
“Here is the 16-bit value.”

Your poller code:
- Reads the register  
- Applies the scaling  
- Stores the real value  

---

## 7. Register Map (ASCII Quick Diagram)

0x0000 → Voltage L1
0x0001 → Voltage L2
0x0006 → Current CT1 (Main L1)
0x0007 → Current CT2 (Main L2)
0x0008 → Current CT3 (PV)

0x000C → Total Power
0x000D → Power L1
0x000E → Power L2
0x000F → Power PV

0x0100 → Energy Import (kWh)
0x0101 → Energy Export (kWh)


---

## 8. Software Expectations (poller.py)

The poller should:
1. Connect to RS-485  
2. Read registers in batches  
3. Apply scaling  
4. Output JSON like:

{
"voltage_l1": 241.2,
"voltage_l2": 239.9,
"current_l1": 12.53,
"current_l2": 10.11,
"current_pv": -4.75,
"power_total": 1580,
"energy_import": 852.1,
"energy_export": 445.8
}

This is what logger.py and the dashboard will consume.

---

## 9. Future-Proofing for V2/V3
These registers cover:
- Home consumption  
- PV production  
- Grid interaction  
- Total power flow  

Upgrades for future versions:
- THD (harmonics)
- Frequency
- Neutral current
- Phase angle tracking
- Reactive power
- Multi-inverter PV systems
- Three-phase commercial loads

---

## 10. Summary (A4 Complete)
SolThrive V1 requires only ~12 Modbus registers to function.

These enable:
- Real-time current (CT1/CT2/CT3)
- Grid import/export
- Solar production
- Home consumption
- Long-term energy tracking

The Pi will poll these registers through RS-485 using the V1 poller script.
