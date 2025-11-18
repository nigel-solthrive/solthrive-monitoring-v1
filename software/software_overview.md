A5 — Software Architecture Overview**

**SolThrive Monitoring V1 — Enhanced Engineering Edition**

---

## **1. Purpose**

This document defines the complete software architecture powering the **SolThrive Monitoring V1** system. It explains:

* How the Raspberry Pi polls the meter
* How register values are scaled and processed
* How snapshots are generated
* How local logging works
* How real-time and historical data are served through a local API
* How system reliability is maintained through systemd services

This is the “brain” that transforms raw electrical data into actionable monitoring.

---

## **2. High-Level Software Components**

SolThrive V1 consists of **three primary Python services**:

### **1. `poller.py` — Modbus Meter Reader**

* Communicates with the RS-485 meter
* Reads Modbus registers (A4)
* Applies scaling (÷10, ÷100, etc.)
* Builds a structured JSON snapshot
* Writes the latest data to disk
* Forwards snapshots to the logger via file or IPC

### **2. `logger.py` — Persistent Data Storage**

* Receives snapshots from poller
* Appends raw data to a JSONL history file
* Aggregates 1-minute logs → CSV
* Produces daily summaries → CSV
* Minimizes SD card wear through batched writes

### **3. `web.py` — Local Read-Only API**

* Lightweight Flask server
* Serves JSON endpoints for dashboards and external tools
* Provides real-time and historical data views
* Powers future on-device UI (V2+)

These services operate independently but cooperate through shared data directories.

---

## **3. Software Data Flow (Enhanced ASCII Diagram)**

```
               ┌─────────────────────┐
               │   Energy Meter       │
               │  (Acrel ADL400-CT)   │
               └─────────┬───────────┘
                         │  RS-485
                         ▼
              ┌──────────────────────┐
              │      poller.py        │
              │  (Modbus Register     │
              │        Reader)        │
              └─────────┬────────────┘
                 JSON snapshot │
                         ▼
              ┌──────────────────────┐
              │      logger.py        │
              │ (Data Storage Engine) │
              └─────────┬────────────┘
     CSV logs, JSONL     │
                         ▼
              ┌──────────────────────┐
              │       web.py          │
              │ (Local API Server)    │
              └─────────┬────────────┘
                         │ HTTP (localhost / LAN)
                         ▼
              ┌──────────────────────┐
              │   Dashboard / Apps    │
              │   (Future V2/V3 UI)   │
              └──────────────────────┘
```

This chain ensures real-time data movement from the meter → Pi → user interface.

---

## **4. `poller.py` Architecture**

### **Core Responsibilities**

1. Open RS-485 serial connection
2. Request batches of registers using Modbus FC3 (read holding registers)
3. Decode integer values
4. Apply scaling factors per A4
5. Write **`latest.json`** to disk
6. Forward snapshot to `logger.py`

### **Polling Interval**

* **1–2 seconds** — interactive, near real-time
* **5 seconds** — low-bandwidth logging setups

### **Example Poller Output**

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

This file lives at:

```
/var/solthrive/data/latest.json
```

---

## **5. `logger.py` Architecture**

The logger stores **long-term, durable** data.

### **Writes To:**

* `history.jsonl` — raw append-only stream
* `logs/1min/` — 1-minute aggregates (CSV)
* `logs/daily/` — per-day summaries

### **Directory Layout**

```
/var/solthrive/
    data/
        latest.json
        history.jsonl
    logs/
        daily/
        monthly/
```

### **Why Baseline Logging Matters**

* Enables graphs
* Enables savings estimates
* Enables troubleshooting
* Supports future V2 cloud sync
* Reduces SD card wear

`logger.py` is optimized for minimal writes and high reliability.

---

## **6. `web.py` — Local API Server**

A lightweight read-only API providing data to dashboards, mobile apps, and installers.

### **Key API Endpoints**

#### **`/api/latest`**

Returns the most recent snapshot.

#### **`/api/history?hours=N`**

Returns last *N* hours from JSONL.

#### **`/api/powerflow`**

Example output:

```
{
  "solar_kw": 3.52,
  "home_kw": 1.44,
  "grid_kw": -2.08
}
```

#### **`/api/system`**

Returns system metadata.

### **Implementation**

* Built using Flask
* Runs locally on port **8080**
* No external network exposure (V1)

---

## **7. Configuration File (`config.yaml`)**

Defines all tunable parameters:

```
serial_port: "/dev/ttyUSB0"
baudrate: 9600
poll_interval: 2
log_dir: "/var/solthrive/logs/"
data_file: "/var/solthrive/data/latest.json"
api_port: 8080
```

Centralizing settings simplifies field updates and future V2 features.

---

## **8. Systemd Services**

To keep SolThrive reliable on the Pi, each component runs as a systemd service:

* `solthrive-poller.service`
* `solthrive-logger.service`
* `solthrive-api.service`

### Benefits:

* Auto-start at boot
* Auto-restart on crash
* Unified logs
* Production-grade stability

Systemd ensures the Pi behaves like a commercial appliance.

---

## **9. Folder Structure for Software**

Recommended GitHub + Pi file layout:

```
solthrive-monitoring-v1/
└── software/
    ├── poller.py
    ├── logger.py
    ├── web.py
    ├── config.yaml
    └── requirements.txt

/var/solthrive/
└── data/
    └── latest.json
    └── history.jsonl
└── logs/
    ├── daily/
    └── monthly/
```

This organization keeps runtime data isolated from source code.

---

## **10. Future Versions (Roadmap)**

### **V2**

* Real-time WebSocket streaming
* On-device dashboard UI
* Remote firmware update capabilities
* Basic edge-based anomaly detection

### **V3**

* Fleet monitoring cloud
* Multi-inverter / multi-meter deployments
* DER integration (battery, EV, flexible loads)
* Contractor/installer portals
* Advanced analytics

The V1 architecture is intentionally lightweight to support all future versions.

---

## **11. Summary (A5 Complete)**

SolThrive V1 software system consists of:

* **`poller.py`** — reads Modbus registers
* **`logger.py`** — writes durable timeseries logs
* **`web.py`** — serves real-time data via local API

Together, they form a small, efficient, reliable monitoring appliance capable of:

* Real-time powerflow
* Long-term consumption/production analysis
* Easy dashboard integration
* Expandability into future versions

This architecture is the backbone of the SolThrive monitoring platform.

---
