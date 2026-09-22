# Run this sample

> [!NOTE]
> Deploy an active model such as `gpt-5.1` in Microsoft Foundry and configure
> its endpoint, API key, and deployment name.
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

## Install libraries

```sh
dotnet restore
```

This installs the OpenAI .NET client and the Model Context Protocol SDK.

## Run

```sh 
dotnet run
```

You should see an output similar to:

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

A lot of the output us just debugging but what's important is that you are listing tools from the MCP Server, turn those into LLM tools and you end up with an MCP client response "Sum 6".