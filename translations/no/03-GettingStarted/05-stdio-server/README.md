# MCP-server med stdio-transportsystem

> **⚠️ Viktig oppdatering**: Fra og med MCP-spesifikasjonen 2025-06-18 er den frittstående SSE (Server-Sent Events) transporten **utfaset** og erstattet av "Streamable HTTP"-transport. Den nåværende MCP-spesifikasjonen definerer to primære transportmekanismer:
> 1. **stdio** - Standard inndata/utdata (anbefalt for lokale servere)
> 2. **Streamable HTTP** - For eksterne servere som kan bruke SSE internt
>
> Denne leksjonen er oppdatert for å fokusere på **stdio-transporten**, som er den anbefalte tilnærmingen for de fleste MCP-serverimplementeringer.

Stdio-transporten lar MCP-servere kommunisere med klienter gjennom standard inndata- og utdatastrømmer. Dette er den mest brukte og anbefalte transportmekanismen i den nåværende MCP-spesifikasjonen, og gir en enkel og effektiv måte å bygge MCP-servere som lett kan integreres med ulike klientapplikasjoner.

## Oversikt

Denne leksjonen dekker hvordan du bygger og bruker MCP-servere med stdio-transporten.

## Læringsmål

Etter denne leksjonen vil du kunne:

- Bygge en MCP-server med stdio-transport.
- Feilsøke en MCP-server ved bruk av Inspector.
- Bruke en MCP-server i Visual Studio Code.
- Forstå nåværende MCP-transportmekanismer og hvorfor stdio er anbefalt.


## stdio-transport – hvordan det fungerer

Stdio-transporten er en av de to standardtransportene i MCP-spesifikasjonen
`2026-07-28`. Slik fungerer den:

- **Enkel kommunikasjon**: Serveren leser JSON-RPC-meldinger fra standard inndata (`stdin`) og sender meldinger til standard utdata (`stdout`).
- **Prosessbasert**: Klienten starter MCP-serveren som en underprosess.
- **Meldingsformat**: Meldinger er individuelle JSON-RPC-forespørsler, notifikasjoner eller responser, avgrenset med ny linje.
- **Logging**: Serveren KAN skrive UTF-8-strenger til standard feildata (`stderr`) for loggformål.

### Viktige krav:
- Meldinger MÅ være avgrenset med ny linje og MÅ IKKE inneholde innebygde nye linjer
- Serveren MÅ IKKE skrive noe til `stdout` som ikke er en gyldig MCP-melding
- Klienten MÅ IKKE skrive noe til serverens `stdin` som ikke er en gyldig MCP-melding

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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

I koden over:

- Importerer vi klassen `Server` og `StdioServerTransport` fra MCP SDK
- Oppretter vi en serverinstans med grunnleggende konfigurasjon og funksjoner
- Lager en `StdioServerTransport`-instans og kobler serveren til den, som muliggjør kommunikasjon over stdin/stdout

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

I koden over:

- Oppretter vi en serverinstans ved bruk av MCP SDK
- Definerer verktøy med dekoratører
- Bruker vi stdio_server som en kontekstbehandler for transporten

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

Hovedforskjellen fra SSE er at stdio-servere:

- Krever ikke oppsett av webserver eller HTTP-endepunkter
- Startes som underprosesser av klienten
- Kommuniserer via stdin/stdout-strømmer
- Er enklere å implementere og feilsøke

## Oppgave: Lage en stdio-server

For å lage serveren vår må vi ha to ting i tankene:

- Vi må bruke en webserver for å eksponere endepunkter for tilkobling og meldinger.
## Lab: Lage en enkel MCP stdio-server

I denne labben lager vi en enkel MCP-server med anbefalt stdio-transport. Denne serveren vil eksponere verktøy som klienter kan kalle via standard Model Context Protocol.

### Forutsetninger

- Python 3.8 eller nyere
- MCP Python SDK: `pip install mcp`
- Grunnleggende forståelse av asynkron programmering

La oss starte med å lage vår første MCP stdio-server:

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

## Viktige forskjeller fra den utfasede SSE-metoden

**Stdio-transport (nåværende standard):**
- Enkel underprosessmodell – klient startes som en barneprosess
- Kommunikasjon via stdin/stdout med JSON-RPC-meldinger
- Krever ikke HTTP-serveroppsett
- Bedre ytelse og sikkerhet
- Letter feilsøking og utvikling

**SSE-transport (utfaset fra MCP 2025-06-18):**
- Krever HTTP-server med SSE-endepunkter
- Mer komplisert oppsett med webserverinfrastruktur
- Tilleggs sikkerhetshensyn for HTTP-endepunkter
- Nå erstattet av Streamable HTTP for nettbaserte scenarier

### Lage en server med stdio-transport

For å lage stdio-serveren må vi:

1. **Importere nødvendige biblioteker** – Vi trenger MCP-serverkomponentene og stdio-transporten
2. **Opprette en serverinstans** – Definere serveren med sine funksjoner
3. **Definere verktøy** – Legge til funksjonalitet som skal eksponeres
4. **Sette opp transporten** – Konfigurere stdio-kommunikasjon
5. **Kjøre serveren** – Starte serveren og håndtere meldinger

La oss bygge dette steg for steg:

### Steg 1: Opprett en grunnleggende stdio-server

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

Serveren vil starte og vente på inndata fra stdin. Den kommuniserer ved bruk av JSON-RPC-meldinger over stdio-transporten.

### Steg 4: Teste med Inspector

Du kan teste serveren din med MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kjør Inspector og pek den mot serveren din
3. Test verktøyene du har laget

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Feilsøking av din stdio-server

### Bruke MCP Inspector

MCP Inspector er et verdifullt verktøy for feilsøking og testing av MCP-servere. Slik bruker du det med din stdio-server:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kjør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test serveren din**: Inspector tilbyr et webgrensesnitt hvor du kan:
   - Se serverens kapasiteter
   - Teste verktøy med ulike parametere
   - Overvåke JSON-RPC-meldinger
   - Feilsøke tilkoblingsproblemer

### Bruke VS Code

Du kan også feilsøke MCP-serveren direkte i VS Code:

1. Lag en launch-konfigurasjon i `.vscode/launch.json`:
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

2. Sett bruddpunkter i serverkoden din
3. Kjør debugeren og test med Inspector

### Vanlige feilsøkingstips

- Bruk `stderr` til logging – skriv aldri til `stdout` da dette er reservert for MCP-meldinger
- Sørg for at alle JSON-RPC-meldinger er newline-avgrenset
- Test først med enkle verktøy før du legger til kompleks funksjonalitet
- Bruk Inspector for å verifisere meldingsformater

## Bruke din stdio-server i VS Code

Når du har bygget MCP stdio-serveren, kan du integrere den i VS Code for å bruke den med Claude eller andre MCP-kompatible klienter.

### Konfigurasjon

1. **Opprett en MCP-konfigurasjonsfil** i `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Start Claude på nytt**: Lukk og åpne Claude igjen for å laste inn den nye serverkonfigurasjonen.

3. **Test tilkoblingen**: Start en samtale med Claude og prøv å bruke serverens verktøy:
   - "Kan du hilse på meg med hilseverktøyet?"
   - "Regn ut summen av 15 og 27"
   - "Hva er serverinfo?"

### TypeScript stdio-server eksempel

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

### .NET stdio-server eksempel

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## Oppsummering

I denne oppdaterte leksjonen har du lært hvordan du:

- Bygger MCP-servere med dagens **stdio-transport** (anbefalt metode)
- Forstår hvorfor SSE-transport ble utfaset til fordel for stdio og Streamable HTTP
- Lager verktøy som kan kalles av MCP-klienter
- Feilsøker serveren din med MCP Inspector
- Integrerer stdio-serveren med VS Code og Claude

Stdio-transporten gir en enklere, sikrere og mer ytelseseffektiv måte å bygge MCP-servere på sammenlignet med den utfasede SSE-tilnærmingen. Det er den anbefalte transporten for de fleste MCP-serverimplementeringer fra og med 2025-06-18-spesifikasjonen.


### .NET

1. La oss først lage noen verktøy, til dette oppretter vi en fil *Tools.cs* med følgende innhold:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Oppgave: Test din stdio-server

Nå som du har bygget stdio-serveren din, la oss teste den for å sikre at den fungerer riktig.

### Forutsetninger

1. Sørg for at MCP Inspector er installert:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Serverkoden din skal være lagret (f.eks. som `server.py`)

### Testing med Inspector

1. **Start Inspector med serveren din**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åpne nettgrensesnittet**: Inspector åpner et nettleservindu som viser serverkapasiteter.

3. **Test verktøyene**:
   - Prøv `get_greeting`-verktøyet med forskjellige navn
   - Test `calculate_sum`-verktøyet med ulike tall
   - Kall `get_server_info`-verktøyet for å se servermetadata

4. **Overvåk kommunikasjonen**: Inspector viser JSON-RPC-meldinger som utveksles mellom klient og server.

### Hva du bør se

Når serveren starter korrekt skal du se:
- Serverkapasiteter listet i Inspector
- Verktøy tilgjengelige for testing
- Vellykkede JSON-RPC-meldingsutvekslinger
- Verktøysvar vist i grensesnittet

### Vanlige problemer og løsninger

**Serveren starter ikke:**
- Sjekk at alle avhengigheter er installert: `pip install mcp`
- Verifiser Python-syntaks og innrykk
- Se etter feilmeldinger i konsollen

**Verktøy vises ikke:**
- Sørg for at `@server.tool()`-dekoratørene er til stede
- Sjekk at verktøyfunksjoner er definert før `main()`
- Verifiser at serveren er riktig konfigurert

**Tilkoblingsproblemer:**
- Sørg for at server bruker stdio-transport riktig
- Sjekk at ingen andre prosesser forstyrrer
- Verifiser Inspector-kommandoens syntaks

## Oppgave

Prøv å bygge ut serveren med flere funksjoner. Se [denne siden](https://api.chucknorris.io/) for eksempelvis å legge til et verktøy som kaller en API. Du bestemmer hvordan serveren skal være. Lykke til :)
## Løsning

[Løsning](./solution/README.md) Her er et mulig forslag med fungerende kode.

## Viktige punkter

Hovedpunktene i dette kapitlet er:

- Stdio-transporten er den anbefalte mekanismen for lokale MCP-servere.
- Stdio-transport gir sømløs kommunikasjon mellom MCP-servere og klienter ved hjelp av standard inn- og utstrømmer.
- Du kan bruke både Inspector og Visual Studio Code for å konsumere stdio-servere direkte, noe som gjør feilsøking og integrasjon enkelt.

## Eksempler

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.NET Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)

## Ytterligere ressurser

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hva skjer videre

## Neste steg

Nå som du har lært å bygge MCP-servere med stdio-transporten, kan du utforske mer avanserte emner:

- **Neste**: [HTTP-strømming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lær om den andre støttede transportmekanismen for eksterne servere
- **Avansert**: [MCP sikkerhetspraksis](../../02-Security/README.md) – Implementer sikkerhet i dine MCP-servere
- **Produksjon**: [Utplasseringstrategier](../09-deployment/README.md) – Utplasser serverne dine for produksjonsbruk

## Ytterligere ressurser

- [MCP-spesifikasjon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Gjeldene spesifikasjon
- [MCP SDK-dokumentasjon](https://github.com/modelcontextprotocol/sdk) – SDK-referanser for alle språk
- [Fellesskapseksempler](../../06-CommunityContributions/README.md) – Flere servereksempler fra fellesskapet

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->