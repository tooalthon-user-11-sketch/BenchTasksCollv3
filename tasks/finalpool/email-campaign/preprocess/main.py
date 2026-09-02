import json

def preprocess(input_data):
    """Preprocess input data for the email-campaign task."""
    processed = []

    for campaign in input_data:
        cleaned = {}

        if "name" in campaign:
            cleaned["name"] = campaign["name"].strip()

        if "audience" in campaign:
            cleaned["audience"] = campaign["audience"].strip()

        if "content" in campaign:
            cleaned["content"] = campaign["content"].strip()

        if "schedule" in campaign:
            cleaned["schedule"] = campaign["schedule"]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "name": "  New Product Launch  ",
            "audience": "  Customers  ",
            "content": "  Check out our new product!  ",
            "schedule": "2024-01-20T09:00:00"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
