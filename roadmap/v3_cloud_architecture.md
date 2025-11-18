SolThrive Monitoring — V3 Cloud Architecture

---

## 1. Purpose of V3

V3 takes SolThrive from a **single-site local appliance** to a **multi-site, cloud-connected monitoring platform**.

Core goals:

* Cloud-based **fleet monitoring** for many deployed systems
* **Installer / contractor portal**
* **Homeowner portal** for viewing their own data
* Secure **device → cloud** data pipeline
* Long-term storage, analytics, and reporting
* Foundation for **future grid services, VPP, and DER integration**

V3 is the bridge from “nice tool” to “real platform.”

---

## 2. High-Level V3 Objectives

| Area         | Objective                                    |
| ------------ | -------------------------------------------- |
| Connectivity | Securely sync devices to the cloud           |
| Storage      | Central time-series data for all sites       |
| UX           | Web portals for installers + homeowners      |
| Analytics    | Fleet health, savings, alerts, anomalies     |
| Identity     | Multi-tenant user / site / device model      |
| Security     | Strong auth, encryption, and least-privilege |
| Operations   | OTA, remote debug, and fleet-wide updates    |

V3 must build on V2, not replace it. Local mode remains first-class.

---

## 3. System Overview

### 3.1 Components

* **Device Layer**

  * SolThrive Pi (V2-ready)
  * Local poller + logger + API + OTA + health

* **Cloud Ingestion**

  * HTTPS / MQTT endpoint for timeseries + events
  * Authenticated and encrypted

* **Cloud Storage**

  * Time-series database (TSDB)
  * Relational DB for metadata (sites, devices, users, installers)

* **Application Layer**

  * REST / GraphQL API for portals and tools
  * Background jobs (aggregation, alerts, anomaly detection)

* **Frontends**

  * Installer Portal (multi-site view)
  * Homeowner Portal (single-site view)
  * Internal Admin console (support / debugging)

---

## 4. Device → Cloud Data Flow

### 4.1 V3 Data Types

The device will send:

1. **Telemetry Snapshots**

   * Timestamped watts, amps, volts, kWh
   * 15–60 sec interval (configurable)

2. **Daily Summaries**

   * Solar kWh, home kWh, import/export kWh
   * Self-consumption, solar offset, peak demand

3. **Health / State Events**

   * Meter offline
   * CT unplugged / polarity issue
   * Pi disk low
   * Service restart events

4. **Version / Identity**

   * Device serial / ID
   * Firmware version
   * Site ID

### 4.2 Transport

**Primary option:** HTTPS POST with JSON

* Endpoint: `https://api.solthrive.cloud/v1/ingest`
* Authentication: device token (see security section)
* TLS enforced

**Alternative (future):** MQTT TLS

* For more real-time streaming or IoT-scale deployments

---

## 5. Cloud Ingestion Layer

### 5.1 Ingestion API

Endpoint structure (example):

* `POST /v1/ingest/telemetry`
* `POST /v1/ingest/daily`
* `POST /v1/ingest/health`

Responsibilities:

* Validate device token
* Validate payload shape
* Normalize timestamps (UTC)
* Enqueue into a message queue or streaming platform (e.g., Kafka/Kinesis/PubSub)
* Return simple status (`ok` / `error` + code)

### 5.2 Rate & Volume

Target initial scale:

* Hundreds → low thousands of devices
* Telemetry every 30–60 seconds
* Daily summaries once per day per site
* Health events on change

Architecture must be **horizontally scalable** but doesn’t need hyperscale complexity in V3.

---

## 6. Data Storage Architecture

### 6.1 Time-Series Telemetry Store

Use a TSDB or equivalent (examples: TimescaleDB, InfluxDB, ClickHouse, etc.).

Store:

* `site_id`
* `device_id`
* `timestamp`
* `solar_kw`
* `home_kw`
* `grid_kw`
* `voltage_l1`, `voltage_l2`
* `pf`, etc.

Partition by:

* Date (daily partition)
* Site or device for large fleets

### 6.2 Relational Metadata Store

Standard relational DB (Postgres or similar) for:

* **Users**

  * id, name, email, role, org, etc.

* **Installers / Contractors**

  * org_id, contact info, permissions

* **Sites**

  * site_id, name, address (or generalized label)
  * timezone
  * system size (kW)
  * meter + CT config
  * rate plan (optional)

* **Devices**

  * device_id, serial
  * site_id
  * model/firmware
  * last_seen_at
  * status

* **Alerts / Events**

  * type, severity, message, created_at, site_id, device_id

### 6.3 Aggregated Tables

Precomputed daily/monthly:

* Per-site:

  * solar_kwh
  * home_kwh
  * import_kwh
  * export_kwh
  * self_consumption %
  * solar_offset %
  * estimated savings

* Per-installer:

  * total production across fleet
  * number of active/alerting systems

---

## 7. Identity, Users, and Tenancy

### 7.1 User Types

* **Homeowner**

  * Sees only their own site(s)

* **Installer / Contractor**

  * Sees multiple sites they installed / manage

* **Internal Admin**

  * Full visibility, used for support/debug

### 7.2 Tenancy Model

* Sites are always owned by **one primary tenant** (usually homeowner or organization).
* Installers get scoped access to:

  * Sites they are assigned to
  * Alert dashboards
  * Commissioning tools

### 7.3 Authentication & Authorization

* JWT-based auth or OAuth2
* Role-based access control (RBAC)
* All API calls must be authenticated except minimal “landing info” routes.

---

## 8. Security & Device Identity

### 8.1 Device Identity

Each SolThrive Pi is provisioned with:

* A unique **device ID**
* A pre-shared **device token** or certificate

Stored on the Pi at:

```
/etc/solthrive/device_id
/etc/solthrive/device_token
```

### 8.2 Secure Transport

* All telemetry sent via **TLS**
* No plain HTTP
* No open inbound ports required on device (device always dials out)

### 8.3 Device Registration Flow

1. Installer installs/commissions device (V1/V2 procedures).
2. Device calls `POST /v1/device/register` with serial + token + installer code.
3. Cloud associates device with:

   * Site
   * Installer
   * User account (when homeowner is onboarded)

---

## 9. Cloud APIs (External)

### 9.1 Public API Surface (for portals / integrations)

* `GET /api/v1/sites`
* `GET /api/v1/sites/{id}`
* `GET /api/v1/sites/{id}/telemetry?from=...&to=...`
* `GET /api/v1/sites/{id}/daily?from=...&to=...`
* `GET /api/v1/sites/{id}/alerts`
* `GET /api/v1/installers/{id}/fleet`
* `GET /api/v1/device/{id}/health`

These back the portals and potential partner integrations.

### 9.2 Internal APIs

* Management tools
* Admin dashboard
* Device provisioning
* Bulk operations (e.g., fleet OTA)

---

## 10. Portals & UX

### 10.1 Homeowner Portal

Views:

* Real-time powerflow
* Today / week / month solar and usage
* Bill-savings estimate
* Outage/alert notifications
* Simple system status (OK / Warning / Error)

### 10.2 Installer Portal

Views:

* Fleet list (all sites)
* Filters: “Alerting”, “Offline”, “Commissioning”, “Healthy”
* Per-site:

  * Field test results
  * CT/meter config
  * Last communication
  * Remote logs preview

Tools:

* Remotely trigger diagnostics
* Mark issues as resolved
* Export data for warranty/utility issues

### 10.3 Internal Admin Tools

* Global search by device ID or site
* Force device deactivation
* Secure remote debug hooks (e.g., temporary SSH tunnel via support channel)

---

## 11. Analytics & Alerts

### 11.1 Alert Types

* Device offline (no data for X minutes/hours)
* Meter offline
* CT zero/flatline (hardware fault)
* PV flatline during known daylight windows
* Voltage out-of-range
* Excessive export / unusual load pattern (optional)

Alerts stored in DB and surfaced via:

* Portal views
* Email/webhook in later versions

### 11.2 Basic Analytics

* Daily solar vs usage
* Self-consumption %
* Offset %
* Estimated $ savings (needs tariff config)
* Comparison vs previous period

---

## 12. Operational Concerns

### 12.1 Observability

Cloud services must have:

* Metrics (latency, error rates)
* Centralized logs
* Traces for critical ingestion paths

Devices already provide V2 health endpoints — V3 adds a fleet-level view.

### 12.2 Deployment Strategy

* Use containerized services (Docker/Kubernetes or equivalent)
* Staging and production environments
* Blue/green for API updates

### 12.3 Backup & Retention

* Database backups (daily)
* TSDB retention: e.g., 1–3 years full granularity, longer in aggregates
* GDPR-like export/delete capability per site if needed later

---

## 13. Scope Boundaries for V3

**In scope:**

* Cloud ingestion for Pi devices
* Fleet portals
* Basic alerts & analytics
* Secure identity and device registration
* Reasonable multi-tenant architecture

**Out of scope (future V4+):**

* Full-blown utility/DSO integrations
* VPP aggregation and dispatch
* Direct DER control (e.g., battery, EV, HVAC control)
* Automated rate optimization / advanced tariff engines
* Third-party marketplace integrations

---

## 14. Summary

V3 adds the **cloud nervous system** around SolThrive:

* Local-first edge device (V1/V2)
* Secure cloud ingestion
* Fleet and site-level views
* Portals for installers and homeowners
* Alerts, health, and long-term analytics

With V3, SolThrive Monitoring evolves from a single-site tool into a **platform** capable of supporting real deployments, partnerships, and future grid-interactive features.

---
