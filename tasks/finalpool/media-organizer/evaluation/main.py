import json
import os

def main():
    """Evaluate the media-organizer implementation."""
    # Check if media library exists
    media_dir = "initial_workspace/media_library"
    if not os.path.exists(media_dir):
        print("No media library directory found.")
        return

    # Count media files
    files = os.listdir(media_dir)
    score = 0
    total = 3

    if len(files) > 0:
        score += 1

    # Check for common media formats
    media_formats = [".jpg", ".jpeg", ".png", ".gif", ".mp4", ".mp3", ".wav"]
    has_media = any(any(f.endswith(fmt) for fmt in media_formats) for f in files)
    if has_media:
        score += 1

    # Check for organization (subdirectories)
    subdirs = [f for f in files if os.path.isdir(os.path.join(media_dir, f))]
    if len(subdirs) > 0:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
