# SolThrive Monitoring V1 — Current Transformer (CT) Specifications

## 1. Purpose of This Document
This document defines the Current Transformer (CT) requirements, behavior, safety, and installation guidelines for the SolThrive Monitoring V1 prototype system.

CTs are critical for measuring:
- Solar production
- Home consumption
- Grid import/export
- Real-time power flow

They act like magnetic sensors that measure current without touching the conductor.

---

## 2. What CTs Do (Plain English)
A CT clamps around a single conductor and detects the magnetic field created by electrical current.

Think of it as:

“A stethoscope for electricity.”

No cutting, splicing, or interrupting wires.

---

## 3. Split-Core vs Solid-Core CTs

### Split-Core CTs (Recommended for V1)
- Clamp-on
- Install without disconnecting conductors
- Safer
- Faster retrofit installs
- Slightly lower accuracy, but ideal for residential monitoring

### Solid-Core CTs
- Require disconnecting the wire
- Extremely accurate
- Not recommended for retrofits

V1 choice: Split-core CTs for all three channels.

---

## 4. CT Amp Ratings

| Location              | CT Rating | Reason                               |
|----------------------|-----------|----------------------------------------|
| Main Service L1      | 100–200A  | Full house load                       |
| Main Service L2      | 100–200A  | Same as above                         |
| PV Backfeed Breaker  | 20–50A    | PV inverter output is much smaller    |

---

## 5. CT Polarity and Orientation

Correct orientation:
- Main CTs → arrow toward the home (toward loads)
- PV CT → arrow toward the inverter (toward source)

If reversed:
- Import/export flips
- Can be corrected in software

---

## 6. CT Wiring (Lead Connections)

Typical color code:
- White = +
- Black = –

Meter terminal mapping:
- CT1 → I1+ / I1–
- CT2 → I2+ / I2–
- CT3 → I3+ / I3–

---

## 7. Accuracy Class

CT accuracy options:
- 1% — ideal for V1
- 0.5% — premium
- 3% — too low

V1 target: 1% accuracy CTs.

---

## 8. Burden Resistors

CTs must have burden resistors.

V1 Requirement:
Use CTs with built-in burden resistors.

Benefits:
- Safer
- Meter compatible
- No risk of overvoltage
- Simpler wiring

---

## 9. CT Safety Notes

- Clamp around one conductor only
- Never clamp around hot + neutral together
- Keep clear of energized lugs
- Shut off main breaker if unsure
- Treat panels as energized even when “off”

---

## 10. Placement Diagrams (ASCII)

### Main Service Conductors
        [Utility Service]
               ↓
   ┌─────────────────────────┐
   │       Main Breaker      │
   │                         │
   │   L1 —— [ CT1 ] ——→     │ → Meter CH1
   │   L2 —— [ CT2 ] ——→     │ → Meter CH2
   └─────────────────────────┘
               ↓
           House Loads

### PV Backfeed Breaker
Inverter → Backfeed Breaker → —— [ CT3 ] ——→ Meter CH3

---

## 11. Recommended CT Models

### Main (100–200A):
- Magnelab SCT-1250
- CCS AccuCT CTBL series
- YHDC SCT-013-000 (budget)

### PV (20–50A):
- Magnelab SCT-0750
- Echun ECS series
- YHDC SCT-013-030

---

## 12. Summary

SolThrive V1 requires:
- (2) 100–200A split-core CTs
- (1) 20–50A split-core CT
- 1% accuracy
- Built-in burden resistors
- Correct orientation toward load/source

Provides accurate:
- Consumption
- PV production
- Grid flow

---
