import json
import os

def main():
    """Evaluate the video-trimmer implementation."""
    # Check if output files exist
    output_file = "initial_workspace/output.mp4"
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
    if output_file.endswith(".mp4"):
        score += 1

    # Check for metadata
    try:
        with open(output_file, "rb") as f:
            header = f.read(4)
            if header == b"\x00\x00\x00\x1c" or header == b"ftyp":
                score += 1
    except Exception:
        pass

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
