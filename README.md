# 🚀 **SolThrive Monitoring V1 — Device Model S1**

**Local Solar + Home Energy Monitoring System (CT-based, Modbus, Raspberry Pi)**
**Version:** V1.0
**Status:** Active / Under Development

---

# 📘 **Overview**

SolThrive Monitoring V1 is the first-generation **local-only** energy monitoring platform designed for:

* Residential solar systems
* Grid import/export monitoring
* CT-based whole-home measurement
* Raspberry Pi edge processing
* Modbus-based energy meters

This system provides real-time powerflow data, local logs, and an installer-friendly commissioning flow — with a roadmap toward V2 local dashboards and V3 cloud fleet management.

SolThrive V1 is fully open and modular, designed for expansion into local dashboards, OTA updates, cloud ingestion, and multi-site fleet management.

---

# 📂 **Repository Structure**

```
solthrive-monitoring-v1/
│
├── docs/                  # A1–A5 engineering specifications
│   ├── A1_CT_Specs.md
│   ├── A2_Meter_Selection.md
│   ├── A3_Pi_Wiring.md
│   ├── A4_Modbus_Register_Map.md
│   ├── A5_Software_Architecture.md
│   ├── Appendix_A0_Overview.md
│   └── Appendix_A1_Glossary.md
│
├── software/              # Pi runtime software (poller, logger, API)
│   ├── poller.py
│   ├── logger.py
│   ├── web.py
│   ├── config.yaml
│   ├── requirements.txt
│   └── README.md          # How to install & run the Pi stack
│
├── roadmap/               # Future versions (V2 local UI, V3 cloud)
│   ├── v2_plans.md
│   └── v3_cloud_architecture.md
│
└── test/                  # Commissioning procedures
    ├── bench_test_procedure.md
    └── field_test_procedure.md
```

---

# 🧠 **What SolThrive Monitoring Does**

### ✔ Measures:

* Solar PV production (CT channel)
* Home consumption (main CTs)
* Grid import/export
* Voltage & power factor
* Accumulated energy (kWh)

### ✔ Provides:

* JSON snapshots updated every 1–2 seconds
* History logs (JSONL + daily CSV)
* Local-only HTTP API
* Simple commissioning tools

### ✔ Supports:

* Acrel ADL200/300/400 series energy meters
* Standard split-core CTs
* RS-485 (Modbus RTU)
* Raspberry Pi 4 recommended

---

# 🔌 **Hardware Requirements**

### **Mandatory**

* Raspberry Pi (4 recommended)
* USB → RS-485 adapter
* Acrel ADL-series Modbus energy meter
* 2–3 CTs (split-core)
* Panel access for CT installation

### **Optional**

* DIN-rail enclosure
* Surge protection
* Cable management kit

See **A2, A3, and A1** in `/docs` for full details.

---

# ⚙️ **Software Architecture (High-Level)**

SolThrive V1 includes three main processes:

### **1. poller.py**

Reads Modbus registers → generates real-world values → writes `latest.json`.

### **2. logger.py**

Watches snapshots → logs 1-minute and daily data → builds historical files.

### **3. web.py**

Serves a local API:

```
/api/latest
/api/history
/api/powerflow
/api/system
```

Full details: `docs/A5_Software_Architecture.md`
Implementation guide: `software/README.md`

---

# 🧪 **Commissioning Flow**

Commissioning consists of two phases:

### **1. Bench Test**

* Validate RS-485 communication
* Confirm snapshots + scaling
* Test API, logs, services
* Stored in `test/bench_test_procedure.md`

### **2. Field Test**

* Install CTs in the panel
* Validate orientation (mains & PV)
* Confirm sign conventions
* Validate import/export
* Stored in `test/field_test_procedure.md`

---

# 🛣️ **Roadmap: V1 → V2 → V3**

### **V1 (This Repo)**

* Local-only monitoring
* Modbus polling
* History logs
* Basic API
* Commissioning procedures
* No cloud

### **V2 (Local UI + OTA)**

See: `roadmap/v2_plans.md`

Includes:

* Local dashboard (browser UI)
* WebSocket live updates
* OTA update system
* Health monitoring
* New API features
* Layered config system

### **V3 (Cloud Fleet Platform)**

See: `roadmap/v3_cloud_architecture.md`

Includes:

* Device → cloud ingestion
* Installer portal
* Homeowner portal
* Alerts & analytics
* Time-series cloud storage
* Identity + multi-site structure

---

# 🔧 **Installation (Quickstart)**

1. Flash Raspberry Pi OS (Lite recommended)
2. Clone repo into `/opt/solthrive-monitoring-v1/`
3. Install dependencies:

```
pip3 install -r software/requirements.txt
```

4. Create data directories:

```
sudo mkdir -p /var/solthrive/data
sudo mkdir -p /var/solthrive/logs/daily
```

5. Configure serial port & Modbus:

Edit `software/config.yaml`.

6. Start services:

```
sudo systemctl start solthrive-poller
sudo systemctl start solthrive-logger
sudo systemctl start solthrive-api
```

---

# 🔍 **Testing the API**

```
curl http://<pi-ip>:8080/api/latest
curl http://<pi-ip>:8080/api/history?hours=1
curl http://<pi-ip>:8080/api/powerflow
curl http://<pi-ip>:8080/api/system
```

---

# 💡 **Why This Project Exists**

SolThrive Monitoring V1 was created to provide:

* A **vendor-agnostic**, CT-based residential energy monitor
* That is **installer-friendly**
* **Locally controlled**
* Fully transparent
* Open-source
* And expandable into a full fleet platform

This repo is the first major step toward SolThrive’s long-term home energy and microgrid ecosystem.

---

# 🤝 **Contributing**

PRs are welcome.
If you add features, please:

* Follow consistent file structure
* Do not break existing JSON snapshot formats
* Update the appropriate doc files (`A1–A5`, roadmap, or software README)
* Test `poller.py`, `logger.py`, and `web.py` together
* Maintain clean commit messages

---

# 📬 **Contact**

SolThrive Renewables
[https://solthriverenewables.com](https://solthriverenewables.com)
[support@solthriverenewables.com](mailto:support@solthriverenewables.com)

---

