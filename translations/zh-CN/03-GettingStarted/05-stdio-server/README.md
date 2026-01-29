# 使用 stdio 传输的 MCP 服务器

> **⚠️ 重要更新**：从 MCP 规范 2025-06-18 开始，独立的 SSE（服务器发送事件）传输已被**弃用**，并由“可流式 HTTP”传输取代。目前的 MCP 规范定义了两种主要的传输机制：
> 1. **stdio** - 标准输入/输出（推荐用于本地服务器）
> 2. **可流式 HTTP** - 用于可能在内部使用 SSE 的远程服务器
>
> 本课程已更新为重点介绍**stdio 传输**，这是大多数 MCP 服务器实现的推荐方法。

stdio 传输允许 MCP 服务器通过标准输入和输出流与客户端通信。这是当前 MCP 规范中最常用且推荐的传输机制，提供了一种简单高效的方式来构建 MCP 服务器，并能轻松与各种客户端应用集成。

## 概述

本课程将介绍如何使用 stdio 传输构建和使用 MCP 服务器。

## 学习目标

完成本课程后，您将能够：

- 使用 stdio 传输构建 MCP 服务器。
- 使用 Inspector 调试 MCP 服务器。
- 在 Visual Studio Code 中使用 MCP 服务器。
- 理解当前 MCP 传输机制以及推荐使用 stdio 的原因。

## stdio 传输 - 工作原理

stdio 传输是当前 MCP 规范（2025-06-18）支持的两种传输类型之一。其工作原理如下：

- **简单通信**：服务器从标准输入（`stdin`）读取 JSON-RPC 消息，并将消息发送到标准输出（`stdout`）。
- **基于进程**：客户端将 MCP 服务器作为子进程启动。
- **消息格式**：消息是单独的 JSON-RPC 请求、通知或响应，以换行符分隔。
- **日志记录**：服务器可以将 UTF-8 字符串写入标准错误（`stderr`）用于日志记录。

### 关键要求：
- 消息必须以换行符分隔，且不得包含嵌入的换行符。
- 服务器不得向 `stdout` 写入任何非 MCP 消息的内容。
- 客户端不得向服务器的 `stdin` 写入任何非 MCP 消息的内容。

### TypeScript 示例

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

- 我们从 MCP SDK 中导入了 `Server` 类和 `StdioServerTransport`。
- 我们创建了一个具有基本配置和功能的服务器实例。

### Python 示例

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

在上述代码中，我们：

- 使用 MCP SDK 创建了一个服务器实例。
- 使用装饰器定义了工具。
- 使用 `stdio_server` 上下文管理器处理传输。

### .NET 示例

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

与 SSE 的主要区别在于 stdio 服务器：

- 不需要设置 Web 服务器或 HTTP 端点。
- 由客户端作为子进程启动。
- 通过 stdin/stdout 流通信。
- 更易于实现和调试。

## 练习：创建一个 stdio 服务器

要创建我们的服务器，需要注意以下两点：

- 我们需要使用 Web 服务器来公开连接和消息的端点。

## 实验：创建一个简单的 MCP stdio 服务器

在本实验中，我们将使用推荐的 stdio 传输创建一个简单的 MCP 服务器。此服务器将公开客户端可以调用的工具，使用标准的模型上下文协议。

### 前置条件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 对异步编程的基本了解

让我们开始创建第一个 MCP stdio 服务器：

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## 与已弃用的 SSE 方法的主要区别

**Stdio 传输（当前标准）：**
- 简单的子进程模型 - 客户端将服务器作为子进程启动。
- 使用 JSON-RPC 消息通过 stdin/stdout 通信。
- 不需要设置 HTTP 服务器。
- 性能和安全性更高。
- 更易于调试和开发。

**SSE 传输（自 MCP 2025-06-18 起弃用）：**
- 需要带有 SSE 端点的 HTTP 服务器。
- 需要更复杂的 Web 服务器基础设施设置。
- 对 HTTP 端点有额外的安全性考虑。
- 现已被可流式 HTTP 替代，用于基于 Web 的场景。

### 使用 stdio 传输创建服务器

要创建 stdio 服务器，我们需要：

1. **导入所需的库** - 我们需要 MCP 服务器组件和 stdio 传输。
2. **创建服务器实例** - 定义服务器及其功能。
3. **定义工具** - 添加我们希望公开的功能。
4. **设置传输** - 配置 stdio 通信。
5. **运行服务器** - 启动服务器并处理消息。

让我们逐步构建：

### 第一步：创建一个基本的 stdio 服务器

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### 第二步：添加更多工具

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

### 第三步：运行服务器

将代码保存为 `server.py`，并从命令行运行：

```bash
python server.py
```

服务器将启动并等待来自 stdin 的输入。它通过 stdio 传输使用 JSON-RPC 消息进行通信。

### 第四步：使用 Inspector 测试

您可以使用 MCP Inspector 测试您的服务器：

1. 安装 Inspector：`npx @modelcontextprotocol/inspector`
2. 运行 Inspector 并指向您的服务器。
3. 测试您创建的工具。

### .NET 示例

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## 调试您的 stdio 服务器

### 使用 MCP Inspector

MCP Inspector 是调试和测试 MCP 服务器的有力工具。以下是如何将其与您的 stdio 服务器一起使用：

1. **安装 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **运行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **测试您的服务器**：Inspector 提供了一个 Web 界面，您可以：
   - 查看服务器功能。
   - 使用不同参数测试工具。
   - 监控 JSON-RPC 消息。
   - 调试连接问题。

### 使用 VS Code

您还可以直接在 VS Code 中调试您的 MCP 服务器：

1. 在 `.vscode/launch.json` 中创建一个启动配置：
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

2. 在服务器代码中设置断点。
3. 运行调试器并使用 Inspector 测试。

### 常见调试提示

- 使用 `stderr` 记录日志 - 不要向 `stdout` 写入任何内容，因为它保留用于 MCP 消息。
- 确保所有 JSON-RPC 消息都以换行符分隔。
- 先测试简单工具，再添加复杂功能。
- 使用 Inspector 验证消息格式。

## 在 VS Code 中使用您的 stdio 服务器

构建 MCP stdio 服务器后，您可以将其集成到 VS Code 中，与 Claude 或其他兼容 MCP 的客户端一起使用。

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

3. **测试连接**：与 Claude 开始对话并尝试使用您的服务器工具：
   - “你能用问候工具向我问好吗？”
   - “计算 15 和 27 的和。”
   - “服务器信息是什么？”

### TypeScript stdio 服务器示例

以下是一个完整的 TypeScript 示例供参考：

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

// Add tools
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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## 总结

在本更新课程中，您学习了如何：

- 使用当前推荐的 **stdio 传输** 构建 MCP 服务器。
- 理解为什么 SSE 传输被弃用，转而推荐使用 stdio 和可流式 HTTP。
- 创建可供 MCP 客户端调用的工具。
- 使用 MCP Inspector 调试您的服务器。
- 将您的 stdio 服务器集成到 VS Code 和 Claude 中。

与已弃用的 SSE 方法相比，stdio 传输提供了一种更简单、更安全且性能更高的方式来构建 MCP 服务器。根据 2025-06-18 规范，这是大多数 MCP 服务器实现的推荐传输方式。

### .NET 示例

1. 首先创建一些工具，为此我们将创建一个名为 *Tools.cs* 的文件，内容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 练习：测试您的 stdio 服务器

现在您已经构建了 stdio 服务器，让我们测试它以确保其正常工作。

### 前置条件

1. 确保已安装 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 确保您的服务器代码已保存（例如，保存为 `server.py`）。

### 使用 Inspector 测试

1. **使用您的服务器启动 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打开 Web 界面**：Inspector 将打开一个浏览器窗口，显示您的服务器功能。

3. **测试工具**：
   - 使用不同的名称尝试 `get_greeting` 工具。
   - 使用各种数字测试 `calculate_sum` 工具。
   - 调用 `get_server_info` 工具查看服务器元数据。

4. **监控通信**：Inspector 显示客户端和服务器之间交换的 JSON-RPC 消息。

### 您应该看到的内容

当您的服务器正确启动时，您应该看到：
- Inspector 中列出的服务器功能。
- 可供测试的工具。
- 成功的 JSON-RPC 消息交换。
- 界面中显示的工具响应。

### 常见问题及解决方案

**服务器无法启动：**
- 检查是否安装了所有依赖项：`pip install mcp`
- 验证 Python 语法和缩进。
- 查看控制台中的错误消息。

**工具未显示：**
- 确保存在 `@server.tool()` 装饰器。
- 检查工具函数是否在 `main()` 之前定义。
- 验证服务器是否正确配置。

**连接问题：**
- 确保服务器正确使用 stdio 传输。
- 检查是否有其他进程干扰。
- 验证 Inspector 命令语法。

## 作业

尝试为您的服务器添加更多功能。例如，访问 [这个页面](https://api.chucknorris.io/) 添加一个调用 API 的工具。您可以自由决定服务器的功能。玩得开心 :)

## 解决方案

[解决方案](./solution/README.md) 提供了一个可能的解决方案和工作代码。

## 关键要点

本章的关键要点如下：

- stdio 传输是本地 MCP 服务器的推荐机制。
- stdio 传输允许 MCP 服务器和客户端通过标准输入和输出流无缝通信。
- 您可以直接使用 Inspector 和 Visual Studio Code 消费 stdio 服务器，使调试和集成变得简单。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python) 

## 其他资源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 接下来

## 下一步

现在您已经学习了如何使用 stdio 传输构建 MCP 服务器，可以探索更高级的主题：

- **下一步**：[MCP 的 HTTP 流式传输（可流式 HTTP）](../06-http-streaming/README.md) - 了解远程服务器支持的另一种传输机制。
- **高级**：[MCP 安全最佳实践](../../02-Security/README.md) - 在 MCP 服务器中实现安全性。
- **生产环境**：[部署策略](../09-deployment/README.md) - 将您的服务器部署到生产环境。

## 其他资源

- [MCP 规范 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方规范。
- [MCP SDK 文档](https://github.com/modelcontextprotocol/sdk) - 各种语言的 SDK 参考。
- [社区示例](../../06-CommunityContributions/README.md) - 更多来自社区的服务器示例。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。