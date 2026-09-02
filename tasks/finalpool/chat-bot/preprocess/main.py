import json

def preprocess(input_data):
    """Preprocess input data for the chat-bot task."""
    processed = []

    for conv in input_data:
        cleaned = {}

        if "user_message" in conv:
            cleaned["user_message"] = conv["user_message"].strip()

        if "bot_response" in conv:
            cleaned["bot_response"] = conv["bot_response"].strip()

        if "timestamp" in conv:
            cleaned["timestamp"] = conv["timestamp"]

        processed.append(cleaned)

    return processed

if __name__ == "__main__":
    sample = [
        {
            "user_message": "  Hello  ",
            "bot_response": "  Hi there!  ",
            "timestamp": "2024-01-15T12:00:00"
        }
    ]
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
