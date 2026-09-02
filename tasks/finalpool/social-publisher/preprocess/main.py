import json

def preprocess(input_data):
    """Preprocess input data for the social-publisher task."""
    processed = {}
    for key, value in input_data.items():
        if isinstance(value, str):
            processed[key] = value.strip()
        else:
            processed[key] = value
    return processed

if __name__ == "__main__":
    sample = {
        "content": "  Hello, world!  ",
        "platform": "twitter",
        "schedule": "2024-01-01T12:00:00"
    }
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
