# HTTPS-streamaus Model Context Protocolilla (MCP)

Tämä luku tarjoaa kattavan oppaan turvallisen, skaalautuvan ja reaaliaikaisen streamauksen toteuttamiseen Model Context Protocolia (MCP) käyttäen HTTPS:n yli. Se käsittelee streamauksen motivaatiota, käytettävissä olevia siirtomekanismeja, streamattavan HTTP:n toteutusta MCP:ssä, parhaat turvallisuuskäytännöt, siirtymisen SSE:stä sekä käytännön ohjeita oman streamaavan MCP-sovelluksen rakentamiseen.

> [!WARNING]
> Tämä oppitunnin toteutus esimerkit kohdistuvat **MCP-spesifikaatioon
> `2025-11-25`** ja demonstroivat perinteistä `initialize` kättelyä,
> `Mcp-Session-Id`, GET tapahtumavirtaa ja jatkettavuutta mallia. MCP `2026-07-28`
> poistaa nämä ominaisuudet. Nykyiset Streamable HTTP -pyynnöt ovat itsetoimivia
> POST-pyyntöjä, joissa on `MCP-Protocol-Version` ja `Mcp-Method` otsikot sekä
> `Mcp-Name`, missä tarpeen. Katso
> [Mitä MCP:ssä on muuttunut: 28.7.2026 spesifikaatio](../../01-CoreConcepts/mcp-2026-07-28.md)
> ennen näiden esimerkkien käyttämistä uudessa toteutuksessa.

## Siirtomekanismit ja streamaus MCP:ssä

Tässä osiossa tarkastellaan MCP:ssä käytettävissä olevia eri siirtomekanismeja ja niiden roolia reaaliaikaisen kommunikaation streamausmahdollisuuksien mahdollistamisessa asiakkaiden ja palvelimien välillä.

### Mikä on siirtomekanismi?

Siirtomekanismi määrittelee, miten data vaihdetaan asiakkaan ja palvelimen välillä. MCP tukee useita siirtotyyppejä erilaisiin ympäristöihin ja vaatimuksiin sopivaksi:

- **stdio**: Standardi tulos-/sisääntulo, sopii paikallisille ja komentorivityökaluilla käytettäville. Yksinkertainen, mutta ei sovellu webiin tai pilveen.
- **HTTP+SSE**: Perinteinen etäkuljetus, joka on vanhentunut MCP:ssa `2025-03-26`
    ja korvattu Streamable HTTP:llä. Älä käytä sitä uusissa toteutuksissa.
- **Streamable HTTP**: Moderni HTTP-pohjainen suoratoistokuljetus, joka tukee ilmoituksia ja parempaa skaalautuvuutta. Suositeltava useimpiin tuotanto- ja pilviympäristöihin.

### Vertailutaulukko

Katso alla oleva vertailutaulukko ymmärtääksesi eroja näiden kuljetusmekanismien välillä:

| Kuljetus | Tila | Ilmoitukset | Tyypillinen käyttötarkoitus |
|---|---|---|---|
| stdio | Nykyinen | Kyllä | Paikalliset aliprosessit |
| HTTP+SSE | Vanhentunut | Kyllä | Perinteiset etäkäyttöiset toteutukset |
| Streamable HTTP | Nykyinen | Kyllä | Etä- ja pilvipalvelimet |

> **Vinkki:** Oikean kuljetuksen valinta vaikuttaa suorituskykyyn, skaalautuvuuteen ja käyttökokemukseen. **Streamable HTTP** on suositeltava moderneihin, skaalautuviin ja pilvivalmiisiin sovelluksiin.

Vakiosuoratoistokuljetukset ovat stdio ja Streamable HTTP. HTTP+SSE esiintyy vain
vanhemmissa esimerkeissä.

## Suoratoisto: Konseptit ja motivaatio

Ymmärtäminen suoratoiston peruskäsitteistä ja motiiveista on olennaista tehokkaiden reaaliaikaisten viestintäjärjestelmien toteuttamiseksi.

**Suoratoisto** on verkkosovellusten tekniikka, joka mahdollistaa datan lähetyksen ja vastaanoton pieninä, hallittavina osina tai tapahtumajonona sen sijaan, että odotettaisiin koko vasteen valmistumista. Tämä on erityisen hyödyllistä:

- Suurille tiedostoille tai tietoaineistoille.
- Reaaliaikaisille päivityksille (esim. chat, etenemispalkit).
- Pitkään kestäville laskelmille, joissa halutaan pitää käyttäjä ajan tasalla.

Tässä mitä sinun tulee tietää suoratoistosta yleisellä tasolla:

- Data välitetään asteittain, ei kokonaan kerralla.
- Asiakas voi käsitellä dataa sitä mukaa kun se vastaanotetaan.
- Vähentää koettua viivettä ja parantaa käyttökokemusta.

### Miksi käyttää suoratoistoa?

Syyt suoratoiston käyttämiseen ovat seuraavat:

- Käyttäjät saavat palautteen heti, eivät vain lopussa
- Mahdollistaa reaaliaikaiset sovellukset ja responsiiviset käyttöliittymät
- Tehokkaampi verkkoyhteyksien ja laskentaresurssien käyttö

### Yksinkertainen esimerkki: HTTP-suoratoistopalvelin ja asiakas

Tässä yksinkertainen esimerkki suoratoiston toteutuksesta:

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

**Asiakas (Python, requests-kirjaston käyttö):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tämä esimerkki osoittaa, miten palvelin lähettää sarjan viestejä asiakkaalle sitä mukaa kun ne valmistuvat, sen sijaan että odottaisi kaikkien viestien valmistumista.

**Miten se toimii:**

- Palvelin tuottaa jokaisen viestin sitä mukaa kun se on valmis.
- Asiakas vastaanottaa ja tulostaa jokaisen osan sitä mukaa kun se saapuu.

**Vaadittavat seikat:**

- Palvelimen on käytettävä suoratoistovastetta (esim. `StreamingResponse` FastAPI:ssa).
- Asiakkaan on käsiteltävä vastaus suoratoistona (`stream=True` requests-kirjastossa).
- Sisältötyyppi on yleensä `text/event-stream` tai `application/octet-stream`.

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

**Java-toteutuksen huomioita:**

- Käyttää Spring Bootin reaktiivista pinoutumaa `Flux` suoratoistoon
- `ServerSentEvent` tarjoaa rakenteellisen tapahtumasuoratoiston tapahtumatyyppeineen
- `WebClient` yhdessä `bodyToFlux()` kanssa mahdollistaa reaktiivisen suoratoistokulutuksen
- `delayElements()` simuloi käsittelyaikaa tapahtumien välillä
- Tapahtumilla voi olla tyyppejä (`info`, `result`) paremman asiakaskäsittelyn takia

### Vertailu: Perinteinen suoratoisto vs MCP-suoratoisto

Erot siinä, miten suoratoisto toimii "klassisesti" verrattuna MCP:hen, voidaan kuvata seuraavasti:

| Ominaisuus             | Klassinen HTTP-suoratoisto     | MCP-suoratoisto (Ilmoitukset)         |
|------------------------|-------------------------------|---------------------------------------|
| Päävastaus             | Palasten muodossa              | Yksittäinen, lopussa                   |
| Edistymispäivitykset   | Lähetetään datapalasina       | Lähetetään ilmoituksina                |
| Asiakasvaatimukset      | On käsiteltävä suoratoisto    | On toteutettava viestikäsittelijä      |
| Käyttötarkoitus        | Suuret tiedostot, AI-token-sarjat | Edistymä, lokit, reaaliaikainen palaute |

### Havaitut keskeiset erot

Lisäksi tässä on joitakin keskeisiä eroja:

- **Viestintäkuvio:**
  - Klassinen HTTP-suoratoisto: Käyttää yksinkertaista palastoitua siirtokoodausta datan lähettämiseen paloissa
  - MCP-suoratoisto: Käyttää rakenteellista ilmoitusjärjestelmää JSON-RPC-protokollalla

- **Viestin muoto:**
  - Klassinen HTTP: Pelkät tekstipalaset rivinvaihtoineen
  - MCP: Rakenteelliset LoggingMessageNotification-objektit metatietoineen

- **Asiakastoteutus:**
  - Klassinen HTTP: Yksinkertainen asiakas, joka käsittelee suoratoistovastauksia
  - MCP: Monimutkaisempi asiakas, jolla on viestikäsittelijä eri tyyppisten viestien käsittelyyn

- **Edistymispäivitykset:**
  - Klassinen HTTP: Edistyminen on osa päävastuetta
  - MCP: Edistymistä lähetetään erillisinä ilmoitusviesteinä, kun taas päävastaus tulee lopuksi

### Suositukset

On joitakin suosituksia, joita annamme klassisen suoratoiston (kuten yllä näytimme päätepisteen käyttämällä `/stream`) ja MCP:n kautta tapahtuvan suoratoiston välillä valitessa.

- **Yksinkertaisiin suoratoistotarpeisiin:** Klassinen HTTP-suoratoisto on helpompi toteuttaa ja riittää perustason suoratoistotarpeisiin.

- **Monimutkaisiin, interaktiivisiin sovelluksiin:** MCP-suoratoisto tarjoaa rakenteellisemman lähestymistavan, jossa on rikkaammat metatiedot ja erot notificationeiden ja lopullisten tulosten välillä.

- **AI-sovelluksiin:** MCP:n notification-järjestelmä on erityisen hyödyllinen pitkäkestoisissa AI-tehtävissä, joissa halutaan pitää käyttäjät ajan tasalla etenemisestä.

## Suoratoisto MCP:ssä

Okei, olet nähnyt joitakin suosituksia ja vertailuja klassisen suoratoiston ja MCP-suoratoiston eroista. Käydään tarkemmin läpi, miten voit hyödyntää suoratoistoa MCP:ssä.

On tärkeää ymmärtää, miten suoratoisto toimii MCP-kehyksessä, jotta voit rakentaa reagoivia sovelluksia, jotka tarjoavat käyttäjille reaaliaikaista palautetta pitkäkestoisten toimintojen aikana.

MCP:ssä suoratoisto ei tarkoita päätuloksen lähettämistä paloina, vaan **notificationien** lähettämistä asiakkaalle työkalun käsitellessä pyyntöä. Näihin notificationeihin voi kuulua etenemisilmoituksia, lokitietoja tai muita tapahtumia.

### Miten se toimii

Päätulos lähetetään silti yhtenä vastauksena. Notificationeita voidaan kuitenkin lähettää erillisinä viesteinä käsittelyn aikana, jolloin asiakas saa päivityksiä reaaliajassa. Asiakkaan täytyy pystyä käsittelemään ja näyttämään nämä notificationit.

### Valinnainen harjoitus: yhdistä isännöityyn MCP-palvelimeen

Voit käyttää Streamable HTTP:tä myös ajamatta paikallista palvelinta. Tässä esimerkissä
yhdistetään [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
löydetään sen työkalut ja haetaan julkista MCP-dokumentaatiota käyttämällä samaa
Python SDK:ta kuin [paikallinen asiakas](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallelin anonyymi päätepiste ei vaadi tiliä tai API-avainta. Ilmainen käyttö on
määrävälein rajoitettua. Tämän skriptin suorittaminen lähettää hakukyselyt, tavoitteen ja
satunnaisen istuntotunnisteen Parallelille. Palvelu tarjoaa myös `web_fetch`,
joka lähettää pyydetyt URL-osoitteet ja annetun kontekstin Parallelille. Käytä julkista
tietoa tässä harjoituksessa; katso sen [ehdot](https://parallel.ai/customer-terms)
ja [tietosuojakäytäntö](https://parallel.ai/privacy-policy).

Kun Python 3.10 tai uudempi ja virtuaaliympäristö on aktivoitu, asenna SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Tallenna tämä nimellä `hosted_search.py` ja suorita `python hosted_search.py`:

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

Löydön odotetaan sisältävän `web_search` ja `web_fetch`, jota seuraa haku
vastaus, joka sisältää lähde-URL-osoitteet ja katkelmat. Tulokset voivat vaihdella tai olla tyhjiä.
Skripti tarkistaa `isError`, koska työkalu voi epäonnistua, vaikka HTTP-pyyntö
onnistuisikin. Jos käyttörajoitus on voimassa, odota ennen uudelleen yrittämistä. Käytä samaa
`session_id` uudelleen, jos laajennat skriptiä liittyvillä hakemis- tai hakukutsuilla.

Streamable HTTP sallii sekä JSON- että SSE-vastaukset; tämä palvelin voi palauttaa
täydellisen JSON-tuloksen ilman etenemisilmoituksia. SDK käsittelee
tiedonsiirron. Jatka alla olevan paikallisen esimerkin parissa oppiaksesi ilmoituksista.
Tämä valinnainen skripti tekee yhden eksplisiittisen haun ja sulkee yhteytensä, kun
se valmistuu. Jos altistat nämä työkalut myöhemmin agentille, agentti voi kutsua
niitä työnsä aikana; käsittele haettua verkkotekstiä epäluotettavana datana.

## Mikä on ilmoitus?

Puhuimme "ilmoituksesta", mitä se tarkoittaa MCP:n yhteydessä?

Ilmoitus on JSON-RPC-viesti, jolla ei ole `id` ja joka ei saa vastausta.
MCP käyttää ilmoituksia etenemisen, peruutuksen ja muiden yksisuuntaisten tapahtumien ilmoittamiseen.


MCP:n `2025-11-25` asiakkaan lähettää `notifications/initialized` alustusvaiheen jälkeen.
MCP:n `2026-07-28`:ssa ei ole alustusvaihetta, joten tämä ilmoitus on vanhaa käytöstä.


Ilmoitus näyttää JSON-viestinä seuraavalta:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Lokitus on yksi ominaisuuksista, joka käyttää ilmoituksia; ilmoitukset itsessään ovat
yleinen JSON-RPC-viestityyppi.

> **Vanhentunut MCP:n `2026-07-28`:ssa:** Lokitusominaisuus on saatavilla
> yhteensopivuuden vuoksi, mutta se voidaan poistaa ensimmäisessä määrittelypäivityksessä,
> joka julkaistaan 28. heinäkuuta 2027 tai sen jälkeen. Uusien toteutusten tulisi käyttää
> `stderr` stdion tai OpenTelemetryn kanssa rakenteelliseen havainnointiin.

Legacy-`2025-11-25`-toteutuksessa palvelin ottaa lokitus-ominaisuuden käyttöön seuraavasti:


```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Käytetystä SDK:sta riippuen lokitus voi olla oletuksena päällä, tai sinun täytyy erikseen ottaa se käyttöön palvelimen asetuksissa.

Ilmoitustyyppejä on erilaisia:

| Taso      | Kuvaus                        | Esimerkkitapaus                |
|-----------|------------------------------|-------------------------------|
| debug     | Yksityiskohtainen vianmääritys | Funktiokutsujen aloitus/lopetus |
| info      | Yleiset tietoa antavat viestit | Toiminnon etenemisen päivitykset |
| notice    | Normaalit mutta merkittävät tapahtumat | Asetusten muutokset           |
| warning   | Varoitustilanteet             | Vanhojen ominaisuuksien käyttö  |
| error     | Virhetilanteet                | Toiminnon epäonnistumiset       |
| critical  | Kriittiset tilat              | Järjestelmän komponenttien vioittumat |
| alert     | Toiminta on tehtävä heti      | Tietojen korruptio havaittu     |
| emergency | Järjestelmä on käyttökelvoton | Koko järjestelmän vika          |

## Ilmoitusten toteuttaminen MCP:ssä

Ilmoitusten toteuttamiseksi MCP:ssä sinun tulee konfiguroida sekä palvelin- että asiakaspuolet käsittelemään reaaliaikaisia päivityksiä. Tällä tavalla sovelluksesi voi antaa välitöntä palautetta käyttäjille pitkäkestoisten toimintojen aikana.

### Palvelinpuoli: Ilmoitusten lähettäminen

Aloitetaan palvelinpuolelta. MCP:ssä määrittelet työkalut, jotka voivat lähettää ilmoituksia käsitellessään pyyntöjä. Palvelin käyttää konteksti-oliota (yleensä `ctx`) lähettääkseen viestejä asiakkaalle.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Edellisessä esimerkissä `process_files`-työkalu lähettää kolme ilmoitusta asiakkaalle käsitellessään jokaista tiedostoa. `ctx.info()`-metodia käytetään tiedotuksellisten viestien lähettämiseen.

Lisäksi ilmoitusten käyttöönottoa varten varmista, että palvelin käyttää suoratoistoyhteyttä (kuten `streamable-http`) ja että asiakas on toteuttanut viestinkäsittelijän käsittelemään ilmoituksia. Näin voit konfiguroida palvelimen käyttämään `streamable-http`-yhteyttä:

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

Tässä .NET-esimerkissä `ProcessFiles`-työkalu on merkitty `Tool`-attribuutilla ja lähettää kolme ilmoitusta asiakkaalle käsitellessään jokaista tiedostoa. `ctx.Info()`-metodia käytetään tiedotuksellisten viestien lähettämiseen.

Ota ilmoitukset käyttöön .NET MCP -palvelimessasi varmistamalla, että käytössä on suoratoistoyhteys:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Asiakaspuoli: Ilmoitusten vastaanottaminen

Asiakasohjelman on toteutettava viestinkäsittelijä käsittelemään ja näyttämään ilmoitukset niiden saapuessa.

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

Edellisessä koodissa `message_handler`-funktio tarkistaa, onko saapuva viesti ilmoitus. Jos on, se tulostaa ilmoituksen; muuten se käsittelee viestin tavallisena palvelinviestinä. Huomaa myös, miten `ClientSession` alustetaan `message_handler`:llä käsittelemään saapuvia ilmoituksia.

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

Tässä .NET-esimerkissä `MessageHandler`-funktio tarkistaa, onko saapuva viesti ilmoitus. Jos on, se tulostaa ilmoituksen; muuten se käsittelee viestin tavallisena palvelinviestinä. `ClientSession` alustetaan viestinkäsittelijällä `ClientSessionOptions`:n kautta.

Ilmoitusten ottamiseksi käyttöön varmista, että palvelimesi käyttää streamauskuljetusta (kuten `streamable-http`) ja että asiakkaasi toteuttaa viestinkäsittelijän ilmoitusten vastaanottamiseksi.

## Edistymisilmoitukset ja käyttötapaukset

Tässä osiossa selitetään MCP:n edistymisilmoitusten käsite, miksi ne ovat tärkeitä ja miten ne toteutetaan käyttäen Streamable HTTP:tä. Löydät myös käytännön harjoituksen ymmärryksesi vahvistamiseksi.

Edistymisilmoitukset ovat reaaliaikaisia viestejä, joita palvelin lähettää asiakkaalle pitkittyvien operaatioiden aikana. Sen sijaan, että odotetaan koko prosessin valmistumista, palvelin pitää asiakkaan ajan tasalla nykytilasta. Tämä parantaa läpinäkyvyyttä, käyttökokemusta ja helpottaa virheiden selvittämistä.

**Esimerkki:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miksi käyttää edistymisilmoituksia?

Edistymisilmoitukset ovat tärkeitä useista syistä:

- **Parempi käyttökokemus:** Käyttäjät näkevät päivityksiä työn edetessä, eivät pelkästään lopussa.
- **Reaaliaikainen palaute:** Asiakkaat voivat näyttää etenemispalkkeja tai lokeja, mikä tekee sovelluksesta reagoivan.
- **Helpompi virheiden selvitys ja valvonta:** Kehittäjät ja käyttäjät näkevät, missä prosessi saattaa olla hidas tai jumissa.

### Miten toteuttaa edistymisilmoitukset

Näin voit toteuttaa edistymisilmoitukset MCP:ssä:

- **Palvelimella:** Käytä `ctx.info()` tai `ctx.log()` lähettääksesi ilmoituksia sitä mukaa, kun jokainen kohde käsitellään. Tämä lähettää viestin asiakkaalle ennen päätepuloksen valmistumista.
- **Asiakkaalla:** Toteuta viestinkäsittelijä, joka kuuntelee ja näyttää saapuvat ilmoitukset. Tämä käsittelijä erottaa ilmoitukset ja lopullisen tuloksen.

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

## Turvallisuusnäkökohdat

Turvallisuuden tulee olla ensisijainen prioriteetti palvelinta toteutettaessa, erityisesti HTTP-pohjaisten kuljetusten, kuten Streamable HTTP:n, käytössä MCP:ssä.

MCP-palvelimia toteutettaessa HTTP-pohjaisilla kuljetuksilla turvallisuus korostuu ja vaatii huolellista huomiota useisiin hyökkäysvektoreihin ja suojamekanismeihin.

### Yleiskatsaus

Turvallisuus on kriittistä MCP-palvelimien altistaessa niitä HTTP:n kautta. Streamable HTTP tuo uusia hyökkäyspintoja ja vaatii huolellista konfigurointia.

Tässä joitakin keskeisiä turvallisuusnäkökohtia:

- **Origin-otsikon validointi**: Varmista aina `Origin`-otsikko, jotta estät DNS-uudelleensidontahyökkäyksiä.
- **Localhost-sidonta**: Paikallisessa kehityksessä sido palvelimet osoitteeseen `localhost`, jotta ne eivät ole julkisen internetin saatavilla.
- **Todennus**: Toteuta todennus (esim. API-avaimet, OAuth) tuotantoympäristössä.
- **CORS**: Määritä Cross-Origin Resource Sharing (CORS) -politiikat pääsyn rajoittamiseksi.
- **HTTPS**: Käytä HTTPS:ää tuotannossa liikenteen salaamiseksi.

### Parhaat käytännöt

Lisäksi, tässä joitakin parhaita käytäntöjä MCP-streamauspalvelimien turvallisuuden toteutuksessa:

- Älä koskaan luota saapuviin pyyntöihin ilman validointia.
- Kirjaa ja valvo kaikki pääsyt ja virheet.
- Päivitä säännöllisesti riippuvuudet korjataksesi turvallisuusaukkoja.

### Haasteet

Ongelmia tulee eteen, kun toteutat turvallisuutta MCP-streamauspalvelimissa:

- Turvallisuuden ja kehityksen helppouden tasapainottaminen
- Yhteensopivuuden varmistaminen eri asiakasympäristöjen kanssa


## Päivitys SSE:stä Streamable HTTP:hen

Sovelluksille, jotka käyttävät tällä hetkellä Server-Sent Events (SSE), siirtyminen Streamable HTTP:hen tarjoaa parannetut ominaisuudet ja paremman pitkäaikaisen ylläpidettävyyden MCP-toteutuksillesi.

### Miksi päivittää?

On kaksi merkittävää syytä päivittää SSE:stä Streamable HTTP:hen:

- Streamable HTTP tarjoaa paremman skaalautuvuuden, yhteensopivuuden ja monipuolisemman ilmoitustuen kuin SSE.
- Se on suositeltu kuljetus uuteen MCP-sovellukseen.

### Migraatiovaiheet

Näin voit siirtyä SSE:stä Streamable HTTP:hen MCP-sovelluksissasi:

- **Päivitä palvelinkoodi** käyttämään `transport="streamable-http"`:tä `mcp.run()`:ssä.
- **Päivitä asiakaskoodi** käyttämään `streamablehttp_client`:tä SSE-asiakkaan sijaan.
- **Toteuta viestinkäsittelijä** asiakkaaseen ilmoitusten käsittelemiseksi.
- **Testaa yhteensopivuus** olemassa olevien työkalujen ja työnkulkujen kanssa.

### Yhteensopivuuden ylläpito

On suositeltavaa ylläpitää yhteensopivuus olemassa olevien SSE-asiakkaiden kanssa siirtymäprosessin aikana. Tässä joitakin strategioita:

- Voit tukea sekä SSE:tä että Streamable HTTP:tä ajamalla molemmat kuljetukset eri päätepisteissä.
- Siirrä asiakkaat vähitellen uuteen kuljetukseen.

### Haasteet

Varmista, että käsittelet seuraavat haasteet migraation aikana:

- Varmista kaikkien asiakkaiden päivitys
- Käsittele eroavaisuudet ilmoitusten toimituksessa

### Harjoitus: Luo oma Streamaus-MCP-sovelluksesi

**Käyttötapaus:**
Rakenna MCP-palvelin ja asiakas, jossa palvelin käsittelee listan kohteita (esim. tiedostoja tai dokumentteja) ja lähettää ilmoituksen jokaisesta käsitellystä kohteesta. Asiakkaan tulee näyttää kukin ilmoitus sitä mukaa, kun se saapuu.

**Vaiheet:**

1. Toteuta palvelintyökalu, joka käsittelee listan ja lähettää ilmoituksia jokaisesta kohteesta.
2. Toteuta asiakas, jossa on viestinkäsittelijä ilmoitusten näyttämiseksi reaaliajassa.
3. Testaa toteutuksesi ajamalla palvelin ja asiakas ja seuraa saapuvia ilmoituksia.

[Ratkaisu](./solution/README.md)

## Lisälukemista ja seuraavat askeleet

Jatka matkaasi MCP-streamauksen parissa ja laajenna osaamistasi. Tämä osio tarjoaa lisäresursseja ja ehdotuksia seuraavista vaiheista kehittyneempien sovellusten rakentamiseksi.

### Lisälukemista

- [Microsoft: Johdanto HTTP-streamaukseen](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core:ssa](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mitä seuraavaksi?

- Kokeile rakentaa edistyneempiä MCP-työkaluja, jotka käyttävät streamausta reaaliaikaisen analytiikan, chatin tai yhteismuokkausten toteutukseen.
- Tutki MCP-streamauksen integrointia frontend-kehyksiin (React, Vue, jne.) live-käyttöliittymäpäivityksiä varten.
- Seuraavaksi: [Microsoft Foundry Toolkitin käyttö Visual Studio Codessa](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->