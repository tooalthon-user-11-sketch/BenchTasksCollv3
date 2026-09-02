import json
import os

def main():
    """Evaluate the voice-processor implementation."""
    # Check if output files exist
    output_file = "initial_workspace/transcription.txt"
    if not os.path.exists(output_file):
        print("No transcription file found.")
        return

    with open(output_file) as f:
        content = f.read()

    # Basic validation
    score = 0
    total = 3

    # Check file is not empty
    if content.strip():
        score += 1

    # Check for reasonable length
    if len(content) > 10:
        score += 1

    # Check for text content
    if any(c.isalpha() for c in content):
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
