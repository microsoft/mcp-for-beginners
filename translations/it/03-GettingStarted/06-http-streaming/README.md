# Streaming HTTPS con il Model Context Protocol (MCP)

Questo capitolo fornisce una guida completa all'implementazione dello streaming sicuro, scalabile e in tempo reale con il Model Context Protocol (MCP) utilizzando HTTPS. Copre la motivazione per lo streaming, i meccanismi di trasporto disponibili, come implementare HTTP streamable in MCP, le migliori pratiche di sicurezza, la migrazione da SSE e indicazioni pratiche per costruire le proprie applicazioni MCP streaming.

> **Uno sguardo al futuro:** questa lezione descrive lo Streamable HTTP secondo la **Specificazione MCP 2025-11-25**, dove viene stabilita una sessione durante `initialize` e associata con un header `Mcp-Session-Id`. Il release candidate `2026-07-28` rimuove completamente la stretta di mano e l'ID di sessione, rendendo ogni richiesta autosufficiente e instradabile a qualsiasi istanza server senza sessioni sticky. Consulta [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) per maggiori dettagli.

## Meccanismi di Trasporto e Streaming in MCP

Questa sezione esplora i diversi meccanismi di trasporto disponibili in MCP e il loro ruolo nell'abilitare le funzionalità di streaming per la comunicazione in tempo reale tra client e server.

### Cos'è un Meccanismo di Trasporto?

Un meccanismo di trasporto definisce come i dati vengono scambiati tra il client e il server. MCP supporta diversi tipi di trasporto per adattarsi a differenti ambienti e requisiti:

- **stdio**: input/output standard, adatto per strumenti locali e basati su CLI. Semplice ma non adatto per web o cloud.
- **SSE (Server-Sent Events)**: consente ai server di inviare aggiornamenti in tempo reale ai client tramite HTTP. Buono per interfacce web, ma limitato in scalabilità e flessibilità. A partire dalla Specificazione MCP 2025-06-18, il trasporto SSE standalone è stato deprecato e sostituito dal trasporto "Streamable HTTP".
- **Streamable HTTP**: trasporto streaming moderno basato su HTTP, supporta notifiche e migliore scalabilità. Consigliato per la maggior parte degli scenari di produzione e cloud.

### Tabella di confronto

Dai un'occhiata alla tabella di confronto sottostante per comprendere le differenze tra questi meccanismi di trasporto:

| Trasporto       | Aggiornamenti in tempo reale | Streaming | Scalabilità | Caso d'uso               |
|-----------------|------------------------------|-----------|-------------|--------------------------|
| stdio           | No                           | No        | Bassa       | Strumenti CLI locali      |
| SSE             | Sì                           | Sì        | Media       | Web, aggiornamenti realtime |
| Streamable HTTP | Sì                           | Sì        | Alta        | Cloud, multi-client       |

> **Suggerimento:** Scegliere il trasporto giusto influisce su prestazioni, scalabilità ed esperienza utente. **Streamable HTTP** è raccomandato per applicazioni moderne, scalabili e pronte per il cloud.

Nota i trasporti stdio e SSE presentati nei capitoli precedenti e come lo Streamable HTTP sia il trasporto trattato in questo capitolo.

## Streaming: Concetti e Motivazione

Comprendere i concetti fondamentali e le motivazioni dietro lo streaming è essenziale per implementare sistemi di comunicazione in tempo reale efficaci.

**Streaming** è una tecnica nella programmazione di rete che permette di inviare e ricevere dati in piccoli blocchi gestibili o come una sequenza di eventi, invece di aspettare che la risposta completa sia pronta. Questo è particolarmente utile per:

- Grandi file o dataset.
- Aggiornamenti in tempo reale (es. chat, barre di progresso).
- Computazioni di lunga durata dove si vuole tenere informato l'utente.

Ecco cosa devi sapere sullo streaming a livello alto:

- I dati vengono consegnati progressivamente, non tutti insieme.
- Il client può elaborare i dati man mano che arrivano.
- Riduce la latenza percepita e migliora l'esperienza utente.

### Perché usare lo streaming?

Le ragioni per usare lo streaming sono le seguenti:

- Gli utenti ricevono feedback immediati, non solo alla fine.
- Abilita applicazioni in tempo reale e interfacce reattive.
- Uso più efficiente delle risorse di rete e calcolo.

### Esempio semplice: Server & Client HTTP Streaming

Ecco un semplice esempio di come lo streaming può essere implementato:

#### Python

**Server (Python, usando FastAPI e StreamingResponse):**

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

**Client (Python, usando requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Questo esempio mostra un server che invia una serie di messaggi al client man mano che diventano disponibili, invece di aspettare che tutti i messaggi siano pronti.

**Come funziona:**

- Il server emette ogni messaggio non appena è pronto.
- Il client riceve e stampa ogni blocco appena arriva.

**Requisiti:**

- Il server deve usare una risposta di streaming (p.es. `StreamingResponse` in FastAPI).
- Il client deve processare la risposta come uno stream (`stream=True` in requests).
- Content-Type è solitamente `text/event-stream` o `application/octet-stream`.

#### Java

**Server (Java, usando Spring Boot e Server-Sent Events):**

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

**Client (Java, usando Spring WebFlux WebClient):**

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

**Note sull'implementazione in Java:**

- Usa lo stack reattivo di Spring Boot con `Flux` per lo streaming
- `ServerSentEvent` fornisce streaming di eventi strutturati con tipi di evento
- `WebClient` con `bodyToFlux()` consente il consumo reattivo dello streaming
- `delayElements()` simula il tempo di elaborazione tra eventi
- Gli eventi possono avere tipi (`info`, `result`) per una migliore gestione lato client

### Confronto: Streaming Classico vs Streaming MCP

Le differenze tra come lo streaming funziona in modo "classico" rispetto a come funziona in MCP possono essere rappresentate così:

| Caratteristica           | Streaming HTTP Classico         | Streaming MCP (Notifiche)        |
|-------------------------|--------------------------------|---------------------------------|
| Risposta principale      | Chunked                        | Singola, alla fine              |
| Aggiornamenti di progresso | Inviati come pacchetti di dati | Inviati come notifiche           |
| Requisiti client          | Deve processare lo streaming  | Deve implementare un gestore di messaggi |
| Caso d'uso               | File grandi, flussi di token AI | Progresso, log, feedback realtime |

### Differenze chiave osservate

Inoltre, ci sono alcune differenze chiave:

- **Pattern di Comunicazione:**
  - Streaming HTTP classico: usa encoding chunked semplice per inviare dati a blocchi
  - Streaming MCP: usa un sistema di notifiche strutturato con protocollo JSON-RPC

- **Formato del Messaggio:**
  - HTTP classico: blocchi di testo semplice con nuove linee
  - MCP: Oggetti LoggingMessageNotification strutturati con metadati

- **Implementazione Client:**
  - HTTP classico: client semplice che processa risposte streaming
  - MCP: client più sofisticato con un message handler per gestire diversi tipi di messaggi

- **Aggiornamenti di Progresso:**
  - HTTP classico: il progresso è parte del flusso di risposta principale
  - MCP: il progresso viene inviato tramite messaggi di notifica separati mentre la risposta principale arriva alla fine

### Raccomandazioni

Ci sono alcune cose che raccomandiamo quando si tratta di scegliere tra implementare lo streaming classico (con un endpoint come `/stream`) oppure scegliere lo streaming via MCP.

- **Per esigenze di streaming semplici:** lo streaming classico HTTP è più semplice da implementare e sufficiente per streaming di base.

- **Per applicazioni complesse e interattive:** lo streaming MCP offre un approccio più strutturato con metadati più ricchi e separazione tra notifiche e risultati finali.

- **Per applicazioni AI:** il sistema di notifiche MCP è particolarmente utile per task AI di lunga durata dove si vuole tenere gli utenti informati sul progresso.

## Streaming in MCP

Ok, hai visto finora alcune raccomandazioni e confronti sulla differenza tra streaming classico e streaming in MCP. Approfondiamo esattamente come puoi sfruttare lo streaming in MCP.

Comprendere come funziona lo streaming all'interno del framework MCP è essenziale per costruire applicazioni reattive che forniscono feedback in tempo reale agli utenti durante operazioni di lunga durata.

In MCP, lo streaming non riguarda l'invio della risposta principale a pezzi, ma l'invio di **notifiche** al client mentre un tool elabora una richiesta. Queste notifiche possono includere aggiornamenti di progresso, log o altri eventi.

### Come funziona

Il risultato principale viene comunque inviato come risposta singola. Tuttavia, le notifiche possono essere inviate come messaggi separati durante l'elaborazione e quindi aggiornare il client in tempo reale. Il client deve essere in grado di gestire e mostrare queste notifiche.

## Cos'è una Notifica?

Abbiamo detto "Notifica", cosa significa nel contesto MCP?

Una notifica è un messaggio inviato dal server al client per informare sul progresso, stato o altri eventi durante un'operazione di lunga durata. Le notifiche migliorano la trasparenza e l'esperienza utente.

Per esempio, un client dovrebbe inviare una notifica una volta completata la stretta di mano iniziale con il server.

Una notifica appare così come messaggio JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Le notifiche appartengono a un topic in MCP denominato ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Avviso di deprecazione:** il release candidate della specifica MCP `2026-07-28` segna il primitivo Logging come deprecato in favore di `stderr` per i trasporti stdio e OpenTelemetry per l'osservabilità strutturata. Il logging continua a funzionare nella versione `2025-11-25` e per almeno un anno dopo qualsiasi deprecazione formale. Vedi [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Per far funzionare il logging, il server deve abilitarlo come funzionalità/capacità così:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> A seconda dell'SDK usato, il logging potrebbe essere abilitato di default o potresti doverlo abilitare esplicitamente nella configurazione del server.

Esistono diversi tipi di notifiche:

| Livello     | Descrizione                    | Esempio d'uso                 |
|-------------|------------------------------|------------------------------|
| debug       | Informazioni dettagliate di debug | Punti di entrata/uscita delle funzioni |
| info        | Messaggi informativi generali    | Aggiornamenti di progresso   |
| notice      | Eventi normali ma significativi  | Cambiamenti di configurazione |
| warning     | Condizioni di avviso              | Uso di funzionalità deprecate |
| error       | Condizioni di errore              | Fallimenti di operazioni     |
| critical    | Condizioni critiche               | Guasti a componenti di sistema |
| alert       | Azione da intraprendere immediatamente | Corruzione dati rilevata    |
| emergency   | Sistema inutilizzabile            | Guasto completo del sistema  |

## Implementare le Notifiche in MCP

Per implementare le notifiche in MCP, devi configurare sia il lato server che il lato client per gestire aggiornamenti in tempo reale. Questo permette alla tua applicazione di fornire feedback immediato agli utenti durante operazioni di lunga durata.

### Lato server: Invio delle Notifiche

Iniziamo dal lato server. In MCP, definisci strumenti che possono inviare notifiche mentre processano richieste. Il server usa l'oggetto di contesto (di solito `ctx`) per inviare messaggi al client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Nell'esempio precedente, lo strumento `process_files` invia tre notifiche al client mentre elabora ciascun file. Il metodo `ctx.info()` è usato per inviare messaggi informativi.

Inoltre, per abilitare le notifiche, assicurati che il server usi un trasporto streaming (come `streamable-http`) e che il client implementi un message handler per processare le notifiche. Ecco come configurare il server per usare il trasporto `streamable-http`:

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

In questo esempio .NET, lo strumento `ProcessFiles` è decorato con l'attributo `Tool` e invia tre notifiche al client mentre elabora ciascun file. Il metodo `ctx.Info()` è usato per inviare messaggi informativi.

Per abilitare le notifiche nel tuo server MCP in .NET, assicurati di usare un trasporto streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lato client: Ricezione delle Notifiche

Il client deve implementare un message handler per processare e mostrare le notifiche appena arrivano.

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

Nel codice precedente, la funzione `message_handler` verifica se il messaggio in arrivo è una notifica. In tal caso, stampa la notifica; altrimenti la elabora come messaggio server regolare. Nota anche come `ClientSession` sia inizializzato con `message_handler` per gestire le notifiche in arrivo.

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

In questo esempio .NET, la funzione `MessageHandler` verifica se il messaggio in arrivo è una notifica. Se sì, stampa la notifica; altrimenti la elabora come un normale messaggio server. Il `ClientSession` è inizializzato con il message handler tramite `ClientSessionOptions`.

Per abilitare le notifiche, assicurati che il tuo server utilizzi un trasporto streaming (come `streamable-http`) e che il client implementi un message handler per processare le notifiche.

## Notifiche di Progresso & Scenari

Questa sezione spiega il concetto di notifiche di progresso in MCP, perché sono importanti e come implementarle usando Streamable HTTP. Troverai anche un esercizio pratico per rafforzare la tua comprensione.

Le notifiche di progresso sono messaggi in tempo reale inviati dal server al client durante operazioni di lunga durata. Invece di aspettare la fine dell'intero processo, il server tiene aggiornato il client sullo stato attuale. Questo migliora trasparenza, esperienza utente e facilita il debugging.

**Esempio:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Perché usare le Notifiche di Progresso?

Le notifiche di progresso sono essenziali per diverse ragioni:

- **Migliore esperienza utente:** Gli utenti vedono aggiornamenti mentre il lavoro procede, non solo alla fine.
- **Feedback in tempo reale:** I client possono mostrare barre di progresso o log, rendendo l'app reattiva.
- **Debug e monitoraggio facilitati:** Sviluppatori e utenti vedono dove un processo può essere lento o bloccato.

### Come implementare le Notifiche di Progresso

Ecco come puoi implementare le notifiche di progresso in MCP:

- **Sul server:** usa `ctx.info()` o `ctx.log()` per inviare notifiche man mano che ogni elemento viene processato. Questo invia un messaggio al client prima che il risultato principale sia pronto.
- **Sul client:** implementa un message handler che ascolta e mostra le notifiche appena arrivano. Questo handler distingue tra notifiche e risultato finale.

**Esempio Server:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Esempio Client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considerazioni sulla Sicurezza

La sicurezza dovrebbe essere una priorità assoluta quando si implementa qualsiasi server, specialmente quando si utilizzano trasporti basati su HTTP come Streamable HTTP in MCP.

Quando si implementano server MCP con trasporti basati su HTTP, la sicurezza diventa una preoccupazione primaria che richiede attenzione accurata a molteplici vettori di attacco e meccanismi di protezione.

### Panoramica

La sicurezza è critica quando si espongono server MCP tramite HTTP. Streamable HTTP introduce nuove superfici di attacco e richiede una configurazione attenta.

Ecco alcune considerazioni chiave sulla sicurezza:

- **Validazione dell'header Origin**: Valida sempre l'header `Origin` per prevenire attacchi di DNS rebinding.
- **Binding su Localhost**: Per lo sviluppo locale, associa i server a `localhost` per evitare di esporli a internet pubblica.
- **Autenticazione**: Implementa l'autenticazione (es. chiavi API, OAuth) per le distribuzioni in produzione.
- **CORS**: Configura le politiche di Cross-Origin Resource Sharing (CORS) per limitare l'accesso.
- **HTTPS**: Usa HTTPS in produzione per criptare il traffico.

### Migliori Pratiche

Inoltre, ecco alcune migliori pratiche da seguire quando implementi la sicurezza nel tuo server streaming MCP:

- Non fidarti mai delle richieste in ingresso senza validazione.
- Registra e monitora tutti gli accessi e gli errori.
- Aggiorna regolarmente le dipendenze per correggere le vulnerabilità di sicurezza.

### Sfide

Affronterai alcune sfide quando implementi la sicurezza nei server streaming MCP:

- Bilanciare la sicurezza con la facilità di sviluppo
- Garantire la compatibilità con vari ambienti client


## Aggiornamento da SSE a Streamable HTTP

Per applicazioni che attualmente usano Server-Sent Events (SSE), migrare a Streamable HTTP offre capacità migliorate e una migliore sostenibilità a lungo termine per le tue implementazioni MCP.

### Perché Aggiornare?

Ci sono due ragioni importanti per aggiornare da SSE a Streamable HTTP:

- Streamable HTTP offre migliore scalabilità, compatibilità e supporto notifiche più ricco rispetto a SSE.
- È il trasporto raccomandato per nuove applicazioni MCP.

### Passaggi per la Migrazione

Ecco come puoi migrare da SSE a Streamable HTTP nelle tue applicazioni MCP:

- **Aggiorna il codice server** per usare `transport="streamable-http"` in `mcp.run()`.
- **Aggiorna il codice client** per usare `streamablehttp_client` invece del client SSE.
- **Implementa un gestore di messaggi** nel client per elaborare le notifiche.
- **Testa la compatibilità** con strumenti e flussi di lavoro esistenti.

### Mantenere la Compatibilità

Si consiglia di mantenere la compatibilità con i client SSE esistenti durante il processo di migrazione. Ecco alcune strategie:

- Puoi supportare sia SSE che Streamable HTTP eseguendo entrambi i trasporti su endpoint diversi.
- Migra gradualmente i client al nuovo trasporto.

### Sfide

Assicurati di affrontare le seguenti sfide durante la migrazione:

- Assicurare che tutti i client vengano aggiornati
- Gestire le differenze nella consegna delle notifiche

### Esercizio: Costruisci la Tua App Streaming MCP

**Scenario:**
Costruisci un server e un client MCP in cui il server processa una lista di elementi (es. file o documenti) e invia una notifica per ogni elemento processato. Il client deve mostrare ogni notifica appena arriva.

**Passaggi:**

1. Implementa uno strumento server che processa una lista e invia notifiche per ogni elemento.
2. Implementa un client con un gestore di messaggi per mostrare le notifiche in tempo reale.
3. Testa la tua implementazione eseguendo sia server che client, e osserva le notifiche.

[Soluzione](./solution/README.md)

## Letture Consigliate & Cosa Fare Dopo?

Per continuare il tuo percorso con lo streaming MCP e ampliare le tue conoscenze, questa sezione fornisce risorse aggiuntive e i prossimi passi suggeriti per costruire applicazioni più avanzate.

### Letture Consigliate

- [Microsoft: Introduzione allo Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Richieste in Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Cosa Fare Dopo?

- Prova a costruire strumenti MCP più avanzati che usano lo streaming per analytics in tempo reale, chat o editing collaborativo.
- Esplora l'integrazione dello streaming MCP con framework frontend (React, Vue, ecc.) per aggiornamenti live dell'interfaccia utente.
- Successivo: [Utilizzo della AI Toolkit per VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->