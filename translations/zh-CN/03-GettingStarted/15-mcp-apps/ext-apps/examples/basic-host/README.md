# 示例：基础 Host

一个参考实现，展示如何构建连接 MCP 服务器并在安全沙箱中渲染工具 UI 的 MCP Host 应用。

此基础 Host 也可用于在本地开发期间测试 MCP 应用。

## 关键文件

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - 具有工具选择、参数输入和 iframe 管理的 React UI Host
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - 带有安全验证和双向消息中继的外层 iframe 代理
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - 核心逻辑：服务器连接、工具调用和 AppBridge 设置

## 入门

```bash
npm install
npm run start
# 打开 http://localhost:8080
```

默认情况下，Host 应用会尝试连接到 `http://localhost:3001/mcp` 的 MCP 服务器。你可以通过设置 `SERVERS` 环境变量为服务器 URL 的 JSON 数组来配置此行为：

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## 架构

此示例使用双 iframe 沙箱模式以实现安全的 UI 隔离：

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**为什么使用两个 iframe？**

- 外层 iframe 运行在不同的源（端口 8081），防止直接访问 Host
- 内层 iframe 通过 `srcdoc` 接收 HTML，并受沙箱属性限制
- 消息通过外层 iframe 流转，进行验证并实现双向中继

此架构确保即使工具 UI 代码是恶意的，也无法访问 Host 应用的 DOM、Cookie 或 JavaScript 上下文。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档由AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译。尽管我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用此翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->