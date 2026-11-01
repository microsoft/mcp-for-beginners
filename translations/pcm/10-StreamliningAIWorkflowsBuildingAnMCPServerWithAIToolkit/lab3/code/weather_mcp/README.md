# Weda MCP Server

This na sample MCP Server for Python wey dey implement weda tools wit mock responses. You fit use am as scaffold for your own MCP Server. E get di followin features: 

- **Weda Tool**: A tool wey dey provide mocked weda information based on di location wey dem give.
- **Connect to Agent Builder**: Feature wey make you fit connect di MCP server to di Agent Builder for testing and debugging.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Feature wey make you fit debug di MCP Server usin di MCP Inspector.

## How to get started wit di Weda MCP Server template

> **Wetin you need**
>
> To run di MCP Server for your local dev machine, you go need:
>
> - [Python](https://www.python.org/)
> - (*Optional - if you prefer uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepare di environment

Two ways dey to set up di environment for dis project. You fit choose any one based on wetin you prefer.

> Note: Reload VSCode or terminal make sure say di virtual environment python dey used after you create di virtual environment.

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create virtual environment: `uv venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select di python wey dey inside di created virtual environment <br>3. Install dependencies (include dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create virtual environment: `python -m venv .venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select di python wey dey inside di created virtual environment<br>3. Install dependencies (include dev dependencies): `pip install -e .[dev]` | 

After you don set up di environment, you fit run di server for your local dev machine via Agent Builder as di MCP Client to get started:
1. Open VS Code Debug panel. Select `Debug in Agent Builder` or press `F5` to start debugging di MCP server.
2. For Microsoft Foundry Toolkit Agent Builder, select an active Foundry deployment like `gpt-5.1`, then enter: `What is the weather in Shanghai?`. Di server go connect automatically.
3. Click `Run` to test di server wit di prompt.

**Congratulations**! You don successfully run di Weda MCP Server for your local dev machine via Agent Builder as di MCP Client.
![Debug MCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wetin dey inside di template

| Folder / File| Wetin e dey contain                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode files wey dey for debugging                   |
| `.aitk`      | Configurations for Microsoft Foundry Toolkit                |
| `src`        | Di source code for di weda mcp server   |

## How to debug di Weda MCP Server

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) na visual developer tool for testing and debugging MCP servers.
> - All debugging modes support breakpoints, so you fit add breakpoints to di tool implementation code.

| Debug Mode | Description | Steps to debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug di MCP server in di Agent Builder via Microsoft Foundry Toolkit. | 1. Open VS Code Debug panel. Select `Debug in Agent Builder` and press `F5` to start debugging di MCP server.<br>2. Select an active Foundry deployment such as `gpt-5.1`, then enter `What is the weather in Shanghai?`. Di server go connect automatically.<br>3. Click `Run` to test di server wit di prompt. |
| MCP Inspector | Debug di MCP server usin di MCP Inspector. | 1. Install [Node.js](https://nodejs.org/)<br> 2. Set up Inspector: `cd inspector` && `npm install` <br> 3. Open VS Code Debug panel. Select `Debug SSE in Inspector (Edge)` or `Debug SSE in Inspector (Chrome)`. Press F5 to start debugging.<br> 4. When MCP Inspector launch for di browser, click di `Connect` button to connect dis MCP server.<br> 5. Then you fit `List Tools`, select a tool, input parameters, and `Run Tool` to debug your server code.<br> |

## Default Ports and customizations

| Debug Mode | Ports | Definitions | Customizations | Note |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) to change di ports wey dey above. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) to change di ports wey dey above.| N/A |

## Feedback

If you get any feedback or suggestions for dis template, abeg open an issue on the [Microsoft Foundry Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->