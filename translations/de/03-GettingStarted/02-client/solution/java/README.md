# MCP Java Client - Rechner-Demo

Dieses Projekt zeigt, wie man einen Java-Client erstellt, der sich mit einem MCP (Model Context Protocol) Server verbindet und mit ihm interagiert. In diesem Beispiel verbinden wir uns mit dem Rechner-Server aus Kapitel 01 und führen verschiedene mathematische Operationen durch.

## Voraussetzungen

Bevor Sie diesen Client ausführen, müssen Sie:

1. **Den Rechner-Server** aus Kapitel 01 starten:
   - Wechseln Sie in das Verzeichnis des Rechner-Servers: `03-GettingStarted/01-first-server/solution/java/`
   - Bauen und starten Sie den Rechner-Server:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Der Server sollte unter `http://localhost:8080` laufen

2. **Java 21 oder höher** auf Ihrem System installiert haben
3. **Maven** (über Maven Wrapper enthalten)

## Was ist der SDKClient?

Der `SDKClient` ist eine Java-Anwendung, die zeigt, wie man:
- Eine Verbindung zu einem MCP-Server über Server-Sent Events (SSE) Transport herstellt
- Verfügbare Tools vom Server auflistet
- Verschiedene Rechner-Funktionen remote aufruft
- Antworten verarbeitet und Ergebnisse anzeigt

## Funktionsweise

Der Client nutzt das Spring AI MCP Framework, um:

1. **Verbindung herzustellen**: Erstellt einen WebFlux SSE Client Transport, um sich mit dem Rechner-Server zu verbinden
2. **Client zu initialisieren**: Richtet den MCP-Client ein und stellt die Verbindung her
3. **Tools zu entdecken**: Listet alle verfügbaren Rechner-Operationen auf
4. **Operationen auszuführen**: Ruft verschiedene mathematische Funktionen mit Beispielwerten auf
5. **Ergebnisse anzuzeigen**: Zeigt die Resultate jeder Berechnung an

## Projektstruktur

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Wichtige Abhängigkeiten

Das Projekt verwendet folgende zentrale Abhängigkeiten:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Diese Abhängigkeit stellt bereit:
- `McpClient` - Die Haupt-Client-Schnittstelle
- `WebFluxSseClientTransport` - SSE-Transport für webbasierte Kommunikation
- MCP-Protokoll-Schemata sowie Anfrage-/Antworttypen

## Projekt bauen

Bauen Sie das Projekt mit dem Maven Wrapper:

```cmd
.\mvnw clean install
```

## Client ausführen

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Hinweis**: Stellen Sie sicher, dass der Rechner-Server unter `http://localhost:8080` läuft, bevor Sie einen dieser Befehle ausführen.

## Was der Client macht

Beim Ausführen verbindet sich der Client mit dem Rechner-Server unter `http://localhost:8080` und:

1. **Verbindet sich** mit dem Rechner-Server
2. **Listet Tools auf** - Zeigt alle verfügbaren Rechner-Operationen an
3. **Führt Berechnungen durch**:
   - Addition: 5 + 3 = 8
   - Subtraktion: 10 - 4 = 6
   - Multiplikation: 6 × 7 = 42
   - Division: 20 ÷ 4 = 5
   - Potenz: 2^8 = 256
   - Quadratwurzel: √16 = 4
   - Absolutwert: |-5.5| = 5.5
   - Hilfe: Zeigt verfügbare Operationen an

## Erwartete Ausgabe

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Hinweis**: Am Ende können Maven-Warnungen über verbleibende Threads erscheinen – das ist bei reaktiven Anwendungen normal und kein Fehler.

## Code verstehen

### 1. Transport einrichten
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Dies erstellt einen SSE (Server-Sent Events) Transport, der sich mit dem Rechner-Server verbindet.

### 2. Client erstellen
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Erstellt einen synchronen MCP-Client und initialisiert die Verbindung.

### 3. Tools aufrufen
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Ruft das Tool „add“ mit den Parametern a=5.0 und b=3.0 auf.

## Fehlerbehebung

### Server läuft nicht
Wenn Verbindungsfehler auftreten, stellen Sie sicher, dass der Rechner-Server aus Kapitel 01 läuft:
```
Error: Connection refused
```
**Lösung**: Starten Sie zuerst den Rechner-Server.

### Port bereits belegt
Wenn Port 8080 bereits verwendet wird:
```
Error: Address already in use
```
**Lösung**: Beenden Sie andere Anwendungen, die Port 8080 nutzen, oder ändern Sie den Port des Servers.

### Build-Fehler
Wenn Build-Fehler auftreten:
```cmd
.\mvnw clean install -DskipTests
```

## Mehr erfahren

- [Spring AI MCP Dokumentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Spezifikation](https://modelcontextprotocol.io/)
- [Spring WebFlux Dokumentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.