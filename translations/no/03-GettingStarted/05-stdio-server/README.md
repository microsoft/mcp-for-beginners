# MCP-server med stdio-transport

> **⚠️ Viktig oppdatering**: Fra og med MCP-spesifikasjon 2025-06-18 har den frittstående SSE (Server-Sent Events) transporten blitt **utfaset** og erstattet av "Streamable HTTP" transport. Den nåværende MCP-spesifikasjonen definerer to hovedtransportmekanismer:
> 1. **stdio** - Standard input/output (anbefalt for lokale servere)
> 2. **Streamable HTTP** - For eksterne servere som kan bruke SSE internt
>
> Denne leksjonen har blitt oppdatert for å fokusere på **stdio-transporten**, som er den anbefalte tilnærmingen for de fleste MCP-serverimplementasjoner.

Stdio-transporten lar MCP-servere kommunisere med klienter via standard inndata- og utstrømmer. Dette er den mest brukte og anbefalte transportmekanismen i den nåværende MCP-spesifikasjonen, og gir en enkel og effektiv måte å bygge MCP-servere som enkelt kan integreres med ulike klientapplikasjoner.

## Oversikt

Denne leksjonen dekker hvordan du kan bygge og bruke MCP-servere med stdio-transport.

## Læringsmål

Ved slutten av denne leksjonen vil du være i stand til å:

- Bygge en MCP-server med stdio-transport.
- Feilsøke en MCP-server ved hjelp av Inspector.
- Bruke en MCP-server med Visual Studio Code.
- Forstå de nåværende MCP-transportmekanismene og hvorfor stdio er anbefalt.


## stdio-transport – Hvordan det fungerer

Stdio-transporten er en av de to standardtransportene i MCP-spesifikasjon
`2026-07-28`. Slik fungerer den:

- **Enkel kommunikasjon**: Serveren leser JSON-RPC-meldinger fra standard inndata (`stdin`) og sender meldinger til standard utdata (`stdout`).
- **Prosessbasert**: Klienten starter MCP-serveren som en underprosess.
- **Meldingsformat**: Meldinger er enkeltstående JSON-RPC-forespørsler, varslinger eller svar, avgrenset med linjeskift.
- **Logging**: Serveren KAN skrive UTF-8-strenger til standard feilutgang (`stderr`) for logging.

### Viktige krav:
- Meldinger MÅ avgrenses med linjeskift og MÅ IKKE inneholde innlagte linjeskift
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

I koden ovenfor:

- Importerer vi `Server`-klassen og `StdioServerTransport` fra MCP SDK
- Vi oppretter en serverinstans med grunnleggende konfigurasjon og funksjonalitet
- Vi oppretter en `StdioServerTransport`-instans og kobler serveren til den, som muliggjør kommunikasjon over stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Opprett serverinstans
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

- Oppretter vi en serverinstans med MCP SDK
- Definerer verktøy ved hjelp av dekoratører
- Bruker `stdio_server` context manager for å håndtere transporten

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

Den viktigste forskjellen fra SSE er at stdio-servere:

- Krever ikke webserver-oppsett eller HTTP-endepunkter
- Startes som underprosesser av klienten
- Kommuniserer via stdin/stdout-strømmer
- Er enklere å implementere og feilsøke

## Øvelse: Lage en stdio-server

For å lage vår server må vi ha to ting i tankene:

- Vi må bruke en webserver for å eksponere endepunkter for tilkobling og meldinger.
## Lab: Lage en enkel MCP stdio-server

I denne labben skal vi lage en enkel MCP-server ved bruk av anbefalt stdio-transport. Denne serveren vil eksponere verktøy som klienter kan kalle ved bruk av standard Model Context Protocol.

### Forutsetninger

- Python 3.8 eller nyere
- MCP Python SDK: `pip install mcp`
- Grunnleggende kunnskap om asynkron programmering

La oss starte med å lage vår første MCP stdio-server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurer logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Opprett serveren
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
    # Bruk stdio-transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Viktige forskjeller fra den utfasede SSE-tilnærmingen

**Stdio-transport (nåværende standard):**
- Enkel underprosessmodell – klienten starter serveren som en barneprosess
- Kommunikasjon via stdin/stdout med JSON-RPC-meldinger
- Krever ikke HTTP-serveroppsett
- Bedre ytelse og sikkerhet
- Enklere feilsøking og utvikling

**SSE-transport (utfaset fra MCP 2025-06-18):**
- Krever HTTP-server med SSE-endepunkter
- Mer komplekst oppsett med webserverinfrastruktur
- Ytterligere sikkerhetsoverveielser for HTTP-endepunkter
- Nå erstattet av Streamable HTTP for webbaserte scenarier

### Lage en server med stdio-transport

For å lage vår stdio-server må vi:

1. **Importere nødvendige biblioteker** – Vi trenger MCP-serverkomponentene og stdio-transporten
2. **Opprette en serverinstans** – Definere serveren med dens funksjoner
3. **Definere verktøy** – Legge til funksjonalitet vi ønsker å eksponere
4. **Sette opp transporten** – Konfigurere stdio-kommunikasjon
5. **Kjøre serveren** – Starte serveren og håndtere meldinger

La oss bygge dette steg for steg:

### Steg 1: Lag en grunnleggende stdio-server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurer logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Opprett serveren
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

Serveren starter og venter på inndata fra stdin. Den kommuniserer ved hjelp av JSON-RPC-meldinger over stdio-transporten.

### Steg 4: Testing med Inspector

Du kan teste serveren din med MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kjør Inspector og pek den til serveren din
3. Test verktøyene du har laget

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Feilsøking av din stdio-server

### Bruke MCP Inspector

MCP Inspector er et verdifullt verktøy for feilsøking og testing av MCP-servere. Her er hvordan du bruker det med din stdio-server:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kjør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test serveren din**: Inspector gir et webgrensesnitt der du kan:
   - Se serverens funksjoner
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

2. Sett breakpoints i serverkoden din
3. Kjør debuggeren og test med Inspector

### Vanlige feilsøkingstips

- Bruk `stderr` for logging – aldri skriv til `stdout` da det er reservert for MCP-meldinger
- Sørg for at alle JSON-RPC-meldinger er linjeskiftavgrenset
- Test med enkle verktøy først før du legger til kompleks funksjonalitet
- Bruk Inspector til å verifisere meldingsformater

## Bruke din stdio-server i VS Code

Når du har bygget din MCP stdio-server, kan du integrere den i VS Code for å bruke den med Claude eller andre MCP-kompatible klienter.

### Konfigurasjon

1. **Lag en MCP-konfigurasjonsfil** på `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Start Claude på nytt**: Lukk og åpne Claude for å laste den nye serverkonfigurasjonen.

3. **Test tilkoblingen**: Start en samtale med Claude og prøv å bruke verktøyene i serveren din:
   - "Kan du hilse på meg med hilse-verktøyet?"
   - "Beregn summen av 15 og 27"
   - "Hva er serverinformasjonen?"

### Eksempel på TypeScript stdio-server

Her er et komplett TypeScript-eksempel som referanse:

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

// Legg til verktøy
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

### Eksempel på .NET stdio-server

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

I denne oppdaterte leksjonen lærte du hvordan du:

- Bygger MCP-servere ved bruk av nåværende **stdio-transport** (anbefalt tilnærming)
- Forstår hvorfor SSE-transporten ble utfaset til fordel for stdio og Streamable HTTP
- Oppretter verktøy som kan kalles av MCP-klienter
- Feilsøker serveren din med MCP Inspector
- Integrerer stdio-serveren din med VS Code og Claude

Stdio-transporten gir en enklere, sikrere og mer ytelseseffektiv måte å bygge MCP-servere på sammenlignet med den utfasede SSE-tilnærmingen. Det er den anbefalte transporten for de fleste MCP-serverimplementasjoner fra og med spesifikasjonen 2025-06-18.


### .NET

1. La oss først lage noen verktøy, for dette oppretter vi filen *Tools.cs* med følgende innhold:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Øvelse: Teste stdio-serveren din

Nå som du har bygget din stdio-server, la oss teste den for å sikre at den fungerer korrekt.

### Forutsetninger

1. Sørg for at du har MCP Inspector installert:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Serverkoden din bør være lagret (for eksempel som `server.py`)

### Testing med Inspector

1. **Start Inspector med serveren din**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åpne webgrensesnittet**: Inspector åpner et nettleservindu som viser serverens funksjoner.

3. **Test verktøyene**:
   - Prøv verktøyet `get_greeting` med forskjellige navn
   - Test verktøyet `calculate_sum` med ulike tall
   - Kall verktøyet `get_server_info` for å se servermetadata

4. **Overvåk kommunikasjonen**: Inspector viser JSON-RPC-meldingene som utveksles mellom klient og server.

### Hva du bør se

Når serveren starter riktig, bør du se:
- Serverens funksjoner listet i Inspector
- Verktøy tilgjengelig for testing
- Vellykkede JSON-RPC-meldingsutvekslinger
- Verktøysvar vist i grensesnittet

### Vanlige problemer og løsninger

**Serveren starter ikke:**
- Sjekk at alle avhengigheter er installert: `pip install mcp`
- Verifiser Python-syntaks og innrykk
- Se etter feilmeldinger i konsollen

**Verktøy vises ikke:**
- Sørg for at `@server.tool()` dekoratører er til stede
- Sjekk at verktøyfunksjonene er definert før `main()`
- Verifiser at serveren er korrekt konfigurert

**Tilkoblingsproblemer:**
- Forsikre deg om at serveren bruker stdio-transport riktig
- Sjekk at ingen andre prosesser forstyrrer
- Verifiser Inspector-kommandosyntaks

## Oppgave

Prøv å bygge ut serveren din med flere funksjoner. Se [denne siden](https://api.chucknorris.io/) for å for eksempel legge til et verktøy som kaller et API. Du bestemmer hvordan serveren skal se ut. Lykke til :)
## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Viktige punkter

De viktigste punktene fra dette kapitlet er følgende:

- Stdio-transporten er den anbefalte mekanismen for lokale MCP-servere.
- Stdio-transporten muliggjør sømløs kommunikasjon mellom MCP-servere og klienter ved bruk av standard inndata- og utstrømmer.
- Du kan bruke både Inspector og Visual Studio Code for å konsumere stdio-servere direkte, noe som gjør feilsøking og integrasjon enkelt.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Ytterligere ressurser

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hva skjer videre

## Neste steg

Nå som du har lært hvordan du bygger MCP-servere med stdio-transport, kan du utforske mer avanserte temaer:

- **Neste**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lær om den andre støttede transportmekanismen for eksterne servere
- **Avansert**: [MCP Sikkerhetspraksis](../../02-Security/README.md) – Implementer sikkerhet i dine MCP-servere
- **Produksjon**: [Distribusjonsstrategier](../09-deployment/README.md) – Distribuer serverne dine for produksjonsbruk

## Ytterligere ressurser

- [MCP Spesifikasjon 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) – Nåværende spesifikasjon
- [MCP SDK Dokumentasjon](https://github.com/modelcontextprotocol/sdk) – SDK-referanser for alle språk
- [Community Eksempler](../../06-CommunityContributions/README.md) – Flere servereksempler fra fellesskapet

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->