import json
import os
from datetime import datetime

def preprocess(input_data):
    """Preprocess input data for the media-organizer task."""
    processed = []

    for media in input_data:
        cleaned = {}

        if "file_path" in media:
            cleaned["file_path"] = media["file_path"].strip()

        if "file_type" in media:
            cleaned["file_type"] = media["file_type"].strip().lower()

        if "tags" in media:
            cleaned["tags"] = [tag.strip().lower() for tag in media["tags"]]

        if "created_date" in media:
            try:
                cleaned["created_date"] = datetime.strptime(media["created_date"], "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                cleaned["created_date"] = datetime.now().strftime("%Y-%m-%d")

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "file_path": "  /path/to/photo.jpg  ",
            "file_type": "  image  ",
            "tags": ["  vacation  ", "  beach  "],
            "created_date": "  2024-01-15  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
