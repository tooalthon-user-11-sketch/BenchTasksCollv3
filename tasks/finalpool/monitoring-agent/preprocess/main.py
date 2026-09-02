import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the monitoring-agent task."""
    processed = []

    for metric in input_data:
        cleaned = {}

        if "timestamp" in metric:
            try:
                cleaned["timestamp"] = datetime.strptime(metric["timestamp"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                cleaned["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        if "cpu_usage" in metric:
            cleaned["cpu_usage"] = float(metric["cpu_usage"])

        if "memory_usage" in metric:
            cleaned["memory_usage"] = float(metric["memory_usage"])

        if "hostname" in metric:
            cleaned["hostname"] = metric["hostname"].strip()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "timestamp": "  2024-01-15T12:00:00  ",
            "cpu_usage": "  45.2  ",
            "memory_usage": "  62.8  ",
            "hostname": "  server-01  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
