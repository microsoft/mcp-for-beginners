# 模型上下文协议 (MCP) 简介：为何它对可扩展的 AI 应用至关重要

[![模型上下文协议简介](../../../translated_images/zh-CN/01.a467036d886b5fb5b9cf7b39bac0e743b6ca0a4a18a492de90061daaf0cc55f0.png)](https://youtu.be/agBbdiOPLQA)

_（点击上方图片观看本课视频）_

生成式 AI 应用是一个巨大的进步，因为它们通常允许用户通过自然语言提示与应用交互。然而，随着在这些应用上投入的时间和资源越来越多，你需要确保能够轻松集成功能和资源，使其易于扩展，让你的应用能够支持多个模型并处理各种模型的复杂性。简而言之，构建生成式 AI 应用在开始时很容易，但随着它们的增长和复杂化，你需要开始定义架构，并可能需要依赖一个标准来确保应用以一致的方式构建。这就是 MCP 的作用，它帮助组织并提供一个标准。

---

## **🔍 什么是模型上下文协议 (MCP)?**

**模型上下文协议 (MCP)** 是一个**开放的标准化接口**，允许大型语言模型 (LLMs) 无缝地与外部工具、API 和数据源交互。它提供了一种一致的架构，增强 AI 模型在训练数据之外的功能，从而实现更智能、更可扩展、更具响应性的 AI 系统。

---

## **🎯 为什么 AI 标准化很重要**

随着生成式 AI 应用变得越来越复杂，采用标准以确保**可扩展性、可扩展性、可维护性**以及**避免供应商锁定**变得至关重要。MCP 通过以下方式解决了这些需求：

- 统一模型与工具的集成
- 减少脆弱的、一次性定制解决方案
- 允许来自不同供应商的多个模型在一个生态系统中共存

**注意：** 虽然 MCP 自称为开放标准，但目前没有计划通过任何现有的标准组织（如 IEEE、IETF、W3C、ISO 或其他标准组织）对 MCP 进行标准化。

---

## **📚 学习目标**

阅读本文后，你将能够：

- 定义**模型上下文协议 (MCP)**及其使用场景
- 理解 MCP 如何标准化模型与工具的通信
- 识别 MCP 架构的核心组件
- 探索 MCP 在企业和开发环境中的实际应用

---

## **💡 为什么模型上下文协议 (MCP) 是一个颠覆性创新**

### **🔗 MCP 解决了 AI 交互中的碎片化问题**

在 MCP 出现之前，模型与工具的集成需要：

- 每个工具-模型对的定制代码
- 每个供应商的非标准化 API
- 因更新而频繁中断
- 随着工具数量增加而难以扩展

### **✅ MCP 标准化的优势**

| **优势**                  | **描述**                                                                      |
|--------------------------|------------------------------------------------------------------------------|
| 互操作性                 | LLMs 可与不同供应商的工具无缝协作                                            |
| 一致性                   | 在平台和工具之间实现统一行为                                                  |
| 可重用性                 | 一次构建的工具可在多个项目和系统中使用                                        |
| 加速开发                 | 通过使用标准化的即插即用接口减少开发时间                                      |

---

## **🧱 MCP 高级架构概述**

MCP 遵循**客户端-服务器模型**，其中：

- **MCP 主机**运行 AI 模型
- **MCP 客户端**发起请求
- **MCP 服务器**提供上下文、工具和功能

### **关键组件：**

- **资源** – 模型的静态或动态数据  
- **提示** – 用于引导生成的预定义工作流  
- **工具** – 可执行功能，如搜索、计算  
- **采样** – 通过递归交互实现代理行为  

---

## MCP 服务器如何工作

MCP 服务器的操作流程如下：

- **请求流程**：
    1. 请求由最终用户或代表用户操作的软件发起。
    2. **MCP 客户端**将请求发送到**MCP 主机**，后者管理 AI 模型运行时。
    3. **AI 模型**接收用户提示，并可能通过一个或多个工具调用请求访问外部工具或数据。
    4. **MCP 主机**（而非模型本身）使用标准化协议与适当的**MCP 服务器**通信。
- **MCP 主机功能**：
    - **工具注册表**：维护可用工具及其功能的目录。
    - **认证**：验证工具访问权限。
    - **请求处理器**：处理模型发来的工具请求。
    - **响应格式化器**：将工具输出结构化为模型可理解的格式。
- **MCP 服务器执行**：
    - **MCP 主机**将工具调用路由到一个或多个**MCP 服务器**，每个服务器提供专门的功能（如搜索、计算、数据库查询）。
    - **MCP 服务器**执行其各自的操作，并以一致的格式将结果返回给**MCP 主机**。
    - **MCP 主机**格式化并将这些结果传递给**AI 模型**。
- **响应完成**：
    - **AI 模型**将工具输出整合到最终响应中。
    - **MCP 主机**将此响应发送回**MCP 客户端**，后者将其交付给最终用户或调用软件。

```mermaid
---
title: MCP Architecture and Component Interactions
description: A diagram showing the flows of the components in MCP.
---
graph TD
    Client[MCP Client/Application] -->|Sends Request| H[MCP Host]
    H -->|Invokes| A[AI Model]
    A -->|Tool Call Request| H
    H -->|MCP Protocol| T1[MCP Server Tool 01: Web Search]
    H -->|MCP Protocol| T2[MCP Server Tool 02: Calculator tool]
    H -->|MCP Protocol| T3[MCP Server Tool 03: Database Access tool]
    H -->|MCP Protocol| T4[MCP Server Tool 04: File System tool]
    H -->|Sends Response| Client

    subgraph "MCP Host Components"
        H
        G[Tool Registry]
        I[Authentication]
        J[Request Handler]
        K[Response Formatter]
    end

    H <--> G
    H <--> I
    H <--> J
    H <--> K

    style A fill:#f9d5e5,stroke:#333,stroke-width:2px
    style H fill:#eeeeee,stroke:#333,stroke-width:2px
    style Client fill:#d5e8f9,stroke:#333,stroke-width:2px
    style G fill:#fffbe6,stroke:#333,stroke-width:1px
    style I fill:#fffbe6,stroke:#333,stroke-width:1px
    style J fill:#fffbe6,stroke:#333,stroke-width:1px
    style K fill:#fffbe6,stroke:#333,stroke-width:1px
    style T1 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T2 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T3 fill:#c2f0c2,stroke:#333,stroke-width:1px
    style T4 fill:#c2f0c2,stroke:#333,stroke-width:1px
```

## 👨‍💻 如何构建 MCP 服务器（附示例）

MCP 服务器允许你通过提供数据和功能来扩展 LLM 的能力。

准备好尝试了吗？以下是语言和/或技术栈的 SDK 示例，展示如何在不同语言/技术栈中创建简单的 MCP 服务器：

- **Python SDK**: https://github.com/modelcontextprotocol/python-sdk

- **TypeScript SDK**: https://github.com/modelcontextprotocol/typescript-sdk

- **Java SDK**: https://github.com/modelcontextprotocol/java-sdk

- **C#/.NET SDK**: https://github.com/modelcontextprotocol/csharp-sdk

---

## 🌍 MCP 的实际应用场景

MCP 通过扩展 AI 的能力支持广泛的应用：

| **应用场景**               | **描述**                                                                      |
|----------------------------|------------------------------------------------------------------------------|
| 企业数据集成               | 将 LLMs 连接到数据库、CRM 或内部工具                                          |
| 代理型 AI 系统             | 通过工具访问和决策工作流启用自主代理                                          |
| 多模态应用                 | 在单一统一的 AI 应用中结合文本、图像和音频工具                                |
| 实时数据集成               | 将实时数据引入 AI 交互中，以提供更准确、最新的输出                              |

### 🧠 MCP = AI 交互的通用标准

模型上下文协议 (MCP) 充当 AI 交互的通用标准，就像 USB-C 标准化了设备的物理连接一样。在 AI 世界中，MCP 提供了一致的接口，使模型（客户端）能够与外部工具和数据提供者（服务器）无缝集成。这消除了为每个 API 或数据源设计多样化、定制协议的需求。

在 MCP 下，兼容 MCP 的工具（称为 MCP 服务器）遵循统一标准。这些服务器可以列出它们提供的工具或操作，并在 AI 代理请求时执行这些操作。支持 MCP 的 AI 代理平台能够通过此标准协议发现服务器提供的工具并调用它们。

### 💡 促进知识访问

除了提供工具，MCP 还促进知识访问。它通过将大型语言模型 (LLMs) 与各种数据源连接，为应用提供上下文。例如，一个 MCP 服务器可能代表公司的文档库，允许代理按需检索相关信息。另一个服务器可能处理特定操作，如发送电子邮件或更新记录。从代理的角度来看，这些只是它可以使用的工具——有些工具返回数据（知识上下文），而另一些工具执行操作。MCP 高效地管理两者。

连接到 MCP 服务器的代理可以通过标准格式自动了解服务器的可用功能和可访问数据。这种标准化实现了动态工具的可用性。例如，将新的 MCP 服务器添加到代理系统中，其功能可以立即使用，而无需进一步定制代理的指令。

这种简化的集成与以下图示中的流程一致，服务器提供工具和知识，确保系统间的无缝协作。

### 👉 示例：可扩展的代理解决方案

```mermaid
---
title: Scalable Agent Solution with MCP
description: A diagram illustrating how a user interacts with an LLM that connects to multiple MCP servers, with each server providing both knowledge and tools, creating a scalable AI system architecture
---
graph TD
    User -->|Prompt| LLM
    LLM -->|Response| User
    LLM -->|MCP| ServerA
    LLM -->|MCP| ServerB
    ServerA -->|Universal connector| ServerB
    ServerA --> KnowledgeA
    ServerA --> ToolsA
    ServerB --> KnowledgeB
    ServerB --> ToolsB

    subgraph Server A
        KnowledgeA[Knowledge]
        ToolsA[Tools]
    end

    subgraph Server B
        KnowledgeB[Knowledge]
        ToolsB[Tools]
    end
```
通用连接器使 MCP 服务器能够相互通信并共享功能，允许 ServerA 将任务委托给 ServerB 或访问其工具和知识。这种工具和数据的联邦化支持了可扩展和模块化的代理架构。由于 MCP 标准化了工具的暴露，代理可以动态发现并在服务器之间路由请求，而无需硬编码集成。

工具和知识联邦化：工具和数据可以跨服务器访问，从而实现更可扩展和模块化的代理架构。

### 🔄 客户端集成 LLM 的高级 MCP 场景

除了基本的 MCP 架构，还有一些高级场景，其中客户端和服务器都包含 LLM，从而实现更复杂的交互。在以下图示中，**客户端应用**可能是一个 IDE，提供多个 MCP 工具供 LLM 使用：

```mermaid
---
title: Advanced MCP Scenarios with Client-Server LLM Integration
description: A sequence diagram showing the detailed interaction flow between user, client application, client LLM, multiple MCP servers, and server LLM, illustrating tool discovery, user interaction, direct tool calling, and feature negotiation phases
---
sequenceDiagram
    autonumber
    actor User as 👤 User
    participant ClientApp as 🖥️ Client App
    participant ClientLLM as 🧠 Client LLM
    participant Server1 as 🔧 MCP Server 1
    participant Server2 as 📚 MCP Server 2
    participant ServerLLM as 🤖 Server LLM
    
    %% Discovery Phase
    rect rgb(220, 240, 255)
        Note over ClientApp, Server2: TOOL DISCOVERY PHASE
        ClientApp->>+Server1: Request available tools/resources
        Server1-->>-ClientApp: Return tool list (JSON)
        ClientApp->>+Server2: Request available tools/resources
        Server2-->>-ClientApp: Return tool list (JSON)
        Note right of ClientApp: Store combined tool<br/>catalog locally
    end
    
    %% User Interaction
    rect rgb(255, 240, 220)
        Note over User, ClientLLM: USER INTERACTION PHASE
        User->>+ClientApp: Enter natural language prompt
        ClientApp->>+ClientLLM: Forward prompt + tool catalog
        ClientLLM->>-ClientLLM: Analyze prompt & select tools
    end
    
    %% Scenario A: Direct Tool Calling
    alt Direct Tool Calling
        rect rgb(220, 255, 220)
            Note over ClientApp, Server1: SCENARIO A: DIRECT TOOL CALLING
            ClientLLM->>+ClientApp: Request tool execution
            ClientApp->>+Server1: Execute specific tool
            Server1-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    
    %% Scenario B: Feature Negotiation (VS Code style)
    else Feature Negotiation (VS Code style)
        rect rgb(255, 220, 220)
            Note over ClientApp, ServerLLM: SCENARIO B: FEATURE NEGOTIATION
            ClientLLM->>+ClientApp: Identify needed capabilities
            ClientApp->>+Server2: Negotiate features/capabilities
            Server2->>+ServerLLM: Request additional context
            ServerLLM-->>-Server2: Provide context
            Server2-->>-ClientApp: Return available features
            ClientApp->>+Server2: Call negotiated tools
            Server2-->>-ClientApp: Return results
            ClientApp->>+ClientLLM: Process results
            ClientLLM-->>-ClientApp: Generate response
            ClientApp-->>-User: Display final answer
        end
    end
```

## 🔐 MCP 的实际优势

以下是使用 MCP 的实际优势：

- **实时性**：模型可以访问超出其训练数据的最新信息
- **能力扩展**：模型可以利用专门的工具完成其未训练的任务
- **减少幻觉**：外部数据源提供事实依据
- **隐私**：敏感数据可以保留在安全环境中，而不是嵌入到提示中

## 📌 关键要点

以下是使用 MCP 的关键要点：

- **MCP** 标准化了 AI 模型与工具和数据的交互方式
- 促进**可扩展性、一致性和互操作性**
- MCP 有助于**减少开发时间、提高可靠性并扩展模型能力**
- 客户端-服务器架构**支持灵活、可扩展的 AI 应用**

## 🧠 练习

思考一个你感兴趣的 AI 应用。

- 哪些**外部工具或数据**可以增强其功能？
- MCP 如何使集成**更简单、更可靠？**

## 其他资源

- [MCP GitHub 仓库](https://github.com/modelcontextprotocol)

---

## 下一步

下一章：[第 1 章：核心概念](../01-CoreConcepts/README.md)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。