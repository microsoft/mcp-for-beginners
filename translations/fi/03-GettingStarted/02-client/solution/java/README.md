# MCP Java Client - Laskin Demo

Tämä projekti näyttää, miten luodaan Java-asiakas, joka yhdistää MCP (Model Context Protocol) -palvelimeen ja kommunikoi sen kanssa. Tässä esimerkissä yhdistämme luvun 01 laskinpalvelimeen ja suoritetaan erilaisia matemaattisia operaatioita.

## Vaatimukset

Ennen tämän asiakkaan käynnistämistä sinun tulee:

1. **Käynnistää luvun 01 laskinpalvelin**:
   - Siirry laskinpalvelimen hakemistoon: `03-GettingStarted/01-first-server/solution/java/`
   - Käännä ja käynnistä laskinpalvelin:
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - Palvelimen pitäisi olla käynnissä osoitteessa `http://localhost:8080`

2. **Java 21 tai uudempi** asennettuna järjestelmääsi
3. **Maven** (sisältyy Maven Wrapperin kautta)

## Mikä on SDKClient?

`SDKClient` on Java-sovellus, joka näyttää, miten:
- Yhdistetään MCP-palvelimeen Server-Sent Events (SSE) -kuljetuksella
- Listataan palvelimen tarjoamat työkalut
- Kutsutaan erilaisia laskimen toimintoja etänä
- Käsitellään vastauksia ja näytetään tulokset

## Miten se toimii

Asiakas käyttää Spring AI MCP -kehystä seuraavasti:

1. **Yhdistää**: Luo WebFlux SSE -asiakaskuljetuksen yhdistääkseen laskinpalvelimeen
2. **Alustaa asiakkaan**: Määrittää MCP-asiakkaan ja muodostaa yhteyden
3. **Löytää työkalut**: Listaa kaikki käytettävissä olevat laskinoperaatiot
4. **Suorittaa operaatiot**: Kutsuu erilaisia matemaattisia funktioita esimerkkidatalla
5. **Näyttää tulokset**: Esittää kunkin laskutoimituksen tulokset

## Projektin rakenne

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## Keskeiset riippuvuudet

Projekti käyttää seuraavia keskeisiä riippuvuuksia:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

Tämä riippuvuus tarjoaa:
- `McpClient` - pääasiakasrajapinnan
- `WebFluxSseClientTransport` - SSE-kuljetuksen web-pohjaiseen viestintään
- MCP-protokollan skeemat sekä pyyntö- ja vastaustyypit

## Projektin kääntäminen

Käännä projekti Maven Wrapperilla:

```cmd
.\mvnw clean install
```

## Asiakkaan käynnistäminen

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**Huom**: Varmista, että laskinpalvelin on käynnissä osoitteessa `http://localhost:8080` ennen komentojen suorittamista.

## Mitä asiakas tekee

Kun ajat asiakkaan, se:

1. **Yhdistää** laskinpalvelimeen osoitteessa `http://localhost:8080`
2. **Listaa työkalut** - näyttää kaikki käytettävissä olevat laskinoperaatiot
3. **Suorittaa laskutoimituksia**:
   - Yhteenlasku: 5 + 3 = 8
   - Vähennyslasku: 10 - 4 = 6
   - Kertolasku: 6 × 7 = 42
   - Jakolasku: 20 ÷ 4 = 5
   - Potenssi: 2^8 = 256
   - Neliöjuuri: √16 = 4
   - Absoluuttinen arvo: |-5.5| = 5.5
   - Ohje: näyttää käytettävissä olevat operaatiot

## Odotettu tulos

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**Huom**: Maven saattaa näyttää varoituksia jäljellä olevista säikeistä lopussa – tämä on normaalia reaktiivisissa sovelluksissa eikä tarkoita virhettä.

## Koodin ymmärtäminen

### 1. Kuljetuksen määrittely
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
Tämä luo SSE (Server-Sent Events) -kuljetuksen, joka yhdistää laskinpalvelimeen.

### 2. Asiakkaan luonti
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
Luo synkronisen MCP-asiakkaan ja alustaa yhteyden.

### 3. Työkalujen kutsuminen
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
Kutsuu "add"-työkalua parametreilla a=5.0 ja b=3.0.

## Vianetsintä

### Palvelin ei ole käynnissä
Jos saat yhteysvirheitä, varmista, että luvun 01 laskinpalvelin on käynnissä:
```
Error: Connection refused
```
**Ratkaisu**: Käynnistä ensin laskinpalvelin.

### Portti on jo käytössä
Jos portti 8080 on varattu:
```
Error: Address already in use
```
**Ratkaisu**: Lopeta muut porttia 8080 käyttävät sovellukset tai muuta palvelimen porttia.

### Käännösvirheet
Jos kohtaat käännösvirheitä:
```cmd
.\mvnw clean install -DskipTests
```

## Lisätietoja

- [Spring AI MCP Documentation](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [Spring WebFlux Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.