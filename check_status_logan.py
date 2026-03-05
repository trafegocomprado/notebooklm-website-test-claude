from notebooklm_tools.cli.utils import get_client
import sys
nb_id = "259e2bb1-fde4-4554-95b9-c5af36b46abf"
with get_client() as client:
    artifacts = client.poll_studio_status(nb_id)
    for a in artifacts:
        print(f"{a['type']}: {a['status']} ({a['artifact_id']})")
