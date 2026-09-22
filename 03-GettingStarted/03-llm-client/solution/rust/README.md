# Running this sample

This is the Rust solution for the LLM client sample. You need a Rust toolchain installed; see the [official install guide](https://www.rust-lang.org/tools/install).

The client calls a deployed Microsoft Foundry model through the Azure OpenAI
v1 endpoint.

> [!NOTE]
> The value passed as `model` is your Foundry deployment name, not necessarily
> the underlying model name.

## -0- Configure Microsoft Foundry

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- Build the sample

```bash
cargo build
```

## -2- Run the sample

```bash
cargo run
```

The client starts the calculator MCP server, fetches its tool list, and uses
the deployed model to call the `add` tool. You should see output indicating
the tool call (for example, "Calling tool: add") and the result of that call.
