import json
import os

def main():
    """Evaluate the content-scheduler implementation."""
    schedule_file = "initial_workspace/schedule.json"
    if not os.path.exists(schedule_file):
        print("No schedule file found.")
        return

    with open(schedule_file) as f:
        schedule = json.load(f)

    required_fields = ["content_id", "publish_time", "platform"]

    score = 0
    total = len(schedule)

    for item in schedule:
        if all(field in item for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid schedule items: {score}/{total}")

if __name__ == "__main__":
    main()
