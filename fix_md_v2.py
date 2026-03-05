import json
import glob
import os
import re

folder = "Meeting Prep - Agencia Logan"
files = glob.glob(os.path.join(folder, "*.md"))
for file in files:
    if "INDEX" in file: continue
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Processing {file}...")
        
        # Try to find a JSON block if it's not purely JSON
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(0))
                if 'value' in data and 'answer' in data['value']:
                    text = data['value']['answer']
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print(f"  -> Fixed using JSON parsing!")
                    continue
            except Exception as e:
                print(f"  -> JSON parse error: {e}")
                
        # If the file starts with "value": or similar because of bad clipping
        if '"answer":' in content:
            print("  -> Found answer key, trying manual extraction")
            parts = content.split('"answer": "')
            if len(parts) > 1:
                extracted = parts[1].split('",\n    "conversation_id"')[0]
                # unescape newlines
                extracted = extracted.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\u2019', '’').replace('\\u2014', '—').replace('\\u201c', '“').replace('\\u201d', '”')
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(extracted)
                print(f"  -> Fixed using manual extraction!")
                continue

    except Exception as e:
        print(f"Failed {file}: {e}")
