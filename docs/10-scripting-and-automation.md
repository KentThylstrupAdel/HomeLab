# 10 - Scripting and Automation

## Overview

This section documents scripting and automation developed as part of the HomeLab.

Python is a developing skill in this project. Rather than focusing on standalone
programming exercises, the goal is to use Python to solve practical infrastructure
and operational tasks within the HomeLab.

The scripts are located in the [`scripts/`](../scripts/) directory.

## Current Scripts

### Kubernetes Health Check

**Script:** `k8s_status.py`

The Kubernetes health check is the first Python utility developed for the HomeLab.
It uses `kubectl` to retrieve information from the Kubernetes cluster as JSON and
evaluates the health of nodes and pods.

The script currently supports:

- Checking the health of all Kubernetes nodes and pods
- Checking nodes only
- Checking pods only
- Checking pods within a specific namespace
- Listing available namespaces
- Recognising successfully completed Kubernetes Jobs
- Returning an exit code indicating whether the health check succeeded or failed

### Usage

Check the complete cluster:

    python scripts/k8s_status.py

Check nodes only:

    python scripts/k8s_status.py --nodes

Check pods only:

    python scripts/k8s_status.py --pods

Check pods in a specific namespace:

    python scripts/k8s_status.py --namespace monitoring

List available namespaces:

    python scripts/k8s_status.py --namespaces

Display available options:

    python scripts/k8s_status.py --help

## Technical Approach

The script currently interacts with Kubernetes by executing `kubectl` commands
through Python's `subprocess` module.

Kubernetes data is requested in JSON format and parsed in Python. The resulting
data structures are then used to determine node and pod health.

The script also uses exit codes so that its result can later be consumed by other
automation or monitoring tools.

## Current Scope

This is an early step toward using scripting as part of the HomeLab's broader
automation approach.

The current implementation intentionally remains relatively simple while I build
experience with Python and infrastructure scripting. Future scripts and
improvements will be added when they solve an actual operational or automation
need within the HomeLab.
