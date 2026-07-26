# Roadmap

## Looking Ahead

This homelab has already taught me far more than I expected when I first started building it.

Along the way I've realised that Platform Engineering isn't about collecting technologies—it's about understanding how they fit together.

There's still plenty to learn, but I'd rather build that knowledge gradually than rush through a long list of tools.

---

## Current Priorities

These are the areas I'm planning to focus on next.

### Monitoring & Observability

Grafana is already deployed, but I'd like to build a more complete monitoring solution by exploring:

* Prometheus
* Loki
* Alertmanager
* Better dashboards
* Basic alerting

My goal is to understand not only how to deploy infrastructure, but also how to operate it.

---

### Networking

The current network is intentionally simple.

As the platform grows, I'd like to explore:

* VLANs
* Internal DNS
* TLS for internal services
* Load balancing
* Improved Ingress configuration

These will be added when they solve a real problem rather than simply because they're available.

---

### CI/CD & GitOps

The current pipeline validates my infrastructure before deployment.

Over time I'd like to expand it with things like:

* Additional validation
* Security scanning
* Container image checks
* More advanced GitHub Actions workflows

Likewise, I'd like to continue exploring more advanced GitOps features in Argo CD once I'm comfortable with the fundamentals.

---

### Kubernetes

I'm becoming increasingly comfortable with Kubernetes, but there's still a lot I'd like to explore.

Some future topics include:

* More applications running in the cluster
* Operators
* Stateful workloads
* Backup and recovery
* High availability
* Storage solutions

As always, I'll add these gradually as the platform evolves.

---

## Long-Term Goal

This project started as a way to learn Kubernetes and automation.

It's gradually become something bigger.

Today I see it as a place where I can safely experiment, make mistakes, solve problems and document what I've learned along the way.

I expect the technologies to change over time, but the goal will remain the same:

To become a better Platform Engineer by building, breaking and improving real systems.

---

## Lessons Learned

Looking back, one of the biggest lessons has been that learning happens much faster when I actually build something.

Reading documentation is valuable, but working through real problems has given me a much deeper understanding of topics like Kubernetes, GitOps, automation and CI.

I've also learned that it's perfectly fine not to know everything from the beginning.

Building the platform one step at a time has made the learning process both more enjoyable and much more sustainable.

---

## Final Thoughts

This repository isn't intended to demonstrate that I already know everything about Platform Engineering.

Instead, it documents what I've built, what I've learned and where I want to go next.

I hope it continues to evolve as my experience grows, and I'll keep updating it as I explore new technologies and improve the platform.
# Roadmap

## Purpose

This document outlines the planned evolution of the Platform Engineering homelab.

The roadmap serves as a living document that identifies future improvements, architectural goals, and technologies that will be introduced as the platform matures.

Rather than implementing every available technology immediately, the project follows an incremental approach where each addition has a clear purpose and supports the overall Platform Engineering objectives.

---

## Guiding Principles

Future development follows several principles:

* Introduce complexity only when it provides value.
* Prefer automation over manual processes.
* Build upon existing architecture rather than replacing it.
* Document every significant architectural decision.
* Maintain a reproducible and version-controlled platform.
* Prioritize operational simplicity.

These principles ensure that the platform grows sustainably without becoming unnecessarily complicated.

---

# Current Platform

The current implementation includes:

| Component               | Status |
| ----------------------- | :----: |
| Git & GitHub            |    ✅   |
| Linux Administration    |    ✅   |
| Kubernetes (k3s)        |    ✅   |
| Ansible                 |    ✅   |
| Helm                    |    ✅   |
| GitHub Actions          |    ✅   |
| Argo CD                 |    ✅   |
| Grafana                 |    ✅   |
| Technical Documentation |    ✅   |

This establishes a complete Platform Engineering foundation that supports Infrastructure as Code, Continuous Integration, GitOps, and Kubernetes operations.

---

# Development Roadmap

The roadmap is divided into phases.

Each phase builds upon the previous one while introducing a limited number of new technologies.

---

# Phase 1 — Platform Foundation

**Status:** Complete ✅

Objectives:

* Build a Kubernetes platform.
* Automate infrastructure using Ansible.
* Implement GitHub Actions.
* Introduce GitOps with Argo CD.
* Create comprehensive platform documentation.

Outcome:

A fully functioning Platform Engineering foundation suitable for experimentation and continued expansion.

---

# Phase 2 — Observability

**Status:** In Progress 🚧

Objectives:

* Deploy Prometheus.
* Deploy Loki.
* Deploy Alertmanager.
* Expand Grafana dashboards.
* Create custom monitoring dashboards.
* Implement basic alerting.

Expected Outcome:

Improved visibility into cluster health, application performance, and platform operations.

---

# Phase 3 — Networking

**Status:** Planned 📋

Objectives:

* Configure Ingress.
* Deploy MetalLB.
* Implement internal DNS.
* Introduce TLS using cert-manager.
* Improve service exposure.

Expected Outcome:

Applications become accessible through stable hostnames with automated certificate management.

---

# Phase 4 — Platform Security

**Status:** Planned 📋

Objectives:

* Kubernetes Network Policies.
* Secrets management.
* RBAC review.
* Secure application configuration.
* Host firewall review.

Expected Outcome:

A stronger security posture with improved isolation between platform components.

---

# Phase 5 — Storage

**Status:** Planned 📋

Objectives:

* Deploy Longhorn.
* Persistent volumes.
* Backup strategy.
* Disaster recovery testing.

Expected Outcome:

Reliable persistent storage for stateful applications together with recovery procedures.

---

# Phase 6 — Advanced Platform Engineering

**Status:** Planned 📋

Objectives:

* Terraform
* External Secrets
* ApplicationSet
* Multi-environment GitOps
* Automated image updates
* Policy validation
* Platform scalability improvements

Expected Outcome:

A platform that more closely resembles enterprise Platform Engineering environments.

---

# Long-Term Goals

The long-term vision of this homelab is to provide practical experience with technologies commonly used by Platform Engineering teams.

Future areas of exploration include:

* High Availability Kubernetes
* Multi-node control planes
* Service Mesh technologies
* Advanced observability
* Backup automation
* Multi-cluster management
* Identity integration
* Policy-as-Code
* Supply chain security
* Container image signing

Not every technology will necessarily be implemented. New additions should always support a practical learning objective rather than increasing complexity for its own sake.

---

# Learning Objectives

This repository is intended to demonstrate experience with:

* Infrastructure as Code
* Kubernetes administration
* Linux system administration
* GitOps workflows
* Continuous Integration
* Platform monitoring
* Infrastructure automation
* Documentation as Code
* Modern Platform Engineering practices

The emphasis is on understanding how these technologies work together rather than simply deploying them individually.

---

# Success Criteria

The project will be considered successful if it continues to:

* Remain fully reproducible.
* Be managed entirely through version-controlled configuration.
* Minimize manual administration.
* Demonstrate modern Platform Engineering practices.
* Serve as a useful technical portfolio.
* Continue evolving through incremental improvements.

---

# Key Takeaways

* The platform follows an incremental development strategy.
* New technologies are introduced only when they provide architectural value.
* Platform stability is prioritized over feature count.
* Documentation evolves alongside the implementation.
* The roadmap reflects continuous learning rather than a fixed end state.

---

# Related Documentation

This roadmap builds upon every previous chapter.

For the current implementation, see:

* [01-overview.md](01-overview.md)
* [02-architecture.md](02-architecture.md)
* [03-kubernetes.md](03-kubernetes.md)
* [04-ansible.md](04-ansible.md)
* [05-ci-cd.md](05-ci-cd.md)
* [06-argocd-gitops.md](06-argocd-gitops.md)
* [07-monitoring.md](07-monitoring.md)
* [08-network.md](08-network.md)

