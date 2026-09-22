# HTTPS Streaming a Model Context Protocol (MCP) segítségével

Ez a fejezet átfogó útmutatót nyújt a biztonságos, skálázható és valós idejű streaming megvalósításához a Model Context Protocol (MCP) használatával HTTPS-en keresztül. Lefedi a streaming motivációját, a rendelkezésre álló szállítási mechanizmusokat, a streamelhető HTTP MCP-ben történő megvalósítását, a biztonsági legjobb gyakorlatokat, az SSE-ről való migrálást, és gyakorlati útmutatót nyújt a saját streaming MCP alkalmazások építéséhez.

> [!WARNING]
> A tananyagban található megvalósítási példák a **MCP specifikációra
> `2025-11-25`** készültek, és bemutatják a régi `initialize` kézfogást,
> a `Mcp-Session-Id`-t, a GET eseményfolyamot és a folytathatósági modellt. Az MCP `2026-07-28`
> eltávolítja ezeket a funkciókat. Az aktuális Streamable HTTP kérések önálló
> POST kérések, melyekben szerepelnek a `MCP-Protocol-Version` és `Mcp-Method` fejléc, továbbá szükség szerint a `Mcp-Name`. Lásd a
> [Mit változott az MCP-ben: a 2026-07-28 specifikáció](../../01-CoreConcepts/mcp-2026-07-28.md)
> dokumentumot, mielőtt ezeket a példákat új implementációban használnád.


## Szállítási mechanizmusok és streaming az MCP-ben

Ez a szakasz bemutatja a MCP-ben elérhető különböző szállítási mechanizmusokat és azok szerepét a streaming képességek biztosításában, amely lehetővé teszi a valós idejű kommunikációt a kliens és a szerver között.

### Mi az a szállítási mechanizmus?

Egy szállítási mechanizmus meghatározza, hogyan cserélődik adat a kliens és a szerver között. A MCP több szállítási típust támogat, hogy különböző környezetekhez és igényekhez igazodjon:

- **stdio**: Standard input/output, helyi és parancssori eszközökhöz alkalmas. Egyszerű, de nem megfelelő web vagy felhő használathoz.
- **HTTP+SSE**: A régi távoli szállítási mód, amely helytelenül MCP `2025-03-26` verzióval elavulttá vált,
    és helyette a Streamable HTTP-t javasolják. Ne használd új implementációknál.
- **Streamable HTTP**: Modern HTTP alapú streaming szállítás, amely támogatja az értesítéseket és jobb skálázhatóságot biztosít. Ajánlott a legtöbb gyártási és felhő alapú forgatókönyvben.

### Összehasonlító tábla

Tekintsd meg az alábbi összehasonlító táblázatot, hogy megértsd a különbségeket ezek között a szállítási mechanizmusok között:

| Szállítás | Állapot | Értesítések | Tipikus felhasználás |
|---|---|---|---|
| stdio | Jelenlegi | Igen | Helyi alfolyamatok |
| HTTP+SSE | Elavult | Igen | Régi távoli megvalósítások |
| Streamable HTTP | Jelenlegi | Igen | Távoli és felhő szerverek |

> **Tipp:** A megfelelő szállítás kiválasztása hatással van a teljesítményre, a skálázhatóságra és a felhasználói élményre. A **Streamable HTTP** ajánlott modern, skálázható és felhő-kompatibilis alkalmazásokhoz.

A szabványos szállítások a stdio és a Streamable HTTP. A HTTP+SSE csak régebbi példákban fordul elő.


## Streaming: Fogalmak és motiváció

A streaming mögötti alapvető fogalmak és motivációk megértése elengedhetetlen a hatékony valós idejű kommunikációs rendszerek megvalósításához.

A **streaming** egy hálózati programozási technika, amely lehetővé teszi az adatok kis, kezelhető darabokban vagy eseménysorrend formájában történő küldését és fogadását, ahelyett, hogy az egész válaszra várnánk. Ez különösen hasznos:

- Nagyméretű fájlok vagy adattömegek esetén.
- Valós idejű frissítésekhez (például chat, folyamatjelző sávok).
- Hosszú futamidejű számításoknál, amikor szeretnénk az felhasználót tájékoztatni.

Íme, amit a streamingről magas szinten tudni kell:

- Az adatok fokozatosan érkeznek, nem egyszerre.
- A kliens az adatok megérkezésekor már dolgozhat velük.
- Csökkenti az észlelt késleltetést és javítja a felhasználói élményt.

### Miért használjunk streaminget?

A streaming használatának okai a következők:


- A felhasználók azonnal visszajelzést kapnak, nem csak a végén
- Lehetővé teszi valós idejű alkalmazások és reszponzív felhasználói felületek létrehozását
- Hatékonyabb hálózati és számítási erőforrás-használat

### Egyszerű példa: HTTP Streaming szerver és kliens

Itt egy egyszerű példa arra, hogyan valósítható meg a streaming:

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

Ez a példa bemutatja, hogy a szerver hogyan küld egy sor üzenetet a kliensnek, amint azok elérhetővé válnak, ahelyett, hogy megvárná, míg az összes üzenet elkészül.

**Hogyan működik:**

- A szerver minden üzenetet lead, amint az elkészül.
- A kliens fogadja és kiírja az érkező részeket.

**Követelmények:**

- A szervernek streaming választ kell használnia (pl. `StreamingResponse` FastAPI-ben).
- A kliensnek a választ streamként kell feldolgoznia (`stream=True` a requests-ben).
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

**Java implementációs megjegyzések:**

- A Spring Boot reaktív stackjét használja `Flux`-szal a streaminghez
- A `ServerSentEvent` strukturált eseménystreamelést biztosít eseménytípusokkal
- A `WebClient` a `bodyToFlux()`-szal reaktív streaming fogyasztást tesz lehetővé
- A `delayElements()` szimulálja az események közötti feldolgozási időt
- Az eseményeknek lehetnek típusai (`info`, `result`) a jobb kliens kezelhetőségért

### Összehasonlítás: Klasszikus streaming és MCP streaming

A különbségek a "klasszikus" streaming és az MCP streaming működése között az alábbiak szerint ábrázolhatók:

| Tulajdonság              | Klasszikus HTTP streaming       | MCP streaming (Értesítések)       |
|------------------------|--------------------------------|-----------------------------------|
| Fő válasz               | Darabokra bontva                | Egyetlen, a végén                  |
| Előrehaladási frissítések | Adatrészként küldve           | Értesítésekként küldve             |
| Ügyfélkövetelmények      | A stream feldolgozása kötelező | Üzenetkezelő megvalósítása kötelező|
| Használati eset          | Nagy fájlok, AI token folyamok | Előrehaladás, naplók, valós idejű visszajelzés |

### Megfigyelt fő különbségek

Ezen kívül itt van néhány fő különbség:

- **Kommunikációs minta:**
  - Klasszikus HTTP streaming: Egyszerű darabokra bontott adatátvitel
  - MCP streaming: Strukturált értesítési rendszer JSON-RPC protokollal

- **Üzenetformátum:**
  - Klasszikus HTTP: Egyszerű szöveges darabok új sorokkal
  - MCP: Strukturált LoggingMessageNotification objektumok metaadatokkal

- **Kliens megvalósítás:**
  - Klasszikus HTTP: Egyszerű kliens, amely feldolgozza a streaming válaszokat
  - MCP: Bonyolultabb kliens, üzenetkezelővel a különböző üzenettípusok kezelésére

- **Előrehaladási frissítések:**
  - Klasszikus HTTP: Az előrehaladás a fő válaszstream része
  - MCP: Az előrehaladás külön értesítési üzenetként érkezik, a fő válasz a végén jön

### Ajánlások

Néhány dolgot javaslunk, amikor eldöntöd, hogy a klasszikus streaminget valósítod meg (például az általunk fent bemutatott `/stream` végponton keresztül), vagy MCP streaminget választod.

- **Egyszerű streaming igényekhez:** A klasszikus HTTP streaming egyszerűbb megvalósítani, és elegendő az alapvető streaming igényekhez.


- **Komplex, interaktív alkalmazások esetén:** Az MCP streaming egy strukturáltabb megközelítést kínál gazdagabb metadátákkal és értesítések és a végső eredmények szétválasztásával.

- **Mesterséges intelligencia alkalmazások esetén:** Az MCP értesítési rendszere különösen hasznos hosszú ideig futó MI feladatoknál, ahol szeretnénk a felhasználókat tájékoztatni a folyamat állapotáról.

## Streaming az MCP-ben

Rendben, eddig láttál néhány ajánlást és összehasonlítást a klasszikus streaming és az MCP streaming közti különbségekről. Most nézzük meg részletesen, hogyan használhatod ki az MCP streaming képességeit.

Az MCP keretrendszeren belül a streamelés működésének megértése alapvető fontosságú olyan válaszkész alkalmazások építéséhez, amelyek valós idejű visszajelzést adnak a felhasználóknak hosszú ideig tartó műveletek alatt.

Az MCP-ben a streaming nem a válasz fő részének darabokban történő küldését jelenti, hanem **értesítések** küldését az ügyfél felé, miközben egy eszköz egy kérés feldolgozásán dolgozik. Ezek az értesítések tartalmazhatnak előrehaladási frissítéseket, naplókat vagy egyéb eseményeket.

### Hogyan működik

A fő eredményt továbbra is egyetlen válaszként küldik. Ugyanakkor az értesítések külön üzenetként küldhetők a feldolgozás során, így valós időben frissítik az ügyfelet. Az ügyfélnek képesnek kell lennie ezeket az értesítéseket kezelni és megjeleníteni.

### Opcionális gyakorlat: csatlakozás egy hosztolt MCP szerverhez

Streamable HTTP-t is használhatsz helyi szerver futtatása nélkül. Ez a példa
csatlakozik a [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp) szolgáltatáshoz,
felfedezi annak eszközeit, és keres a nyilvános MCP dokumentációban ugyanazzal a
Python SDK-val, amit a [helyi kliens](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py) is használ.

A Parallel anonim végpontja nem igényel fiókot vagy API kulcsot. Az ingyenes hozzáférés
korlátozott. A script futtatásakor a keresési lekérdezéseket, célt és egy
véletlenszerű munkamenet-azonosítót küld a Parallelnak. A szolgáltatás támogatja a `web_fetch`-t,
amely elküldi a kért URL-eket és minden megadott kontextust a Parallelnak. Ehhez a gyakorlathoz nyilvános
információkat használjon; lásd a [feltételeket](https://parallel.ai/customer-terms)
és az [adatvédelmi szabályzatot](https://parallel.ai/privacy-policy).

Python 3.10 vagy újabb és egy aktivált virtuális környezet esetén telepítsd az SDK-t:

```sh
python -m pip install "mcp>=1.10,<2"
```

Mentse el `hosted_search.py` néven, majd futtassa: `python hosted_search.py`:

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

A felfedezés tartalmazni fogja a `web_search` és `web_fetch` eszközöket, majd egy keresési
választ, amely forrás URL-eket és részleteket tartalmazhat. Az eredmények változhatnak vagy lehetnek üresek.
A szkript ellenőrzi az `isError` értékét, mert egy eszköz meghibásodhat akkor is, ha az HTTP kérés
sikeres volt. Ha a hozzáférés korlátozott, várjon mielőtt újra próbálkozik. Használja újra ugyanazt
a `session_id`-t, ha a scriptet kiegészíti hasonló keresési vagy lekérési hívásokkal.

A Streamable HTTP mind JSON, mind SSE válaszokat engedélyez; ez a szerver visszaadhat egy
teljes JSON eredményt értesítések nélkül. Az SDK kezeli a
szállítást. Folytassa az alábbi helyi példával az értesítések megismeréséhez.
Ez az opcionális szkript egy keresést hajt végre, majd lezárja a kapcsolatot,
amikor végez. Ha később ezeket az eszközöket egy ügynök számára teszi elérhetővé, az ügynök a munkája alatt
hívhatja meg őket; a lekért webes szöveget megbízhatatlan adatként kezelje.

## Mi az az értesítés?

Mondtuk, hogy „Értesítés”, mit is jelent ez az MCP kontextusában?

Az értesítés egy JSON-RPC üzenet, amelynek nincs `id`-ja és nem
kap választ. Az MCP értesítéseket használ előrehaladás, megszakítás és
egyéb egyirányú események jelzésére.

Az MCP `2025-11-25` verziójában az ügyfél a `notifications/initialized` eseményt küldi el, miután

inicializációs kézfogás. Az MCP `2026-07-28` verziójában nincs inicializációs kézfogás, így
ez a jelzés régi működés.

Egy értesítés így néz ki JSON üzenetként:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

A naplózás egy olyan funkció, ami értesítéseket használ; maguk az értesítések általános JSON-RPC üzenettípusok.


> **Elavult az MCP `2026-07-28` verzióban:** a Naplózás funkció kompatibilitási okokból elérhető marad,
> de jogosult eltávolításra az első olyan specifikáció
> verziófrissítésében, amely 2027. július 28-a vagy azutáni időpontban jelenik meg. Az új megvalósításoknak `stderr`-t kell használniuk stdio-val vagy OpenTelemetry-vel a strukturált megfigyelhetőséghez.


Egy régi, `2025-11-25` megvalósítás esetén a szerver a Naplózás
képességet a következőképpen engedélyezi:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Az SDK-tól függően a naplózás alapértelmezés szerint engedélyezett lehet, vagy a szerver konfigurációjában kifejezetten engedélyezni kell.

Különböző típusú értesítések léteznek:

| Szint      | Leírás                         | Példa használat                 |
|-----------|-------------------------------|--------------------------------|
| debug     | Részletes hibakeresési információk | Függvény eleje/kilépési pontok |
| info      | Általános információs üzenetek | Művelet előrehaladásának frissítései |
| notice    | Normál, de jelentős események   | Konfigurációs változások        |
| warning   | Figyelmeztető állapotok        | Elavult funkció használata      |
| error     | Hibaállapotok                  | Művelet sikertelenségek         |
| critical  | Kritikus állapotok             | Rendszerkomponens hibák         |
| alert     | Azonnali beavatkozás szükséges | Adat integritási hiba észlelve  |
| emergency | A rendszer használhatatlan     | Teljes rendszerleállás          |

## Értesítések megvalósítása az MCP-ben

Az MCP-ben az értesítések megvalósításához mind a szerver, mind a kliens oldalon be kell állítani a valós idejű frissítések kezelését. Ez lehetővé teszi, hogy az alkalmazás azonnali visszajelzést adjon a felhasználónak hosszú műveletek közben.

### Szerver oldal: Értesítések küldése

Kezdjük a szerver oldalával. Az MCP-ben definiálhatók olyan eszközök, amelyek értesítéseket tudnak küldeni a kérések feldolgozása során. A szerver a kontextus objektumot (általában `ctx`) használja arra, hogy üzeneteket küldjön a kliensnek.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

A fenti példában a `process_files` eszköz három értesítést küld a kliensnek minden egyes fájl feldolgozásakor. Az `ctx.info()` metódust információs üzenetek küldésére használják.

Ezen felül, hogy az értesítések engedélyezve legyenek, a szervernek streaming transportot (például `streamable-http`) kell használnia, és a kliensnek üzenetkezelőt kell megvalósítania az értesítések feldolgozásához. Így állítható be a szerver a `streamable-http` transport használatára:

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

Ebben a .NET példában a `ProcessFiles` eszköz a `Tool` attribútummal van ellátva, és három értesítést küld a kliensnek minden egyes fájl feldolgozásakor. Az `ctx.Info()` metódust információs üzenetek küldésére használják.

Az értesítések engedélyezéséhez a .NET MCP szerverben győződj meg róla, hogy streaming transportot használsz:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliens oldal: Értesítések fogadása

A kliensnek meg kell valósítania egy üzenetkezelőt, hogy a beérkező értesítéseket feldolgozza és megjelenítse.

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


A fenti kódban a `message_handler` függvény ellenőrzi, hogy a bejövő üzenet értesítés-e. Ha igen, kiírja az értesítést; különben normál szerverüzenetként dolgozza fel. Vegyük észre azt is, hogy a `ClientSession` példányosításakor a `message_handler` kerül megadásra a bejövő értesítések kezeléséhez.

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


Ebben a .NET példában a `MessageHandler` függvény ellenőrzi, hogy a beérkező üzenet értesítés-e. Ha igen, kiírja az értesítést; különben normál szerverüzenetként dolgozza fel. A `ClientSession` a `ClientSessionOptions` segítségével inicializálódik az üzenetkezelővel.

Az értesítések engedélyezéséhez győződjön meg arról, hogy a szervere streaming transzportot használ (például `streamable-http`), és az ügyfél egy üzenetkezelőt valósít meg az értesítések feldolgozására.

## Előrehaladási értesítések és forgatókönyvek

Ebben a szakaszban bemutatjuk az MCP előrehaladási értesítéseinek fogalmát, miért fontosak, és hogyan valósíthatók meg Streamable HTTP használatával. Egy gyakorlati feladat is segíti a megértést.

Az előrehaladási értesítések valós idejű üzenetek, amelyeket a szerver küld az ügyfél felé hosszú ideig tartó műveletek során. Ahelyett, hogy a teljes folyamat befejezéséig várnánk, a szerver folyamatosan tájékoztatja az ügyfelet az aktuális állapotról. Ez növeli az átláthatóságot, javítja a felhasználói élményt, és megkönnyíti a hibakeresést.

**Példa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miért használjunk előrehaladási értesítéseket?

Az előrehaladási értesítések több okból is nélkülözhetetlenek:

- **Jobb felhasználói élmény:** A felhasználók a munka előrehaladtával kapnak frissítéseket, nem csak a végén.
- **Valós idejű visszacsatolás:** Az ügyfelek megjeleníthetik a folyamatjelző sávokat vagy naplókat, így az alkalmazás válaszkésznek tűnik.
- **Könnyebb hibakeresés és monitorozás:** Fejlesztők és felhasználók láthatják, hol lassulhat vagy akad meg a folyamat.

### Hogyan valósítsuk meg az előrehaladási értesítéseket

Így valósíthatja meg az MCP előrehaladási értesítéseket:

- **A szerveren:** Használja a `ctx.info()` vagy `ctx.log()` függvényt, hogy minden feldolgozott elemről értesítést küldjön. Ez az üzenet az ügyfélhez érkezik még a fő eredmény elkészülte előtt.
- **Az ügyfélen:** Valósítson meg egy üzenetkezelőt, amely hallgatja és megjeleníti az értesítéseket, amint azok érkeznek. Ez a kezelő megkülönbözteti az értesítéseket és a végső eredményt.

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

**Ügyfél példa:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Biztonsági megfontolások

A biztonság legyen kiemelt szempont bármely szerver megvalósításakor, különösen HTTP-alapú transzportok, például a Streamable HTTP MCP-ben történő használatakor.

Az MCP szerverek HTTP-alapú transzportokkal való megvalósítása során a biztonság kiemelt jelentőségű, amely odafigyelést igényel számos támadási vektor és védelmi mechanizmus tekintetében.

### Áttekintés

A biztonság kritikus az MCP szerverek HTTP-n keresztüli elérhetősége esetén. A Streamable HTTP új támadási felületeket hoz és gondos konfigurációt igényel.

Íme néhány fontos biztonsági megfontolás:

- **Origin fejléc érvényesítése**: Mindig ellenőrizze az `Origin` fejlécet, hogy megakadályozza a DNS átirányítási támadásokat.
- **Localhost kötés**: A helyi fejlesztéshez kösse a szervereket `localhost`-hoz, hogy elkerülje a nyilvános internetes elérést.
- **Hitelesítés**: Használjon hitelesítést (pl. API kulcsok, OAuth) éles környezetben.
- **CORS**: Konfigurálja a Cross-Origin Resource Sharing (CORS) szabályokat a hozzáférés korlátozására.
- **HTTPS**: Használjon HTTPS-t éles környezetben a forgalom titkosítására.

### Legjobb gyakorlatok

Emellett kövesse az alábbi legjobb gyakorlatokat az MCP streaming szerver biztonságának megvalósításakor:

- Soha ne bízzon meg az érvényesítés nélküli bejövő kérésekben.
- Naplózza és figyelje az összes hozzáférést és hibát.
- Rendszeresen frissítse a függőségeket a biztonsági sebezhetőségek javítására.

### Kihívások

Biztonság megvalósítása során számos kihívással kell szembenéznie az MCP streaming szervereknél:

- A biztonság és a fejlesztési egyszerűség egyensúlyának megteremtése
- Különböző ügyfélkörnyezetekkel való kompatibilitás biztosítása


## Áttérés SSE-ről Streamable HTTP-re

Azoknak az alkalmazásoknak, amelyek jelenleg Server-Sent Events (SSE) technológiát használnak, a Streamable HTTP-re való áttérés kibővített lehetőségeket és jobb hosszú távú fenntarthatóságot biztosít MCP implementációik számára.

### Miért érdemes frissíteni?

Két fontos ok szól az SSE-ről Streamable HTTP-re való áttérés mellett:

- A Streamable HTTP jobb skálázhatóságot, kompatibilitást és gazdagabb értesítési támogatást kínál, mint az SSE.
- Ez az ajánlott transzport új MCP alkalmazásokhoz.

### Migrációs lépések

Így migrálhat SSE-ről Streamable HTTP-re MCP alkalmazásaiban:

- **Frissítse a szerverkódot** úgy, hogy a `mcp.run()`-ban a `transport="streamable-http"` legyen beállítva.
- **Frissítse az ügyfélkódot** úgy, hogy az SSE kliens helyett `streamablehttp_client`-et használjon.
- **Valósítson meg egy üzenetkezelőt** az ügyfélen az értesítések feldolgozására.
- **Tesztelje a kompatibilitást** a meglévő eszközökkel és munkafolyamatokkal.

### Kompatibilitás megőrzése

Ajánlott a migráció során megtartani a kompatibilitást a meglévő SSE kliensekkel. Íme néhány stratégia:

- Támogathatja mindkét transzport típust azáltal, hogy különböző végpontokon futtatja őket.
- Fokozatosan migrálja az ügyfeleket az új transzportra.

### Kihívások

A migráció során figyelembe kell venni az alábbi kihívásokat:

- Minden ügyfél frissítése
- Az értesítések továbbításában tapasztalható különbségek kezelése

### Feladat: Saját streaming MCP alkalmazás építése

**Forgatókönyv:**
Építsen egy MCP szervert és klienst, ahol a szerver egy elem listát dolgoz fel (pl. fájlokat vagy dokumentumokat), és minden feldolgozott elemről értesítést küld. Az ügyfél jelenítse meg az értesítéseket, amint azok megérkeznek.

**Lépések:**

1. Valósítson meg egy szervereszközt, amely egy listát dolgoz fel és értesítéseket küld minden elemről.
2. Valósítson meg egy ügyfelet, melyben egy üzenetkezelő valós időben jeleníti meg az értesítéseket.
3. Tesztelje a megvalósítást a szerver és ügyfél futtatásával, és figyelje az értesítéseket.

[Megoldás](./solution/README.md)

## További olvasmányok és mi jöhet ezután?

Ahhoz, hogy folytassa útját az MCP streaminggel és bővítse tudását, ez a rész további forrásokat és ajánlott lépéseket kínál fejlettebb alkalmazások építéséhez.

### További olvasmányok

- [Microsoft: Bevezetés a HTTP streamelésbe](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS az ASP.NET Core-ban](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming kérések](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mi jöhet ezután?

- Próbáljon meg fejlettebb MCP eszközöket építeni, amelyek streaminget használnak valós idejű elemzésekhez, csevegéshez vagy együttműködéses szerkesztéshez.
- Fedezze fel az MCP streaming integrálását frontend keretrendszerekkel (React, Vue stb.) élő UI frissítésekhez.
- Következő: [AI eszköztár használata VSCode-hoz](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->