# 使用 MCP Inspector 进行调试

> [!NOTE]
> 使用 `--sse` 的命令和以 `/sse` 结尾的 URL 测试的是传统的 HTTP+SSE
> 传输。对于新的 MCP `2026-07-28` 服务器，请使用支持可流式 HTTP 的 Inspector 版本，
> 并选择该传输方式。

**MCP Inspector** 是一个重要的调试工具，可以让你无需完整的 AI 主机应用，就能交互式地测试和排查 MCP 服务器问题。把它看作 MCP 的“Postman”——它提供了一个可视化界面来发送请求、查看响应并理解服务器行为。

## 为什么使用 MCP Inspector？

在构建 MCP 服务器时，你常常会遇到以下挑战：

- **“我的服务器在运行吗？”** - Inspector 显示连接状态
- **“我的工具注册正确吗？”** - Inspector 列出所有可用工具
- **“响应格式是什么？”** - Inspector 显示完整的 JSON 响应
- **“为什么这个工具不工作？”** - Inspector 显示详细的错误信息

## 先决条件

- 已安装 Node.js 18+
- npm（随 Node.js 一同安装）
- 一个可用于测试的 MCP 服务器（参见 [模块 3.1 - 第一个服务器](../01-first-server/README.md)）

## 安装

### 方案 1：使用 npx 运行（推荐快速测试）

```bash
npx @modelcontextprotocol/inspector
```

### 方案 2：全局安装

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### 方案 3：添加到你的项目中

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

在 `package.json` 中添加：
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## 连接你的服务器

### stdio 服务器（本地进程）

对于通过标准输入/输出通信的服务器：

```bash
# Python 服务器
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js 服务器
npx @modelcontextprotocol/inspector node ./build/index.js

# 带有环境变量
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP 服务器（网络）

对于作为 HTTP 服务运行的服务器：

1. 先启动你的服务器：
   ```bash
   python server.py  # 服务器运行在 http://localhost:8080
   ```

2. 启动 Inspector 并连接：
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector 界面概览

启动 Inspector 后，你会看到一个网页界面（通常在 `http://localhost:5173`）：

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 测试工具

### 列出可用工具

1. 点击 **Tools** 标签页
2. Inspector 会自动调用 `tools/list`
3. 你会看到所有注册的工具，包括：
   - 工具名称
   - 描述
   - 输入模式（参数）

### 调用工具

1. 从列表中选择一个工具
2. 在表单中填写必要参数
3. 点击 **Run Tool**
4. 在结果面板查看响应

**示例：测试一个计算器工具**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### 调试工具错误

当工具调用失败时，Inspector 会显示：

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

常见错误代码：
| 代码 | 含义 |
|------|---------|
| -32700 | 解析错误（无效的 JSON） |
| -32600 | 无效请求 |
| -32601 | 未找到方法 |
| -32602 | 参数无效 |
| -32603 | 内部错误 |

---

## 测试资源

### 列出资源

1. 点击 **Resources** 标签页
2. Inspector 调用 `resources/list`
3. 你会看到：
   - 资源 URI
   - 名称和描述
   - MIME 类型

### 读取资源

1. 选择一个资源
2. 点击 **Read Resource**
3. 查看返回的内容

**示例输出：**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## 测试提示

### 列出提示

1. 点击 **Prompts** 标签页
2. Inspector 调用 `prompts/list`
3. 查看可用的提示模板

### 获取提示

1. 选择一个提示
2. 填写所需参数
3. 点击 **Get Prompt**
4. 查看呈现的提示消息

---

## 消息日志分析

消息日志显示所有 MCP 协议消息。下面的转录来自一个
传统的 `2025-11-25` 服务器，包括已移除的 `initialize` 握手步骤。
`2026-07-28` 服务器使用独立请求元数据和 `server/discover`
来替代。

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### 需要关注的点

- **请求/响应对**：每个 `→` 应该有对应的 `←`
- <strong>错误信息</strong>：查看响应中的 `"error"`
- <strong>时间点</strong>：较大的时间间隔可能表示性能问题
- <strong>协议版本</strong>：确保服务器和客户端协议版本一致

---

## VS Code 集成

你可以直接在 VS Code 中运行 Inspector：

### 使用 launch.json

添加到 `.vscode/launch.json` 文件：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### 使用任务（Tasks）

添加到 `.vscode/tasks.json` 文件：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## 常见调试场景

### 场景 1：服务器无法连接

**症状：** Inspector 显示“Disconnected”或停留在“Connecting...”

**检查列表：**
1. ✅ 服务器命令是否正确？
2. ✅ 是否安装了所有依赖？
3. ✅ 服务器路径为绝对路径还是相对于当前目录？
4. ✅ 是否设置了所需的环境变量？

**调试步骤：**
```bash
# 先手动测试服务器
python -c "import your_server_module; print('OK')"

# 检查导入错误
python -m your_server_module 2>&1 | head -20

# 验证是否安装了MCP SDK
pip show mcp
```

### 场景 2：工具未显示

**症状：** 工具标签页显示为空列表

**可能原因：**
1. 工具未在服务器初始化时注册
2. 服务器启动后崩溃
3. `tools/list` 处理函数返回空数组

**调试步骤：**
1. 检查消息日志中的 `tools/list` 响应
2. 在工具注册代码中添加日志记录
3. 确认存在 `@mcp.tool()` 装饰器（Python）

### 场景 3：工具返回错误

**症状：** 工具调用返回错误响应

**调试方法：**
1. 仔细阅读错误信息
2. 检查参数类型是否符合模式
3. 添加 try/catch 捕获并显示详细错误
4. 检查服务器日志中的堆栈跟踪

**示例：改进的错误处理：**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # 这里是工具逻辑
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### 场景 4：资源内容为空

**症状：** 资源返回了，但内容为空或为 null

**检查列表：**
1. ✅ 文件路径或 URI 是否正确
2. ✅ 服务器是否有权限读取该资源
3. ✅ 资源内容是否正确返回

---

## 高级 Inspector 功能

### 自定义头（SSE）

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### 详细日志记录

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### 记录会话

Inspector 可以导出消息日志以供后续分析：
1. 在消息面板点击 **Export Log**
2. 保存 JSON 文件
3. 与团队成员共享以便调试

---

## 最佳实践

1. <strong>早测多测</strong> - 开发中多使用 Inspector 进行测试，而不仅仅是出现问题时
2. <strong>从简开始</strong> - 先测试基本连接，再测试复杂工具调用
3. <strong>检查模式</strong> - 许多错误来自参数类型不匹配
4. <strong>阅读错误信息</strong> - MCP 的错误通常很有描述性
5. **保持 Inspector 打开** - 有助于开发时及时发现问题

---

## 下一步

你已完成模块 3：入门！继续你的学习：

- [模块 4：实用实现](../../04-PracticalImplementation/README.md)

---

## 其他资源

- [MCP Inspector GitHub 仓库](https://github.com/modelcontextprotocol/inspector)
- [MCP 规范 - 协议消息](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 规范](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->