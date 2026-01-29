# MCP stdio Server - .NET-lösning

> **⚠️ Viktigt**: Den här lösningen har uppdaterats för att använda **stdio-transport** enligt rekommendationerna i MCP-specifikationen 2025-06-18. Den ursprungliga SSE-transporten har avvecklats.

## Översikt

Den här .NET-lösningen visar hur man bygger en MCP-server med den aktuella stdio-transporten. Stdio-transporten är enklare, säkrare och ger bättre prestanda än den avvecklade SSE-metoden.

## Förutsättningar

- .NET 9.0 SDK eller senare
- Grundläggande förståelse för .NET dependency injection

## Installationsinstruktioner

### Steg 1: Återställ beroenden

```bash
dotnet restore
```

### Steg 2: Bygg projektet

```bash
dotnet build
```

## Köra servern

Stdio-servern fungerar annorlunda än den gamla HTTP-baserade servern. Istället för att starta en webbserver kommunicerar den via stdin/stdout:

```bash
dotnet run
```

**Viktigt**: Servern kommer att verka som att den "hänger" – detta är normalt! Den väntar på JSON-RPC-meddelanden från stdin.

## Testa servern

### Metod 1: Använd MCP Inspector (Rekommenderas)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Detta kommer att:
1. Starta din server som en subprocess
2. Öppna ett webbgränssnitt för testning
3. Låta dig testa alla serververktyg interaktivt

### Metod 2: Direkt testning via kommandoraden

Du kan också testa genom att starta Inspectorn direkt:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Tillgängliga verktyg

Servern tillhandahåller följande verktyg:

- **AddNumbers(a, b)**: Addera två tal
- **MultiplyNumbers(a, b)**: Multiplicera två tal  
- **GetGreeting(name)**: Generera en personlig hälsning
- **GetServerInfo()**: Hämta information om servern

### Testa med Claude Desktop

För att använda denna server med Claude Desktop, lägg till följande konfiguration i din `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Projektstruktur

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Viktiga skillnader från HTTP/SSE

**stdio-transport (Nuvarande):**
- ✅ Enklare installation - ingen webbserver behövs
- ✅ Bättre säkerhet - inga HTTP-endpoints
- ✅ Använder `Host.CreateApplicationBuilder()` istället för `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` istället för `WithHttpTransport()`
- ✅ Konsolapplikation istället för webbapplikation
- ✅ Bättre prestanda

**HTTP/SSE-transport (Avvecklad):**
- ❌ Krävde ASP.NET Core-webbserver
- ❌ Behövde `app.MapMcp()`-routning
- ❌ Mer komplex konfiguration och fler beroenden
- ❌ Ytterligare säkerhetsöverväganden
- ❌ Nu avvecklad i MCP 2025-06-18

## Utvecklingsfunktioner

- **Dependency Injection**: Fullt DI-stöd för tjänster och loggning
- **Strukturerad loggning**: Korrekt loggning till stderr med `ILogger<T>`
- **Tool Attributes**: Ren verktygsdefinition med `[McpServerTool]`-attribut
- **Async-stöd**: Alla verktyg stödjer asynkrona operationer
- **Felfunktionalitet**: Smidig felhantering och loggning

## Utvecklingstips

- Använd `ILogger` för loggning (skriv aldrig direkt till stdout)
- Bygg med `dotnet build` innan testning
- Testa med Inspectorn för visuell felsökning
- All loggning går automatiskt till stderr
- Servern hanterar signaler för smidig avstängning

Den här lösningen följer den aktuella MCP-specifikationen och visar bästa praxis för implementering av stdio-transport med .NET.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.