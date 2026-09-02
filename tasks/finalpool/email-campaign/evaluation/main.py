import json
import os

def main():
    """Evaluate the email-campaign implementation."""
    campaign_file = "initial_workspace/campaigns.json"
    if not os.path.exists(campaign_file):
        print("No campaign data file found.")
        return

    with open(campaign_file) as f:
        campaigns = json.load(f)

    required_fields = ["name", "audience", "content", "schedule"]

    score = 0
    total = len(campaigns)

    for campaign in campaigns:
        if all(field in campaign for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid campaigns: {score}/{total}")

if __name__ == "__main__":
    main()
