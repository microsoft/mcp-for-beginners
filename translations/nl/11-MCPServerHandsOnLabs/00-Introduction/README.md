# Introductie tot MCP Database-integratie

> [!NOTE]
> Diagrammen of code in dit leertraject die HTTP/SSE of initialisatie
> opties gebruiken, weerspiegelen de MCP `2025-11-25` afhankelijkheden van het voorbeeld. Voor nieuwe
> implementaties, gebruik `2026-07-28` stateless verzoeken en Streamable HTTP.

## 🎯 Wat Deze Lab Behandelt

Deze introductielab biedt een uitgebreid overzicht van het bouwen van Model Context Protocol (MCP) servers met database-integratie. Je krijgt inzicht in de businesscase, technische architectuur en praktijkvoorbeelden via de Zava Retail analytics use-case op https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## Overzicht

**Model Context Protocol (MCP)** maakt het AI-assistenten mogelijk om veilig toegang te krijgen tot en te interacteren met externe databronnen in realtime. In combinatie met database-integratie ontsluit MCP krachtige mogelijkheden voor datagedreven AI-toepassingen.

Dit leertraject leert je productieklaar MCP-servers bouwen die AI-assistenten verbinden met retailverkoopdata via PostgreSQL, met implementatie van enterprisepatronen zoals Row Level Security, semantische zoekopdrachten en multi-tenant data toegang.

## Leerdoelen

Aan het einde van deze lab kun je:

- **Definiëren** van Model Context Protocol en de kernvoordelen voor database-integratie
- **Identificeren** van sleutelcomponenten van een MCP-serverarchitectuur met databases
- **Begrijpen** van de Zava Retail use-case en de zakelijke vereisten
- **Herkennen** van enterprisepatronen voor veilige, schaalbare database toegang
- **Opsommen** van de gebruikte tools en technologieën door dit leertraject

## 🧭 De Uitdaging: AI Ontmoet Reële Data

### Traditionele AI-beperkingen

Moderne AI-assistenten zijn ongelooflijk krachtig maar hebben aanzienlijke beperkingen bij het werken met reële bedrijfsdata:

| **Uitdaging** | **Beschrijving** | **Zakelijke Impact** |
|---------------|-----------------|-------------------|
| **Statische Kennis** | AI-modellen getraind op vaste datasets hebben geen toegang tot actuele bedrijfsdata | Verouderde inzichten, gemiste kansen |
| **Data Silos** | Informatie opgeslagen in databases, API's en systemen die AI niet kan bereiken | Onvolledige analyse, gefragmenteerde workflows |
| **Beveiligingsbeperkingen** | Directe database toegang brengt beveiligings- en compliancezorgen met zich mee | Beperkte uitrol, handmatige datapreparatie |
| **Complexe Query's** | Zakelijke gebruikers hebben technische kennis nodig om data-inzichten te verkrijgen | Minder adoptie, inefficiënte processen |

### De MCP Oplossing

Model Context Protocol pakt deze uitdagingen aan door:

- **Realtime Data Toegang**: AI-assistenten kunnen live databases en API's bevragen
- **Veilige Integratie**: Gecontroleerde toegang met authenticatie en permissies
- **Natuurlijke Taalinterface**: Zakelijke gebruikers stellen vragen in gewone taal
- **Gestandaardiseerd Protocol**: Werkt met verschillende AI-platforms en tools

## 🏪 Maak kennis met Zava Retail: Onze Leer-casestudy https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

In dit leertraject bouwen we een MCP-server voor **Zava Retail**, een fictieve doe-het-zelf-retailketen met meerdere winkels. Dit realistische scenario demonstreert een MCP-implementatie op enterprise-niveau.

### Zakelijke Context

**Zava Retail** exploiteert:
- **8 fysieke winkels** verspreid over de staat Washington (Seattle, Bellevue, Tacoma, Spokane, Everett, Redmond, Kirkland)
- **1 online winkel** voor e-commerce verkoop
- **Divers productcatalogus** met gereedschap, bouwmaterialen, tuinartikelen en meer
- **Meervoudig managementniveau** met winkelmanagers, regiomanagers en executives

### Zakelijke Vereisten

Winkelmanagers en executives hebben AI-aangedreven analytics nodig om:

1. **Verkoopprestaties analyseren** over winkels en periodes
2. **Voorraden bijhouden** en aanvulbehoeften identificeren
3. **Klanteninzicht verkrijgen** en koopgedrag analyseren
4. **Productinzichten ontdekken** via semantische zoekfunctie
5. **Rapporten genereren** met natuurlijke taalqueries
6. **Data beveiliging behouden** via rolgebaseerde toegangscontrole

### Technische Vereisten

De MCP-server moet bieden:

- **Multi-tenant data toegang** waarbij winkelmanagers alleen de data van hun eigen winkel zien
- **Flexibele querymogelijkheden** met ondersteuning voor complexe SQL-operaties
- **Semantische zoekfunctie** voor productontdekking en aanbevelingen
- **Realtime data** die de actuele bedrijfstoestand weerspiegelt
- **Veilige authenticatie** met row-level security
- **Schaalbare architectuur** die meerdere gelijktijdige gebruikers ondersteunt

## 🏗️ Overzicht MCP Server Architectuur

Onze MCP-server implementeert een gelaagde architectuur geoptimaliseerd voor database-integratie:

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

### Belangrijke Componenten

#### **1. MCP Serverlaag**
- **FastMCP Framework**: Moderne Python MCP serverimplementatie
- **Toolregistratie**: Declaratieve tooldefinities met typeveiligheid
- **Request Context**: Gebruikersidentiteit en sessiebeheer
- **Foutafhandeling**: Robuust foutenbeheer en logging

#### **2. Database Integratielaag**
- **Connection Pooling**: Efficiënt beheer van asyncpg-verbindingen
- **Schema Provider**: Dynamische ontdekking van tabelschema's
- **Query Executor**: Veilige SQL-uitvoering met RLS-context
- **Transactiebeheer**: ACID-compliance en rollback-afhandeling

#### **3. Beveiligingslaag**
- **Row Level Security**: PostgreSQL RLS voor isolatie van multi-tenant data
- **Gebruikersidentiteit**: Authenticatie en autorisatie van winkelmanagers
- **Toegangscontrole**: Fijngranulaire permissies en audit trails
- **Invoervalidatie**: Preventie van SQL-injectie en queryvalidatie

#### **4. AI Versterkingslaag**
- **Semantische Zoekfunctie**: Vector embeddings voor productontdekking
- **Azure OpenAI Integratie**: Generatie van tekstembeddings
- **Similariteitsalgoritmen**: pgvector cosine similarity search
- **Zoekoptimalisatie**: Indexering en prestatie-afstemming

## 🔧 Technologie Stack

### Kerntechnologieën

| **Component** | **Technologie** | **Doel** |
|---------------|----------------|-------------|
| **MCP Framework** | FastMCP (Python) | Moderne MCP serverimplementatie |
| **Database** | PostgreSQL 17 + pgvector | Relationale data met vectorzoekfunctie |
| **AI Services** | Azure OpenAI | Tekstembeddings en taalmodellen |
| **Containerisatie** | Docker + Docker Compose | Ontwikkelomgeving |
| **Cloudplatform** | Microsoft Azure | Productie-implementatie |
| **IDE Integratie** | VS Code | AI Chat en ontwikkelworkflow |

### Ontwikkelingstools

| **Tool** | **Doel** |
|----------|-------------|
| **asyncpg** | Hoogwaardige PostgreSQL-driver |
| **Pydantic** | Datenvalidatie en serialisatie |
| **Azure SDK** | Integratie met cloudservices |
| **pytest** | Testframework |
| **Docker** | Containerisatie en uitrol |

### Productie-stack

| **Service** | **Azure Resource** | **Doel** |
|-------------|-------------------|-------------|
| **Database** | Azure Database for PostgreSQL | Beheerde database-service |
| **Container** | Azure Container Apps | Serverless container-hosting |
| **AI Services** | Microsoft Foundry | OpenAI-modellen en endpoints |
| **Monitoring** | Application Insights | Observeerbaarheid en diagnostiek |
| **Beveiliging** | Azure Key Vault | Beheer van geheimen en configuratie |

## 🎬 Praktijkvoorbeelden

Laten we verkennen hoe verschillende gebruikers interactie hebben met onze MCP-server:

### Scenario 1: Prestatiebeoordeling Winkelmanager

**Gebruiker**: Sarah, Winkelmanager Seattle  
**Doel**: Verkoopprestaties van afgelopen kwartaal analyseren

**Natuurlijke Taal Query**:
> "Laat me de top 10 producten zien op omzet voor mijn winkel in Q4 2024"

**Wat Gebeurt Er**:
1. VS Code AI Chat stuurt query naar MCP-server
2. MCP-server identificeert Sarah's winkelcontext (Seattle)
3. RLS-beleid filtert data naar alleen Seattle winkel
4. SQL-query wordt gegenereerd en uitgevoerd
5. Resultaten worden geformatteerd en teruggestuurd naar AI Chat
6. AI biedt analyse en inzichten

### Scenario 2: Productontdekking met Semantische Zoekfunctie

**Gebruiker**: Mike, Voorraadbeheerder  
**Doel**: Producten vinden die lijken op een klantverzoek

**Natuurlijke Taal Query**:
> "Welke producten verkopen we die lijken op 'waterdichte elektrische connectors voor buitengebruik'?"

**Wat Gebeurt Er**:
1. Query wordt verwerkt door semantische zoektool
2. Azure OpenAI genereert embeddingvector
3. pgvector voert similariteitszoekopdracht uit
4. Gerelateerde producten worden gerangschikt op relevantie
5. Resultaten bevatten productdetails en beschikbaarheid
6. AI doet suggesties voor alternatieven en bundelopties

### Scenario 3: Cross-Store Analytics

**Gebruiker**: Jennifer, Regiomanager  
**Doel**: Prestaties vergelijken over alle winkels

**Natuurlijke Taal Query**:
> "Vergelijk verkoop per categorie voor alle winkels in de afgelopen 6 maanden"

**Wat Gebeurt Er**:
1. RLS-context ingesteld voor regiomanager toegang
2. Complexe multi-store query gegenereerd
3. Data geaggregeerd over winkel locaties
4. Resultaten bevatten trends en vergelijkingen
5. AI identificeert inzichten en aanbevelingen

## 🔒 Beveiliging en Multi-Tenancy Diepteanalyse

Onze implementatie geeft prioriteit aan beveiliging op bedrijfsniveau:

### Row Level Security (RLS)

PostgreSQL RLS zorgt voor data-isolatie:

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

### Gebruikersidentiteitsbeheer

Elke MCP-verbinding bevat:
- **Winkelmanager-ID**: Unieke identifier voor RLS-context
- **Roltoewijzing**: Permissies en toegangslevels
- **Sessiebeheer**: Veilige authenticatietokens
- **Audit Logging**: Volledige toegangslog

### Databeveiliging

Meerdere beveiligingslagen:
- **Verbindingsencryptie**: TLS voor alle databaseverbindingen
- **SQL-injectiepreventie**: Alleen geparametriseerde queries
- **Invoervalidatie**: Uitgebreide validatie van verzoeken
- **Foutafhandeling**: Geen gevoelige data in foutmeldingen

## 🎯 Belangrijkste Leerpunten

Na afronding van deze introductie begrijp je:

✅ **MCP Waardepropositie**: Hoe MCP AI-assistenten en reële data verbindt  
✅ **Zakelijke Context**: Vereisten en uitdagingen van Zava Retail  
✅ **Architectuuroverzicht**: Belangrijke componenten en hun interacties  
✅ **Technologiestack**: Tools en frameworks gebruikt gedurende de cursus  
✅ **Beveiligingsmodel**: Multi-tenant data toegang en bescherming  
✅ **Gebruikspatronen**: Praktijksituaties met query’s en workflows  

## 🚀 Wat Nu?

Klaar om dieper te duiken? Ga verder met:

**[Lab 01: Kernarchitectuurconcepten](../01-Architecture/README.md)**

Leer over MCP-serverarchitectuurpatronen, databaseontwerpprincipes en de gedetailleerde technische implementatie achter onze retail analytics-oplossing.

## 📚 Aanvullende Bronnen

### MCP Documentatie
- [MCP Specificatie](https://modelcontextprotocol.io/docs/) - Officiële protocoldocumentatie
- [MCP voor Beginners](https://aka.ms/mcp-for-beginners) - Uitgebreide MCP leerhandleiding
- [FastMCP Documentatie](https://github.com/modelcontextprotocol/python-sdk) - Python SDK-documentatie

### Database-integratie
- [PostgreSQL Documentatie](https://www.postgresql.org/docs/) - Complete PostgreSQL referentie
- [pgvector Gids](https://github.com/pgvector/pgvector) - Documentatie vector-extensie
- [Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS handleiding

### Azure Services
- [Azure OpenAI Documentatie](https://docs.microsoft.com/azure/cognitive-services/openai/) - Integratie AI-services
- [Azure Database for PostgreSQL](https://docs.microsoft.com/azure/postgresql/) - Beheerde database-service
- [Azure Container Apps](https://docs.microsoft.com/azure/container-apps/) - Serverless containers

---

**Disclaimer**: Dit is een oefening met fictieve retaildata. Volg altijd het data governance- en beveiligingsbeleid van je organisatie bij het implementeren van vergelijkbare oplossingen in productiesystemen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->