import json
import os

def main():
    """Evaluate the content-manager implementation."""
    content_file = "initial_workspace/content.json"
    if not os.path.exists(content_file):
        print("No content file found.")
        return

    with open(content_file) as f:
        content = json.load(f)

    required_fields = ["title", "body", "category"]

    score = 0
    total = len(content)

    for item in content:
        if all(field in item for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid content items: {score}/{total}")

if __name__ == "__main__":
    main()
