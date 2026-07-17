# AGENTS.md

## Projekto apžvalga

**MCP pradedantiesiems** yra atvirojo kodo mokomasis kursas Modelio konteksto protokolo (MCP) mokymuisi - standartizuota sistema sąveikoms tarp AI modelių ir klientų programėlių. Šis saugykla suteikia išsamias mokymosi medžiagas su praktiniais kodo pavyzdžiais keliose programavimo kalbose.

### Pagrindinės technologijos

- **Programavimo kalbos**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Sistemos ir SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Duomenų bazės**: PostgreSQL su pgvector praplėtimu
- **Debesų platformos**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Konstravimo įrankiai**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown su automatizuotu daugiakalbiu vertimu (daugiau nei 48 kalbomis)

### Architektūra

- **11 pagrindinių modulių (00-11)**: Nuosekli mokymosi seka nuo pagrindų iki pažangių temų
- **Praktinės laboratorijos**: Praktiniai užsiėmimai su pilnu sprendimų kodu keliose kalbose
- **Pavyzdiniai projektai**: Veikiantys MCP serverio ir kliento įgyvendinimai
- **Vertimo sistema**: Automatizuotas GitHub Actions darbo eigas daugiakalbei palaikymui
- **Vaizdo ištekliai**: Centralizuota vaizdų katalogas su išverstomis versijomis

## Diegimo komandos

Tai yra dokumentacijai skirta saugykla. Dauguma diegimo vyksta atskiruose pavyzdiniuose projektuose ir laboratorijose.

### Saugyklos diegimas

```bash
# Nuklonuokite saugyklą
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Darbas su pavyzdiniais projektais

Pavyzdiniai projektai yra šiose vietose:
- `03-GettingStarted/samples/` - Kalbai specifiniai pavyzdžiai
- `03-GettingStarted/01-first-server/solution/` - Pirmieji serverio įgyvendinimai
- `03-GettingStarted/02-client/solution/` - Klientų įgyvendinimai
- `11-MCPServerHandsOnLabs/` - Išsamios duomenų bazės integravimo laboratorijos

Kiekvienas pavyzdinis projektas turi savas diegimo instrukcijas:

#### TypeScript/JavaScript projektai
```bash
cd <project-directory>
npm install
npm start
```

#### Python projektai
```bash
cd <project-directory>
pip install -r requirements.txt
# arba
pip install -e .
python main.py
```

#### Java projektai
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Vystymo darbo eiga

### MCP 7-28 parengtis

#### Saugyklos parengiamasis kontrolinis sąrašas

- [x] **Naujo dalyvio aiškumas**: Šis failas apibrėžia saugyklos paskirtį,
  struktūrą, kontributavimo taisykles ir pavyzdinių nustatymų kelius.
- [x] **Konstravimo/testavimo/lint komandų su tiksliomis vėliavomis**:
  - Saugyklos dokumentų lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Saugyklos dokumentų nuorodų modelio patikra:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript pavyzdžio patikra:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python pavyzdžio patikra:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java pavyzdžio patikra:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Vienas realistiškas darbo srautas, kuris gali tapti MCP įrankiu**:
  `validate_curriculum_change`
- [x] **Įėjimai/išėjimai yra aiškūs** (žr. žemiau specifikaciją).
- [x] **Leidimai ir klaidų režimai yra dokumentuoti** (žr. žemiau specifikaciją).
- [x] **CI testavimas yra aiškus** (deterministiniai komandų paleidimai, aiškios
  išeigos kodai ir mašinai skaitomi rezultatai).

#### MCP įrankio kandidato darbo eiga: `validate_curriculum_change`

##### Tikslas

Patikrinti mokymo programos dokumentacijos pakeitimų ir reprezentatyvaus pavyzdinio kodo
būklę prieš sujungimą.

##### Įėjimai

- `changed_paths: string[]` (privaloma) - PR pakeisti santykiniai keliai.
- `run_docs_lint: boolean` (numatytasis `true`)
- `run_links_audit: boolean` (numatytasis `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (numatytasis visi `false`)

##### Išeigos

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Leidimai

- Gali skaityti darbo srities failus ir rašyti įrankio sugeneruotus artefaktus (pvz., lint
  ataskaitas, testų žurnalus) tik; negali rašyti į `translations/` ar
  `translated_images/`.
- Gali vykdyti vietines apvalkalo komandas.
- Tinklo prieiga leidžiama tik paketų atkūrimui (`npm ci`,
  `python -m pip install`, `mvn` priklausomybių išsprendimui).
- Nėra leidimo siųsti, sujungti ar keisti `translations/` ar
  `translated_images/`.

##### Klaidos režimai

- `E_NO_INPUT_PATHS`: `changed_paths` yra tuščias.
- `E_INVALID_PATH`: įėjimo kelias išeina už saugyklos šaknies.
- `E_LINT_FAILED`: markdown lint baigiasi su klaida.
- `E_LINK_AUDIT_FAILED`: nuorodų tikrinimo komanda baigiasi su klaida.
- `E_SAMPLE_TEST_FAILED`: pavyzdinio testo/kompiliavimo komanda baigiasi su klaida.
- `E_TIMEOUT`: komanda viršijo nustatytą laukimo laiką.

##### Rekomenduojamas CI susitarimas

Automatizuotam patikrinimui sukurkite CI darbą, kuris:

- Aktyvuojasi PR, kuriuose keičiasi `*.md`, pavyzdinis kodas ar šis failas.
- Atlieka tiksliai aukščiau išvardintas komandas.
- Išsaugo žurnalus kaip artefaktus.
- Jei bet kuri komanda baigiasi klaida, darbas nesėkmingas.

#### Jei išleidžiate MCP serverį iš šios saugyklos

- [ ] Perskaitykite peržiūros keitinių žurnalą MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Paleiskite savo serverį su SDK beta versijomis:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Pašalinkite sesijų ir rankos paspaudimo prielaidas; traktuokite kiekvieną užklausą kaip
  savarankišką:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Siųskite `Mcp-Method` ir `Mcp-Name` antraštes žaliems HTTP užklausoms:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Peržiūrėkite kietai užkoduotus klaidų kodus (`missing resource` perkeltas iš `-32002` į `-32602`).

- [ ] Pažymėti ir suplanuoti migraciją dėl nebenaudojamų root, atrankos ir
  registravimo:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Pereiti nuo eksperimentinės `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Peržiūrėti autorizaciją OAuth ir OpenID Connect sustiprinimui:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentacijos struktūra

- **Moduliai 00-11**: Pagrindinio mokymo turinys nuoseklia tvarka
- **translations/**: Kalbai skirtos versijos (automatizuotos, redaguoti negalima tiesiogiai)
- **translated_images/**: Lokalizuotos paveikslėlių versijos (automatizuotos)
- **images/**: Šaltinio paveikslėliai ir diagramos

### Kaip keisti dokumentaciją

1. Redaguokite tik anglų kalbos markdown failus pagrindiniuose modulio kataloguose (00-11)
2. Jei reikia, atnaujinkite paveikslėlius `images/` kataloge
3. GitHub veiksmas co-op-translator automatiškai sugeneruos vertimus
4. Vertimai atnaujinami kiekvieno pakeitimo pagrindinėje šakoje metu

### Darbas su vertimais

- **Automatinis vertimas**: GitHub Actions tvarko visą vertimų procesą
- **Neredaguokite rankiniu būdu** `translations/` katalogo failų
- Vertimų metaduomenys įterpti kiekviename išverstame faile
- Palaikomos kalbos: daugiau nei 48 kalbos, įskaitant arabų, kinų, prancūzų, vokiečių, hindi, japonų, korėjiečių, portugalų, rusų, ispanų ir daugelį kitų

## Testavimo instrukcijos

### Dokumentacijos patvirtinimas

Kadangi tai daugiausia dokumentacijos saugykla, testavimas koncentruojasi į:

1. **Nuorodų šablono tikrinimą**: Sąrašas Markdown nuorodų peržiūrai

   ```bash
   # Išvardinti Markdown nuorodas (šablono patikrinimas)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kodo pavyzdžių patvirtinimą**: Patikrinkite, ar kodo pavyzdžiai kompiliuojasi / veikia

   ```bash
   # Eiti į konkretų pavyzdį ir paleisti jo testus
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown stiliaus tikrinimą**: Patikrinkite formatavimo nuoseklumą

   ```bash
   # Jei reikia, naudokite markdownlint
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pavyzdinių projektų testavimas

Kiekviena kalbai skirta pavyzdinė programėlė turi savo testavimo metodiką:

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

## Kodo stiliaus gairės

### Dokumentacijos stilius

- Naudokite aiškią, pradedantiesiems draugišką kalbą
- Pavyzdžiuose pateikite kodą keliose kalbose, kur tai taikoma
- Laikykitės markdown geriausių praktikų:
  - Naudokite ATX stiliaus antraštes (`#` sintaksė)
  - Naudokite tvarkingus kodo blokus su kalbos žymomis
  - Paveikslėliams įtraukite aprašomuosius alt tekstus
  - Laikykite eilučių ilgį protingą (nėra griežto limito, bet būkite saikingi)

### Kodo pavyzdžių stilius

#### TypeScript/JavaScript
- Naudokite ES modulius (`import`/`export`)
- Laikykitės TypeScript griežto režimo taisyklių
- Įtraukite tipo anotacijas
- Tikslinė versija ES2022

#### Python
- Laikykitės PEP 8 stiliaus gairių
- Naudokite tipo užuominas, kur tai tinka
- Funkcijoms ir klasėms pridėkite docstring'us
- Naudokite modernias Python funkcijas (3.8+)

#### Java
- Laikykitės Spring Boot konvencijų
- Naudokite Java 21 funkcijas
- Laikykitės įprastinės Maven projekto struktūros
- Pridėkite Javadoc komentarus

### Failų organizavimas

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

## Kūrimas ir diegimas

### Dokumentacijos diegimas

Saugykla naudoja GitHub Pages arba panašią platformą dokumentacijos talpinimui (jei taikoma). Pakeitimai pagrindinėje šakoje sukelia:

1. Vertimų darbo eigą (`.github/workflows/co-op-translator.yml`)
2. Automatizuotą visų anglų kalbos markdown failų vertimą
3. Paveikslėlių lokalizavimą pagal poreikį

### Nereikia kūrimo proceso

Ši saugykla daugiausia talpina markdown dokumentaciją. Nereikalingas sudarymas ar kūrimas pagrindiniam mokymo turiniui.

### Pavyzdinių projektų diegimas

Atskiri pavyzdiniai projektai gali turėti diegimo instrukcijas:
- Pažiūrėkite `03-GettingStarted/09-deployment/`, jei norite gauti MCP serverio diegimo nurodymus
- Pavyzdžiai Azure Container Apps diegimui `11-MCPServerHandsOnLabs/`

## Indėlio gairės

### Pull Request procesas

1. **Fork ir klonavimas**: Padarykite saugyklos fork ir nuklonuokite jį vietoje
2. **Sukurti šaką**: Naudokite aprašomuosius šakų pavadinimus (pvz., `fix/typo-module-3`, `add/python-example`)
3. **Atlikite pakeitimus**: Redaguokite tik anglų kalbos markdown failus (ne vertimus)
4. **Testuokite vietoje**: Patikrinkite, ar markdown tinkamai atvaizduojamas
5. **Pateikite PR**: Naudokite aiškius PR pavadinimus ir aprašymus
6. **CLA**: Pasirašykite Microsoft Bendradarbio Licencijos Sutartį, kai bus paprašyta

### PR pavadinimo formatas

Naudokite aiškius, aprašomuosius pavadinimus:
- `[Module XX] Trumpas aprašymas` modulio pakeitimams
- `[Samples] Aprašymas` pavyzdinio kodo pakeitimams
- `[Docs] Aprašymas` bendriems dokumentacijos atnaujinimams

### Ką įnešti

- Klaidų taisymai dokumentacijoje arba kodo pavyzdžiuose
- Nauji kodo pavyzdžiai papildomomis kalbomis
- Esamo turinio patikslinimai ir patobulinimai
- Naujos bylos studijos ar praktiški pavyzdžiai
- Probleminių vietų ataskaitos dėl neaiškaus ar neteisingo turinio

### Ko nedaryti

- Neredaguokite tiesiogiai failų `translations/` kataloge
- Neredaguokite `translated_images/` katalogo
- Nedėkite didelių dvejetainių failų be aptarimo
- Nekeiskite vertimų darbo eigos failų be koordinavimo

## Papildomi pastabos

### Saugyklos priežiūra

- **Pakeitimų žurnalas**: Visi svarbūs pakeitimai dokumentuoti `changelog.md`
- **Mokymosi vadovas**: Naudokite `study_guide.md` mokymo plano apžvalgai
- **Klaidų šablonai**: Naudokite GitHub problemų šablonus klaidų ataskaitoms ir funkcijų prašymams
- **Elgesio kodeksas**: Visi bendradarbiai turi laikytis Microsoft atvirojo kodo elgesio kodekso

### Mokymosi kelias

Laikykitės moduliais nuoseklia tvarka (00-11) optimaliai mokymuisi:
1. **00-02**: Pagrindai (Įvadas, Pagrindinės sąvokos, Saugumas)
2. **03**: Pradžia su praktiniu pritaikymu
3. **04-05**: Praktinis įgyvendinimas ir pažangios temos
4. **06-10**: Bendruomenė, geriausios praktikos, realaus pasaulio taikymai
5. **11**: Išsamūs duomenų bazės integravimo laboratoriniai darbai (13 nuoseklių laboratorijų)

### Palaikymo ištekliai

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Bendruomenė**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord serveris
- **Susiję kursai**: Žr. README.md dėl kitų Microsoft mokymosi kelių

### Dažniausiai pasitaikančios problemos

**K: Mano PR nepraeina vertimo patikros**
A: Įsitikinkite, kad redagavote tik anglų kalbos markdown failus pagrindiniuose modulio kataloguose, ne išverstinius variantus.

**K: Kaip pridėti naują kalbą?**
A: Kalbų palaikymas valdomas naudojant co-op-translator darbo eigą. Atsidarykite problemą aptarti naujų kalbų pridėjimą.

**K: Kodo pavyzdžiai neveikia**

A: Įsitikinkite, kad sekėte nustatymo instrukcijas konkretaus pavyzdžio README faile. Patikrinkite, ar įdiegėte tinkamas priklausomybių versijas.

**Klausimas: Paveikslėliai nerodomi**
A: Patikrinkite, ar paveikslėlių keliai yra santykiniai ir naudoja pasvirusiuosius brūkšnelius. Paveikslėliai turėtų būti `images/` kataloge arba `translated_images/` lokalizuotoms versijoms.

### Veikimo efektyvumo svarstymai

- Vertimo procesas gali trukti keletą minučių
- Dideli paveikslėliai turėtų būti optimizuoti prieš įsipareigojant
- Laikykite atskirus markdown failus susitelkusius ir vidutinio dydžio
- Naudokite santykinius nuorodas geresniam perkeliamumui

### Projekto valdymas

Šis projektas laikosi Microsoft atviro kodo praktikų:
- MIT licencija kodui ir dokumentacijai
- Microsoft atviro kodo elgesio kodeksas
- CLA reikalaujama prisidėjimams
- Saugumo klausimai: laikykitės SECURITY.md gairių
- Pagalba: žr. SUPPORT.md pagalbos išteklius

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->