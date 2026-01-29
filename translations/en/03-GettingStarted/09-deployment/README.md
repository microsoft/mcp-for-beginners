# Deploying MCP Servers

Deploying your MCP server lets others access its tools and resources beyond your local setup. There are several deployment options depending on your needs for scalability, reliability, and ease of management. Below you'll find guidance for deploying MCP servers locally, in containers, and in the cloud.

## Overview

This lesson explains how to deploy your MCP Server app.

## Learning Objectives

By the end of this lesson, you will be able to:

- Assess different deployment methods.
- Deploy your app.

## Local development and deployment

If your server is intended to run on users' machines, follow these steps:

1. **Download the server**. If you didn’t create the server, download it to your machine first.  
1. **Start the server process**: Run your MCP server application.

For SSE (not required for stdio type servers):

1. **Configure networking**: Make sure the server is accessible on the expected port.  
1. **Connect clients**: Use local connection URLs like `http://localhost:3000`.

## Cloud Deployment

MCP servers can be deployed on various cloud platforms:

- **Serverless Functions**: Deploy lightweight MCP servers as serverless functions.  
- **Container Services**: Use services like Azure Container Apps, AWS ECS, or Google Cloud Run.  
- **Kubernetes**: Deploy and manage MCP servers in Kubernetes clusters for high availability.

### Example: Azure Container Apps

Azure Container Apps support deploying MCP Servers. This is still a work in progress and currently supports SSE servers.

Here’s how you can do it:

1. Clone a repo:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Run it locally to test:

  ```sh
  uv venv
  uv sync

  # linux/macOS
  export API_KEYS=<AN_API_KEY>
  # windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. To test locally, create a *mcp.json* file in a *.vscode* folder and add the following content:

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

  Once the SSE server is running, click the play icon in the JSON file. You should now see the server’s tools being recognized by GitHub Copilot, indicated by the Tool icon.

1. To deploy, run the following command:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

That’s it—deploy locally or deploy to Azure by following these steps.

## Additional Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## What's Next

- Next: [Practical Implementation](../../04-PracticalImplementation/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.