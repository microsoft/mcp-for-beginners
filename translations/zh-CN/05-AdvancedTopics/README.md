# MCP 高级主题

[![高级 MCP：安全、可扩展和多模态 AI 代理](../../../translated_images/zh-CN/06.42259eaf91fccfc6.webp)](https://youtu.be/4yjmGvJzYdY)

_(点击上方图片观看本课视频)_

本章涵盖了模型上下文协议（MCP）实现中的一系列高级主题，包括多模态集成、可扩展性、安全最佳实践以及企业集成。这些主题对于构建稳健且适用于生产环境的 MCP 应用至关重要，能够满足现代 AI 系统的需求。

## 概述

本课探讨了模型上下文协议实现中的高级概念，重点关注多模态集成、可扩展性、安全最佳实践及企业集成。这些主题对于构建能够处理复杂企业环境需求的生产级 MCP 应用至关重要。

## 学习目标

本课结束时，您将能够：

- 在 MCP 框架中实现多模态能力
- 设计适用于高需求场景的可扩展 MCP 架构
- 应用符合 MCP 安全原则的安全最佳实践
- 将 MCP 集成到企业 AI 系统和框架中
- 优化生产环境中的性能和可靠性

## 课程与示例项目

| 链接 | 标题 | 描述 |
|------|-------|-------------|
| [5.1 Integration with Azure](./mcp-integration/README.md) | 与 Azure 集成 | 学习如何将 MCP 服务器集成到 Azure |
| [5.2 Multi modal sample](./mcp-multi-modality/README.md) | MCP 多模态示例 | 音频、图像及多模态响应示例 |
| [5.3 MCP OAuth2 sample](../../../05-AdvancedTopics/mcp-oauth2-demo) | MCP OAuth2 演示 | 基于 Spring Boot 的最小应用展示 MCP OAuth2，既作为授权服务器也作为资源服务器。演示安全令牌颁发、受保护端点、Azure 容器应用部署及 API 管理集成。 |
| [5.4 Root Contexts](./mcp-root-contexts/README.md) | 根上下文 | 了解根上下文及其实现方法 |
| [5.5 Routing](./mcp-routing/README.md) | 路由 | 了解不同类型的路由 |
| [5.6 Sampling](./mcp-sampling/README.md) | 采样 | 学习采样操作 |
| [5.7 Scaling](./mcp-scaling/README.md) | 可扩展性 | 了解扩展机制 |
| [5.8 Security](./mcp-security/README.md) | 安全 | 保护您的 MCP 服务器 |
| [5.9 Web Search sample](./web-search-mcp/README.md) | Web 搜索 MCP | Python MCP 服务器和客户端结合 SerpAPI，实现实时网页、新闻、产品搜索与问答。展示多工具协作、外部 API 集成及健壮错误处理。 |
| [5.10 Realtime Streaming](./mcp-realtimestreaming/README.md) | 流式传输 | 实时数据流已成为当今数据驱动世界的关键，业务与应用需即时访问信息以做出及时决策。 |
| [5.11 Realtime Web Search](./mcp-realtimesearch/README.md) | 实时网页搜索 | MCP 如何通过为 AI 模型、搜索引擎和应用提供标准化的上下文管理转变实时网页搜索。 |
| [5.12  Entra ID Authentication for Model Context Protocol Servers](./mcp-security-entra/README.md) | Entra ID 认证 | Microsoft Entra ID 提供强大的基于云的身份和访问管理解决方案，确保只有授权用户和应用程序能够与您的 MCP 服务器交互。 |
| [5.13 Azure AI Foundry Agent Integration](./mcp-foundry-agent-integration/README.md) | Azure AI Foundry 集成 | 学习如何将模型上下文协议服务器与 Azure AI Foundry 代理集成，实现强大工具编排及企业 AI 能力，支持标准化外部数据源连接。 |
| [5.14 Context Engineering](./mcp-contextengineering/README.md) | 上下文工程 | MCP 服务器上下文工程技术的未来机遇，包括上下文优化、动态上下文管理及 MCP 框架内有效提示工程策略。 |
| [5.15 MCP Custom Transport](./mcp-transport/README.md) | 自定义传输 | 学习针对特定 MCP 通信场景实现自定义传输机制。 |
| [5.16 Protocol Features Deep Dive](./mcp-protocol-features/README.md) | 协议特性 | 掌握高级协议功能，包括进度通知、请求取消、资源模板及错误处理模式。 |
| [5.17 Adversarial Multi-Agent Reasoning](./mcp-adversarial-agents/README.md) | 对抗性代理 | 使用两个持对立立场的代理，共享单一 MCP 工具集，通过结构化辩论捕捉幻觉、暴露边缘案例并生成更准确的输出。 |

> **MCP 规范 2025-11-25 新增**：规范现包含对<strong>任务</strong>（带进度追踪的长时间操作）、<strong>工具注释</strong>（关于工具行为的元数据以保障安全）、**URL 模式启发**（请求客户端特定 URL 内容）及增强的<strong>根</strong>（用于工作区上下文管理）的实验支持。详细信息请参阅 [MCP 规范更新日志](https://spec.modelcontextprotocol.io/)。

## 附加参考资料

有关高级 MCP 主题的最新信息，请参阅：  
- [MCP 文档](https://modelcontextprotocol.io/)  
- [MCP 规范（2025-11-25）](https://spec.modelcontextprotocol.io/specification/2025-11-25/)  
- [GitHub 仓库](https://github.com/modelcontextprotocol)  
- [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) - 安全风险与缓解措施  
- [MCP 安全峰会研讨会（Sherpa）](https://azure-samples.github.io/sherpa/) - 实操安全培训

## 关键要点

- 多模态 MCP 实现拓展了 AI 的文本处理能力
- 可扩展性是企业部署的关键，可通过横向和纵向扩展实现
- 全面安全措施保护数据并确保正确的访问控制
- 与 Azure OpenAI 和 Microsoft AI Foundry 等平台的企业集成增强 MCP 功能
- 优化架构和资源管理有助于高级 MCP 实现

## 练习

为特定用例设计企业级 MCP 实现：

1. 确定用例的多模态需求  
2. 概述保护敏感数据所需的安全控制措施  
3. 设计能够应对不同负载的可扩展架构  
4. 规划与企业 AI 系统的集成点  
5. 记录潜在性能瓶颈及缓解策略

## 额外资源

- [Azure OpenAI 文档](https://learn.microsoft.com/en-us/azure/ai-services/openai/)  
- [Microsoft AI Foundry 文档](https://learn.microsoft.com/en-us/ai-services/)

---

## 下一步

开始探索本模块中的课程，首课为：[5.1 MCP Integration](./mcp-integration/README.md)

完成本模块后，继续学习：[第6模块：社区贡献](../06-CommunityContributions/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文档是使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译的。虽然我们努力追求准确性，但请注意自动翻译可能包含错误或不准确之处。应以原始语言的原始文档为权威来源。对于关键信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->