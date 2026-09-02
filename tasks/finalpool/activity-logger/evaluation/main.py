import json
import os

def main():
    """Evaluate the activity-logger implementation."""
    activities_file = "initial_workspace/activities.json"
    if not os.path.exists(activities_file):
        print("No activities file found.")
        return

    with open(activities_file) as f:
        activities = json.load(f)

    required_fields = ["user", "action", "timestamp"]

    score = 0
    total = len(activities)

    for activity in activities:
        if all(field in activity for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid activities: {score}/{total}")

if __name__ == "__main__":
    main()
