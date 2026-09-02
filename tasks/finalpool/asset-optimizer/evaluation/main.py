import json
import os

def main():
    """Evaluate the asset-optimizer implementation."""
    # Check if optimized assets exist
    asset_dir = "initial_workspace/optimized"
    if not os.path.exists(asset_dir):
        print("No optimized assets directory found.")
        return

    # Count optimized files
    files = os.listdir(asset_dir)
    score = 0
    total = 3

    if len(files) > 0:
        score += 1

    # Check for common image formats
    image_formats = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
    has_image = any(any(f.endswith(fmt) for fmt in image_formats) for f in files)
    if has_image:
        score += 1

    # Check for reasonable file sizes
    total_size = sum(os.path.getsize(os.path.join(asset_dir, f)) for f in files if os.path.isfile(os.path.join(asset_dir, f)))
    if total_size > 0:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
