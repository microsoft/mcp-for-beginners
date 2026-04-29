# MCP-server med stdio-transport

> **⚠️ Vigtig opdatering**: Fra MCP-specifikationen 2025-06-18 er den selvstændige SSE (Server-Sent Events) transport **afviklet** og erstattet af "Streamable HTTP"-transport. Den nuværende MCP-specifikation definerer to primære transportmekanismer:
> 1. **stdio** - Standard input/output (anbefalet til lokale servere)
> 2. **Streamable HTTP** - Til fjernservere, der internt kan bruge SSE
>
> Denne lektion er opdateret til at fokusere på **stdio-transporten**, som er den anbefalede tilgang til de fleste MCP-serverimplementeringer.

Stdio-transporten tillader MCP-servere at kommunikere med klienter via standard input- og output-strømme. Dette er den mest anvendte og anbefalede transportmekanisme i den nuværende MCP-specifikation, som giver en simpel og effektiv måde at bygge MCP-servere på, der let kan integreres med forskellige klientapplikationer.

## Oversigt

Denne lektion dækker, hvordan man bygger og bruger MCP-servere med stdio-transport.

## Læringsmål

Når denne lektion er færdig, vil du kunne:

- Bygge en MCP-server med stdio-transport.
- Fejlsøge en MCP-server ved hjælp af Inspector.
- Bruge en MCP-server i Visual Studio Code.
- Forstå de nuværende MCP-transportmekanismer og hvorfor stdio anbefales.

## stdio Transport - Sådan virker det

Stdio-transporten er en af to understøttede transporttyper i den nuværende MCP-specifikation (2025-06-18). Sådan virker den:

- **Simpel kommunikation**: Serveren læser JSON-RPC-beskeder fra standard input (`stdin`) og sender beskeder til standard output (`stdout`).
- **Procesbaseret**: Klienten starter MCP-serveren som et subprocess.
- **Beskedformat**: Beskeder er individuelle JSON-RPC-forespørgsler, notifikationer eller svar, afgrænset af linjeskift.
- **Logging**: Serveren KAN skrive UTF-8-strenge til standard fejl (`stderr`) til logformål.

### Nøglekrav:
- Beskeder SKAL være afgrænset af linjeskift og MÅ IKKE indeholde indlejrede linjeskift
- Serveren MÅ IKKE skrive noget til `stdout`, der ikke er en gyldig MCP-besked
- Klienten MÅ IKKE skrive noget til serverens `stdin`, der ikke er en gyldig MCP-besked

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

I den foregående kode:

- Importerer vi `Server` klassen og `StdioServerTransport` fra MCP SDK
- Opretter vi en serverinstans med grundlæggende konfiguration og kapabiliteter
- Opretter vi en `StdioServerTransport` instans og forbinder serveren til den, hvilket muliggør kommunikation over stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Opret serverinstans
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

- Opretter vi en serverinstans ved hjælp af MCP SDK
- Definerer værktøjer ved hjælp af dekoratorer
- Bruger vi stdio_server context manager til at håndtere transporten

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

Den væsentlige forskel fra SSE er, at stdio-servere:

- Kræver ikke opsætning af webserver eller HTTP-endpoints
- Startes som subprocesses af klienten
- Kommunikerer via stdin/stdout-strømme
- Er enklere at implementere og fejlfinde

## Øvelse: Oprettelse af en stdio-server

For at oprette vores server skal vi huske to ting:

- Vi behøver ikke en webserver til at udstille endpoints for forbindelse og beskeder.

## Lab: Opret en simpel MCP stdio-server

I dette laboratorium opretter vi en simpel MCP-server ved hjælp af den anbefalede stdio-transport. Denne server vil udstille værktøjer, som klienter kan kalde ved hjælp af den standard Model Context Protocol.

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

# Konfigurer logning
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Opret serveren
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
    # Brug stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Væsentlige forskelle fra den afviklede SSE-tilgang

**Stdio Transport (Nuværende standard):**
- Simpelt subprocess-model - klient starter server som børneproces
- Kommunikation via stdin/stdout ved brug af JSON-RPC beskeder
- Ingen behov for HTTP-serveropsætning
- Bedre ydeevne og sikkerhed
- Nemmere fejlsøgning og udvikling

**SSE Transport (Aflivet pr. MCP 2025-06-18):**
- Krævede HTTP-server med SSE-endpoints
- Mere kompleks opsætning med webserverinfrastruktur
- Yderligere sikkerhedshensyn for HTTP-endpoints
- Nu erstattet af Streamable HTTP til webbaserede scenarier

### Oprettelse af en server med stdio transport

For at oprette vores stdio-server skal vi:

1. **Importere de nødvendige biblioteker** - Vi har brug for MCP serverkomponenter og stdio transport
2. **Oprette en serverinstans** - Definere serveren med dens kapabiliteter
3. **Definere værktøjer** - Tilføje den funktionalitet, vi ønsker at udstille
4. **Sætte transporten op** - Konfigurere stdio kommunikation
5. **Køre serveren** - Starte serveren og håndtere beskeder

Lad os bygge det trin for trin:

### Trin 1: Opret en grundlæggende stdio-server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurer logning
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Opret serveren
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

Serveren starter og venter på input fra stdin. Den kommunikerer ved hjælp af JSON-RPC beskeder over stdio-transporten.

### Trin 4: Test med Inspector

Du kan teste din server ved hjælp af MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kør Inspector og peg den mod din server
3. Test de værktøjer, du har oprettet

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

3. **Test din server**: Inspector tilbyder en webgrænseflade, hvor du kan:
   - Se serverkapabiliteter
   - Teste værktøjer med forskellige parametre
   - Overvåge JSON-RPC beskeder
   - Fejlsøge forbindelsesproblemer

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

2. Sæt breakpoint i din serverkode
3. Kør debuggeren og test med Inspector

### Almindelige fejlsøgningstips

- Brug `stderr` til logging - skriv aldrig til `stdout`, da det er reserveret til MCP-beskeder
- Sørg for, at alle JSON-RPC-beskeder er linjeskift-afgrænsede
- Test med simple værktøjer først, før du tilføjer kompleks funktionalitet
- Brug Inspector til at verificere beskedformater

## Brug af din stdio-server i VS Code

Når du har bygget din MCP stdio-server, kan du integrere den med VS Code for at bruge den med Claude eller andre MCP-kompatible klienter.

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

2. **Genstart Claude**: Luk og åbn Claude igen for at indlæse den nye serverkonfiguration.

3. **Test forbindelsen**: Start en samtale med Claude og prøv at bruge dine serverværktøjer:
   - "Kan du hilse på mig med hilsen tool?"
   - "Beregn summen af 15 og 27"
   - "Hvad er serverinfo?"

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

// Tilføj værktøjer
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

## Resumé

I denne opdaterede lektion har du lært at:

- Bygge MCP-servere ved brug af den aktuelle **stdio transport** (anbefalet tilgang)
- Forstå hvorfor SSE-transport blev afviklet til fordel for stdio og Streamable HTTP
- Oprette værktøjer, der kan kaldes af MCP-klienter
- Fejlsøge din server med MCP Inspector
- Integrere din stdio-server med VS Code og Claude

Stdio-transporten giver en enklere, mere sikker og mere ydeevnedæmpet metode til at bygge MCP-servere sammenlignet med den afviklede SSE-tilgang. Det er den anbefalede transport for de fleste MCP-serverimplementeringer fra og med specifikationen 2025-06-18.


### .NET

1. Lad os først lave nogle værktøjer. Til dette opretter vi en fil *Tools.cs* med følgende indhold:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Øvelse: Test din stdio-server

Nu hvor du har bygget din stdio-server, lad os teste den for at sikre, at den fungerer korrekt.

### Forudsætninger

1. Sørg for, at du har MCP Inspector installeret:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkode skal være gemt (f.eks. som `server.py`)

### Test med Inspector

1. **Start Inspector sammen med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åbn webgrænsefladen**: Inspector åbner et browservindue, der viser din servers kapabiliteter.

3. **Test værktøjerne**: 
   - Prøv `get_greeting`-værktøjet med forskellige navne
   - Test `calculate_sum`-værktøjet med forskellige tal
   - Kald `get_server_info`-værktøjet for at se servermetadata

4. **Overvåg kommunikationen**: Inspector viser JSON-RPC beskederne, der udveksles mellem klient og server.

### Hvad du bør se

Når din server starter korrekt, bør du se:
- Serverkapabiliteter listet i Inspector
- Værktøjer tilgængelige til test
- Vellykkede JSON-RPC-beskedudvekslinger
- Værktøjsresponser vist i grænsefladen

### Almindelige problemer og løsninger

**Serveren starter ikke:**
- Tjek at alle afhængigheder er installeret: `pip install mcp`
- Verificer Python-syntaks og indrykning
- Se efter fejlmeddelelser i konsollen

**Værktøjer vises ikke:**
- Sørg for at `@server.tool()`-dekoratorerne er til stede
- Tjek at værktøjsfunktioner er defineret før `main()`
- Verificer at serveren er konfigureret korrekt

**Forbindelsesproblemer:**
- Sørg for serveren bruger stdio-transport korrekt
- Kontroller at ingen andre processer forstyrrer
- Verificer Inspector-kommandoens syntaks

## Opgave

Forsøg at udbygge din server med flere funktionaliteter. Se [denne side](https://api.chucknorris.io/) for eksempelvis at tilføje et værktøj, der kalder et API. Du bestemmer, hvordan serveren skal se ud. Hav det sjovt :)

## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Nøglepointer

De vigtigste pointer fra dette kapitel er følgende:

- Stdio-transporten er den anbefalede mekanisme for lokale MCP-servere.
- Stdio-transport muliggør sømløs kommunikation mellem MCP-servere og klienter ved brug af standard input- og output-strømme.
- Du kan bruge både Inspector og Visual Studio Code til direkte at bruge stdio-servere, hvilket gør fejlfinding og integration enkel.

## Eksempler  

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Yderligere ressourcer

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hvad er det næste?

## Næste skridt

Nu hvor du har lært at bygge MCP-servere med stdio-transport, kan du udforske mere avancerede emner:

- **Næste**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) - Lær om den anden understøttede transportmekanisme til fjernservere
- **Avanceret**: [MCPs sikkerheds bedste praksis](../../02-Security/README.md) - Implementer sikkerhed i dine MCP-servere
- **Produktion**: [Implementeringsstrategier](../09-deployment/README.md) - Udrul dine servere til produktionsbrug

## Yderligere ressourcer

- [MCP-specifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiel specifikation
- [MCP SDK Dokumentation](https://github.com/modelcontextprotocol/sdk) - SDK referencer for alle sprog
- [Community-eksempler](../../06-CommunityContributions/README.md) - Flere servereksempler fra fællesskabet

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument i dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->