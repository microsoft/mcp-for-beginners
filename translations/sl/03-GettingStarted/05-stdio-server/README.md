# MCP strežnik s stdio transportom

> **⚠️ Pomembna posodobitev**: Od MCP specifikacije 2025-06-18 je samostojni SSE (Server-Sent Events) transport **opuščen** in nadomeščen s transportom "Streamable HTTP". Trenutna MCP specifikacija opredeljuje dva glavna transportna mehanizma:
> 1. **stdio** - Standardni vhod/izhod (priporočeno za lokalne strežnike)
> 2. **Streamable HTTP** - Za oddaljene strežnike, ki lahko interno uporabljajo SSE
>
> Ta lekcija je posodobljena, da se osredotoča na **stdio transport**, ki je priporočena metoda za večino implementacij MCP strežnikov.

Stdio transport omogoča MCP strežnikom komunikacijo s klienti prek standardnih vhodnih in izhodnih tokov. To je najpogosteje uporabljena in priporočena transportna metoda v trenutni MCP specifikaciji, saj omogoča preprost in učinkovit način za gradnjo MCP strežnikov, ki jih je mogoče enostavno integrirati z različnimi klientskimi aplikacijami.

## Pregled

Ta lekcija pokriva, kako zgraditi in uporabljati MCP strežnike z uporabo stdio transporta.

## Cilji učenja

Do konca te lekcije boste znali:

- Zgraditi MCP strežnik z uporabo stdio transporta.
- Odpravljati napake na MCP strežniku z uporabo Inspectorja.
- Uporabljati MCP strežnik v Visual Studio Code.
- Razumeti trenutne MCP transportne mehanizme in zakaj je stdio priporočljiv.

## stdio transport - Kako deluje

Stdio transport je eden od dveh podprtih transportnih tipov v trenutni MCP specifikaciji (2025-06-18). Tukaj je, kako deluje:

- **Preprosta komunikacija**: Strežnik bere JSON-RPC sporočila iz standardnega vhoda (`stdin`) in pošilja sporočila na standardni izhod (`stdout`).
- **Na osnovi procesov**: Klient zažene MCP strežnik kot podproces.
- **Format sporočil**: Sporočila so posamezne JSON-RPC zahteve, obvestila ali odgovori, ločeni z novimi vrsticami.
- **Beleženje**: Strežnik LAHKO piše UTF-8 nize na standardni izhod za napake (`stderr`) za beleženje.

### Ključne zahteve:
- Sporočila MORAJO biti ločena z novimi vrsticami in NE SMEJO vsebovati vgrajenih novih vrstic.
- Strežnik NE SME pisati ničesar na `stdout`, kar ni veljavno MCP sporočilo.
- Klient NE SME pisati ničesar na strežnikov `stdin`, kar ni veljavno MCP sporočilo.

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

V zgornji kodi:

- Uvozimo razreda `Server` in `StdioServerTransport` iz MCP SDK.
- Ustvarimo instanco strežnika z osnovno konfiguracijo in zmožnostmi.

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

V zgornji kodi:

- Ustvarimo instanco strežnika z uporabo MCP SDK.
- Definiramo orodja z uporabo dekoratorjev.
- Uporabimo kontekstni upravitelj `stdio_server` za upravljanje transporta.

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

Ključna razlika od SSE je, da stdio strežniki:

- Ne potrebujejo nastavitve spletnega strežnika ali HTTP končnih točk.
- So zagnani kot podprocesi s strani klienta.
- Komunicirajo prek tokov stdin/stdout.
- So enostavnejši za implementacijo in odpravljanje napak.

## Vaja: Ustvarjanje stdio strežnika

Za ustvarjanje našega strežnika moramo upoštevati dve stvari:

- Uporabiti moramo spletni strežnik za izpostavitev končnih točk za povezavo in sporočila.

## Laboratorijska vaja: Ustvarjanje preprostega MCP stdio strežnika

V tej vaji bomo ustvarili preprost MCP strežnik z uporabo priporočenega stdio transporta. Ta strežnik bo izpostavil orodja, ki jih lahko klienti kličejo z uporabo standardnega Model Context Protocol.

### Predpogoji

- Python 3.8 ali novejši
- MCP Python SDK: `pip install mcp`
- Osnovno razumevanje asinhronega programiranja

Začnimo z ustvarjanjem našega prvega MCP stdio strežnika:

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

## Ključne razlike od opuščenega SSE pristopa

**Stdio transport (trenutni standard):**
- Preprost model podprocesov - klient zažene strežnik kot otroški proces.
- Komunikacija prek stdin/stdout z uporabo JSON-RPC sporočil.
- Ni potrebna nastavitev spletnega strežnika.
- Boljša zmogljivost in varnost.
- Lažje odpravljanje napak in razvoj.

**SSE transport (opuščen od MCP 2025-06-18):**
- Zahteval je spletni strežnik s SSE končnimi točkami.
- Bolj zapletena nastavitev z infrastrukturo spletnega strežnika.
- Dodatni varnostni premisleki za HTTP končne točke.
- Zdaj nadomeščen s Streamable HTTP za spletne scenarije.

### Ustvarjanje strežnika z stdio transportom

Za ustvarjanje našega stdio strežnika moramo:

1. **Uvoziti potrebne knjižnice** - Potrebujemo komponente MCP strežnika in stdio transport.
2. **Ustvariti instanco strežnika** - Definirati strežnik z njegovimi zmožnostmi.
3. **Definirati orodja** - Dodati funkcionalnosti, ki jih želimo izpostaviti.
4. **Nastaviti transport** - Konfigurirati stdio komunikacijo.
5. **Zagnati strežnik** - Začeti strežnik in obdelovati sporočila.

Gradimo to korak za korakom:

### Korak 1: Ustvarjanje osnovnega stdio strežnika

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

### Korak 2: Dodajanje več orodij

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

### Korak 3: Zagon strežnika

Shrani kodo kot `server.py` in jo zaženi iz ukazne vrstice:

```bash
python server.py
```

Strežnik se bo zagnal in čakal na vhod iz stdin. Komunicira z uporabo JSON-RPC sporočil prek stdio transporta.

### Korak 4: Testiranje z Inspectorjem

Svoj strežnik lahko testirate z uporabo MCP Inspectorja:

1. Namestite Inspector: `npx @modelcontextprotocol/inspector`
2. Zaženite Inspector in ga usmerite na svoj strežnik.
3. Testirajte orodja, ki ste jih ustvarili.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Odpravljanje napak na vašem stdio strežniku

### Uporaba MCP Inspectorja

MCP Inspector je dragoceno orodje za odpravljanje napak in testiranje MCP strežnikov. Tukaj je, kako ga uporabiti z vašim stdio strežnikom:

1. **Namestite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Zaženite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte svoj strežnik**: Inspector ponuja spletni vmesnik, kjer lahko:
   - Pregledate zmožnosti strežnika.
   - Testirate orodja z različnimi parametri.
   - Spremljate JSON-RPC sporočila.
   - Odpravljate težave s povezavo.

### Uporaba VS Code

Svoj MCP strežnik lahko odpravljate neposredno v VS Code:

1. Ustvarite konfiguracijo zagona v `.vscode/launch.json`:
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

2. Nastavite točke prekinitve v kodi strežnika.
3. Zaženite razhroščevalnik in testirajte z Inspectorjem.

### Pogosti nasveti za odpravljanje napak

- Uporabite `stderr` za beleženje - nikoli ne pišite na `stdout`, saj je rezerviran za MCP sporočila.
- Prepričajte se, da so vsa JSON-RPC sporočila ločena z novimi vrsticami.
- Najprej testirajte s preprostimi orodji, preden dodate kompleksno funkcionalnost.
- Uporabite Inspector za preverjanje formatov sporočil.

## Uporaba vašega stdio strežnika v VS Code

Ko ste zgradili svoj MCP stdio strežnik, ga lahko integrirate z VS Code za uporabo s Claude ali drugimi MCP združljivimi klienti.

### Konfiguracija

1. **Ustvarite MCP konfiguracijsko datoteko** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ali `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Ponovno zaženite Claude**: Zaprite in ponovno odprite Claude, da naložite novo konfiguracijo strežnika.

3. **Testirajte povezavo**: Začnite pogovor s Claude in poskusite uporabiti orodja vašega strežnika:
   - "Ali me lahko pozdraviš z orodjem za pozdrav?"
   - "Izračunaj vsoto 15 in 27."
   - "Kakšne so informacije o strežniku?"

### TypeScript primer stdio strežnika

Tukaj je celoten primer v TypeScript za referenco:

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

### .NET primer stdio strežnika

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

## Povzetek

V tej posodobljeni lekciji ste se naučili:

- Graditi MCP strežnike z uporabo trenutnega **stdio transporta** (priporočena metoda).
- Razumeti, zakaj je bil SSE transport opuščen v korist stdio in Streamable HTTP.
- Ustvariti orodja, ki jih lahko kličejo MCP klienti.
- Odpravljati napake na strežniku z uporabo MCP Inspectorja.
- Integrirati svoj stdio strežnik z VS Code in Claude.

Stdio transport ponuja preprostejši, varnejši in zmogljivejši način za gradnjo MCP strežnikov v primerjavi z opuščenim SSE pristopom. To je priporočeni transport za večino implementacij MCP strežnikov od specifikacije 2025-06-18.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.