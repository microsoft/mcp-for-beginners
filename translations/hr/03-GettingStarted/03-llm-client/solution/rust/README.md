# Pokretanje ovog primjera

Ovo je Rust rješenje za uzorak LLM klijenta. Potrebno je imati instaliran Rust alatni lanac; pogledajte [službeni vodič za instalaciju](https://www.rust-lang.org/tools/install).

Klijent poziva implementirani Microsoft Foundry model putem Azure OpenAI
v1 krajnje točke.

> [!NOTE]
> Vrijednost proslijeđena kao `model` je ime vaše Foundry implementacije, a ne nužno
> ime osnovnog modela.

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

## -1- Izgradnja primjera

```bash
cargo build
```

## -2- Pokretanje primjera

```bash
cargo run
```

Klijent pokreće calculator MCP poslužitelj, dohvaća njegov popis alata i koristi
implementirani model za pozivanje `add` alata. Trebali biste vidjeti izlaz koji ukazuje
na poziv alata (na primjer, "Pozivanje alata: add") i rezultat tog poziva.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->