# Ilma MCP Server

See on näidis MCP server Pythonis, mis rakendab ilmatööriistu koos näidisvastustega. Seda saab kasutada oma MCP serveri alusena. See sisaldab järgmisi funktsioone:

- **Ilmatööriist**: Tööriist, mis pakub näidisilmainfot vastavalt antud asukohale.
- **Git Clone tööriist**: Tööriist, mis kloonib git-repositooriumi määratud kausta.
- **VS Code avamise tööriist**: Tööriist, mis avab kausta VS Code'is või VS Code Insidersis.
- **Ühendus Agent Builderiga**: Funktsioon, mis võimaldab MCP serveri ühendamist Agent Builderiga testimiseks ja silumiseks.
- **Silumine [MCP Inspectoris](https://github.com/modelcontextprotocol/inspector)**: Funktsioon, mis võimaldab MCP serveri silumist MCP Inspectoriga.

## Alustamine Ilma MCP Serveri malliga

> **Eeltingimused**
>
> MCP serveri käivitamiseks oma kohalikus arendusmasinas vajate:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Nõutav git_clone_repo tööriista jaoks)
> - [VS Code](https://code.visualstudio.com/) või [VS Code Insiders](https://code.visualstudio.com/insiders/) (Nõutav open_in_vscode tööriista jaoks)
> - (*Valikuline - kui eelistate uv-d*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Keskkonna ettevalmistamine

Selle projekti keskkonna seadistamiseks on kaks lähenemist. Valige endale sobiv.

> Märkus: Laadige VSCode või terminal uuesti, et tagada virtuaalse keskkonna Python kasutamine pärast selle loomist.

| Lähenemine | Sammud |
| ---------- | ------ |
| Kasutades `uv` | 1. Looge virtuaalne keskkond: `uv venv` <br>2. Käivitage VSCode käsk "***Python: Select Interpreter***" ja valige loodud virtuaalse keskkonna Python <br>3. Installige sõltuvused (sh arendussõltuvused): `uv pip install -r pyproject.toml --extra dev` |
| Kasutades `pip` | 1. Looge virtuaalne keskkond: `python -m venv .venv` <br>2. Käivitage VSCode käsk "***Python: Select Interpreter***" ja valige loodud virtuaalse keskkonna Python<br>3. Installige sõltuvused (sh arendussõltuvused): `pip install -e .[dev]` |

Pärast keskkonna seadistamist saate serveri käivitada oma kohalikus arendusmasinas Agent Builderi kaudu MCP kliendina:
1. Avage VS Code silumise paneel. Valige `Debug in Agent Builder` või vajutage `F5`, et alustada MCP serveri silumist.
2. Kasutage AI Toolkit Agent Builderit, et testida serverit [selle käsuga](../../../../../../../../../../../open_prompt_builder). Server ühendatakse automaatselt Agent Builderiga.
3. Klõpsake `Run`, et testida serverit käsuga.

**Palju õnne**! Olete edukalt käivitanud Ilma MCP Serveri oma kohalikus arendusmasinas Agent Builderi kaudu MCP kliendina.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mis on mallis kaasas

| Kaust / Fail | Sisu                                      |
| ------------ | ----------------------------------------- |
| `.vscode`    | VSCode failid silumiseks                  |
| `.aitk`      | AI Toolkiti konfiguratsioonid             |
| `src`        | Ilma MCP serveri lähtekood                |

## Kuidas siluda Ilma MCP Serverit

> Märkused:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalne arendustööriist MCP serverite testimiseks ja silumiseks.
> - Kõik silumisrežiimid toetavad katkestuspunkte, nii et saate lisada katkestuspunkte tööriista rakenduskoodi.

## Saadaval olevad tööriistad

### Ilmatööriist
`get_weather` tööriist pakub näidisilmainfot määratud asukoha kohta.

| Parameeter | Tüüp | Kirjeldus |
| ---------- | ---- | --------- |
| `location` | string | Asukoht, mille kohta ilmainfot küsitakse (nt linna nimi, osariik või koordinaadid) |

### Git Clone tööriist
`git_clone_repo` tööriist kloonib git-repositooriumi määratud kausta.

| Parameeter | Tüüp | Kirjeldus |
| ---------- | ---- | --------- |
| `repo_url` | string | Kloonitava git-repositooriumi URL |
| `target_folder` | string | Kausta tee, kuhu repositoorium peaks kloonitama |

Tööriist tagastab JSON objekti, mis sisaldab:
- `success`: Boolean, mis näitab, kas operatsioon õnnestus
- `target_folder` või `error`: Kloonitud repositooriumi tee või veateade

### VS Code avamise tööriist
`open_in_vscode` tööriist avab kausta VS Code'is või VS Code Insiders rakenduses.

| Parameeter | Tüüp | Kirjeldus |
| ---------- | ---- | --------- |
| `folder_path` | string | Kausta tee, mida avada |
| `use_insiders` | boolean (valikuline) | Kas kasutada VS Code Insidersit tavalise VS Code asemel |

Tööriist tagastab JSON objekti, mis sisaldab:
- `success`: Boolean, mis näitab, kas operatsioon õnnestus
- `message` või `error`: Kinnitussõnum või veateade

| Silumisrežiim | Kirjeldus | Sammud silumiseks |
| ------------- | --------- | ----------------- |
| Agent Builder | Siluge MCP serverit Agent Builderis AI Toolkiti kaudu. | 1. Avage VS Code silumise paneel. Valige `Debug in Agent Builder` ja vajutage `F5`, et alustada MCP serveri silumist.<br>2. Kasutage AI Toolkit Agent Builderit, et testida serverit [selle käsuga](../../../../../../../../../../../open_prompt_builder). Server ühendatakse automaatselt Agent Builderiga.<br>3. Klõpsake `Run`, et testida serverit käsuga. |
| MCP Inspector | Siluge MCP serverit MCP Inspectoriga. | 1. Installige [Node.js](https://nodejs.org/)<br> 2. Seadistage Inspector: `cd inspector` && `npm install` <br> 3. Avage VS Code silumise paneel. Valige `Debug SSE in Inspector (Edge)` või `Debug SSE in Inspector (Chrome)`. Vajutage F5, et alustada silumist.<br> 4. Kui MCP Inspector käivitub brauseris, klõpsake `Connect` nuppu, et ühendada see MCP server.<br> 5. Seejärel saate `List Tools`, valida tööriista, sisestada parameetrid ja `Run Tool`, et siluda oma serveri koodi.<br> |

## Vaikimisi pordid ja kohandused

| Silumisrežiim | Pordid | Definitsioonid | Kohandused | Märkus |
| ------------- | ------ | -------------- | ---------- | ------ |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muutke [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), et muuta ülaltoodud porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 ja 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muutke [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), et muuta ülaltoodud porte. | N/A |

## Tagasiside

Kui teil on selle malli kohta tagasisidet või ettepanekuid, avage probleem [AI Toolkiti GitHubi repositooriumis](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.