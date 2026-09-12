# HTTPS streamovanie s Model Context Protocol (MCP)

Táto kapitola poskytuje komplexný návod na implementáciu bezpečného, škálovateľného a reálneho streamovania pomocou Model Context Protocol (MCP) cez HTTPS. Pokrýva motiváciu pre streamovanie, dostupné transportné mechanizmy, spôsob implementácie streamovateľného HTTP v MCP, bezpečnostné odporúčania, migráciu zo SSE a praktické rady pre vytváranie vlastných streamovacích MCP aplikácií.

> [!WARNING]
> Implementačné príklady v tejto lekcii sú zamerané na **MCP špecifikáciu
> `2025-11-25`** a demonštrujú legacy handshake `initialize`,
> `Mcp-Session-Id`, GET event stream a model obnoviteľnosti. MCP `2026-07-28`
> tieto funkcie odstraňuje. Súčasné Streamovateľné HTTP požiadavky sú samostatné
> POST požiadavky s hlavičkami `MCP-Protocol-Version` a `Mcp-Method`, plus
> `Mcp-Name` tam, kde je to potrebné. Pozrite si
> [Čo sa zmenilo v MCP: Špecifikácia 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> pred použitím týchto príkladov v novej implementácii.

## Transportné mechanizmy a streamovanie v MCP

Táto sekcia skúma rôzne dostupné transportné mechanizmy v MCP a ich úlohu pri umožňovaní streamovacích schopností pre reálnu komunikáciu medzi klientmi a servermi.

### Čo je transportný mechanizmus?

Transportný mechanizmus definuje, ako sa vymieňajú dáta medzi klientom a serverom. MCP podporuje viacero typov transportov, ktoré vyhovujú rôznym prostrediam a požiadavkám:

- **stdio**: Štandardný vstup/výstup, vhodný pre lokálne a CLI nástroje. Jednoduchý, ale nevhodný pre web alebo cloud.
- **HTTP+SSE**: Legacy vzdialený transport, zastaraný v MCP `2025-03-26`
    a nahradený Streamovateľným HTTP. Nepoužívajte ho pre nové implementácie.
- **Streamable HTTP**: Moderný HTTP založený streamovací transport, podporujúci notifikácie a lepšiu škálovateľnosť. Odporúča sa pre väčšinu produkčných a cloudových scénarov.

### Porovnávacia tabuľka

Pozrite sa na porovnávaciu tabuľku nižšie, aby ste pochopili rozdiely medzi týmito transportnými mechanizmami:

| Transport | Stav | Notifikácie | Typické použitie |
|---|---|---|---|
| stdio | Aktuálny | Áno | Lokálne podprocesy |
| HTTP+SSE | Zastaraný | Áno | Legacy vzdialené implementácie |
| Streamable HTTP | Aktuálny | Áno | Vzdialené a cloudové servery |

> **Tip:** Výber správneho transportu ovplyvňuje výkonnosť, škálovateľnosť a užívateľskú skúsenosť. **Streamable HTTP** sa odporúča pre moderné, škálovateľné a cloud-ready aplikácie.

Štandardné transporty sú stdio a Streamable HTTP. HTTP+SSE sa objavuje
iba v starších príkladoch.

## Streamovanie: Koncepty a motivácia

Pochopenie základných konceptov a motivácií za streamovaním je kľúčové pre implementáciu efektívnych systémov reálnej komunikácie.

**Streamovanie** je technika v sieťovom programovaní, ktorá umožňuje posielať a prijímať dáta v malých, spravovateľných častiach alebo ako sekvenciu udalostí, namiesto čakania na celú odpoveď. Toto je obzvlášť užitočné pre:

- Veľké súbory alebo dátové súbory.
- Reálne aktualizácie (napr. chat, progress bary).
- Dlhodobé výpočty s cieľom informovať používateľa priebežne.

Tu je, čo potrebujete vedieť o streamovaní na vysokej úrovni:

- Dáta sa doručujú postupne, nie naraz.
- Klient môže spracovávať dáta, ako prichádzajú.
- Znižuje vnímanú latenciu a zlepšuje používateľskú skúsenosť.

### Prečo používať streamovanie?

Dôvody použitia streamovania sú nasledujúce:

- Používatelia dostávajú okamžitú spätnú väzbu, nielen na konci.
- Umožňuje reálne aplikácie a responzívne používateľské rozhrania.
- Efektívnejšie využitie sieťových a výpočtových zdrojov.

### Jednoduchý príklad: HTTP streaming server a klient

Tu je jednoduchý príklad, ako možno implementovať streamovanie:

#### Python

**Server (Python, používa FastAPI a StreamingResponse):**

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

**Klient (Python, používa requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tento príklad demonštruje server, ktorý posiela sériu správ klientovi, ako sú dostupné, namiesto čakania, kým sú všetky správy pripravené.

**Ako to funguje:**

- Server vydáva každú správu, keď je pripravená.
- Klient prijíma a vypisuje každý dielik, ako prichádza.

**Požiadavky:**

- Server musí používať streamovaciu odpoveď (napr. `StreamingResponse` vo FastAPI).
- Klient musí spracovať odpoveď ako stream (`stream=True` v requests).
- Content-Type je zvyčajne `text/event-stream` alebo `application/octet-stream`.

#### Java

**Server (Java, používa Spring Boot a Server-Sent Events):**

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

**Klient (Java, používa Spring WebFlux WebClient):**

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

- Používa reaktívny stack Spring Boot s `Flux` pre streamovanie
- `ServerSentEvent` poskytuje štruktúrované streamovanie udalostí s typmi udalostí
- `WebClient` s `bodyToFlux()` umožňuje konzumovať reaktívne streamy
- `delayElements()` simuluje spracovanie medzi udalosťami
- Udalosti môžu mať typy (`info`, `result`) pre lepšie spracovanie klientom

### Porovnanie: Klasické streamovanie verzus MCP streamovanie

Rozdiely medzi klasickým spôsobom streamovania a spôsobom v MCP možno znázorniť takto:

| Funkcia                | Klasické HTTP streamovanie     | MCP streamovanie (notifikácie)      |
|------------------------|-------------------------------|-------------------------------------|
| Hlavná odpoveď         | Časti (chunked)                | Jedna, na konci                      |
| Aktualizácie priebehu  | Odosielané ako dátové časti    | Odosielané ako notifikácie           |
| Požiadavky klienta     | Musí spracovať stream          | Musí implementovať spracovač správ  |
| Použitie               | Veľké súbory, AI token stream | Priebeh, logy, spätná väzba v reálnom čase |

### Kľúčové pozorované rozdiely

Okrem toho platia tieto kľúčové rozdiely:

- **Komunikačný vzorec:**
  - Klasické HTTP streamovanie: používa jednoduché chunkované prenosové kódovanie pre dáta v častiach
  - MCP streamovanie: používa štruktúrovaný notifikačný systém s JSON-RPC protokolom

- **Formát správ:**
  - Klasické HTTP: jednoduché textové časti s novými riadkami
  - MCP: štruktúrované LoggingMessageNotification objekty s metadátami

- **Implementácia klienta:**
  - Klasické HTTP: jednoduchý klient spracujúci streamovacie odpovede
  - MCP: zložitejší klient so spracovačom správ na spracovanie rôznych typov správ

- **Aktualizácie priebehu:**
  - Klasické HTTP: priebeh je súčasťou hlavného streamu odpovede
  - MCP: priebeh sa posiela cez samostatné notifikačné správy, zatiaľ čo hlavná odpoveď príde na konci

### Odporúčania

Existujú určité odporúčania pri výbere medzi implementáciou klasického streamovania (ako endpoint, ktorý sme ukázali vyššie pomocou `/stream`) versus použitím streamovania cez MCP.

- **Pre jednoduché potreby streamovania:** Klasické HTTP streamovanie je jednoduchšie na implementáciu a postačuje pre základné streamovacie potreby.


- **Pre zložité, interaktívne aplikácie:** MCP streaming poskytuje štruktúrovanejší prístup s bohatšími metadátami a oddelením medzi notifikáciami a konečnými výsledkami.

- **Pre AI aplikácie:** Notifikačný systém MCP je obzvlášť užitočný pre dlhodobé AI úlohy, kde chcete používateľov informovať o priebehu.

## Streaming v MCP

Dobre, takže doteraz ste videli niektoré odporúčania a porovnania rozdielov medzi klasickým streamovaním a streamovaním v MCP. Pozrime sa podrobnejšie na to, ako presne môžete využiť streaming v MCP.

Pochopenie, ako streaming funguje v rámci MCP rámca je nevyhnutné pre tvorbu responzívnych aplikácií, ktoré poskytujú používateľom spätnú väzbu v reálnom čase počas dlhodobých operácií.

V MCP nejde o posielanie hlavnej odpovede po častiach, ale o posielanie **notifikácií** klientovi počas spracovania požiadavky nástrojom. Tieto notifikácie môžu obsahovať aktualizácie priebehu, logy alebo iné udalosti.

### Ako to funguje

Hlavný výsledok sa stále posiela ako jedna odpoveď. Notifikácie však môžu byť zasielané ako samostatné správy počas spracovania a tak aktualizovať klienta v reálnom čase. Klient musí vedieť tieto notifikácie spracovať a zobraziť.

### Nepovinné cvičenie: pripojenie k hosťovanému MCP serveru

Môžete tiež použiť Streamable HTTP bez toho, aby ste spúšťali lokálny server. Tento príklad
sa pripája k [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
zisťuje jeho nástroje a vyhľadáva verejnú MCP dokumentáciu pomocou toho istého
Python SDK ako [lokálny klient](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Anonymné rozhranie Parallel nevyžaduje účet ani API kľúč. Bezplatný prístup je
limitovaný podľa rýchlosti. Spustením tohto skriptu sa odošlú vyhľadávacie dotazy, cieľ a
náhodný identifikátor relácie na Parallel. Služba tiež ponúka `web_fetch`,
ktorá odosiela požadované URL a akýkoľvek dodaný kontext na Parallel. Pre toto cvičenie používajte verejné
informácie; pozrite si jeho [podmienky](https://parallel.ai/customer-terms)
a [zásady ochrany osobných údajov](https://parallel.ai/privacy-policy).

S Python 3.10 alebo novším a aktivovaným virtuálnym prostredím nainštalujte SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Uložte to ako `hosted_search.py` a spustite `python hosted_search.py`:

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

Očakávajte, že objavovanie bude zahŕňať `web_search` a `web_fetch`, po ktorých nasleduje odpoveď na vyhľadávanie obsahujúca zdrojové URL a úryvky. Výsledky sa môžu líšiť alebo byť prázdne.
Skript kontroluje `isError`, pretože nástroj môže zlyhať aj keď HTTP požiadavka
uspeje. Ak je prístup limitovaný podľa rýchlosti, počkajte pred ďalším pokusom. Opätovne používajte ten istý
`session_id` ak skript rozšírite o súvisiace vyhľadávacie alebo fetch volania.


kompletný JSON výsledok bez notifikácií o priebehu. SDK sa stará o
transport. Pokračujte s lokálnym príkladom nižšie, aby ste sa dozvedeli viac o notifikáciách.
Tento voliteľný skript vykoná jedno explicitné vyhľadávanie a po jeho dokončení zatvorí pripojenie.
Ak neskôr tieto nástroje sprístupníte agentovi, agent ich môže počas svojej práce vyvolať; považujte získaný webový text za nedôveryhodné dáta.



## Čo je to Notifikácia?

Povedali sme "Notifikácia", čo to znamená v kontexte MCP?

Notifikácia je JSON-RPC správa, ktorá nemá `id` a na ktorú sa nečaká odpoveď.
MCP používa notifikácie pre priebeh, zrušenie a
iné jednosmerné udalosti.

V MCP `2025-11-25` klient pošle `notifications/initialized` po

inicializácia handshake. MCP `2026-07-28` nemá inicializačný handshake, takže
toto oznámenie je staré správanie.

Oznámenie vyzerá ako JSON správa:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logovanie je jedna z funkcií, ktorá používa oznámenia; samotné oznámenia sú
všeobecný typ JSON-RPC správy.

> **Zastarané v MCP `2026-07-28`:** funkcia Logovania zostáva dostupná
> pre kompatibilitu, ale môže byť odstránená v prvej revízii špecifikácie
> vydanej dňa alebo po 28. júla 2027. Nové implementácie by mali používať
> `stderr` so stdio alebo OpenTelemetry pre štruktúrovanú pozorovateľnosť.

Pre starú implementáciu `2025-11-25` server aktivuje schopnosť Logovania
nasledovne:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> V závislosti od použitého SDK môže byť logovanie povolené predvolene, alebo ho možno budete musieť explicitne povoliť v konfigurácii servera.

Existujú rôzne typy oznámení:

| Úroveň    | Popis                         | Príklad použitia             |
|-----------|-------------------------------|-----------------------------|
| debug     | Podrobné informácie pre debug  | Vstupy/výstupy funkcií      |
| info      | Všeobecné informačné správy    | Aktualizácie priebehu operácií |
| notice    | Normálne ale významné udalosti  | Zmeny konfigurácie          |
| warning   | Varovné podmienky              | Použitie zastaranej funkcie |
| error     | Chybové podmienky              | Zlyhania operácií           |
| critical  | Kritické podmienky             | Zlyhania systémových komponentov |
| alert     | Vyžaduje okamžité opatrenie   | Zistená korupcia dát        |
| emergency | Systém je nepoužiteľný        | Kompletné zlyhanie systému  |

## Implementácia Oznámení v MCP

Aby ste implementovali oznámenia v MCP, je potrebné nastaviť na strane servera aj klienta spracovanie aktualizácií v reálnom čase. To umožňuje vašej aplikácii poskytovať okamžitú spätnú väzbu používateľom počas dlhšie trvajúcich operácií.

### Strana servera: Odosielanie oznámení

Začnime so stranou servera. V MCP definujete nástroje, ktoré môžu pri spracovaní požiadaviek odosielať oznámenia. Server používa objekt kontextu (obvykle `ctx`) na odosielanie správ klientovi.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V predchádzajúcom príklade nástroj `process_files` odosiela klientovi tri oznámenia počas spracovania každého súboru. Metóda `ctx.info()` sa používa na odosielanie informačných správ.

Okrem toho, aby boli oznámenia povolené, uistite sa, že váš server používa streamingový transport (ako `streamable-http`) a váš klient implementuje spracovanie správ pre oznamovanie oznámení. Takto môžete nastaviť server na použitie transportu `streamable-http`:

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

V tomto príklade .NET je nástroj `ProcessFiles` označený atribútom `Tool` a odosiela klientovi tri oznámenia počas spracovania každého súboru. Metóda `ctx.Info()` sa používa na odosielanie informačných správ.

Na povolenie oznámení vo vašom .NET MCP serveri sa uistite, že používate streamingový transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Strana klienta: Prijímanie oznámení

Klient musí implementovať spracovanie správ na spracovanie a zobrazenie prichádzajúcich oznámení.

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


V predchádzajúcom kóde funkcia `message_handler` kontroluje, či prichádzajúca správa je notifikácia. Ak áno, vypíše notifikáciu; inak ju spracuje ako bežnú serverovú správu. Tiež všimnite si, ako je `ClientSession` inicializovaný so `message_handler`, aby sa spracovali prichádzajúce notifikácie.

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


V tomto príklade .NET funkcia `MessageHandler` kontroluje, či je prichádzajúca správa notifikáciou. Ak áno, vytlačí notifikáciu; inak ju spracuje ako bežnú správu zo servera. `ClientSession` je inicializovaná s obsluhou správ cez `ClientSessionOptions`.

Ak chcete povoliť notifikácie, uistite sa, že váš server používa streamingový transport (ako `streamable-http`) a váš klient implementuje obsluhu správ na spracovanie notifikácií.

## Notifikácie priebehu a scenáre

Táto sekcia vysvetľuje koncept notifikácií priebehu v MCP, prečo sú dôležité a ako ich implementovať pomocou Streamable HTTP. Tiež tu nájdete praktické zadanie na upevnenie vedomostí.

Notifikácie priebehu sú správy v reálnom čase odosielané zo servera klientovi počas dlhodobých operácií. Namiesto čakania, kým sa celý proces dokončí, server priebežne informuje klienta o aktuálnom stave. To zlepšuje transparentnosť, užívateľský zážitok a uľahčuje ladenie.

**Príklad:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Prečo používať notifikácie priebehu?

Notifikácie priebehu sú nevyhnutné z niekoľkých dôvodov:

- **Lepší užívateľský zážitok:** Používatelia vidia aktualizácie počas práce, nie len na jej konci.
- **Spätná väzba v reálnom čase:** Klienti môžu zobrazovať ukazovatele priebehu alebo logy, čo zvyšuje vnímanú reakčnosť aplikácie.
- **Jednoduchšie ladenie a monitorovanie:** Vývojári a používatelia môžu vidieť, kde môže proces spomaliť alebo sa zaseknúť.

### Ako implementovať notifikácie priebehu

Takto môžete implementovať notifikácie priebehu v MCP:

- **Na serveri:** Použite `ctx.info()` alebo `ctx.log()` na odosielanie notifikácií pri spracovaní jednotlivých položiek. Táto správa sa odošle klientovi predtým, než je pripravený hlavný výsledok.
- **Na klientovi:** Implementujte obsluhu správ, ktorá bude počúvať a zobrazovať prichádzajúce notifikácie. Táto obsluha rozlišuje notifikácie a konečný výsledok.

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

Bezpečnosť by mala byť na prvom mieste pri implementácii akéhokoľvek servera, najmä pri použití HTTP-based transportov ako Streamable HTTP v MCP.

Pri implementácii MCP serverov s HTTP-based transportami sa bezpečnosť stáva zásadnou témou, ktorá vyžaduje dôkladnú pozornosť viacerým útokovým vektorom a ochranným mechanizmom.

### Prehľad

Bezpečnosť je kritická pri sprístupňovaní MCP serverov cez HTTP. Streamable HTTP prináša nové útočné povrchy a vyžaduje dôkladnú konfiguráciu.

Tu sú niektoré kľúčové bezpečnostné úvahy:

- **Validácia hlavičky Origin**: Vždy validujte hlavičku `Origin`, aby ste predišli DNS rebinding útokom.
- **Väzba na localhost**: Na lokálny vývoj viažte servery na `localhost`, aby neboli prístupné verejnej sieti.
- **Autentifikácia**: Implementujte autentifikáciu (napr. API kľúče, OAuth) pre produkčné nasadenie.
- **CORS**: Nastavte politiky Cross-Origin Resource Sharing (CORS) na obmedzenie prístupu.
- **HTTPS**: Používajte HTTPS v produkcii na šifrovanie komunikácie.

### Najlepšie praktiky

Okrem toho tu sú niektoré najlepšie praktiky pri implementácii bezpečnosti vo vašom MCP streamingovom serveri:

- Nikdy neverte prichádzajúcim požiadavkám bez validácie.
- Logujte a monitorujte všetky prístupy a chyby.
- Pravidelne aktualizujte závislosti kvôli záplatovaniu bezpečnostných zraniteľností.

### Výzvy

Pri implementácii bezpečnosti v MCP streamingových serveroch vás čakajú tieto výzvy:

- Balansovanie bezpečnosti s jednoduchosťou vývoja
- Zabezpečenie kompatibility s rôznymi klientskymi prostrediami


## Prechod zo SSE na Streamable HTTP

Pre aplikácie, ktoré momentálne používajú Server-Sent Events (SSE), migrácia na Streamable HTTP poskytuje rozšírené možnosti a lepšiu dlhodobú udržateľnosť pre vaše MCP implementácie.

### Prečo prejsť na vyššiu verziu?

Sú dva presvedčivé dôvody na prechod zo SSE na Streamable HTTP:

- Streamable HTTP ponúka lepšiu škálovateľnosť, kompatibilitu a bohatšiu podporu notifikácií než SSE.
- Je odporúčaným transportom pre nové MCP aplikácie.

### Kroky migrácie

Takto môžete migrovať zo SSE na Streamable HTTP vo vašich MCP aplikáciách:

- **Aktualizujte serverový kód** tak, aby používal `transport="streamable-http"` v `mcp.run()`.
- **Aktualizujte klientský kód** tak, aby používal `streamablehttp_client` namiesto SSE klienta.
- **Implementujte obsluhu správ** v klientovi na spracovanie notifikácií.
- **Otestujte kompatibilitu** s existujúcimi nástrojmi a pracovnými tokmi.

### Udržiavanie kompatibility

Počas migrácie sa odporúča udržiavať kompatibilitu s existujúcimi SSE klientmi. Tu sú niektoré stratégie:

- Môžete podporovať SSE aj Streamable HTTP súčasne spustením oboch transportov na rôznych endpointoch.
- Postupne migrujte klientov na nový transport.

### Výzvy

Počas migrácie majte na pamäti nasledujúce výzvy:

- Zaistiť, aby všetci klienti boli aktualizovaní
- Riešiť rozdiely v doručovaní notifikácií

### Zadanie: Vytvorte vlastnú streamingovú MCP aplikáciu

**Scenár:**
Vytvorte MCP server a klienta, kde server spracuje zoznam položiek (napr. súbory alebo dokumenty) a odosiela notifikáciu za každú spracovanú položku. Klient by mal zobrazovať každú notifikáciu hneď, ako príde.

**Kroky:**

1. Implementujte serverový nástroj, ktorý spracuje zoznam a odosiela notifikácie za každú položku.
2. Implementujte klienta s obsluhou správ, ktorý v reálnom čase zobrazí notifikácie.
3. Otestujte implementáciu spustením servera aj klienta a sledujte notifikácie.

[Riešenie](./solution/README.md)

## Ďalšie čítanie a čo ďalej?

Ak chcete pokračovať na svojej ceste s MCP streamingom a rozšíriť svoje vedomosti, táto sekcia poskytuje dodatočné zdroje a navrhované ďalšie kroky pre tvorbu pokročilejších aplikácií.

### Ďalšie čítanie

- [Microsoft: Úvod do HTTP streamingu](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Čo ďalej?

- Skúste vytvoriť pokročilejšie MCP nástroje, ktoré využívajú streaming pre analytiku v reálnom čase, chat alebo kolaboratívnu editáciu.
- Preskúmajte integráciu MCP streamingu s frontendovými frameworkami (React, Vue a pod.) pre živé aktualizácie UI.
- Ďalej: [Využitie AI Toolkit pre VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->