import json
import os

def main():
    """Evaluate the booking-system implementation."""
    bookings_file = "initial_workspace/bookings.json"
    if not os.path.exists(bookings_file):
        print("No bookings file found.")
        return

    with open(bookings_file) as f:
        bookings = json.load(f)

    required_fields = ["customer", "service", "date", "status"]
    valid_statuses = ["confirmed", "pending", "cancelled", "completed"]

    score = 0
    total = len(bookings)

    for booking in bookings:
        if all(field in booking for field in required_fields):
            if booking["status"] in valid_statuses:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid bookings: {score}/{total}")

if __name__ == "__main__":
    main()
