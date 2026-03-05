import subprocess
import json
import os
import time

folder_name = "Meeting Prep - Digital Silk"
nb_id = "c1897d48-acc3-4ebc-be2f-f8ce8f4abdae"

def create_studio(artifact_type, extra_args=[]):
    print(f"Creating {artifact_type}...")
    cmd = ["nlm", "studio", "create", nb_id, artifact_type] + extra_args + ["-y"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

def download_artifact(artifact_type, ext):
    print(f"Downloading {artifact_type}...")
    if artifact_type == "audio":
        filename = "audio_briefing.mp3"
        cmd = ["nlm", "download", nb_id, artifact_type, "-o", os.path.join(folder_name, filename)]
    elif artifact_type == "infographic":
        filename = "04_market_infographic.png"
        cmd = ["nlm", "download", nb_id, artifact_type, "-o", os.path.join(folder_name, filename)]
    elif artifact_type in ["quiz", "flashcards"]:
        filename = f"06_pre_call_quiz.md" if artifact_type == "quiz" else "07_flashcards.md"
        cmd = ["nlm", "download", nb_id, artifact_type, "-o", os.path.join(folder_name, filename), "--format", "markdown"]
    else:
        return
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

# Create all
create_studio("quiz", ["--count", "8", "--difficulty", "medium"])
create_studio("flashcards", ["--difficulty", "medium"])
create_studio("infographic", ["--orientation", "portrait", "--detail", "detailed"])
create_studio("audio", ["--format", "brief", "--length", "short"])

print("Waiting for artifacts to finish...")
# Poll until complete
while True:
    cmd = ["nlm", "studio", "status", nb_id, "--json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if "in_progress" not in result.stdout:
        break
    time.sleep(10)

print("Downloading artifacts...")
download_artifact("quiz", "md")
download_artifact("flashcards", "md")
download_artifact("infographic", "png")
download_artifact("audio", "mp3")

print("All done.")
