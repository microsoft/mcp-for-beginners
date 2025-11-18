<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "999c5e7623c1e2d5e5a07c2feb39eb67",
  "translation_date": "2025-11-18T18:51:11+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md",
  "language_code": "pcm"
}
-->
# Weather MCP Server

Dis na sample MCP Server wey dey use Python wey dey do weather tools wit mock response. E fit work as scaffold for your own MCP Server. E get di following features:

- **Weather Tool**: Tool wey dey give fake weather info based on di location wey you provide.
- **Connect to Agent Builder**: Feature wey go allow you connect di MCP server to di Agent Builder for testing and debugging.
- **Debug for [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Feature wey go allow you debug di MCP Server wit MCP Inspector.

## How you go take start wit di Weather MCP Server template

> **Prerequisites**
>
> To run di MCP Server for your local dev machine, you go need:
>
> - [Python](https://www.python.org/)
> - (*Optional - if you like uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Prepare environment

Two ways dey to set up di environment for dis project. You fit choose anyone wey you like.

> Note: Make sure say you reload VSCode or terminal so dat di virtual environment python go dey active after you don create di virtual environment.

| Approach | Steps |
| -------- | ----- |
| Using `uv` | 1. Create virtual environment: `uv venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select di python wey dey di virtual environment wey you create <br>3. Install dependencies (include dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Using `pip` | 1. Create virtual environment: `python -m venv .venv` <br>2. Run VSCode Command "***Python: Select Interpreter***" and select di python wey dey di virtual environment wey you create<br>3. Install dependencies (include dev dependencies): `pip install -e .[dev]` | 

After you don set up di environment, you fit run di server for your local dev machine via Agent Builder as di MCP Client to start:
1. Open VS Code Debug panel. Select `Debug in Agent Builder` or press `F5` to start debugging di MCP server.
2. Use AI Toolkit Agent Builder to test di server wit [dis prompt](../../../../../../../../../../../open_prompt_builder). Server go auto-connect to di Agent Builder.
3. Click `Run` to test di server wit di prompt.

**Congratulations**! You don successfully run di Weather MCP Server for your local dev machine via Agent Builder as di MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wetin dey inside di template

| Folder / File| Wetin e contain                             |
| ------------ | ------------------------------------------- |
| `.vscode`    | VSCode files for debugging                  |
| `.aitk`      | Configurations for AI Toolkit               |
| `src`        | Di source code for di weather MCP server    |

## How you go take debug di Weather MCP Server

> Notes:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) na visual developer tool wey dey for testing and debugging MCP servers.
> - All debugging modes dey support breakpoints, so you fit add breakpoints for di tool implementation code.

| Debug Mode | Description | Steps to debug |
| ---------- | ----------- | --------------- |
| Agent Builder | Debug di MCP server for di Agent Builder via AI Toolkit. | 1. Open VS Code Debug panel. Select `Debug in Agent Builder` and press `F5` to start debugging di MCP server.<br>2. Use AI Toolkit Agent Builder to test di server wit [dis prompt](../../../../../../../../../../../open_prompt_builder). Server go auto-connect to di Agent Builder.<br>3. Click `Run` to test di server wit di prompt. |
| MCP Inspector | Debug di MCP server wit MCP Inspector. | 1. Install [Node.js](https://nodejs.org/)<br> 2. Set up Inspector: `cd inspector` && `npm install` <br> 3. Open VS Code Debug panel. Select `Debug SSE in Inspector (Edge)` or `Debug SSE in Inspector (Chrome)`. Press F5 to start debugging.<br> 4. When MCP Inspector launch for di browser, click di `Connect` button to connect dis MCP server.<br> 5. Then you fit `List Tools`, select tool, input parameters, and `Run Tool` to debug your server code.<br> |

## Default Ports and customizations

| Debug Mode | Ports | Definitions | Customizations | Note |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) to change di ports. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Edit [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) to change di ports.| N/A |

## Feedback

If you get any feedback or suggestion for dis template, abeg open issue for di [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important information, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->