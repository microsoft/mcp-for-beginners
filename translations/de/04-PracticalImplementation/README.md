# Praktische Umsetzung

[![Wie man MCP-Apps mit echten Tools und Workflows baut, testet und bereitstellt](../../../translated_images/de/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klicken Sie auf das obige Bild, um das Video zu dieser Lektion anzusehen)_

Die praktische Umsetzung ist der Ort, an dem die Kraft des Model Context Protocol (MCP) greifbar wird. Während das Verständnis der Theorie und Architektur hinter MCP wichtig ist, zeigt sich der wirkliche Wert, wenn Sie diese Konzepte anwenden, um Lösungen zu bauen, zu testen und bereitzustellen, die reale Probleme lösen. Dieses Kapitel schlägt eine Brücke zwischen konzeptionellem Wissen und praktischem Entwickeln und führt Sie durch den Prozess, MCP-basierte Anwendungen zum Leben zu erwecken.

Egal, ob Sie intelligente Assistenten entwickeln, KI in Geschäftsabläufe integrieren oder maßgeschneiderte Tools zur Datenverarbeitung bauen – MCP bietet eine flexible Grundlage. Sein sprachunabhängiges Design und offizielle SDKs für populäre Programmiersprachen machen es einer breiten Entwicklergemeinde zugänglich. Durch die Nutzung dieser SDKs können Sie schnell Prototypen erstellen, iterieren und Ihre Lösungen über verschiedene Plattformen und Umgebungen skalieren.

In den folgenden Abschnitten finden Sie praktische Beispiele, Beispielcode und Bereitstellungsstrategien, die zeigen, wie MCP in C#, Java mit Spring, TypeScript, JavaScript und Python implementiert wird. Sie lernen auch, wie Sie Ihre MCP-Server debuggen und testen, APIs verwalten und Lösungen mit Azure in der Cloud bereitstellen. Diese praktischen Ressourcen sollen Ihr Lernen beschleunigen und Ihnen helfen, robuste, produktionsreife MCP-Anwendungen sicher zu erstellen.

## Überblick

Diese Lektion konzentriert sich auf praktische Aspekte der MCP-Implementierung über mehrere Programmiersprachen hinweg. Wir erkunden, wie MCP SDKs in C#, Java mit Spring, TypeScript, JavaScript und Python verwendet werden, um robuste Anwendungen zu erstellen, MCP-Server zu debuggen und zu testen sowie wiederverwendbare Ressourcen, Prompts und Tools zu erstellen.

## Lernziele

Am Ende dieser Lektion können Sie:

- MCP-Lösungen mithilfe offizieller SDKs in verschiedenen Programmiersprachen implementieren
- MCP-Server systematisch debuggen und testen
- Server-Funktionen (Ressourcen, Prompts und Tools) erstellen und nutzen
- Effektive MCP-Workflows für komplexe Aufgaben entwerfen
- MCP-Implementierungen für Performance und Zuverlässigkeit optimieren

## Offizielle SDK-Ressourcen

Das Model Context Protocol bietet offizielle SDKs für mehrere Sprachen (angepaßt an die [MCP-Spezifikation 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java mit Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Hinweis:** benötigt Abhängigkeit von [Project Reactor](https://projectreactor.io). (Siehe [Diskussion Issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Arbeiten mit MCP SDKs

Dieser Abschnitt bietet praktische Beispiele zur Implementierung von MCP in mehreren Programmiersprachen. Beispielcode finden Sie im Verzeichnis `samples`, das nach Sprache organisiert ist.

### Verfügbare Beispiele

Das Repository enthält [Beispielimplementierungen](../../../04-PracticalImplementation/samples) in folgenden Sprachen:

- [C#](./samples/csharp/README.md)
- [Java mit Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Jedes Beispiel demonstriert wichtige MCP-Konzepte und Implementierungsmuster für die jeweilige Sprache und das Ökosystem.

### Praktische Anleitungen

Zusätzliche Anleitungen zur praktischen MCP-Implementierung:

- [Paginierung und große Ergebnislisten](./pagination/README.md) – Umgang mit cursor-basierter Paginierung für Tools, Ressourcen und große Datensätze

## Kernserver-Funktionen

MCP-Server können eine beliebige Kombination dieser Funktionen implementieren:

### Ressourcen

Ressourcen stellen Kontext und Daten bereit, die für den Benutzer oder das KI-Modell verwendet werden können:

- Dokumenten-Repositorien
- Wissensdatenbanken
- Strukturierte Datenquellen
- Dateisysteme

### Prompts

Prompts sind vorgefertigte Nachrichten und Workflows für Benutzer:

- Vorgegebene Gesprächsvorlagen
- Geführte Interaktionsmuster
- Spezialisierte Dialogstrukturen

### Tools

Tools sind Funktionen, die das KI-Modell ausführen kann:

- Datenverarbeitungs-Utilities
- Integration externer APIs
- Rechenfunktionen
- Suchfunktionalität

## Beispielimplementierungen: C# Implementation

Das offizielle C# SDK-Repository enthält mehrere Beispielimplementierungen, die unterschiedliche Aspekte von MCP demonstrieren:

- **Basic MCP Client**: Einfaches Beispiel, das zeigt, wie man einen MCP-Client erstellt und Tools aufruft
- **Basic MCP Server**: Minimale Serverimplementierung mit grundlegender Tool-Registrierung
- **Advanced MCP Server**: Voll ausgestatteter Server mit Tool-Registrierung, Authentifizierung und Fehlerbehandlung
- **ASP.NET Integration**: Beispiele, die die Integration mit ASP.NET Core zeigen
- **Tool-Implementierungsmuster**: Verschiedene Muster zur Implementierung von Tools mit unterschiedlichen Komplexitätsstufen

Das MCP C# SDK befindet sich in der Vorschau und APIs können sich ändern. Wir werden diesen Blog kontinuierlich aktualisieren, während sich das SDK weiterentwickelt.

### Hauptfunktionen

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Aufbau Ihres [ersten MCP Servers](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Für vollständige C# Implementierungsbeispiele besuchen Sie das [offizielle C# SDK Sample-Repository](https://github.com/modelcontextprotocol/csharp-sdk)

## Beispielimplementierung: Java mit Spring Implementation

Das Java mit Spring SDK bietet robuste MCP-Implementierungsoptionen mit Enterprise-Features.

### Hauptfunktionen

- Spring Framework Integration
- Starke Typensicherheit
- Unterstützung für reaktive Programmierung
- Umfassende Fehlerbehandlung

Für eine vollständige Beispielimplementierung in Java mit Spring sehen Sie sich das [Java mit Spring Beispiel](samples/java/containerapp/README.md) im Samples-Verzeichnis an.

## Beispielimplementierung: JavaScript Implementation

Das JavaScript SDK bietet einen leichten und flexiblen Ansatz zur MCP-Implementierung.

### Hauptfunktionen

- Unterstützung für Node.js und Browser
- Promise-basierte API
- Einfache Integration mit Express und anderen Frameworks
- WebSocket-Unterstützung für Streaming

Für eine vollständige Beispielimplementierung in JavaScript sehen Sie sich das [JavaScript Beispiel](samples/javascript/README.md) im Samples-Verzeichnis an.

## Beispielimplementierung: Python Implementation

Das Python SDK bietet einen pythonischen Ansatz zur MCP-Implementierung mit exzellenter Integration in ML-Frameworks.

### Hauptfunktionen

- Async/await-Unterstützung mit asyncio
- FastAPI Integration``
- Einfache Tool-Registrierung
- Native Integration mit populären ML-Bibliotheken

Für eine vollständige Python-Implementierung sehen Sie sich das [Python Beispiel](samples/python/README.md) im Samples-Verzeichnis an.

## API-Management

Azure API Management ist eine großartige Lösung, um MCP-Server zu sichern. Die Idee ist, eine Azure API Management-Instanz vor Ihren MCP-Server zu setzen und dort Features zu nutzen, die Sie wahrscheinlich benötigen wie:

- Ratenbegrenzung
- Tokenverwaltung
- Überwachung
- Lastverteilung
- Sicherheit

### Azure-Beispiel

Hier ist ein Azure-Beispiel, das genau das macht, also [Erstellen eines MCP-Servers und Absichern mit Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Sehen Sie unten, wie der Autorisierungsablauf abläuft:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Im obigen Bild passiert Folgendes:

- Authentifizierung/Autorisierung erfolgt über Microsoft Entra.
- Azure API Management agiert als Gateway und nutzt Richtlinien zur Steuerung und Verwaltung des Datenverkehrs.
- Azure Monitor protokolliert alle Anfragen zur weiteren Analyse.

#### Autorisierungsablauf

Schauen wir uns den Autorisierungsablauf genauer an:

![Sequenzdiagramm](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP-Autorisierungsspezifikation

Erfahren Sie mehr über die [MCP-Autorisierungsspezifikation](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Deployment eines Remote MCP Servers in Azure

Sehen wir uns an, ob wir das vorher erwähnte Beispiel bereitstellen können:

1. Klonen Sie das Repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrieren Sie den Ressourcenanbieter `Microsoft.App`.

   - Wenn Sie die Azure CLI verwenden, führen Sie `az provider register --namespace Microsoft.App --wait` aus.
   - Wenn Sie Azure PowerShell verwenden, führen Sie `Register-AzResourceProvider -ProviderNamespace Microsoft.App` aus. Überprüfen Sie nach einiger Zeit den Registrierungsstatus mit `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`.

1. Führen Sie diesen [azd](https://aka.ms/azd)-Befehl aus, um den API-Management-Dienst, die Function App (mit Code) und alle weiteren benötigten Azure-Ressourcen bereitzustellen

    ```shell
    azd up
    ```

    Dieser Befehl sollte alle Cloud-Ressourcen auf Azure bereitstellen

### Testen Ihres Servers mit MCP Inspector

1. In einem **neuen Terminalfenster** installieren und starten Sie MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Sie sollten eine Oberfläche ähnlich dieser sehen:

    ![Connect to Node inspector](../../../translated_images/de/connect.141db0b2bd05f096.webp)

1. Klicken Sie mit gedrückter STRG-Taste, um die MCP Inspector Web-App von der vom Tool angezeigten URL zu laden (z. B. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Stellen Sie den Transporttyp auf `SSE` ein
1. Stellen Sie die URL auf Ihren laufenden API Management SSE-Endpunkt, der nach `azd up` angezeigt wird, und **verbinden** Sie:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Tools auflisten**. Klicken Sie auf ein Tool und **Tool ausführen**.

Wenn alle Schritte funktioniert haben, sollten Sie jetzt mit dem MCP-Server verbunden sein und ein Tool aufrufen können.

## MCP-Server für Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dieses Set von Repositories ist eine Quickstart-Vorlage zum Erstellen und Bereitstellen benutzerdefinierter Remote-MCP (Model Context Protocol) Server mit Azure Functions in Python, C# .NET oder Node/TypeScript.

Die Samples bieten eine Komplettlösung, mit der Entwickler:

- Lokal entwickeln und ausführen können: Entwickeln und debuggen eines MCP-Servers auf dem lokalen Rechner
- In Azure bereitstellen können: Einfaches Deployment in die Cloud mit einem einfachen azd up-Befehl
- Von Clients verbinden können: Verbindung zum MCP-Server von verschiedenen Clients, inklusive des Copilot Agent Mode von VS Code und des MCP Inspector Tools

### Hauptfunktionen

- Sicherheit von Grund auf: Der MCP-Server ist durch Schlüssel und HTTPS geschützt
- Authentifizierungsoptionen: Unterstützt OAuth mit eingebauter Authentifizierung und/oder API Management
- Netzwerktrennung: Ermöglicht Netzwerktrennung mit Azure Virtual Networks (VNET)
- Serverless-Architektur: Nutzt Azure Functions für skalierbare, event-getriebene Ausführung
- Lokale Entwicklung: Umfassende Unterstützung für lokale Entwicklung und Debugging
- Einfache Bereitstellung: Vereinfachter Bereitstellungsprozess in Azure

Das Repository enthält alle notwendigen Konfigurationsdateien, Quellcode und Infrastrukturdefinitionen, um schnell mit einer produktionsreifen MCP-Server-Implementierung zu starten.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Beispielimplementierung von MCP mit Azure Functions in Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Beispielimplementierung von MCP mit Azure Functions in C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Beispielimplementierung von MCP mit Azure Functions in Node/TypeScript.

## Wichtige Erkenntnisse

- MCP SDKs bieten sprachspezifische Werkzeuge für die Implementierung robuster MCP-Lösungen
- Der Debugging- und Testprozess ist entscheidend für zuverlässige MCP-Anwendungen
- Wiederverwendbare Prompt-Vorlagen ermöglichen konsistente KI-Interaktionen
- Gut gestaltete Workflows können komplexe Aufgaben mit mehreren Tools orchestrieren
- Die Implementierung von MCP-Lösungen erfordert Berücksichtigung von Sicherheit, Leistung und Fehlerbehandlung

## Übung

Entwerfen Sie einen praktischen MCP-Workflow, der ein reales Problem in Ihrem Bereich adressiert:

1. Identifizieren Sie 3-4 Tools, die für die Lösung dieses Problems nützlich wären
2. Erstellen Sie ein Ablaufdiagramm, das zeigt, wie diese Tools interagieren
3. Implementieren Sie eine einfache Version eines Tools in Ihrer bevorzugten Sprache
4. Erstellen Sie eine Prompt-Vorlage, die dem Modell hilft, Ihr Tool effektiv zu nutzen

## Zusätzliche Ressourcen

---

## Was kommt als Nächstes

Weiter: [Erweiterte Themen](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, möchten wir darauf hinweisen, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->