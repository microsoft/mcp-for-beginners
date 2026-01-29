# MCP Server met stdio Transport

> **⚠️ Belangrijke Update**: Vanaf MCP Specificatie 2025-06-18 is de standalone SSE (Server-Sent Events) transport **verouderd** en vervangen door "Streamable HTTP" transport. De huidige MCP specificatie definieert twee primaire transportmechanismen:
> 1. **stdio** - Standaard input/output (aanbevolen voor lokale servers)
> 2. **Streamable HTTP** - Voor externe servers die intern SSE kunnen gebruiken
>
> Deze les is bijgewerkt om te focussen op de **stdio transport**, wat de aanbevolen aanpak is voor de meeste MCP serverimplementaties.

De stdio transport stelt MCP servers in staat om te communiceren met clients via standaard input- en outputstreams. Dit is het meest gebruikte en aanbevolen transportmechanisme in de huidige MCP specificatie, en biedt een eenvoudige en efficiënte manier om MCP servers te bouwen die gemakkelijk geïntegreerd kunnen worden met verschillende clientapplicaties.

## Overzicht

Deze les behandelt hoe je MCP Servers kunt bouwen en gebruiken met de stdio transport.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP Server bouwen met de stdio transport.
- Een MCP Server debuggen met de Inspector.
- Een MCP Server gebruiken met Visual Studio Code.
- De huidige MCP transportmechanismen begrijpen en waarom stdio wordt aanbevolen.

## stdio Transport - Hoe het Werkt

De stdio transport is een van de twee ondersteunde transporttypes in de huidige MCP specificatie (2025-06-18). Zo werkt het:

- **Eenvoudige Communicatie**: De server leest JSON-RPC berichten van standaard input (`stdin`) en stuurt berichten naar standaard output (`stdout`).
- **Proces-gebaseerd**: De client start de MCP server als een subprocess.
- **Berichtformaat**: Berichten zijn individuele JSON-RPC verzoeken, notificaties of antwoorden, gescheiden door nieuwe regels.
- **Logging**: De server MAG UTF-8 strings naar standaard error (`stderr`) schrijven voor logdoeleinden.

### Belangrijke Vereisten:
- Berichten MOETEN gescheiden zijn door nieuwe regels en MOGEN GEEN ingesloten nieuwe regels bevatten.
- De server MAG NIETS naar `stdout` schrijven dat geen geldig MCP bericht is.
- De client MAG NIETS naar de `stdin` van de server schrijven dat geen geldig MCP bericht is.

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

In de bovenstaande code:

- We importeren de `Server` klasse en `StdioServerTransport` uit de MCP SDK.
- We maken een serverinstantie met basisconfiguratie en mogelijkheden.

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

In de bovenstaande code:

- We maken een serverinstantie met behulp van de MCP SDK.
- We definiëren tools met decorators.
- We gebruiken de stdio_server contextmanager om het transport te beheren.

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

Het belangrijkste verschil met SSE is dat stdio servers:

- Geen webserver setup of HTTP endpoints vereisen.
- Als subprocessen door de client worden gestart.
- Communiceren via stdin/stdout streams.
- Eenvoudiger te implementeren en debuggen zijn.

## Oefening: Een stdio Server Maken

Om onze server te maken, moeten we twee dingen in gedachten houden:

- We moeten een webserver gebruiken om endpoints voor verbinding en berichten bloot te stellen.

## Lab: Een eenvoudige MCP stdio server maken

In dit lab maken we een eenvoudige MCP server met de aanbevolen stdio transport. Deze server zal tools blootstellen die clients kunnen aanroepen met behulp van het standaard Model Context Protocol.

### Vereisten

- Python 3.8 of later
- MCP Python SDK: `pip install mcp`
- Basiskennis van asynchrone programmering

Laten we beginnen met het maken van onze eerste MCP stdio server:

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

## Belangrijke verschillen met de verouderde SSE aanpak

**Stdio Transport (Huidige Standaard):**
- Eenvoudig subprocessmodel - client start server als child process.
- Communicatie via stdin/stdout met JSON-RPC berichten.
- Geen HTTP server setup vereist.
- Betere prestaties en beveiliging.
- Eenvoudiger debuggen en ontwikkelen.

**SSE Transport (Verouderd vanaf MCP 2025-06-18):**
- Vereiste HTTP server met SSE endpoints.
- Complexere setup met webserver infrastructuur.
- Extra beveiligingsoverwegingen voor HTTP endpoints.
- Nu vervangen door Streamable HTTP voor web-gebaseerde scenario's.

### Een server maken met stdio transport

Om onze stdio server te maken, moeten we:

1. **De benodigde bibliotheken importeren** - We hebben de MCP servercomponenten en stdio transport nodig.
2. **Een serverinstantie maken** - Definieer de server met zijn mogelijkheden.
3. **Tools definiëren** - Voeg de functionaliteit toe die we willen blootstellen.
4. **Het transport instellen** - Configureer stdio communicatie.
5. **De server uitvoeren** - Start de server en verwerk berichten.

Laten we dit stap voor stap bouwen:

### Stap 1: Een basis stdio server maken

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

### Stap 2: Meer tools toevoegen

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

### Stap 3: De server uitvoeren

Sla de code op als `server.py` en voer het uit vanaf de commandoregel:

```bash
python server.py
```

De server zal starten en wachten op input van stdin. Het communiceert via JSON-RPC berichten over de stdio transport.

### Stap 4: Testen met de Inspector

Je kunt je server testen met de MCP Inspector:

1. Installeer de Inspector: `npx @modelcontextprotocol/inspector`
2. Start de Inspector en wijs deze naar je server.
3. Test de tools die je hebt gemaakt.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debuggen van je stdio server

### Gebruik van de MCP Inspector

De MCP Inspector is een waardevol hulpmiddel voor het debuggen en testen van MCP servers. Zo gebruik je het met je stdio server:

1. **Installeer de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Start de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test je server**: De Inspector biedt een webinterface waar je:
   - Servermogelijkheden kunt bekijken.
   - Tools kunt testen met verschillende parameters.
   - JSON-RPC berichten kunt monitoren.
   - Verbindingsproblemen kunt debuggen.

### Gebruik van VS Code

Je kunt je MCP server ook direct debuggen in VS Code:

1. Maak een launch configuratie in `.vscode/launch.json`:
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

2. Stel breakpoints in je servercode.
3. Voer de debugger uit en test met de Inspector.

### Veelvoorkomende debugging tips

- Gebruik `stderr` voor logging - schrijf nooit naar `stdout`, omdat dit gereserveerd is voor MCP berichten.
- Zorg ervoor dat alle JSON-RPC berichten gescheiden zijn door nieuwe regels.
- Test eerst met eenvoudige tools voordat je complexe functionaliteit toevoegt.
- Gebruik de Inspector om berichtformaten te verifiëren.

## Je stdio server gebruiken in VS Code

Zodra je je MCP stdio server hebt gebouwd, kun je deze integreren met VS Code om deze te gebruiken met Claude of andere MCP-compatibele clients.

### Configuratie

1. **Maak een MCP configuratiebestand** op `%APPDATA%\Claude\claude_desktop_config.json` (Windows) of `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

3. **Test de verbinding**: Start een gesprek met Claude en probeer de tools van je server:
   - "Kun je me begroeten met de begroetingstool?"
   - "Bereken de som van 15 en 27."
   - "Wat zijn de servergegevens?"

### TypeScript stdio server voorbeeld

Hier is een volledig TypeScript voorbeeld ter referentie:

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

### .NET stdio server voorbeeld

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

## Samenvatting

In deze bijgewerkte les heb je geleerd hoe je:

- MCP servers bouwt met de huidige **stdio transport** (aanbevolen aanpak).
- Begrijpt waarom SSE transport is verouderd ten gunste van stdio en Streamable HTTP.
- Tools maakt die door MCP clients kunnen worden aangeroepen.
- Je server debugt met de MCP Inspector.
- Je stdio server integreert met VS Code en Claude.

De stdio transport biedt een eenvoudigere, veiligere en snellere manier om MCP servers te bouwen in vergelijking met de verouderde SSE aanpak. Het is het aanbevolen transport voor de meeste MCP serverimplementaties vanaf de 2025-06-18 specificatie.

### .NET

1. Laten we eerst enkele tools maken. Hiervoor maken we een bestand *Tools.cs* met de volgende inhoud:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Oefening: Testen van je stdio server

Nu je je stdio server hebt gebouwd, laten we deze testen om ervoor te zorgen dat hij correct werkt.

### Vereisten

1. Zorg ervoor dat je de MCP Inspector hebt geïnstalleerd:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Je servercode moet opgeslagen zijn (bijvoorbeeld als `server.py`).

### Testen met de Inspector

1. **Start de Inspector met je server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open de webinterface**: De Inspector opent een browservenster waarin je de mogelijkheden van je server kunt zien.

3. **Test de tools**: 
   - Probeer de `get_greeting` tool met verschillende namen.
   - Test de `calculate_sum` tool met diverse getallen.
   - Roep de `get_server_info` tool aan om servermetadata te bekijken.

4. **Monitor de communicatie**: De Inspector toont de JSON-RPC berichten die worden uitgewisseld tussen client en server.

### Wat je zou moeten zien

Wanneer je server correct start, zou je het volgende moeten zien:
- Servermogelijkheden vermeld in de Inspector.
- Tools beschikbaar voor testen.
- Succesvolle JSON-RPC berichtuitwisselingen.
- Toolreacties weergegeven in de interface.

### Veelvoorkomende problemen en oplossingen

**Server start niet:**
- Controleer of alle afhankelijkheden zijn geïnstalleerd: `pip install mcp`.
- Verifieer Python-syntaxis en inspringing.
- Zoek naar foutmeldingen in de console.

**Tools verschijnen niet:**
- Zorg ervoor dat `@server.tool()` decorators aanwezig zijn.
- Controleer of toolfuncties zijn gedefinieerd vóór `main()`.
- Verifieer dat de server correct is geconfigureerd.

**Verbindingsproblemen:**
- Zorg ervoor dat de server stdio transport correct gebruikt.
- Controleer of er geen andere processen interfereren.
- Verifieer de Inspector commandosyntaxis.

## Opdracht

Probeer je server uit te breiden met meer mogelijkheden. Zie [deze pagina](https://api.chucknorris.io/) om bijvoorbeeld een tool toe te voegen die een API aanroept. Jij bepaalt hoe de server eruit moet zien. Veel plezier :)

## Oplossing

[Oplossing](./solution/README.md) Hier is een mogelijke oplossing met werkende code.

## Belangrijke Punten

De belangrijkste punten uit dit hoofdstuk zijn:

- De stdio transport is het aanbevolen mechanisme voor lokale MCP servers.
- Stdio transport maakt naadloze communicatie mogelijk tussen MCP servers en clients via standaard input- en outputstreams.
- Je kunt zowel Inspector als Visual Studio Code gebruiken om stdio servers direct te gebruiken, wat debuggen en integratie eenvoudig maakt.

## Voorbeelden 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Aanvullende Bronnen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wat Nu

## Volgende Stappen

Nu je hebt geleerd hoe je MCP servers bouwt met de stdio transport, kun je meer geavanceerde onderwerpen verkennen:

- **Volgende**: [HTTP Streaming met MCP (Streamable HTTP)](../06-http-streaming/README.md) - Leer over het andere ondersteunde transportmechanisme voor externe servers.
- **Geavanceerd**: [MCP Security Best Practices](../../02-Security/README.md) - Implementeer beveiliging in je MCP servers.
- **Productie**: [Deployment Strategies](../09-deployment/README.md) - Zet je servers in voor productiegebruik.

## Aanvullende Bronnen

- [MCP Specificatie 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiële specificatie.
- [MCP SDK Documentatie](https://github.com/modelcontextprotocol/sdk) - SDK-referenties voor alle talen.
- [Community Voorbeelden](../../06-CommunityContributions/README.md) - Meer servervoorbeelden van de community.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.