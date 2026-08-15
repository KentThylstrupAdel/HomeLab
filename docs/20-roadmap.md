# Roadmap

## Looking Ahead

This homelab has already taught me far more than I expected when I first started building it.

Along the way I've realised that Platform Engineering isn't about collecting technologies—it's about understanding how they fit together.

There's still plenty to learn, but I'd rather build that knowledge gradually than rush through a long list of tools.

---

## Current Progress

The homelab has grown one step at a time, with each capability building on the previous ones.

Rather than separating completed work from future milestones, the current state of each area is tracked below. This makes it easier to see both what is already working and where I plan to expand the platform next.

### Infrastructure & Ansible

- [x] Configure Ansible for platform management
- [x] Automate server configuration
- [x] Health check playbook
- [x] Maintenance workflow
- [ ] Bootstrap automation
- [ ] Worker node lifecycle
- [ ] Backup automation

### Kubernetes

- [x] Build a Kubernetes cluster with k3s
- [x] Deploy applications using Helm
- [x] Configure Ingress for internal services
- [ ] Practice adding and removing worker nodes
- [ ] Learn StatefulSets and persistent storage
- [ ] Implement backup and recovery
- [ ] Explore high availability
- [ ] Explore Kubernetes Operators

### CI/CD & GitOps

- [x] Store infrastructure and configuration in Git
- [x] Create CI validation with GitHub Actions
- [x] Deploy applications using Argo CD
- [x] Use GitOps as part of the deployment workflow
- [ ] Expand GitHub Actions validation
- [ ] Add security scanning
- [ ] Validate container images
- [ ] Explore more advanced Argo CD features

### Monitoring & Observability

- [x] Deploy Grafana
- [x] Deploy Prometheus
- [x] Build an operational Grafana dashboard
- [x] Monitor Kubernetes node and Pod health
- [x] Monitor CPU, memory and disk usage
- [ ] Deploy Loki
- [ ] Configure Alertmanager
- [ ] Create basic alerts
- [ ] Expand platform health monitoring

### Networking

- [x] Configure internal service access through Ingress
- [x] Provide local hostname access to platform services
- [x] Enable HTTPS for Grafana
- [ ] Explore VLAN segmentation
- [ ] Improve internal DNS
- [ ] Improve Ingress configuration
- [ ] Expand network monitoring

#### Security & PKI

* [x] Internal Root Certificate Authority
* [x] Intermediate Certificate Authority
* [x] Trusted HTTPS for internal services
* [x] Automated certificate expiration checks
* [x] Automated certificate renewal
* [x] Automated Kubernetes TLS Secret updates
* [x] Post-renewal HTTPS validation
* [x] Protect CA credentials using Ansible Vault
* [ ] Unattended certificate lifecycle using systemd
* [ ] Certificate expiration monitoring and alerting
* [ ] Secure/offline Root CA storage
* [ ] Expand PKI to additional internal services

### Documentation

- [x] Document the platform architecture
- [x] Document implemented platform components
- [x] Maintain diagrams of the platform architecture
- [x] Build the repository as a technical portfolio
- [ ] Continue updating documentation as the platform evolves

---

## Long-Term Goal

This project started as a way to learn Kubernetes and automation.

It's gradually become something bigger.

Today I see it as a place where I can safely experiment, make mistakes, solve problems and document what I've learned along the way.

I expect the technologies to change over time, but the goal will remain the same:

> **Become a better Platform Engineer by building, breaking and improving real systems.**

---

## Lessons Learned

Looking back, one of the biggest lessons has been that learning happens much faster when I actually build something.

Reading documentation is valuable, but working through real problems has given me a much deeper understanding of topics like Kubernetes, automation, CI and GitOps.

I've also realised that it's perfectly fine not to know everything from the beginning.

Building the platform one step at a time has made the learning process both more enjoyable and much more sustainable.

---

## Final Thoughts

This repository isn't intended to demonstrate that I already know everything about Platform Engineering.

Instead, it documents what I've built, what I've learned and where I want to go next.

If you've made it this far, I hope you've not only seen the current state of the platform, but also the thought process behind it.

Like the platform itself, this documentation is a living project and will continue to evolve as I gain more experience.
