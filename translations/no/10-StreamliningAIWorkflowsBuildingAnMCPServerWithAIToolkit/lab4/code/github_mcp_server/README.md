# Weather MCP Server

Dette er et eksempel på MCP Server i Python som implementerer værverktøy med mock-responser. Den kan brukes som et utgangspunkt for din egen MCP Server. Den inkluderer følgende funksjoner:

- **Værverktøy**: Et verktøy som gir mock-værinformasjon basert på den angitte lokasjonen.
- **Git Clone Tool**: Et verktøy som kloner et git-repositorium til en spesifisert mappe.
- **VS Code Open Tool**: Et verktøy som åpner en mappe i VS Code eller VS Code Insiders.
- **Koble til Agent Builder**: En funksjon som lar deg koble MCP-serveren til Agent Builder for testing og feilsøking.
- **Debug i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funksjon som lar deg feilsøke MCP-serveren ved hjelp av MCP Inspector.

## Kom i gang med Weather MCP Server-malen

> **Forutsetninger**
>
> For å kjøre MCP Server på din lokale utviklingsmaskin, trenger du:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Påkrevd for git_clone_repo-verktøyet)
> - [VS Code](https://code.visualstudio.com/) eller [VS Code Insiders](https://code.visualstudio.com/insiders/) (Påkrevd for open_in_vscode-verktøyet)
> - (*Valgfritt - hvis du foretrekker uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Forbered miljøet

Det finnes to måter å sette opp miljøet for dette prosjektet. Du kan velge den som passer deg best.

> Merk: Start VSCode eller terminalen på nytt for å sikre at Python fra det virtuelle miljøet brukes etter at det virtuelle miljøet er opprettet.

| Tilnærming | Steg |
| ---------- | ---- |
| Bruke `uv` | 1. Opprett virtuelt miljø: `uv venv` <br>2. Kjør VSCode-kommandoen "***Python: Select Interpreter***" og velg Python fra det opprettede virtuelle miljøet <br>3. Installer avhengigheter (inkludert utviklingsavhengigheter): `uv pip install -r pyproject.toml --extra dev` |
| Bruke `pip` | 1. Opprett virtuelt miljø: `python -m venv .venv` <br>2. Kjør VSCode-kommandoen "***Python: Select Interpreter***" og velg Python fra det opprettede virtuelle miljøet <br>3. Installer avhengigheter (inkludert utviklingsavhengigheter): `pip install -e .[dev]` |

Etter å ha satt opp miljøet, kan du kjøre serveren på din lokale utviklingsmaskin via Agent Builder som MCP-klient for å komme i gang:
1. Åpne VS Code Debug-panelet. Velg `Debug in Agent Builder` eller trykk `F5` for å starte feilsøking av MCP-serveren.
2. Bruk AI Toolkit Agent Builder for å teste serveren med [denne prompten](../../../../../../../../../../../open_prompt_builder). Serveren vil automatisk koble seg til Agent Builder.
3. Klikk `Run` for å teste serveren med prompten.

**Gratulerer**! Du har nå kjørt Weather MCP Server på din lokale utviklingsmaskin via Agent Builder som MCP-klient.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Hva er inkludert i malen

| Mappe / Fil | Innhold                                     |
| ------------ | ------------------------------------------- |
| `.vscode`    | VSCode-filer for feilsøking                 |
| `.aitk`      | Konfigurasjoner for AI Toolkit              |
| `src`        | Kildekoden for Weather MCP Server           |

## Hvordan feilsøke Weather MCP Server

> Notater:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt utviklingsverktøy for testing og feilsøking av MCP-servere.
> - Alle feilsøkingsmoduser støtter breakpoints, så du kan legge til breakpoints i verktøyimplementeringskoden.

## Tilgjengelige verktøy

### Værverktøy
`get_weather`-verktøyet gir mock-værinformasjon for en spesifisert lokasjon.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `location` | string | Lokasjon for å hente værinformasjon (f.eks. bynavn, stat eller koordinater) |

### Git Clone Tool
`git_clone_repo`-verktøyet kloner et git-repositorium til en spesifisert mappe.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `repo_url` | string | URL til git-repositoriet som skal klones |
| `target_folder` | string | Sti til mappen der repositoriet skal klones |

Verktøyet returnerer et JSON-objekt med:
- `success`: Boolean som indikerer om operasjonen var vellykket
- `target_folder` eller `error`: Stien til det klonede repositoriet eller en feilmelding

### VS Code Open Tool
`open_in_vscode`-verktøyet åpner en mappe i VS Code eller VS Code Insiders-applikasjonen.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `folder_path` | string | Sti til mappen som skal åpnes |
| `use_insiders` | boolean (valgfritt) | Om VS Code Insiders skal brukes i stedet for vanlig VS Code |

Verktøyet returnerer et JSON-objekt med:
- `success`: Boolean som indikerer om operasjonen var vellykket
- `message` eller `error`: En bekreftelsesmelding eller en feilmelding

| Feilsøkingsmodus | Beskrivelse | Steg for feilsøking |
| ----------------- | ----------- | ------------------- |
| Agent Builder | Feilsøk MCP-serveren i Agent Builder via AI Toolkit. | 1. Åpne VS Code Debug-panelet. Velg `Debug in Agent Builder` og trykk `F5` for å starte feilsøking av MCP-serveren.<br>2. Bruk AI Toolkit Agent Builder for å teste serveren med [denne prompten](../../../../../../../../../../../open_prompt_builder). Serveren vil automatisk koble seg til Agent Builder.<br>3. Klikk `Run` for å teste serveren med prompten. |
| MCP Inspector | Feilsøk MCP-serveren ved hjelp av MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Sett opp Inspector: `cd inspector` && `npm install` <br> 3. Åpne VS Code Debug-panelet. Velg `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Trykk F5 for å starte feilsøking.<br> 4. Når MCP Inspector åpnes i nettleseren, klikk på `Connect`-knappen for å koble til denne MCP-serveren.<br> 5. Deretter kan du `List Tools`, velge et verktøy, legge inn parametere og `Run Tool` for å feilsøke serverkoden.<br> |

## Standardporter og tilpasninger

| Feilsøkingsmodus | Porter | Definisjoner | Tilpasninger | Merknad |
| ----------------- | ------ | ------------ | ------------ | ------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for å endre portene ovenfor. | N/A |
| MCP Inspector | 3001 (Server); 5173 og 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for å endre portene ovenfor. | N/A |

## Tilbakemeldinger

Hvis du har tilbakemeldinger eller forslag til denne malen, vennligst åpne en sak på [AI Toolkit GitHub-repositoriet](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.