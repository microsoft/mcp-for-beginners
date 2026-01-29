# Seva ya Hali ya Hewa MCP

Hii ni mfano wa Seva ya MCP iliyoandikwa kwa Python inayotekeleza zana za hali ya hewa na majibu ya mfano. Inaweza kutumika kama msingi wa kuunda Seva yako ya MCP. Inajumuisha vipengele vifuatavyo:

- **Zana ya Hali ya Hewa**: Zana inayotoa taarifa za hali ya hewa za mfano kulingana na eneo lililotolewa.
- **Zana ya Kloni ya Git**: Zana inayokloni hifadhi ya git kwenye folda maalum.
- **Zana ya Kufungua VS Code**: Zana inayofungua folda kwenye VS Code au VS Code Insiders.
- **Unganisha na Agent Builder**: Kipengele kinachokuwezesha kuunganisha seva ya MCP na Agent Builder kwa majaribio na urekebishaji.
- **Urekebishaji katika [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Kipengele kinachokuwezesha kurekebisha seva ya MCP kwa kutumia MCP Inspector.

## Anza na kiolezo cha Seva ya Hali ya Hewa MCP

> **Mahitaji ya Awali**
>
> Ili kuendesha Seva ya MCP kwenye mashine yako ya maendeleo ya ndani, utahitaji:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Inahitajika kwa zana ya git_clone_repo)
> - [VS Code](https://code.visualstudio.com/) au [VS Code Insiders](https://code.visualstudio.com/insiders/) (Inahitajika kwa zana ya open_in_vscode)
> - (*Hiari - ikiwa unapendelea uv*) [uv](https://github.com/astral-sh/uv)
> - [Kiendelezi cha Urekebishaji wa Python](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Andaa mazingira

Kuna njia mbili za kuandaa mazingira kwa mradi huu. Unaweza kuchagua mojawapo kulingana na upendeleo wako.

> Kumbuka: Pakia upya VSCode au terminal ili kuhakikisha python ya mazingira ya kawaida inatumika baada ya kuunda mazingira ya kawaida.

| Njia | Hatua |
| -------- | ----- |
| Kutumia `uv` | 1. Unda mazingira ya kawaida: `uv venv` <br>2. Endesha Amri ya VSCode "***Python: Select Interpreter***" na uchague python kutoka mazingira ya kawaida yaliyoandaliwa <br>3. Sakinisha utegemezi (pamoja na utegemezi wa maendeleo): `uv pip install -r pyproject.toml --extra dev` |
| Kutumia `pip` | 1. Unda mazingira ya kawaida: `python -m venv .venv` <br>2. Endesha Amri ya VSCode "***Python: Select Interpreter***" na uchague python kutoka mazingira ya kawaida yaliyoandaliwa<br>3. Sakinisha utegemezi (pamoja na utegemezi wa maendeleo): `pip install -e .[dev]` | 

Baada ya kuandaa mazingira, unaweza kuendesha seva kwenye mashine yako ya maendeleo ya ndani kupitia Agent Builder kama MCP Client ili kuanza:
1. Fungua paneli ya Urekebishaji ya VS Code. Chagua `Debug in Agent Builder` au bonyeza `F5` kuanza kurekebisha seva ya MCP.
2. Tumia AI Toolkit Agent Builder kujaribu seva kwa [hii maelekezo](../../../../../../../../../../../open_prompt_builder). Seva itaunganishwa kiotomatiki na Agent Builder.
3. Bonyeza `Run` kujaribu seva kwa maelekezo.

**Hongera**! Umefanikiwa kuendesha Seva ya Hali ya Hewa MCP kwenye mashine yako ya maendeleo ya ndani kupitia Agent Builder kama MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Nini kimejumuishwa kwenye kiolezo

| Folda / Faili | Yaliyomo                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | Faili za VSCode kwa urekebishaji             |
| `.aitk`      | Usanidi wa AI Toolkit                        |
| `src`        | Msimbo wa chanzo wa seva ya hali ya hewa MCP |

## Jinsi ya kurekebisha Seva ya Hali ya Hewa MCP

> Vidokezo:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ni zana ya kuona ya msanidi programu kwa majaribio na urekebishaji wa seva za MCP.
> - Hali zote za urekebishaji zinaunga mkono alama za kusimamisha, kwa hivyo unaweza kuongeza alama za kusimamisha kwenye msimbo wa utekelezaji wa zana.

## Zana Zinazopatikana

### Zana ya Hali ya Hewa
Zana ya `get_weather` inatoa taarifa za hali ya hewa za mfano kwa eneo maalum.

| Kigezo | Aina | Maelezo |
| --------- | ---- | ----------- |
| `location` | string | Eneo la kupata hali ya hewa (mfano, jina la mji, jimbo, au kuratibu) |

### Zana ya Kloni ya Git
Zana ya `git_clone_repo` inakloni hifadhi ya git kwenye folda maalum.

| Kigezo | Aina | Maelezo |
| --------- | ---- | ----------- |
| `repo_url` | string | URL ya hifadhi ya git ya kukloni |
| `target_folder` | string | Njia ya folda ambapo hifadhi inapaswa kukloniwa |

Zana inarudisha kitu cha JSON chenye:
- `success`: Boolean inayoonyesha ikiwa operesheni imefanikiwa
- `target_folder` au `error`: Njia ya hifadhi iliyokloniwa au ujumbe wa kosa

### Zana ya Kufungua VS Code
Zana ya `open_in_vscode` inafungua folda kwenye programu ya VS Code au VS Code Insiders.

| Kigezo | Aina | Maelezo |
| --------- | ---- | ----------- |
| `folder_path` | string | Njia ya folda ya kufungua |
| `use_insiders` | boolean (hiari) | Ikiwa utumie VS Code Insiders badala ya VS Code ya kawaida |

Zana inarudisha kitu cha JSON chenye:
- `success`: Boolean inayoonyesha ikiwa operesheni imefanikiwa
- `message` au `error`: Ujumbe wa uthibitisho au ujumbe wa kosa

| Hali ya Urekebishaji | Maelezo | Hatua za kurekebisha |
| ---------- | ----------- | --------------- |
| Agent Builder | Rekebisha seva ya MCP kwenye Agent Builder kupitia AI Toolkit. | 1. Fungua paneli ya Urekebishaji ya VS Code. Chagua `Debug in Agent Builder` na bonyeza `F5` kuanza kurekebisha seva ya MCP.<br>2. Tumia AI Toolkit Agent Builder kujaribu seva kwa [hii maelekezo](../../../../../../../../../../../open_prompt_builder). Seva itaunganishwa kiotomatiki na Agent Builder.<br>3. Bonyeza `Run` kujaribu seva kwa maelekezo. |
| MCP Inspector | Rekebisha seva ya MCP kwa kutumia MCP Inspector. | 1. Sakinisha [Node.js](https://nodejs.org/)<br> 2. Andaa Inspector: `cd inspector` && `npm install` <br> 3. Fungua paneli ya Urekebishaji ya VS Code. Chagua `Debug SSE in Inspector (Edge)` au `Debug SSE in Inspector (Chrome)`. Bonyeza F5 kuanza kurekebisha.<br> 4. Wakati MCP Inspector inazinduliwa kwenye kivinjari, bonyeza kitufe cha `Connect` kuunganisha seva hii ya MCP.<br> 5. Kisha unaweza `List Tools`, chagua zana, ingiza vigezo, na `Run Tool` kurekebisha msimbo wa seva yako.<br> |

## Bandari Chaguo-msingi na ubinafsishaji

| Hali ya Urekebishaji | Bandari | Maelezo | Ubinafsishaji | Kumbuka |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Hariri [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) kubadilisha bandari zilizo hapo juu. | N/A |
| MCP Inspector | 3001 (Seva); 5173 na 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Hariri [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) kubadilisha bandari zilizo hapo juu.| N/A |

## Maoni

Ikiwa una maoni au mapendekezo yoyote kwa kiolezo hiki, tafadhali fungua suala kwenye [hifadhi ya GitHub ya AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.