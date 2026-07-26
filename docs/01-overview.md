# Overview

## Purpose

I started this project to gain practical experience with technologies commonly used in Platform Engineering.

Rather than learning Kubernetes, Ansible, GitHub Actions or Argo CD individually, I wanted to understand how they fit together as a complete platform.

This repository documents both the implementation and the decisions I made while building the environment. It serves as a learning project, a reference for myself, and a portfolio that demonstrates the technologies and workflows I've worked with.

---

## Scope

The platform currently includes:

* Infrastructure automation using Ansible
* Kubernetes orchestration with k3s
* Helm for application deployment
* Continuous Integration with GitHub Actions
* GitOps deployments using Argo CD
* Platform monitoring with Grafana
* Technical documentation for the architecture and implementation

My goal has never been to build the biggest homelab possible, but to build one that is understandable, maintainable and easy to expand over time.

---

## Project Objectives

The project has a few simple objectives.

* Learn Platform Engineering by building a working platform.
* Replace manual administration with automation wherever it makes sense.
* Keep infrastructure in version control.
* Build experience with Kubernetes and GitOps.
* Improve my Linux administration skills.
* Document the platform as it evolves.

Whenever I add a new technology, I try to understand why it exists before I install it.

---

## Engineering Principles

A few principles guide most of the decisions I make while working on this project.

### Infrastructure as Code

If I can describe infrastructure as code instead of configuring it manually, I usually prefer that approach.

Keeping configuration in Git makes it easier to understand changes, recover from mistakes and reproduce the environment.

---

### Git as the Source of Truth

Git should describe how the platform is supposed to look.

Instead of logging into servers and changing configuration manually, I try to make changes through the repository whenever possible.

---

### Automation

One of the main reasons for building this homelab was to automate repetitive work.

If I find myself repeating the same administrative task several times, it's usually a good candidate for an Ansible playbook or another form of automation.

---

### Continuous Validation

Small mistakes in YAML or Kubernetes configuration are easy to make.

Using GitHub Actions to validate changes before they become part of the repository has already saved me from introducing several configuration errors.

---

### GitOps

Deployments are handled through Argo CD.

I like the idea that the cluster should reflect what's stored in Git rather than whatever someone last changed manually.

---

### Documentation

I've found that writing documentation forces me to understand the technologies better.

If I can't explain why I configured something a certain way, I probably don't understand it well enough yet.

---

## Why This Project Exists

Most tutorials teach one technology at a time.

You'll find guides on installing Kubernetes, writing Ansible playbooks or deploying applications with Helm.

What interested me more was understanding how these technologies work together.

That has become the focus of this project.

Instead of collecting software, I'm trying to build a platform where each component has a clear purpose.

---

## Who This Repository Is For

The repository is mainly intended for:

* Myself, as documentation and reference.
* Recruiters and hiring managers who want to see practical work.
* Technical interviewers interested in how I've approached the project.
* Anyone curious about building a small Platform Engineering homelab.

---

## Repository Documentation

The documentation is split into individual topics so each document focuses on one part of the platform.

| Document                                   | Description                               |
| ------------------------------------------ | ----------------------------------------- |
| [02-architecture.md](02-architecture.md)   | Overall architecture and design decisions |
| [03-kubernetes.md](03-kubernetes.md)       | Kubernetes cluster                        |
| [04-ansible.md](04-ansible.md)             | Infrastructure automation                 |
| [05-ci-cd.md](05-ci-cd.md)                 | Continuous Integration                    |
| [06-argocd-gitops.md](06-argocd-gitops.md) | GitOps with Argo CD                       |
| [07-monitoring.md](07-monitoring.md)       | Monitoring and observability              |
| [08-network.md](08-network.md)             | Network architecture                      |
| [09-roadmap.md](09-roadmap.md)             | Future improvements                       |

---

## Design Philosophy

Whenever I work on the platform, I generally try to follow a few simple ideas.

* Keep things simple.
* Automate repetitive work.
* Avoid unnecessary complexity.
* Understand a technology before adding another one.
* Document decisions while they're still fresh.
* Improve the platform one step at a time.

I don't expect this homelab to ever be "finished".

As I learn new technologies and gain more experience, the platform will continue to evolve.

---

## Key Takeaways

* This is a practical learning project focused on Platform Engineering.
* The goal is understanding how technologies work together rather than simply installing them.
* Automation, Git, Kubernetes and documentation are central parts of the project.
* The platform is intentionally expanded one component at a time.
* Every new technology should solve a real problem or support a learning objective.

---

## Related Documentation

The next document describes the overall architecture of the platform and the reasoning behind its design.

Continue with **[Architecture](02-architecture.md)**.
