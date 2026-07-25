# Kubernetes

## Purpose

This document describes the Kubernetes platform that forms the runtime environment of the homelab.

It explains the overall cluster design, architectural decisions, and operational responsibilities of the Kubernetes platform. Detailed deployment procedures are intentionally omitted, as the focus of this document is the platform itself rather than individual applications.

---

## Scope

This document covers:

* Kubernetes distribution
* Cluster topology
* Node responsibilities
* Platform services
* Design decisions
* Operational considerations

---

## Why Kubernetes?

Kubernetes provides a consistent platform for deploying, managing, and scaling containerized applications.

The primary objective of introducing Kubernetes into this homelab is not simply to learn container orchestration, but to understand how a modern Platform Engineering team delivers reliable and reproducible infrastructure through declarative configuration and automation.

The cluster serves as the foundation upon which monitoring, GitOps, and future platform services are deployed.

---

## Kubernetes Distribution

The platform uses **k3s**, a lightweight CNCF-compliant Kubernetes distribution developed by Rancher.

k3s was selected because it provides:

* A production-inspired Kubernetes environment
* Low resource requirements
* Simple installation and maintenance
* Full compatibility with standard Kubernetes tooling
* Excellent suitability for homelab environments

Although optimized for edge and resource-constrained systems, k3s remains operationally similar to upstream Kubernetes, making it an excellent platform for practical learning.

---

## Cluster Topology

<p align="center">
  <img src="images/kubernetes-cluster.png"
       alt="Kubernetes Cluster"
       width="850">
</p>

The current cluster consists of one control plane and one worker node.

| Node             | Role          | Operating System |
| ---------------- | ------------- | ---------------- |
| cluster-plane-01 | Control Plane | Ubuntu Server    |
| node-02          | Worker Node   | Ubuntu Server    |

This topology provides a straightforward environment for experimenting with Kubernetes while maintaining a clear separation between cluster management and workload execution.

---

## Control Plane Responsibilities

The control plane is responsible for managing the Kubernetes cluster.

Its primary responsibilities include:

* Kubernetes API Server
* Cluster scheduling
* Desired state management
* Cluster coordination
* etcd datastore
* Node management

The control plane represents the management layer of the Kubernetes environment.

---

## Worker Node Responsibilities

Worker nodes execute containerized workloads.

Responsibilities include:

* Running application Pods
* Executing scheduled workloads
* Providing compute resources
* Reporting node health to the control plane

As the platform grows, additional worker nodes can be added without changing the overall architecture.

---

## Platform Services

The Kubernetes cluster hosts both operational platform services and demonstration workloads.

### Current Services

| Service | Purpose                              |
| ------- | ------------------------------------ |
| Argo CD | GitOps deployment and reconciliation |
| Grafana | Monitoring dashboards                |
| Helm    | Application packaging and deployment |

### Planned Services

| Service      | Purpose                                  |
| ------------ | ---------------------------------------- |
| Prometheus   | Metrics collection                       |
| Loki         | Centralized logging                      |
| Traefik      | Ingress controller                       |
| cert-manager | Automated TLS certificate management     |
| MetalLB      | Load balancing for bare-metal networking |
| Longhorn     | Distributed persistent storage           |

Each additional service has been selected to mirror capabilities commonly found in enterprise Kubernetes platforms.

---

## Workload Management

Applications are deployed declaratively using Helm charts and synchronized through Argo CD.

This deployment model provides:

* Version-controlled releases
* Repeatable deployments
* Simplified upgrades
* Rollback capabilities
* Reduced configuration drift

The Kubernetes cluster therefore remains synchronized with the desired state stored in Git.

---

## Networking

The current cluster uses the default networking provided by k3s.

Future improvements include:

* Ingress management
* External load balancing
* TLS certificate automation
* Network policy implementation

These additions will further align the platform with enterprise Kubernetes environments.

---

## Storage

Persistent storage requirements are currently minimal.

As the platform evolves, distributed storage will be introduced using Longhorn to support stateful workloads and improve resilience.

---

## Operational Principles

The Kubernetes platform is operated according to several guiding principles.

### Declarative Configuration

Cluster resources are defined declaratively rather than configured manually.

---

### Automation

Deployments are automated using GitOps workflows wherever practical.

---

### Repeatability

Applications should be deployable consistently across environments using the same manifests and Helm charts.

---

### Incremental Growth

The platform is intentionally expanded in manageable stages rather than introducing unnecessary complexity early in the project.

---

## Design Decisions

Several architectural decisions influenced the Kubernetes implementation.

### Why k3s?

A lightweight distribution reduces operational overhead while retaining compatibility with the broader Kubernetes ecosystem.

---

### Why Ubuntu Server?

Ubuntu Server provides a stable and widely adopted Linux platform with excellent community support and compatibility with Kubernetes tooling.

---

### Why a Separate Worker Node?

Separating cluster management from workload execution better reflects production environments and simplifies future expansion.

---

## Key Takeaways

* Kubernetes provides the runtime platform for all services.
* k3s offers a lightweight yet fully compatible Kubernetes distribution.
* Infrastructure is managed declaratively using Helm and GitOps.
* The platform is designed to grow incrementally while remaining maintainable.
* Architectural decisions prioritize simplicity, automation, and reproducibility.

---

## Related Documentation

Continue with:

* [04-ansible.md](04-ansible.md)
* [05-ci-cd.md](05-ci-cd.md)
* [06-gitops.md](06-gitops.md)
