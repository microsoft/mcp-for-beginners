# Introduktion til MCP Databaseintegration

> [!NOTE]
> Diagrammer eller kode i denne læringssti, der bruger HTTP/SSE eller initialiserings-
> muligheder, afspejler prøvens MCP `2025-11-25` afhængigheder. For nye
> implementeringer skal du bruge `2026-07-28` statsløse forespørgsler og Streamable HTTP.

## 🎯 Hvad dette lab dækker

Dette introduktionslab giver en omfattende oversigt over opbygning af Model Context Protocol (MCP) servere med databaseintegration. Du vil forstå forretningssagen, teknisk arkitektur og virkelige anvendelser gennem Zava Retail analysescenariet på https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Oversigt

**Model Context Protocol (MCP)** muliggør, at AI-assistenter sikkert kan få adgang til og interagere med eksterne datakilder i realtid. Når det kombineres med databaseintegration, åbner MCP for kraftfulde muligheder til datadrevne AI-applikationer.

Denne læringssti lærer dig at bygge produktionsklare MCP-servere, der forbinder AI-assistenter til detailhandelssalgsdata via PostgreSQL, og implementerer virksomhedsmønstre som række-niveau-sikkerhed, semantisk søgning og multi-lejer dataadgang.

## Læringsmål

Når du er færdig med dette lab, vil du kunne:

- **Definere** Model Context Protocol og dens kernefordele ved databaseintegration
- **Identificere** nøglekomponenter i en MCP-serverarkitektur med databaser
- **Forstå** Zava Retail casescenariet og dets forretningskrav
- **Genkende** virksomhedsmønstre for sikker, skalerbar databaseadgang
- **Liste** de værktøjer og teknologier, der anvendes gennem denne læringssti

## 🧭 Udfordringen: AI møder virkelige data

### Traditionelle AI-begrænsninger

Moderne AI-assistenter er utroligt kraftfulde, men står over for betydelige begrænsninger, når de arbejder med virkelige forretningsdata:

| **Udfordring** | **Beskrivelse** | **Forretningspåvirkning** |
|---------------|-----------------|-------------------------|
| **Statisk viden** | AI-modeller, der er trænet på faste datasæt, kan ikke få adgang til aktuelle forretningsdata | Forældede indsigter, mistede muligheder |
| **Datasiloer** | Information låst i databaser, API'er og systemer, som AI ikke kan nå | Ufuldstændig analyse, fragmenterede arbejdsprocesser |
| **Sikkerhedsbegrænsninger** | Direkte databaseadgang rejser sikkerheds- og overholdelsesbekymringer | Begrænset implementering, manuel datapræparation |
| **Komplekse forespørgsler** | Forretningsbrugere har brug for teknisk viden for at udtrække dataindsigter | Reduceret anvendelse, ineffektive processer |

### MCP-løsningen

Model Context Protocol adresserer disse udfordringer ved at tilbyde:

- **Realtidsdataadgang**: AI-assistenter forespørger levende databaser og API'er
- **Sikker integration**: Kontrolleret adgang med autentificering og tilladelser
- **Naturligt sproginterface**: Forretningsbrugere stiller spørgsmål på almindeligt engelsk
- **Standardiseret protokol**: Fungerer på tværs af forskellige AI-platforme og værktøjer

## 🏪 Mød Zava Retail: Vores læringscase https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Gennem denne læringssti vil vi bygge en MCP-server for **Zava Retail**, en fiktiv gør-det-selv detailkæde med flere butikslokationer. Dette realistiske scenarie demonstrerer virksomhedsklasse MCP-implementering.

### Forretningskontekst

**Zava Retail** driver:
- **8 fysiske butikker** i Washington staten (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online butik** til e-handelssalg
- **Diversificeret produktkatalog** med værktøj, hardware, haveudstyr og byggematerialer
- **Flerlags ledelse** med butikschefer, regionschefer og ledere

### Forretningskrav

Butikschefer og ledere har brug for AI-drevne analyser til at:

1. **Analysere salgspræstation** på tværs af butikker og tidsperioder
2. **Overvåge lagerniveauer** og identificere genopfyldningsbehov
3. **Forstå kundeadfærd** og købsadfærdsmønstre
4. **Opdage produktindsigter** gennem semantisk søgning
5. **Generere rapporter** med forespørgsler på naturligt sprog
6. **Opretholde datasikkerhed** med rollebaseret adgangskontrol

### Tekniske krav

MCP-serveren skal levere:

- **Multi-lejer dataadgang** hvor butikschefer kun ser deres egen butiks data
- **Fleksibel forespørgselsmulighed** der understøtter komplekse SQL-operationer
- **Semantisk søgning** til produktopdagelse og anbefalinger
- **Realtidsdata** der afspejler den aktuelle forretningsstatus
- **Sikker autentificering** med række-niveau-sikkerhed
- **Skalerbar arkitektur** der understøtter flere samtidige brugere

## 🏗️ Oversigt over MCP-serverarkitektur

Vores MCP-server implementerer en lagdelt arkitektur optimeret til databaseintegration:

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

### Centrale komponenter

#### **1. MCP Serverlag**
- **FastMCP Framework**: Moderne Python MCP-serverimplementering
- **Værktøjsregistrering**: Deklarative værktøjsdefinitioner med typesikkerhed
- **Forespørgselskontekst**: Brugeridentitet og sessionsstyring
- **Fejlhåndtering**: Robust fejlstyring og logning

#### **2. Databaseintegrationslag**
- **Forbindelsespulje**: Effektiv asyncpg-forbindelsesstyring
- **Skemaleverandør**: Dynamisk opdagelse af tabelskema
- **Forespørgselsudfører**: Sikker SQL-eksekvering med RLS-kontekst
- **Transaktionsstyring**: ACID-overholdelse og rollback-håndtering

#### **3. Sikkerhedslag**
- **Række-niveau-sikkerhed**: PostgreSQL RLS til multi-lejer dataisolering
- **Brugeridentitet**: Butikschefens autentificering og autorisering
- **Adgangskontrol**: Finkornede tilladelser og revisionsspor
- **Inputvalidering**: Forebyggelse af SQL-injektion og forespørgselsvalidering

#### **4. AI-forbedringslag**
- **Semantisk søgning**: Vektorindlejringer til produktopdagelse
- **Azure OpenAI-integration**: Tekstindlejringsgenerering
- **Lighedsalgoritmer**: pgvector cosine similarity-søgning
- **Søgeoptimering**: Indeksering og ydeevnetilpasning

## 🔧 Teknologistak

### Kerne teknologier

| **Komponent** | **Teknologi** | **Formål** |
|---------------|--------------|------------|
| **MCP Framework** | FastMCP (Python) | Moderne MCP-serverimplementering |
| **Database** | PostgreSQL 17 + pgvector | Relationale data med vektorsøgning |
| **AI Tjenester** | Azure OpenAI | Tekstindlejringer og sprogmodeller |
| **Containerisering** | Docker + Docker Compose | Udviklingsmiljø |
| **Cloud-platform** | Microsoft Azure | Produktionsimplementering |
| **IDE Integration** | VS Code | AI Chat og udviklingsworkflow |

### Udviklingsværktøjer

| **Værktøj** | **Formål** |
|----------|------------|
| **asyncpg** | Højtydende PostgreSQL-driver |
| **Pydantic** | Datavalidering og serialisering |
| **Azure SDK** | Cloud-tjenesteintegration |
| **pytest** | Testframework |
| **Docker** | Containerisering og udrulning |

### Produktionsstak

| **Tjeneste** | **Azure Ressource** | **Formål** |
|-------------|-----------------|---------|
| **Database** | Azure Database for PostgreSQL | Administreret databaseservice |
| **Container** | Azure Container Apps | Serverløs container-hosting |
| **AI Tjenester** | Microsoft Foundry | OpenAI-modeller og endpoints |
| **Overvågning** | Application Insights | Observabilitet og diagnostik |
| **Sikkerhed** | Azure Key Vault | Hemmeligheder og konfigurationsstyring |

## 🎬 Virkelige brugs-scenarier

Lad os udforske, hvordan forskellige brugere interagerer med vores MCP-server:

### Scenarie 1: Butikschefens præstationsgennemgang

**Bruger**: Sarah, butikschef i Seattle  
**Mål**: Analysere sidste kvartals salgspræstation

**Forespørgsel på naturligt sprog**:
> "Vis mig de 10 bedste produkter efter omsætning for min butik i Q4 2024"

**Hvad sker der**:
1. VS Code AI Chat sender forespørgsel til MCP-serveren
2. MCP-serveren identificerer Sarahs butiks kontekst (Seattle)
3. RLS-politikker filtrerer data til kun Seattle-butikken
4. SQL-forespørgsel genereres og eksekveres
5. Resultater formateres og returneres til AI Chat
6. AI leverer analyse og indsigter

### Scenarie 2: Produktopdagelse med semantisk søgning

**Bruger**: Mike, lageransvarlig  
**Mål**: Find produkter, der ligner en kundes forespørgsel

**Forespørgsel på naturligt sprog**:
> "Hvilke produkter sælger vi, der ligner 'vandafvisende elektriske stik til udendørs brug'?"

**Hvad sker der**:
1. Forespørgsel behandles af semantisk søgeværktøj
2. Azure OpenAI genererer indlejringsvektor
3. pgvector udfører lighedsbaseret søgning
4. Relaterede produkter rangeres efter relevans
5. Resultater inkluderer produktdetaljer og tilgængelighed
6. AI foreslår alternativer og bundlingsmuligheder

### Scenarie 3: Tværs-butik analytics

**Bruger**: Jennifer, regionschef  
**Mål**: Sammenligne præstation på tværs af alle butikker

**Forespørgsel på naturligt sprog**:
> "Sammenlign salg efter kategori for alle butikker i de sidste 6 måneder"

**Hvad sker der**:
1. RLS-kontekst sættes for regionschefens adgang
2. Kompleks forespørgsel på tværs af butikker genereres
3. Data aggregeres på tværs af butikslokationer
4. Resultater inkluderer tendenser og sammenligninger
5. AI identificerer indsigter og anbefalinger

## 🔒 Sikkerhed og multi-lejer dybdegående

Vores implementering prioriterer virksomhedsklasse sikkerhed:

### Række-niveau-sikkerhed (RLS)

PostgreSQL RLS sikrer dataisolering:

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

### Brugeridentitetshåndtering

Hver MCP-forbindelse indeholder:
- **Butikschef-ID**: Unik identifikator til RLS-kontekst
- **Rolle tildeling**: Tilladelser og adgangsniveauer
- **Sessionsstyring**: Sikker autentificeringstokens
- **Revisionslog**: Komplet adgangshistorik

### Databeskyttelse

Flere sikkerhedslag:
- **Forbindelseskryptering**: TLS for alle databaseforbindelser
- **Forebyggelse af SQL-injektion**: Kun parameteriserede forespørgsler
- **Inputvalidering**: Omfattende forespørgselsvalidering
- **Fejlhåndtering**: Ingen følsomme data i fejlbemærkninger

## 🎯 Vigtige pointer

Efter at have gennemført denne introduktion, bør du forstå:

✅ **MCP værditilbud**: Hvordan MCP forbinder AI-assistenter og virkelige data  
✅ **Forretningskontekst**: Zava Retails krav og udfordringer  
✅ **Arkitekturoversigt**: Centrale komponenter og deres interaktioner  
✅ **Teknologisk stak**: Værktøjer og frameworks anvendt gennem læringsstien  
✅ **Sikkerhedsmodel**: Multi-lejer dataadgang og beskyttelse  
✅ **Brugsmønstre**: Virkelige forespørgsels-scenarier og arbejdsflows  

## 🚀 Hvad er det næste

Klar til at dykke dybere? Fortsæt med:

**[Lab 01: Kernearkitekturkoncept](../01-Architecture/README.md)**

Lær om MCP-serverarkitektur-mønstre, database designprincipper og den detaljerede tekniske implementering, der driver vores retail analytics-løsning.

## 📚 Yderligere ressourcer

### MCP Dokumentation
- [MCP Specifikation](https://modelcontextprotocol.io/docs/) - Officiel protokol dokumentation
- [MCP for begyndere](https://aka.ms/mcp-for-beginners) - Omfattende MCP læringsguide
- [FastMCP Dokumentation](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentation

### Databaseintegration
- [PostgreSQL Dokumentation](https://www.postgresql.org/docs/) - Fuldstændig PostgreSQL reference
- [pgvector Guide](https://github.com/pgvector/pgvector) - Vektorudvidelsesdokumentation
- [Række-niveau sikkerhed](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS guide

### Azure Services
- [Azure OpenAI Dokumentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI tjenesteintegration
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Administreret databaseservice
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverløse containere

---

**Ansvarsfraskrivelse**: Dette er en læringsøvelse med fiktive detaildata. Følg altid din organisations datastyrings- og sikkerhedspolitikker, når du implementerer lignende løsninger i produktionsmiljøer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->