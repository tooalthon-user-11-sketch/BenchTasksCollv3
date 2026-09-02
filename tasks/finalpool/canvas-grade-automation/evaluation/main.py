import json
import os

def main():
    """Evaluate the canvas-grade-automation implementation."""
    grades_file = "initial_workspace/grades.json"
    if not os.path.exists(grades_file):
        print("No grades file found.")
        return

    with open(grades_file) as f:
        grades = json.load(f)

    required_fields = ["student_id", "assignment", "score"]

    score = 0
    total = len(grades)

    for grade in grades:
        if all(field in grade for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid grades: {score}/{total}")

if __name__ == "__main__":
    main()
