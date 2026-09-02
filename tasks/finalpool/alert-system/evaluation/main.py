import json
import os

def main():
    """Evaluate the alert-system implementation."""
    alerts_file = "initial_workspace/alerts.json"
    if not os.path.exists(alerts_file):
        print("No alerts file found.")
        return

    with open(alerts_file) as f:
        alerts = json.load(f)

    required_fields = ["type", "severity", "message", "status"]
    valid_severities = ["low", "medium", "high", "critical"]
    valid_statuses = ["triggered", "acknowledged", "resolved", "dismissed"]

    score = 0
    total = len(alerts)

    for alert in alerts:
        if all(field in alert for field in required_fields):
            if alert["severity"] in valid_severities and alert["status"] in valid_statuses:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid alerts: {score}/{total}")

if __name__ == "__main__":
    main()
