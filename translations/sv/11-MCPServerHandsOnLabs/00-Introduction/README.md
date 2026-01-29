# Introduktion till MCP-databasintegration

## 🎯 Vad Denna Labb Täcker

Denna introduktionslabb ger en omfattande översikt över hur man bygger Model Context Protocol (MCP)-servrar med databasintegration. Du kommer att förstå affärscaset, den tekniska arkitekturen och verkliga applikationer genom Zava Retails analysfall på https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Översikt

**Model Context Protocol (MCP)** gör det möjligt för AI-assistenter att säkert få åtkomst till och interagera med externa datakällor i realtid. När MCP kombineras med databasintegration öppnar det upp kraftfulla möjligheter för datadrivna AI-applikationer.

Denna lärväg lär dig att bygga produktionsklara MCP-servrar som kopplar AI-assistenter till detaljhandelsförsäljningsdata via PostgreSQL, och implementerar företagsmönster som Row Level Security, semantisk sökning och multi-tenant dataåtkomst.

## Lärandemål

I slutet av denna labb kommer du att kunna:

- **Definiera** Model Context Protocol och dess kärnfördelar för databasintegration
- **Identifiera** nyckelkomponenter i en MCP-serverarkitektur med databaser
- **Förstå** Zava Retails användningsfall och dess affärskrav
- **Känna igen** företagsmönster för säker och skalbar dataåtkomst
- **Lista** verktygen och teknologierna som används genom denna lärväg

## 🧭 Utmaningen: AI Möter Verklig Data

### Begränsningar hos Traditionell AI

Moderna AI-assistenter är otroligt kraftfulla men står inför betydande begränsningar när de arbetar med verklig affärsdata:

| **Utmaning** | **Beskrivning** | **Affärspåverkan** |
|--------------|-----------------|--------------------|
| **Statisk Kunskap** | AI-modeller tränade på fasta dataset kan inte få åtkomst till aktuell affärsdata | Föråldrade insikter, missade möjligheter |
| **Datasilos** | Information låst i databaser, API:er och system som AI inte kan nå | Ofullständig analys, fragmenterade arbetsflöden |
| **Säkerhetsbegränsningar** | Direkt databasåtkomst medför säkerhets- och efterlevnadsproblem | Begränsad implementering, manuell datapreparation |
| **Komplexa Frågor** | Affärsanvändare behöver teknisk kunskap för att extrahera datainsikter | Minskad användning, ineffektiva processer |

### MCP-lösningen

Model Context Protocol löser dessa utmaningar genom att erbjuda:

- **Åtkomst till Realtidsdata**: AI-assistenter kan fråga live-databaser och API:er
- **Säker Integration**: Kontrollerad åtkomst med autentisering och behörigheter
- **Gränssnitt för Naturligt Språk**: Affärsanvändare ställer frågor på vanlig engelska
- **Standardiserad Protokoll**: Fungerar över olika AI-plattformar och verktyg

## 🏪 Möt Zava Retail: Vårt Lärande Fallstudie https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Genom denna lärväg kommer vi att bygga en MCP-server för **Zava Retail**, en fiktiv DIY-detaljhandelskedja med flera butiksplatser. Detta realistiska scenario demonstrerar en företagsklass MCP-implementering.

### Affärskontext

**Zava Retail** driver:
- **8 fysiska butiker** i Washington State (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 onlinebutik** för e-handel
- **Mångsidigt produktkatalog** inklusive verktyg, hårdvara, trädgårdsprodukter och byggmaterial
- **Flernivåledning** med butikschefer, regionchefer och företagsledare

### Affärskrav

Butikschefer och företagsledare behöver AI-drivna analyser för att:

1. **Analysera försäljningsprestanda** över butiker och tidsperioder
2. **Spåra lagernivåer** och identifiera behov av påfyllning
3. **Förstå kundbeteende** och köpmönster
4. **Upptäcka produktinsikter** genom semantisk sökning
5. **Generera rapporter** med naturliga språkfrågor
6. **Upprätthålla datasäkerhet** med rollbaserad åtkomstkontroll

### Tekniska Krav

MCP-servern måste erbjuda:

- **Multi-tenant dataåtkomst** där butikschefer endast ser sin butiks data
- **Flexibel frågeställning** som stödjer komplexa SQL-operationer
- **Semantisk sökning** för produktupptäckt och rekommendationer
- **Realtidsdata** som reflekterar aktuell affärsstatus
- **Säker autentisering** med Row Level Security
- **Skalbar arkitektur** som stödjer flera samtidiga användare

## 🏗️ Översikt över MCP-serverarkitektur

Vår MCP-server implementerar en lagerbaserad arkitektur optimerad för databasintegration:

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

#### **1. MCP-serverlager**
- **FastMCP Framework**: Modern Python MCP-serverimplementation
- **Verktygsregistrering**: Deklarativa verktygsdefinitioner med typkontroll
- **Begärandekontext**: Användaridentitet och sessionshantering
- **Felhantering**: Robust felhantering och loggning

#### **2. Databasintegrationslager**
- **Anslutningspoolning**: Effektiv asyncpg-anslutningshantering
- **Schemaprovider**: Dynamisk tabellschemadetektering
- **Frågeexekutor**: Säker SQL-exekvering med RLS-kontext
- **Transaktionshantering**: ACID-kompatibilitet och rollback-hantering

#### **3. Säkerhetslager**
- **Row Level Security**: PostgreSQL RLS för multi-tenant dataisolering
- **Användaridentitet**: Autentisering och auktorisering för butikschefer
- **Åtkomstkontroll**: Finkorniga behörigheter och granskningsspår
- **Inmatningsvalidering**: SQL-injektionsskydd och frågevalidering

#### **4. AI-förbättringslager**
- **Semantisk sökning**: Vektorinbäddningar för produktupptäckt
- **Azure OpenAI Integration**: Textinbäddningsgenerering
- **Likhetsalgoritmer**: pgvector kosinuslikhetssökning
- **Sökningsoptimering**: Indexering och prestandajustering

## 🔧 Teknologistack

### Kärnteknologier

| **Komponent** | **Teknologi** | **Syfte** |
|---------------|---------------|-----------|
| **MCP Framework** | FastMCP (Python) | Modern MCP-serverimplementation |
| **Databas** | PostgreSQL 17 + pgvector | Relationsdata med vektorsökning |
| **AI-tjänster** | Azure OpenAI | Textinbäddningar och språkmodeller |
| **Containerisering** | Docker + Docker Compose | Utvecklingsmiljö |
| **Molnplattform** | Microsoft Azure | Produktionsdistribution |
| **IDE-integration** | VS Code | AI-chat och utvecklingsarbetsflöde |

### Utvecklingsverktyg

| **Verktyg** | **Syfte** |
|-------------|-----------|
| **asyncpg** | Högpresterande PostgreSQL-drivrutin |
| **Pydantic** | Datavalidering och serialisering |
| **Azure SDK** | Integration av molntjänster |
| **pytest** | Testningsramverk |
| **Docker** | Containerisering och distribution |

### Produktionsstack

| **Tjänst** | **Azure-resurs** | **Syfte** |
|------------|------------------|-----------|
| **Databas** | Azure Database for PostgreSQL | Hanterad databastjänst |
| **Container** | Azure Container Apps | Serverlös containerhosting |
| **AI-tjänster** | Azure AI Foundry | OpenAI-modeller och slutpunkter |
| **Övervakning** | Application Insights | Observabilitet och diagnostik |
| **Säkerhet** | Azure Key Vault | Hantering av hemligheter och konfigurationer |

## 🎬 Verkliga Användningsscenarier

Låt oss utforska hur olika användare interagerar med vår MCP-server:

### Scenario 1: Butikschefens Prestandagranskning

**Användare**: Sarah, butikschef i Seattle  
**Mål**: Analysera försäljningsprestanda för senaste kvartalet

**Naturlig språkfråga**:
> "Visa mig de 10 bästa produkterna efter intäkter för min butik under Q4 2024"

**Vad som händer**:
1. VS Code AI Chat skickar frågan till MCP-servern
2. MCP-servern identifierar Sarahs butikskontext (Seattle)
3. RLS-policyer filtrerar data till endast Seattle-butikens data
4. SQL-fråga genereras och exekveras
5. Resultat formateras och returneras till AI Chat
6. AI ger analys och insikter

### Scenario 2: Produktupptäckt med Semantisk Sökning

**Användare**: Mike, lageransvarig  
**Mål**: Hitta produkter som liknar en kundförfrågan

**Naturlig språkfråga**:
> "Vilka produkter säljer vi som liknar 'vattentäta elektriska kontakter för utomhusbruk'?"

**Vad som händer**:
1. Frågan bearbetas av semantiska sökverktyget
2. Azure OpenAI genererar en vektor för inbäddning
3. pgvector utför likhetssökning
4. Relaterade produkter rankas efter relevans
5. Resultat inkluderar produktdetaljer och tillgänglighet
6. AI föreslår alternativ och paketeringsmöjligheter

### Scenario 3: Tvärbutiksanalys

**Användare**: Jennifer, regionchef  
**Mål**: Jämföra prestanda mellan alla butiker

**Naturlig språkfråga**:
> "Jämför försäljning per kategori för alla butiker under de senaste 6 månaderna"

**Vad som händer**:
1. RLS-kontext sätts för regionchefens åtkomst
2. Komplex multi-butikfråga genereras
3. Data aggregeras över butikslokationer
4. Resultat inkluderar trender och jämförelser
5. AI identifierar insikter och rekommendationer

## 🔒 Säkerhet och Multi-Tenancy Fördjupning

Vår implementering prioriterar säkerhet i företagsklass:

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

### Hantering av Användaridentitet

Varje MCP-anslutning inkluderar:
- **Butikschef-ID**: Unik identifierare för RLS-kontext
- **Rolltilldelning**: Behörigheter och åtkomstnivåer
- **Sessionshantering**: Säker autentiseringstoken
- **Granskningsloggning**: Komplett åtkomsthistorik

### Dataskydd

Flera lager av säkerhet:
- **Anslutningskryptering**: TLS för alla databasanslutningar
- **SQL-injektionsskydd**: Endast parameteriserade frågor
- **Inmatningsvalidering**: Omfattande begärandevalidering
- **Felhantering**: Ingen känslig data i felmeddelanden

## 🎯 Viktiga Slutsatser

Efter att ha genomfört denna introduktion bör du förstå:

✅ **MCP:s Värdeproposition**: Hur MCP kopplar AI-assistenter till verklig data  
✅ **Affärskontext**: Zava Retails krav och utmaningar  
✅ **Arkitekturöversikt**: Nyckelkomponenter och deras interaktioner  
✅ **Teknologisk Stack**: Verktyg och ramverk som används  
✅ **Säkerhetsmodell**: Multi-tenant dataåtkomst och skydd  
✅ **Användningsmönster**: Verkliga frågescenarier och arbetsflöden  

## 🚀 Vad Nästa

Redo att fördjupa dig? Fortsätt med:

**[Lab 01: Kärnarkitekturkoncept](../01-Architecture/README.md)**

Lär dig om MCP-serverarkitekturens mönster, databasdesignprinciper och den detaljerade tekniska implementeringen som driver vår detaljhandelsanalyslösning.

## 📚 Ytterligare Resurser

### MCP-dokumentation
- [MCP-specifikation](https://modelcontextprotocol.io/docs/) - Officiell protokoll-dokumentation
- [MCP för Nybörjare](https://aka.ms/mcp-for-beginners) - Omfattande MCP-lärguide
- [FastMCP-dokumentation](https://github.com/modelcontextprotocol/python-sdk) - Python SDK-dokumentation

### Databasintegration
- [PostgreSQL-dokumentation](https://www.postgresql.org/docs/) - Komplett PostgreSQL-referens
- [pgvector-guide](https://github.com/pgvector/pgvector) - Dokumentation för vektortillägg
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS-guide

### Azure-tjänster
- [Azure OpenAI-dokumentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-tjänstintegration
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Hanterad databastjänst
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverlösa containers

---

**Ansvarsfriskrivning**: Detta är en lärandeövning med fiktiv detaljhandelsdata. Följ alltid din organisations datastyrning och säkerhetspolicyer när du implementerar liknande lösningar i produktionsmiljöer.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.