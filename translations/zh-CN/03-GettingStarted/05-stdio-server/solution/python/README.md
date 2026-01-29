# MCP stdio 服务器 - Python 解决方案

> **⚠️ 重要**: 此解决方案已更新为使用 **stdio 传输**，根据 MCP 规范 2025-06-18 的推荐。原来的 SSE 传输已被弃用。

## 概述

此 Python 解决方案展示了如何使用当前的 stdio 传输构建 MCP 服务器。相比已弃用的 SSE 方法，stdio 传输更简单、更安全，并且性能更优。

## 前置条件

- Python 3.8 或更高版本
- 推荐安装 `uv` 进行包管理，参见 [说明](https://docs.astral.sh/uv/#highlights)

## 设置说明

### 步骤 1: 创建虚拟环境

```bash
python -m venv venv
```

### 步骤 2: 激活虚拟环境

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 步骤 3: 安装依赖项

```bash
pip install mcp
```

## 运行服务器

stdio 服务器的运行方式与旧的 SSE 服务器不同。它通过标准输入/输出进行通信，而不是启动一个 Web 服务器：

```bash
python server.py
```

**重要**: 服务器看起来会挂起——这是正常现象！它正在等待来自标准输入的 JSON-RPC 消息。

## 测试服务器

### 方法 1: 使用 MCP Inspector（推荐）

```bash
npx @modelcontextprotocol/inspector python server.py
```

这将会：
1. 将您的服务器作为子进程启动
2. 打开一个用于测试的 Web 界面
3. 允许您交互式测试所有服务器工具

### 方法 2: 直接进行 JSON-RPC 测试

您也可以通过直接发送 JSON-RPC 消息进行测试：

1. 启动服务器: `python server.py`
2. 发送一个 JSON-RPC 消息（示例）：

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. 服务器将返回可用工具

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
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## 与 SSE 的主要区别

**stdio 传输（当前）:**
- ✅ 设置更简单 - 无需 Web 服务器
- ✅ 更高的安全性 - 无 HTTP 端点
- ✅ 基于子进程的通信
- ✅ 标准输入/输出上的 JSON-RPC
- ✅ 性能更优

**SSE 传输（已弃用）:**
- ❌ 需要设置 HTTP 服务器
- ❌ 需要 Web 框架（Starlette/FastAPI）
- ❌ 路由和会话管理更复杂
- ❌ 额外的安全性考虑
- ❌ 在 MCP 2025-06-18 中已弃用

## 调试提示

- 使用 `stderr` 进行日志记录（不要使用 `stdout`）
- 使用 Inspector 进行可视化调试
- 确保所有 JSON 消息以换行符分隔
- 检查服务器是否正常启动且无错误

此解决方案遵循当前 MCP 规范，并展示了 stdio 传输实现的最佳实践。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。