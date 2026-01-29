# Peruslaskin MCP-palvelu

Tämä palvelu tarjoaa peruslaskutoimituksia Model Context Protocolin (MCP) kautta käyttäen Spring Bootia ja WebFlux-siirtoa. Se on suunniteltu yksinkertaiseksi esimerkiksi aloittelijoille, jotka opettelevat MCP:n toteutuksia.

Lisätietoja löytyy [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) -viitedokumentaatiosta.


## Palvelun käyttö

Palvelu tarjoaa seuraavat API-päätepisteet MCP-protokollan kautta:

- `add(a, b)`: Laskee kahden luvun summan
- `subtract(a, b)`: Vähentää toisen luvun ensimmäisestä
- `multiply(a, b)`: Kertoo kaksi lukua keskenään
- `divide(a, b)`: Jakaa ensimmäisen luvun toisella (tarkistaa nollan)
- `power(base, exponent)`: Laskee luvun potenssin
- `squareRoot(number)`: Laskee neliöjuuren (tarkistaa negatiivisen luvun)
- `modulus(a, b)`: Laskee jakojäännöksen
- `absolute(number)`: Laskee luvun itseisarvon

## Riippuvuudet

Projekti vaatii seuraavat keskeiset riippuvuudet:

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## Projektin kääntäminen

Käännä projekti Mavenilla:
```bash
./mvnw clean install -DskipTests
```

## Palvelimen käynnistäminen

### Javaa käyttäen

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### MCP Inspectorin käyttö

MCP Inspector on hyödyllinen työkalu MCP-palveluiden kanssa työskentelyyn. Käyttääksesi sitä tämän laskinpalvelun kanssa:

1. **Asenna ja käynnistä MCP Inspector** uudessa terminaali-ikkunassa:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Avaa web-käyttöliittymä** klikkaamalla sovelluksen näyttämää URL-osoitetta (yleensä http://localhost:6274)

3. **Määritä yhteys**:
   - Aseta siirtotavaksi "SSE"
   - Aseta URL palvelimesi käynnissä olevaan SSE-päätepisteeseen: `http://localhost:8080/sse`
   - Klikkaa "Connect"

4. **Käytä työkaluja**:
   - Klikkaa "List Tools" nähdäksesi käytettävissä olevat laskutoiminnot
   - Valitse työkalu ja klikkaa "Run Tool" suorittaaksesi toiminnon

![MCP Inspector Screenshot](../../../../../../translated_images/fi/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.