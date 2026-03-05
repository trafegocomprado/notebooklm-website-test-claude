from notebooklm_tools.cli.utils import get_client
from notebooklm_tools.services import downloads
import asyncio
import os

nb_id = "c1897d48-acc3-4ebc-be2f-f8ce8f4abdae"
folder = "Meeting Prep - Digital Silk"

async def main():
    try:
        os.makedirs(folder, exist_ok=True)
        with get_client() as client:
            artifacts = client.poll_studio_status(nb_id)
            for a in artifacts:
                print(f"Generating {a['type']}: {a['status']} ({a['artifact_id']})")
                if a['type'] == 'quiz':
                    print("Downloading quiz...")
                    await downloads.download_async(
                        client, nb_id, "quiz", os.path.join(folder, "06_pre_call_quiz.md"),
                        artifact_id=a['artifact_id'], output_format="markdown"
                    )
                elif a['type'] == 'flashcards':
                    print("Downloading flashcards...")
                    await downloads.download_async(
                        client, nb_id, "flashcards", os.path.join(folder, "07_flashcards.md"),
                        artifact_id=a['artifact_id'], output_format="markdown"
                    )
                elif a['type'] == 'infographic' and a['status'] == 'completed':
                    print("Downloading infographic...")
                    downloads.download_sync(
                        client, nb_id, "infographic", os.path.join(folder, "market_infographic.png"),
                        artifact_id=a['artifact_id']
                    )
                elif a['type'] == 'audio' and a['status'] == 'completed':
                    print("Downloading audio...")
                    await downloads.download_async(
                        client, nb_id, "audio", os.path.join(folder, "audio_briefing.mp3"),
                        artifact_id=a['artifact_id']
                    )
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
