# Kubernetes Cluster

## Distribution

- k3s

## Cluster Nodes

| Node | Role |
|------|------|
| cluster-plane-01 | Control Plane |
| node-02 | Worker |

## Cluster Topology

```mermaid
flowchart TD

    CP["cluster-plane-01
Control Plane"]

    W1["node-02
Worker"]

    CP --> W1
```

## Planned Services

- Traefik
- cert-manager
- Longhorn
- MetalLB
- Argo CD
- Prometheus
- Grafana
- Loki
