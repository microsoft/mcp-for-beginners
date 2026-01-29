# Täydelliset MCP-asiakasohjelman esimerkit

Tämä hakemisto sisältää täydellisiä, toimivia esimerkkejä MCP-asiakasohjelmista eri ohjelmointikielillä. Jokainen asiakasohjelma esittelee kaikki pääasiallisessa README.md-oppaassa kuvatut toiminnot.

## Saatavilla olevat asiakasohjelmat

### 1. Java-asiakasohjelma (`client_example_java.java`)

- **Kuljetus**: SSE (Server-Sent Events) HTTP:n kautta
- **Kohdepalvelin**: `http://localhost:8080`
- **Ominaisuudet**:
  - Yhteyden muodostaminen ja ping
  - Työkalujen listaus
  - Laskinoperaatiot (lisää, vähennä, kerro, jaa, apu)
  - Virheenkäsittely ja tulosten purkaminen

**Suorita:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C#-asiakasohjelma (`client_example_csharp.cs`)

- **Kuljetus**: Stdio (Standard Input/Output)
- **Kohdepalvelin**: Paikallinen .NET MCP-palvelin dotnet run -komennolla
- **Ominaisuudet**:
  - Automaattinen palvelimen käynnistys stdio-kuljetuksen kautta
  - Työkalujen ja resurssien listaus
  - Laskinoperaatiot
  - JSON-tulosten jäsennys
  - Kattava virheenkäsittely

**Suorita:**

```bash
dotnet run
```

### 3. TypeScript-asiakasohjelma (`client_example_typescript.ts`)

- **Kuljetus**: Stdio (Standard Input/Output)
- **Kohdepalvelin**: Paikallinen Node.js MCP-palvelin
- **Ominaisuudet**:
  - Täysi MCP-protokollan tuki
  - Työkalujen, resurssien ja kehotteiden toiminnot
  - Laskinoperaatiot
  - Resurssien lukeminen ja kehotteiden suorittaminen
  - Vahva virheenkäsittely

**Suorita:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python-asiakasohjelma (`client_example_python.py`)

- **Kuljetus**: Stdio (Standard Input/Output)  
- **Kohdepalvelin**: Paikallinen Python MCP-palvelin
- **Ominaisuudet**:
  - Async/await-malli operaatioille
  - Työkalujen ja resurssien etsintä
  - Laskinoperaatioiden testaus
  - Resurssien sisällön lukeminen
  - Luokkapohjainen organisointi

**Suorita:**

```bash
python client_example_python.py
```

## Yhteiset ominaisuudet kaikille asiakasohjelmille

Jokainen asiakasohjelman toteutus esittelee:

1. **Yhteyden hallinta**
   - Yhteyden muodostaminen MCP-palvelimeen
   - Yhteysvirheiden käsittely
   - Asianmukainen siivous ja resurssien hallinta

2. **Palvelimen etsintä**
   - Saatavilla olevien työkalujen listaus
   - Saatavilla olevien resurssien listaus (jos tuettu)
   - Saatavilla olevien kehotteiden listaus (jos tuettu)

3. **Työkalujen käyttö**
   - Peruslaskinoperaatiot (lisää, vähennä, kerro, jaa)
   - Apu-komento palvelintietojen saamiseksi
   - Asianmukainen argumenttien välitys ja tulosten käsittely

4. **Virheenkäsittely**
   - Yhteysvirheet
   - Työkalujen suoritusvirheet
   - Hallittu epäonnistuminen ja käyttäjäpalautteen antaminen

5. **Tulosten käsittely**
   - Tekstisisällön purkaminen vastauksista
   - Tulosten muotoilu luettavuuden parantamiseksi
   - Eri vastausmuotojen käsittely

## Esivaatimukset

Ennen näiden asiakasohjelmien suorittamista varmista, että:

1. **Vastaava MCP-palvelin on käynnissä** (hakemistosta `../01-first-server/`)
2. **Vaaditut riippuvuudet on asennettu** valitsemallesi kielelle
3. **Asianmukainen verkkoyhteys** (HTTP-pohjaisille kuljetuksille)

## Keskeiset erot toteutusten välillä

| Kieli       | Kuljetus   | Palvelimen käynnistys | Async-malli | Keskeiset kirjastot       |
|-------------|------------|-----------------------|-------------|---------------------------|
| Java        | SSE/HTTP   | Ulkoinen             | Synkroninen | WebFlux, MCP SDK          |
| C#          | Stdio      | Automaattinen        | Async/Await | .NET MCP SDK              |
| TypeScript  | Stdio      | Automaattinen        | Async/Await | Node MCP SDK              |
| Python      | Stdio      | Automaattinen        | AsyncIO     | Python MCP SDK            |
| Rust        | Stdio      | Automaattinen        | Async/Await | Rust MCP SDK, Tokio       |

## Seuraavat askeleet

Kun olet tutustunut näihin asiakasohjelmien esimerkkeihin:

1. **Muokkaa asiakasohjelmia** lisätäksesi uusia ominaisuuksia tai toimintoja
2. **Luo oma palvelimesi** ja testaa sitä näillä asiakasohjelmilla
3. **Kokeile eri kuljetuksia** (SSE vs. Stdio)
4. **Rakenna monimutkaisempi sovellus**, joka integroi MCP-toiminnallisuutta

## Vianmääritys

### Yleiset ongelmat

1. **Yhteys kielletty**: Varmista, että MCP-palvelin on käynnissä odotetussa portissa/polussa
2. **Moduulia ei löydy**: Asenna vaadittu MCP SDK valitsemallesi kielelle
3. **Käyttöoikeus kielletty**: Tarkista tiedostojen käyttöoikeudet stdio-kuljetukselle
4. **Työkalua ei löydy**: Varmista, että palvelin toteuttaa odotetut työkalut

### Vinkkejä virheiden korjaamiseen

1. **Ota käyttöön yksityiskohtainen lokitus** MCP SDK:ssa
2. **Tarkista palvelimen lokit** virheilmoitusten varalta
3. **Varmista työkalujen nimet ja allekirjoitukset** vastaavat asiakasohjelman ja palvelimen välillä
4. **Testaa ensin MCP Inspectorilla** palvelimen toiminnallisuuden varmistamiseksi

## Liittyvä dokumentaatio

- [Pääasiakasohjelman opas](./README.md)
- [MCP-palvelimen esimerkit](../../../../03-GettingStarted/01-first-server)
- [MCP ja LLM-integraatio](../../../../03-GettingStarted/03-llm-client)
- [Virallinen MCP-dokumentaatio](https://modelcontextprotocol.io/)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.