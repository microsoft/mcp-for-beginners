# AGENTS.md

## Projektin yleiskatsaus

**MCP for Beginners** on avoimen lähdekoodin opetusohjelma Model Context Protocolin (MCP) oppimiseen - standardoitu kehys AI-mallien ja asiakassovellusten välisille vuorovaikutuksille. Tämä arkisto tarjoaa kattavat oppimateriaalit käytännön koodiesimerkeillä useilla ohjelmointikielillä.

### Keskeiset teknologiat

- **Ohjelmointikielet**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Kehykset ja SDK:t**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Tietokannat**: PostgreSQL pgvector-laajennuksella
- **Pilvialustat**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Rakennustyökalut**: npm, Maven, pip, Cargo
- **Dokumentaatio**: Markdown automaattisella monikielisellä käännöksellä (48+ kieltä)

### Arkkitehtuuri

- **11 ydinosiota (00-11)**: Järjestelmällinen oppimispolku perusteista edistyneisiin aiheisiin
- **Käytännön harjoitukset**: Käytännön tehtäviä täydellisillä ratkaisukoodilla useilla kielillä
- **Esimerkkiprojektit**: Toimivat MCP-palvelin- ja asiakasohjelmointitoteutukset
- **Käännösjärjestelmä**: Automaattinen GitHub Actions -työnkulku monikielistä tukea varten
- **Kuvamateriaalit**: Keskitetty kuvahakemisto käännetyillä versioilla

## Asennuskomennot

Tämä on dokumentaatiokeskeinen arkisto. Suurin osa asennuksesta tapahtuu yksittäisten esimerkkiprojektien ja harjoitusten yhteydessä.

### Arkiston asennus

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Työskentely esimerkkiprojektien kanssa

Esimerkkiprojektit sijaitsevat:
- `03-GettingStarted/samples/` - Kieleen liittyvät esimerkit
- `03-GettingStarted/01-first-server/solution/` - Ensimmäiset palvelintoteutukset
- `03-GettingStarted/02-client/solution/` - Asiakastoteutukset
- `11-MCPServerHandsOnLabs/` - Kattavat tietokantaintegraatioharjoitukset

Jokaisessa esimerkkiprojektissa on omat asennusohjeet:

#### TypeScript/JavaScript-projektit
```bash
cd <project-directory>
npm install
npm start
```

#### Python-projektit
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java-projektit
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Kehitystyönkulku

### Dokumentaation rakenne

- **Osat 00-11**: Ydinkurssisisältö järjestyksessä
- **translations/**: Kieleen liittyvät versiot (automaattisesti luotu, älä muokkaa suoraan)
- **translated_images/**: Paikallistetut kuvaversiot (automaattisesti luotu)
- **images/**: Lähdekuvat ja kaaviot

### Dokumentaation muutosten tekeminen

1. Muokkaa vain englanninkielisiä markdown-tiedostoja päämoduulihakemistoissa (00-11)
2. Päivitä kuvat `images/`-hakemistossa tarvittaessa
3. co-op-translator GitHub Action luo automaattisesti käännökset
4. Käännökset luodaan uudelleen, kun muutokset työnnetään päähaaraan

### Työskentely käännösten kanssa

- **Automaattinen käännös**: GitHub Actions -työnkulku hoitaa kaikki käännökset
- **Älä muokkaa manuaalisesti** tiedostoja `translations/`-hakemistossa
- Käännösten metadata on upotettu jokaiseen käännettyyn tiedostoon
- Tuetut kielet: 48+ kieltä, mukaan lukien arabia, kiina, ranska, saksa, hindi, japani, korea, portugali, venäjä, espanja ja monet muut

## Testausohjeet

### Dokumentaation validointi

Koska tämä on pääasiassa dokumentaatioarkisto, testaus keskittyy:

1. **Linkkien validointi**: Varmista, että kaikki sisäiset linkit toimivat
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Koodiesimerkkien validointi**: Testaa, että koodiesimerkit kääntyvät/toimivat
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-tarkistus**: Tarkista muotoilun johdonmukaisuus
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Esimerkkiprojektien testaus

Jokaisella kieleen liittyvällä esimerkillä on oma testauslähestymistapansa:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Koodityyliohjeet

### Dokumentaatiotyyli

- Käytä selkeää, aloittelijaystävällistä kieltä
- Sisällytä koodiesimerkkejä useilla kielillä, jos mahdollista
- Noudata markdownin parhaita käytäntöjä:
  - Käytä ATX-tyylisiä otsikoita (`#`-syntaksi)
  - Käytä aidattuja koodilohkoja kielitunnisteilla
  - Sisällytä kuvien kuvaileva alt-teksti
  - Pidä rivien pituudet kohtuullisina (ei tiukkaa rajaa, mutta ole järkevä)

### Koodiesimerkkityyli

#### TypeScript/JavaScript
- Käytä ES-moduuleja (`import`/`export`)
- Noudata TypeScriptin tiukan tilan käytäntöjä
- Sisällytä tyyppimerkinnät
- Kohdista ES2022

#### Python
- Noudata PEP 8 -tyyliohjeita
- Käytä tyyppivihjeitä tarvittaessa
- Sisällytä docstringit funktioille ja luokille
- Käytä moderneja Python-ominaisuuksia (3.8+)

#### Java
- Noudata Spring Boot -käytäntöjä
- Käytä Java 21 -ominaisuuksia
- Noudata standardia Maven-projektirakennetta
- Sisällytä Javadoc-kommentit

### Tiedostojen organisointi

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Rakennus ja käyttöönotto

### Dokumentaation käyttöönotto

Arkisto käyttää GitHub Pagesia tai vastaavaa dokumentaation isännöintiin (jos sovellettavissa). Muutokset päähaaraan käynnistävät:

1. Käännöstyönkulun (`.github/workflows/co-op-translator.yml`)
2. Kaikkien englanninkielisten markdown-tiedostojen automaattisen käännöksen
3. Kuvien paikallistamisen tarvittaessa

### Ei vaadittua rakennusprosessia

Tämä arkisto sisältää pääasiassa markdown-dokumentaatiota. Ydinkurssisisällölle ei tarvita kääntämistä tai rakennusvaihetta.

### Esimerkkiprojektien käyttöönotto

Yksittäisillä esimerkkiprojekteilla voi olla käyttöönotto-ohjeita:
- Katso `03-GettingStarted/09-deployment/` MCP-palvelimen käyttöönotto-ohjeet
- Azure Container Apps -käyttöönottoesimerkit `11-MCPServerHandsOnLabs/`-hakemistossa

## Osallistumisohjeet

### Pull Request -prosessi

1. **Fork ja kloonaus**: Haarauta arkisto ja kloonaa haarasi paikallisesti
2. **Luo haara**: Käytä kuvailevia haaran nimiä (esim. `fix/typo-module-3`, `add/python-example`)
3. **Tee muutokset**: Muokkaa vain englanninkielisiä markdown-tiedostoja (ei käännöksiä)
4. **Testaa paikallisesti**: Varmista, että markdown renderöityy oikein
5. **Lähetä PR**: Käytä selkeitä PR-otsikoita ja kuvauksia
6. **CLA**: Allekirjoita Microsoft Contributor License Agreement pyydettäessä

### PR-otsikon muoto

Käytä selkeitä, kuvailevia otsikoita:
- `[Module XX] Lyhyt kuvaus` moduulikohtaisille muutoksille
- `[Samples] Kuvaus` esimerkkikoodimuutoksille
- `[Docs] Kuvaus` yleisille dokumentaatiopäivityksille

### Mitä voi tehdä

- Dokumentaation tai koodiesimerkkien virheiden korjaukset
- Uudet koodiesimerkit lisäkielillä
- Selvennykset ja parannukset olemassa olevaan sisältöön
- Uudet tapaustutkimukset tai käytännön esimerkit
- Epäselvän tai virheellisen sisällön ongelmaraportit

### Mitä EI saa tehdä

- Älä muokkaa suoraan tiedostoja `translations/`-hakemistossa
- Älä muokkaa `translated_images/`-hakemistoa
- Älä lisää suuria binääritiedostoja ilman keskustelua
- Älä muuta käännöstyönkulun tiedostoja ilman koordinointia

## Lisähuomautukset

### Arkiston ylläpito

- **Muutosloki**: Kaikki merkittävät muutokset dokumentoidaan `changelog.md`-tiedostossa
- **Opas**: Käytä `study_guide.md`-tiedostoa kurssin navigointiin
- **Ongelmapohjat**: Käytä GitHubin ongelmapohjia virheraportteihin ja ominaisuuspyyntöihin
- **Toimintaohjeet**: Kaikkien osallistujien on noudatettava Microsoftin avoimen lähdekoodin toimintaohjeita

### Oppimispolku

Noudata moduuleja järjestyksessä (00-11) optimaalisen oppimisen saavuttamiseksi:
1. **00-02**: Perusteet (Johdanto, ydinkonseptit, turvallisuus)
2. **03**: Käytännön toteutus
3. **04-05**: Käytännön toteutus ja edistyneet aiheet
4. **06-10**: Yhteisö, parhaat käytännöt ja tosielämän sovellukset
5. **11**: Kattavat tietokantaintegraatioharjoitukset (13 peräkkäistä harjoitusta)

### Tukiresurssit

- **Dokumentaatio**: https://modelcontextprotocol.io/
- **Määrittely**: https://spec.modelcontextprotocol.io/
- **Yhteisö**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-palvelin
- **Liittyvät kurssit**: Katso README.md Microsoftin muut oppimispolut

### Yleiset ongelmatilanteet

**K: PR:ni epäonnistuu käännöstarkistuksessa**
V: Varmista, että muokkasit vain englanninkielisiä markdown-tiedostoja päämoduulihakemistoissa, et käännettyjä versioita.

**K: Kuinka lisään uuden kielen?**
V: Kielen tuki hallitaan co-op-translator-työnkulun kautta. Avaa ongelma keskustellaksesi uuden kielen lisäämisestä.

**K: Koodiesimerkit eivät toimi**
V: Varmista, että olet noudattanut esimerkin README-tiedoston asennusohjeita. Tarkista, että sinulla on oikeat versiot riippuvuuksista asennettuna.

**K: Kuvat eivät näy**
V: Varmista, että kuvapolut ovat suhteellisia ja käyttävät etuviivoja. Kuvien tulisi olla `images/`-hakemistossa tai `translated_images/`-hakemistossa paikallisille versioille.

### Suorituskykyhuomioita

- Käännöstyönkulku voi kestää useita minuutteja
- Suuret kuvat tulisi optimoida ennen sitouttamista
- Pidä yksittäiset markdown-tiedostot keskittyneinä ja kohtuullisen kokoisina
- Käytä suhteellisia linkkejä paremman siirrettävyyden vuoksi

### Projektin hallinta

Tämä projekti noudattaa Microsoftin avoimen lähdekoodin käytäntöjä:
- MIT-lisenssi koodille ja dokumentaatiolle
- Microsoftin avoimen lähdekoodin toimintaohjeet
- CLA vaaditaan osallistumiseen
- Turvallisuuskysymykset: Noudata SECURITY.md-ohjeita
- Tuki: Katso SUPPORT.md apuresursseja varten

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.