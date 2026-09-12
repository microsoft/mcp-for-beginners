# Streaming HTTPS cu Protocolul Contextului Modelului (MCP)

Acest capitol oferă un ghid cuprinzător pentru implementarea streaming-ului sigur, scalabil și în timp real cu Protocolul Contextului Modelului (MCP) folosind HTTPS. Acoperă motivația pentru streaming, mecanismele de transport disponibile, modul de implementare a HTTP-ului transmitibil în MCP, cele mai bune practici de securitate, migrarea de la SSE și îndrumări practice pentru construirea propriilor aplicații MCP cu streaming. 

> [!WARNING]
> Exemplele de implementare din această lecție vizează **Specificația MCP
> `2025-11-25`** și demonstrează handshake-ul tradițional `initialize`,
> `Mcp-Session-Id`, fluxul de evenimente GET și modelul de reluare. MCP `2026-07-28`
> elimină aceste funcționalități. Cererile de HTTP transmitibil actuale sunt cereri POST autonome
> cu antetele `MCP-Protocol-Version` și `Mcp-Method`, plus `Mcp-Name` unde este necesar. Vezi
> [Ce s-a schimbat în MCP: Specificația 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> înainte de a folosi aceste exemple într-o implementare nouă.


## Mecanisme de Transport și Streaming în MCP

Această secțiune explorează diferitele mecanisme de transport disponibile în MCP și rolul lor în facilitarea capabilităților de streaming pentru comunicarea în timp real între clienți și servere.

### Ce este un Mecanism de Transport?

Un mecanism de transport definește modul în care datele sunt schimbate între client și server. MCP suportă mai multe tipuri de transport pentru a se adapta la diferite medii și cerințe:

- **stdio**: Intrare/ieșire standard, potrivit pentru unelte locale și bazate pe CLI. Simplu, dar nepotrivit pentru web sau cloud.
- **HTTP+SSE**: Transportul de la distanță tradițional, depreciat în MCP `2025-03-26`
    și înlocuit cu Streamable HTTP. Nu îl folosi pentru implementări noi.
- **Streamable HTTP**: Transport modern bazat pe HTTP pentru streaming, suportând notificări și scalabilitate mai bună. Recomandat pentru majoritatea scenariilor de producție și cloud.

### Tabel de Comparare

Vezi tabelul de comparație de mai jos pentru a înțelege diferențele dintre aceste mecanisme de transport:

| Transport | Stare | Notificări | Utilizare tipică |
|---|---|---|---|
| stdio | Curent | Da | Procese locale |
| HTTP+SSE | Depreciat | Da | Implementări tradiționale la distanță |
| Streamable HTTP | Curent | Da | Servere la distanță și cloud |

> **Sfat:** Alegerea mecanismului potrivit de transport influențează performanța, scalabilitatea și experiența utilizatorului. **Streamable HTTP** este recomandat pentru aplicații moderne, scalabile și pregătite pentru cloud.

Transporturile standard sunt stdio și Streamable HTTP. HTTP+SSE apare doar în
exemple mai vechi.

## Streaming: Concepte și Motivație

Înțelegerea conceptelor și motivațiilor fundamentale din spatele streaming-ului este esențială pentru implementarea unor sisteme eficiente de comunicare în timp real.

**Streaming-ul** este o tehnică în programarea rețelelor care permite trimiterea și primirea datelor în bucăți mici, gestionabile sau sub forma unei secvențe de evenimente, în loc să se aștepte ca întregul răspuns să fie gata. Acesta este deosebit de util pentru:

- Fișiere mari sau seturi de date mari.
- Actualizări în timp real (de ex., chat, bare de progres).
- Calculuri de durată lungă unde dorești să ții utilizatorul informat.

Iată ce trebuie să știi despre streaming la un nivel general:

- Datele sunt livrate progresiv, nu toate odată.
- Clientul poate procesa datele pe măsură ce sosesc.
- Reduce latența percepută și îmbunătățește experiența utilizatorului.

### De ce să folosești streaming?

Motivele pentru folosirea streaming-ului sunt următoarele:

- Utilizatorii primesc feedback imediat, nu doar la final
- Permite aplicații în timp real și interfețe reactive
- Utilizare mai eficientă a resurselor de rețea și calcul

### Exemplu Simplu: Server și Client HTTP pentru Streaming

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

Acest exemplu demonstrează un server care trimite o serie de mesaje clientului pe măsură ce devin disponibile, în loc să aștepte până când toate mesajele sunt gata.

**Cum funcționează:**

- Serverul oferă fiecare mesaj pe măsură ce este gata.
- Clientul primește și afișează fiecare bucată pe măsură ce soseste.

**Cerințe:**

- Serverul trebuie să folosească un răspuns de tip streaming (de ex., `StreamingResponse` în FastAPI).
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

**Note despre implementarea Java:**

- Folosește stiva reactivă Spring Boot cu `Flux` pentru streaming
- `ServerSentEvent` oferă streaming structurat de evenimente cu tipuri de evenimente
- `WebClient` cu `bodyToFlux()` permite consumul reactiv al fluxului
- `delayElements()` simulează timpul de procesare între evenimente
- Evenimentele pot avea tipuri (`info`, `result`) pentru o mai bună gestionare de către client

### Comparație: Streaming Clasic vs Streaming MCP

Diferențele dintre modul în care funcționează streaming-ul în mod „clasic” și modul în care funcționează în MCP pot fi ilustrate astfel:

| Caracteristică            | Streaming HTTP Clasic           | Streaming MCP (Notificări)        |
|--------------------------|--------------------------------|----------------------------------|
| Răspuns principal         | Pe bucăți                      | Unic, la final                    |
| Actualizări de progres    | Trimise ca bucăți de date      | Trimise ca notificări             |
| Cerințe client            | Trebuie să proceseze stream-ul | Trebuie să implementeze un handler de mesaje |
| Caz de utilizare          | Fișiere mari, fluxuri de tokeni AI | Progres, loguri, feedback în timp real |

### Diferențe Cheie Observate

În plus, iată câteva diferențe cheie:

- **Model de comunicare:**
  - Streaming HTTP clasic: Folosește codificare simplă transfer chunked pentru a trimite date pe bucăți
  - Streaming MCP: Folosește un sistem structurat de notificări cu protocol JSON-RPC

- **Formatul mesajului:**
  - HTTP clasic: Bucăți de text simplu cu newline-uri
  - MCP: Obiecte structurate LoggingMessageNotification cu metadate

- **Implementarea clientului:**
  - HTTP clasic: Client simplu care procesează răspunsuri streaming
  - MCP: Client mai sofisticat cu un handler de mesaje pentru a procesa diferite tipuri de mesaje

- **Actualizări de progres:**
  - HTTP clasic: Progresul face parte din fluxul principal de răspuns
  - MCP: Progresul este trimis prin mesaje separate de notificare în timp ce răspunsul principal vine la final

### Recomandări

Există câteva lucruri pe care le recomandăm când vine vorba de alegerea între implementarea streaming-ului clasic (ca un punct final pe care l-am arătat mai sus folosind `/stream`) versus alegerea streaming-ului prin MCP.

- **Pentru nevoi simple de streaming:** Streaming-ul HTTP clasic este mai simplu de implementat și suficient pentru nevoi de streaming de bază.


- **Pentru aplicații complexe și interactive:** streamingul MCP oferă o abordare mai structurată cu metadate mai bogate și separarea între notificări și rezultate finale.

- **Pentru aplicații AI:** sistemul de notificări MCP este deosebit de util pentru sarcini AI care rulează pe termen lung, unde doriți să țineți utilizatorii informați despre progres.

## Streaming în MCP

Ok, așadar ai văzut câteva recomandări și comparații până acum despre diferența dintre streamingul clasic și streamingul în MCP. Haide să analizăm în detaliu exact cum poți utiliza streamingul în MCP.

Înțelegerea modului în care funcționează streamingul în cadrul MCP este esențială pentru construirea unor aplicații responsabile care oferă feedback în timp real utilizatorilor în timpul operațiunilor pe termen lung.

În MCP, streamingul nu constă în trimiterea răspunsului principal în bucăți, ci în trimiterea **notificărilor** către client în timp ce un instrument procesează o cerere. Aceste notificări pot include actualizări de progres, jurnale sau alte evenimente.

### Cum funcționează

Rezultatul principal este totuși trimis ca un singur răspuns. Totuși, notificările pot fi trimise ca mesaje separate în timpul procesării și astfel actualizează clientul în timp real. Clientul trebuie să poată gestiona și afișa aceste notificări.

### Exercițiu opțional: conectare la un server MCP găzduit

Poți folosi Streamable HTTP și fără să rulezi un server local. Acest exemplu
se conectează la [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
descoperă instrumentele sale și caută documentația MCP publică folosind același
SDK Python ca [clientul local](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Endpoint-ul anonim al Parallel nu necesită cont sau cheie API. Accesul gratuit este
limitat ca rată. Rularea acestui script trimite interogările de căutare, obiectivul și un
identificator de sesiune aleatoriu către Parallel. Serviciul oferă, de asemenea, `web_fetch`,
care trimite URL-urile solicitate și orice context furnizat către Parallel. Folosește informații
publice pentru acest exercițiu; vezi [termenii](https://parallel.ai/customer-terms)
și [politica de confidențialitate](https://parallel.ai/privacy-policy).

Având Python 3.10 sau o versiune mai nouă și un mediu virtual activat, instalează SDK-ul:

```sh
python -m pip install "mcp>=1.10,<2"
```

Salvează asta ca `hosted_search.py` și rulează `python hosted_search.py`:

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

Așteaptă-te să includă descoperirea `web_search` și `web_fetch`, urmată de un răspuns
la căutare conținând URL-uri sursă și extrase. Rezultatele pot varia sau pot fi goale.
Scriptul verifică `isError` deoarece un instrument poate eșua chiar dacă cererea HTTP
reușește. Dacă accesul este limitat ca rată, așteaptă înainte de a încerca din nou. Refolosește același
`session_id` dacă extinzi scriptul cu apeluri de căutare sau fetch conexe.

Streamable HTTP permite răspunsuri JSON și SSE; acest server poate returna un
rezultat JSON complet fără notificări de progres. SDK-ul gestionează
transportul. Continuă cu exemplul local de mai jos pentru a învăța despre notificări.
Acest script opțional face o căutare explicită și închide conexiunea când
se termină. Dacă ulterior expui aceste instrumente unui agent, agentul ar putea să le invoce
în timpul muncii sale; tratează textele web obținute ca date neîncrezătoare.

## Ce este o Notificare?

Am spus „Notificare”, ce înseamnă asta în contextul MCP?

O notificare este un mesaj JSON-RPC care nu are un `id` și nu
primește un răspuns. MCP folosește notificările pentru progres, anulare și
alte evenimente unidirecționale.

În MCP `2025-11-25`, un client trimite `notifications/initialized` după
handshake-ul de inițializare. MCP `2026-07-28` nu are handshake de inițializare, deci
această notificare este comportament moștenit.

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

Logging-ul este o caracteristică care folosește notificări; notificările în sine sunt un
tip general de mesaj JSON-RPC.

> **Depreciat în MCP `2026-07-28`:** caracteristica Logging rămâne disponibilă
> pentru compatibilitate, dar poate fi eliminată în prima revizuire a specificației
> lansată pe sau după 28 iulie 2027. Implementările noi ar trebui să folosească
> `stderr` cu stdio sau OpenTelemetry pentru observabilitate structurată.

Pentru o implementare moștenită `2025-11-25`, serverul activează capabilitatea Logging
după cum urmează:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> În funcție de SDK-ul folosit, logging-ul poate fi activat implicit, sau este posibil să trebuiască să îl activezi explicit în configurația serverului tău.

Există diferite tipuri de notificări:

| Nivel     | Descriere                     | Caz de utilizare exemplu        |
|-----------|-------------------------------|---------------------------------|
| debug     | Informații detaliate de depanare | Puncte de intrare/ieșire funcții|
| info      | Mesaje informaționale generale | Actualizări de progres la operațiune |
| notice    | Evenimente normale, dar semnificative | Schimbări de configurare      |
| warning   | Condiții de avertizare         | Utilizarea caracteristicilor depreciate |
| error     | Condiții de eroare             | Eșecuri în operațiune           |
| critical  | Condiții critice               | Eșecuri ale componentelor sistemului |
| alert     | Acțiunea trebuie luată imediat | Corupere de date detectată     |
| emergency | Sistemul este inutilizabil     | Eșec complet al sistemului      |

## Implementarea Notificărilor în MCP

Pentru a implementa notificări în MCP, trebuie să configurezi atât partea de server, cât și partea de client pentru a gestiona actualizările în timp real. Aceasta permite aplicației tale să ofere feedback imediat utilizatorilor pe parcursul operațiunilor de durată lungă.

### Partea de server: Trimiterea notificărilor

Să începem cu partea de server. În MCP, definești instrumente care pot trimite notificări în timp ce procesează cereri. Serverul folosește obiectul context (de obicei `ctx`) pentru a trimite mesaje către client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

În exemplul precedent, instrumentul `process_files` trimite trei notificări către client pe măsură ce procesează fiecare fișier. Metoda `ctx.info()` este folosită pentru a trimite mesaje informaționale.

În plus, pentru a activa notificările, asigură-te că serverul tău folosește un transport de streaming (ca `streamable-http`) și clientul tău implementează un handler de mesaje pentru a procesa notificările. Iată cum poți configura serverul pentru a folosi transportul `streamable-http`:

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

În acest exemplu .NET, instrumentul `ProcessFiles` este decorat cu atributul `Tool` și trimite trei notificări către client pe măsură ce procesează fiecare fișier. Metoda `ctx.Info()` este folosită pentru a trimite mesaje informaționale.

Pentru a activa notificările în serverul tău MCP .NET, asigură-te că folosești un transport de streaming:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Partea de client: Primirea notificărilor

Clientul trebuie să implementeze un handler de mesaje pentru a procesa și afișa notificările pe măsură ce acestea sosesc.

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

În codul precedent, funcția `message_handler` verifică dacă mesajul primit este o notificare. Dacă da, afișează notificarea; altfel, o procesează ca mesaj obișnuit de server. Observă de asemenea cum `ClientSession` este inițializat cu `message_handler` pentru a trata notificările primite.

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


În acest exemplu .NET, funcția `MessageHandler` verifică dacă mesajul primit este o notificare. Dacă este, afișează notificarea; altfel, îl procesează ca un mesaj obișnuit de server. `ClientSession` este inițializat cu handlerul de mesaje prin intermediul `ClientSessionOptions`.

Pentru a activa notificările, asigură-te că serverul tău utilizează un transport de streaming (precum `streamable-http`) și că clientul tău implementează un handler de mesaje pentru a procesa notificările.

## Notificări de progres & Scenarii

Această secțiune explică conceptul de notificări de progres în MCP, de ce sunt importante și cum să le implementezi folosind Streamable HTTP. Vei găsi, de asemenea, o sarcină practică pentru a-ți consolida înțelegerea.

Notificările de progres sunt mesaje în timp real trimise de la server către client în timpul operațiunilor de lungă durată. În loc să se aștepte până la finalizarea întregului proces, serverul ține clientul la curent cu starea curentă. Aceasta îmbunătățește transparența, experiența utilizatorului și facilitează depanarea.

**Exemplu:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### De ce să folosești notificări de progres?

Notificările de progres sunt esențiale din mai multe motive:

- **Experiență mai bună pentru utilizator:** Utilizatorii văd actualizările pe măsură ce lucrul avansează, nu doar la final.
- **Feedback în timp real:** Clienții pot afișa bare de progres sau jurnale, făcând aplicația să pară receptivă.
- **Depanare și monitorizare mai ușoară:** Dezvoltatorii și utilizatorii pot vedea unde un proces este lent sau blocat.

### Cum să implementezi notificările de progres

Iată cum poți implementa notificări de progres în MCP:

- **Pe server:** Folosește `ctx.info()` sau `ctx.log()` pentru a trimite notificări pe măsură ce fiecare element este procesat. Aceasta trimite un mesaj clientului înainte ca rezultatul principal să fie gata.
- **Pe client:** Implementează un handler de mesaje care ascultă și afișează notificările pe măsură ce sosesc. Acest handler face distincția între notificări și rezultatul final.

**Exemplu server:**

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

Securitatea trebuie să fie o prioritate de top când implementezi orice server, în special când folosești transporturi bazate pe HTTP precum Streamable HTTP în MCP.

Când implementezi servere MCP cu transporturi bazate pe HTTP, securitatea devine o preocupare esențială ce necesită o atenție atentă asupra mai multor vectori de atac și mecanisme de protecție.

### Prezentare generală

Securitatea este critică când expui servere MCP prin HTTP. Streamable HTTP introduce noi suprafețe de atac și necesită o configurare atentă.

Iată câteva considerații cheie de securitate:

- **Validarea header-ului Origin**: Verifică întotdeauna header-ul `Origin` pentru a preveni atacurile de tip DNS rebinding.
- **Legarea pe localhost**: Pentru dezvoltarea locală, leagă serverele de `localhost` pentru a evita expunerea lor pe internetul public.
- **Autentificare**: Implementează autentificare (de ex. chei API, OAuth) pentru mediile de producție.
- **CORS**: Configurează politicile Cross-Origin Resource Sharing (CORS) pentru a restricționa accesul.
- **HTTPS**: Folosește HTTPS în producție pentru criptarea traficului.

### Cele mai bune practici

În plus, iată câteva bune practici de urmat când implementezi securitatea pe serverul tău MCP de streaming:

- Nu avea încredere în cererile primite fără validare.
- Înregistrează și monitorizează toate accesările și erorile.
- Actualizează regulat dependențele pentru a remedia vulnerabilitățile de securitate.

### Provocări

Vei întâmpina unele provocări la implementarea securității în serverele MCP de streaming:

- Echilibrarea securității cu ușurința dezvoltării
- Asigurarea compatibilității cu diverse medii de client


## Trecerea de la SSE la Streamable HTTP

Pentru aplicațiile care utilizează în prezent Server-Sent Events (SSE), migrarea către Streamable HTTP oferă capabilități îmbunătățite și o sustenabilitate mai bună pe termen lung pentru implementările tale MCP.

### De ce să faci upgrade?

Există două motive convingătoare pentru a face upgrade de la SSE la Streamable HTTP:

- Streamable HTTP oferă o scalabilitate mai bună, compatibilitate și suport mai bogat pentru notificări decât SSE.
- Este transportul recomandat pentru noile aplicații MCP.

### Pașii migrației

Iată cum poți migra de la SSE la Streamable HTTP în aplicațiile tale MCP:

- **Actualizează codul serverului** să folosească `transport="streamable-http"` în `mcp.run()`.
- **Actualizează codul clientului** să folosească `streamablehttp_client` în loc de clientul SSE.
- **Implementează un handler de mesaje** în client pentru a procesa notificările.
- **Testează compatibilitatea** cu uneltele și fluxurile de lucru existente.

### Menținerea compatibilității

Este recomandat să menții compatibilitatea cu clienții SSE existenți în timpul procesului de migrare. Iată câteva strategii:

- Poți susține atât SSE, cât și Streamable HTTP rulând ambele transporturi pe endpoint-uri diferite.
- Migrează treptat clienții la noul transport.

### Provocări

Asigură-te că abordezi următoarele provocări pe durata migrației:

- Asigurarea că toți clienții sunt actualizați
- Gestionarea diferențelor în livrarea notificărilor

### Sarcină: Construiește propria aplicație MCP de streaming

**Scenariu:**
Construiește un server și un client MCP în care serverul procesează o listă de elemente (de exemplu, fișiere sau documente) și trimite o notificare pentru fiecare element procesat. Clientul ar trebui să afișeze fiecare notificare pe măsură ce aceasta soseste.

**Pași:**

1. Implementează un instrument de server care procesează o listă și trimite notificări pentru fiecare element.
2. Implementează un client cu un handler de mesaje pentru a afișa notificările în timp real.
3. Testează implementarea rulând atât serverul, cât și clientul, și observă notificările.

[Soluție](./solution/README.md)

## Lecturi suplimentare & Ce urmează?

Pentru a-ți continua parcursul cu streaming MCP și a-ți extinde cunoștințele, această secțiune oferă resurse suplimentare și pași sugerați pentru a construi aplicații mai avansate.

### Lecturi suplimentare

- [Microsoft: Introducere în HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS în ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Cereri de streaming](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ce urmează?

- Încearcă să construiești instrumente MCP mai avansate care folosesc streaming pentru analize în timp real, chat sau editare colaborativă.
- Explorează integrarea streaming-ului MCP cu framework-uri frontend (React, Vue etc.) pentru actualizări UI live.
- Următorul: [Utilizarea AI Toolkit pentru VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->