# MCP-server med stdio-transport

> **⚠️ Viktig uppdatering**: Från och med MCP-specifikationen 2025-06-18 har den fristående SSE (Server-Sent Events) transporten **avvecklats** och ersatts av "Streamable HTTP"-transporten. Den nuvarande MCP-specifikationen definierar två huvudsakliga transportmekanismer:
> 1. **stdio** - Standard in-/utström (rekommenderas för lokala servrar)
> 2. **Streamable HTTP** - För fjärrservrar som internt kan använda SSE
>
> Den här lektionen har uppdaterats för att fokusera på **stdio-transporten**, som är den rekommenderade metoden för de flesta MCP-serverimplementationer.

Stdio-transporten tillåter MCP-servrar att kommunicera med klienter genom standardin- och utströmmar. Detta är det mest använda och rekommenderade transportmekanismen i den nuvarande MCP-specifikationen och erbjuder ett enkelt och effektivt sätt att bygga MCP-servrar som lätt kan integreras med olika klientapplikationer.

## Översikt

Den här lektionen handlar om hur man bygger och använder MCP-servrar med stdio-transporten.

## Inlärningsmål

När du har avslutat denna lektion ska du kunna:

- Bygga en MCP-server med stdio-transport.
- Felsöka en MCP-server med hjälp av Inspector.
- Använda en MCP-server i Visual Studio Code.
- Förstå de nuvarande MCP-transportmekanismerna och varför stdio rekommenderas.

## stdio-transport – Hur det fungerar

Stdio-transporten är en av två stödjade transporttyper i den nuvarande MCP-specifikationen (2025-06-18). Så här fungerar den:

- **Enkel kommunikation**: Servern läser JSON-RPC-meddelanden från standardin (stdin) och skickar meddelanden till standardut (stdout).
- **Processbaserad**: Klienten startar MCP-servern som en underprocess.
- **Meddelandformat**: Meddelanden är individuella JSON-RPC-förfrågningar, notifikationer eller svar, avgränsade med radbrytningar.
- **Loggning**: Servern KAN skriva UTF-8-strängar till standardfel (stderr) för loggning.

### Viktiga krav:
- Meddelanden MÅSTE avgränsas med radbrytningar och FÅR INTE innehålla inbäddade radbrytningar
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

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

I koden ovan:

- Importerar vi `Server`-klassen och `StdioServerTransport` från MCP SDK:n
- Skapar en serverinstans med grundläggande konfiguration och funktioner
- Skapar en `StdioServerTransport`-instans och kopplar servern till den, vilket möjliggör kommunikation över stdin/stdout

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
- Definierar verktyg med dekoratörer
- Använder kontexthanteraren stdio_server för att hantera transporten

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

- Kräver ingen webbserver eller HTTP-endpoints
- Startas som underprocesser av klienten
- Kommunicerar via stdin/stdout-strömmar
- Är enklare att implementera och felsöka

## Övning: Skapa en stdio-server

För att skapa vår server behöver vi hålla två saker i åtanke:

- Vi behöver använda en webbserver för att exponera endpoints för anslutning och meddelanden.

## Lab: Skapa en enkel MCP stdio-server

I denna labb skapar vi en enkel MCP-server med den rekommenderade stdio-transporten. Denna server kommer att exponera verktyg som klienter kan anropa med den vanliga Model Context Protocol.

### Förutsättningar

- Python 3.8 eller senare
- MCP Python SDK: `pip install mcp`
- Grundläggande kunskap i asynkron programmering

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

**Stdio-transport (nuvarande standard):**
- Enkel subprocessmodell – klienten startar servern som en barnprocess
- Kommunikation via stdin/stdout med JSON-RPC-meddelanden
- Ingen HTTP-server behövs
- Bättre prestanda och säkerhet
- Lättare felsökning och utveckling

**SSE-transport (avvecklad från och med MCP 2025-06-18):**
- Kräver HTTP-server med SSE-endpoints
- Mer komplex setup med webbserverinfrastruktur
- Ytterligare säkerhetsaspekter för HTTP-endpoints
- Ersatt av Streamable HTTP för webbaserade scenarier

### Skapa en server med stdio-transport

För att skapa vår stdio-server behöver vi:

1. **Importera nödvändiga bibliotek** – Vi behöver MCP-serverkomponenterna och stdio-transporten
2. **Skapa en serverinstans** – Definiera servern med dess funktioner
3. **Definiera verktyg** – Lägg till funktionalitet som ska exponeras
4. **Konfigurera transporten** – Ställ in stdio-kommunikation
5. **Köra servern** – Starta servern och hantera meddelanden

Låt oss bygga detta steg för steg:

### Steg 1: Skapa en enkel stdio-server

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

### Steg 3: Köra servern

Spara koden som `server.py` och kör den från kommandoraden:

```bash
python server.py
```

Servern startar och väntar på indata från stdin. Den kommunicerar via JSON-RPC-meddelanden över stdio-transporten.

### Steg 4: Testa med Inspector

Du kan testa din server med MCP Inspector:

1. Installera Inspector: `npx @modelcontextprotocol/inspector`
2. Kör Inspector och peka den mot din server
3. Testa de verktyg du har skapat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Felsöka din stdio-server

### Använda MCP Inspector

MCP Inspector är ett värdefullt verktyg för felsökning och testning av MCP-servrar. Så här använder du det med din stdio-server:

1. **Installera Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kör Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa din server**: Inspector erbjuder ett webbgränssnitt där du kan:
   - Visa serverns funktioner
   - Testa verktyg med olika parametrar
   - Övervaka JSON-RPC-meddelanden
   - Felsöka anslutningsproblem

### Använda VS Code

Du kan även felsöka din MCP-server direkt i VS Code:

1. Skapa en startkonfiguration i `.vscode/launch.json`:
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
3. Kör felsökaren och testa med Inspector

### Vanliga felsökningstips

- Använd `stderr` för loggning – skriv aldrig till `stdout` som är reserverat för MCP-meddelanden
- Säkerställ att alla JSON-RPC-meddelanden är radbrytning-avgränsade
- Testa enkla verktyg först innan du lägger till komplex funktionalitet
- Använd Inspector för att kontrollera meddelandeformat

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

2. **Starta om Claude**: Stäng och öppna Claude igen för att ladda den nya serverkonfigurationen.

3. **Testa anslutningen**: Starta en konversation med Claude och prova att använda dina serververktyg:
   - "Kan du hälsa på mig med hälsningsverktyget?"
   - "Räkna ut summan av 15 och 27"
   - "Vad är serverinformationen?"

### Exempel på TypeScript stdio-server

Här är ett komplett exempel i TypeScript som referens:

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

I denna uppdaterade lektion har du lärt dig att:

- Bygga MCP-servrar med nuvarande **stdio-transport** (rekommenderad metod)
- Förstå varför SSE-transporten avvecklades till förmån för stdio och Streamable HTTP
- Skapa verktyg som kan anropas av MCP-klienter
- Felsöka din server med MCP Inspector
- Integrera din stdio-server med VS Code och Claude

Stdio-transporten erbjuder ett enklare, säkrare och mer presterande sätt att bygga MCP-servrar jämfört med den avvecklade SSE-metoden. Den är den rekommenderade transporten för de flesta MCP-serverimplementationer enligt specifikationen från 2025-06-18.

### .NET

1. Låt oss börja med att skapa några verktyg, vi skapar då en fil *Tools.cs* med följande innehåll:

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

2. Din serverkod ska vara sparad (t.ex. som `server.py`)

### Testa med Inspector

1. **Starta Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öppna webbgränssnittet**: Inspector öppnar ett webbfönster som visar serverns funktioner.

3. **Testa verktygen**:
   - Prova `get_greeting`-verktyget med olika namn
   - Testa `calculate_sum`-verktyget med olika tal
   - Anropa `get_server_info`-verktyget för att se servermetadata

4. **Övervaka kommunikationen**: Inspector visar JSON-RPC-meddelanden som utbyts mellan klient och server.

### Vad du bör se

När din server startar korrekt bör du se:
- Serverns funktioner listade i Inspector
- Verktyg som finns tillgängliga för testning
- Framgångsrika JSON-RPC-meddelandeutbyten
- Verktygsrespons visad i gränssnittet

### Vanliga problem och lösningar

**Servern startar inte:**
- Kontrollera att alla beroenden är installerade: `pip install mcp`
- Kontrollera Python-syntax och indentering
- Leta efter felmeddelanden i konsolen

**Verktyg syns inte:**
- Säkerställ att `@server.tool()`-dekoratörer finns
- Kontrollera att verktygsfunktioner är definierade före `main()`
- Bekräfta att servern är korrekt konfigurerad

**Anslutningsproblem:**
- Se till att servern använder stdio-transport korrekt
- Kontrollera att inga andra processer stör
- Kontrollera syntaxen i Inspector-kommandot

## Uppdrag

Försök bygga ut din server med fler funktioner. Se [den här sidan](https://api.chucknorris.io/) för att till exempel lägga till ett verktyg som anropar ett API. Du bestämmer hur servern ska se ut. Ha kul :)

## Lösning

[Lösning](./solution/README.md) Här finns en möjlig lösning med fungerande kod.

## Viktiga lärdomar

De viktigaste lärdomarna från detta kapitel är:

- stdio-transporten är den rekommenderade mekanismen för lokala MCP-servrar.
- Stdio-transporten möjliggör sömlös kommunikation mellan MCP-servrar och klienter via standardin- och utström.
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

- **Nästa**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lär dig om den andra stödjade transportmekanismen för fjärrservrar
- **Avancerat**: [MCP:s säkerhetsbästa metoder](../../02-Security/README.md) – Implementera säkerhet i dina MCP-servrar
- **Produktion**: [Driftsättningsstrategier](../09-deployment/README.md) – Driftsätt dina servrar för produktion

## Ytterligare resurser

- [MCP-specifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Officiell specifikation
- [MCP SDK-dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-referenser för alla språk
- [Exempel från communityn](../../06-CommunityContributions/README.md) – Fler serverexempel från communityn

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var vänlig observera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->