Bench Test Procedure — SolThrive Monitoring V1

---

## **1. Purpose**

This procedure validates the complete SolThrive Monitoring V1 system **on a bench**, before any field installation.
It confirms:

* Raspberry Pi is correctly configured
* RS-485 communication works
* Modbus registers read correctly
* CT scaling is accurate
* Software services run and restart reliably
* Data is logged and accessible via the API
* The system behaves like a production monitoring appliance

This test must pass before moving to the **Field Test Procedure**.

---

## **2. Hardware Required**

| Component                     | Purpose                  |
| ----------------------------- | ------------------------ |
| Raspberry Pi 4 (preferred)    | Controller               |
| 5V/3A PSU                     | Stable Pi power          |
| SD card (16–64GB)             | OS + SolThrive software  |
| USB → RS-485 adapter          | Modbus interface         |
| Acrel ADL200/300/400-CT meter | Energy meter             |
| (1–3) CTs                     | For scaling verification |
| Short lengths of wire         | Powering the meter       |
| Multimeter                    | Voltage confirmation     |

**Optional but helpful:**

* DIN-rail mounting
* USB keyboard + HDMI (for emergency access)

---

## **3. Pre-Test OS Setup**

1. Flash Raspberry Pi OS Lite.
2. Enable:

   * **SSH**
   * **Hostname:** `solthrive-monitor-v1`
3. Update the system:

   ```
   sudo apt update && sudo apt upgrade -y
   ```
4. Install required Python packages:

   ```
   pip3 install -r requirements.txt
   ```
5. Copy the SolThrive software folder into `/opt/solthrive/`.

---

## **4. Physical Wiring Setup**

### **4.1 Power the Meter**

Apply single-phase power to the meter:

```
L1 → Meter L1
L2 → Meter L2
```

Neutral is not required on most models.

Verify with multimeter:

* 120V from L1 → GND
* 120V from L2 → GND
* 240V from L1 → L2

### **4.2 Connect RS-485**

```
USB-RS485 Adapter A  → Meter A
USB-RS485 Adapter B  → Meter B
USB-RS485 Adapter GND → Meter GND
```

Confirm adapter appears as:

```
ls /dev/ttyUSB*
```

Expected:
`/dev/ttyUSB0`

---

## **5. SolThrive Software Bring-Up**

Ensure the directory structure exists:

```
/var/solthrive/data/latest.json
/var/solthrive/data/history.jsonl
/var/solthrive/logs/daily/
```

If not, create them:

```
sudo mkdir -p /var/solthrive/data
sudo mkdir -p /var/solthrive/logs/daily
sudo chmod 777 -R /var/solthrive/
```

---

## **6. Modbus Communication Test**

Run a single register read manually:

```
python3 poller.py --once
```

Expected behavior:

* Reads 10–12 registers
* Prints scaled values
* Writes `/var/solthrive/data/latest.json`

If you get timeout or CRC errors:

* Check A/B wiring
* Check meter baudrate (should be 9600)
* Confirm Modbus address (default: 1)

---

## **7. Validate Scaling Factors**

Look at the raw registers using a Modbus tool:

```
modpoll -m rtu -a 1 -b 9600 -r 6 -c 1 /dev/ttyUSB0
```

Expected format:

* CTs: integer, scaled by ÷100
* Voltage: integer, scaled by ÷10
* Power: raw W

Compare:

* multimeter amps (if available)
* simulated load through CT
* register value ÷ scaling

Accuracy should be within **1–3%** depending on CT.

---

## **8. Validate Snapshot Output**

After running poller:

```
cat /var/solthrive/data/latest.json
```

Expected fields:

```
voltage_l1
voltage_l2
current_l1
current_l2
current_pv
power_total
energy_import
energy_export
timestamp
```

Values should be non-zero (except PV current if no PV simulation).

---

## **9. Logger Test**

Start logger manually:

```
python3 logger.py
```

Check that:

* `history.jsonl` is appended
* Minute logs appear in `/var/solthrive/logs/daily`

Confirm:

```
tail /var/solthrive/data/history.jsonl
```

---

## **10. API Test**

Start `web.py`:

```
python3 web.py
```

In a browser or curl:

```
curl http://<pi-ip>:8080/api/latest
```

Expected JSON output.

Try:

```
/api/history?hours=1
/api/system
/api/powerflow
```

All should respond instantly and without errors.

---

## **11. Systemd Test (Production Behavior)**

Enable services:

```
sudo systemctl enable solthrive-poller
sudo systemctl enable solthrive-logger
sudo systemctl enable solthrive-api
```

Start them:

```
sudo systemctl start solthrive-poller
sudo systemctl start solthrive-logger
sudo systemctl start solthrive-api
```

Check statuses:

```
sudo systemctl status solthrive-poller
sudo systemctl status solthrive-logger
sudo systemctl status solthrive-api
```

Reboot Pi:

```
sudo reboot
```

After boot, confirm all 3 services are ACTIVE/RUNNING.

---

## **12. Final Bench Checklist**

| Test                       | Pass/Fail |
| -------------------------- | --------- |
| Power applied to meter     | ☐         |
| RS-485 detected as ttyUSB0 | ☐         |
| Register read works        | ☐         |
| Scaling validated          | ☐         |
| Latest.json generated      | ☐         |
| History.jsonl updated      | ☐         |
| API responding             | ☐         |
| Systemd auto-starts        | ☐         |

---

## **13. Bench Test Complete**

Once every item is checked off, the system is ready for:

➡ **Field Test Procedure**
➡ **Roadmap V2 integration**
➡ **Dashboard development**
➡ **Installer testing**

---
