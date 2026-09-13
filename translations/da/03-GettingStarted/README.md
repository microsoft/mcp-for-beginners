## Kom godt i gang  

[![Byg din første MCP-server](../../../translated_images/da/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(Klik på billedet ovenfor for at se videoen til denne lektion)_

Denne sektion består af flere lektioner:

- **1 Din første server**, i denne første lektion lærer du, hvordan du opretter din første server og inspicerer den med inspektørværktøjet, en værdifuld metode til at teste og fejlfinde din server, [til lektionen](01-first-server/README.md)

- **2 Klient**, i denne lektion lærer du, hvordan du skriver en klient, der kan oprette forbindelse til din server, [til lektionen](02-client/README.md)

- **3 Klient med LLM**, en endnu bedre måde at skrive en klient på er ved at tilføje en LLM, så den kan "forhandle" med din server om, hvad der skal gøres, [til lektionen](03-llm-client/README.md)

- **4 Forbrug af en server GitHub Copilot Agent-tilstand i Visual Studio Code**. Her ser vi på at køre vores MCP-server fra Visual Studio Code, [til lektionen](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport er den anbefalede standard for lokal MCP server-til-klient kommunikation, som giver sikker subprocess-baseret kommunikation med indbygget procesisolation [til lektionen](05-stdio-server/README.md)

- **6 HTTP Streaming med MCP (Streamable HTTP)**. Lær om den standard
	fjerntransporter i [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http),
	samt den ældre session-baserede implementering bevaret i lektionen.
	[til lektionen](06-http-streaming/README.md)

- **7 Brug af AI Toolkit til VSCode** for at forbruge og teste dine MCP-klienter og -servere [til lektionen](07-aitk/README.md)

- **8 Testning**. Her vil vi især fokusere på, hvordan vi kan teste vores server og klient på forskellige måder, [til lektionen](08-testing/README.md)

- **9 Udrulning**. Dette kapitel ser på forskellige måder at udrulle dine MCP-løsninger på, [til lektionen](09-deployment/README.md)

- **10 Avanceret serverbrug**. Dette kapitel dækker avanceret serverbrug, [til lektionen](./10-advanced/README.md)

- **11 Auth**. Dette kapitel beskriver, hvordan man tilføjer simpel autentifikation, fra Basic Auth til brug af JWT og RBAC. Det anbefales at starte her og derefter se på Avancerede Emner i Kapitel 5 og udføre yderligere sikkerhedshærdning via anbefalinger i Kapitel 2, [til lektionen](./11-simple-auth/README.md)

- **12 MCP Hosts**. Konfigurer og brug populære MCP-værtsklienter inklusive Claude Desktop, Cursor, Cline og Windsurf. Lær om transporttyper og fejlfinding, [til lektionen](./12-mcp-hosts/README.md)

- **13 MCP Inspector**. Fejlret og test dine MCP-servere interaktivt ved hjælp af MCP Inspector-værktøjet. Lær om fejlfinding, ressourcer og protokolbeskeder, [til lektionen](./13-mcp-inspector/README.md)

- **14 Sampling**. Lær den ældre Sampling-primitiv fra `2025-11-25` og
	om hvordan man migrerer nye designs til direkte LLM-udbyderintegration. Sampling er
	deprecieret i MCP `2026-07-28`. [til lektionen](./14-sampling/README.md)

- **15 MCP Apps**. Byg MCP-servere, der også svarer med UI-instruktioner, [til lektionen](./15-mcp-apps/README.md)

Model Context Protocol (MCP) er en åben protokol, der standardiserer, hvordan applikationer leverer kontekst til LLM'er. Tænk på MCP som en USB-C-port for AI-applikationer - det giver en standardiseret måde at forbinde AI-modeller til forskellige datakilder og værktøjer.

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Opsætte udviklingsmiljøer for MCP i C#, Java, Python, TypeScript og JavaScript
- Bygge og udrulle grundlæggende MCP-servere med brugerdefinerede funktioner (ressourcer, prompts og værktøjer)
- Oprette vært-applikationer, der opretter forbindelse til MCP-servere
- Teste og fejlfinde MCP-implementeringer
- Forstå almindelige opsætningsudfordringer og deres løsninger
- Forbinde dine MCP-implementeringer til populære LLM-tjenester

## Opsætning af dit MCP-miljø

Før du begynder at arbejde med MCP, er det vigtigt at forberede dit udviklingsmiljø og forstå den grundlæggende arbejdsproces. Denne sektion vil guide dig gennem de indledende opsætningsskridt for at sikre en glidende start med MCP.

### Forudsætninger

Før du går i gang med MCP-udvikling, skal du sikre dig, at du har:

- **Udviklingsmiljø**: For det valgte sprog (C#, Java, Python, TypeScript eller JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm eller en moderne kodeeditor
- **Pakkehåndtering**: NuGet, Maven/Gradle, pip eller npm/yarn
- **API-nøgler**: Til eventuelle AI-tjenester, du planlægger at bruge i dine vært-applikationer


### Officielle SDK'er

I de kommende kapitler vil du se løsninger bygget med Python, TypeScript,
Java og .NET. Her er de officielle SDK'er.

SDK-support til MCP `2026-07-28` udrulles uafhængigt efter sprog.
Før du kører et eksempel, skal du tjekke dets pakkeversion og SDK'ens udgivelsesnoter
for understøttede protokolrevisioner. Se den
[officielle SDK-liste](https://modelcontextprotocol.io/docs/sdk):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Vedligeholdt i samarbejde med Microsoft
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Vedligeholdt i samarbejde med Spring AI
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - Den officielle TypeScript-implementering
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Den officielle Python-implementering (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - Den officielle Kotlin-implementering
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Vedligeholdt i samarbejde med Loopwork AI
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - Den officielle Rust-implementering
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - Den officielle Go-implementering

## Vigtige punkter

- Opsætning af et MCP-udviklingsmiljø er ligetil med sprog-specifikke SDK'er
- Bygning af MCP-servere indebærer oprettelse og registrering af værktøjer med klare skemaer
- MCP-klienter opretter forbindelse til servere og modeller for at udnytte udvidede funktioner
- Testning og fejlfinding er essentielt for pålidelige MCP-implementeringer
- Udrulningsmuligheder spænder fra lokal udvikling til skybaserede løsninger

## Øvelse

Vi har et sæt eksempler, der supplerer de øvelser, du vil se i alle kapitler i denne sektion. Derudover har hvert kapitel også sine egne øvelser og opgaver

- [Java Calculator](./samples/java/calculator/README.md)
- [.NET Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## Yderligere ressourcer

- [Byg agenter ved hjælp af Model Context Protocol på Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Fjern-MCP med Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## Hvad er det næste

Start med den første lektion: [Opret din første MCP-server](01-first-server/README.md)

Når du har gennemført denne modul, fortsæt til: [Modul 4: Praktisk implementering](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->