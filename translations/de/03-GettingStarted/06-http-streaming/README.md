# HTTPS-Streaming mit Model Context Protocol (MCP)

Dieses Kapitel bietet eine umfassende Anleitung zur Implementierung von sicherem, skalierbarem und Echtzeit-Streaming mit dem Model Context Protocol (MCP) über HTTPS. Es behandelt die Motivation für Streaming, die verfügbaren Transportmechanismen, wie man streamfähiges HTTP in MCP implementiert, Sicherheitsbest Practices, Migration von SSE sowie praktische Anleitungen zum Erstellen eigener Streaming-MCP-Anwendungen.

> **Ausblick:** Diese Lektion beschreibt Streamable HTTP unter **MCP-Spezifikation 2025-11-25**, bei der eine Session während `initialize` aufgebaut und mit einem `Mcp-Session-Id`-Header angeheftet wird. Die Release-Kandidaten-Version `2026-07-28` entfernt den Handshake und die Session-ID komplett, sodass jede Anfrage selbstenthaltend ist und an jede Serverinstanz ohne Sticky Sessions geroutet werden kann. Details siehe [Was ändert sich in MCP: Der Release Candidate 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transportmechanismen und Streaming in MCP

Dieser Abschnitt behandelt die verschiedenen in MCP verfügbaren Transportmechanismen und ihre Rolle bei der Ermöglichung von Streaming-Funktionalitäten für die Echtzeitkommunikation zwischen Clients und Servern.

### Was ist ein Transportmechanismus?

Ein Transportmechanismus definiert, wie Daten zwischen Client und Server ausgetauscht werden. MCP unterstützt mehrere Transporttypen, um verschiedenen Umgebungen und Anforderungen gerecht zu werden:

- **stdio**: Standard Ein-/Ausgabe, geeignet für lokale und CLI-basierte Tools. Einfach, aber nicht für Web oder Cloud geeignet.
- **SSE (Server-Sent Events)**: Ermöglicht es Servern, Clients über HTTP mit Echtzeit-Updates zu versorgen. Gut für Web-UIs, aber begrenzt in Skalierbarkeit und Flexibilität. Seit MCP-Spezifikation 2025-06-18 wurde der eigenständige SSE-Transport durch den „Streamable HTTP“-Transport ersetzt.
- **Streamable HTTP**: Moderner HTTP-basierter Streaming-Transport, unterstützt Benachrichtigungen und bessere Skalierbarkeit. Empfohlen für die meisten Produktions- und Cloud-Szenarien.

### Vergleichstabelle

Sehen Sie sich die folgende Vergleichstabelle an, um die Unterschiede zwischen diesen Transportmechanismen zu verstehen:

| Transport         | Echtzeit-Updates | Streaming | Skalierbarkeit | Anwendungsfall          |
|-------------------|------------------|-----------|---------------|-------------------------|
| stdio             | Nein             | Nein      | Gering        | Lokale CLI-Tools        |
| SSE               | Ja               | Ja        | Mittel        | Web, Echtzeit-Updates   |
| Streamable HTTP   | Ja               | Ja        | Hoch          | Cloud, Multi-Client     |

> **Tipp:** Die Wahl des richtigen Transports beeinflusst Leistung, Skalierbarkeit und Benutzererfahrung. **Streamable HTTP** wird für moderne, skalierbare und Cloud-fähige Anwendungen empfohlen.

Beachten Sie die Transporte stdio und SSE, die in den vorherigen Kapiteln gezeigt wurden, und wie streamfähiges HTTP in diesem Kapitel behandelt wird.

## Streaming: Konzepte und Motivation

Das Verständnis der grundlegenden Konzepte und Motive hinter Streaming ist entscheidend für die Implementierung effektiver Echtzeitkommunikationssysteme.

**Streaming** ist eine Technik in der Netzwerkprogrammierung, die es ermöglicht, Daten in kleinen, handhabbaren Teilen oder als Folge von Ereignissen zu senden und zu empfangen, anstatt auf eine vollständige Antwort zu warten. Dies ist besonders nützlich für:

- Große Dateien oder Datensätze.
- Echtzeit-Updates (z.B. Chat, Fortschrittsanzeigen).
- Lang laufende Berechnungen, bei denen der Nutzer informiert bleiben soll.

Das sollten Sie auf hoher Ebene über Streaming wissen:

- Daten werden fortlaufend geliefert, nicht auf einmal.
- Der Client kann Daten verarbeiten, sobald sie ankommen.
- Verringert wahrgenommene Latenz und verbessert die Benutzererfahrung.

### Warum Streaming verwenden?

Die Gründe für die Verwendung von Streaming sind folgende:

- Nutzer erhalten sofort Feedback, nicht nur am Ende
- Ermöglicht Echtzeitanwendungen und reaktionsschnelle UIs
- Effizientere Nutzung von Netzwerk- und Rechenressourcen

### Einfaches Beispiel: HTTP-Streaming-Server & Client

Hier ein einfaches Beispiel, wie Streaming implementiert werden kann:

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

**Funktionsweise:**

- Der Server liefert jede Nachricht, sobald sie fertig ist.
- Der Client empfängt und gibt jede eingehende Datenportion aus.

**Anforderungen:**

- Der Server muss eine Streaming-Antwort verwenden (z.B. `StreamingResponse` in FastAPI).
- Der Client muss die Antwort als Stream verarbeiten (`stream=True` bei requests).
- Content-Type ist meist `text/event-stream` oder `application/octet-stream`.

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

**Java-Implementierungsnotizen:**

- Verwendet Spring Boots reaktives Stack mit `Flux` für Streaming
- `ServerSentEvent` ermöglicht strukturiertes Event-Streaming mit Event-Typen
- `WebClient` mit `bodyToFlux()` ermöglicht reaktive Streaming-Verarbeitung
- `delayElements()` simuliert Verarbeitungszeit zwischen Events
- Events können Typen wie (`info`, `result`) zur besseren Client-Verarbeitung haben

### Vergleich: Klassisches Streaming vs. MCP-Streaming

Die Unterschiede zwischen klassischem Streaming und MCP-Streaming lassen sich so darstellen:

| Merkmal               | Klassisches HTTP-Streaming       | MCP-Streaming (Benachrichtigungen) |
|-----------------------|---------------------------------|------------------------------------|
| Hauptantwort          | Chunked                         | Einzelne, am Ende                  |
| Fortschritts-Updates  | Werden als Daten-Chunks gesendet| Werden als Benachrichtigungen gesendet |
| Client-Anforderungen  | Muss Stream verarbeiten          | Muss Nachrichten-Handler implementieren |
| Anwendungsfall        | Große Dateien, AI-Token-Streams  | Fortschritt, Logs, Echtzeit-Feedback |

### Beobachtete Hauptunterschiede

Hier einige wichtige Unterschiede:

- **Kommunikationsmuster:**
  - Klassisches HTTP-Streaming: Verwendet einfache chunked Transfer-Encoding für Daten in Teilen
  - MCP-Streaming: Verwendet ein strukturiertes Benachrichtigungssystem mit JSON-RPC-Protokoll

- **Nachrichtenformat:**
  - Klassisches HTTP: Text-Chunks mit Zeilenumbrüchen
  - MCP: Strukturierte LoggingMessageNotification-Objekte mit Metadaten

- **Client-Implementierung:**
  - Klassisches HTTP: Einfacher Client, der Streaming-Antworten verarbeitet
  - MCP: Komplexerer Client mit Nachrichtenhandler zur Verarbeitung verschiedener Nachrichtentypen

- **Fortschritts-Updates:**
  - Klassisches HTTP: Fortschritt ist Teil des Hauptantwort-Streams
  - MCP: Fortschritt wird via separate Benachrichtigungen gesendet, Hauptantwort kommt am Ende

### Empfehlungen

Wir empfehlen Folgendes bei der Wahl zwischen klassischem Streaming (z.B. Endpoint `/stream`) und MCP-Streaming:

- **Für einfache Streaming-Bedürfnisse:** Klassisches HTTP-Streaming ist simpler und ausreichend für grundlegende Streaming-Anforderungen.

- **Für komplexe, interaktive Anwendungen:** MCP-Streaming bietet eine strukturiertere Vorgehensweise mit reichhaltigeren Metadaten und Trennung zwischen Benachrichtigungen und finalen Ergebnissen.

- **Für KI-Anwendungen:** MCPs Benachrichtigungssystem ist besonders nützlich für lang laufende KI-Aufgaben, bei denen Nutzer über Fortschritte informiert bleiben sollen.

## Streaming in MCP

Ok, Sie haben nun Empfehlungen und Vergleiche zur klassischen Streaming-Variante und MCP-Streaming gesehen. Nun schauen wir uns im Detail an, wie Sie Streaming in MCP nutzen können.

Das Verständnis, wie Streaming im MCP-Framework funktioniert, ist essenziell, um reaktionsfähige Anwendungen zu bauen, die Nutzern während lang dauernder Operationen Echtzeit-Feedback bieten.

Im MCP geht es beim Streaming nicht darum, die Hauptantwort in Teilen zu senden, sondern **Benachrichtigungen** an den Client zu schicken, während ein Tool eine Anfrage verarbeitet. Diese Benachrichtigungen können Fortschrittsmeldungen, Logs oder andere Ereignisse enthalten.

### Wie funktioniert das?

Das Hauptergebnis wird weiterhin als eine einzelne Antwort gesendet. Benachrichtigungen werden jedoch als separate Nachrichten während der Verarbeitung gesendet und halten den Client so in Echtzeit informiert. Der Client muss diese Benachrichtigungen empfangen und anzeigen können.

## Was ist eine Benachrichtigung?

Wir sprachen von "Benachrichtigung" – was bedeutet das im MCP-Kontext?

Eine Benachrichtigung ist eine Nachricht vom Server an den Client, die über Fortschritte, Status oder andere Ereignisse während einer lang laufenden Operation informiert. Benachrichtigungen erhöhen die Transparenz und verbessern die Nutzererfahrung.

Zum Beispiel sollte ein Client eine Benachrichtigung senden, sobald der initiale Handshake mit dem Server erfolgt ist.

Eine Benachrichtigung sieht als JSON-Nachricht so aus:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Benachrichtigungen gehören zu einem Thema in MCP, das als ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) bezeichnet wird.

Damit Logging funktioniert, muss der Server es als Feature/Fähigkeit aktivieren, etwa so:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Je nach verwendetem SDK ist Logging möglicherweise standardmäßig aktiviert oder muss explizit in der Serverkonfiguration eingeschaltet werden.

Es gibt verschiedene Typen von Benachrichtigungen:

| Level     | Beschreibung                | Beispiel-Anwendungsfall         |
|-----------|-----------------------------|---------------------------------|
| debug     | Ausführliche Debug-Informationen | Funktions-Ein- und Austritt     |
| info      | Allgemeine Informationsnachrichten | Fortschrittsupdates             |
| notice    | Normale, aber bedeutende Ereignisse | Konfigurationsänderungen       |
| warning   | Warnsignale                 | Nutzung veralteter Funktionen    |
| error     | Fehlerbedingungen           | Betriebsfehler                  |
| critical  | Kritische Bedingungen       | Komponentenausfälle             |
| alert     | Sofortiges Handeln erforderlich | Datenbeschädigung erkannt     |
| emergency | System ist unbenutzbar      | Totalausfall                   |

## Benachrichtigungen in MCP implementieren

Um Benachrichtigungen in MCP umzusetzen, müssen sowohl Server- als auch Client-Seite eingerichtet werden, um Echtzeit-Updates zu verarbeiten. So bietet Ihre Anwendung Nutzern bei lang laufenden Prozessen sofortiges Feedback.

### Serverseitig: Benachrichtigungen senden

Beginnen wir mit der Serverseite. In MCP definieren Sie Tools, die während der Anfragenverarbeitung Benachrichtigungen senden können. Der Server nutzt das Kontextobjekt (meist `ctx`), um Nachrichten an den Client zu senden.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Im obigen Beispiel sendet das Tool `process_files` drei Benachrichtigungen an den Client, während es jede Datei verarbeitet. Die Methode `ctx.info()` wird verwendet, um Informationsmeldungen zu senden.

Zudem muss Ihre Server-Konfiguration einen Streaming-Transport (wie `streamable-http`) nutzen, und Ihr Client muss einen Nachrichtenhandler implementieren, um Benachrichtigungen zu verarbeiten. Beispiel, wie der Server den `streamable-http` Transport verwendet:

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

In diesem .NET-Beispiel ist das Tool `ProcessFiles` mit dem `Tool`-Attribut dekoriert und sendet während der Verarbeitung jeder Datei drei Benachrichtigungen an den Client. Die Methode `ctx.Info()` wird für Informationsmeldungen genutzt.

Um Benachrichtigungen in Ihrem .NET MCP-Server zu aktivieren, verwenden Sie einen Streaming-Transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Clientseitig: Benachrichtigungen empfangen

Der Client muss einen Nachrichtenhandler implementieren, der Benachrichtigungen empfängt und anzeigt, sobald sie eintreffen.

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

Im obigen Code prüft die Funktion `message_handler`, ob eine eingehende Nachricht eine Benachrichtigung ist. Falls ja, wird diese ausgegeben, andernfalls wird sie als reguläre Servernachricht verarbeitet. Außerdem wird `ClientSession` mit `message_handler` initialisiert, um eingehende Benachrichtigungen zu handhaben.

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

Im .NET-Beispiel prüft die Funktion `MessageHandler`, ob eine eingehende Nachricht eine Benachrichtigung ist. Falls ja, wird diese ausgegeben, andernfalls als reguläre Servernachricht verarbeitet. `ClientSession` wird mit dem Nachrichtenhandler über `ClientSessionOptions` initialisiert.

Um Benachrichtigungen zu ermöglichen, stellen Sie sicher, dass Ihr Server einen Streaming-Transport (wie `streamable-http`) verwendet und Ihr Client einen Nachrichtenhandler implementiert.

## Fortschrittsbenachrichtigungen & Szenarien

Dieser Abschnitt erklärt den Begriff der Fortschrittsbenachrichtigungen in MCP, warum sie wichtig sind und wie sie mit Streamable HTTP implementiert werden können. Außerdem gibt es eine praktische Übung zum besseren Verständnis.

Fortschrittsbenachrichtigungen sind Echtzeitnachrichten, die vom Server während lang laufender Prozesse an den Client gesendet werden. Anstatt auf das Ende des gesamten Prozesses zu warten, hält der Server den Client über den aktuellen Status auf dem Laufenden. Das erhöht Transparenz, Benutzerfreundlichkeit und erleichtert Debugging.

**Beispiel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Warum Fortschrittsbenachrichtigungen verwenden?

Fortschrittsbenachrichtigungen sind aus mehreren Gründen wichtig:

- **Bessere Nutzererfahrung:** Nutzer sehen Updates während der Arbeit, nicht nur am Ende.
- **Echtzeit-Feedback:** Clients können Fortschrittsbalken oder Logs anzeigen, was die Anwendung reaktionsschneller wirken lässt.
- **Leichteres Debuggen und Monitoring:** Entwickler und Nutzer sehen, wo ein Prozess langsam ist oder hängenbleibt.

### So implementieren Sie Fortschrittsbenachrichtigungen

So setzen Sie Fortschrittsbenachrichtigungen in MCP um:

- **Auf dem Server:** Verwenden Sie `ctx.info()` oder `ctx.log()`, um Benachrichtigungen zu senden, während einzelne Items verarbeitet werden. Dies sendet eine Nachricht an den Client, bevor das Hauptergebnis fertig ist.
- **Auf dem Client:** Implementieren Sie einen Nachrichtenhandler, der Benachrichtigungen empfängt und anzeigt. Dieser Handler unterscheidet zwischen Benachrichtigungen und dem Endergebnis.

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

Bei der Implementierung von MCP-Servern mit HTTP-basierten Transporten ist Sicherheit von höchster Bedeutung und erfordert ein sorgfältiges Augenmerk auf verschiedene Angriffsvektoren und Schutzmechanismen.

### Überblick

Sicherheit ist kritisch, wenn MCP-Server über HTTP exponiert werden. Streamable HTTP bringt neue Angriffsflächen mit sich und erfordert sorgfältige Konfiguration.

### Wichtige Punkte
- **Origin-Header-Validierung**: Validieren Sie stets den `Origin`-Header, um DNS-Rebinding-Angriffe zu verhindern.
- **Bindung an localhost**: Binden Sie Server für die lokale Entwicklung an `localhost`, um zu vermeiden, dass sie im öffentlichen Internet zugänglich sind.
- **Authentifizierung**: Implementieren Sie für den Produktionseinsatz eine Authentifizierung (z. B. API-Schlüssel, OAuth).
- **CORS**: Konfigurieren Sie Cross-Origin Resource Sharing (CORS)-Richtlinien, um den Zugriff einzuschränken.
- **HTTPS**: Verwenden Sie in der Produktion HTTPS, um den Datenverkehr zu verschlüsseln.

### Beste Praktiken

- Vertrauen Sie eingehenden Anfragen niemals ohne Validierung.
- Protokollieren und überwachen Sie alle Zugriffe und Fehler.
- Aktualisieren Sie regelmäßig Abhängigkeiten, um Sicherheitslücken zu schließen.

### Herausforderungen

- Balance zwischen Sicherheit und Entwicklungsfreundlichkeit
- Gewährleistung der Kompatibilität mit verschiedenen Client-Umgebungen

## Upgrade von SSE zu Streamable HTTP

Für Anwendungen, die derzeit Server-Sent Events (SSE) verwenden, bietet der Umstieg auf Streamable HTTP erweiterte Möglichkeiten und bessere langfristige Nachhaltigkeit für Ihre MCP-Implementierungen.

### Warum upgraden?

Es gibt zwei überzeugende Gründe, von SSE zu Streamable HTTP zu wechseln:

- Streamable HTTP bietet bessere Skalierbarkeit, Kompatibilität und reichhaltigere Benachrichtigungsunterstützung als SSE.
- Es ist der empfohlene Transport für neue MCP-Anwendungen.

### Migrationsschritte

So migrieren Sie Ihre MCP-Anwendungen von SSE zu Streamable HTTP:

- **Aktualisieren Sie den Server-Code**, um `transport="streamable-http"` in `mcp.run()` zu verwenden.
- **Aktualisieren Sie den Client-Code**, indem Sie `streamablehttp_client` anstelle des SSE-Clients verwenden.
- **Implementieren Sie einen Nachrichten-Handler** im Client, um Benachrichtigungen zu verarbeiten.
- **Testen Sie die Kompatibilität** mit vorhandenen Tools und Workflows.

### Kompatibilität beibehalten

Es wird empfohlen, während des Migrationsprozesses die Kompatibilität zu bestehenden SSE-Clients sicherzustellen. Hier einige Strategien:

- Sie können sowohl SSE als auch Streamable HTTP unterstützen, indem Sie beide Transports auf verschiedenen Endpunkten ausführen.
- Migrieren Sie die Clients schrittweise zum neuen Transport.

### Herausforderungen

Berücksichtigen Sie bei der Migration folgende Herausforderungen:

- Sicherstellen, dass alle Clients aktualisiert werden
- Umgang mit Unterschieden bei der Benachrichtigungszustellung

## Sicherheitshinweise

Sicherheit sollte bei der Implementierung von Servern, insbesondere bei Verwendung von HTTP-basierten Transporten wie Streamable HTTP in MCP, oberste Priorität haben.

Bei der Implementierung von MCP-Servern mit HTTP-basierten Transporten ist Sicherheit ein zentrales Anliegen, das sorgfältige Beachtung verschiedener Angriffsvektoren und Schutzmechanismen erfordert.

### Überblick

Sicherheit ist entscheidend, wenn MCP-Server über HTTP exponiert werden. Streamable HTTP bringt neue Angriffsflächen mit sich und erfordert eine sorgfältige Konfiguration.

Wichtige Sicherheitshinweise:

- **Origin-Header-Validierung**: Validieren Sie stets den `Origin`-Header, um DNS-Rebinding-Angriffe zu verhindern.
- **Bindung an localhost**: Binden Sie Server für die lokale Entwicklung an `localhost`, um zu vermeiden, dass sie im öffentlichen Internet zugänglich sind.
- **Authentifizierung**: Implementieren Sie für den Produktionseinsatz eine Authentifizierung (z. B. API-Schlüssel, OAuth).
- **CORS**: Konfigurieren Sie Cross-Origin Resource Sharing (CORS)-Richtlinien, um den Zugriff einzuschränken.
- **HTTPS**: Verwenden Sie in der Produktion HTTPS, um den Datenverkehr zu verschlüsseln.

### Beste Praktiken

Zusätzlich hier einige bewährte Verfahren für die Sicherheit Ihres MCP-Streaming-Servers:

- Vertrauen Sie eingehenden Anfragen niemals ohne Validierung.
- Protokollieren und überwachen Sie alle Zugriffe und Fehler.
- Aktualisieren Sie regelmäßig Abhängigkeiten, um Sicherheitslücken zu schließen.

### Herausforderungen

Bei der Implementierung der Sicherheit in MCP-Streaming-Servern treten folgende Herausforderungen auf:

- Balance zwischen Sicherheit und Entwicklungsfreundlichkeit
- Gewährleistung der Kompatibilität mit verschiedenen Client-Umgebungen

### Aufgabe: Bauen Sie Ihre eigene Streaming-MCP-App

**Szenario:**  
Erstellen Sie einen MCP-Server und -Client, bei dem der Server eine Liste von Elementen (z. B. Dateien oder Dokumente) verarbeitet und für jedes verarbeitete Element eine Benachrichtigung sendet. Der Client soll jede Benachrichtigung beim Eintreffen anzeigen.

**Schritte:**

1. Implementieren Sie ein Server-Tool, das eine Liste verarbeitet und Benachrichtigungen für jedes Element sendet.
2. Implementieren Sie einen Client mit einem Nachrichten-Handler zur Echtzeitanzeige der Benachrichtigungen.
3. Testen Sie Ihre Implementierung, indem Sie sowohl Server als auch Client ausführen und die Benachrichtigungen beobachten.

[Solution](./solution/README.md)

## Weiterführende Literatur & Was als Nächstes?

Um Ihre Reise mit MCP-Streaming fortzusetzen und Ihr Wissen zu erweitern, bietet dieser Abschnitt zusätzliche Ressourcen und empfohlene nächste Schritte zum Aufbau anspruchsvollerer Anwendungen.

### Weiterführende Literatur

- [Microsoft: Einführung in HTTP-Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Was als Nächstes?

- Probieren Sie aus, komplexere MCP-Tools zu entwickeln, die Streaming für Echtzeitanalysen, Chat oder kollaboratives Bearbeiten verwenden.
- Erkunden Sie die Integration von MCP-Streaming mit Frontend-Frameworks (React, Vue usw.) für Live-UI-Updates.
- Nächstes Thema: [Nutzung des AI Toolkits für VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->