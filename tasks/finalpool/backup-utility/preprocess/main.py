import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the backup-utility task."""
    processed = {}

    if "backup_id" in input_data:
        processed["backup_id"] = input_data["backup_id"].strip()

    if "timestamp" in input_data:
        try:
            processed["timestamp"] = datetime.strptime(input_data["timestamp"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            processed["timestamp"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    if "status" in input_data:
        processed["status"] = input_data["status"].strip().lower()

    if "files" in input_data:
        processed["files"] = [file.strip() for file in input_data["files"]]

    return processed

if __name__ == "__main__":
    sample = {
        "backup_id": "  backup-123  ",
        "timestamp": "  2024-01-15T12:00:00  ",
        "status": "  Completed  ",
        "files": ["  file1.txt  ", "  file2.txt  "]
    }
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
