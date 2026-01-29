# MCP stdio Server - .NET-løsning

> **⚠️ Viktig**: Denne løsningen er oppdatert til å bruke **stdio transport** som anbefalt i MCP-spesifikasjonen 2025-06-18. Den opprinnelige SSE-transporten er utfaset.

## Oversikt

Denne .NET-løsningen viser hvordan man bygger en MCP-server ved bruk av den nåværende stdio-transporten. Stdio-transporten er enklere, mer sikker og gir bedre ytelse enn den utfasete SSE-tilnærmingen.

## Forutsetninger

- .NET 9.0 SDK eller nyere
- Grunnleggende forståelse av .NET dependency injection

## Oppsettinstruksjoner

### Steg 1: Gjenopprett avhengigheter

```bash
dotnet restore
```

### Steg 2: Bygg prosjektet

```bash
dotnet build
```

## Kjøre serveren

Stdio-serveren fungerer annerledes enn den gamle HTTP-baserte serveren. I stedet for å starte en webserver, kommuniserer den via stdin/stdout:

```bash
dotnet run
```

**Viktig**: Serveren vil se ut som den henger – dette er normalt! Den venter på JSON-RPC-meldinger fra stdin.

## Testing av serveren

### Metode 1: Bruke MCP Inspector (Anbefalt)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

Dette vil:
1. Starte serveren din som en underprosess
2. Åpne et webgrensesnitt for testing
3. La deg teste alle serververktøy interaktivt

### Metode 2: Direkte testing via kommandolinjen

Du kan også teste ved å starte Inspector direkte:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### Tilgjengelige verktøy

Serveren tilbyr disse verktøyene:

- **AddNumbers(a, b)**: Legger sammen to tall
- **MultiplyNumbers(a, b)**: Multipliserer to tall  
- **GetGreeting(name)**: Genererer en personlig hilsen
- **GetServerInfo()**: Gir informasjon om serveren

### Testing med Claude Desktop

For å bruke denne serveren med Claude Desktop, legg til denne konfigurasjonen i `claude_desktop_config.json`:

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

## Prosjektstruktur

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## Viktige forskjeller fra HTTP/SSE

**stdio transport (Nåværende):**
- ✅ Enklere oppsett – ingen webserver nødvendig
- ✅ Bedre sikkerhet – ingen HTTP-endepunkter
- ✅ Bruker `Host.CreateApplicationBuilder()` i stedet for `WebApplication.CreateBuilder()`
- ✅ `WithStdioTransport()` i stedet for `WithHttpTransport()`
- ✅ Konsollapplikasjon i stedet for webapplikasjon
- ✅ Bedre ytelse

**HTTP/SSE transport (Utfaset):**
- ❌ Krevde ASP.NET Core-webserver
- ❌ Trengte `app.MapMcp()` routing-oppsett
- ❌ Mer kompleks konfigurasjon og avhengigheter
- ❌ Ekstra sikkerhetsvurderinger
- ❌ Nå utfaset i MCP 2025-06-18

## Utviklingsfunksjoner

- **Dependency Injection**: Full DI-støtte for tjenester og logging
- **Strukturert logging**: Riktig logging til stderr ved bruk av `ILogger<T>`
- **Tool Attributes**: Enkel verktøydefinisjon ved bruk av `[McpServerTool]` attributter
- **Async-støtte**: Alle verktøy støtter asynkrone operasjoner
- **Feilhåndtering**: Smidig feilhåndtering og logging

## Utviklingstips

- Bruk `ILogger` for logging (aldri skriv direkte til stdout)
- Bygg med `dotnet build` før testing
- Test med Inspector for visuell debugging
- All logging går automatisk til stderr
- Serveren håndterer avslutningssignaler på en smidig måte

Denne løsningen følger den nåværende MCP-spesifikasjonen og viser beste praksis for implementering av stdio-transport ved bruk av .NET.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.