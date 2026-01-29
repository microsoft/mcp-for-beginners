# Weather MCP Server

Ito ay isang sample na MCP Server sa Python na nag-iimplementa ng mga kasangkapan sa panahon gamit ang mock na mga tugon. Maaari itong gamitin bilang balangkas para sa iyong sariling MCP Server. Kasama nito ang mga sumusunod na tampok:

- **Weather Tool**: Isang kasangkapan na nagbibigay ng mock na impormasyon sa panahon batay sa ibinigay na lokasyon.
- **Git Clone Tool**: Isang kasangkapan na nagko-clone ng git repository sa tinukoy na folder.
- **VS Code Open Tool**: Isang kasangkapan na nagbubukas ng folder sa VS Code o VS Code Insiders.
- **Connect to Agent Builder**: Isang tampok na nagbibigay-daan sa iyo na ikonekta ang MCP server sa Agent Builder para sa pagsubok at pag-debug.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Isang tampok na nagbibigay-daan sa iyo na i-debug ang MCP Server gamit ang MCP Inspector.

## Paano magsimula gamit ang Weather MCP Server template

> **Mga Kinakailangan**
>
> Upang patakbuhin ang MCP Server sa iyong lokal na dev machine, kakailanganin mo:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Kinakailangan para sa git_clone_repo tool)
> - [VS Code](https://code.visualstudio.com/) o [VS Code Insiders](https://code.visualstudio.com/insiders/) (Kinakailangan para sa open_in_vscode tool)
> - (*Opsyonal - kung mas gusto mo ang uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Ihanda ang kapaligiran

May dalawang paraan upang i-set up ang kapaligiran para sa proyektong ito. Maaari kang pumili ng alinman batay sa iyong kagustuhan.

> Tandaan: I-reload ang VSCode o terminal upang matiyak na ginagamit ang virtual environment python pagkatapos gumawa ng virtual environment.

| Paraan | Mga Hakbang |
| ------ | ----------- |
| Gamit ang `uv` | 1. Gumawa ng virtual environment: `uv venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa ginawa na virtual environment <br>3. I-install ang mga dependencies (kasama ang dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Gamit ang `pip` | 1. Gumawa ng virtual environment: `python -m venv .venv` <br>2. Patakbuhin ang VSCode Command "***Python: Select Interpreter***" at piliin ang python mula sa ginawa na virtual environment<br>3. I-install ang mga dependencies (kasama ang dev dependencies): `pip install -e .[dev]` | 

Pagkatapos i-set up ang kapaligiran, maaari mong patakbuhin ang server sa iyong lokal na dev machine gamit ang Agent Builder bilang MCP Client upang magsimula:
1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` o pindutin ang `F5` upang simulan ang pag-debug ng MCP server.
2. Gamitin ang AI Toolkit Agent Builder upang subukan ang server gamit ang [prompt na ito](../../../../../../../../../../../open_prompt_builder). Ang server ay awtomatikong makokonekta sa Agent Builder.
3. I-click ang `Run` upang subukan ang server gamit ang prompt.

**Binabati kita**! Matagumpay mong napatakbo ang Weather MCP Server sa iyong lokal na dev machine gamit ang Agent Builder bilang MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Ano ang kasama sa template

| Folder / File| Nilalaman                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Mga file ng VSCode para sa pag-debug          |
| `.aitk`      | Mga configuration para sa AI Toolkit         |
| `src`        | Ang source code para sa weather MCP server    |

## Paano i-debug ang Weather MCP Server

> Mga Tala:
> - Ang [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ay isang visual developer tool para sa pagsubok at pag-debug ng MCP servers.
> - Ang lahat ng mga mode ng pag-debug ay sumusuporta sa breakpoints, kaya maaari kang magdagdag ng breakpoints sa code ng tool implementation.

## Mga Available na Kasangkapan

### Weather Tool
Ang `get_weather` tool ay nagbibigay ng mock na impormasyon sa panahon para sa isang tinukoy na lokasyon.

| Parameter | Uri | Deskripsyon |
| --------- | --- | ----------- |
| `location` | string | Lokasyon kung saan kukunin ang impormasyon sa panahon (hal., pangalan ng lungsod, estado, o coordinates) |

### Git Clone Tool
Ang `git_clone_repo` tool ay nagko-clone ng isang git repository sa isang tinukoy na folder.

| Parameter | Uri | Deskripsyon |
| --------- | --- | ----------- |
| `repo_url` | string | URL ng git repository na iko-clone |
| `target_folder` | string | Path sa folder kung saan dapat i-clone ang repository |

Ang tool ay nagbabalik ng JSON object na may:
- `success`: Boolean na nagpapahiwatig kung matagumpay ang operasyon
- `target_folder` o `error`: Ang path ng cloned repository o isang error message

### VS Code Open Tool
Ang `open_in_vscode` tool ay nagbubukas ng folder sa VS Code o VS Code Insiders application.

| Parameter | Uri | Deskripsyon |
| --------- | --- | ----------- |
| `folder_path` | string | Path sa folder na bubuksan |
| `use_insiders` | boolean (opsyonal) | Kung gagamit ng VS Code Insiders sa halip na regular na VS Code |

Ang tool ay nagbabalik ng JSON object na may:
- `success`: Boolean na nagpapahiwatig kung matagumpay ang operasyon
- `message` o `error`: Isang kumpirmasyon o isang error message

| Mode ng Debug | Deskripsyon | Mga Hakbang sa Pag-debug |
| ------------- | ----------- | ------------------------ |
| Agent Builder | I-debug ang MCP server sa Agent Builder gamit ang AI Toolkit. | 1. Buksan ang VS Code Debug panel. Piliin ang `Debug in Agent Builder` at pindutin ang `F5` upang simulan ang pag-debug ng MCP server.<br>2. Gamitin ang AI Toolkit Agent Builder upang subukan ang server gamit ang [prompt na ito](../../../../../../../../../../../open_prompt_builder). Ang server ay awtomatikong makokonekta sa Agent Builder.<br>3. I-click ang `Run` upang subukan ang server gamit ang prompt. |
| MCP Inspector | I-debug ang MCP server gamit ang MCP Inspector. | 1. I-install ang [Node.js](https://nodejs.org/)<br> 2. I-set up ang Inspector: `cd inspector` && `npm install` <br> 3. Buksan ang VS Code Debug panel. Piliin ang `Debug SSE in Inspector (Edge)` o `Debug SSE in Inspector (Chrome)`. Pindutin ang F5 upang simulan ang pag-debug.<br> 4. Kapag nag-launch ang MCP Inspector sa browser, i-click ang `Connect` button upang ikonekta ang MCP server.<br> 5. Pagkatapos, maaari mong `List Tools`, piliin ang tool, mag-input ng parameters, at `Run Tool` upang i-debug ang iyong server code.<br> |

## Default Ports at mga customizations

| Mode ng Debug | Ports | Mga Kahulugan | Mga Customizations | Tala |
| ------------- | ----- | ------------- | ------------------ | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) upang baguhin ang mga ports sa itaas. | N/A |
| MCP Inspector | 3001 (Server); 5173 at 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | I-edit ang [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) upang baguhin ang mga ports sa itaas.| N/A |

## Feedback

Kung mayroon kang anumang feedback o mungkahi para sa template na ito, mangyaring magbukas ng isyu sa [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.