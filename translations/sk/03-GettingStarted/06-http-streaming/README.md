# HTTPS Streaming s Model Context Protocol (MCP)

Táto kapitola poskytuje komplexný návod na implementáciu bezpečného, škálovateľného a real-time streamovania pomocou Model Context Protocol (MCP) cez HTTPS. Zahŕňa motiváciu pre streamovanie, dostupné transportné mechanizmy, ako implementovať streamovateľný HTTP v MCP, bezpečnostné najlepšie praktiky, migráciu zo SSE a praktické rady na vytvorenie vlastných streamovacích MCP aplikácií.

## Transportné mechanizmy a streamovanie v MCP

Táto sekcia skúma rôzne transportné mechanizmy dostupné v MCP a ich úlohu pri umožnení streamovacích schopností pre real-time komunikáciu medzi klientmi a servermi.

### Čo je transportný mechanizmus?

Transportný mechanizmus definuje, ako sa dáta vymieňajú medzi klientom a serverom. MCP podporuje viacero typov transportov, aby vyhovoval rôznym prostrediam a požiadavkám:

- **stdio**: Štandardný vstup/výstup, vhodný pre lokálne a CLI nástroje. Jednoduchý, ale nevhodný pre web alebo cloud.
- **SSE (Server-Sent Events)**: Umožňuje serverom posielať real-time aktualizácie klientom cez HTTP. Dobré pre webové UI, ale obmedzené v škálovateľnosti a flexibilite.
- **Streamovateľný HTTP**: Moderný HTTP-based streamovací transport, podporujúci notifikácie a lepšiu škálovateľnosť. Odporúčaný pre väčšinu produkčných a cloudových scenárov.

### Porovnávacia tabuľka

Pozrite si porovnávaciu tabuľku nižšie, aby ste pochopili rozdiely medzi týmito transportnými mechanizmami:

| Transport         | Real-time aktualizácie | Streamovanie | Škálovateľnosť | Použitie                  |
|-------------------|------------------------|-------------|---------------|---------------------------|
| stdio             | Nie                   | Nie          | Nízka         | Lokálne CLI nástroje      |
| SSE               | Áno                   | Áno          | Stredná       | Web, real-time aktualizácie |
| Streamovateľný HTTP | Áno                  | Áno          | Vysoká        | Cloud, multi-klient       |

> **Tip:** Výber správneho transportu ovplyvňuje výkon, škálovateľnosť a používateľskú skúsenosť. **Streamovateľný HTTP** je odporúčaný pre moderné, škálovateľné a cloud-ready aplikácie.

Všimnite si transporty stdio a SSE, ktoré boli uvedené v predchádzajúcich kapitolách, a ako streamovateľný HTTP je transport pokrytý v tejto kapitole.

## Streamovanie: Koncepty a motivácia

Porozumenie základným konceptom a motiváciám za streamovaním je nevyhnutné pre implementáciu efektívnych real-time komunikačných systémov.

**Streamovanie** je technika v sieťovom programovaní, ktorá umožňuje posielanie a prijímanie dát v malých, spracovateľných častiach alebo ako sekvenciu udalostí, namiesto čakania na kompletnú odpoveď. To je obzvlášť užitočné pre:

- Veľké súbory alebo dataset-y.
- Real-time aktualizácie (napr. chat, progress bary).
- Dlhodobé výpočty, kde chcete informovať používateľa o priebehu.

Tu je, čo potrebujete vedieť o streamovaní na vysokej úrovni:

- Dáta sú doručované postupne, nie naraz.
- Klient môže spracovať dáta, ako prichádzajú.
- Znižuje vnímanú latenciu a zlepšuje používateľskú skúsenosť.

### Prečo používať streamovanie?

Dôvody na používanie streamovania sú nasledujúce:

- Používatelia dostávajú spätnú väzbu okamžite, nie až na konci.
- Umožňuje real-time aplikácie a responzívne UI.
- Efektívnejšie využitie sieťových a výpočtových zdrojov.

### Jednoduchý príklad: HTTP streamovací server a klient

Tu je jednoduchý príklad, ako môže byť streamovanie implementované:

#### Python

**Server (Python, pomocou FastAPI a StreamingResponse):**

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

**Klient (Python, pomocou requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tento príklad demonštruje server, ktorý posiela sériu správ klientovi, ako sú dostupné, namiesto čakania na všetky správy.

**Ako to funguje:**

- Server postupne posiela každú správu, ako je pripravená.
- Klient prijíma a tlačí každú časť, ako prichádza.

**Požiadavky:**

- Server musí používať streamovaciu odpoveď (napr. `StreamingResponse` vo FastAPI).
- Klient musí spracovať odpoveď ako stream (`stream=True` v requests).
- Content-Type je zvyčajne `text/event-stream` alebo `application/octet-stream`.

#### Java

**Server (Java, pomocou Spring Boot a Server-Sent Events):**

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

**Klient (Java, pomocou Spring WebFlux WebClient):**

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

**Poznámky k implementácii v Jave:**

- Používa reaktívny stack Spring Boot s `Flux` pre streamovanie.
- `ServerSentEvent` poskytuje štruktúrované streamovanie udalostí s typmi udalostí.
- `WebClient` s `bodyToFlux()` umožňuje reaktívnu konzumáciu streamovania.
- `delayElements()` simuluje čas spracovania medzi udalosťami.
- Udalosti môžu mať typy (`info`, `result`) pre lepšie spracovanie na strane klienta.

### Porovnanie: Klasické streamovanie vs MCP streamovanie

Rozdiely medzi tým, ako streamovanie funguje "klasickým" spôsobom a ako funguje v MCP, môžeme zobraziť takto:

| Funkcia               | Klasické HTTP streamovanie     | MCP streamovanie (Notifikácie)     |
|-----------------------|-------------------------------|------------------------------------|
| Hlavná odpoveď        | Po častiach                   | Jedna, na konci                   |
| Aktualizácie priebehu | Posielané ako časti dát       | Posielané ako notifikácie         |
| Požiadavky na klienta | Musí spracovať stream         | Musí implementovať handler správ  |
| Použitie              | Veľké súbory, AI token streamy | Priebeh, logy, real-time spätná väzba |

### Pozorované kľúčové rozdiely

Okrem toho sú tu niektoré kľúčové rozdiely:

- **Komunikačný vzor:**
  - Klasické HTTP streamovanie: Používa jednoduché chunked transfer encoding na posielanie dát po častiach.
  - MCP streamovanie: Používa štruktúrovaný systém notifikácií s JSON-RPC protokolom.

- **Formát správy:**
  - Klasické HTTP: Čistý text po častiach s novými riadkami.
  - MCP: Štruktúrované LoggingMessageNotification objekty s metadátami.

- **Implementácia klienta:**
  - Klasické HTTP: Jednoduchý klient, ktorý spracováva streamovacie odpovede.
  - MCP: Sofistikovanejší klient s handlerom správ na spracovanie rôznych typov správ.

- **Aktualizácie priebehu:**
  - Klasické HTTP: Priebeh je súčasťou hlavného streamu odpovede.
  - MCP: Priebeh je posielaný cez samostatné notifikačné správy, zatiaľ čo hlavná odpoveď prichádza na konci.

### Odporúčania

Existujú určité odporúčania pri výbere medzi implementáciou klasického streamovania (ako endpoint, ktorý sme ukázali vyššie pomocou `/stream`) a streamovaním cez MCP.

- **Pre jednoduché streamovacie potreby:** Klasické HTTP streamovanie je jednoduchšie implementovať a postačuje pre základné streamovacie potreby.

- **Pre komplexné, interaktívne aplikácie:** MCP streamovanie poskytuje štruktúrovanejší prístup s bohatšími metadátami a oddelením medzi notifikáciami a finálnymi výsledkami.

- **Pre AI aplikácie:** MCP notifikačný systém je obzvlášť užitočný pre dlhodobé AI úlohy, kde chcete informovať používateľov o priebehu.

## Streamovanie v MCP

Dobre, videli ste niektoré odporúčania a porovnania rozdielov medzi klasickým streamovaním a streamovaním v MCP. Poďme sa podrobne pozrieť na to, ako môžete využiť streamovanie v MCP.

Porozumenie tomu, ako streamovanie funguje v rámci MCP frameworku, je nevyhnutné pre vytváranie responzívnych aplikácií, ktoré poskytujú real-time spätnú väzbu používateľom počas dlhodobých operácií.

V MCP streamovanie nie je o posielaní hlavnej odpovede po častiach, ale o posielaní **notifikácií** klientovi počas spracovania požiadavky. Tieto notifikácie môžu zahŕňať aktualizácie priebehu, logy alebo iné udalosti.

### Ako to funguje

Hlavný výsledok je stále posielaný ako jedna odpoveď. Avšak notifikácie môžu byť posielané ako samostatné správy počas spracovania, čím sa klient aktualizuje v real-time. Klient musí byť schopný spracovať a zobraziť tieto notifikácie.

## Čo je notifikácia?

Povedali sme "Notifikácia", čo to znamená v kontexte MCP?

Notifikácia je správa poslaná zo servera klientovi na informovanie o priebehu, stave alebo iných udalostiach počas dlhodobej operácie. Notifikácie zlepšujú transparentnosť a používateľskú skúsenosť.

Napríklad klient má poslať notifikáciu po tom, čo sa uskutoční počiatočný handshake so serverom.

Notifikácia vyzerá takto ako JSON správa:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifikácie patria do témy v MCP označovanej ako ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Aby logging fungoval, server ho musí povoliť ako funkciu/schopnosť takto:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> V závislosti od použitého SDK môže byť logging predvolene povolený, alebo ho budete musieť explicitne povoliť v konfigurácii servera.

Existujú rôzne typy notifikácií:

| Úroveň     | Popis                        | Príklad použitia                 |
|------------|------------------------------|----------------------------------|
| debug      | Detailné informácie o ladení | Vstup/výstup funkcie             |
| info       | Všeobecné informačné správy  | Aktualizácie priebehu operácie   |
| notice     | Normálne, ale významné udalosti | Zmeny konfigurácie              |
| warning    | Varovné podmienky            | Použitie zastaranej funkcie      |
| error      | Chybové podmienky            | Zlyhanie operácie                |
| critical   | Kritické podmienky           | Zlyhanie systémovej komponenty   |
| alert      | Nutná okamžitá akcia         | Zistená korupcia dát             |
| emergency  | Systém je nepoužiteľný       | Kompletné zlyhanie systému       |

## Implementácia notifikácií v MCP

Na implementáciu notifikácií v MCP musíte nastaviť serverovú aj klientskú stranu na spracovanie real-time aktualizácií. To umožňuje vašej aplikácii poskytovať okamžitú spätnú väzbu používateľom počas dlhodobých operácií.

### Serverová strana: Posielanie notifikácií

Začnime serverovou stranou. V MCP definujete nástroje, ktoré môžu posielať notifikácie počas spracovania požiadaviek. Server používa objekt kontextu (zvyčajne `ctx`) na posielanie správ klientovi.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V predchádzajúcom príklade nástroj `process_files` posiela tri notifikácie klientovi, ako spracováva každý súbor. Metóda `ctx.info()` sa používa na posielanie informačných správ.

Okrem toho, aby ste povolili notifikácie, uistite sa, že váš server používa streamovací transport (ako `streamable-http`) a váš klient implementuje handler správ na spracovanie notifikácií. Tu je, ako môžete nastaviť server na používanie transportu `streamable-http`:

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

V tomto .NET príklade je nástroj `ProcessFiles` označený atribútom `Tool` a posiela tri notifikácie klientovi, ako spracováva každý súbor. Metóda `ctx.Info()` sa používa na posielanie informačných správ.

Na povolenie notifikácií vo vašom .NET MCP serveri sa uistite, že používate streamovací transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientská strana: Prijímanie notifikácií

Klient musí implementovať handler správ na spracovanie a zobrazenie notifikácií, ako prichádzajú.

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

V predchádzajúcom kóde funkcia `message_handler` kontroluje, či prichádzajúca správa je notifikácia. Ak áno, tlačí notifikáciu; inak ju spracováva ako bežnú správu servera. Tiež si všimnite, ako je `ClientSession` inicializovaný s `message_handler` na spracovanie prichádzajúcich notifikácií.

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

V tomto .NET príklade funkcia `MessageHandler` kontroluje, či prichádzajúca správa je notifikácia. Ak áno, tlačí notifikáciu; inak ju spracováva ako bežnú správu servera. `ClientSession` je inicializovaný s handlerom správ cez `ClientSessionOptions`.

Na povolenie notifikácií sa uistite, že váš server používa streamovací transport (ako `streamable-http`) a váš klient implementuje handler správ na spracovanie notifikácií.

## Notifikácie priebehu & Scenáre

Táto sekcia vysvetľuje koncept notifikácií priebehu v MCP, prečo sú dôležité a ako ich implementovať pomocou Streamable HTTP. Nájdete tu aj praktické zadanie na posilnenie vášho porozumenia.

Notifikácie priebehu sú real-time správy posielané zo servera klientovi počas dlhodobých operácií. Namiesto čakania na dokončenie celého procesu server udržuje klienta informovaného o aktuálnom stave. To zlepšuje transparentnosť, používateľskú skúsenosť a uľahčuje ladenie.

**Príklad:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Prečo používať notifikácie priebehu?

Notifikácie priebehu sú nevyhnutné z viacerých dôvodov:

- **Lepšia používateľská skúsenosť:** Používatelia vidia aktualizácie, ako práca postupuje, nie len na konci.
- **Real-time spätná väzba:** Klienti môžu zobrazovať progress bary alebo logy, čím aplikácia pôsobí responzívne.
- **Jednoduchšie ladenie a monitorovanie:** Vývojári a používatelia môžu vidieť, kde proces môže byť pomalý alebo zaseknutý.

### Ako implementovať notifikácie priebehu

Tu je, ako môžete implementovať notifikácie priebehu v MCP:

- **Na serveri:** Použite `ctx.info()` alebo `ctx.log()` na posielanie notifikácií, ako sa každý prvok spracováva. Tým sa pošle správa klientovi predtým, než je hlavný výsledok pripravený.
- **Na klientovi:** Implementujte handler správ, ktorý počúva na notifikácie a zobrazuje ich, ako prichádzajú. Tento handler rozlišuje medzi notifikáciami a finálnym výsledkom.

**Príklad servera:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Príklad klienta:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Bezpečnostné úvahy

Pri implementácii MCP serverov s HTTP-based transportmi sa bezpečnosť stáva kľúčovou otázkou, ktorá si vyžaduje dôkladnú pozornosť voči viacerým vektorom útokov a ochranným mechanizmom.

### Prehľad

Bezpečnosť je kritická pri vystavovaní MCP serverov cez HTTP. Streamable HTTP prináša nové povrchové útoky a vyžaduje dôkladnú konfiguráciu.

### Kľúčové body

- **Validácia hlavičky Origin**: Vždy validujte hlavičku `Origin`, aby ste zabránili DNS rebinding útokom.
- **Lokálne viazanie**: Pre lokálny vývoj viažte servery na `localhost`, aby ste ich neodhalili verejnému internetu.
- **Autentifikácia**: Implementujte autentifikáciu (napr. API kľúče, OAuth) pre produkčné nasadenia.
- **CORS**: Konfigurujte Cross-Origin Resource Sharing (CORS) politiky na obmedzenie príst
Existujú dva presvedčivé dôvody na prechod zo SSE na Streamable HTTP:

- Streamable HTTP ponúka lepšiu škálovateľnosť, kompatibilitu a bohatšiu podporu notifikácií ako SSE.
- Je to odporúčaný transport pre nové MCP aplikácie.

### Kroky migrácie

Tu je postup, ako môžete migrovať zo SSE na Streamable HTTP vo vašich MCP aplikáciách:

- **Aktualizujte serverový kód**, aby používal `transport="streamable-http"` v `mcp.run()`.
- **Aktualizujte klientský kód**, aby používal `streamablehttp_client` namiesto SSE klienta.
- **Implementujte správcu správ** v klientovi na spracovanie notifikácií.
- **Otestujte kompatibilitu** s existujúcimi nástrojmi a pracovnými postupmi.

### Udržiavanie kompatibility

Odporúča sa udržiavať kompatibilitu s existujúcimi SSE klientmi počas procesu migrácie. Tu sú niektoré stratégie:

- Môžete podporovať SSE aj Streamable HTTP spustením oboch transportov na rôznych koncových bodoch.
- Postupne migrujte klientov na nový transport.

### Výzvy

Uistite sa, že riešite nasledujúce výzvy počas migrácie:

- Zabezpečenie aktualizácie všetkých klientov
- Riešenie rozdielov v doručovaní notifikácií

## Bezpečnostné aspekty

Bezpečnosť by mala byť najvyššou prioritou pri implementácii akéhokoľvek servera, najmä pri používaní transportov založených na HTTP, ako je Streamable HTTP v MCP.

Pri implementácii MCP serverov s transportmi založenými na HTTP sa bezpečnosť stáva kľúčovou otázkou, ktorá si vyžaduje dôkladnú pozornosť voči viacerým vektorom útokov a ochranným mechanizmom.

### Prehľad

Bezpečnosť je kritická pri vystavovaní MCP serverov cez HTTP. Streamable HTTP zavádza nové povrchy útokov a vyžaduje dôkladnú konfiguráciu.

Tu sú niektoré kľúčové bezpečnostné aspekty:

- **Validácia hlavičky Origin**: Vždy validujte hlavičku `Origin`, aby ste predišli útokom typu DNS rebinding.
- **Viazanie na localhost**: Pre lokálny vývoj viažte servery na `localhost`, aby ste ich nevystavili verejnému internetu.
- **Autentifikácia**: Implementujte autentifikáciu (napr. API kľúče, OAuth) pre produkčné nasadenia.
- **CORS**: Nakonfigurujte politiky Cross-Origin Resource Sharing (CORS) na obmedzenie prístupu.
- **HTTPS**: Používajte HTTPS v produkcii na šifrovanie prenosu.

### Najlepšie postupy

Okrem toho, tu sú niektoré najlepšie postupy, ktoré by ste mali dodržiavať pri implementácii bezpečnosti vo vašom MCP streaming serveri:

- Nikdy nedôverujte prichádzajúcim požiadavkám bez validácie.
- Zaznamenávajte a monitorujte všetky prístupy a chyby.
- Pravidelne aktualizujte závislosti na opravu bezpečnostných zraniteľností.

### Výzvy

Pri implementácii bezpečnosti v MCP streaming serveroch sa môžete stretnúť s nasledujúcimi výzvami:

- Vyváženie bezpečnosti a jednoduchosti vývoja
- Zabezpečenie kompatibility s rôznymi klientskými prostrediami

### Zadanie: Vytvorte vlastnú streaming MCP aplikáciu

**Scenár:**
Vytvorte MCP server a klienta, kde server spracováva zoznam položiek (napr. súborov alebo dokumentov) a posiela notifikáciu pre každú spracovanú položku. Klient by mal zobrazovať každú notifikáciu v reálnom čase.

**Kroky:**

1. Implementujte serverový nástroj, ktorý spracováva zoznam a posiela notifikácie pre každú položku.
2. Implementujte klienta so správcom správ na zobrazovanie notifikácií v reálnom čase.
3. Otestujte svoju implementáciu spustením servera a klienta a sledujte notifikácie.

[Solution](./solution/README.md)

## Ďalšie čítanie a čo ďalej?

Ak chcete pokračovať vo svojej ceste s MCP streamingom a rozšíriť svoje znalosti, táto sekcia poskytuje dodatočné zdroje a navrhované ďalšie kroky na vytváranie pokročilejších aplikácií.

### Ďalšie čítanie

- [Microsoft: Úvod do HTTP streamingu](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Čo ďalej?

- Skúste vytvoriť pokročilejšie MCP nástroje, ktoré využívajú streaming na analýzu v reálnom čase, chat alebo kolaboratívne úpravy.
- Preskúmajte integráciu MCP streamingu s frontendovými frameworkami (React, Vue, atď.) pre živé aktualizácie používateľského rozhrania.
- Ďalej: [Využitie AI Toolkit pre VSCode](../07-aitk/README.md)

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.