# 🚀 MCP Server med PostgreSQL - Komplett Læringsvejledning

## 🧠 Oversigt over MCP Databaseintegrations Læringsvej

Denne omfattende læringsvejledning lærer dig, hvordan du bygger produktionsklare **Model Context Protocol (MCP) servere**, der integreres med databaser gennem en praktisk detailanalytisk implementering. Du vil lære virksomhedsklare mønstre inklusive **Row Level Security (RLS)**, **semantisk søgning**, **Azure AI-integration** og **multi-lejer dataadgang**.

Uanset om du er backend-udvikler, AI-ingeniør eller dataarkitekt, giver denne vejledning struktureret læring med virkelige eksempler og praktiske øvelser, som fører dig gennem følgende MCP-server https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Officielle MCP Ressourcer

- 📘 [MCP Dokumentation](https://modelcontextprotocol.io/) – Detaljerede vejledninger og brugerguides
- 📜 [MCP Specifikation (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokolarkitektur og tekniske referencer
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Open-source SDK'er, værktøjer og kodeeksempler
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – Deltag i diskussioner og bidrag til fællesskabet
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Sikkerhedspraksis og risikomitigering


## 🧭 MCP Databaseintegrations Læringsvej

### 📚 Komplet Læringsstruktur for https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Emne | Beskrivelse | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Grundlæggende** | | | |
| 00 | [Introduktion til MCP Databaseintegration](./00-Introduction/README.md) | Oversigt over MCP med databaseintegration og detailanalytisk brugsscenario | [Start her](./00-Introduction/README.md) |
| 01 | [Kernearkitektur Koncepter](./01-Architecture/README.md) | Forståelse af MCP serverarkitektur, databaselag og sikkerhedsmønstre | [Lær](./01-Architecture/README.md) |
| 02 | [Sikkerhed og Multi-lejer](./02-Security/README.md) | Row Level Security, autentifikation og multi-lejer dataadgang | [Lær](./02-Security/README.md) |
| 03 | [Miljøopsætning](./03-Setup/README.md) | Opsætning af udviklingsmiljø, Docker, Azure-ressourcer | [Opsæt](./03-Setup/README.md) |
| **Lab 4-6: Byg MCP Serveren** | | | |
| 04 | [Database Design og Skema](./04-Database/README.md) | PostgreSQL opsætning, detail-skema design og eksempeldata | [Byg](./04-Database/README.md) |
| 05 | [MCP Server Implementering](./05-MCP-Server/README.md) | Bygning af FastMCP server med databaseintegration | [Byg](./05-MCP-Server/README.md) |
| 06 | [Værktøjsudvikling](./06-Tools/README.md) | Skabelse af databaseforespørgselsværktøjer og skemainspektion | [Byg](./06-Tools/README.md) |
| **Lab 7-9: Avancerede Funktioner** | | | |
| 07 | [Semantisk Søgning Integration](./07-Semantic-Search/README.md) | Implementering af vektor indlejring med Azure OpenAI og pgvector | [Avanceret](./07-Semantic-Search/README.md) |
| 08 | [Test og Fejlfinding](./08-Testing/README.md) | Teststrategier, fejlfinding og valideringsmetoder | [Test](./08-Testing/README.md) |
| 09 | [VS Code Integration](./09-VS-Code/README.md) | Konfiguration af VS Code MCP-integration og AI Chat brug | [Integrér](./09-VS-Code/README.md) |
| **Lab 10-12: Produktion og Bedste Praksis** | | | |
| 10 | [Deploymentsstrategier](./10-Deployment/README.md) | Docker deployment, Azure Container Apps og skaleringsovervejelser | [Deploy](./10-Deployment/README.md) |
| 11 | [Overvågning og Observabilitet](./11-Monitoring/README.md) | Application Insights, logning, ydelsesovervågning | [Overvåg](./11-Monitoring/README.md) |
| 12 | [Bedste Praksis og Optimering](./12-Best-Practices/README.md) | Ydelsesoptimering, sikkerhedshærdning og produktionstips | [Optimér](./12-Best-Practices/README.md) |

### 💻 Hvad Du Vil Bygge

Ved afslutningen af denne læringsvej vil du have bygget en komplet **Zava Retail Analytics MCP Server**, der indeholder:

- **Multi-tabel detaildatabase** med kundeordrer, produkter og inventar
- **Row Level Security** for butikbaseret dataisolation
- **Semantisk produktsøgning** ved brug af Azure OpenAI embeddings
- **VS Code AI Chat integration** for forespørgsler i naturligt sprog
- **Produktionsklar deployment** med Docker og Azure
- **Omfattende overvågning** med Application Insights

## 🎯 Forudsætninger for Læring

For at få mest muligt ud af denne læringsvej bør du have:

- **Programmeringserfaring**: Fortrolighed med Python (foretrukket) eller lignende sprog
- **Databasekendskab**: Grundlæggende forståelse af SQL og relationelle databaser
- **API-koncepter**: Forståelse af REST APIs og HTTP-konsepter
- **Udviklingsværktøjer**: Erfaring med kommandolinje, Git og kodeeditorer
- **Cloud Grundlæggende**: (Valgfrit) Grundlæggende kendskab til Azure eller lignende cloud platforme
- **Docker Fortrolighed**: (Valgfrit) Forståelse af containeriseringskoncepter

### Nødvendige Værktøjer

- **Docker Desktop** - Til kørsel af PostgreSQL og MCP serveren
- **Azure CLI** - Til udrulning af cloud ressourcer
- **VS Code** - Til udvikling og MCP-integration
- **Git** - Til versionskontrol
- **Python 3.8+** - Til MCP serverudvikling

## 📚 Studieguide & Ressourcer

Denne læringsvej inkluderer omfattende ressourcer til effektiv navigation:

### Studieguide

Hver lab inkluderer:
- **Klare læringsmål** - Hvad du opnår
- **Trin-for-trin instruktioner** - Detaljerede implementationsvejledninger
- **Kodeeksempler** - Fungerende eksempler med forklaringer
- **Øvelser** - Praktiske øvelser
- **Fejlfinding** - Almindelige problemer og løsninger
- **Yderligere ressourcer** - Videre læsning og udforskning

### Forudsætningskontrol

Før start af hver lab finder du:
- **Nødvendig viden** - Hvad du bør kende på forhånd
- **Opsætningsvalidering** - Hvordan du verificerer dit miljø
- **Tidsestimeringer** - Forventet gennemførelse tid
- **Læringsudbytte** - Hvad du ved efter gennemførelse

### Anbefalede læringsveje

Vælg din vej baseret på dit erfaringsniveau:

#### 🟢 **Begyndervenlig Vej** (Ny til MCP)
1. Sørg for at have gennemført 0-10 af [MCP for Beginners](https://aka.ms/mcp-for-beginners) først
2. Gennemfør labs 00-03 for at styrke grundlaget
3. Følg labs 04-06 for praktisk bygning
4. Prøv labs 07-09 for praktisk brug

#### 🟡 **Mellemliggende Vej** (Nogen MCP Erfaring)
1. Gennemgå labs 00-01 for databasespecifikke koncepter
2. Fokusér på labs 02-06 for implementering
3. Dyk dybt i labs 07-12 for avancerede funktioner

#### 🔴 **Avanceret Vej** (Erfaren med MCP)
1. Skim labs 00-03 for kontekst
2. Fokusér på labs 04-09 for databaseintegration
3. Koncentrér dig om labs 10-12 for produktionsudrulning

## 🛠️ Sådan bruger du denne læringsvej effektivt

### Sekventiel Læring (Anbefalet)

Arbejd gennem labs i rækkefølge for en fuldstændig forståelse:

1. **Læs oversigten** - Forstå hvad du vil lære
2. **Tjek forudsætninger** - Sørg for at have nødvendig viden
3. **Følg trin-for-trin guider** - Implementer mens du lærer
4. **Gennemfør øvelser** - Styrk din forståelse
5. **Gennemgå nøglepointer** - Konsolider læringsudbyttet

### Målrettet Læring

Hvis du har brug for specifikke færdigheder:

- **Databaseintegration**: Fokusér på labs 04-06
- **Sikkerhedsimplementering**: Koncentrér dig om labs 02, 08, 12
- **AI/Semantisk Søgning**: Dyk ned i lab 07
- **Produktionsudrulning**: Studér labs 10-12

### Praktisk Øvelse

Hver lab inkluderer:
- **Fungerende kodeeksempler** - Kopiér, modificér og eksperimentér
- **Virkelighedsnære scenarier** - Praktiske detailanalytiske brugssager
- **Progressiv kompleksitet** - Byg ud fra simpelt til avanceret
- **Valideringstrin** - Bekræft at din implementering virker

## 🌟 Fællesskab og Support

### Få hjælp

- **Azure AI Discord**: [Deltag for eksperthjælp](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repo og Implementerings Eksempel**: [Deploymentsample og Ressourcer](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Community**: [Deltag i bredere MCP diskussioner](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Klar til at starte?

Begynd din rejse med **[Lab 00: Introduktion til MCP Databaseintegration](./00-Introduction/README.md)**

---

*Mestring af at bygge produktionsklare MCP servere med databaseintegration gennem denne omfattende, praktiske læringserfaring.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->