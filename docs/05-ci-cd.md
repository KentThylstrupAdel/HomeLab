# Continuous Integration

## Purpose

One of the habits I wanted to build while working on this project was validating changes before they reached the platform.

Even in a small homelab, it's easy to introduce YAML mistakes, broken Helm charts or invalid Ansible playbooks.

Using GitHub Actions means I can catch many of those problems automatically instead of discovering them later when something fails.

---

## CI Workflow

<p align="center">
  <img src="images/infrastructure-validation-pipeline.png"
       alt="Continuous Integration Workflow"
       width="900">
</p>

Whenever I push changes to GitHub, a workflow runs automatically.

The workflow checks that the repository is still in a healthy state before I continue working with it.

At the moment, the pipeline validates:

* YAML files
* Ansible playbooks
* Helm charts
* Kubernetes manifests

It's a simple pipeline, but it already catches many of the mistakes I would otherwise have found manually.

---

## Why GitHub Actions?

Since the rest of the project already lives in GitHub, GitHub Actions felt like a natural choice.

It integrates directly with the repository and makes it easy to validate changes every time I push new code.

For this project, it gives me everything I need without adding unnecessary complexity.

---

## My Workflow

A typical change looks something like this:

1. Make a change locally.
2. Commit and push it to GitHub.
3. GitHub Actions validates the repository.
4. Fix any issues if validation fails.
5. Continue with deployment through Argo CD.

That means I usually know whether something is broken before it ever reaches the Kubernetes cluster.

---

## What I've Learned

Before building this project, I mostly thought of CI as something used in software development.

Working on the homelab changed that perspective.

Even though I'm not compiling an application, validating infrastructure code has been just as valuable.

A missing space in a YAML file or a mistake in a Helm chart can easily prevent an application from deploying correctly.

Catching those issues early saves a lot of troubleshooting later.

---

## Design Decisions

A few ideas have guided how I built the pipeline.

### Keep Validation Fast

The pipeline should finish quickly.

If validation takes too long, it's tempting to stop using it.

---

### Validate Before Deployment

I'd rather catch configuration mistakes during validation than while trying to debug a running cluster.

That keeps troubleshooting focused on real platform issues instead of simple syntax errors.

---

### Start Simple

The current pipeline is intentionally small.

As I continue expanding the platform, the validation can grow alongside it.

There's no need to automate everything on day one.

---

## Future Improvements

Some ideas I'd like to explore include:

* Security scanning
* Container image validation
* More advanced Kubernetes testing
* Additional linting and quality checks

These aren't essential for the current project, but they would be interesting areas to learn more about as the platform evolves.

---

## Key Takeaways

* GitHub Actions validates changes before they reach the platform.
* Automated validation catches common configuration mistakes early.
* Even a simple CI pipeline adds confidence when making changes.
* Infrastructure benefits from Continuous Integration just as much as application code.
* The pipeline will continue evolving as the platform grows.

---

## Related Documentation

Once changes have been validated, they are deployed through GitOps using Argo CD.

Continue with:

* [06-argocd-gitops.md](06-argocd-gitops.md)
