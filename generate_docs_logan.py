import subprocess
import json
import os
import re

nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
folder = "Meeting Prep - Logan"
os.makedirs(folder, exist_ok=True)

prompts = {
    "01_briefing_doc.md": "Write an executive briefing document about the agency Logan Marketing (not any other Logan) based on the sources, focusing on their background, history (especially in Brazil/ABC Paulista), services offered, market size, and a proposed pitch for a partnership.",
    "02_deep_research_report.md": "Create a detailed deep research report analyzing Logan Marketing's competitive landscape, potential weaknesses or growth areas, and how a white-label engineering partnership can help them scale.",
    "03_competitive_intel.md": "Act as a competitive intelligence analyst. Write a tactical cheat sheet on Logan Marketing. Include key points, their current positioning, and 5 hard-hitting discovery questions to ask."
}

for filename, prompt in prompts.items():
    print(f"Generating {filename}...")
    try:
        cmd = ["nlm", "notebook", "query", nb_id, prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Output is likely JSON or raw text. Try to extract
        content = result.stdout
        
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            try:
                data = json.loads(match.group(0))
                if 'value' in data and 'answer' in data['value']:
                    text = data['value']['answer']
                else:
                    text = content
            except Exception:
                text = content
        else:
            text = content
            
        if '"answer": "' in text:
            parts = text.split('"answer": "')
            if len(parts) > 1:
                text = parts[1].split('",\n    "conversation_id"')[0]
                text = text.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\u2019', "'").replace('\\u2014', "-").replace('\\u201c', '"').replace('\\u201d', '"')
        
        filepath = os.path.join(folder, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Saved {filepath}")
    except Exception as e:
        print(f"Error generating {filename}: {e}")
