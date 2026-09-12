# 使用 stdio 传输的 MCP 服务器

> **⚠️ 重要更新**：自 MCP 规范 2025-06-18 起，独立的 SSE（Server-Sent Events）传输已被<strong>弃用</strong>，并由“可流式 HTTP”传输取代。当前 MCP 规范定义了两种主要的传输机制：
> 1. **stdio** - 标准输入/输出（推荐用于本地服务器）
> 2. **可流式 HTTP** - 用于可能在内部使用 SSE 的远程服务器
>
> 本课程已更新，重点讲解<strong>stdio 传输</strong>，这是大多数 MCP 服务器实现的推荐方式。

stdio 传输允许 MCP 服务器通过标准输入和输出流与客户端通信。这是当前 MCP 规范中最常用且推荐的传输机制，提供了一种简单高效的方式来构建易于与各种客户端应用程序集成的 MCP 服务器。

## 概览

本课程介绍如何使用 stdio 传输构建和使用 MCP 服务器。

## 学习目标

课程结束后，您将能够：

- 使用 stdio 传输构建 MCP 服务器。
- 使用 Inspector 调试 MCP 服务器。
- 在 Visual Studio Code 中使用 MCP 服务器。
- 理解当前 MCP 传输机制及为何推荐使用 stdio。


## stdio 传输 - 工作原理

stdio 传输是 MCP 规范
`2026-07-28` 中的两种标准传输之一。其工作方式如下：

- <strong>简单通信</strong>：服务器从标准输入（`stdin`）读取 JSON-RPC 消息，并向标准输出（`stdout`）发送消息。
- <strong>基于进程</strong>：客户端将 MCP 服务器作为子进程启动。
- <strong>消息格式</strong>：消息是单独的 JSON-RPC 请求、通知或响应，以换行符分隔。
- <strong>日志记录</strong>：服务器可向标准错误（`stderr`）写入 UTF-8 字符串以进行日志记录。

### 主要要求：
- 消息必须由换行符分隔，且不得包含嵌入的换行符
- 服务器不得向 `stdout` 写入非有效 MCP 消息内容
- 客户端不得向服务器的 `stdin` 写入非有效 MCP 消息内容

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

上述代码中：

- 我们从 MCP SDK 中导入了 `Server` 类和 `StdioServerTransport`
- 创建了一个具有基本配置和功能的服务器实例
- 创建了 `StdioServerTransport` 实例并将服务器连接到它，实现通过 stdin/stdout 通信

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

以上代码中我们：

- 使用 MCP SDK 创建服务器实例
- 用装饰器定义工具
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
- 实现和调试更简单

## 练习：创建 stdio 服务器

创建服务器时，我们需要记住两点：

- 我们需要使用 Web 服务器来暴露连接和消息端点。
## 实验：创建一个简单的 MCP stdio 服务器

本实验中，我们将使用推荐的 stdio 传输创建一个简单的 MCP 服务器。该服务器将暴露供客户端使用标准 Model Context Protocol 调用的工具。

### 先决条件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 对异步编程有基本了解

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

## 与弃用的 SSE 方法的关键区别

**Stdio 传输（当前标准）：**
- 简单的子进程模型 - 客户端启动服务器作为子进程
- 通过 stdin/stdout 使用 JSON-RPC 消息通信
- 无需设置 HTTP 服务器
- 性能和安全性更佳
- 更易于调试和开发

**SSE 传输（自 MCP 2025-06-18 起弃用）：**
- 需要带有 SSE 端点的 HTTP 服务器
- 需要更复杂的 Web 服务器基础设施
- HTTP 端点有额外的安全考量
- 已被用于 Web 场景的可流式 HTTP 取代

### 使用 stdio 传输创建服务器

创建 stdio 服务器，我们需要：

1. <strong>导入所需库</strong> - 需要 MCP 服务器组件和 stdio 传输
2. <strong>创建服务器实例</strong> - 定义服务器及其能力
3. <strong>定义工具</strong> - 添加要暴露的功能
4. <strong>设置传输</strong> - 配置 stdio 通信
5. <strong>运行服务器</strong> - 启动服务器并处理消息

让我们一步步构建：

### 第 1 步：创建基础 stdio 服务器

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

### 第 2 步：添加更多工具

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

### 第 3 步：运行服务器

将代码保存为 `server.py`，然后从命令行运行：

```bash
python server.py
```

服务器将启动并等待来自 stdin 的输入。它通过 stdio 传输使用 JSON-RPC 消息通信。

### 第 4 步：使用 Inspector 测试

您可以使用 MCP Inspector 测试您的服务器：

1. 安装 Inspector：`npx @modelcontextprotocol/inspector`
2. 运行 Inspector 并指向您的服务器
3. 测试您创建的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 调试您的 stdio 服务器

### 使用 MCP Inspector

MCP Inspector 是调试和测试 MCP 服务器的有价值工具。以下是如何与您的 stdio 服务器一起使用它：

1. **安装 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **运行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>测试服务器</strong>：Inspector 提供一个 Web 界面，您可以在其中：
   - 查看服务器能力
   - 使用不同参数测试工具
   - 监视 JSON-RPC 消息
   - 调试连接问题

### 使用 VS Code

您也可以直接在 VS Code 中调试 MCP 服务器：

1. 在 `.vscode/launch.json` 中创建启动配置：
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

### 常见调试技巧

- 使用 `stderr` 进行日志记录 - 永远不要向 `stdout` 写入内容，因为它保留给 MCP 消息
- 确保所有 JSON-RPC 消息均以换行符分隔
- 先用简单工具测试，再添加复杂功能
- 使用 Inspector 验证消息格式

## 在 VS Code 中使用您的 stdio 服务器

构建完 MCP stdio 服务器后，您可以将其集成到 VS Code 中，用于 Claude 或其他兼容 MCP 的客户端。

### 配置

1. **创建 MCP 配置文件**，路径为 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

3. <strong>测试连接</strong>：开始与 Claude 对话并尝试使用服务器的工具：
   - “你能用问候工具向我打个招呼吗？”
   - “计算 15 和 27 的和”
   - “服务器信息是什么？”

### TypeScript stdio 服务器示例

以下是完整的 TypeScript 示例，供参考：

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

- 使用当前推荐的<strong>stdio 传输</strong>构建 MCP 服务器
- 理解为何 SSE 传输被弃用，转而推荐 stdio 和可流式 HTTP
- 创建 MCP 客户端可以调用的工具
- 使用 MCP Inspector 调试服务器
- 将 stdio 服务器与 VS Code 和 Claude 集成

stdio 传输相比弃用的 SSE 方法，提供了更简洁、更安全且性能更佳的 MCP 服务器构建方式。自 2025-06-18 规范起，它是大多数 MCP 服务器实现的推荐传输。


### .NET

1. 我们先创建一些工具，为此将在文件 *Tools.cs* 中写入以下内容：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 练习：测试您的 stdio 服务器

现在您已经构建了 stdio 服务器，接下来测试它以确保正常运行。

### 先决条件

1. 确保已安装 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 您的服务器代码应已保存（例如 `server.py`）

### 使用 Inspector 测试

1. **使用您的服务器启动 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. <strong>打开网页界面</strong>：Inspector 会打开浏览器窗口，显示您的服务器能力。

3. <strong>测试工具</strong>： 
   - 用不同名称尝试 `get_greeting` 工具
   - 用各种数字测试 `calculate_sum` 工具
   - 调用 `get_server_info` 工具查看服务器元数据

4. <strong>监控通信</strong>：Inspector 展示客户端与服务器之间交换的 JSON-RPC 消息。

### 您应该看到的内容

服务器正确启动时，您将看到：
- Inspector 中列出的服务器能力
- 可用于测试的工具
- 成功的 JSON-RPC 消息交换
- 工具响应在界面中显示

### 常见问题及解决方案

**服务器无法启动：**
- 检查是否安装所有依赖项：`pip install mcp`
- 验证 Python 语法和缩进
- 查找控制台错误信息

**工具未显示：**
- 确保存在 `@server.tool()` 装饰器
- 确认工具函数定义在 `main()` 前
- 确认服务器配置正确

**连接问题：**
- 确保服务器正确使用 stdio 传输
- 检查是否有其他进程干扰
- 验证 Inspector 命令语法

## 作业

尝试为服务器添加更多功能。请访问 [此页面](https://api.chucknorris.io/) 以添加调用 API 的工具。服务器长什么样，由你决定。玩得开心 :)
## 解决方案

[解决方案](./solution/README.md) 这里有一份带有可运行代码的可能解决方案。

## 关键要点

本章关键要点如下：

- stdio 传输是本地 MCP 服务器的推荐机制。
- stdio 传输允许 MCP 服务器和客户端通过标准输入输出流无缝通信。
- 您可以直接使用 Inspector 和 Visual Studio Code 消费 stdio 服务器，使调试和集成更简单。

## 示例 

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python) 

## 额外资源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下来做什么

## 后续步骤

既然您已经学习了如何使用 stdio 传输构建 MCP 服务器，可以探索更高级的主题：

- <strong>下一步</strong>：[MCP HTTP 流（可流式 HTTP）](../06-http-streaming/README.md) - 了解远程服务器使用的另一种支持传输机制
- <strong>高级</strong>：[MCP 安全最佳实践](../../02-Security/README.md) - 在您的 MCP 服务器中实施安全措施
- <strong>生产</strong>：[部署策略](../09-deployment/README.md) - 部署您的服务器以供生产使用

## 额外资源

- [MCP 规范 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - 当前规范
- [MCP SDK 文档](https://github.com/modelcontextprotocol/sdk) - 各语言 SDK 参考
- [社区示例](../../06-CommunityContributions/README.md) - 社区提供的更多服务器示例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->