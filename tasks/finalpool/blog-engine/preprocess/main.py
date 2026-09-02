import json

def preprocess(input_data):
    """Preprocess input data for the blog-engine task."""
    processed = []

    for post in input_data:
        cleaned = {}

        if "title" in post:
            cleaned["title"] = post["title"].strip()

        if "content" in post:
            cleaned["content"] = post["content"].strip()

        if "status" in post:
            cleaned["status"] = post["status"].strip().lower()

        if "categories" in post:
            cleaned["categories"] = [cat.strip().lower() for cat in post["categories"]]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "title": "  AI Trends  ",
            "content": "  The future of AI...  ",
            "status": "  Published  ",
            "categories": ["  Technology  ", "  AI  "]
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
