# Ilma MCP Server

See on näidis MCP server Pythonis, mis rakendab ilmatööriistu koos näidisvastustega. Seda saab kasutada oma MCP serveri alusena. See sisaldab järgmisi funktsioone:

- **Ilmatööriist**: Tööriist, mis pakub näidisena ilmainfot vastavalt antud asukohale.
- **Ühendus Agent Builderiga**: Funktsioon, mis võimaldab MCP serveri ühendada Agent Builderiga testimiseks ja silumiseks.
- **Silumine [MCP Inspectoris](https://github.com/modelcontextprotocol/inspector)**: Funktsioon, mis võimaldab MCP serverit siluda MCP Inspectoriga.

## Alustamine Ilma MCP Serveri malliga

> **Eeltingimused**
>
> MCP serveri käivitamiseks oma kohalikus arendusmasinas on vaja:
>
> - [Python](https://www.python.org/)
> - (*Valikuline - kui eelistate uv-d*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Keskkonna ettevalmistamine

Selle projekti keskkonna seadistamiseks on kaks lähenemisviisi. Valige endale sobivaim.

> Märkus: Taaskäivitage VSCode või terminal, et veenduda, et virtuaalse keskkonna Python on kasutusel pärast selle loomist.

| Lähenemine | Sammud |
| ---------- | ------ |
| Kasutades `uv` | 1. Loo virtuaalne keskkond: `uv venv` <br>2. Käivitage VSCode käsk "***Python: Select Interpreter***" ja valige loodud virtuaalse keskkonna Python <br>3. Installige sõltuvused (sh arendussõltuvused): `uv pip install -r pyproject.toml --extra dev` |
| Kasutades `pip` | 1. Loo virtuaalne keskkond: `python -m venv .venv` <br>2. Käivitage VSCode käsk "***Python: Select Interpreter***" ja valige loodud virtuaalse keskkonna Python<br>3. Installige sõltuvused (sh arendussõltuvused): `pip install -e .[dev]` |

Pärast keskkonna seadistamist saate serveri oma kohalikus arendusmasinas käivitada, kasutades Agent Builderit MCP kliendina alustamiseks:
1. Avage VS Code silumispaneel. Valige `Debug in Agent Builder` või vajutage `F5`, et alustada MCP serveri silumist.
2. Kasutage AI Toolkit Agent Builderit, et testida serverit [selle käsuga](../../../../../../../../../../../open_prompt_builder). Server ühendatakse automaatselt Agent Builderiga.
3. Klõpsake `Run`, et testida serverit käsuga.

**Palju õnne**! Olete edukalt käivitanud Ilma MCP Serveri oma kohalikus arendusmasinas, kasutades Agent Builderit MCP kliendina.
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
> - Kõik silumisrežiimid toetavad murdepunkte, nii et saate lisada murdepunkte tööriista rakenduskoodi.

| Silumisrežiim | Kirjeldus | Silumise sammud |
| ------------- | --------- | --------------- |
| Agent Builder | Siluge MCP serverit Agent Builderis AI Toolkiti kaudu. | 1. Avage VS Code silumispaneel. Valige `Debug in Agent Builder` ja vajutage `F5`, et alustada MCP serveri silumist.<br>2. Kasutage AI Toolkit Agent Builderit, et testida serverit [selle käsuga](../../../../../../../../../../../open_prompt_builder). Server ühendatakse automaatselt Agent Builderiga.<br>3. Klõpsake `Run`, et testida serverit käsuga. |
| MCP Inspector | Siluge MCP serverit MCP Inspectoriga. | 1. Installige [Node.js](https://nodejs.org/)<br> 2. Seadistage Inspector: `cd inspector` && `npm install` <br> 3. Avage VS Code silumispaneel. Valige `Debug SSE in Inspector (Edge)` või `Debug SSE in Inspector (Chrome)`. Vajutage F5, et alustada silumist.<br> 4. Kui MCP Inspector avaneb brauseris, klõpsake `Connect` nuppu, et ühendada see MCP server.<br> 5. Seejärel saate `List Tools`, valida tööriista, sisestada parameetrid ja `Run Tool`, et siluda oma serverikoodi.<br> |

## Vaikimisi pordid ja kohandused

| Silumisrežiim | Pordid | Definitsioonid | Kohandused | Märkus |
| ------------- | ------ | -------------- | ---------- | ------ |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muutke [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), et muuta ülaltoodud porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 ja 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muutke [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), et muuta ülaltoodud porte. | N/A |

## Tagasiside

Kui teil on selle malli kohta tagasisidet või ettepanekuid, avage palun probleem [AI Toolkiti GitHubi repositooriumis](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.