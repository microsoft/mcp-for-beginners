# Next Steps after `azd init`

## Table of Contents

1. [Next Steps](#next-steps)
2. [What was added](#what-was-added)
3. [Billing](#billing)
4. [Troubleshooting](#troubleshooting)

## Next Steps

### Provision infrastructure and deploy application code

Run `azd up` to provision your infrastructure and deploy to Azure in one step (or run `azd provision` then `azd deploy` to accomplish the tasks separately). Visit the service endpoints listed to see your application up-and-running!

To troubleshoot any issues, see [troubleshooting](#troubleshooting).

### Configure CI/CD pipeline

Run `azd pipeline config -e <environment name>` to configure the deployment pipeline to connect securely to Azure. An environment name is specified here to configure the pipeline with a different environment for isolation purposes. Run `azd env list` and `azd env set` to reselect the default environment after this step.

- Deploying with `GitHub Actions`: Select `GitHub` when prompted for a provider. If your project lacks the `azure-dev.yml` file, accept the prompt to add it and proceed with pipeline configuration.

- Deploying with `Azure DevOps Pipeline`: Select `Azure DevOps` when prompted for a provider. If your project lacks the `azure-dev.yml` file, accept the prompt to add it and proceed with pipeline configuration.

## What was added

### Infrastructure configuration

To describe the infrastructure and application, an `azure.yaml` was added with the following directory structure:

```yaml
- azure.yaml     # azd project configuration
```

This file contains a single service, which references your project's App Host. When needed, `azd` generates the required infrastructure as code in memory and uses it.

If you would like to see or modify the infrastructure that `azd` uses, run `azd infra synth` to persist it to disk.

If you do this, some additional directories will be created:

```yaml
- infra/            # Infrastructure as Code (bicep) files
  - main.bicep      # main deployment module
  - resources.bicep # resources shared across your application's services
```

In addition, for each project resource referenced by your app host, a `containerApp.tmpl.yaml` file will be created in a directory named `manifests` next the project file. This file contains the infrastructure as code for running the project on Azure Container Apps.

*Note*: Once you have synthesized your infrastructure to disk, changes made to your App Host will not be reflected in the infrastructure. You can re-generate the infrastructure by running `azd infra synth` again. It will prompt you before overwriting files. You can pass `--force` to force `azd infra synth` to overwrite the files without prompting.

*Note*: `azd infra synth` is currently an alpha feature and must be explicitly enabled by running `azd config set alpha.infraSynth on`. You only need to do this once.

## Billing

Visit the *Cost Management + Billing* page in Azure Portal to track current spend. For more information about how you're billed, and how you can monitor the costs incurred in your Azure subscriptions, visit [billing overview](https://learn.microsoft.com/azure/developer/intro/azure-developer-billing).

## Troubleshooting

Q: I visited the service endpoint listed, and I'm seeing a blank page, a generic welcome page, or an error page.

A: Your service may have failed to start, or it may be missing some configuration settings. To investigate further:

1. Run `azd show`. Click on the link under "View in Azure Portal" to open the resource group in Azure Portal.
2. Navigate to the specific Container App service that is failing to deploy.
3. Click on the failing revision under "Revisions with Issues".
4. Review "Status details" for more information about the type of failure.
5. Observe the log outputs from Console log stream and System log stream to identify any errors.
6. If logs are written to disk, use *Console* in the navigation to connect to a shell within the running container.

For more troubleshooting information, visit [Container Apps troubleshooting](https://learn.microsoft.com/azure/container-apps/troubleshooting). 

### Additional information

For additional information about setting up your `azd` project, visit our official [docs](https://learn.microsoft.com/azure/developer/azure-developer-cli/make-azd-compatible?pivots=azd-convert).
