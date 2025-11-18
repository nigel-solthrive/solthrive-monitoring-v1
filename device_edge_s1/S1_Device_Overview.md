# SolThrive Edge S1 — Device Overview

## 📦 What Is the SolThrive Edge S1?

The SolThrive Edge S1 is the first-generation **local energy monitoring device** in the SolThrive ecosystem.  
It combines:

- CT-based sensing  
- Modbus metering  
- Raspberry Pi edge processing  
- Local API & data storage  
- Installer-friendly commissioning  

All packaged into a single field-ready hardware unit.

---

## 🎯 Purpose

The Edge S1 enables:

- Real-time solar + home consumption monitoring  
- Local-only operation (no cloud required)  
- Reliable energy visibility for installers & homeowners  
- A foundation for V2 local dashboards and V3 cloud ingestion  

---

## 🔌 Core Functions

- Monitors grid import/export  
- Tracks solar PV generation  
- Measures whole-home load  
- Provides 1–2 second live data via API  
- Logs daily history JSON/CSV  
- Supports future OTA updates  
- Integrates with the SolThrive App ecosystem (V3)

---

## 🧠 Software Platform

The device runs **SolThrive Monitoring V1**, located in `/software/`.

The firmware stack includes:
- `poller.py` (Modbus ingestion)  
- `logger.py` (history logging)  
- `web.py` (local HTTP API)  
- `config.yaml` (device configuration)

---

## 🧩 System Role

The Edge S1 is the **physical appliance** powering the SolThrive monitoring architecture:

- Hardware Device: SolThrive Edge S1
- Software Platform: SolThrive Monitoring V1
- Local UI Roadmap: SolThrive Dashboard V2
- Cloud Platform Roadmap: SolThrive Cloud V3

---

## 🛣 Roadmap for the S-Series Hardware

**S1 (current)**  
- Meter + CT based  
- Raspberry Pi  
- DIN-rail oriented design  
- Basic enclosure  
- Local API  

**S2 (future)**  
- Custom PCB  
- Built-in RS-485  
- Integrated CT ports  
- Optional 4G/LTE module  
- Thermal-optimized enclosure  

**S3 (future)**  
- Professional-grade device  
- Installer tool ecosystem  
- Direct SolThrive Cloud ingestion  
- Advanced diagnostics  
