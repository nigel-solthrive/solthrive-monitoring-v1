Appendix A0 — Documentation Overview
SolThrive Monitoring V1 — Enhanced Engineering Edition
(Based on APPENDIX_OVERVIEW.md)
1. Purpose
This appendix provides a high-level overview of all SolThrive Monitoring V1 documentation, including:
How the A-series (A1–A5) fits together
How to use the engineering PDF
Where supporting material and checklists live
How to navigate the repository as an installer, engineer, or contributor
This appendix is intended to act as your table of contents and onboarding guide.
2. Repository Layout
The V1 repository follows a clear engineering structure:
solthrive-monitoring-v1/
  README.md

  docs/
    SolThrive_V1_FullSpec_Manual_Simple.pdf
    A1_CT_Specs.md
    A2_Meter_Selection.md
    A3_Pi_Wiring.md
    A4_Modbus_Register_Map.md
    A5_Software_Architecture.md
    Appendix_A0_Overview.md
    Appendix_A1_Glossary.md

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
This structure allows engineers to easily find hardware specs, software logic, and installation procedures.
3. Core Document Set (A-Series)
A1 — CT Specifications
Physical CT selection, ratings, accuracy, polarity, and placement.
A2 — Meter Selection
Required features of the energy meter, Modbus compatibility, and recommended models.
A3 — Raspberry Pi Wiring
Pi hardware, wiring, RS-485 setup, enclosure recommendations, and field-mounting layout.
A4 — Modbus Register Map
Exact registers the Pi reads, scaling factors, and polling behavior.
A5 — Software Architecture
poller → logger → API pipeline, data flow diagrams, directory layout, systemd services.
This A-series forms the core engineering spec of SolThrive Monitoring V1.
4. Supporting Material
Engineering Manual (PDF)
SolThrive_V1_FullSpec_Manual_Simple.pdf
Includes black-and-white simplified diagrams, installation notes, and appendices A–H.
Field Test Procedures
bench_test_procedure.md — bring-up testing
field_test_procedure.md — in-panel live test steps
Future Roadmaps
V2 plans (dashboard, WebSockets)
V3 cloud architecture (fleet monitoring, remote sync)
5. How to Use This Documentation
If you are an installer:
Follow A1 → A2 → A3 → Bench Test → Field Test.
If you are a developer:
Start at A4 → A5 → software/ directory.
If you are reviewing the system:
Read this appendix → A5 → PDF manual.
If you want to extend or modify the system:
Start with V2/V3 roadmap documents.
6. Summary
This appendix provides:
A map of the entire documentation ecosystem
A clean entry point into the A-series
A guide for installers, engineers, and reviewers
A bridge between the engineering PDF and GitHub markdown files
The full set creates a complete, professional-grade reference for SolThrive Monitoring V1.
