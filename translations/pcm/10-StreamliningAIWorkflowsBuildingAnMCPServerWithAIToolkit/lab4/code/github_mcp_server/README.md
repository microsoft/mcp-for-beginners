# Weda MCP Server

Dis na sample MCP Server for Python wey dey implement weda tools wit mock responses. You fit use am as scaffold for your own MCP Server. E get di following features: 

- **Weather Tool**: Tool wey dey provide mock weda information based on di location wey you give.
- **Git Clone Tool**: Tool wey dey clone git repository go specified folder.
- **VS Code Open Tool**: Tool wey dey open folder for VS Code or VS Code Insiders.
- **Connect to Agent Builder**: Feature wey make you fit connect di MCP server to di Agent Builder for testing and debugging.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Feature wey allow you debug di MCP Server usin di MCP Inspector.

## How to start with di Weda MCP Server template

> **Wetin you need**
>
> To run the MCP Server for your local dev machine, you go need:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Needed for git_clone_repo tool)
> - [VS Code](https://code.visualstudio.com/) or [VS Code Insiders](https://code.visualstudio.com/insiders/) (Needed for open_in_vscode tool)
> - (*Optional - if you prefer uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepare di environment

Dere two approaches you fit use to set up di environment for dis project. You fit choose any one based on wetin you prefer.

> Note: Reload VSCode or terminal make sure di virtual environment python dey used after you create di virtual environment.

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create di virtual environment: `uv venv` <br>2. Run di VSCode Command "***Python: Select Interpreter***" and select di python wey dey the virtual environment wey you create <br>3. Install dependencies (include dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create di virtual environment: `python -m venv .venv` <br>2. Run di VSCode Command "***Python: Select Interpreter***" and select di python wey dey the virtual environment wey you create<br>3. Install dependencies (include dev dependencies): `pip install -e .[dev]` | 

After you don set up di environment, you fit run di server for your local dev machine via Agent Builder as di MCP Client to get started:
1. Open di VS Code Debug panel. Select `Debug in Agent Builder` or press `F5` to start debugging di MCP server.
2. For Microsoft Foundry Toolkit for Visual Studio Code Agent Builder, select an active Foundry deployment such as `gpt-5.1`, den enter: `What is the weather in Shanghai?`. Di server go connect automatically.
3. Click `Run` to test di server wit di prompt.

**Congratulations**! You don successfully run di Weda MCP Server for your local dev machine via Agent Builder as di MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wetin dey included in di template

| Folder / File| Contents                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode files wey dem dey use for debugging                   |
| `.aitk`      | Microsoft Foundry Toolkit configuration      |
| `src`        | Di source code for di weda mcp server   |

## How to debug di Weda MCP Server

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) na visual developer tool for testing and debugging MCP servers.
> - All debugging modes support breakpoints, so you fit add breakpoints to di tool implementation code.

## Available Tools

### Weather Tool
The `get_weather` tool dey provide mock weda information for a specified location.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `location` | string | Location to get weda for (e.g., city name, state, or coordinates) |

### Git Clone Tool
The `git_clone_repo` tool dey clone git repository go specified folder.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `repo_url` | string | URL of di git repository wey you want clone |
| `target_folder` | string | Path to di folder wey di repository go clone inside |

Di tool dey return one JSON object we get:
- `success`: Boolean wey show if di operation succeed
- `target_folder` or `error`: Di path of di cloned repository or one error message

### VS Code Open Tool
The `open_in_vscode` tool dey open folder for VS Code or VS Code Insiders application.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `folder_path` | string | Path to di folder wey you wan open |
| `use_insiders` | boolean (optional) | Whether to use VS Code Insiders instead of regular VS Code |

Di tool dey return one JSON object we get:
- `success`: Boolean wey show if di operation succeed
- `message` or `error`: Confirmation message or error message

| Debug Mode | Description | Steps to debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug di MCP server for Agent Builder via Microsoft Foundry Toolkit for Visual Studio Code. | 1. Open di VS Code Debug panel. Select `Debug in Agent Builder` and press `F5` to start debugging di MCP server.<br>2. Select an active Foundry deployment such as `gpt-5.1`, then enter `What is the weather in Shanghai?`. Di server go be connected automatically.<br>3. Click `Run` to test di server with di prompt. |
| MCP Inspector | Debug di MCP server using di MCP Inspector. | 1. Install [Node.js](https://nodejs.org/)<br> 2. Set up Inspector: `cd inspector` && `npm install` <br> 3. Open VS Code Debug panel. Select `Debug SSE in Inspector (Edge)` or `Debug SSE in Inspector (Chrome)`. Press F5 to start debugging.<br> 4. When MCP Inspector launch for di browser, click di `Connect` button to connect dis MCP server.<br> 5. Then you fit `List Tools`, select a tool, input parameters, and `Run Tool` to debug your server code.<br> |

## Default Ports and customizations

| Debug Mode | Ports | Definitions | Customizations | Note |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change di ports wey dey above. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change di ports wey dey above.| N/A |

## Feedback

If you get any feedback or suggestions for dis template, abeg open an issue on the [Microsoft Foundry Toolkit for Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->