import subprocess
import json
import sys


def get_nodes():
    result = subprocess.run(
        ["kubectl", "get", "nodes", "-o", "json"],
        capture_output=True,
        text=True

    )

    if result.returncode != 0:
        print("ERROR: Unable to communicate with Kubernetes cluster.")
        print(result.stderr)
        sys.exit(1)
    try:
        nodes = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("ERROR: Unable to parse Kubernetes nodes output.")
        sys.exit(1)

    return nodes


def get_node_ready_status(node):
    for condition in node["status"]["conditions"]:
        if condition["type"] == "Ready":
            return condition["status"] == "True"
    return False

nodes = get_nodes()

all_nodes_ready = True

for node in nodes["items"]:
    print(f"Node Name: {node['metadata']['name']}")
    ready_status = get_node_ready_status(node)
    if ready_status:
        print("  status: READY")
    else:
        print("  status: NOT READY")
        all_nodes_ready = False

if all_nodes_ready:
    print("All nodes are ready.")
else:
    print("Some nodes are not ready.")