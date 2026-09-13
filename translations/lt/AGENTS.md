# AGENTS.md

## Projekto apžvalga

**MCP pradedantiesiems** yra atviro kodo mokomasis kursas, skirtas Modelio Konteksto Protokolo (MCP) mokymuisi – standartizuota sistema AI modelių ir klientų programų sąveikai. Ši saugykla pateikia išsamias mokymosi medžiagas su praktiniais kodo pavyzdžiais keliomis programavimo kalbomis.

### Pagrindinės technologijos

- **Programavimo kalbos**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework’ai ir SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Duomenų bazės**: PostgreSQL su pgvector plėtiniu
- **Debesų platformos**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Kūrimo įrankiai**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown su automatizuotu daugiakalbiu vertimu (48+ kalbų)

### Architektūra

- **11 pagrindinių modulių (00-11)**: Sekanti mokymosi eiga nuo pagrindų iki pažangių temų
- **Praktiniai darbai**: Praktinės užduotys su pilnu sprendimo kodu keliomis kalbomis
- **Pavyzdiniai projektai**: Veikiantys MCP serverio ir kliento įgyvendinimai
- **Vertimo sistema**: Automatizuotas GitHub Actions darbo eiga daugiakalbei pagalbai
- **Vaizdų ištekliai**: Centralizuota vaizdų direktorija su išverstomis versijomis

## Įdiegimo komandos

Tai dokumentacijai skirta saugykla. Daugiausia nustatymų atliekama kiekviename atskirame pavyzdiniame projekte ir užduotyse.

### Saugyklos nustatymas

```bash
# Nukopijuokite saugyklą
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Darbas su pavyzdiniais projektais

Pavyzdiniai projektai randami:
- `03-GettingStarted/samples/` - Kalbai būdingi pavyzdžiai
- `03-GettingStarted/01-first-server/solution/` - Pirmojo serverio įgyvendinimai
- `03-GettingStarted/02-client/solution/` - Kliento įgyvendinimai
- `11-MCPServerHandsOnLabs/` - Išsamios duomenų bazės integracijos užduotys

Kiekvienas pavyzdinis projektas turi atskiras įdiegimo instrukcijas:

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

## Kūrimo darbo eiga

### MCP 7-28 pasiruošimas

#### Saugyklos pasiruošimo sąrašas

- [x] **Naujo dalyvio aiškumas**: Šis failas apibrėžia saugyklos paskirtį,
  struktūrą, indėlio taisykles ir pavyzdinius nustatymų kelius.
- [x] **Tikslūs statybos/testavimo/lint komandų parametrai**:
  - Dokumentacijos lint tikrinimas:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Dokumentacijos nuorodų šablonų patikra:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript pavyzdžio validacija:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python pavyzdžio validacija:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java pavyzdžio validacija:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Vienas realistiškas darbo eiga, galinti tapti MCP įrankiu**:
  `validate_curriculum_change`
- [x] **Įvestys/išvestys yra aiškios** (žr. žemiau pateiktą specifikaciją).
- [x] **Leidimai ir klaidų režimai yra dokumentuoti** (žr. žemiau pateiktą specifikaciją).
- [x] **CI testavimas yra aiškus** (deterministinės komandos, aiškūs
  išėjimo kodai ir mašinai skaitomi pranešimai).

#### Kandidato MCP įrankio darbo eiga: `validate_curriculum_change`

##### Tikslas

Patikrinti mokymo programos dokumentacijos pakeitimus ir reprezentatyvų pavyzdinį kodą
prieš sujungiant.

##### Įvestys

- `changed_paths: string[]` (privalomas) - PR pakeisti santykiniai keliai.
- `run_docs_lint: boolean` (numatytasis `true`)
- `run_links_audit: boolean` (numatytasis `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (numatytasis viskas `false`)

##### Išvestys

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Leidimai

- Skaityti darbo srities failus ir rašyti įrankio sugeneruotus artefaktus (pvz., lint
  ataskaitas, testavimo žurnalus) tik; negalima rašyti į `translations/` arba
  `translated_images/`.
- Vykdyti vietines apvalkalo komandas.
- Tinklo prieiga leidžiama tik priklausomybių atkūrimui (`npm ci`,
  `python -m pip install`, `mvn` priklausomybių tvarkymas).
- Nėra leidimo siųsti, sujungti ar keisti `translations/` ar
  `translated_images/`.

##### Klaidų režimai

- `E_NO_INPUT_PATHS`: `changed_paths` tuščias.
- `E_INVALID_PATH`: įvesties kelias išeina už saugyklos šaknies ribų.
- `E_LINT_FAILED`: markdown lint baigėsi klaida.
- `E_LINK_AUDIT_FAILED`: nuorodų patikros komanda baigėsi klaida.
- `E_SAMPLE_TEST_FAILED`: pavyzdžio testas/statyba baigėsi klaida.
- `E_TIMEOUT`: komandai viršytas nustatytas laiko limitas.

##### Rekomenduojamas CI susitarimas

Automatikai patvirtinti reikia konfigūruoti CI darbą, kuris:

- Reaguoja į pull request’us, liečiančius `*.md`, pavyzdinį kodą ar šį failą.
- Vykdo tiksliai aukščiau nurodytas komandas.
- Saugoti žurnalus kaip artefaktus.
- Nubausti darbą, jei bet kuri komandos išėjimo reikšmė nėra nulis.

#### Jei iš šios saugyklos paleidžiate MCP serverį

- [ ] Perskaitykite galutinį MCP „2026-07-28“ keitimų žurnalą:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Patikrinkite, ar pasirinktas SDK leidimas palaiko MCP „2026-07-28“:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Panaikinkite sesijos ir susitarimo prielaidas; traktukite kiekvieną užklausą kaip
  savarankišką:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Siųskite `Mcp-Method` ir `Mcp-Name` antraštes žaliems HTTP užklausoms:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Patikrinkite, ar nėra kietai įrašytų klaidų kodų (`missing resource` perkeltas iš `-32002` į `-32602`).
- [ ] Migravimas nuo pasenusių Roots, Sampling, Logging ir Dinaminio Kliento
  registracijos:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migravimas nuo eksperimentinės `2025-11-25` Užduočių API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Peržiūrėkite įgaliojimus OAuth ir OpenID Connect stiprinimui:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentacijos struktūra

- **Moduliai 00-11**: Pagrindinis mokymo programos turinys sekančia tvarka
- **translations/**: Kalbai būdingos versijos (automatizuotos, redaguoti ne tiesiogiai)
- **translated_images/**: Lokalizuotos vaizdų versijos (automatizuotos)
- **images/**: Šaltinio vaizdai ir schemos

### Dokumentacijos keitimo eiga

1. Redaguokite tik angliškus markdown failus pagrindiniuose modulio aplankuose (00-11)
2. Pagal poreikį atnaujinkite vaizdus `images/` kataloge
3. GitHub Action co-op-translator automatiškai generuos vertimus
4. Vertimai renovuojami iš karto po pakeitimų pagrindiniame šakoje

### Darbas su vertimais

- **Automatinis vertimas**: GitHub Actions darbo eiga tvarko visus vertimus
- **Neredaguokite rankiniu būdu** failų `translations/` direktorijoje
- Vertimo metaduomenys įterpiami į kiekvieną išverstą failą
- Palaikomos kalbos: 48+ kalbos, įskaitant arabų, kinų, prancūzų, vokiečių, hindi, japonų, korėjiečių, portugalų, rusų, ispanų ir daugelį kitų

## Testavimo instrukcijos

### Dokumentacijos patikra

Kadangi tai pagrinde dokumentacijos saugykla, testavimas orientuojamas į:

1. **Nuorodų šablonų patikra**: markdown nuorodų išrašas peržiūrai

   ```bash
   # Išvardinti Markdown nuorodas (šablono patikra)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kodo pavyzdžių validacija**: Patikrinkite, ar kodo pavyzdžiai kompiliuojasi/veikia

   ```bash
   # Eikite į konkretų pavyzdį ir paleiskite jo testus
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown lint tikrinimas**: Formato atitikimo patikra

   ```bash
   # Naudokite markdownlint, jei reikia
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Pavyzdinių projektų testavimas

Kiekvienas kalbai būdingas pavyzdys turi savitą testavimo metodiką:

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

## Kodo stiliaus gaires

### Dokumentacijos stilius

- Naudokite aiškią, pradedantiesiems suprantamą kalbą
- Įtraukite kodo pavyzdžius keliose kalbose, kur taikoma
- Vadovaukitės markdown gerąja praktika:
  - Naudokite ATX stiliaus antraštes (`#` sintaksė)
  - Naudokite aptvertus kodo blokus su kalbų žymomis
  - Pateikite aprašomąjį alt tekstą vaizdams
  - Laikykitės racionalaus eilučių ilgio (nėra griežtos ribos, bet naudokite sveiką protą)

### Kodo pavyzdžių stilius

#### TypeScript/JavaScript
- Naudokite ES modulius (`import`/`export`)
- Vadovaukitės TypeScript griežto režimo konvencijomis
- Įtraukite tipų anotacijas
- Tikslinė aplinka – ES2022

#### Python
- Vadovaukitės PEP 8 stiliaus gairėmis
- Naudokite tipų užuominas, kur tinka
- Pridėkite docstring’us funkcijoms bei klasėms
- Naudokite modernias Python funkcijas (3.8+)

#### Java
- Vadovaukitės Spring Boot konvencijomis
- Naudokite Java 21 funkcijas
- Vadovaukitės standartu Maven projekto struktūrai
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

Saugykla naudoja GitHub Pages arba panašias priemones dokumentacijos talpinimui (jei taikoma). Pakeitimai pagrindiniame šakoje sukelia:

1. Vertimo darbo eigą (`.github/workflows/co-op-translator.yml`)
2. Automatinį visų anglų kalbos markdown failų vertimą
3. Vaizdų lokalizavimą pagal poreikį

### Statybos proceso nereikia

Ši saugykla daugiausia sudaryta iš markdown dokumentacijos. Pagrindiniam mokymo programos turiniui nereikia kompiliavimo ar statybos žingsnio.

### Pavyzdinių projektų diegimas

Kiekvienas pavyzdinis projektas gali turėti diegimo instrukcijų:
- Žr. `03-GettingStarted/09-deployment/` MCP serverio diegimo rekomendacijas
- Azure Container Apps diegimo pavyzdžiai `11-MCPServerHandsOnLabs/`

## Indėlio gairės

### Pull request proceso eiga

1. **Fork’inimas ir klonavimas**: Fork’inkite saugyklą ir klonuokite savo forką vietoje
2. **Šakos kūrimas**: Naudokite aprašomuosius šakų pavadinimus (pvz., `fix/typo-module-3`, `add/python-example`)
3. **Pakeitimų darymas**: Redaguokite tik anglų kalbos markdown failus (ne vertimus)
4. **Vietinis testavimas**: Patikrinkite, jog markdown atvaizduojamas tinkamai
5. **PR pateikimas**: Naudokite aiškius PR pavadinimus ir aprašymus
6. **CLA**: Pasirašykite Microsoft bendradarbio licencijos sutartį, kai bus paprašyta

### PR pavadinimų formatas

Naudokite aiškius ir aprašomuosius pavadinimus:
- `[Modulis XX] Trumpas aprašymas` moduliui būdingiems pakeitimams
- `[Pavyzdžiai] Aprašymas` pavyzdinių kodo pakeitimų atvejais
- `[Dokumentacija] Aprašymas` bendriems dokumentacijos atnaujinimams

### Ką prisidėti

- Dokumentacijos arba pavyzdinių kodo klaidų taisymas
- Nauji kodo pavyzdžiai papildomomis kalbomis
- Esamo turinio paaiškinimai ir patobulinimai
- Naujos atvejų studijos arba praktiniai pavyzdžiai
- Neaiškaus ar neteisingo turinio klaidų pranešimai

### Ko nedaryti

- Neredaguokite tiesiogiai failų `translations/` direktorijoje
- Neredaguokite `translated_images/` direktorijos
- Nerekite didelių dvejetainių failų be aptarimo
- Nekoreguokite vertimo darbo eigos failų be koordinacijos

## Papildomos pastabos

### Saugyklos priežiūra

- **Keitimų žurnalas**: Visos reikšmingos permainos dokumentuojamos `changelog.md`
- **Mokymosi vadovas**: Naudokite `study_guide.md` mokymo programos naršymo apžvalgai
- **Klaidų formos**: Naudokite GitHub problemų šablonus klaidų ataskaitoms bei funkcijų užklausoms
- **Elgesio kodeksas**: Visi bendradarbiai privalo laikytis Microsoft atvirojo kodo elgesio kodekso

### Mokymosi eiga

Vadovaukitės moduliais sekančia tvarka (00-11) optimaliai mokymuisi:
1. **00-02**: Pagrindai (Įvadas, Pagrindinės sąvokos, Saugumas)
2. **03**: Susipažinimas su praktine implementacija
3. **04-05**: Praktinė implementacija ir pažangios temos
4. **06-10**: Bendruomenė, geriausios praktikos ir realaus pasaulio taikymai
5. **11**: Išsamios duomenų bazės integracijos užduotys (13 nuoseklių laboratorinių darbų)

### Pagalbiniai ištekliai

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Bendruomenė**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord serveris
- **Susiję kursai**: Žr. README.md kitoms Microsoft mokymosi programoms

### Dažnos problemos ir sprendimai

**Q: Mano PR nepraleidžia vertimo patikros**
A: Įsitikinkite, kad redagavote tik anglų kalbos markdown failus pagrindiniuose modulio aplankuose, o ne išverstus failus.

**Q: Kaip pridėti naują kalbą?**
A: Kalbų palaikymą valdo co-op-translator darbo eiga. Atsidarykite problemą (issue) kalbų pridėjimo aptarimui.

**Q: Kodo pavyzdžiai neveikia**
A: Įsitikinkite, kad sekėte specifinio pavyzdžio README diegimo instrukcijas. Patikrinkite, ar turite tinkamas priklausomybių versijas.

**Q: Vaizdai nerodomi**

A: Patikrinkite, ar paveikslėlių keliai yra reliatyvūs ir naudoja pasvirusiuosius brūkšnelius. Paveikslėliai turėtų būti kataloge `images/` arba `translated_images/` lokalizuotoms versijoms.

### Veikimo našumo svarstymai

- Vertimo darbo eiga gali užtrukti kelias minutes
- Dideli paveikslėliai turėtų būti optimizuoti prieš įsipareigojant
- Išlaikykite atskirus markdown failus sutelktus ir protingo dydžio
- Naudokite reliatyvius ryšius geresniam perkėlimo patogumui

### Projekto valdymas

Šis projektas laikosi Microsoft atviro kodo praktikų:
- MIT licencija kodui ir dokumentacijai
- Microsoft atviro kodo elgesio kodeksas
- Prisidėjimams reikalinga CLA
- Saugumo problemos: laikykitės SECURITY.md gairių
- Palaikymas: žr. SUPPORT.md pagalbos šaltiniams

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->