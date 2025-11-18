<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f400d87053221363769113c24f117248",
  "translation_date": "2025-11-18T18:54:49+00:00",
  "source_file": "03-GettingStarted/README.md",
  "language_code": "pcm"
}
-->
## How to Start  

[![Build Your First MCP Server](../../../translated_images/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.pcm.png)](https://youtu.be/sNDZO9N4m9Y)

_(Click di image wey dey up to watch di video for dis lesson)_

Dis section get plenty lessons:

- **1 Your first server**, for dis first lesson, you go learn how to build your first server and use di inspector tool check am, e dey useful for test and debug your server, [go di lesson](01-first-server/README.md)

- **2 Client**, for dis lesson, you go learn how to write client wey fit connect to your server, [go di lesson](02-client/README.md)

- **3 Client with LLM**, di better way to write client na to add LLM so e fit "discuss" with your server on wetin to do, [go di lesson](03-llm-client/README.md)

- **4 How to use server GitHub Copilot Agent mode for Visual Studio Code**. For here, we go look how to run MCP Server from inside Visual Studio Code, [go di lesson](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport na di standard way wey dem recommend for MCP server-to-client communication for di current specification, e dey provide secure subprocess-based communication [go di lesson](05-stdio-server/README.md)

- **6 HTTP Streaming with MCP (Streamable HTTP)**. Learn about di modern HTTP streaming, progress notifications, and how to use Streamable HTTP build scalable, real-time MCP servers and clients. [go di lesson](06-http-streaming/README.md)

- **7 How to use AI Toolkit for VSCode** to test and use your MCP Clients and Servers [go di lesson](07-aitk/README.md)

- **8 Testing**. For here, we go focus on how we fit test our server and client in different ways, [go di lesson](08-testing/README.md)

- **9 Deployment**. Dis chapter go show different ways to deploy your MCP solutions, [go di lesson](09-deployment/README.md)

- **10 Advanced server usage**. Dis chapter dey talk about advanced server usage, [go di lesson](./10-advanced/README.md)

- **11 Auth**. Dis chapter dey show how to add simple auth, from Basic Auth to using JWT and RBAC. Dem dey encourage you make you start here and then check Advanced Topics for Chapter 5 and do extra security hardening with di recommendations for Chapter 2, [go di lesson](./11-simple-auth/README.md)

Di Model Context Protocol (MCP) na open protocol wey dey standardize how applications dey provide context to LLMs. Think of MCP like USB-C port for AI applications - e dey provide standard way to connect AI models to different data sources and tools.

## Wetin You Go Learn

By di end of dis lesson, you go fit:

- Set up development environments for MCP for C#, Java, Python, TypeScript, and JavaScript
- Build and deploy basic MCP servers with custom features (resources, prompts, and tools)
- Create host applications wey dey connect to MCP servers
- Test and debug MCP implementations
- Understand common setup challenges and di solutions
- Connect your MCP implementations to popular LLM services

## How to Set Up Your MCP Environment

Before you start work with MCP, e important make you prepare your development environment and understand di basic workflow. Dis section go guide you through di first setup steps to make sure say you start MCP well.

### Wetin You Need

Before you start MCP development, make sure say you get:

- **Development Environment**: For di language wey you choose (C#, Java, Python, TypeScript, or JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, or any modern code editor
- **Package Managers**: NuGet, Maven/Gradle, pip, or npm/yarn
- **API Keys**: For any AI services wey you wan use for your host applications

### Official SDKs

For di chapters wey dey come, you go see solutions wey dem build with Python, TypeScript, Java and .NET. Here be di officially supported SDKs.

MCP dey provide official SDKs for plenty languages:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Dem dey maintain am with Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Dem dey maintain am with Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Di official TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Di official Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Di official Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Dem dey maintain am with Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Di official Rust implementation

## Wetin You Go Remember

- To set up MCP development environment dey easy with language-specific SDKs
- To build MCP servers, you go need create and register tools with clear schemas
- MCP clients dey connect to servers and models to use extra features
- Testing and debugging dey important for MCP implementations wey go work well
- Deployment options dey range from local development to cloud-based solutions

## Practice

We get samples wey dey follow di exercises wey you go see for all di chapters for dis section. Plus, each chapter get their own exercises and assignments.

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## Extra Resources

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Wetin Go Happen Next

Next: [How to Create Your First MCP Server](01-first-server/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->