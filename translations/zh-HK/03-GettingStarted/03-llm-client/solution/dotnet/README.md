# 執行此範例

> [!NOTE]  
> 此範例假設你正在使用 GitHub Codespaces 實例。如果你想在本地執行，則需要在 GitHub 上設定個人存取權杖 (PAT)。  
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

## 安裝函式庫

```sh
dotnet restore
```

應該會安裝以下函式庫：Azure AI Inference、Azure Identity、Microsoft.Extension、Model.Hosting、ModelContextProtcol

## 執行

```sh 
dotnet run
```

你應該會看到類似以下的輸出：

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

大部分輸出只是除錯資訊，但重點是你正在列出 MCP Server 的工具，將它們轉換成 LLM 工具，最後你會得到 MCP 用戶端回應「Sum 6」。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。