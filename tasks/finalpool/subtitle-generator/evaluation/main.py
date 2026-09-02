import json
import os

def main():
    """Evaluate the subtitle-generator implementation."""
    # Check if subtitle files exist
    subtitle_file = "initial_workspace/subtitles.srt"
    if not os.path.exists(subtitle_file):
        print("No subtitle file found.")
        return

    with open(subtitle_file) as f:
        content = f.read()

    # Basic validation
    lines = content.strip().split("\n")
    score = 0
    total = 0

    # Check for SRT format
    if lines and lines[0].isdigit():
        score += 1
        total += 1

    # Check for timecodes
    timecode_count = 0
    for line in lines:
        if "--:" in line:
            timecode_count += 1
    if timecode_count > 0:
        score += 1
        total += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
