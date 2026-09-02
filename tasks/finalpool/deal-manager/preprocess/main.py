import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the deal-manager task."""
    processed = []

    for deal in input_data:
        cleaned = {}

        if "name" in deal:
            cleaned["name"] = deal["name"].strip()

        if "value" in deal:
            cleaned["value"] = float(deal["value"])

        if "stage" in deal:
            cleaned["stage"] = deal["stage"].strip().lower()

        if "expected_close_date" in deal:
            try:
                cleaned["expected_close_date"] = datetime.strptime(deal["expected_close_date"], "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                cleaned["expected_close_date"] = datetime.now().strftime("%Y-%m-%d")

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "name": "  Acme Corp  ",
            "value": "  50000  ",
            "stage": "  Negotiation  ",
            "expected_close_date": "2024-06-30"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
