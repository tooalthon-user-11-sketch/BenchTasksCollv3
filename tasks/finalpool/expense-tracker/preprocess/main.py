import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the expense-tracker task."""
    processed = []

    for item in input_data:
        expense = {}

        if "amount" in item:
            expense["amount"] = float(item["amount"])

        if "category" in item:
            expense["category"] = item["category"].strip().title()

        if "date" in item:
            try:
                expense["date"] = datetime.strptime(item["date"], "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                expense["date"] = datetime.now().strftime("%Y-%m-%d")

        if "description" in item:
            expense["description"] = item["description"].strip()

        processed.append(expense)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "amount": "25.50",
            "category": "food",
            "date": "2024-01-15",
            "description": "Lunch at restaurant"
        },
        {
            "amount": "100.00",
            "category": "transport",
            "date": "2024-01-16",
            "description": "Gas"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
