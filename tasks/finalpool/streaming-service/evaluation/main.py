import json
import os

def main():
    """Evaluate the streaming-service implementation."""
    # Check if content library exists
    content_dir = "initial_workspace/content_library"
    if not os.path.exists(content_dir):
        print("No content library directory found.")
        return

    # Count content files
    files = os.listdir(content_dir)
    score = 0
    total = 3

    if len(files) > 0:
        score += 1

    # Check for common streaming formats
    streaming_formats = [".mp4", ".mp3", ".wav", ".hls", ".m3u8"]
    has_content = any(any(f.endswith(fmt) for fmt in streaming_formats) for f in files)
    if has_content:
        score += 1

    # Check for metadata files
    metadata_files = [f for f in files if f.endswith(".json") or f.endswith(".metadata")]
    if len(metadata_files) > 0:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
