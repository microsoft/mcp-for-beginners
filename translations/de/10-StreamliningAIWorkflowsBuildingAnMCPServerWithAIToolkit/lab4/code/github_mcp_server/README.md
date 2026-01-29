# Wetter MCP Server

Dies ist ein Beispiel-MCP-Server in Python, der Wetter-Tools mit simulierten Antworten implementiert. Er kann als Grundlage für Ihren eigenen MCP-Server verwendet werden. Er umfasst die folgenden Funktionen:

- **Wetter-Tool**: Ein Tool, das simulierte Wetterinformationen basierend auf dem angegebenen Standort bereitstellt.
- **Git Clone Tool**: Ein Tool, das ein Git-Repository in einen angegebenen Ordner klont.
- **VS Code Open Tool**: Ein Tool, das einen Ordner in VS Code oder VS Code Insiders öffnet.
- **Verbindung zum Agent Builder**: Eine Funktion, die es ermöglicht, den MCP-Server mit dem Agent Builder für Tests und Debugging zu verbinden.
- **Debugging im [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: Eine Funktion, die es ermöglicht, den MCP-Server mit dem MCP Inspector zu debuggen.

## Einstieg mit der Wetter-MCP-Server-Vorlage

> **Voraussetzungen**
>
> Um den MCP-Server auf Ihrem lokalen Entwicklungsrechner auszuführen, benötigen Sie:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (Erforderlich für das Tool `git_clone_repo`)
> - [VS Code](https://code.visualstudio.com/) oder [VS Code Insiders](https://code.visualstudio.com/insiders/) (Erforderlich für das Tool `open_in_vscode`)
> - (*Optional - falls Sie uv bevorzugen*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Umgebung vorbereiten

Es gibt zwei Ansätze, um die Umgebung für dieses Projekt einzurichten. Sie können je nach Vorliebe einen davon wählen.

> Hinweis: Laden Sie VSCode oder das Terminal neu, um sicherzustellen, dass die Python-Version der virtuellen Umgebung nach deren Erstellung verwendet wird.

| Ansatz | Schritte |
| ------ | -------- |
| Mit `uv` | 1. Virtuelle Umgebung erstellen: `uv venv` <br>2. VSCode-Befehl "***Python: Interpreter auswählen***" ausführen und die Python-Version der erstellten virtuellen Umgebung auswählen <br>3. Abhängigkeiten installieren (einschließlich Entwicklungsabhängigkeiten): `uv pip install -r pyproject.toml --extra dev` |
| Mit `pip` | 1. Virtuelle Umgebung erstellen: `python -m venv .venv` <br>2. VSCode-Befehl "***Python: Interpreter auswählen***" ausführen und die Python-Version der erstellten virtuellen Umgebung auswählen <br>3. Abhängigkeiten installieren (einschließlich Entwicklungsabhängigkeiten): `pip install -e .[dev]` |

Nach der Einrichtung der Umgebung können Sie den Server auf Ihrem lokalen Entwicklungsrechner über den Agent Builder als MCP-Client ausführen, um loszulegen:
1. Öffnen Sie das Debug-Panel in VS Code. Wählen Sie `Debug in Agent Builder` oder drücken Sie `F5`, um das Debugging des MCP-Servers zu starten.
2. Verwenden Sie den AI Toolkit Agent Builder, um den Server mit [diesem Prompt](../../../../../../../../../../../open_prompt_builder) zu testen. Der Server wird automatisch mit dem Agent Builder verbunden.
3. Klicken Sie auf `Run`, um den Server mit dem Prompt zu testen.

**Herzlichen Glückwunsch**! Sie haben den Wetter-MCP-Server erfolgreich auf Ihrem lokalen Entwicklungsrechner über den Agent Builder als MCP-Client ausgeführt.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Was ist in der Vorlage enthalten?

| Ordner / Datei | Inhalt                                      |
| -------------- | ------------------------------------------- |
| `.vscode`      | VSCode-Dateien für Debugging                |
| `.aitk`        | Konfigurationen für das AI Toolkit          |
| `src`          | Der Quellcode für den Wetter-MCP-Server     |

## So debuggen Sie den Wetter-MCP-Server

> Hinweise:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ist ein visuelles Entwickler-Tool zum Testen und Debuggen von MCP-Servern.
> - Alle Debugging-Modi unterstützen Breakpoints, sodass Sie Breakpoints im Implementierungscode der Tools setzen können.

## Verfügbare Tools

### Wetter-Tool
Das Tool `get_weather` liefert simulierte Wetterinformationen für einen angegebenen Standort.

| Parameter  | Typ    | Beschreibung                                   |
| ---------- | ------ | --------------------------------------------- |
| `location` | string | Standort, für den das Wetter abgerufen werden soll (z. B. Stadtname, Bundesland oder Koordinaten) |

### Git Clone Tool
Das Tool `git_clone_repo` klont ein Git-Repository in einen angegebenen Ordner.

| Parameter       | Typ    | Beschreibung                                   |
| --------------- | ------ | --------------------------------------------- |
| `repo_url`      | string | URL des zu klonenden Git-Repositorys          |
| `target_folder` | string | Pfad zu dem Ordner, in den das Repository geklont werden soll |

Das Tool gibt ein JSON-Objekt zurück mit:
- `success`: Boolean, der angibt, ob die Operation erfolgreich war
- `target_folder` oder `error`: Der Pfad des geklonten Repositorys oder eine Fehlermeldung

### VS Code Open Tool
Das Tool `open_in_vscode` öffnet einen Ordner in der VS Code- oder VS Code Insiders-Anwendung.

| Parameter      | Typ     | Beschreibung                                   |
| -------------- | ------- | --------------------------------------------- |
| `folder_path`  | string  | Pfad zu dem Ordner, der geöffnet werden soll  |
| `use_insiders` | boolean (optional) | Ob VS Code Insiders anstelle von regulärem VS Code verwendet werden soll |

Das Tool gibt ein JSON-Objekt zurück mit:
- `success`: Boolean, der angibt, ob die Operation erfolgreich war
- `message` oder `error`: Eine Bestätigungsnachricht oder eine Fehlermeldung

| Debug-Modus    | Beschreibung | Schritte zum Debuggen                     |
| -------------- | ------------ | ----------------------------------------- |
| Agent Builder  | Debuggen des MCP-Servers im Agent Builder über das AI Toolkit. | 1. Öffnen Sie das Debug-Panel in VS Code. Wählen Sie `Debug in Agent Builder` und drücken Sie `F5`, um das Debugging des MCP-Servers zu starten.<br>2. Verwenden Sie den AI Toolkit Agent Builder, um den Server mit [diesem Prompt](../../../../../../../../../../../open_prompt_builder) zu testen. Der Server wird automatisch mit dem Agent Builder verbunden.<br>3. Klicken Sie auf `Run`, um den Server mit dem Prompt zu testen. |
| MCP Inspector  | Debuggen des MCP-Servers mit dem MCP Inspector. | 1. Installieren Sie [Node.js](https://nodejs.org/)<br> 2. Richten Sie den Inspector ein: `cd inspector` && `npm install` <br> 3. Öffnen Sie das Debug-Panel in VS Code. Wählen Sie `Debug SSE in Inspector (Edge)` oder `Debug SSE in Inspector (Chrome)`. Drücken Sie F5, um das Debugging zu starten.<br> 4. Wenn der MCP Inspector im Browser gestartet wird, klicken Sie auf die Schaltfläche `Connect`, um diesen MCP-Server zu verbinden.<br> 5. Anschließend können Sie `List Tools` auswählen, Parameter eingeben und `Run Tool`, um Ihren Servercode zu debuggen. |

## Standardports und Anpassungen

| Debug-Modus    | Ports | Definitionen | Anpassungen | Hinweis |
| -------------- | ----- | ------------ | ----------- | ------- |
| Agent Builder  | 3001  | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bearbeiten Sie [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), um die oben genannten Ports zu ändern. | N/A |
| MCP Inspector  | 3001 (Server); 5173 und 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | Bearbeiten Sie [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json), um die oben genannten Ports zu ändern. | N/A |

## Feedback

Wenn Sie Feedback oder Vorschläge zu dieser Vorlage haben, öffnen Sie bitte ein Issue im [AI Toolkit GitHub Repository](https://github.com/microsoft/vscode-ai-toolkit/issues).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.