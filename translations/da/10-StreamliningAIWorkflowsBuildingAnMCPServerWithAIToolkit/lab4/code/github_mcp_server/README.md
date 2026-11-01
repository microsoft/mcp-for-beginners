# Weather MCP Server

Dette er en eksempel MCP Server i Python, der implementerer vejrværktøjer med mock-responser. Den kan bruges som et stillads til din egen MCP Server. Den inkluderer følgende funktioner: 

- **Vejrværktøj**: Et værktøj, der leverer fiktive vejrinformationer baseret på den givne placering.
- **Git Clone Tool**: Et værktøj, der kloner et git-repositorium til en specificeret mappe.
- **VS Code Open Tool**: Et værktøj, der åbner en mappe i VS Code eller VS Code Insiders.
- **Forbind til Agent Builder**: En funktion, der giver dig mulighed for at forbinde MCP-serveren til Agent Builder til test og fejlfinding.
- **Fejlfinding i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funktion, der giver dig mulighed for at fejlsøge MCP Serveren med MCP Inspector.

## Kom i gang med Weather MCP Server skabelonen

> **Forudsætninger**
>
> For at køre MCP Serveren på din lokale udviklingsmaskine, skal du bruge:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Nødvendig for git_clone_repo værktøjet)
> - [VS Code](https://code.visualstudio.com/) eller [VS Code Insiders](https://code.visualstudio.com/insiders/) (Nødvendig for open_in_vscode værktøjet)
> - (*Valgfrit - hvis du foretrækker uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Forbered miljøet

Der er to tilgange til at opsætte miljøet for dette projekt. Du kan vælge den ene baseret på din præference.

> Bemærk: Genindlæs VSCode eller terminal for at sikre, at den virtuelle miljø-python bruges efter oprettelse af det virtuelle miljø.

| Tilgang | Trin |
| -------- | ----- |
| Brug af `uv` | 1. Opret virtuel miljø: `uv venv` <br>2. Kør VSCode kommando "***Python: Select Interpreter***" og vælg python fra det oprettede virtuelle miljø <br>3. Installer afhængigheder (inkl. dev-afhængigheder): `uv pip install -r pyproject.toml --extra dev` |
| Brug af `pip` | 1. Opret virtuel miljø: `python -m venv .venv` <br>2. Kør VSCode kommando "***Python: Select Interpreter***" og vælg python fra det oprettede virtuelle miljø<br>3. Installer afhængigheder (inkl. dev-afhængigheder): `pip install -e .[dev]` | 

Efter miljøet er sat op, kan du køre serveren på din lokale udviklingsmaskine via Agent Builder som MCP Client for at komme i gang:
1. Åbn VS Code Fejlfinding panel. Vælg `Debug in Agent Builder` eller tryk `F5` for at starte fejlfinding af MCP-serveren.
2. I Microsoft Foundry Toolkit for Visual Studio Code Agent Builder, vælg en aktiv Foundry-udrulning som fx `gpt-5.1`, og indtast: `What is the weather in Shanghai?` Serveren vil blive tilsluttet automatisk.
3. Klik på `Run` for at teste serveren med prompten.

**Tillykke**! Du har med succes kørt Weather MCP Serveren på din lokale udviklingsmaskine via Agent Builder som MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Hvad skabelonen indeholder

| Mappe / Fil | Indhold                                      |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode filer til fejlfinding                    |
| `.aitk`      | Microsoft Foundry Toolkit konfiguration          |
| `src`        | Kildekoden til weather mcp serveren              |

## Sådan fejlfinder du Weather MCP Serveren

> Bemærk:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt udviklerværktøj til test og fejlfinding af MCP servere.
> - Alle fejlfindingstilstande understøtter breakpoint, så du kan tilføje breakpoints i værktøjets implementeringskode.

## Tilgængelige værktøjer

### Vejrværktøj
`get_weather` værktøjet leverer fiktive vejrinformationer for en specificeret placering.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `location` | string | Placering til at hente vejret for (f.eks. bynavn, delstat eller koordinater) |

### Git Clone Tool
`git_clone_repo` værktøjet kloner et git-repositorium til en specificeret mappe.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `repo_url` | string | URL til git-repositoriet, der skal klones |
| `target_folder` | string | Sti til mappen, hvor repositoriet skal klones |

Værktøjet returnerer et JSON-objekt med:
- `success`: Boolean, der angiver om operationen lykkedes
- `target_folder` eller `error`: Stien til det klonede repository eller en fejlmeddelelse

### VS Code Open Tool
`open_in_vscode` værktøjet åbner en mappe i VS Code eller VS Code Insiders applikationen.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `folder_path` | string | Sti til mappen, der skal åbnes |
| `use_insiders` | boolean (valgfri) | Om der skal bruges VS Code Insiders i stedet for almindelig VS Code |

Værktøjet returnerer et JSON-objekt med:
- `success`: Boolean, der angiver om operationen lykkedes
- `message` eller `error`: En bekræftelsesmeddelelse eller en fejlmeddelelse

| Fejlfindingsmode | Beskrivelse | Trin til fejlfinding |
| ---------- | ----------- | --------------- |
| Agent Builder | Fejlfind MCP-serveren i Agent Builder via Microsoft Foundry Toolkit for Visual Studio Code. | 1. Åbn VS Code Fejlfinding panel. Vælg `Debug in Agent Builder` og tryk `F5` for at starte fejlfinding af MCP-serveren.<br>2. Vælg en aktiv Foundry-udrulning som `gpt-5.1`, og indtast `What is the weather in Shanghai?`. Serveren tilsluttes automatisk.<br>3. Klik på `Run` for at teste serveren med prompten. |
| MCP Inspector | Fejlfind MCP-serveren med MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Opsæt Inspector: `cd inspector` && `npm install` <br> 3. Åbn VS Code Fejlfinding panel. Vælg `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Tryk F5 for at starte fejlfinding.<br> 4. Når MCP Inspector åbnes i browseren, klik på `Connect` knappen for at forbinde denne MCP server.<br> 5. Derefter kan du `List Tools`, vælge et værktøj, indtaste parametre, og `Run Tool` for at fejlsøge din serverkode.<br> |

## Standardporte og tilpasninger

| Fejlfindingsmode | Porte | Definitioner | Tilpasninger | Bemærkning |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for at ændre ovenstående porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 og 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for at ændre ovenstående porte.| N/A |

## Feedback

Hvis du har feedback eller forslag til denne skabelon, skriv venligst en issue på [Microsoft Foundry Toolkit for Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->