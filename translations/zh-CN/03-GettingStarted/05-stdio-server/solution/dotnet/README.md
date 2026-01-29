# MCP stdio 服务器 - .NET 解决方案

> **⚠️ 重要**：此解决方案已更新为使用 **stdio 传输**，这是 MCP 规范 2025-06-18 推荐的方式。原有的 SSE 传输已被弃用。

## 概述

此 .NET 解决方案展示了如何使用当前的 stdio 传输构建 MCP 服务器。相比已弃用的 SSE 方法，stdio 传输更简单、更安全，并且性能更优。

## 前置条件

- .NET 9.0 SDK 或更高版本
- 基本了解 .NET 的依赖注入

## 设置说明

### 步骤 1：恢复依赖项

```bash
dotnet restore
```

### 步骤 2：构建项目

```bash
dotnet build
```

## 运行服务器

stdio 服务器的运行方式与旧的基于 HTTP 的服务器不同。它通过标准输入/输出（stdin/stdout）进行通信，而不是启动一个 Web 服务器：

```bash
dotnet run
```

**重要**：服务器看起来会“挂起”——这是正常现象！它正在等待从标准输入接收 JSON-RPC 消息。

## 测试服务器

### 方法 1：使用 MCP Inspector（推荐）

```bash
npx @modelcontextprotocol/inspector dotnet run
```

此操作将：
1. 将服务器作为子进程启动
2. 打开一个用于测试的 Web 界面
3. 允许您交互式测试所有服务器工具

### 方法 2：直接使用命令行测试

您也可以通过直接启动 Inspector 进行测试：

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### 可用工具

服务器提供以下工具：

- **AddNumbers(a, b)**：将两个数字相加
- **MultiplyNumbers(a, b)**：将两个数字相乘  
- **GetGreeting(name)**：生成个性化问候语
- **GetServerInfo()**：获取服务器信息

### 使用 Claude Desktop 测试

要在 Claude Desktop 中使用此服务器，请将以下配置添加到您的 `claude_desktop_config.json` 文件中：

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## 项目结构

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## 与 HTTP/SSE 的主要区别

**stdio 传输（当前）：**
- ✅ 设置更简单 - 无需 Web 服务器
- ✅ 更高的安全性 - 无 HTTP 端点
- ✅ 使用 `Host.CreateApplicationBuilder()` 替代 `WebApplication.CreateBuilder()`
- ✅ 使用 `WithStdioTransport()` 替代 `WithHttpTransport()`
- ✅ 控制台应用程序替代 Web 应用程序
- ✅ 性能更优

**HTTP/SSE 传输（已弃用）：**
- ❌ 需要 ASP.NET Core Web 服务器
- ❌ 需要设置 `app.MapMcp()` 路由
- ❌ 配置和依赖项更复杂
- ❌ 存在额外的安全性考量
- ❌ 已在 MCP 2025-06-18 中被弃用

## 开发功能

- **依赖注入**：全面支持服务和日志记录的 DI
- **结构化日志**：通过 `ILogger<T>` 向标准错误输出正确记录日志
- **工具属性**：使用 `[McpServerTool]` 属性清晰定义工具
- **异步支持**：所有工具支持异步操作
- **错误处理**：优雅的错误处理和日志记录

## 开发提示

- 使用 `ILogger` 进行日志记录（切勿直接写入标准输出）
- 在测试前使用 `dotnet build` 构建项目
- 使用 Inspector 进行可视化调试
- 所有日志记录会自动输出到标准错误
- 服务器会处理优雅的关闭信号

此解决方案遵循当前 MCP 规范，展示了使用 .NET 实现 stdio 传输的最佳实践。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。