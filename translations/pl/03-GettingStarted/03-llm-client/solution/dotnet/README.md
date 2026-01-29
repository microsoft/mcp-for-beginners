# Uruchom ten przykład

> [!NOTE]
> Ten przykład zakłada, że korzystasz z instancji GitHub Codespaces. Jeśli chcesz uruchomić go lokalnie, musisz utworzyć personalny token dostępu (PAT) na GitHub.
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

## Instalacja bibliotek

```sh
dotnet restore
```

Powinno to zainstalować następujące biblioteki: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## Uruchomienie

```sh 
dotnet run
```

Powinieneś zobaczyć wynik podobny do:

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

Wiele z wyjścia to tylko debugowanie, ale ważne jest to, że wyświetlasz narzędzia z MCP Server, przekształcasz je w narzędzia LLM i otrzymujesz odpowiedź klienta MCP "Sum 6".

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.