## 测试与调试

在开始测试你的 MCP 服务器之前，了解可用的工具和调试的最佳实践非常重要。有效的测试能确保服务器按预期运行，并帮助你快速发现和解决问题。以下部分将介绍验证 MCP 实现的推荐方法。

## 概述

本课将介绍如何选择合适的测试方法以及最有效的测试工具。

## 学习目标

完成本课后，你将能够：

- 描述各种测试方法。
- 使用不同工具有效地测试代码。

## 测试 MCP 服务器

MCP 提供了帮助你测试和调试服务器的工具：

- **MCP Inspector**：一个命令行工具，可作为 CLI 工具或可视化工具运行。
- **手动测试**：你可以使用 curl 这类工具发送网络请求，任何支持 HTTP 的工具都可以。
- **单元测试**：可以使用你喜欢的测试框架来测试服务器和客户端的功能。

### 使用 MCP Inspector

我们在之前的课程中介绍过该工具的使用，这里做个简要说明。它是基于 Node.js 构建的工具，你可以通过调用 `npx` 命令来使用，`npx` 会临时下载并安装该工具，运行完成后会自动清理。

[MCP Inspector](https://github.com/modelcontextprotocol/inspector) 可以帮助你：

- **发现服务器功能**：自动检测可用的资源、工具和提示
- **测试工具执行**：尝试不同参数，实时查看响应
- **查看服务器元数据**：检查服务器信息、模式和配置

工具的典型运行示例如下：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

上述命令启动 MCP 及其可视化界面，并在浏览器中打开本地网页界面。你会看到一个仪表盘，显示已注册的 MCP 服务器、可用工具、资源和提示。该界面允许你交互式地测试工具执行、检查服务器元数据和查看实时响应，方便验证和调试 MCP 服务器实现。

界面示例如下： ![Inspector](../../../../translated_images/zh-CN/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.png)

你也可以在 CLI 模式下运行该工具，只需添加 `--cli` 参数。下面是以“CLI”模式运行工具并列出服务器上所有工具的示例：

```sh
npx @modelcontextprotocol/inspector --cli node build/index.js --method tools/list
```

### 手动测试

除了使用 inspector 工具测试服务器功能外，另一种类似的方法是使用支持 HTTP 的客户端工具，比如 curl。

使用 curl，你可以通过 HTTP 请求直接测试 MCP 服务器：

```bash
# Example: Test server metadata
curl http://localhost:3000/v1/metadata

# Example: Execute a tool
curl -X POST http://localhost:3000/v1/tools/execute \
  -H "Content-Type: application/json" \
  -d '{"name": "calculator", "parameters": {"expression": "2+2"}}'
```

如上所示，使用 curl 发送 POST 请求，调用工具时需要传递工具名称和参数的负载。选择最适合你的方法。CLI 工具通常使用更快，也便于脚本化，这在 CI/CD 环境中非常有用。

### 单元测试

为你的工具和资源编写单元测试，确保它们按预期工作。以下是示例测试代码。

```python
import pytest

from mcp.server.fastmcp import FastMCP
from mcp.shared.memory import (
    create_connected_server_and_client_session as create_session,
)

# Mark the whole module for async tests
pytestmark = pytest.mark.anyio


async def test_list_tools_cursor_parameter():
    """Test that the cursor parameter is accepted for list_tools.

    Note: FastMCP doesn't currently implement pagination, so this test
    only verifies that the cursor parameter is accepted by the client.
    """

 server = FastMCP("test")

    # Create a couple of test tools
    @server.tool(name="test_tool_1")
    async def test_tool_1() -> str:
        """First test tool"""
        return "Result 1"

    @server.tool(name="test_tool_2")
    async def test_tool_2() -> str:
        """Second test tool"""
        return "Result 2"

    async with create_session(server._mcp_server) as client_session:
        # Test without cursor parameter (omitted)
        result1 = await client_session.list_tools()
        assert len(result1.tools) == 2

        # Test with cursor=None
        result2 = await client_session.list_tools(cursor=None)
        assert len(result2.tools) == 2

        # Test with cursor as string
        result3 = await client_session.list_tools(cursor="some_cursor_value")
        assert len(result3.tools) == 2

        # Test with empty string cursor
        result4 = await client_session.list_tools(cursor="")
        assert len(result4.tools) == 2
    
```

上述代码实现了：

- 利用 pytest 框架，可以将测试写成函数并使用 assert 语句。
- 创建了一个包含两个不同工具的 MCP 服务器。
- 使用 `assert` 语句检查特定条件是否满足。

完整文件请查看 [full file here](https://github.com/modelcontextprotocol/python-sdk/blob/main/tests/client/test_list_methods_cursor.py)

基于上述文件，你可以测试自己的服务器，确保功能按预期创建。

所有主流 SDK 都有类似的测试部分，你可以根据所选运行环境进行调整。

## 示例

- [Java 计算器](../samples/java/calculator/README.md)
- [.Net 计算器](../../../../03-GettingStarted/samples/csharp)
- [JavaScript 计算器](../samples/javascript/README.md)
- [TypeScript 计算器](../samples/typescript/README.md)
- [Python 计算器](../../../../03-GettingStarted/samples/python)

## 额外资源

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## 后续内容

- 下一节：[部署](../09-deployment/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。