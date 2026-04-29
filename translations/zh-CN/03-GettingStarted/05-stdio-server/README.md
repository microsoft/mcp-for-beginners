# 使用 stdio 传输的 MCP 服务器

> **⚠️ 重要更新**：自 MCP 规范 2025-06-18 起，独立的 SSE（服务器发送事件）传输已被<strong>弃用</strong>，并由“可流式 HTTP”传输取代。当前 MCP 规范定义了两种主要的传输机制：
> 1. **stdio** - 标准输入/输出（推荐用于本地服务器）
> 2. **可流式 HTTP** - 适用于可能内部使用 SSE 的远程服务器
>
> 本课已更新为重点介绍<strong>stdio 传输</strong>，这是大多数 MCP 服务器实现推荐的方式。

stdio 传输允许 MCP 服务器通过标准输入和输出流与客户端通信。这是当前 MCP 规范中最常用且推荐的传输机制，提供了一种简单高效的方式来构建 MCP 服务器，可轻松集成到各种客户端应用程序中。

## 概览

本课介绍如何使用 stdio 传输构建和使用 MCP 服务器。

## 学习目标

在本课结束时，你将能够：

- 使用 stdio 传输构建 MCP 服务器。
- 使用 Inspector 调试 MCP 服务器。
- 在 Visual Studio Code 中使用 MCP 服务器。
- 理解当前 MCP 的传输机制及为何推荐 stdio。

## stdio 传输 - 工作原理

stdio 传输是当前 MCP 规范（2025-06-18）支持的两种传输类型之一。工作原理如下：

- <strong>简单通信</strong>：服务器从标准输入 (`stdin`) 读取 JSON-RPC 消息，向标准输出 (`stdout`) 发送消息。
- <strong>基于进程</strong>：客户端将 MCP 服务器作为子进程启动。
- <strong>消息格式</strong>：消息为单独的 JSON-RPC 请求、通知或响应，用换行符分隔。
- <strong>日志记录</strong>：服务器可以将 UTF-8 字符串写入标准错误 (`stderr`) 用于日志记录。

### 关键要求：
- 消息必须以换行符分隔，且消息内部不得包含换行符
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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

在上述代码中：

- 我们从 MCP SDK 导入了 `Server` 类和 `StdioServerTransport`
- 创建了带有基本配置和功能的服务器实例
- 创建了 `StdioServerTransport` 实例并将服务器连接到该传输，实现通过 stdin/stdout 通信

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

- 使用 MCP SDK 创建服务器实例
- 使用装饰器定义工具
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

与 SSE 的主要区别是 stdio 服务器：

- 不需要 Web 服务器或 HTTP 端点
- 由客户端作为子进程启动
- 通过 stdin/stdout 流通信
- 实现和调试更简单

## 练习：创建 stdio 服务器

创建服务器时需牢记两点：

- 我们需要使用 Web 服务器来暴露连接和消息端点。
## 实验：创建一个简单的 MCP stdio 服务器

本实验中，我们将使用推荐的 stdio 传输创建一个简单的 MCP 服务器。该服务器将暴露客户可调用的工具，使用标准的模型上下文协议。

### 前提条件

- Python 3.8 或更高版本
- MCP Python SDK：`pip install mcp`
- 基本的异步编程理解

开始创建第一个 MCP stdio 服务器：

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
    # 使用stdio传输
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
- 简单子进程模型——客户端作为子进程启动服务器
- 通过 stdin/stdout 使用 JSON-RPC 消息通信
- 无需 HTTP 服务器设置
- 性能和安全性更优
- 更易调试与开发

**SSE 传输（自 MCP 2025-06-18 起弃用）：**
- 需要带 SSE 端点的 HTTP 服务器
- 需更复杂的 Web 服务器基础设施
- 需要额外考虑 HTTP 端点的安全性
- 已被可流式 HTTP 取代，适用于基于 Web 的场景

### 使用 stdio 传输创建服务器

创建 stdio 服务器需要：

1. <strong>导入所需库</strong> - 需要 MCP 服务器组件和 stdio 传输
2. <strong>创建服务器实例</strong> - 定义服务器及其功能
3. <strong>定义工具</strong> - 添加希望暴露的功能
4. <strong>设置传输</strong> - 配置 stdio 通信
5. <strong>运行服务器</strong> - 启动服务器并处理消息

让我们分步构建：

### 第 1 步：创建一个基本的 stdio 服务器

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

将代码保存为 `server.py`，通过命令行运行：

```bash
python server.py
```

服务器将启动并等待来自 stdin 的输入。它通过 stdio 传输使用 JSON-RPC 消息通信。

### 第 4 步：使用 Inspector 测试

你可以使用 MCP Inspector 测试服务器：

1. 安装 Inspector：`npx @modelcontextprotocol/inspector`
2. 运行 Inspector，指向你的服务器
3. 测试你创建的工具

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## 调试你的 stdio 服务器

### 使用 MCP Inspector

MCP Inspector 是调试和测试 MCP 服务器的有力工具。以下是如何配合 stdio 服务器使用：

1. **安装 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **运行 Inspector**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. <strong>测试服务器</strong>：Inspector 提供 Web 界面，可以：
   - 查看服务器功能
   - 使用不同参数测试工具
   - 监视 JSON-RPC 消息
   - 调试连接问题

### 使用 VS Code

你也可以直接在 VS Code 中调试 MCP 服务器：

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
3. 运行调试器，并用 Inspector 测试

### 常见调试技巧

- 使用 `stderr` 进行日志记录——切勿向 `stdout` 写入，因其保留给 MCP 消息
- 确保所有 JSON-RPC 消息均以换行符分隔
- 先用简单工具测试，再添加复杂功能
- 使用 Inspector 验证消息格式

## 在 VS Code 中使用你的 stdio 服务器

构建完成 MCP stdio 服务器后，可将其与 VS Code 集成，以便与 Claude 或其他兼容 MCP 的客户端使用。

### 配置

1. <strong>创建 MCP 配置文件</strong>于 `%APPDATA%\Claude\claude_desktop_config.json`（Windows）或 `~/Library/Application Support/Claude/claude_desktop_config.json`（Mac）：

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

2. **重启 Claude**：关闭并重新打开 Claude 以加载新服务器配置。

3. <strong>测试连接</strong>：与 Claude 开启对话，尝试使用服务器工具：
   - “你能用问候工具和我打个招呼吗？”
   - “计算 15 和 27 的和”
   - “服务器信息是什么？”

### TypeScript stdio 服务器示例

以下为完整的 TypeScript 示例，供参考：

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

在本更新课程中，你学会了：

- 使用当前推荐的 **stdio 传输** 构建 MCP 服务器
- 理解为何 SSE 传输被弃用，取而代之的是 stdio 和可流式 HTTP
- 创建 MCP 客户端可调用的工具
- 使用 MCP Inspector 调试服务器
- 在 VS Code 和 Claude 中集成 stdio 服务器

stdio 传输提供了比已弃用的 SSE 方法更简单、更安全、更高效的 MCP 服务器构建方式。根据 2025-06-18 规范，它是大多数 MCP 服务器实现的推荐传输方式。

### .NET

1. 让我们先创建一些工具，为此我们将创建一个名为 *Tools.cs* 的文件，内容如下：

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## 练习：测试你的 stdio 服务器

构建好 stdio 服务器后，我们来测试确认其正确运行。

### 前提条件

1. 确保已安装 MCP Inspector：
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. 服务器代码已保存（例如为 `server.py`）

### 使用 Inspector 测试

1. **启动 Inspector 并连接服务器**：
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **打开 Web 界面**：Inspector 会打开浏览器窗口，显示服务器功能。

3. <strong>测试工具</strong>：
   - 用不同名称尝试 `get_greeting` 工具
   - 用各种数字测试 `calculate_sum` 工具
   - 调用 `get_server_info` 工具查看服务器元数据

4. <strong>监控通信</strong>：Inspector 显示客户端与服务器之间交换的 JSON-RPC 消息。

### 你应该看到的内容

服务器正确启动时，应看到：
- Inspector 中列出服务器功能
- 可测试的工具
- 成功的 JSON-RPC 消息交换
- 界面中显示的工具响应

### 常见问题和解决方案

**服务器无法启动：**
- 检查所有依赖是否安装：`pip install mcp`
- 验证 Python 语法和缩进
- 查看控制台的错误信息

**工具未显示：**
- 确认存在 `@server.tool()` 装饰器
- 确认工具函数定义在 `main()` 之前
- 确认服务器配置正确

**连接问题：**
- 确保服务器正确使用 stdio 传输
- 检查是否有其他进程干扰
- 确认 Inspector 命令语法无误

## 任务

尝试为你的服务器添加更多功能。参见[此页面](https://api.chucknorris.io/)以添加调用 API 的工具。服务器该怎样设计，由你决定。玩得开心 :)

## 解决方案

[解决方案](./solution/README.md) 这是一个包含可运行代码的可能方案。

## 关键要点

本章节的关键要点如下：

- stdio 传输是本地 MCP 服务器推荐的实现机制。
- stdio 传输允许 MCP 服务器与客户端通过标准输入输出流无缝通信。
- 可使用 Inspector 和 Visual Studio Code 直接使用 stdio 服务器，调试和集成方便。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python) 

## 附加资源

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 后续内容

## 接下来

既然你已经学会了如何使用 stdio 传输构建 MCP 服务器，可以探索更高级的主题：

- <strong>下一步</strong>：[使用 MCP 的 HTTP 流（可流式 HTTP）](../06-http-streaming/README.md) - 了解另一种远程服务器支持的传输机制
- <strong>高级</strong>：[MCP 安全最佳实践](../../02-Security/README.md) - 在 MCP 服务器中实现安全
- <strong>生产</strong>：[部署策略](../09-deployment/README.md) - 部署服务器供生产使用

## 附加资源

- [MCP 规范 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - 官方规范
- [MCP SDK 文档](https://github.com/modelcontextprotocol/sdk) - 各语言 SDK 参考
- [社区示例](../../06-CommunityContributions/README.md) - 来自社区的更多服务器示例

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文档的原语言版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->