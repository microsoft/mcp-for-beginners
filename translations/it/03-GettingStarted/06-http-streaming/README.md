# Streaming HTTPS con il Protocollo Model Context (MCP)

Questo capitolo offre una guida completa per implementare lo streaming sicuro, scalabile e in tempo reale con il Protocollo Model Context (MCP) utilizzando HTTPS. Copre la motivazione per lo streaming, i meccanismi di trasporto disponibili, come implementare HTTP streamable in MCP, le migliori pratiche di sicurezza, la migrazione da SSE e indicazioni pratiche per costruire le proprie applicazioni MCP di streaming.

## Meccanismi di Trasporto e Streaming in MCP

Questa sezione esplora i diversi meccanismi di trasporto disponibili in MCP e il loro ruolo nell'abilitare capacità di streaming per la comunicazione in tempo reale tra client e server.

### Cos'è un Meccanismo di Trasporto?

Un meccanismo di trasporto definisce come i dati vengono scambiati tra client e server. MCP supporta diversi tipi di trasporto per adattarsi a diversi ambienti e requisiti:

- **stdio**: Input/output standard, adatto per strumenti locali e basati su CLI. Semplice ma non adatto per il web o il cloud.
- **SSE (Server-Sent Events)**: Consente ai server di inviare aggiornamenti in tempo reale ai client tramite HTTP. Buono per interfacce web, ma limitato in scalabilità e flessibilità.
- **Streamable HTTP**: Trasporto moderno basato su HTTP per lo streaming, supporta notifiche e offre una migliore scalabilità. Raccomandato per la maggior parte degli scenari di produzione e cloud.

### Tabella Comparativa

Dai un'occhiata alla tabella comparativa qui sotto per comprendere le differenze tra questi meccanismi di trasporto:

| Trasporto          | Aggiornamenti in tempo reale | Streaming | Scalabilità | Caso d'uso                |
|--------------------|-----------------------------|-----------|-------------|---------------------------|
| stdio              | No                          | No        | Bassa       | Strumenti CLI locali      |
| SSE                | Sì                          | Sì        | Media       | Web, aggiornamenti in tempo reale |
| Streamable HTTP    | Sì                          | Sì        | Alta        | Cloud, multi-client       |

> **Suggerimento:** La scelta del trasporto giusto influisce su prestazioni, scalabilità ed esperienza utente. **Streamable HTTP** è raccomandato per applicazioni moderne, scalabili e pronte per il cloud.

Nota i trasporti stdio e SSE che ti sono stati mostrati nei capitoli precedenti e come lo Streamable HTTP sia il trasporto trattato in questo capitolo.

## Streaming: Concetti e Motivazione

Comprendere i concetti fondamentali e le motivazioni dietro lo streaming è essenziale per implementare sistemi di comunicazione in tempo reale efficaci.

**Streaming** è una tecnica nella programmazione di rete che consente di inviare e ricevere dati in piccoli pezzi gestibili o come una sequenza di eventi, piuttosto che aspettare che l'intera risposta sia pronta. Questo è particolarmente utile per:

- File o dataset di grandi dimensioni.
- Aggiornamenti in tempo reale (es. chat, barre di progresso).
- Computazioni di lunga durata dove si vuole mantenere l'utente informato.

Ecco cosa devi sapere sullo streaming a livello generale:

- I dati vengono consegnati progressivamente, non tutti in una volta.
- Il client può elaborare i dati man mano che arrivano.
- Riduce la latenza percepita e migliora l'esperienza utente.

### Perché usare lo streaming?

Le ragioni per utilizzare lo streaming sono le seguenti:

- Gli utenti ricevono feedback immediato, non solo alla fine.
- Abilita applicazioni in tempo reale e interfacce utente reattive.
- Utilizzo più efficiente delle risorse di rete e calcolo.

### Esempio Semplice: Server e Client HTTP Streaming

Ecco un esempio semplice di come lo streaming può essere implementato:

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

Questo esempio dimostra un server che invia una serie di messaggi al client man mano che diventano disponibili, piuttosto che aspettare che tutti i messaggi siano pronti.

**Come funziona:**

- Il server genera ogni messaggio man mano che è pronto.
- Il client riceve e stampa ogni pezzo man mano che arriva.

**Requisiti:**

- Il server deve utilizzare una risposta di streaming (es. `StreamingResponse` in FastAPI).
- Il client deve elaborare la risposta come un flusso (`stream=True` in requests).
- Il Content-Type è solitamente `text/event-stream` o `application/octet-stream`.

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

- Utilizza lo stack reattivo di Spring Boot con `Flux` per lo streaming.
- `ServerSentEvent` fornisce uno streaming di eventi strutturato con tipi di evento.
- `WebClient` con `bodyToFlux()` abilita il consumo reattivo dello streaming.
- `delayElements()` simula il tempo di elaborazione tra gli eventi.
- Gli eventi possono avere tipi (`info`, `result`) per una migliore gestione da parte del client.

### Confronto: Streaming Classico vs Streaming MCP

Le differenze tra il funzionamento dello streaming in modo "classico" rispetto a come funziona in MCP possono essere rappresentate così:

| Caratteristica          | Streaming HTTP Classico       | Streaming MCP (Notifiche)         |
|-------------------------|-------------------------------|------------------------------------|
| Risposta principale     | A pezzi                      | Singola, alla fine                |
| Aggiornamenti di progresso | Inviati come pezzi di dati   | Inviati come notifiche            |
| Requisiti del client    | Deve elaborare il flusso      | Deve implementare un gestore di messaggi |
| Caso d'uso              | File grandi, flussi di token AI | Progresso, log, feedback in tempo reale |

### Differenze Chiave Osservate

Inoltre, ecco alcune differenze chiave:

- **Pattern di Comunicazione:**
  - Streaming HTTP classico: Utilizza una semplice codifica di trasferimento a pezzi per inviare dati in blocchi.
  - Streaming MCP: Utilizza un sistema di notifiche strutturato con protocollo JSON-RPC.

- **Formato del Messaggio:**
  - HTTP classico: Blocchi di testo semplice con nuove righe.
  - MCP: Oggetti LoggingMessageNotification strutturati con metadati.

- **Implementazione del Client:**
  - HTTP classico: Client semplice che elabora risposte di streaming.
  - MCP: Client più sofisticato con un gestore di messaggi per elaborare diversi tipi di messaggi.

- **Aggiornamenti di Progresso:**
  - HTTP classico: Il progresso fa parte del flusso di risposta principale.
  - MCP: Il progresso viene inviato tramite messaggi di notifica separati mentre la risposta principale arriva alla fine.

### Raccomandazioni

Ci sono alcune cose che raccomandiamo quando si tratta di scegliere tra l'implementazione dello streaming classico (come un endpoint che ti abbiamo mostrato sopra usando `/stream`) e lo streaming tramite MCP.

- **Per esigenze di streaming semplici:** Lo streaming HTTP classico è più semplice da implementare e sufficiente per esigenze di streaming di base.

- **Per applicazioni complesse e interattive:** Lo streaming MCP offre un approccio più strutturato con metadati più ricchi e separazione tra notifiche e risultati finali.

- **Per applicazioni AI:** Il sistema di notifiche di MCP è particolarmente utile per attività AI di lunga durata dove si vuole mantenere gli utenti informati sul progresso.

## Streaming in MCP

Ok, quindi hai visto alcune raccomandazioni e confronti finora sulla differenza tra lo streaming classico e lo streaming in MCP. Vediamo in dettaglio come puoi sfruttare lo streaming in MCP.

Comprendere come funziona lo streaming all'interno del framework MCP è essenziale per costruire applicazioni reattive che forniscono feedback in tempo reale agli utenti durante operazioni di lunga durata.

In MCP, lo streaming non riguarda l'invio della risposta principale in pezzi, ma l'invio di **notifiche** al client mentre uno strumento sta elaborando una richiesta. Queste notifiche possono includere aggiornamenti di progresso, log o altri eventi.

### Come funziona

Il risultato principale viene comunque inviato come una singola risposta. Tuttavia, le notifiche possono essere inviate come messaggi separati durante l'elaborazione, aggiornando così il client in tempo reale. Il client deve essere in grado di gestire e visualizzare queste notifiche.

## Cos'è una Notifica?

Abbiamo detto "Notifica", cosa significa nel contesto di MCP?

Una notifica è un messaggio inviato dal server al client per informare sul progresso, lo stato o altri eventi durante un'operazione di lunga durata. Le notifiche migliorano la trasparenza e l'esperienza utente.

Ad esempio, un client dovrebbe inviare una notifica una volta effettuata la stretta di mano iniziale con il server.

Una notifica appare così come un messaggio JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Le notifiche appartengono a un argomento in MCP chiamato ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Per far funzionare il logging, il server deve abilitarlo come funzionalità/capacità in questo modo:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> A seconda dell'SDK utilizzato, il logging potrebbe essere abilitato di default, oppure potrebbe essere necessario abilitarlo esplicitamente nella configurazione del server.

Ci sono diversi tipi di notifiche:

| Livello    | Descrizione                     | Caso d'uso esempio              |
|------------|---------------------------------|----------------------------------|
| debug      | Informazioni dettagliate di debug | Punti di ingresso/uscita funzione |
| info       | Messaggi informativi generali   | Aggiornamenti sul progresso      |
| notice     | Eventi normali ma significativi | Modifiche alla configurazione    |
| warning    | Condizioni di avviso            | Uso di funzionalità deprecate    |
| error      | Condizioni di errore            | Fallimenti operativi             |
| critical   | Condizioni critiche             | Fallimenti di componenti di sistema |
| alert      | Azione immediata necessaria     | Rilevamento di corruzione dati   |
| emergency  | Sistema inutilizzabile          | Fallimento completo del sistema  |

## Implementazione delle Notifiche in MCP

Per implementare le notifiche in MCP, è necessario configurare sia il lato server che il lato client per gestire gli aggiornamenti in tempo reale. Questo consente alla tua applicazione di fornire feedback immediato agli utenti durante operazioni di lunga durata.

### Lato server: Invio delle Notifiche

Iniziamo con il lato server. In MCP, definisci strumenti che possono inviare notifiche mentre elaborano richieste. Il server utilizza l'oggetto contesto (di solito `ctx`) per inviare messaggi al client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Nell'esempio precedente, lo strumento `process_files` invia tre notifiche al client mentre elabora ciascun file. Il metodo `ctx.info()` viene utilizzato per inviare messaggi informativi.

Inoltre, per abilitare le notifiche, assicurati che il tuo server utilizzi un trasporto di streaming (come `streamable-http`) e che il tuo client implementi un gestore di messaggi per elaborare le notifiche. Ecco come puoi configurare il server per utilizzare il trasporto `streamable-http`:

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

In questo esempio .NET, lo strumento `ProcessFiles` è decorato con l'attributo `Tool` e invia tre notifiche al client mentre elabora ciascun file. Il metodo `ctx.Info()` viene utilizzato per inviare messaggi informativi.

Per abilitare le notifiche nel tuo server MCP .NET, assicurati di utilizzare un trasporto di streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lato client: Ricezione delle Notifiche

Il client deve implementare un gestore di messaggi per elaborare e visualizzare le notifiche man mano che arrivano.

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

Nel codice precedente, la funzione `message_handler` verifica se il messaggio in arrivo è una notifica. Se lo è, stampa la notifica; altrimenti, la elabora come un normale messaggio del server. Nota anche come la `ClientSession` viene inizializzata con il `message_handler` per gestire le notifiche in arrivo.

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

In questo esempio .NET, la funzione `MessageHandler` verifica se il messaggio in arrivo è una notifica. Se lo è, stampa la notifica; altrimenti, la elabora come un normale messaggio del server. La `ClientSession` viene inizializzata con il gestore di messaggi tramite le `ClientSessionOptions`.

Per abilitare le notifiche, assicurati che il tuo server utilizzi un trasporto di streaming (come `streamable-http`) e che il tuo client implementi un gestore di messaggi per elaborare le notifiche.

## Notifiche di Progresso e Scenari

Questa sezione spiega il concetto di notifiche di progresso in MCP, perché sono importanti e come implementarle utilizzando Streamable HTTP. Troverai anche un esercizio pratico per rafforzare la tua comprensione.

Le notifiche di progresso sono messaggi in tempo reale inviati dal server al client durante operazioni di lunga durata. Invece di aspettare che l'intero processo finisca, il server tiene aggiornato il client sullo stato corrente. Questo migliora la trasparenza, l'esperienza utente e facilita il debug.

**Esempio:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Perché Usare le Notifiche di Progresso?

Le notifiche di progresso sono essenziali per diversi motivi:

- **Migliore esperienza utente:** Gli utenti vedono aggiornamenti man mano che il lavoro progredisce, non solo alla fine.
- **Feedback in tempo reale:** I client possono visualizzare barre di progresso o log, rendendo l'app più reattiva.
- **Debug e monitoraggio più facili:** Sviluppatori e utenti possono vedere dove un processo potrebbe essere lento o bloccato.

### Come Implementare le Notifiche di Progresso

Ecco come puoi implementare le notifiche di progresso in MCP:

- **Sul server:** Usa `ctx.info()` o `ctx.log()` per inviare notifiche man mano che ogni elemento viene elaborato. Questo invia un messaggio al client prima che il risultato principale sia pronto.
- **Sul client:** Implementa un gestore di messaggi che ascolta e visualizza le notifiche man mano che arrivano. Questo gestore distingue tra notifiche e risultato finale.

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

Quando si implementano server MCP con trasporti basati su HTTP, la sicurezza diventa una preoccupazione fondamentale che richiede attenzione a molteplici vettori di attacco e meccanismi di protezione.

### Panoramica

La sicurezza è critica quando si espongono server MCP su HTTP. Lo Streamable HTTP introduce nuove superfici di attacco e richiede una configurazione attenta.

### Punti Chiave

- **Validazione dell'header Origin**: Valida sempre l'header `Origin` per prevenire attacchi di DNS rebinding.
- **Binding su localhost**: Per lo sviluppo locale, collega i server a `localhost` per evitare di esporli su internet pubblica.
- **Autenticazione**: Implementa l'autenticazione (es. chiavi API, OAuth) per i deployment in produzione.
- **CORS**: Configura le politiche di Cross-Origin Resource Sharing (CORS) per limitare l'accesso.
- **HTTPS**: Usa HTTPS in produzione per criptare il traffico.

### Migliori Pratiche

- Non fidarti mai delle richieste in arrivo senza validazione.
- Registra e monitora tutti gli accessi e gli errori.
- Aggiorna regolarmente le dipendenze per correggere vulnerabilità di sicurezza.

### Sfide

- Bilanciare sicurezza e facilità di sviluppo.
- Garantire compatibilità con vari ambienti client.

## Aggiornamento da SSE a Streamable HTTP

Per le applicazioni che attualmente utilizzano Server-Sent Events (SSE), migrare a Streamable HTTP offre capacità migliorate e una migliore sostenibilità a lungo termine per le implementazioni MCP.

### Perché Aggiornare?
Ci sono due motivi convincenti per passare da SSE a Streamable HTTP:

- Streamable HTTP offre una migliore scalabilità, compatibilità e supporto per notifiche più ricche rispetto a SSE.
- È il trasporto raccomandato per le nuove applicazioni MCP.

### Passaggi per la Migrazione

Ecco come puoi migrare da SSE a Streamable HTTP nelle tue applicazioni MCP:

- **Aggiorna il codice del server** per utilizzare `transport="streamable-http"` in `mcp.run()`.
- **Aggiorna il codice del client** per utilizzare `streamablehttp_client` invece del client SSE.
- **Implementa un gestore di messaggi** nel client per elaborare le notifiche.
- **Testa la compatibilità** con gli strumenti e i flussi di lavoro esistenti.

### Mantenere la Compatibilità

Si consiglia di mantenere la compatibilità con i client SSE esistenti durante il processo di migrazione. Ecco alcune strategie:

- Puoi supportare sia SSE che Streamable HTTP eseguendo entrambi i trasporti su endpoint diversi.
- Migra gradualmente i client al nuovo trasporto.

### Sfide

Assicurati di affrontare le seguenti sfide durante la migrazione:

- Garantire che tutti i client siano aggiornati
- Gestire le differenze nella consegna delle notifiche

## Considerazioni sulla Sicurezza

La sicurezza dovrebbe essere una priorità assoluta quando si implementa un server, specialmente utilizzando trasporti basati su HTTP come Streamable HTTP in MCP.

Quando si implementano server MCP con trasporti basati su HTTP, la sicurezza diventa una preoccupazione fondamentale che richiede attenzione a molteplici vettori di attacco e meccanismi di protezione.

### Panoramica

La sicurezza è fondamentale quando si espongono server MCP su HTTP. Streamable HTTP introduce nuove superfici di attacco e richiede una configurazione attenta.

Ecco alcune considerazioni chiave sulla sicurezza:

- **Validazione dell'header Origin**: Valida sempre l'header `Origin` per prevenire attacchi di DNS rebinding.
- **Binding su Localhost**: Per lo sviluppo locale, vincola i server a `localhost` per evitare di esporli a Internet pubblico.
- **Autenticazione**: Implementa l'autenticazione (ad esempio, chiavi API, OAuth) per i deployment in produzione.
- **CORS**: Configura le politiche di Cross-Origin Resource Sharing (CORS) per limitare l'accesso.
- **HTTPS**: Usa HTTPS in produzione per crittografare il traffico.

### Migliori Pratiche

Inoltre, ecco alcune migliori pratiche da seguire quando implementi la sicurezza nel tuo server di streaming MCP:

- Non fidarti mai delle richieste in arrivo senza validazione.
- Registra e monitora tutti gli accessi e gli errori.
- Aggiorna regolarmente le dipendenze per correggere le vulnerabilità di sicurezza.

### Sfide

Affronterai alcune sfide nell'implementare la sicurezza nei server di streaming MCP:

- Bilanciare la sicurezza con la facilità di sviluppo
- Garantire la compatibilità con vari ambienti client

### Compito: Crea la Tua Applicazione MCP in Streaming

**Scenario:**
Crea un server e un client MCP in cui il server elabora un elenco di elementi (ad esempio, file o documenti) e invia una notifica per ogni elemento elaborato. Il client dovrebbe visualizzare ogni notifica non appena arriva.

**Passaggi:**

1. Implementa uno strumento server che elabora un elenco e invia notifiche per ogni elemento.
2. Implementa un client con un gestore di messaggi per visualizzare le notifiche in tempo reale.
3. Testa la tua implementazione eseguendo sia il server che il client e osserva le notifiche.

[Soluzione](./solution/README.md)

## Ulteriori Letture e Prossimi Passi

Per continuare il tuo percorso con lo streaming MCP ed espandere le tue conoscenze, questa sezione fornisce risorse aggiuntive e suggerimenti per i prossimi passi nella creazione di applicazioni più avanzate.

### Ulteriori Letture

- [Microsoft: Introduzione allo Streaming HTTP](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Prossimi Passi

- Prova a creare strumenti MCP più avanzati che utilizzano lo streaming per analisi in tempo reale, chat o editing collaborativo.
- Esplora l'integrazione dello streaming MCP con framework frontend (React, Vue, ecc.) per aggiornamenti live dell'interfaccia utente.
- Prossimo: [Utilizzare AI Toolkit per VSCode](../07-aitk/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.