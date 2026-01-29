# HTTPS-Streaming mit Model Context Protocol (MCP)

Dieses Kapitel bietet eine umfassende Anleitung zur Implementierung von sicherem, skalierbarem und Echtzeit-Streaming mit dem Model Context Protocol (MCP) unter Verwendung von HTTPS. Es behandelt die Motivation für Streaming, die verfügbaren Transportmechanismen, die Implementierung von streambarem HTTP in MCP, bewährte Sicherheitspraktiken, die Migration von SSE und praktische Hinweise zum Aufbau eigener MCP-Streaming-Anwendungen.

## Transportmechanismen und Streaming in MCP

Dieser Abschnitt untersucht die verschiedenen Transportmechanismen, die in MCP verfügbar sind, und ihre Rolle bei der Aktivierung von Streaming-Funktionen für die Echtzeitkommunikation zwischen Clients und Servern.

### Was ist ein Transportmechanismus?

Ein Transportmechanismus definiert, wie Daten zwischen Client und Server ausgetauscht werden. MCP unterstützt mehrere Transporttypen, um unterschiedlichen Umgebungen und Anforderungen gerecht zu werden:

- **stdio**: Standard-Ein-/Ausgabe, geeignet für lokale und CLI-basierte Tools. Einfach, aber nicht geeignet für Web oder Cloud.
- **SSE (Server-Sent Events)**: Ermöglicht es Servern, Echtzeit-Updates über HTTP an Clients zu senden. Gut für Web-Oberflächen, aber begrenzt in Skalierbarkeit und Flexibilität.
- **Streambares HTTP**: Moderner HTTP-basierter Streaming-Transport, der Benachrichtigungen und bessere Skalierbarkeit unterstützt. Empfohlen für die meisten Produktions- und Cloud-Szenarien.

### Vergleichstabelle

Sehen Sie sich die folgende Vergleichstabelle an, um die Unterschiede zwischen diesen Transportmechanismen zu verstehen:

| Transport         | Echtzeit-Updates | Streaming | Skalierbarkeit | Anwendungsfall           |
|-------------------|------------------|-----------|----------------|--------------------------|
| stdio             | Nein             | Nein      | Niedrig        | Lokale CLI-Tools         |
| SSE               | Ja               | Ja        | Mittel         | Web, Echtzeit-Updates    |
| Streambares HTTP  | Ja               | Ja        | Hoch           | Cloud, Multi-Client      |

> **Tipp:** Die Wahl des richtigen Transports beeinflusst Leistung, Skalierbarkeit und Benutzererfahrung. **Streambares HTTP** wird für moderne, skalierbare und cloudfähige Anwendungen empfohlen.

Beachten Sie die Transportmechanismen stdio und SSE, die in den vorherigen Kapiteln behandelt wurden, und wie streambares HTTP der Transport ist, der in diesem Kapitel behandelt wird.

## Streaming: Konzepte und Motivation

Das Verständnis der grundlegenden Konzepte und Motivationen hinter Streaming ist entscheidend für die Implementierung effektiver Echtzeit-Kommunikationssysteme.

**Streaming** ist eine Technik in der Netzwerkprogrammierung, die es ermöglicht, Daten in kleinen, handhabbaren Teilen oder als Ereignisfolge zu senden und zu empfangen, anstatt auf eine vollständige Antwort zu warten. Dies ist besonders nützlich für:

- Große Dateien oder Datensätze.
- Echtzeit-Updates (z. B. Chat, Fortschrittsbalken).
- Langwierige Berechnungen, bei denen der Benutzer auf dem Laufenden gehalten werden soll.

Das sollten Sie über Streaming auf hoher Ebene wissen:

- Daten werden schrittweise geliefert, nicht auf einmal.
- Der Client kann Daten verarbeiten, sobald sie eintreffen.
- Verringert die wahrgenommene Latenz und verbessert die Benutzererfahrung.

### Warum Streaming verwenden?

Die Gründe für die Verwendung von Streaming sind folgende:

- Benutzer erhalten sofortiges Feedback, nicht erst am Ende.
- Ermöglicht Echtzeitanwendungen und reaktionsfähige Benutzeroberflächen.
- Effizientere Nutzung von Netzwerk- und Computerressourcen.

### Einfaches Beispiel: HTTP-Streaming-Server & -Client

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

Dieses Beispiel zeigt, wie ein Server eine Reihe von Nachrichten an den Client sendet, sobald sie verfügbar sind, anstatt darauf zu warten, dass alle Nachrichten bereit sind.

**Wie es funktioniert:**

- Der Server gibt jede Nachricht aus, sobald sie bereit ist.
- Der Client empfängt und druckt jeden Teil, sobald er eintrifft.

**Anforderungen:**

- Der Server muss eine Streaming-Antwort verwenden (z. B. `StreamingResponse` in FastAPI).
- Der Client muss die Antwort als Stream verarbeiten (`stream=True` in requests).
- Content-Type ist normalerweise `text/event-stream` oder `application/octet-stream`.

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

**Hinweise zur Java-Implementierung:**

- Verwendet Spring Boots reaktiven Stack mit `Flux` für Streaming.
- `ServerSentEvent` bietet strukturiertes Ereignis-Streaming mit Ereignistypen.
- `WebClient` mit `bodyToFlux()` ermöglicht reaktiven Streaming-Konsum.
- `delayElements()` simuliert die Verarbeitungszeit zwischen Ereignissen.
- Ereignisse können Typen (`info`, `result`) haben, um die Client-Verarbeitung zu verbessern.

### Vergleich: Klassisches Streaming vs MCP-Streaming

Die Unterschiede zwischen klassischem Streaming und MCP-Streaming können wie folgt dargestellt werden:

| Merkmal               | Klassisches HTTP-Streaming      | MCP-Streaming (Benachrichtigungen) |
|-----------------------|---------------------------------|------------------------------------|
| Hauptantwort          | In Teilen                      | Einzeln, am Ende                  |
| Fortschritts-Updates  | Als Datenstücke gesendet       | Als Benachrichtigungen gesendet   |
| Client-Anforderungen  | Muss Stream verarbeiten        | Muss Nachrichtenhandler implementieren |
| Anwendungsfall        | Große Dateien, AI-Token-Streams | Fortschritt, Logs, Echtzeit-Feedback |

### Beobachtete Hauptunterschiede

Zusätzlich gibt es einige wichtige Unterschiede:

- **Kommunikationsmuster:**
  - Klassisches HTTP-Streaming: Verwendet einfache chunked transfer encoding, um Daten in Teilen zu senden.
  - MCP-Streaming: Verwendet ein strukturiertes Benachrichtigungssystem mit JSON-RPC-Protokoll.

- **Nachrichtenformat:**
  - Klassisches HTTP: Plaintext-Stücke mit Zeilenumbrüchen.
  - MCP: Strukturierte LoggingMessageNotification-Objekte mit Metadaten.

- **Client-Implementierung:**
  - Klassisches HTTP: Einfacher Client, der Streaming-Antworten verarbeitet.
  - MCP: Anspruchsvollerer Client mit einem Nachrichtenhandler, der verschiedene Nachrichtentypen verarbeitet.

- **Fortschritts-Updates:**
  - Klassisches HTTP: Der Fortschritt ist Teil des Hauptantwortstreams.
  - MCP: Fortschritt wird über separate Benachrichtigungsnachrichten gesendet, während die Hauptantwort am Ende kommt.

### Empfehlungen

Es gibt einige Empfehlungen, wenn es darum geht, zwischen der Implementierung von klassischem Streaming (wie dem oben gezeigten Endpoint `/stream`) und Streaming über MCP zu wählen.

- **Für einfache Streaming-Anforderungen:** Klassisches HTTP-Streaming ist einfacher zu implementieren und ausreichend für grundlegende Streaming-Anforderungen.

- **Für komplexe, interaktive Anwendungen:** MCP-Streaming bietet einen strukturierteren Ansatz mit reichhaltigeren Metadaten und einer Trennung zwischen Benachrichtigungen und Endergebnissen.

- **Für KI-Anwendungen:** Das Benachrichtigungssystem von MCP ist besonders nützlich für langwierige KI-Aufgaben, bei denen Benutzer über Fortschritte informiert werden sollen.

## Streaming in MCP

Okay, Sie haben bisher einige Empfehlungen und Vergleiche zu den Unterschieden zwischen klassischem Streaming und Streaming in MCP gesehen. Lassen Sie uns genau darauf eingehen, wie Sie Streaming in MCP nutzen können.

Das Verständnis, wie Streaming innerhalb des MCP-Frameworks funktioniert, ist entscheidend für den Aufbau reaktionsfähiger Anwendungen, die Benutzern während langwieriger Operationen Echtzeit-Feedback bieten.

In MCP geht es beim Streaming nicht darum, die Hauptantwort in Teilen zu senden, sondern darum, **Benachrichtigungen** an den Client zu senden, während ein Tool eine Anfrage verarbeitet. Diese Benachrichtigungen können Fortschritts-Updates, Logs oder andere Ereignisse enthalten.

### Wie es funktioniert

Das Hauptergebnis wird weiterhin als einzelne Antwort gesendet. Benachrichtigungen können jedoch während der Verarbeitung als separate Nachrichten gesendet werden und den Client in Echtzeit aktualisieren. Der Client muss in der Lage sein, diese Benachrichtigungen zu verarbeiten und anzuzeigen.

## Was ist eine Benachrichtigung?

Wir haben "Benachrichtigung" gesagt – was bedeutet das im Kontext von MCP?

Eine Benachrichtigung ist eine Nachricht, die vom Server an den Client gesendet wird, um über Fortschritt, Status oder andere Ereignisse während einer langwierigen Operation zu informieren. Benachrichtigungen verbessern die Transparenz und Benutzererfahrung.

Zum Beispiel sollte ein Client eine Benachrichtigung senden, sobald der erste Handshake mit dem Server erfolgt ist.

Eine Benachrichtigung sieht als JSON-Nachricht wie folgt aus:

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

Um Logging zu aktivieren, muss der Server es als Funktion/Fähigkeit wie folgt aktivieren:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Abhängig vom verwendeten SDK kann Logging standardmäßig aktiviert sein, oder Sie müssen es explizit in Ihrer Serverkonfiguration aktivieren.

Es gibt verschiedene Arten von Benachrichtigungen:

| Ebene      | Beschreibung                  | Beispielanwendungsfall          |
|------------|-------------------------------|----------------------------------|
| debug      | Detaillierte Debug-Informationen | Funktions-Ein-/Austrittspunkte |
| info       | Allgemeine Informationsmeldungen | Fortschritts-Updates           |
| notice     | Normale, aber bedeutende Ereignisse | Konfigurationsänderungen       |
| warning    | Warnbedingungen               | Verwendung veralteter Funktionen |
| error      | Fehlerbedingungen             | Fehlgeschlagene Operationen     |
| critical   | Kritische Bedingungen         | Ausfälle von Systemkomponenten  |
| alert      | Sofortiges Handeln erforderlich | Datenkorruption erkannt        |
| emergency  | System ist unbrauchbar        | Vollständiger Systemausfall     |

## Implementierung von Benachrichtigungen in MCP

Um Benachrichtigungen in MCP zu implementieren, müssen Sie sowohl die Server- als auch die Client-Seite einrichten, um Echtzeit-Updates zu verarbeiten. Dadurch kann Ihre Anwendung Benutzern während langwieriger Operationen sofortiges Feedback geben.

### Server-seitig: Senden von Benachrichtigungen

Beginnen wir mit der Server-Seite. In MCP definieren Sie Tools, die während der Verarbeitung von Anfragen Benachrichtigungen senden können. Der Server verwendet das Kontextobjekt (normalerweise `ctx`), um Nachrichten an den Client zu senden.

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

Zusätzlich, um Benachrichtigungen zu aktivieren, stellen Sie sicher, dass Ihr Server einen Streaming-Transport verwendet (wie `streamable-http`) und Ihr Client einen Nachrichtenhandler implementiert, um Benachrichtigungen zu verarbeiten. So richten Sie den Server ein, um den `streamable-http`-Transport zu verwenden:

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

In diesem .NET-Beispiel ist das Tool `ProcessFiles` mit dem `Tool`-Attribut dekoriert und sendet drei Benachrichtigungen an den Client, während es jede Datei verarbeitet. Die Methode `ctx.Info()` wird verwendet, um Informationsmeldungen zu senden.

Um Benachrichtigungen in Ihrem .NET-MCP-Server zu aktivieren, stellen Sie sicher, dass Sie einen Streaming-Transport verwenden:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-seitig: Empfangen von Benachrichtigungen

Der Client muss einen Nachrichtenhandler implementieren, um Benachrichtigungen zu verarbeiten und anzuzeigen, sobald sie eintreffen.

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

Im obigen Code überprüft die Funktion `message_handler`, ob die eingehende Nachricht eine Benachrichtigung ist. Wenn ja, wird die Benachrichtigung gedruckt; andernfalls wird sie als reguläre Servernachricht verarbeitet. Beachten Sie auch, wie die `ClientSession` mit dem `message_handler` initialisiert wird, um eingehende Benachrichtigungen zu verarbeiten.

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

In diesem .NET-Beispiel überprüft die Funktion `MessageHandler`, ob die eingehende Nachricht eine Benachrichtigung ist. Wenn ja, wird die Benachrichtigung gedruckt; andernfalls wird sie als reguläre Servernachricht verarbeitet. Die `ClientSession` wird mit dem Nachrichtenhandler über die `ClientSessionOptions` initialisiert.

Um Benachrichtigungen zu aktivieren, stellen Sie sicher, dass Ihr Server einen Streaming-Transport verwendet (wie `streamable-http`) und Ihr Client einen Nachrichtenhandler implementiert, um Benachrichtigungen zu verarbeiten.

## Fortschrittsbenachrichtigungen & Szenarien

Dieser Abschnitt erklärt das Konzept der Fortschrittsbenachrichtigungen in MCP, warum sie wichtig sind und wie man sie mit Streamable HTTP implementiert. Sie finden auch eine praktische Aufgabe, um Ihr Verständnis zu vertiefen.

Fortschrittsbenachrichtigungen sind Echtzeit-Nachrichten, die vom Server während langwieriger Operationen an den Client gesendet werden. Anstatt darauf zu warten, dass der gesamte Prozess abgeschlossen ist, hält der Server den Client über den aktuellen Status auf dem Laufenden. Dies verbessert die Transparenz, Benutzererfahrung und erleichtert das Debugging.

**Beispiel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Warum Fortschrittsbenachrichtigungen verwenden?

Fortschrittsbenachrichtigungen sind aus mehreren Gründen wichtig:

- **Bessere Benutzererfahrung:** Benutzer sehen Updates, während die Arbeit fortschreitet, nicht erst am Ende.
- **Echtzeit-Feedback:** Clients können Fortschrittsbalken oder Logs anzeigen, wodurch die App reaktionsschnell wirkt.
- **Einfacheres Debugging und Monitoring:** Entwickler und Benutzer können sehen, wo ein Prozess möglicherweise langsam oder blockiert ist.

### Wie man Fortschrittsbenachrichtigungen implementiert

So können Sie Fortschrittsbenachrichtigungen in MCP implementieren:

- **Auf dem Server:** Verwenden Sie `ctx.info()` oder `ctx.log()`, um Benachrichtigungen zu senden, während jedes Element verarbeitet wird. Dies sendet eine Nachricht an den Client, bevor das Hauptergebnis bereit ist.
- **Auf dem Client:** Implementieren Sie einen Nachrichtenhandler, der Benachrichtigungen abhört und anzeigt, sobald sie eintreffen. Dieser Handler unterscheidet zwischen Benachrichtigungen und dem Endergebnis.

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

Bei der Implementierung von MCP-Servern mit HTTP-basierten Transporten ist Sicherheit ein entscheidender Aspekt, der sorgfältige Aufmerksamkeit gegenüber mehreren Angriffsvektoren und Schutzmechanismen erfordert.

### Überblick

Sicherheit ist entscheidend, wenn MCP-Server über HTTP exponiert werden. Streamable HTTP führt neue Angriffsflächen ein und erfordert eine sorgfältige Konfiguration.

### Wichtige Punkte

- **Origin-Header-Validierung**: Validieren Sie immer den `Origin`-Header, um DNS-Rebinding-Angriffe zu verhindern.
- **Localhost-Bindung**: Für lokale Entwicklung Server an `localhost` binden, um eine öffentliche Internetexposition zu vermeiden.
- **Authentifizierung**: Implementieren Sie Authentifizierung (z. B. API-Schlüssel, OAuth) für Produktionsbereitstellungen.
- **CORS**: Konfigurieren Sie Cross-Origin Resource Sharing (CORS)-Richtlinien, um den Zugriff einzuschränken.
- **HTTPS**: Verwenden Sie HTTPS in der Produktion, um den Datenverkehr zu verschlüsseln.

### Best Practices

- Vertrauen Sie eingehenden Anfragen niemals ohne Validierung.
- Protokollieren und überwachen Sie alle Zugriffe und Fehler.
- Aktualisieren Sie regelmäßig Abhängigkeiten, um Sicherheitslücken zu schließen.

### Herausforderungen

- Sicherheit mit einfacher Entwicklung in Einklang bringen.
- Kompatibilität mit verschiedenen Client-Umgebungen sicherstellen.

## Upgrade von SSE zu Streamable HTTP

Für Anwendungen, die derzeit Server-Sent Events (SSE) verwenden, bietet die Migration zu Streamable HTTP erweiterte Funktionen und eine bessere langfristige Nachhaltigkeit für Ihre MCP-Implementierungen.

### Warum upgraden?
Es gibt zwei überzeugende Gründe, von SSE zu Streamable HTTP zu wechseln:

- Streamable HTTP bietet bessere Skalierbarkeit, Kompatibilität und umfangreichere Benachrichtigungsunterstützung als SSE.
- Es ist der empfohlene Transport für neue MCP-Anwendungen.

### Migrationsschritte

So können Sie in Ihren MCP-Anwendungen von SSE zu Streamable HTTP migrieren:

- **Aktualisieren Sie den Servercode**, um `transport="streamable-http"` in `mcp.run()` zu verwenden.
- **Aktualisieren Sie den Clientcode**, um `streamablehttp_client` anstelle des SSE-Clients zu verwenden.
- **Implementieren Sie einen Nachrichten-Handler** im Client, um Benachrichtigungen zu verarbeiten.
- **Testen Sie die Kompatibilität** mit bestehenden Tools und Workflows.

### Kompatibilität beibehalten

Es wird empfohlen, während des Migrationsprozesses die Kompatibilität mit bestehenden SSE-Clients aufrechtzuerhalten. Hier sind einige Strategien:

- Sie können sowohl SSE als auch Streamable HTTP unterstützen, indem Sie beide Transporte auf unterschiedlichen Endpunkten betreiben.
- Migrieren Sie die Clients schrittweise auf den neuen Transport.

### Herausforderungen

Stellen Sie sicher, dass Sie die folgenden Herausforderungen während der Migration angehen:

- Sicherstellen, dass alle Clients aktualisiert werden
- Umgang mit Unterschieden in der Benachrichtigungsübermittlung

## Sicherheitsüberlegungen

Sicherheit sollte oberste Priorität haben, wenn ein Server implementiert wird, insbesondere bei der Verwendung von HTTP-basierten Transporten wie Streamable HTTP in MCP.

Bei der Implementierung von MCP-Servern mit HTTP-basierten Transporten ist Sicherheit ein zentrales Anliegen, das sorgfältige Aufmerksamkeit auf verschiedene Angriffsvektoren und Schutzmechanismen erfordert.

### Überblick

Sicherheit ist entscheidend, wenn MCP-Server über HTTP bereitgestellt werden. Streamable HTTP eröffnet neue Angriffsflächen und erfordert eine sorgfältige Konfiguration.

Hier sind einige wichtige Sicherheitsüberlegungen:

- **Validierung des Origin-Headers**: Validieren Sie immer den `Origin`-Header, um DNS-Rebinding-Angriffe zu verhindern.
- **Binding an Localhost**: Für die lokale Entwicklung sollten Server an `localhost` gebunden werden, um eine öffentliche Exposition zu vermeiden.
- **Authentifizierung**: Implementieren Sie eine Authentifizierung (z. B. API-Schlüssel, OAuth) für Produktionsbereitstellungen.
- **CORS**: Konfigurieren Sie Cross-Origin Resource Sharing (CORS)-Richtlinien, um den Zugriff einzuschränken.
- **HTTPS**: Verwenden Sie in der Produktion HTTPS, um den Datenverkehr zu verschlüsseln.

### Best Practices

Zusätzlich sollten Sie die folgenden Best Practices befolgen, wenn Sie Sicherheit in Ihrem MCP-Streaming-Server implementieren:

- Vertrauen Sie eingehenden Anfragen niemals ohne Validierung.
- Protokollieren und überwachen Sie alle Zugriffe und Fehler.
- Aktualisieren Sie regelmäßig Abhängigkeiten, um Sicherheitslücken zu schließen.

### Herausforderungen

Sie werden einige Herausforderungen bei der Implementierung von Sicherheit in MCP-Streaming-Servern bewältigen müssen:

- Die Balance zwischen Sicherheit und einfacher Entwicklung
- Sicherstellen der Kompatibilität mit verschiedenen Client-Umgebungen

### Aufgabe: Erstellen Sie Ihre eigene Streaming-MCP-App

**Szenario:**
Erstellen Sie einen MCP-Server und -Client, bei dem der Server eine Liste von Elementen (z. B. Dateien oder Dokumente) verarbeitet und für jedes verarbeitete Element eine Benachrichtigung sendet. Der Client sollte jede Benachrichtigung in Echtzeit anzeigen.

**Schritte:**

1. Implementieren Sie ein Server-Tool, das eine Liste verarbeitet und Benachrichtigungen für jedes Element sendet.
2. Implementieren Sie einen Client mit einem Nachrichten-Handler, um Benachrichtigungen in Echtzeit anzuzeigen.
3. Testen Sie Ihre Implementierung, indem Sie sowohl den Server als auch den Client ausführen und die Benachrichtigungen beobachten.

[Solution](./solution/README.md)

## Weiterführende Literatur & Nächste Schritte

Um Ihre Reise mit MCP-Streaming fortzusetzen und Ihr Wissen zu erweitern, bietet dieser Abschnitt zusätzliche Ressourcen und Vorschläge für die Entwicklung fortgeschrittener Anwendungen.

### Weiterführende Literatur

- [Microsoft: Einführung in HTTP-Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Nächste Schritte

- Versuchen Sie, fortgeschrittenere MCP-Tools zu entwickeln, die Streaming für Echtzeitanalysen, Chats oder kollaboratives Bearbeiten nutzen.
- Erkunden Sie die Integration von MCP-Streaming mit Frontend-Frameworks (React, Vue usw.) für Live-UI-Updates.
- Weiter: [Nutzung des AI-Toolkits für VSCode](../07-aitk/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.