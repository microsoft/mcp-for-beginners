# Pagpapatakbo ng sample na ito

Ito ang Rust na solusyon para sa LLM client sample. Kailangan mong may naka-install na Rust toolchain; tingnan ang [opisyal na gabay sa pag-install](https://www.rust-lang.org/tools/install).

Tinatawag ng client ang isang naka-deploy na Microsoft Foundry na modelo sa pamamagitan ng Azure OpenAI
v1 endpoint.

> [!NOTE]
> Ang halagang ipinasa bilang `model` ay ang iyong Foundry deployment name, hindi kinakailangang
> ang pangalan ng batayang modelo.

## -0- I-configure ang Microsoft Foundry

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

## -1- I-build ang sample

```bash
cargo build
```

## -2- Patakbuhin ang sample

```bash
cargo run
```

Sinisimulan ng client ang calculator MCP server, kinukuha ang listahan ng mga tool nito, at ginagamit
ang naka-deploy na modelo upang tawagan ang `add` na tool. Dapat mong makita ang output na nagpapakita
ng pagtawag ng tool (halimbawa, "Calling tool: add") at ang resulta ng pagtawag na iyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->