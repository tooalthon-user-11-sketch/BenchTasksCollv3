import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the alert-system task."""
    processed = []

    for alert in input_data:
        cleaned = {}

        if "type" in alert:
            cleaned["type"] = alert["type"].strip().lower()

        if "severity" in alert:
            cleaned["severity"] = alert["severity"].strip().lower()

        if "message" in alert:
            cleaned["message"] = alert["message"].strip()

        if "status" in alert:
            cleaned["status"] = alert["status"].strip().lower()

        if "timestamp" in alert:
            try:
                cleaned["timestamp"] = datetime.strptime(alert["timestamp"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                cleaned["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "type": "  cpu  ",
            "severity": "  High  ",
            "message": "  CPU usage above 90%  ",
            "status": "  Triggered  ",
            "timestamp": "  2024-01-15T12:00:00  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
