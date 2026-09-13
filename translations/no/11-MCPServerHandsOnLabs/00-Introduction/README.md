# Introduksjon til MCP-databaseintegrasjon

> [!NOTE]
> Diagrammer eller kode i denne læringsveien som bruker HTTP/SSE eller initialiserings-
> alternativer reflekterer eksempelets MCP `2025-11-25` avhengigheter. For nye
> implementeringer, bruk `2026-07-28` tilstandsløse forespørsler og Streamable HTTP.

## 🎯 Hva denne labben dekker

Denne introduksjonslabben gir en omfattende oversikt over bygging av Model Context Protocol (MCP) servere med databaseintegrasjon. Du vil forstå forretningssaken, teknisk arkitektur, og virkelige anvendelser gjennom Zava Retail-analytikk tilfellet på https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Oversikt

**Model Context Protocol (MCP)** lar AI-assistenter trygt få tilgang til og samhandle med eksterne datakilder i sanntid. Kombinert med databaseintegrasjon, åpner MCP kraftige muligheter for datadrevne AI-applikasjoner.

Denne læringsveien lærer deg å bygge produksjonsklare MCP-servere som kobler AI-assistenter til detaljhandelssalgsdata gjennom PostgreSQL, og implementerer bedriftsmønstre som Row Level Security, semantisk søk, og flerleietilgang til data.

## Læringsmål

Etter denne labben skal du kunne:

- **Definere** Model Context Protocol og dets kjernefordeler for databaseintegrasjon
- **Identifisere** nøkkelkomponenter i en MCP-serverarkitektur med databaser
- **Forstå** Zava Retail-tilfellet og dets forretningskrav
- **Gjenkjenne** bedriftsmønstre for sikker og skalerbar databaseadgang
- **Liste opp** verktøy og teknologier brukt gjennom læringsveien

## 🧭 Utfordringen: AI møter virkelige data

### Tradisjonelle AI-begrensninger

Moderne AI-assistenter er utrolig kraftige, men møter betydelige begrensninger når de arbeider med virkelige forretningsdata:

| **Utfordring** | **Beskrivelse** | **Forretningspåvirkning** |
|---------------|-----------------|-------------------|
| **Statisk kunnskap** | AI-modeller trent på faste datasett kan ikke få tilgang til oppdaterte forretningsdata | Utdaterte innsikter, tapte muligheter |
| **Datasiloer** | Informasjon låst i databaser, API-er og systemer AI ikke kan nå | Ufullstendig analyse, fragmenterte arbeidsflyter |
| **Sikkerhetsbegrensninger** | Direkte databaseadgang reiser sikkerhets- og samsvarshensyn | Begrenset distribusjon, manuell dataklargjøring |
| **Komplekse spørringer** | Forretningsbrukere trenger teknisk kunnskap for å hente ut datainnsikt | Redusert adopsjon, ineffektive prosesser |

### MCP-løsningen

Model Context Protocol adresserer disse utfordringene ved å tilby:

- **Sanntidsdata-tilgang**: AI-assistenter spør live databaser og API-er
- **Sikker integrasjon**: Kontrollert tilgang med autentisering og tillatelser
- **Naturlig språkgrensesnitt**: Forretningsbrukere stiller spørsmål på vanlig engelsk
- **Standardisert protokoll**: Fungerer på tvers av ulike AI-plattformer og verktøy

## 🏪 Møt Zava Retail: Vårt læringseksempel https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

Gjennom denne læringsveien skal vi bygge en MCP-server for **Zava Retail**, en fiktiv gjør-det-selv detaljhandelkjede med flere butikksteder. Dette realistiske scenariet demonstrerer bedriftsklasse MCP-implementering.

### Forretningskontekst

**Zava Retail** opererer:
- **8 fysiske butikker** fordelt på Washington State (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 nettbutikk** for netthandel
- **Mangfoldig produktkatalog** inkludert verktøy, maskinvare, hageartikler og byggematerialer
- **Flernivå-ledelse** med butikksjefer, regionsjefer og ledere

### Forretningskrav

Butikksjefer og ledere trenger AI-drevne analyser for å:

1. **Analysere salgsytelse** på tvers av butikker og tidsperioder
2. **Sporingsnivå for lagerbeholdning** og identifisere påfyllingsbehov
3. **Forstå kundeadferd** og kjøpsmønstre
4. **Oppdage produktoppslag** gjennom semantisk søk
5. **Generere rapporter** med spørsmål i naturlig språk
6. **Opprettholde datasikkerhet** med rollebasert tilgangskontroll

### Tekniske krav

MCP-serveren må tilby:

- **Flerleietilgang til data** der butikksjefer kun ser sin butiks data
- **Fleksible spørringer** som støtter komplekse SQL-operasjoner
- **Semantisk søk** for produktoppdagelse og anbefalinger
- **Sanntidsdata** som reflekterer gjeldende forretningsstatus
- **Sikker autentisering** med row-level security
- **Skalerbar arkitektur** som støtter flere samtidige brukere

## 🏗️ MCP-serverarkitekturoversikt

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

#### **1. MCP-serverlag**
- **FastMCP Framework**: Moderne MCP-serverimplementasjon i Python
- **Verktøyregistrering**: Deklarative verktøydefinisjoner med typesikkerhet
- **Forespørselssammenheng**: Brukeridentitet og sesjonsadministrasjon
- **Feilhåndtering**: Robust feilbehandling og logging

#### **2. Databaseintegrasjonslag**
- **Koblingspooling**: Effektiv asynkron asyncpg-tilkoblingshåndtering
- **Skjemaleverandør**: Dynamisk oppdagelse av tabellskjemaer
- **Spørringsutfører**: Sikker SQL-kjøring med RLS-sammenheng
- **Transaksjonshåndtering**: ACID-kompatibilitet og rollback-håndtering

#### **3. Sikkerhetslag**
- **Row Level Security**: PostgreSQL RLS for flerleiedata-isolasjon
- **Brukeridentitet**: Autentisering og autorisasjon for butikksjefer
- **Tilgangskontroll**: Finkornede tillatelser og revisjonsspor
- **Inndata-validering**: Forebygging av SQL-injeksjon og gyldighetskontroll for spørringer

#### **4. AI-forbedringslag**
- **Semantisk søk**: Vektorinnbakinger for produktopdagelse
- **Azure OpenAI-integrasjon**: Tekstinnbakinggenerering
- **Likhetsalgoritmer**: pgvector cosine similarity-søk
- **Søkeoptimalisering**: Indeksering og ytelsestuning

## 🔧 Teknologistabel

### Kjerne-teknologier

| **Komponent** | **Teknologi** | **Formål** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderne MCP-serverimplementasjon |
| **Database** | PostgreSQL 17 + pgvector | Relasjonsdata med vektorsøk |
| **AI-tjenester** | Azure OpenAI | Tekstinnbakinger og språkmodeller |
| **Containerisering** | Docker + Docker Compose | Utviklingsmiljø |
| **Skyplattform** | Microsoft Azure | Produksjonsdistribusjon |
| **IDE-integrasjon** | VS Code | AI Chat og utviklingsarbeidsflyt |

### Utviklingsverktøy

| **Verktøy** | **Formål** |
|----------|-------------|
| **asyncpg** | Høyytelses PostgreSQL-driver |
| **Pydantic** | Datavalidering og serialisering |
| **Azure SDK** | Sky tjenesteintegrasjon |
| **pytest** | Test-rammeverk |
| **Docker** | Containerisering og distribusjon |

### Produksjonsstabel

| **Tjeneste** | **Azure-ressurs** | **Formål** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Administrert databasen tjeneste |
| **Container** | Azure Container Apps | Serverløs containerhosting |
| **AI-tjenester** | Microsoft Foundry | OpenAI-modeller og endepunkter |
| **Overvåking** | Application Insights | Observabilitet og diagnostikk |
| **Sikkerhet** | Azure Key Vault | Hemmeligheter og konfigurasjonsstyring |

## 🎬 Virkelige bruksscenarioer

La oss utforske hvordan ulike brukere samhandler med vår MCP-server:

### Scenario 1: Butikksjefens ytelsesgjennomgang

**Bruker**: Sarah, butikksjef i Seattle  
**Mål**: Analysere fjorårets kvartalssalg

**Spørsmål i naturlig språk**:
> "Vis meg de 10 beste produktene etter omsetning for min butikk i Q4 2024"

**Hva skjer**:
1. VS Code AI Chat sender spørring til MCP-serveren
2. MCP-serveren identifiserer Sarahs butikksammenheng (Seattle)
3. RLS-policy filtrerer data til kun Seattle-butikken
4. SQL-spørring genereres og kjøres
5. Resultater formateres og returneres til AI Chat
6. AI gir analyse og innsikter

### Scenario 2: Produktoppdagelse med semantisk søk

**Bruker**: Mike, lageransvarlig  
**Mål**: Finne produkter som ligner på en kunders forespørsel

**Spørsmål i naturlig språk**:
> "Hvilke produkter selger vi som ligner på 'vanntette elektriske kontakter for utendørs bruk'?"

**Hva skjer**:
1. Spørringen behandles av semantisk søkeverktøy
2. Azure OpenAI genererer innbakkingsvektor
3. pgvector utfører likhetssøk
4. Relaterte produkter rangeres etter relevans
5. Resultater inkluderer produktdetaljer og tilgjengelighet
6. AI foreslår alternativer og pakke-muligheter

### Scenario 3: Analyse på tvers av butikker

**Bruker**: Jennifer, regionsjef  
**Mål**: Sammenligne ytelse på tvers av alle butikker

**Spørsmål i naturlig språk**:
> "Sammenlign salg etter kategori for alle butikker de siste 6 månedene"

**Hva skjer**:
1. RLS-sammenheng settes for regionssjefs tilgang
2. Kompleks flerstedt-spørring genereres
3. Data aggregeres på tvers av butikkenes lokasjoner
4. Resultater inkluderer trender og sammenligninger
5. AI identifiserer innsikter og anbefalinger

## 🔒 Sikkerhet og flerleie-dypdykk

Vår implementering prioriterer sikkerhet på bedriftsnivå:

### Row Level Security (RLS)

PostgreSQL RLS sikrer data-isolasjon:

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

### Brukeridentitetsstyring

Hver MCP-tilkobling inkluderer:
- **Butikksjef-ID**: Unik identifikator for RLS-sammenheng
- **Rollefordeling**: Tillatelser og tilgangsnivåer
- **Sesjonsadministrasjon**: Sikker autentiseringstoken
- **Revisjonslogging**: Fullstendig tilgangshistorikk

### Databeskyttelse

Flere sikkerhetslag:
- **Kryptering av tilkobling**: TLS for alle databaseforbindelser
- **Forebygging av SQL-injeksjon**: Kun parameteriserte spørringer
- **Inndatavalidering**: Omfattende validering av forespørsler
- **Feilhåndtering**: Ingen sensitiv data i feilmeldinger

## 🎯 Viktige konklusjoner

Etter å ha fullført denne introduksjonen, bør du forstå:

✅ **MCPs verdiforslag**: Hvordan MCP kobler AI-assistenter til virkelige data  
✅ **Forretningskontekst**: Zava Retails krav og utfordringer  
✅ **Arkitekturoversikt**: Nøkkelkomponenter og deres samspill  
✅ **Teknologistabel**: Verktøy og rammeverk brukt gjennom hele veien  
✅ **Sikkerhetsmodell**: Flerleietilgang og databeskyttelse  
✅ **Bruksmønstre**: Virkelige spørringsscenarioer og arbeidsflyter  

## 🚀 Hva nå?

Klar for å gå dypere? Fortsett med:

**[Lab 01: Kjernearkitekturkonsepter](../01-Architecture/README.md)**

Lær om MCP-serverarkitektur-mønstre, databasedesignprinsipper og detaljert teknisk implementering som driver vår detaljhandelsanalyseløsning.

## 📚 Ytterligere ressurser

### MCP Dokumentasjon
- [MCP Spesifikasjon](https://modelcontextprotocol.io/docs/) - Offisiell protokoll-dokumentasjon
- [MCP for Nybegynnere](https://aka.ms/mcp-for-beginners) - Omfattende MCP-læringsguide
- [FastMCP Dokumentasjon](https://github.com/modelcontextprotocol/python-sdk) - Python SDK dokumentasjon

### Databaseintegrasjon
- [PostgreSQL Dokumentasjon](https://www.postgresql.org/docs/) - Komplett PostgreSQL-referanse
- [pgvector Guide](https://github.com/pgvector/pgvector) - Vektorutvidelsesdokumentasjon
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS-guide

### Azure-tjenester
- [Azure OpenAI Dokumentasjon](https://docs.microsoft.com/azure/cognitive-services/openai/) - AI-tjenesteintegrasjon
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Administrert databasen tjeneste
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverløse containere

---

**Ansvarsfraskrivelse**: Dette er en læringsøvelse med fiktive detaljhandelsdata. Følg alltid din organisasjons retningslinjer for datastyring og sikkerhet ved implementasjon av lignende løsninger i produksjonsmiljøer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->