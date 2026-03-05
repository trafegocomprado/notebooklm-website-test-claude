import subprocess
import os

nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
folder = "Meeting Prep - Logan PT"
os.makedirs(folder, exist_ok=True)

print("Iniciando a geração dos artefatos no Studio (PT-BR)...")
commands = [
    ["nlm", "audio", "create", nb_id, "--language", "pt", "-y"],
    ["nlm", "infographic", "create", nb_id, "--language", "pt", "-y"],
    ["nlm", "quiz", "create", nb_id, "-c", "5", "--focus", "Gere todas as 5 perguntas e respostas do teste de conhecimento obrigatoriamente e exclusivamente em Português do Brasil (PT-BR).", "-y"],
    ["nlm", "flashcards", "create", nb_id, "--focus", "Gere o conteúdo frente e verso dos flashcards (perguntas e respostas) exclusivamente no idioma Português do Brasil (PT-BR).", "-y"]
]

for cmd in commands:
    print(f"Executando: {' '.join(cmd)}")
    subprocess.run(cmd, shell=True) 
    
print("Geração do Studio enviada. Aguarde alguns minutos com o script de status.")
