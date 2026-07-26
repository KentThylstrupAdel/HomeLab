# Monitoring

## Purpose

As the homelab grew, I realised it was becoming harder to answer a simple question:

> **Is everything working as expected?**

That's why I introduced monitoring.

Rather than logging into servers or checking individual services, I wanted a central place to see the health of the platform.

---

## Monitoring Overview

<p align="center">
  <img src="images/monitoring-stack.png"
       alt="Monitoring Stack"
       width="900">
</p>

The monitoring stack is centred around Grafana.

As the platform continues to grow, it will become the main place for viewing dashboards, metrics and the overall health of the environment.

---

## Why Grafana?

I chose Grafana because it's widely used, integrates with many different data sources and provides a good overview of what's happening in the platform.

More importantly, it encourages me to look at the platform from an operational perspective instead of only reacting when something breaks.

---

## What I Monitor

The dashboards currently focus on the platform itself rather than the applications running on it.

Examples include:

* Cluster health
* Node status
* Resource usage
* Platform services

As I add more applications, I'd like the monitoring to grow alongside them.

---

## Lessons Learned

One thing I've realised is that monitoring isn't only useful when something is broken.

It's just as valuable for understanding how the platform behaves when everything is working normally.

That makes it much easier to recognise when something changes unexpectedly.

---

## Design Decisions

### Start with the Platform

Rather than creating dashboards for every application, I wanted to understand the health of the underlying platform first.

Once that foundation is in place, application monitoring becomes much easier to build on.

---

### Keep Dashboards Useful

It's easy to fill Grafana with dozens of dashboards.

I'd rather have a smaller number that I actually use than a large collection that I never look at.

---

### Grow Over Time

The monitoring stack is still evolving.

As I gain more experience, I expect to add new dashboards, alerts and data sources.

---

## Future Improvements

Some areas I'd like to explore include:

* Prometheus
* Loki
* Alertmanager
* Log aggregation
* Custom dashboards
* Alerting

These would give a more complete view of the platform and help me learn more about observability.

---

## Key Takeaways

* Monitoring gives me a better understanding of how the platform behaves.
* Grafana provides a central place to view the health of the environment.
* I focus on monitoring the platform before individual applications.
* The monitoring stack will continue evolving as the homelab grows.
* Understanding normal behaviour makes troubleshooting much easier.

---

## Related Documentation

The next chapter describes the network architecture and how the different parts of the platform communicate.

Continue with:

* [08-network.md](08-network.md)
