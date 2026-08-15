# Architecture

## Purpose

This document gives an overview of how the homelab is put together and why I made the architectural choices that I did.

I wanted to build a platform where each component has a clear responsibility rather than simply installing technologies for the sake of it. Every major component should support the overall goal of creating a manageable, reproducible and observable Platform Engineering environment.

---

## Scope

This document covers:

- The overall platform architecture
- How the different components interact
- High-level deployment and management flows
- Design decisions
- The reasoning behind the chosen technologies

More detailed information about Kubernetes, Ansible, GitOps, monitoring, networking and PKI can be found in their respective chapters.

---

## Platform Architecture

<p align="center">
  <img src="images/platform-architecture.png"
       alt="Platform Engineering Homelab Architecture"
       width="1100">
</p>

The platform uses Git as the central source of truth for version-controlled configuration.

Application and Kubernetes configuration changes are committed to the repository, validated through GitHub Actions and synchronized to the cluster by Argo CD.

Ansible has a different responsibility. It manages the underlying Ubuntu hosts and operational workflows such as system maintenance and platform health checks.

This creates a separation between two types of automation:

```text
Infrastructure & Operations
        │
        └── Ansible
             │
             └── Ubuntu / Kubernetes hosts

Application Configuration
        │
        └── Git
             │
             ├── GitHub Actions
             │
             └── Argo CD
                    │
                    └── Kubernetes
```

Where possible, I try to make changes through these automated workflows rather than configuring systems manually.

---

## The Building Blocks

The platform is made up of a number of components with different responsibilities.

| Component | Purpose |
|---|---|
| Bazzite Workstation | Development and administration |
| Distrobox | Ansible and administration environment |
| GitHub | Source control and source of truth |
| GitHub Actions | Automated configuration validation |
| Ansible | Infrastructure and operational automation |
| Kubernetes (k3s) | Application platform |
| Helm | Kubernetes package management |
| Argo CD | GitOps deployment and reconciliation |
| Traefik | Ingress and TLS termination |
| Prometheus | Metrics collection |
| Grafana | Monitoring and visualisation |
| Internal PKI | Certificate issuance and trusted HTTPS |

Each component has a specific responsibility rather than being added simply to increase the number of technologies in the platform.

---

## How Everything Fits Together

There are two main management flows in the platform.

### Application and Configuration Flow

A typical version-controlled change follows roughly this process:

1. I make a change to the repository.
2. GitHub Actions validates the change.
3. If validation succeeds, the change becomes part of the repository.
4. Argo CD detects relevant Kubernetes configuration changes.
5. Argo CD synchronizes the desired state to the cluster.
6. Prometheus and Grafana provide visibility into the resulting platform state.

This keeps Git at the centre of application and Kubernetes configuration management.

### Infrastructure and Operations Flow

Ansible manages the underlying Ubuntu infrastructure separately.

It connects to the servers over SSH and is used for tasks such as:

- Server configuration
- Package management
- System updates
- Platform health checks
- Maintenance workflows
- Kubernetes host preparation

This separation allows Argo CD to focus on Kubernetes workloads while Ansible handles operations outside or around the cluster.

---

## Security and PKI

The platform now includes a small internal Public Key Infrastructure for trusted service communication.

The current certificate hierarchy is:

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

The Root CA acts as the trust anchor, while the Intermediate CA is used to issue service certificates.

Grafana is currently the first service using the internal PKI. Its certificate is deployed to Kubernetes and presented through Traefik, providing trusted HTTPS access to the service.

Certificate issuance is currently manual, with certificate lifecycle automation planned as the next stage.

See **[PKI and Certificate Management](09-pki.md)** for the implementation.

---

## Monitoring and Observability

Prometheus and Grafana provide the current monitoring foundation.

Prometheus collects metrics from the Kubernetes environment, while Grafana provides dashboards for visualising platform health and resource usage.

The current monitoring includes:

- Kubernetes node status
- Pod health
- CPU usage
- Memory usage
- Disk usage

Loki, alerting and additional observability capabilities are planned as the monitoring stack develops.

See **[Monitoring and Observability](07-monitoring.md)** for more detail.

---

## Design Decisions

While building the platform, I try to balance learning value with operational simplicity.

### Why k3s?

I wanted a Kubernetes distribution that behaves like upstream Kubernetes but is lightweight enough to run comfortably on my available hardware.

k3s provides that while remaining compatible with the wider Kubernetes ecosystem.

---

### Why Ansible?

One of my goals was to stop configuring servers manually.

Ansible allows infrastructure configuration and operational procedures to become repeatable automation rather than collections of commands that need to be remembered and executed manually.

---

### Why GitHub Actions?

Even in a small homelab it's surprisingly easy to introduce YAML mistakes or configuration errors.

Automated validation provides a quality gate before configuration changes are accepted into the repository.

---

### Why Argo CD?

Argo CD allows the Kubernetes cluster to continuously compare its state against the desired configuration stored in Git.

This provides both automated deployment and drift detection while supporting the goal of keeping Git as the source of truth.

---

### Why Prometheus and Grafana?

As the platform grows, I don't want to rely on manually checking individual systems to determine whether everything is healthy.

Prometheus provides metrics collection while Grafana provides a central place to visualise that information.

Together they provide the foundation for gradually building better observability into the platform.

---

### Why an Internal PKI?

I wanted to understand certificate management beyond simply accepting self-signed certificate warnings.

Building an internal PKI allowed me to work with private keys, Certificate Signing Requests, Certificate Authorities, certificate chains and client trust in a practical environment.

It also provides a foundation for automating certificate lifecycle management later.

---

## Keeping Things Simple

One thing I've learned while building this project is that it's easy to make a homelab more complicated than it needs to be.

Whenever I consider adding a new technology, I usually ask myself two questions:

- Does it solve a problem I actually have?
- Will I learn something useful from implementing it?

If the answer to both questions is "yes", it probably belongs in the platform.

Otherwise, I'd rather wait until there's a real reason to introduce it.

---

## Current Architecture

The platform currently consists of:

- One Bazzite management workstation
- An Ansible environment running through Distrobox
- One Kubernetes control-plane node
- One Kubernetes worker node
- Git-based configuration management
- Automated validation through GitHub Actions
- GitOps deployment using Argo CD
- Infrastructure and operational automation using Ansible
- Monitoring using Prometheus and Grafana
- Ingress through Traefik
- Internal PKI and trusted HTTPS for Grafana

The environment is intentionally small, but it is large enough to explore many of the workflows and operational problems found in larger infrastructure environments.

---

## Key Takeaways

- Git is the central source of truth for version-controlled platform configuration.
- Ansible manages infrastructure and operational workflows.
- Argo CD manages the desired state of Kubernetes workloads.
- GitHub Actions provides automated validation before changes are accepted.
- Prometheus and Grafana provide visibility into platform health.
- The internal PKI provides a foundation for trusted service communication.
- Automation is preferred over manual administration.
- The architecture is intentionally kept small enough to understand while still allowing new capabilities to be added over time.

---

## Related Documentation

For more detail about individual parts of the platform:

- **[Kubernetes](03-kubernetes.md)**
- **[Ansible](04-ansible.md)**
- **[Continuous Integration](05-ci-cd.md)**
- **[GitOps with Argo CD](06-argocd-gitops.md)**
- **[Monitoring and Observability](07-monitoring.md)**
- **[Network](08-network.md)**
- **[PKI and Certificate Management](09-pki.md)**
- **[Roadmap](20-roadmap.md)**
