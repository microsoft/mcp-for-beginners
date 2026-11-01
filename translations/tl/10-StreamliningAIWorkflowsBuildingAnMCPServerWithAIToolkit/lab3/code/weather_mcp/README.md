# Weather MCP Server

Ito ay isang halimbawa ng MCP Server sa Python na nagpapatupad ng mga tool sa panahon kasama ang mga pekeng tugon. Maaari itong gamitin bilang isang balangkas para sa iyong sariling MCP Server. Kasama nito ang mga sumusunod na tampok:

- **Weather Tool**: Isang tool na nagbibigay ng pekeng impormasyon sa panahon batay sa ibinigay na lokasyon.
- **Connect to Agent Builder**: Isang tampok na nagpapahintulot sa iyo na ikonekta ang MCP server sa Agent Builder para sa pagsubok at pag-debug.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Isang tampok na nagpapahintulot sa iyo na i-debug ang MCP Server gamit ang MCP Inspector.

## Magsimula gamit ang Weather MCP Server template

> **Mga Kinakailangan**
>
> Upang patakbuhin ang MCP Server sa iyong lokal na makina ng dev, kakailanganin mo:
>
> - [Python](https://www.python.org/)
> - (*Opsyonal - kung mas gusto mo ang uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ihanda ang kapaligiran

May dalawang paraan upang i-setup ang kapaligiran para sa proyekto na ito. Maaari kang pumili alinman batay sa iyong kagustuhan.

> Tala: I-reload ang VSCode o terminal upang matiyak na ginagamit ang virtual environment python matapos likhain ang virtual environment.

| Paraan | Mga Hakbang |
| -------- | ----- |
| Paggamit ng `uv` | 1. Gumawa ng virtual environment: `uv venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa nilikhang virtual environment <br>3. I-install ang mga dependencies (kasama ang dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Paggamit ng `pip` | 1. Gumawa ng virtual environment: `python -m venv .venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa nilikhang virtual environment<br>3. I-install ang mga dependencies (kasama ang dev dependencies): `pip install -e .[dev]` | 

Pagkatapos i-setup ang kapaligiran, maaari mong patakbuhin ang server sa iyong lokal na makina ng dev sa pamamagitan ng Agent Builder bilang MCP Client upang magsimula:
1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` o pindutin ang `F5` upang simulan ang pag-debug ng MCP server.
2. Sa Microsoft Foundry Toolkit Agent Builder, piliin ang isang aktibong Foundry deployment tulad ng `gpt-5.1`, pagkatapos ay ilagay: `What is the weather in Shanghai?` Awtomatikong makakonekta ang server.
3. I-click ang `Run` upang subukan ang server gamit ang prompt.

**Congratulations**! Matagumpay mong naipatakbo ang Weather MCP Server sa iyong lokal na makina ng dev sa pamamagitan ng Agent Builder bilang MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Ano ang kasama sa template

| Folder / File| Nilalaman                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Mga file ng VSCode para sa pag-debug                   |
| `.aitk`      | Mga Configuration para sa Microsoft Foundry Toolkit                |
| `src`        | Ang source code para sa weather mcp server   |

## Paano mag-debug ng Weather MCP Server

> Mga Tala:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay isang visual developer tool para sa pagsubok at pag-debug ng MCP servers.
> - Lahat ng debugging mode ay sumusuporta sa breakpoints, kaya maaari kang magdagdag ng mga breakpoint sa tool implementation code.

| Debug Mode | Paglalarawan | Mga Hakbang sa pag-debug |
| ---------- | ----------- | --------------- |
| Agent Builder | I-debug ang MCP server sa Agent Builder sa pamamagitan ng Microsoft Foundry Toolkit. | 1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` at pindutin ang `F5` upang simulan ang pag-debug ng MCP server.<br>2. Piliin ang isang aktibong Foundry deployment tulad ng `gpt-5.1`, pagkatapos ilagay ang `What is the weather in Shanghai?`. Awtomatikong makakonekta ang server.<br>3. I-click ang `Run` upang subukan ang server gamit ang prompt. |
| MCP Inspector | I-debug ang MCP server gamit ang MCP Inspector. | 1. I-install ang [Node.js](https://nodejs.org/)<br> 2. I-setup ang Inspector: `cd inspector` && `npm install` <br> 3. Buksan ang VS Code Debug panel. Piliin ang `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Pindutin ang F5 upang simulan ang pag-debug.<br> 4. Kapag na-launch ang MCP Inspector sa browser, i-click ang `Connect` button upang ikonekta ang MCP server na ito.<br> 5. Pagkatapos maaari mong `List Tools`, pumili ng tool, mag-input ng mga parameter, at `Run Tool` upang i-debug ang iyong server code.<br> |

## Mga Default na Port at mga customizations

| Debug Mode | Mga Port | Mga Kahulugan | Mga Customizations | Tala |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) upang baguhin ang mga port sa itaas. | Wala |
| MCP Inspector | 3001 (Server); 5173 at 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) upang baguhin ang mga port sa itaas.| Wala |

## Feedback

Kung mayroon kang anumang feedback o mungkahi para sa template na ito, mangyaring magbukas ng isyu sa [Microsoft Foundry Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->