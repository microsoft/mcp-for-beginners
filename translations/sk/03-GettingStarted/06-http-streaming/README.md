# HTTPS streamovanie s Model Context Protocol (MCP)

Táto kapitola poskytuje komplexný návod na implementáciu bezpečného, škálovateľného a v reálnom čase streamovania pomocou Model Context Protocol (MCP) cez HTTPS. Pokrýva motiváciu pre streamovanie, dostupné transportné mechanizmy, ako implementovať streamovateľné HTTP v MCP, bezpečnostné najlepšie praktiky, migráciu zo SSE a praktické rady pre tvorbu vlastných streamingových MCP aplikácií.

> **Výhľad:** táto lekcia popisuje Streamable HTTP podľa **MCP Špecifikácie 2025-11-25**, kde sa relácia nadviaže počas `initialize` a fixuje pomocou hlavičky `Mcp-Session-Id`. Release kandidát `2026-07-28` úplne odstraňuje handshake a session ID, čím sa každý požiadavok stáva samostatným a smerovateľným na ktorýkoľvek server bez viazaných relácií. Pozrite si [Čo sa mení v MCP: Release Kandidát 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) pre detaily.

## Transportné mechanizmy a streamovanie v MCP

Táto sekcia skúma rôzne transportné mechanizmy dostupné v MCP a ich úlohu pri umožňovaní streamingových schopností pre komunikáciu v reálnom čase medzi klientmi a servermi.

### Čo je transportný mechanizmus?

Transportný mechanizmus definuje, ako si klient a server vymieňajú dáta. MCP podporuje viacero typov transportov, ktoré vyhovujú rôznym prostrediam a požiadavkám:

- **stdio**: Štandardný vstup/výstup, vhodný pre lokálne a CLI nástroje. Jednoduchý, ale nevhodný pre web alebo cloud.
- **SSE (Server-Sent Events)**: Umožňuje serverom tlačiť aktualizácie v reálnom čase klientom cez HTTP. Dobré pre webové UI, ale obmedzené škálovanie a flexibilitu. Od MCP Špecifikácie 2025-06-18 je samostatný SSE transport zastaraný a je nahradený transportom „Streamable HTTP“.
- **Streamable HTTP**: Moderný HTTP založený streamingový transport, ktorý podporuje notifikácie a lepšie škálovanie. Odporúča sa pre väčšinu produkčných a cloudových scénarov.

### Porovnávacia tabuľka

Pozrite si nižšie porovnávaciu tabuľku pre pochopenie rozdielov medzi týmito transportmi:

| Transport         | Aktualizácie v reálnom čase | Streamovanie | Škálovateľnosť | Použitie                  |
|-------------------|-----------------------------|-------------|----------------|--------------------------|
| stdio             | Nie                         | Nie         | Nízka          | Lokálne CLI nástroje      |
| SSE               | Áno                         | Áno         | Stredná        | Web, aktualizácie v reálnom čase |
| Streamable HTTP   | Áno                         | Áno         | Vysoká         | Cloud, multi-klient       |

> **Tip:** Výber správneho transportu ovplyvňuje výkon, škálovateľnosť a užívateľský zážitok. **Streamable HTTP** sa odporúča pre moderné, škálovateľné a cloud-pripravené aplikácie.

Všímajte si transporty stdio a SSE, ktoré ste videli v predchádzajúcich kapitolách, a ako streamovateľné HTTP je transport, ktorý sa pokrýva v tejto kapitole.

## Streamovanie: Koncepty a motivácia

Pochopenie základných konceptov a motivácií za streamovaním je nevyhnutné pre implementáciu efektívnych komunikačných systémov v reálnom čase.

**Streamovanie** je technika v sieťovom programovaní, ktorá umožňuje odosielať a prijímať dáta v malých, spravovateľných častiach alebo ako sekvenciu udalostí namiesto čakania na kompletnú odpoveď. Je to obzvlášť užitočné pre:

- Veľké súbory alebo dátové množiny.
- Aktualizácie v reálnom čase (napríklad chat, ukazovatele priebehu).
- Dlhodobé výpočty, kde chcete informovať používateľa priebežne.

Tu je to, čo potrebujete vedieť o streamovaní na vysokú úroveň:

- Dáta sa doručujú postupne, nie naraz.
- Klient môže spracovávať dáta, ako prichádzajú.
- Znižuje vnímanú latenciu a zlepšuje užívateľský zážitok.

### Prečo používať streamovanie?

Dôvody na používanie streamovania sú:

- Používatelia dostávajú spätnú väzbu okamžite, nie až na konci.
- Umožňuje aplikáciám v reálnom čase a responzívnym UI.
- Efektívnejšie využitie sieťových a výpočtových zdrojov.

### Jednoduchý príklad: HTTP streamingový server a klient

Tu je jednoduchý príklad, ako môže byť streamovanie implementované:

#### Python

**Server (Python, s FastAPI a StreamingResponse):**

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

Tento príklad ukazuje server posielajúci sériu správ klientovi, ako sú k dispozícii, namiesto čakania na všetky správy.

**Ako to funguje:**

- Server vydáva každú správu, keď je pripravená.
- Klient prijíma a vypisuje každú časť, ako prichádza.

**Požiadavky:**

- Server musí použiť streamingovú odpoveď (napr. `StreamingResponse` vo FastAPI).
- Klient musí spracovať odpoveď ako stream (`stream=True` v requests).
- Content-Type býva obyčajne `text/event-stream` alebo `application/octet-stream`.

#### Java

**Server (Java, s Spring Boot a Server-Sent Events):**

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

**Klient (Java, s Spring WebFlux WebClient):**

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

- Používa Spring Boot reaktívny stack s `Flux` pre streamovanie
- `ServerSentEvent` poskytuje štruktúrované streamovanie udalostí s typmi udalostí
- `WebClient` s `bodyToFlux()` umožňuje konzumáciu reaktívneho streamu
- `delayElements()` simuluje čas spracovania medzi udalosťami
- Udalosti môžu mať typy (`info`, `result`) pre lepšie spracovanie na klientovi

### Porovnanie: Klasické streamovanie vs MCP streamovanie

Rozdiely medzi tým, ako funguje streamovanie v "klasickom" štýle oproti MCP, môžeme znázorniť takto:

| Funkcia                | Klasické HTTP streamovanie       | MCP streamovanie (Notifikácie)     |
|------------------------|---------------------------------|------------------------------------|
| Hlavná odpoveď          | Po častiach (chunked)            | Jediná, na konci                   |
| Aktualizácie priebehu   | Posielané ako dátové časti       | Posielané ako notifikácie          |
| Požiadavky klienta      | Musí spracovať stream            | Musí implementovať správca správ   |
| Použitie                | Veľké súbory, AI tok tokenov     | Priebeh, logy, spätná väzba v reálnom čase |

### Kľúčové pozorované rozdiely

Okrem toho sú tu niektoré kľúčové rozdiely:

- **Komunikačný vzor:**
  - Klasické HTTP streamovanie: Používa jednoduché chunked transfer encoding na posielanie dát po častiach
  - MCP streamovanie: Používa štruktúrovaný notifikačný systém s JSON-RPC protokolom

- **Formát správ:**
  - Klasické HTTP: Časti obyčajného textu s novými riadkami
  - MCP: Štruktúrované LoggingMessageNotification objekty s metaúdajmi

- **Implementácia klienta:**
  - Klasické HTTP: Jednoduchý klient, ktorý spracováva streamingové odpovede
  - MCP: Komplexnejší klient so správcom správ na spracovanie rôznych typov správ

- **Aktualizácie priebehu:**
  - Klasické HTTP: Priebeh je súčasťou hlavného streamu odpovede
  - MCP: Priebeh sa posiela cez samostatné notifikačné správy, hlavná odpoveď príde na konci

### Odporúčania

Existujú niektoré odporúčania pri rozhodovaní medzi implementáciou klasického streamovania (ako endpoint, ktorý sme vám ukázali vyššie používajúci `/stream`) a streamovaním cez MCP.

- **Pre jednoduché potreby streamovania:** Klasické HTTP streamovanie je jednoduchšie na implementáciu a postačuje pre základné potreby.

- **Pre zložité, interaktívne aplikácie:** MCP streamovanie poskytuje štruktúrovanejší prístup s bohatšími metaúdajmi a oddelením medzi notifikáciami a konečnými výsledkami.

- **Pre AI aplikácie:** Notifikačný systém MCP je obzvlášť užitočný pre dlhodobé AI úlohy, kde chcete používateľov priebežne informovať o pokroku.

## Streamovanie v MCP

Takže ste doteraz videli niektoré odporúčania a porovnania o rozdieloch medzi klasickým streamovaním a streamovaním v MCP. Poďme sa podrobne pozrieť, ako môžete v MCP využiť streamovanie.

Pochopenie fungovania streamovania v rámci MCP je nevyhnutné pre budovanie responzívnych aplikácií, ktoré poskytujú spätnú väzbu v reálnom čase používateľom počas dlhodobých operácií.

V MCP nejde o posielanie hlavnej odpovede po častiach, ale o posielanie **notifikácií** klientovi počas spracovávania požiadavky nástrojom. Tieto notifikácie môžu zahŕňať aktualizácie priebehu, logy alebo iné udalosti.

### Ako to funguje

Hlavný výsledok je stále zaslaný ako jedna odpoveď. Notifikácie však môžu byť počas spracovania posielané ako samostatné správy a tým klienta aktualizovať v reálnom čase. Klient musí byť schopný tieto notifikácie spracovať a zobraziť.

## Čo je notifikácia?

Spomenuli sme „Notifikáciu“, čo to znamená v kontexte MCP?

Notifikácia je správa poslaná zo servera klientovi, aby informovala o priebehu, stave alebo iných udalostiach počas dlhodobej operácie. Notifikácie zlepšujú prehľadnosť a užívateľský zážitok.

Napríklad klient má poslať notifikáciu po tom, čo bol vytvorený úvodný handshake so serverom.

Notifikácia vyzerá ako JSON správa takto:

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

> **Upozornenie na zastaralosť:** Release kandidát MCP špecifikácie `2026-07-28` označuje základný Logging primitív za zastaraný v prospech `stderr` pre stdio transporty a OpenTelemetry pre štruktúrovanú observabilitu. Logging funguje v `2025-11-25` a minimálne rok po formálnom zastaraní. Viď [Čo sa mení v MCP: Release Kandidát 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Aby logging fungoval, server ho musí povoliť ako funkciu/možnosť takto:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> V závislosti od použitého SDK môže byť logging povolený predvolene alebo ho možno budete musieť explicitne povoliť v konfigurácii servera.

Existujú rôzne typy notifikácií:

| Úroveň      | Popis                            | Príklad použitia              |
|------------|---------------------------------|------------------------------|
| debug      | Podrobné debugovacie informácie | Prístup/výstup funkcie       |
| info       | Všeobecné informačné správy     | Aktualizácie priebehu        |
| notice     | Normálne, ale významné udalosti | Zmeny konfigurácie           |
| warning    | Varovné stavy                   | Použitie zastaranej funkcie  |
| error      | Chybové stavy                   | Zlyhania operácie            |
| critical   | Kritické stavy                  | Zlyhanie systémovej komponenty|
| alert      | Okamžitá nutnosť zásahu         | Zistená korupcia dát         |
| emergency  | Systém nepoužiteľný             | Kompletné zlyhanie systému   |

## Implementácia notifikácií v MCP

Pre implementáciu notifikácií v MCP musíte nastaviť serverovú aj klientskú časť, aby zvládali aktualizácie v reálnom čase. To umožní vašej aplikácii poskytovať používateľom okamžitú spätnú väzbu počas dlhodobých operácií.

### Na strane servera: Odosielanie notifikácií

Začnime na strane servera. V MCP definujete nástroje, ktoré môžu posielať notifikácie počas spracovávania požiadaviek. Server používa kontextový objekt (obyčajne `ctx`) na posielanie správ klientovi.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V predchádzajúcom príklade nástroj `process_files` posiela klientovi tri notifikácie, keď spracováva každý súbor. Metóda `ctx.info()` sa používa na posielanie informačných správ.

Na zapnutie notifikácií uistite sa, že váš server používa streamingový transport (napríklad `streamable-http`) a klient implementuje správcu správ pre spracovanie notifikácií. Tu je spôsob, ako nastaviť server pre použitie transportu `streamable-http`:

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

V tomto .NET príklade nástroj `ProcessFiles` je označený atribútom `Tool` a počas spracovania každej úlohy posiela klientovi tri notifikácie. Metóda `ctx.Info()` slúži na posielanie informačných správ.

Pre zapnutie notifikácií vo vašom .NET MCP serveri, uistite sa, že používate streamingový transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Na strane klienta: Prijímanie notifikácií

Klient musí implementovať správcu správ, ktorý spracuje a zobrazí notifikácie, keď prídu.

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

V predchádzajúcom kóde funkcia `message_handler` kontroluje, či prichádzajúca správa je notifikácia. Ak áno, vypíše notifikáciu, inak ju spracuje ako bežnú správu zo servera. Tiež si všimnite, že `ClientSession` sa inicializuje s `message_handler` pre spracovanie prichádzajúcich notifikácií.

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

V tomto .NET príklade funkcia `MessageHandler` kontroluje, či je prichádzajúca správa notifikácia. Ak áno, vypíše ju, inak ju spracuje ako bežnú správu zo servera. `ClientSession` sa inicializuje so správcom správ cez `ClientSessionOptions`.

Na zapnutie notifikácií uistite sa, že váš server používa streamingový transport (ako `streamable-http`) a klient implementuje správcu správ na spracovanie notifikácií.

## Notifikácie o priebehu a scenáre

Táto sekcia vysvetľuje koncept notifikácií o priebehu v MCP, prečo sú dôležité a ako ich implementovať pomocou Streamable HTTP. Nájdete tu aj praktické zadanie na upevnenie vedomostí.

Notifikácie o priebehu sú správy v reálnom čase posielané zo servera klientovi počas dlhodobých operácií. Namiesto čakania na dokončenie celého procesu server priebežne informuje klienta o aktuálnom stave. To zvyšuje prehľadnosť, užívateľský zážitok a uľahčuje ladenie.

**Príklad:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Prečo používať notifikácie o priebehu?

Notifikácie o priebehu sú nevyhnutné z niekoľkých dôvodov:

- **Lepší užívateľský zážitok:** Používatelia vidia aktualizácie počas práce, nie až nakoniec.
- **Spätná väzba v reálnom čase:** Klienti môžu zobrazovať ukazovatele priebehu alebo logy, čím aplikácia pôsobí responzívnejšie.
- **Jednoduchšie ladenie a monitoring:** Vývojári a používatelia vidia, kde môže proces viaznuť alebo byť pomalý.

### Ako implementovať notifikácie o priebehu

Tu je spôsob, ako implementovať notifikácie o priebehu v MCP:

- **Na serveri:** Použite `ctx.info()` alebo `ctx.log()` na posielanie notifikácií pri spracovaní každej položky. Takto server posiela správu klientovi ešte pred dokončením hlavného výsledku.
- **Na klientovi:** Implementujte správcu správ, ktorý počúva a zobrazuje notifikácie, ako prichádzajú. Tento správca rozlišuje medzi notifikáciami a konečným výsledkom.

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

Bezpečnosť by mala byť najvyššou prioritou pri implementácii akéhokoľvek servera, najmä pri použití HTTP založených transportov ako Streamable HTTP v MCP.

Pri implementácii MCP serverov s HTTP založenými transportmi sa bezpečnosť stáva kľúčovou záležitosťou, ktorá si vyžaduje dôkladnú pozornosť voči rôznym útokom a ochranným mechanizmom.

### Prehľad

Bezpečnosť je kritická pri vystavovaní MCP serverov cez HTTP. Streamable HTTP prináša nové možnosti útokov a vyžaduje starostlivé nastavenie.

Tu sú niektoré kľúčové bezpečnostné úvahy:

- **Overenie hlavičky Origin**: Vždy overujte hlavičku `Origin`, aby ste zabránili DNS rebinding útokom.
- **Viazanie na localhost**: Pre lokálny vývoj viažte servery na `localhost`, aby neboli vystavené verejnému internetu.
- **Autentifikácia**: Implementujte autentifikáciu (napr. API kľúče, OAuth) pre produkčné nasadenia.
- **CORS**: Konfigurujte politiky Cross-Origin Resource Sharing (CORS) na obmedzenie prístupu.
- **HTTPS**: Používajte HTTPS v produkcii na šifrovanie prenosu dát.

### Najlepšie praktiky

Okrem toho tu sú niektoré najlepšie praktiky, ktoré treba dodržiavať pri implementácii bezpečnosti vo vašom MCP streamovacom serveri:

- Nikdy neverte prichádzajúcim požiadavkám bez overenia.
- Logujte a monitorujte všetky prístupy a chyby.
- Pravidelne aktualizujte závislosti, aby ste opravili bezpečnostné zraniteľnosti.

### Výzvy

Pri implementácii bezpečnosti v MCP streamovacích serveroch sa stretnete s niektorými výzvami:

- Vyváženie bezpečnosti a jednoduchosti vývoja
- Zaistenie kompatibility s rôznymi klientskymi prostrediami


## Aktualizácia zo SSE na Streamable HTTP

Pre aplikácie, ktoré v súčasnosti používajú Server-Sent Events (SSE), migrácia na Streamable HTTP prináša vylepšené schopnosti a lepšiu dlhodobú udržateľnosť vašich MCP implementácií.

### Prečo aktualizovať?

Existujú dva presvedčivé dôvody na aktualizáciu zo SSE na Streamable HTTP:

- Streamable HTTP ponúka lepšiu škálovateľnosť, kompatibilitu a bohatšiu podporu notifikácií než SSE.
- Je odporúčaným transportom pre nové MCP aplikácie.

### Kroky migrácie

Tu je, ako môžete migrovať zo SSE na Streamable HTTP vo vašich MCP aplikáciách:

- **Aktualizujte serverový kód** na použitie `transport="streamable-http"` v `mcp.run()`.
- **Aktualizujte klientsky kód** na použitie `streamablehttp_client` namiesto SSE klienta.
- **Implementujte spracovateľa správ** v klientovi na spracovanie notifikácií.
- **Otestujte kompatibilitu** s existujúcimi nástrojmi a pracovnými tokmi.

### Udržiavanie kompatibility

Odporúča sa udržiavať kompatibilitu so súčasnými SSE klientmi počas procesu migrácie. Tu sú niektoré stratégie:

- Môžete podporovať oba transporty SSE aj Streamable HTTP spustením na rôznych koncových bodoch.
- Postupne migrujte klientov na nový transport.

### Výzvy

Počas migrácie zabezpečte riešenie nasledujúcich výziev:

- Zaistenie aktualizácie všetkých klientov
- Riešenie rozdielov v doručovaní notifikácií

### Zadanie: Vytvorte si vlastnú streamovaciu MCP aplikáciu

**Scenár:**
Vytvorte MCP server a klienta, kde server spracováva zoznam položiek (napr. súbory alebo dokumenty) a posiela notifikáciu pre každú spracovanú položku. Klient by mal zobrazovať každú notifikáciu, ako prichádza.

**Kroky:**

1. Implementujte serverový nástroj, ktorý spracováva zoznam a posiela notifikácie pre každú položku.
2. Implementujte klienta so spracovateľom správ pre zobrazenie notifikácií v reálnom čase.
3. Otestujte vašu implementáciu spustením servera a klienta a sledujte prichádzajúce notifikácie.

[Riešenie](./solution/README.md)

## Ďalšie čítanie a čo ďalej?

Ak chcete pokračovať na svojej ceste so streamovaním MCP a rozšíriť si vedomosti, táto časť poskytuje ďalšie zdroje a odporúčané kroky pre vytváranie pokročilejších aplikácií.

### Ďalšie čítanie

- [Microsoft: Úvod do HTTP streamovania](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Čo ďalej?

- Skúste vytvoriť pokročilejšie MCP nástroje, ktoré používajú streamovanie pre analýzy v reálnom čase, chat alebo kolaboratívne úpravy.
- Preskúmajte integráciu MCP streamovania s frontendovými rámcami (React, Vue, atď.) pre živé aktualizácie UI.
- Ďalej: [Využívanie AI Toolkit pre VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->