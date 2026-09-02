import json
import os

def main():
    """Evaluate the task-scheduler implementation."""
    # Check if task data file exists
    task_file = "initial_workspace/tasks.json"
    if not os.path.exists(task_file):
        print("No task data file found.")
        return

    with open(task_file) as f:
        tasks = json.load(f)

    # Validate structure
    required_fields = ["title", "due_date", "priority"]
    valid_priorities = ["low", "medium", "high", "urgent"]

    score = 0
    total = len(tasks)

    for task in tasks:
        if all(field in task for field in required_fields):
            if task["priority"] in valid_priorities:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid tasks: {score}/{total}")

    # Generate summary
    priorities = {}
    for task in tasks:
        if "priority" in task:
            priorities[task["priority"]] = priorities.get(task["priority"], 0) + 1

    print("\nPriority Summary:")
    for pri, count in priorities.items():
        print(f"  {pri}: {count}")

if __name__ == "__main__":
    main()
