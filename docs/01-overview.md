# Platform Engineering Homelab

## Overview

This repository contains my personal Platform Engineering homelab, created to gain practical experience with modern infrastructure management, Kubernetes, Infrastructure as Code, and GitOps.

The project is designed to simulate a simplified enterprise platform where infrastructure, application deployment, and configuration are managed through version-controlled code rather than manual administration.

The primary objective has been to deepen my understanding of technologies commonly used within Platform Engineering while following engineering practices similar to those used in professional environments.

---

# Objectives

The homelab focuses on the following engineering disciplines:

- Linux system administration
- Infrastructure as Code (Ansible)
- Kubernetes cluster administration
- Helm package management
- GitHub Actions Continuous Integration (CI)
- Argo CD Continuous Delivery (CD)
- GitOps workflows
- Infrastructure documentation
- Version-controlled configuration management

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Linux | Operating system |
| Git & GitHub | Source control |
| GitHub Actions | Continuous Integration |
| Ansible | Infrastructure automation |
| Kubernetes (k3s) | Container orchestration |
| Helm | Kubernetes package management |
| Argo CD | GitOps Continuous Delivery |
| Grafana | Monitoring and dashboards |

---

# High-Level Architecture

```text
Developer
     │
     ▼
Git Repository
     │
     ▼
GitHub Actions
     │
     ├── YAML Validation
     ├── Ansible Syntax Validation
     └── Helm Validation
     │
     ▼
Argo CD
     │
     ▼
Kubernetes Cluster
     │
     ▼
Applications
```

---

# CI/CD Workflow

Every change begins as a Git commit.

GitHub Actions automatically validates the repository by checking YAML formatting, Ansible playbooks, and Helm charts.

Once validation succeeds, Argo CD continuously compares the desired state stored in Git with the Kubernetes cluster and automatically reconciles any differences.

This follows a GitOps deployment model where Git is the single source of truth.

---

# Current Capabilities

- Multi-node Kubernetes cluster
- Infrastructure automation using Ansible
- Helm chart development
- GitHub Actions CI pipeline
- Automated GitOps deployments using Argo CD
- Grafana monitoring
- Infrastructure documentation

---

# Future Improvements

Planned additions include:

- Terraform
- Prometheus
- Alertmanager
- cert-manager
- External Secrets / HashiCorp Vault
- Network Policies
- High Availability Kubernetes
- Backup and disaster recovery
- Container image build pipeline

---

# Purpose of this Repository

This repository serves both as a learning project and as a demonstration of practical Platform Engineering skills.

Rather than focusing solely on individual technologies, the project emphasizes how multiple tools integrate into a coherent engineering platform following modern DevOps and GitOps practices.
