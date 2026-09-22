# Įvadas į MCP duomenų bazės integraciją

> [!NOTE]
> Šio mokymosi kelio schemos arba kodas, naudojantis HTTP/SSE arba inicializacijos
> parinktis, atspindi mėginio MCP „2025-11-25“ priklausomybes. Naujoms
> diegimams naudokite „2026-07-28“ būsenos neturinčius užklausimus ir srautinius HTTP.

## 🎯 Ko šis laboratorinis darbas apima

Šis įvadinis laboratorinis darbas suteikia išsamų Model Context Protocol (MCP) serverių kūrimo su duomenų bazės integracija apžvalgą. Suprasite verslo atvejį, techninę architektūrą ir realaus pasaulio taikymus per Zava Retail analizės naudojimo atvejį https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Apžvalga

**Model Context Protocol (MCP)** leidžia AI asistentams saugiai prieiti ir sąveikauti su išoriniais duomenų šaltiniais realiu laiku. Derinant su duomenų bazės integracija, MCP atrakina galingas galimybes duomenimis pagrįstoms AI programoms.

Šis mokymosi kelias moko jus kurti gamybinio lygio MCP serverius, kurie sujungia AI asistentus su mažmeninės prekybos pardavimų duomenimis per PostgreSQL, įgyvendinant įmonių modelius, tokius kaip eilutės lygio saugumas, semantinis paieška ir daugiaklientės prieigos prie duomenų valdymas.

## Mokymosi tikslai

Baigę šį laboratorinį darbą, galėsite:

- **Apibrėžti** Model Context Protocol ir jo pagrindinius privalumus duomenų bazės integracijai
- **Nustatyti** svarbias MCP serverio architektūros su duomenų bazėmis sudedamąsias dalis
- **Suprasti** Zava Retail naudojimo atvejį ir jo verslo reikalavimus
- **Atpažinti** įmonių modelius saugiai ir mastelį palaikančiai duomenų prieigai
- **Išvardinti** įrankius ir technologijas, naudojamas šiame mokymosi kelyje

## 🧭 Iššūkis: AI susitinka su realaus pasaulio duomenimis

### Tradiciniai AI apribojimai

Šiuolaikiniai AI asistentai yra nepaprastai galingi, tačiau susiduria su reikšmingais apribojimais dirbdami su realaus verslo duomenimis:

| **Iššūkis** | **Aprašymas** | **Verslo poveikis** |
|---------------|-----------------|-------------------|
| **Statinės žinios** | AI modeliai, apmokyti fiksuotais duomenų rinkiniais, neturi prieigos prie dabartinių verslo duomenų | Pasenę įžvalgos, prarastos galimybės |
| **Duomenų salos** | Informacija užrakinta duomenų bazėse, API ir sistemose, kurių AI negali pasiekti | Nepilnas analizavimas, fragmentuoti darbo srautai |
| **Saugumo apribojimai** | Tiesioginė prieiga prie duomenų bazės kelia saugumo ir atitikties problemų | Ribotas diegimas, rankinis duomenų paruošimas |
| **Sudėtingos užklausos** | Verslo vartotojams reikia techninių žinių išgauti duomenų įžvalgas | Sumažintas naudojimas, neefektyvūs procesai |

### MCP sprendimas

Model Context Protocol sprendžia šiuos iššūkius, suteikdamas:

- **Realios laiko duomenų prieigą**: AI asistentai gali užklausti gyvų duomenų bazių ir API
- **Saugų integravimą**: Kontroliuojama prieiga su autentifikacija ir leidimais
- **Natūralios kalbos sąsają**: Verslo vartotojai užduoda klausimus paprasta angliškomis formomis
- **Standartizuotą protokolą**: Veikia per skirtingas AI platformas ir įrankius

## 🏪 Susipažinkite su Zava Retail: mūsų mokymosi atveju https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Visą šį mokymosi kelią kursime MCP serverį **Zava Retail**, fiktyviai „pasidaryk pats“ mažmeninės prekybos tinklu, turinčiu keletą parduotuvių. Ši realistiška situacija demonstruoja įmonių lygio MCP diegimą.

### Verslo kontekstas

**Zava Retail** veikia:
- **8 fizinių parduotuvių** Vašingtono valstijoje (Sietlas, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 internetinę parduotuvę** e. prekybos pardavimams
- **Įvairų produktų katalogą**, įskaitant įrankius, aparatūrą, sodo prekes ir statybines medžiagas
- **Daugiapakopę vadybą** su parduotuvių vadovais, regiono vadovais ir vadovybe

### Verslo reikalavimai

Parduotuvės vadovai ir vadovybė reikia AI pagrįstų analitikų, kad galėtų:

1. **Analizuoti pardavimų rezultatus** per parduotuves ir laikotarpius
2. **Stebėti atsargų lygius** ir nustatyti papildymo poreikius
3. **Suprasti klientų elgseną** ir pirkimo modelius
4. **Atrasti produktų įžvalgas** naudojant semantinę paiešką
5. **Generuoti ataskaitas** natūralios kalbos užklausomis
6. **Užtikrinti duomenų saugumą** naudojant vaidmenų pagrindu valdomą prieigą

### Techniniai reikalavimai

MCP serveris turi suteikti:

- **Daugiaklientę duomenų prieigą**, kur parduotuvių vadovai mato tik savo parduotuvės duomenis
- **Lankstų užklausų palaikymą**, leidžiant sudėtingas SQL operacijas
- **Semantinę paiešką** produktų atradimui ir rekomendacijoms
- **Realiojo laiko duomenis**, atspindinčius dabartinę verslo būklę
- **Saugų autentifikavimą** su eilutės lygiu saugumu
- **Mastelį palaikančią architektūrą**, leidžiančią keliems vartotojams vienu metu

## 🏗️ MCP serverio architektūros apžvalga

Mūsų MCP serveris įgyvendina sluoksniuotą architektūrą, optimizuotą duomenų bazių integracijai:

```
┌─────────────────────────────────────────────────────────────┐
│                    VS Code AI Client                       │
│                  (Natural Language Queries)                │
└─────────────────────┬───────────────────────────────────────┘
                      │ HTTP/SSE
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                     MCP Server                             │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │   Tool Layer    │ │  Security Layer │ │  Config Layer │ │
│  │                 │ │                 │ │               │ │
│  │ • Query Tools   │ │ • RLS Context   │ │ • Environment │ │
│  │ • Schema Tools  │ │ • User Identity │ │ • Connections │ │
│  │ • Search Tools  │ │ • Access Control│ │ • Validation  │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ asyncpg
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                PostgreSQL Database                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌───────────────┐ │
│  │  Retail Schema  │ │   RLS Policies  │ │   pgvector    │ │
│  │                 │ │                 │ │               │ │
│  │ • Stores        │ │ • Store-based   │ │ • Embeddings  │ │
│  │ • Customers     │ │   Isolation     │ │ • Similarity  │ │
│  │ • Products      │ │ • Role Control  │ │   Search      │ │
│  │ • Orders        │ │ • Audit Logs    │ │               │ │
│  └─────────────────┘ └─────────────────┘ └───────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │ REST API
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  Azure OpenAI                              │
│               (Text Embeddings)                            │
└─────────────────────────────────────────────────────────────┘
```

### Pagrindinės sudedamosios dalys

#### **1. MCP serverio sluoksnis**
- **FastMCP Framework**: modernus Python MCP serverio įgyvendinimas
- **Įrankių registracija**: deklaratyvūs įrankių apibrėžimai su tipų saugumu
- **Užklausos kontekstas**: vartotojo tapatybė ir sesijos valdymas
- **Klaidų valdymas**: tvirtas klaidų tvarkymas ir žurnalavimas

#### **2. Duomenų bazės integracijos sluoksnis**
- **Jungčių valdymas**: efektyvus asyncpg jungčių valdymas
- **Schemos tiekėjas**: dinaminis lentelės schemos aptikimas
- **Užklausos vykdytojas**: saugus SQL vykdymas su RLS kontekstu
- **Transakcijų valdymas**: ACID atitiktis ir atšaukimo valdymas

#### **3. Saugumo sluoksnis**
- **Eilutės lygio saugumas**: PostgreSQL RLS daugiklio klientų duomenų izoliacijai
- **Vartotojo tapatybė**: parduotuvės vadybininko autentifikacija ir autorizacija
- **Prieigos kontrolė**: smulkiai reguliuojami leidimai ir audito įrašai
- **Įvesties validacija**: SQL injekcijos prevencija ir užklausų tikrinimas

#### **4. AI patobulinimų sluoksnis**
- **Semantinė paieška**: vektorinės įterptinės reprezentacijos produktų atradimui
- **Azure OpenAI integracija**: teksto įterpiniai generavimui
- **Panašumo algoritmai**: pgvector kosinuso panašumo paieška
- **Paieškos optimizavimas**: indeksavimas ir našumo tobulinimas

## 🔧 Technologijų rinkinys

### Pagrindinės technologijos

| **Sudedamoji dalis** | **Technologija** | **Paskirtis** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Modernus MCP serverio įgyvendinimas |
| **Duomenų bazė** | PostgreSQL 17 + pgvector | Reliaciniai duomenys su vektorine paieška |
| **AI paslaugos** | Azure OpenAI | Teksto įterptinių ir kalbos modeliai |
| **Konteinerizacija** | Docker + Docker Compose | Kūrimo aplinka |
| **Debesų platforma** | Microsoft Azure | Gamybinis diegimas |
| **IDE integracija** | VS Code | AI pokalbių ir kūrimo darbo eiga |

### Kūrimo įrankiai

| **Įrankis** | **Paskirtis** |
|----------|-------------|
| **asyncpg** | Didelio našumo PostgreSQL vairuotojas |
| **Pydantic** | Duomenų validavimas ir serializavimas |
| **Azure SDK** | Debesų paslaugų integracija |
| **pytest** | Testavimo karkasas |
| **Docker** | Konteinerizacija ir diegimas |

### Gamybinis rinkinys

| **Paslauga** | **Azure resursas** | **Paskirtis** |
|-------------|-------------------|-------------|
| **Duomenų bazė** | Azure Database for PostgreSQL | Valdomos duomenų bazės paslauga |
| **Konteineris** | Azure Container Apps | Serverio nesudėtingas konteinerių talpinimas |
| **AI paslaugos** | Microsoft Foundry | OpenAI modeliai ir galiniai taškai |
| **Stebėsena** | Application Insights | Stebėjimo ir diagnostikos įrankiai |
| **Saugumas** | Azure Key Vault | Slaptažodžių ir konfigūracijų valdymas |

## 🎬 Realūs naudojimo scenarijai

Pažiūrėkime, kaip įvairūs vartotojai sąveikauja su mūsų MCP serveriu:

### Scenarijus 1: Parduotuvės vadovo veiklos apžvalga

**Vartotojas**: Sarah, Sietlo parduotuvės vadovė  
**Tikslas**: Analizuoti praėjusio ketvirčio pardavimų rezultatus

**Natūralios kalbos užklausa**:
> "Parodyk man 10 pelningiausių produktų mano parduotuvėje 2024 m. IV ketvirtį"

**Kas vyksta**:
1. VS Code AI pokalbis siunčia užklausą MCP serveriui
2. MCP serveris identifikuoja Sarah parduotuvės kontekstą (Sietlas)
3. RLS politika filtruoją duomenis tik Sietlo parduotuvei
4. Generuojama ir vykdoma SQL užklausa
5. Rezultatai formatuojami ir grąžinami AI pokalbiui
6. AI pateikia analizę ir įžvalgas

### Scenarijus 2: Produktų atradimas naudojant semantinę paiešką

**Vartotojas**: Mike, atsargų vadybininkas  
**Tikslas**: Rasti produktus, panašius į kliento užklausą

**Natūralios kalbos užklausa**:
> "Kokius produktus parduodame, kurie panašūs į ‘atsparius vandeniui lauko elektros jungiklius’?"

**Kas vyksta**:
1. Užklausa apdorojama semantinės paieškos įrankiu
2. Azure OpenAI generuoja įterpinio vektorių
3. pgvector atlieka panašumo paiešką
4. Susiję produktai vertinami pagal aktualumą
5. Rezultatuose pateikiamos produkto detalės ir prieinamumas
6. AI siūlo alternatyvas ir komplektavimo galimybes

### Scenarijus 3: Analizė per parduotuves

**Vartotojas**: Jennifer, regiono vadovė  
**Tikslas**: Palyginti veiklą visose parduotuvėse

**Natūralios kalbos užklausa**:
> "Palyginkite pardavimus pagal kategoriją per paskutinius 6 mėnesius visose parduotuvėse"

**Kas vyksta**:
1. Nustatomas RLS kontekstas regiono vadovo prieigai
2. Sugeneruojama sudėtinga daugaparduotuvės užklausa
3. Duomenys apibendrinami iš visų parduotuvių vietų
4. Rezultatai pateikia tendencijas ir palyginimus
5. AI identifikuoja įžvalgas ir rekomendacijas

## 🔒 Saugumo ir daugiaklientės prieigos giluminė analizė

Mūsų įgyvendinimas prioritetizuoja įmonių lygio saugumą:

### Eilutės lygio saugumas (RLS)

PostgreSQL RLS užtikrina duomenų izoliaciją:

```sql
-- Store managers see only their store's data
CREATE POLICY store_manager_policy ON retail.orders
  FOR ALL TO store_managers
  USING (store_id = get_current_user_store());

-- Regional managers see multiple stores
CREATE POLICY regional_manager_policy ON retail.orders
  FOR ALL TO regional_managers
  USING (store_id = ANY(get_user_store_list()));
```

### Vartotojo tapatybės valdymas

Kiekviena MCP jungtis apima:
- **Parduotuvės vadybininko ID**: unikalus identifikatorius RLS kontekstui
- **Vaidmens priskyrimas**: leidimai ir prieigos lygiai
- **Sesijos valdymas**: saugūs autentifikacijos žetonai
- **Audito žurnalas**: pilna prieigos istorija

### Duomenų apsauga

Kelios saugumo sluoksniai:
- **Jungčių šifravimas**: TLS visiems duomenų bazės ryšiams
- **SQL injekcijos prevencija**: tik parametrizuotos užklausos
- **Įvesties validacija**: išsami užklausų tikrinimas
- **Klaidų valdymas**: klaidų pranešimuose nėra jautrios informacijos

## 🎯 Pagrindinės įžvalgos

Baigę šį įvadą, turėtumėte suprasti:

✅ **MCP vertės pasiūlymas**: kaip MCP jungia AI asistentus ir realaus pasaulio duomenis  
✅ **Verslo kontekstas**: Zava Retail reikalavimai ir iššūkiai  
✅ **Architektūros apžvalga**: pagrindinės sudedamosios dalys ir jų sąveika  
✅ **Technologijų rinkinys**: įrankiai ir karkasai, naudojami viso mokymosi kelio metu  
✅ **Saugumo modelis**: daugiaklientės prieigos prie duomenų ir apsauga  
✅ **Naudojimo modeliai**: realaus pasaulio užklausų scenarijai ir darbo srautai  

## 🚀 Kas toliau

Norite gilintis? Tęskite su:

**[Laboratorinis darbas 01: Pagrindinės architektūros sąvokos](../01-Architecture/README.md)**

Sužinokite apie MCP serverio architektūros modelius, duomenų bazės projektavimo principus ir išsamų techninį įgyvendinimą, kuris palaiko mūsų mažmeninės prekybos analizės sprendimą.

## 📚 Papildomi ištekliai

### MCP dokumentacija
- [MCP specifikacija](https://modelcontextprotocol.io/docs/) - oficiali protokolo dokumentacija
- [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners) - išsamus MCP mokymosi vadovas
- [FastMCP dokumentacija](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentacija

### Duomenų bazės integracija
- [PostgreSQL dokumentacija](https://www.postgresql.org/docs/) - išsami PostgreSQL nuoroda
- [pgvector vadovas](https://github.com/pgvector/pgvector) - vektorių plėtinio dokumentacija
- [Eilutės lygio saugumas](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS vadovas

### Azure paslaugos
- [Azure OpenAI dokumentacija](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI paslaugų integracija
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - valdomos duomenų bazės paslauga
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - serverio nesudėtingi konteineriai

---

**Atsakomybės apribojimas**: tai mokymosi pratimas naudojant išgalvotus mažmeninės prekybos duomenis. Visada laikykitės savo organizacijos duomenų valdymo ir saugumo politikos diegdami panašius sprendimus gamybos aplinkose.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->