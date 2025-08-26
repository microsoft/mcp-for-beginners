<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a22b7dd11cd7690f99f9195877cafdc3",
  "translation_date": "2025-08-26T17:03:31+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md",
  "language_code": "lt"
}
-->
# 🌐 Modulis 2: MCP ir AI įrankių rinkinio pagrindai

[![Trukmė](https://img.shields.io/badge/Duration-20%20minutes-blue.svg)]()
[![Sudėtingumas](https://img.shields.io/badge/Difficulty-Intermediate-yellow.svg)]()
[![Reikalavimai](https://img.shields.io/badge/Prerequisites-Module%201%20Complete-orange.svg)]()

## 📋 Mokymosi tikslai

Šio modulio pabaigoje galėsite:
- ✅ Suprasti Model Context Protocol (MCP) architektūrą ir privalumus
- ✅ Susipažinti su „Microsoft“ MCP serverių ekosistema
- ✅ Integruoti MCP serverius su AI Toolkit Agent Builder
- ✅ Sukurti funkcionalų naršyklės automatizavimo agentą naudojant Playwright MCP
- ✅ Konfigūruoti ir testuoti MCP įrankius savo agentuose
- ✅ Eksportuoti ir diegti MCP pagrindu veikiančius agentus gamybai

## 🎯 Tęsiame nuo 1 modulio

1 modulyje išmokome AI Toolkit pagrindus ir sukūrėme pirmąjį Python agentą. Dabar mes **patobulinsime** jūsų agentus, prijungdami juos prie išorinių įrankių ir paslaugų per revoliucinį **Model Context Protocol (MCP)**.

Įsivaizduokite, kad pereinate nuo paprasto skaičiuotuvo prie pilno kompiuterio – jūsų AI agentai įgis galimybę:
- 🌐 Naršyti ir sąveikauti su svetainėmis
- 📁 Pasiekti ir manipuliuoti failais
- 🔧 Integruotis su įmonių sistemomis
- 📊 Apdoroti realaus laiko duomenis iš API

## 🧠 Model Context Protocol (MCP) supratimas

### 🔍 Kas yra MCP?

Model Context Protocol (MCP) yra **„USB-C AI programoms“** – revoliucinis atviras standartas, jungiantis didelius kalbos modelius (LLM) su išoriniais įrankiais, duomenų šaltiniais ir paslaugomis. Kaip USB-C pašalino kabelių chaosą, suteikdamas vieną universalų jungtį, MCP pašalina AI integracijos sudėtingumą su vienu standartizuotu protokolu.

### 🎯 Problema, kurią sprendžia MCP

**Prieš MCP:**
- 🔧 Individualios integracijos kiekvienam įrankiui
- 🔄 Priklausomybė nuo tiekėjų su patentuotais sprendimais  
- 🔒 Saugumo spragos dėl ad hoc jungčių
- ⏱️ Mėnesiai vystymo paprastoms integracijoms

**Su MCP:**
- ⚡ Įrankių integracija „plug-and-play“ principu
- 🔄 Nepriklausoma nuo tiekėjų architektūra
- 🛡️ Įdiegti saugumo geriausios praktikos
- 🚀 Naujos galimybės per kelias minutes

### 🏗️ MCP architektūros analizė

MCP naudoja **kliento-serverio architektūrą**, kuri sukuria saugią ir mastelio keičiamą ekosistemą:

```mermaid
graph TB
    A[AI Application/Agent] --> B[MCP Client]
    B --> C[MCP Server 1: Files]
    B --> D[MCP Server 2: Web APIs]
    B --> E[MCP Server 3: Database]
    B --> F[MCP Server N: Custom Tools]
    
    C --> G[Local File System]
    D --> H[External APIs]
    E --> I[Database Systems]
    F --> J[Enterprise Systems]
```

**🔧 Pagrindiniai komponentai:**

| Komponentas | Vaidmuo | Pavyzdžiai |
|-------------|---------|------------|
| **MCP Hostai** | Programos, kurios naudoja MCP paslaugas | Claude Desktop, VS Code, AI Toolkit |
| **MCP Klientai** | Protokolo tvarkytojai (1:1 su serveriais) | Įdiegti host programose |
| **MCP Serveriai** | Teikia galimybes per standartinį protokolą | Playwright, Files, Azure, GitHub |
| **Transporto sluoksnis** | Komunikacijos metodai | stdio, HTTP, WebSockets |

## 🏢 „Microsoft“ MCP serverių ekosistema

„Microsoft“ vadovauja MCP ekosistemai, siūlydama išsamų verslo klasės serverių rinkinį, kuris sprendžia realius verslo poreikius.

### 🌟 „Microsoft“ MCP serveriai

#### 1. ☁️ Azure MCP serveris
**🔗 Saugykla**: [azure/azure-mcp](https://github.com/azure/azure-mcp)  
**🎯 Tikslas**: Išsamus Azure resursų valdymas su AI integracija

**✨ Pagrindinės funkcijos:**
- Deklaratyvus infrastruktūros paruošimas
- Realiojo laiko resursų stebėjimas
- Kaštų optimizavimo rekomendacijos
- Saugumo atitikties tikrinimas

**🚀 Naudojimo atvejai:**
- Infrastruktūra kaip kodas su AI pagalba
- Automatinis resursų mastelio keitimas
- Debesų kaštų optimizavimas
- DevOps darbo eigos automatizavimas

#### 2. 📊 Microsoft Dataverse MCP
**📚 Dokumentacija**: [Microsoft Dataverse Integration](https://go.microsoft.com/fwlink/?linkid=2320176)  
**🎯 Tikslas**: Natūralios kalbos sąsaja verslo duomenims

**✨ Pagrindinės funkcijos:**
- Natūralios kalbos duomenų bazės užklausos
- Verslo konteksto supratimas
- Individualūs šablonai
- Įmonės duomenų valdymas

**🚀 Naudojimo atvejai:**
- Verslo analitikos ataskaitos
- Klientų duomenų analizė
- Pardavimų proceso įžvalgos
- Atitikties duomenų užklausos

#### 3. 🌐 Playwright MCP serveris
**🔗 Saugykla**: [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)  
**🎯 Tikslas**: Naršyklės automatizavimas ir sąveika su tinklalapiais

**✨ Pagrindinės funkcijos:**
- Naršyklių automatizavimas (Chrome, Firefox, Safari)
- Išmanus elementų aptikimas
- Ekrano nuotraukų ir PDF generavimas
- Tinklo srauto stebėjimas

**🚀 Naudojimo atvejai:**
- Automatizuoti testavimo procesai
- Tinklalapių duomenų ištraukimas
- UI/UX stebėjimas
- Konkurencijos analizės automatizavimas

#### 4. 📁 Files MCP serveris
**🔗 Saugykla**: [microsoft/files-mcp-server](https://github.com/microsoft/files-mcp-server)  
**🎯 Tikslas**: Išmanios failų sistemos operacijos

**✨ Pagrindinės funkcijos:**
- Deklaratyvus failų valdymas
- Turinio sinchronizavimas
- Versijų kontrolės integracija
- Metaduomenų ištraukimas

**🚀 Naudojimo atvejai:**
- Dokumentų valdymas
- Kodo saugyklos organizavimas
- Turinio publikavimo darbo eigos
- Duomenų srautų failų tvarkymas

#### 5. 📝 MarkItDown MCP serveris
**🔗 Saugykla**: [microsoft/markitdown](https://github.com/microsoft/markitdown)  
**🎯 Tikslas**: Pažangus Markdown apdorojimas ir manipuliavimas

**✨ Pagrindinės funkcijos:**
- Išsamus Markdown analizavimas
- Formatų konvertavimas (MD ↔ HTML ↔ PDF)
- Turinio struktūros analizė
- Šablonų apdorojimas

**🚀 Naudojimo atvejai:**
- Techninės dokumentacijos darbo eigos
- Turinio valdymo sistemos
- Ataskaitų generavimas
- Žinių bazės automatizavimas

#### 6. 📈 Clarity MCP serveris
**📦 Paketas**: [@microsoft/clarity-mcp-server](https://www.npmjs.com/package/@microsoft/clarity-mcp-server)  
**🎯 Tikslas**: Tinklalapių analizė ir vartotojų elgsenos įžvalgos

**✨ Pagrindinės funkcijos:**
- Šilumos žemėlapių duomenų analizė
- Vartotojų sesijų įrašai
- Našumo metrikos
- Konversijos proceso analizė

**🚀 Naudojimo atvejai:**
- Svetainės optimizavimas
- Vartotojų patirties tyrimai
- A/B testavimo analizė
- Verslo analitikos ataskaitos

### 🌍 Bendruomenės ekosistema

Be „Microsoft“ serverių, MCP ekosistema apima:
- **🐙 GitHub MCP**: Saugyklų valdymas ir kodo analizė
- **🗄️ Duomenų bazės MCP**: PostgreSQL, MySQL, MongoDB integracijos
- **☁️ Debesų tiekėjų MCP**: AWS, GCP, Digital Ocean įrankiai
- **📧 Komunikacijos MCP**: Slack, Teams, el. pašto integracijos

## 🛠️ Praktinis darbas: Naršyklės automatizavimo agento kūrimas

**🎯 Projekto tikslas**: Sukurti išmanų naršyklės automatizavimo agentą, naudojant Playwright MCP serverį, kuris galėtų naršyti svetainėse, išgauti informaciją ir atlikti sudėtingas sąveikas.

### 🚀 1 etapas: Agentų pagrindų nustatymas

#### 1 žingsnis: Sukurkite savo agentą
1. **Atidarykite AI Toolkit Agent Builder**
2. **Sukurkite naują agentą** su šia konfigūracija:
   - **Pavadinimas**: `BrowserAgent`
   - **Modelis**: Pasirinkite GPT-4o 

![BrowserAgent](../../../../translated_images/BrowserAgent.09c1adde5e136573b64ab1baecd830049830e295eac66cb18bebb85fb386e00a.lt.png)

### 🔧 2 etapas: MCP integracijos darbo eiga

#### 3 žingsnis: Pridėkite MCP serverio integraciją
1. **Eikite į įrankių skyrių** Agent Builder
2. **Spustelėkite „Pridėti įrankį“**, kad atidarytumėte integracijos meniu
3. **Pasirinkite „MCP serverį“** iš galimų parinkčių

![AddMCP](../../../../translated_images/AddMCP.afe3308ac20aa94469a5717b632d77b2197b9838a438b05d39aeb2db3ec47ef1.lt.png)

**🔍 Įrankių tipų supratimas:**
- **Įmontuoti įrankiai**: Iš anksto sukonfigūruotos AI Toolkit funkcijos
- **MCP serveriai**: Išorinių paslaugų integracijos
- **Individualūs API**: Jūsų pačių paslaugų galiniai taškai
- **Funkcijų kvietimas**: Tiesioginė modelio funkcijų prieiga

#### 4 žingsnis: MCP serverio pasirinkimas
1. **Pasirinkite „MCP serverį“**, kad tęstumėte
![AddMCPServer](../../../../translated_images/AddMCPServer.69b911ccef872cbd0d0c0c2e6a00806916e1673e543b902a23dee23e6ff54b4c.lt.png)

2. **Naršykite MCP katalogą**, kad atrastumėte galimas integracijas
![MCPCatalog](../../../../translated_images/MCPCatalog.a817d053145699006264f5a475f2b48fbd744e43633f656b6453c15a09ba5130.lt.png)

### 🎮 3 etapas: Playwright MCP konfigūracija

#### 5 žingsnis: Pasirinkite ir konfigūruokite Playwright
1. **Spustelėkite „Naudoti rekomenduojamus MCP serverius“**, kad pasiektumėte „Microsoft“ patvirtintus serverius
2. **Pasirinkite „Playwright“** iš rekomenduojamų sąrašo
3. **Priimkite numatytą MCP ID** arba pritaikykite savo aplinkai

![MCPID](../../../../translated_images/MCPID.67d446052979e819c945ff7b6430196ef587f5217daadd3ca52fa9659c1245c9.lt.png)

#### 6 žingsnis: Įgalinkite Playwright galimybes
**🔑 Kritinis žingsnis**: Pasirinkite **VISAS** galimas Playwright funkcijas, kad užtikrintumėte maksimalų funkcionalumą

![Tools](../../../../translated_images/Tools.3ea23c447b4d9feccbd7101e6dcf9e27cb0e5273f351995fde62c5abf9a78b4c.lt.png)

**🛠️ Esminiai Playwright įrankiai:**
- **Navigacija**: `goto`, `goBack`, `goForward`, `reload`
- **Sąveika**: `click`, `fill`, `press`, `hover`, `drag`
- **Ištraukimas**: `textContent`, `innerHTML`, `getAttribute`
- **Validacija**: `isVisible`, `isEnabled`, `waitForSelector`
- **Fiksavimas**: `screenshot`, `pdf`, `video`
- **Tinklas**: `setExtraHTTPHeaders`, `route`, `waitForResponse`

#### 7 žingsnis: Patikrinkite integracijos sėkmę
**✅ Sėkmės indikatoriai:**
- Visi įrankiai rodomi Agent Builder sąsajoje
- Nėra klaidų pranešimų integracijos skydelyje
- Playwright serverio būsena rodo „Prisijungta“

![AgentTools](../../../../translated_images/AgentTools.053cfb96a17e02199dcc6563010d2b324d4fc3ebdd24889657a6950647a52f63.lt.png)

**🔧 Dažniausių problemų sprendimas:**
- **Nepavyko prisijungti**: Patikrinkite interneto ryšį ir ugniasienės nustatymus
- **Trūksta įrankių**: Įsitikinkite, kad visos galimybės buvo pasirinktos nustatymo metu
- **Leidimų klaidos**: Patikrinkite, ar VS Code turi reikiamus sistemos leidimus

### 🎯 4 etapas: Pažangus promptų kūrimas

#### 8 žingsnis: Sukurkite išmanius sistemos promptus
Sukurkite sudėtingus promptus, kurie išnaudoja visas Playwright galimybes:

```markdown
# Web Automation Expert System Prompt

## Core Identity
You are an advanced web automation specialist with deep expertise in browser automation, web scraping, and user experience analysis. You have access to Playwright tools for comprehensive browser control.

## Capabilities & Approach
### Navigation Strategy
- Always start with screenshots to understand page layout
- Use semantic selectors (text content, labels) when possible
- Implement wait strategies for dynamic content
- Handle single-page applications (SPAs) effectively

### Error Handling
- Retry failed operations with exponential backoff
- Provide clear error descriptions and solutions
- Suggest alternative approaches when primary methods fail
- Always capture diagnostic screenshots on errors

### Data Extraction
- Extract structured data in JSON format when possible
- Provide confidence scores for extracted information
- Validate data completeness and accuracy
- Handle pagination and infinite scroll scenarios

### Reporting
- Include step-by-step execution logs
- Provide before/after screenshots for verification
- Suggest optimizations and alternative approaches
- Document any limitations or edge cases encountered

## Ethical Guidelines
- Respect robots.txt and rate limiting
- Avoid overloading target servers
- Only extract publicly available information
- Follow website terms of service
```

#### 9 žingsnis: Sukurkite dinamiškus vartotojo promptus
Sukurkite promptus, kurie demonstruoja įvairias galimybes:

**🌐 Tinklalapio analizės pavyzdys:**
```markdown
Navigate to github.com/kinfey and provide a comprehensive analysis including:
1. Repository structure and organization
2. Recent activity and contribution patterns  
3. Documentation quality assessment
4. Technology stack identification
5. Community engagement metrics
6. Notable projects and their purposes

Include screenshots at key steps and provide actionable insights.
```

![Prompt](../../../../translated_images/Prompt.bfc846605db4999f4d9c1b09c710ef63cae7b3057444e68bf07240fb142d9f8f.lt.png)

### 🚀 5 etapas: Vykdymas ir testavimas

#### 10 žingsnis: Paleiskite pirmąją automatizaciją
1. **Spustelėkite „Paleisti“**, kad pradėtumėte automatizacijos seką
2. **Stebėkite realaus laiko vykdymą**:
   - Chrome naršyklė paleidžiama automatiškai
   - Agentas naršo tikslinę svetainę
   - Ekrano nuotraukos fiksuoja kiekvieną svarbų žingsnį
   - Analizės rezultatai transliuojami realiu laiku

![Browser](../../../../translated_images/Browser.ec011d0bd64d0d112c8a29bd8cc44c76d0bbfd0b019cb2983ef679328435ce5d.lt.png)

#### 11 žingsnis: Analizuokite rezultatus ir įžvalgas
Peržiūrėkite išsamią analizę Agent Builder sąsajoje:

![Result](../../../../translated_images/Result.8638f2b6703e9ea6d58d4e4475e39456b6a51d4c787f9bf481bae694d370a69a.lt.png)

### 🌟 6 etapas: Pažangios galimybės ir diegimas

#### 12 žingsnis: Eksportavimas ir diegimas gamybai
Agent Builder palaiko kelias diegimo parinktis:

![Code](../../../../translated_images/Code.d9eeeead0b96db0ca19c5b10ad64cfea8c1d0d1736584262970a4d43e1403d13.lt.png)

## 🎓 Modulio 2 santrauka ir tolesni žingsniai

### 🏆 Pasiekimas: MCP integracijos meistras

**✅ Įgyti įgūdžiai:**
- [ ] MCP architektūros ir privalumų supratimas
- [ ] „Microsoft“ MCP serverių ekosistemos naršymas
- [ ] Playwright MCP integracija su AI Toolkit
- [ ] Pažangių naršyklės automatizavimo agentų kūrimas
- [ ] Pažangus promptų kūrimas tinklalapių automatizavimui

### 📚 Papildomi ištekliai

- **🔗 MCP specifikacija**: [Oficiali protokolo dokumentacija](https://modelcontextprotocol.io/)
- **🛠️ Playwright API**: [Visas metodų sąrašas](https://playwright.dev/docs/api/class-playwright)
- **🏢 „Microsoft“ MCP serveriai**: [Verslo integracijos vadovas](https://github.com/microsoft/mcp-servers)
- **🌍 Bendruomenės pavyzdžiai**: [MCP serverių galerija](https://github.com/modelcontextprotocol/servers)

**🎉 Sveikiname!** Jūs sėkmingai įvaldėte MCP integraciją ir dabar galite kurti gamybai paruoštus AI agentus su išorinių įrankių galimybėmis!

### 🔜 Tęskite kitą modulį

Pasiruošę tobulinti savo
- Sukurkite orų MCP serverį nuo nulio

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.