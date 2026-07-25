# Architecture

## Purpose

This document describes the overall architecture of the Platform Engineering homelab and explains how the platform components interact to provide a modern Infrastructure as Code and GitOps workflow.

The platform is intentionally designed to resemble a simplified enterprise environment, where infrastructure, application deployments, and operational practices are managed through version-controlled code rather than manual configuration.

---

## Scope

This document covers:

* Overall platform architecture
* Core platform components
* Component interactions
* High-level deployment workflow
* Design decisions

Implementation details for each technology are described in their respective documentation.

---

## Platform Architecture

<p align="center">
  <img src="images/platform-architecture.png"
       alt="Platform Engineering Homelab Architecture"
       width="1100">
</p>

The platform follows a GitOps workflow where Git serves as the single source of truth for infrastructure and application configuration.

Changes are validated automatically before being synchronized to the Kubernetes cluster, ensuring consistent and reproducible deployments.

---

## Architecture Overview

The platform consists of five primary layers.

| Layer                  | Responsibility                                                |
| ---------------------- | ------------------------------------------------------------- |
| Development            | Infrastructure and application development                    |
| Source Control         | Version control and configuration management                  |
| Continuous Integration | Validation and quality assurance                              |
| GitOps                 | Declarative deployment and reconciliation                     |
| Runtime Platform       | Kubernetes cluster hosting platform services and applications |

Each layer has a clearly defined responsibility, reducing operational complexity while improving maintainability.

---

## Core Components

### Development Workstation

The development workstation is used for infrastructure administration and platform development.

Primary responsibilities include:

* Developing Ansible playbooks
* Creating Helm charts
* Managing Kubernetes resources
* Maintaining Git repositories
* Executing cluster administration tasks

Although the workstation runs Bazzite Linux, all engineering tooling is executed within a Distrobox container to provide a consistent and isolated development environment.

---

### GitHub Repository

GitHub serves as the central source of truth for the platform.

The repository contains:

* Infrastructure automation
* Kubernetes manifests
* Helm charts
* GitHub Actions workflows
* Documentation

Every infrastructure change begins as a Git commit.

---

### Continuous Integration

GitHub Actions automatically validates repository changes.

Current validation includes:

* YAML linting
* Ansible syntax validation
* Helm chart validation
* Helm template rendering

Only validated changes are considered ready for deployment.

---

### GitOps

Argo CD continuously monitors the Git repository and compares the desired state with the running Kubernetes cluster.

When differences are detected, Argo CD reconciles the cluster automatically, eliminating the need for manual deployment procedures.

---

### Kubernetes Platform

The Kubernetes cluster provides the runtime environment for platform services and demonstration applications.

Current platform services include:

* Argo CD
* Grafana
* Helm-managed applications

Additional platform services will be introduced as the homelab evolves.

---

## High-Level Deployment Workflow

The platform follows a predictable deployment process.

1. Infrastructure or application changes are committed to Git.
2. GitHub Actions validates the repository.
3. Argo CD detects repository changes.
4. Kubernetes synchronizes to the desired state.
5. Updated workloads become available within the cluster.

This workflow minimizes manual intervention while ensuring deployments remain reproducible.

---

## Design Decisions

The platform has been designed around several key architectural decisions.

### Git-Centric Operations

Git is treated as the authoritative source for infrastructure and application configuration.

This provides version history, traceability, and rollback capabilities.

---

### Declarative Infrastructure

Infrastructure and application definitions are stored declaratively whenever possible.

This approach reduces configuration drift and improves reproducibility.

---

### Lightweight Kubernetes

The platform uses **k3s** to provide a CNCF-compliant Kubernetes distribution that is lightweight enough for homelab hardware while remaining operationally similar to upstream Kubernetes.

---

### Automation

Administrative tasks are automated using Ansible and Kubernetes-native tooling wherever practical.

Automation improves consistency while reducing repetitive manual work.

---

### Documentation

Documentation is maintained alongside the source code.

This ensures architectural decisions and implementation details evolve together with the platform.

---

## Architectural Goals

The long-term objectives of the platform architecture are to provide:

* Reproducible deployments
* Automated validation
* Declarative configuration
* Operational simplicity
* Incremental scalability
* Maintainable infrastructure

These goals influence every architectural decision made throughout the project.

---

## Related Documentation

For implementation details, continue with the following documents:

* [03-kubernetes.md](03-kubernetes.md)
* [04-ansible.md](04-ansible.md)
* [05-ci-cd.md](05-ci-cd.md)
* [06-gitops.md](06-gitops.md)
