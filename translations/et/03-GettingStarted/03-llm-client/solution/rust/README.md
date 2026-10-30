# Selle näidise käivitamine

See on Rusti lahendus LLM-kliendi näidisele. Selleks on vaja Rusti tööriistakomplekti; vaata [ametlikku installijuhendit](https://www.rust-lang.org/tools/install).

Klient kutsub juurutatud Microsoft Foundry mudelit läbi Azure OpenAI
v1 lõpp-punkti.

> [!NOTE]
> Väärtus, mis antakse `model` kaudu, on sinu Foundry juurutuse nimi, mitte tingimata
> aluseks oleva mudeli nimi.

## -0- Konfigureeri Microsoft Foundry

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

## -1- Koosta näidis

```bash
cargo build
```

## -2- Käivita näidis

```bash
cargo run
```

Klient käivitab kalkulaatori MCP-serveri, hangib selle tööriistade loendi ja kasutab
juurutatud mudelit `add` tööriista kutsumiseks. Sa peaksid nägema väljundit, mis näitab
tööriista kutset (näiteks, "Calling tool: add") ja selle kutse tulemust.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->