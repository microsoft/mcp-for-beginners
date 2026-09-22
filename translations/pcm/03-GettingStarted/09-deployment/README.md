# Deploying MCP Servers

> [!NOTE]
> Configuration examples wey dey use `/sse` endpoint dey target di old HTTP+SSE
> transport. MCP `2026-07-28` remote servers dey use Streamable HTTP, normally na
> server-set endpoint like `/mcp`.

To deploy your MCP server mean say oda people fit use e tools and resources beyond your local environment. E get different ways to deploy depending on how you want am for scalability, reliability, and easier management. Below you go find how to deploy MCP servers for your local machine, for containers, and for cloud.

## Overview

Dis lesson dey teach how to deploy your MCP Server app.

## Learning Objectives

By the time you finish dis lesson, you go fit:

- Check different ways to deploy.
- Deploy your app.

## Local development and deployment

If your server na for run for user machine, follow these steps:

1. **Download the server**. If you no be di one wey write di server, download am first to your machine. 
1. **Start the server process**: Run your MCP server application 

For SSE (no need for stdio type server)

1. **Configure networking**: Make sure say di server dey accessible for di port wey you expect 
1. **Connect clients**: Use local connection URLs like `http://localhost:3000`

## Cloud Deployment

MCP servers fit deploy for different cloud platforms:

- **Serverless Functions**: Deploy small MCP servers as serverless functions
- **Container Services**: Use services like Azure Container Apps, AWS ECS, or Google Cloud Run
- **Kubernetes**: Deploy and manage MCP servers inside Kubernetes clusters for beta available

### Example: Azure Container Apps

Azure Container Apps go support deployment of MCP Servers. E still dey work and e dey support SSE servers now.

How you fit run am:

1. Clone the repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Run am locally to test:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. To try am locally, create one *mcp.json* file inside *.vscode* folder and put this content:

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

  Once SSE server don start, you fit click di play icon inside di JSON file, you go see tools wey server dey pick for GitHub Copilot, look di Tool icon. 

1. To deploy, run dis command:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

That one be am, deploy am locally, deploy am to Azure through these steps.

## Additional Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## What's Next

- Next: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->