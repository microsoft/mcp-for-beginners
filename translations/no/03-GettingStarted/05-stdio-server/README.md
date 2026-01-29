# MCP-server med stdio-transport

> **⚠️ Viktig oppdatering**: Fra og med MCP-spesifikasjonen 2025-06-18 er den frittstående SSE (Server-Sent Events)-transporten **utdatert** og erstattet av "Streamable HTTP"-transport. Den nåværende MCP-spesifikasjonen definerer to primære transportmekanismer:
> 1. **stdio** - Standard input/output (anbefalt for lokale servere)
> 2. **Streamable HTTP** - For eksterne servere som kan bruke SSE internt
>
> Denne leksjonen er oppdatert for å fokusere på **stdio-transport**, som er den anbefalte tilnærmingen for de fleste MCP-serverimplementasjoner.

Stdio-transporten lar MCP-servere kommunisere med klienter gjennom standard input- og output-strømmer. Dette er den mest brukte og anbefalte transportmekanismen i den nåværende MCP-spesifikasjonen, og gir en enkel og effektiv måte å bygge MCP-servere som enkelt kan integreres med ulike klientapplikasjoner.

## Oversikt

Denne leksjonen dekker hvordan man bygger og bruker MCP-servere med stdio-transport.

## Læringsmål

Ved slutten av denne leksjonen vil du kunne:

- Bygge en MCP-server ved hjelp av stdio-transport.
- Feilsøke en MCP-server ved hjelp av Inspector.
- Bruke en MCP-server med Visual Studio Code.
- Forstå de nåværende MCP-transportmekanismene og hvorfor stdio anbefales.

## Stdio-transport – Hvordan det fungerer

Stdio-transporten er en av to støttede transporttyper i den nåværende MCP-spesifikasjonen (2025-06-18). Slik fungerer det:

- **Enkel kommunikasjon**: Serveren leser JSON-RPC-meldinger fra standard input (`stdin`) og sender meldinger til standard output (`stdout`).
- **Prosessbasert**: Klienten starter MCP-serveren som en underprosess.
- **Meldingsformat**: Meldinger er individuelle JSON-RPC-forespørsler, varsler eller svar, adskilt med linjeskift.
- **Logging**: Serveren KAN skrive UTF-8-strenger til standard error (`stderr`) for loggingsformål.

### Viktige krav:
- Meldinger MÅ være adskilt med linjeskift og MÅ IKKE inneholde innebygde linjeskift.
- Serveren MÅ IKKE skrive noe til `stdout` som ikke er en gyldig MCP-melding.
- Klienten MÅ IKKE skrive noe til serverens `stdin` som ikke er en gyldig MCP-melding.

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);
```

I koden ovenfor:

- Importerer vi `Server`-klassen og `StdioServerTransport` fra MCP SDK.
- Oppretter vi en serverinstans med grunnleggende konfigurasjon og funksjonalitet.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

I koden ovenfor:

- Oppretter vi en serverinstans ved hjelp av MCP SDK.
- Definerer vi verktøy ved hjelp av dekoratorer.
- Bruker vi stdio_server-kontekstbehandleren for å håndtere transporten.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Den viktigste forskjellen fra SSE er at stdio-servere:

- Krever ikke oppsett av webserver eller HTTP-endepunkter.
- Startes som underprosesser av klienten.
- Kommuniserer gjennom stdin/stdout-strømmer.
- Er enklere å implementere og feilsøke.

## Øvelse: Lage en stdio-server

For å lage vår server må vi huske to ting:

- Vi må bruke en webserver for å eksponere endepunkter for tilkobling og meldinger.

## Lab: Lage en enkel MCP-stdio-server

I denne laben skal vi lage en enkel MCP-server ved hjelp av den anbefalte stdio-transporten. Denne serveren vil eksponere verktøy som klienter kan kalle ved hjelp av standard Model Context Protocol.

### Forutsetninger

- Python 3.8 eller nyere
- MCP Python SDK: `pip install mcp`
- Grunnleggende forståelse av asynkron programmering

La oss starte med å lage vår første MCP-stdio-server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Viktige forskjeller fra den utgåtte SSE-tilnærmingen

**Stdio-transport (nåværende standard):**
- Enkel underprosessmodell – klienten starter serveren som en underprosess.
- Kommunikasjon via stdin/stdout ved hjelp av JSON-RPC-meldinger.
- Ingen behov for oppsett av HTTP-server.
- Bedre ytelse og sikkerhet.
- Enklere feilsøking og utvikling.

**SSE-transport (utgått fra MCP 2025-06-18):**
- Krevde HTTP-server med SSE-endepunkter.
- Mer komplisert oppsett med webserverinfrastruktur.
- Ytterligere sikkerhetsvurderinger for HTTP-endepunkter.
- Nå erstattet av Streamable HTTP for webbaserte scenarier.

### Lage en server med stdio-transport

For å lage vår stdio-server må vi:

1. **Importere nødvendige biblioteker** – Vi trenger MCP-serverkomponenter og stdio-transport.
2. **Opprette en serverinstans** – Definere serveren med dens funksjonalitet.
3. **Definere verktøy** – Legge til funksjonaliteten vi vil eksponere.
4. **Sette opp transporten** – Konfigurere stdio-kommunikasjon.
5. **Kjøre serveren** – Starte serveren og håndtere meldinger.

La oss bygge dette steg for steg:

### Steg 1: Lag en grunnleggende stdio-server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### Steg 2: Legg til flere verktøy

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### Steg 3: Kjøre serveren

Lagre koden som `server.py` og kjør den fra kommandolinjen:

```bash
python server.py
```

Serveren vil starte og vente på input fra stdin. Den kommuniserer ved hjelp av JSON-RPC-meldinger over stdio-transporten.

### Steg 4: Testing med Inspector

Du kan teste serveren din ved hjelp av MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kjør Inspector og pek den til serveren din.
3. Test verktøyene du har laget.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Feilsøking av stdio-serveren din

### Bruke MCP Inspector

MCP Inspector er et verdifullt verktøy for feilsøking og testing av MCP-servere. Slik bruker du det med stdio-serveren din:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kjør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test serveren din**: Inspector gir et webgrensesnitt hvor du kan:
   - Se serverens funksjonalitet.
   - Teste verktøy med ulike parametere.
   - Overvåke JSON-RPC-meldinger.
   - Feilsøke tilkoblingsproblemer.

### Bruke VS Code

Du kan også feilsøke MCP-serveren din direkte i VS Code:

1. Opprett en startkonfigurasjon i `.vscode/launch.json`:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. Sett opp brytepunkter i serverkoden din.
3. Kjør feilsøkeren og test med Inspector.

### Vanlige feilsøkingstips

- Bruk `stderr` til logging – skriv aldri til `stdout`, da det er reservert for MCP-meldinger.
- Sørg for at alle JSON-RPC-meldinger er linjeskift-adskilt.
- Test med enkle verktøy først før du legger til kompleks funksjonalitet.
- Bruk Inspector for å verifisere meldingsformater.

## Bruke stdio-serveren din i VS Code

Når du har bygget MCP-stdio-serveren din, kan du integrere den med VS Code for å bruke den med Claude eller andre MCP-kompatible klienter.

### Konfigurasjon

1. **Opprett en MCP-konfigurasjonsfil** på `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Start Claude på nytt**: Lukk og åpne Claude på nytt for å laste den nye serverkonfigurasjonen.

3. **Test tilkoblingen**: Start en samtale med Claude og prøv å bruke serverens verktøy:
   - "Kan du hilse på meg ved hjelp av hilsningsverktøyet?"
   - "Regn ut summen av 15 og 27."
   - "Hva er serverinformasjonen?"

### TypeScript stdio-servereksempel

Her er et komplett TypeScript-eksempel for referanse:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Add tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio-servereksempel

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Oppsummering

I denne oppdaterte leksjonen lærte du hvordan du:

- Bygger MCP-servere ved hjelp av den nåværende **stdio-transporten** (anbefalt tilnærming).
- Forstår hvorfor SSE-transport ble utgått til fordel for stdio og Streamable HTTP.
- Lager verktøy som kan kalles av MCP-klienter.
- Feilsøker serveren din ved hjelp av MCP Inspector.
- Integrerer stdio-serveren din med VS Code og Claude.

Stdio-transporten gir en enklere, sikrere og mer effektiv måte å bygge MCP-servere på sammenlignet med den utgåtte SSE-tilnærmingen. Det er den anbefalte transporten for de fleste MCP-serverimplementasjoner fra og med spesifikasjonen 2025-06-18.

## Øvelse: Teste stdio-serveren din

Nå som du har bygget stdio-serveren din, la oss teste den for å sikre at den fungerer som den skal.

### Forutsetninger

1. Sørg for at du har MCP Inspector installert:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Serverkoden din bør være lagret (f.eks. som `server.py`).

### Testing med Inspector

1. **Start Inspector med serveren din**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åpne webgrensesnittet**: Inspector åpner et nettleservindu som viser serverens funksjonalitet.

3. **Test verktøyene**: 
   - Prøv `get_greeting`-verktøyet med ulike navn.
   - Test `calculate_sum`-verktøyet med forskjellige tall.
   - Kall `get_server_info`-verktøyet for å se servermetadata.

4. **Overvåk kommunikasjonen**: Inspector viser JSON-RPC-meldingene som utveksles mellom klient og server.

### Hva du bør se

Når serveren din starter riktig, bør du se:
- Serverens funksjonalitet listet i Inspector.
- Verktøy tilgjengelige for testing.
- Vellykkede JSON-RPC-meldingsutvekslinger.
- Verktøysvar vist i grensesnittet.

### Vanlige problemer og løsninger

**Serveren starter ikke:**
- Sjekk at alle avhengigheter er installert: `pip install mcp`.
- Verifiser Python-syntaks og innrykk.
- Se etter feilmeldinger i konsollen.

**Verktøy vises ikke:**
- Sørg for at `@server.tool()`-dekoratorer er til stede.
- Sjekk at verktøyfunksjoner er definert før `main()`.
- Verifiser at serveren er riktig konfigurert.

**Tilkoblingsproblemer:**
- Sørg for at serveren bruker stdio-transport riktig.
- Sjekk at ingen andre prosesser forstyrrer.
- Verifiser Inspector-kommandoens syntaks.

## Oppgave

Prøv å utvide serveren din med flere funksjoner. Se [denne siden](https://api.chucknorris.io/) for eksempel for å legge til et verktøy som kaller en API. Du bestemmer hvordan serveren skal se ut. Ha det gøy :)

## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Viktige punkter

De viktigste punktene fra dette kapittelet er følgende:

- Stdio-transport er den anbefalte mekanismen for lokale MCP-servere.
- Stdio-transport tillater sømløs kommunikasjon mellom MCP-servere og klienter ved hjelp av standard input- og output-strømmer.
- Du kan bruke både Inspector og Visual Studio Code til å bruke stdio-servere direkte, noe som gjør feilsøking og integrasjon enkelt.

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python) 

## Tilleggsressurser

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hva nå

## Neste steg

Nå som du har lært hvordan du bygger MCP-servere med stdio-transport, kan du utforske mer avanserte emner:

- **Neste**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lær om den andre støttede transportmekanismen for eksterne servere.
- **Avansert**: [MCP Sikkerhetspraksis](../../02-Security/README.md) – Implementer sikkerhet i MCP-serverne dine.
- **Produksjon**: [Distribusjonsstrategier](../09-deployment/README.md) – Distribuer serverne dine for produksjonsbruk.

## Tilleggsressurser

- [MCP-spesifikasjon 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Offisiell spesifikasjon.
- [MCP SDK-dokumentasjon](https://github.com/modelcontextprotocol/sdk) – SDK-referanser for alle språk.
- [Eksempler fra fellesskapet](../../06-CommunityContributions/README.md) – Flere servereksempler fra fellesskapet.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.