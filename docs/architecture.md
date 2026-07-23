# Homelab Architecture

## Overview

This document describes the current architecture of my homelab.

## Infrastructure

| Hostname | Operating System | IP Address | Role |
|----------|------------------|------------|------|
| Bazzite Workstation | Bazzite Linux | 192.168.86.248 | Workstation & Ansible Controller |
| cluster-plane-01 | Ubuntu Server | 192.168.86.100 | Kubernetes (k3s) Control Plane |
| node-02 | Ubuntu Server | 192.168.86.160 | Kubernetes (k3s) Worker Node |

---

## Architecture Diagram

```mermaid
flowchart LR

    subgraph LAN["Home Network (192.168.86.0/24)"]

        BZ["💻
Bazzite Linux
192.168.86.248

Ansible Controller"]

        subgraph K3S["Kubernetes Cluster (k3s)"]

            CP["🖥️
cluster-plane-01
192.168.86.100

Control Plane"]

            N2["🖥️
node-02
192.168.86.160

Worker Node"]

            CP <-->|Cluster Communication| N2
        end

        BZ -->|SSH / Ansible| CP
        BZ -->|SSH / Ansible| N2

    end
```

---

## Components

### Bazzite Linux

- Daily workstation
- Runs Ansible
- SSH access to infrastructure
- Used for cluster management

### cluster-plane-01

- Ubuntu Server
- k3s Control Plane
- Kubernetes API Server
- Cluster management

### node-02

- Ubuntu Server
- k3s Worker Node
- Runs Kubernetes workloads

---

## Future Expansion as proposed by the incredible internet!

Planned additions:

- [ ] Longhorn
- [ ] MetalLB
- [ ] Traefik
- [ ] cert-manager
- [ ] Argo CD
- [ ] Prometheus
- [ ] Grafana
- [ ] Loki
- [ ] Pi-hole
- [ ] NAS
- [ ] GitHub Actions
