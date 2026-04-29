## 测试和调试

在开始测试您的 MCP 服务器之前，了解可用的工具和调试的最佳实践非常重要。有效的测试可以确保您的服务器按预期工作，并帮助您快速识别和解决问题。以下部分概述了验证您的 MCP 实现的推荐方法。

## 概述

本课将介绍如何选择合适的测试方法以及最有效的测试工具。

## 学习目标

在本课结束时，您将能够：

- 描述各种测试方法。
- 使用不同的工具有效地测试您的代码。

## 测试 MCP 服务器

MCP 提供了帮助您测试和调试服务器的工具：

- **MCP Inspector**：一个命令行工具，可以作为 CLI 工具和可视化工具运行。
- <strong>手动测试</strong>：您可以使用 curl 这样的工具运行 Web 请求，但任何能够运行 HTTP 的工具都可以。
- <strong>单元测试</strong>：您可以使用您喜欢的测试框架来测试服务器和客户端的功能。

### 使用 MCP Inspector

我们在之前的课程中描述过该工具的用法，这里略作介绍。它是一个基于 Node.js 构建的工具，您可以通过调用 `npx` 可执行文件来使用，它会临时下载并安装该工具，请求执行完毕后会自动清理。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 可以帮助您：

- <strong>发现服务器功能</strong>：自动检测可用的资源、工具和提示
- <strong>测试工具执行</strong>：尝试不同参数，实时查看响应
- <strong>查看服务器元数据</strong>：检查服务器信息、模式和配置

工具的典型运行示例如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述命令启动 MCP 及其可视化界面，并在浏览器中启动一个本地网页界面。您可以看到一个仪表盘，显示您注册的 MCP 服务器、其可用的工具、资源和提示。该界面允许您交互式地测试工具执行、检查服务器元数据和查看实时响应，从而更轻松地验证和调试您的 MCP 服务器实现。

界面示例如下： ![Inspector](../../../../translated_images/zh-CN/connect.141db0b2bd05f096.webp)

您也可以以 CLI 模式运行此工具，添加 `--cli` 参数。下面是以“CLI”模式运行该工具的示例，列出服务器上的所有工具：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手动测试

除了运行 inspector 工具测试服务器功能之外，另一种类似的方法是运行能够使用 HTTP 的客户端工具，例如 curl。

使用 curl，您可以直接通过 HTTP 请求测试 MCP 服务器：

```bash
# 示例：测试服务器元数据
curl http://localhost:3000/v1/metadata

# 示例：执行一个工具
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

如上所示，使用 curl，通过 POST 请求调用工具，携带包括工具名称及其参数的负载。请选择最适合您的方法。CLI 工具一般使用速度较快，且便于脚本化，这在 CI/CD 环境中非常有用。

### 单元测试

为您的工具和资源创建单元测试，确保其按预期工作。下面是一些示例测试代码。

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# 标记整个模块为异步测试
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # 创建几个测试工具
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # 测试无光标参数（省略）
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # 测试光标为 None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # 测试光标为字符串
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # 测试光标为空字符串
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

上述代码实现了：

- 利用 pytest 框架，允许您将测试编写为函数并使用 assert 语句。
- 创建了一个带有两个不同工具的 MCP 服务器。
- 使用 `assert` 语句检查是否满足某些条件。

请查看[完整文件](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

基于上述文件，您可以测试自己的服务器，确保功能如期构建。

所有主要 SDK 都有类似的测试部分，您可以根据选择的运行环境进行调整。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)

## 附加资源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 接下来

- 下一步：[部署](../09-deployment/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件通过 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们力求准确，但请注意自动翻译可能包含错误或不准确之处。原始文档的原语言版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用该翻译而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->