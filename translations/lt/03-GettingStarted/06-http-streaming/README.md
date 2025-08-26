<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f1383103523fa822e1fec7ef81904d5",
  "translation_date": "2025-08-26T16:52:52+00:00",
  "source_file": "03-GettingStarted/06-http-streaming/README.md",
  "language_code": "lt"
}
-->
# HTTPS transliacija naudojant Model Context Protocol (MCP)

Šiame skyriuje pateikiamas išsamus vadovas, kaip įgyvendinti saugią, mastelio keičiamą ir realaus laiko transliaciją naudojant Model Context Protocol (MCP) per HTTPS. Jame aptariama transliacijos motyvacija, galimi transporto mechanizmai, kaip įgyvendinti HTTP transliaciją MCP, saugumo geriausios praktikos, perėjimas nuo SSE ir praktiniai patarimai, kaip kurti savo MCP transliacijos programas.

## Transporto mechanizmai ir transliacija MCP

Šiame skyriuje nagrinėjami skirtingi MCP transporto mechanizmai ir jų vaidmuo užtikrinant realaus laiko ryšio transliacijos galimybes tarp klientų ir serverių.

### Kas yra transporto mechanizmas?

Transporto mechanizmas apibrėžia, kaip duomenys keičiasi tarp kliento ir serverio. MCP palaiko kelis transporto tipus, kad atitiktų skirtingas aplinkas ir poreikius:

- **stdio**: Standartinis įvesties/išvesties mechanizmas, tinkamas vietiniams ir CLI pagrįstiems įrankiams. Paprastas, bet netinkamas žiniatinkliui ar debesų aplinkai.
- **SSE (Server-Sent Events)**: Leidžia serveriams per HTTP siųsti realaus laiko atnaujinimus klientams. Geras pasirinkimas žiniatinklio sąsajoms, tačiau ribotas mastelio keitimo ir lankstumo galimybėmis.
- **Streamable HTTP**: Modernus HTTP pagrįstas transliacijos transportas, palaikantis pranešimus ir geresnį mastelio keitimą. Rekomenduojamas daugumai gamybos ir debesų scenarijų.

### Palyginimo lentelė

Peržiūrėkite žemiau pateiktą palyginimo lentelę, kad suprastumėte šių transporto mechanizmų skirtumus:

| Transportas         | Realūs laiko atnaujinimai | Transliacija | Mastelio keitimas | Naudojimo atvejis          |
|---------------------|--------------------------|--------------|-------------------|---------------------------|
| stdio              | Ne                       | Ne           | Žemas             | Vietiniai CLI įrankiai    |
| SSE                | Taip                     | Taip         | Vidutinis         | Žiniatinklis, realūs atnaujinimai |
| Streamable HTTP    | Taip                     | Taip         | Aukštas           | Debesys, keli klientai    |

> **Patarimas:** Tinkamo transporto pasirinkimas turi įtakos našumui, mastelio keitimui ir vartotojo patirčiai. **Streamable HTTP** rekomenduojamas modernioms, mastelio keičiamoms ir debesų paruoštoms programoms.

Atkreipkite dėmesį į transportus stdio ir SSE, apie kuriuos buvo kalbėta ankstesniuose skyriuose, ir kaip streamable HTTP yra transportas, aptariamas šiame skyriuje.

## Transliacija: sąvokos ir motyvacija

Suprasti pagrindines transliacijos sąvokas ir motyvacijas yra būtina norint įgyvendinti efektyvias realaus laiko ryšio sistemas.

**Transliacija** yra tinklo programavimo technika, leidžianti duomenis siųsti ir gauti mažomis, valdomomis dalimis arba kaip įvykių seką, o ne laukti, kol bus paruoštas visas atsakymas. Tai ypač naudinga:

- Dideliems failams ar duomenų rinkiniams.
- Realūs laiko atnaujinimai (pvz., pokalbiai, progreso juostos).
- Ilgai trunkančios skaičiavimo operacijos, kai norite informuoti vartotoją.

Štai ką reikia žinoti apie transliaciją aukštu lygiu:

- Duomenys pristatomi palaipsniui, o ne visi iš karto.
- Klientas gali apdoroti duomenis, kai jie atvyksta.
- Sumažina suvokiamą vėlavimą ir pagerina vartotojo patirtį.

### Kodėl naudoti transliaciją?

Transliacijos naudojimo priežastys yra šios:

- Vartotojai gauna grįžtamąjį ryšį iš karto, o ne tik pabaigoje.
- Leidžia realaus laiko programas ir interaktyvias sąsajas.
- Efektyvesnis tinklo ir skaičiavimo išteklių naudojimas.

### Paprastas pavyzdys: HTTP transliacijos serveris ir klientas

Štai paprastas pavyzdys, kaip galima įgyvendinti transliaciją:

#### Python

**Serveris (Python, naudojant FastAPI ir StreamingResponse):**

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

**Klientas (Python, naudojant requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Šis pavyzdys demonstruoja, kaip serveris siunčia pranešimų seriją klientui, kai jie tampa prieinami, o ne laukia, kol visi pranešimai bus paruošti.

**Kaip tai veikia:**

- Serveris pateikia kiekvieną pranešimą, kai jis paruoštas.
- Klientas gauna ir spausdina kiekvieną dalį, kai ji atvyksta.

**Reikalavimai:**

- Serveris turi naudoti transliacijos atsakymą (pvz., `StreamingResponse` FastAPI).
- Klientas turi apdoroti atsakymą kaip transliaciją (`stream=True` requests).
- Turinys paprastai yra `text/event-stream` arba `application/octet-stream`.

#### Java

**Serveris (Java, naudojant Spring Boot ir Server-Sent Events):**

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

**Klientas (Java, naudojant Spring WebFlux WebClient):**

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

**Java įgyvendinimo pastabos:**

- Naudojamas Spring Boot reaktyvusis stekas su `Flux` transliacijai.
- `ServerSentEvent` užtikrina struktūrizuotą įvykių transliaciją su įvykių tipais.
- `WebClient` su `bodyToFlux()` leidžia reaktyvų transliacijos vartojimą.
- `delayElements()` simuliuoja apdorojimo laiką tarp įvykių.
- Įvykiai gali turėti tipus (`info`, `result`) geresniam kliento apdorojimui.

### Palyginimas: klasikinė transliacija vs MCP transliacija

Skirtumai tarp klasikinės transliacijos ir MCP transliacijos gali būti apibūdinti taip:

| Funkcija             | Klasikinė HTTP transliacija     | MCP transliacija (pranešimai)       |
|----------------------|---------------------------------|-------------------------------------|
| Pagrindinis atsakymas | Dalimis                        | Vienas, pabaigoje                  |
| Progreso atnaujinimai | Siunčiami kaip duomenų dalys   | Siunčiami kaip pranešimai          |
| Kliento reikalavimai | Turi apdoroti transliaciją      | Turi įgyvendinti pranešimų tvarkyklę |
| Naudojimo atvejis     | Dideli failai, AI tokenų srautai | Progresas, žurnalai, realūs laiko atsiliepimai |

### Pastebėti pagrindiniai skirtumai

Papildomai, štai keli pagrindiniai skirtumai:

- **Komunikacijos modelis:**
  - Klasikinė HTTP transliacija: Naudoja paprastą dalimis perduodamą kodavimą duomenims siųsti.
  - MCP transliacija: Naudoja struktūrizuotą pranešimų sistemą su JSON-RPC protokolu.

- **Pranešimų formatas:**
  - Klasikinė HTTP: Paprastos teksto dalys su naujomis eilutėmis.
  - MCP: Struktūrizuoti LoggingMessageNotification objektai su metaduomenimis.

- **Kliento įgyvendinimas:**
  - Klasikinė HTTP: Paprastas klientas, apdorojantis transliacijos atsakymus.
  - MCP: Sudėtingesnis klientas su pranešimų tvarkykle, apdorojančia skirtingų tipų pranešimus.

- **Progreso atnaujinimai:**
  - Klasikinė HTTP: Progresas yra pagrindinio atsakymo srauto dalis.
  - MCP: Progresas siunčiamas per atskirus pranešimus, o pagrindinis atsakymas pateikiamas pabaigoje.

### Rekomendacijos

Kai reikia pasirinkti tarp klasikinės transliacijos (kaip parodyta aukščiau naudojant `/stream` galinį tašką) ir transliacijos per MCP, rekomenduojame:

- **Paprastiems transliacijos poreikiams:** Klasikinė HTTP transliacija yra paprastesnė įgyvendinti ir pakankama pagrindiniams transliacijos poreikiams.
- **Sudėtingoms, interaktyvioms programoms:** MCP transliacija suteikia struktūrizuotą požiūrį su turtingesniais metaduomenimis ir atskyrimu tarp pranešimų ir galutinių rezultatų.
- **AI programoms:** MCP pranešimų sistema ypač naudinga ilgai trunkančioms AI užduotims, kai norite informuoti vartotojus apie progresą.

## Transliacija MCP

Gerai, jūs jau matėte keletą rekomendacijų ir palyginimų apie klasikinės transliacijos ir MCP transliacijos skirtumus. Dabar išsamiai aptarkime, kaip galite pasinaudoti transliacija MCP.

Suprasti, kaip transliacija veikia MCP sistemoje, yra būtina norint kurti interaktyvias programas, kurios teikia realaus laiko atsiliepimus vartotojams ilgai trunkančių operacijų metu.

MCP transliacija nėra apie pagrindinio atsakymo siuntimą dalimis, o apie **pranešimų** siuntimą klientui, kol įrankis apdoroja užklausą. Šie pranešimai gali apimti progreso atnaujinimus, žurnalus ar kitus įvykius.

### Kaip tai veikia

Pagrindinis rezultatas vis dar siunčiamas kaip vienas atsakymas. Tačiau pranešimai gali būti siunčiami kaip atskiri pranešimai apdorojimo metu, taip atnaujinant klientą realiu laiku. Klientas turi sugebėti apdoroti ir rodyti šiuos pranešimus.

## Kas yra pranešimas?

Mes sakėme „Pranešimas“, ką tai reiškia MCP kontekste?

Pranešimas yra žinutė, siunčiama iš serverio klientui, informuojanti apie progresą, būseną ar kitus įvykius ilgai trunkančios operacijos metu. Pranešimai pagerina skaidrumą ir vartotojo patirtį.

Pavyzdžiui, klientas turėtų siųsti pranešimą, kai pradinė rankos paspaudimo operacija su serveriu yra atlikta.

Pranešimas atrodo taip kaip JSON žinutė:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Pranešimai priklauso MCP temai, vadinamai ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Kad žurnalai veiktų, serveris turi juos įjungti kaip funkciją/galimybę taip:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Priklausomai nuo naudojamo SDK, žurnalai gali būti įjungti pagal numatytuosius nustatymus arba gali tekti juos aiškiai įjungti serverio konfigūracijoje.

Yra skirtingi pranešimų tipai:

| Lygis      | Aprašymas                     | Naudojimo atvejis               |
|------------|-------------------------------|---------------------------------|
| debug      | Išsami derinimo informacija   | Funkcijos įėjimo/išėjimo taškai |
| info       | Bendros informacinės žinutės  | Operacijos progreso atnaujinimai |
| notice     | Normalūs, bet reikšmingi įvykiai | Konfigūracijos pakeitimai      |
| warning    | Įspėjimo sąlygos              | Pasenusių funkcijų naudojimas   |
| error      | Klaidos sąlygos               | Operacijos nesėkmės             |
| critical   | Kritinės sąlygos              | Sistemos komponentų gedimai     |
| alert      | Reikia nedelsiant imtis veiksmų | Duomenų korupcija aptikta      |
| emergency  | Sistema yra nenaudojama       | Visiškas sistemos gedimas       |

## Pranešimų įgyvendinimas MCP

Norint įgyvendinti pranešimus MCP, reikia nustatyti tiek serverio, tiek kliento puses, kad jos galėtų apdoroti realaus laiko atnaujinimus. Tai leidžia jūsų programai teikti momentinį grįžtamąjį ryšį vartotojams ilgai trunkančių operacijų metu.

### Serverio pusė: pranešimų siuntimas

Pradėkime nuo serverio pusės. MCP sistemoje jūs apibrėžiate įrankius, kurie gali siųsti pranešimus apdorojant užklausas. Serveris naudoja konteksto objektą (paprastai `ctx`), kad siųstų žinutes klientui.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Ankstesniame pavyzdyje `process_files` įrankis siunčia tris pranešimus klientui, kai apdoroja kiekvieną failą. `ctx.info()` metodas naudojamas informacinių žinučių siuntimui.

Be to, norint įjungti pranešimus, įsitikinkite, kad jūsų serveris naudoja transliacijos transportą (pvz., `streamable-http`), o jūsų klientas įgyvendina pranešimų tvarkyklę, kad apdorotų pranešimus. Štai kaip galite nustatyti serverį naudoti `streamable-http` transportą:

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

Šiame .NET pavyzdyje `ProcessFiles` įrankis yra dekoruotas `Tool` atributu ir siunčia tris pranešimus klientui, kai apdoroja kiekvieną failą. `ctx.Info()` metodas naudojamas informacinių žinučių siuntimui.

Norint įjungti pranešimus jūsų .NET MCP serveryje, įsitikinkite, kad naudojate transliacijos transportą:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliento pusė: pranešimų gavimas

Klientas turi įgyvendinti pranešimų tvarkyklę, kad apdorotų ir rodytų pranešimus, kai jie atvyksta.

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

Ankstesniame kode `message_handler` funkcija tikrina, ar gaunama žinutė yra pranešimas. Jei taip, ji spausdina pranešimą; priešingu atveju ji apdoroja jį kaip įprastą serverio žinutę. Taip pat atkreipkite dėmesį, kaip `ClientSession` yra inicializuojama su `message_handler`, kad apdorotų gaunamus pranešimus.

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

Šiame .NET pavyzdyje `MessageHandler` funkcija tikrina, ar gaunama žinutė yra pranešimas. Jei taip, ji spausdina pranešimą; priešingu atveju ji apdoroja jį kaip įprastą serverio žinutę. `ClientSession` inicializuojama su pranešimų tvarkykle per `ClientSessionOptions`.

Norint įjungti pranešimus, įsitikinkite, kad jūsų serveris naudoja transliacijos transportą (pvz., `streamable-http`), o jūsų klientas įgyvendina pranešimų tvarkyklę, kad apdorotų pranešimus.

## Progreso pranešimai ir scenarijai

Šiame skyriuje paaiškinama progreso pranešimų sąvoka MCP, kodėl jie svarbūs ir kaip juos įgyvendinti naudojant Streamable HTTP. Taip pat rasite praktinę užduotį, kad sustiprintumėte savo supratimą.

Progreso pranešimai yra realaus laiko žinutės, siunčiamos iš serverio klientui ilgai trunkančių operacijų metu. Vietoj to, kad lauktų, kol visas procesas bus baigtas, serveris nuolat atnaujina klientą apie dabartinę būseną. Tai pagerina skaidrumą, vartotojo patirtį ir palengvina derinimą.

**Pavyzdys:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Kodėl naudoti progreso pranešimus?

Progreso pranešimai yra būtini dėl kelių priežasčių:

- **Geresnė vartotojo patirtis:** Vartotojai mato atnaujinimus, kai darbas progresuoja, o ne tik pabaigoje.
- **Realūs laiko atsiliepimai:** Klientai gali rodyti progreso juostas ar žurnalus, todėl programa atrodo interaktyvi.
- **Lengvesnis derinimas ir stebėjimas:** Kūrėjai ir vartotojai gali matyti, kur procesas gali būti lėtas ar užstrigęs.

### Kaip įgyvendinti progreso pranešimus

Štai kaip galite įgyvendinti progreso pranešimus MCP:

- **Serverio pusėje:** Naudokite `ctx
Yra dvi svarbios priežastys, kodėl verta pereiti nuo SSE prie Streamable HTTP:

- Streamable HTTP siūlo geresnį mastelio pritaikymą, suderinamumą ir turtingesnę pranešimų palaikymą nei SSE.
- Tai rekomenduojamas transportas naujoms MCP programoms.

### Migracijos žingsniai

Štai kaip galite pereiti nuo SSE prie Streamable HTTP savo MCP programose:

- **Atnaujinkite serverio kodą**, naudodami `transport="streamable-http"` funkcijoje `mcp.run()`.
- **Atnaujinkite kliento kodą**, naudodami `streamablehttp_client` vietoj SSE kliento.
- **Įgyvendinkite pranešimų tvarkyklę** kliente, kad apdorotumėte pranešimus.
- **Patikrinkite suderinamumą** su esamais įrankiais ir darbo procesais.

### Suderinamumo palaikymas

Rekomenduojama palaikyti suderinamumą su esamais SSE klientais migracijos metu. Štai keletas strategijų:

- Galite palaikyti tiek SSE, tiek Streamable HTTP, vykdydami abu transportus skirtinguose galiniuose taškuose.
- Palaipsniui perkelkite klientus į naują transportą.

### Iššūkiai

Užtikrinkite, kad spręstumėte šiuos iššūkius migracijos metu:

- Užtikrinti, kad visi klientai būtų atnaujinti
- Tvarkyti pranešimų pristatymo skirtumus

## Saugumo aspektai

Saugumas turėtų būti pagrindinis prioritetas, įgyvendinant bet kokį serverį, ypač naudojant HTTP pagrįstus transportus, tokius kaip Streamable HTTP MCP.

Įgyvendinant MCP serverius su HTTP pagrįstais transportais, saugumas tampa svarbia problema, reikalaujančia atidžiai apsvarstyti įvairius atakos vektorius ir apsaugos mechanizmus.

### Apžvalga

Saugumas yra itin svarbus, kai MCP serveriai yra pasiekiami per HTTP. Streamable HTTP atveria naujus atakos paviršius ir reikalauja kruopštaus konfigūravimo.

Štai keletas pagrindinių saugumo aspektų:

- **Origin antraštės validacija**: Visada tikrinkite `Origin` antraštę, kad išvengtumėte DNS peradresavimo atakų.
- **Localhost susiejimas**: Vietiniam vystymui susiekite serverius su `localhost`, kad išvengtumėte jų viešo prieinamumo internete.
- **Autentifikacija**: Įgyvendinkite autentifikaciją (pvz., API raktus, OAuth) gamybos aplinkoje.
- **CORS**: Konfigūruokite Cross-Origin Resource Sharing (CORS) politiką, kad apribotumėte prieigą.
- **HTTPS**: Naudokite HTTPS gamybos aplinkoje, kad užšifruotumėte srautą.

### Geriausios praktikos

Be to, štai keletas geriausių praktikų, kurių reikėtų laikytis įgyvendinant saugumą MCP srautinio perdavimo serveryje:

- Niekada nepasitikėkite gaunamais užklausomis be validacijos.
- Registruokite ir stebėkite visą prieigą ir klaidas.
- Reguliariai atnaujinkite priklausomybes, kad pašalintumėte saugumo pažeidžiamumus.

### Iššūkiai

Įgyvendinant saugumą MCP srautinio perdavimo serveriuose, susidursite su tam tikrais iššūkiais:

- Saugumo ir vystymo paprastumo balansas
- Suderinamumo užtikrinimas su įvairiomis klientų aplinkomis

### Užduotis: Sukurkite savo srautinę MCP programą

**Scenarijus:**
Sukurkite MCP serverį ir klientą, kur serveris apdoroja elementų sąrašą (pvz., failus ar dokumentus) ir siunčia pranešimą apie kiekvieną apdorotą elementą. Klientas turėtų rodyti kiekvieną pranešimą realiuoju laiku.

**Žingsniai:**

1. Įgyvendinkite serverio įrankį, kuris apdoroja sąrašą ir siunčia pranešimus apie kiekvieną elementą.
2. Įgyvendinkite klientą su pranešimų tvarkykle, kad realiuoju laiku rodytų pranešimus.
3. Išbandykite savo įgyvendinimą, paleisdami tiek serverį, tiek klientą, ir stebėkite pranešimus.

[Sprendimas](./solution/README.md)

## Papildoma literatūra ir kas toliau?

Norėdami tęsti savo kelionę su MCP srautinio perdavimo technologija ir plėsti savo žinias, šiame skyriuje pateikiami papildomi ištekliai ir siūlomi tolesni žingsniai kuriant pažangesnes programas.

### Papildoma literatūra

- [Microsoft: Įvadas į HTTP srautinį perdavimą](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Srautinės užklausos](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Kas toliau?

- Išbandykite kurti pažangesnius MCP įrankius, kurie naudoja srautinį perdavimą realaus laiko analitikai, pokalbiams ar bendradarbiavimui redaguojant.
- Tyrinėkite MCP srautinio perdavimo integraciją su front-end karkasais (React, Vue ir kt.) realaus laiko UI atnaujinimams.
- Toliau: [AI įrankių naudojimas VSCode](../07-aitk/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.