import json

def preprocess(input_data):
    """Preprocess input data for the email-classification-system task."""
    processed = []

    for email in input_data:
        cleaned = {}

        if "subject" in email:
            cleaned["subject"] = email["subject"].strip()

        if "body" in email:
            cleaned["body"] = email["body"].strip()

        if "sender" in email:
            cleaned["sender"] = email["sender"].strip()

        if "timestamp" in email:
            cleaned["timestamp"] = email["timestamp"]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "subject": "  Meeting Tomorrow  ",
            "body": "  Let's discuss the project.  ",
            "sender": "  alice@example.com  ",
            "timestamp": "2024-01-15T10:00:00"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
