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
