import re
import json
import os

SOURCE_FILE = "src/app.js"
OUTPUT_FILE = "locales/en.json"

pattern = r'"(.*?)"'

def extract_strings():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    matches = re.findall(pattern, content)

    data = {}
    for i, text in enumerate(matches):
        data[f"key_{i+1}"] = text

    os.makedirs("locales", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Done!")

extract_strings()
