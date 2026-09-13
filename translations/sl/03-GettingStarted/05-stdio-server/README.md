# MCP strežnik s stdio transportom

> **⚠️ Pomembna posodobitev**: Od MCP specifikacije 2025-06-18 je samostojni SSE (Server-Sent Events) transport **prenehan** in nadomeščen s "Streamable HTTP" transportom. Trenutna MCP specifikacija določa dva osnovna transportna mehanizma:
> 1. **stdio** - Standardni vhod/izhod (priporočeno za lokalne strežnike)
> 2. **Streamable HTTP** - Za oddaljene strežnike, ki lahko interno uporabljajo SSE
>
> Ta lekcija je posodobljena in se osredotoča na **stdio transport**, ki je priporočena metoda za večino implementacij MCP strežnikov.

Stdio transport omogoča MCP strežnikom komunikacijo s strankami skozi standardne vhode in izhode. To je najpogosteje uporabljen in priporočljiv transportni mehanizem v trenutni MCP specifikaciji, ki zagotavlja enostaven in učinkovit način za izdelavo MCP strežnikov, ki jih je enostavno integrirati z različnimi odjemalskimi aplikacijami.

## Pregled

Ta lekcija pokriva, kako ustvariti in uporabljati MCP strežnike z uporabo stdio transporta.

## Cilji učenja

Ob koncu te lekcije boste sposobni:

- Izdelati MCP strežnik z stdio transportom.
- Odpravljati napake MCP strežnika z uporabo Inspektorja.
- Uporabiti MCP strežnik v Visual Studio Code.
- Razumeti trenutne MCP transportne mehanizme in zakaj je stdio priporočljiv.


## stdio Transport - Kako deluje

Stdio transport je eden od dveh standardnih transportov v MCP specifikaciji
`2026-07-28`. Tako deluje:

- **Preprosta komunikacija**: strežnik bere JSON-RPC sporočila iz standardnega vhoda (`stdin`) in pošilja sporočila na standardni izhod (`stdout`).
- **Na podlagi procesa**: odjemalec zažene MCP strežnik kot podproces.
- **Format sporočil**: sporočila so posamezni JSON-RPC zahtevki, obvestila ali odgovori, ločeni z novimi vrsticami.
- **Dnevni zapis**: strežnik LAHKO piše UTF-8 nize na standardno napako (`stderr`) za potrebe beleženja.

### Ključne zahteve:
- Sporočila MORAJO biti ločena z novimi vrsticami in NE SMEJO vsebovati vdelanih novih vrstic
- Strežnik NE SME pisati ničesar na `stdout`, kar ni veljavno MCP sporočilo
- Odjemalec NE SME pisati ničesar v strežnikov `stdin`, kar ni veljavno MCP sporočilo

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

- Uvozimo `Server` razred in `StdioServerTransport` iz MCP SDK
- Ustvarimo instanco strežnika z osnovno konfiguracijo in zmožnostmi
- Ustvarimo instanco `StdioServerTransport` in povežemo strežnik z njim, kar omogoča komunikacijo preko stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Ustvari primerek strežnika
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

- Ustvarimo instanco strežnika z uporabo MCP SDK
- Definiramo orodja s pomočjo dekoratorjev
- Uporabimo upravljalnik konteksta stdio_server za upravljanje transporta

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

Ključna razlika od SSE je, da stdio strežniki:

- Ne potrebujejo nastavitve spletnega strežnika ali HTTP končnih točk
- So zagnani kot podprocesi s strani odjemalca
- Komunicirajo preko stdin/stdout tokov
- So preprostejši za izvedbo in odpravljanje napak

## Vaja: Ustvarjanje stdio strežnika

Za izdelavo strežnika moramo imeti dve stvari v mislih:

- Potrebujemo spletni strežnik za izpostavitev končnih točk za povezavo in sporočila.
## Laboratorij: Ustvarjanje preprostega MCP stdio strežnika

V tem laboratoriju bomo ustvarili preprost MCP strežnik z uporabo priporočanega stdio transporta. Ta strežnik bo izpostavil orodja, ki jih lahko kličejo stranke z uporabo standardnega Model Context Protocola.

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

# Konfiguriraj beleženje
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ustvari strežnik
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
    # Uporabi stdio prenos
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ključne razlike v primerjavi s prenehanim SSE pristopom

**Stdio Transport (trenutni standard):**
- Preprost model podprocesa - odjemalec zažene strežnik kot otroški proces
- Komunikacija preko stdin/stdout z uporabo JSON-RPC sporočil
- Ni potrebna nastavitev HTTP strežnika
- Boljša zmogljivost in varnost
- Lažje odpravljanje napak in razvoj

**SSE Transport (prenehan od MCP 2025-06-18):**
- Zahtevani HTTP strežnik z SSE končnimi točkami
- Bolj zapletena nastavitev s spletno strežniško infrastrukturo
- Dodatne varnostne zahteve za HTTP končne točke
- Zdaj nadomeščen s Streamable HTTP za spletne scenarije

### Ustvarjanje strežnika s stdio transportom

Za ustvarjanje našega stdio strežnika moramo:

1. **Uvoziti potrebne knjižnice** - potrebujemo MCP strežniške komponente in stdio transport
2. **Ustvariti instanco strežnika** - definirati strežnik z njegovimi zmožnostmi
3. **Definirati orodja** - dodati funkcionalnosti, ki jih želimo izpostaviti
4. **Nastaviti transport** - konfigurirati stdio komunikacijo
5. **Zagnati strežnik** - zagnati strežnik in upravljati sporočila

Zgradimo to korak za korakom:

### Korak 1: Ustvarite osnovni stdio strežnik

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfiguriraj beleženje
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ustvari strežnik
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

Kodo shranite kot `server.py` in jo zaženite iz ukazne vrstice:

```bash
python server.py
```

Strežnik se bo zagnal in čakal na vhod iz stdin. Komunicira preko JSON-RPC sporočil prek stdio transporta.

### Korak 4: Testiranje z Inspektorjem

Strežnik lahko testirate z MCP Inspektorjem:

1. Namestite Inspektor: `npx @modelcontextprotocol/inspector`
2. Zaženite Inspektor in ga usmerite na svoj strežnik
3. Testirajte orodja, ki ste jih ustvarili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Odpravljanje napak vašega stdio strežnika

### Uporaba MCP Inspektorja

MCP Inspektor je dragoceno orodje za odpravljanje napak in testiranje MCP strežnikov. Tako ga uporabite z vašim stdio strežnikom:

1. **Namestite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Zaženite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte strežnik**: Inspektor ponuja spletni vmesnik, kjer lahko:
   - Prikazujete zmožnosti strežnika
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

2. Nastavite točke prekinitve v vaši kodi strežnika
3. Zaženite razhroščevalnik in testirajte z Inspektorjem

### Pogosti nasveti za odpravljanje napak

- Uporabljajte `stderr` za beleženje - nikoli ne pišite na `stdout`, saj je rezerviran za MCP sporočila
- Poskrbite, da so vsa JSON-RPC sporočila ločena z novo vrstico
- Najprej testirajte s preprostimi orodji, preden dodate kompleksno funkcionalnost
- Uporabljajte Inspektor za preverjanje formatov sporočil

## Uporaba vašega stdio strežnika v VS Code


Ko zgradite svoj MCP stdio strežnik, ga lahko integrirate z VS Code, da ga uporabljate z Claude ali drugimi MCP-kompatibilnimi odjemalci.

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

3. **Preizkusite povezavo**: Začnite pogovor s Claude in poskusite uporabiti orodja vašega strežnika:
   - "Me lahko pozdraviš z orodjem za pozdrav?"
   - "Izračunaj vsoto 15 in 27"
   - "Kaj so informacije o strežniku?"

### Primer stdio strežnika v TypeScriptu

Tukaj je popoln primer v TypeScriptu za referenco:

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

// Dodaj orodja
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

### Primer stdio strežnika v .NET

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

V tej posodobljeni lekciji ste se naučili:

- Kako graditi MCP strežnike z uporabo trenutnega **stdio transporta** (priporočeni pristop)
- Razumeti, zakaj je bil SSE transport opuščen v prid stdio in Streamable HTTP
- Ustvarjati orodja, ki jih lahko kličejo MCP odjemalci
- Razhroščevati vaš strežnik z uporabo MCP Inspectorja
- Integrirati vaš stdio strežnik z VS Code in Claude

Stdio transport zagotavlja preprostejši, varnejši in zmogljivejši način za gradnjo MCP strežnikov v primerjavi z opuščenim SSE pristopom. Je priporočen transport za večino MCP strežniških implementacij od specifikacije 2025-06-18.


### .NET

1. Najprej ustvarimo nekaj orodij, za to bomo ustvarili datoteko *Tools.cs* z naslednjo vsebino:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vaja: Testiranje vašega stdio strežnika

Zdaj, ko ste zgradili svoj stdio strežnik, ga preizkusimo, da zagotovimo pravilno delovanje.

### Zahteve

1. Prepričajte se, da imate nameščen MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaša koda strežnika mora biti shranjena (npr. kot `server.py`)

### Testiranje z Inspectorjem

1. **Zaženite Inspector z vašim strežnikom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Odprite spletni vmesnik**: Inspector bo odprl brskalnik, ki prikazuje zmogljivosti vašega strežnika.

3. **Preizkusite orodja**:
   - Preizkusite orodje `get_greeting` z različnimi imeni
   - Preizkusite orodje `calculate_sum` z različnimi številkami
   - Pokličite orodje `get_server_info` za ogled metapodatkov strežnika

4. **Nadzorujte komunikacijo**: Inspector prikazuje JSON-RPC sporočila, ki se izmenjujejo med odjemalcem in strežnikom.

### Kaj bi morali videti

Ko se vaš strežnik uspešno zažene, bi morali videti:
- Zmogljivosti strežnika navedene v Inspectorju
- Orodja, na voljo za testiranje
- Uspešne izmenjave JSON-RPC sporočil
- Odzivi orodij prikazani v vmesniku

### Pogoste težave in rešitve

**Strežnik se ne zažene:**
- Preverite, da so vse odvisnosti nameščene: `pip install mcp`
- Preverite Python sintakso in zamike
- Poiščite sporočila o napakah v konzoli

**Orodja se ne prikazujejo:**
- Prepričajte se, da so prisotni dekoratorji `@server.tool()`
- Preverite, da so funkcije orodij definirane pred `main()`
- Preverite, da je strežnik pravilno konfiguriran

**Težave s povezavo:**
- Prepričajte se, da strežnik pravilno uporablja stdio transport
- Preverite, da ne motijo drugi procesi
- Preverite sintakso ukaza Inspectorja

## Domača naloga

Poskusite razširiti svoj strežnik z več zmogljivostmi. Ogledate si [to stran](https://api.chucknorris.io/) in na primer dodajte orodje, ki kliče API. Vi odločite, kako naj strežnik izgleda. Zabavajte se :)
## Rešitev

[Rešitev](./solution/README.md) Tukaj je možna rešitev z delujočo kodo.

## Ključne ugotovitve

Ključne ugotovitve iz tega poglavja so naslednje:

- Stdio transport je priporočeni mehanizem za lokalne MCP strežnike.
- Stdio transport omogoča nemoteno komunikacijo med MCP strežniki in odjemalci z uporabo standardnih vhodnih in izhodnih tokov.
- Uporabljate lahko tako Inspector kot Visual Studio Code za neposredno uporabo stdio strežnikov, kar omogoča enostavno razhroščevanje in integracijo.

## Primeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)

## Dodatni viri

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kaj sledi

## Naslednji koraki

Zdaj, ko ste se naučili graditi MCP strežnike s stdio transportom, lahko raziščete bolj napredne teme:

- **Naslednji**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Spoznajte drugi podprti mehanizem transporta za oddaljene strežnike
- **Napredno**: [Najboljše prakse MCP varnosti](../../02-Security/README.md) - Uvedba varnosti v vaše MCP strežnike
- **Produkcija**: [Strategije uvajanja](../09-deployment/README.md) - Postavite svoje strežnike za produkcijsko uporabo

## Dodatni viri

- [MCP specifikacija 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutna specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za vse jezike
- [Skupnostni primeri](../../06-CommunityContributions/README.md) - Več strežniških primerov iz skupnosti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->