from notebooklm_tools.cli.utils import get_client
import sys
nb_id = "98130b33-0d57-4bd8-b309-76affac8354c"
with get_client() as client:
    artifacts = client.poll_studio_status(nb_id)
    for a in artifacts:
        print(f"{a['type']}: {a['status']} ({a['artifact_id']})")
