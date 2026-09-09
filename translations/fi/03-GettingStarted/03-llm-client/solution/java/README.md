# Laskin LLM -asiakas

Java-sovellus, joka näyttää, kuinka LangChain4j:ää käytetään yhdistämään MCP (Mallikontekstiprotokolla) -laskinpalveluun MiniMax OpenAI-yhteensopivan API:n kautta.

## Edellytykset

- Java 21 tai uudempi
- Maven 3.6+ (tai käytä mukana olevaa Maven-wrapperia)
- MiniMax API-avain
- MCP-laskinpalvelu käynnissä osoitteessa `http://localhost:8080`

## API-avaimen hankinta

Tämä sovellus käyttää MiniMax OpenAI-yhteensopivaa API:a. Noudata näitä ohjeita saadaksesi avaimen ja päätepisteen:

### 1. Valitse päätepiste
1. Käytä `https://api.minimax.io/v1` globaalille päätepisteelle
2. Käytä `https://api.minimaxi.com/v1` Kiinan päätepisteelle

### 2. Luo API-avain
1. Luo MiniMax API-avain MiniMax-tililtäsi
2. Säilytä avain turvallisesti

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

1. **Kloonaa tai siirry projektin hakemistoon**

2. **Asenna riippuvuudet**:
   ```cmd
   mvnw clean install
   ```
   Tai jos Maven on asennettu globaalisti:
   ```cmd
   mvn clean install
   ```

3. **Aseta ympäristömuuttujat** (katso "API-avaimen hankinta" yllä)

4. **Käynnistä MCP-laskinpalvelu**:
   Varmista, että luvun 1 MCP-laskinpalvelu on käynnissä osoitteessa `http://localhost:8080/sse`. Sen tulee olla käynnissä ennen asiakasohjelman käynnistystä.

## Sovelluksen käynnistäminen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mitä sovellus tekee

Sovellus näyttää kolme pääasiallista vuorovaikutusta laskinpalvelun kanssa:

1. **Yhteenlasku**: Laskee luvut 24.5 ja 17.3 yhteen
2. **Neliöjuuri**: Laskee luvun 144 neliöjuuren
3. **Ohje**: Näyttää saatavilla olevat laskintoiminnot

## Odotettu tulos

Kun suoritat onnistuneesti, näet tuloksen, joka on samankaltainen kuin:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Vianetsintä

### Yleisiä ongelmia

1. **"OPENAI_API_KEY -ympäristömuuttujaa ei ole asetettu"**
   - Varmista, että olet asettanut `OPENAI_API_KEY` -ympäristömuuttujan
   - Käynnistä komentotulkki/terminaali uudelleen muuttujan asettamisen jälkeen

2. **"Yhteys kielletty localhost:8080"**
   - Varmista että MCP-laskinpalvelu on käynnissä portissa 8080
   - Tarkista, ettei toinen palvelu käytä porttia 8080

3. **"Todentaminen epäonnistui"**
   - Tarkista API-avaimesi kelvollisuus
   - Varmista, että `OPENAI_BASE_URL` vastaa käyttämääsi päätepistettä

4. **Maven-käännösvirheet**
   - Varmista, että käytät Java 21:tä tai uudempaa: `java -version`
   - Kokeile puhdistaa käännös: `mvnw clean`

### Virheenetsintä

Debug-lokin käyttöönotto onnistuu lisäämällä seuraava JVM-argumentti käynnistyksen yhteydessä:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguraatio

Sovellus on konfiguroitu seuraavasti:
- Oletuksena käytetään MiniMax-M3:a; aseta `MINIMAX_MODEL_ID` valitaksesi joko `MiniMax-M3` tai `MiniMax-M2.7`
- Yhdistetään `OPENAI_BASE_URL` osoitteeseen, jos se on asetettu; muuten käytetään `https://api.minimaxi.com/v1` osoitetta, kun `MINIMAX_REGION=cn_zh`, tai oletuksena `https://api.minimax.io/v1`
- Yhdistetään MCP-palveluun osoitteessa `http://localhost:8080/sse`
- Käytetään 60 sekunnin aikakatkaisua pyynnöille

## Riippuvuudet

Tämän projektin keskeiset riippuvuudet:
- **LangChain4j**: AI-integraatioon ja työkalujen hallintaan
- **LangChain4j MCP**: Mallikontekstiprotokollan tukeen
- **LangChain4j OpenAI official**: MiniMax OpenAI-yhteensopivan API-integraation toteuttamiseen
- **Spring Boot**: Sovelluskehykseen ja riippuvuushallintaan

## Lisenssi

Tämä projekti on lisensoitu Apache-lisenssillä 2.0 - katso [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) tiedostosta lisätiedot.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->