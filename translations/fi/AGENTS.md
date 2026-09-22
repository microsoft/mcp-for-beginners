# AGENTS.md

## Projektin yleiskatsaus

**MCP aloittelijoille** on avoimen lähdekoodin opetussuunnitelma Model Context Protocolin (MCP) oppimiseen - standardoitu kehys tekoälymallien ja asiakasohjelmien välisille vuorovaikutuksille. Tämä arkisto tarjoaa kattavia oppimateriaaleja käytännön koodiesimerkkien kera useilla ohjelmointikielillä.

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
- **Dokumentaatio**: Markdown automatisoidulla monikielisellä käännöksellä (yli 48 kieltä)

### Arkkitehtuuri

- **11 ydintä modulit (00-11)**: Järjestelmällinen oppimispolku perusteista edistyneisiin aiheisiin
- **Käytännön labrat**: Käytännön harjoituksia täydellisillä ratkaisukodeilla useilla kielillä
- **Esimerkkiprojektit**: Toimivia MCP-palvelin- ja asiakasratkaisuja
- **Käännösjärjestelmä**: Automaattinen GitHub Actions -työnkulku monikielisen tuen aikaansaamiseksi
- **Kuvavarastot**: Keskitetty kuvahakemisto käännetyllä versiolla

## Asennuskomennot

Tämä on dokumentaatioon keskittyvä arkisto. Suurin osa asennuksesta tapahtuu yksittäisissä esimerkkiprojekteissa ja labroissa.

### Arkiston asentaminen

```bash
# Kloonaa arkisto
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Työskentely esimerkkiprojektien kanssa

Esimerkkiprojektit sijaitsevat:
- `03-GettingStarted/samples/` - Kielikohtaisia esimerkkejä
- `03-GettingStarted/01-first-server/solution/` - Ensimmäiset palvelinratkaisut
- `03-GettingStarted/02-client/solution/` - Asiakasratkaisut
- `11-MCPServerHandsOnLabs/` - Kattavat tietokantaintegraatiolabraharjoitukset

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
# tai
pip install -e .
python main.py
```

#### Java-projektit
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Kehitysprosessi

### MCP 7-28 valmius

#### Arkiston valmiuslistaus

- [x] **Uuden kontribuuttorin selkeys**: Tämä tiedosto määrittelee arkiston tarkoituksen,
  rakenteen, kontribuutiomääräykset ja esimerkkiasetusten polut.
- [x] **Rakennus/testaus/lint-komennot tarkkoine liputuksineen**:
  - Arkiston dokumentaation linttaus:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Arkiston dokumentaatiolinkkien mallin tarkastus:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript-esimerkin validointi:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python-esimerkin validointi:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java-esimerkin validointi:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`

- [x] **Yksi realistinen työnkulku, joka voi toimia MCP-työkaluna**:
  `validate_curriculum_change`
- [x] **Syötteet/tulosteet ovat eksplisiittisiä** (katso alla oleva määrittely).
- [x] **Oikeudet ja vikatilat on dokumentoitu** (katso alla oleva määrittely).
- [x] **CI-testattavuus on eksplisiittistä** (deterministiset komennot, eksplisiittiset
  lopetuskoodit ja koneellisesti luettavat tulosteet).

#### Ehdokas MCP-työnkulku: `validate_curriculum_change`

##### Tavoite

Varmistaa opetussuunnitelmadokumentaation muutosten ja edustavan esimerkkikoodin
kunnollisuus ennen yhdistämistä.

##### Syötteet

- `changed_paths: string[]` (vaadittu) - PR:ssä muuttuneet suhteelliset polut.
- `run_docs_lint: boolean` (oletus `true`)
- `run_links_audit: boolean` (oletus `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (oletus kaikki `false`)

##### Tulosteet

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Oikeudet

- Lukee työtilan tiedostoja ja kirjoittaa työkalun generoimia artefakteja (esim. lint
  raportteja, testilokeja) vain; ei kirjoita `translations/` tai
  `translated_images/`.
- Suorittaa paikallisia shell-komentoja.
- Valinnainen verkkoyhteys vain pakettien palauttamiseen (`npm ci`,
  `python -m pip install`, `mvn` riippuvuuksien ratkaisussa).
- Ei oikeutta pushata, yhdistää tai muokata `translations/` tai
  `translated_images/`.

##### Vikatilat

- `E_NO_INPUT_PATHS`: `changed_paths` tyhjä.
- `E_INVALID_PATH`: syötepolku karkaa repositorion juuresta.
- `E_LINT_FAILED`: markdown lint palauttaa nollasta poikkeavan koodin.
- `E_LINK_AUDIT_FAILED`: linkkikatselmointikomento palauttaa nollasta poikkeavan koodin.
- `E_SAMPLE_TEST_FAILED`: esimerkkitesti/kokoaminen palauttaa nollasta poikkeavan koodin.
- `E_TIMEOUT`: komento ylitti asetetun aikakatkaisun.

##### Suositeltu CI-sopimus

Automaattisen varmistuksen mahdollistamiseksi konfiguroi CI-tehtävä, joka:

- Laukaisee pull requesteissa, jotka koskettavat `*.md`-tiedostoja, esimerkkikoodia tai tätä tiedostoa.
- Suorittaa yllä luetellut tarkat komennot.
- Tallentaa lokit artefakteiksi.
- Epäonnistuu, jos jokin lopetuskoodi on nollasta poikkeava.

#### Jos toimitat MCP-palvelimen tästä repositoriosta

- [ ] Lue lopullinen MCP `2026-07-28` muutospäiväkirja:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Varmista, että valittu SDK-versio tukee MCP:tä `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Poista istunto- ja kättelyoletukset; käsittele jokainen pyyntö
  itsenäisenä:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Lähetä `Mcp-Method` ja `Mcp-Name` otsikot raakoihin HTTP-pyyntöihin:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Tarkasta kovakoodatut virhekoodit (`missing resource` siirtyi arvosta `-32002` arvoon `-32602`).

- [ ] Siirrä käytöstä poistetut Roots-, Sampling-, Logging- ja Dynamic Client
  Rekisteröinti:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Siirry pois kokeellisesta `2025-11-25` Tasks API:sta:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Tarkista OAuth- ja OpenID Connect -vahvistusten valtuutus:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentaation rakenne

- **Moduulit 00-11**: Perusopetuksen sisältö peräkkäisessä järjestyksessä
- **translations/**: Kieli- ja aluekohtaiset versiot (automaattisesti luotuja, ei muokattava suoraan)
- **translated_images/**: Paikallistetut kuvat (automaattisesti luotuja)
- **images/**: Lähdekuvat ja kaaviot

### Dokumentaation muutosten tekeminen

1. Muokkaa vain englanninkielisiä markdown-tiedostoja juurimoduulien kansioissa (00-11)
2. Päivitä kuvat tarvittaessa `images/` -kansiossa
3. co-op-translator GitHub Action luo käännökset automaattisesti
4. Käännökset päivitetään automaattisesti työnnettäessä päähaaraan

### Kääntämisen työskentely

- **Automaattinen kääntäminen**: GitHub Actions -työnkulku käsittelee kaikki käännökset
- ÄLÄ muokkaa manuaalisesti tiedostoja `translations/`-kansiossa
- Käännöksen metatiedot ovat upotettuina jokaiseen käännettyyn tiedostoon
- Tuetut kielet: yli 48 kieltä, mukaan lukien arabia, kiina, ranska, saksa, hindi, japani, korea, portugali, venäjä, espanja ja monet muut

## Testiohjeet

### Dokumentaation validointi

Koska kyseessä on pääasiassa dokumentaatiovarasto, testaus keskittyy:

1. **Linkkikaavion tarkistus**: Listaa Markdown-linkit tarkastelua varten

   ```bash
   # Listaa Markdown-linkit (kaaviotarkastus)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Koodiesimerkkien validointi**: Testaa, että koodiesimerkit kääntyvät/ajautuvat

   ```bash
   # Siirry tiettyyn näytteeseen ja suorita sen testit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdownin linttaus**: Tarkista muotoilun johdonmukaisuus

   ```bash
   # Käytä tarvittaessa markdownlintiä
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Esimerkkiprojektin testaus

Jokaisella kielikohtaisella esimerkillä on oma testausmenetelmänsä:

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
- Sisällytä koodiesimerkkejä useilla kielillä tarvittaessa
- Noudata markdownin parhaita käytäntöjä:
  - Käytä ATX-tyylisiä otsikoita (`#`-syntaksi)
  - Käytä aidattuja koodilohkoja kielitunnistein
  - Lisää kuville kuvaava alt-teksti
  - Pidä rivipituudet järkevissä rajoissa (ei tiukkaa rajaa, mutta harkitse asioita)

### Koodiesimerkin tyyli

#### TypeScript/JavaScript
- Käytä ES-moduuleja (`import`/`export`)
- Noudata TypeScriptin tiukkoja tiloja
- Lisää tyyppimerkinnät
- Kohdista ES2022:een

#### Python
- Noudata PEP 8 -tyyliohjeita
- Käytä tyyppivihjeitä tarpeen mukaan
- Sisällytä docstringit funktioille ja luokille
- Käytä moderneja Python-ominaisuuksia (3.8+)

#### Java
- Noudata Spring Boot -käytäntöjä
- Käytä Java 21 -ominaisuuksia
- Noudata tavallista Maven-projektirakennetta
- Sisällytä Javadoc-kommentteja

### Tiedostojen järjestely

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

## Kokoaminen ja käyttöönotto

### Dokumentaation käyttöönotto

Varasto käyttää GitHub Pagesia tai vastaavaa dokumentaation isännöintiin (jos sovellettavissa). Muutokset päähaarassa käynnistävät:

1. Käännöstyönkulun (`.github/workflows/co-op-translator.yml`)
2. Automaattinen kaikkien englanninkielisten markdown-tiedostojen käännös
3. Kuvien paikallistaminen tarpeen mukaan

### Rakentamisprosessia ei vaadita

Tämä varasto sisältää pääasiassa markdown-dokumentaatiota. Perusopetuksen sisältöä varten ei tarvita käännös- tai rakennusvaihetta.

### Esimerkkiprojektin käyttöönotto

Yksittäisillä esimerkkiprojekteilla voi olla omat käyttöönotto-ohjeensa:
- Katso `03-GettingStarted/09-deployment/` MCP-palvelimen käyttöönotto-oppaaksi
- Azure Container Apps -käyttöönottiesimerkkejä `11-MCPServerHandsOnLabs/`-kansiossa

## Osallistumisohjeet

### Pull request -prosessi

1. **Forkkaa ja kloonaa**: Forkkaa varasto ja kloonaa oma fork paikallisesti
2. **Luo haara**: Käytä kuvaavia haaranimiä (esim. `fix/typo-module-3`, `add/python-example`)
3. **Tee muutokset**: Muokkaa vain englanninkielisiä markdown-tiedostoja (ei käännöksiä)
4. **Testaa paikallisesti**: Varmista, että markdown näkyy oikein
5. **Lähetä PR**: Käytä selkeitä PR-otsikoita ja kuvauksia
6. **CLA**: Allekirjoita Microsoft Contributor License Agreement pyydettäessä

### PR-otsikon muoto

Käytä selkeitä, kuvaavia otsikoita:
- `[Module XX] Lyhyt kuvaus` moduulikohtaisista muutoksista
- `[Samples] Kuvaus` esimerkkikoodimuutoksista
- `[Docs] Kuvaus` yleisistä dokumentaatiopäivityksistä

### Mitä osallistua

- Virheenkorjaukset dokumentaatiossa tai koodiesimerkeissä
- Uudet koodiesimerkit lisäkielillä
- Selvennykset ja parannukset olemassa olevaan sisältöön
- Uudet tapaustutkimukset tai käytännön esimerkit
- Virheraportit epäselvästä tai virheellisestä sisällöstä

### Mitä EI saa tehdä

- Älä muokkaa suoraan tiedostoja `translations/`-kansiossa
- Älä muokkaa `translated_images/`-kansiota
- Älä lisää suuria binääritiedostoja ilman keskustelua
- Älä muuta käännöstyönkulun tiedostoja ilman koordinointia

## Lisähuomiot

### Varaston ylläpito

- **Muutosloki**: Kaikki merkittävät muutokset dokumentoidaan `changelog.md`-tiedostossa
- **Opas**: Käytä `study_guide.md` opintopolun yleiskatsauksen avaamiseen
- **Issue-mallit**: Käytä GitHubin issue-malleja virheraportteihin ja ominaisuuspyyntöihin
- **Käyttäytymissäännöt**: Kaikkien osallistujien tulee noudattaa Microsoftin avoimen lähdekoodin käyttäytymissääntöjä

### Oppimispolku

Noudata moduuleja peräkkäisessä järjestyksessä (00-11) parhaan oppimisen saavuttamiseksi:
1. **00-02**: Perusteet (Johdanto, ydinkonseptit, turvallisuus)
2. **03**: Käytännön aloitus
3. **04-05**: Käytännön toteutus ja edistyneet aiheet
4. **06-10**: Yhteisö, parhaat käytännöt ja todelliset sovellukset
5. **11**: Laajat tietokantaintegroitavuuden laboratoriot (13 peräkkäistä laboratoriota)

### Tukiresurssit

- **Dokumentaatio**: https://modelcontextprotocol.io/
- **Määrittely**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Yhteisö**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord -palvelin
- **Aiheeseen liittyvät kurssit**: Katso README.md muista Microsoftin oppimispoluista

### Tavalliset vianetsintäongelmat

**K: PR:ni ei läpäise käännöstarkistusta**
V: Varmista, että muokkasit vain englanninkielisiä markdown-tiedostoja juurimoduulien kansioissa, etkä käännettyjä versioita.

**K: Kuinka lisään uuden kielen?**
V: Kielitukea hallinnoi co-op-translator työnkulku. Avaa issue keskustellaksesi uusien kielten lisäämisestä.

**K: Koodiesimerkit eivät toimi**
V: Varmista, että olet seurannut kunkin esimerkin README-tiedoston asennusohjeita. Tarkista, että sinulla on oikeat riippuvuusversiot asennettuna.


**K: Kuvat eivät näy**

A: Varmista, että kuvapolut ovat suhteellisia ja käyttävät eteenpäin meneviä kauttaviivoja. Kuvien tulisi olla `images/`-hakemistossa tai `translated_images/`-hakemistossa paikallistetuille versioille.

### Suorituskykyyn liittyvät seikat

- Käännöstyö voi kestää useita minuutteja
- Suurten kuvien optimointi ennen sitomista
- Pidä yksittäiset markdown-tiedostot keskittyneinä ja kohtuullisen kokoisina
- Käytä suhteellisia linkkejä paremman siirrettävyyden vuoksi

### Projektin hallinto

Tämä projekti noudattaa Microsoftin avoimen lähdekoodin käytäntöjä:
- MIT-lisenssi koodille ja dokumentaatiolle
- Microsoftin avoimen lähdekoodin käytösohjeet
- CLA vaaditaan kontribuutioihin
- Turva-asiat: Noudata SECURITY.md-ohjeita
- Tuki: Katso SUPPORT.md saadaksesi apuresursseja

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->