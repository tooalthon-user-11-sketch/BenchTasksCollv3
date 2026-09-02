import json
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the content-scheduler task."""
    processed = []

    for item in input_data:
        cleaned = {}

        if "content_id" in item:
            cleaned["content_id"] = item["content_id"].strip()

        if "publish_time" in item:
            try:
                cleaned["publish_time"] = datetime.strptime(item["publish_time"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                cleaned["publish_time"] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        if "platform" in item:
            cleaned["platform"] = item["platform"].strip().lower()

        if "content" in item:
            cleaned["content"] = item["content"].strip()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "content_id": "  post-123  ",
            "publish_time": "  2024-01-15T09:00:00  ",
            "platform": "  blog  ",
            "content": "  Hello, world!  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
