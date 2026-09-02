import json
import os

def main():
    """Evaluate the backup-utility implementation."""
    backup_file = "initial_workspace/backup_manifest.json"
    if not os.path.exists(backup_file):
        print("No backup manifest file found.")
        return

    with open(backup_file) as f:
        manifest = json.load(f)

    required_fields = ["backup_id", "timestamp", "status", "files"]
    valid_statuses = ["completed", "failed", "in_progress"]

    score = 0
    total = 4

    if "backup_id" in manifest:
        score += 1

    if "timestamp" in manifest:
        score += 1

    if "status" in manifest and manifest["status"] in valid_statuses:
        score += 1

    if "files" in manifest and len(manifest["files"]) > 0:
        score += 1

    final_score = score / total
    print(f"Score: {final_score}")
    print(f"Checks passed: {score}/{total}")

if __name__ == "__main__":
    main()
