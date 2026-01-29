# Calculator HTTP Streaming Demo

Tämä projekti esittelee HTTP-streamausta Server-Sent Events (SSE) -tekniikalla Spring Boot WebFluxin avulla. Se koostuu kahdesta sovelluksesta:

- **Calculator Server**: reaktiivinen verkkopalvelu, joka suorittaa laskutoimituksia ja lähettää tulokset SSE:n kautta
- **Calculator Client**: asiakassovellus, joka kuluttaa streamaavaa päätepistettä

## Vaatimukset

- Java 17 tai uudempi
- Maven 3.6 tai uudempi

## Projektin rakenne

```
java/
├── calculator-server/     # Spring Boot server with SSE endpoint
│   ├── src/main/java/com/example/calculatorserver/
│   │   ├── CalculatorServerApplication.java
│   │   └── CalculatorController.java
│   └── pom.xml
├── calculator-client/     # Spring Boot client application
│   ├── src/main/java/com/example/calculatorclient/
│   │   └── CalculatorClientApplication.java
│   └── pom.xml
└── README.md
```

## Miten se toimii

1. **Calculator Server** tarjoaa `/calculate`-päätepisteen, joka:
   - Ottaa vastaan kyselyparametrit: `a` (numero), `b` (numero), `op` (operaatio)
   - Tuetut operaatiot: `add`, `sub`, `mul`, `div`
   - Palauttaa Server-Sent Events -viestejä laskennan etenemisestä ja tuloksesta

2. **Calculator Client** yhdistää palvelimeen ja:
   - Tekee pyynnön laskea `7 * 5`
   - Kuluttaa streamaavan vastauksen
   - Tulostaa jokaisen tapahtuman konsoliin

## Sovellusten käynnistäminen

### Vaihtoehto 1: Mavenin käyttäminen (suositeltu)

#### 1. Käynnistä Calculator Server

Avaa terminaali ja siirry palvelimen hakemistoon:

```bash
cd calculator-server
mvn clean package
mvn spring-boot:run
```

Palvelin käynnistyy osoitteeseen `http://localhost:8080`

Näet tulosteen, joka näyttää tältä:
```
Started CalculatorServerApplication in X.XXX seconds
Netty started on port 8080 (http)
```

#### 2. Käynnistä Calculator Client

Avaa **uusi terminaali** ja siirry asiakkaan hakemistoon:

```bash
cd calculator-client
mvn clean package
mvn spring-boot:run
```

Asiakas yhdistää palvelimeen, suorittaa laskutoimituksen ja näyttää streamatut tulokset.

### Vaihtoehto 2: Suora Java-komentojen käyttö

#### 1. Käännä ja käynnistä palvelin:

```bash
cd calculator-server
mvn clean package
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

#### 2. Käännä ja käynnistä asiakas:

```bash
cd calculator-client
mvn clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

## Palvelimen manuaalinen testaus

Voit testata palvelinta myös selaimella tai curl-komennolla:

### Selaimella:
Siirry osoitteeseen: `http://localhost:8080/calculate?a=10&b=5&op=add`

### Curl-komennolla:
```bash
curl "http://localhost:8080/calculate?a=10&b=5&op=add" -H "Accept: text/event-stream"
```

## Odotettu tuloste

Kun ajat asiakasta, näet streamatun tulosteen, joka näyttää suunnilleen tältä:

```
event:info
data:Calculating: 7.0 mul 5.0

event:result
data:35.0
```

## Tuetut operaatiot

- `add` - yhteenlasku (a + b)
- `sub` - vähennyslasku (a - b)
- `mul` - kertolasku (a * b)
- `div` - jakolasku (a / b, palauttaa NaN jos b = 0)

## API-dokumentaatio

### GET /calculate

**Parametrit:**
- `a` (pakollinen): Ensimmäinen luku (double)
- `b` (pakollinen): Toinen luku (double)
- `op` (pakollinen): Operaatio (`add`, `sub`, `mul`, `div`)

**Vastaus:**
- Content-Type: `text/event-stream`
- Palauttaa Server-Sent Events -viestejä laskennan etenemisestä ja tuloksesta

**Esimerkkipyyntö:**
```
GET /calculate?a=7&b=5&op=mul HTTP/1.1
Host: localhost:8080
Accept: text/event-stream
```

**Esimerkkivastaus:**
```
event: info
data: Calculating: 7.0 mul 5.0

event: result
data: 35.0
```

## Vianetsintä

### Yleisiä ongelmia

1. **Portti 8080 on jo käytössä**
   - Lopeta muut sovellukset, jotka käyttävät porttia 8080
   - Tai vaihda palvelimen portti tiedostossa `calculator-server/src/main/resources/application.yml`

2. **Yhteys evätty**
   - Varmista, että palvelin on käynnissä ennen asiakkaan käynnistämistä
   - Tarkista, että palvelin käynnistyi onnistuneesti porttiin 8080

3. **Parametrien nimeämisongelmat**
   - Tässä projektissa on Maven-kääntäjän asetuksena `-parameters`-lippu
   - Jos kohtaat ongelmia parametrien sitomisessa, varmista että projekti on käännetty tällä asetuksella

### Sovellusten pysäyttäminen

- Paina `Ctrl+C` terminaalissa, jossa sovellus on käynnissä
- Tai käytä komentoa `mvn spring-boot:stop`, jos sovellus on taustaprosessina

## Teknologiat

- **Spring Boot 3.3.1** - Sovelluskehys
- **Spring WebFlux** - Reaktiivinen web-kehys
- **Project Reactor** - Reaktiivisten streamien kirjasto
- **Netty** - Ei-blokkaava I/O-palvelin
- **Maven** - Rakennustyökalu
- **Java 17+** - Ohjelmointikieli

## Seuraavat askeleet

Kokeile muokata koodia niin, että:
- Lisää muita matemaattisia operaatioita
- Lisää virheenkäsittely virheellisille operaatioille
- Lisää pyyntö- ja vastauslokitus
- Toteuta autentikointi
- Lisää yksikkötestejä

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.