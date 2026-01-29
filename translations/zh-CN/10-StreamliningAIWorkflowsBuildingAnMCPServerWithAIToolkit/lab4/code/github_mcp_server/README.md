# Weather MCP Server

这是一个用 Python 实现的示例 MCP 服务器，提供天气工具的模拟响应。它可以作为您自己的 MCP 服务器的模板。它包括以下功能：

- **天气工具**：一个根据给定位置提供模拟天气信息的工具。
- **Git 克隆工具**：一个将 Git 仓库克隆到指定文件夹的工具。
- **VS Code 打开工具**：一个在 VS Code 或 VS Code Insiders 中打开文件夹的工具。
- **连接到 Agent Builder**：允许您将 MCP 服务器连接到 Agent Builder 进行测试和调试的功能。
- **在 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 中调试**：允许您使用 MCP Inspector 调试 MCP 服务器的功能。

## 开始使用 Weather MCP Server 模板

> **先决条件**
>
> 要在本地开发机器上运行 MCP 服务器，您需要：
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/)（Git 克隆工具所需）
> - [VS Code](https://code.visualstudio.com/) 或 [VS Code Insiders](https://code.visualstudio.com/insiders/)（VS Code 打开工具所需）
> - （*可选 - 如果您更喜欢 uv*）[uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 准备环境

有两种方法可以为此项目设置环境。您可以根据自己的喜好选择其中一种。

> 注意：创建虚拟环境后，请重新加载 VSCode 或终端以确保使用虚拟环境中的 Python。

| 方法 | 步骤 |
| -------- | ----- |
| 使用 `uv` | 1. 创建虚拟环境：`uv venv` <br>2. 运行 VSCode 命令“***Python: Select Interpreter***”，选择创建的虚拟环境中的 Python <br>3. 安装依赖项（包括开发依赖项）：`uv pip install -r pyproject.toml --extra dev` |
| 使用 `pip` | 1. 创建虚拟环境：`python -m venv .venv` <br>2. 运行 VSCode 命令“***Python: Select Interpreter***”，选择创建的虚拟环境中的 Python <br>3. 安装依赖项（包括开发依赖项）：`pip install -e .[dev]` |

设置环境后，您可以通过 Agent Builder 作为 MCP 客户端在本地开发机器上运行服务器以开始使用：
1. 打开 VS Code 调试面板。选择 `Debug in Agent Builder` 或按 `F5` 开始调试 MCP 服务器。
2. 使用 AI Toolkit Agent Builder 测试服务器，使用[此提示](../../../../../../../../../../../open_prompt_builder)。服务器将自动连接到 Agent Builder。
3. 点击 `Run` 使用提示测试服务器。

**恭喜**！您已成功通过 Agent Builder 作为 MCP 客户端在本地开发机器上运行 Weather MCP Server。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## 模板中包含的内容

| 文件夹 / 文件 | 内容                                     |
| ------------ | ---------------------------------------- |
| `.vscode`    | 用于调试的 VSCode 文件                   |
| `.aitk`      | AI Toolkit 的配置文件                    |
| `src`        | Weather MCP Server 的源代码              |

## 如何调试 Weather MCP Server

> 注意：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 是一个用于测试和调试 MCP 服务器的可视化开发工具。
> - 所有调试模式都支持断点，您可以在工具实现代码中添加断点。

## 可用工具

### 天气工具
`get_weather` 工具为指定位置提供模拟天气信息。

| 参数 | 类型 | 描述 |
| ---- | ---- | ---- |
| `location` | string | 获取天气信息的位置（例如城市名称、州或坐标） |

### Git 克隆工具
`git_clone_repo` 工具将 Git 仓库克隆到指定文件夹。

| 参数 | 类型 | 描述 |
| ---- | ---- | ---- |
| `repo_url` | string | 要克隆的 Git 仓库的 URL |
| `target_folder` | string | 仓库克隆到的目标文件夹路径 |

工具返回一个 JSON 对象，包括：
- `success`：表示操作是否成功的布尔值
- `target_folder` 或 `error`：克隆的仓库路径或错误信息

### VS Code 打开工具
`open_in_vscode` 工具在 VS Code 或 VS Code Insiders 应用中打开文件夹。

| 参数 | 类型 | 描述 |
| ---- | ---- | ---- |
| `folder_path` | string | 要打开的文件夹路径 |
| `use_insiders` | boolean（可选） | 是否使用 VS Code Insiders 而不是普通 VS Code |

工具返回一个 JSON 对象，包括：
- `success`：表示操作是否成功的布尔值
- `message` 或 `error`：确认信息或错误信息

| 调试模式 | 描述 | 调试步骤 |
| -------- | ---- | -------- |
| Agent Builder | 通过 AI Toolkit 在 Agent Builder 中调试 MCP 服务器。 | 1. 打开 VS Code 调试面板。选择 `Debug in Agent Builder` 并按 `F5` 开始调试 MCP 服务器。<br>2. 使用 AI Toolkit Agent Builder 测试服务器，使用[此提示](../../../../../../../../../../../open_prompt_builder)。服务器将自动连接到 Agent Builder。<br>3. 点击 `Run` 使用提示测试服务器。 |
| MCP Inspector | 使用 MCP Inspector 调试 MCP 服务器。 | 1. 安装 [Node.js](https://nodejs.org/)<br> 2. 设置 Inspector：`cd inspector` && `npm install` <br> 3. 打开 VS Code 调试面板。选择 `Debug SSE in Inspector (Edge)` 或 `Debug SSE in Inspector (Chrome)`。按 F5 开始调试。<br> 4. 当 MCP Inspector 在浏览器中启动时，点击 `Connect` 按钮连接此 MCP 服务器。<br> 5. 然后您可以 `List Tools`，选择一个工具，输入参数，并 `Run Tool` 调试您的服务器代码。 |

## 默认端口和自定义

| 调试模式 | 端口 | 定义 | 自定义 | 注意 |
| -------- | ---- | ---- | ---- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | 编辑 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) 更改上述端口。 | N/A |
| MCP Inspector | 3001（服务器）；5173 和 3000（Inspector） | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | 编辑 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) 更改上述端口。| N/A |

## 反馈

如果您对该模板有任何反馈或建议，请在 [AI Toolkit GitHub 仓库](https://github.com/microsoft/vscode-ai-toolkit/issues) 上提交问题。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。