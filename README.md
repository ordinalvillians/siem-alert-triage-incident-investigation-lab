# SIEM Alert Triage and Incident Investigation Lab

## Overview

This beginner-level cybersecurity project demonstrates a basic Security Operations Center (SOC) workflow using Python and a structured dataset of simulated security alerts.

The project focuses on reviewing alert severity, assigning preliminary investigation priorities, recommending follow-up actions, and documenting investigation limitations.

**Important:** All alert records are simulated for educational purposes. No production SIEM data or live security incidents were used.

## Objectives

- Analyse structured security alert records with Python.
- Summarise alerts by reported severity.
- Assign preliminary triage priorities.
- Recommend investigation and escalation actions.
- Produce a written incident investigation report.
- Practise evidence-based documentation without treating alerts as confirmed incidents.

## Tools and Technologies

- Kali Linux
- Python 3
- Python CSV module
- Linux terminal
- Git and GitHub

## Project Structure

```text
Day10-SIEM-Alert-Triage/
├── data/
│   └── siem_alerts.csv
├── evidence/
│   ├── incident_investigation_report.md
│   └── triage_output.txt
├── screenshots/
├── scripts/
│   └── triage_alerts.py
└── README.md
```

## How to Run

Clone or download the repository, then open a terminal in the project directory.

Run the triage script:

```bash
python3 scripts/triage_alerts.py
```

To save the output while displaying it in the terminal:

```bash
python3 scripts/triage_alerts.py | tee evidence/triage_output.txt
```

## Simulated Alert Summary

The dataset contains eight records.

| Severity | Count |
|---|---:|
| Critical | 2 |
| High | 3 |
| Medium | 2 |
| Low | 1 |
| **Total** | **8** |

Alert types include repeated failed logins, successful logins following failures, unusual PowerShell activity, a malware detection, and a normal successful login.

## Investigation Approach

1. Load the CSV dataset using Python.
2. Count alerts by reported severity.
3. Assign preliminary priorities using simple triage rules.
4. Recommend initial follow-up actions for each alert.
5. Document findings, evidence requirements, and limitations.

## Key Learning Outcomes

- Reading structured security data with Python.
- Distinguishing reported severity from analyst-assigned priority.
- Recognising authentication patterns that may warrant further investigation.
- Identifying the additional evidence needed to investigate endpoint and PowerShell alerts.
- Documenting uncertainty and avoiding unsupported conclusions.

## Limitations

This is a learning simulation, not a production SIEM integration.

The project does not ingest live logs, query an endpoint detection platform, confirm malicious activity, or automatically contain threats. Priorities are preliminary recommendations and should be validated against the organisation's procedures and available evidence.

## Future Improvements

- Add input validation and clearer handling of malformed CSV records.
- Expand correlation logic for related authentication alerts.
- Add unit tests for priority-assignment rules.
- Integrate a larger, clearly labelled sample dataset.
- Explore the same investigation workflow in a SIEM platform.

## Author

Oluwaseun Adebayo

Cybersecurity portfolio project focused on foundational SOC analysis and incident investigation.
