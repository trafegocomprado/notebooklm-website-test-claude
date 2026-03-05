from notebooklm_tools.cli.utils import get_client
from notebooklm_tools.services import downloads
import asyncio
import os

nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
folder = "Meeting Prep - Logan"

async def main():
    try:
        os.makedirs(folder, exist_ok=True)
        with get_client() as client:
            artifacts = client.poll_studio_status(nb_id)
            for a in artifacts:
                print(f"{a['type']}: {a['status']} ({a['artifact_id']})")
                if a['type'] == 'quiz' and a['status'] == 'completed':
                    print("Downloading quiz...")
                    await downloads.download_async(
                        client, nb_id, "quiz", os.path.join(folder, "06_pre_call_quiz.md"),
                        artifact_id=a['artifact_id'], output_format="markdown"
                    )
                elif a['type'] == 'flashcards' and a['status'] == 'completed':
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
                        client, nb_id, "audio", os.path.join(folder, "audio_briefing.m4a"),
                        artifact_id=a['artifact_id']
                    )
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
