# 🚀 MCP-server med PostgreSQL - Komplett lärandeguide

## 🧠 Översikt över MCP-databasintegrationslärandevägen

Denna omfattande lärandeguide lär dig hur du bygger produktionsklara **Model Context Protocol (MCP) servrar** som integreras med databaser genom en praktisk implementering för detaljhandelns analys. Du lär dig företagsklassmönster inklusive **Row Level Security (RLS)**, **semantisk sökning**, **Azure AI-integration** och **flerhyresgästsdataåtkomst**.

Oavsett om du är backendutvecklare, AI-ingenjör eller dataarkitekt, erbjuder denna guide strukturerat lärande med verkliga exempel och praktiska övningar som går igenom följande MCP-server https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail.

## 🔗 Officiella MCP-resurser

- 📘 [MCP Dokumentation](https://modelcontextprotocol.io/) – Detaljerade handledningar och användarguider
- 📜 [MCP Specifikation (2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/) – Protokollarkitektur och tekniska referenser
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – Öppen källkod SDK:er, verktyg och kodexempel
- 🌐 [MCP Community](https://github.com/orgs/modelcontextprotocol/discussions) – Delta i diskussioner och bidra till communityn
- 🔒 [OWASP MCP Top 10](https://microsoft.github.io/mcp-azure-security-guide/mcp/) – Säkerhetsbästa praxis och riskminimeringar


## 🧭 MCP-databasintegrationslärandeväg

### 📚 Komplett lärandestruktur för https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail

| Laboratorium | Ämne | Beskrivning | Länk |
|--------|-------|-------------|------|
| **Lab 1-3: Grunder** | | | |
| 00 | [Introduktion till MCP-databasintegration](./00-Introduction/README.md) | Översikt av MCP med databasintegration och detaljhandelsanalysfall | [Börja här](./00-Introduction/README.md) |
| 01 | [Kärnarkitekturkoncept](./01-Architecture/README.md) | Förståelse för MCP-serverarkitektur, databaslager och säkerhetsmönster | [Läs](./01-Architecture/README.md) |
| 02 | [Säkerhet och flerhyresgästhantering](./02-Security/README.md) | Row Level Security, autentisering och flerhyresgästsdataåtkomst | [Läs](./02-Security/README.md) |
| 03 | [Miljöinställning](./03-Setup/README.md) | Sätta upp utvecklingsmiljö, Docker, Azure-resurser | [Konfigurera](./03-Setup/README.md) |
| **Lab 4-6: Bygga MCP-servern** | | | |
| 04 | [Databasdesign och schema](./04-Database/README.md) | PostgreSQL-inställning, detaljhandelsschema och exempeldata | [Bygg](./04-Database/README.md) |
| 05 | [MCP-serverimplementering](./05-MCP-Server/README.md) | Bygga FastMCP-servern med databasintegration | [Bygg](./05-MCP-Server/README.md) |
| 06 | [Verktygsutveckling](./06-Tools/README.md) | Skapa databasfrågeverktyg och schemaintrång | [Bygg](./06-Tools/README.md) |
| **Lab 7-9: Avancerade funktioner** | | | |
| 07 | [Semantisk sökntegration](./07-Semantic-Search/README.md) | Implementera vektorinkapslingar med Azure OpenAI och pgvector | [Fördjupa](./07-Semantic-Search/README.md) |
| 08 | [Testning och felsökning](./08-Testing/README.md) | Teststrategier, felsökningsverktyg och valideringsmetoder | [Testa](./08-Testing/README.md) |
| 09 | [VS Code-integrering](./09-VS-Code/README.md) | Konfigurera VS Code MCP-integration och AI-chat-användning | [Integrera](./09-VS-Code/README.md) |
| **Lab 10-12: Produktion och bästa praxis** | | | |
| 10 | [Distribueringsstrategier](./10-Deployment/README.md) | Docker-distribution, Azure Container Apps och skalningsöverväganden | [Distribuera](./10-Deployment/README.md) |
| 11 | [Övervakning och observation](./11-Monitoring/README.md) | Application Insights, loggning, prestandaövervakning | [Övervaka](./11-Monitoring/README.md) |
| 12 | [Bästa praxis och optimering](./12-Best-Practices/README.md) | Prestandaoptimering, säkerhetshärdning och tips för produktion | [Optimera](./12-Best-Practices/README.md) |

### 💻 Vad du kommer att bygga

I slutet av denna lärandeväg kommer du att ha byggt en komplett **Zava Retail Analytics MCP-server** med följande funktioner:

- **Multitabells detaljhandelsdatabas** med kundorder, produkter och lager
- **Row Level Security** för dataisolering baserad på butik
- **Semantisk produktsökning** med Azure OpenAI-inkapslingar
- **VS Code AI Chat-integration** för naturliga språkfrågor
- **Produktionsklar distribution** med Docker och Azure
- **Omfattande övervakning** med Application Insights

## 🎯 Förkunskapskrav för lärande

För att få ut det mesta av denna lärandeväg bör du ha:

- **Programmeringserfarenhet**: Bekantskap med Python (föredras) eller liknande språk
- **Databaskunskap**: Grundläggande förståelse av SQL och relationsdatabaser
- **API-koncept**: Förståelse för REST API:er och HTTP-koncept
- **Utvecklingsverktyg**: Erfarenhet av kommandorad, Git och kodredigerare
- **Molnbasics**: (Valfritt) Grundläggande kunskap om Azure eller liknande molnplattformar
- **Docker-kunskap**: (Valfritt) Förståelse för containerisering

### Krävda verktyg

- **Docker Desktop** - För att köra PostgreSQL och MCP-servern
- **Azure CLI** - För molnresursdistribution
- **VS Code** - För utveckling och MCP-integrering
- **Git** - För versionskontroll
- **Python 3.8+** - För MCP-serverutveckling

## 📚 Studieguides & resurser

Denna lärandeväg inkluderar omfattande resurser för att hjälpa dig navigera effektivt:

### Studieguides

Varje labb inkluderar:
- **Klara lärandemål** - Vad du kommer att uppnå
- **Steg-för-steg-instruktioner** - Detaljerade implementeringsguider
- **Kodexempel** - Fungerande provexempel med förklaringar
- **Övningar** - Praktiska övningar
- **Felsökningsguider** - Vanliga problem och lösningar
- **Ytterligare resurser** - Vidare läsning och utforskning

### Förkunskapskontroll

Innan varje labb hittar du:
- **Nödvändig kunskap** - Vad du bör veta i förväg
- **Miljövalidering** - Hur du verifierar din miljö
- **Tidsuppskattningar** - Förväntad tid för slutförande
- **Läranderesultat** - Vad du kommer att kunna efter slutförande

### Rekommenderade lärandevägar

Välj din väg beroende på din erfarenhetsnivå:

#### 🟢 **Nybörjarväg** (Ny till MCP)
1. Se till att du först har genomfört 0-10 av [MCP för nybörjare](https://aka.ms/mcp-for-beginners)
2. Slutför labbar 00-03 för att förstärka dina grundläggande kunskaper
3. Följ labbar 04-06 för praktisk byggande
4. Prova labbar 07-09 för praktisk användning

#### 🟡 **Mellanväg** (Viss MCP-erfarenhet)
1. Granska labbar 00-01 för databasspecifika koncept
2. Fokusera på labbar 02-06 för implementering
3. Fördjupa dig i labbar 07-12 för avancerade funktioner

#### 🔴 **Avancerad väg** (Erfaren med MCP)
1. Skumma igenom labbar 00-03 för kontext
2. Fokusera på labbar 04-09 för databasintegration
3. Koncentrera dig på labbar 10-12 för produktionsdistribution

## 🛠️ Hur du använder denna lärandeväg effektivt

### Sekventiellt lärande (Rekommenderat)

Arbeta igenom labbar i ordning för en heltäckande förståelse:

1. **Läs översikten** - Förstå vad du kommer att lära dig
2. **Kontrollera förkunskaper** - Säkerställ att du har nödvändig kunskap
3. **Följ steg-för-steg-guider** - Implementera medan du lär dig
4. **Slutför övningar** - Förstärk din förståelse
5. **Granska viktiga slutsatser** - Förankra läranderesultaten

### Målstyrt lärande

Om du behöver specifika färdigheter:

- **Databasintegration**: Fokusera på labbar 04-06
- **Säkerhetsimplementering**: Koncentrera på labbar 02, 08, 12
- **AI/Semantisk sökning**: Fördjupa dig i labb 07
- **Produktionsdistribution**: Studera labbar 10-12

### Praktiska övningar

Varje labb innehåller:
- **Fungerande kodexempel** - Kopiera, modifiera och experimentera
- **Verkliga scenarier** - Praktiska detaljhandelsanalysfall
- **Progressiv komplexitet** - Bygger från enkelt till avancerat
- **Valideringssteg** - Verifiera att din implementering fungerar

## 🌟 Community och support

### Få hjälp

- **Azure AI Discord**: [Gå med för experthjälp](https://discord.com/invite/ByRwuEEgH4)
- **GitHub-repo och implementationsprov**: [Distributionsprov och resurser](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/)
- **MCP Community**: [Delta i bredare MCP-diskussioner](https://github.com/orgs/modelcontextprotocol/discussions)

## 🚀 Redo att börja?

Börja din resa med **[Lab 00: Introduktion till MCP-databasintegration](./00-Introduction/README.md)**

---

*Behärska att bygga produktionsklara MCP-servrar med databasintegration genom denna omfattande, praktiska lärandeupplevelse.*

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->