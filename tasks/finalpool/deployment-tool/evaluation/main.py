import json
import os

def main():
    """Evaluate the deployment-tool implementation."""
    deployment_file = "initial_workspace/deployments.json"
    if not os.path.exists(deployment_file):
        print("No deployment data file found.")
        return

    with open(deployment_file) as f:
        deployments = json.load(f)

    required_fields = ["version", "environment", "status"]
    valid_environments = ["dev", "staging", "production"]
    valid_statuses = ["pending", "in_progress", "completed", "failed", "rolled_back"]

    score = 0
    total = len(deployments)

    for deployment in deployments:
        if all(field in deployment for field in required_fields):
            if deployment["environment"] in valid_environments and deployment["status"] in valid_statuses:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid deployments: {score}/{total}")

if __name__ == "__main__":
    main()
