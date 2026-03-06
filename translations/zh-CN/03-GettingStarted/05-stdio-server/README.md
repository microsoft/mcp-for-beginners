# 使用 stdio 传输的 MCP 服务器

> **⚠️ 重要更新**：自 MCP 规范 2025-06-18 起，独立的 SSE（服务端事件）传输已被 **废弃**，并被“可流 HTTP（Streamable HTTP）”传输所取代。当前的 MCP 规范定义了两种主要传输机制：
> 1. **stdio** - 标准输入/输出（推荐用于本地服务器）
> 2. **可流 HTTP** - 用于可能在内部使用 SSE 的远程服务器
>
> 本课已更新为重点介绍 **stdio 传输**，这是大多数 MCP 服务器实现的推荐方式。

stdio 传输允许 MCP 服务器通过标准输入和输出流与客户端通信。这是在当前 MCP 规范中最常用且推荐的传输机制，提供了一种简单有效的方式来构建 MCP 服务器，可以轻松集成各种客户端应用程序。

## 概述

本课涵盖如何使用 stdio 传输构建和使用 MCP 服务器。

## 学习目标

完成本课后，您将能够：

- 使用 stdio 传输构建 MCP 服务器。
- 使用 Inspector 调试 MCP 服务器。
- 使用 Visual Studio Code 调用 MCP 服务器。
- 了解当前的 MCP 传输机制及为何推荐 stdio。

## stdio 传输工作原理

stdio 传输是当前 MCP 规范（2025-06-18）支持的两种传输类型之一。其工作原理如下：

- **简单通信**：服务器从标准输入（`stdin`）读取 JSON-RPC 消息，并通过标准输出（`stdout`）发送消息。
- **基于进程**：客户端作为子进程启动 MCP 服务器。
- **消息格式**：消息是单独的 JSON-RPC 请求、通知或响应，以换行符分隔。
- **日志记录**：服务器可向标准错误输出（`stderr`）写入 UTF-8 字符串以作日志记录。

### 关键要求：
- 消息必须以换行符分隔，且不得包含嵌入式换行符
- 服务器不得向 `stdout` 写入任何非有效 MCP 消息的内容
- 客户端不得向服务器的 `stdin` 写入任何非有效 MCP 消息的内容

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

在上述代码中：

- 我们从 MCP SDK 导入了 `Server` 类和 `StdioServerTransport`
- 使用基本配置和能力创建了服务器实例

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 创建服务器实例
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

在上述代码中我们：

- 使用 MCP SDK 创建了服务器实例
- 使用装饰器定义了工具
- 使用 stdio_server 上下文管理器处理传输

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

与 SSE 的主要区别在于 stdio 服务器：

- 不需要 Web 服务器设置或 HTTP 端点
- 由客户端作为子进程启动
- 通过 stdin/stdout 流通信
- 更简单实现与调试

## 练习：创建 stdio 服务器

要创建服务器，我们需要牢记两点：

- 需要使用 Web 服务器公开用于连接和消息的端点。

## 实验：创建简单 MCP stdio 服务器

本实验中，我们将使用推荐的 stdio 传输创建一个简单的 MCP 服务器。服务器将公开客户端可通过标准 Model Context Protocol 调用的工具。

### 先决条件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 异步编程基础知识

让我们开始创建第一个 MCP stdio 服务器：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建服务器
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # 使用 stdio 传输
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 与已废弃 SSE 方法的关键差异

**Stdio 传输（当前标准）：**
- 简单的子进程模型——客户端以子进程形式启动服务器
- 通过 stdin/stdout 使用 JSON-RPC 消息通信
- 无需 HTTP 服务器设置
- 性能更优，安全性更高
- 更容易调试和开发

**SSE 传输（自 MCP 2025-06-18 起废弃）：**
- 需要带 SSE 端点的 HTTP 服务器
- 配置更复杂，需要 web 服务器基础设施
- HTTP 端点的额外安全考虑
- 现已由可流 HTTP 替代，适用于基于 Web 的场景

### 使用 stdio 传输创建服务器

创建 stdio 服务器需要：

1. **导入所需库** - 需要 MCP 服务器组件和 stdio 传输
2. **创建服务器实例** - 定义服务器及其能力
3. **定义工具** - 添加希望公开的功能
4. **设置传输** - 配置 stdio 通信
5. **运行服务器** - 启动服务器并处理消息

让我们逐步构建：

### 步骤 1：创建基本 stdio 服务器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# 配置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建服务器
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### 步骤 2：添加更多工具

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### 步骤 3：运行服务器

将代码保存为 `server.py`，在命令行运行：

```bash
python server.py
```

服务器启动后将等待来自 stdin 的输入。它通过 stdio 传输使用 JSON-RPC 消息通信。

### 步骤 4：使用 Inspector 测试

您可以使用 MCP Inspector 测试服务器：

1. 安装 Inspector：`npx @modelcontextprotocol/inspector`
2. 运行 Inspector 并连接到服务器
3. 测试您创建的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## 调试 stdio 服务器

### 使用 MCP Inspector

MCP Inspector 是调试和测试 MCP 服务器的有用工具。以下是如何用它调试 stdio 服务器：

1. **安装 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **运行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **测试服务器**：Inspector 提供了一个 Web 界面，您可以：
   - 查看服务器能力
   - 使用不同参数测试工具
   - 监控 JSON-RPC 消息
   - 调试连接问题

### 使用 VS Code

您也可以直接在 VS Code 中调试 MCP 服务器：

1. 在 `.vscode/launch.json` 创建启动配置：
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. 在服务器代码中设置断点
3. 运行调试器并使用 Inspector 测试

### 常见调试提示

- 使用 `stderr` 进行日志记录——切勿写入 `stdout`，因其保留给 MCP 消息
- 确保所有 JSON-RPC 消息均由换行符分隔
- 初始测试时使用简单的工具，逐步添加复杂功能
- 使用 Inspector 核验消息格式

## 在 VS Code 中调用 stdio 服务器

构建完成 MCP stdio 服务器后，您可以将其集成到 VS Code 中，以便与 Claude 或其他兼容 MCP 的客户端一起使用。

### 配置

1. 在 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）创建 MCP 配置文件：

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **重启 Claude**：关闭并重新打开 Claude 以加载新的服务器配置。

3. **测试连接**：开始与 Claude 的对话并尝试使用服务器工具：
   - “你能用问候工具向我问好吗？”
   - “计算 15 和 27 的和”
   - “服务器信息是什么？”

### TypeScript stdio 服务器示例

以下是完整的 TypeScript 参考示例：

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// 添加工具
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio 服务器示例

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 总结

在本更新课程中，您学会了：

- 使用当前推荐的 **stdio 传输** 构建 MCP 服务器
- 了解为何 SSE 传输被废弃，转向 stdio 和可流 HTTP
- 创建可以被 MCP 客户端调用的工具
- 使用 MCP Inspector 调试服务器
- 将 stdio 服务器集成到 VS Code 和 Claude 中

与已废弃的 SSE 方法相比，stdio 传输提供了更简单、更安全且性能更优的 MCP 服务器构建方式。根据 2025-06-18 规范，它是大多数 MCP 服务器实现的推荐传输。

### .NET

1. 让我们先创建一些工具，为此将创建一个名为 *Tools.cs* 的文件，内容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 练习：测试你的 stdio 服务器

现在您已经构建了 stdio 服务器，接下来测试确保其运行正常。

### 先决条件

1. 确保已安装 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 服务器代码已保存（例如保存为 `server.py`）

### 使用 Inspector 测试

1. **与服务器一起启动 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打开 Web 界面**：Inspector 将打开浏览器窗口显示服务器能力。

3. **测试工具**：
   - 使用不同名字尝试 `get_greeting` 工具
   - 使用各种数字测试 `calculate_sum` 工具
   - 调用 `get_server_info` 查看服务器元信息

4. **监控通信**：Inspector 会显示客户端和服务器间交换的 JSON-RPC 消息。

### 您应该看到的内容

当服务器启动正确时，您应看到：
- Inspector 中列出的服务器能力
- 可供测试的工具
- 成功的 JSON-RPC 消息交换
- 界面中显示的工具响应

### 常见问题及解决方案

**服务器无法启动：**
- 检查所有依赖库是否安装：`pip install mcp`
- 验证 Python 语法和缩进
- 检查控制台中的错误信息

**工具未显示：**
- 确保存在 `@server.tool()` 装饰器
- 确保工具函数定义在 `main()` 之前
- 验证服务器是否正确配置

**连接问题：**
- 确认服务器正确使用 stdio 传输
- 确保无其他进程干扰
- 检查 Inspector 命令语法

## 作业

尝试扩展服务器功能。参考[此页面](https://api.chucknorris.io/)，例如添加调用 API 的工具。你决定服务器该如何表现。玩得开心 :)

## 解决方案

[解决方案](./solution/README.md) 这是一个工作示例代码的可能解决方案。

## 关键要点

本章关键要点如下：

- stdio 传输是本地 MCP 服务器的推荐机制。
- stdio 传输允许 MCP 服务器和客户端通过标准输入输出流实现无缝通信。
- 你可以直接使用 Inspector 和 Visual Studio Code 调用 stdio 服务器，使调试和集成变得简单。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)

## 附加资源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下来

## 下一步

学会使用 stdio 传输构建 MCP 服务器后，你可以探索更高级的主题：

- **下一步**：[MCP 的 HTTP 流式传输（Streamable HTTP）](../06-http-streaming/README.md) - 了解远程服务器支持的另一传输机制
- **进阶**：[MCP 安全最佳实践](../../02-Security/README.md) - 在 MCP 服务器中实现安全
- **生产环境**：[部署策略](../09-deployment/README.md) - 将服务器部署到生产环境

## 附加资源

- [MCP 规范 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方规范
- [MCP SDK 文档](https://github.com/modelcontextprotocol/sdk) - 各语言 SDK 参考
- [社区示例](../../06-CommunityContributions/README.md) - 社区更多服务器示例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文档由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原文应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或曲解，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->