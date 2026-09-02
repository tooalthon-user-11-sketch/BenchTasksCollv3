import json
import os

def main():
    """Evaluate the monitoring-agent implementation."""
    metrics_file = "initial_workspace/metrics.json"
    if not os.path.exists(metrics_file):
        print("No metrics file found.")
        return

    with open(metrics_file) as f:
        metrics = json.load(f)

    required_fields = ["timestamp", "cpu_usage", "memory_usage"]

    score = 0
    total = len(metrics)

    for metric in metrics:
        if all(field in metric for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid metrics: {score}/{total}")

if __name__ == "__main__":
    main()
