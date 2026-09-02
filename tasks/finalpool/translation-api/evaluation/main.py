import json
import os

def main():
    """Evaluate the translation-api implementation."""
    translation_file = "initial_workspace/translations.json"
    if not os.path.exists(translation_file):
        print("No translation data file found.")
        return

    with open(translation_file) as f:
        translations = json.load(f)

    required_fields = ["source_text", "target_language", "translated_text"]

    score = 0
    total = len(translations)

    for translation in translations:
        if all(field in translation for field in required_fields):
            score += 1

    final_score = score / total if total > 0 else 0
    print(f"Score: {final_score}")
    print(f"Valid translations: {score}/{total}")

if __name__ == "__main__":
    main()
