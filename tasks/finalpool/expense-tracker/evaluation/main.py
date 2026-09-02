import json
import os

def main():
    """Evaluate the expense-tracker implementation."""
    expense_file = "initial_workspace/expenses.json"
    if not os.path.exists(expense_file):
        print("No expense data file found.")
        return

    with open(expense_file) as f:
        expenses = json.load(f)

    required_fields = ["amount", "category", "date"]
    valid_categories = ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Other"]

    score = 0
    total = len(expenses)

    for exp in expenses:
        if all(field in exp for field in required_fields):
            if exp["category"] in valid_categories:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid expenses: {score}/{total}")

    categories = {}
    for exp in expenses:
        if "category" in exp:
            categories[exp["category"]] = categories.get(exp["category"], 0) + exp.get("amount", 0)

    print("\nCategory Summary:")
    for cat, total in categories.items():
        print(f"  {cat}: ${total:.2f}")

if __name__ == "__main__":
    main()
