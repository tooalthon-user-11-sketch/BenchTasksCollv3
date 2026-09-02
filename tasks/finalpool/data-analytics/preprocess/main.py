import json

def preprocess(input_data):
    """Preprocess input data for the data-analytics task."""
    processed = []

    for record in input_data:
        cleaned = {}

        for key, value in record.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
            elif isinstance(value, (int, float)):
                cleaned[key] = value
            else:
                cleaned[key] = str(value)

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "product": "  Widget A  ",
            "sales": "  150  ",
            "region": "  North  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
