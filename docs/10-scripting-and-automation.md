# Scripting and Automation

## Purpose

Scripting is being introduced into the homelab to automate operational tasks
that do not necessarily fit naturally into Ansible, Kubernetes manifests or
other existing automation tooling.

Python is currently a developing skill for me. The focus is on learning it
through practical infrastructure tasks rather than standalone programming
exercises.

## Current Scripts

### Kubernetes Health Check

**Location:** `scripts/k8s_status.py`

The Kubernetes health check is the first Python utility developed for the
homelab.

It queries the Kubernetes cluster through `kubectl`, retrieves cluster data
as JSON and evaluates the health of nodes and pods.

Current functionality includes:

- Cluster-wide node and pod health checks
- Individual node or pod checks
- Pod health checks for a specific namespace
- Namespace discovery
- Handling of successfully completed Kubernetes Jobs
- Exit codes for use by other automation

## Usage

Check the complete cluster:

    python scripts/k8s_status.py

Check nodes only:

    python scripts/k8s_status.py --nodes

Check pods only:

    python scripts/k8s_status.py --pods

Check a specific namespace:

    python scripts/k8s_status.py --namespace monitoring

List namespaces:

    python scripts/k8s_status.py --namespaces

Show available options:

    python scripts/k8s_status.py --help

## Implementation

The script uses Python's `subprocess` module to execute `kubectl` commands
and requests Kubernetes output in JSON format.

The JSON responses are parsed in Python and evaluated to determine resource
health.

Node health is determined from the Kubernetes `Ready` condition. Pod health
is determined from container readiness, while successfully completed Jobs
are treated as healthy.

The script returns a non-zero exit code when a health check fails, allowing
it to be used by other automation or CI/CD processes in the future.

## Development

This is the first step toward using Python for infrastructure scripting
within the homelab.

The current implementation is intentionally relatively simple while I
develop practical experience with Python. Future scripting will be added
when there is an operational problem where scripting provides an appropriate
solution.
