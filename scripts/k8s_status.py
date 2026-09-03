import subprocess
import json

result = subprocess.run(
    ["kubectl", "get", "nodes", "-o", "json"],
    capture_output=True,
    text=True
)

nodes = json.loads(result.stdout)

print(nodes["items"][0]["metadata"]["name"])
