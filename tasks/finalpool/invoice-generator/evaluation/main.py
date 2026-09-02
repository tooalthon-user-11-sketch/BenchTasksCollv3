import json
import os

def main():
    """Evaluate the invoice-generator implementation."""
    invoice_file = "initial_workspace/invoices.json"
    if not os.path.exists(invoice_file):
        print("No invoice file found.")
        return

    with open(invoice_file) as f:
        invoices = json.load(f)

    required_fields = ["client", "items", "total_amount", "due_date"]

    score = 0
    total = len(invoices)

    for invoice in invoices:
        if all(field in invoice for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid invoices: {score}/{total}")

if __name__ == "__main__":
    main()
