# HTTPS streamování s protokolem Model Context Protocol (MCP)

Tato kapitola poskytuje komplexního průvodce implementací bezpečného, škálovatelného a real-time streamování pomocí Model Context Protocol (MCP) s využitím HTTPS. Pokrývá motivaci ke streamování, dostupné transportní mechanismy, jak implementovat streamovatelný HTTP v MCP, nejlepší bezpečnostní postupy, migraci ze SSE a praktické rady pro vytváření vlastních aplikací streamující MCP.

> **Výhled do budoucnosti:** tato lekce popisuje Streamovatelný HTTP podle **MCP Specifikace 2025-11-25**, kde se během `initialize` navazuje a připíná session pomocí hlavičky `Mcp-Session-Id`. Release kandidát `2026-07-28` zcela odstraňuje handshake a ID session, čímž je každý požadavek samostatný a směrovatelný na jakýkoli server bez sticky sessions. Detaily jsou v [Co se mění v MCP: Release kandidát 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transportní mechanismy a streamování v MCP

Tato část zkoumá různé dostupné transportní mechanismy v MCP a jejich roli v umožnění streamovacích schopností pro real-time komunikaci mezi klienty a servery.

### Co je transportní mechanismus?

Transportní mechanismus definuje, jak jsou data vyměňována mezi klientem a serverem. MCP podporuje několik typů transportů, aby vyhověl různým prostředím a požadavkům:

- **stdio**: Standardní vstup/výstup, vhodný pro lokální a CLI nástroje. Jednoduchý, ale nevhodný pro web nebo cloud.
- **SSE (Server-Sent Events)**: Umožňuje serverům posílat klientům real-time aktualizace přes HTTP. Dobré pro webová uživatelská rozhraní, ale omezené v škálovatelnosti a flexibilitě. Od MCP specifikace 2025-06-18 byl samostatný SSE transport zastaralý a nahrazen transportem "Streamovatelný HTTP".
- **Streamovatelný HTTP**: Moderní HTTP založený streamovací transport podporující notifikace a lepší škálovatelnost. Doporučený pro většinu produkčních a cloud scénářů.

### Srovnávací tabulka

Podívejte se na srovnávací tabulku níže pro pochopení rozdílů mezi těmito transportními mechanismy:

| Transport         | Real-time aktualizace | Streamování | Škálovatelnost | Použití                 |
|-------------------|-----------------------|-------------|----------------|-------------------------|
| stdio             | Ne                    | Ne          | Nízká          | Lokální CLI nástroje    |
| SSE               | Ano                   | Ano         | Střední        | Web, real-time aktualizace |
| Streamovatelný HTTP | Ano                  | Ano         | Vysoká         | Cloud, multi-klient     |

> **Tip:** Výběr správného transportu ovlivňuje výkon, škálovatelnost a uživatelský zážitek. **Streamovatelný HTTP** je doporučený pro moderní, škálovatelné a cloudové aplikace.

Všimněte si transportů stdio a SSE, které byly ukázány v předchozích kapitolách, a jak streamovatelný HTTP je transportem pokrytým v této kapitole.

## Streamování: Koncepty a motivace

Porozumění základním konceptům a motivacím za streamováním je zásadní pro implementaci efektivních real-time komunikačních systémů.

**Streamování** je technika v síťovém programování, která umožňuje posílat a přijímat data v malých, zvládnutelných částech nebo jako posloupnost událostí, místo čekání na kompletní odpověď. To je zvláště užitečné pro:

- Velké soubory nebo datové sady.
- Real-time aktualizace (např. chat, progress bary).
- Dlouhotrvající výpočty, kde chcete uživatele informovat.

Zde je, co potřebujete vědět o streamování na vysoké úrovni:

- Data jsou doručována postupně, ne najednou.
- Klient může zpracovávat data, jakmile přijdou.
- Snižuje vnímanou latenci a zlepšuje uživatelský zážitek.

### Proč používat streamování?

Důvody pro použití streamování jsou následující:

- Uživatelé dostávají zpětnou vazbu okamžitě, ne až na konci
- Umožňuje real-time aplikace a responzivní UI
- Efektivnější využití síťových a výpočetních zdrojů

### Jednoduchý příklad: HTTP streamovací server a klient

Zde je jednoduchý příklad, jak může být streamování implementováno:

#### Python

**Server (Python, použití FastAPI a StreamingResponse):**

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

**Klient (Python, použití requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tento příklad ukazuje server, který posílá sérii zpráv klientovi, jakmile jsou dostupné, místo čekání na všechny zprávy najednou.

**Jak to funguje:**

- Server postupně posílá každou zprávu, jak je připravena.
- Klient přijímá a vypisuje každý kousek, jak dorazí.

**Požadavky:**

- Server musí používat streamovací odpověď (např. `StreamingResponse` ve FastAPI).
- Klient musí zpracovat odpověď jako stream (`stream=True` v requests).
- Content-Type je obvykle `text/event-stream` nebo `application/octet-stream`.

#### Java

**Server (Java, použití Spring Boot a Server-Sent Events):**

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

**Klient (Java, použití Spring WebFlux WebClient):**

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

**Poznámky k implementaci v Javě:**

- Používá reaktivní stack Spring Boot s `Flux` pro streamování
- `ServerSentEvent` poskytuje strukturované streamování událostí s typy událostí
- `WebClient` s `bodyToFlux()` umožňuje konzumaci reaktivního streamu
- `delayElements()` simuluje zpracování času mezi událostmi
- Události mohou mít typy (`info`, `result`) pro lepší zpracování klientem

### Srovnání: Klasické streamování vs MCP streamování

Rozdíly mezi klasickým streamováním a MCP streamováním lze zachytit takto:

| Vlastnost              | Klasické HTTP streamování      | MCP streamování (notifikace)    |
|------------------------|-------------------------------|---------------------------------|
| Hlavní odpověď          | Po částech                    | Jedna, na konci                 |
| Progresní aktualizace   | Posílány jako datové bloky    | Posílány jako notifikace         |
| Požadavky na klienta    | Musí zpracovat stream         | Musí implementovat zprávový handler |
| Případy použití         | Velké soubory, AI token stream | Progres, logy, real-time zpětná vazba |

### Pozorované klíčové rozdíly

Dále zde jsou některé klíčové rozdíly:

- **Komunikační vzor:**
  - Klasické HTTP streamování: Používá jednoduché chunked transfer kódování k posílání dat po částech
  - MCP streamování: Používá strukturovaný systém notifikací s JSON-RPC protokolem

- **Formát zprávy:**
  - Klasické HTTP: Prostý text chunků s novými řádky
  - MCP: Strukturované objekty LoggingMessageNotification s metadata

- **Implementace klienta:**
  - Klasické HTTP: Jednoduchý klient, který zpracovává streamované odpovědi
  - MCP: Sofistikovanější klient s zprávovým handlerem ke zpracování různých typů zpráv

- **Progresní aktualizace:**
  - Klasické HTTP: Progres je součástí hlavního streamu odpovědi
  - MCP: Progres je zasílán přes samostatné zprávy notifikací, zatímco hlavní výsledek přijde na konci

### Doporučení

Doporučujeme následující při rozhodování mezi klasickým streamováním (jako toho end-pointu `/stream`, který jsme ukázali výše) a streamováním pomocí MCP.

- **Pro jednoduché potřeby streamování:** Klasické HTTP streamování je snazší na implementaci a dostačující pro základní potřeby.

- **Pro komplexní, interaktivní aplikace:** MCP streamování poskytuje strukturovanější přístup s bohatými metadata a oddělení notifikací a finálních výsledků.

- **Pro AI aplikace:** Notifikační systém MCP je zvlášť užitečný pro dlouhotrvající AI úlohy, kde chcete uživatele informovat o průběhu.

## Streamování v MCP

Takže jste zatím viděli některá doporučení a srovnání rozdílů mezi klasickým streamováním a streamováním v MCP. Pojďme nyní podrobně vysvětlit, jak přesně můžete streamování v MCP využít.

Porozumění tomu, jak streamování funguje v rámci MCP, je zásadní pro vytváření responzivních aplikací, které poskytují real-time zpětnou vazbu uživatelům během dlouhotrvajících operací.

V MCP nejde o posílání hlavní odpovědi po částech, ale o posílání **notifikací** klientovi během zpracování požadavku nástrojem. Tyto notifikace mohou obsahovat aktualizace o průběhu, logy nebo jiné události.

### Jak to funguje

Hlavní výsledek je stále posílán jako jedna odpověď. Nicméně během zpracování mohou být odesílány notifikace jako samostatné zprávy, které aktualizují klienta v reálném čase. Klient musí tyto notifikace umět zpracovat a zobrazit.

## Co je to notifikace?

Řekli jsme "notifikace", co to znamená v kontextu MCP?

Notifikace je zpráva zasílaná ze serveru klientovi k informování o průběhu, stavu nebo jiných událostech během dlouhotrvající operace. Notifikace zlepšují transparentnost a uživatelský zážitek.

Například klient by měl odeslat notifikaci jakmile je inicializováno spojení se serverem.

Notifikace vypadá jako JSON zpráva:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifikace patří do tématu v MCP nazývaném ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Oznámení o zastarání:** release kandidát MCP specifikace `2026-07-28` označuje prvek Logging jako zastaralý ve prospěch `stderr` pro stdio transporty a OpenTelemetry pro strukturovanou observabilitu. Logging bude fungovat ve verzi `2025-11-25` a alespoň rok po formálním ukončení podpory. Více na [Co se mění v MCP: Release kandidát 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Pro správnou funkci logování musí server tuto schopnost aktivovat takto:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> V závislosti na použitém SDK může být logování ve výchozím nastavení povoleno, nebo je třeba aktivovat explicitně v konfiguraci serveru.

Existují různé typy notifikací:

| Úroveň     | Popis                         | Příklad použití                   |
|-----------|-------------------------------|----------------------------------|
| debug     | Detailní informace pro debugování | Vstup/exit do funkcí           |
| info      | Obecné informační zprávy        | Aktualizace průběhu operace      |
| notice    | Normální, ale významné události | Změny konfigurace               |
| warning   | Varovné stavy                  | Používání zastaralých funkcí     |
| error     | Chybové stavy                  | Selhání operace                  |
| critical  | Kritické stavy                 | Selhání komponent systému       |
| alert     | Nutná okamžitá akce            | Zjištěná korupce dat             |
| emergency | Systém je nepoužitelný         | Kompletní selhání systému        |

## Implementace notifikací v MCP

Pro implementaci notifikací v MCP je potřeba nastavit jak server, tak klienta, aby zvládli real-time aktualizace. To umožňuje vaší aplikaci poskytovat okamžitou zpětnou vazbu uživatelům během dlouhotrvajících operací.

### Serverová strana: Odesílání notifikací

Začněme serverovou stranou. V MCP definujete nástroje, které mohou posílat notifikace během zpracování požadavků. Server používá objekt context (obvykle `ctx`) k odesílání zpráv klientovi.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V předchozím příkladu nástroj `process_files` posílá klientovi tři notifikace při zpracování každého souboru. Metoda `ctx.info()` slouží k odesílání informačních zpráv.

K povolení notifikací ujistěte se, že váš server používá streamovací transport (např. `streamable-http`) a váš klient implementuje zprávový handler pro zpracování notifikací. Zde je ukázka, jak nastavit server k použití transportu `streamable-http`:

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

V tomto příkladu .NET je nástroj `ProcessFiles` označen atributem `Tool` a posílá klientovi tři notifikace během zpracování každého souboru. Metoda `ctx.Info()` slouží k odesílání informačních zpráv.

Pro povolení notifikací na vašem .NET MCP serveru ujistěte se, že používáte streamovací transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientská strana: Příjem notifikací

Klient musí implementovat zprávový handler pro zpracování a zobrazování notifikací, jakmile přijdou.

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

V předchozím kódu funkce `message_handler` zjišťuje, jestli je příchozí zpráva notifikací. Pokud ano, vypisuje ji; jinak ji zpracovává jako běžnou serverovou zprávu. Také si všimněte, že `ClientSession` je inicializována s `message_handler` k obsluze přicházejících notifikací.

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

V tomto .NET příkladu funkce `MessageHandler` zjišťuje, jestli je příchozí zpráva notifikací. Pokud ano, vypisuje ji; jinak ji zpracovává jako běžnou serverovou zprávu. `ClientSession` je inicializován se zprávovým handlerem přes `ClientSessionOptions`.

Pro povolení notifikací ujistěte se, že server používá streamovací transport (např. `streamable-http`) a klient implementuje zprávový handler pro jejich zpracování.

## Progresní notifikace a scénáře

Tato část vysvětluje koncept progresních notifikací v MCP, proč jsou důležité a jak je implementovat pomocí Streamovatelného HTTP. Také zde najdete praktické zadání pro upevnění znalostí.

Progresní notifikace jsou real-time zprávy posílané ze serveru klientovi během dlouhotrvajících operací. Místo čekání na dokončení procesu server průběžně klienta informuje o aktuálním stavu. To zlepšuje transparentnost, uživatelský zážitek a usnadňuje ladění.

**Příklad:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Proč používat progresní notifikace?

Progresní notifikace jsou zásadní z několika důvodů:

- **Lepší uživatelský zážitek:** Uživatelé vidí průběžné aktualizace, ne jen na konci.
- **Real-time zpětná vazba:** Klienti mohou zobrazovat progress bary nebo logy, což dělá aplikaci responzivní.
- **Snazší ladění a monitoring:** Vývojáři i uživatelé mohou vidět, kde může být proces pomalý nebo zablokovaný.

### Jak implementovat progresní notifikace

Zde je, jak můžete implementovat progresní notifikace v MCP:

- **Na serveru:** Použijte `ctx.info()` nebo `ctx.log()` k odesílání notifikací při zpracování každé položky. Toto pošle zprávu klientovi dříve, než je hotový hlavní výsledek.
- **Na klientovi:** Implementujte zprávový handler, který poslouchá a zobrazuje notifikace jak přicházejí. Tento handler rozlišuje mezi notifikacemi a finálním výsledkem.

**Příklad serveru:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Příklad klienta:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Bezpečnostní úvahy

Bezpečnost by měla být nejvyšší prioritou při implementaci jakéhokoli serveru, zejména při použití HTTP založených přenosů, jako je Streamable HTTP v MCP.

Při implementaci MCP serverů s HTTP založenými přenosy se bezpečnost stává klíčovou záležitostí, která vyžaduje pečlivé sledování různých vektorů útoku a ochranných mechanismů.

### Přehled

Bezpečnost je kritická při zpřístupňování MCP serverů přes HTTP. Streamable HTTP přináší nové útokové plochy a vyžaduje pečlivou konfiguraci.

Zde jsou některé klíčové bezpečnostní úvahy:

- **Validace hlavičky Origin**: Vždy ověřujte hlavičku `Origin`, abyste zabránili DNS rebinding útokům.
- **Vazba na localhost**: Pro lokální vývoj připojujte servery k `localhost`, aby nebyly vystaveny veřejnému internetu.
- **Autentizace**: Implementujte autentizaci (např. API klíče, OAuth) pro produkční nasazení.
- **CORS**: Konfigurujte zásady Cross-Origin Resource Sharing (CORS) pro omezení přístupu.
- **HTTPS**: Používejte HTTPS v produkci k šifrování provozu.

### Nejlepší postupy

Dále zde jsou některé nejlepší postupy, které je třeba dodržovat při implementaci zabezpečení ve vašem MCP streamingovém serveru:

- Nikdy nevěřte příchozím požadavkům bez ověření.
- Logujte a monitorujte veškerý přístup a chyby.
- Pravidelně aktualizujte závislosti kvůli záplatování bezpečnostních zranitelností.

### Výzvy

Při implementaci bezpečnosti u MCP streamingových serverů se setkáte s několika výzvami:

- Vyvážení bezpečnosti a snadnosti vývoje
- Zajištění kompatibility s různými klientskými prostředími


## Přechod ze SSE na Streamable HTTP

Pro aplikace, které aktuálně používají Server-Sent Events (SSE), přechod na Streamable HTTP přináší rozšířené možnosti a lepší dlouhodobou udržitelnost vašich implementací MCP.

### Proč upgradovat?

Existují dva přesvědčivé důvody pro upgrade ze SSE na Streamable HTTP:

- Streamable HTTP nabízí lepší škálovatelnost, kompatibilitu a bohatší podporu notifikací než SSE.
- Je doporučeným přenosem pro nové MCP aplikace.

### Kroky migrace

Zde je postup, jak migrovat ze SSE na Streamable HTTP ve vašich MCP aplikacích:

- **Aktualizujte serverový kód** pro použití `transport="streamable-http"` v `mcp.run()`.
- **Aktualizujte klientský kód** pro použití `streamablehttp_client` místo SSE klienta.
- **Implementujte obsluhu zpráv** v klientovi pro zpracování notifikací.
- **Testujte kompatibilitu** s existujícími nástroji a pracovními postupy.

### Udržování kompatibility

Doporučuje se během migrace zachovat kompatibilitu se stávajícími SSE klienty. Zde jsou některé strategie:

- Můžete podporovat oba typy přenosů, SSE i Streamable HTTP, spuštěním obou na různých koncových bodech.
- Postupně migrujte klienty na nový přenos.

### Výzvy

Ujistěte se, že během migrace řešíte následující výzvy:

- Zajištění aktualizace všech klientů
- Řešení rozdílů v doručování notifikací

### Zadání: Vybudujte si vlastní streamingovou MCP aplikaci

**Scénář:**
Vytvořte MCP server a klienta, kde server zpracovává seznam položek (např. soubory nebo dokumenty) a posílá notifikaci pro každou zpracovanou položku. Klient by měl zobrazovat každou notifikaci po jejím přijetí.

**Kroky:**

1. Implementujte serverový nástroj, který zpracovává seznam a posílá notifikace pro jednotlivé položky.
2. Implementujte klienta s obsluhou zpráv, který zobrazuje notifikace v reálném čase.
3. Otestujte svou implementaci spuštěním serveru i klienta a sledujte notifikace.

[Řešení](./solution/README.md)

## Další čtení a co dál?

Pro pokračování v práci s MCP streamingem a rozšíření znalostí tato sekce poskytuje další zdroje a navrhované další kroky pro budování pokročilejších aplikací.

### Další čtení

- [Microsoft: Úvod do HTTP streamingu](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Co dál?

- Zkuste vyvíjet pokročilejší MCP nástroje, které využívají streaming pro analytiku v reálném čase, chat nebo kolaborativní úpravy.
- Prozkoumejte integraci MCP streamingu s frontendovými frameworky (React, Vue, atd.) pro živé aktualizace UI.
- Dále: [Využití AI Toolkit pro VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->