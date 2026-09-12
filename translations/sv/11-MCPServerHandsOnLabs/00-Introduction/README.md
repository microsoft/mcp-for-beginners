# Introduktion till MCP-databasintegration

> [!NOTE]
> Diagram eller kod i denna inlärningsväg som använder HTTP/SSE eller initialiserings-
> alternativ speglar exempelns MCP `2025-11-25` beroenden. För nya
> implementationer, använd `2026-07-28` stateless-förfrågningar och Streamable HTTP.

## 🎯 Vad denna labb täcker

Denna introduktionslabb ger en omfattande översikt över att bygga Model Context Protocol (MCP) servrar med databasintegration. Du kommer att förstå affärsfall, teknisk arkitektur och verkliga tillämpningar genom Zava Retails analysfall på https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Översikt

**Model Context Protocol (MCP)** möjliggör för AI-assistenter att säkert få tillgång till och interagera med externa datakällor i realtid. I kombination med databasintegration låser MCP upp kraftfulla möjligheter för datadrivna AI-applikationer.

Denna inlärningsväg lär dig att bygga produktionsklara MCP-servrar som kopplar AI-assistenter till detaljhandelsförsäljningsdata via PostgreSQL, och implementerar företagsmönster som Row Level Security, semantisk sökning och multi-tenant datatillgång.

## Inlärningsmål

I slutet av denna labb kommer du att kunna:

- **Definiera** Model Context Protocol och dess kärnfördelar för databasintegration
- **Identifiera** nyckelkomponenter i en MCP-serverarkitektur med databaser
- **Förstå** Zava Retails användningsfall och dess affärskrav
- **Känna igen** företagsmönster för säker, skalbar databasåtkomst
- **Lista** verktyg och teknologier som används genom denna inlärningsväg

## 🧭 Utmaningen: AI möter verkliga data

### Traditionella AI-begränsningar

Moderna AI-assistenter är otroligt kraftfulla men har betydande begränsningar när de arbetar med verkliga affärsdata:

| **Utmaning** | **Beskrivning** | **Affärspåverkan** |
|---------------|-----------------|-------------------|
| **Statisk kunskap** | AI-modeller tränade på fasta datasätt kan inte komma åt aktuell affärsdata | Föråldrade insikter, missade möjligheter |
| **Data-silor** | Information låst i databaser, API:er och system som AI inte når | Ofullständig analys, fragmenterade arbetsflöden |
| **Säkerhetsbegränsningar** | Direkt databasåtkomst innebär säkerhets- och efterlevnadsproblem | Begränsad distribution, manuell datapreparering |
| **Komplexa frågor** | Affärsanvändare behöver teknisk kunskap för att utvinna datainsikter | Minskad adoption, ineffektiva processer |

### MCP-lösningen

Model Context Protocol löser dessa utmaningar genom att erbjuda:

- **Realtidsåtkomst till data**: AI-assistenter gör förfrågningar till live-databaser och API:er
- **Säker integration**: Kontrollerad åtkomst med autentisering och behörigheter
- **Naturligt språkgränssnitt**: Affärsanvändare ställer frågor på vanlig engelska
- **Standardiserat protokoll**: Fungerar över olika AI-plattformar och verktyg

## 🏪 Möt Zava Retail: Vårt inlärningsfall https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Genom denna inlärningsväg bygger vi en MCP-server för **Zava Retail**, en fiktiv gör-det-själv detaljhandelskedja med flera butikslokaler. Detta realistiska scenario demonstrerar MCP-implementering i företagsklass.

### Affärskontext

**Zava Retail** driver:
- **8 fysiska butiker** i delstaten Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 webbutik** för e-handelsförsäljning
- **Mångsidig produktkatalog** som inkluderar verktyg, byggmaterial, trädgårdsvaror och byggmaterial
- **Flerlagersledning** med butikschefer, regionchefer och ledning

### Affärskrav

Butikschefer och ledning behöver AI-driven analys för att:

1. **Analysera försäljningsprestanda** över butiker och tidsperioder
2. **Spåra lagernivåer** och identifiera påfyllnadsbehov
3. **Förstå kundbeteende** och köpmönster
4. **Upptäcka produktinsikter** via semantisk sökning
5. **Generera rapporter** med naturliga språkfrågor
6. **Bibehålla datasäkerhet** med rollbaserad åtkomstkontroll

### Tekniska krav

MCP-servern måste tillhandahålla:

- **Multi-tenant-datatillgång** där butikschefer endast ser sin butiks data
- **Flexibel frågeställning** som stödjer komplexa SQL-operationer
- **Semantisk sökning** för produktupptäckt och rekommendationer
- **Realtidsdata** som speglar nuvarande affärstillstånd
- **Säker autentisering** med row-level security
- **Skalbar arkitektur** som stödjer flera samtidiga användare

## 🏗️ Översikt över MCP-serverarkitektur

Vår MCP-server implementerar en lagerindelad arkitektur optimerad för databasintegration:

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

### Nyckelkomponenter

#### **1. MCP-serverlagret**
- **FastMCP Framework**: Modern Python-implementering av MCP-server
- **Verktygsregistrering**: Deklarativa verktygsdefinitioner med typesäkerhet
- **Förfrågningskontext**: Användaridentitet och sessionshantering
- **Felhantering**: Robust felhantering och loggning

#### **2. Databasintegrationslager**
- **Anslutningspoolning**: Effektiv asyncpg-anslutningshantering
- **Schemasupport**: Dynamisk tabellschemaupptäckt
- **Frågeexekverare**: Säker SQL-exekvering med RLS-kontext
- **Transaktionshantering**: ACID-kompatibilitet och rollback-hantering

#### **3. Säkerhetslager**
- **Row Level Security**: PostgreSQL RLS för isolering av multi-tenant-data
- **Användaridentitet**: Autentisering och auktorisation för butikschefer
- **Åtkomstkontroll**: Finmaskiga behörigheter och revisionsloggar
- **Inputvalidering**: Skydd mot SQL-injektion och validering av frågor

#### **4. AI-förbättringslager**
- **Semantisk sökning**: Vektor-embeddingar för produktupptäckt
- **Azure OpenAI-integration**: Textembeddinggenerering
- **Likhetsalgoritmer**: pgvector kosinuslikhetssökning
- **Sökningsoptimering**: Indexering och prestandaförbättringar

## 🔧 Teknikstack

### Kärnteknologier

| **Komponent** | **Teknologi** | **Syfte** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Modern MCP-serverimplementation |
| **Databas** | PostgreSQL 17 + pgvector | Relationsdata med vektorsökning |
| **AI-tjänster** | Azure OpenAI | Textembeddingar och språkmodeller |
| **Containerisering** | Docker + Docker Compose | Utvecklingsmiljö |
| **Molnplattform** | Microsoft Azure | Produktionsdrift |
| **IDE-integration** | VS Code | AI-chatt och utvecklingsarbetsflöde |

### Utvecklingsverktyg

| **Verktyg** | **Syfte** |
|----------|-------------|
| **asyncpg** | Högeffektiv PostgreSQL-drivrutin |
| **Pydantic** | Datavalidering och serialisering |
| **Azure SDK** | Molntjänsteintegration |
| **pytest** | Testningsramverk |
| **Docker** | Containerisering och distribution |

### Produktionsstack

| **Tjänst** | **Azure-resurs** | **Syfte** |
|-------------|-------------------|-------------|
| **Databas** | Azure Database for PostgreSQL | Hanterad databastjänst |
| **Container** | Azure Container Apps | Serverlös containerhosting |
| **AI-tjänster** | Microsoft Foundry | OpenAI-modeller och endpoints |
| **Övervakning** | Application Insights | Observabilitet och diagnostik |
| **Säkerhet** | Azure Key Vault | Hantering av hemligheter och konfiguration |

## 🎬 Verkliga användningsscenarier

Låt oss utforska hur olika användare interagerar med vår MCP-server:

### Scenario 1: Butikschefens prestationsgranskning

**Användare**: Sarah, butikschef i Seattle  
**Mål**: Analysera försäljningsprestanda för senaste kvartalet

**Naturlig språkfråga**:
> "Visa de 10 bäst säljande produkterna efter intäkt för min butik i Q4 2024"

**Vad som händer**:
1. VS Code AI Chat skickar förfrågan till MCP-servern
2. MCP-servern identifierar Sarahs butiks kontext (Seattle)
3. RLS-regler filtrerar data till endast Seattle-butiken
4. SQL-fråga genereras och körs
5. Resultat formateras och returneras till AI Chat
6. AI tillhandahåller analys och insikter

### Scenario 2: Produktupptäckt med semantisk sökning

**Användare**: Mike, lageransvarig  
**Mål**: Hitta produkter som liknar en kundförfrågan

**Naturlig språkfråga**:
> "Vilka produkter säljer vi som liknar 'vattentäta elektriska kontakter för utomhusbruk'?"

**Vad som händer**:
1. Fråga behandlas av verktyg för semantisk sökning
2. Azure OpenAI genererar embedding-vektor
3. pgvector utför likhetssökning
4. Relaterade produkter rankas efter relevans
5. Resultat inkluderar produktdetaljer och tillgänglighet
6. AI föreslår alternativ och paketmöjligheter

### Scenario 3: Analys över flera butiker

**Användare**: Jennifer, regionchef  
**Mål**: Jämföra prestanda över alla butiker

**Naturlig språkfråga**:
> "Jämför försäljning per kategori för alla butiker under de senaste 6 månaderna"

**Vad som händer**:
1. RLS-kontext ställs in för regionchefsåtkomst
2. Komplex flertbutiksfråga genereras
3. Data aggregeras över butikslokaler
4. Resultat inkluderar trender och jämförelser
5. AI identifierar insikter och rekommendationer

## 🔒 Säkerhet och multi-tenancy på djupet

Vår implementation prioriterar företagsklass säkerhet:

### Row Level Security (RLS)

PostgreSQL RLS säkerställer dataisolering:

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

### Användaridentitetshantering

Varje MCP-anslutning inkluderar:
- **Butikschef-ID**: Unik identifierare för RLS-kontext
- **Rolltilldelning**: Behörigheter och åtkomstnivåer
- **Sessionshantering**: Säkra autentiseringstokener
- **Revisionsloggning**: Komplett åtkomsthistorik

### Dataskydd

Flera säkerhetslager:
- **Anslutningskryptering**: TLS för alla databasanslutningar
- **Skydd mot SQL-injektion**: Endast parametriserade frågor
- **Inputvalidering**: Omfattande förfrågningsvalidering
- **Felhantering**: Inga känsliga data i felmeddelanden

## 🎯 Viktiga slutsatser

Efter denna introduktion bör du förstå:

✅ **MCPs värdeerbjudande**: Hur MCP länkar AI-assistenter och verkliga data  
✅ **Affärskontext**: Zava Retails krav och utmaningar  
✅ **Arkitekturoversikt**: Nyckelkomponenter och deras interaktioner  
✅ **Teknikstack**: Verktyg och ramverk som används genomgående  
✅ **Säkerhetsmodell**: Multi-tenant datatillgång och skydd  
✅ **Användningsmönster**: Verkliga fråga-scenarier och arbetsflöden  

## 🚀 Vad händer härnäst

Redo att fördjupa dig? Fortsätt med:

**[Labb 01: Kärnarkitekturkoncept](../01-Architecture/README.md)**

Lär dig om MCP-serverarkitekturens mönster, databasdesignprinciper och den detaljerade tekniska implementeringen som driver vår detaljhandelsanalyslösning.

## 📚 Ytterligare resurser

### MCP-dokumentation
- [MCP-specifikation](https://modelcontextprotocol.io/docs/) - Officiell protokolldokumentation
- [MCP för nybörjare](https://aka.ms/mcp-for-beginners) - Omfattande MCP-inlärningsguide
- [FastMCP-dokumentation](https://github.com/modelcontextprotocol/python-sdk) - Python SDK-dokumentation

### Databasintegration
- [PostgreSQL-dokumentation](https://www.postgresql.org/docs/) - Komplett PostgreSQL-referens
- [pgvector-guide](https://github.com/pgvector/pgvector) - Dokumentation för vektorextension
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - Guide för PostgreSQL RLS

### Azure-tjänster
- [Azure OpenAI-dokumentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-tjänsteintegration
- [Azure Database för PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Hanterad databastjänst
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverlösa containers

---

**Friskrivning**: Detta är en övning med fiktiva detaljhandelsdata. Följ alltid din organisations policy för datastyrning och säkerhet när du implementerar liknande lösningar i produktionsmiljöer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->