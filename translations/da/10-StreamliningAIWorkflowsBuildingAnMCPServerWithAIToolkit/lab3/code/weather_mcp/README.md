# Weather MCP Server

Dette er en eksempel MCP Server i Python, der implementerer værktøjer til vejret med mock-svar. Den kan bruges som en ramme til din egen MCP Server. Den inkluderer følgende funktioner:

- **Vejr-værktøj**: Et værktøj, der leverer simulerede vejroplysninger baseret på den givne placering.
- **Forbind til Agent Builder**: En funktion, der giver dig mulighed for at forbinde MCP-serveren til Agent Builder til test og fejlfinding.
- **Fejlfinding i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funktion, der giver dig mulighed for at fejlfinde MCP Serveren ved hjælp af MCP Inspector.

## Kom godt i gang med Weather MCP Server-skabelonen

> **Forudsætninger**
>
> For at køre MCP Serveren på din lokale udviklingsmaskine, skal du have:
>
> - [Python](https://www.python.org/)
> - (*Valgfrit - hvis du foretrækker uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Forbered miljøet

Der er to tilgange til at opsætte miljøet for dette projekt. Du kan vælge en af dem baseret på din præference.

> Bemærk: Genstart VSCode eller terminalen for at sikre, at den virtuelle miljø-python bruges efter oprettelse af det virtuelle miljø.

| Tilgang | Trin |
| -------- | ----- |
| Brug af `uv` | 1. Opret virtuelt miljø: `uv venv` <br>2. Kør VSCode-kommandoen "***Python: Vælg fortolker***" og vælg python fra det oprettede virtuelle miljø <br>3. Installer afhængigheder (inklusive udviklingsafhængigheder): `uv pip install -r pyproject.toml --extra dev` |
| Brug af `pip` | 1. Opret virtuelt miljø: `python -m venv .venv` <br>2. Kør VSCode-kommandoen "***Python: Vælg fortolker***" og vælg python fra det oprettede virtuelle miljø<br>3. Installer afhængigheder (inklusive udviklingsafhængigheder): `pip install -e .[dev]` | 

Efter opsætning af miljøet kan du køre serveren på din lokale udviklingsmaskine via Agent Builder som MCP Client for at komme i gang:
1. Åbn VS Code Fejlfinding-panel. Vælg `Debug in Agent Builder` eller tryk `F5` for at starte fejlfinding af MCP-serveren.
2. I Microsoft Foundry Toolkit Agent Builder vælg en aktiv Foundry-udrulning såsom `gpt-5.1`, og indtast derefter: `What is the weather in Shanghai?` Serveren bliver automatisk forbundet.
3. Klik på `Run` for at teste serveren med prompten.

**Tillykke**! Du har med succes kørt Weather MCP Serveren på din lokale udviklingsmaskine via Agent Builder som MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Hvad skabelonen indeholder

| Mappe / Fil | Indhold                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-filer til fejlfinding                   |
| `.aitk`      | Konfigurationer til Microsoft Foundry Toolkit                |
| `src`        | Kildekoden til weather mcp serveren   |

## Sådan fejlfinder du Weather MCP Server

> Noter:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt udviklingsværktøj til test og fejlfinding af MCP-servere.
> - Alle fejlfindingstilstande understøtter breakpoints, så du kan tilføje breakpoints til kodeimplementeringen af værktøjet.

| Fejlfindingstilstand | Beskrivelse | Trin til fejlfinding |
| ---------- | ----------- | --------------- |
| Agent Builder | Fejlfinding af MCP-serveren i Agent Builder via Microsoft Foundry Toolkit. | 1. Åbn VS Code Fejlfinding-panel. Vælg `Debug in Agent Builder` og tryk `F5` for at starte fejlfinding af MCP-serveren.<br>2. Vælg en aktiv Foundry-udrulning såsom `gpt-5.1`, og indtast `What is the weather in Shanghai?`. Serveren bliver automatisk forbundet.<br>3. Klik `Run` for at teste serveren med prompten. |
| MCP Inspector | Fejlfinding af MCP-serveren ved hjælp af MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Opsæt Inspector: `cd inspector` && `npm install` <br> 3. Åbn VS Code Fejlfinding-panel. Vælg `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Tryk på F5 for at starte fejlfinding.<br> 4. Når MCP Inspector åbner i browseren, klik på `Connect` knappen for at forbinde denne MCP server.<br> 5. Så kan du `List Tools`, vælge et værktøj, indtaste parametre og `Run Tool` for at fejlfinde din serverkode.<br> |

## Standardporte og tilpasninger

| Fejlfindingstilstand | Porte | Definitioner | Tilpasninger | Bemærkning |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) for at ændre ovenstående porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 og 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) for at ændre ovenstående porte.| N/A |

## Feedback

Hvis du har feedback eller forslag til denne skabelon, så opret et issue på [Microsoft Foundry Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->