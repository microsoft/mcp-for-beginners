# Weather MCP Server

Dies ist ein Beispiel für einen MCP Server in Python, der Wetter-Tools mit simulierten Antworten implementiert. Er kann als Grundlage für deinen eigenen MCP Server verwendet werden. Folgende Funktionen sind enthalten:

- **Weather Tool**: Ein Tool, das simulierte Wetterinformationen basierend auf dem angegebenen Standort bereitstellt.
- **Verbindung zum Agent Builder**: Eine Funktion, mit der du den MCP Server zum Testen und Debuggen mit dem Agent Builder verbinden kannst.
- **Debuggen im [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Eine Funktion, mit der du den MCP Server mit dem MCP Inspector debuggen kannst.

## Erste Schritte mit der Weather MCP Server Vorlage

> **Voraussetzungen**
>
> Um den MCP Server auf deinem lokalen Entwicklungsrechner auszuführen, benötigst du:
>
> - [Python](https://www.python.org/)
> - (*Optional – falls du uv bevorzugst*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Umgebung vorbereiten

Es gibt zwei Möglichkeiten, die Umgebung für dieses Projekt einzurichten. Du kannst je nach Vorliebe eine davon wählen.

> Hinweis: Lade VSCode oder das Terminal neu, um sicherzustellen, dass nach dem Erstellen der virtuellen Umgebung das richtige Python verwendet wird.

| Vorgehensweise | Schritte |
| -------------- | -------- |
| Mit `uv`       | 1. Virtuelle Umgebung erstellen: `uv venv` <br>2. Führe den VSCode-Befehl "***Python: Select Interpreter***" aus und wähle das Python aus der erstellten virtuellen Umgebung aus <br>3. Abhängigkeiten installieren (inklusive Dev-Abhängigkeiten): `uv pip install -r pyproject.toml --extra dev` |
| Mit `pip`      | 1. Virtuelle Umgebung erstellen: `python -m venv .venv` <br>2. Führe den VSCode-Befehl "***Python: Select Interpreter***" aus und wähle das Python aus der erstellten virtuellen Umgebung aus <br>3. Abhängigkeiten installieren (inklusive Dev-Abhängigkeiten): `pip install -e .[dev]` |

Nachdem die Umgebung eingerichtet ist, kannst du den Server auf deinem lokalen Entwicklungsrechner über den Agent Builder als MCP Client starten, um loszulegen:
1. Öffne das Debug-Panel in VS Code. Wähle `Debug in Agent Builder` oder drücke `F5`, um das Debugging des MCP Servers zu starten.
2. Verwende den AI Toolkit Agent Builder, um den Server mit [diesem Prompt](../../../../../../../../../../open_prompt_builder) zu testen. Der Server wird automatisch mit dem Agent Builder verbunden.
3. Klicke auf `Run`, um den Server mit dem Prompt zu testen.

**Herzlichen Glückwunsch**! Du hast den Weather MCP Server erfolgreich auf deinem lokalen Entwicklungsrechner über den Agent Builder als MCP Client ausgeführt.  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Was die Vorlage enthält

| Ordner / Datei | Inhalt                                      |
| -------------- | ------------------------------------------ |
| `.vscode`      | VSCode-Dateien für das Debugging           |
| `.aitk`        | Konfigurationen für AI Toolkit              |
| `src`          | Quellcode für den Weather MCP Server       |

## So debuggst du den Weather MCP Server

> Hinweise:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ist ein visuelles Entwickler-Tool zum Testen und Debuggen von MCP Servern.
> - Alle Debugging-Modi unterstützen Breakpoints, sodass du Haltepunkte im Code der Tool-Implementierung setzen kannst.

| Debug-Modus    | Beschreibung | Schritte zum Debuggen |
| -------------- | ------------ | --------------------- |
| Agent Builder  | Debugge den MCP Server im Agent Builder über AI Toolkit. | 1. Öffne das Debug-Panel in VS Code. Wähle `Debug in Agent Builder` und drücke `F5`, um das Debugging des MCP Servers zu starten.<br>2. Verwende den AI Toolkit Agent Builder, um den Server mit [diesem Prompt](../../../../../../../../../../open_prompt_builder) zu testen. Der Server wird automatisch mit dem Agent Builder verbunden.<br>3. Klicke auf `Run`, um den Server mit dem Prompt zu testen. |
| MCP Inspector | Debugge den MCP Server mit dem MCP Inspector. | 1. Installiere [Node.js](https://nodejs.org/)<br>2. Richte den Inspector ein: `cd inspector` && `npm install` <br>3. Öffne das Debug-Panel in VS Code. Wähle `Debug SSE in Inspector (Edge)` oder `Debug SSE in Inspector (Chrome)`. Drücke F5, um das Debugging zu starten.<br>4. Wenn der MCP Inspector im Browser startet, klicke auf den `Connect`-Button, um diesen MCP Server zu verbinden.<br>5. Danach kannst du `List Tools` auswählen, ein Tool auswählen, Parameter eingeben und `Run Tool` ausführen, um deinen Server-Code zu debuggen.<br> |

## Standardports und Anpassungen

| Debug-Modus   | Ports                         | Definitionen                      | Anpassungen                                                                 | Hinweis |
| ------------- | -----------------------------| -------------------------------- | -------------------------------------------------------------------------- | ------- |
| Agent Builder | 3001                         | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Bearbeite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), um die Ports zu ändern. | N/A     |
| MCP Inspector | 3001 (Server); 5173 und 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | Bearbeite [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json), um die Ports zu ändern. | N/A     |

## Feedback

Wenn du Feedback oder Vorschläge zu dieser Vorlage hast, öffne bitte ein Issue im [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit/issues)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.