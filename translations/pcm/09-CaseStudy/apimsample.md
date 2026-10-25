# Case Study: How to make REST API show for API Management as MCP server

Azure API Management na service wey dey provide a Gateway on top of your API Endpoints. How e dey work be say Azure API Management dey act like proxy in front of your APIs and fit decide wetin to do with incoming requests.

By using it, you add a whole host of features like:

- **Security**, you fit use everything from API keys, JWT to managed identity.
- **Rate limiting**, na beta feature wey make you fit decide how many calls go pass for a certain time. E dey help make sure say all users get better experience and also make your service no choke with requests.
- **Scaling & Load balancing**. You fit set up a number of endpoints to balance out the load and you fit also decide how to "load balance". 
- **AI features like semantic caching**, token limit and token monitoring and more. These na beta features wey dey improve responsiveness as well as help you dey on top of your token spending. [Read more here](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Why MCP + Azure API Management?

Model Context Protocol dey quickly become standard for agentic AI apps and how to expose tools and data in a consistent way. Azure API Management na natural choice when you need to "manage" APIs. MCP Servers often integrate with other APIs to resolve requests to a tool, for example. Therefore combining Azure API Management and MCP make plenty sense.

## Overview

For this specific use case we go learn how to expose API endpoints as an MCP Server. By doing this, we fit easily make these endpoints part of an agentic app while also leveraging the features wey Azure API Management give.

## Key Features

- You choose the endpoint methods wey you want make dem exposed as tools.
- The extra features wey you go get depend on wetin you configure in the policy section for your API. But here we go show you how you fit add rate limiting.

## Pre-step: import an API

If you don get an API in Azure API Management already, good, then you fit skip this step. If not, check out this link, [importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expose API as MCP Server

To expose the API endpoints, make we follow these steps:

1. Navigate to Azure Portal and go to this address <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Navigate to your API Management instance.

1. In the left menu, select APIs > MCP Servers > + Create new MCP Server.

1. In API, select a REST API to expose as an MCP server.

1. Select one or more API Operations to expose as tools. You fit select all operations or only specific operations.

    ![Choose methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Select **Create**.

1. Navigate to the menu option **APIs** and **MCP Servers**, you go see the following:

    ![See the MCP Server for the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    The MCP server don get created and the API operations don expose as tools. The MCP server dey listed in the MCP Servers pane. The URL column dey show the endpoint of the MCP server wey you fit call for testing or inside a client application.

## Optional: Configure policies

Azure API Management get the core concept of policies where you fit set up different rules for your endpoints like for example rate limiting or semantic caching. These policies dem author for XML.

Here na how you fit set up a policy to rate limit your MCP Server:

1. In the portal, under APIs, select **MCP Servers**.

1. Select the MCP server you created.

1. In the left menu, under MCP, select **Policies**.

1. In the policy editor, add or edit the policies wey you want to apply to the MCP server's tools. The policies dey defined in XML format. For example, you fit add a policy to limit calls to the MCP server's tools (in this example, 5 calls per 30 seconds per client IP address). Here na the XML wey go make am rate limit:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Here na an image of the policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Try am out

Make we make sure say our MCP Server dey work as e suppose.

> [!NOTE]
> Azure API Management currently dey expose this server through the Streamable
> HTTP `/mcp` endpoint. The older HTTP+SSE `/sse` transport na deprecated and
> e suppose make dem use am only with legacy clients.

For this, we go use Visual Studio Code and GitHub Copilot and its Agent mode. We go add the MCP server to a *mcp.json* file. By doing so, Visual Studio Code go act as a client with agentic capabilities and end users go fit type a prompt and interact with that server.

Make we see how to add the MCP server in Visual Studio Code:

1. Use the MCP: **Add Server command from the Command Palette**.

1. When dem prompt you, select the server type: **HTTP (HTTP or Server Sent Events)**.

1. Enter the Streamable HTTP URL shown for the MCP server in API Management.
    For example:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Enter a server ID of your choice. This no too important but e go help you remember wetin this server instance be.

1. Select whether to save the configuration to your workspace settings or user settings.

    - **Workspace settings** - The server configuration dey saved to a `.vscode/mcp.json` file, wey only dey available in the current workspace.

      *mcp.json*

      ```json
      "servers": {
          "APIM petstore" : {
              "type": "http",
              "url": "url-to-mcp-server/mcp"
          }
      }
      ```

    - **User settings** - The server configuration dey added to your global *settings.json* file and dey available across all workspaces. The configuration go look similar to the following:

      ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. You also need to add a configuration header to make sure say e authenticate properly towards Azure API Management. E dey use a header wey dem dey call **Ocp-Apim-Subscription-Key**.

    - This na how you fit add am to settings:


    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), this go cause a prompt to show to ask you for the API key value wey you fit find in Azure Portal for your Azure API Management instance.

   - If you wan add am to *mcp.json* instead, you fit add am like so:

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

### Use Agent mode

Now we don set everything either for settings or in *.vscode/mcp.json*. Make we try am. 

You suppose see a Tools icon like so, wey the exposed tools from your server dey listed:

![Tools wey come from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Click the tools icon and you go see a list of tools like so:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Enter a prompt in the chat to invoke the tool. For example, if you selected a tool to get information about an order, you fit ask the agent about an order. Here na an example prompt:

    ```text
    get information from order 2
    ```

    You go now be presented with a tools icon wey go ask you to proceed to call a tool. Select to continue to run the tool, you go now see an output like this:

    ![Result wey come from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Wetin you see for above depend on which tools you don set up, but the idea na say you go get textual response like that**


## References

Here na how you fit learn more:

- [Tutorial about Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Great repo wey show plenty AI capabilities with Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/)  E get workshops wey dey use Azure Portal, wey na a good way to start to evaluate AI capabilities.

## Wetin Next

- Back to: [Case Studies Overview](./README.md)
- Next: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->