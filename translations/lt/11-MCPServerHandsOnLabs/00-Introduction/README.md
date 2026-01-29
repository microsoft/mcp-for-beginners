# Įvadas į MCP duomenų bazės integraciją

## 🎯 Ką apima šis praktinis užsiėmimas

Šis įvadinis praktinis užsiėmimas suteikia išsamų supratimą apie Model Context Protocol (MCP) serverių kūrimą su duomenų bazės integracija. Jūs suprasite verslo atvejį, techninę architektūrą ir realaus pasaulio pritaikymą per Zava Retail analitikos pavyzdį, pateiktą adresu https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Apžvalga

**Model Context Protocol (MCP)** leidžia dirbtinio intelekto asistentams saugiai pasiekti ir sąveikauti su išoriniais duomenų šaltiniais realiuoju laiku. Sujungus MCP su duomenų bazės integracija, atsiveria galingos galimybės duomenimis pagrįstoms dirbtinio intelekto programoms.

Ši mokymosi programa moko jus kurti gamybai paruoštus MCP serverius, kurie jungia dirbtinio intelekto asistentus su mažmeninės prekybos pardavimų duomenimis per PostgreSQL, įgyvendinant įmonės modelius, tokius kaip eilutės lygio saugumas, semantinė paieška ir daugiabučių duomenų prieiga.

## Mokymosi tikslai

Baigę šį praktinį užsiėmimą, jūs galėsite:

- **Apibrėžti** Model Context Protocol ir jo pagrindinius privalumus duomenų bazės integracijai
- **Identifikuoti** pagrindinius MCP serverio architektūros komponentus su duomenų bazėmis
- **Suprasti** Zava Retail pavyzdį ir jo verslo reikalavimus
- **Atpažinti** įmonės modelius saugiai ir mastelio požiūriu efektyviai duomenų prieigai
- **Išvardinti** įrankius ir technologijas, naudojamus visoje mokymosi programoje

## 🧭 Iššūkis: AI susitinka su realaus pasaulio duomenimis

### Tradiciniai AI apribojimai

Šiuolaikiniai dirbtinio intelekto asistentai yra nepaprastai galingi, tačiau susiduria su reikšmingais apribojimais dirbant su realaus pasaulio verslo duomenimis:

| **Iššūkis** | **Aprašymas** | **Verslo poveikis** |
|-------------|---------------|---------------------|
| **Statinės žinios** | AI modeliai, apmokyti fiksuotais duomenų rinkiniais, negali pasiekti dabartinių verslo duomenų | Pasenusi įžvalga, praleistos galimybės |
| **Duomenų silosai** | Informacija užrakinta duomenų bazėse, API ir sistemose, kurių AI negali pasiekti | Nepilna analizė, suskaidyti darbo procesai |
| **Saugumo apribojimai** | Tiesioginė duomenų bazės prieiga kelia saugumo ir atitikties problemas | Ribotas diegimas, rankinis duomenų paruošimas |
| **Sudėtingos užklausos** | Verslo vartotojams reikia techninių žinių, kad išgautų duomenų įžvalgas | Sumažėjęs priėmimas, neefektyvūs procesai |

### MCP sprendimas

Model Context Protocol sprendžia šiuos iššūkius, suteikdamas:

- **Duomenų prieigą realiuoju laiku**: AI asistentai užklausia gyvas duomenų bazes ir API
- **Saugų integravimą**: Kontroliuojama prieiga su autentifikacija ir leidimais
- **Natūralios kalbos sąsają**: Verslo vartotojai užduoda klausimus paprasta anglų kalba
- **Standartizuotą protokolą**: Veikia su skirtingomis AI platformomis ir įrankiais

## 🏪 Susipažinkite su Zava Retail: mūsų mokymosi atvejo studija https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Visoje mokymosi programoje mes kursime MCP serverį **Zava Retail**, fiktyviai „pasidaryk pats“ mažmeninės prekybos tinklui su keliais parduotuvių vietomis. Šis realistiškas scenarijus demonstruoja įmonės lygio MCP įgyvendinimą.

### Verslo kontekstas

**Zava Retail** valdo:
- **8 fizines parduotuves** Vašingtono valstijoje (Sietlas, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 internetinę parduotuvę** e. prekybos pardavimams
- **Įvairų produktų katalogą**, įskaitant įrankius, techninę įrangą, sodo reikmenis ir statybines medžiagas
- **Daugiapakopę valdymo struktūrą** su parduotuvių vadovais, regioniniais vadovais ir vadovais

### Verslo reikalavimai

Parduotuvės vadovams ir vadovams reikia AI pagrįstos analitikos, kad:

1. **Analizuotų pardavimų rezultatus** skirtingose parduotuvėse ir laikotarpiuose
2. **Sekti inventoriaus lygį** ir nustatyti poreikį papildyti atsargas
3. **Suprasti klientų elgesį** ir pirkimo modelius
4. **Atrasti produktų įžvalgas** per semantinę paiešką
5. **Generuoti ataskaitas** naudojant natūralios kalbos užklausas
6. **Užtikrinti duomenų saugumą** su vaidmenimis pagrįsta prieigos kontrole

### Techniniai reikalavimai

MCP serveris turi suteikti:

- **Daugiabučių duomenų prieigą**, kur parduotuvių vadovai mato tik savo parduotuvės duomenis
- **Lankstų užklausų vykdymą**, palaikant sudėtingas SQL operacijas
- **Semantinę paiešką** produktų atradimui ir rekomendacijoms
- **Duomenis realiuoju laiku**, atspindinčius dabartinę verslo būklę
- **Saugų autentifikavimą** su eilutės lygio saugumu
- **Mastelio požiūriu efektyvią architektūrą**, palaikančią kelis vartotojus vienu metu

## 🏗️ MCP serverio architektūros apžvalga

Mūsų MCP serveris įgyvendina sluoksniuotą architektūrą, optimizuotą duomenų bazės integracijai:

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

### Pagrindiniai komponentai

#### **1. MCP serverio sluoksnis**
- **FastMCP Framework**: Moderni Python MCP serverio įgyvendinimo sistema
- **Įrankių registracija**: Deklaratyvūs įrankių apibrėžimai su tipų saugumu
- **Užklausos kontekstas**: Vartotojo tapatybė ir sesijos valdymas
- **Klaidų tvarkymas**: Patikimas klaidų valdymas ir registravimas

#### **2. Duomenų bazės integracijos sluoksnis**
- **Jungčių valdymas**: Efektyvus asyncpg jungčių valdymas
- **Schemos tiekėjas**: Dinaminis lentelių schemos atradimas
- **Užklausų vykdytojas**: Saugus SQL vykdymas su RLS kontekstu
- **Sandorių valdymas**: ACID atitiktis ir atšaukimo tvarkymas

#### **3. Saugumo sluoksnis**
- **Eilutės lygio saugumas**: PostgreSQL RLS daugiabučių duomenų izoliacijai
- **Vartotojo tapatybė**: Parduotuvės vadovo autentifikavimas ir autorizacija
- **Prieigos kontrolė**: Smulkiai detalizuoti leidimai ir audito pėdsakai
- **Įvesties validacija**: SQL injekcijų prevencija ir užklausų validacija

#### **4. AI patobulinimo sluoksnis**
- **Semantinė paieška**: Vektoriniai įterpimai produktų atradimui
- **Azure OpenAI integracija**: Teksto įterpimų generavimas
- **Panašumo algoritmai**: pgvector kosininio panašumo paieška
- **Paieškos optimizavimas**: Indeksavimas ir našumo gerinimas

## 🔧 Technologijų rinkinys

### Pagrindinės technologijos

| **Komponentas** | **Technologija** | **Paskirtis** |
|------------------|------------------|---------------|
| **MCP Framework** | FastMCP (Python) | Moderni MCP serverio įgyvendinimo sistema |
| **Duomenų bazė** | PostgreSQL 17 + pgvector | Reliaciniai duomenys su vektorine paieška |
| **AI paslaugos** | Azure OpenAI | Teksto įterpimai ir kalbos modeliai |
| **Konteinerizacija** | Docker + Docker Compose | Kūrimo aplinka |
| **Debesų platforma** | Microsoft Azure | Gamybos diegimas |
| **IDE integracija** | VS Code | AI pokalbiai ir kūrimo darbo eiga |

### Kūrimo įrankiai

| **Įrankis** | **Paskirtis** |
|-------------|--------------|
| **asyncpg** | Aukštos našumo PostgreSQL tvarkyklė |
| **Pydantic** | Duomenų validacija ir serializacija |
| **Azure SDK** | Debesų paslaugų integracija |
| **pytest** | Testavimo sistema |
| **Docker** | Konteinerizacija ir diegimas |

### Gamybos rinkinys

| **Paslauga** | **Azure resursas** | **Paskirtis** |
|--------------|--------------------|---------------|
| **Duomenų bazė** | Azure Database for PostgreSQL | Valdoma duomenų bazės paslauga |
| **Konteineris** | Azure Container Apps | Serverless konteinerių talpinimas |
| **AI paslaugos** | Azure AI Foundry | OpenAI modeliai ir galiniai taškai |
| **Stebėjimas** | Application Insights | Stebėjimas ir diagnostika |
| **Saugumas** | Azure Key Vault | Slaptų duomenų ir konfigūracijos valdymas |

## 🎬 Realūs naudojimo scenarijai

Pažvelkime, kaip skirtingi vartotojai sąveikauja su mūsų MCP serveriu:

### Scenarijus 1: Parduotuvės vadovo veiklos peržiūra

**Vartotojas**: Sarah, Sietlo parduotuvės vadovė  
**Tikslas**: Analizuoti praėjusio ketvirčio pardavimų rezultatus

**Natūralios kalbos užklausa**:
> "Parodykite 10 geriausių produktų pagal pajamas mano parduotuvėje 2024 m. IV ketvirtyje"

**Kas vyksta**:
1. VS Code AI pokalbis siunčia užklausą MCP serveriui
2. MCP serveris identifikuoja Sarah parduotuvės kontekstą (Sietlas)
3. RLS politika filtruoja duomenis tik Sietlo parduotuvei
4. SQL užklausa generuojama ir vykdoma
5. Rezultatai formatuojami ir grąžinami AI pokalbiui
6. AI pateikia analizę ir įžvalgas

### Scenarijus 2: Produktų atradimas su semantine paieška

**Vartotojas**: Mike, inventoriaus vadovas  
**Tikslas**: Rasti produktus, panašius į kliento užklausą

**Natūralios kalbos užklausa**:
> "Kokius produktus mes parduodame, kurie yra panašūs į 'vandeniui atsparius elektros jungiklius lauko naudojimui'?"

**Kas vyksta**:
1. Užklausa apdorojama semantinės paieškos įrankiu
2. Azure OpenAI generuoja įterpimo vektorių
3. pgvector atlieka panašumo paiešką
4. Susiję produktai reitinguojami pagal aktualumą
5. Rezultatai apima produktų detales ir prieinamumą
6. AI siūlo alternatyvas ir komplektavimo galimybes

### Scenarijus 3: Kryžminė parduotuvių analizė

**Vartotojas**: Jennifer, regioninė vadovė  
**Tikslas**: Palyginti pardavimus pagal kategorijas visose parduotuvėse

**Natūralios kalbos užklausa**:
> "Palyginkite pardavimus pagal kategorijas visose parduotuvėse per pastaruosius 6 mėnesius"

**Kas vyksta**:
1. RLS kontekstas nustatomas regioninės vadovės prieigai
2. Generuojama sudėtinga daugiabučių parduotuvių užklausa
3. Duomenys agreguojami visose parduotuvių vietose
4. Rezultatai apima tendencijas ir palyginimus
5. AI identifikuoja įžvalgas ir rekomendacijas

## 🔒 Saugumas ir daugiabučių duomenų prieiga

Mūsų įgyvendinimas prioritetą teikia įmonės lygio saugumui:

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
- **Parduotuvės vadovo ID**: Unikalus identifikatorius RLS kontekstui
- **Vaidmenų priskyrimas**: Leidimai ir prieigos lygiai
- **Sesijos valdymas**: Saugūs autentifikavimo žetonai
- **Audito registravimas**: Pilna prieigos istorija

### Duomenų apsauga

Kelios saugumo sluoksniai:
- **Jungties šifravimas**: TLS visoms duomenų bazės jungtims
- **SQL injekcijų prevencija**: Tik parametrizuotos užklausos
- **Įvesties validacija**: Išsami užklausų validacija
- **Klaidų tvarkymas**: Jokių jautrių duomenų klaidų pranešimuose

## 🎯 Pagrindinės išvados

Baigę šį įvadą, turėtumėte suprasti:

✅ **MCP vertės pasiūlymą**: Kaip MCP sujungia AI asistentus ir realaus pasaulio duomenis  
✅ **Verslo kontekstą**: Zava Retail reikalavimus ir iššūkius  
✅ **Architektūros apžvalgą**: Pagrindinius komponentus ir jų sąveiką  
✅ **Technologijų rinkinį**: Naudotus įrankius ir sistemas  
✅ **Saugumo modelį**: Daugiabučių duomenų prieigą ir apsaugą  
✅ **Naudojimo modelius**: Realūs užklausų scenarijai ir darbo procesai  

## 🚀 Kas toliau

Pasiruošę gilintis? Tęskite su:

**[Lab 01: Pagrindinės architektūros sąvokos](../01-Architecture/README.md)**

Sužinokite apie MCP serverio architektūros modelius, duomenų bazės projektavimo principus ir išsamią techninę įgyvendinimą, kuris palaiko mūsų mažmeninės prekybos analitikos sprendimą.

## 📚 Papildomi ištekliai

### MCP dokumentacija
- [MCP specifikacija](https://modelcontextprotocol.io/docs/) - Oficialus protokolo dokumentas
- [MCP pradedantiesiems](https://aka.ms/mcp-for-beginners) - Išsamus MCP mokymosi vadovas
- [FastMCP dokumentacija](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentacija

### Duomenų bazės integracija
- [PostgreSQL dokumentacija](https://www.postgresql.org/docs/) - Pilnas PostgreSQL vadovas
- [pgvector vadovas](https://github.com/pgvector/pgvector) - Vektorinės plėtinio dokumentacija
- [Eilutės lygio saugumas](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS vadovas

### Azure paslaugos
- [Azure OpenAI dokumentacija](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI paslaugų integracija
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Valdoma duomenų bazės paslauga
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless konteineriai

---

**Atsakomybės apribojimas**: Tai mokymosi užduotis, naudojant fiktyvius mažmeninės prekybos duomenis. Visada laikykitės savo organizacijos duomenų valdymo ir saugumo politikos, įgyvendindami panaš

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.