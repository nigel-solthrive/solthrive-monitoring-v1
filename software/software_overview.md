# SolThrive Monitoring V1 — Software Architecture Overview

## 1. Purpose of This Document
This document defines the complete software architecture for the SolThrive Monitoring V1 system, including:

- Polling meter data via Modbus RTU  
- Processing & scaling registers  
- Local JSON data output  
- Logging to disk  
- API endpoints for a dashboard or mobile app  
- Service design for reliability  

This is the software “brain” running on the Raspberry Pi.

---

## 2. High-Level Software Components

SolThrive V1 uses **three main Python services**:

### 1. poller.py
- Talks to the energy meter over RS-485  
- Reads Modbus registers  
- Converts raw values → real units (volts, amps, watts, kWh)  
- Produces a single JSON “snapshot” every cycle  
- Sends data to logger.py (via local file or socket)

### 2. logger.py
- Receives the JSON from poller.py  
- Writes data to:
  - Rolling log file (CSV or JSONL)
  - Hourly summaries
  - Daily summaries
- Prevents SD card abuse by batching writes

### 3. web.py (Local API Server)
- Lightweight Flask API  
- Provides read-only endpoints for:
  - Latest values
  - Last 24h history
  - Daily totals
  - Raw JSON snapshots  
- Future V2: Could serve a full dashboard UI

These three services run independently but communicate through shared files or local memory.

---

## 3. Data Flow Diagram (ASCII)

### Overall V1 Architecture

            ┌───────────────┐
            │   Energy Meter │
            │  (Acrel ADL400)│
            └───────┬───────┘
                    │ RS-485
                    ▼
            ┌─────────────────┐
            │   poller.py     │
            │  (Modbus Reader)│
            └───────┬────────┘
                    │ JSON snapshot
                    ▼
            ┌─────────────────┐
            │   logger.py     │
            │ (Data Storage)  │
            └───────┬────────┘
                    │ CSV/JSONL logs
                    ▼
            ┌─────────────────┐
            │    web.py       │
            │ (Local API)     │
            └───────┬────────┘
                    │ HTTP (localhost)
                    ▼
            ┌─────────────────┐
            │ Future Dashboard│
            │   (V2 / V3)     │
            └─────────────────┘

---

## 4. Poller Architecture (poller.py)

### Responsibilities
1. Open RS-485 serial connection  
2. Request batches of Modbus registers  
3. Decode + scale meter values  
4. Package results into a structured dict  
5. Write JSON to:
   - `/var/solthrive/data/latest.json` (recommended)
   - Memory (future V2)
   - Or a local socket

### Polling Interval
- **1–2 seconds** → For real-time responsiveness  
- 5 seconds acceptable for logging-only setups  

### Example Poll Output
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

---

## 5. Logger Architecture (logger.py)

### Purpose
To safely store historical data without burning out the SD card.

### Logging Strategy
- Writes raw snapshots → JSON Lines (jsonl)
- Writes 1-minute aggregated logs → CSV
- Writes daily totals → CSV

### Suggested File Structure

/var/solthrive/
data/
latest.json
history.jsonl
logs/
daily/
monthly/

### Why this matters
- JSONL allows fast appends  
- CSV allows easy external analysis  
- Keeps Pi stable long-term  

---

## 6. Web API (web.py)

A minimal Flask API that serves data like:

### `/api/latest`
Returns latest JSON snapshot.

### `/api/history?hours=24`
Returns last X hours of logs.

### `/api/powerflow`
Returns:
{
"solar_kw": 3.52,
"home_kw": 1.44,
"grid_kw": -2.08
}

### `/api/system`
Returns system metadata.

---

## 7. Software Directory Layout

Recommended:

solthrive-monitoring-v1/
software/
poller.py
logger.py
web.py
config.yaml
requirements.txt

Supporting directories created at runtime:

/var/solthrive/data/
/var/solthrive/logs/

---

## 8. Systemd Services (V1 Deployment)

To run the system automatically:

### poller service:
solthrive-poller.service

### logger service:
solthrive-logger.service

### api service:
solthrive-api.service

Benefits:
- Auto-restart on crash  
- Boot-time startup  
- Robust for field installs  

(We will create the service files in A8.)

---

## 9. Config File Structure (config.yaml)

This defines:
- Serial port  
- Modbus baud rate  
- Register map  
- Logging paths  
- Polling intervals  
- API port  

Example:
serial_port: "/dev/ttyUSB0"
baudrate: 9600
poll_interval: 2
log_dir: "/var/solthrive/logs/"
data_file: "/var/solthrive/data/latest.json"
api_port: 8080

---

## 10. Future Versions (V2 / V3)

### V2:
- Live WebSocket stream  
- Local dashboard UI  
- Auto firmware updates  
- Edge anomaly detection

### V3:
- Cloud sync  
- Remote fleet dashboard  
- Multi-meter support  
- Battery state tracking  
- Contractor portal  

---

## 11. Summary (A5 Complete)

SolThrive V1 software stack is built around:
- poller → Reads data  
- logger → Stores data  
- web.py → Serves data  

This architecture is lightweight, resilient, and designed for future expansion (V2/V3).


