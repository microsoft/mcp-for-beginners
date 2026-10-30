# Ilma MCP-server

See on näide MCP-serverist Pythoni jaoks, mis sisaldab ilmatööriistu koos simuleeritud vastustega. Seda saab kasutada oma MCP-serveri lähtepunktina. See sisaldab järgmisi funktsioone: 

- **Weather Tool**: tööriist, mis pakub antud asukoha põhjal simuleeritud ilmainfot.
- **Git Clone Tool**: tööriist, mis kloonib git-repositsiooni määratud kausta.
- **VS Code Open Tool**: tööriist, mis avab kausta VS Code'is või VS Code Insiders'is.
- **Connect to Agent Builder**: funktsioon, mis võimaldab ühendada MCP-serveri Agent Builderiga testimiseks ja silumiseks.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: funktsioon, mis võimaldab teil siluda MCP-serverit, kasutades MCP Inspectorit.

## Alustamine Ilma MCP-serveri malliga

> **Eeltingimused**
>
> MCP-serveri käivitamiseks oma kohalikus arendusmasinas vajate:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Nõutav git_clone_repo tööriista jaoks)
> - [VS Code](https://code.visualstudio.com/) or [VS Code Insiders](https://code.visualstudio.com/insiders/) (Nõutav open_in_vscode tööriista jaoks)
> - (*Valikuline - kui eelistate uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Keskkonna ettevalmistamine

Selle projekti keskkonna seadistamiseks on kaks lähenemist. Valige üks vastavalt oma eelistustele.

> Märkus: Pärast virtuaalse keskkonna loomist taaskäivitage VSCode või terminal, et veenduda virtuaalse keskkonna Python'i kasutamises.

| Lähenemine | Sammud |
| -------- | ----- |
| Kasutades `uv` | 1. Loo virtuaalne keskkond: `uv venv` <br>2. Käivita VSCode käsk "***Python: Select Interpreter***" ja vali loodud virtuaalse keskkonna Python <br>3. Paigalda sõltuvused (ka arendussõltuvused): `uv pip install -r pyproject.toml --extra dev` |
| Kasutades `pip` | 1. Loo virtuaalne keskkond: `python -m venv .venv` <br>2. Käivita VSCode käsk "***Python: Select Interpreter***" ja vali loodud virtuaalse keskkonna Python<br>3. Paigalda sõltuvused (ka arendussõltuvused): `pip install -e .[dev]` | 

Pärast keskkonna seadistamist saate serveri oma kohalikus arendusmasinas käivitada Agent Builderi kaudu MCP-kliendina, et alustada:
1. Ava VS Code'i silumise paneel. Vali `Debug in Agent Builder` või vajuta `F5`, et alustada MCP-serveri silumist.
2. Microsoft Foundry Toolkit for Visual Studio Code Agent Builderis vali aktiivne Foundry juurutus nagu `gpt-5.1`, seejärel sisesta: `What is the weather in Shanghai?`. Server ühendub automaatselt.
3. Klõpsake `Run`, et testida serverit promptiga.

**Palju õnne**! Olete edukalt käivitanud Ilma MCP-serveri oma kohalikus arendusmasinas Agent Builderi kaudu MCP-kliendina.
![MCP silumine](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mida mall sisaldab

| Kaust / Fail| Sisu                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode failid silumiseks                   |
| `.aitk`      | Microsoft Foundry Toolkit konfiguratsioon      |
| `src`        | Ilma MCP-serveri lähtekood   |

## Kuidas siluda Ilma MCP-serverit

> Märkused:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalne arendajatööriist MCP-serverite testimiseks ja silumiseks.
> - Kõikide silumismoodide jaoks on toetatud katkestuspunktid, nii et saate lisada katkestuspunkte tööriista rakenduskoodi.

## Saadaval olevad tööriistad

### Weather Tool
Tööriist `get_weather` pakub määratud asukoha jaoks simuleeritud ilmainfot.

| Parameeter | Tüüp | Kirjeldus |
| --------- | ---- | ----------- |
| `location` | string | Asukoht, mille kohta saada ilm (nt linna nimi, osariik või koordinaadid) |

### Git Clone Tool
Tööriist `git_clone_repo` kloonib git-repositsiooni määratud kausta.

| Parameeter | Tüüp | Kirjeldus |
| --------- | ---- | ----------- |
| `repo_url` | string | Kloonitava git-repositsiooni URL |
| `target_folder` | string | Kausta tee, kuhu hoidla tuleks kloonida |

Tööriist tagastab JSON-objekti, mis sisaldab:
- `success`: boolean, mis näitab, kas operatsioon oli edukas
- `target_folder` või `error`: kloonitud hoidla tee või veateade

### VS Code Open Tool
Tööriist `open_in_vscode` avab kausta VS Code'is või VS Code Insiders rakenduses.

| Parameeter | Tüüp | Kirjeldus |
| --------- | ---- | ----------- |
| `folder_path` | string | Avatava kausta tee |
| `use_insiders` | boolean (optional) | Kas kasutada VS Code Insidersit tavapärase VS Code'i asemel |

Tööriist tagastab JSON-objekti, mis sisaldab:
- `success`: boolean, mis näitab, kas operatsioon oli edukas
- `message` või `error`: kinnitussõnum või veateade

| Silumisrežiim | Kirjeldus | Silumise sammud |
| ---------- | ----------- | --------------- |
| Agent Builder | Silumine MCP-serveri Agent Builderis Microsoft Foundry Toolkit for Visual Studio Code kaudu. | 1. Ava VS Code'i silumise paneel. Vali `Debug in Agent Builder` ja vajuta `F5`, et alustada MCP-serveri silumist.<br>2. Vali aktiivne Foundry juurutus nagu `gpt-5.1`, seejärel sisesta `What is the weather in Shanghai?`. Server ühendub automaatselt.<br>3. Klõpsake `Run`, et testida serverit promptiga. |
| MCP Inspector | Siluda MCP-serverit, kasutades MCP Inspectorit. | 1. Installige [Node.js](https://nodejs.org/)<br> 2. Seadistage Inspector: `cd inspector` && `npm install` <br> 3. Avage VS Code'i silumise paneel. Valige `Debug SSE in Inspector (Edge)` või `Debug SSE in Inspector (Chrome)`. Vajutage F5, et alustada silumist.<br> 4. Kui MCP Inspector käivitub brauseris, klõpsake nuppu `Connect`, et ühendada see MCP-server.<br> 5. Seejärel saate `List Tools`, valida tööriista, sisestada parameetrid ja `Run Tool`, et siluda oma serveri koodi.<br> |

## Vaikimisi pordid ja kohandused

| Silumisrežiim | Pordid | Määratlused | Kohandused | Märkus |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muuda ülaltoodud porte redigeerides [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json). | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Muuda ülaltoodud porte redigeerides [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json).| N/A |

## Tagasiside

Kui teil on selle malli kohta tagasisidet või ettepanekuid, palun avage issue [Microsoft Foundry Toolkit for Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->