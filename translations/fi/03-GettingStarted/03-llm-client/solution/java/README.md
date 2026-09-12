# Laskin LLM -asiakas

> [!NOTE]
> Tämä ratkaisu yhdistää kurssin perinteiseen HTTP+SSE-laskinpalveluun ja
> käyttää MCP:n `2025-11-25` SDK-rajapintoja. Se ei ole `2026-07-28` Streamable HTTP
> -esimerkki.

Java-sovellus, joka näyttää kuinka käyttää LangChain4j:ää yhdistämiseen MCP (Model Context Protocol) -laskinpalveluun MiniMax OpenAI-yhteensopivan API:n kautta.

## Esivaatimukset

- Java 21 tai uudempi
- Maven 3.6+ (tai käytä mukana tulevaa Maven-wrapperia)
- MiniMax API-avain
- MCP-laskinpalvelu käynnissä osoitteessa `http://localhost:8080`

## API-avaimen hankkiminen

Tämä sovellus käyttää MiniMax OpenAI-yhteensopivaa API:a. Noudata näitä ohjeita saadaksesi avaimen ja päätepisteen:

### 1. Valitse päätepiste
1. Käytä `https://api.minimax.io/v1` globaaliin päätepisteeseen
2. Käytä `https://api.minimaxi.com/v1` Kiinan päätepisteeseen

### 2. Luo API-avain
1. Luo MiniMax API-avain MiniMax-tililtäsi
2. Säilytä avain turvallisessa paikassa

### 3. Aseta ympäristömuuttujat

#### Windowsissa (Komentokehote):
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### Windowsissa (PowerShell):
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### macOS/Linux:
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## Asennus ja käyttöönotto

1. **Kloonaa tai siirry projektihakemistoon**

2. **Asenna riippuvuudet**:
   ```cmd
   mvnw clean install
   ```
   Tai jos Maven on asennettu globaalisti:
   ```cmd
   mvn clean install
   ```

3. **Aseta ympäristömuuttujat** (katso "API-avaimen hankkiminen" yllä)

4. **Käynnistä MCP-laskinpalvelu**:
   Varmista, että luvun 1 MCP-laskinpalvelu on käynnissä osoitteessa `http://localhost:8080/sse`. Sen tulee olla käynnissä ennen asiakkaan käynnistämistä.

## Sovelluksen ajaminen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mitä sovellus tekee

Sovellus demonstroi kolmea päätoimintoa laskinpalvelun kanssa:

1. **Yhteenlasku**: Laskee luvun 24.5 ja 17.3 summan
2. **Neliöjuuri**: Laskee luvun 144 neliöjuuren
3. **Ohje**: Näyttää käytettävissä olevat laskinfunktion toiminnot

## Odotettu tulos

Kun suoritat onnistuneesti, sinun pitäisi nähdä tuloste, joka on samanlainen kuin:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Vianetsintä

### Yleisiä ongelmia

1. **"OPENAI_API_KEY -ympäristömuuttujaa ei ole asetettu"**
   - Varmista, että olet asettanut `OPENAI_API_KEY`-ympäristömuuttujan
   - Käynnistä komentorivi tai terminaali uudelleen muuttujan asettamisen jälkeen

2. **"Yhteys localhost:8080 estetty"**
   - Varmista, että MCP-laskinpalvelu on käynnissä portissa 8080
   - Tarkista, ettei toinen palvelu käytä porttia 8080

3. **"Autentikointi epäonnistui"**
   - Varmista, että API-avaimesi on kelvollinen
   - Tarkista, että `OPENAI_BASE_URL` vastaa käyttämääsi päätepistettä

4. **Maven-rakennusvirheet**
   - Varmista, että käytät Java 21 tai uudempaa: `java -version`
   - Yritä puhdistaa rakennus: `mvnw clean`

### Virheenkorjaus

Debug-lokin aktivoimiseksi lisää seuraava JVM-parametri ajon yhteydessä:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfigurointi

Sovellus on konfiguroitu seuraavasti:
- Käyttämään oletuksena MiniMax-M3:ta; aseta `MINIMAX_MODEL_ID` valitaksesi joko `MiniMax-M3` tai `MiniMax-M2.7`
- Yhdistämään `OPENAI_BASE_URL`:iin, jos se on asetettu; muuten käyttää `https://api.minimaxi.com/v1` kun `MINIMAX_REGION=cn_zh`, tai oletuksena `https://api.minimax.io/v1`
- Yhdistämään MCP-palveluun osoitteessa `http://localhost:8080/sse`
- Käyttämään 60 sekunnin aikakatkaisua pyynnöille

## Riippuvuudet

Keskeiset tämän projektin riippuvuudet:
- **LangChain4j**: tekoälyintegraatioon ja työkaluhallintaan
- **LangChain4j MCP**: Model Context Protocol -tuella
- **LangChain4j OpenAI official**: MiniMax OpenAI-yhteensopivan API:n integrointiin
- **Spring Boot**: sovelluskehykseen ja riippuvuussuhteiden injektointiin

## Lisenssi

Tämä projekti on lisensoitu Apache License 2.0 -lisenssillä - lisätietoja löydät [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE)-tiedostosta.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->