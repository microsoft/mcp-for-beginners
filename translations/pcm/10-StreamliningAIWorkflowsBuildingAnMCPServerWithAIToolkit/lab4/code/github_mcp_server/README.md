<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a6a4d3497921d2f6d9699f0a6a1890c",
  "translation_date": "2025-11-18T18:52:42+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/README.md",
  "language_code": "pcm"
}
-->
# Weather MCP Server

Dis na sample MCP Server wey dem write for Python wey dey use weather tools wit mock response. You fit use am as base to build your own MCP Server. E get di following features:

- **Weather Tool**: Tool wey dey give fake weather info based on di location wey you provide.
- **Git Clone Tool**: Tool wey dey copy git repository go di folder wey you choose.
- **VS Code Open Tool**: Tool wey dey open folder for VS Code or VS Code Insiders.
- **Connect to Agent Builder**: Feature wey go allow you connect di MCP server to Agent Builder for testing and debugging.
- **Debug for [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Feature wey go allow you debug di MCP Server wit MCP Inspector.

## How you go take start wit di Weather MCP Server template

> **Prerequisites**
>
> To run di MCP Server for your local dev machine, you go need:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (E dey important for git_clone_repo tool)
> - [VS Code](https://code.visualstudio.com/) or [VS Code Insiders](https://code.visualstudio.com/insiders/) (E dey important for open_in_vscode tool)
> - (*Optional - if you like uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepare environment

Two ways dey to set up di environment for dis project. You fit choose anyone wey you like.

> Note: Make sure say you reload VSCode or terminal so dat di virtual environment python go dey active after you create di virtual environment.

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create virtual environment: `uv venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and choose di python wey dey di virtual environment wey you create <br>3. Install dependencies (include dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create virtual environment: `python -m venv .venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and choose di python wey dey di virtual environment wey you create<br>3. Install dependencies (include dev dependencies): `pip install -e .[dev]` | 

After you don set up di environment, you fit run di server for your local dev machine via Agent Builder as di MCP Client to start:
1. Open VS Code Debug panel. Choose `Debug in Agent Builder` or press `F5` to start debugging di MCP server.
2. Use AI Toolkit Agent Builder to test di server wit [dis prompt](../../../../../../../../../../../open_prompt_builder). Di server go connect to di Agent Builder automatically.
3. Click `Run` to test di server wit di prompt.

**Congratulations**! You don successfully run di Weather MCP Server for your local dev machine via Agent Builder as di MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wetin dey inside di template

| Folder / File| Wetin e contain                             |
| ------------ | ------------------------------------------- |
| `.vscode`    | VSCode files for debugging                  |
| `.aitk`      | Configurations for AI Toolkit               |
| `src`        | Di source code for di weather MCP server    |

## How you fit debug di Weather MCP Server

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) na visual developer tool wey you fit use test and debug MCP servers.
> - All debugging modes dey support breakpoints, so you fit add breakpoints for di tool implementation code.

## Tools wey dey available

### Weather Tool
Di `get_weather` tool dey give fake weather info for di location wey you provide.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `location` | string | Di location wey you wan get weather info for (e.g., city name, state, or coordinates) |

### Git Clone Tool
Di `git_clone_repo` tool dey copy git repository go di folder wey you choose.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `repo_url` | string | Di URL of di git repository wey you wan copy |
| `target_folder` | string | Di path to di folder wey you wan copy di repository go |

Di tool dey return JSON object wey get:
- `success`: Boolean wey dey show if di operation work
- `target_folder` or `error`: Di path of di copied repository or error message

### VS Code Open Tool
Di `open_in_vscode` tool dey open folder for VS Code or VS Code Insiders application.

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| `folder_path` | string | Di path to di folder wey you wan open |
| `use_insiders` | boolean (optional) | If you wan use VS Code Insiders instead of di regular VS Code |

Di tool dey return JSON object wey get:
- `success`: Boolean wey dey show if di operation work
- `message` or `error`: Confirmation message or error message

| Debug Mode | Description | Steps to debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug di MCP server for di Agent Builder via AI Toolkit. | 1. Open VS Code Debug panel. Choose `Debug in Agent Builder` and press `F5` to start debugging di MCP server.<br>2. Use AI Toolkit Agent Builder to test di server wit [dis prompt](../../../../../../../../../../../open_prompt_builder). Di server go connect to di Agent Builder automatically.<br>3. Click `Run` to test di server wit di prompt. |
| MCP Inspector | Debug di MCP server wit MCP Inspector. | 1. Install [Node.js](https://nodejs.org/)<br> 2. Set up Inspector: `cd inspector` && `npm install` <br> 3. Open VS Code Debug panel. Choose `Debug SSE in Inspector (Edge)` or `Debug SSE in Inspector (Chrome)`. Press F5 to start debugging.<br> 4. When MCP Inspector open for browser, click di `Connect` button to connect dis MCP server.<br> 5. You fit `List Tools`, choose tool, put di parameters, and `Run Tool` to debug your server code.<br> |

## Default Ports and customizations

| Debug Mode | Ports | Definitions | Customizations | Note |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change di ports wey dey above. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) to change di ports wey dey above.| N/A |

## Feedback

If you get any feedback or suggestion for dis template, abeg open issue for di [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg sabi say machine translation fit get mistake or no correct well. Di original dokyument for im native language na di main source wey you go trust. For important information, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->