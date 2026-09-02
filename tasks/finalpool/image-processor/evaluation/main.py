import json
import os

def main():
    """Evaluate the image-processor implementation."""
    # Check if output files exist
    output_file = "initial_workspace/output.jpg"
    if not os.path.exists(output_file):
        print("No output file found.")
        return

    # Basic validation
    score = 0
    total = 3

    # Check file size
    if os.path.getsize(output_file) > 0:
        score += 1

    # Check file extension
    if output_file.endswith((".jpg", ".jpeg", ".png", ".gif")):
        score += 1

    # Check for image header
    try:
        with open(output_file, "rb") as f:
            header = f.read(3)
            if header == b"\xff\xd8\xff" or header == b"GIF" or header[:8] == b"\x89PNG\r\n\x1a\n":
                score += 1
    except Exception:
        pass

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
