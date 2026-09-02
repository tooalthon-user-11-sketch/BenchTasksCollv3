import json
import os

def main():
    """Evaluate the crm-system implementation."""
    # Check if CRM data files exist
    contacts_file = "initial_workspace/contacts.json"
    if not os.path.exists(contacts_file):
        print("No contacts file found.")
        return

    with open(contacts_file) as f:
        contacts = json.load(f)

    required_fields = ["name", "email", "company"]

    score = 0
    total = len(contacts)

    for contact in contacts:
        if all(field in contact for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid contacts: {score}/{total}")

if __name__ == "__main__":
    main()
