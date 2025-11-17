# SolThrive Monitoring V1

Universal solar monitoring prototype for a 20A, 120/240V residential system.

This project measures:
- Solar PV production
- Home load consumption
- Net grid import/export

using:
- Split-core CTs
- A 3‑channel Modbus energy meter (RS‑485)
- A Raspberry Pi gateway (poller + logger + local dashboard)

## Repository Structure

```text
solthrive-monitoring-v1/
  README.md

  docs/
    SolThrive_V1_FullSpec_Manual_Simple.pdf
    APPENDIX_OVERVIEW.md

  software/
    poller.py
    logger.py
    web.py
    config.yaml
    requirements.txt

  hardware/
    meter_selection.md
    ct_specs.md
    pi_wiring.md

  test/
    bench_test_procedure.md
    field_test_procedure.md

  roadmap/
    v2_plans.md
    v3_cloud_architecture.md
```

## High-Level Architecture

- CTs on:
  - Main L1
  - Main L2
  - PV breaker (20A)
- 3‑channel Modbus energy meter reads current & voltage
- RS‑485 (A/B) → USB adapter → Raspberry Pi
- Pi runs:
  - `poller.py` (reads Modbus)
  - `logger.py` (CSV logging)
  - `web.py` (Flask dashboard)
  - watchdog/systemd for auto‑recovery

## Status

- This repo is a **V1 engineering sandbox** for Nigel + friend.
- Code is starter/skeleton and will be refined once the actual meter model and register map are chosen.