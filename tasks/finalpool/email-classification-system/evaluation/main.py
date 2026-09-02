import json
import os

def main():
    """Evaluate the email-classification-system implementation."""
    email_file = "initial_workspace/emails.json"
    if not os.path.exists(email_file):
        print("No email data file found.")
        return

    with open(email_file) as f:
        emails = json.load(f)

    required_fields = ["subject", "category", "priority"]
    valid_categories = ["Work", "Personal", "Spam", "Promotions", "Social"]
    valid_priorities = ["low", "medium", "high", "urgent"]

    score = 0
    total = len(emails)

    for email in emails:
        if all(field in email for field in required_fields):
            if email["category"] in valid_categories and email["priority"] in valid_priorities:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid emails: {score}/{total}")

if __name__ == "__main__":
    main()
