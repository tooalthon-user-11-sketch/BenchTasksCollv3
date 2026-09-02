import json
import os

def main():
    """Evaluate the blog-engine implementation."""
    posts_file = "initial_workspace/posts.json"
    if not os.path.exists(posts_file):
        print("No posts file found.")
        return

    with open(posts_file) as f:
        posts = json.load(f)

    required_fields = ["title", "content", "status"]
    valid_statuses = ["draft", "published", "archived"]

    score = 0
    total = len(posts)

    for post in posts:
        if all(field in post for field in required_fields):
            if post["status"] in valid_statuses:
                score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid posts: {score}/{total}")

if __name__ == "__main__":
    main()
