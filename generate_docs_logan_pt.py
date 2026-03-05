import subprocess
import json
import os
import re

nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
folder = "Meeting Prep - Logan PT"
os.makedirs(folder, exist_ok=True)

prompts = {
    "01_briefing_doc.md": "Escreva um documento de briefing executivo corporativo detalhado sobre a agência Logan Marketing (baseada no Brasil) com base nas fontes, focando em seu background, métricas principais, serviços oferecidos (Performance, UX, Conteúdo, etc) e escreva uma proposta de pitch para uma parceria. O formato DEVE ser Markdown e o idioma OBRIGATÓRIAMENTE PT-BR (Português do Brasil).",
    "02_deep_research_report.md": "Crie um relatório profundo (Deep Research) analisando o cenário competitivo da Logan Marketing no mercado brasileiro (marketing digital, tráfego pago, lançamentos). Aponte virtudes, possíveis gargalos de crescimento (capacidade produtiva, engenharia pesada) e faça um business case sobre como uma parceria técnica white-label nossa pode ajudá-los a escalar vendas online de forma mais agressiva. Responda em Português do Brasil de forma executiva e estruturada em tópicos.",
    "03_competitive_intel.md": "Atue como um analista de inteligência competitiva e redija um 'cheat sheet' (folha de dicas) super tático focado na Logan Marketing Brasil. Mapeie o atual posicionamento e elabore 5 perguntas afiadas de descoberta ('Discovery Questions') para fazer ao C-level deles durante a nossa call. O resultado deve ser em PT-BR (Português) em formato Markdown legível e profissional."
}

for filename, prompt in prompts.items():
    print(f"Gerando {filename}...")
    try:
        cmd = ["nlm", "notebook", "query", nb_id, prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # O output geralmente vem sujo se for via CLI sem JSON ou com JSON mal escapado.
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
