# Bereitstellung von MCP-Servern

Die Bereitstellung Ihres MCP-Servers ermöglicht es anderen, auf dessen Werkzeuge und Ressourcen über Ihre lokale Umgebung hinaus zuzugreifen. Es gibt mehrere Bereitstellungsstrategien, die je nach Ihren Anforderungen an Skalierbarkeit, Zuverlässigkeit und einfache Verwaltung zu berücksichtigen sind. Nachfolgend finden Sie Hinweise zur Bereitstellung von MCP-Servern lokal, in Containern und in der Cloud.

## Übersicht

Diese Lektion behandelt, wie Sie Ihre MCP Server-App bereitstellen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Verschiedene Bereitstellungsansätze zu bewerten.
- Ihre App bereitzustellen.

## Lokale Entwicklung und Bereitstellung

Wenn Ihr Server dazu gedacht ist, auf den Rechnern der Nutzer ausgeführt zu werden, können Sie die folgenden Schritte befolgen:

1. **Server herunterladen**. Wenn Sie den Server nicht selbst geschrieben haben, laden Sie ihn zuerst auf Ihren Rechner herunter.  
1. **Serverprozess starten**: Führen Sie Ihre MCP Server-Anwendung aus

Für SSE (nicht notwendig für stdio-Typ-Server)

1. **Netzwerk konfigurieren**: Stellen Sie sicher, dass der Server auf dem erwarteten Port erreichbar ist  
1. **Clients verbinden**: Verwenden Sie lokale Verbindungs-URLs wie `http://localhost:3000`

## Cloud-Bereitstellung

MCP-Server können auf verschiedenen Cloud-Plattformen bereitgestellt werden:

- **Serverless Functions**: Leichte MCP-Server als Serverless Functions bereitstellen  
- **Containerdienste**: Verwenden Sie Dienste wie Azure Container Apps, AWS ECS oder Google Cloud Run  
- **Kubernetes**: MCP-Server in Kubernetes-Clustern bereitstellen und verwalten für hohe Verfügbarkeit

### Beispiel: Azure Container Apps

Azure Container Apps unterstützen die Bereitstellung von MCP-Servern. Es ist noch ein Work in Progress und unterstützt derzeit SSE-Server.

So gehen Sie vor:

1. Ein Repository klonen:

  ```sh
  git clone https://github.com/anthonychu/azure-container-apps-mcp-sample.git
  ```

1. Lokale Ausführung zum Testen:

  ```sh
  uv venv
  uv sync

  # Linux/macOS
  export API_KEYS=<AN_API_KEY>
  # Windows
  set API_KEYS=<AN_API_KEY>

  uv run fastapi dev main.py
  ```

1. Um es lokal zu testen, erstellen Sie eine *mcp.json*-Datei in einem *.vscode*-Ordner und fügen Sie folgenden Inhalt hinzu:

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

  Sobald der SSE-Server gestartet ist, können Sie auf das Wiedergabesymbol in der JSON-Datei klicken, und Sie sollten nun Werkzeuge auf dem Server sehen, die von GitHub Copilot erkannt werden, siehe das Werkzeugsymbol.

1. Um bereitzustellen, führen Sie folgenden Befehl aus:

  ```sh
  az containerapp up -g <RESOURCE_GROUP_NAME> -n weather-mcp --environment mcp -l westus --env-vars API_KEYS=<AN_API_KEY> --source .
  ```

Damit haben Sie es: lokal bereitstellen, über diese Schritte auf Azure bereitstellen.

## Zusätzliche Ressourcen

- [Azure Functions + MCP](https://learn.microsoft.com/en-us/samples/azure-samples/remote-mcp-functions-dotnet/remote-mcp-functions-dotnet/)  
- [Azure Container Apps Artikel](https://techcommunity.microsoft.com/blog/appsonazureblog/host-remote-mcp-servers-in-azure-container-apps/4403550)  
- [Azure Container Apps MCP Repo](https://github.com/anthonychu/azure-container-apps-mcp-sample)  


## Was kommt als Nächstes

- Weiter: [Erweiterte Server-Themen](../10-advanced/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir bestrebt sind, Genauigkeit zu gewährleisten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->