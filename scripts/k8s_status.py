import subprocess
import json
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Check the health of the HomeLab Kubernetes cluster."
)

parser.add_argument(
    "--nodes",
    action="store_true",
    help="Check Kubernetes node health."
)

parser.add_argument(
    "--pods",
    action="store_true",
    help="Check Kubernetes pod health."
)

parser.add_argument(
    "--namespace",
    type=str,
    default=None,
    metavar="NAME",
    help="Specify a namespace to check pod health (default: all namespaces)."
)

parser.add_argument(
    "--namespaces",
    action="store_true",
    help="List available Kubernetes namespaces."
)

args = parser.parse_args()
check_everything = (
    not args.nodes
    and not args.pods
    and not args.namespace
    and not args.namespaces
)

all_nodes_ready = True
all_pods_ready = True

def get_namespaces():
    result = subprocess.run(
        ["kubectl", "get", "namespaces", "-o", "json"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("ERROR: Unable to get Kubernetes namespaces.")
        print(result.stderr)
        sys.exit(1)

    try:
        namespaces = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("ERROR: Unable to parse Kubernetes namespace output.")
        sys.exit(1)

    return namespaces

def get_pods(namespace=None):
    if namespace:
        command = [
            "kubectl", "get", "pods",
            "-n", namespace,
            "-o", "json"
        ]
    else:
        command = [
            "kubectl", "get", "pods",
            "-A",
            "-o", "json"
        ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("ERROR: Unable to communicate with Kubernetes cluster.")
        print(result.stderr)
        sys.exit(1)

    try:
        pods = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("ERROR: Unable to parse Kubernetes pods output.")
        sys.exit(1)

    return pods


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


def get_pod_ready_status(pod):
    if pod["status"]["phase"] == "Succeeded":
        return True

    container_statuses = pod["status"].get("containerStatuses", [])

    if not container_statuses:
        return False

    for container in container_statuses:
        if not container["ready"]:
            return False

    return True

if args.pods or args.namespace or check_everything:
    pods = get_pods(args.namespace)

    all_pods_ready = True
    for pod in pods["items"]:
        pod_ready = get_pod_ready_status(pod)

        if pod_ready:
            status = "READY"
        else:
            status = "NOT READY"
            all_pods_ready = False

        print(
            f'Pod Name: {pod["metadata"]["name"]} | '
            f'Namespace: {pod["metadata"]["namespace"]} | '
            f'Status: {status}'
        )
    if all_pods_ready:
        print("All pods are ready.")
    else:
        print("Some pods are not ready.")

if args.nodes or check_everything:
    nodes = get_nodes()
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

if args.namespaces:
    namespaces = get_namespaces()

    print("Available namespaces:")

    for namespace in namespaces["items"]:
        print(f'  {namespace["metadata"]["name"]}')

if not all_nodes_ready or not all_pods_ready:
    sys.exit(1)