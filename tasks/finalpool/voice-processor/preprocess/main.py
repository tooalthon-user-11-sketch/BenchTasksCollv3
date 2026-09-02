import json

def preprocess(input_data):
    """Preprocess input data for the voice-processor task."""
    processed = []

    for audio in input_data:
        cleaned = {}

        if "file_path" in audio:
            cleaned["file_path"] = audio["file_path"].strip()

        if "language" in audio:
            cleaned["language"] = audio["language"].strip().lower()

        if "duration" in audio:
            cleaned["duration"] = float(audio["duration"])

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "file_path": "  /path/to/audio.mp3  ",
            "language": "  english  ",
            "duration": "  120.5  "
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
