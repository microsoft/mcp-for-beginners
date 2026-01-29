# Weather MCP Server

Huu ni mfano wa MCP Server katika Python unaotekeleza zana za hali ya hewa kwa majibu ya mfano. Inaweza kutumika kama msingi wa MCP Server yako mwenyewe. Inajumuisha vipengele vifuatavyo:

- **Zana ya Hali ya Hewa**: Zana inayotoa taarifa za hali ya hewa za mfano kulingana na eneo lililotolewa.
- **Unganisha na Agent Builder**: Kipengele kinachokuwezesha kuunganisha MCP server na Agent Builder kwa ajili ya majaribio na utatuzi.
- **Tatua matatizo katika [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Kipengele kinachokuwezesha kutatua matatizo ya MCP Server kwa kutumia MCP Inspector.

## Anza na kiolezo cha Weather MCP Server

> **Mahitaji ya awali**
>
> Ili kuendesha MCP Server kwenye mashine yako ya maendeleo ya ndani, utahitaji:
>
> - [Python](https://www.python.org/)
> - (*Hiari - ikiwa unapendelea uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Andaa mazingira

Kuna njia mbili za kuandaa mazingira kwa mradi huu. Unaweza kuchagua moja kulingana na upendeleo wako.

> Kumbuka: Reload VSCode au terminal ili kuhakikisha python ya mazingira pepe inatumika baada ya kuunda mazingira pepe.

| Njia | Hatua |
| -------- | ----- |
| Kutumia `uv` | 1. Unda mazingira pepe: `uv venv` <br>2. Endesha Amri ya VSCode "***Python: Select Interpreter***" na chagua python kutoka mazingira pepe yaliyoundwa <br>3. Sakinisha utegemezi (pamoja na utegemezi wa maendeleo): `uv pip install -r pyproject.toml --extra dev` |
| Kutumia `pip` | 1. Unda mazingira pepe: `python -m venv .venv` <br>2. Endesha Amri ya VSCode "***Python: Select Interpreter***" na chagua python kutoka mazingira pepe yaliyoundwa<br>3. Sakinisha utegemezi (pamoja na utegemezi wa maendeleo): `pip install -e .[dev]` |

Baada ya kuandaa mazingira, unaweza kuendesha server kwenye mashine yako ya maendeleo ya ndani kupitia Agent Builder kama MCP Client kuanza:
1. Fungua paneli ya Debug ya VS Code. Chagua `Debug in Agent Builder` au bonyeza `F5` kuanza kutatua matatizo ya MCP server.
2. Tumia AI Toolkit Agent Builder kujaribu server kwa [prompt hii](../../../../../../../../../../open_prompt_builder). Server itajiunga moja kwa moja na Agent Builder.
3. Bonyeza `Run` kujaribu server na prompt.

**Hongera**! Umefanikiwa kuendesha Weather MCP Server kwenye mashine yako ya maendeleo ya ndani kupitia Agent Builder kama MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Kile kilichojumuishwa kwenye kiolezo

| Folda / Faili | Yaliyomo                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Faili za VSCode kwa ajili ya utatuzi          |
| `.aitk`      | Mipangilio ya AI Toolkit                      |
| `src`        | Chanzo cha msimbo wa weather mcp server      |

## Jinsi ya kutatua matatizo ya Weather MCP Server

> Vidokezo:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ni zana ya kuona kwa mtengenezaji kwa ajili ya majaribio na utatuzi wa MCP servers.
> - Njia zote za utatuzi zinaunga mkono breakpoints, hivyo unaweza kuongeza breakpoints kwenye msimbo wa utekelezaji wa zana.

| Njia ya Utatuzi | Maelezo | Hatua za kutatua matatizo |
| ---------- | ----------- | --------------- |
| Agent Builder | Tatua matatizo ya MCP server katika Agent Builder kupitia AI Toolkit. | 1. Fungua paneli ya Debug ya VS Code. Chagua `Debug in Agent Builder` na bonyeza `F5` kuanza kutatua matatizo ya MCP server.<br>2. Tumia AI Toolkit Agent Builder kujaribu server na [prompt hii](../../../../../../../../../../open_prompt_builder). Server itajiunga moja kwa moja na Agent Builder.<br>3. Bonyeza `Run` kujaribu server na prompt. |
| MCP Inspector | Tatua matatizo ya MCP server kwa kutumia MCP Inspector. | 1. Sakinisha [Node.js](https://nodejs.org/)<br> 2. Andaa Inspector: `cd inspector` && `npm install` <br> 3. Fungua paneli ya Debug ya VS Code. Chagua `Debug SSE in Inspector (Edge)` au `Debug SSE in Inspector (Chrome)`. Bonyeza F5 kuanza kutatua matatizo.<br> 4. Wakati MCP Inspector inapoanzishwa kwenye kivinjari, bonyeza kitufe cha `Connect` kuunganisha MCP server hii.<br> 5. Kisha unaweza `List Tools`, chagua zana, ingiza vigezo, na `Run Tool` kutatua matatizo ya msimbo wa server yako.<br> |

## Bandari za Msingi na mabadiliko

| Njia ya Utatuzi | Bandari | Maelezo | Mabadiliko | Kumbuka |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Hariri [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) kubadilisha bandari zilizo hapo juu. | Haina |
| MCP Inspector | 3001 (Server); 5173 na 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Hariri [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) kubadilisha bandari zilizo hapo juu.| Haina |

## Maoni

Kama una maoni au mapendekezo kuhusu kiolezo hiki, tafadhali fungua tatizo kwenye [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.