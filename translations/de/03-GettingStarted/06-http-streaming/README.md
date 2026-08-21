# HTTPS-Streaming mit dem Model Context Protocol (MCP)

Dieses Kapitel bietet eine umfassende Anleitung zur Implementierung von sicherem, skalierbarem und Echtzeit-Streaming mit dem Model Context Protocol (MCP) über HTTPS. Es behandelt die Motivation für Streaming, die verfügbaren Transportmechanismen, wie man streamfähiges HTTP in MCP implementiert, Sicherheitsbest Practices, die Migration von SSE und praktische Hinweise zum Aufbau eigener Streaming-MCP-Anwendungen.

> **Vorausschau:** Diese Lektion beschreibt Streamable HTTP unter **MCP Specification 2025-11-25**, wobei eine Sitzung während der `initialize`-Phase etabliert und mit einem `Mcp-Session-Id`-Header gebunden wird. Der Release Candidate `2026-07-28` entfernt den Handshake und die Session-ID vollständig, sodass jede Anfrage eigenständig ist und an jede Serverinstanz ohne Sticky Sessions routbar ist. Details finden Sie unter [What’s Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transportmechanismen und Streaming in MCP

Dieser Abschnitt untersucht die verschiedenen in MCP verfügbaren Transportmechanismen und deren Rolle bei der Ermöglichung von Streaming-Funktionen für die Echtzeitkommunikation zwischen Clients und Servern.

### Was ist ein Transportmechanismus?

Ein Transportmechanismus definiert, wie Daten zwischen Client und Server ausgetauscht werden. MCP unterstützt mehrere Transporttypen, die unterschiedliche Umgebungen und Anforderungen abdecken:

- **stdio**: Standard-Ein-/Ausgabe, geeignet für lokale und CLI-basierte Werkzeuge. Einfach, aber nicht für Web oder Cloud geeignet.
- **SSE (Server-Sent Events)**: Ermöglicht es Servern, Echtzeit-Updates über HTTP an Clients zu senden. Gut für Web-UIs, aber in Skalierbarkeit und Flexibilität eingeschränkt. Ab MCP Specification 2025-06-18 wurde der eigenständige SSE-Transport zugunsten von „Streamable HTTP“ eingestellt.
- **Streamable HTTP**: Moderner HTTP-basierter Streaming-Transport, unterstützt Benachrichtigungen und bessere Skalierbarkeit. Empfohlen für die meisten Produktions- und Cloud-Szenarien.

### Vergleichstabelle

Werfen Sie einen Blick auf die folgende Vergleichstabelle, um die Unterschiede zwischen diesen Transportmechanismen zu verstehen:

| Transport         | Echtzeit-Updates | Streaming | Skalierbarkeit | Anwendungsfall         |
|-------------------|------------------|-----------|---------------|------------------------|
| stdio             | Nein             | Nein      | Niedrig       | Lokale CLI-Tools       |
| SSE               | Ja               | Ja        | Mittel        | Web, Echtzeit-Updates  |
| Streamable HTTP   | Ja               | Ja        | Hoch          | Cloud, Multi-Client    |

> **Tipp:** Die Wahl des richtigen Transports beeinflusst Leistung, Skalierbarkeit und Benutzererfahrung. **Streamable HTTP** wird für moderne, skalierbare und cloudfähige Anwendungen empfohlen.

Beachten Sie die Transports stdio und SSE, die in den vorherigen Kapiteln behandelt wurden, sowie den in diesem Kapitel behandelten Transport Streamable HTTP.

## Streaming: Konzepte und Motivation

Das Verständnis der grundlegenden Konzepte und Motivationen hinter Streaming ist entscheidend für die Implementierung effektiver Echtzeit-Kommunikationssysteme.

**Streaming** ist eine Technik in der Netzwerkprogrammierung, die es ermöglicht, Daten in kleinen, handhabbaren Teilen oder als Ereignisfolge zu senden und zu empfangen, anstatt auf eine vollständige Antwort zu warten. Dies ist besonders nützlich für:

- Große Dateien oder Datensätze.
- Echtzeit-Updates (z. B. Chat, Fortschrittsbalken).
- Lang laufende Berechnungen, bei denen der Benutzer informiert bleiben soll.

Hier sind die wichtigsten Punkte zum Streaming auf hoher Ebene:

- Daten werden fortlaufend geliefert, nicht auf einmal.
- Der Client kann Daten verarbeiten, sobald sie ankommen.
- Verringert die wahrgenommene Latenz und verbessert die Benutzererfahrung.

### Warum Streaming verwenden?

Die Gründe für die Nutzung von Streaming sind folgende:

- Benutzer erhalten sofort Rückmeldung, nicht erst am Ende
- Ermöglicht Echtzeitanwendungen und reaktionsfähige UIs
- Effizientere Nutzung von Netzwerk- und Rechenressourcen

### Einfaches Beispiel: HTTP Streaming Server & Client

Hier ist ein einfaches Beispiel, wie Streaming implementiert werden kann:

#### Python

**Server (Python, mit FastAPI und StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Client (Python, mit requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dieses Beispiel zeigt, wie ein Server eine Reihe von Nachrichten an den Client sendet, sobald sie verfügbar sind, anstatt auf alle Nachrichten gleichzeitig zu warten.

**So funktioniert es:**

- Der Server liefert jede Nachricht, sobald sie bereitsteht.
- Der Client empfängt und gibt jeden Datenblock aus, sobald er ankommt.

**Anforderungen:**

- Der Server muss eine Streaming-Antwort verwenden (z. B. `StreamingResponse` in FastAPI).
- Der Client muss die Antwort als Stream verarbeiten (`stream=True` in requests).
- Der Content-Type ist üblicherweise `text/event-stream` oder `application/octet-stream`.

#### Java

**Server (Java, mit Spring Boot und Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Client (Java, mit Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Anmerkungen zur Java-Implementierung:**

- Verwendet Spring Boot Reactive Stack mit `Flux` fürs Streaming
- `ServerSentEvent` bietet strukturierten Event-Stream mit Event-Typen
- `WebClient` mit `bodyToFlux()` ermöglicht reaktives Streaming
- `delayElements()` simuliert Verarbeitungszeit zwischen Events
- Events können Typen (`info`, `result`) haben für bessere Client-Verarbeitung

### Vergleich: Klassisches Streaming vs. MCP Streaming

Die Unterschiede zwischen klassischem Streaming und Streaming in MCP können folgendermaßen dargestellt werden:

| Merkmal               | Klassisches HTTP-Streaming        | MCP Streaming (Benachrichtigungen)   |
|-----------------------|---------------------------------|---------------------------------------|
| Hauptantwort          | Chunked                         | Einzeln, am Ende                     |
| Fortschrittsupdates   | Als Datenblöcke gesendet        | Als Benachrichtigungen gesendet      |
| Client-Anforderungen  | Muss Stream verarbeiten          | Muss Nachrichten-Handler implementieren |
| Anwendungsfall        | Große Dateien, AI Token-Streams | Fortschritte, Logs, Echtzeit-Feedback|

### Beobachtete Hauptunterschiede

Außerdem gibt es einige wichtige Unterschiede:

- **Kommunikationsmuster:**
  - Klassisches HTTP-Streaming: Verwendet einfache Chunked Transfer-Encoding, um Daten in Blöcken zu senden
  - MCP Streaming: Verwendet ein strukturiertes Benachrichtigungssystem mit JSON-RPC-Protokoll

- **Nachrichtenformat:**
  - Klassisches HTTP: Nur Textblöcke mit Zeilenumbrüchen
  - MCP: Strukturierte LoggingMessageNotification-Objekte mit Metadaten

- **Client-Implementierung:**
  - Klassisches HTTP: Einfacher Client, der Streaming-Antworten verarbeitet
  - MCP: Anspruchsvollerer Client mit Nachrichten-Handler für verschiedene Nachrichtentypen

- **Fortschritts-Updates:**
  - Klassisches HTTP: Fortschritt ist Teil des Hauptantworts-Streams
  - MCP: Fortschritt wird über separate Benachrichtigungsnachrichten gesendet, während das Hauptergebnis am Ende kommt

### Empfehlungen

Es gibt einige Empfehlungen bezüglich der Wahl zwischen klassischem Streaming (wie oben mit dem Endpunkt `/stream` gezeigt) und Streaming via MCP.

- **Für einfache Streaming-Anforderungen:** Klassisches HTTP-Streaming ist einfacher zu implementieren und für grundlegende Streaming-Bedürfnisse ausreichend.

- **Für komplexe, interaktive Anwendungen:** MCP Streaming bietet einen strukturierten Ansatz mit reichhaltigen Metadaten und Trennung zwischen Benachrichtigungen und Endergebnissen.

- **Für KI-Anwendungen:** Das Benachrichtigungssystem von MCP ist besonders nützlich für lang laufende KI-Aufgaben, bei denen Benutzer über Fortschritte informiert werden sollen.

## Streaming in MCP

Sie haben also bisher einige Empfehlungen und Vergleiche zur Unterscheidung von klassischem Streaming und Streaming in MCP gesehen. Nun wollen wir im Detail betrachten, wie Sie Streaming in MCP nutzen können.

Das Verständnis, wie Streaming innerhalb des MCP-Frameworks funktioniert, ist entscheidend, um reaktionsfähige Anwendungen zu bauen, die Benutzern während lang laufender Operationen Echtzeit-Feedback liefern.

Im MCP geht es beim Streaming nicht darum, die Hauptantwort in Blöcken zu senden, sondern **Benachrichtigungen** an den Client zu senden, während ein Werkzeug eine Anfrage verarbeitet. Diese Benachrichtigungen können Fortschrittsupdates, Logs oder andere Ereignisse sein.

### Wie es funktioniert

Das Hauptergebnis wird weiterhin als einzelne Antwort gesendet. Benachrichtigungen können jedoch während der Verarbeitung als separate Nachrichten gesendet werden und halten so den Client in Echtzeit auf dem Laufenden. Der Client muss in der Lage sein, diese Benachrichtigungen zu verarbeiten und anzuzeigen.

## Was ist eine Benachrichtigung?

Wir haben „Benachrichtigung“ gesagt, was bedeutet das im Kontext von MCP?

Eine Benachrichtigung ist eine vom Server an den Client gesendete Nachricht, die über Fortschritt, Status oder andere Ereignisse während einer lang laufenden Operation informiert. Benachrichtigungen verbessern Transparenz und Benutzererfahrung.

Beispielsweise soll ein Client eine Benachrichtigung senden, sobald der anfängliche Handshake mit dem Server erfolgt ist.

Eine Benachrichtigung sieht in Form einer JSON-Nachricht so aus:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Benachrichtigungen gehören in MCP zu einem Thema, das als ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) bezeichnet wird.

> **Abschalt-Hinweis:** Der MCP Specification Release Candidate `2026-07-28` kennzeichnet die Logging-Primitiv als veraltet zugunsten von `stderr` für stdio-Transporte und OpenTelemetry für strukturierte Observability. Logging funktioniert weiterhin in `2025-11-25` und mindestens ein Jahr nach einer formalen Abschaltung. Siehe [What’s Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Um Logging zu aktivieren, muss der Server es als Feature/Fähigkeit freischalten, etwa so:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Je nach verwendetem SDK ist Logging möglicherweise standardmäßig aktiviert oder muss explizit in der Serverkonfiguration aktiviert werden.

Es gibt verschiedene Benachrichtigungstypen:

| Ebene     | Beschreibung                  | Beispielanwendung              |
|-----------|------------------------------|-------------------------------|
| debug     | Detaillierte Debug-Informationen | Funktions-Ein-/Ausgangspunkt  |
| info      | Allgemeine Informationsmeldungen | Fortschrittsupdates          |
| notice    | Normale, aber bedeutende Ereignisse | Konfigurationsänderungen     |
| warning   | Warnbedingungen               | Nutzung veralteter Funktionen |
| error     | Fehlerbedingungen             | Operation schlägt fehl         |
| critical  | Kritische Bedingungen         | Ausfälle von Systemkomponenten |
| alert     | Unmittelbar erforderliche Maßnahmen | Datenkorruption erkannt      |
| emergency | System nicht betriebsbereit   | Totalausfall des Systems       |

## Implementierung von Benachrichtigungen in MCP

Um Benachrichtigungen in MCP zu implementieren, müssen sowohl Server- als auch Client-Seite eingerichtet werden, um Echtzeit-Updates zu verarbeiten. So kann Ihre Anwendung den Benutzern während lang laufender Operationen sofortiges Feedback geben.

### Serverseitig: Senden von Benachrichtigungen

Beginnen wir mit dem Server. In MCP definieren Sie Werkzeuge, die Benachrichtigungen während der Verarbeitung von Anfragen senden können. Der Server verwendet das Kontextobjekt (meist `ctx`), um Nachrichten an den Client zu senden.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Im obigen Beispiel sendet das Werkzeug `process_files` drei Benachrichtigungen an den Client, während es jede Datei verarbeitet. Die Methode `ctx.info()` wird zum Senden von Informationsmeldungen verwendet.

Zusätzlich muss Ihr Server einen Streaming-Transport (z. B. `streamable-http`) verwenden, und Ihr Client muss einen Nachrichten-Handler implementieren, der Benachrichtigungen verarbeitet. So richten Sie den Server für die Nutzung des `streamable-http`-Transports ein:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

In diesem .NET-Beispiel ist das Werkzeug `ProcessFiles` mit dem Attribut `Tool` dekoriert und sendet drei Benachrichtigungen an den Client, während jede Datei verarbeitet wird. Die Methode `ctx.Info()` wird verwendet, um Informationsmeldungen zu senden.

Um Benachrichtigungen in Ihrem .NET MCP-Server zu aktivieren, stellen Sie sicher, dass Sie einen Streaming-Transport verwenden:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Clientseitig: Empfangen von Benachrichtigungen

Der Client muss einen Nachrichten-Handler implementieren, um Benachrichtigungen zu verarbeiten und anzuzeigen, sobald sie eintreffen.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

Im obigen Code prüft die Funktion `message_handler`, ob die eingehende Nachricht eine Benachrichtigung ist. Falls ja, wird die Benachrichtigung ausgegeben; andernfalls wird sie als reguläre Servernachricht verarbeitet. Beachten Sie auch, wie die `ClientSession` mit dem `message_handler` initialisiert wird, um eingehende Benachrichtigungen zu handhaben.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

In diesem .NET-Beispiel prüft die Funktion `MessageHandler`, ob die eingehende Nachricht eine Benachrichtigung ist. Falls ja, wird die Benachrichtigung ausgegeben; andernfalls wird sie als normale Servernachricht verarbeitet. Die `ClientSession` wird über die `ClientSessionOptions` mit dem Nachrichten-Handler initialisiert.

Um Benachrichtigungen zu aktivieren, stellen Sie sicher, dass Ihr Server einen Streaming-Transport (wie `streamable-http`) verwendet und Ihr Client einen Nachrichten-Handler zur Verarbeitung von Benachrichtigungen implementiert.

## Fortschrittsbenachrichtigungen & Szenarien

Dieser Abschnitt erläutert das Konzept der Fortschrittsbenachrichtigungen in MCP, warum sie wichtig sind und wie man diese mit Streamable HTTP implementiert. Ebenso gibt es eine praktische Aufgabe zur Festigung des Verständnisses.

Fortschrittsbenachrichtigungen sind Echtzeitnachrichten, die vom Server während lang laufender Operationen an den Client gesendet werden. Statt auf den Abschluss des gesamten Prozesses zu warten, hält der Server den Client über den aktuellen Status auf dem Laufenden. Dies verbessert Transparenz, Benutzererfahrung und erleichtert das Debugging.

**Beispiel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Warum Fortschrittsbenachrichtigungen verwenden?

Fortschrittsbenachrichtigungen sind aus mehreren Gründen wichtig:

- **Bessere Benutzererfahrung:** Benutzer sehen Updates während der Arbeit, nicht erst am Ende.
- **Echtzeit-Feedback:** Clients können Fortschrittsbalken oder Logs anzeigen, wodurch die App reaktionsfähig wirkt.
- **Einfacheres Debugging und Monitoring:** Entwickler und Benutzer erkennen, wo ein Prozess langsam ist oder hängen bleibt.

### So implementieren Sie Fortschrittsbenachrichtigungen

So können Sie Fortschrittsbenachrichtigungen in MCP umsetzen:

- **Serverseitig:** Verwenden Sie `ctx.info()` oder `ctx.log()`, um Benachrichtigungen zu senden, während jedes Element verarbeitet wird. Diese Nachrichten erreichen den Client vor dem Hauptergebnis.
- **Clientseitig:** Implementieren Sie einen Nachrichten-Handler, der Benachrichtigungen empfängt und anzeigt, sobald sie eintreffen. Der Handler unterscheidet zwischen Benachrichtigungen und finalem Ergebnis.

**Server-Beispiel:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Client-Beispiel:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Sicherheitsüberlegungen

Sicherheit sollte bei der Implementierung eines Servers oberste Priorität haben, insbesondere beim Einsatz von HTTP-basierten Transporten wie Streamable HTTP in MCP.

Bei der Implementierung von MCP-Servern mit HTTP-basierten Transporten ist Sicherheit ein vorrangiges Anliegen, das eine sorgfältige Beachtung mehrerer Angriffsvektoren und Schutzmechanismen erfordert.

### Überblick

Sicherheit ist entscheidend, wenn MCP-Server über HTTP zugänglich gemacht werden. Streamable HTTP bringt neue Angriffsflächen mit sich und erfordert eine sorgfältige Konfiguration.

Hier sind einige wichtige Sicherheitsüberlegungen:

- **Validierung des Origin-Headers**: Validieren Sie stets den `Origin`-Header, um DNS-Rebinding-Angriffe zu verhindern.
- **Binding an Localhost**: Binden Sie Server für die lokale Entwicklung an `localhost`, um eine öffentliche Exposition zu vermeiden.
- **Authentifizierung**: Implementieren Sie Authentifizierung (z. B. API-Schlüssel, OAuth) für Produktiveinsätze.
- **CORS**: Konfigurieren Sie Cross-Origin Resource Sharing (CORS)-Richtlinien, um den Zugriff einzuschränken.
- **HTTPS**: Verwenden Sie HTTPS in der Produktion zur Verschlüsselung des Datenverkehrs.

### Beste Praktiken

Hier sind zusätzliche bewährte Praktiken zur Umsetzung der Sicherheit in Ihrem MCP-Streaming-Server:

- Vertrauen Sie niemals eingehenden Anfragen ohne Validierung.
- Protokollieren und überwachen Sie alle Zugriffe und Fehler.
- Aktualisieren Sie regelmäßig Abhängigkeiten, um Sicherheitslücken zu schließen.

### Herausforderungen

Sie werden bei der Implementierung der Sicherheit in MCP-Streaming-Servern auf einige Herausforderungen stoßen:

- Die Balance zwischen Sicherheit und einfacher Entwicklung halten
- Kompatibilität mit verschiedenen Client-Umgebungen sicherstellen


## Upgrade von SSE zu Streamable HTTP

Für Anwendungen, die derzeit Server-Sent Events (SSE) nutzen, bietet die Migration zu Streamable HTTP erweiterte Möglichkeiten und bessere langfristige Nachhaltigkeit für Ihre MCP-Implementierungen.

### Warum updaten?

Es gibt zwei überzeugende Gründe, von SSE auf Streamable HTTP umzusteigen:

- Streamable HTTP bietet bessere Skalierbarkeit, Kompatibilität und reichere Benachrichtigungsunterstützung als SSE.
- Es ist der empfohlene Transport für neue MCP-Anwendungen.

### Migrationsschritte

So können Sie in Ihren MCP-Anwendungen von SSE zu Streamable HTTP migrieren:

- **Aktualisieren Sie den Servercode** zur Verwendung von `transport="streamable-http"` in `mcp.run()`.
- **Aktualisieren Sie den Clientcode**, um `streamablehttp_client` anstelle des SSE-Clients zu verwenden.
- **Implementieren Sie einen Nachrichten-Handler** im Client zur Verarbeitung von Benachrichtigungen.
- **Testen Sie die Kompatibilität** mit bestehenden Tools und Workflows.

### Kompatibilität erhalten

Es wird empfohlen, während des Migrationsprozesses die Kompatibilität mit bestehenden SSE-Clients aufrechtzuerhalten. Hier einige Strategien:

- Sie können sowohl SSE als auch Streamable HTTP unterstützen, indem Sie beide Transporte auf unterschiedlichen Endpunkten betreiben.
- Führen Sie eine schrittweise Migration der Clients zum neuen Transport durch.

### Herausforderungen

Stellen Sie sicher, dass Sie während der Migration folgende Herausforderungen adressieren:

- Sicherstellen, dass alle Clients aktualisiert werden
- Umgang mit Unterschieden bei der Zustellung von Benachrichtigungen

### Aufgabe: Erstellen Sie Ihre eigene Streaming-MCP-Anwendung

**Szenario:**
Entwickeln Sie einen MCP-Server und -Client, bei dem der Server eine Liste von Elementen (z. B. Dateien oder Dokumente) verarbeitet und für jedes verarbeitete Element eine Benachrichtigung sendet. Der Client soll jede Benachrichtigung bei Ankunft anzeigen.

**Schritte:**

1. Implementieren Sie ein Server-Tool, das eine Liste verarbeitet und für jedes Element Benachrichtigungen sendet.
2. Implementieren Sie einen Client mit einem Nachrichten-Handler, der Benachrichtigungen in Echtzeit anzeigt.
3. Testen Sie Ihre Implementierung, indem Sie Server und Client ausführen und die Benachrichtigungen beobachten.

[Lösung](./solution/README.md)

## Weiterführende Literatur & Was kommt als Nächstes?

Um Ihre Reise mit MCP-Streaming fortzusetzen und Ihr Wissen zu vertiefen, bietet dieser Abschnitt zusätzliche Ressourcen und empfohlene nächste Schritte für den Aufbau fortgeschrittener Anwendungen.

### Weiterführende Literatur

- [Microsoft: Einführung in HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Was kommt als Nächstes?

- Versuchen Sie, fortgeschrittenere MCP-Tools zu erstellen, die Streaming für Echtzeitanalysen, Chat oder kollaboratives Bearbeiten nutzen.
- Erkunden Sie die Integration von MCP-Streaming mit Frontend-Frameworks (React, Vue usw.) für Live-UI-Updates.
- Nächstes: [Verwendung des AI Toolkit für VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->