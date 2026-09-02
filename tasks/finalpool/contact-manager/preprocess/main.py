import json

def preprocess(input_data):
    """Preprocess input data for the contact-manager task."""
    processed = []

    for contact in input_data:
        cleaned = {}

        if "name" in contact:
            cleaned["name"] = contact["name"].strip()

        if "email" in contact:
            cleaned["email"] = contact["email"].strip().lower()

        if "phone" in contact:
            cleaned["phone"] = contact["phone"].strip()

        if "company" in contact:
            cleaned["company"] = contact["company"].strip()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "name": "  John Doe  ",
            "email": "  JOHN@EXAMPLE.COM  ",
            "phone": "  555-1234  ",
            "company": "  Acme Corp  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
