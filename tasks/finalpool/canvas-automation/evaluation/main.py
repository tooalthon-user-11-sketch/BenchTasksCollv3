import json
import os

def main():
    """Evaluate the canvas-automation implementation."""
    config_file = "initial_workspace/automation_config.json"
    if not os.path.exists(config_file):
        print("No automation config file found.")
        return

    with open(config_file) as f:
        config = json.load(f)

    required_fields = ["course_id", "automations"]

    score = 0
    total = 2

    if "course_id" in config:
        score += 1

    if "automations" in config and len(config["automations"]) > 0:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
