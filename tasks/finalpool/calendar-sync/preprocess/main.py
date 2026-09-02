import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the calendar-sync task."""
    processed = []

    for event in input_data:
        cleaned = {}

        if "title" in event:
            cleaned["title"] = event["title"].strip()

        if "start_time" in event:
            try:
                cleaned["start_time"] = datetime.strptime(event["start_time"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                cleaned["start_time"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        if "end_time" in event:
            try:
                cleaned["end_time"] = datetime.strptime(event["end_time"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                cleaned["end_time"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        if "calendar" in event:
            cleaned["calendar"] = event["calendar"].strip().lower()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "title": "  Team Meeting  ",
            "start_time": "  2024-01-15T10:00:00  ",
            "end_time": "  2024-01-15T11:00:00  ",
            "calendar": "  google  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
