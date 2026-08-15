## Certificate Lifecycle Automation

The initial PKI implementation was deliberately manual.

Before automating certificate management, I wanted to understand the complete process:

1. Generate a private key.
2. Create a Certificate Signing Request (CSR).
3. Sign the CSR using the Intermediate CA.
4. Build the certificate chain.
5. Deploy the certificate.
6. Configure client trust.
7. Verify the complete trust chain.

Once this process was working manually, I implemented the same lifecycle using Ansible.

### Automated Renewal Workflow

Grafana certificates are currently issued with a validity period of 180 days.

The Ansible certificate lifecycle playbook checks whether the current certificate will expire within 30 days.

```text
Check Certificate Expiration
            │
            ▼
     More than 30 days?
        │           │
       Yes          No
        │           │
        ▼           ▼
     No Change   Generate New Key
                    │
                    ▼
                 Create CSR
                    │
                    ▼
              Intermediate CA
                 Signs CSR
                    │
                    ▼
               Build Chain
                    │
                    ▼
          Update Kubernetes Secret
                    │
                    ▼
               Verify HTTPS
                    │
                    ▼
          Promote New Certificate
```

If the certificate is still valid for more than 30 days, the playbook makes no changes.

When renewal is required, the playbook:

- Generates a new private key.
- Protects the private key with restrictive file permissions.
- Generates a new CSR.
- Uses the Intermediate CA to issue a new 180-day certificate.
- Builds the certificate chain.
- Updates the Kubernetes TLS Secret.
- Verifies that Grafana is successfully serving HTTPS with a trusted certificate.
- Promotes the verified certificate and key to become the current certificate.

The existing certificate is not replaced locally until the newly issued certificate has been deployed and HTTPS verification succeeds.

This provides a basic safety mechanism during certificate replacement.

---

## Protecting CA Credentials

The Intermediate CA private key is encrypted with a passphrase.

The passphrase required for automated certificate issuance is stored as an Ansible variable inside an encrypted Ansible Vault file.

This keeps the secret separate from the playbook itself and prevents the passphrase from appearing directly in the automation stored in Git.

Tasks that provide the CA passphrase to OpenSSL also use:

```yaml
no_log: true
```

to prevent sensitive command information from being displayed in Ansible output.

The Root CA private key is not used by the certificate lifecycle automation.

Its responsibility is limited to establishing trust and signing the Intermediate CA.

```text
Root CA
   │
   │  Not used for normal certificate issuance
   ▼
Intermediate CA
   │
   │  Used by certificate automation
   ▼
Service Certificates
```

This allows the Root CA to eventually be moved to offline or otherwise protected storage.

---

## Current Automation Limitation

Certificate renewal is automated, but execution is currently attended.

The Ansible Vault password must still be supplied when the certificate lifecycle playbook is started:

```bash
ansible-playbook ansible/playbooks/certificate-lifecycle.yml --ask-vault-pass
```

This means certificate generation, signing, deployment and verification are automated, while authorization to access the Intermediate CA credentials still requires manual interaction.

A future improvement is unattended execution using a securely stored Vault credential and a scheduled systemd timer.

The intended model is to check certificate validity regularly and only perform renewal when the certificate enters the configured renewal window.

---

## Lessons Learned

Building the PKI manually before automating it made the automation significantly easier to understand.

Rather than treating certificate renewal as a single command, I now see it as a lifecycle involving key generation, identity requests, certificate issuance, trust chains, deployment and validation.

The implementation also highlighted the relationship between automation and security.

Removing manual interaction can improve reliability, but unattended automation also requires credentials to be available to the automation system. This introduces a security tradeoff that needs to be considered when designing the solution.
