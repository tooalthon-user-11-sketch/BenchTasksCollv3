import json

def preprocess(input_data):
    """Preprocess input data for the canvas-automation task."""
    processed = {}

    for key, value in input_data.items():
        if isinstance(value, str):
            processed[key] = value.strip()
        elif isinstance(value, list):
            processed[key] = [item.strip() if isinstance(item, str) else item for item in value]
        else:
            processed[key] = value

    return processed

if __name__ == "__main__":
    sample = {
        "course_id": "  12345  ",
        "automations": ["  grading  ", "  enrollment  "]
    }
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
