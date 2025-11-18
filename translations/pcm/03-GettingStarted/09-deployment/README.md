<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1d9dc83260576b76f272d330ed93c51f",
  "translation_date": "2025-11-18T19:21:39+00:00",
  "source_file": "03-GettingStarted/09-deployment/README.md",
  "language_code": "pcm"
}
-->
# How to Deploy MCP Servers

When you deploy MCP server, e go allow other people fit use di tools and resources wey dey inside am, no be only for your local environment. You get different ways wey you fit take deploy am, depending on wetin you need for scalability, reliability, and how easy e go be to manage am. For here, you go see guide on how to deploy MCP servers for local, inside containers, and for cloud.

## Overview

Dis lesson go show you how you fit deploy your MCP Server app.

## Wetin You Go Learn

By the time you finish dis lesson, you go sabi:

- Check different ways to deploy MCP server.
- Deploy your app.

## Local Development and Deployment

If di server na for people wey dey use am for their machine, you fit follow dis steps:

1. **Download di server**. If na another person write di server, first download am for your machine.
1. **Start di server process**: Run di MCP server application.

For SSE (no need for stdio type server)

1. **Set up networking**: Make sure say di server dey accessible for di port wey you expect.
1. **Connect clients**: Use local connection URLs like `http://localhost:3000`.

## Cloud Deployment

You fit deploy MCP servers for different cloud platforms:

- **Serverless Functions**: Deploy MCP servers wey no heavy as serverless functions.
- **Container Services**: Use services like Azure Container Apps, AWS ECS, or Google Cloud Run.
- **Kubernetes**: Deploy and manage MCP servers for Kubernetes clusters wey go make am dey available well well.

### Example: Azure Container Apps

Azure Container Apps dey support deployment of MCP Servers. Dem still dey work on am and e dey support SSE servers for now.

How you fit do am:

1. Clone di repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Run am for your machine to test am:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. To test am for your machine, create one *mcp.json* file inside *.vscode* directory and put dis content:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Once di SSE server don start, you fit click di play icon for di JSON file, you go see tools for di server dey show for GitHub Copilot, check di Tool icon.

1. To deploy am, run dis command:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Na so e be, deploy am for your machine, deploy am for Azure with dis steps.

## Extra Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## Wetin Next

- Next: [Practical Implementation](../../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for di language wey dem write am first na di main correct source. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->