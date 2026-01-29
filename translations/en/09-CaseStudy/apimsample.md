# Case Study: Exposing a REST API in API Management as an MCP Server

Azure API Management is a service that provides a gateway for your API endpoints. Essentially, it acts as a proxy in front of your APIs and determines how to handle incoming requests.

By using Azure API Management, you gain access to a wide range of features, such as:

- **Security**: You can implement everything from API keys and JWT to managed identity.
- **Rate limiting**: This feature allows you to control how many calls are permitted within a specific time frame. It ensures a great user experience and prevents your service from being overwhelmed by requests.
- **Scaling & Load balancing**: You can configure multiple endpoints to distribute the load and decide on the load-balancing strategy.
- **AI features like semantic caching**: These include token limits, token monitoring, and more. These features enhance responsiveness and help you manage token usage effectively. [Learn more here](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Why Combine MCP and Azure API Management?

The Model Context Protocol (MCP) is rapidly becoming a standard for agentic AI applications, providing a consistent way to expose tools and data. Azure API Management is a natural fit when you need to manage APIs. MCP servers often integrate with other APIs to fulfill tool-related requests. Therefore, combining Azure API Management with MCP is a logical choice.

## Overview

In this use case, we will learn how to expose API endpoints as an MCP server. This allows you to integrate these endpoints into an agentic application while leveraging the features of Azure API Management.

## Key Features

- You can choose which endpoint methods to expose as tools.
- Additional features depend on the configurations you set in the policy section of your API. For example, we will demonstrate how to add rate limiting.

## Pre-step: Import an API

If you already have an API in Azure API Management, you can skip this step. Otherwise, refer to this guide: [Importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expose API as an MCP Server

To expose API endpoints, follow these steps:

1. Go to the Azure Portal at <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>. Navigate to your API Management instance.

1. In the left menu, select **APIs > MCP Servers > + Create new MCP Server**.

1. Under **API**, select a REST API to expose as an MCP server.

1. Choose one or more API operations to expose as tools. You can select all operations or specific ones.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Click **Create**.

1. Navigate to **APIs > MCP Servers** in the menu. You should see the following:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    The MCP server is now created, and the API operations are exposed as tools. The MCP server is listed in the MCP Servers pane. The **URL** column displays the endpoint of the MCP server, which you can use for testing or in a client application.

## Optional: Configure Policies

Azure API Management allows you to define policies, which are rules for your endpoints, such as rate limiting or semantic caching. These policies are written in XML.

Here’s how to set up a policy to rate limit your MCP server:

1. In the portal, under **APIs**, select **MCP Servers**.

1. Choose the MCP server you created.

1. In the left menu, under **MCP**, select **Policies**.

1. In the policy editor, add or modify the policies you want to apply to the MCP server's tools. For example, to limit calls to 5 per 30 seconds per client IP address, use the following XML:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Here’s an image of the policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Try It Out

Let’s verify that the MCP server is functioning as expected.

We’ll use Visual Studio Code, GitHub Copilot, and its Agent mode. By adding the MCP server to an *mcp.json* file, Visual Studio Code will act as a client with agentic capabilities, allowing end users to interact with the server via prompts.

Here’s how to add the MCP server in Visual Studio Code:

1. Use the **MCP: Add Server** command from the Command Palette.

1. When prompted, select the server type: **HTTP (HTTP or Server Sent Events)**.

1. Enter the URL of the MCP server in API Management. For example:
   - **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE endpoint)
   - **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP endpoint)

   Note the difference in transport: `/sse` or `/mcp`.

1. Enter a server ID of your choice. This is just a label to help you identify the server instance.

1. Choose whether to save the configuration to your workspace settings or user settings.

   - **Workspace settings**: The server configuration is saved to a *.vscode/mcp.json* file, available only in the current workspace.

     *mcp.json*:

     ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

     If you choose streaming HTTP as the transport, the configuration will look slightly different:

     ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

   - **User settings**: The server configuration is added to your global *settings.json* file, making it available across all workspaces. The configuration will look like this:

     ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Add a header for authentication to ensure proper communication with Azure API Management. Use the **Ocp-Apim-Subscription-Key** header.

   - To add it to settings:

     ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)

     This will prompt you to enter the API key value, which you can find in the Azure Portal for your Azure API Management instance.

   - To add it to *mcp.json*, use the following format:

     ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Use Agent Mode

Now that everything is set up in either settings or *.vscode/mcp.json*, let’s test it.

You should see a **Tools** icon, where the exposed tools from your server are listed:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Click the **Tools** icon to view a list of tools:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Enter a prompt in the chat to invoke a tool. For example, if you exposed a tool to retrieve order information, you can ask the agent about an order. Example prompt:

    ```text
    get information from order 2
    ```

    You’ll see a tools icon prompting you to proceed with calling a tool. Select it to continue, and you should see an output like this:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **The output will vary depending on the tools you’ve set up, but the idea is to receive a textual response like the one above.**

## References

Here are additional resources to learn more:

- [Tutorial on Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)
- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)
- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway): A great repository showcasing AI capabilities with Azure API Management.
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/): Workshops using the Azure Portal, ideal for evaluating AI capabilities.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.