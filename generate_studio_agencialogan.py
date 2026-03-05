import subprocess
import os

nb_id = "98130b33-0d57-4bd8-b309-76affac8354c"
folder = "Meeting Prep - Agencia Logan"
os.makedirs(folder, exist_ok=True)

print("Iniciando a geração dos artefatos no Studio (PT-BR) para Agencia Logan...")
commands = [
    ["nlm", "audio", "create", nb_id, "--language", "pt", "-y"],
    ["nlm", "infographic", "create", nb_id, "--language", "pt", "-y"],
    ["nlm", "quiz", "create", nb_id, "-c", "5", "--focus", "Gere todas as 5 perguntas e respostas de múltipla escolha focadas explicitamente no idioma Português do Brasil (PT-BR).", "-y"],
    ["nlm", "flashcards", "create", nb_id, "--focus", "Gere o conteúdo dos flashcards (perguntas e respostas) detalhando o modelo de negócios da Agencia Logan exclusivamente em Português do Brasil (PT-BR).", "-y"]
]

for cmd in commands:
    print(f"Executando: {' '.join(cmd)}")
    subprocess.run(cmd, shell=True) 
    
print("Geração do Studio enviada. Monitorar pelo script de status.")
