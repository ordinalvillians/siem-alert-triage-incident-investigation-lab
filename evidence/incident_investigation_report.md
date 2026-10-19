# SIEM Alert Triage and Incident Investigation Report

## 1. Project Overview

This lab demonstrates a basic Security Operations Center (SOC) workflow for reviewing, prioritising, and documenting security alerts.

The dataset is simulated for learning purposes. It does not represent logs collected from a live organisation or prove that a real security incident occurred.

## 2. Objectives

- Review a structured dataset of security alerts.
- Summarise alerts by reported severity.
- Assign preliminary investigation priorities.
- Recommend appropriate follow-up actions.
- Document findings, limitations, and escalation considerations.

## 3. Dataset Summary

Eight simulated alert records were analysed.

| Reported severity | Alert count |
|---|---:|
| Critical | 2 |
| High | 3 |
| Medium | 2 |
| Low | 1 |
| **Total** | **8** |

The dataset includes repeated failed logins, successful logins following failures, unusual PowerShell activity, a malware detection, and a normal successful login.

## 4. Key Triage Findings

### A1005 — Malware Detection

**Reported severity:** Critical  
**Preliminary priority:** P1

The endpoint protection alert reports a malware detection on `WIN-CLIENT04` associated with user `mbrown`.

Recommended follow-up:
- Review the endpoint protection detection details.
- Identify the detected file, process, detection time, and affected endpoint.
- Check available endpoint telemetry for related activity.
- Follow the organisation's incident response and containment procedures if the detection is validated.

The simulated record alone does not establish whether malware executed or caused harm.

### A1007 — Successful Login After Repeated Failures

**Reported severity:** Critical  
**Preliminary priority:** P1

The dataset records a successful login for the `administrator` account on `WIN-SRV02` after repeated authentication failures. The listed source address is `198.51.100.23`.

Recommended follow-up:
- Correlate the failed and successful authentication events by timestamp, account, host, and source address.
- Verify whether the login was expected and authorised.
- Review available authentication and endpoint records for related activity.
- Escalate if the activity cannot be explained or is confirmed to be unauthorised.

The source address belongs to a documentation-reserved range and is not evidence of a real attacker.

### A1002 — Successful Login After Failures

**Reported severity:** High  
**Preliminary priority:** P1

The record indicates a successful login for `jsmith` on `WIN-CLIENT01` following repeated failures.

Recommended follow-up:
- Compare the timestamps and source information for the related authentication events.
- Confirm the login with the appropriate account owner or administrator.
- Check for related account or endpoint activity.

This pattern warrants investigation but does not independently confirm account compromise.

### A1003 — Repeated Failed Logins Against Administrator

**Reported severity:** High  
**Preliminary priority:** P2

Repeated failures involving the `administrator` account on `WIN-SRV02` warrant review.

Recommended follow-up:
- Group authentication events by account and source.
- Check whether the activity is consistent with expected administrative operations.
- Look for related successful logins or other suspicious events.

### A1004 — Unusual PowerShell Activity

**Reported severity:** High  
**Preliminary priority:** P2

PowerShell activity on `WIN-CLIENT03` was flagged for review.

Recommended follow-up:
- Obtain the actual process command line and parent process.
- Review process execution time and user context.
- Correlate with endpoint protection and other available security records.

The alert description does not include enough technical detail to determine whether the activity was malicious.

### A1001 and A1008 — Repeated Failed Logins

**Reported severity:** Medium  
**Preliminary priority:** P3

These records describe repeated authentication failures involving `jsmith` and `guest`.

Recommended follow-up:
- Review failure frequency, source addresses, and targeted accounts.
- Correlate with other authentication events.
- Raise the priority if additional evidence indicates a broader or ongoing incident.

### A1006 — Successful Login

**Reported severity:** Low  
**Preliminary priority:** P3

The record describes a successful login for `kwilson` on `WIN-CLIENT02`.

Recommended follow-up:
- Compare the event with expected account and access patterns.
- Close as routine only if supporting evidence confirms the activity is expected.

## 5. Investigation Limitations

- All alert records are simulated.
- No live SIEM platform or production telemetry was queried.
- No raw Windows event logs, endpoint process details, or complete authentication timelines were provided.
- The listed source addresses use documentation-reserved IP ranges.
- The assigned priorities are preliminary recommendations based on the supplied alert descriptions and reported severity.
- No alert should be labelled a confirmed security incident without additional evidence.

## 6. Conclusion

The Python triage script successfully processed eight simulated alerts and summarised their reported severity.

The malware detection and successful login after repeated failures were prioritised for urgent review. The remaining alerts were assigned follow-up actions according to their descriptions and reported severity.

In a real SOC environment, an analyst would validate alert details, correlate relevant logs, document supporting evidence, and follow the organisation's escalation procedures before drawing conclusions.

## 7. Evidence Files

- `data/siem_alerts.csv` — simulated alert dataset
- `scripts/triage_alerts.py` — Python triage script
- `evidence/triage_output.txt` — captured script output
- `evidence/incident_investigation_report.md` — this report
