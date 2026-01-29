# MCP stdio Server - .NET-løsning

> **⚠️ Vigtigt**: Denne løsning er blevet opdateret til at bruge **stdio transport** som anbefalet i MCP-specifikationen 2025-06-18. Den oprindelige SSE-transport er blevet udfaset.

## Oversigt

Denne .NET-løsning viser, hvordan man bygger en MCP-server ved hjælp af den nuværende stdio transport. Stdio transport er enklere, mere sikker og giver bedre ydeevne end den udfasede SSE-metode.

## Forudsætninger

- .NET 9.0 SDK eller nyere
- Grundlæggende forståelse af .NET dependency injection

## Opsætningsinstruktioner

### Trin 1: Gendan afhængigheder

```bash
dotnet restore
```

### Trin 2: Byg projektet

```bash
dotnet build
```

## Kørsel af serveren

Stdio-serveren fungerer anderledes end den gamle HTTP-baserede server. I stedet for at starte en webserver kommunikerer den via stdin/stdout:

```bash
dotnet run
```

**Vigtigt**: Serveren vil tilsyneladende fryse - dette er normalt! Den venter på JSON-RPC-beskeder fra stdin.

## Test af serveren

### Metode 1: Brug af MCP Inspector (Anbefalet)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dette vil:
1. Starte din server som en underproces
2. Åbne en webgrænseflade til test
3. Give dig mulighed for at teste alle serverværktøjer interaktivt

### Metode 2: Direkte test via kommandolinjen

Du kan også teste ved at starte Inspector direkte:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Tilgængelige værktøjer

Serveren tilbyder følgende værktøjer:

- **AddNumbers(a, b)**: Læg to tal sammen
- **MultiplyNumbers(a, b)**: Gang to tal sammen  
- **GetGreeting(name)**: Generer en personlig hilsen
- **GetServerInfo()**: Hent information om serveren

### Test med Claude Desktop

For at bruge denne server med Claude Desktop skal du tilføje følgende konfiguration til din `claude_desktop_config.json`:

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

## Vigtige forskelle fra HTTP/SSE

**stdio transport (Nuværende):**
- ✅ Simpel opsætning - ingen webserver nødvendig
- ✅ Bedre sikkerhed - ingen HTTP-endpoints
- ✅ Bruger `Host.CreateApplicationBuilder()` i stedet for `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` i stedet for `WithHttpTransport()`
- ✅ Konsolapplikation i stedet for webapplikation
- ✅ Bedre ydeevne

**HTTP/SSE transport (Udfaset):**
- ❌ Krævede ASP.NET Core-webserver
- ❌ Krævede `app.MapMcp()` routing-opsætning
- ❌ Mere kompleks konfiguration og afhængigheder
- ❌ Yderligere sikkerhedsovervejelser
- ❌ Nu udfaset i MCP 2025-06-18

## Udviklingsfunktioner

- **Dependency Injection**: Fuld DI-understøttelse til services og logging
- **Struktureret logging**: Korrekt logging til stderr ved hjælp af `ILogger<T>`
- **Tool Attributes**: Ren værktøjsdefinition ved hjælp af `[McpServerTool]` attributter
- **Async Support**: Alle værktøjer understøtter asynkrone operationer
- **Fejlhåndtering**: Elegant fejlhåndtering og logging

## Udviklingstips

- Brug `ILogger` til logging (skriv aldrig direkte til stdout)
- Byg med `dotnet build` før test
- Test med Inspector for visuel debugging
- Al logging går automatisk til stderr
- Serveren håndterer elegante nedlukningssignaler

Denne løsning følger den nuværende MCP-specifikation og demonstrerer bedste praksis for stdio transport-implementering ved hjælp af .NET.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.