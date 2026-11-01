# Kjør dette eksempelet

Dette er Rust-løsningen for LLM-klienteksemplet. Du trenger en installert Rust-verktøykjede; se den [offisielle installasjonsveiledningen](https://www.rust-lang.org/tools/install).

Klienten kaller en distribuert Microsoft Foundry-modell gjennom Azure OpenAI
v1-endepunktet.

> [!NOTE]
> Verdien som sendes som `model` er navnet på Foundry-distribusjonen din, ikke nødvendigvis
> det underliggende modellnavnet.

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

## -1- Bygg eksempelet

```bash
cargo build
```

## -2- Kjør eksempelet

```bash
cargo run
```

Klienten starter kalkulatorens MCP-server, henter verktøyliste, og bruker
den distribuerte modellen til å kalle `add`-verktøyet. Du bør se utdata som indikerer
verktøykallet (for eksempel, "Calling tool: add") og resultatet av det kallet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->