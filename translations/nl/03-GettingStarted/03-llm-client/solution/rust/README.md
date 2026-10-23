# Dit voorbeeld uitvoeren

Dit is de Rust-oplossing voor het LLM-clientvoorbeeld. Je hebt een Rust-toolchain nodig; zie de [officiële installatiewijzer](https://www.rust-lang.org/tools/install).

De client roept een geïmplementeerd Microsoft Foundry-model aan via de Azure OpenAI
v1 endpoint.

> [!NOTE]
> De waarde die wordt doorgegeven als `model` is de naam van je Foundry-implementatie, niet noodzakelijkerwijs
> de onderliggende modelnaam.

## -0- Configureer Microsoft Foundry

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

## -1- Bouw het voorbeeld

```bash
cargo build
```

## -2- Voer het voorbeeld uit

```bash
cargo run
```

De client start de calculator MCP-server, haalt de lijst met tools op en gebruikt
het geïmplementeerde model om de `add` tool aan te roepen. Je zou uitvoer moeten zien die
de tool-aanroep aangeeft (bijvoorbeeld "Calling tool: add") en het resultaat van die aanroep.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->