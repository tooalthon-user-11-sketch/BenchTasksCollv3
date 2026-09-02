import json

def preprocess(input_data):
    """Preprocess input data for the crm-system task."""
    processed = []

    for contact in input_data:
        cleaned = {}

        if "name" in contact:
            cleaned["name"] = contact["name"].strip()

        if "email" in contact:
            cleaned["email"] = contact["email"].strip().lower()

        if "company" in contact:
            cleaned["company"] = contact["company"].strip()

        if "phone" in contact:
            cleaned["phone"] = contact["phone"].strip()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "name": "  John Doe  ",
            "email": "  JOHN@EXAMPLE.COM  ",
            "company": "  Acme Corp  ",
            "phone": "  555-1234  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
