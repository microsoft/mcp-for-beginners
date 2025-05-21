# Deploying MCP Servers

Deploying your MCP server allows others to access its tools and resources beyond your local environment. There are several deployment strategies to consider, depending on your requirements for scalability, reliability, and ease of management. Below you'll find guidance for deploying MCP servers locally, in containers, and to the cloud.

## Overview

This lesson covers how to deploy your MCP Server app.

## Learning Objectives

By the end of this lesson, you will be able to:

- Evaluate different deployment approaches.
- Deploy your app.

## Local Development and Deployment

If your server is meant to be consumed by running on a user's machine, you can follow these steps:

1. **Download the server**. If you didn't write the server, download it first to your machine.
2. **Start the server process**: Run your MCP server application.

For SSE (not needed for stdio-type servers):

3. **Configure networking**: Ensure the server is accessible on the expected port.
4. **Connect clients**: Use local connection URLs like `http://localhost:3000`.

## Cloud Deployment

MCP servers can be deployed to various cloud platforms:

- **Serverless Functions**: Deploy lightweight MCP servers as serverless functions.
- **Container Services**: Use services like Azure Container Apps, AWS ECS, or Google Cloud Run.
- **Kubernetes**: Deploy and manage MCP servers in Kubernetes clusters for high availability.

### Example: Azure Container Apps

Azure Container Apps support the deployment of MCP servers. This is still a work in progress and currently supports SSE servers.

Here's how you can go about it:

1. Clone the repo:

    ```sh
    git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
    ```

2. Run it locally to test things out:

    ```sh
    uv venv
    uv sync

    # Linux/macOS
    export API_KEYS=<AN_API_KEY>
    # Windows
    set API_KEYS=<AN_API_KEY>

    uv run fastapi dev main.py
    ```

3. To try it locally, create an *mcp.json* file in a *.vscode* directory and add the following content:

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

    Once the SSE server is started, you can click the play icon in the JSON file. You should now see tools on the server picked up by GitHub Copilot—see the Tool icon.

4. To deploy, run the following command:

    ```sh
    az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
    ```

There you have it: deploy locally, or deploy to Azure through these steps.

## Additional Resources

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps article](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)

## What's Next

Next: [Practical Implementation](/04-PracticalImplementation/README.md)
