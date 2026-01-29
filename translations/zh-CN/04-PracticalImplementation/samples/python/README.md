# Model Context Protocol (MCP) Python 实现

本仓库包含 Model Context Protocol (MCP) 的 Python 实现，演示如何创建基于 MCP 标准通信的服务器和客户端应用。

## 概述

MCP 实现包含两个主要部分：

1. **MCP 服务器（`server.py`）** - 一个提供以下功能的服务器：
   - **工具**：可远程调用的函数
   - **资源**：可获取的数据
   - **提示**：用于生成语言模型提示的模板

2. **MCP 客户端（`client.py`）** - 连接服务器并使用其功能的客户端应用

## 功能

该实现展示了 MCP 的几个关键功能：

### 工具
- `completion` - 生成 AI 模型的文本补全（模拟）
- `add` - 简单的加法计算器，计算两个数字之和

### 资源
- `models://` - 返回可用 AI 模型的信息
- `greeting://{name}` - 返回针对指定名称的个性化问候

### 提示
- `review_code` - 生成代码审查的提示模板

## 安装

使用此 MCP 实现前，请安装所需的依赖包：

```powershell
pip install mcp-server mcp-client
```

## 启动服务器和客户端

### 启动服务器

在一个终端窗口运行服务器：

```powershell
python server.py
```

服务器也可以通过 MCP CLI 以开发模式运行：

```powershell
mcp dev server.py
```

或者安装到 Claude Desktop（如果可用）：

```powershell
mcp install server.py
```

### 运行客户端

在另一个终端窗口运行客户端：

```powershell
python client.py
```

这将连接服务器并演示所有可用功能。

### 客户端使用

客户端（`client.py`）演示了所有 MCP 功能：

```powershell
python client.py
```

这将连接服务器并调用所有功能，包括工具、资源和提示。输出将显示：

1. 计算器工具结果（5 + 7 = 12）
2. 对 “What is the meaning of life?” 的补全工具响应
3. 可用 AI 模型列表
4. 针对 “MCP Explorer” 的个性化问候
5. 代码审查提示模板

## 实现细节

服务器使用 `FastMCP` API 实现，提供了定义 MCP 服务的高级抽象。以下是定义工具的简化示例：

```python
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of the two numbers
    """
    logger.info(f"Adding {a} and {b}")
    return a + b
```

客户端使用 MCP 客户端库连接并调用服务器：

```python
async with stdio_client(server_params) as (reader, writer):
    async with ClientSession(reader, writer) as session:
        await session.initialize()
        result = await session.call_tool("add", arguments={"a": 5, "b": 7})
```

## 了解更多

欲了解更多关于 MCP 的信息，请访问：https://modelcontextprotocol.io/

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。