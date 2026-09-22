![MCP-for-beginners](../../translated_images/pcm/mcp-beginners.2ce2b317996369ff.webp) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![MCP Toplist](https://mcptoplist.com/badge/mcp.so%2Fmcp-for-beginners%2Fmicrosoft.svg)](https://mcptoplist.com/server/mcp.so%2Fmcp-for-beginners%2Fmicrosoft)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Follow these steps to get started using these resources:
1. **Fork the Repository**: Click [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **Clone the Repository**:   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. **Join The** [![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)


### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/mcp-for-beginners.git
> cd mcp-for-beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> This gives you everything you need to complete the course with a much faster download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

# 🚀 Model Context Protocol (MCP) Curriculum for Beginners

## **Learn MCP with Hands-on Code Examples in C#, Java, JavaScript, Rust, Python, and TypeScript**

## 🧠 Overview of the Model Context Protocol Curriculum
Welcome to your journey into the Model Context Protocol! If you've ever wondered how AI applications communicate with different tools and services, you're about to discover the elegant solution that's transforming how developers build intelligent systems.

Think of MCP as a universal translator for AI applications - just like how USB ports let you connect any device to your computer, MCP lets AI models connect to any tool or service in a standardized way. Whether you're building your first chatbot or working on complex AI workflows, understanding MCP will give you the power to create more capable and flexible applications.

This curriculum is designed with patience and care for your learning journey. We'll start with simple concepts you already understand and gradually build your expertise through hands-on practice in your favorite programming language. Every step includes clear explanations, practical examples, and plenty of encouragement along the way.

By the time you complete this journey, you'll have the confidence to build your own MCP servers, integrate them with popular AI platforms, and understand how this technology is reshaping the future of AI development. Let's begin this exciting adventure together!

### Official Documentation and Specifications

The current protocol revision is **MCP Specification 2026-07-28**. The MCP
specification uses date-based versioning (YYYY-MM-DD format) to make protocol
compatibility explicit.

> **Version note:** this curriculum teaches the current `2026-07-28`
> concepts, including stateless requests, the Extensions framework, and the
> deprecation of Roots, Sampling, and Logging. Some hands-on examples remain
> explicitly versioned to `2025-11-25` while SDK support catches up. See
> [What's Changed in MCP: The 2026-07-28 Specification](./01-CoreConcepts/mcp-2026-07-28.md)
> for the changes and migration guidance.

These resources become more valuable as your understanding grows, but don't feel pressured to read everything immediately. Start with the areas that interest you most!
- 📘 [MCP Documentation](https://modelcontextprotocol.io/) – This is your go-to resource for step-by-step tutorials and user guides. The documentation is written with beginners in mind, providing clear examples you can follow along with at your own pace.
- 📜 [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28) – Think of this as your comprehensive reference manual. As you work through the curriculum, you'll find yourself returning here to look up specific details and explore advanced features.
- 📜 [MCP Specification Versioning](https://modelcontextprotocol.io/specification/versioning) – This contains information about protocol version history and how MCP uses date-based versioning (YYYY-MM-DD format).
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) –  Here you'll find SDKs, tools, and code samples in multiple programming languages. It's like a treasure trove of practical examples and ready-to-use components.
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – Join fellow learners and experienced developers in discussions about MCP. It's a supportive community where questions are welcome and knowledge is shared freely.
  
## Learning Objectives

By the end of this curriculum, you'll feel confident and excited about your new abilities. Here's what you'll achieve:

• **Understand MCP fundamentals**: You'll grasp what the Model Context Protocol is and why it's revolutionizing how AI applications work together, using analogies and examples that make sense.

• **Build your first MCP server**: You'll create a working MCP server in your preferred programming language, starting with simple examples and growing your skills step by step.

• **Connect AI models to real tools**: You'll learn how to bridge the gap between AI models and actual services, giving your applications powerful new capabilities.

• **Implement security best practices**: You'll understand how to keep your MCP implementations safe and secure, protecting both your applications and your users.

• **Deploy with confidence**: You'll know how to take your MCP projects from development to production, with practical deployment strategies that work in the real world.

• **Join the MCP community**: You'll become part of a growing community of developers who are shaping the future of AI application development. 

## Essential Background

Before we dive into MCP specifics, let's make sure you feel comfortable with some foundational concepts. Don't worry if you're not an expert in these areas - we'll explain everything you need to know as we go!

### Understanding Protocols (The Foundation)

Think of a protocol like the rules for a conversation. When you call a friend, you both know to say "hello" when you answer, take turns speaking, and say "goodbye" when you're done. Computer programs need similar rules to communicate effectively.

MCP is a protocol - a set of agreed-upon rules that help AI models and applications have productive "conversations" with tools and services. Just like how having conversation rules makes human communication smoother, having MCP makes AI application communication much more reliable and powerful.

### Client-Server Relationships (How Programs Work Together)

You already use client-server relationships every day! When you use a web browser (the client) to visit a website, you're connecting to a web server that sends you the page content. The browser knows how to ask for information, and the server knows how to respond.

In MCP, we have a similar relationship: AI models act as clients that request information or actions, while MCP servers provide those capabilities. It's like having a helpful assistant (the server) that the AI can ask to perform specific tasks.

### Why Standardization Matters (Making Things Work Together)

Imagine if every car manufacturer used different shaped gas pumps - you'd need a different adapter for each car! Standardization means agreeing on common approaches so things work together seamlessly.

MCP provides this standardization for AI applications. Instead of every AI model needing custom code to work with every tool, MCP creates a universal way for them to communicate. This means developers can build tools once and have them work with many different AI systems.

## 🧭 Your Learning Path Overview

Your MCP journey is carefully structured to build your confidence and skills progressively. Each phase introduces new concepts while reinforcing what you've already learned.

### 🌱 Foundation Phase: Understanding the Basics (Modules 0-2)

This is where your adventure begins! We'll introduce you to MCP concepts using familiar analogies and simple examples. You'll understand what MCP is, why it exists, and how it fits into the larger world of AI development.


• **Module 0 - Introduction to MCP**: We go start by explore wetin MCP be and why e important well-well for modern AI applications. You go see real-world examples of MCP for action and understand how e dey solve common wahala wey developers dey face.

• **Module 1 - Core Concepts Explained**: for here, you go learn the main building blocks of MCP. We go use plenty analogies and visual examples to make sure say these concepts clear and easy to understand.

• **Module 2 - Security in MCP**: Security fit sound fear, but we go show you how MCP get built-in safety features and teach you beta practices wey go protect your applications from start.

### 🔨 Building Phase: Creating Your First Implementations (Module 3)

Now the real fun don start! You go get hands-on experience to build actual MCP servers and clients. No worry - we go start simple and guide you every step.

This module get multiple hands-on guides wey go make you practice for your preferred programming language. You go create your first server, build client wey go connect to am, and even join popular development tools like VS Code.

Every guide get full code examples, troubleshooting tips, and explanations why we choose certain design. By the end of this phase, you go get working MCP implementations wey you fit proud of!

### 🚀 Growing Phase: Advanced Concepts and Real-World Application (Modules 4-5)

After you don sabi basics, you ready to explore more advanced MCP features. We go talk about practical implementation methods, debugging techniques, and advanced topics like multi-modal AI integration.

You go also learn how to scale your MCP implementations for production use and integrate with cloud platforms like Azure. These modules go prepare you to build MCP solutions wey fit handle real-world wahala.

### 🌟 Mastery Phase: Community and Specialization (Modules 6-11)

The final phase na about joining the MCP community and specialize for areas wey you like pass. You go learn how to contribute to open-source MCP projects, implement advanced authentication patterns, and build full database-integrated solutions.

Module 11 deserve special mention - na complete 13-lab hands-on learning path wey teach you how to build production-ready MCP servers with PostgreSQL integration. E be like capstone project wey bring all you don learn together!

### 📚 Complete Curriculum Structure

| Module | Topic | Description | Link |
|--------|-------|-------------|------|
| **Module 0-3: Fundamentals** | | | |
| 00 | Introduction to MCP | Overview of the Model Context Protocol and its significance in AI pipelines | [Read more](./00-Introduction/README.md) |
| 01 | Core Concepts Explained | In-depth exploration of core MCP concepts | [Read more](./01-CoreConcepts/README.md) |
| 1.1 | What's Changed in MCP (2026-07-28) | Stateless protocol, Extensions framework, and feature deprecations in the current specification | [Guide](./01-CoreConcepts/mcp-2026-07-28.md) |
| 02 | Security in MCP | Security threats and best practices | [Read more](./02-Security/README.md) |
| 2.1 | CIMD and DCR Authorization | Compare preferred CIMD registration with deprecated DCR fallback using a protected MCP server | [Sample](./02-Security/samples/cimd-dcr-auth/README.md) |
| 03 | Getting Started with MCP | Environment setup, basic servers/clients, integration | [Read more](./03-GettingStarted/README.md) |
| **Module 3: Building Your First Server & Client** | | | |
| 3.1 | First Server | Create your first MCP server | [Guide](./03-GettingStarted/01-first-server/README.md) |
| 3.2 | First Client | Develop a basic MCP client | [Guide](./03-GettingStarted/02-client/README.md) |
| 3.3 | Client with LLM | Integrate large language models | [Guide](./03-GettingStarted/03-llm-client/README.md) |
| 3.4 | VS Code Integration | Consume MCP servers in VS Code | [Guide](./03-GettingStarted/04-vscode/README.md) |
| 3.5 | stdio Server | Create servers using stdio transport | [Guide](./03-GettingStarted/05-stdio-server/README.md) |
| 3.6 | HTTP Streaming | Implement HTTP streaming in MCP | [Guide](./03-GettingStarted/06-http-streaming/README.md) |
| 3.7 | Microsoft Foundry Toolkit | Use Microsoft Foundry Toolkit with MCP | [Guide](./03-GettingStarted/07-aitk/README.md) |
| 3.8 | Testing | Test your MCP server implementation | [Guide](./03-GettingStarted/08-testing/README.md) |
| 3.9 | Deployment | Deploy MCP servers to production | [Guide](./03-GettingStarted/09-deployment/README.md) |
| 3.10 | Advanced server usage | Use advanced servers for advanced feature usage and improved architecture | [Guide](./03-GettingStarted/10-advanced/README.md) |
| 3.11 | Simple auth | A chapter showing you auth from the beginning and RBAC | [Guide](./03-GettingStarted/11-simple-auth/README.md) |
| 3.12 | MCP Hosts | Configure Claude Desktop, Cursor, Cline, and other MCP hosts | [Guide](./03-GettingStarted/12-mcp-hosts/README.md) |
| 3.13 | MCP Inspector | Debug and test MCP servers with the Inspector tool | [Guide](./03-GettingStarted/13-mcp-inspector/README.md) |
| 3.14 | Sampling | Use sampling to collaborate with the client | [Guide](./03-GettingStarted/14-sampling/README.md) |
| 3.15 | MCP Apps | Build MCP Apps | [Guide](./03-GettingStarted/15-mcp-apps/README.md) |
| **Module 4-5: Practical & Advanced** | | | |
| 04 | Practical Implementation | SDKs, debugging, testing, reusable prompt templates | [Read more](./04-PracticalImplementation/README.md) |
| 4.1 | Pagination | Handle large result sets with cursor-based pagination | [Guide](./04-PracticalImplementation/pagination/README.md) |
| 05 | Advanced Topics in MCP | Multi-modal AI, scaling, enterprise use | [Read more](./05-AdvancedTopics/README.md) |
| 5.1 | Azure Integration | MCP Integration with Azure | [Guide](./05-AdvancedTopics/mcp-integration/README.md) |
| 5.2 | Multi-modality | Working with multiple modalities | [Guide](./05-AdvancedTopics/mcp-multi-modality/README.md) |
| 5.3 | OAuth2 Demo | Implement OAuth2 authentication | [Guide](./05-AdvancedTopics/mcp-oauth2-demo/README.md) |
| 5.4 | Root Contexts | Understand and implement root contexts | [Guide](./05-AdvancedTopics/mcp-root-contexts/README.md) |
| 5.5 | Routing | MCP routing strategies | [Guide](./05-AdvancedTopics/mcp-routing/README.md) |
| 5.6 | Sampling | Sampling techniques in MCP | [Guide](./05-AdvancedTopics/mcp-sampling/README.md) |
| 5.7 | Scaling | Scale MCP implementations | [Guide](./05-AdvancedTopics/mcp-scaling/README.md) |
| 5.8 | Security | Advanced security considerations | [Guide](./05-AdvancedTopics/mcp-security/README.md) |
| 5.9 | Web Search | Implement web search capabilities | [Guide](./05-AdvancedTopics/web-search-mcp/README.md) |
| 5.10 | Realtime Streaming | Build realtime streaming functionality | [Guide](./05-AdvancedTopics/mcp-realtimestreaming/README.md) |
| 5.11 | Realtime Search | Implement realtime search | [Guide](./05-AdvancedTopics/mcp-realtimesearch/README.md) |
| 5.12 | Entra ID Auth | Authentication with Microsoft Entra ID | [Guide](./05-AdvancedTopics/mcp-security-entra/README.md) |
| 5.13 | Foundry Integration | Integrate with Microsoft Foundry | [Guide](./05-AdvancedTopics/mcp-foundry-agent-integration/README.md) |
| 5.14 | Context Engineering | Techniques for effective context engineering | [Guide](./05-AdvancedTopics/mcp-contextengineering/README.md) |
| 5.15 | MCP Custom Transport | Custom Transport implementations | [Guide](./05-AdvancedTopics/mcp-transport/README.md) |
| 5.16 | Protocol Features | Progress notifications, cancellation, resource templates | [Guide](./05-AdvancedTopics/mcp-protocol-features/README.md) |
| 5.17 | Adversarial Multi-Agent Reasoning | Two agents argue opposite sides using shared MCP tools, evaluated by a judge agent | [Guide](./05-AdvancedTopics/mcp-adversarial-agents/README.md) |
| **Module 6-10: Community & Best Practices** | | | |
| 06 | Community Contributions | How to contribute to the MCP ecosystem | [Guide](./06-CommunityContributions/README.md) |
| 07 | Insights from Early Adoption | Real-world implementation stories | [Guide](./07-LessonsfromEarlyAdoption/README.md) |
| 08 | Best Practices for MCP | Performance, fault-tolerance, resilience | [Guide](./08-BestPractices/README.md) |
| 09 | MCP Case Studies | Practical implementation examples | [Guide](./09-CaseStudy/README.md) |
| 10 | Hands-on Workshop | Building an MCP Server with Microsoft Foundry Toolkit | [Lab](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md) |
| **Module 11: MCP Server Hands On Lab** | | | |
| 11 | MCP Server Database Integration | Comprehensive 13-lab hands-on learning path for PostgreSQL integration | [Labs](./11-MCPServerHandsOnLabs/README.md) |
| 11.1 | Introduction | Overview of MCP with database integration and retail analytics use case | [Lab 00](./11-MCPServerHandsOnLabs/00-Introduction/README.md) |
| 11.2 | Core Architecture | Understanding MCP server architecture, database layers, and security patterns | [Lab 01](./11-MCPServerHandsOnLabs/01-Architecture/README.md) |
| 11.3 | Security & Multi-Tenancy | Row Level Security, authentication, and multi-tenant data access | [Lab 02](./11-MCPServerHandsOnLabs/02-Security/README.md) |
| 11.4 | Environment Setup | Setting up development environment, Docker, Azure resources | [Lab 03](./11-MCPServerHandsOnLabs/03-Setup/README.md) |
| 11.5 | Database Design | PostgreSQL setup, retail schema design, and sample data | [Lab 04](./11-MCPServerHandsOnLabs/04-Database/README.md) |
| 11.6 | MCP Server Implementation | Building the FastMCP server with database integration | [Lab 05](./11-MCPServerHandsOnLabs/05-MCP-Server/README.md) |
| 11.7 | Tool Development | Creating database query tools and schema introspection | [Lab 06](./11-MCPServerHandsOnLabs/06-Tools/README.md) |
| 11.8 | Semantic Search | Implementing vector embeddings with Azure OpenAI and pgvector | [Lab 07](./11-MCPServerHandsOnLabs/07-Semantic-Search/README.md) |
| 11.9 | Testing & Debugging | Testing strategies, debugging tools, and validation approaches | [Lab 08](./11-MCPServerHandsOnLabs/08-Testing/README.md) |
| 11.10 | VS Code Integration | Configuring VS Code MCP integration and AI Chat usage | [Lab 09](./11-MCPServerHandsOnLabs/09-VS-Code/README.md) |
| 11.11 | Deployment Strategies | Docker deployment, Azure Container Apps, and scaling considerations | [Lab 10](./11-MCPServerHandsOnLabs/10-Deployment/README.md) |
| 11.12 | Monitoring | Application Insights, logging, performance monitoring | [Lab 11](./11-MCPServerHandsOnLabs/11-Monitoring/README.md) |
| 11.13 | Best Practices | Performance optimization, security hardening, and production tips | [Lab 12](./11-MCPServerHandsOnLabs/12-Best-Practices/README.md) |
| **Module 12: MCP Tooling** | | | |
| 12.1 | Tooling | MCP usage in Copilot App | [ Guide ](./12-tooling/README.md) |

### 💻 Sample Code Projects


One of di most excitin parts of learnin MCP na to see your code skills dey develop step by step. We don design our code examples make dem start simple den grow more sophisticated as you sabi more. Na so we dey introduce concepts - wit code wey easy to understand but show real MCP principles, you go sabi no only wetin dis code dey do, but why e dey arranged like dis and how e take fit for big MCP applications.

#### Basic MCP Calculator Samples

| Language | Description | Link |
|----------|-------------|------|
| C# | MCP Server Example | [View Code](./03-GettingStarted/samples/csharp/README.md) |
| Java | MCP Calculator | [View Code](./03-GettingStarted/samples/java/calculator/README.md) |
| JavaScript | MCP Demo | [View Code](./03-GettingStarted/samples/javascript/README.md) |
| Python | MCP Server | [View Code](../../03-GettingStarted/samples/python/mcp_calculator_server.py) |
| TypeScript | MCP Example | [View Code](./03-GettingStarted/samples/typescript/README.md) |
| Rust | MCP Example | [View Code](./03-GettingStarted/samples/rust/README.md) |

#### Advanced MCP Implementations

| Language | Description | Link |
|----------|-------------|------|
| C# | Advanced Sample | [View Code](./04-PracticalImplementation/samples/csharp/README.md) |
| Java with Spring | Container App Example | [View Code](./04-PracticalImplementation/samples/java/containerapp/README.md) |
| JavaScript | Advanced Sample | [View Code](./04-PracticalImplementation/samples/javascript/README.md) |
| Python | Complex Implementation | [View Code](./04-PracticalImplementation/samples/python/README.md) |
| TypeScript | Container Sample | [View Code](./04-PracticalImplementation/samples/typescript/README.md) |


## 🎯 Prerequisites for Learning MCP

To get di most outta dis curriculum, you suppose get:

- Basic knowledge of programming for at least one of dis languages: C#, Java, JavaScript, Python, or TypeScript
- Understanding of client-server model and APIs
- Familiarity wit REST and HTTP concepts
- (Optional) Background for AI/ML concepts

- Joining our community discussions for help

## 📚 Study Guide & Resources

Dis repository get plenty resources to help you waka and learn well:

### Study Guide

Comprehensive [Study Guide](./study_guide.md) dey to help you navigate dis repository well. Dis visual curriculum map show how all di topics connect and give guide on how to use di sample projects well. E good especially if you be visual learner wey like see di whole picture.

Di guide get:
- Visual curriculum map weh show all di topics wey e cover
- Details about each repository section
- Guidance on how to use sample projects
- Recommended learning paths for different skill levels
- Additional resources to support your learning journey

### Changelog

We dey maintain detailed [Changelog](./changelog.md) wey track all important updates to di curriculum materials, so you fit dey current wit di latest improvements and additions.
- New content additions
- Structural changes
- Feature improvements
- Documentation updates

## 🛠️ How to Use Dis Curriculum Well

Each lesson for dis guide get:

1. Clear explanations of MCP concepts  
2. Live code examples for many languages  
3. Exercises to build real MCP applications  
4. Extra resources for advanced learners

### Make We Learn MCP wit C# - Tutorial Series
Make we learn about di Model Context Protocol (MCP), one sharp framework wey dem create to standardize how AI models and client applications dey interact. Through dis beginner-friendly session, we go introduce you to MCP and guide you to create your first MCP server.
#### C#: [https://aka.ms/letslearnmcp-csharp](https://aka.ms/letslearnmcp-csharp)
#### Java: [https://aka.ms/letslearnmcp-java](https://aka.ms/letslearnmcp-java)
#### JavaScript: [https://aka.ms/letslearnmcp-javascript](https://aka.ms/letslearnmcp-javascript)
#### Python: [https://aka.ms/letslearnmcp-python](https://aka.ms/letslearnmcp-python)

## 🎓 Your MCP Journey Don Start

Congratulations! You don take di first step for one exciting journey wey go expand your programming skills and connect you to the cutting edge of AI development.

### Wetin You Don Accomplish

By readin dis introduction, you don already start to build your MCP knowledge foundation. You sabi wetin MCP be, why e matter, and how dis curriculum go support your learning journey. Na big achievement and di beginning of your expertise for dis important technology.

### Di Adventure Wey Dey Go Front

As you dey progress through di modules, remember say every expert be beginner at first. Di concepts wey fit look complex now go become easy as you dey practice and use dem. Every small step dey build powerful skills wey go help you all through your development career.

### Your Support Network

You dey join community of learners and experts wey dey passionate about MCP and ready to help others succeed. Whether you stuck for coding challenge or you dey excited to share breakthrough, di community dey here to support your journey.

If you jam wahala or get any question about how to build AI apps, join fellow learners and experienced developers for discussions about MCP. E sure community where questions dey welcome and knowledge dey shared freely.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or errors while you dey build, visit:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

### Ready to Begin?

Your MCP adventure don start now! Begin wit Module 0 to dive into your first hands-on MCP experiences, or check out di sample projects to see wetin you go dey build. Remember - every expert start exactly where you dey now, and wit patience and practice, you go surprise yourself with wetin you fit achieve.

Welcome to di world of Model Context Protocol development. Make we build something beta together!

## 🤝 How to Contribute to di Learning Community

Dis curriculum go strong as learners like you dey contribute! Whether you dey fix typo, suggest better explanation, or add new example, your contributions dey help other beginners succeed.

Thanks to Microsoft Valued Professional [Shivam Goyal](https://www.linkedin.com/in/shivam2003/) for contributing code samples.

Di contribution process dey designed to be welcoming and supportive. Most contributions need Contributor License Agreement (CLA), but automated tools go guide you well through di process.

## 📜 Open Source Learning

Dis whole curriculum dey available under MIT [LICENSE](../../LICENSE), meaning you fit use, modify, and share am freely. Dis na to support our mission to make MCP knowledge available to developers everywhere.
## 🤝 Contribution Guidelines

Dis project welcome contributions and suggestions. Most contributions need say you agree with
Contributor License Agreement (CLA) wey talk say you get right to, and you dey really grant us
di rights to use your contribution. For details, visit <https://cla.opensource.microsoft.com>.

When you submit pull request, CLA bot go automatically check whether you need provide
CLA and add di right decoration for the PR (e.g., status check, comment). Just follow instructions
wey di bot provide. You go only do dis once for all repos wey dey use our CLA.

Dis project don adopt [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more info, see [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) for any additional questions or comments.

---

*You ready to start your MCP journey? Begin wit [Module 00 - Introduction to MCP](./00-Introduction/README.md) and take your first steps inside di world of Model Context Protocol development!*



## 🎒 Other Courses
Our team dey produce other courses! Check am out:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)

[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Serie Dem
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->