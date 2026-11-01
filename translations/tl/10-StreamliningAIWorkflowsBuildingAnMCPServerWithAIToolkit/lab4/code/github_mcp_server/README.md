# Weather MCP Server

Ito ay isang halimbawa ng MCP Server sa Python na nagpapatupad ng mga tool sa panahon na may mga mock na tugon. Maaari itong gamitin bilang panimulang balangkas para sa iyong sariling MCP Server. Kasama nito ang mga sumusunod na tampok:

- **Weather Tool**: Isang tool na nagbibigay ng mock na impormasyon sa panahon batay sa ibinigay na lokasyon.
- **Git Clone Tool**: Isang tool na kumokopya ng isang git repository patungo sa isang tinukoy na folder.
- **VS Code Open Tool**: Isang tool na nagbubukas ng folder sa VS Code o VS Code Insiders.
- **Connect to Agent Builder**: Isang tampok na nagpapahintulot sa iyo na ikonekta ang MCP server sa Agent Builder para sa pagsubok at debugging.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Isang tampok na nagpapahintulot sa iyo na i-debug ang MCP Server gamit ang MCP Inspector.

## Pagsisimula gamit ang Weather MCP Server template

> **Mga Kinakailangan**
>
> Para patakbuhin ang MCP Server sa iyong lokal na dev machine, kakailanganin mo:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Kinakailangan para sa git_clone_repo tool)
> - [VS Code](https://code.visualstudio.com/) o [VS Code Insiders](https://code.visualstudio.com/insiders/) (Kinakailangan para sa open_in_vscode tool)
> - (*Opsyonal - kung nais mo ng uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ihanda ang kapaligiran

May dalawang paraan upang isaayos ang kapaligiran para sa proyektong ito. Maaari kang pumili ng alinman batay sa iyong kagustuhan.

> Tandaan: I-reload ang VSCode o terminal upang matiyak na ang python ng virtual environment ang gagamitin matapos malikha ang virtual environment.

| Pamamaraan | Mga Hakbang |
| -------- | ----- |
| Paggamit ng `uv` | 1. Gumawa ng virtual environment: `uv venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa nilikhang virtual environment <br>3. I-install ang mga dependencies (kasama ang dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Paggamit ng `pip` | 1. Gumawa ng virtual environment: `python -m venv .venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa nilikhang virtual environment<br>3. I-install ang mga dependencies (kasama ang dev dependencies): `pip install -e .[dev]` |

Pagkatapos isaayos ang kapaligiran, maaari mong patakbuhin ang server sa iyong lokal na dev machine gamit ang Agent Builder bilang MCP Client upang makapagsimula:
1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` o pindutin ang `F5` upang simulan ang pag-debug ng MCP server.
2. Sa Microsoft Foundry Toolkit para sa Visual Studio Code Agent Builder, piliin ang aktibong Foundry deployment tulad ng `gpt-5.1`, pagkatapos ay ipasok: `What is the weather in Shanghai?` Awtomatikong ikokonekta ang server.
3. I-click ang `Run` upang subukan ang server gamit ang prompt.

**Binabati kita**! Matagumpay mong naipatakbo ang Weather MCP Server sa iyong lokal na dev machine gamit ang Agent Builder bilang MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Ano ang kasama sa template

| Folder / File| Nilalaman                                    |
| ------------ | -------------------------------------------- |
| `.vscode`    | Mga file ng VSCode para sa debugging         |
| `.aitk`      | Microsoft Foundry Toolkit configuration      |
| `src`        | Ang source code para sa weather mcp server   |

## Paano mag-debug ng Weather MCP Server

> Mga Tala:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay isang visual na developer tool para sa pagsusuri at pag-debug ng MCP servers.
> - Lahat ng modo ng pag-debug ay sumusuporta sa breakpoints, kaya maaari kang magdagdag ng breakpoints sa code ng implementasyon ng tool.

## Mga Magagamit na Tool

### Weather Tool
Ang `get_weather` tool ay nagbibigay ng mock na impormasyon tungkol sa panahon para sa tinukoy na lokasyon.

| Parameter | Uri | Paglalarawan |
| --------- | ---- | ----------- |
| `location` | string | Lokasyon para kunin ang panahon (hal., pangalan ng lungsod, estado, o coordinates) |

### Git Clone Tool
Ang `git_clone_repo` tool ay kumokopya ng git repository sa isang tinukoy na folder.

| Parameter | Uri | Paglalarawan |
| --------- | ---- | ----------- |
| `repo_url` | string | URL ng git repository na kokopyahin |
| `target_folder` | string | Path ng folder kung saan kokopyahin ang repository |

Ang tool ay nagbabalik ng isang JSON object na may:
- `success`: Boolean na nagsasaad kung matagumpay ang operasyon
- `target_folder` o `error`: Ang path ng kinopyang repository o isang mensahe ng error

### VS Code Open Tool
Ang `open_in_vscode` tool ay nagbubukas ng folder sa VS Code o VS Code Insiders na aplikasyon.

| Parameter | Uri | Paglalarawan |
| --------- | ---- | ----------- |
| `folder_path` | string | Path ng folder na bubuksan |
| `use_insiders` | boolean (opsyonal) | Kung gagamitin ang VS Code Insiders imbes na regular na VS Code |

Ang tool ay nagbabalik ng isang JSON object na may:
- `success`: Boolean na nagsasaad kung matagumpay ang operasyon
- `message` o `error`: Isang kumpirmasyon na mensahe o isang error na mensahe

| Debug Mode | Paglalarawan | Mga Hakbang sa pag-debug |
| ---------- | ----------- | --------------- |
| Agent Builder | I-debug ang MCP server sa Agent Builder gamit ang Microsoft Foundry Toolkit para sa Visual Studio Code. | 1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` at pindutin ang `F5` upang simulan ang pag-debug ng MCP server.<br>2. Piliin ang aktibong Foundry deployment tulad ng `gpt-5.1`, pagkatapos ay ipasok ang `What is the weather in Shanghai?`. Awtomatikong ikokonekta ang server.<br>3. I-click ang `Run` upang subukan ang server gamit ang prompt. |
| MCP Inspector | I-debug ang MCP server gamit ang MCP Inspector. | 1. I-install ang [Node.js](https://nodejs.org/)<br> 2. Isaayos ang Inspector: `cd inspector` && `npm install` <br> 3. Buksan ang VS Code Debug panel. Piliin ang `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Pindutin ang F5 upang simulan ang pag-debug.<br> 4. Kapag nagbukas ang MCP Inspector sa browser, i-click ang `Connect` button upang ikonekta ang MCP server na ito.<br> 5. Pagkatapos ay maaari mong `List Tools`, pumili ng tool, magpasok ng mga parameter, at `Run Tool` upang i-debug ang iyong server code.<br> |

## Default Ports at mga customizations

| Debug Mode | Mga Port | Mga Kahulugan | Mga Customization | Tala |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) upang baguhin ang mga port sa itaas. | Walang Anumang |
| MCP Inspector | 3001 (Server); 5173 at 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) upang baguhin ang mga port sa itaas.| Walang Anumang |

## Feedback

Kung mayroon kang anumang puna o mungkahi para sa template na ito, mangyaring magbukas ng isyu sa [Microsoft Foundry Toolkit para sa Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->