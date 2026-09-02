import json

def preprocess(input_data):
    """Preprocess input data for the cms-builder task."""
    processed = {}

    for key, value in input_data.items():
        if isinstance(value, str):
            processed[key] = value.strip()
        else:
            processed[key] = value

    return processed

if __name__ == "__main__":
    sample = {
        "platform": "  wordpress  ",
        "version": "  6.0  ",
        "plugins": ["  akismet  ", "  yoast  "]
    }
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
