import json
import os

def main():
    """Evaluate the load-balancer implementation."""
    config_file = "initial_workspace/load_balancer_config.json"
    if not os.path.exists(config_file):
        print("No load balancer config file found.")
        return

    with open(config_file) as f:
        config = json.load(f)

    required_fields = ["servers", "algorithm", "health_check"]
    valid_algorithms = ["round_robin", "least_connections", "ip_hash", "weighted"]

    score = 0
    total = 3

    if "servers" in config and len(config["servers"]) > 0:
        score += 1

    if "algorithm" in config and config["algorithm"] in valid_algorithms:
        score += 1

    if "health_check" in config:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
