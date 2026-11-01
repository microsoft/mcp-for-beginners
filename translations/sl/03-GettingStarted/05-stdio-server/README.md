# MCP strežnik s stdio prenosom

> **⚠️ Pomembna posodobitev**: Od specifikacije MCP 2025-06-18 je samostojen SSE (Server-Sent Events) prenos **zastarel** in nadomeščen z "Streamable HTTP" prenosom. Trenutna specifikacija MCP določa dva osnovna mehanizma prenosa:
> 1. **stdio** - Standardni vhod/izhod (priporočeno za lokalne strežnike)
> 2. **Streamable HTTP** - Za oddaljene strežnike, ki lahko uporabljajo SSE interno
>
> Ta lekcija je posodobljena, da se osredotoči na **stdio prenos**, ki je priporočeni pristop za večino izvedb MCP strežnikov.

Prenos stdio omogoča MCP strežnikom komunikacijo s klienti prek standardnih vhodnih in izhodnih tokov. To je najpogosteje uporabljen in priporočeni mehanizem prenosa v trenutni MCP specifikaciji, ki zagotavlja preprost in učinkovit način gradnje MCP strežnikov, ki jih je enostavno vključiti v različne odjemalce.

## Pregled

Ta lekcija obravnava, kako zgraditi in uporabljati MCP strežnike s stdio prenosom.

## Cilji učenja

Do konca te lekcije boste sposobni:

- Zgraditi MCP strežnik z uporabo stdio prenosa.
- Odpravljati napake MCP strežnika z uporabo Inspektorja.
- Uporabljati MCP strežnik z Visual Studio Code.
- Razumeti trenutne mehanizme prenosa MCP in zakaj je stdio priporočeno.


## stdio prenos - Kako deluje

stdio prenos je eden od dveh standardnih prenosov v specifikaciji MCP
`2026-07-28`. Tukaj je, kako deluje:

- **Preprosta komunikacija**: Strežnik bere JSON-RPC sporočila iz standardnega vhoda (`stdin`) in pošilja sporočila na standardni izhod (`stdout`).
- **Procesno osnovano**: Klient zažene MCP strežnik kot podproces.
- **Format sporočil**: Sporočila so posamezne JSON-RPC zahteve, obvestila ali odgovori, ločeni z novimi vrsticami.
- **Dnevniško beleženje**: Strežnik LAHKO piše UTF-8 nize na standardni error (`stderr`) za potrebe beleženja.

### Ključne zahteve:
- Sporočila MORAJO biti ločena z novimi vrsticami in NE SMEJO vsebovati vstavljenih novih vrstic
- Strežnik NE SME pisati ničesar v `stdout`, kar ni veljavno MCP sporočilo
- Klient NE SME pisati ničesar v strežnikov `stdin`, kar ni veljavno MCP sporočilo

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

V zgornji kodi:

- Uvozimo razred `Server` in `StdioServerTransport` iz MCP SDK
- Ustvarimo primer strežnika z osnovno konfiguracijo in zmogljivostmi
- Ustvarimo primer `StdioServerTransport` in povežemo strežnik z njim, omogočimo komunikacijo preko stdin/stdout

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

- Ustvarimo primer strežnika z uporabo MCP SDK
- Definiramo orodja z dekoraterji
- Uporabimo kontekstni upravljalnik stdio_server za prenos

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

Ključna razlika v primerjavi s SSE je, da stdio strežniki:

- Ne potrebujejo nastavitev spletnega strežnika ali HTTP končnih točk
- So zagnani kot podprocesi s strani klienta
- Komunicirajo prek tokov stdin/stdout
- So enostavnejši za implementacijo in odpravljanje napak

## Vaja: Ustvarjanje stdio strežnika

Za ustvarjanje našega strežnika moramo upoštevati dve stvari:

- Potrebno je uporabiti spletni strežnik za izpostavitev končnih točk za povezave in sporočila.
## Laboratorij: Ustvarjanje preprostega MCP stdio strežnika

V tem laboratoriju bomo ustvarili preprost MCP strežnik z uporabo priporočene stdio prenosa. Ta strežnik bo izpostavil orodja, ki jih lahko kličejo klienti preko standardnega Model Context Protocol.

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

## Ključne razlike od zastarelega SSE pristopa

**Stdio prenos (trenutni standard):**
- Preprost model podprocesov - klient zažene strežnik kot otroški proces
- Komunikacija preko stdin/stdout z uporabo JSON-RPC sporočil
- Ni potrebna nastavitev HTTP strežnika
- Boljša zmogljivost in varnost
- Lažje odpravljanje napak in razvoj

**SSE prenos (zastarel od MCP 2025-06-18):**
- Potreben HTTP strežnik s SSE končnimi točkami
- Bolj zapletena nastavitev s spletno strežniško infrastrukturo
- Dodatni varnostni premisleki za HTTP končne točke
- Zamenjan s Streamable HTTP za spletne scenarije

### Ustvarjanje strežnika s stdio prenosom

Za ustvarjanje našega stdio strežnika moramo:

1. **Uvoziti zahtevane knjižnice** - Potrebujemo MCP strežniške komponente in stdio prenos
2. **Ustvariti primer strežnika** - Definirati strežnik z njegovimi zmogljivostmi
3. **Definirati orodja** - Dodati funkcionalnosti, ki jih želimo izpostaviti
4. **Nastaviti prenos** - Konfigurirati stdio komunikacijo
5. **Zagnati strežnik** - Zagnati strežnik in obravnavati sporočila

Gradimo to korak za korakom:

### Korak 1: Ustvarite osnovni stdio strežnik

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

### Korak 2: Dodajte več orodij

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

Strežnik se bo zagnal in čakal na vhod iz stdin. Komunicira z uporabo JSON-RPC sporočil preko stdio prenosa.

### Korak 4: Testiranje z Inspektorjem

Strežnik lahko testirate z MCP Inspektorjem:

1. Namestite Inspektor: `npx @modelcontextprotocol/inspector`
2. Zaženite Inspektor in ga usmerite na svoj strežnik
3. Testirajte ustvarjena orodja

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Odpravljanje napak vašega stdio strežnika

### Uporaba MCP Inspektorja

MCP Inspektor je dragoceno orodje za odpravljanje napak in testiranje MCP strežnikov. Tako ga uporabiti z vašim stdio strežnikom:

1. **Namestite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Zaženite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte svoj strežnik**: Inspektor nudi spletni vmesnik, kjer lahko:
   - Ogledate zmogljivosti strežnika
   - Testirate orodja z različnimi parametri
   - Spremljate JSON-RPC sporočila
   - Odpravljate težave s povezavo

### Uporaba VS Code

MCP strežnik lahko tudi neposredno odpravljate v VS Code:

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

2. Postavite prekinitvene točke v kodi strežnika
3. Zaženite razhroščevalnik in testirajte z Inspektorjem

### Pogosti nasveti za odpravljanje napak

- Uporabljajte `stderr` za dnevniško beleženje - nikoli ne pišite v `stdout`, ker je rezervirano za MCP sporočila
- Poskrbite, da so vsa JSON-RPC sporočila zaključena z novo vrstico
- Najprej testirajte s preprostimi orodji, preden dodate kompleksno funkcionalnost
- Uporabite Inspektor za preverjanje formatov sporočil

## Uporaba vašega stdio strežnika v VS Code

Ko ustvarite svoj MCP stdio strežnik, ga lahko integrirate z VS Code in uporabljate s Claude ali drugimi MCP-kompatibilnimi klienti.

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

2. **Znova zaženite Claude**: Zaprite in ponovno odprite Claude, da naloži novo konfiguracijo strežnika.

3. **Testirajte povezavo**: Začnite pogovor s Claude in poskusite uporabiti orodja vašega strežnika:
   - "Me lahko pozdraviš z orodjem za pozdrav?"
   - "Izračunaj vsoto 15 in 27"
   - "Kakšne so informacije o strežniku?"

### Primer TypeScript stdio strežnika

Tu je za primer celoten TypeScript primer za referenco:

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

### Primer .NET stdio strežnika

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

## Povzetek

V tej posodobljeni lekciji ste se naučili, kako:

- Zgraditi MCP strežnike z uporabo trenutnega **stdio prenosa** (priporočeni pristop)
- Razumeti, zakaj je bil SSE prenos zastarel v korist stdio in Streamable HTTP
- Ustvariti orodja, ki jih lahko kličejo MCP klienti
- Odpravljati napake na strežniku z uporabo MCP Inspektorja
- Integrirati stdio strežnik z VS Code in Claude

stdio prenos omogoča enostavnejši, varnejši in bolj učinkovit način gradnje MCP strežnikov v primerjavi z zastarelim SSE pristopom. Je priporočeni prenos za večino izvedb MCP strežnikov po specifikaciji 2025-06-18.


### .NET

1. Najprej ustvarimo nekaj orodij, za to bomo ustvarili datoteko *Tools.cs* z naslednjo vsebino:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vaja: Testiranje vašega stdio strežnika

Ko ste zgradili stdio strežnik, ga preizkusimo, da zagotovimo pravilno delovanje.

### Predpogoji

1. Prepričajte se, da imate nameščen MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaša strežniška koda mora biti shranjena (npr. kot `server.py`)

### Testiranje z Inspektorjem

1. **Zaženite Inspektor s strežnikom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Odprite spletni vmesnik**: Inspektor bo odprl brskalnik, ki prikazuje zmogljivosti vašega strežnika.

3. **Testirajte orodja**: 
   - Preizkusite orodje `get_greeting` z različnimi imeni
   - Testirajte orodje `calculate_sum` z različnimi številkami
   - Pokličite orodje `get_server_info` za ogled metapodatkov strežnika

4. **Nadzor komunikacije**: Inspektor prikazuje JSON-RPC sporočila, ki se izmenjujejo med klientom in strežnikom.

### Kaj naj bi videli

Ko se vaš strežnik uspešno zažene, bi morali videti:
- Zmogljivosti strežnika navedene v Inspektorju
- Orodja na voljo za testiranje
- Uspešne izmenjave JSON-RPC sporočil
- Odgovori orodij prikazani v vmesniku

### Pogoste težave in rešitve

**Strežnik se ne zažene:**
- Preverite, da so vse odvisnosti nameščene: `pip install mcp`
- Preverite Python sintakso in zamike
- Iščite sporočila o napakah v konzoli

**Orodja se ne prikazujejo:**
- Prepričajte se, da so prisotni dekoraterji `@server.tool()`
- Preverite, da so funkcije orodij definirane pred `main()`
- Preverite, da je strežnik pravilno konfiguriran

**Težave s povezavo:**
- Prepričajte se, da strežnik pravilno uporablja stdio prenos
- Preverite, da nobeni drugi procesi ne motijo
- Preverite sintakso ukaza Inspektorja

## Naloga

Poskusite razširiti svoj strežnik z več zmogljivostmi. Oglejte si [to stran](https://api.chucknorris.io/), da na primer dodate orodje, ki kliče API. Odločite se, kako naj strežnik izgleda. Zabavajte se :)
## Rešitev

[Rešitev](./solution/README.md) Tukaj je možna rešitev s delujočo kodo.

## Ključne ugotovitve

Ključne ugotovitve iz tega poglavja so:

- Stdio prenos je priporočeni mehanizem za lokalne MCP strežnike.
- Stdio prenos omogoča nemoteno komunikacijo med MCP strežniki in klienti preko standardnih vhodnih in izhodnih tokov.
- Za porabo stdio strežnikov lahko uporabljate tako Inspektor kot Visual Studio Code, kar poenostavlja odpravljanje napak in integracijo.

## Primeri 

- [Java kalkulator](../samples/java/calculator/README.md)
- [.NET kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkulator](../samples/javascript/README.md)
- [TypeScript kalkulator](../samples/typescript/README.md)
- [Python kalkulator](../../../../03-GettingStarted/samples/python) 

## Dodatni viri

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kaj sledi

## Naslednji koraki

Zdaj, ko ste se naučili, kako graditi MCP strežnike s stdio prenosom, lahko raziskujete bolj napredne teme:

- **Naslednje**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Spoznajte drugi podprti mehanizem prenosa za oddaljene strežnike
- **Napredno**: [Najboljše prakse za varnost MCP](../../02-Security/README.md) - Vpeljite varnost v vaše MCP strežnike
- **Produkcija**: [Strategije namestitve](../09-deployment/README.md) - Namestite svoje strežnike za produkcijsko rabo

## Dodatni viri

- [Specifikacija MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutna specifikacija
- [Dokumentacija MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referenčni SDK za vse jezike
- [Primeri skupnosti](../../06-CommunityContributions/README.md) - Več strežniških primerov iz skupnosti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->