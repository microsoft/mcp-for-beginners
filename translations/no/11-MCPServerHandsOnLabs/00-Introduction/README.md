# Introduksjon til MCP-databaseintegrasjon

## 🎯 Hva Denne Labben Dekker

Denne introduksjonslabben gir en omfattende oversikt over hvordan man bygger Model Context Protocol (MCP)-servere med databaseintegrasjon. Du vil forstå forretningscasen, teknisk arkitektur og virkelige applikasjoner gjennom Zava Retail-analytikkeksempelet på https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Oversikt

**Model Context Protocol (MCP)** gjør det mulig for AI-assistenter å få sikker tilgang til og samhandle med eksterne datakilder i sanntid. Når MCP kombineres med databaseintegrasjon, åpnes kraftige muligheter for datadrevne AI-applikasjoner.

Denne læringsstien lærer deg å bygge produksjonsklare MCP-servere som kobler AI-assistenter til detaljhandelsdata via PostgreSQL, og implementerer bedriftsmønstre som Row Level Security, semantisk søk og multi-tenant datatilgang.

## Læringsmål

Ved slutten av denne labben vil du kunne:

- **Definere** Model Context Protocol og dens kjernefordeler for databaseintegrasjon
- **Identifisere** nøkkelkomponenter i en MCP-serverarkitektur med databaser
- **Forstå** Zava Retail-brukstilfellet og dets forretningskrav
- **Gjenkjenne** bedriftsmønstre for sikker og skalerbar datatilgang
- **Liste opp** verktøyene og teknologiene som brukes gjennom denne læringsstien

## 🧭 Utfordringen: AI Møter Virkelige Data

### Begrensninger i Tradisjonell AI

Moderne AI-assistenter er utrolig kraftige, men står overfor betydelige begrensninger når de arbeider med virkelige forretningsdata:

| **Utfordring** | **Beskrivelse** | **Forretningspåvirkning** |
|----------------|-----------------|---------------------------|
| **Statisk Kunnskap** | AI-modeller trent på faste datasett kan ikke få tilgang til oppdaterte forretningsdata | Utdaterte innsikter, tapte muligheter |
| **Datasiloer** | Informasjon låst i databaser, API-er og systemer AI ikke kan nå | Ufullstendig analyse, fragmenterte arbeidsflyter |
| **Sikkerhetsbegrensninger** | Direkte databaseadgang skaper sikkerhets- og samsvarsproblemer | Begrenset utrulling, manuell datapreparering |
| **Komplekse Spørringer** | Forretningsbrukere trenger teknisk kunnskap for å hente data | Redusert adopsjon, ineffektive prosesser |

### MCP-løsningen

Model Context Protocol adresserer disse utfordringene ved å tilby:

- **Sanntidsdatatilgang**: AI-assistenter kan hente data fra live databaser og API-er
- **Sikker Integrasjon**: Kontrollert tilgang med autentisering og tillatelser
- **Naturlig Språkgrensesnitt**: Forretningsbrukere kan stille spørsmål på vanlig norsk
- **Standardisert Protokoll**: Fungerer på tvers av ulike AI-plattformer og verktøy

## 🏪 Møt Zava Retail: Vårt Læringscasestudie https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Gjennom denne læringsstien skal vi bygge en MCP-server for **Zava Retail**, en fiktiv gjør-det-selv detaljhandelskjede med flere butikksteder. Dette realistiske scenariet demonstrerer MCP-implementering på bedriftsnivå.

### Forretningskontekst

**Zava Retail** driver:
- **8 fysiske butikker** i Washington State (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 nettbutikk** for e-handel
- **Mangfoldig produktkatalog** inkludert verktøy, maskinvare, hageutstyr og byggematerialer
- **Flernivåledelse** med butikksjefer, regionsjefer og ledere

### Forretningskrav

Butikksjefer og ledere trenger AI-drevet analyse for å:

1. **Analysere salgsytelse** på tvers av butikker og tidsperioder
2. **Sporing av lagerbeholdning** og identifisering av behov for påfylling
3. **Forstå kundeadferd** og kjøpsmønstre
4. **Oppdage produktinnsikter** gjennom semantisk søk
5. **Generere rapporter** med naturlige språkspørringer
6. **Opprettholde datasikkerhet** med rollebasert tilgangskontroll

### Tekniske Krav

MCP-serveren må tilby:

- **Multi-tenant datatilgang** der butikksjefer kun ser data for sin butikk
- **Fleksible spørringer** som støtter komplekse SQL-operasjoner
- **Semantisk søk** for produktoppdagelse og anbefalinger
- **Sanntidsdata** som reflekterer nåværende forretningsstatus
- **Sikker autentisering** med Row Level Security
- **Skalerbar arkitektur** som støtter flere samtidige brukere

## 🏗️ MCP-serverarkitektur Oversikt

Vår MCP-server implementerer en lagdelt arkitektur optimalisert for databaseintegrasjon:

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

### Nøkkelkomponenter

#### **1. MCP Server Lag**
- **FastMCP Framework**: Moderne Python MCP-serverimplementering
- **Verktøyregistrering**: Deklarative verktøydefinisjoner med typekontroll
- **Forespørselkontekst**: Brukeridentitet og sesjonsadministrasjon
- **Feilhåndtering**: Robust feiladministrasjon og logging

#### **2. Databaseintegrasjonslag**
- **Tilkoblingspooling**: Effektiv asyncpg-tilkoblingsadministrasjon
- **Skjemaleverandør**: Dynamisk oppdagelse av tabellskjema
- **Spørringsutfører**: Sikker SQL-eksekvering med RLS-kontekst
- **Transaksjonsadministrasjon**: ACID-samsvar og rollback-håndtering

#### **3. Sikkerhetslag**
- **Row Level Security**: PostgreSQL RLS for multi-tenant dataisolasjon
- **Brukeridentitet**: Autentisering og autorisasjon for butikksjefer
- **Tilgangskontroll**: Finkornede tillatelser og revisjonsspor
- **Inputvalidering**: Forebygging av SQL-injeksjon og spørringsvalidering

#### **4. AI-forbedringslag**
- **Semantisk søk**: Vektorinnbygging for produktoppdagelse
- **Azure OpenAI-integrasjon**: Generering av tekstinnbygging
- **Likhetsalgoritmer**: pgvector kosinuslikhetssøk
- **Søkeoptimalisering**: Indeksering og ytelsestuning

## 🔧 Teknologistabel

### Kjerne Teknologier

| **Komponent** | **Teknologi** | **Formål** |
|---------------|---------------|------------|
| **MCP Framework** | FastMCP (Python) | Moderne MCP-serverimplementering |
| **Database** | PostgreSQL 17 + pgvector | Relasjonsdata med vektorsøk |
| **AI-tjenester** | Azure OpenAI | Tekstinnbygging og språkmodeller |
| **Containerisering** | Docker + Docker Compose | Utviklingsmiljø |
| **Skyplattform** | Microsoft Azure | Produksjonsutrulling |
| **IDE-integrasjon** | VS Code | AI-chat og utviklingsarbeidsflyt |

### Utviklingsverktøy

| **Verktøy** | **Formål** |
|-------------|------------|
| **asyncpg** | Høyytelses PostgreSQL-driver |
| **Pydantic** | Datavalidering og serialisering |
| **Azure SDK** | Integrasjon av skytjenester |
| **pytest** | Testrammeverk |
| **Docker** | Containerisering og utrulling |

### Produksjonsstabel

| **Tjeneste** | **Azure Ressurs** | **Formål** |
|--------------|-------------------|------------|
| **Database** | Azure Database for PostgreSQL | Administrert databaseservice |
| **Container** | Azure Container Apps | Serverløs containerhosting |
| **AI-tjenester** | Azure AI Foundry | OpenAI-modeller og endepunkter |
| **Overvåking** | Application Insights | Observabilitet og diagnostikk |
| **Sikkerhet** | Azure Key Vault | Hemmelige data og konfigurasjonsadministrasjon |

## 🎬 Virkelige Bruksscenarier

La oss utforske hvordan ulike brukere interagerer med vår MCP-server:

### Scenario 1: Butikksjefens Ytelsesgjennomgang

**Bruker**: Sarah, butikksjef i Seattle  
**Mål**: Analysere salgsytelsen for siste kvartal

**Naturlig Språkspørring**:
> "Vis meg de 10 beste produktene etter inntekt for min butikk i Q4 2024"

**Hva Skjer**:
1. VS Code AI Chat sender spørringen til MCP-serveren
2. MCP-serveren identifiserer Sarahs butikkontekst (Seattle)
3. RLS-policyer filtrerer data til kun Seattle-butikken
4. SQL-spørring genereres og utføres
5. Resultater formateres og returneres til AI Chat
6. AI gir analyse og innsikter

### Scenario 2: Produktoppdagelse med Semantisk Søk

**Bruker**: Mike, lageransvarlig  
**Mål**: Finne produkter som ligner på en kundes forespørsel

**Naturlig Språkspørring**:
> "Hvilke produkter selger vi som ligner på 'vanntette elektriske kontakter for utendørs bruk'?"

**Hva Skjer**:
1. Spørringen behandles av semantisk søkeverktøy
2. Azure OpenAI genererer vektorinnbygging
3. pgvector utfører likhetssøk
4. Relaterte produkter rangeres etter relevans
5. Resultater inkluderer produktdetaljer og tilgjengelighet
6. AI foreslår alternativer og pakkemuligheter

### Scenario 3: Tverrbutikkanalyse

**Bruker**: Jennifer, regionsjef  
**Mål**: Sammenligne ytelse på tvers av alle butikker

**Naturlig Språkspørring**:
> "Sammenlign salg etter kategori for alle butikker de siste 6 månedene"

**Hva Skjer**:
1. RLS-kontekst settes for regionsjefens tilgang
2. Kompleks tverrbutikkspørring genereres
3. Data aggregeres på tvers av butikksteder
4. Resultater inkluderer trender og sammenligninger
5. AI identifiserer innsikter og anbefalinger

## 🔒 Sikkerhet og Multi-Tenant Dypdykk

Vår implementering prioriterer sikkerhet på bedriftsnivå:

### Row Level Security (RLS)

PostgreSQL RLS sikrer dataisolasjon:

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

### Brukeridentitetsadministrasjon

Hver MCP-tilkobling inkluderer:
- **Butikksjef-ID**: Unik identifikator for RLS-kontekst
- **Rollefordeling**: Tillatelser og tilgangsnivåer
- **Sesjonsadministrasjon**: Sikker autentiseringstoken
- **Revisjonslogging**: Fullstendig tilgangshistorikk

### Databeskyttelse

Flere lag med sikkerhet:
- **Tilkoblingskryptering**: TLS for alle databasetilkoblinger
- **Forebygging av SQL-injeksjon**: Kun parameteriserte spørringer
- **Inputvalidering**: Omfattende forespørselsvalidering
- **Feilhåndtering**: Ingen sensitiv data i feilmeldinger

## 🎯 Viktige Lærdommer

Etter å ha fullført denne introduksjonen, bør du forstå:

✅ **MCP-verdi**: Hvordan MCP kobler AI-assistenter til virkelige data  
✅ **Forretningskontekst**: Zava Retails krav og utfordringer  
✅ **Arkitekturoversikt**: Nøkkelkomponenter og deres interaksjoner  
✅ **Teknologisk stabel**: Verktøy og rammeverk som brukes  
✅ **Sikkerhetsmodell**: Multi-tenant datatilgang og beskyttelse  
✅ **Bruksmønstre**: Virkelige spørringsscenarier og arbeidsflyter  

## 🚀 Hva Nå?

Klar til å gå dypere? Fortsett med:

**[Lab 01: Kjernearkitekturkonsepter](../01-Architecture/README.md)**

Lær om MCP-serverarkitekturmønstre, prinsipper for databasedesign og den detaljerte tekniske implementeringen som driver vår detaljhandelsanalyseløsning.

## 📚 Tilleggsressurser

### MCP-dokumentasjon
- [MCP-spesifikasjon](https://modelcontextprotocol.io/docs/) - Offisiell protokoll-dokumentasjon
- [MCP for Nybegynnere](https://aka.ms/mcp-for-beginners) - Omfattende MCP-læringsguide
- [FastMCP-dokumentasjon](https://github.com/modelcontextprotocol/python-sdk) - Python SDK-dokumentasjon

### Databaseintegrasjon
- [PostgreSQL-dokumentasjon](https://www.postgresql.org/docs/) - Komplett PostgreSQL-referanse
- [pgvector-guide](https://github.com/pgvector/pgvector) - Dokumentasjon for vektorekstensjon
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS-guide

### Azure-tjenester
- [Azure OpenAI-dokumentasjon](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-tjenesteintegrasjon
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Administrert databaseservice
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverløse containere

---

**Ansvarsfraskrivelse**: Dette er en læringsøvelse med fiktive detaljhandelsdata. Følg alltid organisasjonens retningslinjer for datastyring og sikkerhet når du implementerer lignende løsninger i produksjonsmiljøer.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.