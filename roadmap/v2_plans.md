SolThrive Monitoring — V2 Roadmap

---

# **1. Purpose of V2**

SolThrive V2 builds directly on top of the fully stable V1 system.
The goal is to transition from a solid “engineering prototype” into a **semi-productized residential monitoring system**.

V2 introduces:

* A **local dashboard UI**
* **Real-time live streaming** (WebSockets)
* **Over-the-air update framework**
* **System health monitoring**
* **Enhanced configuration system**
* **Security upgrades**
* **Better data retention & rollup policies**
* **Future-facing expansion ports** (inverter telemetry, ESS, EV)

V2 is where SolThrive Monitoring starts behaving like a real home energy appliance.

---

# **2. High-Level V2 Objectives**

| Category      | Objective                                       |
| ------------- | ----------------------------------------------- |
| UI            | Build an on-device dashboard served by the Pi   |
| Data          | Enable real-time streaming (WebSockets)         |
| Reliability   | Add heartbeat, watchdog, error reporting        |
| Updates       | Add OTA update system for Python services       |
| Architecture  | Modularize services into packages               |
| Security      | Strengthen API & authentication                 |
| Config        | Introduce layered config system                 |
| Analytics     | Add basic powerflow and daily summary endpoints |
| Extensibility | Add multi-meter & future inverter pathways      |

---

# **3. V2 Functional Requirements**

## **3.1 Local Dashboard (Primary Goal)**

A new endpoint on the Pi, e.g.:

```
http://<pi-ip>:8080/dashboard
```

Must support:

* Real-time gauge for:

  * Solar production
  * Home consumption
  * Grid import/export
* 24-hour mini graph
* Connection status indicator
* CT orientation warnings
* Error indicators (RS-485, scaling failures)

**Tech Options:**

* Lightweight web UI (HTML/JS)
* Canvas- or SVG-based graphs
* Templated via Flask or static served

---

## **3.2 WebSocket Real-Time Stream**

Endpoint:

```
ws://<pi-ip>:8080/ws
```

Pushes:

* Snapshot updates every 1s
* System heartbeat
* Error flags
* Data drop detection

This removes the need for rapid `/api/latest` polling.

---

## **3.3 OTA Update Framework**

Version-controlled deployments:

### Requirements:

* Update server folder on GitHub or private S3 bucket
* Pi checks update manifest daily
* Downloads updated Python modules safely
* Rolls back if service fails
* Sends alert if update fails

### Flow:

```
Pi → Fetch manifest
   → Download patch
   → Graceful service restart
   → Validate system recovering
```

---

## **3.4 Error & Self-Diagnostics Layer**

Add a new internal module:

```
/software/diagnostics/
    healthcheck.py
    watchdog.py
    error_flags.py
```

Monitors:

* RS-485 communication errors
* Snapshot staleness
* Disk space thresholds
* Uptime and reboot count
* Poll timing drift
* API stall

Outputs to:

```
/api/system
/api/health
```

V2 must detect:

* “CT unplugged”
* “Meter not responding”
* “Data stale”
* “Low storage”
* “Service crash”

---

## **3.5 Configuration Layer (Major Rework)**

Move from single YAML → multi-file layered config:

```
/etc/solthrive/
    base.yaml
    network.yaml
    meter.yaml
    api.yaml
    logging.yaml
```

And allow overrides:

```
/boot/solthrive/config.yaml
```

Supports:

* Custom meters
* Multiple CT scaling profiles
* Multi-inverter setups (future)
* Rate tariff profiles (for savings calculations)

---

## **3.6 API Enhancements**

New endpoints:

### **`/api/daily_summary`**

Returns:

```
{
  "solar_kwh": ...,
  "home_kwh": ...,
  "import_kwh": ...,
  "export_kwh": ...,
  "self_consumption": ...,
  "solar_offset": ...
}
```

### **`/api/health`**

Returns:

```
{
  "modbus_status": "ok",
  "api_status": "ok",
  "storage": "12GB_free",
  "last_snapshot_age_sec": 1,
  "errors": []
}
```

### **`/api/device`**

Device metadata:

* serial
* firmware version
* uptime
* last update check

---

# **4. Software Architecture Changes for V2**

## **4.1 Convert scripts → service modules**

Reorganize:

```
software/
    solthrive/
        poller/
        logger/
        api/
        utils/
        diagnostics/
```

Use imports instead of standalone scripts.

---

## **4.2 Service-Level Plugability**

Allow additional data sources in future:

* Modbus inverters (SolarEdge, SMA, Enphase Gateway)
* CT-based subpanel monitors
* Battery telemetry (LFP)
* EV chargers (OCPP)

V2 lays groundwork even if unused initially.

---

## **4.3 Performance Improvements**

* Switch to **batch register reads**
* Reduce CPU wake-ups
* Add caching layer for API
* Separate async WebSocket loop from API loop

---

# **5. Security Enhancements**

## **5.1 API Token Authentication**

* Token file in `/etc/solthrive/token`
* Token required for:

  * `/api/history`
  * `/api/daily_summary`
  * `/api/device`

## **5.2 SSH Hardening**

* Disable password login
* Key-based authentication only
* Fail2ban for brute-force protection

## **5.3 Firewall Rules**

Allow only:

* 22 (SSH)
* 8080 (local UI)
  Block WAN access by default.

---

# **6. Data Retention Policies**

Define:

* Keep 1-minute logs for 30 days
* Aggregate into daily summaries
* Monthly rollups
* Prune anything older than 365 days (configurable)

This reduces storage consumption and keeps JSONL manageable.

---

# **7. Developer Tooling Improvements**

### Tools added in V2:

* Internal CLI utility:

  ```
  solthrive-cli check
  solthrive-cli logs
  solthrive-cli version
  ```
* Debug endpoint:

  ```
  /api/debug
  ```
* Structured error logs with timestamps
* Bench & field auto-validation scripts

---

# **8. V2 Feature Matrix**

| Feature                  | Status   | Notes                    |
| ------------------------ | -------- | ------------------------ |
| Local dashboard          | New      | V2 anchor feature        |
| WebSocket stream         | New      | Replaces polling         |
| OTA updates              | New      | Essential for fleets     |
| Health monitoring        | New      | Must detect meter faults |
| Enhanced API             | Upgrade  | Adds powerful endpoints  |
| Security overhaul        | Upgrade  | Token + firewall         |
| Config layering          | Upgrade  | Major redesign           |
| Architecture restructure | Internal | Preps V3                 |

---

# **9. Stretch Goals (If Time Permits)**

### Nice-to-haves for V2, non-blocking:

* Animation-based real-time powerflow UI
* Dark mode dashboard
* Multi-language support
* Optional local notifications
* OS upgrade automation
* CT auto-orientation detection (phase comparison)
* Custom MQTT publisher adapter

---

# **10. What V2 Does NOT Include**

These are explicitly deferred to V3:

* Cloud portal
* Remote installer dashboard
* Device registration system
* TLS-secured device→cloud ingestion
* Payment/billing integration
* Multi-site fleet view
* Mobile app
* Grid services/demand response integration

V2 remains **local-only** by design.

---

# **11. Summary**

SolThrive V2 transforms the system from:

> **“A stable engineering prototype”**
> to
> **“A polished local monitoring appliance with real-time updates, OTA, diagnostics, and a proper UI.”**

When V2 is completed, SolThrive will be ready for:

* real installers
* pilot trials
* homeowner beta testers
* preparation for V3 cloud ecosystem

---
