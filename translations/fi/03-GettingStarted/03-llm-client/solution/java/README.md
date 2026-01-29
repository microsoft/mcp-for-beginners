# Calculator LLM Client

Java-sovellus, joka näyttää, miten LangChain4j:ta käytetään yhdistämään MCP (Model Context Protocol) -laskinpalveluun GitHub Models -integraation kanssa.

## Vaatimukset

- Java 21 tai uudempi
- Maven 3.6+ (tai käytä mukana tulevaa Maven-wrapperia)
- GitHub-tili, jolla on pääsy GitHub Models -palveluun
- MCP-laskinpalvelu käynnissä osoitteessa `http://localhost:8080`

## GitHub-tokenin hankkiminen

Tämä sovellus käyttää GitHub Models -palvelua, joka vaatii GitHubin henkilökohtaisen käyttöoikeustunnuksen. Noudata näitä ohjeita saadaksesi tokenin:

### 1. Siirry GitHub Models -palveluun
1. Mene osoitteeseen [GitHub Models](https://github.com/marketplace/models)
2. Kirjaudu sisään GitHub-tililläsi
3. Pyydä pääsy GitHub Models -palveluun, jos et ole sitä vielä tehnyt

### 2. Luo henkilökohtainen käyttöoikeustunnus
1. Mene osoitteeseen [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Klikkaa "Generate new token" → "Generate new token (classic)"
3. Anna tokenillesi kuvaava nimi (esim. "MCP Calculator Client")
4. Aseta vanhenemisaika tarpeen mukaan
5. Valitse seuraavat oikeudet:
   - `repo` (jos käytät yksityisiä repositorioita)
   - `user:email`
6. Klikkaa "Generate token"
7. **Tärkeää**: Kopioi token heti – et näe sitä enää uudelleen!

### 3. Aseta ympäristömuuttuja

#### Windowsissa (Komentokehote):
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### Windowsissa (PowerShell):
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### macOS/Linux:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Asennus ja käyttöönotto

1. **Kloonaa tai siirry projektin kansioon**

2. **Asenna riippuvuudet**:
   ```cmd
   mvnw clean install
   ```
   Tai jos Maven on asennettuna globaalisti:
   ```cmd
   mvn clean install
   ```

3. **Aseta ympäristömuuttuja** (katso "GitHub-tokenin hankkiminen" yllä)

4. **Käynnistä MCP Calculator Service**:
   Varmista, että luku 1:n MCP-laskinpalvelu on käynnissä osoitteessa `http://localhost:8080/sse`. Palvelun tulee olla käynnissä ennen asiakkaan käynnistämistä.

## Sovelluksen käynnistäminen

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Mitä sovellus tekee

Sovellus näyttää kolme pääasiallista vuorovaikutusta laskinpalvelun kanssa:

1. **Yhteenlasku**: Laskee luvut 24.5 ja 17.3 yhteen
2. **Neliöjuuri**: Laskee luvun 144 neliöjuuren
3. **Ohje**: Näyttää käytettävissä olevat laskintoiminnot

## Odotettu tulos

Onnistuneen suorituksen jälkeen näet tulosteen, joka näyttää suunnilleen tältä:

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## Vianetsintä

### Yleisiä ongelmia

1. **"GITHUB_TOKEN environment variable not set"**
   - Varmista, että olet asettanut `GITHUB_TOKEN`-ympäristömuuttujan
   - Käynnistä komentokehote/terminaali uudelleen muuttujan asettamisen jälkeen

2. **"Connection refused to localhost:8080"**
   - Varmista, että MCP-laskinpalvelu on käynnissä portissa 8080
   - Tarkista, ettei jokin muu palvelu käytä porttia 8080

3. **"Authentication failed"**
   - Tarkista, että GitHub-tokenisi on voimassa ja sillä on oikeat oikeudet
   - Varmista, että sinulla on pääsy GitHub Models -palveluun

4. **Maven-käännösvirheet**
   - Varmista, että käytössäsi on Java 21 tai uudempi: `java -version`
   - Kokeile puhdistaa käännös: `mvnw clean`

### Virheenkorjaus

Ota debug-lokit käyttöön lisäämällä seuraava JVM-argumentti sovelluksen käynnistyksen yhteydessä:
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## Konfiguraatio

Sovellus on konfiguroitu seuraavasti:
- Käyttää GitHub Models -palvelua mallilla `gpt-4.1-nano`
- Yhdistää MCP-palveluun osoitteessa `http://localhost:8080/sse`
- Käyttää 60 sekunnin aikakatkaisua pyyntöihin
- Ottaa käyttöön pyyntöjen ja vastausten lokituksen virheenkorjausta varten

## Riippuvuudet

Tämän projektin keskeiset riippuvuudet:
- **LangChain4j**: AI-integraatioon ja työkalujen hallintaan
- **LangChain4j MCP**: Model Context Protocol -tuen tarjoamiseen
- **LangChain4j GitHub Models**: GitHub Models -integraatioon
- **Spring Boot**: Sovelluskehykseen ja riippuvuuksien injektointiin

## Lisenssi

Tämä projekti on lisensoitu Apache License 2.0 -lisenssillä – katso lisätiedot [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) -tiedostosta.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.