## SolThrive Monitoring V1 — Software Stack

This directory contains the **runtime software** for the SolThrive Monitoring V1 system running on a Raspberry Pi.

The Pi is responsible for:

- Polling the Modbus energy meter (RS-485)
- Converting raw registers into real-world units (V, A, W, kWh)
- Storing historical data on disk
- Serving a local HTTP API for dashboards and tools

If the hardware is the body, this folder is the brain.

---

## 1. Directory Contents

text
software/
  poller.py          # Reads Modbus registers from the meter
  logger.py          # Writes snapshots & summaries to disk
  web.py             # Local HTTP API server (Flask)
  config.yaml        # Core runtime configuration
  requirements.txt   # Python dependencies

For a full conceptual overview, see:

* docs/A5_Software_Architecture.md

---

## 2. Runtime Overview

Three main services run on the Pi:

1. **poller.py**

   * Talks to the RS-485 meter
   * Reads registers defined in the Modbus register map (A4)
   * Applies scaling (÷10, ÷100, etc.)
   * Writes a JSON snapshot to disk

2. **logger.py**

   * Watches for new snapshots
   * Appends raw data to history logs (JSONL)
   * Writes 1-minute / daily aggregates (CSV)

3. **web.py**

   * Exposes a local HTTP API (/api/latest, /api/history, etc.)
   * Intended for dashboards, installers, and future mobile apps

These are normally run as **systemd services**, but can also be run manually during development.

---

## 3. Install & Setup (On the Pi)

### 3.1 Clone the Repo

cd /opt
sudo git clone https://github.com/nigel-solthrive/solthrive-monitoring-v1.git
sudo chown -R pi:pi solthrive-monitoring-v1
cd solthrive-monitoring-v1/software

> Replace pi:pi with your actual user if different.

### 3.2 Install Python Dependencies

pip3 install -r requirements.txt

Typical dependencies include:

* pymodbus
* pyserial
* flask
* pyyaml

(Exact list is in requirements.txt)

### 3.3 Create Data Directories

sudo mkdir -p /var/solthrive/data
sudo mkdir -p /var/solthrive/logs/daily
sudo mkdir -p /var/solthrive/logs/monthly
sudo chmod -R 777 /var/solthrive

These paths are referenced in config.yaml.

---

## 4. Configuration (config.yaml)

config.yaml defines how the software talks to the meter and where it stores data.

**Example structure:**

serial_port: "/dev/ttyUSB0"
baudrate: 9600
modbus_address: 1
poll_interval: 2           # Seconds
log_dir: "/var/solthrive/logs/"
data_dir: "/var/solthrive/data/"
latest_file: "/var/solthrive/data/latest.json"
history_file: "/var/solthrive/data/history.jsonl"
api_port: 8080

Key fields:

* **serial_port**: RS-485 adapter device path (usually /dev/ttyUSB0)
* **baudrate**: Modbus baud (9600 recommended)
* **modbus_address**: Meter slave address (default 1 for most Acrel units)
* **poll_interval**: Seconds between snapshots (1–5s)
* **log_dir / data_dir**: Where logs & snapshots live
* **api_port**: HTTP port for web.py

> Any time you change serial settings or register layout, update config.yaml and restart services.

---

## 5. Running Services Manually (Dev Mode)

### 5.1 Run the Poller

cd /opt/solthrive-monitoring-v1/software
python3 poller.py

Expected:

* Periodic logs in the terminal
* A file at /var/solthrive/data/latest.json being updated every cycle

> For a one-shot read (debugging):
> python3 poller.py --once (if supported in your version)

### 5.2 Run the Logger

python3 logger.py

Expected:

* history.jsonl growing over time
* Daily CSV files created in /var/solthrive/logs/daily/

### 5.3 Run the API

python3 web.py

Then from another machine on the LAN:

curl http://<pi-ip>:8080/api/latest
curl http://<pi-ip>:8080/api/history?hours=1
curl http://<pi-ip>:8080/api/system

You should see JSON responses with current values.

---

## 6. Systemd Service Integration (Production Mode)

In production, each script runs as a **systemd service** so it:

* Starts at boot
* Restarts on crash
* Logs to journalctl

Typical service names (example):

* solthrive-poller.service
* solthrive-logger.service
* solthrive-api.service

### 6.1 Enable Services

sudo systemctl enable solthrive-poller
sudo systemctl enable solthrive-logger
sudo systemctl enable solthrive-api

### 6.2 Start Services

sudo systemctl start solthrive-poller
sudo systemctl start solthrive-logger
sudo systemctl start solthrive-api

### 6.3 Check Status

sudo systemctl status solthrive-poller
sudo systemctl status solthrive-logger
sudo systemctl status solthrive-api

### 6.4 View Logs

journalctl -u solthrive-poller -f
journalctl -u solthrive-logger -f
journalctl -u solthrive-api -f

---

## 7. Data Files & Formats

### 7.1 Latest Snapshot

**File:** /var/solthrive/data/latest.json
**Format:**

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

### 7.2 Raw History

**File:** /var/solthrive/data/history.jsonl
**Format:** one JSON object per line:

{"timestamp": "...", "voltage_l1": ..., ...}
{"timestamp": "...", "voltage_l1": ..., ...}

### 7.3 Aggregated Logs

* /var/solthrive/logs/daily/YYYY-MM-DD.csv
* (Optional) monthly rollups in /var/solthrive/logs/monthly/

---

## 8. API Endpoints (Local Only, V1)

Served by web.py:

* GET /api/latest
  Returns latest snapshot.

* GET /api/history?hours=N
  Returns last N hours of data.

* GET /api/powerflow
  Returns a simplified view:

  {
    "solar_kw": 3.52,
    "home_kw": 1.44,
    "grid_kw": -2.08
  }

* GET /api/system
  Returns system metadata (device info, versions, etc. — implementation-dependent).

> V2 introduces WebSockets and a local dashboard. This README focuses on the V1 stack.

---

## 9. Development Notes & Extensibility

### 9.1 Changing the Register Map

If you change meters or add additional measurements:

1. Update the Modbus register definitions in poller.py.
2. Keep scaling factors consistent with **A4 — Modbus Register Map**.
3. Extend the JSON snapshot structure carefully; avoid breaking existing fields.
4. Update any dashboard or client code that expects specific keys.

### 9.2 Supporting Additional Channels

You can extend the system to:

* Monitor subpanels
* Monitor dedicated loads (EV, HVAC, etc.)
* Add new CT channels if the meter supports them

Approach:

* Add new registers in poller.py
* Add new fields to JSON snapshots
* Adjust logger & API as needed

### 9.3 Performance Tuning

If CPU or I/O becomes an issue:

* Increase poll_interval in config.yaml
* Batch register reads into fewer Modbus calls
* Reduce logging frequency / verbosity
* Move heavy analytics off the Pi (V2/V3 cloud integration)

---

## 10. Troubleshooting

### No data in `latest.json`?

* Check serial_port and modbus_address in config.yaml
* Confirm /dev/ttyUSB0 exists
* Check RS-485 wiring (A ↔ A, B ↔ B, GND ↔ GND)
* Run poller.py manually and watch for exceptions

### API not responding?

* Confirm web.py is running:

  sudo systemctl status solthrive-api
  
* Check api_port in config.yaml
* Make sure no firewall is blocking port 8080

### Strange negative values?

* Check CT orientation (arrows)
* Validate sign conventions in poller.py scaling logic

---

## 11. Roadmap Hooks (V2/V3)

This V1 software stack is designed to evolve into:

* **V2**:

  * Local dashboard UI
  * WebSocket streaming
  * OTA updates
  * Health & diagnostics layer

* **V3**:

  * Cloud ingestion
  * Fleet monitoring
  * Installer & homeowner portals

The current architecture (poller → logger → API) is intentionally simple and modular to support these future steps.

---

## 12. Contact / Notes

This software is part of the **SolThrive Monitoring V1** project.

For architecture docs, see:

* docs/A1_CT_Specs.md
* docs/A2_Meter_Selection.md
* docs/A3_Pi_Wiring.md`
* docs/A4_Modbus_Register_Map.md
* docs/A5_Software_Architecture.md
* docs/Appendix_A1_Glossary.md

