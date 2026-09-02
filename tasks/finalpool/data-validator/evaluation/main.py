import json
import os

def main():
    """Evaluate the data-validator implementation."""
    validation_file = "initial_workspace/validation_results.json"
    if not os.path.exists(validation_file):
        print("No validation results file found.")
        return

    with open(validation_file) as f:
        results = json.load(f)

    required_fields = ["dataset", "rules_applied", "issues_found"]

    score = 0
    total = len(results)

    for result in results:
        if all(field in result for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid results: {score}/{total}")

if __name__ == "__main__":
    main()
