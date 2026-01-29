# Weather MCP Server

Dit is een voorbeeld van een MCP Server in Python die weerhulpmiddelen implementeert met mock-antwoorden. Het kan worden gebruikt als basis voor je eigen MCP Server. Het bevat de volgende functies:

- **Weather Tool**: Een tool die gemockte weerinformatie geeft op basis van de opgegeven locatie.
- **Connect to Agent Builder**: Een functie waarmee je de MCP-server kunt verbinden met de Agent Builder voor testen en debuggen.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Een functie waarmee je de MCP Server kunt debuggen met behulp van de MCP Inspector.

## Aan de slag met de Weather MCP Server template

> **Vereisten**
>
> Om de MCP Server op je lokale ontwikkelmachine te draaien, heb je nodig:
>
> - [Python](https://www.python.org/)
> - (*Optioneel - als je uv prefereert*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Omgeving voorbereiden

Er zijn twee manieren om de omgeving voor dit project op te zetten. Je kunt er één kiezen op basis van je voorkeur.

> Opmerking: Herstart VSCode of de terminal om zeker te zijn dat de python van de virtuele omgeving wordt gebruikt nadat je de virtuele omgeving hebt aangemaakt.

| Aanpak | Stappen |
| ------- | ------- |
| Met `uv` | 1. Maak virtuele omgeving aan: `uv venv` <br>2. Voer VSCode-commando "***Python: Select Interpreter***" uit en selecteer de python van de aangemaakte virtuele omgeving <br>3. Installeer dependencies (inclusief dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Met `pip` | 1. Maak virtuele omgeving aan: `python -m venv .venv` <br>2. Voer VSCode-commando "***Python: Select Interpreter***" uit en selecteer de python van de aangemaakte virtuele omgeving<br>3. Installeer dependencies (inclusief dev dependencies): `pip install -e .[dev]` |

Na het opzetten van de omgeving kun je de server lokaal draaien via Agent Builder als MCP Client om te beginnen:
1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` of druk op `F5` om het debuggen van de MCP server te starten.
2. Gebruik AI Toolkit Agent Builder om de server te testen met [deze prompt](../../../../../../../../../../open_prompt_builder). De server wordt automatisch verbonden met de Agent Builder.
3. Klik op `Run` om de server met de prompt te testen.

**Gefeliciteerd**! Je hebt de Weather MCP Server succesvol lokaal draaien via Agent Builder als MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wat zit er in de template

| Map / Bestand | Inhoud                                      |
| ------------- | ------------------------------------------- |
| `.vscode`     | VSCode-bestanden voor debuggen              |
| `.aitk`       | Configuraties voor AI Toolkit                |
| `src`         | De broncode voor de weather mcp server      |

## Hoe debug je de Weather MCP Server

> Opmerkingen:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is een visuele ontwikkelaarstool voor het testen en debuggen van MCP-servers.
> - Alle debug-modi ondersteunen breakpoints, dus je kunt breakpoints toevoegen in de tool-implementatiecode.

| Debugmodus | Beschrijving | Stappen om te debuggen |
| ---------- | ------------ | ---------------------- |
| Agent Builder | Debug de MCP server in de Agent Builder via AI Toolkit. | 1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` en druk op `F5` om het debuggen van de MCP server te starten.<br>2. Gebruik AI Toolkit Agent Builder om de server te testen met [deze prompt](../../../../../../../../../../open_prompt_builder). De server wordt automatisch verbonden met de Agent Builder.<br>3. Klik op `Run` om de server met de prompt te testen. |
| MCP Inspector | Debug de MCP server met behulp van de MCP Inspector. | 1. Installeer [Node.js](https://nodejs.org/)<br> 2. Zet Inspector op: `cd inspector` && `npm install` <br> 3. Open het Debug-paneel in VS Code. Selecteer `Debug SSE in Inspector (Edge)` of `Debug SSE in Inspector (Chrome)`. Druk op F5 om te starten met debuggen.<br> 4. Wanneer MCP Inspector in de browser opent, klik op de knop `Connect` om deze MCP server te verbinden.<br> 5. Daarna kun je `List Tools` gebruiken, een tool selecteren, parameters invoeren en `Run Tool` om je servercode te debuggen.<br> |

## Standaardpoorten en aanpassingen

| Debugmodus | Poorten | Definities | Aanpassingen | Opmerking |
| ---------- | ------- | ---------- | ------------ | --------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Pas [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) aan om bovenstaande poorten te wijzigen. | N.v.t. |
| MCP Inspector | 3001 (Server); 5173 en 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Pas [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) aan om bovenstaande poorten te wijzigen. | N.v.t. |

## Feedback

Als je feedback of suggesties hebt voor deze template, open dan een issue op de [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.