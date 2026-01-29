# 使用 Azure Content Safety 实现高级 MCP 安全

Azure Content Safety 提供了多种强大工具，可增强您的 MCP 实现的安全性：

## Prompt Shields

微软的 AI Prompt Shields 通过以下方式为防止直接和间接的提示注入攻击提供强有力的保护：

1. **高级检测**：利用机器学习识别内容中嵌入的恶意指令。
2. **聚焦处理**：转换输入文本，帮助 AI 系统区分有效指令和外部输入。
3. **分隔符和数据标记**：标记可信数据与不可信数据之间的边界。
4. **内容安全集成**：与 Azure AI Content Safety 协作，检测越狱尝试和有害内容。
5. **持续更新**：微软定期更新保护机制，应对新兴威胁。

## 在 MCP 中实现 Azure Content Safety

此方法提供多层保护：
- 处理前扫描输入
- 返回前验证输出
- 使用黑名单过滤已知有害模式
- 利用 Azure 持续更新的内容安全模型

## Azure Content Safety 资源

如需了解如何在 MCP 服务器中实现 Azure Content Safety，请参考以下官方资源：

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety 官方文档。
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - 了解如何防止提示注入攻击。
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - 内容安全的详细 API 参考。
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - 使用 C# 的快速入门指南。
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - 各种编程语言的客户端库。
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - 检测和防止越狱尝试的具体指导。
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - 有效实施内容安全的最佳实践。

如需更深入的实现细节，请参阅我们的[Azure Content Safety 实现指南](./azure-content-safety-implementation.md)。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。