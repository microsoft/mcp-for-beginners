# MCP-server med stdio-transport

> **⚠️ Viktig uppdatering**: Från och med MCP-specifikationen 2025-06-18 har den fristående SSE-transporten (Server-Sent Events) **avvecklats** och ersatts av "Streamable HTTP"-transport. Den nuvarande MCP-specifikationen definierar två primära transportmekanismer:
> 1. **stdio** - Standard in-/utmatning (rekommenderas för lokala servrar)
> 2. **Streamable HTTP** - För fjärrservrar som kan använda SSE internt
>
> Den här lektionen har uppdaterats för att fokusera på **stdio-transport**, vilket är det rekommenderade tillvägagångssättet för de flesta MCP-serverimplementationer.

Stdio-transporten gör det möjligt för MCP-servrar att kommunicera med klienter via standard in- och utmatningsströmmar. Detta är den mest använda och rekommenderade transportmekanismen i den nuvarande MCP-specifikationen, och den erbjuder ett enkelt och effektivt sätt att bygga MCP-servrar som enkelt kan integreras med olika klientapplikationer.

## Översikt

Den här lektionen täcker hur man bygger och använder MCP-servrar med stdio-transport.

## Lärandemål

I slutet av den här lektionen kommer du att kunna:

- Bygga en MCP-server med stdio-transport.
- Felsöka en MCP-server med hjälp av Inspector.
- Använda en MCP-server i Visual Studio Code.
- Förstå de nuvarande MCP-transportmekanismerna och varför stdio rekommenderas.

## Stdio-transport – Så fungerar det

Stdio-transporten är en av två stödda transporttyper i den nuvarande MCP-specifikationen (2025-06-18). Så här fungerar det:

- **Enkel kommunikation**: Servern läser JSON-RPC-meddelanden från standard inmatning (`stdin`) och skickar meddelanden till standard utmatning (`stdout`).
- **Processbaserad**: Klienten startar MCP-servern som en underprocess.
- **Meddelandeformat**: Meddelanden är individuella JSON-RPC-förfrågningar, notifieringar eller svar, avgränsade med radbrytningar.
- **Loggning**: Servern KAN skriva UTF-8-strängar till standardfel (`stderr`) för loggningsändamål.

### Viktiga krav:
- Meddelanden MÅSTE avgränsas med radbrytningar och FÅR INTE innehålla inbäddade radbrytningar.
- Servern FÅR INTE skriva något till `stdout` som inte är ett giltigt MCP-meddelande.
- Klienten FÅR INTE skriva något till serverns `stdin` som inte är ett giltigt MCP-meddelande.

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

- Importerar vi klassen `Server` och `StdioServerTransport` från MCP SDK.
- Skapar vi en serverinstans med grundläggande konfiguration och funktioner.

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

I koden ovan:

- Skapar vi en serverinstans med hjälp av MCP SDK.
- Definierar vi verktyg med hjälp av dekoratorer.
- Använder vi stdio_server-kontrollhanteraren för att hantera transporten.

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

Den största skillnaden från SSE är att stdio-servrar:

- Kräver inte webbserverinställningar eller HTTP-slutpunkter.
- Startas som underprocesser av klienten.
- Kommunicerar via stdin/stdout-strömmar.
- Är enklare att implementera och felsöka.

## Övning: Skapa en stdio-server

För att skapa vår server behöver vi tänka på två saker:

- Vi behöver använda en webbserver för att exponera slutpunkter för anslutning och meddelanden.

## Laboration: Skapa en enkel MCP-stdio-server

I den här laborationen ska vi skapa en enkel MCP-server med den rekommenderade stdio-transporten. Den här servern kommer att exponera verktyg som klienter kan anropa med hjälp av standardprotokollet Model Context Protocol.

### Förutsättningar

- Python 3.8 eller senare
- MCP Python SDK: `pip install mcp`
- Grundläggande förståelse för asynkron programmering

Låt oss börja med att skapa vår första MCP-stdio-server:

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

## Viktiga skillnader från den avvecklade SSE-metoden

**Stdio-transport (nuvarande standard):**
- Enkel underprocessmodell – klienten startar servern som en barnprocess.
- Kommunikation via stdin/stdout med JSON-RPC-meddelanden.
- Ingen HTTP-serverinställning krävs.
- Bättre prestanda och säkerhet.
- Enklare felsökning och utveckling.

**SSE-transport (avvecklad från och med MCP 2025-06-18):**
- Krävde en HTTP-server med SSE-slutpunkter.
- Mer komplex inställning med webbserverinfrastruktur.
- Ytterligare säkerhetsöverväganden för HTTP-slutpunkter.
- Har nu ersatts av Streamable HTTP för webbaserade scenarier.

### Skapa en server med stdio-transport

För att skapa vår stdio-server behöver vi:

1. **Importera nödvändiga bibliotek** – Vi behöver MCP-serverkomponenterna och stdio-transporten.
2. **Skapa en serverinstans** – Definiera servern med dess funktioner.
3. **Definiera verktyg** – Lägg till den funktionalitet vi vill exponera.
4. **Ställ in transporten** – Konfigurera stdio-kommunikationen.
5. **Kör servern** – Starta servern och hantera meddelanden.

Låt oss bygga detta steg för steg:

### Steg 1: Skapa en grundläggande stdio-server

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

Servern startar och väntar på inmatning från stdin. Den kommunicerar med JSON-RPC-meddelanden via stdio-transporten.

### Steg 4: Testa med Inspector

Du kan testa din server med MCP Inspector:

1. Installera Inspector: `npx @modelcontextprotocol/inspector`
2. Kör Inspector och peka den mot din server.
3. Testa de verktyg du har skapat.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Felsöka din stdio-server

### Använda MCP Inspector

MCP Inspector är ett värdefullt verktyg för att felsöka och testa MCP-servrar. Så här använder du det med din stdio-server:

1. **Installera Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Kör Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa din server**: Inspector tillhandahåller ett webbgränssnitt där du kan:
   - Visa serverfunktioner.
   - Testa verktyg med olika parametrar.
   - Övervaka JSON-RPC-meddelanden.
   - Felsöka anslutningsproblem.

### Använda VS Code

Du kan också felsöka din MCP-server direkt i VS Code:

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

2. Sätt brytpunkter i din serverkod.
3. Kör felsökaren och testa med Inspector.

### Vanliga felsökningstips

- Använd `stderr` för loggning – skriv aldrig till `stdout` eftersom det är reserverat för MCP-meddelanden.
- Se till att alla JSON-RPC-meddelanden är radbrytningsavgränsade.
- Testa med enkla verktyg först innan du lägger till komplex funktionalitet.
- Använd Inspector för att verifiera meddelandeformat.

## Använda din stdio-server i VS Code

När du har byggt din MCP-stdio-server kan du integrera den med VS Code för att använda den med Claude eller andra MCP-kompatibla klienter.

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

3. **Testa anslutningen**: Starta en konversation med Claude och prova att använda din servers verktyg:
   - "Kan du hälsa på mig med hälsningsverktyget?"
   - "Beräkna summan av 15 och 27."
   - "Vad är serverinformationen?"

### TypeScript stdio-serverexempel

Här är ett komplett TypeScript-exempel som referens:

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

### .NET stdio-serverexempel

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

## Sammanfattning

I den här uppdaterade lektionen lärde du dig att:

- Bygga MCP-servrar med den nuvarande **stdio-transporten** (rekommenderat tillvägagångssätt).
- Förstå varför SSE-transporten avvecklades till förmån för stdio och Streamable HTTP.
- Skapa verktyg som kan anropas av MCP-klienter.
- Felsöka din server med MCP Inspector.
- Integrera din stdio-server med VS Code och Claude.

Stdio-transporten erbjuder ett enklare, säkrare och mer prestandaeffektivt sätt att bygga MCP-servrar jämfört med den avvecklade SSE-metoden. Det är den rekommenderade transporten för de flesta MCP-serverimplementationer enligt specifikationen från 2025-06-18.

## Övning: Testa din stdio-server

Nu när du har byggt din stdio-server, låt oss testa den för att säkerställa att den fungerar korrekt.

### Förutsättningar

1. Se till att du har MCP Inspector installerad:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Din serverkod ska vara sparad (t.ex. som `server.py`).

### Testa med Inspector

1. **Starta Inspector med din server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Öppna webbgränssnittet**: Inspector öppnar ett webbläsarfönster som visar din servers funktioner.

3. **Testa verktygen**: 
   - Prova verktyget `get_greeting` med olika namn.
   - Testa verktyget `calculate_sum` med olika siffror.
   - Anropa verktyget `get_server_info` för att se servermetadata.

4. **Övervaka kommunikationen**: Inspector visar JSON-RPC-meddelanden som utbyts mellan klient och server.

### Vad du bör se

När din server startar korrekt bör du se:
- Serverfunktioner listade i Inspector.
- Verktyg tillgängliga för testning.
- Framgångsrika JSON-RPC-meddelandeutbyten.
- Verktygssvar som visas i gränssnittet.

### Vanliga problem och lösningar

**Servern startar inte:**
- Kontrollera att alla beroenden är installerade: `pip install mcp`.
- Verifiera Python-syntax och indrag.
- Leta efter felmeddelanden i konsolen.

**Verktyg visas inte:**
- Se till att `@server.tool()`-dekoratorer är närvarande.
- Kontrollera att verktygsfunktioner är definierade före `main()`.
- Verifiera att servern är korrekt konfigurerad.

**Anslutningsproblem:**
- Se till att servern använder stdio-transport korrekt.
- Kontrollera att inga andra processer stör.
- Verifiera Inspector-kommandosyntaxen.

## Uppgift

Försök att bygga ut din server med fler funktioner. Se [den här sidan](https://api.chucknorris.io/) för att till exempel lägga till ett verktyg som anropar ett API. Du bestämmer hur servern ska se ut. Ha kul :)

## Lösning

[Lösning](./solution/README.md) Här är en möjlig lösning med fungerande kod.

## Viktiga insikter

De viktigaste insikterna från det här kapitlet är följande:

- Stdio-transporten är den rekommenderade mekanismen för lokala MCP-servrar.
- Stdio-transport möjliggör sömlös kommunikation mellan MCP-servrar och klienter via standard in- och utmatningsströmmar.
- Du kan använda både Inspector och Visual Studio Code för att direkt använda stdio-servrar, vilket gör felsökning och integration enkel.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Ytterligare resurser

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Vad kommer härnäst

## Nästa steg

Nu när du har lärt dig att bygga MCP-servrar med stdio-transport kan du utforska mer avancerade ämnen:

- **Nästa**: [HTTP Streaming med MCP (Streamable HTTP)](../06-http-streaming/README.md) – Lär dig om den andra stödda transportmekanismen för fjärrservrar.
- **Avancerat**: [MCP-säkerhetsbästa praxis](../../02-Security/README.md) – Implementera säkerhet i dina MCP-servrar.
- **Produktion**: [Distributionsstrategier](../09-deployment/README.md) – Distribuera dina servrar för produktionsanvändning.

## Ytterligare resurser

- [MCP-specifikation 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Officiell specifikation.
- [MCP SDK-dokumentation](https://github.com/modelcontextprotocol/sdk) – SDK-referenser för alla språk.
- [Community-exempel](../../06-CommunityContributions/README.md) – Fler serverexempel från communityn.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.