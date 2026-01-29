# HTTPS-suoratoisto Model Context Protocolin (MCP) avulla

Tässä luvussa tarjotaan kattava opas turvallisen, skaalautuvan ja reaaliaikaisen suoratoiston toteuttamiseen Model Context Protocolin (MCP) avulla käyttäen HTTPS:ää. Se käsittelee suoratoiston motivaatiota, käytettävissä olevia siirtomekanismeja, HTTP-suoratoiston toteuttamista MCP:ssä, turvallisuuden parhaita käytäntöjä, siirtymistä SSE:stä sekä käytännön ohjeita omien MCP-suoratoistosovellusten rakentamiseen.

## Siirtomekanismit ja suoratoisto MCP:ssä

Tässä osiossa tarkastellaan MCP:n eri siirtomekanismeja ja niiden roolia reaaliaikaisen viestinnän mahdollistamisessa asiakkaiden ja palvelimien välillä.

### Mikä on siirtomekanismi?

Siirtomekanismi määrittää, miten dataa vaihdetaan asiakkaan ja palvelimen välillä. MCP tukee useita siirtotyyppejä, jotka sopivat erilaisiin ympäristöihin ja tarpeisiin:

- **stdio**: Standardi syöte/tuloste, sopii paikallisiin ja CLI-pohjaisiin työkaluihin. Yksinkertainen, mutta ei sovellu web- tai pilvikäyttöön.
- **SSE (Server-Sent Events)**: Mahdollistaa palvelimien reaaliaikaisten päivitysten lähettämisen asiakkaille HTTP:n kautta. Hyvä web-käyttöliittymille, mutta rajoitettu skaalautuvuudessa ja joustavuudessa.
- **Streamable HTTP**: Moderni HTTP-pohjainen suoratoistosiirto, joka tukee ilmoituksia ja parempaa skaalautuvuutta. Suositeltava useimpiin tuotanto- ja pilviskenaarioihin.

### Vertailutaulukko

Alla oleva vertailutaulukko auttaa ymmärtämään näiden siirtomekanismien erot:

| Siirtomekanismi   | Reaaliaikaiset päivitykset | Suoratoisto | Skaalautuvuus | Käyttötapaus              |
|-------------------|---------------------------|-------------|---------------|---------------------------|
| stdio             | Ei                        | Ei          | Matala        | Paikalliset CLI-työkalut  |
| SSE               | Kyllä                     | Kyllä       | Keskitaso     | Web, reaaliaikaiset päivitykset |
| Streamable HTTP   | Kyllä                     | Kyllä       | Korkea        | Pilvi, moniasiakasympäristöt |

> **Vinkki:** Oikean siirtomekanismin valinta vaikuttaa suorituskykyyn, skaalautuvuuteen ja käyttökokemukseen. **Streamable HTTP** on suositeltava modernien, skaalautuvien ja pilvivalmiiden sovellusten toteutukseen.

Huomaa aiemmissa luvuissa käsitellyt stdio- ja SSE-siirrot sekä tämän luvun keskiössä oleva streamable HTTP.

## Suoratoisto: Konseptit ja motivaatio

Suoratoiston peruskäsitteiden ja motivaation ymmärtäminen on olennaista tehokkaiden reaaliaikaisten viestintäjärjestelmien toteuttamiseksi.

**Suoratoisto** on verkkosovellusohjelmoinnin tekniikka, joka mahdollistaa datan lähettämisen ja vastaanottamisen pieninä, hallittavina paloina tai tapahtumina sen sijaan, että odotettaisiin koko vastauksen valmistumista. Tämä on erityisen hyödyllistä seuraavissa tapauksissa:

- Suuret tiedostot tai tietoaineistot.
- Reaaliaikaiset päivitykset (esim. chat, edistymispalkit).
- Pitkäkestoiset laskennat, joissa käyttäjää halutaan pitää ajan tasalla.

Tässä on, mitä suoratoistosta on hyvä tietää yleisellä tasolla:

- Data toimitetaan vähitellen, ei kerralla.
- Asiakas voi käsitellä dataa sitä mukaa, kun se saapuu.
- Vähentää koettua viivettä ja parantaa käyttökokemusta.

### Miksi käyttää suoratoistoa?

Suoratoiston käytön syyt ovat seuraavat:

- Käyttäjät saavat palautetta heti, eivät vasta lopuksi.
- Mahdollistaa reaaliaikaiset sovellukset ja responsiiviset käyttöliittymät.
- Tehokkaampi verkko- ja laskentaresurssien käyttö.

### Yksinkertainen esimerkki: HTTP-suoratoistopalvelin ja -asiakas

Tässä on yksinkertainen esimerkki suoratoiston toteuttamisesta:

#### Python

**Palvelin (Python, käyttäen FastAPI:ta ja StreamingResponsea):**

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

**Asiakas (Python, käyttäen requests-kirjastoa):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Tämä esimerkki havainnollistaa palvelinta, joka lähettää viestisarjan asiakkaalle sitä mukaa, kun viestit ovat valmiita, sen sijaan että odotettaisiin kaikkien viestien valmistumista.

**Miten se toimii:**

- Palvelin tuottaa jokaisen viestin sitä mukaa, kun se on valmis.
- Asiakas vastaanottaa ja tulostaa jokaisen palan sitä mukaa, kun se saapuu.

**Vaadittavat ominaisuudet:**

- Palvelimen on käytettävä suoratoistovastausta (esim. `StreamingResponse` FastAPI:ssa).
- Asiakkaan on käsiteltävä vastaus suoratoistona (`stream=True` requests-kirjastossa).
- Content-Type on yleensä `text/event-stream` tai `application/octet-stream`.

#### Java

**Palvelin (Java, käyttäen Spring Bootia ja Server-Sent Eventsejä):**

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

**Asiakas (Java, käyttäen Spring WebFlux WebClientiä):**

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

- Käyttää Spring Bootin reaktiivista pinoa ja `Flux`-luokkaa suoratoistoon.
- `ServerSentEvent` tarjoaa rakenteellisen tapahtumasuoratoiston tapahtumatyypeillä.
- `WebClient` ja `bodyToFlux()` mahdollistavat reaktiivisen suoratoiston kulutuksen.
- `delayElements()` simuloi käsittelyaikaa tapahtumien välillä.
- Tapahtumilla voi olla tyyppejä (`info`, `result`) paremman asiakaskäsittelyn mahdollistamiseksi.

### Vertailu: Klassinen suoratoisto vs MCP-suoratoisto

Erot klassisen suoratoiston ja MCP-suoratoiston välillä voidaan kuvata seuraavasti:

| Ominaisuus            | Klassinen HTTP-suoratoisto     | MCP-suoratoisto (ilmoitukset)      |
|-----------------------|-------------------------------|-------------------------------------|
| Päävastaus           | Paloiteltu                   | Yksittäinen, lopussa               |
| Edistymispäivitykset  | Lähetetään datan paloina      | Lähetetään ilmoituksina            |
| Asiakasvaatimukset    | Täytyy käsitellä suoratoisto  | Täytyy toteuttaa viestinkäsittelijä |
| Käyttötapaus          | Suuret tiedostot, AI-tokenit  | Edistyminen, lokit, reaaliaikainen palaute |

### Havaitut keskeiset erot

Lisäksi tässä on joitakin keskeisiä eroja:

- **Viestintämalli:**
  - Klassinen HTTP-suoratoisto: Käyttää yksinkertaista paloittelusiirtoa datan lähettämiseen paloina.
  - MCP-suoratoisto: Käyttää rakenteellista ilmoitusjärjestelmää JSON-RPC-protokollan avulla.

- **Viestimuoto:**
  - Klassinen HTTP: Yksinkertaiset tekstipalat rivinvaihtoineen.
  - MCP: Rakenteelliset `LoggingMessageNotification`-objektit metatiedoilla.

- **Asiakastoteutus:**
  - Klassinen HTTP: Yksinkertainen asiakas, joka käsittelee suoratoistovastauksia.
  - MCP: Kehittyneempi asiakas, jossa on viestinkäsittelijä erilaisten viestien käsittelyyn.

- **Edistymispäivitykset:**
  - Klassinen HTTP: Edistyminen on osa päävastauksen suoratoistoa.
  - MCP: Edistyminen lähetetään erillisinä ilmoitusviesteinä, kun päävastaus saapuu lopuksi.

### Suositukset

Seuraavassa on suosituksia klassisen suoratoiston (esim. `/stream`-päätepisteen) ja MCP-suoratoiston välillä valitsemiseen:

- **Yksinkertaisiin suoratoistotarpeisiin:** Klassinen HTTP-suoratoisto on yksinkertaisempi toteuttaa ja riittävä perussuoratoistotarpeisiin.
- **Monimutkaisiin, interaktiivisiin sovelluksiin:** MCP-suoratoisto tarjoaa rakenteellisemman lähestymistavan, jossa on rikkaammat metatiedot ja erottelu ilmoitusten ja lopputulosten välillä.
- **AI-sovelluksiin:** MCP:n ilmoitusjärjestelmä on erityisen hyödyllinen pitkäkestoisissa AI-tehtävissä, joissa käyttäjää halutaan pitää ajan tasalla edistymisestä.
On kaksi vakuuttavaa syytä päivittää SSE:stä Streamable HTTP:hen:

- Streamable HTTP tarjoaa paremman skaalautuvuuden, yhteensopivuuden ja monipuolisemman ilmoitustuen kuin SSE.
- Se on suositeltu kuljetusmuoto uusille MCP-sovelluksille.

### Siirtymisvaiheet

Näin voit siirtyä SSE:stä Streamable HTTP:hen MCP-sovelluksissasi:

- **Päivitä palvelinkoodi** käyttämään `transport="streamable-http"`-asetusta `mcp.run()`-funktiossa.
- **Päivitä asiakaskoodi** käyttämään `streamablehttp_client`-asiakasta SSE-asiakkaan sijaan.
- **Toteuta viestinkäsittelijä** asiakkaassa ilmoitusten käsittelyä varten.
- **Testaa yhteensopivuus** olemassa olevien työkalujen ja työnkulkujen kanssa.

### Yhteensopivuuden ylläpitäminen

Suositeltavaa on ylläpitää yhteensopivuutta olemassa olevien SSE-asiakkaiden kanssa siirtymäprosessin aikana. Tässä muutamia strategioita:

- Voit tukea sekä SSE:tä että Streamable HTTP:tä käyttämällä molempia kuljetusmuotoja eri päätepisteissä.
- Siirrä asiakkaat vähitellen uuteen kuljetusmuotoon.

### Haasteet

Varmista, että käsittelet seuraavat haasteet siirtymän aikana:

- Varmista, että kaikki asiakkaat päivitetään.
- Käsittele erot ilmoitusten toimituksessa.

## Tietoturvanäkökohdat

Tietoturvan tulisi olla ensisijainen prioriteetti minkä tahansa palvelimen toteutuksessa, erityisesti HTTP-pohjaisten kuljetusmuotojen, kuten Streamable HTTP:n, käytössä MCP:ssä.

Kun toteutat MCP-palvelimia HTTP-pohjaisilla kuljetusmuodoilla, tietoturva nousee keskeiseksi huolenaiheeksi, joka vaatii huolellista huomiointia useisiin hyökkäysvektoreihin ja suojamekanismeihin.

### Yleiskatsaus

Tietoturva on kriittistä MCP-palvelimien altistamisessa HTTP:n kautta. Streamable HTTP tuo mukanaan uusia hyökkäyspintoja ja vaatii huolellista konfigurointia.

Tässä keskeisiä tietoturvanäkökulmia:

- **Origin-otsikon validointi**: Validoi aina `Origin`-otsikko DNS-uudelleensidontahyökkäysten estämiseksi.
- **Paikallinen sidonta**: Kehitysvaiheessa sido palvelimet `localhost`-osoitteeseen, jotta ne eivät altistu julkiselle internetille.
- **Autentikointi**: Toteuta autentikointi (esim. API-avaimet, OAuth) tuotantokäyttöä varten.
- **CORS**: Määritä Cross-Origin Resource Sharing (CORS) -käytännöt pääsyn rajoittamiseksi.
- **HTTPS**: Käytä HTTPS:ää tuotannossa liikenteen salaamiseksi.

### Parhaat käytännöt

Lisäksi tässä muutamia parhaita käytäntöjä tietoturvan toteuttamiseen MCP-suoratoistopalvelimessa:

- Älä koskaan luota saapuviin pyyntöihin ilman validointia.
- Kirjaa ja seuraa kaikki pääsy- ja virhelokit.
- Päivitä riippuvuudet säännöllisesti tietoturvahaavoittuvuuksien korjaamiseksi.

### Haasteet

Tietoturvan toteuttamisessa MCP-suoratoistopalvelimissa kohtaat joitakin haasteita:

- Tietoturvan ja kehityksen helppouden tasapainottaminen
- Yhteensopivuuden varmistaminen eri asiakasympäristöjen kanssa

### Tehtävä: Rakenna oma suoratoistava MCP-sovellus

**Tilanne:**
Rakenna MCP-palvelin ja asiakas, jossa palvelin käsittelee listan kohteita (esim. tiedostoja tai dokumentteja) ja lähettää ilmoituksen jokaisesta käsitellystä kohteesta. Asiakkaan tulisi näyttää jokainen ilmoitus sen saapuessa.

**Vaiheet:**

1. Toteuta palvelintyökalu, joka käsittelee listan ja lähettää ilmoituksia jokaisesta kohteesta.
2. Toteuta asiakas, jossa on viestinkäsittelijä ilmoitusten näyttämiseksi reaaliajassa.
3. Testaa toteutuksesi ajamalla sekä palvelin että asiakas ja tarkkaile ilmoituksia.

[Solution](./solution/README.md)

## Lisälukemista ja seuraavat askeleet

Jatka MCP-suoratoiston parissa ja laajenna tietämystäsi tämän osion lisäresurssien ja ehdotettujen seuraavien askelten avulla rakentaaksesi edistyneempiä sovelluksia.

### Lisälukemista

- [Microsoft: Johdatus HTTP-suoratoistoon](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core:ssa](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Suoratoistopyynnöt](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Seuraavat askeleet

- Kokeile rakentaa edistyneempiä MCP-työkaluja, jotka hyödyntävät suoratoistoa reaaliaikaiseen analytiikkaan, keskusteluihin tai yhteistyömuokkaukseen.
- Tutki MCP-suoratoiston integrointia frontend-kehyksiin (React, Vue jne.) reaaliaikaisia käyttöliittymäpäivityksiä varten.
- Seuraavaksi: [AI Toolkitin hyödyntäminen VSCode:ssa](../07-aitk/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.