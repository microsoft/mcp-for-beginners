# 🚀 MCP Server met PostgreSQL - Complete Leerhandleiding

## 🧠 Overzicht van het MCP Database Integratie Leerpad

Deze uitgebreide leerhandleiding leert je hoe je productieklare **Model Context Protocol (MCP) servers** bouwt die integreren met databases via een praktische implementatie voor retail analytics. Je leert enterprise-grade patronen waaronder **Row Level Security (RLS)**, **semantisch zoeken**, **Azure AI integratie**, en **multi-tenant data toegang**.

Of je nu een backendontwikkelaar, AI-engineer of data-architect bent, deze gids biedt gestructureerd leren met praktijkvoorbeelden en hands-on oefeningen die je begeleiden door de volgende MCP server https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Officiële MCP Bronnen

- 📘 [MCP Documentatie](https://modelcontextprotocol.io/) – Gedetailleerde tutorials en gebruikershandleidingen
- 📜 [MCP Specificatie (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protocolarchitectuur en technische referenties
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Open-source SDK’s, tools, en codevoorbeelden
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – Neem deel aan discussies en draag bij aan de community
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Best practices voor beveiliging en risicobeperking


## 🧭 MCP Database Integratie Leerpad

### 📚 Complete Leerstructuur voor https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Onderwerp | Beschrijving | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Basisprincipes** | | | |
| 00 | [Introductie tot MCP Database Integratie](./00-Introduction/README.md) | Overzicht van MCP met database-integratie en retail analytics use case | [Begin Hier](./00-Introduction/README.md) |
| 01 | [Kernarchitectuur Concepten](./01-Architecture/README.md) | Begrip van MCP serverarchitectuur, databaselagen, en beveiligingspatronen | [Leer](./01-Architecture/README.md) |
| 02 | [Beveiliging en Multi-Tenancy](./02-Security/README.md) | Row Level Security, authenticatie, en multi-tenant data toegang | [Leer](./02-Security/README.md) |
| 03 | [Omgevingsconfiguratie](./03-Setup/README.md) | Het opzetten van ontwikkelomgeving, Docker, Azure resources | [Installeer](./03-Setup/README.md) |
| **Lab 4-6: Bouwen van de MCP Server** | | | |
| 04 | [Databaseontwerp en Schema](./04-Database/README.md) | PostgreSQL setup, retail schema ontwerp, en voorbeelddata | [Bouw](./04-Database/README.md) |
| 05 | [MCP Server Implementatie](./05-MCP-Server/README.md) | Het bouwen van de FastMCP server met database-integratie | [Bouw](./05-MCP-Server/README.md) |
| 06 | [Toolontwikkeling](./06-Tools/README.md) | Creëren van database query tools en schema-introspectie | [Bouw](./06-Tools/README.md) |
| **Lab 7-9: Geavanceerde Functies** | | | |
| 07 | [Integratie van Semantisch Zoeken](./07-Semantic-Search/README.md) | Implementatie van vector embeddings met Azure OpenAI en pgvector | [Versterk](./07-Semantic-Search/README.md) |
| 08 | [Testen en Debuggen](./08-Testing/README.md) | Teststrategieën, debugging tools, en validatiebenaderingen | [Test](./08-Testing/README.md) |
| 09 | [VS Code Integratie](./09-VS-Code/README.md) | Configuratie van VS Code MCP integratie en AI Chat gebruik | [Integreer](./09-VS-Code/README.md) |
| **Lab 10-12: Productie en Best Practices** | | | |
| 10 | [Uitrolstrategieën](./10-Deployment/README.md) | Docker-uitrol, Azure Container Apps, en schaaloverwegingen | [Rol Uit](./10-Deployment/README.md) |
| 11 | [Monitoring en Observeerbaarheid](./11-Monitoring/README.md) | Application Insights, logging, prestatiemonitoring | [Monitor](./11-Monitoring/README.md) |
| 12 | [Best Practices en Optimalisatie](./12-Best-Practices/README.md) | Prestatieoptimalisatie, beveiligingsversteviging, en productietips | [Optimaliseer](./12-Best-Practices/README.md) |

### 💻 Wat Je Gaat Bouwen

Aan het einde van dit leerpad heb je een complete **Zava Retail Analytics MCP Server** gebouwd met:

- **Meerdere tabellen retaildatabase** met klantorders, producten, en voorraad
- **Row Level Security** voor winkelgebonden data-isolatie
- **Semantisch product zoeken** met Azure OpenAI embeddings
- **VS Code AI Chat integratie** voor natuurlijke taalvragen
- **Productieklaar uitrollen** met Docker en Azure
- **Uitgebreide monitoring** met Application Insights

## 🎯 Vereisten voor het Leren

Om het meeste uit dit leerpad te halen, dien je te beschikken over:

- **Programmeervaardigheden**: Vertrouwdheid met Python (voorkeur) of vergelijkbare talen
- **Databasekennis**: Basiskennis van SQL en relationele databases
- **API Concepten**: Begrip van REST API’s en HTTP-concepten
- **Ontwikkeltools**: Ervaring met command line, Git, en code-editors
- **Cloudbasiskennis**: (Optioneel) Basiskennis van Azure of vergelijkbare cloudplatformen
- **Docker Bekendheid**: (Optioneel) Begrip van containerisatieconcepten

### Vereiste Tools

- **Docker Desktop** - Voor het draaien van PostgreSQL en de MCP server
- **Azure CLI** - Voor cloud resource uitrol
- **VS Code** - Voor ontwikkeling en MCP integratie
- **Git** - Voor versiebeheer
- **Python 3.8+** - Voor MCP serverontwikkeling

## 📚 Studiegids & Bronnen

Dit leerpad bevat uitgebreide bronnen om je effectief te begeleiden:

### Studiegids

Elke lab bevat:
- **Duidelijke leerdoelen** - Wat je zult bereiken
- **Stapsgewijze instructies** - Gedetailleerde implementatiehandleidingen
- **Codevoorbeelden** - Werkende voorbeelden met uitleg
- **Oefeningen** - Praktijkmogelijkheden
- **Probleemoplossingsgids** - Veelvoorkomende problemen en oplossingen
- **Extra bronnen** - Verdere literatuur en verkenning

### Vereisten Check

Voor aanvang van elke lab vind je:
- **Benodigde kennis** - Wat je vooraf moet weten
- **Configuratievalidatie** - Hoe je je omgeving controleert
- **Tijdsindicaties** - Verwachte doorlooptijd
- **Leerresultaten** - Wat je weet na afronding

### Aanbevolen Leerwegen

Kies je pad op basis van je ervaringsniveau:

#### 🟢 **Beginner Pad** (Nieuw bij MCP)
1. Zorg dat je eerst 0-10 van [MCP voor Beginners](https://aka.ms/mcp-for-beginners) hebt afgerond
2. Voltooi labs 00-03 om je basiskennis te versterken
3. Volg labs 04-06 voor hands-on bouwen
4. Probeer labs 07-09 voor praktische toepassingen

#### 🟡 **Intermediate Pad** (Enige ervaring met MCP)
1. Herzie labs 00-01 voor databasespecifieke concepten
2. Focus op labs 02-06 voor implementatie
3. Duik diep in labs 07-12 voor geavanceerde functies

#### 🔴 **Geavanceerd Pad** (Ervaren met MCP)
1. Bekijk labs 00-03 voor context
2. Focus op labs 04-09 voor database-integratie
3. Richt je op labs 10-12 voor productie-uitrol

## 🛠️ Hoe Gebruik Je Dit Leerpad Effectief

### Opeenvolgend Leren (Aanbevolen)

Volg de labs op volgorde voor een volledig begrip:

1. **Lees het overzicht** - Begrijp wat je zult leren
2. **Controleer vereisten** - Zorg dat je benodigde kennis hebt
3. **Volg stapsgewijze handleidingen** - Implementeer terwijl je leert
4. **Maak oefeningen** - Versterk je begrip
5. **Bekijk kernpunten** - Veranker leerresultaten

### Gericht Leren

Als je specifieke vaardigheden nodig hebt:

- **Database Integratie**: Focus op labs 04-06
- **Beveiligingsimplementatie**: Concentreer je op labs 02, 08, 12
- **AI/Semantisch Zoeken**: Duik dieper in lab 07
- **Productie-uitrol**: Bestudeer labs 10-12

### Hands-on Oefeningen

Elke lab bevat:
- **Werkende codevoorbeelden** - Kopieer, pas aan, en experimenteer
- **Praktijkvoorbeelden uit de echte wereld** - Praktische retail analytics use cases
- **Oplopende complexiteit** - Bouwen van simpel naar geavanceerd
- **Validatiestappen** - Controleer dat je implementatie werkt

## 🌟 Community en Ondersteuning

### Hulp Krijgen

- **Azure AI Discord**: [Word lid voor deskundige ondersteuning](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repo en Implementatievoorbeeld**: [Uitrolvoorbeeld en bronnen](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Community**: [Doe mee aan bredere MCP-discussies](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Klaar om te Beginnen?

Begin je reis met **[Lab 00: Introductie tot MCP Database Integratie](./00-Introduction/README.md)**

---

*Beheers het bouwen van productieklare MCP servers met database-integratie via deze uitgebreide, hands-on leerervaring.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->