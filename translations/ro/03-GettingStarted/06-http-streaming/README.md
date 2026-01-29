# Streaming HTTPS cu Protocolul Model Context (MCP)

Acest capitol oferă un ghid cuprinzător pentru implementarea streaming-ului securizat, scalabil și în timp real folosind Protocolul Model Context (MCP) prin HTTPS. Acoperă motivația pentru streaming, mecanismele de transport disponibile, cum să implementezi HTTP streamabil în MCP, cele mai bune practici de securitate, migrarea de la SSE și sfaturi practice pentru construirea propriilor aplicații MCP de streaming.

## Mecanisme de Transport și Streaming în MCP

Această secțiune explorează diferitele mecanisme de transport disponibile în MCP și rolul lor în activarea capabilităților de streaming pentru comunicarea în timp real între clienți și servere.

### Ce este un Mecanism de Transport?

Un mecanism de transport definește modul în care datele sunt schimbate între client și server. MCP suportă mai multe tipuri de transport pentru a se potrivi diferitelor medii și cerințe:

- **stdio**: Intrare/ieșire standard, potrivit pentru unelte locale și bazate pe CLI. Simplu, dar nepotrivit pentru web sau cloud.
- **SSE (Server-Sent Events)**: Permite serverelor să trimită actualizări în timp real către clienți prin HTTP. Bun pentru interfețe web, dar limitat în scalabilitate și flexibilitate.
- **HTTP streamabil**: Transport modern bazat pe HTTP pentru streaming, care suportă notificări și o scalabilitate mai bună. Recomandat pentru majoritatea scenariilor de producție și cloud.

### Tabel Comparativ

Consultați tabelul comparativ de mai jos pentru a înțelege diferențele dintre aceste mecanisme de transport:

| Transport         | Actualizări în timp real | Streaming | Scalabilitate | Caz de utilizare         |
|-------------------|--------------------------|-----------|---------------|--------------------------|
| stdio             | Nu                       | Nu        | Scăzut        | Unelte CLI locale        |
| SSE               | Da                       | Da        | Mediu         | Web, actualizări în timp real |
| HTTP streamabil   | Da                       | Da        | Ridicat       | Cloud, multi-client      |

> **Sfat:** Alegerea transportului potrivit influențează performanța, scalabilitatea și experiența utilizatorului. **HTTP streamabil** este recomandat pentru aplicații moderne, scalabile și pregătite pentru cloud.

Observați transporturile stdio și SSE prezentate în capitolele anterioare și cum HTTP streamabil este transportul acoperit în acest capitol.

## Streaming: Concepte și Motivație

Înțelegerea conceptelor fundamentale și a motivațiilor din spatele streaming-ului este esențială pentru implementarea unor sisteme eficiente de comunicare în timp real.

**Streaming-ul** este o tehnică în programarea rețelelor care permite trimiterea și primirea datelor în bucăți mici și gestionabile sau ca o secvență de evenimente, în loc să aștepți ca un răspuns complet să fie gata. Acest lucru este util în special pentru:

- Fișiere sau seturi de date mari.
- Actualizări în timp real (de exemplu, chat, bare de progres).
- Calculuri de lungă durată unde dorești să informezi utilizatorul.

Iată ce trebuie să știi despre streaming la un nivel înalt:

- Datele sunt livrate progresiv, nu toate deodată.
- Clientul poate procesa datele pe măsură ce sosesc.
- Reduce latența percepută și îmbunătățește experiența utilizatorului.

### De ce să folosești streaming-ul?

Motivele pentru utilizarea streaming-ului sunt următoarele:

- Utilizatorii primesc feedback imediat, nu doar la final.
- Permite aplicații în timp real și interfețe responsive.
- Utilizare mai eficientă a resurselor de rețea și calcul.

### Exemplu Simplu: Server și Client HTTP Streaming

Iată un exemplu simplu despre cum poate fi implementat streaming-ul:

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

- Serverul transmite fiecare mesaj pe măsură ce este pregătit.
- Clientul primește și afișează fiecare bucățică pe măsură ce sosește.

**Cerințe:**

- Serverul trebuie să folosească un răspuns de tip streaming (de exemplu, `StreamingResponse` în FastAPI).
- Clientul trebuie să proceseze răspunsul ca un flux (`stream=True` în requests).
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

**Note despre Implementarea în Java:**

- Folosește stiva reactivă din Spring Boot cu `Flux` pentru streaming.
- `ServerSentEvent` oferă streaming structurat de evenimente cu tipuri de evenimente.
- `WebClient` cu `bodyToFlux()` permite consumul reactiv al fluxului.
- `delayElements()` simulează timpul de procesare între evenimente.
- Evenimentele pot avea tipuri (`info`, `result`) pentru o gestionare mai bună pe partea clientului.

### Comparație: Streaming Clasic vs Streaming MCP

Diferențele dintre modul în care funcționează streaming-ul într-un mod "clasic" și modul în care funcționează în MCP pot fi descrise astfel:

| Caracteristică          | Streaming HTTP Clasic         | Streaming MCP (Notificări)         |
|-------------------------|-------------------------------|-------------------------------------|
| Răspuns principal       | Fragmentat                   | Unic, la final                     |
| Actualizări de progres  | Trimise ca bucăți de date     | Trimise ca notificări              |
| Cerințe client          | Trebuie să proceseze fluxul  | Trebuie să implementeze un handler de mesaje |
| Caz de utilizare        | Fișiere mari, fluxuri AI      | Progres, loguri, feedback în timp real |

### Diferențe Cheie Observate

Iată câteva diferențe cheie:

- **Model de Comunicare:**
  - Streaming HTTP clasic: Folosește codificare simplă de transfer fragmentat pentru a trimite date în bucăți.
  - Streaming MCP: Folosește un sistem structurat de notificări cu protocol JSON-RPC.

- **Formatul Mesajului:**
  - HTTP Clasic: Bucăți de text simplu cu linii noi.
  - MCP: Obiecte structurate `LoggingMessageNotification` cu metadate.

- **Implementarea Clientului:**
  - HTTP Clasic: Client simplu care procesează răspunsuri de streaming.
  - MCP: Client mai sofisticat cu un handler de mesaje pentru a procesa diferite tipuri de mesaje.

- **Actualizări de Progres:**
  - HTTP Clasic: Progresul face parte din fluxul principal de răspuns.
  - MCP: Progresul este trimis prin mesaje de notificare separate, în timp ce răspunsul principal vine la final.

### Recomandări

Iată câteva recomandări pentru alegerea între implementarea streaming-ului clasic (ca un endpoint pe care l-am arătat mai sus folosind `/stream`) și streaming-ul prin MCP:

- **Pentru nevoi simple de streaming:** Streaming-ul HTTP clasic este mai simplu de implementat și suficient pentru nevoi de bază.
- **Pentru aplicații complexe și interactive:** Streaming-ul MCP oferă o abordare mai structurată, cu metadate mai bogate și separarea între notificări și rezultate finale.
- **Pentru aplicații AI:** Sistemul de notificări al MCP este deosebit de util pentru sarcini AI de lungă durată, unde dorești să informezi utilizatorii despre progres.

## Streaming în MCP

Ok, ai văzut câteva recomandări și comparații până acum despre diferența dintre streaming-ul clasic și cel din MCP. Să intrăm în detaliu despre cum poți folosi streaming-ul în MCP.

În MCP, streaming-ul nu înseamnă trimiterea răspunsului principal în bucăți, ci trimiterea de **notificări** către client în timp ce un instrument procesează o cerere. Aceste notificări pot include actualizări de progres, loguri sau alte evenimente.

### Cum funcționează

Rezultatul principal este tot trimis ca un singur răspuns. Cu toate acestea, notificările pot fi trimise ca mesaje separate în timpul procesării, actualizând astfel clientul în timp real. Clientul trebuie să fie capabil să gestioneze și să afișeze aceste notificări.

## Ce este o Notificare?

Am menționat "Notificare", ce înseamnă asta în contextul MCP?

O notificare este un mesaj trimis de la server către client pentru a informa despre progres, stare sau alte evenimente în timpul unei operațiuni de lungă durată. Notificările îmbunătățesc transparența și experiența utilizatorului.

De exemplu, un client ar trebui să trimită o notificare odată ce strângerea de mână inițială cu serverul a fost realizată.

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

Pentru ca logarea să funcționeze, serverul trebuie să o activeze ca funcționalitate/capabilitate astfel:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> În funcție de SDK-ul utilizat, logarea poate fi activată implicit sau poate fi necesar să o activezi explicit în configurația serverului.

Există diferite tipuri de notificări:

| Nivel      | Descriere                     | Exemplu de utilizare            |
|------------|-------------------------------|----------------------------------|
| debug      | Informații detaliate de depanare | Puncte de intrare/ieșire funcții |
| info       | Mesaje generale informaționale | Actualizări de progres operațional |
| notice     | Evenimente normale dar semnificative | Schimbări de configurație       |
| warning    | Condiții de avertizare         | Utilizarea unei funcții depășite |
| error      | Condiții de eroare             | Eșecuri operaționale             |
| critical   | Condiții critice               | Eșecuri ale componentelor sistemului |
| alert      | Acțiune imediată necesară      | Detectarea coruperii datelor     |
| emergency  | Sistem inutilizabil            | Eșec complet al sistemului       |

## Implementarea Notificărilor în MCP

Pentru a implementa notificări în MCP, trebuie să configurezi atât partea de server, cât și cea de client pentru a gestiona actualizările în timp real. Acest lucru permite aplicației tale să ofere feedback imediat utilizatorilor în timpul operațiunilor de lungă durată.

### Partea de Server: Trimiterea Notificărilor

Să începem cu partea de server. În MCP, definești unelte care pot trimite notificări în timp ce procesează cereri. Serverul folosește obiectul context (de obicei `ctx`) pentru a trimite mesaje către client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

În exemplul precedent, instrumentul `process_files` trimite trei notificări către client pe măsură ce procesează fiecare fișier. Metoda `ctx.info()` este utilizată pentru a trimite mesaje informaționale.

De asemenea, pentru a activa notificările, asigură-te că serverul tău folosește un transport de tip streaming (cum ar fi `streamable-http`) și că clientul tău implementează un handler de mesaje pentru a procesa notificările. Iată cum poți configura serverul pentru a folosi transportul `streamable-http`:

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

În acest exemplu .NET, instrumentul `ProcessFiles` este decorat cu atributul `Tool` și trimite trei notificări către client pe măsură ce procesează fiecare fișier. Metoda `ctx.Info()` este utilizată pentru a trimite mesaje informaționale.

Pentru a activa notificările în serverul MCP .NET, asigură-te că folosești un transport de tip streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Partea de Client: Primirea Notificărilor

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

În codul precedent, funcția `message_handler` verifică dacă mesajul primit este o notificare. Dacă este, o afișează; altfel, îl procesează ca pe un mesaj obișnuit de la server. De asemenea, observă cum `ClientSession` este inițializat cu `message_handler` pentru a gestiona notificările primite.

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

În acest exemplu .NET, funcția `MessageHandler` verifică dacă mesajul primit este o notificare. Dacă este, o afișează; altfel, îl procesează ca pe un mesaj obișnuit de la server. `ClientSession` este inițializat cu handler-ul de mesaje prin `ClientSessionOptions`.

Pentru a activa notificările, asigură-te că serverul tău folosește un transport de tip streaming (cum ar fi `streamable-http`) și că clientul tău implementează un handler de mesaje pentru a procesa notificările.

## Notificări de Progres și Scenarii

Această secțiune explică conceptul de notificări de progres în MCP, de ce sunt importante și cum să le implementezi folosind HTTP streamabil. Vei găsi, de asemenea, un exercițiu practic pentru a-ți consolida înțelegerea.

Notificările de progres sunt mesaje în timp real trimise de la server către client în timpul operațiunilor de lungă durată. În loc să aștepte finalizarea întregului proces, serverul ține clientul la curent cu starea curentă. Acest lucru îmbunătățește transparența, experiența utilizatorului și facilitează depanarea.

**Exemplu:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### De ce să folosești notificări de progres?

Notificările de progres sunt esențiale din mai multe motive:

- **Experiență mai bună pentru utilizator:** Utilizatorii văd actualizări pe măsură ce munca progresează, nu doar la final.
- **Feedback în timp real:** Clienții pot afișa bare de progres sau loguri, făcând aplicația să pară mai receptivă.
- **Depanare și monitorizare mai ușoară:** Dezvoltatorii și utilizatorii pot vedea unde un proces ar putea fi lent sau blocat.

### Cum să implementezi notificări de progres

Iată cum poți implementa notificări de progres în MCP:

- **Pe server:** Folosește `ctx.info()` sau `ctx.log()` pentru a trimite notificări pe măsură ce fiecare element este procesat. Acest lucru trimite un mesaj către client înainte ca rezultatul principal să fie gata.
- **Pe client:** Implementează un handler de mesaje care ascultă și afișează notificările pe măsură ce sosesc. Acest handler distinge între notificări și rezultatul final.

**Exemplu Server:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Exemplu Client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Considerații de Securitate

Când implementezi servere MCP cu transporturi bazate pe HTTP, securitatea devine o preocupare majoră care necesită atenție la multiple vectori de atac și mecanisme de protecție.

### Prezentare Generală

Securitatea este esențială atunci când expui servere MCP prin HTTP. HTTP streamabil introduce noi suprafețe de atac și necesită o configurare atentă.

### Puncte Cheie

- **Validarea Header-ului Origin:** Validează întotdeauna header-ul `Origin` pentru a preveni atacurile de tip DNS rebinding.
- **Legare la Localhost:** Pentru dezvoltare locală, leagă serverele de `localhost` pentru a evita expunerea lor pe internet.
- **Autentificare:** Implementează autentificare (de exemplu, chei API, OAuth) pentru implementările de producție.
- **CORS:** Configurează politici Cross-Origin Resource Sharing (CORS) pentru a restricționa accesul.
- **HTTPS:** Folosește HTTPS în producție pentru a cripta traficul.

### Cele Mai Bune Practici

- Nu avea încredere în cererile primite fără validare.
- Loghează și monitorizează toate accesările și erorile.
- Actualizează regulat dependențele pentru a remedia vulnerabilitățile de securitate.

### Provocări

- Echilibrarea securității cu ușurința dezvoltării.
- Asigurarea compatibilității cu diverse medii client.

## Actualizarea de la SSE la HTTP Streamabil

Pentru aplicațiile care folosesc în prezent Server-Sent Events (SSE), migrarea la HTTP streamabil oferă capabilități îmbunătățite și o sustenabilitate mai bună pe termen lung pentru implementările MCP.

### De ce să faci upgrade?
Există două motive convingătoare pentru a face upgrade de la SSE la Streamable HTTP:

- Streamable HTTP oferă o scalabilitate mai bună, compatibilitate mai mare și suport mai bogat pentru notificări decât SSE.
- Este transportul recomandat pentru noile aplicații MCP.

### Pași de Migrare

Iată cum poți migra de la SSE la Streamable HTTP în aplicațiile tale MCP:

- **Actualizează codul serverului** pentru a utiliza `transport="streamable-http"` în `mcp.run()`.
- **Actualizează codul clientului** pentru a utiliza `streamablehttp_client` în loc de clientul SSE.
- **Implementează un handler de mesaje** în client pentru a procesa notificările.
- **Testează compatibilitatea** cu uneltele și fluxurile de lucru existente.

### Menținerea Compatibilității

Se recomandă menținerea compatibilității cu clienții SSE existenți în timpul procesului de migrare. Iată câteva strategii:

- Poți suporta atât SSE, cât și Streamable HTTP, rulând ambele transporturi pe endpoint-uri diferite.
- Migrează treptat clienții către noul transport.

### Provocări

Asigură-te că abordezi următoarele provocări în timpul migrării:

- Actualizarea tuturor clienților
- Gestionarea diferențelor în livrarea notificărilor

## Considerații de Securitate

Securitatea ar trebui să fie o prioritate principală atunci când implementezi orice server, mai ales când utilizezi transporturi bazate pe HTTP, cum ar fi Streamable HTTP în MCP.

Când implementezi servere MCP cu transporturi bazate pe HTTP, securitatea devine o preocupare esențială care necesită atenție la multiple vectori de atac și mecanisme de protecție.

### Prezentare Generală

Securitatea este esențială atunci când expui servere MCP prin HTTP. Streamable HTTP introduce noi suprafețe de atac și necesită o configurare atentă.

Iată câteva considerații cheie de securitate:

- **Validarea Header-ului Origin**: Validează întotdeauna header-ul `Origin` pentru a preveni atacurile de tip DNS rebinding.
- **Binding pe Localhost**: Pentru dezvoltarea locală, configurează serverele să fie legate de `localhost` pentru a evita expunerea lor pe internetul public.
- **Autentificare**: Implementează autentificare (de exemplu, chei API, OAuth) pentru implementările în producție.
- **CORS**: Configurează politicile Cross-Origin Resource Sharing (CORS) pentru a restricționa accesul.
- **HTTPS**: Utilizează HTTPS în producție pentru a cripta traficul.

### Cele Mai Bune Practici

În plus, iată câteva bune practici de urmat atunci când implementezi securitatea în serverul tău MCP de streaming:

- Nu avea încredere în cererile primite fără validare.
- Loghează și monitorizează toate accesările și erorile.
- Actualizează regulat dependențele pentru a remedia vulnerabilitățile de securitate.

### Provocări

Vei întâmpina unele provocări atunci când implementezi securitatea în serverele MCP de streaming:

- Echilibrarea securității cu ușurința dezvoltării
- Asigurarea compatibilității cu diverse medii de client

### Sarcină: Construiește-ți Propria Aplicație MCP de Streaming

**Scenariu:**
Construiește un server și un client MCP în care serverul procesează o listă de elemente (de exemplu, fișiere sau documente) și trimite o notificare pentru fiecare element procesat. Clientul ar trebui să afișeze fiecare notificare pe măsură ce aceasta sosește.

**Pași:**

1. Implementează un instrument server care procesează o listă și trimite notificări pentru fiecare element.
2. Implementează un client cu un handler de mesaje pentru a afișa notificările în timp real.
3. Testează implementarea rulând atât serverul, cât și clientul, și observă notificările.

[Solution](./solution/README.md)

## Lecturi Suplimentare & Ce Urmează?

Pentru a-ți continua călătoria cu streaming-ul MCP și pentru a-ți extinde cunoștințele, această secțiune oferă resurse suplimentare și pași sugerați pentru construirea unor aplicații mai avansate.

### Lecturi Suplimentare

- [Microsoft: Introducere în HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS în ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Cereri de Streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ce Urmează?

- Încearcă să construiești unelte MCP mai avansate care utilizează streaming pentru analize în timp real, chat sau editare colaborativă.
- Explorează integrarea streaming-ului MCP cu framework-uri frontend (React, Vue, etc.) pentru actualizări live ale interfeței.
- Următorul pas: [Utilizarea AI Toolkit pentru VSCode](../07-aitk/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.