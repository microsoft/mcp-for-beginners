# Weer MCP Server

Dit is een voorbeeld van een MCP Server in Python die weerhulpmiddelen implementeert met mock-antwoorden. Het kan worden gebruikt als een kader voor je eigen MCP Server. Het bevat de volgende functies:

- **Weer Hulpmiddel**: Een hulpmiddel dat gemockte weerinformatie biedt op basis van de gegeven locatie.
- **Git Clone Hulpmiddel**: Een hulpmiddel dat een git-repository kloont naar een opgegeven map.
- **VS Code Open Hulpmiddel**: Een hulpmiddel dat een map opent in VS Code of VS Code Insiders.
- **Verbinden met Agent Builder**: Een functie waarmee je de MCP-server kunt verbinden met de Agent Builder voor testen en debuggen.
- **Debuggen in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Een functie waarmee je de MCP Server kunt debuggen met de MCP Inspector.

## Aan de slag met de Weather MCP Server-template

> **Vereisten**
>
> Om de MCP Server op je lokale ontwikkelmachine te draaien, heb je nodig:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Vereist voor git_clone_repo hulpmiddel)
> - [VS Code](https://code.visualstudio.com/) of [VS Code Insiders](https://code.visualstudio.com/insiders/) (Vereist voor open_in_vscode hulpmiddel)
> - (*Optioneel - als je uv prefereert*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Voorbereid de omgeving

Er zijn twee benaderingen om de omgeving voor dit project op te zetten. Je kunt een van beide kiezen op basis van je voorkeur.

> Opmerking: Herlaad VSCode of terminal om te zorgen dat de python van de virtuele omgeving wordt gebruikt nadat je de virtuele omgeving hebt gemaakt.

| Benadering | Stappen |
| -------- | ----- |
| Gebruik van `uv` | 1. Maak virtuele omgeving aan: `uv venv` <br>2. Voer VSCode-commando "***Python: Select Interpreter***" uit en selecteer de python van de gemaakte virtuele omgeving <br>3. Installeer de afhankelijkheden (inclusief dev-afhankelijkheden): `uv pip install -r pyproject.toml --extra dev` |
| Gebruik van `pip` | 1. Maak virtuele omgeving aan: `python -m venv .venv` <br>2. Voer VSCode-commando "***Python: Select Interpreter***" uit en selecteer de python van de gemaakte virtuele omgeving<br>3. Installeer de afhankelijkheden (inclusief dev-afhankelijkheden): `pip install -e .[dev]` |

Nadat je de omgeving hebt ingesteld, kun je de server draaien op je lokale ontwikkelmachine via Agent Builder als MCP Client om aan de slag te gaan:
1. Open het Debug-paneel van VS Code. Selecteer `Debug in Agent Builder` of druk op `F5` om het debuggen van de MCP server te starten.
2. In Microsoft Foundry Toolkit voor Visual Studio Code Agent Builder, selecteer een actieve Foundry deployment zoals `gpt-5.1`, voer dan in: `What is the weather in Shanghai?` De server zal automatisch verbonden worden.
3. Klik `Run` om de server met de prompt te testen.

**Gefeliciteerd**! Je hebt de Weather MCP Server succesvol gedraaid op je lokale ontwikkelmachine via Agent Builder als MCP Client.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Wat zit er in de template

| Map / Bestand | Inhoud                                      |
| ------------ | ------------------------------------------- |
| `.vscode`    | VSCode-bestanden voor debugging             |
| `.aitk`      | Microsoft Foundry Toolkit configuratie      |
| `src`        | De broncode voor de weer mcp server          |

## Hoe de Weather MCP Server te debuggen

> Notities:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is een visuele ontwikkelaarstool voor het testen en debuggen van MCP servers.
> - Alle debug-modi ondersteunen breakpoints, dus je kunt breakpoints toevoegen in de tool-implementatiecode.

## Beschikbare Hulpmiddelen

### Weer Hulpmiddel
Het `get_weather` hulpmiddel biedt gemockte weerinformatie voor een opgegeven locatie.

| Parameter | Type | Beschrijving |
| --------- | ---- | ----------- |
| `location` | string | Locatie om weer voor op te vragen (bijv. stadsnaam, staat, of coördinaten) |

### Git Clone Hulpmiddel
Het `git_clone_repo` hulpmiddel kloont een git-repository naar een opgegeven map.

| Parameter | Type | Beschrijving |
| --------- | ---- | ----------- |
| `repo_url` | string | URL van de git-repository die gekloond moet worden |
| `target_folder` | string | Pad naar de map waar de repository gekloond moet worden |

Het hulpmiddel geeft een JSON-object terug met:
- `success`: Boolean die aangeeft of de bewerking succesvol was
- `target_folder` of `error`: Het pad van de gekloonde repository of een foutmelding

### VS Code Open Hulpmiddel
Het `open_in_vscode` hulpmiddel opent een map in VS Code of VS Code Insiders applicatie.

| Parameter | Type | Beschrijving |
| --------- | ---- | ----------- |
| `folder_path` | string | Pad naar de map die geopend moet worden |
| `use_insiders` | boolean (optioneel) | Of je VS Code Insiders moet gebruiken in plaats van reguliere VS Code |

Het hulpmiddel geeft een JSON-object terug met:
- `success`: Boolean die aangeeft of de bewerking succesvol was
- `message` of `error`: Een bevestigingsbericht of een foutmelding

| Debug Modus | Beschrijving | Stappen om te debuggen |
| ---------- | ----------- | ---------------------- |
| Agent Builder | Debug de MCP server in de Agent Builder via Microsoft Foundry Toolkit voor Visual Studio Code. | 1. Open het Debug-paneel van VS Code. Selecteer `Debug in Agent Builder` en druk op `F5` om het debuggen van de MCP server te starten.<br>2. Selecteer een actieve Foundry deployment zoals `gpt-5.1`, voer dan `What is the weather in Shanghai?` in. De server wordt automatisch verbonden.<br>3. Klik `Run` om de server met de prompt te testen. |
| MCP Inspector | Debug de MCP server met behulp van MCP Inspector. | 1. Installeer [Node.js](https://nodejs.org/)<br> 2. Stel Inspector in: `cd inspector` && `npm install` <br> 3. Open het Debug-paneel van VS Code. Selecteer `Debug SSE in Inspector (Edge)` of `Debug SSE in Inspector (Chrome)`. Druk op F5 om te starten met debuggen.<br> 4. Wanneer MCP Inspector in de browser opent, klik op de `Connect` knop om deze MCP server te verbinden.<br> 5. Dan kun je `List Tools`, selecteer een hulpmiddel, voer parameters in, en `Run Tool` om je servercode te debuggen.<br> |

## Standaard Poorten en aanpassingen

| Debug Modus | Poorten | Definities | Aanpassingen | Opmerking |
| ---------- | ------- | ---------- | ----------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) om bovenstaande poorten te wijzigen. | N.v.t. |
| MCP Inspector | 3001 (Server); 5173 en 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bewerk [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) om bovenstaande poorten te wijzigen. | N.v.t. |

## Feedback

Als je feedback of suggesties hebt voor deze template, open dan een issue op de [Microsoft Foundry Toolkit voor Visual Studio Code GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->