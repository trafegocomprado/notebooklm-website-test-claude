from notebooklm_tools.cli.utils import get_client
from notebooklm_tools.services import downloads
import asyncio
import os

nb_id = "98130b33-0d57-4bd8-b309-76affac8354c"
folder = "Meeting Prep - Agencia Logan"

async def main():
    try:
        os.makedirs(folder, exist_ok=True)
        with get_client() as client:
            artifacts = client.poll_studio_status(nb_id)
            
            latest_artifacts = {}
            for a in artifacts:
                latest_artifacts[a['type']] = a
                
            for t, a in latest_artifacts.items():
                print(f"Latest {t}: {a['status']} ({a['artifact_id']})")
                if a['status'] == 'completed':
                    if t == 'quiz':
                        print("Downloading quiz...")
                        await downloads.download_async(
                            client, nb_id, "quiz", os.path.join(folder, "06_pre_call_quiz.md"),
                            artifact_id=a['artifact_id'], output_format="markdown"
                        )
                    elif t == 'flashcards':
                        print("Downloading flashcards...")
                        await downloads.download_async(
                            client, nb_id, "flashcards", os.path.join(folder, "07_flashcards.md"),
                            artifact_id=a['artifact_id'], output_format="markdown"
                        )
                    elif t == 'infographic':
                        print("Downloading infographic...")
                        await downloads.download_async(
                            client, nb_id, "infographic", os.path.join(folder, "market_infographic.png"),
                            artifact_id=a['artifact_id']
                        )
                    elif t == 'audio':
                        print("Downloading audio...")
                        await downloads.download_async(
                            client, nb_id, "audio", os.path.join(folder, "audio_briefing.m4a"),
                            artifact_id=a['artifact_id']
                        )
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
