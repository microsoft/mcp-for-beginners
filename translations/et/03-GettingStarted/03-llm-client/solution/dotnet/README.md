# Käivita see näidis

> [!NOTE]
> See näidis eeldab, et kasutate GitHub Codespaces'i instantsi. Kui soovite seda kohapeal käivitada, peate GitHubis seadistama isikliku juurdepääsuluba (PAT).
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

## Raamatukogude installimine

```sh
dotnet restore
```

Peaks installima järgmised raamatukogud: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtocol 

## Käivitamine

```sh 
dotnet run
```

Peaksite nägema väljundit, mis sarnaneb järgmisega:

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

Suur osa väljundist on lihtsalt silumine, kuid oluline on see, et loetlete tööriistad MCP serverist, muudate need LLM tööriistadeks ja tulemuseks on MCP kliendi vastus "Sum 6".

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.