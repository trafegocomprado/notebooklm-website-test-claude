import subprocess
import json
import os
import re

nb_id = "98130b33-0d57-4bd8-b309-76affac8354c"
folder = "Meeting Prep - Agencia Logan"
os.makedirs(folder, exist_ok=True)

prompts = {
    "01_briefing_doc.md": "Escreva um documento de briefing executivo corporativo detalhado sobre a Agência Logan (de Cabo Frio, RJ) com base nas fontes. Foque em seu histórico, programa Acelera em 3, métricas, serviços e redija uma proposta de pitch para parceria. Idioma: PT-BR. Formato: Markdown.",
    "02_deep_research_report.md": "Crie um relatório profundo (Deep Research) analisando o cenário competitivo da Agência Logan (foco em conversão e Google Ads/Meta Ads). Aponte virtudes, possíveis gargalos de crescimento, e faça um business case sobre como uma aliança estratégica em engenharia pode ajudá-los a atender projetos maiores. Responda em Português do Brasil (PT-BR). Formato: Markdown estruturado.",
    "03_competitive_intel.md": "Atue como um analista de inteligência competitiva e redija um 'cheat sheet' muito tático focado na Agência Logan de Cabo Frio. Mapeie o atual posicionamento contra agências vitrine (agências de posts) e elabore 5 perguntas afiadas de descoberta ('Discovery Questions') para fazer ao líder deles na nossa reunião. Idioma: PT-BR de forma executiva."
}

for filename, prompt in prompts.items():
    print(f"Gerando {filename}...")
    try:
        cmd = ["nlm", "notebook", "query", nb_id, prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
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
        print(f"Salvo em {filepath}")
    except Exception as e:
        print(f"Erro ao gerar {filename}: {e}")
