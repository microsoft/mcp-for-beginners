# HTTPS srautinis perdavimas naudojant Model Context Protocol (MCP)

Šiame skyriuje pateikiamas išsamus vadovas, kaip įgyvendinti saugų, mastelį keičiančią ir realaus laiko srautinę perdavimą naudojant Model Context Protocol (MCP) per HTTPS. Apžvelgiama srautinio perdavimo prasmė, galimi perdavimo mechanizmai, kaip įgyvendinti srautinį HTTP MCP, geriausios saugumo praktikos, migravimas nuo SSE, praktinės rekomendacijos kuriant savo srautinio perdavimo MCP programas.

> **Žvilgsnis į ateitį:** ši pamoka aprašo Streamable HTTP pagal **MCP specifikaciją 2025-11-25**, kai seansas užmezgamas per `initialize` ir susiejamas su antrašte `Mcp-Session-Id`. `2026-07-28` leidimo kandidatas visiškai pašalina rankos paspaudimą ir seanso ID, todėl kiekvienas užklausimas yra savarankiškas ir nukreipiamas į bet kurią serverio instanciją be sticky sessions. Daugiau detalių žr. [Kas keičiasi MCP: 2026-07-28 leidimo kandidatas](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Perdavimo mechanizmai ir srautinės transliacijos MCP

Šiame skyriuje nagrinėjami MCP prieinami skirtingi perdavimo mechanizmai ir jų vaidmuo leidžiant realaus laiko srautinį ryšį tarp klientų ir serverių.

### Kas yra perdavimo mechanizmas?

Perdavimo mechanizmas apibrėžia, kaip duomenys keičiasi tarp kliento ir serverio. MCP palaiko kelis perdavimo tipus, skirtus skirtingoms aplinkoms ir poreikiams:

- **stdio**: Standartinė įvestis/išvestis, tinkama vietiniams ir CLI įrankiams. Paprasta, bet netinka internetui ar debesijai.
- **SSE (Server-Sent Events)**: Leidžia serveriams siųsti realaus laiko atnaujinimus klientams per HTTP. Tinka internetinėms UI, tačiau ribota mastelio keitimo ir lankstumo galimybė. Nuo MCP specifikacijos 2025-06-18 atskiro SSE perdavimo atsisakyta ir pakeista "Streamable HTTP" perdavimu.
- **Streamable HTTP**: Modernus HTTP pagrindu veikiantis srautinio perdavimo mechanizmas, palaikantis pranešimus ir geresnį mastelio keitimą. Rekomenduojamas daugumai produkcinių ir debesijos scenarijų.

### Palyginimo lentelė

Žemiau pateiktoje lentelėje galite pamatyti šių perdavimo mechanizmų skirtumus:

| Perdavimas         | Realio laiko atnaujinimai | Srautinis perdavimas | Mastelį keičiantis | Naudojimo atvejis       |
|-------------------|--------------------------|---------------------|--------------------|-------------------------|
| stdio             | Ne                       | Ne                  | Žemas             | Vietiniai CLI įrankiai  |
| SSE               | Taip                     | Taip                | Vidutinis          | Internetas, realaus laiko atnaujinimai |
| Streamable HTTP   | Taip                     | Taip                | Aukštas            | Debesija, daug klientų  |

> **Patartina:** Teisingas perdavimo metodo pasirinkimas įtakoja našumą, mastelio keitimą ir naudotojo patirtį. **Streamable HTTP** rekomenduojamas modernioms, lanksčioms ir debesijos programoms.

Atkreipkite dėmesį į perdavimus stdio ir SSE, pateiktus ankstesniuose skyriuose, ir kaip šio skyriaus tema yra srautinio HTTP perdavimas.

## Srautinio perdavimo pagrindai ir motyvacija

Suprasti srautinio perdavimo pagrindines sąvokas ir motyvus yra būtina norint efektyviai įgyvendinti realaus laiko komunikacijos sistemas.

**Srautinimas** yra tinklo programavimo technika, kai duomenys siunčiami ir gaunami mažomis, valdomomis dalimis arba kaip įvykių sekos, o ne laukti visos atsakymo paruošimo. Tai ypač naudinga:

- Dideliems failams ar duomenų rinkiniams.
- Realio laiko atnaujinimams (pvz., pokalbiams, progreso juostoms).
- Ilgalaikiams skaičiavimams, kai norite vartotoją informuoti apie eigą.

Štai ką svarbu žinoti apie srautinį perdavimą plačiai:

- Duomenys perduodami progresyviai, ne iš karto visi.
- Klientas gali apdoroti duomenis juos gavęs.
- Sumažina suvokiamą vėlavimą ir pagerina naudotojo patirtį.

### Kodėl naudoti srautinį perdavimą?

Srautinio perdavimo priežastys yra šios:

- Vartotojai iš karto gauna atsiliepimus, ne tik pabaigoje.
- Leidžia kurti realaus laiko programas ir reaguojančias UI.
- Efektyvesnis tinklo ir skaičiavimo išteklių naudojimas.

### Paprastas pavyzdys: HTTP srautinio perdavimo serveris ir klientas

Štai paprastas pavyzdys, kaip galima įgyvendinti srautinį perdavimą:

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

Šiame pavyzdyje serveris siunčia žinučių seriją klientui, kai jos tampa prieinamos, o ne laukia visų žinučių paruošimo.

**Kaip tai veikia:**

- Serveris atiduoda kiekvieną žinutę ją paruošęs.
- Klientas gauna ir išspausdina kiekvieną dalį ją gavęs.

**Reikalavimai:**

- Serveris turi naudoti srautinį atsaką (pvz., `StreamingResponse` FastAPI).
- Klientas turi apdoroti atsakymą kaip srautą (`stream=True` requests).
- Turinio tipas paprastai `text/event-stream` arba `application/octet-stream`.

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

- Naudoja Spring Boot reaktyviąją staktę su `Flux` srautui
- `ServerSentEvent` teikia struktūruotą įvykių srautą su įvykių tipais
- `WebClient` su `bodyToFlux()` leidžia reaguojantį srautinį vartojimą
- `delayElements()` simuliuoja apdorojimo laiką tarp įvykių
- Įvykiai gali turėti tipus (`info`, `result`) geresniam kliento apdorojimui

### Palyginimas: klasikinis srautinimas vs MCP srautinimas

Skirtumai tarp klasikinio srautinio perdavimo ir MCP srautinio perdavimo galima apibūdinti taip:

| Ypatybė               | Klasikinis HTTP srautas        | MCP srautas (Pranešimai)      |
|-----------------------|-------------------------------|-------------------------------|
| Pagrindinis atsakymas  | Dalijamas į dalis              | Vienas, pabaigoje             |
| Progreso atnaujinimai | Siunčiami kaip duomenų dalys   | Siunčiami kaip pranešimai     |
| Kliento reikalavimai   | Privalo apdoroti srautą        | Privalo įgyvendinti žinučių apdorojimą |
| Naudojimo atvejis      | Dideli failai, AI žinučių srautai | Progresas, žurnalai, realaus laiko atsiliepimai |

### Pagrindiniai skirtumai

Be to, yra keletas žymių skirtumų:

- **Komunikacijos modelis:**
  - Klasikinis HTTP srautas: naudoja paprastą dalijamo perdavimo kodavimą duomenims siųsti dalimis
  - MCP srautas: naudoja struktūruotą pranešimų sistemą su JSON-RPC protokolu

- **Žinutės formatas:**
  - Klasikinis HTTP: paprastos teksto dalys su naujomis eilutėmis
  - MCP: struktūruoti LoggingMessageNotification objektai su meta duomenimis

- **Kliento įgyvendinimas:**
  - Klasikinis HTTP: paprastas klientas, apdorojantis srautinius atsakymus
  - MCP: sudėtingesnis klientas su žinučių apdorojimo funkcija, leidžiančia apdoroti skirtingo tipo žinutes

- **Progreso atnaujinimai:**
  - Klasikinis HTTP: progresas yra pagrindiniame srautiniame atsakyme
  - MCP: progresas siunčiamas atskirais pranešimų pranešimais, o pagrindinis atsakymas ateina pabaigoje

### Rekomendacijos

Kai ką rekomenduojame rinktis tarp klasikinio srautinio perdavimo (kaip parodyta naudojant `/stream` galinį tašką) ir MCP srautinio perdavimo.

- **Paprastiems srautinio perdavimo poreikiams:** klasikinis HTTP srautas yra paprastas įgyvendinti ir pakankamas pagrindiniam srautiniam perdavimui.

- **Sudėtingoms, interaktyvioms programoms:** MCP srautas suteikia labiau struktūruotą požiūrį su turtingesniais meta duomenimis ir atskyrimu tarp pranešimų ir galutinių rezultatų.

- **AI programoms:** MCP pranešimų sistema ypač naudinga ilgalaikiams AI užduotims, kur norima nuolat informuoti vartotojus apie progresą.

## Srautinio perdavimo įgyvendinimas MCP

Taigi, matėte kai kurias rekomendacijas ir palyginimus, kaip skiriasi klasikinis srautas nuo srauto MCP. Pažiūrėkime detaliai, kaip galite pasinaudoti srautiniu perdavimu MCP.

Suprasti, kaip veikia srautas MCP sistemoje, yra svarbu kuriant reagavusias programas, kurios suteikia realaus laiko atsiliepimą vartotojams per ilgai trunkančias operacijas.

MCP srautas nėra pagrindinio atsakymo siuntimas dalimis, o **pranešimų** siuntimas klientui, kai įrankis apdoroja užklausą. Šie pranešimai gali apimti progreso atnaujinimus, žurnalus ar kitus įvykius.

### Kaip tai veikia

Pagrindinis rezultatas vis tiek siunčiamas kaip vienas atsakymas. Tačiau pranešimai gali būti siunčiami atskirai apdorojimo metu ir taip realiu laiku atnaujinti klientą. Klientas turi sugebėti apdoroti ir parodyti šiuos pranešimus.

## Kas yra pranešimas (notification)?

Sakėme "Pranešimas", ką tai reiškia MCP kontekste?

Pranešimas yra žinutė, siunčiama iš serverio klientui, informuojanti apie progresą, būseną ar kitus įvykius per ilgai trunkančią operaciją. Pranešimai gerina skaidrumą ir naudotojo patirtį.

Pavyzdžiui, klientas turėtų išsiųsti pranešimą, kai pradinė rankos paspauda su serveriu įvykdyta.

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

Pranešimai priskiriami MCP temai, vadinamai ["Žurnalas"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Branginimo pranešimas:** `2026-07-28` MCP specifikacijos leidimo kandidatas žymi Žurnalą kaip branginamą naudoti `stderr` stdio perdavimams ir OpenTelemetry struktūruotam stebėjimui. Žurnalas veikia `2025-11-25` ir bent metus po oficialaus branginimo pabaigos. Daugiau žr. [Kas keičiasi MCP: 2026-07-28 leidimo kandidatas](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Norint įjungti žurnalą, serveris turi tai aktyvuoti kaip funkciją/galimybę taip:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Priklausomai nuo naudojamo SDK, žurnalas gali būti įjungtas pagal numatytuosius nustatymus arba jį gali tekti įjungti serverio konfigūracijoje.

Yra skirtingi pranešimų tipai:

| Lygmuo   | Aprašymas                    | Pavyzdinė naudojimo sritis    |
|---------|------------------------------|------------------------------|
| debug   | Išsamios derinimo informacijos | Funkcijų įėjimai/išeigos     |
| info    | Bendros informacinės žinutės   | Operacijos progreso atnaujinimai |
| notice  | Normalių, bet reikšmingų įvykių | Konfigūracijos pakeitimai    |
| warning | Įspėjimo būsenos              | Pasenusių funkcijų naudojimas |
| error   | Klaidos būsenos               | Operacijų klaidos            |
| critical| Kritinės būsenos              | Sistemos komponentų gedimai  |
| alert   | Veiksmai turi būti atlikti nedelsiant | Aptikta duomenų korupcija |
| emergency| Sistema neveikia               | Sistemos visiškas gedimas    |

## Pranešimų įgyvendinimas MCP

Norėdami įgyvendinti pranešimus MCP, turite paruošti tiek serverio, tiek kliento puses realaus laiko atnaujinimų apdorojimui. Tai leidžia programai suteikti nedelsiamą atsiliepimą vartotojams ilgai trunkančių operacijų metu.

### Serverio pusė: pranešimų siuntimas

Pradėkime nuo serverio pusės. MCP apibrėžia įrankius, galinčius siųsti pranešimus atliekant užklausų apdorojimą. Serveris naudoja konteksto objektą (dažniausiai `ctx`) pranešimams siųsti klientui.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Ankstesniame pavyzdyje `process_files` įrankis siunčia tris pranešimus klientui, apdorodamas kiekvieną failą. `ctx.info()` metodas skirtas informacinių žinučių siuntimui.

Be to, kad įjungtumėte pranešimus, įsitikinkite, kad serveris naudoja srautinio perdavimo perkėlimo mechanizmą (pvz., `streamable-http`) ir klientas įgyvendina žinučių apdorojimo funkciją pranešimų apdorojimui. Štai kaip galima nustatyti serverį naudoti `streamable-http` perkėlimą:

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

Šiame .NET pavyzdyje `ProcessFiles` įrankis paženklintas atributu `Tool` ir siunčia tris pranešimus klientui apdorodamas kiekvieną failą. `ctx.Info()` metodas siunčia informacines žinutes.

Norint įjungti pranešimus .NET MCP serveryje, užtikrinkite, kad naudojate srautinio perdavimo perkėlimą:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliento pusė: pranešimų gavimas

Klientas turi įgyvendinti žinučių apdorojimo funkciją, kuri apdoroja ir rodo pranešimus, kai jie atvyksta.

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

Aukščiau pateiktame kode funkcija `message_handler` tikrina, ar atėjusi žinutė yra pranešimas. Jei taip, ji išspausdina pranešimą; kitu atveju apdoroja jį kaip įprastą serverio žinutę. Taip pat atkreipkite dėmesį, kaip `ClientSession` inicializuojama su `message_handler`, skirtu gaunamiems pranešimams apdoroti.

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

Šiame .NET pavyzdyje funkcija `MessageHandler` tikrina, ar gaunama žinutė yra pranešimas. Jei taip, ji išspausdina pranešimą; kitu atveju apdoroja kaip įprastą serverio žinutę. `ClientSession` inicializuojama su žinučių apdorojimo funkcija per `ClientSessionOptions`.

Norėdami įjungti pranešimus, įsitikinkite, kad serveris naudoja srautinį perdavimo perkėlimą (pvz., `streamable-http`), o klientas įgyvendina žinutės apdorojimą pranešimams.

## Progreso pranešimai ir jų scenarijai

Šiame skyriuje paaiškinama progreso pranešimų sąvoka MCP, jų svarba ir kaip juos įgyvendinti naudojant Streamable HTTP. Taip pat rasite praktinę užduotį savo įgūdžiams tobulinti.

Progreso pranešimai yra realaus laiko žinutės, siunčiamos iš serverio klientui per ilgalaikes operacijas. Vietoje laukimo, kol visas procesas baigsis, serveris nuolat informuoja klientą apie esamą būseną. Tai gerina skaidrumą, naudotojo patirtį ir palengvina derinimą.

**Pavyzdys:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Kodėl naudoti progreso pranešimus?

Progreso pranešimai yra svarbūs dėl kelių priežasčių:

- **Geresnė naudotojo patirtis:** Vartotojai mato atnaujinimus vykdymo metu, ne tik pabaigoje.
- **Realaus laiko atsiliepimai:** Klientai gali rodyti progreso juostas ar žurnalus, todėl programa atrodo reaguojanti.
- **Lengvesnis derinimas ir stebėsena:** Kūrėjai ir vartotojai gali matyti, kur procesas sulėtėja ar užstringa.

### Kaip įgyvendinti progreso pranešimus

Štai kaip galite įgyvendinti progreso pranešimus MCP:

- **Serverio pusėje:** Naudokite `ctx.info()` arba `ctx.log()`, kad siųstumėte pranešimus, kai apdorojamas kiekvienas elementas. Tai siunčia žinutę klientui dar prieš paruošiant pagrindinį rezultatą.
- **Kliento pusėje:** Įgyvendinkite žinučių apdorojimo funkciją, kuri klauso ir rodo atvykstančius pranešimus. Ši funkcija atskiria pranešimus nuo galutinio rezultato.

**Serverio pavyzdys:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Kliento pavyzdys:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Saugumo svarstymai

Saugumas turėtų būti prioritetas įgyvendinant bet kurį serverį, ypač naudojant HTTP pagrindu veikiančius transportus, tokius kaip Streamable HTTP MCP.

Įgyvendinant MCP serverius su HTTP pagrindu veikiančiais transportais, saugumas tampa svarbiausiu klausimu, reikalaujančiu atidaus dėmesio keliems atakų vektoriams ir apsaugos mechanizmams.

### Apžvalga

Saugumas yra kritiškai svarbus kai MCP serveriai yra atveriami per HTTP. Streamable HTTP sukuria naujas atakų paviršius ir reikalauja kruopštaus konfigūravimo.

Štai keletas pagrindinių saugumo aspektų:

- **Origin antraštės patikra**: Visada tikrinkite `Origin` antraštę, kad išvengtumėte DNS peradresavimo atakų.
- **Binding vietiniam kompiuteriui**: Vietiniam kūrimui prijunkite serverius prie `localhost`, kad jie nebūtų pasiekiami viešajame internete.
- **Autentifikacija**: Produkcijai įgyvendinkite autentifikaciją (pavyzdžiui, API raktus, OAuth).
- **CORS**: Konfigūruokite Kryžminio šaltinio resursų dalinimosi (CORS) politiką, kad ribotumėte prieigą.
- **HTTPS**: Produkcijoje naudokite HTTPS, kad užšifruotumėte srautą.

### Geriausios praktikos

Be to, štai keletas geriausių praktikų, kurių vertėtų laikytis įgyvendinant saugumą savo MCP srautinio perdavimo serveryje:

- Niekada nepasitikėkite įeinančiais užklausimais be patikros.
- Loguokite ir stebėkite visus prieigos įvykius ir klaidas.
- Reguliariai atnaujinkite priklausomybes, kad užtaisytumėte saugumo spragas.

### Iššūkiai

Susidursite su tam tikrais iššūkiais įgyvendindami saugumą MCP srautinio perdavimo serveriuose:

- Saugumo ir kuriamumo patogumo balansas
- Užtikrinimas, kad veiktų įvairiose kliento aplinkose


## Pereinamasis laikotarpis nuo SSE prie Streamable HTTP

Programėlėms, kurios šiuo metu naudoja Server-Sent Events (SSE), migracija į Streamable HTTP suteikia patobulintas galimybes ir geresnį ilgalaikį tvarumą MCP įgyvendinimuose.

### Kodėl verta pereiti?

Yra du svarbūs argumentai pereiti nuo SSE prie Streamable HTTP:

- Streamable HTTP siūlo geresnį mastelį, suderinamumą ir turtingesnę pranešimų palaikymą nei SSE.
- Tai rekomenduojamas transportas naujoms MCP programėlėms.

### Migracijos žingsniai

Štai kaip galite migruoti nuo SSE prie Streamable HTTP savo MCP programėlėse:

- **Atnaujinkite serverio kodą** naudoti `transport="streamable-http"` funkcijoje `mcp.run()`.
- **Atnaujinkite kliento kodą** naudoti `streamablehttp_client` vietoj SSE kliento.
- **Įgyvendinkite žinutės apdorojimo funkciją** kliente pranešimams apdoroti.
- **Išbandykite suderinamumą** su esamais įrankiais ir darbo procesais.

### Suderinamumo išlaikymas

Rekomenduojama migracijos metu išlaikyti suderinamumą su esamais SSE klientais. Štai keletas strategijų:

- Galite palaikyti tiek SSE, tiek Streamable HTTP paleidžiant abu transportus skirtinguose taškuose.
- Palaipsniui migruoti klientus prie naujo transporto.

### Iššūkiai

Užtikrinkite, kad migracijos metu išspręstumėte šiuos iššūkius:

- Užtikrinti, kad visi klientai būtų atnaujinti
- Tvarkyti skirtumus pranešimų pristatymo būduose

### Užduotis: Sukurkite savo srautinių duomenų MCP programėlę

**Scenarijus:**
Sukurkite MCP serverį ir klientą, kur serveris apdoros elementų sąrašą (pvz., failus ar dokumentus) ir siųs pranešimą už kiekvieną apdorotą elementą. Klientas turėtų rodyti kiekvieną pranešimą, kai jis atvyksta.

**Žingsniai:**

1. Įgyvendinkite serverio įrankį, kuris apdoroja sąrašą ir siunčia pranešimus apie kiekvieną elementą.
2. Įgyvendinkite klientą su žinučių apdorojimo funkcija, kuri realiu laiku rodo pranešimus.
3. Išbandykite savo įgyvendinimą paleidę tiek serverį, tiek klientą, ir stebėkite pranešimus.

[Sprendimas](./solution/README.md)

## Tolimesnė literatūra ir kas toliau?

Norėdami tęsti MCP srautinio perdavimo mokymąsi ir išplėsti savo žinias, ši skiltis pateikia papildomų išteklių ir siūlomų žingsnių, kaip kurti pažangesnes programėles.

### Tolimesnė literatūra

- [Microsoft: Įvadas į HTTP srautą](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Srautinės užklausos](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Kas toliau?

- Išbandykite kurti sudėtingesnius MCP įrankius, kurie naudoja srautą realaus laiko analitikai, pokalbiui ar bendradarbiavimui redaguojant.
- Tyrinėkite MCP srautinio perdavimo integravimą su frontend karkasais (React, Vue ir kt.) gyviems naudotojo sąsajos atnaujinimams.
- Toliau: [Dirbdami su AI įrankių rinkiniu VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->