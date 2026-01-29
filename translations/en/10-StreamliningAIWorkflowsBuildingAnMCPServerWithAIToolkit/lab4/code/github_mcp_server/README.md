# Weather MCP Server

This is a sample MCP Server in Python that implements weather tools with mock responses. It can serve as a foundation for creating your own MCP Server. It includes the following features:

- **Weather Tool**: A tool that provides simulated weather information based on the specified location.
- **Git Clone Tool**: A tool that clones a git repository into a designated folder.
- **VS Code Open Tool**: A tool that opens a folder in VS Code or VS Code Insiders.
- **Connect to Agent Builder**: A feature that enables you to connect the MCP server to the Agent Builder for testing and debugging.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: A feature that allows you to debug the MCP Server using the MCP Inspector.

## Get started with the Weather MCP Server template

> **Prerequisites**
>
> To run the MCP Server on your local development machine, you will need:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Required for the git_clone_repo tool)
> - [VS Code](https://code.visualstudio.com/) or [VS Code Insiders](https://code.visualstudio.com/insiders/) (Required for the open_in_vscode tool)
> - (*Optional - if you prefer uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepare environment

There are two ways to set up the environment for this project. Choose the one that suits you best.

> Note: Reload VSCode or your terminal to ensure the virtual environment's Python is being used after creating the virtual environment.

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create a virtual environment: `uv venv` <br>2. Run the VSCode command "***Python: Select Interpreter***" and select the Python interpreter from the created virtual environment <br>3. Install dependencies (including development dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create a virtual environment: `python -m venv .venv` <br>2. Run the VSCode command "***Python: Select Interpreter***" and select the Python interpreter from the created virtual environment<br>3. Install dependencies (including development dependencies): `pip install -e .[dev]` | 

After setting up the environment, you can run the server on your local development machine via Agent Builder as the MCP Client to get started:
1. Open the VS Code Debug panel. Select `Debug in Agent Builder` or press `F5` to start debugging the MCP server.
2. Use the AI Toolkit Agent Builder to test the server with [this prompt](../../../../../../../../../../../open_prompt_builder). The server will automatically connect to the Agent Builder.
3. Click `Run` to test the server with the prompt.

**Congratulations**! You have successfully run the Weather MCP Server on your local development machine via Agent Builder as the MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## What's included in the template

| Folder / File| Contents                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode files for debugging                   |
| `.aitk`      | Configurations for AI Toolkit                |
| `src`        | The source code for the weather MCP server   |

## How to debug the Weather MCP Server

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is a visual developer tool for testing and debugging MCP servers.
> - All debugging modes support breakpoints, so you can add breakpoints to the tool implementation code.

## Available Tools

### Weather Tool
The `get_weather` tool provides simulated weather information for a specified location.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `location` | string | The location for which to retrieve weather information (e.g., city name, state, or coordinates) |

### Git Clone Tool
The `git_clone_repo` tool clones a git repository into a designated folder.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `repo_url` | string | The URL of the git repository to clone |
| `target_folder` | string | The path to the folder where the repository should be cloned |

The tool returns a JSON object with:
- `success`: A boolean indicating whether the operation was successful
- `target_folder` or `error`: The path of the cloned repository or an error message

### VS Code Open Tool
The `open_in_vscode` tool opens a folder in the VS Code or VS Code Insiders application.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `folder_path` | string | The path to the folder to open |
| `use_insiders` | boolean (optional) | Whether to use VS Code Insiders instead of regular VS Code |

The tool returns a JSON object with:
- `success`: A boolean indicating whether the operation was successful
- `message` or `error`: A confirmation message or an error message

| Debug Mode | Description | Steps to debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug the MCP server in the Agent Builder via AI Toolkit. | 1. Open the VS Code Debug panel. Select `Debug in Agent Builder` and press `F5` to start debugging the MCP server.<br>2. Use the AI Toolkit Agent Builder to test the server with [this prompt](../../../../../../../../../../../open_prompt_builder). The server will automatically connect to the Agent Builder.<br>3. Click `Run` to test the server with the prompt. |
| MCP Inspector | Debug the MCP server using the MCP Inspector. | 1. Install [Node.js](https://nodejs.org/)<br> 2. Set up Inspector: `cd inspector` && `npm install` <br> 3. Open the VS Code Debug panel. Select `Debug SSE in Inspector (Edge)` or `Debug SSE in Inspector (Chrome)`. Press F5 to start debugging.<br> 4. When MCP Inspector launches in the browser, click the `Connect` button to connect this MCP server.<br> 5. Then you can `List Tools`, select a tool, input parameters, and `Run Tool` to debug your server code.<br> |

## Default Ports and customizations

| Debug Mode | Ports | Definitions | Customizations | Note |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change the above ports. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change the above ports.| N/A |

## Feedback

If you have any feedback or suggestions for this template, please open an issue on the [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.