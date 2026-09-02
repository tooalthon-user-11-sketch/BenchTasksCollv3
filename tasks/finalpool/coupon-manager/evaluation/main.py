import json
import os

def main():
    """Evaluate the coupon-manager implementation."""
    coupon_file = "initial_workspace/coupons.json"
    if not os.path.exists(coupon_file):
        print("No coupon data file found.")
        return

    with open(coupon_file) as f:
        coupons = json.load(f)

    required_fields = ["code", "discount_type", "value", "expiration_date"]
    valid_discount_types = ["percentage", "fixed_amount", "free_shipping", "buy_one_get_one"]

    score = 0
    total = len(coupons)

    for coupon in coupons:
        if all(field in coupon for field in required_fields):
            if coupon["discount_type"] in valid_discount_types:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid coupons: {score}/{total}")

if __name__ == "__main__":
    main()
