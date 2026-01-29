# AGENTS.md

## Projekto apžvalga

**MCP pradedantiesiems** yra atvirojo kodo edukacinė programa, skirta mokytis Model Context Protocol (MCP) – standartizuoto AI modelių ir klientų programų sąveikos pagrindo. Ši saugykla siūlo išsamią mokomąją medžiagą su praktiniais kodų pavyzdžiais įvairiomis programavimo kalbomis.

### Pagrindinės technologijos

- **Programavimo kalbos**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework'ai ir SDK**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Duomenų bazės**: PostgreSQL su pgvector plėtiniu
- **Debesų platformos**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Kūrimo įrankiai**: npm, Maven, pip, Cargo
- **Dokumentacija**: Markdown su automatiniu daugiakalbiu vertimu (48+ kalbos)

### Architektūra

- **11 pagrindinių modulių (00-11)**: Nuoseklus mokymosi kelias nuo pagrindų iki pažangių temų
- **Praktinės laboratorijos**: Praktiniai pratimai su pilnais sprendimų kodais įvairiomis kalbomis
- **Pavyzdiniai projektai**: Veikiantys MCP serverio ir kliento įgyvendinimai
- **Vertimo sistema**: Automatinis GitHub Actions darbo procesas daugiakalbei paramai
- **Vaizdiniai ištekliai**: Centralizuotas vaizdų katalogas su išversta versija

## Nustatymo komandos

Tai dokumentacijai skirtas saugyklos projektas. Dauguma nustatymų atliekami atskiruose pavyzdiniuose projektuose ir laboratorijose.

### Saugyklos nustatymas

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Darbas su pavyzdiniais projektais

Pavyzdiniai projektai yra:
- `03-GettingStarted/samples/` - Kalboms specifiniai pavyzdžiai
- `03-GettingStarted/01-first-server/solution/` - Pirmieji serverio įgyvendinimai
- `03-GettingStarted/02-client/solution/` - Kliento įgyvendinimai
- `11-MCPServerHandsOnLabs/` - Išsamios duomenų bazės integracijos laboratorijos

Kiekvienas pavyzdinis projektas turi savo nustatymo instrukcijas:

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
# or
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

### Dokumentacijos struktūra

- **Moduliai 00-11**: Pagrindinė mokymo programa nuoseklia tvarka
- **translations/**: Kalboms specifinės versijos (automatiškai generuojamos, neredaguoti tiesiogiai)
- **translated_images/**: Lokalizuotos vaizdų versijos (automatiškai generuojamos)
- **images/**: Šaltinio vaizdai ir diagramos

### Dokumentacijos pakeitimų atlikimas

1. Redaguokite tik anglų kalbos markdown failus pagrindiniuose modulių kataloguose (00-11)
2. Jei reikia, atnaujinkite vaizdus kataloge `images/`
3. GitHub Action co-op-translator automatiškai generuos vertimus
4. Vertimai generuojami po įkėlimo į pagrindinę šaką

### Darbas su vertimais

- **Automatinis vertimas**: GitHub Actions darbo procesas tvarko visus vertimus
- **Neredaguokite** failų kataloge `translations/`
- Vertimo metaduomenys yra įterpti kiekviename išverstame faile
- Palaikomos kalbos: 48+ kalbos, įskaitant arabų, kinų, prancūzų, vokiečių, hindi, japonų, korėjiečių, portugalų, rusų, ispanų ir daugelį kitų

## Testavimo instrukcijos

### Dokumentacijos patikra

Kadangi tai daugiausia dokumentacijos saugykla, testavimas apima:

1. **Nuorodų patikra**: Įsitikinkite, kad visos vidinės nuorodos veikia
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Kodo pavyzdžių patikra**: Patikrinkite, ar kodo pavyzdžiai kompiliuojasi/veikia
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown linting**: Patikrinkite formatavimo nuoseklumą
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Pavyzdinių projektų testavimas

Kiekvienas kalbai specifinis pavyzdys turi savo testavimo metodiką:

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
- Įtraukite kodo pavyzdžius keliomis kalbomis, kur tai taikoma
- Laikykitės geriausių markdown praktikų:
  - Naudokite ATX stiliaus antraštes (`#` sintaksė)
  - Naudokite aptvertus kodo blokus su kalbos identifikatoriais
  - Įtraukite aprašomuosius alt tekstus vaizdams
  - Laikykite linijų ilgį protingą (be griežto limito, bet būkite racionalūs)

### Kodo pavyzdžių stilius

#### TypeScript/JavaScript
- Naudokite ES modulius (`import`/`export`)
- Laikykitės TypeScript griežto režimo konvencijų
- Įtraukite tipų anotacijas
- Taikykite ES2022

#### Python
- Laikykitės PEP 8 stiliaus gairių
- Naudokite tipų užuominas, kur tai tinkama
- Įtraukite docstring'us funkcijoms ir klasėms
- Naudokite modernias Python funkcijas (3.8+)

#### Java
- Laikykitės Spring Boot konvencijų
- Naudokite Java 21 funkcijas
- Laikykitės standartinės Maven projekto struktūros
- Įtraukite Javadoc komentarus

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

Saugykla naudoja GitHub Pages ar panašų dokumentacijos talpinimui (jei taikoma). Pakeitimai pagrindinėje šakoje sukelia:

1. Vertimo darbo procesą (`.github/workflows/co-op-translator.yml`)
2. Automatinį visų anglų markdown failų vertimą
3. Vaizdų lokalizaciją, jei reikia

### Nereikalingas kūrimo procesas

Ši saugykla daugiausia apima markdown dokumentaciją. Pagrindinės mokymo programos turiniui nereikia kompiliavimo ar kūrimo žingsnio.

### Pavyzdinių projektų diegimas

Atskiri pavyzdiniai projektai gali turėti diegimo instrukcijas:
- Žr. `03-GettingStarted/09-deployment/` MCP serverio diegimo gaires
- Azure Container Apps diegimo pavyzdžiai `11-MCPServerHandsOnLabs/`

## Prisidėjimo gairės

### Pull Request procesas

1. **Fork ir Clone**: Fork'inkite saugyklą ir nukopijuokite savo fork'ą lokaliai
2. **Sukurkite šaką**: Naudokite aprašomuosius šakos pavadinimus (pvz., `fix/typo-module-3`, `add/python-example`)
3. **Atlikite pakeitimus**: Redaguokite tik anglų markdown failus (ne vertimus)
4. **Testuokite lokaliai**: Įsitikinkite, kad markdown tinkamai atvaizduojamas
5. **Pateikite PR**: Naudokite aiškius PR pavadinimus ir aprašymus
6. **CLA**: Pasirašykite Microsoft Contributor License Agreement, kai to prašoma

### PR pavadinimo formatas

Naudokite aiškius, aprašomuosius pavadinimus:
- `[Module XX] Trumpas aprašymas` moduliui specifiniams pakeitimams
- `[Samples] Aprašymas` pavyzdinio kodo pakeitimams
- `[Docs] Aprašymas` bendriems dokumentacijos atnaujinimams

### Ką prisidėti

- Dokumentacijos ar kodo pavyzdžių klaidų taisymai
- Nauji kodo pavyzdžiai papildomomis kalbomis
- Esamo turinio paaiškinimai ir patobulinimai
- Nauji atvejų tyrimai ar praktiniai pavyzdžiai
- Problemos pranešimai dėl neaiškaus ar neteisingo turinio

### Ko nedaryti

- Neredaguokite failų kataloge `translations/`
- Neredaguokite katalogo `translated_images/`
- Neįkelkite didelių dvejetainių failų be diskusijos
- Nekeiskite vertimo darbo procesų failų be koordinacijos

## Papildomos pastabos

### Saugyklos priežiūra

- **Pakeitimų žurnalas**: Visi reikšmingi pakeitimai dokumentuojami `changelog.md`
- **Mokymosi vadovas**: Naudokite `study_guide.md` mokymo programos navigacijos apžvalgai
- **Problemos šablonai**: Naudokite GitHub problemų šablonus klaidų pranešimams ir funkcijų užklausoms
- **Elgesio kodeksas**: Visi prisidedantys turi laikytis Microsoft Open Source Code of Conduct

### Mokymosi kelias

Sekite modulius nuoseklia tvarka (00-11) optimaliam mokymuisi:
1. **00-02**: Pagrindai (Įvadas, Pagrindinės sąvokos, Saugumas)
2. **03**: Pradžia su praktiniu įgyvendinimu
3. **04-05**: Praktinis įgyvendinimas ir pažangios temos
4. **06-10**: Bendruomenė, geriausios praktikos ir realaus pasaulio taikymas
5. **11**: Išsamios duomenų bazės integracijos laboratorijos (13 nuoseklių laboratorijų)

### Pagalbos ištekliai

- **Dokumentacija**: https://modelcontextprotocol.io/
- **Specifikacija**: https://spec.modelcontextprotocol.io/
- **Bendruomenė**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord serveris
- **Susiję kursai**: Žr. README.md kitoms Microsoft mokymosi programoms

### Dažniausiai užduodami klausimai

**K: Mano PR nepavyksta vertimo patikroje**
A: Įsitikinkite, kad redagavote tik anglų markdown failus pagrindiniuose modulių kataloguose, o ne išverstus failus.

**K: Kaip pridėti naują kalbą?**
A: Kalbų palaikymas valdomas per co-op-translator darbo procesą. Atidarykite problemą, kad aptartumėte naujų kalbų pridėjimą.

**K: Kodo pavyzdžiai neveikia**
A: Įsitikinkite, kad laikėtės nustatymo instrukcijų konkretaus pavyzdžio README faile. Patikrinkite, ar turite tinkamas priklausomybių versijas.

**K: Vaizdai nerodomi**
A: Patikrinkite, ar vaizdų keliai yra santykiniai ir naudojami įstrižiniai brūkšniai. Vaizdai turėtų būti kataloge `images/` arba `translated_images/` lokalizuotoms versijoms.

### Našumo svarstymai

- Vertimo darbo procesas gali užtrukti kelias minutes
- Dideli vaizdai turėtų būti optimizuoti prieš įkeliant
- Laikykite atskirus markdown failus sutelktus ir protingo dydžio
- Naudokite santykines nuorodas geresniam perkeliamumui

### Projekto valdymas

Šis projektas laikosi Microsoft atvirojo kodo praktikų:
- MIT licencija kodui ir dokumentacijai
- Microsoft Open Source Code of Conduct
- Reikalingas CLA prisidėjimui
- Saugumo klausimai: Laikykitės SECURITY.md gairių
- Pagalba: Žr. SUPPORT.md pagalbos ištekliams

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.