# MCP stdio 服务器解决方案

> **⚠️ 重要**: 这些解决方案已更新为使用 **stdio 传输**，这是 MCP 规范 2025-06-18 推荐的方式。原有的 SSE（服务器发送事件）传输已被弃用。

以下是使用 stdio 传输构建 MCP 服务器的完整解决方案，涵盖不同的运行时环境：

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - 完整的 stdio 服务器实现
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - 基于 asyncio 的 Python stdio 服务器
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - 支持依赖注入的 .NET stdio 服务器

每个解决方案都展示了以下内容：
- 配置 stdio 传输
- 定义服务器工具
- 正确处理 JSON-RPC 消息
- 与 MCP 客户端（如 Claude）的集成

所有解决方案均遵循当前的 MCP 规范，并使用推荐的 stdio 传输，以实现最佳性能和安全性。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。