<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2228721599c0c8673de83496b4d7d7a9",
  "translation_date": "2025-11-18T19:41:37+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "pcm"
}
-->
# Case Study: Show REST API for API Management as MCP Server

Azure API Management na service wey dey provide Gateway on top your API Endpoints. How e dey work be say Azure API Management go act like proxy wey go dey front of your APIs and e fit decide wetin to do with requests wey dey come.

If you use am, you go fit add plenty features like:

- **Security**, you fit use anything from API keys, JWT to managed identity.
- **Rate limiting**, one better feature be say you fit decide how many calls go pass for one certain time. This one go help make sure say all users go enjoy and your service no go too full with requests.
- **Scaling & Load balancing**. You fit set up plenty endpoints to balance the load and you fit decide how you wan "load balance".
- **AI features like semantic caching**, token limit and token monitoring and more. These features dey improve how fast e go respond and e go help you manage your token spending. [Read more here](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Why MCP + Azure API Management?

Model Context Protocol dey quick turn to standard for agentic AI apps and how to show tools and data in one consistent way. Azure API Management na better choice if you wan "manage" APIs. MCP Servers dey usually join with other APIs to solve requests to one tool for example. So to combine Azure API Management and MCP make plenty sense.

## Overview

For this use case, we go learn how to show API endpoints as MCP Server. If we do am like this, we fit make these endpoints part of one agentic app and still enjoy the features wey Azure API Management get.

## Key Features

- You go fit choose the endpoint methods wey you wan show as tools.
- The extra features wey you go get go depend on wetin you configure for the policy section for your API. But for here, we go show you how you fit add rate limiting.

## Pre-step: Import API

If you don already get API for Azure API Management, e good, you fit skip this step. If you no get, check this link, [importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Show API as MCP Server

To show the API endpoints, make we follow these steps:

1. Go Azure Portal for this address <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Go your API Management instance.

1. For the left menu, select APIs > MCP Servers > + Create new MCP Server.

1. For API, choose REST API wey you wan show as MCP server.

1. Choose one or more API Operations wey you wan show as tools. You fit choose all operations or only the ones wey you want.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Select **Create**.

1. Go the menu option **APIs** and **MCP Servers**, you suppose see this:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    The MCP server don create and the API operations don show as tools. The MCP server go dey listed for the MCP Servers pane. The URL column go show the endpoint of the MCP server wey you fit call for testing or inside one client application.

## Optional: Configure Policies

Azure API Management get one core concept of policies wey you fit use set different rules for your endpoints like rate limiting or semantic caching. These policies dey use XML.

Here’s how you fit set policy to rate limit your MCP Server:

1. For the portal, under APIs, select **MCP Servers**.

1. Select the MCP server wey you create.

1. For the left menu, under MCP, select **Policies**.

1. For the policy editor, add or edit the policies wey you wan apply to the MCP server tools. The policies dey defined for XML format. For example, you fit add policy to limit calls to the MCP server tools (for this example, 5 calls per 30 seconds per client IP address). Here’s XML wey go make am rate limit:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Here’s one image of the policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Try am out

Make we confirm say our MCP Server dey work as e suppose.

For this one, we go use Visual Studio Code and GitHub Copilot and its Agent mode. We go add the MCP server to one *mcp.json* file. If we do am like this, Visual Studio Code go act like client with agentic capabilities and end users go fit type prompt and interact with the server.

Make we see how to add the MCP server for Visual Studio Code:

1. Use the MCP: **Add Server command from the Command Palette**.

1. When dem ask, choose the server type: **HTTP (HTTP or Server Sent Events)**.

1. Enter the URL of the MCP server for API Management. Example: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE endpoint) or **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP endpoint), note the difference between the transports na `/sse` or `/mcp`.

1. Enter one server ID wey you like. This value no too matter but e go help you remember wetin this server instance be.

1. Choose whether to save the configuration to your workspace settings or user settings.

  - **Workspace settings** - The server configuration go save to one .vscode/mcp.json file wey dey only available for the current workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    or if you choose streaming HTTP as transport, e go small different:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - The server configuration go dey added to your global *settings.json* file and e go dey available for all workspaces. The configuration go look like this:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. You go still need to add configuration, one header to make sure say e dey authenticate well with Azure API Management. E dey use one header wey dem call **Ocp-Apim-Subscription-Key*. 

    - Here’s how you fit add am to settings:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), this one go make prompt show to ask you for the API key value wey you fit find for Azure Portal for your Azure API Management instance.

   - To add am to *mcp.json* instead, you fit add am like this:

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

Now we don set everything for either settings or for *.vscode/mcp.json*. Make we try am.

You suppose see one Tools icon like this, where the tools wey your server show go dey listed:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Click the tools icon and you suppose see list of tools like this:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Enter one prompt for the chat to use the tool. For example, if you choose one tool to get information about one order, you fit ask the agent about the order. Here’s one example prompt:

    ```text
    get information from order 2
    ```

    You go see one tools icon wey go ask you to continue call the tool. Select to continue run the tool, you suppose see output like this:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **wetin you go see for above go depend on the tools wey you set up, but the idea na say you go get one text response like above**

## References

Here’s how you fit learn more:

- [Tutorial on Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Better repo wey show many AI capabilities with Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/)  E get workshops wey dey use Azure Portal, wey be better way to start evaluate AI capabilities.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey accurate well. Di original dokyument for di language wey dem take write am first na di one wey you go take as di correct one. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->