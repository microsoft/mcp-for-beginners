# 课程：构建一个 Web 搜索 MCP 服务器

本章演示如何构建一个真实世界的 AI 代理，集成外部 API，处理多样化数据类型，管理错误，并协调多个工具——所有这些都以生产就绪的形式呈现。你将看到：

- **集成需要身份验证的外部 API**
- **处理来自多个端点的多样化数据类型**
- **健壮的错误处理和日志策略**
- **单一服务器中的多工具协调**

到最后，你将获得构建高级 AI 和基于 LLM 应用所必需的模式和最佳实践的实战经验。

## 介绍

在本课中，你将学习如何构建一个高级 MCP 服务器和客户端，利用 SerpAPI 将 LLM 能力扩展到实时网络数据。这是开发能够访问最新网络信息的动态 AI 代理的关键技能。

## 学习目标

完成本课后，你将能够：

- 安全地将外部 API（如 SerpAPI）集成到 MCP 服务器中
- 实现用于网页、新闻、产品搜索和问答的多种工具
- 解析并格式化结构化数据以供 LLM 使用
- 有效处理错误和管理 API 速率限制
- 构建并测试自动化和交互式 MCP 客户端

## Web 搜索 MCP 服务器

本节介绍 Web 搜索 MCP 服务器的架构和功能。你将看到 FastMCP 和 SerpAPI 如何协同工作，将 LLM 能力扩展到实时网络数据。

### 概述

该实现包含四个工具，展示了 MCP 安全高效处理多样化外部 API 任务的能力：

- **general_search**：用于广泛的网页搜索结果
- **news_search**：用于最新新闻头条
- **product_search**：用于电商数据
- **qna**：用于问答片段

### 功能
- **代码示例**：包含针对 Python 的语言特定代码块（并可轻松扩展到其他语言），使用代码切换以增强清晰度

### Python

```python
# Example usage of the general_search tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "open source LLMs"})
            print(result)
```

---

在运行客户端之前，了解服务器的功能会很有帮助。[`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 文件实现了 MCP 服务器，通过集成 SerpAPI，暴露了网页、新闻、产品搜索和问答工具。它处理传入请求，管理 API 调用，解析响应，并将结构化结果返回给客户端。

你可以查看 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 的完整实现。

下面是服务器如何定义和注册工具的简要示例：

### Python 服务器

```python
# server.py (excerpt)
from mcp.server import MCPServer, Tool

async def general_search(query: str):
    # ...implementation...

server = MCPServer()
server.add_tool(Tool("general_search", general_search))

if __name__ == "__main__":
    server.run()
```

---

- **外部 API 集成**：演示了 API 密钥和外部请求的安全处理
- **结构化数据解析**：展示如何将 API 响应转换为适合 LLM 使用的格式
- **错误处理**：健壮的错误处理和适当的日志记录
- **交互式客户端**：包含自动化测试和交互模式以便测试
- **上下文管理**：利用 MCP Context 进行日志记录和请求跟踪

## 先决条件

开始之前，请确保你的环境已正确配置，按照以下步骤操作。这将确保所有依赖项已安装，API 密钥配置正确，方便开发和测试。

- Python 3.8 或更高版本
- SerpAPI API Key（在 [SerpAPI](https://serpapi.com/) 注册 - 提供免费套餐）

## 安装

开始之前，请按照以下步骤设置环境：

1. 使用 uv（推荐）或 pip 安装依赖：

```bash
# Using uv (recommended)
uv pip install -r requirements.txt

# Using pip
pip install -r requirements.txt
```

2. 在项目根目录创建 `.env` 文件，写入你的 SerpAPI 密钥：

```
SERPAPI_KEY=your_serpapi_key_here
```

## 使用方法

Web 搜索 MCP 服务器是核心组件，通过集成 SerpAPI，暴露网页、新闻、产品搜索和问答工具。它处理传入请求，管理 API 调用，解析响应，并将结构化结果返回给客户端。

你可以查看 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 的完整实现。

### 启动服务器

使用以下命令启动 MCP 服务器：

```bash
python server.py
```

服务器将作为基于 stdio 的 MCP 服务器运行，客户端可以直接连接。

### 客户端模式

客户端（`client.py`）支持两种与 MCP 服务器交互的模式：

- **普通模式**：运行自动化测试，调用所有工具并验证响应。适合快速检查服务器和工具是否正常工作。
- **交互模式**：启动菜单驱动界面，你可以手动选择并调用工具，输入自定义查询，实时查看结果。适合探索服务器功能和尝试不同输入。

你可以查看 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py) 的完整实现。

### 运行客户端

运行自动化测试（会自动启动服务器）：

```bash
python client.py
```

或运行交互模式：

```bash
python client.py --interactive
```

### 使用不同方法测试

根据需求和工作流程，有多种方式测试和交互服务器提供的工具。

#### 使用 MCP Python SDK 编写自定义测试脚本
你也可以使用 MCP Python SDK 编写自己的测试脚本：

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_custom_query():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            # Call tools with your custom parameters
            result = await session.call_tool("general_search", 
                                           arguments={"query": "your custom query"})
            # Process the result
```

---

在这里，“测试脚本”指的是你编写的自定义 Python 程序，作为 MCP 服务器的客户端。它不是正式的单元测试，而是让你以编程方式连接服务器，调用任意工具并传入参数，检查结果。这种方式适合：

- 原型设计和工具调用实验
- 验证服务器对不同输入的响应
- 自动化重复调用工具
- 在 MCP 服务器基础上构建自己的工作流或集成

你可以用测试脚本快速尝试新查询，调试工具行为，甚至作为更高级自动化的起点。下面是使用 MCP Python SDK 创建此类脚本的示例：

## 工具说明

服务器提供了以下工具，用于执行不同类型的搜索和查询。每个工具的参数和示例用法如下。

本节详细介绍每个可用工具及其参数。

### general_search

执行通用网页搜索并返回格式化结果。

**如何调用此工具：**

你可以通过 MCP Python SDK 在自己的脚本中调用 `general_search`，也可以通过 Inspector 或交互式客户端模式交互调用。以下是使用 SDK 的代码示例：

# [Python 示例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_general_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("general_search", arguments={"query": "latest AI trends"})
            print(result)
```

---

或者在交互模式中，从菜单选择 `general_search`，然后输入查询。

**参数：**
- `query`（字符串）：搜索查询

**示例请求：**

```json
{
  "query": "latest AI trends"
}
```

### news_search

搜索与查询相关的最新新闻文章。

**如何调用此工具：**

你可以通过 MCP Python SDK 在自己的脚本中调用 `news_search`，也可以通过 Inspector 或交互式客户端模式交互调用。以下是使用 SDK 的代码示例：

# [Python 示例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_news_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("news_search", arguments={"query": "AI policy updates"})
            print(result)
```

---

或者在交互模式中，从菜单选择 `news_search`，然后输入查询。

**参数：**
- `query`（字符串）：搜索查询

**示例请求：**

```json
{
  "query": "AI policy updates"
}
```

### product_search

搜索匹配查询的产品。

**如何调用此工具：**

你可以通过 MCP Python SDK 在自己的脚本中调用 `product_search`，也可以通过 Inspector 或交互式客户端模式交互调用。以下是使用 SDK 的代码示例：

# [Python 示例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_product_search():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("product_search", arguments={"query": "best AI gadgets 2025"})
            print(result)
```

---

或者在交互模式中，从菜单选择 `product_search`，然后输入查询。

**参数：**
- `query`（字符串）：产品搜索查询

**示例请求：**

```json
{
  "query": "best AI gadgets 2025"
}
```

### qna

从搜索引擎获取问题的直接答案。

**如何调用此工具：**

你可以通过 MCP Python SDK 在自己的脚本中调用 `qna`，也可以通过 Inspector 或交互式客户端模式交互调用。以下是使用 SDK 的代码示例：

# [Python 示例](../../../../05-AdvancedTopics/web-search-mcp)

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_qna():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            result = await session.call_tool("qna", arguments={"question": "what is artificial intelligence"})
            print(result)
```

---

或者在交互模式中，从菜单选择 `qna`，然后输入问题。

**参数：**
- `question`（字符串）：要查询答案的问题

**示例请求：**

```json
{
  "question": "what is artificial intelligence"
}
```

## 代码细节

本节提供服务器和客户端实现的代码片段和参考。

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

完整实现请参见 [`server.py`](../../../../05-AdvancedTopics/web-search-mcp/server.py) 和 [`client.py`](../../../../05-AdvancedTopics/web-search-mcp/client.py)。

```python
# Example snippet from server.py:
import os
import httpx
# ...existing code...
```

---

## 本课的高级概念

在开始构建之前，这里介绍一些本章中会出现的重要高级概念。理解它们将帮助你更好地跟进内容，即使你之前不熟悉：

- **多工具协调**：指在单一 MCP 服务器中运行多个不同工具（如网页搜索、新闻搜索、产品搜索和问答）。这让服务器能处理多种任务，而非单一功能。
- **API 速率限制处理**：许多外部 API（如 SerpAPI）限制一定时间内的请求次数。良好的代码会检测这些限制并优雅处理，避免应用崩溃。
- **结构化数据解析**：API 响应通常复杂且嵌套。该概念指将响应转换为简洁、易用的格式，方便 LLM 或其他程序使用。
- **错误恢复**：有时会出现网络故障或 API 返回异常。错误恢复意味着代码能处理这些问题，提供有用反馈，而非崩溃。
- **参数验证**：检查传入工具的所有输入是否正确且安全，包括设置默认值和类型校验，有助于防止错误和混淆。

本节将帮助你诊断和解决使用 Web 搜索 MCP 服务器时可能遇到的常见问题。如果遇到错误或异常行为，先查看本节的解决方案——它们通常能快速帮你排除故障。

## 故障排除

在使用 Web 搜索 MCP 服务器时，偶尔会遇到问题——这在开发外部 API 和新工具时很常见。本节提供最常见问题的实用解决方案，帮助你快速恢复。如果遇到错误，请从这里开始：以下提示涵盖了大多数用户遇到的问题，通常能无需额外帮助就解决。

### 常见问题

以下是用户最常遇到的问题及其清晰解释和解决步骤：

1. **.env 文件中缺少 SERPAPI_KEY**
   - 如果出现 `SERPAPI_KEY environment variable not found` 错误，说明应用找不到访问 SerpAPI 所需的 API 密钥。解决方法是在项目根目录创建 `.env` 文件（如果尚未创建），并添加一行 `SERPAPI_KEY=your_serpapi_key_here`。请将 `your_serpapi_key_here` 替换为你从 SerpAPI 网站获取的实际密钥。

2. **模块未找到错误**
   - 如 `ModuleNotFoundError: No module named 'httpx'` 表示缺少必要的 Python 包。通常是因为未安装所有依赖。解决方法是在终端运行 `pip install -r requirements.txt`，安装项目所需的全部依赖。

3. **连接问题**
   - 如果出现 `Error during client execution`，通常表示客户端无法连接服务器，或服务器未按预期运行。请确认客户端和服务器版本兼容，`server.py` 文件存在且在正确目录运行。重启服务器和客户端也可能解决问题。

4. **SerpAPI 错误**
   - 出现 `Search API returned error status: 401` 表示 SerpAPI 密钥缺失、错误或过期。请登录 SerpAPI 控制台核实密钥，并根据需要更新 `.env` 文件。如果密钥正确但仍报错，检查免费套餐配额是否用尽。

### 调试模式

默认情况下，应用只记录重要信息。如果你想查看更多细节（例如诊断复杂问题），可以启用 DEBUG 模式。这样会显示应用执行的更多步骤信息。

**示例：正常输出**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

**示例：DEBUG 输出**
```plaintext
2025-06-01 10:15:23,456 - __main__ - INFO - Calling general_search with params: {'query': 'open source LLMs'}
2025-06-01 10:15:23,457 - httpx - DEBUG - HTTP Request: GET https://serpapi.com/search ...
2025-06-01 10:15:23,458 - httpx - DEBUG - HTTP Response: 200 OK ...
2025-06-01 10:15:24,123 - __main__ - INFO - Successfully called general_search

GENERAL_SEARCH RESULTS:
... (search results here) ...
```

注意 DEBUG 模式会额外显示 HTTP 请求、响应及其他内部细节，有助于故障排查。
要启用 DEBUG 模式，请在 `client.py` 或 `server.py` 文件顶部将日志级别设置为 DEBUG：

# [Python](../../../../05-AdvancedTopics/web-search-mcp)

```python
# At the top of your client.py or server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Change from INFO to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

---

---

## 接下来做什么

- [5.10 实时流](../mcp-realtimestreaming/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。