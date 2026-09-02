import json
import os

def main():
    """Evaluate the data-analytics implementation."""
    # Check if analysis files exist
    analysis_file = "initial_workspace/analysis_results.json"
    if not os.path.exists(analysis_file):
        print("No analysis results file found.")
        return

    with open(analysis_file) as f:
        results = json.load(f)

    required_fields = ["dataset", "metrics", "insights"]

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
