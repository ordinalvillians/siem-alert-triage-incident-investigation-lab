import csv
from collections import Counter
from pathlib import Path

DATA_FILE = Path("data/siem_alerts.csv")

def assign_priority(alert):
    alert_type = alert["alert_type"].strip().lower()
    severity = alert["severity"].strip().lower()

    if alert_type == "malware detection":
        return "P1", "Escalate for immediate investigation"

    if alert_type == "successful login after failures":
        return "P1", "Investigate authentication sequence"

    if alert_type == "unusual powershell activity":
        return "P2", "Review process and command evidence"

    if alert_type == "repeated failed logins":
        if severity == "high":
            return "P2", "Review account and source patterns"
        return "P3", "Monitor and correlate related events"

    if severity == "critical":
        return "P1", "Escalate for immediate investigation"

    if severity == "high":
        return "P2", "Investigate and gather context"

    return "P3", "Review during routine triage"


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: Dataset not found: {DATA_FILE}")
        return

    with DATA_FILE.open(newline="", encoding="utf-8") as file:
        alerts = list(csv.DictReader(file))

    if not alerts:
        print("ERROR: No alert records found.")
        return

    severity_counts = Counter(
        alert["severity"].strip().title() for alert in alerts
    )

    print("=" * 65)
    print("SIEM ALERT TRIAGE REPORT")
    print("Dataset: Simulated security alerts")
    print("=" * 65)
    print(f"Total alerts analysed: {len(alerts)}")

    print("\nSEVERITY SUMMARY")
    for severity in ["Critical", "High", "Medium", "Low"]:
        print(f"{severity}: {severity_counts.get(severity, 0)}")

    print("\nALERT-BY-ALERT TRIAGE")
    print("-" * 65)

    for alert in alerts:
        priority, action = assign_priority(alert)

        print(
            f"{alert['alert_id']} | "
            f"Severity: {alert['severity']} | "
            f"Priority: {priority}"
        )
        print(
            f"  Host: {alert['hostname']} | "
            f"User: {alert['username']}"
        )
        print(f"  Alert: {alert['alert_type']}")
        print(f"  Recommended action: {action}")
        print()

    print("NOTE: Priorities are preliminary triage recommendations.")
    print("The dataset is simulated; alerts do not prove compromise.")
    print("=" * 65)


if __name__ == "__main__":
    main()
