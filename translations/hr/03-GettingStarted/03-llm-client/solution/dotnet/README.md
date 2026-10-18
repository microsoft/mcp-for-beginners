# Pokrenite ovaj primjer

> [!NOTE]
> Deployajte aktivni model poput `gpt-5.1` u Microsoft Foundry i konfigurirajte
> njegov endpoint, API ključ i ime deploymenta.
>
> ```bash
> # zsh/bash
> export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
> export AZURE_OPENAI_API_KEY="<api-key>"
> export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
> ```
>
> ```powershell
> # PowerShell
> $env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
> $env:AZURE_OPENAI_API_KEY = "<api-key>"
> $env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
> ```

## Instalirajte biblioteke

```sh
dotnet restore
```

Ovo instalira OpenAI .NET klijent i Model Context Protocol SDK.

## Pokreni

```sh 
dotnet run
```

Trebali biste vidjeti izlaz sličan ovome:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: OpenAI.Chat.ChatTool
MCP Tools def: 0: OpenAI.Chat.ChatTool
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

Veliki dio izlaza je samo za debugiranje, ali ono što je važno jest da navodite alate s MCP Servera, pretvarate ih u LLM alate i na kraju dobijete MCP klijentski odgovor "Sum 6".

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->