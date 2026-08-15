# Public Key Infrastructure

## Purpose

As the homelab has grown, I wanted to gain practical experience with Public Key Infrastructure (PKI) and certificate management.

Rather than only using automatically generated or self-signed service certificates, I built a small internal Certificate Authority hierarchy and used it to provide trusted HTTPS access to Grafana.

The goal was to understand how certificates, Certificate Authorities, trust chains and private keys work together in practice.

---

## PKI Architecture

The internal PKI consists of a Root Certificate Authority, an Intermediate Certificate Authority and certificates issued to individual services.

```text
HomeLab Root CA
        │
        │ signs
        ▼
HomeLab Intermediate CA
        │
        │ signs
        ▼
Service Certificates
        │
        └── grafana.homelab
