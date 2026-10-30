# Zagon tega vzorca

To je Rust rešitev za vzorec odjemalca LLM. Potrebujete nameščen Rust toolchain; poglejte [uradni vodič za namestitev](https://www.rust-lang.org/tools/install).

Odjemalec kliče nameščen Microsoft Foundry model preko Azure OpenAI
v1 končne točke.

> [!NOTE]
> Vrednost, posredovana kot `model`, je ime vaše Foundry namestitve, ne nujno
> ime osnovnega modela.

## -0- Konfiguracija Microsoft Foundry

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

## -1- Sestavi vzorec

```bash
cargo build
```

## -2- Zaženi vzorec

```bash
cargo run
```

Odjemalec zažene MCP strežnik kalkulatorja, pridobi seznam njegovih orodij in uporabi
nameščen model za klic orodja `add`. Izpis bi moral prikazati
klic orodja (na primer, "Kličem orodje: add") in rezultat tega klica.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->