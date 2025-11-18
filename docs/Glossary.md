Appendix A1 — Engineering Glossary

---

## **Introduction**

This glossary defines all important electrical, solar, networking, hardware, software, and monitoring terms used throughout the SolThrive Monitoring V1 project.
Definitions are written in clean, practical language with context for why the term matters to SolThrive.

---

# **1. Electrical Concepts**

### **Voltage (V)**

Electrical “pressure” that pushes current through a circuit.

### **Current (A)**

The flow of electricity through a conductor; read by CTs.

### **Power (W / kW)**

Instantaneous energy usage or production.
Calculation: **Power = Voltage × Current**.

### **Energy (kWh)**

Total electricity consumed or produced over time.

### **Split-Phase (120/240V)**

Standard U.S. residential service with L1, L2, neutral.

### **Power Factor (PF)**

How effectively electrical power is used (0–1.0).

### **Reactive Power (VAR)**

Non-working power; relevant for AC motors.

### **THD (Total Harmonic Distortion)**

Electrical noise/distortion; future V2 metric.

### **Backfeed Breaker**

Breaker through which the inverter feeds solar energy into the panel.

### **Service Entrance**

Point where utility power enters the home.

### **Burden Resistor**

Resistor attached to CT secondary; ensures safe voltage levels.

---

# **2. Solar Monitoring Terms**

### **Production**

Solar power output from the PV system.

### **Consumption**

Home load demand.

### **Import / Export**

Power drawn from or sent to the grid.

### **Net Metering**

Billing method where exported kWh offset imported kWh.

### **Aggregate Power**

Total instantaneous power at a measurement point.

### **PV Array**

Group of solar modules wired together.

### **Optimizer**

Panel-level power management device.

### **Panel-Level Monitoring**

Module-level telemetry provided by OEM inverter systems.

### **Inverter Telemetry**

Data accessed through OEM monitoring (not universal).

---

# **3. Hardware & Field Components**

### **CT (Current Transformer)**

Clamp-on sensor measuring current via magnetic induction.

### **Split-Core CT**

Hinged design for retrofit installs.

### **Solid-Core CT**

Requires removing conductor; high accuracy.

### **Polarity Arrow**

Indicates direction of current flow expectation.

### **RS-485**

Two-wire differential communication standard used for Modbus RTU.

### **Modbus RTU**

Protocol used by the Pi to read registers from the meter.

### **DIN Rail**

Standard mounting system for electrical equipment.

### **Ferrules**

Crimped sleeves for stranded wire terminations.

---

# **4. Software & Data Concepts**

### **JSON**

Lightweight data format used for snapshots.

### **JSONL**

“JSON Lines”. One JSON object per line; ideal for logs.

### **CSV**

Comma-separated text file; used for minute/daily summaries.

### **API Endpoint**

URL path that serves data.

### **REST API**

Simple HTTP-based API.

### **WebSocket**

Protocol for real-time streaming (planned for V2).

### **Poller**

Service that reads Modbus and generates snapshots.

### **Logger**

Service that stores data long-term.

### **Daemon / Systemd Service**

Background process with auto-start and auto-restart capability.

### **Timeseries Data**

Data indexed by timestamps.

### **Sampling Interval**

How often the system reads the meter.

---

# **5. Networking Terms**

### **LAN**

Local network of the home/installation site.

### **Ethernet**

Preferred wired network connection.

### **Wi-Fi**

Wireless connection; acceptable but less reliable.

### **DHCP**

Router assigns IP automatically.

### **Static IP**

Manually assigned IP; future-proof for commercial installs.

### **Port**

Communication endpoint (e.g., 8080 for API).

### **Latency**

Round-trip delay for packet transmission.

---

# **6. Raspberry Pi Concepts**

### **GPIO**

General-purpose input/output pins.

### **UART**

Serial communication interface; RS-485 adapters often use UART internally.

### **Serial Port (`/dev/ttyUSB0`)**

Device path used for Modbus communication.

### **System Logs**

Linux system activity logs.

### **Cron Job**

Scheduled recurring task (not used in V1).

### **Restart Policy**

Defines how services behave on crash (systemd restart=always).

---

# **7. Advanced / Future Concepts**

### **Edge Computing**

Processing data locally rather than in the cloud.

### **Cloud Sync**

Uploading summaries to a cloud backend.

### **Firmware Update (OTA)**

Remote updates without physical access.

### **Fleet Monitoring**

Centralized view of many deployed systems.

### **Load Disaggregation**

Machine learning to identify appliances from power signatures.

### **Anomaly Detection**

Detect unusual consumption or inverter failures.

---

# **Glossary Complete**

This glossary now matches the style, clarity, and quality of the entire A-series and is ready for GitHub.

---

# ✅ Appendices Completed

Your documentation suite is now fully rebuilt:

* A1
* A2
* A3
* A4
* A5
* Appendix A0
* Appendix A1

If you want, I can now:

### ➜ Build a **master README**

### ➜ Create a **navigation sidebar**

### ➜ Add **cross-links** between all A-sections

### ➜ Design a **docs/ folder structure**

### ➜ Generate a **printable combined PDF** of the entire A-series

Just tell me where you want to go next, Nigel.
