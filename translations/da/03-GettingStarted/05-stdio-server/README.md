# MCP Server med stdio Transport

> **⚠️ Vigtig Opdatering**: Fra og med MCP-specifikationen 2025-06-18 er den selvstændige SSE (Server-Sent Events) transport **udfaset** og erstattet af "Streamable HTTP" transport. Den nuværende MCP-specifikation definerer to primære transportmekanismer:
> 1. **stdio** - Standard input/output (anbefalet til lokale servere)
> 2. **Streamable HTTP** - Til fjernservere, der internt kan bruge SSE
>
> Denne lektion er opdateret til at fokusere på **stdio transport**, som er den anbefalede tilgang til de fleste MCP-serverimplementeringer.

Stdio transport gør det muligt for MCP-servere at kommunikere med klienter via standard input- og outputstrømme. Dette er den mest anvendte og anbefalede transportmekanisme i den nuværende MCP-specifikation, da den giver en enkel og effektiv måde at bygge MCP-servere på, som nemt kan integreres med forskellige klientapplikationer.

## Oversigt

Denne lektion dækker, hvordan man bygger og bruger MCP-servere med stdio transport.

## Læringsmål

Ved slutningen af denne lektion vil du være i stand til at:

- Bygge en MCP-server ved hjælp af stdio transport.
- Fejlsøge en MCP-server med Inspector.
- Bruge en MCP-server med Visual Studio Code.
- Forstå de nuværende MCP transportmekanismer og hvorfor stdio anbefales.

## stdio Transport - Sådan fungerer det

Stdio transport er en af de to understøttede transporttyper i den nuværende MCP-specifikation (2025-06-18). Sådan fungerer det:

- **Enkel kommunikation**: Serveren læser JSON-RPC-beskeder fra standard input (`stdin`) og sender beskeder til standard output (`stdout`).
- **Procesbaseret**: Klienten starter MCP-serveren som en underproces.
- **Beskedformat**: Beskeder er individuelle JSON-RPC-forespørgsler, notifikationer eller svar, adskilt af linjeskift.
- **Logning**: Serveren KAN skrive UTF-8-strenge til standard error (`stderr`) til logningsformål.

### Vigtige krav:
- Beskeder SKAL adskilles af linjeskift og MÅ IKKE indeholde indlejrede linjeskift.
- Serveren MÅ IKKE skrive noget til `stdout`, der ikke er en gyldig MCP-besked.
- Klienten MÅ IKKE skrive noget til serverens `stdin`, der ikke er en gyldig MCP-besked.

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

I den foregående kode:

- Importerer vi `Server`-klassen og `StdioServerTransport` fra MCP SDK.
- Opretter vi en serverinstans med grundlæggende konfiguration og funktioner.

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

I den foregående kode:

- Opretter vi en serverinstans ved hjælp af MCP SDK.
- Definerer vi værktøjer ved hjælp af dekoratorer.
- Bruger vi stdio_server context manager til at håndtere transporten.

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

Den væsentligste forskel fra SSE er, at stdio-servere:

- Ikke kræver opsætning af en webserver eller HTTP-endpoints.
- Startes som underprocesser af klienten.
- Kommunikerer via stdin/stdout-strømme.
- Er enklere at implementere og fejlfinde.

## Øvelse: Oprettelse af en stdio-server

For at oprette vores server skal vi huske to ting:

- Vi skal bruge en webserver til at eksponere endpoints til forbindelse og beskeder.

## Laboratorium: Oprettelse af en simpel MCP stdio-server

I dette laboratorium opretter vi en simpel MCP-server ved hjælp af den anbefalede stdio transport. Denne server vil eksponere værktøjer, som klienter kan kalde ved hjælp af den standardiserede Model Context Protocol.

### Forudsætninger

- Python 3.8 eller nyere
- MCP Python SDK: `pip install mcp`
- Grundlæggende forståelse af asynkron programmering

Lad os starte med at oprette vores første MCP stdio-server:

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

## Væsentlige forskelle fra den udfasede SSE-tilgang

**Stdio Transport (Nuværende Standard):**
- Enkel underprocesmodel - klienten starter serveren som en underproces.
- Kommunikation via stdin/stdout ved hjælp af JSON-RPC-beskeder.
- Ingen opsætning af HTTP-server kræves.
- Bedre ydeevne og sikkerhed.
- Nem fejlfinding og udvikling.

**SSE Transport (Udfaset fra MCP 2025-06-18):**
- Krævede en HTTP-server med SSE-endpoints.
- Mere kompleks opsætning med webserverinfrastruktur.
- Yderligere sikkerhedsovervejelser for HTTP-endpoints.
- Nu erstattet af Streamable HTTP til webbaserede scenarier.

### Oprettelse af en server med stdio transport

For at oprette vores stdio-server skal vi:

1. **Importere de nødvendige biblioteker** - Vi skal bruge MCP-serverkomponenterne og stdio transport.
2. **Oprette en serverinstans** - Definere serveren med dens funktioner.
3. **Definere værktøjer** - Tilføje de funktioner, vi vil eksponere.
4. **Opsætte transporten** - Konfigurere stdio-kommunikation.
5. **Køre serveren** - Starte serveren og håndtere beskeder.

Lad os bygge dette trin for trin:

### Trin 1: Opret en grundlæggende stdio-server

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

### Trin 2: Tilføj flere værktøjer

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

### Trin 3: Kør serveren

Gem koden som `server.py` og kør den fra kommandolinjen:

```bash
python server.py
```

Serveren starter og venter på input fra stdin. Den kommunikerer ved hjælp af JSON-RPC-beskeder over stdio transport.

### Trin 4: Test med Inspector

Du kan teste din server ved hjælp af MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kør Inspector og peg den mod din server.
3. Test de værktøjer, du har oprettet.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Fejlfinding af din stdio-server

### Brug af MCP Inspector

MCP Inspector er et værdifuldt værktøj til fejlfinding og test af MCP-servere. Sådan bruger du det med din stdio-server:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test din server**: Inspector giver en webgrænseflade, hvor du kan:
   - Se serverens funktioner.
   - Teste værktøjer med forskellige parametre.
   - Overvåge JSON-RPC-beskeder.
   - Fejlsøge forbindelsesproblemer.

### Brug af VS Code

Du kan også fejlfinde din MCP-server direkte i VS Code:

1. Opret en launch-konfiguration i `.vscode/launch.json`:
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

2. Sæt breakpoints i din serverkode.
3. Kør debuggeren og test med Inspector.

### Almindelige fejlfindingstips

- Brug `stderr` til logning - skriv aldrig til `stdout`, da det er reserveret til MCP-beskeder.
- Sørg for, at alle JSON-RPC-beskeder er linjeskift-adskilte.
- Test med simple værktøjer først, før du tilføjer kompleks funktionalitet.
- Brug Inspector til at verificere beskedformater.

## Brug af din stdio-server i VS Code

Når du har oprettet din MCP stdio-server, kan du integrere den med VS Code for at bruge den med Claude eller andre MCP-kompatible klienter.

### Konfiguration

1. **Opret en MCP-konfigurationsfil** på `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Genstart Claude**: Luk og genåbn Claude for at indlæse den nye serverkonfiguration.

3. **Test forbindelsen**: Start en samtale med Claude og prøv at bruge din servers værktøjer:
   - "Kan du hilse på mig ved hjælp af hilsenværktøjet?"
   - "Beregn summen af 15 og 27."
   - "Hvad er serverinformationen?"

### TypeScript stdio-server eksempel

Her er et komplet TypeScript-eksempel til reference:

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

## Opsummering

I denne opdaterede lektion lærte du at:

- Bygge MCP-servere ved hjælp af den nuværende **stdio transport** (anbefalet tilgang).
- Forstå, hvorfor SSE transport blev udfaset til fordel for stdio og Streamable HTTP.
- Oprette værktøjer, der kan kaldes af MCP-klienter.
- Fejlsøge din server ved hjælp af MCP Inspector.
- Integrere din stdio-server med VS Code og Claude.

Stdio transport giver en enklere, mere sikker og mere effektiv måde at bygge MCP-servere på sammenlignet med den udfasede SSE-tilgang. Det er den anbefalede transport til de fleste MCP-serverimplementeringer fra og med specifikationen 2025-06-18.

## Øvelse: Test din stdio-server

Nu hvor du har bygget din stdio-server, lad os teste den for at sikre, at den fungerer korrekt.

### Forudsætninger

1. Sørg for, at du har MCP Inspector installeret:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkode skal være gemt (f.eks. som `server.py`).

### Test med Inspector

1. **Start Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åbn webgrænsefladen**: Inspector åbner et browser-vindue, der viser din servers funktioner.

3. **Test værktøjerne**: 
   - Prøv `get_greeting`-værktøjet med forskellige navne.
   - Test `calculate_sum`-værktøjet med forskellige tal.
   - Kald `get_server_info`-værktøjet for at se servermetadata.

4. **Overvåg kommunikationen**: Inspector viser JSON-RPC-beskederne, der udveksles mellem klient og server.

### Hvad du bør se

Når din server starter korrekt, bør du se:
- Serverens funktioner listet i Inspector.
- Værktøjer tilgængelige til test.
- Succesfulde JSON-RPC-beskedudvekslinger.
- Værktøjsrespons vist i grænsefladen.

### Almindelige problemer og løsninger

**Serveren starter ikke:**
- Tjek, at alle afhængigheder er installeret: `pip install mcp`.
- Verificer Python-syntaks og indrykning.
- Kig efter fejlmeddelelser i konsollen.

**Værktøjer vises ikke:**
- Sørg for, at `@server.tool()`-dekoratorer er til stede.
- Tjek, at værktøjsfunktioner er defineret før `main()`.
- Verificer, at serveren er korrekt konfigureret.

**Forbindelsesproblemer:**
- Sørg for, at serveren bruger stdio transport korrekt.
- Tjek, at ingen andre processer forstyrrer.
- Verificer Inspector-kommandoens syntaks.

## Opgave

Prøv at udvide din server med flere funktioner. Se [denne side](https://api.chucknorris.io/) for eksempelvis at tilføje et værktøj, der kalder en API. Du bestemmer, hvordan serveren skal se ud. Hav det sjovt :)

## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Vigtige pointer

De vigtigste pointer fra dette kapitel er følgende:

- Stdio transport er den anbefalede mekanisme til lokale MCP-servere.
- Stdio transport muliggør problemfri kommunikation mellem MCP-servere og klienter ved hjælp af standard input- og outputstrømme.
- Du kan bruge både Inspector og Visual Studio Code til at bruge stdio-servere direkte, hvilket gør fejlfinding og integration ligetil.

## Eksempler 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Yderligere ressourcer

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hvad er det næste

## Næste skridt

Nu hvor du har lært at bygge MCP-servere med stdio transport, kan du udforske mere avancerede emner:

- **Næste**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) - Lær om den anden understøttede transportmekanisme til fjernservere.
- **Avanceret**: [MCP Sikkerhedsbedste Praksis](../../02-Security/README.md) - Implementer sikkerhed i dine MCP-servere.
- **Produktion**: [Udrulningsstrategier](../09-deployment/README.md) - Udrul dine servere til produktionsbrug.

## Yderligere ressourcer

- [MCP-specifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiel specifikation.
- [MCP SDK Dokumentation](https://github.com/modelcontextprotocol/sdk) - SDK-referencer for alle sprog.
- [Community Eksempler](../../06-CommunityContributions/README.md) - Flere servereksempler fra fællesskabet.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.