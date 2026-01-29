# Weather MCP Server

这是一个用 Python 实现的天气工具示例 MCP Server，返回模拟的响应。它可以作为你自己 MCP Server 的基础框架。包含以下功能：

- **Weather Tool**：一个根据给定位置提供模拟天气信息的工具。
- **连接到 Agent Builder**：允许你将 MCP Server 连接到 Agent Builder 以进行测试和调试。
- **在 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 中调试**：支持使用 MCP Inspector 调试 MCP Server。

## 使用 Weather MCP Server 模板快速开始

> **前提条件**
>
> 要在本地开发机器上运行 MCP Server，你需要：
>
> - [Python](https://www.python.org/)
> - （可选 - 如果你喜欢使用 uv）[uv](https://github.com/astral-sh/uv)
> - [Python 调试扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 准备环境

有两种方式可以为该项目设置环境，你可以根据喜好选择其中一种。

> 注意：创建虚拟环境后，请重新加载 VSCode 或终端，确保使用虚拟环境中的 Python。

| 方式 | 步骤 |
| -------- | ----- |
| 使用 `uv` | 1. 创建虚拟环境：`uv venv` <br>2. 运行 VSCode 命令 "***Python: Select Interpreter***"，选择刚创建的虚拟环境中的 Python <br>3. 安装依赖（包括开发依赖）：`uv pip install -r pyproject.toml --extra dev` |
| 使用 `pip` | 1. 创建虚拟环境：`python -m venv .venv` <br>2. 运行 VSCode 命令 "***Python: Select Interpreter***"，选择刚创建的虚拟环境中的 Python <br>3. 安装依赖（包括开发依赖）：`pip install -e .[dev]` |

环境配置完成后，你可以通过 Agent Builder 作为 MCP Client 在本地开发机器上运行服务器，开始使用：
1. 打开 VS Code 调试面板。选择 `Debug in Agent Builder` 或按 `F5` 启动 MCP Server 调试。
2. 使用 AI Toolkit Agent Builder 通过[此提示](../../../../../../../../../../open_prompt_builder)测试服务器。服务器会自动连接到 Agent Builder。
3. 点击 `Run` 使用该提示测试服务器。

**恭喜**！你已成功通过 Agent Builder 作为 MCP Client 在本地开发机器上运行了 Weather MCP Server。  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## 模板包含内容

| 文件夹 / 文件 | 内容 |
| ------------ | -------------------------------------------- |
| `.vscode`    | 用于调试的 VSCode 配置文件                   |
| `.aitk`      | AI Toolkit 的配置文件                         |
| `src`        | weather mcp server 的源代码                   |

## 如何调试 Weather MCP Server

> 说明：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 是一个用于测试和调试 MCP Server 的可视化开发工具。
> - 所有调试模式均支持断点，你可以在工具实现代码中添加断点。

| 调试模式 | 说明 | 调试步骤 |
| ---------- | ----------- | --------------- |
| Agent Builder | 通过 AI Toolkit 在 Agent Builder 中调试 MCP Server。 | 1. 打开 VS Code 调试面板。选择 `Debug in Agent Builder` 并按 `F5` 启动 MCP Server 调试。<br>2. 使用 AI Toolkit Agent Builder 通过[此提示](../../../../../../../../../../open_prompt_builder)测试服务器。服务器会自动连接到 Agent Builder。<br>3. 点击 `Run` 使用该提示测试服务器。 |
| MCP Inspector | 使用 MCP Inspector 调试 MCP Server。 | 1. 安装 [Node.js](https://nodejs.org/)<br>2. 设置 Inspector：`cd inspector` && `npm install` <br>3. 打开 VS Code 调试面板。选择 `Debug SSE in Inspector (Edge)` 或 `Debug SSE in Inspector (Chrome)`，按 F5 启动调试。<br>4. 当 MCP Inspector 在浏览器中启动时，点击 `Connect` 按钮连接该 MCP Server。<br>5. 然后你可以 `List Tools`，选择工具，输入参数，点击 `Run Tool` 来调试服务器代码。<br> |

## 默认端口及自定义

| 调试模式 | 端口 | 定义文件 | 自定义方式 | 备注 |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | 编辑 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) 来修改端口。 | 无 |
| MCP Inspector | 3001（服务器）；5173 和 3000（Inspector） | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | 编辑 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json)、[__init__.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) 来修改端口。 | 无 |

## 反馈

如果你对该模板有任何反馈或建议，请在 [AI Toolkit GitHub 仓库](https://github.com/microsoft/vscode-ai-toolkit/issues) 提交 issue。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。