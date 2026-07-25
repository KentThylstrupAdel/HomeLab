# Ansible

## Purpose

This document describes how Ansible is used to automate infrastructure management within the homelab.

Rather than manually configuring servers, Ansible provides a repeatable and version-controlled approach to provisioning, configuring, and maintaining the platform.

Infrastructure automation forms one of the core engineering principles of this project and helps ensure consistency across all managed systems.

---

## Scope

This document covers:

* Infrastructure automation
* Inventory management
* Playbook organization
* Configuration management
* Design decisions
* Operational workflow

---

## Why Ansible?

Manual configuration is difficult to reproduce and often leads to configuration drift over time.

Ansible addresses this by defining infrastructure as code.

Every configuration change can be:

* Version controlled
* Reviewed
* Repeated
* Audited
* Improved over time

This makes infrastructure management more predictable while reducing repetitive administrative work.

---

## Management Architecture

<p align="center">
  <img src="images/ansible-management.png"
       alt="Ansible Management Architecture"
       width="950">
</p>

The Bazzite workstation acts as the management node.

All infrastructure automation is executed from an isolated Distrobox container, ensuring that the host operating system remains clean while providing a reproducible engineering environment.

Managed servers are accessed securely using SSH key authentication.

---

## Infrastructure Management Workflow

The typical infrastructure workflow follows these steps:

1. Infrastructure changes are written as Ansible playbooks.
2. Playbooks are committed to Git.
3. Changes are validated through GitHub Actions.
4. Playbooks are executed against the target infrastructure.
5. Infrastructure reaches the desired configuration.

This workflow promotes consistency while minimizing manual intervention.

---

## Inventory Management

Infrastructure is organized using an Ansible inventory.

The inventory defines:

* Managed hosts
* Host groups
* Connection methods
* Variables

Separating inventory from automation logic improves maintainability and makes it easier to expand the platform in the future.

---

## Playbook Organization

Playbooks are organized according to their responsibilities.

Typical automation tasks include:

* Operating system updates
* Kubernetes installation
* Helm installation
* Application deployment
* Platform configuration
* Service installation

Each playbook focuses on a single responsibility, making automation easier to understand and maintain.

---

## Idempotent Configuration

One of Ansible's key advantages is idempotency.

Running the same playbook multiple times should produce the same desired system state without introducing unintended changes.

This allows infrastructure automation to be executed repeatedly with confidence.

---

## SSH Authentication

Infrastructure management relies exclusively on SSH key authentication.

Benefits include:

* Secure authentication
* Elimination of password-based logins during automation
* Simplified unattended execution
* Improved operational security

SSH keys are configured before infrastructure automation is introduced.

---

## Infrastructure as Code

Infrastructure configuration is maintained alongside application code within the Git repository.

This provides:

* Complete version history
* Change tracking
* Rollback capability
* Collaborative development
* Reproducible environments

Infrastructure becomes part of the software development lifecycle rather than a separate operational task.

---

## Design Decisions

Several architectural decisions influenced the automation strategy.

### Why Ansible?

Ansible is agentless, easy to understand, and widely adopted for infrastructure automation.

Its declarative approach aligns well with the overall Platform Engineering goals of the project.

---

### Why Distrobox?

The engineering workstation runs Bazzite Linux, an immutable operating system.

Running Ansible within Distrobox provides a consistent Linux environment while preserving the benefits of an immutable host system.

---

### Why SSH Keys?

SSH keys enable secure, repeatable, and unattended infrastructure management without exposing passwords.

---

### Why Agentless Automation?

Avoiding agents reduces operational complexity and makes it easier to manage a small infrastructure while still reflecting common enterprise practices.

---

## Operational Principles

Infrastructure automation follows several guiding principles.

* Infrastructure should never rely on undocumented manual configuration.
* Every configuration change should be reproducible.
* Playbooks should remain idempotent.
* Automation should be understandable before being optimized.
* Small, focused playbooks are preferred over large monolithic automation.

---

## Key Takeaways

* Ansible provides repeatable infrastructure automation.
* Infrastructure is treated as code and maintained in Git.
* SSH key authentication enables secure, agentless management.
* Playbooks are designed to be idempotent and maintainable.
* Automation reduces configuration drift and improves consistency across the platform.

---

## Related Documentation

Continue with:

* [05-ci-cd.md](05-ci-cd.md)
* [06-gitops.md](06-gitops.md)

For the platform architecture, see:

* [02-architecture.md](02-architecture.md)

For Kubernetes-specific implementation details, see:

* [03-kubernetes.md](03-kubernetes.md)
