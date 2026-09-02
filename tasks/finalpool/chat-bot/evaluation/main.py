import json
import os

def main():
    """Evaluate the chat-bot implementation."""
    conversation_file = "initial_workspace/conversations.json"
    if not os.path.exists(conversation_file):
        print("No conversation file found.")
        return

    with open(conversation_file) as f:
        conversations = json.load(f)

    required_fields = ["user_message", "bot_response"]

    score = 0
    total = len(conversations)

    for conv in conversations:
        if all(field in conv for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid conversations: {score}/{total}")

if __name__ == "__main__":
    main()
