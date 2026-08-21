# HTTPS-suoratoisto Model Context Protocolin (MCP) kanssa

Tässä luvussa annetaan kattava opas turvallisen, skaalautuvan ja reaaliaikaisen suoratoiston toteuttamiseen Model Context Protocolin (MCP) avulla käyttäen HTTPS:ää. Se käsittelee suoratoiston motivaatiota, käytettävissä olevia siirtomekanismeja, suoratoistettavan HTTP:n toteuttamista MCP:ssä, turvallisuuden parhaita käytäntöjä, siirtymää SSE:stä sekä käytännön ohjeita omien suoratoistavien MCP-sovellusten rakentamiseksi.

> **Katse eteenpäin:** Tämä opetus kuvaa Streamable HTTP -toiminnallisuutta **MCP-määrittelyn 2025-11-25** mukaisesti, jossa istunto luodaan `initialize`-vaiheessa ja kiinnitetään `Mcp-Session-Id`-otsakkeella. Julkaisuehdokas `2026-07-28` poistaa kädenpuristuksen ja istunnon tunnuksen kokonaan, tehden jokaisesta pyynnöstä itsenäisen ja ohjattavissa mihin tahansa palvelininstanssiin ilman istuntokiinnityksiä. Katso lisätiedot kohdasta [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Siirtomekanismit ja suoratoisto MCP:ssä

Tässä osiossa tarkastellaan MCP:n eri saatavilla olevia siirtomekanismeja ja niiden roolia suoratoistomahdollisuuksien mahdollistamisessa reaaliaikaiseen viestintään asiakkaiden ja palvelimien välillä.

### Mikä on siirtomekanismi?

Siirtomekanismi määrittää, miten data vaihdetaan asiakkaan ja palvelimen välillä. MCP tukee useita siirtotyyppejä erilaisiin ympäristöihin ja vaatimuksiin:

- **stdio**: Standarditulot ja -lähdöt, sopii paikallisiin ja komentorivityökaluihin. Yksinkertainen, mutta ei sovellu verkkosovelluksiin tai pilveen.
- **SSE (Server-Sent Events)**: Mahdollistaa palvelimien työntää reaaliaikaisia päivityksiä asiakkaille HTTP:n yli. Hyvä verkkokäyttöliittymille, mutta rajoitettu skaalautuvuudessa ja joustavuudessa. MCP-määrittelyn 2025-06-18 version mukaan itsenäinen SSE-siirto on poistettu käytöstä ja korvattu "Streamable HTTP" -siirrolla.
- **Streamable HTTP**: Moderni HTTP-pohjainen suoratoistosiirto, tukee ilmoituksia ja parempaa skaalautuvuutta. Suositellaan useimpiin tuotantosovelluksiin ja pilviympäristöihin.

### Vertailutaulukko

Katso alla olevaa vertailutaulukkoa ymmärtääksesi eroja näiden siirtomekanismien välillä:

| Siirto             | Reaaliaikaiset päivitykset | Suoratoisto | Skaalautuvuus | Käyttötapaus               |
|-------------------|----------------------------|-------------|---------------|---------------------------|
| stdio             | Ei                         | Ei          | Matala        | Paikalliset komentorivityökalut |
| SSE               | Kyllä                      | Kyllä       | Keskitaso     | Web, reaaliaikaiset päivitykset |
| Streamable HTTP   | Kyllä                      | Kyllä       | Korkea        | Pilvi, moniasiakas         |

> **Vinkki:** Oikean siirron valinta vaikuttaa suorituskykyyn, skaalautuvuuteen ja käyttäjäkokemukseen. **Streamable HTTP** on suositeltava moderniin, skaalautuvaan ja pilviin valmiiseen sovellukseen.

Huomaa aiemmissa luvuissa esitellyt stdio ja SSE ja miten tässä luvussa käsitellään suoratoistettavaa HTTP-siirtoa.

## Suoratoisto: käsitteet ja motivaatio

Suoratoiston peruskäsitteiden ja motiivien ymmärtäminen on olennaista tehokkaiden reaaliaikaisten viestintäjärjestelmien toteuttamiseksi.

**Suoratoisto** on verkko-ohjelmoinnin tekniikka, joka mahdollistaa datan lähettämisen ja vastaanottamisen pieninä, hallittavina paloina tai tapahtumasarjana sen sijaan, että odotettaisiin koko vastauksen valmistumista. Tämä on erityisen hyödyllistä:

- Suurissa tiedostoissa tai aineistoissa.
- Reaaliaikaisissa päivityksissä (esim. chat, etenemispalkit).
- Pitkissä laskutoimituksissa, joissa halutaan pitää käyttäjä ajan tasalla.

Tässä on suoratoistosta korkean tason tärkeimmät asiat:

- Data toimitetaan vaiheittain, ei kerralla.
- Asiakas voi käsitellä dataa sitä mukaa kuin se saapuu.
- Vähentää koettua viivettä ja parantaa käyttäjäkokemusta.

### Miksi käyttää suoratoistoa?

Suoratoiston käyttämisen syyt ovat seuraavat:

- Käyttäjä saa palautteen heti, ei vain lopussa.
- Mahdollistaa reaaliaikaiset sovellukset ja reagoivat käyttöliittymät.
- Verkko- ja laskentaresurssien tehokkaampi käyttö.

### Yksinkertainen esimerkki: HTTP-suoratoistopalvelin ja asiakas

Tässä on yksinkertainen esimerkki suoratoiston toteuttamisesta:

#### Python

**Palvelin (Python, FastAPI ja StreamingResponse):**

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

**Asiakas (Python, requests-kirjastolla):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tämä esimerkki demonstroi palvelinta, joka lähettää sarjan viestejä asiakkaalle sitä mukaa kun ne ovat saatavilla sen sijaan, että odottaisi kaikkien viestien valmistumista.

**Miten se toimii:**

- Palvelin lähettää kukin viestin sitä mukaa kun se on valmis.
- Asiakas vastaanottaa ja tulostaa jokaisen osan saapuessaan.

**Vaateet:**

- Palvelimen tulee käyttää suoratoistovastausta (esim. `StreamingResponse` FastAPI:ssa).
- Asiakkaan tulee käsitellä vastaus suoratoistona (`stream=True` requestsissa).
- Content-Type on tavallisesti `text/event-stream` tai `application/octet-stream`.

#### Java

**Palvelin (Java, Spring Boot ja Server-Sent Events):**

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

**Asiakas (Java, Spring WebFlux WebClient):**

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

**Java-toteutusmuistiinpanot:**

- Käyttää Spring Bootin reaktiivista pinoa `Flux`-suoratoistolla.
- `ServerSentEvent` tarjoaa rakenteellisen tapahtumasuoratoiston tapahtumatyypeillä.
- `WebClient` ja `bodyToFlux()` mahdollistavat reaktiivisen suoratoiston kulutuksen.
- `delayElements()` simuloi tapahtumien välistä käsittelyaikaa.
- Tapahtumilla voi olla tyyppejä (`info`, `result`) paremman asiakaskäsittelyn vuoksi.

### Vertailu: Klassinen suoratoisto vs MCP-suoratoisto

Eroja suoratoiston toiminnassa "klassisen" mallin ja MCP:n välillä voidaan kuvata seuraavasti:

| Ominaisuus             | Klassinen HTTP-suoratoisto       | MCP-suoratoisto (Ilmoitukset)  |
|-----------------------|---------------------------------|--------------------------------|
| Päävastaus            | Osissa                          | Yksi kerralla lopussa           |
| Etenemispäivitykset   | Lähetetään datan paloina        | Lähetetään ilmoituksina         |
| Asiakkaan vaatimukset | Streaming pitää käsitellä       | Viestinkäsittelijä oltava       |
| Käyttötapaus          | Suuret tiedostot, AI-tokenvirrat | Eteneminen, lokit, reaaliaikainen palaute |

### Havaittuja keskeisiä eroja

Lisäksi seuraavat keskeiset erot ovat huomionarvoisia:

- **Viestintämalli:**
  - Klassinen HTTP-suoratoisto: Käyttää yksinkertaista paloittain siirtoa datan lähettämiseen palasina
  - MCP-suoratoisto: Käyttää rakenteellista ilmoitusjärjestelmää JSON-RPC-protokollalla

- **Viesti-muoto:**
  - Klassinen HTTP: Tekstipalat rivinvaihtoineen
  - MCP: Rakenteelliset LoggingMessageNotification-objektit metatiedoin

- **Asiakkaan toteutus:**
  - Klassinen HTTP: Yksinkertainen asiakas, joka käsittelee suoratoistovastauksia
  - MCP: Kehittyneempi asiakas viestinkäsittelijällä eri viestityyppien käsittelyyn

- **Etenemispäivitykset:**
  - Klassinen HTTP: Eteneminen on osa päävastausvirtaa
  - MCP: Eteneminen lähetetään erillisinä ilmoitusviesteinä, päävastaus saapuu lopuksi

### Suositukset

Suosittelemme seuraavia asioita valitessasi klassisen suoratoiston (kuten yllä `/stream`-rajapinta) ja MCP-suoratoiston välillä.

- **Yksinkertaisiin suoratoistotarpeisiin:** Klassinen HTTP-suoratoisto on helpompi toteuttaa ja riittävä perussuoratoistoon.

- **Monimutkaisiin, interaktiivisiin sovelluksiin:** MCP-suoratoisto tarjoaa rakenteellisemman lähestymistavan, jossa on rikkaampi metatietojen tuki sekä erottelu ilmoitusten ja lopullisen tuloksen välillä.

- **AI-sovelluksiin:** MCP:n ilmoitusjärjestelmä on erityisen hyödyllinen pitkäkestoisissa AI-tehtävissä, joissa halutaan pitää käyttäjät ajan tasalla edistymisestä.

## Suoratoisto MCP:ssä

Olet jo nähnyt suosituksia ja vertailuja klassisen suoratoiston ja MCP-suoratoiston eroista. Sukelletaan tarkemmin siihen, miten voit hyödyntää suoratoistoa MCP:ssä.

On tärkeää ymmärtää, miten suoratoisto toimii MCP-kehyksessä, jotta voit rakentaa reagoivia sovelluksia, jotka tarjoavat reaaliaikaista palautetta käyttäjille pitkissä toiminnoissa.

MCP:ssä suoratoisto ei tarkoita päävastauksen lähettämistä paloittain, vaan **ilmoitusten** lähettämistä asiakkaalle sen ajan, kun työkalu käsittelee pyyntöä. Nämä ilmoitukset voivat sisältää etenemispäivityksiä, lokeja tai muita tapahtumia.

### Miten se toimii

Pääasema lähetetään edelleen yhtenä vastauksena. Kuitenkin ilmoituksia voidaan lähettää erillisinä viesteinä prosessoinnin aikana, jolloin asiakas saa reaaliaikaiset päivitykset. Asiakkaan on pystyttävä käsittelemään ja näyttämään nämä ilmoitukset.

## Mikä on ilmoitus?

Mainitsimme "ilmoitus" – mitä se tarkoittaa MCP:n kontekstissa?

Ilmoitus on palvelimen lähettämä viesti asiakkaalle, joka tiedottaa etenemisestä, tilasta tai muista tapahtumista pitkän prosessin aikana. Ilmoitukset parantavat läpinäkyvyyttä ja käyttäjäkokemusta.

Esimerkiksi asiakas voi lähettää ilmoituksen heti, kun palvelimen kanssa on tehty alkuperäinen kädenpuristus.

Ilmoitus näyttää JSON-viestinä tältä:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Ilmoitukset kuuluvat MCP:n aihepiiriin nimeltä ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Poistumisilmoitus:** MCP-määrittelyn 2026-07-28 julkaisuehdokas merkitsee Logging-primitiivin poistuvaksi ja suosii `stderr`-käyttöä stdio-siirroissa sekä OpenTelemetryä rakenteelliseen havaittavuuteen. Logging toimii edelleen versiossa 2025-11-25 ja ainakin vuoden ajan minkä tahansa virallisen poiston jälkeen. Katso lisätietoja kohdasta [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Jotta lokitus toimii, palvelimen täytyy ottaa se käyttöön ominaisuutena näin:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Käytetystä SDK:sta riippuen lokitus saattaa olla oletuksena käytössä tai se täytyy erikseen aktivoida palvelimen asetuksissa.

Ilmoituksia on erilaisia:

| Taso       | Kuvaus                          | Esimerkkikäyttö                |
|------------|--------------------------------|-------------------------------|
| debug      | Yksityiskohtainen debug-tieto  | Funktioiden sisään-/uloskulut  |
| info       | Yleiset informatiiviset viestit| Toiminnon etenemispäivitykset |
| notice     | Normaaleja, mutta merkittäviä tapahtumia | Asetusmuutokset          |
| warning    | Varoitusolosuhteet             | Poistuvien ominaisuuksien käyttö |
| error      | Virhetilanteet                | Toimintavirheet               |
| critical   | Kriittiset tilat              | Järjestelmän osakomponentin viat |
| alert      | Toimenpiteitä vaaditaan heti  | Tiedon korruptio havaittu     |
| emergency  | Järjestelmä ei ole käyttökelpoinen | Täydellinen järjestelmän vika |

## Ilmoitusten toteuttaminen MCP:ssä

Ilmoitusten toteuttamiseksi MCP:ssä sinun tulee konfiguroida sekä palvelin- että asiakaspuolet käsittelemään reaaliaikaisia päivityksiä. Tämä mahdollistaa sovelluksesi tarjoavan välitöntä palautetta käyttäjille pitkissä toiminnoissa.

### Palvelinpuoli: Ilmoitusten lähettäminen

Aloitetaan palvelinpuolelta. MCP:ssä määrittelet työkalut, jotka voivat lähettää ilmoituksia pyyntöjä käsitellessään. Palvelin käyttää konteksti-oliota (yleensä `ctx`) lähettääkseen viestejä asiakkaalle.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Edellisessä esimerkissä `process_files`-työkalu lähettää kolme ilmoitusta asiakkaalle käsitellessään kutakin tiedostoa. `ctx.info()`-metodia käytetään informatiivisten viestien lähettämiseen.

Lisäksi ilmoitusten käyttöönottoa varten varmista, että palvelimesi käyttää suoratoistosiirtoa (kuten `streamable-http`) ja että asiakkaasi toteuttaa viestinkäsittelijän ilmoitusten käsittelemiseksi. Näin otat palvelimessa käyttöön `streamable-http`-siirron:

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

Tässä .NET-esimerkissä `ProcessFiles`-työkalu on koristeltu `Tool`-attribuutilla ja lähettää kolme ilmoitusta asiakkaalle tiedostoja käsitellessään. `ctx.Info()`-metodia käytetään informatiivisten viestien lähettämiseen.

Ilmoitusten käyttöönottoa varten .NET MCP -palvelimellasi varmista, että käytät suoratoistosiirtoa:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Asiakaspuoli: Ilmoitusten vastaanottaminen

Asiakkaan täytyy toteuttaa viestinkäsittelijä, joka prosessoi ja näyttää ilmoitukset heti kun ne saapuvat.

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

Edellisessä koodissa `message_handler`-funktio tarkistaa, onko saapuva viesti ilmoitus. Jos on, se tulostaa ilmoituksen; muuten käsittelee sen tavallisena palvelinviestinä. Huomaa myös, että `ClientSession` alustetaan `message_handler`illa käsittelemään saapuvia ilmoituksia.

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

Tässä .NET-esimerkissä `MessageHandler`-funktio tarkistaa, onko viesti ilmoitus. Jos on, se tulostaa ilmoituksen; muuten käsittelee sen tavallisena palvelinviestinä. `ClientSession` alustetaan viestinkäsittelijällä `ClientSessionOptions` kautta.

Ilmoitusten käyttöönottoa varten varmista, että palvelimesi käyttää suoratoistosiirtoa (kuten `streamable-http`) ja asiakkaasi toteuttaa viestinkäsittelijän ilmoitusten käsittelemiseksi.

## Etenemisilmoitukset ja skenaariot

Tässä osiossa selitetään etenemisilmoitusten käsite MCP:ssä, miksi ne ovat tärkeitä ja miten ne voi toteuttaa Streamable HTTP:n avulla. Löydät myös käytännön tehtävän ymmärryksen vahvistamiseksi.

Etenemisilmoitukset ovat palvelimelta asiakkaalle lähetettäviä reaaliaikaisia viestejä pitkien toimintojen aikana. Sen sijaan, että odotettaisiin koko prosessin valmistumista, palvelin pitää asiakasta ajan tasalla nykytilanteesta. Tämä parantaa läpinäkyvyyttä, käyttäjäkokemusta ja helpottaa virheiden selvitystä.

**Esimerkki:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miksi käyttää etenemisilmoituksia?

Etenemisilmoitukset ovat välttämättömiä monista syistä:

- **Parempi käyttäjäkokemus:** Käyttäjät näkevät päivityksiä työn edetessä, eivät vain lopussa.
- **Reaaliaikainen palaute:** Asiakkaat voivat näyttää etenemis- tai lokipalkkeja, tehden sovelluksesta reagoivan.
- **Helpompi virheiden selvitys ja valvonta:** Kehittäjät ja käyttäjät voivat nähdä, missä kohdassa prosessi on hidas tai jumissa.

### Miten toteuttaa etenemisilmoituksia

Näin voit toteuttaa etenemisilmoituksia MCP:ssä:

- **Palvelimella:** Käytä `ctx.info()` tai `ctx.log()` lähettääksesi ilmoituksia sitä mukaa kun kukin kohde käsitellään. Tämä lähettää viestin asiakkaalle ennen päävastauksen valmistumista.
- **Asiakkaalla:** Toteuta viestinkäsittelijä, joka kuuntelee ja näyttää ilmoitukset saapuessaan. Tämä käsittelijä erottaa ilmoitukset ja lopullisen tuloksen.

**Palvelinesimerkki:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Asiakas-esimerkki:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Turvallisuusseikat

Turvallisuuden tulee olla ensisijainen tavoite minkä tahansa palvelimen toteuttamisessa, erityisesti käytettäessä HTTP-pohjaisia tiedonsiirtomenetelmiä, kuten Streamable HTTP:tä MCP:ssä.

Kun toteutat MCP-palvelimia, joissa käytetään HTTP-pohjaisia tiedonsiirtoratkaisuja, turvallisuus on ensisijaisen tärkeää ja se vaatii huolellista tarkastelua useiden hyökkäysvektorien ja suojausmekanismien osalta.

### Yleiskatsaus

Turvallisuus on kriittinen tekijä, kun paljastetaan MCP-palvelimia HTTP:n välityksellä. Streamable HTTP tuo mukanaan uusia hyökkäyspintoja ja vaatii huolellisia asetuksia.

Tässä muutamia keskeisiä turvallisuusseikkoja:

- **Origin-otsikon validointi**: Varmista aina `Origin`-otsikon oikeellisuus estääksesi DNS-omistuksen uudelleenohjauksen hyökkäykset.
- **Localhost-sidonta**: Paikallisessa kehityksessä sitouta palvelimet `localhost`-osoitteeseen, jotta ne eivät ole julkisen internetin saavutettavissa.
- **Todennus**: Toteuta todennus (esim. API-avaimet, OAuth) tuotantokäytössä.
- **CORS**: Konfiguroi Cross-Origin Resource Sharing (CORS) -käytännöt pääsyn rajoittamiseksi.
- **HTTPS**: Käytä HTTPS-protokollaa tuotannossa liikenteen salaamiseen.

### Hyvät käytännöt

Lisäksi tässä on joitakin parhaita käytäntöjä, joita kannattaa noudattaa, kun toteutat turvallisuutta MCP-striimauspalvelimessasi:

- Älä koskaan luota saapuviin pyyntöihin ilman validointia.
- Kirjaa ylös ja valvo kaikkia käyttöjä ja virheitä.
- Päivitä riippuvuudet säännöllisesti tietoturvahaavoittuvuuksien paikkaamiseksi.

### Haasteet

Turvallisuuden toteuttamisessa MCP-striimauspalvelimissa kohtaat seuraavia haasteita:

- Turvallisuuden ja kehityksen helppouden tasapainottaminen
- Yhteensopivuuden varmistaminen eri asiakkaiden ympäristöjen kanssa


## Päivitys SSE:stä Streamable HTTP:hen

Sovelluksille, jotka käyttävät tämänhetkisesti Server-Sent Eventsiä (SSE), siirtyminen Streamable HTTP:hen tarjoaa parannettuja ominaisuuksia ja paremman pitkän aikavälin kestävyden MCP-toteutuksillesi.

### Miksi päivittää?

Päivittämiseen SSE:stä Streamable HTTP:hen on kaksi vakuuttavaa syytä:

- Streamable HTTP tarjoaa paremman skaalautuvuuden, yhteensopivuuden ja rikkaamman ilmoitustuen kuin SSE.
- Se on suositeltu tiedonsiirtoratkaisu uusille MCP-sovelluksille.

### Siirtymisen vaiheet

Näin voit siirtyä SSE:stä Streamable HTTP:hen MCP-sovelluksissasi:

- **Päivitä palvelinkoodi** käyttämään `transport="streamable-http"` `mcp.run()` -kutsussa.
- **Päivitä asiakaskoodi** käyttämään `streamablehttp_client` SSE-asiakkaan sijaan.
- **Toteuta viestinkäsittelijä** asiakkaaseen ilmoitusten käsittelemiseksi.
- **Testaa yhteensopivuus** olemassa olevien työkalujen ja työprosessien kanssa.

### Yhteensopivuuden ylläpito

On suositeltavaa ylläpitää yhteensopivuutta olemassa olevien SSE-asiakkaiden kanssa migraatioprosessin aikana. Tässä joitakin strategioita:

- Voit tukea sekä SSE:tä että Streamable HTTP:tä käyttämällä molempia tiedonsiirtotapoja eri päätepisteissä.
- Siirrä asiakkaat vähitellen uuteen tiedonsiirtotapaan.

### Haasteet

Huolehdi seuraavista haasteista siirtymän aikana:

- Kaikkien asiakkaiden päivittäminen
- Ilmoitusten toimituserojen käsittely

### Tehtävä: Rakenna oma MCP-striimaussovellus

**Tilanne:**
Rakenna MCP-palvelin ja asiakas, missä palvelin käsittelee listan kohteita (esim. tiedostoja tai dokumentteja) ja lähettää ilmoituksen jokaisesta käsitellystä kohteesta. Asiakkaan tulee näyttää jokainen ilmoitus sitä mukaa kun se saapuu.

**Vaiheet:**

1. Toteuta palvelintyökalu, joka käsittelee listan ja lähettää ilmoitukset jokaisesta kohteesta.
2. Toteuta asiakas, jossa on viestinkäsittelijä ilmoitusten reaaliaikaiseen näyttämiseen.
3. Testaa toteutus käynnistämällä sekä palvelin että asiakas ja seuraa ilmoituksia.

[Ratkaisu](./solution/README.md)

## Lisälukemista & Mitä seuraavaksi?

Jatka matkasi MCP-striimauksen parissa ja laajenna osaamistasi. Tämä osio tarjoaa lisäresursseja ja ehdotettuja seuraavia askeleita kehittyneempien sovellusten rakentamiseen.

### Lisälukemista

- [Microsoft: Johdanto HTTP-striimaukseen](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Coressa](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mitä seuraavaksi?

- Kokeile rakentaa kehittyneempiä MCP-työkaluja, jotka käyttävät striimausta reaaliaikaiseen analytiikkaan, chattiin tai yhteisölliseen muokkaukseen.
- Tutki MCP-striimauksen integrointia frontend-kehyksiin (React, Vue jne.) live-käyttöliittymäpäivityksiä varten.
- Seuraavaksi: [AI Toolkitin käyttäminen VSCode:ssa](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->