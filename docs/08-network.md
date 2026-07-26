# Network

## Purpose

When I started building the homelab, I wanted the network to be simple enough to understand while still reflecting how a small Platform Engineering environment might be structured.

Rather than introducing unnecessary complexity, I've focused on building something that's easy to troubleshoot and can grow over time.

---

## Network Overview

<p align="center">
  <img src="images/network-topology.png"
       alt="Network Topology"
       width="900">
</p>

The environment currently consists of three physical machines connected to my home network.

* **cluster-plane-01** hosts the Kubernetes control plane.
* **node-02** runs workloads as a worker node.
* **My Bazzite workstation** is where I manage the platform using Ansible, Git and kubectl.

All communication between these systems happens over the local network using SSH and the Kubernetes API.

---

## Design Decisions

### Keep the Network Simple

I deliberately avoided creating multiple VLANs or complex routing rules.

At this stage, my goal is to learn Kubernetes and Platform Engineering—not advanced networking.

A simple network makes it easier to understand where problems occur and lets me focus on the platform itself.

---

### Separate Management from the Cluster

I use my workstation to manage the environment rather than running management tools directly on the cluster.

This keeps the Kubernetes nodes focused on running workloads while development and administration happen from a separate machine.

It's also closer to how I expect to work in a professional environment.

---

### Build for Growth

Although the network is intentionally simple today, I've tried to make choices that leave room for future improvements.

As the homelab grows, I can expand the network without needing to redesign everything from scratch.

---

## Current State

The networking is intentionally uncomplicated.

Everything runs on a single home network, and that has worked well for the current size of the environment.

As I've added Kubernetes, GitHub Actions and Argo CD, the focus has been understanding how the different components interact rather than building an enterprise network.

---

## Future Improvements

Networking is another area I'd like to expand over time.

Some ideas include:

* VLAN segmentation
* Internal DNS
* Load balancing
* Ingress improvements
* TLS for internal services
* Better network monitoring

I'll add these gradually as the platform evolves and as I become more comfortable with the technologies involved.

---

## Lessons Learned

One thing I've learned while building this project is that networking doesn't need to be complicated to be useful.

Keeping the design simple has made troubleshooting much easier and allowed me to spend more time learning Kubernetes, automation and GitOps instead of chasing network issues.

As the platform grows, I'll introduce more advanced networking features when they solve a real problem rather than simply because they're available.

---

## Key Takeaways

* The platform runs on a simple home network.
* Management happens from a separate workstation.
* The network is designed to be easy to understand and troubleshoot.
* More advanced networking features are planned as the platform grows.
* Simplicity has helped me focus on learning the platform itself.

---

## Related Documentation

The final chapter outlines where I'd like to take the homelab next and the technologies I plan to explore.

Continue with:

* [09-roadmap.md](09-roadmap.md)
