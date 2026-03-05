import subprocess
import os

nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
folder = "Meeting Prep - Logan"
os.makedirs(folder, exist_ok=True)

# Generate everything
print("Starting studio generation...")
commands = [
    ["nlm", "audio", "create", nb_id, "-y"],
    ["nlm", "infographic", "create", nb_id, "-y"],
    ["nlm", "quiz", "create", nb_id, "-c", "5", "-y"],
    ["nlm", "flashcards", "create", nb_id, "-y"]
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, shell=True) # Use shell=True for windows if needed, but not strictly necessary. Let's just run it.
    
print("Studio generation started. Run 'check_status_logan.py' to monitor.")
