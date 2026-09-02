import json

def preprocess(input_data):
    """Preprocess input data for the data-validator task."""
    processed = []

    for record in input_data:
        cleaned = {}

        for key, value in record.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
            else:
                cleaned[key] = value

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "name": "  John Doe  ",
            "email": "  john@example.com  ",
            "age": "  30  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
