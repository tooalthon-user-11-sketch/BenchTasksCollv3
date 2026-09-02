import json

def preprocess(input_data):
    """Preprocess input data for the content-manager task."""
    processed = []

    for item in input_data:
        cleaned = {}

        if "title" in item:
            cleaned["title"] = item["title"].strip()

        if "body" in item:
            cleaned["body"] = item["body"].strip()

        if "category" in item:
            cleaned["category"] = item["category"].strip().lower()

        if "tags" in item:
            cleaned["tags"] = [tag.strip().lower() for tag in item["tags"]]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "title": "  AI Trends  ",
            "body": "  The future of AI...  ",
            "category": "  Technology  ",
            "tags": ["  AI  ", "  Tech  "]
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
