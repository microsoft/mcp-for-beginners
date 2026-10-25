# Ilma MCP-server

See on näide MCP-serverist Pythonis, mis rakendab ilmatööriistu simuleeritud vastustega. Seda saab kasutada oma MCP-serveri lähtepunktina. See sisaldab järgmisi funktsioone: 

- **Weather Tool**: tööriist, mis annab antud asukoha põhjal simuleeritud ilmaandmeid.
- **Connect to Agent Builder**: funktsioon, mis võimaldab ühendada MCP-serveri Agent Builderiga testimiseks ja silumiseks.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: funktsioon, mis võimaldab siluda MCP-serverit, kasutades MCP Inspectorit.

## Alustamine Ilma MCP-serveri malliga

> **Eeltingimused**
>
> MCP-serveri käitamiseks oma lokaalses arenduskeskkonnas vajate:
>
> - [Python](https://www.python.org/)
> - (*Valikuline - kui eelistad uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Keskkonna ettevalmistamine

Selle projekti keskkonna seadistamiseks on kaks lähenemist. Võite valida kumbki vastavalt eelistusele.

> Märkus: Pärast virtuaalkeskkonna loomist laadige VSCode või terminal uuesti, et veenduda, et kasutatakse virtuaalkeskkonna pythoni.

| Lähenemine | Sammud |
| -------- | ----- |
| Kasutades `uv` | 1. Loo virtuaalkeskkond: `uv venv` <br>2. Käivita VSCode käsk "***Python: Select Interpreter***" ja vali loodud virtuaalkeskkonna python <br>3. Paigalda sõltuvused (sh arendus-sõltuvused): `uv pip install -r pyproject.toml --extra dev` |
| Kasutades `pip` | 1. Loo virtuaalkeskkond: `python -m venv .venv` <br>2. Käivita VSCode käsk "***Python: Select Interpreter***" ja vali loodud virtuaalkeskkonna python<br>3. Paigalda sõltuvused (sh arendus-sõltuvused): `pip install -e .[dev]` | 

Pärast keskkonna seadistamist saate serveri oma lokaalses arenduskeskkonnas käivitada Agent Builderi kaudu MCP-kliendina, et alustada:
1. Avage VS Code silumise paneel. Valige `Debug in Agent Builder` või vajutage `F5`, et alustada MCP-serveri silumist.
2. Microsoft Foundry Toolkit Agent Builderis valige aktiivne Foundry juurutus nagu `gpt-5.1`, seejärel sisestage: `What is the weather in Shanghai?` Server ühendatakse automaatselt.
3. Klõpsake `Run`, et testida serverit promptiga.

**Palju õnne**! Olete edukalt käivitanud Ilma MCP-serveri oma lokaalses arenduskeskkonnas Agent Builderi kaudu MCP-kliendina.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Mida mall sisaldab

| Kaust / Fail| Sisu                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode failid silumiseks                   |
| `.aitk`      | Seadistused Microsoft Foundry Toolkitile                |
| `src`        | Ilma MCP-serveri lähtekood   |

## Kuidas siluda Ilma MCP-serverit

> Märkused:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) on visuaalne arendustööriist MCP-serverite testimiseks ja silumiseks.
> - Kõik silumise režiimid toetavad murdepunktide (breakpoints) kasutamist, nii et saate lisada murdepunkte tööriista teostuse koodi.

| Silumise režiim | Kirjeldus | Sammud silumiseks |
| ---------- | ----------- | --------------- |
| Agent Builder | Siluge MCP-serverit Agent Builderis Microsoft Foundry Toolkiti kaudu. | 1. Avage VS Code silumise paneel. Valige `Debug in Agent Builder` ja vajutage `F5`, et alustada MCP-serveri silumist.<br>2. Valige aktiivne Foundry juurutus, nagu `gpt-5.1`, seejärel sisestage `What is the weather in Shanghai?`. Server ühendatakse automaatselt.<br>3. Klõpsake `Run`, et testida serverit promptiga. |
| MCP Inspector | Siluge MCP-serverit kasutades MCP Inspectorit. | 1. Paigaldage [Node.js](https://nodejs.org/)<br> 2. Seadistage Inspector: `cd inspector` && `npm install` <br> 3. Avage VS Code silumise paneel. Valige `Debug SSE in Inspector (Edge)` või `Debug SSE in Inspector (Chrome)`. Vajutage F5, et alustada silumist.<br> 4. Kui MCP Inspector käivitub brauseris, klõpsake nuppu `Connect`, et ühendada see MCP-server.<br> 5. Seejärel saate `List Tools`, valida tööriista, sisestada parameetrid ja `Run Tool`, et siluda oma serveri koodi.<br> |

## Vaikimisi pordid ja kohandused

| Silumise režiim | Pordid | Määratlused | Kohandused | Märkus |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muuda [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), et muuta ülaltoodud porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 and 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Muuda [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) , et muuta ülaltoodud porte.| N/A |

## Tagasiside

Kui teil on selle malli kohta tagasisidet või ettepanekuid, avage palun issue [Microsoft Foundry Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->