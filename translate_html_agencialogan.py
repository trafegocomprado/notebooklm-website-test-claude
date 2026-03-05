import re
import os

filepath = r"d:\Antigravity\notebooklm-website-test-claude\Meeting Prep - Agencia Logan\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Swap company name mentions
html = html.replace("Logan Marketing", "Agência Logan (Cabo Frio)")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
