# MCP-server met stdio Transport

> **⚠️ Belangrijke update**: Vanaf MCP-specificatie 2025-06-18 is de standalone SSE (Server-Sent Events) transport **verouderd** en vervangen door "Streamable HTTP" transport. De huidige MCP-specificatie definieert twee primaire transportmechanismen:
> 1. **stdio** - Standaard invoer/uitvoer (aanbevolen voor lokale servers)
> 2. **Streamable HTTP** - Voor externe servers die intern mogelijk SSE gebruiken
>
> Deze les is bijgewerkt om zich te richten op de **stdio transport**, wat de aanbevolen aanpak is voor de meeste MCP-serverimplementaties.

De stdio transport maakt het mogelijk voor MCP-servers om te communiceren met clients via standaard invoer- en uitvoerstromen. Dit is het meest gebruikte en aanbevolen transportmechanisme in de huidige MCP-specificatie, en biedt een eenvoudige en efficiënte manier om MCP-servers te bouwen die makkelijk kunnen worden geïntegreerd met diverse clienttoepassingen.

## Overzicht

Deze les behandelt hoe je MCP-servers bouwt en gebruikt met de stdio transport.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP-server bouwen met de stdio transport.
- Een MCP-server debuggen met de Inspector.
- Een MCP-server gebruiken met Visual Studio Code.
- De huidige MCP-transportmechanismen begrijpen en waarom stdio wordt aanbevolen.


## stdio Transport - Hoe het werkt

De stdio transport is een van de twee standaardtransports in MCP-specificatie
`2026-07-28`. Zo werkt het:

- **Eenvoudige communicatie**: De server leest JSON-RPC-berichten van standaardinvoer (`stdin`) en stuurt berichten naar standaarduitvoer (`stdout`).
- **Procesgebaseerd**: De client start de MCP-server als een subprocess.
- **Berichtformaat**: Berichten zijn afzonderlijke JSON-RPC-verzoeken, notificaties of antwoorden, gescheiden door nieuwe regels.
- **Logging**: De server MAG UTF-8-teksten naar standaardfout (`stderr`) schrijven voor logdoeleinden.

### Belangrijke vereisten:
- Berichten MOETEN gescheiden zijn door nieuwe regels en MOETEN GEEN ingesloten nieuwe regels bevatten
- De server MAG NIETS schrijven naar `stdout` dat geen geldig MCP-bericht is
- De client MAG NIETS schrijven naar de server's `stdin` dat geen geldig MCP-bericht is

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

In bovenstaande code:

- Importeren we de `Server` klasse en `StdioServerTransport` van de MCP SDK
- Maken we een serverinstantie met basisconfiguratie en mogelijkheden
- Maken we een `StdioServerTransport` instantie en verbinden we de server ermee, waardoor communicatie via stdin/stdout mogelijk wordt

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

In bovenstaande code:

- Maken we een serverinstantie met de MCP SDK
- Definiëren we tools met behulp van decorators
- Gebruiken we de stdio_server contextmanager om de transport te beheren

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

Het belangrijkste verschil met SSE is dat stdio-servers:

- Geen webserverconfiguratie of HTTP-eindpunten vereisen
- Door de client als subprocesses worden gestart
- Communiceren via stdin/stdout-stromen
- Makkelijker te implementeren en debuggen zijn

## Oefening: Een stdio-server maken

Om onze server te maken, moeten we aan twee dingen denken:

- We moeten een webserver gebruiken om eindpunten voor connectie en berichten bloot te stellen.
## Lab: Een eenvoudige MCP stdio-server maken

In deze lab maken we een eenvoudige MCP-server die gebruikmaakt van de aanbevolen stdio transport. Deze server zal tools blootstellen die clients kunnen aanroepen via het standaard Model Context Protocol.

### Vereisten

- Python 3.8 of nieuwer
- MCP Python SDK: `pip install mcp`
- Basiskennis van asynchrone programmering

Laten we beginnen met het maken van onze eerste MCP stdio-server:

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

## Belangrijkste verschillen met de verouderde SSE-benadering

**Stdio Transport (Huidige standaard):**
- Eenvoudig subprocess-model - client start server als child process
- Communicatie via stdin/stdout met JSON-RPC-berichten
- Geen HTTP-server configuratie nodig
- Betere prestaties en beveiliging
- Makkelijker te debuggen en ontwikkelen

**SSE Transport (Verouderd sinds MCP 2025-06-18):**
- Vereiste HTTP-server met SSE-eindpunten
- Complexere setup met webserverinfrastructuur
- Extra beveiligingsoverwegingen voor HTTP-eindpunten
- Nu vervangen door Streamable HTTP voor webgebaseerde scenario's

### Een server maken met stdio transport

Om onze stdio-server te maken, moeten we:

1. **De benodigde bibliotheken importeren** - We hebben de MCP-servercomponenten en stdio transport nodig
2. **Een serverinstantie maken** - Definieer de server met zijn mogelijkheden
3. **Tools definiëren** - Voeg de functionaliteit toe die we willen blootstellen
4. **De transport instellen** - Configureer stdio-communicatie
5. **De server starten** - Start de server en verwerk berichten

Laten we dit stap voor stap opbouwen:

### Stap 1: Een basis stdio-server maken

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

### Stap 3: De server draaien

Sla de code op als `server.py` en start deze vanuit de opdrachtregel:

```bash
python server.py
```

De server start en wacht op invoer via stdin. Communicatie verloopt via JSON-RPC-berichten over de stdio transport.

### Stap 4: Testen met de Inspector

Je kunt je server testen met de MCP Inspector:

1. Installeer de Inspector: `npx @modelcontextprotocol/inspector`
2. Start de Inspector en wijs deze naar je server
3. Test de tools die je hebt gemaakt

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Je stdio-server debuggen

### Met de MCP Inspector

De MCP Inspector is een waardevol hulpmiddel voor het debuggen en testen van MCP-servers. Zo gebruik je het met je stdio-server:

1. **Installeer de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Start de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test je server**: De Inspector biedt een webinterface waarin je kunt:
   - Servermogelijkheden bekijken
   - Tools testen met verschillende parameters
   - JSON-RPC-berichten monitoren
   - Connectieproblemen debuggen

### Met VS Code

Je kunt je MCP-server ook rechtstreeks debuggen in VS Code:

1. Maak een launch-configuratie in `.vscode/launch.json`:
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

- Gebruik `stderr` voor logging - schrijf nooit naar `stdout` want die is gereserveerd voor MCP-berichten
- Zorg ervoor dat alle JSON-RPC-berichten gescheiden zijn door nieuwe regels
- Test eerst met eenvoudige tools voordat je complexe functionaliteit toevoegt
- Gebruik de Inspector om berichtformaten te verifiëren

## Je stdio-server gebruiken in VS Code

Zodra je je MCP stdio-server hebt gebouwd, kun je deze integreren met VS Code om hem te gebruiken met Claude of andere MCP-compatibele clients.

### Configuratie

1. **Maak een MCP-configuratiebestand** aan op `%APPDATA%\Claude\claude_desktop_config.json` (Windows) of `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Herstart Claude**: Sluit Claude en start het opnieuw om de nieuwe serverconfiguratie te laden.

3. **Test de verbinding**: Begin een gesprek met Claude en probeer de tools van je server:
   - "Kun je me begroeten met de begroetingstool?"
   - "Bereken de som van 15 en 27"
   - "Wat is de serverinfo?"

### TypeScript stdio-server voorbeeld

Hier is een volledig TypeScript-voorbeeld ter referentie:

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

### .NET stdio-server voorbeeld

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

In deze bijgewerkte les heb je geleerd hoe je:

- MCP-servers bouwt met de huidige **stdio transport** (aanbevolen aanpak)
- Begrijpt waarom SSE transport verouderd is ten gunste van stdio en Streamable HTTP
- Tools maakt die door MCP-clients kunnen worden aangeroepen
- Je server debugt met behulp van de MCP Inspector
- Je stdio-server integreert met VS Code en Claude

De stdio transport biedt een eenvoudigere, veiligere en beter presterende manier om MCP-servers te bouwen in vergelijking met de verouderde SSE-benadering. Het is de aanbevolen transportmethode voor de meeste MCP-serverimplementaties vanaf de 2025-06-18-specificatie.


### .NET

1. Laten we eerst een paar tools maken, hiervoor maken we een bestand *Tools.cs* met de volgende inhoud:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Oefening: Je stdio-server testen

Nu je je stdio-server hebt gebouwd, gaan we deze testen om zeker te zijn dat hij correct werkt.

### Vereisten

1. Zorg dat je de MCP Inspector geïnstalleerd hebt:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Je servercode moet opgeslagen zijn (bijv. als `server.py`)

### Testen met de Inspector

1. **Start de Inspector met je server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Open de webinterface**: De Inspector opent een browservenster met de servermogelijkheden.

3. **Test de tools**:
   - Probeer de `get_greeting` tool met verschillende namen
   - Test de `calculate_sum` tool met verschillende getallen
   - Roep de `get_server_info` tool aan om servermetadata te bekijken

4. **Monitor de communicatie**: De Inspector toont de JSON-RPC-berichten die worden uitgewisseld tussen client en server.

### Wat je moet zien

Wanneer je server correct start, zou je moeten zien:
- Servermogelijkheden vermeld in de Inspector
- Tools beschikbaar voor testen
- Succesvolle uitwisseling van JSON-RPC-berichten
- Reponsen van tools weergegeven in de interface

### Veelvoorkomende problemen en oplossingen

**Server start niet:**
- Controleer of alle afhankelijkheden geïnstalleerd zijn: `pip install mcp`
- Controleer Python-syntaxis en inspringing
- Zoek naar foutmeldingen in de console

**Tools verschijnen niet:**
- Zorg dat `@server.tool()` decorators aanwezig zijn
- Controleer of toolfuncties zijn gedefinieerd vóór `main()`
- Verify de server is goed geconfigureerd

**Verbindingsproblemen:**
- Zorg dat de server stdio transport correct gebruikt
- Controleer dat geen andere processen storen
- Controleer de Inspector commandosyntaxis

## Opdracht

Probeer je server uit te breiden met meer mogelijkheden. Zie [deze pagina](https://api.chucknorris.io/) om bijvoorbeeld een tool toe te voegen die een API aanroept. Jij bepaalt hoe de server eruit komt te zien. Veel plezier :)
## Oplossing

[Oplossing](./solution/README.md) Hier is een mogelijke oplossing met werkende code.

## Belangrijkste inzichten

De belangrijkste inzichten uit dit hoofdstuk zijn:

- De stdio transport is het aanbevolen mechanisme voor lokale MCP-servers.
- Stdio transport maakt naadloze communicatie tussen MCP-servers en clients mogelijk via standaard invoer- en uitvoerstromen.
- Je kunt zowel Inspector als Visual Studio Code gebruiken om stdio-servers direct te gebruiken, wat debuggen en integratie vereenvoudigt.

## Voorbeelden

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Aanvullende bronnen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wat nu?

## Volgende stappen

Nu je geleerd hebt hoe MCP-servers te bouwen met de stdio transport, kun je meer geavanceerde onderwerpen verkennen:

- **Volgende**: [HTTP Streaming met MCP (Streamable HTTP)](../06-http-streaming/README.md) - Leer over het andere ondersteunde transportmechanisme voor externe servers
- **Geavanceerd**: [MCP Beveiligingsbest Practices](../../02-Security/README.md) - Implementeer beveiliging in je MCP-servers
- **Productie**: [Deploystrategieën](../09-deployment/README.md) - Zet je servers in voor gebruik in productie

## Aanvullende bronnen

- [MCP-specificatie 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Huidige specificatie
- [MCP SDK-documentatie](https://github.com/modelcontextprotocol/sdk) - SDK-referenties voor alle talen
- [Communityvoorbeelden](../../06-CommunityContributions/README.md) - Meer servervoorbeelden uit de community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->