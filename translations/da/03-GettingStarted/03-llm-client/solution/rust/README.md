# Kør dette eksempel

Dette er Rust-løsningen til LLM-klienteksemplet. Du skal have en Rust toolchain installeret; se den [officielle installationsvejledning](https://www.rust-lang.org/tools/install).

Klienten kalder en deployeret Microsoft Foundry-model via Azure OpenAI
v1-endpointet.

> [!NOTE]
> Værdien, der sendes som `model`, er navnet på din Foundry-udrulning, ikke nødvendigvis
> det underliggende modelnavn.

## -0- Konfigurer Microsoft Foundry

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

## -1- Byg eksemplet

```bash
cargo build
```

## -2- Kør eksemplet

```bash
cargo run
```

Klienten starter calculator MCP-serveren, henter dens liste over værktøjer og bruger
den deployerede model til at kalde `add`-værktøjet. Du bør se output, der viser
kaldet af værktøjet (for eksempel "Calling tool: add") og resultatet af det kald.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->