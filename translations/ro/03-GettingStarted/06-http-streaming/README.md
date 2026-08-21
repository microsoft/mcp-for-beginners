# Streaming HTTPS cu Model Context Protocol (MCP)

Acest capitol oferă un ghid cuprinzător pentru implementarea streaming-ului securizat, scalabil și în timp real cu Model Context Protocol (MCP) folosind HTTPS. Acoperă motivația pentru streaming, mecanismele de transport disponibile, cum să implementezi HTTP streamabil în MCP, cele mai bune practici de securitate, migrarea de la SSE și ghid practic pentru construirea propriilor aplicații streaming MCP.

> **Privind înainte:** această lecție descrie Streamable HTTP sub **MCP Specification 2025-11-25**, unde o sesiune este stabilită în timpul `initialize` și fixată cu un header `Mcp-Session-Id`. Candidatul la lansarea `2026-07-28` elimină complet handshake-ul și ID-ul sesiunii, făcând fiecare cerere autonomă și rutabilă către orice instanță de server fără sesiuni sticky. Vezi [Ce se schimbă în MCP: Candidatul la lansare 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) pentru detalii.

## Mecanisme de Transport și Streaming în MCP

Această secțiune explorează diferitele mecanisme de transport disponibile în MCP și rolul lor în activarea capacităților de streaming pentru comunicarea în timp real între clienți și servere.

### Ce este un mecanism de transport?

Un mecanism de transport definește modul în care datele sunt schimbate între client și server. MCP suportă multiple tipuri de transport pentru a se potrivi diferitelor medii și cerințe:

- **stdio**: Intrare/ieșire standard, potrivit pentru instrumente locale și bazate pe CLI. Simplu dar nepotrivit pentru web sau cloud.
- **SSE (Server-Sent Events)**: Permite serverelor să trimită actualizări în timp real către clienți peste HTTP. Bun pentru interfețe web, dar limitat în scalabilitate și flexibilitate. Începând cu MCP Specification 2025-06-18, transportul SSE standalone a fost depreciat și înlocuit cu transportul „Streamable HTTP”.
- **Streamable HTTP**: Transport modern de streaming bazat pe HTTP, suportând notificări și o scalabilitate mai bună. Recomandat pentru majoritatea scenariilor de producție și cloud.

### Tabel comparativ

Aruncă o privire la tabelul comparativ de mai jos pentru a înțelege diferențele dintre aceste mecanisme de transport:

| Transport         | Actualizări în timp real | Streaming | Scalabilitate | Caz de utilizare         |
|-------------------|-------------------------|-----------|--------------|-------------------------|
| stdio             | Nu                      | Nu        | Scăzut       | Instrumente CLI locale   |
| SSE               | Da                      | Da        | Mediu        | Web, actualizări în timp real |
| Streamable HTTP    | Da                      | Da        | Ridicat      | Cloud, multi-client      |

> **Sfat:** Alegerea transportului potrivit impactează performanța, scalabilitatea și experiența utilizatorului. **Streamable HTTP** este recomandat pentru aplicații moderne, scalabile și pregătite pentru cloud.

Observă serviciile stdio și SSE prezentate în capitolele anterioare și că transportul streamable HTTP este acoperit în acest capitol.

## Streaming: Concepte și motivație

Înțelegerea conceptelor fundamentale și motivațiilor din spatele streamingului este esențială pentru implementarea unor sisteme eficiente de comunicare în timp real.

**Streaming** este o tehnică în programarea rețelelor care permite trimiterea și recepția datelor în porții mici, gestionabile sau ca o succesiune de evenimente, în loc să se aștepte până când un răspuns complet este gata. Aceasta este utilă în special pentru:

- Fișiere mari sau seturi de date.
- Actualizări în timp real (ex: chat, bare de progres).
- Computații pe termen lung unde dorești să ții utilizatorul informat.

Iată ce trebuie să știi despre streaming la nivel înalt:

- Datele sunt livrate progresiv, nu toate odată.
- Clientul poate procesa datele pe măsură ce sosesc.
- Reduce latența percepută și îmbunătățește experiența utilizatorului.

### De ce să folosești streaming?

Motivele pentru utilizarea streamingului sunt următoarele:

- Utilizatorii primesc feedback imediat, nu doar la final.
- Permite aplicații în timp real și interfețe responsive.
- Utilizare mai eficientă a resurselor de rețea și calcul.

### Exemplu simplu: Server și client HTTP Streaming

Iată un exemplu simplu despre cum poate fi implementat streamingul:

#### Python

**Server (Python, folosind FastAPI și StreamingResponse):**

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

**Client (Python, folosind requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Acest exemplu demonstrează un server care trimite o serie de mesaje către client pe măsură ce devin disponibile, în loc să aștepte ca toate mesajele să fie gata.

**Cum funcționează:**

- Serverul emite fiecare mesaj pe măsură ce este gata.
- Clientul primește și afișează fiecare porție pe măsură ce sosește.

**Cerințe:**

- Serverul trebuie să folosească un răspuns streamabil (ex: `StreamingResponse` în FastAPI).
- Clientul trebuie să proceseze răspunsul ca un stream (`stream=True` în requests).
- Content-Type este de obicei `text/event-stream` sau `application/octet-stream`.

#### Java

**Server (Java, folosind Spring Boot și Server-Sent Events):**

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

**Client (Java, folosind Spring WebFlux WebClient):**

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

**Note despre implementarea în Java:**

- Folosește stiva reactivă Spring Boot cu `Flux` pentru streaming
- `ServerSentEvent` oferă streaming structurat de evenimente cu tipuri de evenimente
- `WebClient` cu `bodyToFlux()` permite consumul reactiv al stream-ului
- `delayElements()` simulează timpul de procesare între evenimente
- Evenimentele pot avea tipuri (`info`, `result`) pentru o mai bună gestionare de către client

### Comparație: Streaming Clasic vs Streaming MCP

Diferențele dintre modul în care funcționează streamingul în mod "clasic" versus streamingul în MCP pot fi reprezentate astfel:

| Caracteristică           | Streaming HTTP Clasic       | Streaming MCP (Notificări)      |
|-------------------------|-----------------------------|---------------------------------|
| Răspuns principal        | Fragmentat                  | Unic, la final                  |
| Actualizări de progres   | Trimise ca bucăți de date   | Trimise ca notificări           |
| Cerințe client           | Trebuie să proceseze stream | Trebuie să implementeze handler mesaje |
| Caz de utilizare         | Fișiere mari, fluxuri token AI | Progres, loguri, feedback în timp real |

### Diferențe cheie observate

În plus, iată câteva diferențe cheie:

- **Modelul de comunicație:**
  - Streaming HTTP clasic: Folosește codare simplă de transfer fragmentat pentru a trimite date în bucăți
  - Streaming MCP: Folosește un sistem structurat de notificări cu protocol JSON-RPC

- **Formatul mesajelor:**
  - HTTP clasic: Fragmente text simple cu newline-uri
  - MCP: Obiecte structurate LoggingMessageNotification cu metadate

- **Implementarea clientului:**
  - HTTP clasic: Client simplu care procesează răspunsuri streamabile
  - MCP: Client mai sofisticat cu handler de mesaje pentru procesarea diferitelor tipuri de mesaje

- **Actualizări de progres:**
  - HTTP clasic: Progresul face parte din fluxul principal de răspuns
  - MCP: Progresul este trimis prin mesaje separate de notificare în timp ce răspunsul principal vine la final

### Recomandări

Există câteva lucruri pe care le recomandăm când vine vorba de alegerea între implementarea streamingului clasic (ca un endpoint pe care ți l-am arătat mai sus folosind `/stream`) versus alegerea streamingului prin MCP.

- **Pentru nevoi simple de streaming:** Streamingul HTTP clasic este mai simplu de implementat și suficient pentru nevoi de bază.

- **Pentru aplicații complexe, interactive:** Streamingul MCP oferă o abordare mai structurată cu metadate bogate și separație între notificări și rezultate finale.

- **Pentru aplicații AI:** Sistemul de notificări MCP este foarte util pentru sarcini AI de lungă durată unde dorești să ții utilizatorii informați despre progres.

## Streaming în MCP

Bine, deci ai văzut deja câteva recomandări și comparații până acum despre diferența dintre streamingul clasic și streamingul în MCP. Hai să intrăm în detaliu despre cum poți valorifica exact streamingul în MCP.

Înțelegerea modului în care streamingul funcționează în cadrul MCP este esențială pentru construirea de aplicații responsive care oferă feedback în timp real utilizatorilor în timpul unor operațiuni pe termen lung.

În MCP, streamingul nu este despre trimiterea răspunsului principal în bucăți, ci despre trimiterea de **notificări** către client în timp ce un instrument procesează o cerere. Aceste notificări pot include actualizări de progres, log-uri sau alte evenimente.

### Cum funcționează

Rezultatul principal este în continuare trimis ca un răspuns unic. Totuși, notificările pot fi trimise ca mesaje separate în timpul procesării și astfel să actualizeze clientul în timp real. Clientul trebuie să poată gestiona și afișa aceste notificări.

## Ce este o Notificare?

Am spus „Notificare”, ce înseamnă asta în contextul MCP?

O notificare este un mesaj trimis de la server către client pentru a informa despre progres, stare sau alte evenimente în timpul unei operațiuni de durată. Notificările sporesc transparența și experiența utilizatorului.

De exemplu, un client ar trebui să trimită o notificare odată ce handshake-ul inițial cu serverul a fost realizat.

O notificare arată astfel ca mesaj JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notificările aparțin unui subiect în MCP denumit ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Notificare de depreciere:** candidatul la lansare pentru specificația MCP `2026-07-28` marchează primitivele Logging ca depreciate în favoarea `stderr` pentru transporturile stdio și OpenTelemetry pentru observabilitate structurată. Logging-ul continuă să funcționeze în `2025-11-25` și pentru cel puțin un an după orice depreciere formală. Vezi [Ce se schimbă în MCP: Candidatul la lansare 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Pentru a face logging-ul să funcționeze, serverul trebuie să-l activeze ca funcționalitate/capabilitate astfel:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> În funcție de SDK-ul folosit, logging-ul poate fi activat implicit, sau poate fi nevoie să-l activezi explicit în configurația serverului tău.

Există diferite tipuri de notificări:

| Nivel     | Descriere                     | Exemplu de utilizare             |
|-----------|-------------------------------|---------------------------------|
| debug     | Informații detaliate de depanare | Puncte de intrare/ieșire funcție |
| info      | Mesaje generale informaționale | Actualizări de progres ale operațiunii |
| notice    | Evenimente normale dar semnificative | Schimbări de configurație      |
| warning   | Condiții de avertizare          | Utilizarea funcției depreciate   |
| error     | Condiții de eroare             | Eșecuri ale operațiunii         |
| critical  | Condiții critice               | Defecțiuni ale componentelor sistemului |
| alert     | Trebuie luate măsuri imediat   | Detectare de corupere a datelor  |
| emergency | Sistem inutilizabil            | Eșec complet al sistemului       |

## Implementarea Notificărilor în MCP

Pentru a implementa notificări în MCP, trebuie să configurezi atât partea de server cât și partea de client pentru a gestiona actualizările în timp real. Acest lucru permite aplicației tale să ofere feedback imediat utilizatorilor în timpul operațiunilor de durată.

### Partea de server: Trimiterea notificărilor

Să începem cu partea de server. În MCP, definești unelte care pot trimite notificări în timp ce procesează cererile. Serverul folosește obiectul context (de obicei `ctx`) pentru a trimite mesaje clientului.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

În exemplul anterior, unealta `process_files` trimite trei notificări clientului pe măsură ce procesează fiecare fișier. Metoda `ctx.info()` este folosită pentru a trimite mesaje informaționale.

În plus, pentru a activa notificările, asigură-te că serverul tău folosește un transport streaming (ca `streamable-http`) și clientul tău implementează un handler de mesaje pentru a procesa notificările. Iată cum poți configura serverul să utilizeze transportul `streamable-http`:

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

În acest exemplu .NET, unealta `ProcessFiles` este decorată cu atributul `Tool` și trimite trei notificări clientului pe măsură ce procesează fiecare fișier. Metoda `ctx.Info()` este folosită pentru a trimite mesaje informaționale.

Pentru a activa notificările în serverul tău MCP .NET, asigură-te că folosești un transport streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Partea de client: Primirea notificărilor

Clientul trebuie să implementeze un handler de mesaje pentru a procesa și afișa notificările pe măsură ce sosesc.

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

În codul precedent, funcția `message_handler` verifică dacă mesajul primit este o notificare. Dacă este, afișează notificarea; altfel, îl procesează ca mesaj obișnuit de la server. De asemenea, observă cum `ClientSession` este inițializată cu `message_handler` pentru a gestiona notificările primite.

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

În acest exemplu .NET, funcția `MessageHandler` verifică dacă mesajul primit este o notificare. Dacă este, afișează notificarea; altfel, îl procesează ca mesaj obișnuit de la server. `ClientSession` este inițializată cu handlerul de mesaje prin `ClientSessionOptions`.

Pentru a activa notificările, asigură-te că serverul tău folosește un transport streaming (ca `streamable-http`) și clientul tău implementează un handler de mesaje pentru a procesa notificările.

## Notificări de progres și scenarii

Această secțiune explică conceptul de notificări de progres în MCP, de ce sunt importante și cum să le implementezi folosind Streamable HTTP. Vei găsi și o sarcină practică pentru a-ți consolida înțelegerea.

Notificările de progres sunt mesaje în timp real trimise de la server către client în timpul operațiunilor de durată. În loc să aștepte ca procesul să se termine complet, serverul ține clientul la curent cu starea curentă. Acest lucru îmbunătățește transparența, experiența utilizatorului și face depanarea mai ușoară.

**Exemplu:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### De ce să folosești notificări de progres?

Notificările de progres sunt esențiale din mai multe motive:

- **Experiență mai bună a utilizatorului:** Utilizatorii văd actualizări pe măsură ce munca progresează, nu doar la final.
- **Feedback în timp real:** Clienții pot afișa bare de progres sau log-uri, făcând aplicația să pară mai receptivă.
- **Depanare și monitorizare mai ușoară:** Dezvoltatorii și utilizatorii pot vedea unde un proces este lent sau blocat.

### Cum să implementezi notificările de progres

Iată cum poți implementa notificările de progres în MCP:

- **Pe server:** Folosește `ctx.info()` sau `ctx.log()` pentru a trimite notificări pe măsură ce fiecare element este procesat. Acestea trimit un mesaj către client înainte ca rezultatul principal să fie gata.
- **Pe client:** Implementează un handler de mesaje care ascultă și afișează notificările pe măsură ce sosesc. Acest handler face distincția între notificări și rezultatul final.

**Exemplu de server:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Exemplu client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considerații de securitate

Securitatea ar trebui să fie o prioritate principală atunci când implementați orice server, în special atunci când utilizați transporturi bazate pe HTTP, cum ar fi Streamable HTTP în MCP.

Atunci când implementați servere MCP cu transporturi bazate pe HTTP, securitatea devine o preocupare primordială care necesită atenție atentă la multiple vectori de atac și mecanisme de protecție.

### Prezentare generală

Securitatea este critică când expuneți servere MCP prin HTTP. Streamable HTTP introduce noi suprafețe de atac și necesită o configurare atentă.

Iată câteva considerații cheie de securitate:

- **Validarea antetului Origin**: Validați întotdeauna antetul `Origin` pentru a preveni atacurile de tip DNS rebinding.
- **Legarea la localhost**: Pentru dezvoltare locală, legați serverele de `localhost` pentru a evita expunerea lor pe internetul public.
- **Autentificare**: Implementați autentificarea (de ex., chei API, OAuth) pentru implementările în producție.
- **CORS**: Configurați politicile Cross-Origin Resource Sharing (CORS) pentru a restrânge accesul.
- **HTTPS**: Utilizați HTTPS în producție pentru a cripta traficul.

### Cele mai bune practici

De asemenea, iată câteva cele mai bune practici de urmat când implementați securitatea în serverul vostru de streaming MCP:

- Nu aveți încredere niciodată în cererile primite fără validare.
- Înregistrați și monitorizați toate accesările și erorile.
- Actualizați regulat dependențele pentru a remedia vulnerabilitățile de securitate.

### Provocări

Veți întâmpina unele provocări la implementarea securității în serverele de streaming MCP:

- Echilibrarea securității cu ușurința dezvoltării
- Asigurarea compatibilității cu diverse medii client


## Trecerea de la SSE la Streamable HTTP

Pentru aplicațiile care folosesc în prezent Server-Sent Events (SSE), migrarea la Streamable HTTP oferă capabilități îmbunătățite și o sustenabilitate mai bună pe termen lung pentru implementările MCP.

### De ce să faceți upgrade?

Există două motive convingătoare pentru a face upgrade de la SSE la Streamable HTTP:

- Streamable HTTP oferă scalabilitate mai bună, compatibilitate și suport mai bogat pentru notificări decât SSE.
- Este transportul recomandat pentru noile aplicații MCP.

### Pași pentru migrare

Iată cum puteți migra de la SSE la Streamable HTTP în aplicațiile voastre MCP:

- **Actualizați codul serverului** pentru a folosi `transport="streamable-http"` în `mcp.run()`.
- **Actualizați codul clientului** pentru a folosi `streamablehttp_client` în loc de clientul SSE.
- **Implementați un handler de mesaje** în client pentru a procesa notificările.
- **Testați compatibilitatea** cu uneltele și fluxurile de lucru existente.

### Menținerea compatibilității

Se recomandă să mențineți compatibilitatea cu clienții SSE existenți pe durata procesului de migrare. Iată câteva strategii:

- Puteți suporta atât SSE, cât și Streamable HTTP rulând ambele transporturi pe endpoint-uri diferite.
- Migrați gradual clienții către noul transport.

### Provocări

Asigurați-vă că abordați următoarele provocări în timpul migrării:

- Asigurarea că toți clienții sunt actualizați
- Gestionarea diferențelor în livrarea notificărilor

### Exercițiu: Construiți propria aplicație MCP de streaming

**Scenariu:**
Construiți un server și un client MCP unde serverul procesează o listă de elemente (de exemplu, fișiere sau documente) și trimite o notificare pentru fiecare element procesat. Clientul ar trebui să afișeze fiecare notificare pe măsură ce aceasta soseste.

**Pași:**

1. Implementați un instrument server care procesează o listă și trimite notificări pentru fiecare element.
2. Implementați un client cu un handler de mesaje pentru a afișa notificările în timp real.
3. Testați implementarea rulând atât serverul, cât și clientul, și observați notificările.

[Soluție](./solution/README.md)

## Lecturi suplimentare & Ce urmează?

Pentru a continua călătoria cu streaming MCP și a vă extinde cunoștințele, această secțiune oferă resurse suplimentare și pași sugerați pentru construirea unor aplicații mai avansate.

### Lecturi suplimentare

- [Microsoft: Introducere în HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS în ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Cereri de streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ce urmează?

- Încercați să construiți unelte MCP mai avansate care folosesc streaming pentru analize în timp real, chat sau editare colaborativă.
- Explorați integrarea streaming MCP cu framework-uri frontend (React, Vue etc.) pentru actualizări live ale UI.
- Următorul: [Utilizarea AI Toolkit pentru VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->