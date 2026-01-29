# ਇਸ ਨਮੂਨੇ ਨੂੰ ਚਲਾਓ

> [!NOTE]
> ਇਹ ਨਮੂਨਾ ਮੰਨਦਾ ਹੈ ਕਿ ਤੁਸੀਂ GitHub Codespaces ਇੰਸਟੈਂਸ ਵਰਤ ਰਹੇ ਹੋ। ਜੇ ਤੁਸੀਂ ਇਸਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ GitHub 'ਤੇ ਇੱਕ personal access token (PAT) ਸੈੱਟਅਪ ਕਰਨਾ ਪਵੇਗਾ।
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

## ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ

```sh
dotnet restore
```

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol

## ਚਲਾਓ

```sh 
dotnet run
```

ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਆਉਟਪੁੱਟ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

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

ਆਉਟਪੁੱਟ ਦਾ ਬਹੁਤ ਹਿੱਸਾ ਸਿਰਫ ਡੀਬੱਗਿੰਗ ਲਈ ਹੈ ਪਰ ਜਰੂਰੀ ਗੱਲ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ MCP Server ਤੋਂ ਟੂਲਜ਼ ਦੀ ਲਿਸਟ ਬਣਾ ਰਹੇ ਹੋ, ਉਹਨਾਂ ਨੂੰ LLM ਟੂਲਜ਼ ਵਿੱਚ ਬਦਲ ਰਹੇ ਹੋ ਅਤੇ ਅਖੀਰ ਵਿੱਚ ਤੁਹਾਨੂੰ MCP client ਦਾ ਜਵਾਬ "Sum 6" ਮਿਲਦਾ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।