# Bereitstellung von MCP-Servern

> [!NOTE]
> Konfigurationsbeispiele, die ein `/sse`-Endpunktziel verwenden, richten sich an den Legacy HTTP+SSE
> Transport. MCP `2026-07-28` Remote-Server verwenden Streamable HTTP, normalerweise an einem
> serverdefinierten Endpunkt wie `/mcp`.

Die Bereitstellung Ihres MCP-Servers ermöglicht anderen den Zugriff auf seine Werkzeuge und Ressourcen über Ihre lokale Umgebung hinaus. Es gibt mehrere Bereitstellungsstrategien, die je nach Ihren Anforderungen an Skalierbarkeit, Zuverlässigkeit und Verwaltungsfreundlichkeit zu berücksichtigen sind. Im Folgenden finden Sie Anleitungen zur Bereitstellung von MCP-Servern lokal, in Containern und in der Cloud.

## Überblick

Diese Lektion behandelt, wie Sie Ihre MCP Server-App bereitstellen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Verschiedene Bereitstellungsansätze zu bewerten.
- Ihre App bereitzustellen.

## Lokale Entwicklung und Bereitstellung

Wenn Ihr Server auf dem Rechner der Nutzer laufen soll, können Sie die folgenden Schritte befolgen:

1. **Laden Sie den Server herunter**. Falls Sie den Server nicht selbst geschrieben haben, laden Sie ihn zuerst auf Ihre Maschine herunter.
1. **Starten Sie den Serverprozess**: Führen Sie Ihre MCP-Serveranwendung aus

Für SSE (nicht nötig für stdio-Typ Server)

1. **Netzwerkkonfiguration**: Stellen Sie sicher, dass der Server auf dem erwarteten Port erreichbar ist
1. **Verbinden Sie die Clients**: Verwenden Sie lokale Verbindungs-URLs wie `http://localhost:3000`

## Cloud-Bereitstellung

MCP-Server können auf verschiedenen Cloud-Plattformen bereitgestellt werden:

- **Serverlose Funktionen**: Stellen Sie leichte MCP-Server als serverlose Funktionen bereit
- **Container-Dienste**: Verwenden Sie Dienste wie Azure Container Apps, AWS ECS oder Google Cloud Run
- **Kubernetes**: Stellen Sie MCP-Server in Kubernetes-Clustern für hohe Verfügbarkeit bereit und verwalten Sie sie

### Beispiel: Azure Container Apps

Azure Container Apps unterstützen die Bereitstellung von MCP-Servern. Die Funktion befindet sich noch in der Entwicklung und unterstützt aktuell SSE-Server.

So können Sie vorgehen:

1. Klonen Sie ein Repository:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Führen Sie es lokal aus, um alles zu testen:

  ```sh
  uv venv
  uv sync

  # Linux/macOS
  export API_KEYS=<AN_API_KEY>
  # Windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Um es lokal auszuprobieren, erstellen Sie eine *mcp.json*-Datei in einem *.vscode*-Verzeichnis und fügen Sie folgenden Inhalt hinzu:

  ```json
  {
      "inputs": [
          {
              "type": "promptString",
              "id": "weather-api-key",
              "description": "Weather API Key",
              "password": true
          }
      ],
      "servers": {
          "weather-sse": {
              "type": "sse",
              "url": "http://localhost:8000/sse",
              "headers": {
                  "x-api-key": "${input:weather-api-key}"
              }
          }
      }
  }
  ```

  Sobald der SSE-Server gestartet ist, können Sie auf das Wiedergabe-Symbol in der JSON-Datei klicken. Sie sollten dann Werkzeuge auf dem Server sehen, die von GitHub Copilot erkannt werden, siehe das Werkzeug-Symbol.

1. Um bereitzustellen, führen Sie folgenden Befehl aus:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Da haben Sie es, stellen Sie es lokal oder über Azure mit diesen Schritten bereit.

## Weitere Ressourcen

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)
- [Azure Container Apps Artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)
- [Azure Container Apps MCP Repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)


## Was kommt als Nächstes

- Nächstes Thema: [Erweiterte Server-Themen](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->