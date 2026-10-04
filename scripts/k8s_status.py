import subprocess
import json
import sys
import argparse


# ---------------------------------------------------------------------------
# Command-line arguments
# ---------------------------------------------------------------------------
# By default the script checks both nodes and pods.
# The optional arguments can be used to limit the health check or list
# available Kubernetes namespaces.

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

# If no filtering arguments are supplied, perform the complete health check.
check_everything = (
    not args.nodes
    and not args.pods
    and not args.namespace
    and not args.namespaces
)

# Start by assuming the cluster is healthy.
# These values are changed to False if an unhealthy resource is found.
all_nodes_ready = True
all_pods_ready = True


# ---------------------------------------------------------------------------
# Kubernetes data collection
# ---------------------------------------------------------------------------

def get_namespaces():
    """Retrieve all Kubernetes namespaces as JSON."""

    result = subprocess.run(
        ["kubectl", "get", "namespaces", "-o", "json"],
        capture_output=True,
        text=True
    )

    # kubectl returns a non-zero exit code if the command fails.
    if result.returncode != 0:
        print("ERROR: Unable to get Kubernetes namespaces.")
        print(result.stderr)
        sys.exit(1)

    # Convert the JSON returned by kubectl into Python data structures.
    try:
        namespaces = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("ERROR: Unable to parse Kubernetes namespace output.")
        sys.exit(1)

    return namespaces


def get_pods(namespace=None):
    """Retrieve pods from a specific namespace or from the entire cluster."""

    # Use -n when a namespace is supplied; otherwise use -A for all namespaces.
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
    """Retrieve Kubernetes nodes as JSON."""

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


# ---------------------------------------------------------------------------
# Health evaluation
# ---------------------------------------------------------------------------

def get_node_ready_status(node):
    """Return True when the Kubernetes Ready condition for a node is True."""

    # Kubernetes stores several conditions for each node.
    # We specifically care about the condition with type "Ready".
    for condition in node["status"]["conditions"]:
        if condition["type"] == "Ready":
            return condition["status"] == "True"

    # If Kubernetes did not provide a Ready condition, treat the node as unhealthy.
    return False


def get_pod_ready_status(pod):
    """Return True when a pod has completed successfully or all containers are ready."""

    # Completed Jobs normally have phase "Succeeded".
    # Their containers are no longer running, so they should not be marked unhealthy.
    if pod["status"]["phase"] == "Succeeded":
        return True

    container_statuses = pod["status"].get("containerStatuses", [])

    # A pod without container status information cannot be confirmed as ready.
    if not container_statuses:
        return False

    # Every container in the pod must report ready.
    for container in container_statuses:
        if not container["ready"]:
            return False

    return True


# ---------------------------------------------------------------------------
# Pod health check
# ---------------------------------------------------------------------------

# Run when pods were explicitly requested, a namespace was supplied,
# or no filters were supplied (the default complete health check).
if args.pods or args.namespace or check_everything:
    pods = get_pods(args.namespace)

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


# ---------------------------------------------------------------------------
# Node health check
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Namespace listing
# ---------------------------------------------------------------------------

if args.namespaces:
    namespaces = get_namespaces()

    print("Available namespaces:")

    for namespace in namespaces["items"]:
        print(f'  {namespace["metadata"]["name"]}')


# ---------------------------------------------------------------------------
# Final result
# ---------------------------------------------------------------------------
# Exit code 0 means the requested health checks passed.
# Exit code 1 allows CI/CD, monitoring or other automation to detect a failure.

if not all_nodes_ready or not all_pods_ready:
    sys.exit(1)
