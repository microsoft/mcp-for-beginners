# HTTPS Streaming a Model Context Protocol (MCP) használatával

Ez a fejezet átfogó útmutatót nyújt a biztonságos, skálázható és valós idejű streaming megvalósításához a Model Context Protocol (MCP) segítségével HTTPS-en keresztül. Kitér a streaming motivációjára, az elérhető szállítási mechanizmusokra, az MCP-ben használható streamelhető HTTP megvalósítására, a biztonsági legjobb gyakorlatokra, az SSE-ről való átállásra, valamint gyakorlati tanácsokat ad saját streaming MCP alkalmazások építéséhez.

## Szállítási mechanizmusok és streaming az MCP-ben

Ez a rész bemutatja az MCP-ben elérhető különböző szállítási mechanizmusokat, és azok szerepét a valós idejű kommunikáció streaming képességeinek lehetővé tételében az ügyfelek és a szerverek között.

### Mi az a szállítási mechanizmus?

A szállítási mechanizmus meghatározza, hogyan cserélnek adatokat az ügyfél és a szerver. Az MCP többféle szállítási típust támogat, hogy különböző környezetekhez és igényekhez igazodjon:

- **stdio**: Standard input/output, helyi és CLI-alapú eszközökhöz alkalmas. Egyszerű, de nem megfelelő webes vagy felhőalapú használatra.
- **SSE (Server-Sent Events)**: Lehetővé teszi, hogy a szerver valós idejű frissítéseket küldjön az ügyfeleknek HTTP-n keresztül. Jó webes felhasználói felületekhez, de korlátozott a skálázhatósága és rugalmassága.
- **Streamelhető HTTP**: Modern, HTTP-alapú streaming szállítás, amely értesítéseket és jobb skálázhatóságot biztosít. A legtöbb éles és felhőalapú forgatókönyvhöz ajánlott.

### Összehasonlító táblázat

Az alábbi táblázatban látható a szállítási mechanizmusok közötti különbségek:

| Szállítás          | Valós idejű frissítések | Streaming | Skálázhatóság | Használati eset            |
|--------------------|-------------------------|-----------|--------------|----------------------------|
| stdio              | Nem                    | Nem       | Alacsony     | Helyi CLI eszközök         |
| SSE                | Igen                   | Igen      | Közepes      | Web, valós idejű frissítések |
| Streamelhető HTTP  | Igen                   | Igen      | Magas        | Felhő, több ügyfél         |

> **Tipp:** A megfelelő szállítás kiválasztása hatással van a teljesítményre, a skálázhatóságra és a felhasználói élményre. A **streamelhető HTTP** ajánlott modern, skálázható és felhőre kész alkalmazásokhoz.

Jegyezd meg az előző fejezetekben bemutatott stdio és SSE szállításokat, és hogy ebben a fejezetben a streamelhető HTTP szállítás kerül bemutatásra.

## Streaming: Alapfogalmak és motiváció

A streaming alapfogalmainak és motivációjának megértése elengedhetetlen a hatékony valós idejű kommunikációs rendszerek megvalósításához.

A **streaming** egy hálózati programozási technika, amely lehetővé teszi az adatok kis, kezelhető darabokban vagy eseménysorozatként történő küldését és fogadását, ahelyett, hogy megvárnánk a teljes válasz elkészültét. Ez különösen hasznos:

- Nagy fájlok vagy adathalmazok esetén.
- Valós idejű frissítésekhez (pl. csevegés, folyamatjelző sávok).
- Hosszú számításoknál, ahol a felhasználót folyamatosan tájékoztatni kell.

Íme, amit magas szinten tudni kell a streamingről:

- Az adatok fokozatosan érkeznek, nem egyszerre.
- Az ügyfél az adatokat érkezés közben feldolgozhatja.
- Csökkenti az érzékelt késleltetést és javítja a felhasználói élményt.

### Miért használjunk streaminget?

A streaming használatának okai a következők:

- A felhasználók azonnali visszajelzést kapnak, nem csak a végén.
- Lehetővé teszi a valós idejű alkalmazásokat és a reszponzív felhasználói felületeket.
- Hatékonyabb hálózati és számítási erőforrás-felhasználás.

### Egyszerű példa: HTTP streaming szerver és kliens

Íme egy egyszerű példa a streaming megvalósítására:

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

Ez a példa bemutatja, hogyan küld a szerver üzenetek sorozatát az ügyfélnek, amint azok elérhetővé válnak, ahelyett, hogy megvárná az összes üzenet elkészültét.

**Hogyan működik:**

- A szerver minden üzenetet elküld, amint az elkészül.
- Az ügyfél minden érkező darabot feldolgoz és megjelenít.

**Követelmények:**

- A szervernek streaming választ kell használnia (pl. `StreamingResponse` a FastAPI-ban).
- Az ügyfélnek a választ streamként kell feldolgoznia (`stream=True` a requests-ben).
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

- A Spring Boot reaktív stackjét használja `Flux`-szal a streaminghez.
- A `ServerSentEvent` strukturált esemény streaminget biztosít eseménytípusokkal.
- A `WebClient` a `bodyToFlux()` segítségével lehetővé teszi a reaktív streaming fogyasztást.
- A `delayElements()` szimulálja az események közötti feldolgozási időt.
- Az események típusokkal rendelkezhetnek (`info`, `result`) a jobb ügyfélkezelés érdekében.

### Összehasonlítás: Klasszikus streaming vs MCP streaming

A klasszikus streaming és az MCP streaming működése közötti különbségek az alábbiak szerint ábrázolhatók:

| Funkció              | Klasszikus HTTP streaming       | MCP streaming (értesítések)        |
|----------------------|---------------------------------|------------------------------------|
| Fő válasz            | Darabolt                       | Egyszeri, a végén                 |
| Folyamatfrissítések  | Adatdarabokként küldve         | Értesítésekként küldve            |
| Ügyfél követelményei | Stream feldolgozása szükséges  | Üzenetkezelő implementálása       |
| Használati eset      | Nagy fájlok, AI token streamek | Folyamat, naplók, valós idejű visszajelzés |

### Megfigyelt kulcsfontosságú különbségek

További különbségek:

- **Kommunikációs minta:**
  - Klasszikus HTTP streaming: Egyszerű darabolt átvitelkódolást használ az adatok darabokban történő küldésére.
  - MCP streaming: Strukturált értesítési rendszert használ JSON-RPC protokollal.

- **Üzenetformátum:**
  - Klasszikus HTTP: Egyszerű szöveges darabok új sorokkal.
  - MCP: Strukturált LoggingMessageNotification objektumok metaadatokkal.

- **Ügyfélmegvalósítás:**
  - Klasszikus HTTP: Egyszerű ügyfél, amely feldolgozza a streaming válaszokat.
  - MCP: Összetettebb ügyfél, amely üzenetkezelőt használ különböző üzenettípusok feldolgozására.

- **Folyamatfrissítések:**
  - Klasszikus HTTP: A folyamat a fő válaszstream része.
  - MCP: A folyamat külön értesítési üzeneteken keresztül érkezik, míg a fő válasz a végén jön.

### Ajánlások

Néhány ajánlás a klasszikus streaming (pl. `/stream` végpont) és az MCP streaming közötti választáshoz:

- **Egyszerű streaming igényekhez:** A klasszikus HTTP streaming egyszerűbb és elegendő az alapvető streaming igényekhez.
- **Összetett, interaktív alkalmazásokhoz:** Az MCP streaming strukturáltabb megközelítést kínál gazdagabb metaadatokkal és az értesítések és végső eredmények szétválasztásával.
- **AI alkalmazásokhoz:** Az MCP értesítési rendszere különösen hasznos hosszú futású AI feladatokhoz, ahol a felhasználókat folyamatosan tájékoztatni kell a folyamatról.
Két meggyőző érv szól az SSE-ről Streamable HTTP-re való áttérés mellett:

- A Streamable HTTP jobb skálázhatóságot, kompatibilitást és gazdagabb értesítési támogatást kínál, mint az SSE.
- Ez az ajánlott adatátviteli mód az új MCP alkalmazásokhoz.

### Migrációs lépések

Így migrálhat az SSE-ről Streamable HTTP-re az MCP alkalmazásaiban:

- **Frissítse a szerver kódját**, hogy `transport="streamable-http"` legyen megadva az `mcp.run()`-ban.
- **Frissítse a kliens kódját**, hogy az SSE kliens helyett a `streamablehttp_client`-et használja.
- **Valósítson meg egy üzenetkezelőt** a kliensben az értesítések feldolgozásához.
- **Tesztelje a kompatibilitást** a meglévő eszközökkel és munkafolyamatokkal.

### Kompatibilitás fenntartása

Ajánlott a meglévő SSE kliensekkel való kompatibilitás fenntartása a migráció során. Íme néhány stratégia:

- Támogathatja mind az SSE-t, mind a Streamable HTTP-t, ha különböző végpontokon futtatja az adatátvitelt.
- Fokozatosan migrálja a klienseket az új adatátvitelre.

### Kihívások

Győződjön meg arról, hogy a következő kihívásokat kezeli a migráció során:

- Az összes kliens frissítése
- Az értesítések kézbesítésében lévő különbségek kezelése

## Biztonsági szempontok

A biztonság kiemelt fontosságú, amikor bármilyen szervert implementál, különösen, ha HTTP-alapú adatátvitelek, például Streamable HTTP használatáról van szó MCP-ben.

Amikor MCP szervereket valósít meg HTTP-alapú adatátvitelekkel, a biztonság elsődleges szempont, amely több támadási felület és védelmi mechanizmus alapos figyelembevételét igényli.

### Áttekintés

A biztonság kritikus fontosságú, amikor MCP szervereket tesz elérhetővé HTTP-n keresztül. A Streamable HTTP új támadási felületeket vezet be, és gondos konfigurációt igényel.

Íme néhány kulcsfontosságú biztonsági szempont:

- **Origin fejléc ellenőrzése**: Mindig ellenőrizze az `Origin` fejlécet a DNS rebinding támadások megelőzése érdekében.
- **Localhost kötés**: Helyi fejlesztés során kösse a szervereket a `localhost`-hoz, hogy elkerülje azok nyilvános internetre való kitettségét.
- **Hitelesítés**: Valósítson meg hitelesítést (pl. API kulcsok, OAuth) a termelési környezetekben.
- **CORS**: Konfigurálja a Cross-Origin Resource Sharing (CORS) szabályokat a hozzáférés korlátozására.
- **HTTPS**: Használjon HTTPS-t a termelési környezetben a forgalom titkosításához.

### Legjobb gyakorlatok

Ezenkívül itt van néhány legjobb gyakorlat, amelyet követnie kell az MCP streaming szerver biztonságának megvalósításakor:

- Soha ne bízzon meg bejövő kérésekben ellenőrzés nélkül.
- Naplózza és figyelje az összes hozzáférést és hibát.
- Rendszeresen frissítse a függőségeket a biztonsági rések javítása érdekében.

### Kihívások

Néhány kihívással szembesülhet az MCP streaming szerverek biztonságának megvalósításakor:

- A biztonság és a fejlesztés egyszerűségének egyensúlyozása
- A különböző klienskörnyezetekkel való kompatibilitás biztosítása

### Feladat: Építsen saját streaming MCP alkalmazást

**Forgatókönyv:**
Építsen egy MCP szervert és klienst, ahol a szerver feldolgoz egy elemlistát (pl. fájlokat vagy dokumentumokat), és értesítést küld minden feldolgozott elemről. A kliensnek valós időben kell megjelenítenie az értesítéseket.

**Lépések:**

1. Valósítson meg egy szerver eszközt, amely feldolgoz egy listát, és értesítéseket küld minden elemről.
2. Valósítson meg egy klienst egy üzenetkezelővel, amely valós időben megjeleníti az értesítéseket.
3. Tesztelje az implementációt a szerver és a kliens futtatásával, és figyelje meg az értesítéseket.

[Megoldás](./solution/README.md)

## További olvasmányok és következő lépések

Ha szeretné folytatni az MCP streaminggel kapcsolatos ismereteinek bővítését, ez a szakasz további forrásokat és javasolt következő lépéseket kínál fejlettebb alkalmazások építéséhez.

### További olvasmányok

- [Microsoft: Bevezetés a HTTP streamingbe](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS az ASP.NET Core-ban](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming kérések](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mi a következő lépés?

- Próbáljon meg fejlettebb MCP eszközöket építeni, amelyek streaminget használnak valós idejű elemzéshez, csevegéshez vagy együttműködő szerkesztéshez.
- Fedezze fel az MCP streaming integrálását frontend keretrendszerekkel (React, Vue stb.) az élő felhasználói felület frissítésekhez.
- Következő: [AI Toolkit használata a VSCode-hoz](../07-aitk/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.