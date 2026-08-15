## PKI Vision

The current PKI implementation is intentionally manual.

My first goal was to understand the complete certificate lifecycle before attempting to automate it. This included creating the Certificate Authorities, generating private keys and Certificate Signing Requests, signing certificates, verifying the certificate chain and finally deploying a trusted certificate to a real service.

Grafana is the first service using the internal PKI, but the longer-term goal is to make certificate management a platform capability rather than something configured individually for each application.

The intended direction is:

```text
Internal Root CA
        │
        ▼
Intermediate CA
        │
        ▼
Automated Certificate Issuance
        │
        ├── Grafana
        ├── Argo CD
        └── Future Services


```

---

## PKI Roadmap

### Implemented

- ✅ Root Certificate Authority
- ✅ Intermediate Certificate Authority
- ✅ Certificate chain verification
- ✅ Service certificate for `grafana.homelab`
- ✅ Kubernetes TLS Secret
- ✅ HTTPS through Traefik
- ✅ Client trust configuration

### Next Steps

- ⏳ Certificate expiration monitoring
- ⏳ Automated certificate renewal
- ⏳ Automatic Kubernetes Secret updates
- ⏳ Additional service certificates
- ⏳ Secure/offline Root CA storage
- ⏳ Automated validation after certificate replacement
