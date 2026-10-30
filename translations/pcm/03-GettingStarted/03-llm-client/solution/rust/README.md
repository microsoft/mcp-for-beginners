# How to run dis sample

Na Rust solution dis for di LLM client sample. You need Rust toolchain wey don install; see the [official install guide](https://www.rust-lang.org/tools/install).

Di client dey call one deployed Microsoft Foundry model through di Azure OpenAI
v1 endpoint.

> [!NOTE]
> Di value wey you pass as `model` na your Foundry deployment name, e no necessarily
> di underlying model name.

## -0- Set up Microsoft Foundry

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

## -1- Build di sample

```bash
cargo build
```

## -2- Run di sample

```bash
cargo run
```

Di client go start di calculator MCP server, fetch im tool list, an use
di deployed model to call the `add` tool. You go see output wey show
di tool call (for example, "Calling tool: add") an di result of dat call.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->