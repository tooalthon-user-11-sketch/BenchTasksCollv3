import json

def evaluate(response, ground_truth):
    """Evaluate the order processor response."""
    score = 0.0
    if response and ground_truth:
        score = 1.0 if "confirmed" in response.lower() else 0.5
    return {"score": score}
