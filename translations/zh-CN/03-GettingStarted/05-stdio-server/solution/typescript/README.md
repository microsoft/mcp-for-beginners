# MCP stdio 服务器 - TypeScript 解决方案

> **⚠️ 重要**: 此解决方案已更新为使用 **stdio 传输**，根据 MCP 规范 2025-06-18 的推荐。原来的 SSE 传输已被弃用。

## 概述

此 TypeScript 解决方案展示了如何使用当前的 stdio 传输构建 MCP 服务器。相比已弃用的 SSE 方法，stdio 传输更简单、更安全，并且性能更优。

## 前置条件

- Node.js 18 或更高版本
- npm 或 yarn 包管理工具

## 设置说明

### 步骤 1: 安装依赖

```bash
npm install
```

### 步骤 2: 构建项目

```bash
npm run build
```

## 运行服务器

stdio 服务器的运行方式与旧的 SSE 服务器不同。它不启动一个 Web 服务器，而是通过 stdin/stdout 进行通信：

```bash
npm start
```

**重要**: 服务器看起来会像是挂起了——这是正常现象！它正在等待来自 stdin 的 JSON-RPC 消息。

## 测试服务器

### 方法 1: 使用 MCP Inspector（推荐）

```bash
npm run inspector
```

这将会：
1. 将您的服务器作为子进程启动
2. 打开一个用于测试的 Web 界面
3. 允许您交互式测试所有服务器工具

### 方法 2: 直接使用命令行测试

您也可以通过直接启动 Inspector 进行测试：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### 可用工具

服务器提供以下工具：

- **add(a, b)**: 将两个数字相加
- **multiply(a, b)**: 将两个数字相乘  
- **get_greeting(name)**: 生成个性化问候语
- **get_server_info()**: 获取服务器信息

### 使用 Claude Desktop 进行测试

要在 Claude Desktop 中使用此服务器，请将以下配置添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## 项目结构

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## 与 SSE 的关键区别

**stdio 传输（当前）：**
- ✅ 设置更简单 - 不需要 HTTP 服务器
- ✅ 更高的安全性 - 无需 HTTP 端点
- ✅ 基于子进程的通信
- ✅ 通过 stdin/stdout 使用 JSON-RPC
- ✅ 性能更优

**SSE 传输（已弃用）：**
- ❌ 需要设置 Express 服务器
- ❌ 需要复杂的路由和会话管理
- ❌ 更多依赖项（Express、HTTP 处理）
- ❌ 额外的安全性考虑
- ❌ 在 MCP 2025-06-18 中已被弃用

## 开发提示

- 使用 `console.error()` 进行日志记录（不要使用 `console.log()`，因为它会写入 stdout）
- 在测试之前使用 `npm run build` 进行构建
- 使用 Inspector 进行可视化调试
- 确保所有 JSON 消息格式正确
- 服务器会在接收到 SIGINT/SIGTERM 时自动处理优雅关闭

此解决方案遵循当前 MCP 规范，并展示了使用 TypeScript 实现 stdio 传输的最佳实践。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。