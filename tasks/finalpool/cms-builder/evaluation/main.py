import json
import os

def main():
    """Evaluate the cms-builder implementation."""
    config_file = "initial_workspace/cms_config.json"
    if not os.path.exists(config_file):
        print("No CMS config file found.")
        return

    with open(config_file) as f:
        config = json.load(f)

    required_fields = ["platform", "version", "plugins"]

    score = 0
    total = len(required_fields)

    for field in required_fields:
        if field in config:
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Required fields present: {score}/{total}")

if __name__ == "__main__":
    main()
