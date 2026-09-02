import json
import os

def main():
    """Evaluate the template-engine implementation."""
    template_file = "initial_workspace/template.json"
    if not os.path.exists(template_file):
        print("No template file found.")
        return

    with open(template_file) as f:
        template = json.load(f)

    required_fields = ["name", "content", "placeholders"]

    score = 0
    total = len(required_fields)

    for field in required_fields:
        if field in template:
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Required fields present: {score}/{total}")

if __name__ == "__main__":
    main()
