# Streaming HTTPS con il Protocollo Model Context (MCP)

Questo capitolo fornisce una guida completa per implementare uno streaming sicuro, scalabile e in tempo reale con il Model Context Protocol (MCP) utilizzando HTTPS. Copre la motivazione per lo streaming, i meccanismi di trasporto disponibili, come implementare HTTP streamabile in MCP, le best practice di sicurezza, la migrazione da SSE e indicazioni pratiche per costruire le proprie applicazioni MCP con streaming.

> [!WARNING]
> Gli esempi di implementazione in questa lezione sono rivolti alla **Specificazione MCP
> `2025-11-25`** e mostrano il handshake legacy `initialize`,
> `Mcp-Session-Id`, lo stream di eventi GET e il modello di riprendibilità. MCP `2026-07-28`
> rimuove queste funzionalità. Le richieste Streamable HTTP attuali sono richieste POST autonome
> con intestazioni `MCP-Protocol-Version` e `Mcp-Method`, più `Mcp-Name` dove richiesto.
> Vedi
> [Cosa è cambiato in MCP: la specifica 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> prima di usare questi esempi in una nuova implementazione.

## Meccanismi di Trasporto e Streaming in MCP

Questa sezione esplora i diversi meccanismi di trasporto disponibili in MCP e il loro ruolo nell’abilitare funzionalità di streaming per la comunicazione in tempo reale tra client e server.

### Cos’è un Meccanismo di Trasporto?

Un meccanismo di trasporto definisce come i dati vengono scambiati tra client e server. MCP supporta diversi tipi di trasporto per adattarsi a diversi ambienti e requisiti:

- **stdio**: Input/output standard, adatto per strumenti locali e CLI. Semplice ma non adatto per il web o cloud.
- **HTTP+SSE**: Il trasporto remoto legacy, deprecato in MCP `2025-03-26`
    e sostituito da Streamable HTTP. Non usarlo per nuove implementazioni.
- **Streamable HTTP**: Trasporto moderno basato su HTTP per streaming, con supporto a notifiche e migliore scalabilità. Raccomandato per la maggior parte dei casi di produzione e cloud.

### Tabella di Confronto

Dai un’occhiata alla tabella di confronto qui sotto per capire le differenze tra questi meccanismi di trasporto:

| Trasporto | Stato | Notifiche | Uso Tipico |
|---|---|---|---|
| stdio | Attuale | Sì | Processi locali |
| HTTP+SSE | Deprecato | Sì | Implementazioni remote legacy |
| Streamable HTTP | Attuale | Sì | Server remoti e cloud |

> **Suggerimento:** La scelta del trasporto giusto incide su prestazioni, scalabilità ed esperienza utente. **Streamable HTTP** è raccomandato per applicazioni moderne, scalabili e pronte per il cloud.

I trasporti standard sono stdio e Streamable HTTP. HTTP+SSE appare
solo in esempi più vecchi.

## Streaming: Concetti e Motivazione

Comprendere i concetti fondamentali e le motivazioni dietro lo streaming è essenziale per implementare sistemi di comunicazione in tempo reale efficaci.

**Lo streaming** è una tecnica nella programmazione di rete che permette di inviare e ricevere dati in piccoli pezzi gestibili o come una sequenza di eventi, invece di aspettare che tutta la risposta sia pronta. Questo è particolarmente utile per:

- File o dataset di grandi dimensioni.
- Aggiornamenti in tempo reale (es. chat, barre di progresso).
- Calcoli a lunga durata per tenere informato l’utente.

Ecco cosa devi sapere sullo streaming a grandi linee:

- I dati sono forniti progressivamente, non tutti insieme.
- Il client può processare i dati man mano che arrivano.
- Riduce la latenza percepita e migliora l’esperienza utente.

### Perché usare lo streaming?

Le ragioni per usare lo streaming sono le seguenti:

- Gli utenti ricevono feedback subito, non solo alla fine
- Abilita applicazioni in tempo reale e interfacce reattive
- Uso più efficiente delle risorse di rete e calcolo

### Esempio semplice: Server & Client HTTP Streaming

Ecco un esempio semplice di come si può implementare lo streaming:

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

Questo esempio mostra un server che invia una serie di messaggi al client mano a mano che sono disponibili, invece di aspettare che tutti i messaggi siano pronti.

**Come funziona:**

- Il server produce ogni messaggio appena è pronto.
- Il client riceve e stampa ogni pezzo appena arriva.

**Requisiti:**

- Il server deve usare una risposta di streaming (es. `StreamingResponse` in FastAPI).
- Il client deve processare la risposta come stream (`stream=True` in requests).
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

**Note sull’implementazione Java:**

- Usa lo stack reattivo di Spring Boot con `Flux` per lo streaming
- `ServerSentEvent` fornisce streaming di eventi strutturati con tipi di evento
- `WebClient` con `bodyToFlux()` permette il consumo reattivo dello streaming
- `delayElements()` simula il tempo di elaborazione tra gli eventi
- Gli eventi possono avere tipi (`info`, `result`) per una gestione migliore lato client

### Confronto: Streaming Classico vs Streaming MCP

Le differenze tra come funziona lo streaming in modo “classico” rispetto a come funziona in MCP possono essere rappresentate così:

| Caratteristica             | Streaming HTTP Classico         | Streaming MCP (Notifiche)         |
|---------------------------|--------------------------------|----------------------------------|
| Risposta principale        | A pezzi (chunked)               | Singola, alla fine               |
| Aggiornamenti di progresso | Inviati come pezzi di dati      | Inviati come notifiche           |
| Requisiti client           | Deve processare lo stream       | Deve implementare un gestore messaggi |
| Caso d’uso                 | File grandi, stream di token AI | Progresso, log, feedback realtime|

### Differenze chiave osservate

Inoltre, ecco alcune differenze chiave:

- **Pattern di comunicazione:** 
  - Streaming HTTP classico: usa un semplice encoding transfer chunked per inviare dati a pezzi
  - Streaming MCP: usa un sistema strutturato di notifiche con protocollo JSON-RPC

- **Formato del messaggio:** 
  - HTTP classico: pezzi di testo semplice con newline
  - MCP: oggetti LoggingMessageNotification strutturati con metadata

- **Implementazione client:** 
  - HTTP classico: client semplice che processa risposte in streaming
  - MCP: client più sofisticato con gestore messaggi per processare tipi diversi di messaggi

- **Aggiornamenti di progresso:** 
  - HTTP classico: il progresso è parte del flusso della risposta principale
  - MCP: il progresso è inviato tramite messaggi di notifica separati mentre la risposta principale arriva alla fine

### Raccomandazioni

Ci sono alcune cose che raccomandiamo nella scelta tra implementare lo streaming classico (come il punto finale `/stream` che abbiamo mostrato sopra) oppure scegliere lo streaming via MCP.

- **Per necessità di streaming semplici:** Lo streaming HTTP classico è più semplice da implementare e sufficiente per necessità di streaming di base.


- **Per applicazioni complesse e interattive:** Lo streaming MCP fornisce un approccio più strutturato con metadati più ricchi e separazione tra notifiche e risultati finali.

- **Per applicazioni AI:** Il sistema di notifiche MCP è particolarmente utile per compiti AI a lunga durata in cui si desidera tenere gli utenti informati sul progresso.

## Streaming in MCP

Bene, finora hai visto alcune raccomandazioni e confronti sulla differenza tra lo streaming classico e lo streaming in MCP. Entriamo nei dettagli su come puoi sfruttare lo streaming in MCP.

Comprendere come funziona lo streaming nel framework MCP è essenziale per costruire applicazioni reattive che offrano feedback in tempo reale agli utenti durante operazioni a lunga durata.

In MCP, lo streaming non riguarda l'invio della risposta principale a pezzi, ma l'invio di **notifiche** al client mentre uno strumento sta elaborando una richiesta. Queste notifiche possono includere aggiornamenti sul progresso, log o altri eventi.

### Come funziona

Il risultato principale viene comunque inviato come risposta singola. Tuttavia, le notifiche possono essere inviate come messaggi separati durante l'elaborazione e aggiornare così il client in tempo reale. Il client deve essere in grado di gestire e visualizzare queste notifiche.

### Esercizio opzionale: connettersi a un server MCP ospitato

Puoi anche usare Streamable HTTP senza eseguire un server locale. Questo esempio
si connette a [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
scopre i suoi strumenti e cerca la documentazione MCP pubblica usando lo stesso
SDK Python del [client locale](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

L'endpoint anonimo di Parallel non richiede account né chiave API. L'accesso gratuito è
limitato in frequenza. Eseguendo questo script vengono inviati le query di ricerca, l'obiettivo e un
identificatore di sessione casuale a Parallel. Il servizio offre anche `web_fetch`,
che invia URL richieste e qualsiasi contesto fornito a Parallel. Usa informazioni pubbliche
per questo esercizio; consulta i suoi [termini](https://parallel.ai/customer-terms)
e la [politica sulla privacy](https://parallel.ai/privacy-policy).

Con Python 3.10 o versione più recente e un ambiente virtuale attivato, installa lo SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Salva questo come `hosted_search.py` ed esegui `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Aspettati che la scoperta includa `web_search` e `web_fetch`, seguiti da una risposta di ricerca
contenente URL delle fonti ed estratti. I risultati possono variare o essere vuoti.
Lo script controlla `isError` perché uno strumento può fallire anche se la richiesta HTTP
ha successo. Se l'accesso è limitato in frequenza, attendi prima di riprovare. Riutilizza lo stesso
`session_id` se estendi lo script con chiamate correlate di ricerca o fetch.

Streamable HTTP consente risposte sia JSON che SSE; questo server può restituire un
risultato JSON completo senza notifiche di progresso. Lo SDK gestisce il
trasporto. Continua con l'esempio locale qui sotto per imparare sulle notifiche.
Questo script opzionale fa una ricerca esplicita e chiude la connessione quando
questa termina. Se in seguito esponi questi strumenti a un agente, l’agente può invocarli
durante il suo lavoro; tratta il testo web recuperato come dati non affidabili.

## Cos’è una Notifica?

Abbiamo detto "Notifica", cosa significa nel contesto di MCP?

Una notifica è un messaggio JSON-RPC che non ha un `id` e non
riceve una risposta. MCP usa le notifiche per progresso, cancellazione e
altri eventi unidirezionali.

In MCP `2025-11-25`, un client invia `notifications/initialized` dopo il
handshake di inizializzazione. MCP `2026-07-28` non ha handshake di inizializzazione, quindi
questa notifica è comportamento legacy.

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

Il logging è una delle funzionalità che usa le notifiche; le notifiche stesse sono un
tipo di messaggio JSON-RPC generico.

> **Deprecato in MCP `2026-07-28`:** la funzione Logging rimane disponibile
> per compatibilità ma può essere rimossa nella prima revisione dello standard
> pubblicata dopo il 28 luglio 2027. Le nuove implementazioni dovrebbero usare
> `stderr` con stdio o OpenTelemetry per osservabilità strutturata.

Per un'implementazione legacy `2025-11-25`, il server abilita la capacità Logging
come segue:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> A seconda dello SDK usato, il logging potrebbe essere abilitato di default o potrebbe essere necessario abilitarlo esplicitamente nella configurazione del server.

Esistono diversi tipi di notifiche:

| Livello   | Descrizione                   | Caso d’Uso Esempio             |
|-----------|------------------------------|-------------------------------|
| debug     | Informazioni dettagliate per il debug | Punti di ingresso/uscita funzione |
| info      | Messaggi informativi generali | Aggiornamenti sul progresso dell’operazione |
| notice    | Eventi normali ma significativi | Cambiamenti di configurazione    |
| warning   | Condizioni di avviso           | Uso di funzionalità deprecate    |
| error     | Condizioni di errore           | Fallimenti dell’operazione        |
| critical  | Condizioni critiche            | Fallimenti di componenti di sistema |
| alert     | Deve essere presa azione immediatamente | Rilevata corruzione dati        |
| emergency | Sistema inutilizzabile         | Guasto completo del sistema       |

## Implementazione delle Notifiche in MCP

Per implementare le notifiche in MCP, devi configurare sia il lato server che client per gestire aggiornamenti in tempo reale. Questo permette alla tua applicazione di fornire feedback immediato agli utenti durante operazioni a lunga durata.

### Lato server: Invio Notifiche

Cominciamo dal lato server. In MCP definisci strumenti che possono inviare notifiche durante l'elaborazione delle richieste. Il server usa l'oggetto contesto (di solito `ctx`) per inviare messaggi al client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Nell’esempio precedente, lo strumento `process_files` invia tre notifiche al client mentre elabora ogni file. Il metodo `ctx.info()` viene usato per inviare messaggi informativi.

Inoltre, per abilitare le notifiche, assicurati che il server usi un trasporto streaming (come `streamable-http`) e che il client implementi un gestore dei messaggi per elaborare le notifiche. Ecco come impostare il server per usare il trasporto `streamable-http`:

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

In questo esempio .NET, lo strumento `ProcessFiles` è decorato con l'attributo `Tool` e invia tre notifiche al client mentre elabora ogni file. Il metodo `ctx.Info()` è usato per inviare messaggi informativi.

Per abilitare le notifiche nel tuo server MCP .NET, assicurati di utilizzare un trasporto streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Lato client: Ricezione Notifiche

Il client deve implementare un gestore dei messaggi per elaborare e visualizzare le notifiche non appena arrivano.

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

Nel codice precedente, la funzione `message_handler` verifica se il messaggio in arrivo è una notifica. Se lo è, stampa la notifica; altrimenti, la elabora come un messaggio server normale. Nota anche come la `ClientSession` viene inizializzata con `message_handler` per gestire le notifiche in arrivo.

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


In questo esempio .NET, la funzione `MessageHandler` verifica se il messaggio in arrivo è una notifica. Se lo è, stampa la notifica; altrimenti, la elabora come un messaggio normale del server. La `ClientSession` viene inizializzata con il gestore di messaggi tramite le `ClientSessionOptions`.

Per abilitare le notifiche, assicurati che il tuo server utilizzi un trasporto streaming (come `streamable-http`) e che il tuo client implementi un gestore di messaggi per elaborare le notifiche.

## Notifiche di progresso e scenari

Questa sezione spiega il concetto di notifiche di progresso in MCP, perché sono importanti e come implementarle usando Streamable HTTP. Troverai anche un esercizio pratico per rafforzare la tua comprensione.

Le notifiche di progresso sono messaggi in tempo reale inviati dal server al client durante operazioni di lunga durata. Invece di attendere che l'intero processo finisca, il server aggiorna il client sullo stato attuale. Questo migliora la trasparenza, l'esperienza utente e facilita il debug.

**Esempio:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Perché usare le notifiche di progresso?

Le notifiche di progresso sono essenziali per diversi motivi:

- **Migliore esperienza utente:** Gli utenti vedono gli aggiornamenti mentre il lavoro procede, non solo alla fine.
- **Feedback in tempo reale:** I client possono mostrare barre di progresso o log, rendendo l’app più reattiva.
- **Debug e monitoraggio più facili:** Sviluppatori e utenti possono vedere dove un processo potrebbe essere lento o bloccato.

### Come implementare le notifiche di progresso

Ecco come puoi implementare le notifiche di progresso in MCP:

- **Sul server:** Usa `ctx.info()` o `ctx.log()` per inviare notifiche mentre ogni elemento viene processato. Questo invia un messaggio al client prima che il risultato principale sia pronto.
- **Sul client:** Implementa un gestore di messaggi che ascolta e mostra le notifiche non appena arrivano. Questo gestore distingue tra notifiche e risultato finale.

**Esempio server:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Esempio client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considerazioni sulla sicurezza

La sicurezza dovrebbe essere una priorità assoluta quando si implementa qualsiasi server, specialmente usando trasporti HTTP come Streamable HTTP in MCP.

Quando si implementano server MCP con trasporti basati su HTTP, la sicurezza diventa una preoccupazione fondamentale che richiede attenzione a molteplici vettori di attacco e meccanismi di protezione.

### Panoramica

La sicurezza è critica quando si espongono server MCP via HTTP. Streamable HTTP introduce nuove superfici di attacco e richiede una configurazione attenta.

Ecco alcune considerazioni chiave sulla sicurezza:

- **Validazione dell'header Origin:** Valida sempre l’header `Origin` per prevenire attacchi di DNS rebinding.
- **Bind su localhost:** Per lo sviluppo locale, lega i server a `localhost` per evitare di esporli su internet pubblico.
- **Autenticazione:** Implementa l’autenticazione (ad es., chiavi API, OAuth) per le distribuzioni in produzione.
- **CORS:** Configura politiche di Cross-Origin Resource Sharing (CORS) per limitare l’accesso.
- **HTTPS:** Usa HTTPS in produzione per cifrare il traffico.

### Best Practices

Inoltre, ecco alcune best practice da seguire quando implementi la sicurezza nel tuo server streaming MCP:

- Non fidarti mai di richieste in ingresso senza validazione.
- Registra e monitora tutti gli accessi e errori.
- Aggiorna regolarmente le dipendenze per correggere vulnerabilità di sicurezza.

### Sfide

Affronterai alcune sfide quando implementi la sicurezza in server MCP streaming:

- Bilanciare sicurezza e facilità di sviluppo
- Garantire compatibilità con vari ambienti client


## Aggiornamento da SSE a Streamable HTTP

Per applicazioni che attualmente usano Server-Sent Events (SSE), migrare a Streamable HTTP offre capacità migliorate e migliore sostenibilità a lungo termine per le tue implementazioni MCP.

### Perché aggiornare?

Ci sono due motivi convincenti per aggiornare da SSE a Streamable HTTP:

- Streamable HTTP offre migliore scalabilità, compatibilità e supporto alle notifiche più ricco rispetto a SSE.
- È il trasporto raccomandato per nuove applicazioni MCP.

### Passi per la migrazione

Ecco come puoi migrare da SSE a Streamable HTTP nelle tue applicazioni MCP:

- **Aggiorna il codice server** per usare `transport="streamable-http"` in `mcp.run()`.
- **Aggiorna il codice client** per usare `streamablehttp_client` invece del client SSE.
- **Implementa un gestore di messaggi** nel client per elaborare le notifiche.
- **Testa la compatibilità** con strumenti e flussi di lavoro esistenti.

### Mantenere la compatibilità

È consigliabile mantenere la compatibilità con i client SSE esistenti durante il processo di migrazione. Ecco alcune strategie:

- Puoi supportare sia SSE che Streamable HTTP eseguendo entrambi i trasporti su endpoint differenti.
- Migra i client gradualmente al nuovo trasporto.

### Sfide

Assicurati di affrontare le seguenti sfide durante la migrazione:

- Aggiornare tutti i client
- Gestire le differenze nella consegna delle notifiche

### Esercizio: Costruisci la tua app MCP streaming

**Scenario:**
Costruisci un server MCP e un client in cui il server elabora una lista di elementi (es., file o documenti) e invia una notifica per ogni elemento processato. Il client deve mostrare ogni notifica appena arriva.

**Passi:**

1. Implementa uno strumento server che elabora una lista e invia notifiche per ogni elemento.
2. Implementa un client con un gestore di messaggi per mostrare le notifiche in tempo reale.
3. Testa la tua implementazione eseguendo sia server che client e osserva le notifiche.

[Soluzione](./solution/README.md)

## Letture aggiuntive e cosa fare dopo?

Per continuare il tuo percorso con MCP streaming ed espandere le tue conoscenze, questa sezione fornisce risorse aggiuntive e passaggi consigliati per costruire applicazioni più avanzate.

### Letture aggiuntive

- [Microsoft: Introduzione a HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Cosa fare dopo?

- Prova a costruire strumenti MCP più avanzati che usano lo streaming per analisi in tempo reale, chat o editing collaborativo.
- Esplora l’integrazione dello streaming MCP con framework frontend (React, Vue, ecc.) per aggiornamenti live dell’interfaccia.
- Next: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->