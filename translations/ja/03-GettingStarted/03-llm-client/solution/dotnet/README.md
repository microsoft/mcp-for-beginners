# このサンプルを実行する

> [!NOTE]  
> このサンプルはGitHub Codespacesのインスタンスを使用していることを前提としています。ローカルで実行したい場合は、GitHubでパーソナルアクセストークン（PAT）を設定する必要があります。  
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

## ライブラリのインストール

```sh
dotnet restore
```

以下のライブラリがインストールされるはずです：Azure AI Inference、Azure Identity、Microsoft.Extension、Model.Hosting、ModelContextProtcol

## 実行

```sh 
dotnet run
```

以下のような出力が表示されるはずです：

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

多くの出力はデバッグ用ですが、重要なのはMCPサーバーからツールをリストアップし、それらをLLMツールに変換し、最終的にMCPクライアントの応答「Sum 6」が得られることです。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。