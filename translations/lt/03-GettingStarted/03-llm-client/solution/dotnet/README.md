# Paleiskite šį pavyzdį

> [!NOTE]
> Šis pavyzdys daro prielaidą, kad naudojate GitHub Codespaces instanciją. Jei norite paleisti jį lokaliai, turite nustatyti asmeninį prieigos raktą (PAT) GitHub platformoje.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## Įdiekite bibliotekas

```sh
dotnet restore
```

Reikia įdiegti šias bibliotekas: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtocol 

## Paleidimas

```sh 
dotnet run
```

Turėtumėte matyti rezultatą, panašų į:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Dauguma rezultatų yra tik derinimo informacija, tačiau svarbiausia yra tai, kad jūs iš MCP serverio gaunate įrankių sąrašą, paverčiate juos LLM įrankiais ir gaunate MCP kliento atsakymą „Sum 6“.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.