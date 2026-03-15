# Practical Implementation

[![How to Build, Test, and Deploy MCP Apps with Real Tools and Workflows](../../../translated_images/pcm/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Click di picture we dey above to watch di video of dis lesson)_

Practical implementation na where di power of di Model Context Protocol (MCP) go clear. Even though to sabi di theory and how MCP architecture dey important, di real kin beta value na wen you apply dis concepts to build, test, and deploy solutions wey solve real-world matter. Dis chapter dey join di gap between to sabi concept plus hands-on development, e go guide you as you wan bring MCP-based apps come life.

Whether you dey develop sharp assistants, put AI for business workflows, or build custom tools for data processing, MCP dey give solid foundation wey flexible. E no dey tied to any language, plus e get official SDKs for popular programming languages wey make e easy for plenty developers. If you use these SDKs well, you fit quickly prototype, try again, and grow your solutions across different platforms and environment dem.

For the next sections, you go see practical examples, sample code, and deployment strategies wey go show you how to implement MCP for C#, Java with Spring, TypeScript, JavaScript, and Python. You also go learn how to debug and test your MCP servers, manage APIs, and deploy solutions for cloud with Azure. These hands-on resources dey designed to speed up your learning and help you build strong MCP apps wey ready for production.

## Overview

Dis lesson go focus on practical sides of MCP implementation for plenty programming languages. We go check how to use MCP SDKs for C#, Java with Spring, TypeScript, JavaScript, and Python to build solid apps, debug and test MCP servers, plus create reusable resources, prompts, and tools.

## Learning Objectives

By di time you finish dis lesson, you go fit:

- Implement MCP solutions using official SDKs for different programming languages
- Debug and test MCP servers properly
- Create and use server features (Resources, Prompts, and Tools)
- Design beta MCP workflows for complicated tasks
- Optimize MCP implementations for better performance and reliability

## Official SDK Resources

Di Model Context Protocol get official SDKs for different languages (wey dey follow [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java with Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Note:** you suppose get dependency on [Project Reactor](https://projectreactor.io). (Check [discussion issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Working with MCP SDKs

Dis section dey give practical examples on how to implement MCP for plenty programming languages. You fit find sample code for di `samples` folder arranged by language.

### Available Samples

Di repo get [sample implementations](../../../04-PracticalImplementation/samples) for dis languages:

- [C#](./samples/csharp/README.md)
- [Java with Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Each sample dey show important MCP concepts and how to do di implementation patterns for each language and ecosystem.

### Practical Guides

Extra guides for practical MCP implementation:

- [Pagination and Large Result Sets](./pagination/README.md) - Handle cursor-based pagination for tools, resources, and big datasets

## Core Server Features

MCP servers fit implement any combination of these features:

### Resources

Resources dey provide context plus data for user or AI model to use:

- Document warehouses
- Knowledge bases
- Structured data sources
- File systems

### Prompts

Prompts na templated messages and workflows for users:

- Pre-set conversation templates
- Guided interaction patterns
- Special dialogue structures

### Tools

Tools na functions wey AI model fit execute:

- Data processing tools
- External API connections
- Computational power
- Search function

## Sample Implementations: C# Implementation

Di official C# SDK repo get many sample implementations wey show different MCP aspects:

- **Basic MCP Client**: Simple example wey show how to create MCP client and call tools
- **Basic MCP Server**: Small server implementation with basic tool registration
- **Advanced MCP Server**: Full server with tool registration, authentication, and error handling
- **ASP.NET Integration**: Examples wey show how to integrate with ASP.NET Core
- **Tool Implementation Patterns**: Different patterns for implementing tools with different complexity levels

Di MCP C# SDK still dey preview and APIs fit change. We go dey update this blog as SDK dey grow.

### Key Features

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Build your [first MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

For full C# implementation samples, visit di [official C# SDK samples repo](https://github.com/modelcontextprotocol/csharp-sdk)

## Sample implementation: Java with Spring Implementation

Di Java with Spring SDK dey offer strong MCP implementation options with enterprise-grade features.

### Key Features

- Spring Framework integration
- Strong type safety
- Reactive programming support
- Full error handling

For complete Java with Spring implementation sample, check [Java with Spring sample](samples/java/containerapp/README.md) for inside samples folder.

## Sample implementation: JavaScript Implementation

Di JavaScript SDK dey lightweight and flexible for MCP implementation.

### Key Features

- Node.js and browser support
- Promise-based API
- Easy to integrate with Express and other frameworks
- WebSocket support for streaming

For full JavaScript implementation sample, check [JavaScript sample](samples/javascript/README.md) inside samples folder.

## Sample implementation: Python Implementation

Di Python SDK dey give Pythonic way to do MCP implementation with better ML framework connections.

### Key Features

- Async/await support with asyncio
- FastAPI integration``
- Easy tool registration
- Native support for popular ML libraries

For full Python implementation sample, check [Python sample](samples/python/README.md) inside samples folder.

## API management

Azure API Management na better way to secure MCP Servers. Di idea na to put Azure API Management before your MCP Server make e handle features wey you go like such as:

- rate limiting
- token management
- monitoring
- load balancing
- security

### Azure Sample

Here get Azure Sample wey dey do exactly dat, dat na [create MCP Server and secure am with Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

See how authorization flow dey happen for di picture below:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

For the picture above, this things happen:

- Authentication/Authorization dey happen using Microsoft Entra.
- Azure API Management dey act as gateway and e dey use policies to direct and manage traffic.
- Azure Monitor dey log all requests for later analysis.

#### Authorization flow

Make we check di authorization flow well well:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

Learn more about di [MCP Authorization specification](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Deploy Remote MCP Server to Azure

Make we see if we fit deploy di sample we mention before:

1. Clone di repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Register `Microsoft.App` resource provider.

   - If you dey use Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
   - If you dey use Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` after some time to check if registration don finish.

1. Run dis [azd](https://aka.ms/azd) command to set up api management service, function app(with code) plus all other Azure resources wey you need

    ```shell
    azd up
    ```

    Dis commands go deploy all the cloud resources for Azure

### Testing your server with MCP Inspector

1. For **new terminal window**, install and run MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    You go see interface wey look like dis:

    ![Connect to Node inspector](../../../translated_images/pcm/connect.141db0b2bd05f096.webp)

1. Press CTRL plus click to load MCP Inspector web app from di URL wey app show (e.g. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Set transport type to `SSE`
1. Set URL to your running API Management SSE endpoint wey show after you do `azd up` and then **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **List Tools**.  Click tool and **Run Tool**.

If all steps don succeed, you don connect to MCP server and you fit call tool.

## MCP servers for Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dis set of repos na quickstart template to build and deploy custom remote MCP (Model Context Protocol) servers using Azure Functions with Python, C# .NET or Node/TypeScript.

Dis Samples dey provide complete solution wey allow developers to:

- Build and run locally: Develop and debug MCP server on local machine
- Deploy to Azure: Simple deploy to cloud with one azd up command
- Connect from clients: Connect MCP server from different clients including VS Code's Copilot agent mode and MCP Inspector tool

### Key Features

- Security by design: MCP server dey secure with keys and HTTPS
- Authentication options: Support OAuth with built-in auth and/or API Management
- Network isolation: Let you isolate net using Azure Virtual Networks (VNET)
- Serverless architecture: Use Azure Functions for scalable event-driven execution
- Local development: Complet local dev and debug support
- Simple deployment: Easy deploy process to Azure

Dis repo get all configuration files, source code, and infrastructure definitions to help you quickly start MCP server production-ready implementation.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Sample MCP implementation using Azure Functions with Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Sample MCP implementation using Azure Functions with C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Sample MCP implementation using Azure Functions with Node/TypeScript.

## Key Takeaways

- MCP SDKs dey provide language-specific tools for building strong MCP solutions
- Debug and test process important well well for reliable MCP apps
- Reusable prompt templates fit give consistent AI interaction
- Well designed workflows fit organize complex tasks wey get many tools
- To implement MCP solutions, you must reason security, performance, plus error handling

## Exercise

Design one practical MCP workflow wey go solve real-world problem for your own area:

1. Find 3-4 tools wey go help solve dis matter
2. Draw workflow diagram wey show how these tools dey interact
3. Make simple version of one of di tools using your language wey you like
4. Create prompt template wey go help model use your tool well

## Additional Resources

---

## What's Next

Next: [Advanced Topics](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document na so AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make am correct, abeg sabi say automated translation fit get mistakes or no too clear. The original document wey dem write for im own language na the correct one. If matter serious, e better make human professional translate am. We no go carry any blame if pesin miss understand or no catch the correct meaning because of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->