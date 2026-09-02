import json

def evaluate(response, ground_truth):
    """Evaluate the network analyzer response."""
    # Basic evaluation logic
    score = 0.0
    if response and ground_truth:
        score = 1.0 if "anomaly" in response.lower() else 0.5
    return {"score": score}
