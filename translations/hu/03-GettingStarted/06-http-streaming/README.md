# HTTPS Streaming a Model Context Protocol-lal (MCP)

Ez a fejezet átfogó útmutatót nyújt a biztonságos, skálázható és valós idejű streaming megvalósításához a Model Context Protocol (MCP) használatával HTTPS-en keresztül. Lefedi a streaming motivációját, a rendelkezésre álló szállítási mechanizmusokat, a streamelhető HTTP megvalósítását MCP-ben, a biztonsági legjobb gyakorlatokat, az SSE-ről való átállást, valamint gyakorlati útmutatást saját streaming MCP alkalmazások építéséhez.

> **Előre tekintve:** ez a lecké leírja a Streamelhető HTTP-t az **MCP Szabvány 2025-11-25** szerint, ahol a munkamenet `initialize` során jön létre és rögzítve van egy `Mcp-Session-Id` fejlécben. A `2026-07-28`-i kiadás-jelölt teljesen eltávolítja a kézfogást és a munkamenet azonosítót, így minden kérés önálló és bármely szerver példányhoz irányítható ragadós munkamenetek nélkül. Részletekért lásd: [Mi változik MCP-ben: A 2026-07-28 kiadás-jelölt](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Szállítási mechanizmusok és streaming az MCP-ben

Ez a szakasz feltárja az MCP-ben elérhető különböző szállítási mechanizmusokat és azok szerepét a streaming képességek biztosításában a kliens és szerver közötti valós idejű kommunikációhoz.

### Mi az a szállítási mechanizmus?

A szállítási mechanizmus meghatározza, hogyan cserélődnek az adatok a kliens és a szerver között. Az MCP több szállítási típust támogat, hogy megfeleljen különböző környezeteknek és követelményeknek:

- **stdio**: Szabványos bemenet/kimenet, helyi és parancssoros eszközökhöz alkalmas. Egyszerű, de nem alkalmas web vagy felhő környezetre.
- **SSE (Server-Sent Events)**: Lehetővé teszi a szervereknek valós idejű frissítések küldését a klienseknek HTTP-n keresztül. Jó webes felhasználói felületekhez, de korlátozott skálázhatósággal és rugalmassággal. Az MCP Specification 2025-06-18 szerint az önálló SSE szállítás elavult, és helyette a „Streamable HTTP” szállítás lépett.
- **Streamelhető HTTP**: Modern HTTP-alapú streaming szállítás, értesítésekkel és jobb skálázhatósággal. Ajánlott a legtöbb termelési és felhő környezethez.

### Összehasonlító táblázat

Nézd meg az alábbi összehasonlító táblázatot, hogy megértsd a különbségeket a szállítási mechanizmusok között:

| Szállítás          | Valós idejű frissítések | Streaming | Skálázhatóság | Használati eset          |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | Nem               | Nem       | Alacsony    | Helyi CLI eszközök      |
| SSE               | Igen              | Igen      | Közepes     | Web, valós idejű frissítések  |
| Streamelhető HTTP  | Igen              | Igen      | Magas       | Felhő, több kliens       |

> **Tipp:** A megfelelő szállítás kiválasztása befolyásolja a teljesítményt, skálázhatóságot és a felhasználói élményt. A **Streamelhető HTTP** ajánlott modern, skálázható és felhő-kész alkalmazásokhoz.

Figyeld meg a stdio és SSE szállításokat, amiket az előző fejezetekben mutattunk, és hogy ebben a fejezetben a streamelhető HTTP-t tárgyaljuk.

## Streaming: Fogalmak és motiváció

A streaming alapvető fogalmainak és motivációinak megértése elengedhetetlen a hatékony valós idejű kommunikációs rendszerek megvalósításához.

A **streaming** egy olyan technika a hálózati programozásban, amely lehetővé teszi, hogy az adatokat kis, kezelhető részekben vagy eseménysorozatként küldjék és fogadják, ahelyett, hogy megvárnánk a teljes válasz elkészülését. Ez különösen hasznos:

- Nagy fájlok vagy adatállományok esetén.
- Valós idejű frissítéseknél (pl. chat, folyamatjelző sávok).
- Hosszú számítások esetén, amikor tájékoztatni akarjuk a felhasználót.

Íme, amit a streamingről nagyvonalakban tudni kell:

- Az adatok fokozatosan érkeznek, nem egyszerre.
- A kliens képes feldolgozni az adatokat érkezésük során.
- Csökkenti az észlelt késleltetést és javítja a felhasználói élményt.

### Miért használjunk streaminget?

A streaming használatának okai a következők:

- A felhasználók azonnali visszacsatolást kapnak, nem csak a végén
- Lehetővé teszi valós idejű alkalmazások és reszponzív UI-k létrehozását
- Hálózati és számítási erőforrások hatékonyabb kihasználása

### Egyszerű példa: HTTP Streaming szerver és kliens

Íme egy egyszerű példa arra, hogyan valósítható meg a streaming:

#### Python

**Szerver (Python, FastAPI és StreamingResponse használatával):**

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

**Kliens (Python, requests használatával):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ez a példa bemutatja, hogyan küld a szerver sorozatos üzeneteket a kliensnek, amint azok elérhetővé válnak, ahelyett, hogy megvárná az összes üzenet elkészülését.

**Hogyan működik:**

- A szerver feldob minden üzenetet, amint az készen áll.
- A kliens fogadja és kiírja az egyes adatrészeket érkezésük szerint.

**Követelmények:**

- A szerver streaming válasz használatával működik (pl. `StreamingResponse` FastAPI-ben).
- A kliensnek a választ streamingként kell feldolgoznia (`stream=True` a requests-ben).
- A Content-Type általában `text/event-stream` vagy `application/octet-stream`.

#### Java

**Szerver (Java, Spring Boot és Server-Sent Events használatával):**

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

**Kliens (Java, Spring WebFlux WebClient használatával):**

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

**Java megvalósítási megjegyzések:**

- A Spring Boot reakív stack-je `Flux`-szal a streaminghez
- `ServerSentEvent` strukturált esemény streaminget biztosít eseménytípusokkal
- `WebClient` `bodyToFlux()`-szal lehetővé teszi a reakív streaming fogyasztást
- A `delayElements()` az események közti feldolgozási időt szimulálja
- Az események típust kaphatnak (`info`, `result`) a jobb klienskezelés érdekében

### Összehasonlítás: Klasszikus Streaming vs MCP Streaming

A streaming működésének különbségei a „klasszikus” mód és az MCP szerinti mód között az alábbi táblázattal szemléltethetők:

| Jellemző               | Klasszikus HTTP Streaming      | MCP Streaming (Értesítések)       |
|------------------------|-------------------------------|----------------------------------|
| Fő válasz               | Darabolt                      | Egyszeri, végén                   |
| Előrehaladás frissítés | Adatrészként küldve           | Értesítésekként küldve            |
| Kliens követelmények    | Feldolgozza a streamet        | Üzenetkezelőt implementál         |
| Használati eset         | Nagy fájlok, AI token streamek | Előrehaladás, naplók, valós idejű visszacsatolás |

### Megfigyelt kulcsfontosságú különbségek

Emellett néhány fő különbség:

- **Kommunikációs minta:**
  - Klasszikus HTTP streaming: Egyszerű darabolt átvitel a részek küldésére
  - MCP streaming: Strukturált értesítési rendszer JSON-RPC protokollal

- **Üzenet formátum:**
  - Klasszikus HTTP: Egyszerű szöveges darabok, sortörésekkel
  - MCP: Strukturált LoggingMessageNotification objektumok metaadatokkal

- **Kliens megvalósítás:**
  - Klasszikus HTTP: Egyszerű kliens a streaming válasz feldolgozásához
  - MCP: Bonyolultabb kliens, üzenetkezelővel az eltérő üzenettípusok feldolgozására

- **Előrehaladás frissítések:**
  - Klasszikus HTTP: Az előrehaladás része a fő válasz streamnek
  - MCP: Az előrehaladás külön értesítő üzenetekként érkezik, a fő válasz pedig a végén

### Ajánlások

Néhány tanács arra vonatkozóan, hogy mikor válaszd a klasszikus streaminget (például a fent mutatott `/stream` végponton keresztül) és mikor az MCP streaminget.

- **Egyszerű streaming igényekhez:** Klasszikus HTTP streaming egyszerűbb megvalósítani és elegendő az alapvető streaming esetekhez.

- **Összetett, interaktív alkalmazásokhoz:** Az MCP streaming strukturáltabb megközelítést nyújt gazdagabb metaadatokkal, valamint az értesítések és végső eredmény elválasztásával.

- **AI alkalmazásokhoz:** Az MCP értesítési rendszere különösen hasznos hosszú futásidejű AI feladatoknál, ahol informálni akarod a felhasználókat az előrehaladásról.

## Streaming az MCP-ben

Rendben, már láttál néhány ajánlást és összehasonlítást a klasszikus streaming és az MCP streaming között. Most nézzük meg részletesen, hogyan használhatod ki az MCP streamingjét.

Az MCP keretrendszeren belüli streaming működésének megértése alapvető fontosságú, ha reszponzív alkalmazásokat akarsz építeni, melyek valós idejű visszacsatolást adnak a felhasználóknak hosszú futású műveletek során.

Az MCP-ben a streaming nem arról szól, hogy a fő választ részletekben küldjük, hanem arról, hogy **értesítéseket** küldünk a kliensnek a feldolgozás alatt álló kérés közben. Ezek az értesítések tartalmazhatnak előrehaladás frissítéseket, naplókat vagy egyéb eseményeket.

### Hogyan működik?

A fő eredmény továbbra is egyetlen válaszként érkezik. Ugyanakkor kezelhetők külön értesítő üzenetek feldolgozás közben, melyek valós időben frissítik a klienst. A kliensnek képesnek kell lennie kezelni és megjeleníteni ezeket az értesítéseket.

## Mi az az értesítés?

Mondtuk, hogy „értesítés”, de mit jelent ez MCP kontextusban?

Az értesítés olyan üzenet, amelyet a szerver küld a kliensnek, hogy tájékoztassa a folyamatban lévő hosszú művelet állapotáról, előrehaladásáról vagy más eseményekről. Az értesítések javítják az átláthatóságot és felhasználói élményt.

Például egy kliensnek értesítést kell küldenie, amikor megtörtént az eredeti kézfogás a szerverrel.

Egy értesítés egy JSON üzenet formájában így néz ki:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Az értesítések egy MCP témához tartoznak, amelyet ["Logging"-nak](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) neveznek.

> **Elavulási értesítés:** a `2026-07-28` MCP specifikáció kiadás-jelöltje a Logging primitívet elavulttá nyilvánítja, helyette a `stderr`-t használja stdio szállításokhoz, és OpenTelemetry-t strukturált megfigyelhetőséghez. A Logging továbbra is működik a `2025-11-25` verzióban, és legalább egy évig az elavulás hivatalos bejelentése után. Lásd: [Mi változik MCP-ben: A 2026-07-28 kiadás-jelölt](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

A logging működéséhez a szerveren engedélyezni kell ezt mint képességet/feature-t, így:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Az SDK-tól függően a logging lehet alapértelmezettként engedélyezve, vagy explicit aktiválásra szorulhat a szerver konfigurációjában.

Különféle értesítés típusok léteznek:

| Szint      | Leírás                         | Példa használat              |
|-----------|-------------------------------|-----------------------------|
| debug     | Részletes hibakeresési információk | Függvény kezdő/befejező pontok |
| info      | Általános információs üzenetek | Művelet előrehaladás frissítései |
| notice    | Normál, de jelentős események  | Konfigurációs változások     |
| warning   | Figyelmeztető állapotok        | Elavult funkció használata   |
| error     | Hibás állapotok                | Műveleti hibák               |
| critical  | Kritikus állapotok             | Rendszerkomponens hibák     |
| alert     | Azonnali beavatkozás szükséges  | Adatsérülés észlelése        |
| emergency | Rendszer használhatatlan       | Teljes rendszerhiba          |

## Értesítések megvalósítása az MCP-ben

Az értesítések megvalósításához az MCP-ben be kell állítanod mind a szervert, mind a klienst a valós idejű frissítések kezelésére. Ez lehetővé teszi, hogy az alkalmazásod azonnali visszacsatolást adjon a hosszú futású műveletek során.

### Szerver oldal: Értesítések küldése

Kezdjük a szerver oldallal. Az MCP-ben olyan eszközöket definiálsz, amelyek értesítéseket küldhetnek a feldolgozás alatt álló kérés közben. A szerver a kontextus objektumot (általában `ctx`) használja az üzenetek kliensnek küldésére.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

A fenti példában a `process_files` eszköz három értesítést küld a kliensnek, miközben feldolgozza az egyes fájlokat. A `ctx.info()` metódust használja információs üzenetek küldésére.

Továbbá, az értesítések engedélyezéséhez győződj meg róla, hogy a szerver streaming szállítást használ (például `streamable-http`), és a kliens implementál egy üzenetkezelőt az értesítések feldolgozásához. Így állíthatod be a szervert a `streamable-http` szállításhoz:

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

Ebben a .NET példában a `ProcessFiles` eszközt a `Tool` attribútummal díszítették, és három értesítést küld a kliensnek, miközben feldolgozza az egyes fájlokat. A `ctx.Info()` metódust használja információs üzenetek küldésére.

Az értesítések engedélyezéséhez a .NET MCP szerveredben győződj meg róla, hogy streaming szállítást használsz:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliens oldal: Értesítések fogadása

A kliensnek üzenetkezelőt kell implementálnia, hogy feldolgozza és megjelenítse az értesítéseket érkezésük során.

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

A fenti kódban a `message_handler` funkció ellenőrzi, hogy a bejövő üzenet értesítés-e. Ha igen, kiírja az értesítést; ha nem, akkor szabványos szerver üzenetként dolgozza fel. Emellett figyeld meg, hogy a `ClientSession` a `message_handler`-rel inicializálódik, hogy kezelje a bejövő értesítéseket.

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

Ebben a .NET példában a `MessageHandler` funkció ellenőrzi, hogy a bejövő üzenet értesítés-e. Ha igen, kiírja az értesítést; ha nem, szabványos szerver üzenetként dolgozza fel. A `ClientSession` a `ClientSessionOptions`-on keresztül inicializálódik az üzenetkezelővel.

Az értesítések engedélyezéséhez győződj meg róla, hogy a szerver streaming szállítást használ (például `streamable-http`), és a kliens implementál üzenetkezelőt az értesítések feldolgozására.

## Előrehaladás értesítések és forgatókönyvek

Ez a szakasz elmagyarázza az előrehaladás értesítések koncepcióját az MCP-ben, miért fontosak, és hogyan valósíthatók meg Streamelhető HTTP-vel. Találsz továbbá egy gyakorlati feladatot a megértés megerősítésére.

Az előrehaladás értesítések valós idejű üzenetek, amelyeket a szerver küld a kliensnek hosszú futású műveletek során. Ahelyett, hogy megvárnánk a teljes folyamat befejezését, a szerver folyamatosan tájékoztatja a klienst a jelenlegi állapotról. Ez javítja az átláthatóságot, a felhasználói élményt, és megkönnyíti a hibakeresést.

**Példa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miért használjuk az előrehaladás értesítéseket?

Az előrehaladás értesítések több okból is fontosak:

- **Jobb felhasználói élmény:** A felhasználók látják a frissítéseket a munka előrehaladtával, nem csak a végén.
- **Valós idejű visszacsatolás:** A kliensek megjeleníthetnek előrehaladási sávokat vagy naplókat, így az alkalmazás reszponzívnak hat.
- **Könnyebb hibakeresés és monitorozás:** Fejlesztők és felhasználók láthatják, hol lassú vagy elakadt a folyamat.

### Hogyan valósítsuk meg az előrehaladás értesítéseket?

Íme, hogyan valósíthatod meg az előrehaladás értesítéseket az MCP-ben:

- **A szerveren:** Használd a `ctx.info()` vagy `ctx.log()` metódusokat, hogy értesítéseket küldj minden feldolgozott elem után. Ez üzenetet küld a kliensnek, még mielőtt a fő eredmény elkészülne.
- **A kliensen:** Implementálj egy üzenetkezelőt, amely figyeli és megjeleníti az értesítéseket érkezésük szerint. Ez a kezelő megkülönbözteti az értesítéseket a végleges eredménytől.

**Szerver példa:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Kliens példa:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Biztonsági szempontok

A biztonságnak elsődleges fontosságnak kell lennie bármely szerver megvalósításakor, különösen HTTP-alapú átviteli módok, például az MCP-ben használt Streamable HTTP esetén.

Az MCP szerverek HTTP-alapú átvitellel történő megvalósításakor a biztonság kiemelt kérdés, amely gondos figyelmet igényel a különböző támadási felületekre és védelmi mechanizmusokra.

### Áttekintés

A biztonság létfontosságú, amikor az MCP szervereket HTTP-n keresztül teszik elérhetővé. A Streamable HTTP új támadási felületeket vezet be, és gondos konfigurációt igényel.

Íme néhány kulcsfontosságú biztonsági szempont:

- **Origin fejlécek érvényesítése**: Mindig érvényesítsd az `Origin` fejlécet, hogy megakadályozd a DNS átirányítási támadásokat.
- **Localhost kötés**: Helyi fejlesztéshez kössd a szervereket `localhost`-hoz, hogy elkerüld azok nyilvános internetre való kitettségét.
- **Hitelesítés**: Valós környezetben valósíts meg hitelesítést (pl. API kulcsok, OAuth).
- **CORS**: Konfiguráld a Cross-Origin Resource Sharing (CORS) szabályokat a hozzáférés korlátozására.
- **HTTPS**: Használj HTTPS-t termelési környezetben a forgalom titkosítására.

### Legjobb gyakorlatok

Ezen felül itt van néhány ajánlott gyakorlat a MCP streaming szerveren történő biztonság megvalósításához:

- Soha ne bízz meg bejövő kérésekben érvényesítés nélkül.
- Naplózz és figyeld az összes hozzáférést és hibát.
- Rendszeresen frissítsd a függőségeket a biztonsági sérülékenységek javítása érdekében.

### Kihívások

Biztonság implementálásakor MCP streaming szervereknél a következő kihívásokkal találkozol:

- A biztonság és a fejlesztés egyszerűségének egyensúlyozása
- Különböző kliens környezetekkel való kompatibilitás biztosítása


## Frissítés SSE-ről Streamable HTTP-re

Azoknak az alkalmazásoknak, amelyek jelenleg Server-Sent Events (SSE) technológiát használnak, a Streamable HTTP-re való áttérés bővített képességeket és jobb hosszú távú fenntarthatóságot kínál MCP implementációkhoz.

### Miért frissíts?

Két meggyőző okból érdemes SSE-ről Streamable HTTP-re váltani:

- A Streamable HTTP jobb skálázhatóságot, kompatibilitást és gazdagabb értesítési támogatást nyújt, mint az SSE.
- Ez az ajánlott átviteli mód új MCP alkalmazásokhoz.

### Áttérési lépések

Így válthatsz SSE-ről Streamable HTTP-re MCP alkalmazásaidban:

- **Frissítsd a szerverkódot**, hogy a `mcp.run()`-ban a `transport="streamable-http"` értéket használd.
- **Frissítsd a klienskódot**, hogy az SSE kliens helyett `streamablehttp_client`-et használj.
- **Valósíts meg egy üzenetkezelőt** a kliensben az értesítések feldolgozására.
- **Teszteld a kompatibilitást** meglévő eszközökkel és munkafolyamatokkal.

### Kompatibilitás fenntartása

Ajánlott az átállás alatt megőrizni a kompatibilitást a meglévő SSE kliensekkel. Itt vannak néhány stratégia:

- Támogathatod mind az SSE-t, mind a Streamable HTTP-t úgy, hogy különböző végpontokon futtatod a két átvitelt.
- Fokozatosan migráld a klienseket az új átviteli módra.

### Kihívások

Az áttérés során a következő kihívásokat kell kezelni:

- Biztosítani, hogy minden kliens frissüljön
- Kezelni az értesítések kézbesítésének különbségeit

### Feladat: Építsd meg saját streaming MCP alkalmazásodat

**Forgatókönyv:**
Építs egy MCP szervert és klienst, ahol a szerver egy lista elemeit (pl. fájlokat vagy dokumentumokat) dolgozza fel, és minden feldolgozott elemhez értesítést küld. A kliensnek meg kell jelenítenie az értesítések beérkezésekor azokat.

**Lépések:**

1. Valósíts meg egy szerver eszközt, amely feldolgoz egy listát és értesítéseket küld minden elemhez.
2. Készíts egy klienst üzenetkezelővel, amely valós időben jeleníti meg az értesítéseket.
3. Teszteld megvalósításodat úgy, hogy mind szervert, mind klienst futtatod, és figyeled az értesítéseket.

[Megoldás](./solution/README.md)

## További olvasnivalók és mi következik?

Az MCP streaminggel kapcsolatos tudásod bővítéséhez, illetve fejlettebb alkalmazások fejlesztéséhez ez a szakasz további forrásokat és javasolt következő lépéseket kínál.

### További olvasnivalók

- [Microsoft: Bevezetés HTTP streamingbe](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS az ASP.NET Core-ban](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming kérések](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mi következik?

- Próbálj meg fejlettebb MCP eszközöket építeni, amelyek streameket használnak valós idejű elemzésekhez, csevegéshez vagy közös szerkesztéshez.
- Fedezd fel az MCP streaming integrálását frontend keretrendszerekkel (React, Vue stb.) valós idejű felhasználói felület frissítésekhez.
- Következő: [AI eszköztár használata VSCode-ban](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->