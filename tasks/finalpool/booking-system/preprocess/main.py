import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the booking-system task."""
    processed = []

    for booking in input_data:
        cleaned = {}

        if "customer" in booking:
            cleaned["customer"] = booking["customer"].strip()

        if "service" in booking:
            cleaned["service"] = booking["service"].strip()

        if "date" in booking:
            try:
                cleaned["date"] = datetime.strptime(booking["date"], "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                cleaned["date"] = datetime.now().strftime("%Y-%m-%d")

        if "status" in booking:
            cleaned["status"] = booking["status"].strip().lower()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "customer": "  John Doe  ",
            "service": "  Table for 4  ",
            "date": "  2024-01-15  ",
            "status": "  Confirmed  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
