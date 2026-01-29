# 🚀 10 Microsoft MCP Servers That Are Transforming Developer Productivity

## 🎯 What You'll Learn in This Guide

This practical guide highlights ten Microsoft MCP servers that are actively changing how developers work with AI assistants. Instead of just describing what MCP servers *can* do, we’ll show you servers that are already making a real impact on daily development workflows at Microsoft and beyond.

Each server featured here is chosen based on real-world use and developer feedback. You’ll learn not only what each server does, but why it matters and how to get the most out of it in your own projects. Whether you’re new to MCP or looking to expand your current setup, these servers represent some of the most practical and powerful tools in the Microsoft ecosystem.

> **💡 Quick Start Tip**
> 
> New to MCP? No worries! This guide is beginner-friendly. We’ll explain concepts as we go, and you can always revisit our [Introduction to MCP](../00-Introduction/README.md) and [Core Concepts](../01-CoreConcepts/README.md) modules for more background.

## Overview

This comprehensive guide explores ten Microsoft MCP servers that are revolutionizing how developers interact with AI assistants and external tools. From managing Azure resources to processing documents, these servers showcase the power of the Model Context Protocol in creating smooth, productive development workflows.

## Learning Objectives

By the end of this guide, you will:
- Understand how MCP servers boost developer productivity
- Learn about Microsoft’s most impactful MCP server implementations
- Discover practical use cases for each server
- Know how to set up and configure these servers in VS Code and Visual Studio
- Explore the broader MCP ecosystem and future directions

## 🔧 Understanding MCP Servers: A Beginner's Guide

### What Are MCP Servers?

If you’re new to the Model Context Protocol (MCP), you might ask: “What exactly is an MCP server, and why should I care?” Let’s start with a simple analogy.

Think of MCP servers as specialized helpers that enable your AI coding companion (like GitHub Copilot) to connect with external tools and services. Just like you use different apps on your phone for different tasks—weather, navigation, banking—MCP servers let your AI assistant interact with various development tools and services.

### The Problem MCP Servers Solve

Before MCP servers, if you wanted to:
- Check your Azure resources
- Create a GitHub issue
- Query your database
- Search through documentation

You’d have to stop coding, open a browser, go to the right website, and do these tasks manually. This constant switching breaks your flow and lowers productivity.

### How MCP Servers Transform Your Development Experience

With MCP servers, you can stay inside your development environment (VS Code, Visual Studio, etc.) and simply ask your AI assistant to handle these tasks. For example:

**Instead of this traditional workflow:**
1. Stop coding  
2. Open browser  
3. Navigate to Azure portal  
4. Look up storage account details  
5. Return to VS Code  
6. Resume coding  

**You can now do this:**
1. Ask AI: “What’s the status of my Azure storage accounts?”  
2. Keep coding with the info provided  

### Key Benefits for Beginners

#### 1. 🔄 **Stay in Your Flow State**
- No more switching between multiple apps  
- Keep your focus on the code you’re writing  
- Reduce mental overhead from juggling different tools  

#### 2. 🤖 **Use Natural Language Instead of Complex Commands**
- Instead of memorizing SQL syntax, just describe the data you need  
- Instead of recalling Azure CLI commands, explain what you want to do  
- Let AI handle the technical details while you focus on logic  

#### 3. 🔗 **Connect Multiple Tools Together**
- Build powerful workflows by combining different services  
- Example: “Get all recent GitHub issues and create matching Azure DevOps work items”  
- Automate tasks without writing complex scripts  

#### 4. 🌐 **Access a Growing Ecosystem**
- Benefit from servers built by Microsoft, GitHub, and others  
- Mix and match tools from different vendors seamlessly  
- Join a standardized ecosystem that works across various AI assistants  

#### 5. 🛠️ **Learn by Doing**
- Start with pre-built servers to grasp the concepts  
- Gradually build your own servers as you gain confidence  
- Use available SDKs and documentation to guide your learning  

### Real-World Example for Beginners

Imagine you’re new to web development and working on your first project. Here’s how MCP servers can help:

**Traditional approach:**  
```
1. Code a feature
2. Open browser → Navigate to GitHub
3. Create an issue for testing
4. Open another tab → Check Azure docs for deployment
5. Open third tab → Look up database connection examples
6. Return to VS Code
7. Try to remember what you were doing
```

**With MCP servers:**  
```
1. Code a feature
2. Ask AI: "Create a GitHub issue for testing this login feature"
3. Ask AI: "How do I deploy this to Azure according to the docs?"
4. Ask AI: "Show me the best way to connect to my database"
5. Continue coding with all the information you need
```

### The Enterprise Standard Advantage

MCP is becoming an industry-wide standard, which means:
- **Consistency**: Similar experience across different tools and companies  
- **Interoperability**: Servers from different vendors work together  
- **Future-proofing**: Skills and setups transfer between different AI assistants  
- **Community**: Large ecosystem of shared knowledge and resources  

### Getting Started: What You'll Learn

In this guide, we’ll explore 10 Microsoft MCP servers that are especially useful for developers at all levels. Each server is designed to:
- Solve common development challenges  
- Cut down repetitive tasks  
- Improve code quality  
- Enhance learning opportunities  

> **💡 Learning Tip**
> 
> If you’re brand new to MCP, start with our [Introduction to MCP](../00-Introduction/README.md) and [Core Concepts](../01-CoreConcepts/README.md) modules first. Then come back here to see these ideas in action with real Microsoft tools.  
>
> For more on why MCP matters, check out Maria Naggaga’s post: [Connect Once, Integrate Anywhere with MCP](https://devblogs.microsoft.com/blog/connect-once-integrate-anywhere-with-mcps).

## Getting Started with MCP in VS Code and Visual Studio 🚀

Setting up these MCP servers is easy if you’re using Visual Studio Code or Visual Studio 2022 with GitHub Copilot.

### VS Code Setup

Here’s the basic process for VS Code:

1. **Enable Agent Mode**: In VS Code, switch to Agent mode in the Copilot Chat window  
2. **Configure MCP Servers**: Add server configurations to your VS Code settings.json file  
3. **Start Servers**: Click “Start” for each server you want to use  
4. **Select Tools**: Choose which MCP servers to enable for your current session  

For detailed setup instructions, see the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp).

> **💡 Pro Tip: Manage MCP Servers like a pro!**
> 
> The VS Code Extensions view now includes a [handy new UI to manage installed MCP Servers](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_use-mcp-tools-in-agent-mode)! You can quickly start, stop, and manage any installed MCP Servers with a clear, simple interface. Give it a try!

### Visual Studio 2022 Setup

For Visual Studio 2022 (version 17.14 or later):

1. **Enable Agent Mode**: Click the “Ask” dropdown in the GitHub Copilot Chat window and select “Agent”  
2. **Create Configuration File**: Create a `.mcp.json` file in your solution directory (recommended location: `<SOLUTIONDIR>\.mcp.json`)  
3. **Configure Servers**: Add your MCP server configurations using the standard MCP format  
4. **Tool Approval**: When prompted, approve the tools you want to use with the right scope permissions  

For detailed Visual Studio setup instructions, see the [Visual Studio MCP documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers).

Each MCP server has its own configuration needs (connection strings, authentication, etc.), but the setup process is consistent across both IDEs.

## Lesson Learned from Microsoft MCP Servers 🛠️

### 1. 📚 Microsoft Learn Docs MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Microsoft_Docs_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Microsoft_Docs_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=microsoft.docs.mcp&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Flearn.microsoft.com%2Fapi%2Fmcp%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**What it does**: The Microsoft Learn Docs MCP Server is a cloud-hosted service that gives AI assistants real-time access to official Microsoft documentation through the Model Context Protocol. It connects to `https://learn.microsoft.com/api/mcp` and enables semantic search across Microsoft Learn, Azure docs, Microsoft 365 docs, and other official Microsoft sources.

**Why it’s useful**: While it might seem like “just documentation,” this server is actually essential for every developer working with Microsoft technologies. One of the biggest complaints from .NET developers about AI coding assistants is that they’re not up to date on the latest .NET and C# releases. The Microsoft Learn Docs MCP Server fixes this by providing real-time access to the most current documentation, API references, and best practices. Whether you’re using the latest Azure SDKs, exploring new C# 13 features, or implementing cutting-edge .NET Aspire patterns, this server ensures your AI assistant has access to authoritative, up-to-date info to generate accurate, modern code.

**Real-world use**: “What are the az cli commands to create an Azure container app according to official Microsoft Learn documentation?” or “How do I configure Entity Framework with dependency injection in ASP.NET Core?” Or “Review this code to make sure it follows the performance recommendations in the Microsoft Learn Documentation.” The server covers Microsoft Learn, Azure docs, and Microsoft 365 docs using advanced semantic search to find the most relevant info. It returns up to 10 high-quality content chunks with article titles and URLs, always pulling from the latest Microsoft documentation as it’s published.

**Featured example**: The server offers the `microsoft_docs_search` tool that performs semantic search against Microsoft’s official technical documentation. Once set up, you can ask questions like “How do I implement JWT authentication in ASP.NET Core?” and get detailed, official answers with source links. The search quality is excellent because it understands context—asking about “containers” in an Azure context returns Azure Container Instances docs, while the same term in a .NET context returns relevant C# collection info.

This is especially helpful for rapidly changing or recently updated libraries and scenarios. For example, in recent projects I wanted to use features from the latest .NET Aspire and Microsoft.Extensions.AI releases. By including the Microsoft Learn Docs MCP server, I could leverage not just API docs but also walkthroughs and guidance that had just been published.
> **💡 Pro Tip**
> 
> Even tool-friendly models need encouragement to use MCP tools! Consider adding a system prompt or [copilot-instructions.md](https://docs.github.com/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) like: "You have access to `microsoft.docs.mcp` – use this tool to search Microsoft's latest official documentation when handling questions about Microsoft technologies like C#, Azure, ASP.NET Core, or Entity Framework."
>
> For a great example of this in action, check out the [C# .NET Janitor chat mode](https://github.com/awesome-copilot/chatmodes/blob/main/csharp-dotnet-janitor.chatmode.md) from the Awesome GitHub Copilot repository. This mode specifically leverages the Microsoft Learn Docs MCP server to help clean up and modernize C# code using the latest patterns and best practices.
### 2. ☁️ Azure MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fazure-mcp%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**What it does**: The Azure MCP Server is a comprehensive suite of over 15 specialized Azure service connectors that bring the entire Azure ecosystem into your AI workflow. It’s not just a single server – it’s a powerful collection that includes resource management, database connectivity (PostgreSQL, SQL Server), Azure Monitor log analysis with KQL, Cosmos DB integration, and much more.

**Why it’s useful**: Beyond managing Azure resources, this server significantly improves code quality when working with Azure SDKs. When you use Azure MCP in Agent mode, it doesn’t just help you write code – it helps you write *better* Azure code that follows current authentication patterns, best practices for error handling, and leverages the latest SDK features. Instead of generic code that might work, you get code that follows Azure’s recommended patterns for production workloads.

**Key modules include**:
- **🗄️ Database Connectors**: Natural language access to Azure Database for PostgreSQL and SQL Server
- **📊 Azure Monitor**: KQL-powered log analysis and operational insights
- **🌐 Resource Management**: Full Azure resource lifecycle management
- **🔐 Authentication**: DefaultAzureCredential and managed identity patterns
- **📦 Storage Services**: Blob Storage, Queue Storage, and Table Storage operations
- **🚀 Container Services**: Azure Container Apps, Container Instances, and AKS management
- **And many more specialized connectors**

**Real-world use**: "List my Azure storage accounts", "Query my Log Analytics workspace for errors in the last hour", or "Help me build an Azure application using Node.js with proper authentication"

**Full demo scenario**: Here’s a complete walkthrough showing the power of combining Azure MCP with the GitHub Copilot for Azure extension in VS Code. When you have both installed and prompt:

> "Create a Python script that uploads a file to Azure Blob Storage using DefaultAzureCredential authentication. The script should connect to my Azure storage account named 'mycompanystorage', upload to a container named 'documents', create a test file with the current timestamp to upload, handle errors gracefully and provide informative output, follow Azure best practices for authentication and error handling, include comments explaining how the DefaultAzureCredential authentication works, and make the script well-structured with proper functions and documentation."

The Azure MCP Server will generate a complete, production-ready Python script that:
- Uses the latest Azure Blob Storage SDK with proper async patterns
- Implements DefaultAzureCredential with a detailed fallback chain explanation
- Includes robust error handling with specific Azure exception types
- Follows Azure SDK best practices for resource management and connection handling
- Provides detailed logging and informative console output
- Creates a well-structured script with functions, documentation, and type hints

What makes this remarkable is that without Azure MCP, you might get generic blob storage code that works but doesn’t follow current Azure patterns. With Azure MCP, you get code that uses the latest authentication methods, handles Azure-specific error scenarios, and follows Microsoft’s recommended practices for production applications.

**Featured example**: I’ve struggled to remember the specific commands for the `az` and `azd` CLIs for ad-hoc use. It’s always a two-step process for me: first look up the syntax, then run the command. I often just jump into the portal and click around because I don’t want to admit I can’t remember CLI syntax. Being able to just describe what I want is amazing, and even better to do that without leaving my IDE!

There’s a great list of use cases in the [Azure MCP repository](https://github.com/Azure/azure-mcp?tab=readme-ov-file#-what-can-you-do-with-the-azure-mcp-server) to get you started. For detailed setup guides and advanced configuration options, check out the [official Azure MCP documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/).

### 3. 🐙 GitHub MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/github/github-mcp-server)

**What it does**: The official GitHub MCP Server offers seamless integration with GitHub’s entire ecosystem, providing both hosted remote access and local Docker deployment options. It’s not just about basic repository operations – it’s a comprehensive toolkit including GitHub Actions management, pull request workflows, issue tracking, security scanning, notifications, and advanced automation features.

**Why it’s useful**: This server changes how you interact with GitHub by bringing the full platform experience directly into your development environment. Instead of constantly switching between VS Code and GitHub.com for project management, code reviews, and CI/CD monitoring, you can handle everything through natural language commands while staying focused on your code.

> **ℹ️ Note: Different Types of 'Agents'**
> 
> Don’t confuse this GitHub MCP Server with GitHub’s Coding Agent (the AI agent you can assign issues to for automated coding tasks). The GitHub MCP Server works within VS Code’s Agent mode to provide GitHub API integration, while GitHub’s Coding Agent is a separate feature that creates pull requests when assigned to GitHub issues.

**Key capabilities include**:
- **⚙️ GitHub Actions**: Full CI/CD pipeline management, workflow monitoring, and artifact handling
- **🔀 Pull Requests**: Create, review, merge, and manage PRs with detailed status tracking
- **🐛 Issues**: Complete issue lifecycle management, commenting, labeling, and assignment
- **🔒 Security**: Code scanning alerts, secret detection, and Dependabot integration
- **🔔 Notifications**: Smart notification management and repository subscription control
- **📁 Repository Management**: File operations, branch management, and repository administration
- **👥 Collaboration**: User and organization search, team management, and access control

**Real-world use**: "Create a pull request from my feature branch", "Show me all failed CI runs this week", "List open security alerts for my repositories", or "Find all issues assigned to me across my organizations"

**Full demo scenario**: Here’s a powerful workflow demonstrating the GitHub MCP Server’s capabilities:

> "I need to prepare for our sprint review. Show me all pull requests I’ve created this week, check the status of our CI/CD pipelines, create a summary of any security alerts we need to address, and help me draft release notes based on merged PRs with the 'feature' label."

The GitHub MCP Server will:
- Query your recent pull requests with detailed status information
- Analyze workflow runs and highlight any failures or performance issues
- Compile security scanning results and prioritize critical alerts
- Generate comprehensive release notes by extracting info from merged PRs
- Provide actionable next steps for sprint planning and release preparation

**Featured example**: I love using this for code review workflows. Instead of jumping between VS Code, GitHub notifications, and pull request pages, I can say "Show me all PRs waiting for my review" and then "Add a comment to PR #123 asking about the error handling in the authentication method." The server handles the GitHub API calls, keeps context about the discussion, and even helps me craft more constructive review comments.

**Authentication options**: The server supports both OAuth (seamless in VS Code) and Personal Access Tokens, with configurable toolsets to enable only the GitHub features you need. You can run it as a remote hosted service for instant setup or locally via Docker for full control.

> **💡 Pro Tip**
> 
> Enable only the toolsets you need by configuring the `--toolsets` parameter in your MCP server settings to reduce context size and improve AI tool selection. For example, add `"--toolsets", "repos,issues,pull_requests,actions"` to your MCP configuration args for core development workflows, or use `"--toolsets", "notifications, security"` if you mainly want GitHub monitoring features.

### 4. 🔄 Azure DevOps MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_DevOps_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_DevOps_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20DevOps%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-azure-devops%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/azure-devops-mcp)

**What it does**: Connects to Azure DevOps services for full project management, work item tracking, build pipeline management, and repository operations.

**Why it’s useful**: For teams using Azure DevOps as their main DevOps platform, this MCP server removes the need to constantly switch between your development environment and the Azure DevOps web interface. You can manage work items, check build statuses, query repositories, and handle project management tasks directly from your AI assistant.

**Real-world use**: "Show me all active work items in the current sprint for the WebApp project", "Create a bug report for the login issue I just found", or "Check the status of our build pipelines and show me any recent failures"

**Featured example**: You can easily check your team’s current sprint status with a simple query like "Show me all active work items in the current sprint for the WebApp project" or "Create a bug report for the login issue I just found" without leaving your development environment.

### 5. 📝 MarkItDown MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_MarkItDown_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_MarkItDown_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=MarkItDown%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-markitdown%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/markitdown)

**What it does**: MarkItDown is a powerful document conversion server that transforms a wide variety of file formats into high-quality Markdown, optimized for LLM consumption and text analysis workflows.

**Why it's useful**: Essential for modern documentation workflows! MarkItDown supports an impressive range of file formats while preserving important document structures like headings, lists, tables, and links. Unlike simple text extraction tools, it focuses on maintaining semantic meaning and formatting that benefits both AI processing and human readability.

**Supported file formats**:
- **Office Documents**: PDF, PowerPoint (PPTX), Word (DOCX), Excel (XLSX/XLS)
- **Media Files**: Images (with EXIF metadata and OCR), Audio (with EXIF metadata and speech transcription)
- **Web Content**: HTML, RSS feeds, YouTube URLs, Wikipedia pages
- **Data Formats**: CSV, JSON, XML, ZIP files (processes contents recursively)
- **Publishing Formats**: EPub, Jupyter notebooks (.ipynb)
- **Email**: Outlook messages (.msg)
- **Advanced**: Azure Document Intelligence integration for enhanced PDF processing

**Advanced capabilities**: MarkItDown supports LLM-powered image descriptions (when used with an OpenAI client), Azure Document Intelligence for enhanced PDF processing, audio transcription for speech content, and a plugin system to extend support for additional file formats.

**Real-world use**: "Convert this PowerPoint presentation to Markdown for our documentation site," "Extract text from this PDF with proper heading structure," or "Transform this Excel spreadsheet into a readable table format."

**Featured example**: To quote the [MarkItDown docs](https://github.com/microsoft/markitdown#why-markdown):

> Markdown is very close to plain text, with minimal markup or formatting, yet it still provides a way to represent important document structure. Mainstream LLMs, like OpenAI's GPT-4o, natively "speak" Markdown and often include Markdown in their responses without prompting. This suggests they have been trained on vast amounts of Markdown-formatted text and understand it well. As a bonus, Markdown conventions are also very token-efficient.

MarkItDown excels at preserving document structure, which is crucial for AI workflows. For example, when converting a PowerPoint presentation, it maintains slide organization with appropriate headings, extracts tables as Markdown tables, includes alt text for images, and even processes speaker notes. Charts are converted into readable data tables, and the resulting Markdown keeps the logical flow of the original presentation. This makes it ideal for feeding presentation content into AI systems or creating documentation from existing slides.

### 6. 🗃️ SQL Server MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_SQL_Database-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_SQL_Database-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20SQL%20Database&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40azure%2Fmcp%40latest%22%2C%22server%22%2C%22start%22%2C%22--namespace%22%2C%22sql%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Azure/azure-mcp)

**What it does**: Provides conversational access to SQL Server databases (on-premises, Azure SQL, or Fabric)

**Why it's useful**: Similar to the PostgreSQL server but designed for the Microsoft SQL ecosystem. Connect with a simple connection string and start querying using natural language – no more switching contexts!

**Real-world use**: "Find all orders that haven't been fulfilled in the last 30 days" gets translated into the appropriate SQL queries and returns formatted results.

**Featured example**: Once your database connection is set up, you can start interacting with your data right away. The blog post demonstrates this with a simple question: "Which database are you connected to?" The MCP server responds by invoking the right database tool, connecting to your SQL Server instance, and returning details about your current database connection – all without writing a single line of SQL. The server supports full database operations from schema management to data manipulation, all through natural language prompts. For complete setup instructions and configuration examples with VS Code and Claude Desktop, see: [Introducing MSSQL MCP Server (Preview)](https://devblogs.microsoft.com/azure-sql/introducing-mssql-mcp-server/).

### 7. 🎭 Playwright MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Playwright_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Playwright_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Playwright%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-playwright%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/playwright-mcp)

**What it does**: Allows AI agents to interact with web pages for testing and automation

> **ℹ️ Powering GitHub Copilot**
> 
> The Playwright MCP Server powers GitHub Copilot's Coding Agent, giving it web browsing capabilities! [Learn more about this feature](https://github.blog/changelog/2025-07-02-copilot-coding-agent-now-has-its-own-web-browser/).

**Why it's useful**: Ideal for automated testing driven by natural language descriptions. AI can navigate websites, fill out forms, and extract data through structured accessibility snapshots – this is incredibly powerful!

**Real-world use**: "Test the login flow and verify that the dashboard loads correctly" or "Generate a test that searches for products and validates the results page" – all without needing access to the application's source code.

**Featured example**: My teammate Debbie O'Brien has been doing amazing work with the Playwright MCP Server recently! For example, she demonstrated how you can generate complete Playwright tests without even having access to the application's source code. In her example, she asked Copilot to create a test for a movie search app: navigate to the site, search for "Garfield," and verify the movie appears in the results. The MCP launched a browser session, explored the page structure using DOM snapshots, identified the correct selectors, and generated a fully working TypeScript test that passed on the first run.

What makes this so powerful is that it bridges the gap between natural language instructions and executable test code. Traditional methods require either manual test writing or access to the codebase for context. But with Playwright MCP, you can test external sites, client applications, or perform black-box testing where code access isn’t available.

### 8. 💻 Dev Box MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Dev_Box_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Dev_Box_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Dev%20Box%20MCP&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22%40microsoft%2Fmcp-devbox%40latest%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/microsoft/mcp)

**What it does**: Manages Microsoft Dev Box environments using natural language

**Why it's useful**: Greatly simplifies managing development environments! Create, configure, and manage Dev Boxes without needing to remember specific commands.

**Real-world use**: "Set up a new Dev Box with the latest .NET SDK and configure it for our project," "Check the status of all my development environments," or "Create a standardized demo environment for our team presentations."

**Featured example**: I’m a big fan of using Dev Box for personal development. My lightbulb moment came when James Montemagno explained how great Dev Box is for conference demos, since it offers a super-fast ethernet connection regardless of the conference, hotel, or airplane Wi-Fi I might be using. In fact, I recently practiced a conference demo while my laptop was tethered to my phone hotspot on a bus from Bruges to Antwerp! My next step is to explore managing multiple development environments for teams and standardized demo environments. Another popular use case I’ve heard from customers and coworkers is using Dev Box for preconfigured development environments. In both cases, using an MCP to configure and manage Dev Boxes lets you interact via natural language, all while staying within your development environment.

### 9. 🤖 Azure AI Foundry MCP Server
[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Azure_AI_Foundry_MCP-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Azure_AI_Foundry_MCP-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Azure%20Foundry%20MCP%20Server&config=%7B%22type%22%3A%22stdio%22%2C%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22--prerelease%3Dallow%22%2C%22--from%22%2C%22git%2Bhttps%3A%2F%2Fgithub.com%2Fazure-ai-foundry%2Fmcp-foundry.git%22%2C%22run-azure-ai-foundry-mcp%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/azure-ai-foundry/mcp-foundry)

**What it does**: The Azure AI Foundry MCP Server gives developers full access to Azure’s AI ecosystem, including model catalogs, deployment management, knowledge indexing with Azure AI Search, and evaluation tools. This experimental server bridges AI development with Azure’s powerful AI infrastructure, making it easier to build, deploy, and assess AI applications.

**Why it's useful**: This server changes how you work with Azure AI services by integrating enterprise-grade AI capabilities directly into your development workflow. Instead of toggling between the Azure portal, documentation, and your IDE, you can discover models, deploy services, manage knowledge bases, and evaluate AI performance using natural language commands. It’s especially valuable for developers building RAG (Retrieval-Augmented Generation) applications, managing multi-model deployments, or setting up comprehensive AI evaluation pipelines.

**Key developer capabilities**:
- **🔍 Model Discovery & Deployment**: Browse Azure AI Foundry’s model catalog, access detailed model info with code samples, and deploy models to Azure AI Services
- **📚 Knowledge Management**: Create and manage Azure AI Search indexes, add documents, configure indexers, and build advanced RAG systems
- **⚡ AI Agent Integration**: Connect with Azure AI Agents, query existing agents, and evaluate agent performance in real-world scenarios
- **📊 Evaluation Framework**: Run thorough text and agent evaluations, generate markdown reports, and implement quality assurance for AI applications
- **🚀 Prototyping Tools**: Get setup instructions for GitHub-based prototyping and access Azure AI Foundry Labs for cutting-edge research models

**Real-world developer use**: “Deploy a Phi-4 model to Azure AI Services for my app,” “Create a new search index for my documentation RAG system,” “Evaluate my agent’s responses against quality metrics,” or “Find the best reasoning model for my complex analysis tasks.”

**Full demo scenario**: Here’s a powerful AI development workflow:

> “I’m building a customer support agent. Help me find a good reasoning model from the catalog, deploy it to Azure AI Services, create a knowledge base from our documentation, set up an evaluation framework to test response quality, and then help me prototype the integration with GitHub token for testing.”

The Azure AI Foundry MCP Server will:
- Query the model catalog to recommend the best reasoning models based on your needs
- Provide deployment commands and quota details for your preferred Azure region
- Set up Azure AI Search indexes with the right schema for your documentation
- Configure evaluation pipelines with quality metrics and safety checks
- Generate prototyping code with GitHub authentication for immediate testing
- Offer detailed setup guides tailored to your technology stack

**Featured example**: As a developer, I’ve struggled to keep up with the many LLM models available. I know a few main ones but felt like I was missing out on productivity and efficiency gains. Managing tokens and quotas is stressful and tricky—I never know if I’m choosing the right model for the task or wasting my budget. I recently heard about this MCP Server from James Montemagno while discussing MCP Server recommendations with teammates, and I’m excited to try it out! The model discovery features look especially useful for someone like me who wants to explore beyond the usual options and find models optimized for specific tasks. The evaluation framework should help me confirm that I’m actually improving results, not just experimenting for the sake of it.

> **ℹ️ Experimental Status**
> 
> This MCP server is experimental and actively being developed. Features and APIs may change. It’s perfect for exploring Azure AI capabilities and building prototypes, but make sure to verify stability before using it in production.

### 10. 🏢 Microsoft 365 Agents Toolkit MCP Server

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_M365_Agents_Toolkit-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D) [![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_M365_Agents_Toolkit-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=M365AgentsToolkit%20Server&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22@microsoft%2Fm365agentstoolkit-mcp%40latest%22%2C%22server%22%2C%22start%22%5D%7D&quality=insiders) [![GitHub](https://img.shields.io/badge/GitHub-View_Repository-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/OfficeDev/microsoft-365-agents-toolkit)

**What it does**: Provides developers with essential tools for building AI agents and applications that integrate with Microsoft 365 and Microsoft 365 Copilot, including schema validation, sample code retrieval, and troubleshooting help.

**Why it's useful**: Developing for Microsoft 365 and Copilot involves complex manifest schemas and specific development patterns. This MCP server brings key development resources right into your coding environment, helping you validate schemas, find sample code, and troubleshoot common issues without constantly referring to documentation.

**Real-world use**: “Validate my declarative agent manifest and fix any schema errors,” “Show me sample code for implementing a Microsoft Graph API plugin,” or “Help me troubleshoot my Teams app authentication issues.”

**Featured example**: I reached out to my friend John Miller after talking with him at Build about M365 Agents, and he recommended this MCP. It’s great for developers new to M365 Agents since it provides templates, sample code, and scaffolding to get started without drowning in documentation. The schema validation features look especially helpful for avoiding manifest structure errors that can cause hours of debugging.

> **💡 Pro Tip**
> 
> Use this server alongside the Microsoft Learn Docs MCP Server for full M365 development support—one offers official documentation while this one provides practical development tools and troubleshooting help.

## What's Next? 🔮

## 📋 Conclusion

The Model Context Protocol (MCP) is changing how developers interact with AI assistants and external tools. These 10 Microsoft MCP servers showcase the power of standardized AI integration, enabling smooth workflows that keep developers focused while accessing powerful external capabilities.

From deep Azure ecosystem integration to specialized tools like Playwright for browser automation and MarkItDown for document processing, these servers demonstrate how MCP can boost productivity across various development scenarios. The standardized protocol ensures these tools work together seamlessly, creating a unified development experience.

As the MCP ecosystem grows, staying involved with the community, exploring new servers, and building custom solutions will be key to maximizing your productivity. The open standard nature of MCP lets you mix and match tools from different vendors to create the perfect workflow for your needs.

## 🔗 Additional Resources

- [Official Microsoft MCP Repository](https://github.com/microsoft/mcp)
- [MCP Community & Documentation](https://modelcontextprotocol.io/introduction)
- [VS Code MCP Documentation](https://code.visualstudio.com/docs/copilot/copilot-mcp)
- [Visual Studio MCP Documentation](https://learn.microsoft.com/visualstudio/ide/mcp-servers)
- [Azure MCP Documentation](https://learn.microsoft.com/azure/developer/azure-mcp-server/)
- [Let's Learn – MCP Events](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/lets-learn---mcp-events-a-beginners-guide-to-the-model-context-protocol/4429023)
- [Awesome GitHub Copilot Customizations](https://github.com/awesome-copilot)
- [C# MCP SDK](https://developer.microsoft.com/blog/microsoft-partners-with-anthropic-to-create-official-c-sdk-for-model-context-protocol)
- [MCP Dev Days Live 29th/30th July or watch on Demand](https://aka.ms/mcpdevdays)

## 🎯 Exercises

1. **Install and Configure**: Set up one of the MCP servers in your VS Code environment and test basic functionality.
2. **Workflow Integration**: Design a development workflow that combines at least three different MCP servers.
3. **Custom Server Planning**: Identify a task in your daily development routine that could benefit from a custom MCP server and create a specification for it.
4. **Performance Analysis**: Compare the efficiency of using MCP servers versus traditional approaches for common development tasks.
5. **Security Assessment**: Evaluate the security implications of using MCP servers in your development environment and propose best practices.

Next:[Best Practices](../08-BestPractices/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.