# MCP-server med stdio Transport

> **⚠️ Vigtig opdatering**: Fra MCP-specifikationen 2025-06-18 er den selvstændige SSE (Server-Sent Events) transport **udgået** og erstattet af "Streamable HTTP" transport. Den nuværende MCP-specifikation definerer to primære transportmekanismer:
> 1. **stdio** - Standard input/output (anbefalet til lokale servere)
> 2. **Streamable HTTP** - For fjernservere, der kan bruge SSE internt
>
> Denne lektion er opdateret til at fokusere på **stdio transporten**, som er den anbefalede tilgang til de fleste MCP-serverimplementeringer.

Stdio transporten giver MCP-servere mulighed for at kommunikere med klienter via standard input og output strømmene. Dette er den mest anvendte og anbefalede transportmekanisme i den nuværende MCP-specifikation og giver en enkel og effektiv måde at bygge MCP-servere, som nemt kan integreres med forskellige klientapplikationer.

## Oversigt

Denne lektion dækker, hvordan man bygger og forbruger MCP-servere ved hjælp af stdio transporten.

## Læringsmål

Ved slutningen af denne lektion vil du kunne:

- Bygge en MCP-server ved hjælp af stdio transport.
- Fejlsøge en MCP-server ved hjælp af Inspector.
- Forbruge en MCP-server ved hjælp af Visual Studio Code.
- Forstå de nuværende MCP transportmekanismer og hvorfor stdio anbefales.


## stdio Transport – Hvordan det virker

Stdio transporten er en af de to standardtransporter i MCP-specifikationen
`2026-07-28`. Sådan fungerer den:

- **Simpel kommunikation**: Serveren læser JSON-RPC beskeder fra standard input (`stdin`) og sender beskeder til standard output (`stdout`).
- **Proces-baseret**: Klienten starter MCP-serveren som en subprocess.
- **Beskedformat**: Beskeder er individuelle JSON-RPC forespørgsler, notifikationer eller svar, afgrænset af nye linjer.
- **Logning**: Serveren KAN skrive UTF-8 strenge til standard error (`stderr`) til logformål.

### Vigtige krav:
- Beskeder SKAL være afgrænset af nye linjer og MÅ IKKE indeholde indlejrede nye linjer
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

I ovenstående kode:

- Importerer vi `Server` klassen og `StdioServerTransport` fra MCP SDK
- Opretter en serverinstans med grundlæggende konfiguration og muligheder
- Opretter en `StdioServerTransport` instans og forbinder serveren til den, så kommunikation over stdin/stdout muliggøres

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

I ovenstående kode:

- Opretter vi en serverinstans ved brug af MCP SDK
- Definerer værktøjer ved hjælp af dekoratører
- Bruger stdio_server kontekstmanageren til at håndtere transporten

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
- Kommunikerer via stdin/stdout strømme
- Er enklere at implementere og fejlfinde

## Øvelse: Opret en stdio-server

For at oprette vores server skal vi have to ting i tankerne:

- Vi skal bruge en webserver til at eksponere endpoints for forbindelse og beskeder.
## Laboratorium: Opret en simpel MCP stdio server

I dette laboratorium vil vi lave en simpel MCP-server ved hjælp af den anbefalede stdio-transport. Denne server vil eksponere værktøjer, som klienter kan kalde ved brug af den standard Model Context Protocol.

### Forudsætninger

- Python 3.8 eller senere
- MCP Python SDK: `pip install mcp`
- Grundlæggende forståelse af asynkron programmering

Lad os starte med at oprette vores første MCP stdio server:

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

## Væsentlige forskelle fra den udfasede SSE-metode

**Stdio Transport (Nuværende standard):**
- Simpel subprocess-model – klienten starter server som underproces
- Kommunikation via stdin/stdout ved brug af JSON-RPC beskeder
- Ingen HTTP-serveropsætning nødvendig
- Bedre ydeevne og sikkerhed
- Nemmere fejlsøgning og udvikling

**SSE Transport (Udfaset fra og med MCP 2025-06-18):**
- Krævet HTTP-server med SSE-endpoints
- Mere kompleks opsætning med webserverinfrastruktur
- Yderligere sikkerhedsovervejelser for HTTP-endpoints
- Er nu erstattet af Streamable HTTP til webbaserede scenarier

### Oprettelse af en server med stdio transport

For at oprette vores stdio server skal vi:

1. **Importere de nødvendige biblioteker** – Vi skal bruge MCP-serverkomponenterne og stdio-transporten
2. **Oprette en serverinstans** – Definere serveren med dens kapabiliteter
3. **Definere værktøjer** – Tilføje den funktionalitet, vi ønsker at eksponere
4. **Konfigurere transporten** – Sætte stdio-kommunikationen op
5. **Køre serveren** – Starte serveren og håndtere beskeder

Lad os bygge dette trin for trin:

### Trin 1: Opret en basal stdio server

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

### Trin 3: Køre serveren

Gem koden som `server.py` og kør den fra kommandolinjen:

```bash
python server.py
```

Serveren starter og venter på input fra stdin. Den kommunikerer ved brug af JSON-RPC beskeder over stdio transporten.

### Trin 4: Test med Inspector

Du kan teste din server ved at bruge MCP Inspector:

1. Installer Inspector: `npx @modelcontextprotocol/inspector`
2. Kør Inspector og peg den på din server
3. Test de værktøjer, du har oprettet

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Fejlsøgning af din stdio server

### Brug af MCP Inspector

MCP Inspector er et værdifuldt værktøj til fejlfinding og test af MCP-servere. Sådan bruger du det med din stdio server:

1. **Installer Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kør Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test din server**: Inspector leverer et webinterface hvor du kan:
   - Se serverens kapabiliteter
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

2. Sæt breakpoints i din serverkode
3. Kør debuggeren og test med Inspector

### Almindelige fejlfindingstips

- Brug `stderr` til logning – skriv aldrig til `stdout`, da det er reserveret til MCP-beskeder
- Sørg for at alle JSON-RPC beskeder er afgrænset med nye linjer
- Test med simple værktøjer først før tilføjelse af kompleks funktionalitet
- Brug Inspector til at verificere beskedformater

## Forbrug din stdio server i VS Code

Når du har bygget din MCP stdio server, kan du integrere den med VS Code for at bruge den med Claude eller andre MCP-kompatible klienter.

### Konfiguration

1. **Opret en MCP konfigurationsfil** på `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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
   - "Kan du hilse på mig med hilsen-værktøjet?"
   - "Beregn summen af 15 og 27"
   - "Hvad er serverinformationen?"

### TypeScript stdio server eksempel

Her er et komplet TypeScript eksempel til reference:

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

### .NET stdio server eksempel

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

I denne opdaterede lektion har du lært hvordan man:

- Bygger MCP-servere ved hjælp af den nuværende **stdio transport** (anbefalet tilgang)
- Forstår hvorfor SSE transporten blev udfaset til fordel for stdio og Streamable HTTP
- Opretter værktøjer, som MCP-klienter kan kalde
- Fejlsøger din server ved hjælp af MCP Inspector
- Integrerer din stdio server med VS Code og Claude

Stdio transporten tilbyder en enklere, mere sikker og mere effektiv måde at bygge MCP-servere på sammenlignet med den udfasede SSE tilgang. Det er den anbefalede transport for de fleste MCP-serverimplementeringer fra og med 2025-06-18 specifikationen.


### .NET

1. Lad os først lave nogle værktøjer, til dette opretter vi en fil *Tools.cs* med følgende indhold:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Øvelse: Test din stdio-server

Nu hvor du har bygget din stdio-server, lad os teste den for at sikre, at den virker korrekt.

### Forudsætninger

1. Sørg for at MCP Inspector er installeret:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkode skal være gemt (f.eks. som `server.py`)

### Test med Inspector

1. **Start Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Åbn webinterfacet**: Inspector åbner et browservindue, der viser serverens kapabiliteter.

3. **Test værktøjerne**: 
   - Prøv `get_greeting` værktøjet med forskellige navne
   - Test `calculate_sum` værktøjet med forskellige tal
   - Kald `get_server_info` værktøjet for at se servermetadata

4. **Overvåg kommunikationen**: Inspector viser JSON-RPC beskeder mellem klient og server.

### Hvad du bør se

Når serveren starter korrekt, bør du se:
- Serverens kapabiliteter listet i Inspector
- Værktøjer tilgængelige til test
- Vellykkede JSON-RPC beskedudvekslinger
- Værktøjsresponser vist i interfacet

### Almindelige problemer og løsninger

**Serveren vil ikke starte:**
- Tjek at alle afhængigheder er installerede: `pip install mcp`
- Verificer Python syntaks og indrykning
- Kig efter fejlmeddelelser i konsollen

**Værktøjer vises ikke:**
- Sørg for `@server.tool()` dekoratører er til stede
- Tjek at værktøjsfunktioner er defineret før `main()`
- Verificer at serveren er korrekt konfigureret

**Forbindelsesproblemer:**
- Sørg for at serveren bruger stdio transport korrekt
- Tjek at ingen andre processer forstyrrer
- Verificer Inspector kommandosyntaks

## Opgave

Prøv at udbygge din server med flere funktionaliteter. Se [denne side](https://api.chucknorris.io/) for eksempelvis at tilføje et værktøj der kalder en API. Du bestemmer, hvordan serveren skal se ud. Hav det sjovt :)
## Løsning

[Løsning](./solution/README.md) Her er en mulig løsning med fungerende kode.

## Vigtige pointer

De væsentlige pointer fra dette kapitel er følgende:

- Stdio transporten er den anbefalede mekanisme for lokale MCP-servere.
- Stdio transport tillader sømløs kommunikation mellem MCP-servere og klienter ved brug af standard input- og outputstrømme.
- Du kan bruge både Inspector og Visual Studio Code til direkte at forbruge stdio-servere, hvilket gør fejlfinding og integration nem.

## Eksempler

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Yderligere ressourcer

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Hvad nu?

## Næste skridt

Nu hvor du har lært at bygge MCP-servere med stdio transporten, kan du udforske mere avancerede emner:

- **Næste**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) - Lær om den anden understøttede transportmekanisme til fjernservere
- **Avanceret**: [MCP Security Best Practices](../../02-Security/README.md) - Implementér sikkerhed i dine MCP-servere
- **Produktion**: [Deploymentsstrategier](../09-deployment/README.md) - Udrul dine servere til produktion

## Yderligere ressourcer

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Nuværende specifikation
- [MCP SDK Dokumentation](https://github.com/modelcontextprotocol/sdk) - SDK-referencer for alle sprog
- [Community Eksempler](../../06-CommunityContributions/README.md) - Flere servereksempler fra fællesskabet

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->