import json

def preprocess(input_data):
    """Preprocess input data for the deployment-tool task."""
    processed = []

    for deployment in input_data:
        cleaned = {}

        if "version" in deployment:
            cleaned["version"] = deployment["version"].strip()

        if "environment" in deployment:
            cleaned["environment"] = deployment["environment"].strip().lower()

        if "status" in deployment:
            cleaned["status"] = deployment["status"].strip().lower()

        if "timestamp" in deployment:
            cleaned["timestamp"] = deployment["timestamp"]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "version": "  1.0.0  ",
            "environment": "  Staging  ",
            "status": "  Completed  ",
            "timestamp": "2024-01-15T12:00:00"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
