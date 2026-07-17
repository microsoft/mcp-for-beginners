# AGENTS.md

## Projektin yleiskatsaus

**MCP aloittelijoille** on avoimen lähdekoodin opetussuunnitelma Model Context Protocolin (MCP) oppimiseen - standardoitu kehys tekoälymallien ja asiakassovellusten välisille vuorovaikutuksille. Tämä repositorio tarjoaa kattavat oppimateriaalit käytännön koodiesimerkkien kera useilla ohjelmointikielillä.

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
- **Dokumentaatio**: Markdown automaattisella monikielisellä käännöksellä (yli 48 kieltä)

### Arkkitehtuuri

- **11 ydintä modulit (00-11)**: Järjestelmällinen oppimispolku perusasioista edistyneisiin aiheisiin
- **Käytännön labrat**: Käytännön harjoitukset täydellisillä ratkaisukoodiesimerkeillä useilla kielillä
- **Esimerkkiprojektit**: Toimivat MCP-palvelin- ja asiakasimplementaatiot
- **Käännösjärjestelmä**: Automaattinen GitHub Actions -työnkulku monikielisyyden tukemiseksi
- **Kuvavarastot**: Keskitetty kuvahakemisto käännetyillä versioilla

## Asennuskomennot

Tämä on dokumentaatiopainotteinen repositorio. Suurin osa asennuksista tapahtuu yksittäisissä esimerkkiprojekteissa ja labroissa.

### Repulikannan käyttöönotto

```bash
# Kloonaa arkisto
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Työskentely esimerkkiprojektien kanssa

Esimerkkiprojektit sijaitsevat kansioissa:
- `03-GettingStarted/samples/` - Kielikohtaiset esimerkit
- `03-GettingStarted/01-first-server/solution/` - Ensimmäiset palvelinimplementaatiot
- `03-GettingStarted/02-client/solution/` - Asiakasimplementaatiot
- `11-MCPServerHandsOnLabs/` - Kattavat tietokantaintegraatiolabratoorat

Jokaisella esimerkkiprojektilla on omat asennusohjeensa:

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

#### Repon valmiuslista

- [x] **Uuden kontribuuttorin selkeys**: Tämä tiedosto määrittelee repokannan tarkoituksen,
  rakenteen, kontribuutiotavat ja esimerkkien asennuspolut.
- [x] **Rakennus/testaus/lint-komennot täsmällisillä lipuilla**:
  - Repodokumentaation lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Repon dokumentaation linkkikaavion tarkastus:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript-esimerkin validointi:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python-esimerkin validointi:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java-esimerkin validointi:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Yksi realistinen työnkulku, joka voi muodostaa MCP-työkalun**:
  `validate_curriculum_change`
- [x] **Syötteet/tuotokset ovat eksplisiittisiä** (ks. alla oleva spesifikaatio).
- [x] **Oikeudet ja epäonnistumistavat dokumentoitu** (ks. alla oleva spesifikaatio).
- [x] **CI-testattavuus eksplisiittinen** (deterministiset komennot, eksplisiittiset
  poistu-koodit ja koneellisesti luettavat tuotokset).

#### Ehdokas MCP-työnkulku: `validate_curriculum_change`

##### Tavoite

Tarkistaa opetussuunnitelman dokumentaatiomuutokset ja edustavien esimerkkikoodien
kunto ennen yhdistämistä.

##### Syötteet

- `changed_paths: string[]` (pakollinen) - PR:ssä muuttuneet suhteelliset polut.
- `run_docs_lint: boolean` (oletus `true`)
- `run_links_audit: boolean` (oletus `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (oletus kaikki `false`)

##### Tuotokset

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Oikeudet

- Lukee työtilan tiedostoja ja kirjoittaa työkaluilla tuotettuja artefakteja (esim. lint-
  raportit, testilokit) ainoastaan; ei kirjoituksia `translations/` tai
  `translated_images/` kansioihin.
- Suorittaa paikallisia shell-komentoja.
- Valinnainen verkko-yhteys ainoastaan pakettien palautukseen (`npm ci`,
  `python -m pip install`, `mvn` riippuvuuksien ratkaisu).
- Ei oikeutta puskea, yhdistää tai muokata `translations/` tai
  `translated_images/`.

##### Epäonnistumistavat

- `E_NO_INPUT_PATHS`: `changed_paths` tyhjä.
- `E_INVALID_PATH`: syötepolku karkaa repokannan juurihakemistosta.
- `E_LINT_FAILED`: markdown-lint epäonnistuu ei-nolla poistu-koodilla.
- `E_LINK_AUDIT_FAILED`: linkkikaavion tarkastuskomento epäonnistuu ei-nolla poistu-koodilla.
- `E_SAMPLE_TEST_FAILED`: esimerkkien testaus/rakennus epäonnistuu ei-nolla poistu-koodilla.
- `E_TIMEOUT`: komento ylitti määritellyn aikakatkaisun.

##### Suositeltu CI-sopimus

Automaattiseen tarkastukseen määritetään CI-tehtävä, joka:

- Käynnistyy pull requestien yhteydessä, jotka muuttavat `*.md` tiedostoja, esimerkkikoodia tai tätä tiedostoa.
- Suorittaa yllä listatut täsmälliset komennot.
- Tallentaa lokit artefakteiksi.
- Epäonnistuu, jos mikään komento palauttaa ei-nolla koodin.

#### Jos toimitat MCP-palvelimen tästä reposta

- [ ] Lue MCP 7-28 luonnosmuutokset:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Testaa palvelimesi SDK-beetoja vastaan:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Poista istunto- ja kädenpuristusolettamukset; käsittele jokaista pyyntöä
  itse sisältävinä:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Lähetä `Mcp-Method` ja `Mcp-Name` otsikot raakoihin HTTP-pyyntöihin:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Tarkasta kovakoodatut virhekoodit (`missing resource` siirtyi `-32002`:sta `-32602`:een).

- [ ] Merkitse ja suunnittele siirtymää vanhentuneille juuri-kohteille, otoksille ja
  lokitukselle:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Siirry pois kokeellisesta `2025-11-25` Tasks API:sta:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Tarkista OAuth- ja OpenID Connect -valtuutukset tiukentamista varten:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentaation rakenne

- **Moduulit 00-11**: Ydinopetussisällöt järjestyksessä
- **translations/**: Kielikohtaiset versiot (automaattisesti luotu, älä muokkaa suoraan)
- **translated_images/**: Lokalisoidut kuvaversiot (automaattisesti luotu)
- **images/**: Lähdekuvat ja kaaviot

### Dokumentaation muutosten tekeminen

1. Muokkaa vain englanninkielisiä markdown-tiedostoja juurimoduulihakemistoissa (00-11)
2. Päivitä kuvat `images/`-hakemistossa tarvittaessa
3. co-op-translator GitHub-toiminto luo käännökset automaattisesti
4. Käännökset luodaan uudelleen kun työstö työnnetään päähaarassa

### Työskentely käännösten kanssa

- **Automaattinen käännös**: GitHub Actions -työnkulku hoitaa kaikki käännökset
- **ÄLÄ** muokkaa manuaalisesti `translations/`-hakemiston tiedostoja
- Käännösten metatiedot on upotettu jokaiselle käännetylle tiedostolle
- Tuetut kielet: yli 48 kieltä, mukaan lukien arabia, kiina, ranska, saksa, hindi, japani, korea, portugali, venäjä, espanja ja moni muu

## Testausohjeet

### Dokumentaation validointi

Koska kyseessä on pääasiassa dokumentaatiovarasto, testaus keskittyy:

1. **Linkkikaavion tarkastus**: Listaa Markdown-linkit tarkistusta varten

   ```bash
   # Listaa Markdown-linkit (kuvion tarkastus)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Koodiesimerkkien validointi**: Testaa, että koodiesimerkit kääntyvät/ajautuvat

   ```bash
   # Siirry tiettyyn näytteeseen ja suorita sen testit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdownin tyylintarkastus**: Tarkista muotoilun yhdenmukaisuus

   ```bash
   # Käytä markdownlint:iä tarvittaessa
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
- Sisällytä koodiesimerkkejä useilla kielillä, jos mahdollista
- Noudata markdownin parhaita käytäntöjä:
  - Käytä ATX-tyylisiä otsikoita (`#` syntaksi)
  - Käytä aidattuja koodilohkoja, joissa on kielitunnisteet
  - Sisällytä kuvien kuvaileva vaihtoehtoinen teksti
  - Pidä rivit kohtuullisen pituisina (ei tiukkaa rajaa, mutta ole järkevä)

### Koodiesimerkkien tyyli

#### TypeScript/JavaScript
- Käytä ES-moduuleja (`import`/`export`)
- Noudata TypeScriptin tiukkoja tiloja koskevia sääntöjä
- Lisää tyyppimääritykset
- Kohdista ES2022:een

#### Python
- Noudata PEP 8 -tyyliohjeita
- Käytä tyyppivihjeitä tarpeen mukaan
- Sisällytä funktioiden ja luokkien docstringit
- Käytä moderneja Python-ominaisuuksia (3.8+)

#### Java
- Noudata Spring Bootin käytäntöjä
- Käytä Java 21 -ominaisuuksia
- Noudata vakiintunutta Maven-projektirakennetta
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

## Kokoaminen ja käyttöönotto

### Dokumentaation käyttöönotto

Varasto käyttää GitHub Pagesia tai vastaavaa dokumentaation isännöintiin (jos sovellettavissa). Päähaaran muutokset käynnistävät:

1. Käännöstyönkulun (`.github/workflows/co-op-translator.yml`)
2. Kaikkien englanninkielisten markdown-tiedostojen automaattinen käännös
3. Kuvien lokalisaatio tarpeen mukaan

### Ei tarvitse kokoamisprosessia

Tämä varasto sisältää pääosin markdown-dokumentaatiota. Ydinopetussisällön kokoamista tai käännöstä ei tarvita.

### Esimerkkiprojektin käyttöönotto

Yksittäisillä esimerkkiprojekteilla voi olla käyttöönotto-ohjeet:
- Katso `03-GettingStarted/09-deployment/` MCP-palvelimen käyttöönoton ohjeita
- Azure Container Apps -käyttöönoton esimerkkejä hakemistossa `11-MCPServerHandsOnLabs/`

## Osallistumisohjeet

### Pull request -prosessi

1. **Forkkaa ja kloonaa**: Tee fork ja kloonaa se paikallisesti
2. **Luo haarukka**: Käytä kuvaavia haarukkanimetä (esim. `fix/typo-module-3`, `add/python-example`)
3. **Tee muutokset**: Muokkaa vain englanninkielisiä markdown-tiedostoja (ei käännöksiä)
4. **Testaa paikallisesti**: Varmista, että markdown renderöityy oikein
5. **Lähetä PR**: Käytä selkeitä PR-otsikoita ja kuvauksia
6. **CLA**: Hyväksy Microsoft Contributor License Agreement kun pyydetään

### PR-otsikon muoto

Käytä selkeitä, kuvaavia otsikoita:
- `[Module XX] Lyhyt kuvaus` moduulikohtaisissa muutoksissa
- `[Samples] Kuvaus` koodiesimerkkimuutoksissa
- `[Docs] Kuvaus` yleisissä dokumentaatiopäivityksissä

### Mitä osallistumisessa voi tehdä

- Virheenkorjaukset dokumentaatiossa tai koodiesimerkeissä
- Uudet koodiesimerkit lisäkielillä
- Selvennykset ja parannukset olemassa olevaan sisältöön
- Uudet tapaustutkimukset tai käytännön esimerkit
- Virheraportit epäselvästä tai virheellisestä sisällöstä

### Mitä ei saa tehdä

- Älä muokkaa suoraan `translations/`-hakemiston tiedostoja
- Älä muokkaa `translated_images/`-hakemistoa
- Älä lisää suuria binääritiedostoja ilman keskustelua
- Älä muuta käännöstyönkulun tiedostoja ilman koordinointia

## Lisätietoja

### Varaston ylläpito

- **Muutosten loki**: Kaikki merkittävät muutokset on dokumentoitu tiedostossa `changelog.md`
- **Opas**: Käytä `study_guide.md` opetussuunnitelman yleiskatsaukseen
- **Ongelmapohjat**: Käytä GitHubin issue-pohjia bugiraportteihin ja ominaisuuspyyntöihin
- **Toimintasäännöt**: Kaikkien osallistujien on noudatettava Microsoftin avoimen lähdekoodin toimintasääntöjä

### Oppimispolku

Seuraa moduuleja järjestyksessä (00-11) parhaan oppimisen saavuttamiseksi:
1. **00-02**: Perusteet (Johdanto, ydinkäsitteet, turvallisuus)
2. **03**: Käytännön alkuun pääseminen
3. **04-05**: Käytännön toteutus ja edistyneet aiheet
4. **06-10**: Yhteisö, parhaat käytännöt ja todelliset sovellukset
5. **11**: Laajat tietokanta-integraatioharjoitukset (13 peräkkäistä labraa)

### Tukiresurssit

- **Dokumentaatio**: https://modelcontextprotocol.io/
- **Määrittely**: https://spec.modelcontextprotocol.io/
- **Yhteisö**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord -palvelin
- **Aiheeseen liittyvät kurssit**: Katso README.md muista Microsoftin oppimispoluista

### Yleisiä ongelmanratkaisuja

**K: PR:ni epäonnistuu käännösten tarkistuksessa**
V: Varmista, että muokkasit vain englanninkielisiä markdown-tiedostoja juurimoduulihakemistoissa, et käännettyjä versioita.

**K: Kuinka lisään uuden kielen?**
V: Kielen tuki hoidetaan co-op-translator-työnkulun kautta. Avaa issue keskustelua varten uusista kielistä.

**K: Koodiesimerkit eivät toimi**

V: Varmista, että olet noudattanut kyseisen esimerkin README-tiedoston asennusohjeita. Tarkista, että sinulla on asennettuna oikeat riippuvuuksien versiot.

**K: Kuvia ei näy**
V: Varmista, että kuva- polut ovat suhteellisia ja käyttävät eteenpäin kallistuvaa vinoviivaa (/). Kuvien tulisi olla `images/`-hakemistossa tai lokalisoiduilla versioilla `translated_images/`-hakemistossa.

### Suorituskykyä koskevia huomioita

- Käännösprosessissa voi kestää useita minuutteja
- Suuret kuvat tulee optimoida ennen lähettämistä
- Pidä yksittäiset markdown-tiedostot fokusoiduin ja kohtuullisen kokoisina
- Käytä suhteellisia linkkejä paremman siirrettävyyden vuoksi

### Projektin hallinto

Tämä projekti noudattaa Microsoftin avoimen lähdekoodin käytäntöjä:
- MIT-lisenssi koodille ja dokumentaatiolle
- Microsoft Open Source Code of Conduct
- CLA vaaditaan kontribuutioihin
- Turvallisuusongelmat: noudata SECURITY.md ohjeita
- Tuki: Katso SUPPORT.md apuresurssit

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->