# Weather MCP Server

Dette er en eksempel MCP-server i Python, der implementerer værktøjer til vejrinformation med mock-responser. Den kan bruges som en skabelon til din egen MCP-server. Den inkluderer følgende funktioner:

- **Weather Tool**: Et værktøj, der giver mock-vejrinformation baseret på den angivne lokation.
- **Git Clone Tool**: Et værktøj, der kloner et git-repository til en specificeret mappe.
- **VS Code Open Tool**: Et værktøj, der åbner en mappe i VS Code eller VS Code Insiders.
- **Connect to Agent Builder**: En funktion, der gør det muligt at forbinde MCP-serveren til Agent Builder for test og fejlfinding.
- **Debug i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funktion, der gør det muligt at debugge MCP-serveren ved hjælp af MCP Inspector.

## Kom godt i gang med Weather MCP Server-skabelonen

> **Forudsætninger**
>
> For at køre MCP-serveren på din lokale udviklingsmaskine skal du bruge:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Påkrævet for git_clone_repo-værktøjet)
> - [VS Code](https://code.visualstudio.com/) eller [VS Code Insiders](https://code.visualstudio.com/insiders/) (Påkrævet for open_in_vscode-værktøjet)
> - (*Valgfrit - hvis du foretrækker uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Forbered miljøet

Der er to metoder til at opsætte miljøet for dette projekt. Du kan vælge den, der passer dig bedst.

> Bemærk: Genindlæs VSCode eller terminalen for at sikre, at den virtuelle miljø-python bruges efter oprettelse af det virtuelle miljø.

| Metode | Trin |
| ------ | ---- |
| Brug `uv` | 1. Opret virtuelt miljø: `uv venv` <br>2. Kør VSCode-kommandoen "***Python: Select Interpreter***" og vælg python fra det oprettede virtuelle miljø <br>3. Installer afhængigheder (inklusive udviklingsafhængigheder): `uv pip install -r pyproject.toml --extra dev` |
| Brug `pip` | 1. Opret virtuelt miljø: `python -m venv .venv` <br>2. Kør VSCode-kommandoen "***Python: Select Interpreter***" og vælg python fra det oprettede virtuelle miljø <br>3. Installer afhængigheder (inklusive udviklingsafhængigheder): `pip install -e .[dev]` |

Efter opsætning af miljøet kan du køre serveren på din lokale udviklingsmaskine via Agent Builder som MCP-klient for at komme i gang:
1. Åbn VS Code Debug-panelet. Vælg `Debug in Agent Builder` eller tryk på `F5` for at starte debugging af MCP-serveren.
2. Brug AI Toolkit Agent Builder til at teste serveren med [denne prompt](../../../../../../../../../../../open_prompt_builder). Serveren vil automatisk blive forbundet til Agent Builder.
3. Klik på `Run` for at teste serveren med prompten.

**Tillykke**! Du har med succes kørt Weather MCP Server på din lokale udviklingsmaskine via Agent Builder som MCP-klient.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Hvad er inkluderet i skabelonen

| Mappe / Fil | Indhold                                      |
| ----------- | -------------------------------------------- |
| `.vscode`   | VSCode-filer til debugging                   |
| `.aitk`     | Konfigurationer til AI Toolkit               |
| `src`       | Kildekoden til Weather MCP Server            |

## Sådan debugger du Weather MCP Server

> Bemærkninger:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt udviklingsværktøj til test og debugging af MCP-servere.
> - Alle debugging-tilstande understøtter breakpoints, så du kan tilføje breakpoints til værktøjets implementeringskode.

## Tilgængelige værktøjer

### Weather Tool
`get_weather`-værktøjet giver mock-vejrinformation for en specificeret lokation.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `location` | string | Lokation for at få vejrinformation (f.eks. bynavn, stat eller koordinater) |

### Git Clone Tool
`git_clone_repo`-værktøjet kloner et git-repository til en specificeret mappe.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `repo_url` | string | URL til git-repositoryet, der skal klones |
| `target_folder` | string | Sti til mappen, hvor repositoryet skal klones |

Værktøjet returnerer et JSON-objekt med:
- `success`: Boolean, der angiver, om operationen var vellykket
- `target_folder` eller `error`: Stien til det klonede repository eller en fejlmeddelelse

### VS Code Open Tool
`open_in_vscode`-værktøjet åbner en mappe i VS Code eller VS Code Insiders-applikationen.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `folder_path` | string | Sti til mappen, der skal åbnes |
| `use_insiders` | boolean (valgfrit) | Om der skal bruges VS Code Insiders i stedet for almindelig VS Code |

Værktøjet returnerer et JSON-objekt med:
- `success`: Boolean, der angiver, om operationen var vellykket
- `message` eller `error`: En bekræftelsesmeddelelse eller en fejlmeddelelse

| Debug-tilstand | Beskrivelse | Trin til debugging |
| -------------- | ----------- | ------------------ |
| Agent Builder | Debug MCP-serveren i Agent Builder via AI Toolkit. | 1. Åbn VS Code Debug-panelet. Vælg `Debug in Agent Builder` og tryk på `F5` for at starte debugging af MCP-serveren.<br>2. Brug AI Toolkit Agent Builder til at teste serveren med [denne prompt](../../../../../../../../../../../open_prompt_builder). Serveren vil automatisk blive forbundet til Agent Builder.<br>3. Klik på `Run` for at teste serveren med prompten. |
| MCP Inspector | Debug MCP-serveren ved hjælp af MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Opsæt Inspector: `cd inspector` && `npm install` <br> 3. Åbn VS Code Debug-panelet. Vælg `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Tryk på F5 for at starte debugging.<br> 4. Når MCP Inspector åbnes i browseren, klik på `Connect`-knappen for at forbinde denne MCP-server.<br> 5. Derefter kan du `List Tools`, vælge et værktøj, indtaste parametre og `Run Tool` for at debugge din serverkode.<br> |

## Standardporte og tilpasninger

| Debug-tilstand | Porte | Definitioner | Tilpasninger | Bemærkning |
| -------------- | ----- | ------------ | ------------ | ---------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for at ændre ovenstående porte. | N/A |
| MCP Inspector | 3001 (Server); 5173 og 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for at ændre ovenstående porte. | N/A |

## Feedback

Hvis du har feedback eller forslag til denne skabelon, kan du oprette en issue på [AI Toolkit GitHub-repositoryet](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.