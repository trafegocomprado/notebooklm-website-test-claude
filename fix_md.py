import json
import glob
import os

folder = "Meeting Prep - Digital Silk"
files = glob.glob(os.path.join(folder, "*.md"))
for file in files:
    if "INDEX" in file: continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        try:
            data = json.loads(content)
            text = data.get('value', {}).get('answer', '')
            if text:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Fixed {file}")
        except Exception:
            pass
    except Exception as e:
        print(f"Failed {file}: {e}")
