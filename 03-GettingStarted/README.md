## Getting Started  

Welcome to the hands-on section of MCP for Beginners! This chapter will guide you through setting up your environment, building your first MCP server, connecting clients, and testing your implementation. Each lesson includes practical exercises and sample code in C#, Java, Python, TypeScript, and JavaScript.

- **-1- Building your first MCP Server**. Learn how to create a basic MCP server in your preferred language. [Go to the lesson](/03-GettingStarted/01-first-server/README.md)
- **-2- Creating a client**. Discover how to connect to an MCP server and invoke its features. [Go to the lesson](/03-GettingStarted/02-client/README.md)
- **-3- Creating a client with an LLM**. See how to connect an LLM client to an MCP server. [Go to the lesson](/03-GettingStarted/03-llm-client/README.md)
- **-4- Consuming a server in GitHub Copilot Agent mode in Visual Studio Code**. Learn how to run your MCP server from within Visual Studio Code. [Go to the lesson](/03-GettingStarted/04-vscode/README.md)
- **-5- Consuming from SSE (Server-Sent Events)**. SSE is a standard for server-to-client streaming, allowing servers to push real-time updates to clients over HTTP. [Go to the lesson](/03-GettingStarted/05-sse-server/README.md)
- **-6- Utilising AI Toolkit for VSCode** to consume and test your MCP clients and servers. [Go to the lesson](/03-GettingStarted/06-aitk/README.md)
- **-7- Testing**. Focus on how to test your server and client in different ways. [Go to the lesson](/03-GettingStarted/07-testing/README.md)
- **-8- Deployment**. Learn how to deploy your MCP server to production environments. [Go to the lesson](/03-GettingStarted/08-deployment/README.md)

The Model Context Protocol (MCP) is an open protocol that standardises how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications - it provides a standardised way to connect AI models to different data sources and tools.

## Learning Objectives

By the end of this lesson, you will be able to:

- Set up development environments for MCP in C#, Java, Python, TypeScript, and JavaScript.
- Build and deploy basic MCP servers with custom features (resources, prompts, and tools).
- Create host applications that connect to MCP servers.
- Test and debug MCP implementations.
- Understand common setup challenges and their solutions.
- Connect your MCP implementations to popular LLM services.

## Setting Up Your MCP Environment

Before you begin working with MCP, it's important to prepare your development environment and understand the basic workflow. This section will guide you through the initial setup steps to ensure a smooth start with MCP.

### Prerequisites

Before diving into MCP development, ensure you have:

- **Development Environment**: For your chosen language (C#, Java, Python, TypeScript, or JavaScript).
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, or any modern code editor.
- **Package Managers**: NuGet, Maven/Gradle, pip, or npm/yarn.
- **API Keys**: For any AI services you plan to use in your host applications.

### Official SDKs

In the upcoming chapters, you will see solutions built using Python, TypeScript, Java and .NET. Here are all the officially supported SDKs.

MCP provides official SDKs for multiple languages:
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Maintained in collaboration with Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Maintained in collaboration with Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - The official TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - The official Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - The official Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Maintained in collaboration with Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - The official Rust implementation

## Key Takeaways

- Setting up an MCP development environment is straightforward with language-specific SDKs.
- Building MCP servers involves creating and registering tools with clear schemas.
- MCP clients connect to servers and models to leverage extended capabilities.
- Testing and debugging are essential for reliable MCP implementations.
- Deployment options range from local development to cloud-based solutions.

## Practicing

We have a set of samples that complement the exercises you will see in all chapters in this section. Additionally, each chapter also has its own exercises and assignments.

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](./samples/csharp/)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](./samples/python/)

## Additional Resources

- [MCP GitHub Repository](https://github.com/microsoft/mcp-for-beginners)

## What's next

Next: [Creating your first MCP Server](/03-GettingStarted/01-first-server/README.md)
