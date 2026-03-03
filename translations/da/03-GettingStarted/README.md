## Kom godt i gang  

[![Byg din første MCP-server](../../../translated_images/da/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

Denne sektion består af flere lektioner:

- **1 Din første server**, i denne første lektion lærer du, hvordan du opretter din første server og inspicerer den med inspector-værktøjet, en værdifuld måde at teste og fejlfinde din server på, [til lektionen](01-first-server/README.md)

- **2 Klient**, i denne lektion lærer du, hvordan du skriver en klient, der kan forbinde til din server, [til lektionen](02-client/README.md)

- **3 Klient med LLM**, en endnu bedre måde at skrive en klient på er ved at tilføje en LLM, så den kan "forhandle" med din server om, hvad der skal gøres, [til lektionen](03-llm-client/README.md)

- **4 Forbrug af en server GitHub Copilot Agent-tilstand i Visual Studio Code**. Her kigger vi på at køre vores MCP-server fra Visual Studio Code, [til lektionen](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport er den anbefalede standard for lokal MCP server-til-klient kommunikation, der giver sikker kommunikation baseret på subprocesser med indbygget procesisolation [til lektionen](05-stdio-server/README.md)

- **6 HTTP Streaming med MCP (Streamable HTTP)**. Lær om moderne HTTP streaming transport (den anbefalede tilgang til fjern-MCP-servere ifølge [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http)), fremskridtsnotifikationer, og hvordan du implementerer skalerbare, realtids MCP-servere og klienter ved brug af Streamable HTTP. [til lektionen](06-http-streaming/README.md)

- **7 Udnyttelse af AI Toolkit for VSCode** til at forbruge og teste dine MCP-klienter og servere [til lektionen](07-aitk/README.md)

- **8 Testning**. Her vil vi især fokusere på, hvordan vi kan teste vores server og klient på forskellige måder, [til lektionen](08-testing/README.md)

- **9 Implementering**. Dette kapitel ser på forskellige måder at implementere dine MCP-løsninger på, [til lektionen](09-deployment/README.md)

- **10 Avanceret serverbrug**. Dette kapitel dækker avanceret serverbrug, [til lekelsen](./10-advanced/README.md)

- **11 Auth**. Dette kapitel beskriver, hvordan du tilføjer simpel autentifikation, fra Basic Auth til brug af JWT og RBAC. Du opfordres til at starte her og derefter se på Avancerede emner i kapitel 5 og udføre yderligere sikkerhedshærdning via anbefalingerne i kapitel 2, [til lektionen](./11-simple-auth/README.md)

- **12 MCP Hosts**. Konfigurer og brug populære MCP host-klienter inklusive Claude Desktop, Cursor, Cline og Windsurf. Lær transporttyper og fejlfinding, [til lektionen](./12-mcp-hosts/README.md)

- **13 MCP Inspector**. Fejlret og test dine MCP-servere interaktivt ved hjælp af MCP Inspector-værktøjet. Lær at fejlfinde værktøjer, ressourcer og protokolbeskeder, [til lekelsen](./13-mcp-inspector/README.md)

- **14 Sampling**. Opret MCP-servere, der samarbejder med MCP-klienter om LLM-relaterede opgaver. [til lekelsen](./14-sampling/README.md)

- **15 MCP Apps**. Byg MCP-servere, der også svarer med UI-instruktioner, [til lekelsen](./15-mcp-apps/README.md)

Model Context Protocol (MCP) er en åben protokol, der standardiserer, hvordan applikationer leverer kontekst til LLM'er. Tænk på MCP som en USB-C-port til AI-applikationer – det giver en standardiseret måde at forbinde AI-modeller til forskellige datakilder og værktøjer.

## Læringsmål

Når du er færdig med denne lektion, vil du kunne:

- Opsætte udviklingsmiljøer til MCP i C#, Java, Python, TypeScript og JavaScript
- Bygge og implementere grundlæggende MCP-servere med brugerdefinerede funktioner (ressourcer, prompts og værktøjer)
- Oprette host-applikationer, der forbinder til MCP-servere
- Teste og fejlfinde MCP-implementeringer
- Forstå almindelige opsætningsudfordringer og deres løsninger
- Forbinde dine MCP-implementeringer til populære LLM-tjenester

## Opsætning af dit MCP-miljø

Før du begynder at arbejde med MCP, er det vigtigt at forberede dit udviklingsmiljø og forstå den grundlæggende arbejdsgang. Denne sektion guider dig gennem de indledende opsætningstrin for at sikre en glidende start med MCP.

### Forudsætninger

Før du dykker ned i MCP-udvikling, skal du sikre dig, at du har:

- **Udviklingsmiljø**: Til det valgte sprog (C#, Java, Python, TypeScript eller JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm eller en hvilken som helst moderne kodeeditor
- **Pakkestyringsværktøjer**: NuGet, Maven/Gradle, pip, eller npm/yarn
- **API-nøgler**: Til eventuelle AI-tjenester, du planlægger at bruge i dine host-applikationer


### Officielle SDK'er

I de kommende kapitler vil du se løsninger bygget med Python, TypeScript, Java og .NET. Her er alle de officielt understøttede SDK'er.

MCP leverer officielle SDK'er til flere sprog (i overensstemmelse med [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Vedligeholdes i samarbejde med Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Vedligeholdes i samarbejde med Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Den officielle TypeScript-implementering
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Den officielle Python-implementering (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Den officielle Kotlin-implementering
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Vedligeholdes i samarbejde med Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Den officielle Rust-implementering
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - Den officielle Go-implementering

## Vigtige punkter

- Opsætning af et MCP-udviklingsmiljø er ligetil med sprogspecifikke SDK'er
- Opbygning af MCP-servere involverer at oprette og registrere værktøjer med klare skemaer
- MCP-klienter forbinder til servere og modeller for at udnytte udvidede muligheder
- Test og debugging er essentielle for pålidelige MCP-implementeringer
- Implementeringsmuligheder spænder fra lokal udvikling til cloud-baserede løsninger

## Øvelser

Vi har et sæt eksempler, der supplerer øvelserne, som du vil se i alle kapitler i denne sektion. Derudover har hvert kapitel også deres egne øvelser og opgaver

- [Java-lommeregner](./samples/java/calculator/README.md)
- [.Net lommeregner](../../../03-GettingStarted/samples/csharp)
- [JavaScript lommeregner](./samples/javascript/README.md)
- [TypeScript lommeregner](./samples/typescript/README.md)
- [Python lommeregner](../../../03-GettingStarted/samples/python)

## Yderligere ressourcer

- [Byg agenter ved hjælp af Model Context Protocol på Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Fjern-MCP med Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP-agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Hvad er det næste

Start med den første lektion: [Opret din første MCP-server](01-first-server/README.md)

Når du har gennemført denne modul, fortsæt til: [Modul 4: Praktisk implementering](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->