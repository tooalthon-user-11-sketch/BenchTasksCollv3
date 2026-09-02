import json

def preprocess(input_data):
    """Preprocess input data for the image-processor task."""
    processed = []

    for image in input_data:
        cleaned = {}

        if "file_path" in image:
            cleaned["file_path"] = image["file_path"].strip()

        if "operations" in image:
            cleaned["operations"] = [op.strip().lower() for op in image["operations"]]

        if "output_format" in image:
            cleaned["output_format"] = image["output_format"].strip().lower()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "file_path": "  /path/to/image.jpg  ",
            "operations": ["  resize  ", "  enhance  "],
            "output_format": "  png  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
