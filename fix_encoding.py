import os
import glob
import re

for root, dirs, files in os.walk(r"d:\Antigravity\notebooklm-website-test-claude"):
    for file in files:
        if file == "index.html":
            filepath = os.path.join(root, file)
            # Try reading with latin1 or utf8
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # The character might be lost ("Trfego comPrep"), or "Trfego comPrep"
            fixed_content = re.sub(r'Tr[^a-zA-Z\s]*fego comPrep', 'Tráfego comPrep', content)
            fixed_content = fixed_content.replace('Tr?fego comPrep', 'Tráfego comPrep')
            fixed_content = fixed_content.replace('Trfego comPrep', 'Tráfego comPrep')
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(fixed_content)
            
            print(f"Fixed {filepath}")
