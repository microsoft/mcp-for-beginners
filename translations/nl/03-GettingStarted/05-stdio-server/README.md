# MCP Server met stdio Transport

> **⚠️ Belangrijke update**: Vanaf de MCP Specificatie 2025-06-18 is de standalone SSE (Server-Sent Events) transport **afgeschreven** en vervangen door "Streamable HTTP" transport. De huidige MCP-specificatie definieert twee primaire transportmechanismen:
> 1. **stdio** - Standaard input/output (aanbevolen voor lokale servers)
> 2. **Streamable HTTP** - Voor externe servers die intern SSE kunnen gebruiken
>
> Deze les is aangepast om te focussen op de **stdio transport**, wat de aanbevolen aanpak is voor de meeste MCP servers.

De stdio transport stelt MCP-servers in staat om te communiceren met clients via standaard input- en outputstromen. Dit is de meest gebruikte en aanbevolen transportmechanisme in de huidige MCP-specificatie, wat een eenvoudige en efficiënte manier biedt om MCP servers te bouwen die makkelijk te integreren zijn met diverse clienttoepassingen.

## Overzicht

Deze les behandelt hoe MCP Servers te bouwen en te gebruiken met de stdio transport.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP Server bouwen met de stdio transport.
- Een MCP Server debuggen met gebruik van de Inspector.
- Een MCP Server gebruiken met Visual Studio Code.
- De huidige MCP transportmechanismen begrijpen en waarom stdio wordt aanbevolen.

## stdio Transport - Hoe werkt het?

De stdio transport is een van de twee ondersteunde transporttypen in de huidige MCP-specificatie (2025-06-18). Zo werkt het:

- **Eenvoudige communicatie**: De server leest JSON-RPC berichten van standaard input (`stdin`) en stuurt berichten naar standaard output (`stdout`).
- **Proces-gebaseerd**: De client start de MCP server als een subprocess.
- **Berichtformaat**: Berichten zijn individuele JSON-RPC requests, notificaties, of responses, gescheiden door nieuwe regels.
- **Loggen**: De server MAG UTF-8 strings schrijven naar standaard error (`stderr`) voor logging.

### Belangrijke eisen:
- Berichten MOETEN gescheiden zijn door nieuwe regels en mogen GEEN embedded nieuwe regels bevatten
- De server MAG NIETS schrijven naar `stdout` dat geen geldig MCP-bericht is
- De client MAG NIETS schrijven naar `stdin` van de server dat geen geldig MCP-bericht is

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

In de bovenstaande code:

- Importeren we de `Server` klasse en `StdioServerTransport` uit de MCP SDK
- Maken we een server instantie met een basisconfiguratie en mogelijkheden
- Maken we een `StdioServerTransport` instantie en verbinden we de server hiermee, waarmee communicatie via stdin/stdout mogelijk wordt

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Maak server instantie aan
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

In de bovenstaande code:

- Maken we een server instantie met de MCP SDK
- Definiëren we tools met decorators
- Gebruiken we de stdio_server context manager om het transport te beheren

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

Het belangrijkste verschil met SSE is dat stdio servers:

- Geen webserver of HTTP endpoints nodig hebben
- Als subprocesses worden gestart door de client
- Communiceren via stdin/stdout stromen
- Eenvoudiger te implementeren en te debuggen zijn

## Oefening: Een stdio Server maken

Om onze server te maken moeten we rekening houden met twee zaken:

- We moeten een webserver gebruiken om endpoints beschikbaar te stellen voor verbinding en berichten.

## Lab: Een eenvoudige MCP stdio server maken

In dit lab maken we een eenvoudige MCP server met de aanbevolen stdio transport. Deze server zal tools blootstellen die clients kunnen aanroepen via het standaard Model Context Protocol.

### Vereisten

- Python 3.8 of later
- MCP Python SDK: `pip install mcp`
- Basiskennis van async programmeren

Laten we beginnen met het maken van onze eerste MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Logboekregistratie configureren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Maak de server aan
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
    # Gebruik stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Belangrijkste verschillen met de afgeschreven SSE-aanpak

**Stdio Transport (Huidige standaard):**
- Eenvoudig subprocess model - client start server als child process
- Communicatie via stdin/stdout met JSON-RPC berichten
- Geen HTTP server setup vereist
- Betere prestaties en beveiliging
- Makkelijker te debuggen en ontwikkelen

**SSE Transport (Afgeschreven sinds MCP 2025-06-18):**
- Vereiste HTTP server met SSE endpoints
- Complexere setup met webserver infrastructuur
- Extra beveiligingsmaatregelen voor HTTP endpoints
- Nu vervangen door Streamable HTTP voor webscenario’s

### Een server maken met stdio transport

Om onze stdio server te maken moeten we:

1. **De benodigde bibliotheken importeren** - We hebben de MCP server componenten en stdio transport nodig
2. **Een server instantie maken** - Definieer de server met zijn mogelijkheden
3. **Tools definiëren** - Voeg de functionaliteit toe die we willen blootstellen
4. **De transport instellen** - Configureer de stdio communicatie
5. **De server draaien** - Start de server en verwerk berichten

Laten we dit stap voor stap bouwen:

### Stap 1: Maak een eenvoudige stdio server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configureer logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Maak de server aan
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

### Stap 2: Voeg meer tools toe

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

### Stap 3: De server draaien

Sla de code op als `server.py` en start het vanaf de opdrachtregel:

```bash
python server.py
```

De server zal starten en wachten op input van stdin. Hij communiceert via JSON-RPC berichten over de stdio transport.

### Stap 4: Testen met de Inspector

Je kunt je server testen met de MCP Inspector:

1. Installeer de Inspector: `npx @modelcontextprotocol/inspector`
2. Start de Inspector en wijs hem naar je server
3. Test de tools die je hebt gemaakt

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Je stdio server debuggen

### MCP Inspector gebruiken

De MCP Inspector is een waardevol hulpmiddel voor het debuggen en testen van MCP servers. Zo gebruik je hem met je stdio server:

1. **Installeer de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Start de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test je server**: De Inspector biedt een webinterface waar je kunt:
   - Server mogelijkheden bekijken
   - Tools testen met verschillende parameters
   - JSON-RPC berichten monitoren
   - Verbindingsproblemen debuggen

### Gebruik van VS Code

Je kunt je MCP server ook direct debuggen in VS Code:

1. Maak een launch-configuratie aan in `.vscode/launch.json`:
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

2. Zet breakpoints in je servercode
3. Start de debugger en test met de Inspector

### Veelvoorkomende debugtips

- Gebruik `stderr` voor logging - schrijf nooit naar `stdout` want dat is gereserveerd voor MCP berichten
- Zorg dat alle JSON-RPC berichten door nieuwe regels gescheiden zijn
- Test eerst met eenvoudige tools voordat je complexe functionaliteit toevoegt
- Gebruik de Inspector om berichtformaten te controleren

## Je stdio server gebruiken in VS Code

Zodra je je MCP stdio server hebt gebouwd, kun je hem integreren met VS Code om hem te gebruiken met Claude of andere MCP-compatibele clients.

### Configuratie

1. **Maak een MCP configuratiebestand** aan op `%APPDATA%\Claude\claude_desktop_config.json` (Windows) of `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Herstart Claude**: Sluit en open Claude opnieuw om de nieuwe serverconfiguratie te laden.

3. **Test de verbinding**: Begin een gesprek met Claude en probeer de tools van je server:
   - "Kun je me begroeten met de greeting tool?"
   - "Bereken de som van 15 en 27"
   - "Wat is de serverinfo?"

### Voorbeeld van een TypeScript stdio server

Hier is een compleet TypeScript voorbeeld ter referentie:

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

// Voeg hulpmiddelen toe
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

### Voorbeeld van een .NET stdio server

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

## Samenvatting

In deze geüpdatete les heb je geleerd:

- MCP servers te bouwen met de huidige **stdio transport** (aanbevolen aanpak)
- Te begrijpen waarom SSE transport werd afgeschreven ten gunste van stdio en Streamable HTTP
- Tools te maken die MCP clients kunnen aanroepen
- Je server te debuggen met de MCP Inspector
- Je stdio server te integreren met VS Code en Claude

De stdio transport biedt een eenvoudigere, veiligere en hogere performance methode om MCP servers te bouwen in vergelijking met de afgeschreven SSE-aanpak. Het is de aanbevolen transport voor de meeste MCP server implementaties sinds de specificatie van 2025-06-18.

### .NET

1. Laten we eerst enkele tools maken, hiervoor maken we een bestand *Tools.cs* met de volgende inhoud:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Oefening: Je stdio server testen

Nu je je stdio server hebt gebouwd, gaan we hem testen om zeker te zijn dat hij correct werkt.

### Vereisten

1. Zorg dat je de MCP Inspector hebt geïnstalleerd:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Je servercode moet opgeslagen zijn (bijvoorbeeld als `server.py`)

### Testen met de Inspector

1. **Start de Inspector met je server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open de webinterface**: De Inspector opent een browser venster waarin je de server mogelijkheden ziet.

3. **Test de tools**:
   - Probeer de `get_greeting` tool met verschillende namen
   - Test de `calculate_sum` tool met verschillende getallen
   - Roep de `get_server_info` tool aan om server metadata te zien

4. **Monitor de communicatie**: De Inspector toont de JSON-RPC berichten die tussen client en server worden uitgewisseld.

### Wat je zou moeten zien

Als je server goed start, zie je:
- Server mogelijkheden in de Inspector
- Beschikbare tools om te testen
- Succesvolle JSON-RPC berichtuitwisseling
- Tool responses getoond in de interface

### Veelvoorkomende problemen en oplossingen

**Server start niet:**
- Controleer of alle dependencies geïnstalleerd zijn: `pip install mcp`
- Controleer Python syntax en inspringen
- Bekijk foutmeldingen in de console

**Tools verschijnen niet:**
- Zorg dat `@server.tool()` decorators aanwezig zijn
- Controleer of tool functies gedefinieerd zijn vóór `main()`
- Kijk of de server correct is geconfigureerd

**Verbindingsproblemen:**
- Controleer of de server stdio transport correct gebruikt
- Kijk of andere processen niet storen
- Controleer de syntax van het Inspector-commando

## Opdracht

Probeer je server verder uit te breiden met meer mogelijkheden. Zie [deze pagina](https://api.chucknorris.io/) om bijvoorbeeld een tool toe te voegen die een API aanroept. Jij bepaalt hoe de server eruit moet zien. Veel plezier :)

## Oplossing

[Oplossing](./solution/README.md) Hier is een mogelijke oplossing met werkende code.

## Belangrijkste punten

De belangrijkste punten uit dit hoofdstuk zijn:

- De stdio transport is de aanbevolen mechanisme voor lokale MCP servers.
- Stdio transport maakt naadloze communicatie mogelijk tussen MCP servers en clients via standaard input en outputstromen.
- Je kunt zowel Inspector als Visual Studio Code gebruiken om stdio servers direct te consumeren, wat debugging en integratie eenvoudig maakt.

## Voorbeelden 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Extra bronnen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wat nu

## Volgende stappen

Nu je hebt geleerd hoe je MCP servers bouwt met de stdio transport, kun je meer geavanceerde onderwerpen verkennen:

- **Volgende**: [HTTP Streaming met MCP (Streamable HTTP)](../06-http-streaming/README.md) - Leer over het andere ondersteunde transportmechanisme voor externe servers
- **Geavanceerd**: [MCP Security Best Practices](../../02-Security/README.md) - Implementeer beveiliging in je MCP servers
- **Productie**: [Deployment Strategies](../09-deployment/README.md) - Zet je servers in voor productief gebruik

## Extra bronnen

- [MCP Specificatie 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiële specificatie
- [MCP SDK Documentatie](https://github.com/modelcontextprotocol/sdk) - SDK referenties voor alle talen
- [Community Voorbeelden](../../06-CommunityContributions/README.md) - Meer server voorbeelden uit de community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->