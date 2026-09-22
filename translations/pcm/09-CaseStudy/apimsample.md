# Case Study: Show REST API for API Management as MCP server

Azure API Management, na service wey dey provide Gateway ontop your API Endpoints. How e dey work be say Azure API Management dey act like proxy for front of your APIs and fit decide wetin to do with incoming requests.

By using am, you come add plenty features like:

- **Security**, you fit use anything from API keys, JWT go reach managed identity.
- **Rate limiting**, one beta feature na say you fit decide how many calls go fit pass per one time unit. Dis one dey help make sure say all users get beta experience and your service no go overload with requests.
- **Scaling & Load balancing**. You fit set up plenti endpoints to balance load and you fit also choose how to "load balance". 
- **AI features like semantic caching**, token limit and token monitoring and more. Dem beta features wey go improve responsiveness and also dey help you dey control your token use. [Read more here](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). 

## Why MCP + Azure API Management?

Model Context Protocol dey quickly become standard for agentic AI apps and how to show tools and data consistent. Azure API Management na natural choice when you need to "manage" your APIs. MCP Servers dey often integrate with other APIs to fit solve requests to tool for example. So combine Azure API Management and MCP make sense well well.

## Overview

For this use case we go learn how to show API endpoints as MCP Server. If we do am like this, the endpoints fit easily become part of an agentic app plus we fit still use beta features from Azure API Management.

## Key Features

- You go select which endpoint methods you want make dem show as tools.
- Di other beta features wey you go get depend on wetin you configure for policy section for your API. But here we go show you how to fit add rate limiting.

## Pre-step: import API

If you get API already for Azure API Management, good, you fit skip dis step. If no, check dis link, [importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Show API as MCP Server

To show the API endpoints, make we follow these steps:

1. Go Azure Portal and open dis address <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> 
Go your API Management instance.

1. For the left menu, select APIs > MCP Servers > + Create new MCP Server.

1. For API, select one REST API to show as MCP server.

1. Choose one or more API Operations to show as tools. You fit choose all operations or just some specific.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Select **Create**.

1. Go menu choice **APIs** and **MCP Servers**, you go see wetin follow:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server don create and API operations don show as tools. MCP server dey for MCP Servers pane. URL column show endpoint for MCP server wey you fit call for testing or inside client application.

## Optional: Set policies

Azure API Management get main concept called policies where you fit set different rules for your endpoints like rate limiting or semantic caching. These policies na XML for write.

See how you fit set policy to rate limit your MCP Server:

1. For portal, under APIs, select **MCP Servers**.

1. Select MCP server wey you create.

1. For left menu, under MCP, select **Policies**.

1. For policy editor, add or edit policies wey you want apply to MCP server tools. Policies na XML format. For example, you fit add policy to limit calls to MCP server tools (example be say, 5 calls per 30 seconds per client IP address). Dis na XML wey fit rate limit am:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    This na image of policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Try am

Make sure our MCP Server dey work as e suppose.

> [!NOTE]
> Azure API Management dey expose dis server now through Streamable
> HTTP `/mcp` endpoint. Old HTTP+SSE `/sse` transport don old and
> suppose use only with old legacy clients.

For dis, we go use Visual Studio Code and GitHub Copilot plus im Agent mode. We go add MCP server to *mcp.json* file. If we do so, Visual Studio Code go act like client wey get agentic powers and users fit type prompt and interact with the server.

Make we see how to add MCP server for Visual Studio Code:

1. Use MCP: **Add Server command from the Command Palette**.

1. When e ask you, select server type: **HTTP (HTTP or Server Sent Events)**.

1. Put the Streamable HTTP URL wey show for MCP server for API Management.
    For example:
    `https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp`.

1. Enter server ID wey you like. E no too important but e go help you remember the server instance.

1. Choose whether to save config to your workspace settings or user settings.

  - **Workspace settings** - The server config go save to .vscode/mcp.json file wey only dey this workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - The server config go add to your global *settings.json* file and e go dey for all workspaces. The config look like dis:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. You still need add config, one header to make sure e authenticate well towards Azure API Management. E dey use header wey dem call **Ocp-Apim-Subscription-Key*. 

    - See how to add am to settings:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), this one go make prompt show ask you for API key value wey you fit find for Azure Portal for your Azure API Management instance.

   - To add am to *mcp.json* instead, you fit add am like dis:

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

Now everything don set for either settings or for *.vscode/mcp.json*. Make we try am.

You go see Tools icon like dis, where the tools wey your server dey show so they list:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Click tools icon and you go see list of tools like dis:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Put prompt for chat to run tool. For example, if you choose tool to get info about order, you fit ask agent about order. Example prompt be this:

    ```text
    get information from order 2
    ```

    You go now dey show tools icon ask you to continue call tool. Choose to continue run tool, you go see result like this:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **wetin you see for top na depend the tools wey you setup, but idea be say you go get text response like dis**


## References

See how you fit learn more:

- [Tutorial on Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Great repo wey show many AI capabilities with Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/)  Get workshops wey use Azure Portal, beta way to start test AI capabilities.

## Wetin Next

- Back to: [Case Studies Overview](./README.md)
- Next: [Azure AI Travel Agents](./travelagentsample.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->