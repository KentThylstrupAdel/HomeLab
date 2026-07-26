# GitOps with Argo CD

## Purpose

Once I had Kubernetes running, I wanted a better way to deploy and manage applications than applying YAML files manually.

That's what led me to GitOps and Argo CD.

Instead of treating Git as a backup of the configuration, Git becomes the place that defines how the cluster should look.

---

## GitOps Workflow

<p align="center">
  <img src="images/gitops-workflow.png"
       alt="GitOps Workflow"
       width="900">
</p>

The basic workflow is straightforward:

1. Make a change in Git.
2. Push the change to GitHub.
3. GitHub Actions validates the repository.
4. Argo CD detects the update.
5. The Kubernetes cluster is synchronized automatically.

Most of the time, I don't need to deploy anything manually.

---

## Why Argo CD?

Before this project I was mostly thinking in terms of manually deploying changes whenever something needed updating.

Argo CD introduced me to a different way of thinking.

Rather than asking:

> *"How do I deploy this?"*

the question becomes:

> *"Is Git describing the state I want?"*

If the answer is yes, Argo CD takes care of bringing the cluster into that state.

That change in mindset has probably been one of the biggest things I've learned while building this homelab.

---

## Why GitOps?

One thing I like about GitOps is that everything starts in Git.

If I want to understand why something changed, I don't have to remember which commands I ran on a server a few weeks ago.

I can simply look at the commit history.

That makes the platform easier to understand and much easier to recover if something goes wrong.

---

## Working with Argo CD

Most of my interaction with Argo CD is fairly simple.

I typically:

* Add or update manifests.
* Commit the changes.
* Watch GitHub Actions validate the repository.
* Let Argo CD synchronize the cluster.
* Verify that everything deployed successfully.

It's a workflow that's become surprisingly natural after using it for a while.

---

## Things I've Learned

When I first started looking at GitOps, I honestly thought it sounded like an extra layer that wasn't really necessary.

After working with it, I've changed my mind.

It removes a lot of manual deployment work and gives me confidence that the cluster reflects what's stored in Git.

I also spend much less time wondering whether I've forgotten to update something manually.

---

## Design Decisions

### Git Is the Source of Truth

If there's a difference between Git and the running cluster, I want Git to win.

That keeps the platform predictable and avoids configuration drift over time.

---

### Avoid Manual Changes

Making manual changes directly in Kubernetes is sometimes useful for troubleshooting.

But if the change should be permanent, I try to make it in Git instead.

That way the next deployment doesn't accidentally overwrite it.

---

### Keep the Workflow Consistent

Every deployment follows the same general process.

That consistency makes the platform easier to understand and means I don't have to remember different deployment methods for different applications.

---

## Future Improvements

As the project grows, I'd like to explore:

* ApplicationSets
* Multi-environment deployments
* Progressive delivery
* More advanced GitOps patterns

For now, I'd rather become comfortable with the fundamentals before adding more complexity.

---

## Key Takeaways

* Git defines the desired state of the platform.
* Argo CD keeps the cluster synchronized with that state.
* Most deployments happen automatically after changes are committed.
* GitOps has changed how I think about managing infrastructure.
* Keeping deployments consistent makes the platform easier to maintain.

---

## Related Documentation

Once applications are running, the next step is making sure they're healthy and observable.

Continue with:

* [07-monitoring.md](07-monitoring.md)
