# Weather MCP Server

Det här är en exempelserver för MCP i Python som implementerar verktyg för väder med mock-svar. Den kan användas som en grund för din egen MCP-server. Den inkluderar följande funktioner:

- **Väderverktyg**: Ett verktyg som tillhandahåller mockad väderinformation baserat på angiven plats.
- **Git Clone Tool**: Ett verktyg som klonar ett git-repository till en angiven mapp.
- **VS Code Open Tool**: Ett verktyg som öppnar en mapp i VS Code eller VS Code Insiders.
- **Anslut till Agent Builder**: En funktion som låter dig ansluta MCP-servern till Agent Builder för testning och felsökning.
- **Debugga i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funktion som låter dig felsöka MCP-servern med MCP Inspector.

## Kom igång med Weather MCP Server-mallen

> **Förutsättningar**
>
> För att köra MCP-servern på din lokala utvecklingsmaskin behöver du:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Krävs för git_clone_repo-verktyget)
> - [VS Code](https://code.visualstudio.com/) eller [VS Code Insiders](https://code.visualstudio.com/insiders/) (Krävs för open_in_vscode-verktyget)
> - (*Valfritt - om du föredrar uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Förbered miljön

Det finns två sätt att ställa in miljön för detta projekt. Du kan välja det som passar dig bäst.

> Obs: Ladda om VSCode eller terminalen för att säkerställa att Python från den virtuella miljön används efter att den har skapats.

| Metod | Steg |
| -------- | ----- |
| Använda `uv` | 1. Skapa en virtuell miljö: `uv venv` <br>2. Kör VSCode-kommandot "***Python: Select Interpreter***" och välj Python från den skapade virtuella miljön <br>3. Installera beroenden (inklusive utvecklingsberoenden): `uv pip install -r pyproject.toml --extra dev` |
| Använda `pip` | 1. Skapa en virtuell miljö: `python -m venv .venv` <br>2. Kör VSCode-kommandot "***Python: Select Interpreter***" och välj Python från den skapade virtuella miljön<br>3. Installera beroenden (inklusive utvecklingsberoenden): `pip install -e .[dev]` | 

Efter att ha ställt in miljön kan du köra servern på din lokala utvecklingsmaskin via Agent Builder som MCP-klient för att komma igång:
1. Öppna VS Code Debug-panelen. Välj `Debug in Agent Builder` eller tryck på `F5` för att starta felsökning av MCP-servern.
2. Använd AI Toolkit Agent Builder för att testa servern med [denna prompt](../../../../../../../../../../../open_prompt_builder). Servern ansluts automatiskt till Agent Builder.
3. Klicka på `Run` för att testa servern med prompten.

**Grattis**! Du har framgångsrikt kört Weather MCP Server på din lokala utvecklingsmaskin via Agent Builder som MCP-klient.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Vad som ingår i mallen

| Mapp / Fil | Innehåll                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-filer för felsökning                  |
| `.aitk`      | Konfigurationer för AI Toolkit               |
| `src`        | Källkoden för Weather MCP Server             |

## Hur man felsöker Weather MCP Server

> Noteringar:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) är ett visuellt utvecklingsverktyg för testning och felsökning av MCP-servrar.
> - Alla felsökningslägen stödjer brytpunkter, så du kan lägga till brytpunkter i verktygets implementeringskod.

## Tillgängliga verktyg

### Väderverktyg
Verktyget `get_weather` tillhandahåller mockad väderinformation för en angiven plats.

| Parameter | Typ | Beskrivning |
| --------- | ---- | ----------- |
| `location` | string | Plats att hämta väder för (t.ex. stadsnamn, delstat eller koordinater) |

### Git Clone Tool
Verktyget `git_clone_repo` klonar ett git-repository till en angiven mapp.

| Parameter | Typ | Beskrivning |
| --------- | ---- | ----------- |
| `repo_url` | string | URL till git-repositoryt som ska klonas |
| `target_folder` | string | Sökväg till mappen där repositoryt ska klonas |

Verktyget returnerar ett JSON-objekt med:
- `success`: Boolean som indikerar om operationen lyckades
- `target_folder` eller `error`: Sökvägen till det klonade repositoryt eller ett felmeddelande

### VS Code Open Tool
Verktyget `open_in_vscode` öppnar en mapp i VS Code eller VS Code Insiders-applikationen.

| Parameter | Typ | Beskrivning |
| --------- | ---- | ----------- |
| `folder_path` | string | Sökväg till mappen som ska öppnas |
| `use_insiders` | boolean (valfritt) | Om VS Code Insiders ska användas istället för vanlig VS Code |

Verktyget returnerar ett JSON-objekt med:
- `success`: Boolean som indikerar om operationen lyckades
- `message` eller `error`: Ett bekräftelsemeddelande eller ett felmeddelande

| Felsökningsläge | Beskrivning | Steg för felsökning |
| ---------- | ----------- | --------------- |
| Agent Builder | Felsök MCP-servern i Agent Builder via AI Toolkit. | 1. Öppna VS Code Debug-panelen. Välj `Debug in Agent Builder` och tryck på `F5` för att starta felsökning av MCP-servern.<br>2. Använd AI Toolkit Agent Builder för att testa servern med [denna prompt](../../../../../../../../../../../open_prompt_builder). Servern ansluts automatiskt till Agent Builder.<br>3. Klicka på `Run` för att testa servern med prompten. |
| MCP Inspector | Felsök MCP-servern med MCP Inspector. | 1. Installera [Node.js](https://nodejs.org/)<br> 2. Ställ in Inspector: `cd inspector` && `npm install` <br> 3. Öppna VS Code Debug-panelen. Välj `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Tryck på F5 för att starta felsökning.<br> 4. När MCP Inspector startar i webbläsaren, klicka på `Connect`-knappen för att ansluta denna MCP-server.<br> 5. Därefter kan du `List Tools`, välja ett verktyg, ange parametrar och `Run Tool` för att felsöka din serverkod.<br> |

## Standardportar och anpassningar

| Felsökningsläge | Portar | Definitioner | Anpassningar | Notering |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Redigera [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) för att ändra ovanstående portar. | N/A |
| MCP Inspector | 3001 (Server); 5173 och 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Redigera [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) för att ändra ovanstående portar.| N/A |

## Feedback

Om du har feedback eller förslag för denna mall, vänligen öppna ett ärende på [AI Toolkit GitHub-repositoryt](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.