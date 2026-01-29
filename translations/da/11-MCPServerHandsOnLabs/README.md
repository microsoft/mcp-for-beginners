# 🚀 MCP Server med PostgreSQL - Komplet Læringsguide

## 🧠 Oversigt over MCP Database Integration Læringssti

Denne omfattende læringsguide lærer dig, hvordan du bygger produktionsklare **Model Context Protocol (MCP) servere**, der integrerer med databaser gennem en praktisk implementering af detailanalyse. Du vil lære mønstre i virksomhedsklassen, herunder **Row Level Security (RLS)**, **semantisk søgning**, **Azure AI-integration** og **multi-tenant dataadgang**.

Uanset om du er backend-udvikler, AI-ingeniør eller dataarkitekt, giver denne guide struktureret læring med eksempler fra den virkelige verden og praktiske øvelser, der leder dig gennem følgende MCP-server https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Officielle MCP Ressourcer

- 📘 [MCP Dokumentation](https://modelcontextprotocol.io/) – Detaljerede vejledninger og brugermanualer
- 📜 [MCP Specifikation](https://modelcontextprotocol.io/docs/) – Protokolarkitektur og tekniske referencer
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Open-source SDK'er, værktøjer og kodeeksempler
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – Deltag i diskussioner og bidrag til fællesskabet

## 🧭 MCP Database Integration Læringssti

### 📚 Komplet Læringsstruktur for https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Lab | Emne | Beskrivelse | Link |
|--------|-------|-------------|------|
| **Lab 1-3: Grundlæggende** | | | |
| 00 | [Introduktion til MCP Database Integration](./00-Introduction/README.md) | Oversigt over MCP med databaseintegration og detailanalyse use case | [Start Her](./00-Introduction/README.md) |
| 01 | [Kernearkitektur Koncepter](./01-Architecture/README.md) | Forstå MCP serverarkitektur, databaselag og sikkerhedsmønstre | [Lær](./01-Architecture/README.md) |
| 02 | [Sikkerhed og Multi-Tenancy](./02-Security/README.md) | Row Level Security, autentifikation og multi-tenant dataadgang | [Lær](./02-Security/README.md) |
| 03 | [Opsætning af Miljø](./03-Setup/README.md) | Opsætning af udviklingsmiljø, Docker, Azure ressourcer | [Opsæt](./03-Setup/README.md) |
| **Lab 4-6: Bygning af MCP Server** | | | |
| 04 | [Database Design og Skema](./04-Database/README.md) | PostgreSQL opsætning, detail skemadesign og eksempeldata | [Byg](./04-Database/README.md) |
| 05 | [MCP Server Implementering](./05-MCP-Server/README.md) | Bygning af FastMCP server med databaseintegration | [Byg](./05-MCP-Server/README.md) |
| 06 | [Udvikling af Værktøjer](./06-Tools/README.md) | Oprettelse af databaseforespørgselsværktøjer og skema introspektion | [Byg](./06-Tools/README.md) |
| **Lab 7-9: Avancerede Funktioner** | | | |
| 07 | [Semantisk Søgningsintegration](./07-Semantic-Search/README.md) | Implementering af vektorembeddings med Azure OpenAI og pgvector | [Avancer](./07-Semantic-Search/README.md) |
| 08 | [Test og Fejlfinding](./08-Testing/README.md) | Teststrategier, fejlfindingsværktøjer og valideringsmetoder | [Test](./08-Testing/README.md) |
| 09 | [VS Code Integration](./09-VS-Code/README.md) | Konfiguration af VS Code MCP integration og AI Chat brug | [Integrer](./09-VS-Code/README.md) |
| **Lab 10-12: Produktion og Best Practices** | | | |
| 10 | [Udrulningsstrategier](./10-Deployment/README.md) | Docker udrulning, Azure Container Apps og skaleringsovervejelser | [Udrul](./10-Deployment/README.md) |
| 11 | [Overvågning og Observabilitet](./11-Monitoring/README.md) | Application Insights, logning, performance overvågning | [Overvåg](./11-Monitoring/README.md) |
| 12 | [Best Practices og Optimering](./12-Best-Practices/README.md) | Performance optimering, sikkerhedshærdning og produktionstips | [Optimer](./12-Best-Practices/README.md) |

### 💻 Hvad Du Vil Bygge

Ved afslutningen af denne læringssti vil du have bygget en komplet **Zava Retail Analytics MCP Server** med følgende funktioner:

- **Multi-table detaildatabase** med kundeordrer, produkter og lager
- **Row Level Security** for butiksspecifik dataisolering
- **Semantisk produktsøgning** ved hjælp af Azure OpenAI embeddings
- **VS Code AI Chat integration** til naturlige sprogforespørgsler
- **Produktionsklar udrulning** med Docker og Azure
- **Omfattende overvågning** med Application Insights

## 🎯 Forudsætninger for Læring

For at få mest muligt ud af denne læringssti bør du have:

- **Programmeringserfaring**: Kendskab til Python (foretrukket) eller lignende sprog
- **Databasekendskab**: Grundlæggende forståelse af SQL og relationelle databaser
- **API-koncepter**: Forståelse af REST API'er og HTTP-koncepter
- **Udviklingsværktøjer**: Erfaring med kommandolinje, Git og kodeeditorer
- **Cloud Basics**: (Valgfrit) Grundlæggende kendskab til Azure eller lignende cloud-platforme
- **Docker Kendskab**: (Valgfrit) Forståelse af containeriseringskoncepter

### Nødvendige Værktøjer

- **Docker Desktop** - Til at køre PostgreSQL og MCP serveren
- **Azure CLI** - Til udrulning af cloud-ressourcer
- **VS Code** - Til udvikling og MCP integration
- **Git** - Til versionskontrol
- **Python 3.8+** - Til MCP serverudvikling

## 📚 Studieguide & Ressourcer

Denne læringssti inkluderer omfattende ressourcer til at hjælpe dig med at navigere effektivt:

### Studieguide

Hver lab inkluderer:
- **Klare læringsmål** - Hvad du vil opnå
- **Trin-for-trin instruktioner** - Detaljerede implementeringsvejledninger
- **Kodeeksempler** - Arbejdseksempler med forklaringer
- **Øvelser** - Praktiske øvelsesmuligheder
- **Fejlfindingsvejledninger** - Almindelige problemer og løsninger
- **Yderligere ressourcer** - Yderligere læsning og udforskning

### Forudsætningskontrol

Før du starter hver lab, vil du finde:
- **Nødvendig viden** - Hvad du bør vide på forhånd
- **Opsætningsvalidering** - Hvordan du verificerer dit miljø
- **Tidsestimater** - Forventet gennemførselstid
- **Læringsresultater** - Hvad du vil vide efter afslutning

### Anbefalede Læringsstier

Vælg din sti baseret på dit erfaringsniveau:

#### 🟢 **Begyndersti** (Ny til MCP)
1. Sørg for, at du har gennemført 0-10 af [MCP for Begyndere](https://aka.ms/mcp-for-beginners) først
2. Gennemfør labs 00-03 for at styrke din forståelse af grundlæggende
3. Følg labs 04-06 for praktisk opbygning
4. Prøv labs 07-09 for praktisk anvendelse

#### 🟡 **Mellemsti** (Noget MCP Erfaring)
1. Gennemgå labs 00-01 for database-specifikke koncepter
2. Fokuser på labs 02-06 for implementering
3. Dyk dybt ned i labs 07-12 for avancerede funktioner

#### 🔴 **Avanceret sti** (Erfaren med MCP)
1. Skim labs 00-03 for kontekst
2. Fokuser på labs 04-09 for databaseintegration
3. Koncentrer dig om labs 10-12 for produktionsudrulning

## 🛠️ Sådan Bruger Du Denne Læringssti Effektivt

### Sekventiel Læring (Anbefalet)

Arbejd gennem labs i rækkefølge for en omfattende forståelse:

1. **Læs oversigten** - Forstå hvad du vil lære
2. **Tjek forudsætninger** - Sørg for, at du har den nødvendige viden
3. **Følg trin-for-trin vejledninger** - Implementer mens du lærer
4. **Gennemfør øvelser** - Styrk din forståelse
5. **Gennemgå nøglepunkter** - Konsolider læringsresultater

### Målrettet Læring

Hvis du har brug for specifikke færdigheder:

- **Databaseintegration**: Fokuser på labs 04-06
- **Sikkerhedsimplementering**: Koncentrer dig om labs 02, 08, 12
- **AI/Semantisk Søgning**: Dyk dybt ned i lab 07
- **Produktionsudrulning**: Studér labs 10-12

### Praktisk Øvelse

Hver lab inkluderer:
- **Arbejdende kodeeksempler** - Kopiér, modificér og eksperimentér
- **Virkelighedsnære scenarier** - Praktiske detailanalyse use cases
- **Progressiv kompleksitet** - Byg fra simpelt til avanceret
- **Valideringstrin** - Bekræft, at din implementering fungerer

## 🌟 Fællesskab og Support

### Få Hjælp

- **Azure AI Discord**: [Deltag for ekspertstøtte](https://discord.com/invite/ByRwuEEgH4)
- **GitHub Repo og Implementerings Eksempel**: [Udrulnings Eksempel og Ressourcer](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Community**: [Deltag i bredere MCP diskussioner](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Klar til at Starte?

Begynd din rejse med **[Lab 00: Introduktion til MCP Database Integration](./00-Introduction/README.md)**

---

*Bliv ekspert i at bygge produktionsklare MCP servere med databaseintegration gennem denne omfattende, praktiske læringsoplevelse.*

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.