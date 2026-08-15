# Overview

## Purpose

I started this project to gain practical experience with technologies commonly used in Platform Engineering.

Rather than learning Kubernetes, Ansible, GitHub Actions or Argo CD individually, I wanted to understand how they fit together as a working platform.

This repository documents both the implementation and the decisions I made while building the environment. It serves as a learning project, a reference for myself, and a portfolio showing the technologies and workflows I've worked with.

---

## Scope

The platform currently includes:

- Infrastructure automation using Ansible
- Kubernetes orchestration with k3s
- Helm for application deployment
- Continuous Integration with GitHub Actions
- GitOps deployments using Argo CD
- REST API interaction and automation
- Monitoring with Prometheus and Grafana
- Technical documentation for the architecture and implementation

The goal is not to build the biggest homelab possible, but one that is understandable, maintainable and easy to expand.

---

## Project Objectives

The project has a few simple objectives:

- Learn Platform Engineering by building a working platform.
- Replace repetitive manual administration with automation.
- Keep infrastructure and configuration in version control.
- Build practical experience with Kubernetes, GitOps and APIs.
- Improve my Linux administration skills.
- Learn how to monitor and operate the platform after deployment.
- Document the platform as it evolves.

Whenever I add a new technology, I try to understand why it exists before installing it.

---

## Engineering Principles

A few principles guide most of the decisions I make while working on the project.

### Infrastructure as Code

If I can describe infrastructure as code instead of configuring it manually, I usually prefer that approach.

Keeping configuration in Git makes changes easier to understand, review and reproduce.

---

### Git as the Source of Truth

Git should describe how the platform is supposed to look.

Instead of making permanent Kubernetes changes manually, I try to update the repository and let Argo CD reconcile the cluster with the desired state.

---

### Automation

One of the main reasons for building the homelab was to automate repetitive work.

Ansible is currently used for tasks such as:

- Updating the Ubuntu servers
- Shutting down the cluster
- Calling REST APIs
- Repeating administrative tasks in a consistent way

---

### Continuous Validation

Small mistakes in YAML or infrastructure configuration are easy to make.

GitHub Actions validates changes before I rely on them, including:

- YAML linting
- Ansible syntax checking
- Helm linting

The pipeline has already caught several configuration mistakes during development.

---

### GitOps

Kubernetes deployments are managed through Argo CD.

The desired state is stored in Git, and Argo CD continuously compares that state with the running cluster.

This also provides self-healing if a managed resource is changed manually.

---

### API-Driven Automation

As the project has grown, I've started using REST APIs directly instead of relying only on command-line tools.

Examples include:

- Querying Grafana health information
- Reading Kubernetes namespaces and Pods
- Changing Kubernetes resources through the API
- Using Ansible's `uri` module for repeatable API calls

This has helped me understand how automation tools interact with modern platforms behind the user interface.

---

### Monitoring

The monitoring setup now includes:

- Prometheus for metrics collection
- Grafana for dashboards and visualisation
- Kubernetes node health
- Pod readiness
- CPU usage by node
- Memory usage by node
- Disk usage by node

The dashboard configuration is stored in Git alongside the rest of the project.

---

### Security

Security is being introduced gradually as the platform becomes more capable.

The first implemented security component is an internal Public Key Infrastructure (PKI), providing trusted certificates for services within the homelab.

The current PKI uses a simple certificate hierarchy:

```text
HomeLab Root CA
        │
        ▼
HomeLab Intermediate CA
        │
        ▼
Service Certificates
        │
        └── grafana.homelab

```

---

### Documentation

Writing documentation has become part of the learning process.

If I cannot explain why something was configured a certain way, I probably do not understand it well enough yet.

---

## Why This Project Exists

Most tutorials teach one technology at a time.

You'll find guides for Kubernetes, Ansible, Helm, GitHub Actions or Prometheus individually.

What interested me more was understanding how they work together.

That has become the focus of the project.

Instead of collecting software, I'm trying to build a platform where every component has a clear purpose.

---

## Who This Repository Is For

The repository is mainly intended for:

- Myself, as documentation and reference
- Recruiters and hiring managers who want to see practical work
- Technical interviewers interested in how I've approached the project
- Anyone curious about building a small Platform Engineering homelab

---

## Repository Documentation

The documentation is split into individual topics so each document focuses on one part of the platform.

| Document | Description |
|---|---|
| 02-architecture.md | Overall architecture and design decisions |
| 03-kubernetes.md | Kubernetes cluster |
| 04-ansible.md | Infrastructure and API automation |
| 05-ci-cd.md | Continuous Integration |
| 06-argocd-gitops.md | GitOps with Argo CD |
| 07-monitoring.md | Monitoring and observability |
| 08-network.md | Network architecture |
| 09-roadmap.md | PKI architecture |
| 20-roadmap.md | Current and future improvements |

---

## Design Philosophy

Whenever I work on the platform, I generally try to follow a few simple ideas:

- Keep things simple.
- Automate repetitive work.
- Avoid unnecessary complexity.
- Understand a technology before adding another one.
- Keep configuration in Git where practical.
- Document decisions while they're still fresh.
- Improve the platform one step at a time.

I don't expect the homelab to ever be completely "finished".

As I learn new technologies and gain more experience, the platform will continue to evolve.

---

## Key Takeaways

- This is a practical learning project focused on Platform Engineering.
- The goal is understanding how technologies work together rather than simply installing them.
- Automation, Git, Kubernetes, APIs and monitoring are central parts of the project.
- The platform is intentionally expanded one component at a time.
- Implemented features are documented as implemented, while future ideas remain on the roadmap.

---

## Related Documentation

The next document describes the overall architecture of the platform and the reasoning behind its design.

Continue with **[Architecture](02-architecture.md)**.
