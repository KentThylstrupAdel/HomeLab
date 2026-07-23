# Network Documentation

## Network

| Network | CIDR |
|----------|------|
| Home LAN | 192.168.86.0/24 |

## Hosts

| Host | IP Address |
|------|------------|
| Bazzite Workstation | 192.168.86.248 |
| cluster-plane-01 | 192.168.86.100 |
| node-02 | 192.168.86.160 |

## SSH Access

The Bazzite workstation acts as the management host and connects to all servers using SSH.
Public/Private key has been established and installed for ease of access.

```text
Bazzite
 ├── SSH → cluster-plane-01
 └── SSH → node-02
```
