import json
import os

def main():
    """Evaluate the deal-manager implementation."""
    deal_file = "initial_workspace/deals.json"
    if not os.path.exists(deal_file):
        print("No deal data file found.")
        return

    with open(deal_file) as f:
        deals = json.load(f)

    required_fields = ["name", "value", "stage", "expected_close_date"]
    valid_stages = ["lead", "qualified", "proposal", "negotiation", "closed_won", "closed_lost"]

    score = 0
    total = len(deals)

    for deal in deals:
        if all(field in deal for field in required_fields):
            if deal["stage"] in valid_stages:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid deals: {score}/{total}")

if __name__ == "__main__":
    main()
