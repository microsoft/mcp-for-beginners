# Deploying MCP Servers

Deploying your MCP server dey allow oda people access e tools and resources beyond your local environment. E get plenti deployment ways wey you fit consider, depend on wetin you want for scalability, reliability, and easy management. Down below, you go find how to deploy MCP servers for local machine, inside container, and for cloud.

## Overview

Dis lesson go show you how to deploy your MCP Server app.

## Learning Objectives

By the time you finish dis lesson, you go fit:

- Check different deployment ways.
- Deploy your app.

## Local development and deployment

If your server suppose dey run for users machine, you fit follow dis steps:

1. **Download the server**. If you no write the server, then download am first to your machine.  
1. **Start the server process**: Run your MCP server application 

For SSE (no need for stdio type server)

1. **Configure networking**: Make sure say the server dey reachable for the right port  
1. **Connect clients**: Use local connection URLs like `http://localhost:3000`

## Cloud Deployment

MCP servers fit deploy for different cloud platforms:

- **Serverless Functions**: Deploy small MCP servers as serverless functions
- **Container Services**: Use services like Azure Container Apps, AWS ECS, or Google Cloud Run
- **Kubernetes**: Deploy and manage MCP servers for Kubernetes clusters, make e dey always available

### Example: Azure Container Apps

Azure Container Apps dey support MCP Servers deployment. E still dey work progress and e dey support SSE servers now.

Na so you fit do am:

1. Clone a repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Run am locally to test am:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. To try am locally, create *mcp.json* file for *.vscode* directory and put this content:

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

  Once the SSE server start, you fit click the play icon for the JSON file, you go see tools for the server dey show inside GitHub Copilot, check the Tool icon. 

1. To deploy am, run this command:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

That’s all, deploy am locally, deploy am for Azure through these steps.

## Additional Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## What's Next

- Next: [Advanced Server Topics](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you sabi say automated translations fit get some mistakes or no too clear. Di original document wey e dey for im own language na di correct one wey you suppose use. If na serious info, e good make professional human translation do am. We no go fit take responsibility for any kin misunderstanding or wrong interpretation wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->