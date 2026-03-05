from notebooklm_tools.cli.utils import get_client
import sys
nb_id = "c1897d48-acc3-4ebc-be2f-f8ce8f4abdae"
with get_client() as client:
    artifacts = client.poll_studio_status(nb_id)
    for a in artifacts:
        print(f"{a['type']}: {a['status']} ({a['artifact_id']})")
