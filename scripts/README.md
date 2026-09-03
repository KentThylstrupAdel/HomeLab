Scripts in this folder will do different tasks in order to script my way out of repeatable tasks.
The purpose is a duality of optimising processes and improving my python scripting abilities.

k8s_status.py
This script can check the health of my kubernetes cluster, and works with the following commands:
python scripts/k8s_status.py
python scripts/k8s_status.py --nodes
python scripts/k8s_status.py --pods
python scripts/k8s_status.py --namespace monitoring
python scripts/k8s_status.py --namespaces
