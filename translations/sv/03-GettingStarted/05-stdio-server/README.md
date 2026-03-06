# MCP-server med stdio-transport

> **⚠️ Viktig uppdatering**: Från och med MCP-specifikationen 2025-06-18 har den fristående SSE (Server-Sent Events)-transporten **avvecklats** och ersatts av "Streamable HTTP"-transport. Den nuvarande MCP-specifikationen definierar två huvudsakliga transportmekanismer:
> 1. **stdio** - Standard in-/utström (rekommenderas för lokala servrar)
> 2. **Streamable HTTP** - För fjärrservrar som kan använda SSE internt
>
> Denna lektion har uppdaterats för att fokusera på **stdio-transporten**, som är den rekommenderade metoden för de flesta MCP-serverimplementationer.

Stdio-transporten tillåter MCP-servrar att kommunicera med klienter via standardin- och utströmmar. Detta är den vanligaste och rekommenderade transportmekanismen i den nuvarande MCP-specifikationen, vilket ger ett enkelt och effektivt sätt att bygga MCP-servrar som lätt kan integreras med olika klientapplikationer.

## Översikt

Denna lektion täcker hur man skapar och använder MCP-servrar med stdio-transporten.

## Läromål

Efter denna lektion kommer du kunna:

- Bygga en MCP-server med stdio-transporten.
- Felsöka en MCP-server med Inspector.
- Använda en MCP-server i Visual Studio Code.
- Förstå de nuvarande MCP-transportmekanismerna och varför stdio rekommenderas.

## stdio-transport – Hur det fungerar

Stdio-transporten är en av två stödda transporttyper i den nuvarande MCP-specifikationen (2025-06-18). Så här fungerar den:

- **Enkel kommunikation**: Servern läser JSON-RPC-meddelanden från standardin (`stdin`) och skickar meddelanden till standardut (`stdout`).
- **Processbaserad**: Klienten startar MCP-servern som en underprocess.
- **Meddelandeformat**: Meddelanden är enskilda JSON-RPC-förfrågningar, notifikationer eller svar, avgränsade med nya rader.
- **Loggning**: Servern KAN skriva UTF-8-strängar till standardfel (`stderr`) för loggningsändamål.

### Viktiga krav:
- Meddelanden MÅSTE avgränsas med nya rader och FÅR INTE innehålla inbäddade nya rader
- Servern FÅR INTE skriva något till `stdout` som inte är ett giltigt MCP-meddelande
- Klienten FÅR INTE skriva något till serverns `stdin` som inte är ett giltigt MCP-meddelande

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

I koden ovan:

- Importerar vi klassen `Server` och `StdioServerTransport` från MCP SDK
- Skapar en serverinstans med grundläggande konfiguration och kapabiliteter

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Skapa serverinstans
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

I koden ovan:

- Skapar vi en serverinstans med MCP SDK
- Definierar verktyg med dekoratorer
- Använder context managern stdio_server för att hantera transporten

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

Den stora skillnaden från SSE är att stdio-servrar:

- Kräver ingen webbserverkonfiguration eller HTTP-endpoints
- Startas som underprocesser av klienten
- Kommunicerar via stdin/stdout-strömmar
- Är enklare att implementera och felsöka

## Övning: Skapa en stdio-server

För att skapa vår server måste vi hålla två saker i åtanke:

- Vi behöver använda en webbserver för att exponera endpoints för anslutning och meddelanden.

## Lab: Skapa en enkel MCP stdio-server

I denna labb skapar vi en enkel MCP-server med rekommenderad stdio-transport. Denna server kommer att exponera verktyg som klienter kan anropa med standard Model Context Protocol.

### Förutsättningar

- Python 3.8 eller senare
- MCP Python SDK: `pip install mcp`
- Grundläggande förståelse för asynkron programmering

Låt oss börja med att skapa vår första MCP stdio-server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigurera loggning
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Skapa servern
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
    # Använd stdio-transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Viktiga skillnader från den avvecklade SSE-metoden

**Stdio Transport (Nuvarande standard):**
- Enkel underprocessmodell – klient startar server som barnprocess
- Kommunikation via stdin/stdout med JSON-RPC-meddelanden
- Ingen HTTP-server behövs
- Bättre prestanda och säkerhet
- Lättare att felsöka och utveckla

**SSE Transport (Avvecklad sedan MCP 2025-06-18):**
- Kräver HTTP-server med SSE-endpoints
- Mer komplex setup med webbserverinfrastruktur
- Ytterligare säkerhetsaspekter för HTTP-endpoints
- Ersatt av Streamable HTTP för webb-baserade scenarier

### Skapa en server med stdio-transport

För att skapa vår stdio-server behöver vi:

1. **Importera nödvändiga bibliotek** - Vi behöver MCP-serverkomponenter och stdio-transport
2. **Skapa en serverinstans** - Definiera servern och dess kapabiliteter
3. **Definiera verktyg** - Lägg till funktionalitet som ska exponeras
4. **Konfigurera transporten** - Ställ in stdio-kommunikation
5. **Kör servern** - Starta servern och hantera meddelanden

Låt oss bygga detta steg för steg:

### Steg 1: Skapa en grundläggande stdio-server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurera loggning
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Skapa servern
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

### Steg 2: Lägg till fler verktyg

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

### Steg 3: Kör servern

Spara koden som `server.py` och kör den via kommandoraden:

```bash
python server.py
```

Servern startar och väntar på indata via stdin. Den kommunicerar med JSON-RPC-meddelanden över stdio-transporten.

### Steg 4: Testa med Inspector

Du kan testa din server med MCP Inspector:

1. Installera Inspector: `npx @modelcontextprotocol/inspector`
2. Starta Inspector och peka den mot din server
3. Testa de verktyg du har skapat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Felsök din stdio-server

### Använd MCP Inspector

MCP Inspector är ett värdefullt verktyg för felsökning och testning av MCP-servrar. Så här använder du det med din stdio-server:

1. **Installera Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kör Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa servern**: Inspectorn erbjuder ett webbgränssnitt där du kan:
   - Visa serverns kapabiliteter
   - Testa verktyg med olika parametrar
   - Övervaka JSON-RPC-meddelanden
   - Felsöka anslutningsproblem

### Använda VS Code

Du kan också felsöka din MCP-server direkt i VS Code:

1. Skapa en launch-konfiguration i `.vscode/launch.json`:
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

2. Sätt brytpunkter i serverkoden
3. Kör debuggern och testa med Inspector

### Vanliga felsökningstips

- Använd `stderr` för loggning – skriv aldrig till `stdout` eftersom det är reserverat för MCP-meddelanden
- Säkerställ att alla JSON-RPC-meddelanden är radavgränsade
- Testa med enkla verktyg innan du lägger till komplex funktionalitet
- Använd Inspector för att verifiera meddelandeformat

## Använda din stdio-server i VS Code

När du har byggt din MCP stdio-server kan du integrera den med VS Code för att använda den med Claude eller andra MCP-kompatibla klienter.

### Konfiguration

1. **Skapa en MCP-konfigurationsfil** på `%APPDATA%\Claude\claude_desktop_config.json` (Windows) eller `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Starta om Claude**: Stäng och öppna Claude på nytt för att läsa in den nya serverkonfigurationen.

3. **Testa anslutningen**: Starta en konversation med Claude och försök använda serverns verktyg:
   - "Kan du hälsa på mig med hälsningsverktyget?"
   - "Beräkna summan av 15 och 27"
   - "Vad är serverinformationen?"

### Exempel på TypeScript stdio-server

Här är ett komplett TypeScript-exempel för referens:

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

// Lägg till verktyg
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

### Exempel på .NET stdio-server

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

## Sammanfattning

I denna uppdaterade lektion lärde du dig att:

- Bygga MCP-servrar med nuvarande **stdio-transport** (rekommenderad metod)
- Förstå varför SSE-transport avvecklades till förmån för stdio och Streamable HTTP
- Skapa verktyg som kan anropas av MCP-klienter
- Felsöka din server med MCP Inspector
- Integrera din stdio-server med VS Code och Claude

Stdio-transporten erbjuder ett enklare, säkrare och mer effektivt sätt att bygga MCP-servrar jämfört med den avvecklade SSE-metoden. Det är den rekommenderade transporten för de flesta MCP-serverimplementationer enligt specifikationen från 2025-06-18.


### .NET

1. Låt oss först skapa några verktyg, för detta skapar vi en fil *Tools.cs* med följande innehåll:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Övning: Testa din stdio-server

Nu när du har byggt din stdio-server, låt oss testa att den fungerar korrekt.

### Förutsättningar

1. Säkerställ att du har MCP Inspector installerad:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkod ska sparas (t.ex. som `server.py`)

### Testa med Inspector

1. **Starta Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öppna webbgränssnittet**: Inspectorn öppnar ett webbfönster där din servers kapabiliteter visas.

3. **Testa verktygen**:
   - Prova `get_greeting`-verktyget med olika namn
   - Testa `calculate_sum`-verktyget med olika siffror
   - Anropa `get_server_info`-verktyget för att se servermetadata

4. **Övervaka kommunikationen**: Inspectorn visar de JSON-RPC-meddelanden som utbyts mellan klient och server.

### Vad du bör se

När din server startar korrekt bör du se:
- Serverns kapabiliteter listade i Inspectorn
- Verktyg tillgängliga för testning
- Lyckade JSON-RPC-meddelandebyten
- Verktygssvar visade i gränssnittet

### Vanliga problem och lösningar

**Servern startar inte:**
- Kontrollera att alla beroenden är installerade: `pip install mcp`
- Verifiera Python-syntax och indentering
- Leta efter felmeddelanden i konsolen

**Verktygen visas inte:**
- Säkerställ att `@server.tool()`-dekoratorer finns med
- Kontrollera att verktygsfunktioner är definierade före `main()`
- Verifiera att servern är korrekt konfigurerad

**Anslutningsproblem:**
- Kontrollera att servern använder stdio-transport korrekt
- Kontrollera att inga andra processer stör
- Verifiera syntaxen för Inspector-kommandot

## Uppgift

Försök att bygga ut din server med fler kapabiliteter. Se [den här sidan](https://api.chucknorris.io/) för exempel på hur du kan lägga till ett verktyg som anropar ett API. Du bestämmer hur servern ska se ut. Lycka till :)

## Lösning

[Lösning](./solution/README.md) Här är en möjlig lösning med fungerande kod.

## Viktiga punkter

De viktigaste punkterna från detta kapitel är:

- Stdio-transport är den rekommenderade mekanismen för lokala MCP-servrar.
- Stdio-transport möjliggör sömlös kommunikation mellan MCP-servrar och klienter med standard in- och utflöden.
- Du kan använda både Inspector och Visual Studio Code för att direkt använda stdio-servrar, vilket gör felsökning och integration enkel.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Ytterligare resurser

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Vad händer härnäst

## Nästa steg

Nu när du har lärt dig bygga MCP-servrar med stdio-transport kan du utforska mer avancerade ämnen:

- **Nästa**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lär dig om den andra stödda transportmekanismen för fjärrservrar
- **Avancerat**: [MCP Security Best Practices](../../02-Security/README.md) – Implementera säkerhet i dina MCP-servrar
- **Produktion**: [Deploy-strategier](../09-deployment/README.md) – Driftsätt dina servrar för produktion

## Ytterligare resurser

- [MCP-specifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Officiell specifikation
- [MCP SDK-dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-referenser för alla språk
- [Community-exempel](../../06-CommunityContributions/README.md) – Fler serverexempel från communityn

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->