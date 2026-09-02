import json

def preprocess(input_data):
    """Preprocess input data for the translation-api task."""
    processed = []

    for translation in input_data:
        cleaned = {}

        if "source_text" in translation:
            cleaned["source_text"] = translation["source_text"].strip()

        if "target_language" in translation:
            cleaned["target_language"] = translation["target_language"].strip().lower()

        if "source_language" in translation:
            cleaned["source_language"] = translation["source_language"].strip().lower()

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "source_text": "  Hello, world  ",
            "target_language": "  french  ",
            "source_language": "  english  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
