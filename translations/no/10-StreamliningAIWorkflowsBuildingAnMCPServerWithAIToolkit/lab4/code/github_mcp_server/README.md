# Vær MCP Server

Dette er en eksempel MCP Server i Python som implementerer værverktøy med simulerte svar. Den kan brukes som en ramme for din egen MCP Server. Den inkluderer følgende funksjoner:

- **Værverktøy**: Et verktøy som gir simulert værinformasjon basert på angitt sted.
- **Git Clone-verktøy**: Et verktøy som kloner et git-repositorium til en spesifisert mappe.
- **VS Code Åpen Verktøy**: Et verktøy som åpner en mappe i VS Code eller VS Code Insiders.
- **Koble til Agent Builder**: En funksjon som lar deg koble MCP-serveren til Agent Builder for testing og feilsøking.
- **Feilsøk i [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: En funksjon som lar deg feilsøke MCP Serveren ved hjelp av MCP Inspector.

## Kom i gang med Vær MCP Server-malen

> **Forutsetninger**
>
> For å kjøre MCP Server på din lokale utviklingsmaskin trenger du:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Nødvendig for git_clone_repo-verktøyet)
> - [VS Code](https://code.visualstudio.com/) eller [VS Code Insiders](https://code.visualstudio.com/insiders/) (Nødvendig for open_in_vscode-verktøyet)
> - (*Valgfritt - hvis du foretrekker uv*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Forbered miljø

Det finnes to måter å sette opp miljøet for dette prosjektet. Du kan velge den som passer best for deg.

> Merk: Last inn VSCode eller terminal på nytt for å sikre at python i det virtuelle miljøet brukes etter oppretting av det virtuelle miljøet.

| Tilnærming | Steg |
| -------- | ----- |
| Bruke `uv` | 1. Lag virtuell miljø: `uv venv` <br>2. Kjør VSCode-kommandoen "***Python: Select Interpreter***" og velg python fra det opprettede virtuelle miljøet <br>3. Installer avhengigheter (inkludert utviklingsavhengigheter): `uv pip install -r pyproject.toml --extra dev` |
| Bruke `pip` | 1. Lag virtuell miljø: `python -m venv .venv` <br>2. Kjør VSCode-kommandoen "***Python: Select Interpreter***" og velg python fra det opprettede virtuelle miljøet<br>3. Installer avhengigheter (inkludert utviklingsavhengigheter): `pip install -e .[dev]` | 

Etter at miljøet er satt opp kan du kjøre serveren på din lokale utviklingsmaskin via Agent Builder som MCP-klient for å komme i gang:
1. Åpne VS Code Feilsøk-panel. Velg `Debug in Agent Builder` eller trykk `F5` for å starte feilsøking av MCP-serveren.
2. I Microsoft Foundry Toolkit for Visual Studio Code Agent Builder, velg en aktiv Foundry-implementering som `gpt-5.1`, skriv deretter inn: `What is the weather in Shanghai?` Serveren kobles til automatisk.
3. Klikk `Run` for å teste serveren med prompten.

**Gratulerer**! Du har med suksess kjørt Vær MCP Server på din lokale utviklingsmaskin via Agent Builder som MCP-klient.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Hva som er inkludert i malen

| Mappe / Fil | Innhold                                      |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode-filer for feilsøking                   |
| `.aitk`      | Microsoft Foundry Toolkit konfigurasjon       |
| `src`        | Kildekoden for vær MCP serveren                |

## Hvordan feilsøke Vær MCP Server

> Notater:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) er et visuelt utviklerverktøy for testing og feilsøking av MCP-servere.
> - Alle feilsøkingsmoduser støtter brytepunkter, så du kan legge til brytepunkter i verktøyets implementasjonskode.

## Tilgjengelige verktøy

### Værverktøy
`get_weather` verktøyet gir simulert værinformasjon for et spesifisert sted.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `location` | streng | Sted å hente vær for (f.eks., bynavn, fylke eller koordinater) |

### Git Clone-verktøy
`git_clone_repo` verktøyet kloner et git-repositorium til en spesifisert mappe.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `repo_url` | streng | URL til git-repositoriet som skal klones |
| `target_folder` | streng | Sti til mappen der repositoriet skal klones |

Verktøyet returnerer et JSON-objekt med:
- `success`: Boolsk verdi som indikerer om operasjonen var vellykket
- `target_folder` eller `error`: Stien til det klonede repositoriet eller en feilmelding

### VS Code Åpen Verktøy
`open_in_vscode` verktøyet åpner en mappe i VS Code eller VS Code Insiders-applikasjonen.

| Parameter | Type | Beskrivelse |
| --------- | ---- | ----------- |
| `folder_path` | streng | Sti til mappen som skal åpnes |
| `use_insiders` | boolsk (valgfritt) | Om det skal brukes VS Code Insiders i stedet for vanlig VS Code |

Verktøyet returnerer et JSON-objekt med:
- `success`: Boolsk verdi som angir om operasjonen var vellykket
- `message` eller `error`: En bekreftelsesmelding eller en feilmelding

| Feilsøkingsmodus | Beskrivelse | Steg for å feilsøke |
| ---------- | ----------- | --------------- |
| Agent Builder | Feilsøk MCP-serveren i Agent Builder via Microsoft Foundry Toolkit for Visual Studio Code. | 1. Åpne VS Code Feilsøk-panel. Velg `Debug in Agent Builder` og trykk `F5` for å starte feilsøking av MCP-serveren.<br>2. Velg en aktiv Foundry-implementering som `gpt-5.1`, skriv deretter inn `What is the weather in Shanghai?`. Serveren kobles til automatisk.<br>3. Klikk `Run` for å teste serveren med prompten. |
| MCP Inspector | Feilsøk MCP-serveren ved hjelp av MCP Inspector. | 1. Installer [Node.js](https://nodejs.org/)<br> 2. Sett opp Inspector: `cd inspector` && `npm install` <br> 3. Åpne VS Code Feilsøk-panel. Velg `Debug SSE in Inspector (Edge)` eller `Debug SSE in Inspector (Chrome)`. Trykk F5 for å starte feilsøking.<br> 4. Når MCP Inspector åpnes i nettleseren, klikk på `Connect` knappen for å koble denne MCP-serveren.<br> 5. Deretter kan du `List Tools`, velge et verktøy, legge inn parametere, og `Run Tool` for å feilsøke serverkoden din.<br> |

## Standardporter og tilpasninger

| Feilsøkingsmodus | Porter | Definisjoner | Tilpasninger | Merknad |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for å endre portene over. | Ikke relevant |
| MCP Inspector | 3001 (Server); 5173 og 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Rediger [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) for å endre portene over.| Ikke relevant |

## Tilbakemelding

Hvis du har tilbakemeldinger eller forslag til denne malen, vennligst opprett en sak i [Microsoft Foundry Toolkit for Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->