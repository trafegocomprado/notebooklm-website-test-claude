import re
import os

filepath = r"d:\Antigravity\notebooklm-website-test-claude\Meeting Prep - Logan PT\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("Meeting Prep", "Prep. P/ Reunião")
html = html.replace("Export PDF", "Exportar PDF")

html = html.replace("Briefing Doc", "Briefing Exec.")
html = html.replace("Competitive Intel", "Análise Competi.")
html = html.replace("Deep Research", "Pesquisa Profunda")
html = html.replace("Knowledge Test", "Teste Conhecim.")
html = html.replace("Flashcards", "Flashcards")
html = html.replace("Infographic", "Infográfico")

html = html.replace("Audio Briefing", "Briefing em Áudio")
html = html.replace("Deep dive discussion generated from selected sources", "Mergulho profundo em áudio gerado a partir do conteúdo")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(html)
