# MCP-server med stdio-transport

> **⚠️ Vigtig opdatering**: Fra og med MCP-specifikationen 2025-06-18 er den selvstændige SSE (Server-Sent Events) transport blevet **afskaffet** og erstattet af "Streamable HTTP"-transport. Den aktuelle MCP-specifikation definerer to primære transportmekanismer:
> 1. **stdio** - Standard input/output (anbefalet til lokale servere)
> 2. **Streamable HTTP** - Til fjernservere, der eventuelt bruger SSE internt
>
> Denne lektion er blevet opdateret til at fokusere på **stdio-transporten**, som er den anbefalede tilgang for de fleste MCP-serverimplementeringer.

Stdio-transporten gør det muligt for MCP-servere at kommunikere med klienter gennem standard input og output-strømme. Dette er den mest anvendte og anbefalede transportmekanisme i den aktuelle MCP-specifikation, og giver en enkel og effektiv måde at bygge MCP-servere, som nemt kan integreres med forskellige klientapplikationer.

## Oversigt

Denne lektion dækker, hvordan man bygger og bruger MCP-servere med stdio-transporten.

## Læringsmål

Når du har gennemført denne lektion, vil du kunne:

- Bygge en MCP-server ved hjælp af stdio-transporten.
- Debugge en MCP-server med Inspector.
- Bruge en MCP-server via Visual Studio Code.
- Forstå de nuværende MCP-transportmekanismer og hvorfor stdio anbefales.


## stdio-transport – Sådan fungerer det

Stdio-transporten er en af to understøttede transporttyper i den aktuelle MCP-specifikation (2025-06-18). Sådan fungerer den:

- **Simpel kommunikation**: Serveren læser JSON-RPC-beskeder fra standard input (`stdin`) og sender beskeder til standard output (`stdout`).
- **Procesbaseret**: Klienten starter MCP-serveren som en underproces.
- **Beskedformat**: Beskeder er enkeltstående JSON-RPC-forespørgsler, notifikationer eller svar, adskilt af linjeskift.
- **Logging**: Serveren KAN skrive UTF-8-strenge til standard error (`stderr`) til logformål.

### Nøglekrav:
- Beskeder SKAL være adskilt af linjeskift og MÅ IKKE indeholde indlejrede linjeskift
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
```

I den foregående kode:

- Importerer vi `Server`-klassen og `StdioServerTransport` fra MCP SDK'en
- Opretter vi en serverinstans med grundlæggende konfiguration og kapaciteter

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
- Definerer vi værktøjer med dekoratorer
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

Den vigtigste forskel fra SSE er, at stdio-servere:

- Ikke kræver opsætning af webserver eller HTTP-endpoints
- Startes som underprocesser af klienten
- Kommunikerer via stdin/stdout-strømme
- Er nemmere at implementere og debugge

## Øvelse: Oprette en stdio-server

For at oprette vores server skal vi huske to ting:

- Vi behøver ikke en webserver til at eksponere endpoints for forbindelse og beskeder.
## Laboratorium: Oprette en simpel MCP stdio-server

I dette laboratorium vil vi oprette en simpel MCP-server ved hjælp af den anbefalede stdio-transport. Denne server vil eksponere værktøjer, som klienter kan kalde via den standard Model Context Protocol.

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

## Vigtige forskelle fra den afskaffede SSE-tilgang

**Stdio-transport (nuværende standard):**
- Simpel underprocesmodel – klienten starter server som en underproces
- Kommunikation via stdin/stdout med JSON-RPC-beskeder
- Kræver ikke opsætning af HTTP-server
- Bedre ydelse og sikkerhed
- Nemmere at debugge og udvikle

**SSE-transport (afskaffet pr. MCP 2025-06-18):**
- Krævede HTTP-server med SSE-endpoints
- Mere kompleks opsætning med webserverinfrastruktur
- Yderligere sikkerhedshensyn for HTTP-endpoints
- Er nu erstattet af Streamable HTTP til webbaserede scenarier

### Oprette en server med stdio-transport

For at oprette vores stdio-server skal vi:

1. **Importere de nødvendige biblioteker** - Vi skal bruge MCP-serverkomponenter og stdio-transporten
2. **Oprette en serverinstans** - Definer serveren med dens kapaciteter
3. **Definere værktøjer** - Tilføje den funktionalitet, vi vil eksponere
4. **Opsætte transporten** - Konfigurere stdio-kommunikationen
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

Serveren starter og venter på input fra stdin. Den kommunikerer via JSON-RPC-beskeder over stdio-transporten.

### Trin 4: Test med Inspector

Du kan teste din server med MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kør Inspector og peg den mod din server
3. Test de værktøjer, du har oprettet

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug din stdio-server

### Brug af MCP Inspector

MCP Inspector er et værdifuldt værktøj til debugging og test af MCP-servere. Sådan bruger du det med din stdio-server:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test din server**: Inspector tilbyder en webgrænseflade, hvor du kan:
   - Se serverkapaciteter
   - Teste værktøjer med forskellige parametre
   - Overvåge JSON-RPC-beskeder
   - Debugge forbindelsesproblemer

### Brug af VS Code

Du kan også debugge din MCP-server direkte i VS Code:

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

2. Sæt breakpoints i din serverkode
3. Kør debuggeren og test med Inspector

### Almindelige debuggingtips

- Brug `stderr` til logging – skriv aldrig til `stdout`, da det er reserveret til MCP-beskeder
- Sørg for, at alle JSON-RPC-beskeder er linjeskift-delimiterede
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

2. **Genstart Claude**: Luk og genåbn Claude for at loade den nye serverkonfiguration.

3. **Test forbindelsen**: Start en samtale med Claude og prøv at bruge dine serverværktøjer:
   - "Kan du hilse på mig med hilsesværktøjet?"
   - "Beregn summen af 15 og 27"
   - "Hvad er serveroplysningerne?"

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

I denne opdaterede lektion lærte du at:

- Bygge MCP-servere med den nuværende **stdio-transport** (anbefalet metode)
- Forstå hvorfor SSE-transport blev afskaffet til fordel for stdio og Streamable HTTP
- Oprette værktøjer, som MCP-klienter kan kalde
- Debugge din server med MCP Inspector
- Integrere din stdio-server med VS Code og Claude

Stdio-transporten giver en enklere, mere sikker og mere effektiv måde at bygge MCP-servere på sammenlignet med den afskaffede SSE-tilgang. Det er den anbefalede transport for de fleste MCP-serverimplementeringer i henhold til specifikationen fra 2025-06-18.


### .NET

1. Lad os først oprette nogle værktøjer, til dette laver vi en fil *Tools.cs* med følgende indhold:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Øvelse: Test din stdio-server

Nu hvor du har bygget din stdio-server, lad os teste, at den fungerer korrekt.

### Forudsætninger

1. Sørg for, at MCP Inspector er installeret:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkode skal være gemt (f.eks. som `server.py`)

### Test med Inspector

1. **Start Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åbn webgrænsefladen**: Inspector åbner et browservindue, der viser dine serverkapaciteter.

3. **Test værktøjerne**: 
   - Prøv `get_greeting`-værktøjet med forskellige navne
   - Test `calculate_sum`-værktøjet med forskellige tal
   - Kald `get_server_info`-værktøjet for at se servermetadata

4. **Overvåg kommunikationen**: Inspector viser JSON-RPC-beskederne, der udveksles mellem klient og server.

### Hvad du bør se

Når din server starter korrekt, bør du se:
- Serverkapaciteter listet i Inspector
- Værktøjer tilgængelige til test
- Vellykkede JSON-RPC-beskedudvekslinger
- Værktøjs-svar vist i grænsefladen

### Almindelige problemer og løsninger

**Serveren starter ikke:**
- Tjek at alle afhængigheder er installeret: `pip install mcp`
- Verificer Python-syntaks og indrykninger
- Kig efter fejlbeskeder i konsollen

**Værktøjer vises ikke:**
- Sørg for, at `@server.tool()`-dekoratører er til stede
- Kontroller at værktøjsfunktionerne er defineret før `main()`
- Bekræft at serveren er korrekt konfigureret

**Forbindelsesproblemer:**
- Sørg for, at serveren bruger stdio-transport korrekt
- Tjek at ingen andre processer forstyrrer
- Verificer Inspector-kommandoens syntaks

## Opgave

Prøv at udvide din server med flere kapaciteter. Se [denne side](https://api.chucknorris.io/) for eksempelvis at tilføje et værktøj, der kalder et API. Du bestemmer, hvordan serveren skal se ud. God fornøjelse :)
## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Centrale pointer

De vigtigste pointer fra dette kapitel er:

- Stdio-transporten er den anbefalede mekanisme til lokale MCP-servere.
- Stdio-transport muliggør gnidningsfri kommunikation mellem MCP-servere og klienter via standard input- og output-strømme.
- Du kan bruge både Inspector og Visual Studio Code til at anvende stdio-servere direkte, hvilket gør debugging og integration nemt.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Yderligere ressourcer

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hvad er næste skridt

## Næste skridt

Nu hvor du har lært at bygge MCP-servere med stdio-transporten, kan du udforske mere avancerede emner:

- **Næste:** [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) - Lær om den anden understøttede transportmekanisme til fjernservere
- **Avanceret:** [MCP Security Best Practices](../../02-Security/README.md) - Implementer sikkerhed i dine MCP-servere
- **Produktion:** [Deployeringstrategier](../09-deployment/README.md) - Udrul dine servere til produktion

## Yderligere ressourcer

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiel specifikation
- [MCP SDK-dokumentation](https://github.com/modelcontextprotocol/sdk) - SDK-referencer for alle sprog
- [Community-eksempler](../../06-CommunityContributions/README.md) - Flere servereksempler fra fællesskabet

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->