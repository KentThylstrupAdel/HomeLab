# Platform Engineering Homelab

A personal Platform Engineering homelab built to gain practical experience with modern infrastructure management, Kubernetes, Infrastructure as Code, Continuous Integration, and GitOps.

The objective of this project is not simply to learn individual technologies, but to understand how they integrate into a cohesive platform similar to those used in professional environments.

---

## Project Goals

This homelab was created to develop practical experience in:

* Linux administration
* Infrastructure as Code (Ansible)
* Kubernetes administration (k3s)
* Helm chart development
* Git-based workflows
* Continuous Integration (GitHub Actions)
* GitOps Continuous Delivery (Argo CD)
* Platform monitoring (Grafana)
* Technical documentation

---

## Architecture

> **Architecture diagram coming soon**

The platform follows a GitOps deployment model where Git acts as the single source of truth.

```text
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     ├── YAML Validation
     ├── Ansible Syntax Validation
     └── Helm Validation
     │
     ▼
Argo CD
     │
     ▼
k3s Kubernetes Cluster
     │
     ▼
Applications
```

A detailed architectural description can be found in the documentation.

---

## Technology Stack

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| Bazzite Linux    | Engineering workstation          |
| Distrobox        | Isolated development environment |
| Ubuntu Server    | Kubernetes nodes                 |
| Git & GitHub     | Source control                   |
| GitHub Actions   | Continuous Integration           |
| Ansible          | Infrastructure automation        |
| Kubernetes (k3s) | Container orchestration          |
| Helm             | Kubernetes package management    |
| Argo CD          | GitOps Continuous Delivery       |
| Grafana          | Monitoring and visualization     |

---

## Current Capabilities

* Multi-node Kubernetes cluster
* Infrastructure managed with Ansible
* Helm-based application packaging
* Automated CI validation using GitHub Actions
* GitOps deployments with Argo CD
* Monitoring with Grafana
* Version-controlled infrastructure and documentation

---

## Repository Structure

```text
.
├── ansible/          Infrastructure automation
├── argocd/           GitOps application definitions
├── charts/           Helm charts
├── docs/             Technical documentation
├── .github/          GitHub Actions workflows
└── README.md
```

---

## Documentation

The documentation is organized into focused topics:

| Document             | Description                                        |
| -------------------- | -------------------------------------------------- |
| `01-overview.md`     | Project goals, scope and engineering principles    |
| `02-architecture.md` | Overall platform architecture and design decisions |
| `03-kubernetes.md`   | Kubernetes cluster design and operation            |
| `04-ansible.md`      | Infrastructure automation using Ansible            |
| `05-ci-cd.md`        | Continuous Integration with GitHub Actions         |
| `06-gitops.md`       | GitOps deployment using Argo CD                    |
| `07-monitoring.md`   | Monitoring and observability                       |
| `08-roadmap.md`      | Planned improvements and future development        |

---

## Engineering Principles

The platform is built around a small set of engineering principles:

* Infrastructure should be defined as code.
* Git is the single source of truth.
* Configuration changes should be validated automatically.
* Deployments should be reproducible.
* Documentation should evolve alongside the platform.
* Automation should replace repetitive manual tasks whenever practical.

---

## Current Status

| Component               |     Status     |
| ----------------------- | :------------: |
| Kubernetes Cluster      |        ✅       |
| Ansible Automation      |        ✅       |
| GitHub Actions CI       |        ✅       |
| Helm Charts             |        ✅       |
| Argo CD GitOps          |        ✅       |
| Grafana Monitoring      |        ✅       |
| Technical Documentation | 🚧 In Progress |

---

## Roadmap

The platform will continue to evolve with additional enterprise-focused capabilities, including:

* Terraform
* Prometheus
* Alertmanager
* cert-manager
* Secret management
* Network Policies
* High Availability Kubernetes
* Backup and disaster recovery
* Automated container image builds

---

## About This Project

This repository serves as a practical learning project and a technical portfolio demonstrating modern Platform Engineering practices.

Rather than focusing on individual technologies in isolation, the project demonstrates how automation, Kubernetes, Continuous Integration, and GitOps can be combined into a maintainable and reproducible platform.
