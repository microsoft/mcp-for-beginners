# Esegui questo esempio

> [!NOTE]
> Questo esempio presuppone che tu stia utilizzando un'istanza di GitHub Codespaces. Se vuoi eseguirlo localmente, devi configurare un token di accesso personale (PAT) su GitHub.
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

## Installa le librerie

```sh
dotnet restore
```

Dovrebbe installare le seguenti librerie: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Esegui

```sh 
dotnet run
```

Dovresti vedere un output simile a:

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

Gran parte dell'output è solo per il debug, ma ciò che conta è che stai elencando gli strumenti dal MCP Server, li trasformi in strumenti LLM e ottieni una risposta dal client MCP "Sum 6".

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.