# Weather MCP Server

Dit is een voorbeeld MCP Server in Python die weerhulpmiddelen implementeert met gemockte reacties. Het kan worden gebruikt als basis voor je eigen MCP Server. Het bevat de volgende functies:

- **Weergereedschap**: Een tool die gemockte weerinformatie levert op basis van de opgegeven locatie.
- **Verbinden met Agent Builder**: Een functie die je in staat stelt de MCP-server te verbinden met de Agent Builder voor testen en debuggen.
- **Debuggen in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Een functie die je in staat stelt de MCP Server te debuggen met behulp van de MCP Inspector.

## Aan de slag met de Weather MCP Server-templates

> **Vereisten**
>
> Om de MCP Server op je lokale ontwikkelmachine te draaien, heb je nodig:
>
> - [Python](https://www.python.org/)
> - (*Optioneel - als je uv prefereert*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Voorbereiding van de omgeving

Er zijn twee manieren om de omgeving voor dit project op te zetten. Je kunt er een kiezen op basis van je voorkeur.

> Opmerking: Herlaad VSCode of terminal om te verzekeren dat de python van de virtuele omgeving wordt gebruikt na het aanmaken van de virtuele omgeving.

| Benadering | Stappen |
| --------- | ------- |
| Gebruik maken van `uv` | 1. Maak virtuele omgeving: `uv venv` <br>2. Voer in VSCode de opdracht "***Python: Select Interpreter***" uit en selecteer de python van de aangemaakte virtuele omgeving <br>3. Installeer dependencies (inclusief dev dependencies): `uv pip install -r pyproject.toml --extra dev` |
| Gebruik maken van `pip` | 1. Maak virtuele omgeving: `python -m venv .venv` <br>2. Voer in VSCode de opdracht "***Python: Select Interpreter***" uit en selecteer de python van de aangemaakte virtuele omgeving<br>3. Installeer dependencies (inclusief dev dependencies): `pip install -e .[dev]` | 

Nadat je de omgeving hebt opgezet, kun je de server lokaal op je ontwikkelmachine draaien via Agent Builder als MCP Client om te beginnen:
1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` of druk op `F5` om het debuggen van de MCP-server te starten.
2. In Microsoft Foundry Toolkit Agent Builder, selecteer een actieve Foundry-implementatie zoals `gpt-5.1`, voer dan in: `What is the weather in Shanghai?` De server wordt automatisch verbonden.
3. Klik op `Run` om de server te testen met de prompt.

**Gefeliciteerd**! Je hebt de Weather MCP Server succesvol lokaal draaien via Agent Builder als MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wat is inbegrepen in de template

| Map / Bestand| Inhoud                                      |
| ------------ | ------------------------------------------- |
| `.vscode` | VSCode bestanden voor debuggen               |
| `.aitk` | Configuraties voor Microsoft Foundry Toolkit               |
| `src` | De broncode voor de weather MCP-server         |

## Hoe de Weather MCP Server te debuggen

> Notities:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is een visuele ontwikkelaarstool voor het testen en debuggen van MCP-servers.
> - Alle debug-modi ondersteunen breakpoints, dus je kunt breakpoints toevoegen in de toolimplementatiecode.

| Debugmodus | Beschrijving | Stappen om te debuggen |
| ---------- | ----------- | ---------------------- |
| Agent Builder | Debug de MCP-server in Agent Builder via Microsoft Foundry Toolkit. | 1. Open het Debug-paneel in VS Code. Selecteer `Debug in Agent Builder` en druk op `F5` om het debuggen van de MCP-server te starten.<br>2. Selecteer een actieve Foundry-implementatie zoals `gpt-5.1`, voer dan `What is the weather in Shanghai?` in. De server wordt automatisch verbonden.<br>3. Klik op `Run` om de server met de prompt te testen. |
| MCP Inspector | Debug de MCP-server met de MCP Inspector. | 1. Installeer [Node.js](https://nodejs.org/)<br> 2. Stel Inspector in: `cd inspector` && `npm install` <br> 3. Open het Debug-paneel in VS Code. Selecteer `Debug SSE in Inspector (Edge)` of `Debug SSE in Inspector (Chrome)`. Druk op F5 om te starten met debuggen.<br> 4. Wanneer MCP Inspector in de browser opent, klik op de `Connect` knop om deze MCP-server te verbinden.<br> 5. Daarna kun je `List Tools`, een tool selecteren, parameters invoeren, en `Run Tool` om je servercode te debuggen.<br> |

## Standaardpoorten en aanpassingen

| Debugmodus | Poorten | Definities | Aanpassingen | Opmerking |
| ---------- | ------- | ---------- | ------------ | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) om bovenstaande poorten te wijzigen. | N.v.t. |
| MCP Inspector | 3001 (Server); 5173 en 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) om bovenstaande poorten te wijzigen.| N.v.t. |

## Feedback

Als je feedback of suggesties hebt voor deze template, open dan een issue in het [Microsoft Foundry Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->