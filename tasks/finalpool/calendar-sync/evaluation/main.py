import json
import os

def main():
    """Evaluate the calendar-sync implementation."""
    events_file = "initial_workspace/events.json"
    if not os.path.exists(events_file):
        print("No events file found.")
        return

    with open(events_file) as f:
        events = json.load(f)

    required_fields = ["title", "start_time", "end_time", "calendar"]

    score = 0
    total = len(events)

    for event in events:
        if all(field in event for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid events: {score}/{total}")

if __name__ == "__main__":
    main()
