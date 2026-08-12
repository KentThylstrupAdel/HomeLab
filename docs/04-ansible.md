# Ansible

## Purpose

One of the first things I wanted to avoid in this project was manually configuring servers.

If I ever needed to rebuild a machine or repeat a configuration, I didn't want to rely on memory or handwritten notes.

That's why I chose Ansible as the primary tool for infrastructure automation.

---

## What Ansible Manages

<p align="center">
  <img src="images/ansible-management.png"
       alt="Ansible Management"
       width="900">
</p>

Ansible is responsible for preparing and maintaining the servers that make up the platform.

Some examples include:

* Installing packages
* Updating systems
* Deploying Kubernetes components
* Installing Helm
* Configuring supporting services
* Keeping configuration consistent across machines

Whenever possible, I'd rather write a playbook once than repeat the same commands multiple times.

---

## Why Ansible?

Before starting this project, most of my Linux administration was done manually.

That works when you only have one machine, but it quickly becomes repetitive as the environment grows.

Using Ansible has helped me build better habits by treating infrastructure as something that can be reproduced instead of something that has to be configured manually each time.

---

## How I Use It

The playbooks are stored in the Git repository alongside the rest of the project.

That means infrastructure changes are version controlled just like application code.

A typical workflow looks something like this:

1. Update a playbook.
2. Test it.
3. Commit the change.
4. Run the playbook.
5. Verify the result.

Keeping the playbooks in Git also makes it much easier to understand how the platform has evolved over time.

---

## Building Playbooks

Most playbooks focus on one specific task.

Examples include:

* Installing software
* Updating packages
* Deploying Helm charts
* Preparing Kubernetes nodes
* Installing platform components

I've found that keeping playbooks focused makes them easier to understand, troubleshoot and reuse.

---

## Operational Playbooks

As the homelab has matured, I've started building operational playbooks rather than focusing only on deployment.

The current playbooks include:

- `healthcheck.yml`
  - Checks Ubuntu host health
  - Verifies Kubernetes node readiness
  - Checks Pod health
  - Verifies Grafana availability
  - Verifies Prometheus availability

- `maintenance.yml`
  - Runs a pre-maintenance health check
  - Updates Ubuntu servers one at a time
  - Reboots hosts if required
  - Waits for the Kubernetes cluster to recover
  - Runs a post-maintenance health check

The goal is to build a repeatable maintenance workflow that can safely perform routine operational tasks.

---

## REST API Automation

Besides SSH-based automation, I've started using Ansible's uri module to interact with REST APIs. As part of the homelab I have created playbooks that:

* Query a test API (used httpbin)
* Retrieved Grafana health information
* Query Kubernetes for namespaces and pods
* Scale a Kubernetes deployment through the REST API

---

## Lessons Learned

One thing this project has taught me is that automation isn't just about saving time.

It's also about reducing mistakes.

A command typed manually today might be forgotten next month, but a playbook documents exactly what was done and can be run again whenever it's needed.

I've also learned that writing good automation usually takes longer than running the commands manually the first time—but it pays off every time after that.

---

## Design Decisions

A few principles guide how I write playbooks.

### Keep Tasks Focused

I prefer several smaller playbooks over one very large playbook that tries to do everything.

It's usually easier to understand and maintain later.

---

### Make Playbooks Repeatable

Running a playbook multiple times shouldn't create unexpected changes.

That makes it much easier to update systems with confidence.

---

### Version Everything

Playbooks live in Git together with the rest of the platform.

That keeps infrastructure changes visible and makes it easier to revisit earlier decisions if needed.

---

## Future Improvements

Some areas I'd like to improve include:

* Better use of Ansible roles
* More reusable variables
* Improved inventory management
* Additional automation for new platform components

As the homelab grows, I'd like the automation to grow with it rather than becoming harder to maintain.

---

## Key Takeaways

* Ansible is my primary tool for infrastructure automation.
* The goal is to reduce manual administration and improve consistency.
* Infrastructure changes are stored in Git alongside the rest of the project.
* Small, focused playbooks are easier to maintain than large, complex ones.
* Automation has become just as much about reliability as it is about saving time.

---

## Related Documentation

After the infrastructure is prepared with Ansible, the next step is validating changes before deployment.

Continue with:

* [05-ci-cd.md](05-ci-cd.md)
