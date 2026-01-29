# Weather MCP Server

Dit is een voorbeeld van een MCP Server in Python die weerhulpmiddelen implementeert met gesimuleerde antwoorden. Het kan worden gebruikt als basis voor je eigen MCP Server. Het bevat de volgende functies:

- **Weather Tool**: Een hulpmiddel dat gesimuleerde weersinformatie biedt op basis van de opgegeven locatie.
- **Git Clone Tool**: Een hulpmiddel dat een git-repository naar een opgegeven map kloont.
- **VS Code Open Tool**: Een hulpmiddel dat een map opent in VS Code of VS Code Insiders.
- **Connect to Agent Builder**: Een functie waarmee je de MCP Server kunt verbinden met de Agent Builder voor testen en debuggen.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Een functie waarmee je de MCP Server kunt debuggen met behulp van de MCP Inspector.

## Aan de slag met de Weather MCP Server-template

> **Vereisten**
>
> Om de MCP Server op je lokale ontwikkelmachine te draaien, heb je nodig:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Vereist voor het git_clone_repo-hulpmiddel)
> - [VS Code](https://code.visualstudio.com/) of [VS Code Insiders](https://code.visualstudio.com/insiders/) (Vereist voor het open_in_vscode-hulpmiddel)
> - (*Optioneel - als je uv verkiest*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Omgeving voorbereiden

Er zijn twee manieren om de omgeving voor dit project in te stellen. Je kunt er een kiezen op basis van je voorkeur.

> Opmerking: Herlaad VSCode of de terminal om ervoor te zorgen dat de Python van de virtuele omgeving wordt gebruikt nadat je de virtuele omgeving hebt aangemaakt.

| Methode | Stappen |
| -------- | ------- |
| Met `uv` | 1. Maak een virtuele omgeving: `uv venv` <br>2. Voer de VSCode-opdracht "***Python: Select Interpreter***" uit en selecteer de Python van de aangemaakte virtuele omgeving <br>3. Installeer afhankelijkheden (inclusief ontwikkelafhankelijkheden): `uv pip install -r pyproject.toml --extra dev` |
| Met `pip` | 1. Maak een virtuele omgeving: `python -m venv .venv` <br>2. Voer de VSCode-opdracht "***Python: Select Interpreter***" uit en selecteer de Python van de aangemaakte virtuele omgeving <br>3. Installeer afhankelijkheden (inclusief ontwikkelafhankelijkheden): `pip install -e .[dev]` |

Na het instellen van de omgeving kun je de server op je lokale ontwikkelmachine draaien via Agent Builder als de MCP Client om aan de slag te gaan:
1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` of druk op `F5` om het debuggen van de MCP Server te starten.
2. Gebruik AI Toolkit Agent Builder om de server te testen met [deze prompt](../../../../../../../../../../../open_prompt_builder). De server wordt automatisch verbonden met de Agent Builder.
3. Klik op `Run` om de server met de prompt te testen.

**Gefeliciteerd**! Je hebt de Weather MCP Server succesvol gedraaid op je lokale ontwikkelmachine via Agent Builder als de MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wat zit er in de template

| Map / Bestand | Inhoud                                     |
| ------------- | ------------------------------------------ |
| `.vscode`     | VSCode-bestanden voor debuggen             |
| `.aitk`       | Configuraties voor AI Toolkit              |
| `src`         | De broncode voor de Weather MCP Server     |

## Hoe debug je de Weather MCP Server

> Opmerkingen:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is een visuele ontwikkeltool voor het testen en debuggen van MCP Servers.
> - Alle debugmodi ondersteunen breakpoints, zodat je breakpoints kunt toevoegen aan de implementatiecode van het hulpmiddel.

## Beschikbare hulpmiddelen

### Weather Tool
Het `get_weather`-hulpmiddel biedt gesimuleerde weersinformatie voor een opgegeven locatie.

| Parameter | Type | Beschrijving |
| --------- | ---- | ------------ |
| `location` | string | Locatie waarvoor je het weer wilt opvragen (bijv. stadsnaam, staat of coördinaten) |

### Git Clone Tool
Het `git_clone_repo`-hulpmiddel kloont een git-repository naar een opgegeven map.

| Parameter | Type | Beschrijving |
| --------- | ---- | ------------ |
| `repo_url` | string | URL van de git-repository die je wilt klonen |
| `target_folder` | string | Pad naar de map waar de repository moet worden gekloond |

Het hulpmiddel retourneert een JSON-object met:
- `success`: Boolean die aangeeft of de operatie succesvol was
- `target_folder` of `error`: Het pad van de gekloonde repository of een foutmelding

### VS Code Open Tool
Het `open_in_vscode`-hulpmiddel opent een map in de VS Code- of VS Code Insiders-applicatie.

| Parameter | Type | Beschrijving |
| --------- | ---- | ------------ |
| `folder_path` | string | Pad naar de map die je wilt openen |
| `use_insiders` | boolean (optioneel) | Of je VS Code Insiders wilt gebruiken in plaats van reguliere VS Code |

Het hulpmiddel retourneert een JSON-object met:
- `success`: Boolean die aangeeft of de operatie succesvol was
- `message` of `error`: Een bevestigingsbericht of een foutmelding

| Debugmodus | Beschrijving | Stappen om te debuggen |
| ---------- | ------------ | ---------------------- |
| Agent Builder | Debug de MCP Server in de Agent Builder via AI Toolkit. | 1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` en druk op `F5` om het debuggen van de MCP Server te starten.<br>2. Gebruik AI Toolkit Agent Builder om de server te testen met [deze prompt](../../../../../../../../../../../open_prompt_builder). De server wordt automatisch verbonden met de Agent Builder.<br>3. Klik op `Run` om de server met de prompt te testen. |
| MCP Inspector | Debug de MCP Server met behulp van de MCP Inspector. | 1. Installeer [Node.js](https://nodejs.org/)<br> 2. Stel de Inspector in: `cd inspector` && `npm install` <br> 3. Open het Debug-paneel in VS Code. Selecteer `Debug SSE in Inspector (Edge)` of `Debug SSE in Inspector (Chrome)`. Druk op F5 om het debuggen te starten.<br> 4. Wanneer MCP Inspector in de browser wordt gestart, klik op de knop `Connect` om deze MCP Server te verbinden.<br> 5. Vervolgens kun je `List Tools` gebruiken, een hulpmiddel selecteren, parameters invoeren en `Run Tool` gebruiken om je servercode te debuggen.<br> |

## Standaardpoorten en aanpassingen

| Debugmodus | Poorten | Definities | Aanpassingen | Opmerking |
| ---------- | ------- | ---------- | ------------ | --------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) om bovenstaande poorten te wijzigen. | N.v.t. |
| MCP Inspector | 3001 (Server); 5173 en 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) om bovenstaande poorten te wijzigen. | N.v.t. |

## Feedback

Als je feedback of suggesties hebt voor deze template, open dan een issue op de [AI Toolkit GitHub-repository](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.