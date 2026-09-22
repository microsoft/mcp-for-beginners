# Sissejuhatus MCP andmebaasi integratsiooni

> [!NOTE]
> Selle õppeprogrammi diagrammid või kood, mis kasutab HTTP/SSE või initsialiseerimisvalikuid,
> kajastavad MCP `2025-11-25` sõltuvusi näidises. Uute
> rakenduste puhul kasutage `2026-07-28`-i seisundivabu päringuid ja voogedastatavat HTTP-d.

## 🎯 Mida see labor katab

See sissejuhatav labor annab põhjaliku ülevaate Model Context Protocol (MCP) serverite ehitamisest andmebaasi integratsiooniga. Saate aru äriülesandest, tehnilisest arhitektuurist ja reaalsest kasutusjuhtumist Zava Retail analüütilise näite kaudu aadressil https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Ülevaade

**Model Context Protocol (MCP)** võimaldab tehisintellekti assistentidel turvaliselt reaalajas juurde pääseda ja suhelda väliste andmeallikatega. Koos andmebaasi integratsiooniga avab MCP võimsad võimalused andmepõhistele tehisintellekti rakendustele.

See õppeprogramm õpetab ehitama tootmiseks valmis MCP servereid, mis ühendavad tehisintellekti assistendid jaemüügi müügiandmetega PostgreSQL-i kaudu, rakendades ettevõtte mustreid nagu ridade taseme turvalisus, semantiline otsing ja mitme kasutajaga andmetele ligipääs.

## Õpipõhjused

Selle labori lõpuks oskad:

- **Defineeri** Model Context Protocol ja selle põhieelised andmebaasi integratsioonis
- **Tuvasta** MCP serveri arhitektuuri põhikomponendid andmebaasidega
- **Saa aru** Zava Retail kasutusjuhtumist ja selle ärivajadustest
- **Tunne ära** ettevõtte mustrid turvaliseks, skaleeritavaks andmebaasi ligipääsuks
- **Loetle** tööriistad ja tehnoloogiad, mida kogu õppeprogrammis kasutatakse

## 🧭 Väljakutse: AI kohtub reaalse maailma andmetega

### Traditsioonilised AI piirangud

Tänapäeva AI assistendid on väga võimsad, kuid neil on olulisi piiranguid, kui nad töötavad reaalse ärimaailma andmetega:

| **Väljakutse** | **Kirjeldus** | **Äriprost mõjud** |
|---------------|-----------------|-------------------|
| **Staatiline teadmine** | AI mudelid, mis on treenitud fikseeritud andmestikel, ei pääse juurde praegustele ärandmetele | Aegunud teadmised, kasutamata võimalused |
| **Andmesilod** | Informatsioon on lukustatud andmebaasides, API-des ja süsteemides, kuhu AI ei pääse | Ebapiisav analüüs, killustunud tööprotsessid |
| **Turvapiirangud** | Otsene andmebaasi ligipääs tekitab turva- ja vastavusküsimusi | Piiratud juurutus, käsitsi andmete ettevalmistus |
| **Keerukad päringud** | Ärikasutajad vajavad tehnilisi teadmisi andmete tõmbamiseks | Vähenenud kasutuselevõtt, ebatõhusad protsessid |

### MCP lahendus

Model Context Protocol lahendab need väljakutsed, pakkudes:

- **Reaalajas andmetele ligipääs**: AI assistendid esitavad päringuid otse andmebaasidesse ja API-desse
- **Turvaline integratsioon**: Kontrollitud ligipääs autentimise ja õigustega
- **Loomuliku keele liides**: Ärikasutajad esitavad küsimusi lihtsas inglise keeles
- **Standardiseeritud protokoll**: Töötleb erinevaid AI platvorme ja tööriistu

## 🏪 Tutvuge Zava Retailiga: meie õppe juhtumiuuring https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Selle õppeprogrammi jooksul ehitame MCP serveri **Zava Retailile**, väljamõeldud ehitusmaterjalide jaemüügikettile mitme poe asukohaga. See realistlik stsenaarium demonstreerib ettevõtte tasemel MCP rakendust.

### Ärikontext

**Zava Retail** haldab:
- **8 füüsilist poodi** Washingtoni osariigis (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 veebipood** e-kaubanduse jaoks
- **Mitmekesine tootekataloog**, mis sisaldab tööriistu, riistvara, aedade tarvikuid ja ehitusmaterjale
- **Mitmetasandiline juhtimine** poodide juhid, piirkondlikud juhid ja juhatus

### Ärinõuded

Poejuhid ja juhid vajavad AI-põhist analüütikat, et:

1. **Analüüsida müügitulemusi** poodide ja ajaperioodide lõikes
2. **Jälgida laoseisusid** ja tuvastada täiendamisvajadusi
3. **Mõista kliendikäitumist** ja ostumustreid
4. **Avastada tooteinfo** semantilise otsingu kaudu
5. **Koostada aruandeid** loomulikus keeles esitatud päringutega
6. **Hooldada andmeturvet** rollipõhise ligipääsukontrolliga

### Tehnilised nõuded

MCP server peab pakkuma:

- **Mitme kasutaja andmepõhine ligipääs** – poe juhid näevad ainult oma poe andmeid
- **Paindlikud päringud**, mis toetavad keerukaid SQL operatsioone
- **Semantiline otsing** toodete leidmiseks ja soovitusteks
- **Reaalajas andmed**, mis peegeldavad praegust äriolukorda
- **Turvaline autentimine** ridade taseme turvalisuse (RLS) abil
- **Skaleeritav arhitektuur** mitme samaaegse kasutaja toetuseks

## 🏗️ MCP serveri arhitektuuri ülevaade

Meie MCP server realiseerib kihilise arhitektuuri, mis on optimeeritud andmebaasi integratsiooniks:

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

### Peamised komponendid

#### **1. MCP serveri kiht**
- **FastMCP raamistik**: kaasaegne Python MCP serveri rakendus
- **Tööriistade registreerimine**: deklaratiivsed tööriistade definitsioonid tüübikindlusega
- **Päringu kontekst**: kasutaja identiteet ja sessiooni haldus
- **Vea haldus**: vastupidav veahaldus ja logimine

#### **2. Andmebaasi integratsioonikiht**
- **Ühenduse puhvrite haldus**: efektiivne asyncpg ühenduste haldus
- **Skeemi pakkuja**: dünaamiline tabeliskeemi avastamine
- **Päringute täitja**: turvaline SQL täideviimine RLS kontekstiga
- **Tehingute haldus**: ACID-i kooskõla ja tühistamise haldus

#### **3. Turvakiht**
- **Ridade taseme turvalisus**: PostgreSQL RLS mitme kasutajaga andmete isoleerimiseks
- **Kasutaja identiteet**: poejuhi autentimine ja autoriseerimine
- **Ligipääsukontroll**: detailsete õiguste ja auditeerimise logid
- **Sisendi valideerimine**: SQL süstimise ennetamine ja päringute valideerimine

#### **4. AI täienduskiht**
- **Semantiline otsing**: vektorpõhised manused toodete leidmiseks
- **Azure OpenAI integratsioon**: tekstimanuste genereerimine
- **Sarnasuse algoritmid**: pgvector kosinussarnasuse otsing
- **Otsingu optimeerimine**: indekseerimine ja jõudluse häälestus

## 🔧 Tehnoloogia virn

### Põhitehnoloogiad

| **Komponent** | **Tehnoloogia** | **Eesmärk** |
|---------------|----------------|-------------|
| **MCP raamistik** | FastMCP (Python) | Kaasaegne MCP serveri rakendus |
| **Andmebaas** | PostgreSQL 17 + pgvector | Relatsiooniline andmebaas koos vektorotsinguga |
| **AI teenused** | Azure OpenAI | Tekstimanused ja keelemudelid |
| **Konteinerimine** | Docker + Docker Compose | Arenduskeskkond |
| **Pilveplatvorm** | Microsoft Azure | Tootmisjuurutus |
| **IDE integratsioon** | VS Code | AI vestlus ja arendusvoog |

### Arendustööriistad

| **Tööriist** | **Eesmärk** |
|----------|-------------|
| **asyncpg** | Kõrge jõudlusega PostgreSQL draiver |
| **Pydantic** | Andmete valideerimine ja serialiseerimine |
| **Azure SDK** | Pilveteenuste integratsioon |
| **pytest** | Testimiskeskkond |
| **Docker** | Konteinerimine ja juurutus |

### Tootmisvirn

| **Teenuse** | **Azure ressurss** | **Eesmärk** |
|-------------|-------------------|-------------|
| **Andmebaas** | Azure Database for PostgreSQL | Hallatav andmebaasiteenus |
| **Konteiner** | Azure Container Apps | Serverivaba konteineri majutamine |
| **AI teenused** | Microsoft Foundry | OpenAI mudelid ja lõpp-punktid |
| **Jälgimine** | Application Insights | Seiresüsteem ja diagnostika |
| **Turvalisus** | Azure Key Vault | Saladuste ja konfiguratsiooni haldus |

## 🎬 Reaalse maailma kasutusstsenaariumid

Vaatame, kuidas erinevad kasutajad meie MCP serveriga suhtlevad:

### Stsenaarium 1: Poejuhi tulemuslikkuse ülevaade

**Kasutaja**: Sarah, Seattle poejuht  
**Eesmärk**: Analüüsida eelmise kvartali müügitulemusi

**Loomuliku keele päring**:
> "Näita mulle minu poe 10 enim tulu toonud toodet 2024. aasta 4. kvartalis"

**Mis juhtub**:
1. VS Code AI Chat saadab päringu MCP serverile
2. MCP server tuvastab Sarah poe konteksti (Seattle)
3. RLS-poliitikad filtreerivad andmed ainult Seattle poe jaoks
4. SQL päring genereeritakse ja täidetakse
5. Tulemused vormindatakse ja tagastatakse AI vestlusele
6. AI pakub analüüsi ja arusaamu

### Stsenaarium 2: Toote avastamine semantilise otsinguga

**Kasutaja**: Mike, laohaldur  
**Eesmärk**: Leida tooted, mis sarnanevad kliendi päringuga

**Loomuliku keele päring**:
> "Milliseid tooteid me müüme, mis on sarnased „veekindlatele välitingimustes kasutatavateelektriühendustele“?"

**Mis juhtub**:
1. Päring töödeldakse semantilise otsingu tööriistaga
2. Azure OpenAI genereerib manuste vektori
3. pgvector teostab sarnasuse otsingu
4. Seotud tooted järjestatakse asjakohasuse alusel
5. Tulemused sisaldavad toodete detaile ja saadavust
6. AI soovitab alternatiive ja komplekteerimisvõimalusi

### Stsenaarium 3: Poeketiülene analüüs

**Kasutaja**: Jennifer, piirkondlik juht  
**Eesmärk**: Võrrelda kõigi poodide tulemuslikkust

**Loomuliku keele päring**:
> "Võrdle müüki kategooriate kaupa kõikides poodides viimase 6 kuu jooksul"

**Mis juhtub**:
1. RLS kontekst seatakse piirkondliku juhi ligipääsuks
2. Genereeritakse keerukas mitme poe päring
3. Andmeid koondatakse poodide asukohtade lõikes
4. Tulemused sisaldavad trende ja võrdlusi
5. AI tuvastab arusaamu ja soovitusi

## 🔒 Turvalisus ja mitme kasutajaga süvitsi minek

Meie rakendus seab esikohale ettevõtte tasemel turvalisuse:

### Ridade taseme turvalisus (RLS)

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

### Kasutaja identiteedi haldus

Iga MCP ühendus sisaldab:
- **Poejuhi ID**: ainulaadne identifikaator RLS konteksti jaoks
- **Rolli määramine**: õigused ja ligipääsutasemed
- **Sessioonihaldus**: turvalised autentimismärgid
- **Auditi logimine**: täielik ligipääsu ajalugu

### Andmekaitse

Mitmekihiline turvalisus:
- **Ühenduse krüptimine**: TLS kõigi andmebaasi ühenduste jaoks
- **SQL süstimise ennetamine**: ainult parameetriseeritud päringud
- **Sisendi valideerimine**: põhjalik päringute valideerimine
- **Veahaldus**: veateadetes ei kuvata tundlikku infot

## 🎯 Peamised järeldused

Pärast selle sissejuhatuse läbimist peaksid saama aru:

✅ **MCP väärtuspakkumine**: kuidas MCP ühendab AI assistendid ja reaalse maailma andmed  
✅ **Ärikontext**: Zava Retaili nõuded ja väljakutsed  
✅ **Arhitektuuri ülevaade**: põhikomponendid ja nende omavaheline koostöö  
✅ **Tehnoloogia virn**: selles õppeprogrammis kasutatud tööriistad ja raamistikud  
✅ **Turvemudel**: mitmekasutajaliides ja andmekaitse  
✅ **Kasutusmustrid**: reaalse maailma päringu stsenaariumid ja töövood  

## 🚀 Mis edasi

Valmis süvitsi minema? Jätka:

**[Labor 01: Põhiarhitektuuri kontseptsioonid](../01-Architecture/README.md)**

Õpi MCP serveri arhitektuuri mustreid, andmebaasi disaini põhimõtteid ja üksikasjalikku tehnilist rakendust, mis toidab meie jaemüügianalüüsi lahendust.

## 📚 Täiendavad ressursid

### MCP dokumentatsioon
- [MCP spetsifikatsioon](https://modelcontextprotocol.io/docs/) - ametlik protokolli dokumentatsioon
- [MCP alustajatele](https://aka.ms/mcp-for-beginners) - põhjalik MCP õppematerjal
- [FastMCP dokumentatsioon](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentatsioon

### Andmebaasi integratsioon
- [PostgreSQL dokumentatsioon](https://www.postgresql.org/docs/) - täielik PostgreSQL viitejuhend
- [pgvector juhend](https://github.com/pgvector/pgvector) - Vektorextensiooni dokumentatsioon
- [Ridade taseme turvalisus](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS juhend

### Azure teenused
- [Azure OpenAI dokumentatsioon](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI teenuse integratsioon
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - hallatav andmebaasiteenus
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - serverivabad konteinerid

---

**Selgitus**: See on õppetöö väljamõeldud jaemüügiandmete kasutamisega. Järgige alati oma organisatsiooni andmekorralduse ja turvapoliitikaid sarnaste lahenduste tootmiskeskkondades rakendamisel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->