# Sissejuhatus MCP andmebaasi integreerimisse

## 🎯 Mida see labor hõlmab

See sissejuhatav labor annab põhjaliku ülevaate Model Context Protocol (MCP) serverite loomisest koos andmebaasi integreerimisega. Saate aru ärijuhtumist, tehnilisest arhitektuurist ja reaalsetest rakendustest, kasutades Zava Retaili analüütika näidet aadressil https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Ülevaade

**Model Context Protocol (MCP)** võimaldab AI-assistentidel turvaliselt ja reaalajas suhelda väliste andmeallikatega. Koos andmebaasi integreerimisega avab MCP võimsad võimalused andmepõhiste AI-rakenduste jaoks.

See õppeprogramm õpetab, kuidas luua tootmiskõlblikke MCP servereid, mis ühendavad AI-assistendid jaemüügi müügiandmetega PostgreSQL-i kaudu, rakendades ettevõtte tasemel mustreid nagu rea taseme turvalisus, semantiline otsing ja mitme rentniku andmejuurdepääs.

## Õpieesmärgid

Selle labori lõpuks suudate:

- **Määratleda** Model Context Protocol ja selle peamised eelised andmebaasi integreerimisel
- **Tuvastada** MCP serveri arhitektuuri põhikomponendid koos andmebaasidega
- **Mõista** Zava Retaili kasutusjuhtumit ja selle ärinõudeid
- **Tunda ära** ettevõtte mustrid turvaliseks ja skaleeritavaks andmebaasi juurdepääsuks
- **Loetleda** tööriistad ja tehnoloogiad, mida selles õppeprogrammis kasutatakse

## 🧭 Väljakutse: AI kohtub pärismaailma andmetega

### Traditsioonilise AI piirangud

Kaasaegsed AI-assistendid on uskumatult võimsad, kuid neil on olulisi piiranguid pärismaailma äriliste andmetega töötamisel:

| **Väljakutse** | **Kirjeldus** | **Äriline mõju** |
|----------------|---------------|------------------|
| **Staatilised teadmised** | AI-mudelid, mis on treenitud fikseeritud andmekogumite põhjal, ei pääse ligi ajakohastele ärilistele andmetele | Aegunud teadmised, kasutamata võimalused |
| **Andmesilod** | Andmed on lukustatud andmebaasidesse, API-desse ja süsteemidesse, millele AI ei pääse ligi | Mittetäielik analüüs, killustatud töövood |
| **Turvapiirangud** | Otsene juurdepääs andmebaasidele tekitab turva- ja vastavusprobleeme | Piiratud kasutuselevõtt, käsitsi andmete ettevalmistamine |
| **Keerulised päringud** | Ärikasutajad vajavad tehnilisi teadmisi, et andmetest ülevaateid saada | Vähenenud kasutuselevõtt, ebaefektiivsed protsessid |

### MCP lahendus

Model Context Protocol lahendab need väljakutsed, pakkudes:

- **Reaalajas andmejuurdepääsu**: AI-assistendid saavad päringuid teha otse andmebaasidesse ja API-desse
- **Turvalist integreerimist**: Kontrollitud juurdepääs autentimise ja õigustega
- **Looduskeele liidest**: Ärikasutajad saavad esitada küsimusi lihtsas inglise keeles
- **Standardiseeritud protokolli**: Töötab erinevate AI-platvormide ja tööriistadega

## 🏪 Tutvuge Zava Retailiga: meie õppejuhtum https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Selle õppeprogrammi jooksul loome MCP serveri **Zava Retailile**, väljamõeldud isetegemise jaemüügiketile, millel on mitu kauplust. See realistlik stsenaarium demonstreerib ettevõtte tasemel MCP rakendust.

### Äriline kontekst

**Zava Retail** haldab:
- **8 füüsilist kauplust** Washingtoni osariigis (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 veebipoodi** e-kaubanduse müügiks
- **Mitmekesist tootekataloogi**, mis sisaldab tööriistu, ehitusmaterjale, aiatarbeid ja ehitusmaterjale
- **Mitmetasandilist juhtimist** kaupluse juhtide, piirkonnajuhtide ja juhtkonnaga

### Ärinõuded

Kaupluse juhid ja juhid vajavad AI-põhiseid analüüse, et:

1. **Analüüsida müügitulemusi** kaupluste ja ajaperioodide lõikes
2. **Jälgida laoseisu** ja tuvastada täiendamise vajadusi
3. **Mõista klientide käitumist** ja ostumustreid
4. **Avastada tooteid** semantilise otsingu abil
5. **Luua aruandeid** looduskeele päringutega
6. **Tagada andmete turvalisus** rollipõhise juurdepääsukontrolliga

### Tehnilised nõuded

MCP server peab pakkuma:

- **Mitme rentniku andmejuurdepääsu**, kus kaupluse juhid näevad ainult oma kaupluse andmeid
- **Paindlikke päringuid**, mis toetavad keerukaid SQL-operatsioone
- **Semantilist otsingut** toodete avastamiseks ja soovitusteks
- **Reaalajas andmeid**, mis kajastavad praegust äriseisundit
- **Turvalist autentimist** rea taseme turvalisusega
- **Skaleeritavat arhitektuuri**, mis toetab mitut samaaegset kasutajat

## 🏗️ MCP serveri arhitektuuri ülevaade

Meie MCP server rakendab kihilist arhitektuuri, mis on optimeeritud andmebaasi integreerimiseks:

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

### Põhikomponendid

#### **1. MCP serveri kiht**
- **FastMCP raamistik**: Kaasaegne Pythonil põhinev MCP serveri rakendus
- **Tööriistade registreerimine**: Deklaratiivsed tööriistade määratlused tüübikindlusega
- **Päringu kontekst**: Kasutaja identiteedi ja seansi haldamine
- **Vigade käsitlemine**: Tugev vigade haldamine ja logimine

#### **2. Andmebaasi integreerimise kiht**
- **Ühenduste haldamine**: Tõhus asyncpg ühenduste haldamine
- **Skeemi pakkuja**: Dünaamiline tabeliskeemide avastamine
- **Päringu täitja**: Turvaline SQL-i täitmine RLS kontekstis
- **Tehingute haldamine**: ACID-ühilduvus ja tagasipööramise käsitlemine

#### **3. Turvakiht**
- **Rea taseme turvalisus**: PostgreSQL RLS mitme rentniku andmete isoleerimiseks
- **Kasutaja identiteet**: Kaupluse juhtide autentimine ja autoriseerimine
- **Juurdepääsukontroll**: Peeneteralised õigused ja auditeerimislogid
- **Sisendi valideerimine**: SQL-süstimise ennetamine ja päringute valideerimine

#### **4. AI täiustamise kiht**
- **Semantiline otsing**: Vektorite põhine otsing toodete avastamiseks
- **Azure OpenAI integreerimine**: Teksti vektorite genereerimine
- **Sarnasuse algoritmid**: pgvector kosinuse sarnasuse otsing
- **Otsingu optimeerimine**: Indekseerimine ja jõudluse häälestamine

## 🔧 Tehnoloogiline virn

### Põhitehnoloogiad

| **Komponent** | **Tehnoloogia** | **Eesmärk** |
|---------------|----------------|-------------|
| **MCP raamistik** | FastMCP (Python) | Kaasaegne MCP serveri rakendus |
| **Andmebaas** | PostgreSQL 17 + pgvector | Relatsioonilised andmed vektorotsinguga |
| **AI teenused** | Azure OpenAI | Teksti vektorid ja keelemudelid |
| **Konteineriseerimine** | Docker + Docker Compose | Arenduskeskkond |
| **Pilveplatvorm** | Microsoft Azure | Tootmiskeskkonna juurutamine |
| **IDE integreerimine** | VS Code | AI Chat ja arendustöövoog |

### Arendustööriistad

| **Tööriist** | **Eesmärk** |
|-------------|-------------|
| **asyncpg** | Kõrge jõudlusega PostgreSQL draiver |
| **Pydantic** | Andmete valideerimine ja serialiseerimine |
| **Azure SDK** | Pilveteenuste integreerimine |
| **pytest** | Testimise raamistik |
| **Docker** | Konteineriseerimine ja juurutamine |

### Tootmisvirn

| **Teenused** | **Azure'i ressurss** | **Eesmärk** |
|--------------|---------------------|-------------|
| **Andmebaas** | Azure Database for PostgreSQL | Hallatud andmebaasi teenus |
| **Konteiner** | Azure Container Apps | Serverless konteinerite majutamine |
| **AI teenused** | Azure AI Foundry | OpenAI mudelid ja lõpp-punktid |
| **Jälgimine** | Application Insights | Jälgitavus ja diagnostika |
| **Turvalisus** | Azure Key Vault | Salasõnade ja konfiguratsiooni haldamine |

## 🎬 Reaalsed kasutusstsenaariumid

Vaatame, kuidas erinevad kasutajad meie MCP serveriga suhtlevad:

### Stsenaarium 1: Kaupluse juhi tulemuslikkuse ülevaade

**Kasutaja**: Sarah, Seattle'i kaupluse juht  
**Eesmärk**: Analüüsida eelmise kvartali müügitulemusi

**Looduskeele päring**:
> "Näita mulle minu kaupluse 10 enim tulu toonud toodet 2024. aasta IV kvartalis"

**Mis juhtub**:
1. VS Code AI Chat saadab päringu MCP serverile
2. MCP server tuvastab Sarah' kaupluse konteksti (Seattle)
3. RLS-poliitikad filtreerivad andmed ainult Seattle'i kauplusele
4. SQL-päring luuakse ja täidetakse
5. Tulemused vormindatakse ja tagastatakse AI Chatile
6. AI pakub analüüsi ja ülevaateid

### Stsenaarium 2: Toodete avastamine semantilise otsinguga

**Kasutaja**: Mike, laojuhataja  
**Eesmärk**: Leida tooteid, mis sarnanevad kliendi sooviga

**Looduskeele päring**:
> "Milliseid tooteid müüme, mis sarnanevad 'veekindlate elektriliste ühendustega välitingimustes kasutamiseks'?"

**Mis juhtub**:
1. Päring töödeldakse semantilise otsingu tööriistaga
2. Azure OpenAI genereerib vektori
3. pgvector teostab sarnasuse otsingu
4. Seotud tooted järjestatakse asjakohasuse järgi
5. Tulemused sisaldavad toote üksikasju ja saadavust
6. AI soovitab alternatiive ja komplekteerimisvõimalusi

### Stsenaarium 3: Kauplustevaheline analüüs

**Kasutaja**: Jennifer, piirkonnajuht  
**Eesmärk**: Võrrelda müüki kõigis kauplustes

**Looduskeele päring**:
> "Võrdle müüki kategooriate kaupa kõigis kauplustes viimase 6 kuu jooksul"

**Mis juhtub**:
1. RLS-kontekst määratakse piirkonnajuhi juurdepääsuks
2. Luua keeruline mitme kaupluse päring
3. Andmed koondatakse kaupluste lõikes
4. Tulemused sisaldavad trende ja võrdlusi
5. AI tuvastab ülevaated ja soovitused

## 🔒 Turvalisus ja mitme rentniku lahendused

Meie rakendus seab esikohale ettevõtte tasemel turvalisuse:

### Rea taseme turvalisus (RLS)

PostgreSQL RLS tagab andmete isoleerimise:

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

### Kasutaja identiteedi haldamine

Iga MCP ühendus sisaldab:
- **Kaupluse juhi ID**: Unikaalne identifikaator RLS konteksti jaoks
- **Rollide määramine**: Õigused ja juurdepääsutasemed
- **Seansi haldamine**: Turvalised autentimistokenid
- **Auditeerimislogid**: Täielik juurdepääsu ajalugu

### Andmekaitse

Mitmekihiline turvalisus:
- **Ühenduse krüpteerimine**: TLS kõigi andmebaasiühenduste jaoks
- **SQL-süstimise ennetamine**: Ainult parameetritega päringud
- **Sisendi valideerimine**: Päringute põhjalik valideerimine
- **Vigade käsitlemine**: Tundlikke andmeid ei kuvata veateadetes

## 🎯 Peamised järeldused

Pärast selle sissejuhatuse läbimist peaksite mõistma:

✅ **MCP väärtuspakkumine**: Kuidas MCP ühendab AI-assistendid ja pärismaailma andmed  
✅ **Äriline kontekst**: Zava Retaili nõuded ja väljakutsed  
✅ **Arhitektuuri ülevaade**: Põhikomponendid ja nende omavaheline seos  
✅ **Tehnoloogiline virn**: Tööriistad ja raamistikud, mida kasutatakse  
✅ **Turvamudel**: Mitme rentniku andmejuurdepääs ja kaitse  
✅ **Kasutusmustrid**: Reaalsed päringustsenaariumid ja töövood  

## 🚀 Mis edasi?

Valmis sügavamale sukelduma? Jätkake:

**[Labor 01: Põhiarhitektuuri kontseptsioonid](../01-Architecture/README.md)**

Õppige tundma MCP serveri arhitektuuri mustreid, andmebaasi disaini põhimõtteid ja üksikasjalikku tehnilist rakendust, mis toetab meie jaemüügi analüütika lahendust.

## 📚 Lisamaterjalid

### MCP dokumentatsioon
- [MCP spetsifikatsioon](https://modelcontextprotocol.io/docs/) - Ametlik protokolli dokumentatsioon
- [MCP algajatele](https://aka.ms/mcp-for-beginners) - Põhjalik MCP õppejuhend
- [FastMCP dokumentatsioon](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentatsioon

### Andmebaasi integreerimine
- [PostgreSQL dokumentatsioon](https://www.postgresql.org/docs/) - Täielik PostgreSQL viide
- [pgvector juhend](https://github.com/pgvector/pgvector) - Vektori laienduse dokumentatsioon
- [Rea taseme turvalisus](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS juhend

### Azure'i teenused
- [Azure OpenAI dokumentatsioon](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-teenuste integreerimine
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Hallatud andmebaasi teenus
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless konteinerid

---

**Vastutusest loobumine**: See on õppematerjal, mis kasutab väljamõeldud jaemüügi andmeid. Sarnaste lahenduste rakendamisel tootmiskeskkonnas järgige alati oma organisatsiooni andmehalduse ja turvalisuse poliitikaid.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.