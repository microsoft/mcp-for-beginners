# MCP-server met stdio Transport

> **⚠️ Belangrijke update**: Vanaf MCP-specificatie 2025-06-18 is de standalone SSE (Server-Sent Events) transport **verouderd** en vervangen door "Streamable HTTP" transport. De huidige MCP-specificatie definieert twee primaire transportmechanismen:
> 1. **stdio** - Standaard invoer/uitvoer (aanbevolen voor lokale servers)
> 2. **Streamable HTTP** - Voor externe servers die intern SSE kunnen gebruiken
>
> Deze les is bijgewerkt om zich te richten op de **stdio transport**, wat de aanbevolen aanpak is voor de meeste MCP server implementaties.

De stdio transport maakt het mogelijk voor MCP-servers om te communiceren met clients via standaard invoer- en uitvoerstromen. Dit is het meest gebruikte en aanbevolen transportmechanisme in de huidige MCP-specificatie, en biedt een eenvoudige en efficiënte manier om MCP-servers te bouwen die gemakkelijk kunnen worden geïntegreerd met verschillende clientapplicaties.

## Overzicht

In deze les leer je hoe je MCP-servers bouwt en gebruikt met de stdio transport.

## Leerdoelen

Aan het einde van deze les kun je:

- Een MCP-server bouwen met de stdio transport.
- Een MCP-server debuggen met behulp van de Inspector.
- Een MCP-server gebruiken in Visual Studio Code.
- Begrijpen wat de huidige MCP transportmechanismen zijn en waarom stdio wordt aanbevolen.

## stdio Transport - Hoe het werkt

De stdio transport is een van de twee ondersteunde transporttypen in de huidige MCP-specificatie (2025-06-18). Zo werkt het:

- **Eenvoudige communicatie**: De server leest JSON-RPC berichten van standaardinvoer (`stdin`) en stuurt berichten naar standaarduitvoer (`stdout`).
- **Proces-gebaseerd**: De client start de MCP-server als een subprocess.
- **Berichtformaat**: Berichten zijn individuele JSON-RPC verzoeken, notificaties of responses, gescheiden door nieuwe regels.
- **Logging**: De server MAG UTF-8 strings naar standaardfout (`stderr`) schrijven voor loggingdoeleinden.

### Belangrijke vereisten:
- Berichten MOGEN alleen worden gescheiden door nieuwe regels en MOGEN geen ingesloten nieuwe regels bevatten
- De server MAG NIETS naar `stdout` schrijven dat geen geldig MCP-bericht is
- De client MAG NIETS naar de `stdin` van de server schrijven dat geen geldig MCP-bericht is

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

- Importeren we de `Server` klasse en `StdioServerTransport` uit de MCP SDK
- Maken we een serverinstantie met basisconfiguratie en mogelijkheden

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Maak server-voorbeeld aan
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

- Maken we een serverinstantie met de MCP SDK
- Definiëren we tools met decorators
- Gebruiken we de stdio_server contextmanager om het transport te beheren

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

- Geen opzet van webserver of HTTP-eindpunten vereisen
- Als subprocesses door de client worden gestart
- Communiceren via stdin/stdout-streams
- Makkelijker te implementeren en debuggen zijn

## Oefening: Een stdio-server maken

Om onze server te maken moeten we twee dingen in gedachten houden:

- We moeten een webserver gebruiken om eindpunten te exposen voor verbinding en berichten.

## Lab: Een simpele MCP stdio-server maken

In deze lab maken we een simpele MCP-server met de aanbevolen stdio transport. Deze server zal tools exposen die clients kunnen aanroepen met het standaard Model Context Protocol.

### Vereisten

- Python 3.8 of later
- MCP Python SDK: `pip install mcp`
- Basiskennis van async programmeren

Laten we beginnen met het maken van onze eerste MCP stdio-server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Logboekregistratie configureren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Maak de server
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

## Belangrijkste verschillen met de verouderde SSE-aanpak

**Stdio Transport (Huidige standaard):**
- Eenvoudig subprocess-model - client start server als child process
- Communicatie via stdin/stdout met JSON-RPC berichten
- Geen HTTP-server opzet nodig
- Betere prestaties en veiligheid
- Makkelijker te debuggen en ontwikkelen

**SSE Transport (Verouderd sinds MCP 2025-06-18):**
- Vereiste HTTP-server met SSE-eindpunten
- Complexere opzet met webserverinfrastructuur
- Extra beveiligingsoverwegingen voor HTTP-eindpunten
- Nu vervangen door Streamable HTTP voor webgebaseerde scenario's

### Een server maken met stdio transport

Om onze stdio-server te maken, moeten we:

1. **De benodigde bibliotheken importeren** - We hebben de MCP-servercomponenten en stdio transport nodig
2. **Een serverinstantie creëren** - Definieer de server met zijn mogelijkheden
3. **Tools definiëren** - Voeg functionaliteit toe die je wilt exposen
4. **Transport opzetten** - Configureer stdio-communicatie
5. **De server draaien** - Start de server en verwerk berichten

Laten we dit stap voor stap bouwen:

### Stap 1: Maak een basis stdio-server

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

### Stap 3: Server draaien

Sla de code op als `server.py` en voer deze uit vanaf de opdrachtregel:

```bash
python server.py
```

De server start en wacht op invoer van stdin. Hij communiceert met JSON-RPC berichten via de stdio transport.

### Stap 4: Testen met de Inspector

Je kunt je server testen met de MCP Inspector:

1. Installeer de Inspector: `npx @modelcontextprotocol/inspector`
2. Start de Inspector en verbind deze met je server
3. Test de tools die je hebt gemaakt

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Je stdio-server debuggen

### MCP Inspector gebruiken

De MCP Inspector is een waardevol hulpmiddel voor het debuggen en testen van MCP-servers. Zo gebruik je hem met je stdio-server:

1. **Installeer de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Start de Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Test je server**: De Inspector biedt een webinterface waarmee je:
   - Servermogelijkheden kunt bekijken
   - Tools kunt testen met verschillende parameters
   - JSON-RPC berichten kunt volgen
   - Verbindingsproblemen kunt debuggen

### Gebruik van VS Code

Je kunt je MCP-server ook direct in VS Code debuggen:

1. Maak een launchconfiguratie aan in `.vscode/launch.json`:
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

### Algemene debuggingtips

- Gebruik `stderr` voor logging - schrijf nooit naar `stdout`, dit is gereserveerd voor MCP-berichten
- Zorg dat alle JSON-RPC berichten gescheiden zijn door nieuwe regels
- Test eerst met eenvoudige tools voordat je complexe functionaliteit toevoegt
- Gebruik de Inspector om berichtformaten te verifiëren

## Je stdio-server gebruiken in VS Code

Zodra je je MCP stdio-server hebt gebouwd, kun je deze integreren met VS Code om hem te gebruiken met Claude of andere MCP-compatibele clients.

### Configuratie

1. **Maak een MCP-configuratiebestand aan** op `%APPDATA%\Claude\claude_desktop_config.json` (Windows) of `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Herstart Claude**: Sluit Claude en open het opnieuw om de nieuwe serverconfiguratie te laden.

3. **Test de verbinding**: Begin een gesprek met Claude en probeer je servertools:
   - "Kun je me begroeten met de begroetingstool?"
   - "Bereken de som van 15 en 27"
   - "Wat is de serverinformatie?"

### Voorbeeld TypeScript stdio-server

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

// Gereedschappen toevoegen
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

### Voorbeeld .NET stdio-server

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

In deze geüpdatete les heb je geleerd hoe je:

- MCP-servers bouwt met de huidige **stdio transport** (aanbevolen aanpak)
- Begrijpt waarom SSE transport is verouderd ten gunste van stdio en Streamable HTTP
- Tools maakt die door MCP-clients kunnen worden aangeroepen
- Je server debugt met de MCP Inspector
- Je stdio-server integreert met VS Code en Claude

De stdio transport biedt een eenvoudigere, veiligere en snellere manier om MCP-servers te bouwen vergeleken met de verouderde SSE-aanpak. Het is het aanbevolen transport voor de meeste MCP-serverimplementaties vanaf de specificatie van 2025-06-18.

### .NET

1. Laten we eerst wat tools maken, hiervoor maken we een bestand *Tools.cs* met de volgende inhoud:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Oefening: Test je stdio-server

Nu je je stdio-server hebt gebouwd, gaan we deze testen om zeker te zijn dat hij correct werkt.

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

2. **Open de webinterface**: De Inspector opent een browservenster waarin de mogelijkheden van je server worden getoond.

3. **Test de tools**: 
   - Probeer de `get_greeting` tool met verschillende namen
   - Test de `calculate_sum` tool met verschillende getallen
   - Roep de `get_server_info` tool aan om servermetadata te bekijken

4. **Volg de communicatie**: De Inspector toont de JSON-RPC-berichten die tussen client en server worden uitgewisseld.

### Wat je zou moeten zien

Wanneer je server goed start, zie je:
- Servermogelijkheden in de Inspector
- Tools beschikbaar om te testen
- Succesvolle uitwisseling van JSON-RPC berichten
- Reacties van tools in de interface weergegeven

### Veelvoorkomende problemen en oplossingen

**Server start niet:**
- Controleer of alle afhankelijkheden zijn geïnstalleerd: `pip install mcp`
- Controleer Python-syntaxis en inspringing
- Kijk naar foutmeldingen in de console

**Tools verschijnen niet:**
- Zorg dat `@server.tool()` decorators aanwezig zijn
- Controleer of toolfuncties zijn gedefinieerd voordat `main()` wordt aangeroepen
- Verifieer dat de server goed is geconfigureerd

**Verbindingsproblemen:**
- Zorg dat de server correct de stdio transport gebruikt
- Controleer of geen andere processen conflicteren
- Verifieer de Inspector commando syntaxis

## Opdracht

Probeer je server uit te breiden met meer mogelijkheden. Bekijk [deze pagina](https://api.chucknorris.io/) om bijvoorbeeld een tool toe te voegen die een API aanroept. Jij bepaalt hoe de server eruit moet zien. Veel plezier :)
## Oplossing

[Oplossing](./solution/README.md) Hier is een mogelijke oplossing met werkende code.

## Belangrijkste punten

De belangrijkste punten uit dit hoofdstuk zijn:

- De stdio transport is het aanbevolen mechanisme voor lokale MCP-servers.
- Stdio transport maakt naadloze communicatie mogelijk tussen MCP-servers en clients via standaard in- en uitvoerstromen.
- Je kunt zowel Inspector als Visual Studio Code gebruiken om stdio-servers direct aan te spreken, waardoor debugging en integratie eenvoudig is.

## Voorbeelden

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Aanvullende bronnen

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Wat volgt

## Volgende stappen

Nu je weet hoe je MCP-servers bouwt met de stdio transport, kun je meer geavanceerde onderwerpen verkennen:

- **Volgend**: [HTTP Streaming met MCP (Streamable HTTP)](../06-http-streaming/README.md) - Leer over het andere ondersteunde transportmechanisme voor externe servers
- **Geavanceerd**: [MCP Beveiligingspraktijken](../../02-Security/README.md) - Implementeer beveiliging in je MCP-servers
- **Productie**: [Deployment-strategieën](../09-deployment/README.md) - Zet je servers in productie

## Aanvullende bronnen

- [MCP-specificatie 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Officiële specificatie
- [MCP SDK-documentatie](https://github.com/modelcontextprotocol/sdk) - SDK-referenties voor alle talen
- [Communityvoorbeelden](../../06-CommunityContributions/README.md) - Meer servervoorbeelden van de community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel wij streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties voortvloeiend uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->