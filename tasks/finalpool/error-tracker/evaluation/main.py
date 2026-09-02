import json
import os

def main():
    """Evaluate the error-tracker implementation."""
    # Check if error data file exists
    error_file = "initial_workspace/errors.json"
    if not os.path.exists(error_file):
        print("No error data file found.")
        return

    with open(error_file) as f:
        errors = json.load(f)

    # Validate structure
    required_fields = ["type", "severity", "message"]
    valid_severities = ["low", "medium", "high", "critical"]

    score = 0
    total = len(errors)

    for err in errors:
        if all(field in err for field in required_fields):
            if err["severity"] in valid_severities:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid errors: {score}/{total}")

    # Generate summary
    severities = {}
    for err in errors:
        if "severity" in err:
            severities[err["severity"]] = severities.get(err["severity"], 0) + 1

    print("\nSeverity Summary:")
    for sev, count in severities.items():
        print(f"  {sev}: {count}")

if __name__ == "__main__":
    main()
