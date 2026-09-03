# Scripts

This directory contains scripts developed to automate repetitive operational tasks within the HomeLab.

The purpose is twofold: to identify opportunities where scripting can simplify or automate infrastructure operations, and to develop my Python skills through practical use cases.

## Kubernetes Health Check

**Script:** `k8s_status.py`

A Python CLI utility for checking the health of the Kubernetes cluster. It evaluates node and pod readiness and can limit pod checks to a specific namespace.

### Usage

Check the complete cluster:

```bash
python scripts/k8s_status.py
```

Check nodes only:

```bash
python scripts/k8s_status.py --nodes
```

Check pods only:

```bash
python scripts/k8s_status.py --pods
```

Check pods in a specific namespace:

```bash
python scripts/k8s_status.py --namespace monitoring
```

List available namespaces:

```bash
python scripts/k8s_status.py --namespaces
```

For all available options:

```bash
python scripts/k8s_status.py --help
```
