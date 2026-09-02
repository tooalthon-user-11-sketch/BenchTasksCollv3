import json

def preprocess(input_data):
    """Preprocess input data for the load-balancer task."""
    processed = {}

    if "servers" in input_data:
        processed["servers"] = [server.strip() for server in input_data["servers"]]

    if "algorithm" in input_data:
        processed["algorithm"] = input_data["algorithm"].strip().lower()

    if "health_check" in input_data:
        processed["health_check"] = input_data["health_check"]

    return processed

if __name__ == "__main__":
    sample = {
        "servers": ["  server-1  ", "  server-2  ", "  server-3  "],
        "algorithm": "  Round Robin  ",
        "health_check": {"interval": 30, "timeout": 5}
    }
    result = preprocess(sample)
    print(json.dumps(result, indent=2))
