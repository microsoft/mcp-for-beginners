# MCP strežnik s stdio prenosom

> **⚠️ Pomembna posodobitev**: Od specifikacije MCP 2025-06-18 je samostojni SSE (Server-Sent Events) prenos **ukinjen** in zamenjan s prenosom "Streamable HTTP". Trenutna specifikacija MCP določa dva primarna mehanizma prenosa:
> 1. **stdio** - Standardni vhod/izhod (priporočeno za lokalne strežnike)
> 2. **Streamable HTTP** - Za oddaljene strežnike, ki lahko notranje uporabljajo SSE
>
> Ta lekcija je posodobljena, da se osredotoči na **stdio prenos**, ki je priporočeni pristop za večino implementacij MCP strežnikov.

Prenos stdio omogoča MCP strežnikom komunikacijo s klienti prek standardnih vhodnih in izhodnih tokov. To je najenostavnejši in priporočeni mehanizem prenosa v trenutni specifikaciji MCP, ki omogoča preprosto in učinkovito gradnjo MCP strežnikov, ki jih je mogoče enostavno integrirati z različnimi klientskimi aplikacijami.

## Pregled

V tej lekciji bomo pokrili, kako ustvariti in uporabljati MCP strežnike z uporabo stdio prenosa.

## Cilji učenja

Do konca te lekcije boste znali:

- Ustvariti MCP strežnik s stdio prenosom.
- Odpravljati napake na MCP strežniku z uporabo Inspektorja.
- Uporabljati MCP strežnik v Visual Studio Code.
- Razumeti trenutne mehanizme prenosa MCP in zakaj je stdio priporočeno.

## Prenos stdio - Kako deluje

Prenos stdio je ena od dveh podprtih vrst prenosa v trenutni MCP specifikaciji (2025-06-18). Tako deluje:

- **Preprosta komunikacija**: strežnik bere JSON-RPC sporočila s standardnega vhoda (`stdin`) in pošilja sporočila na standardni izhod (`stdout`).
- **Postopek značen**: klient zažene MCP strežnik kot podproces.
- **Oblika sporočil**: sporočila so posamezni JSON-RPC zahtevki, obvestila ali odgovori, ločeni z novimi vrsticami.
- **Dnevniški zapisi**: strežnik LAHKO piše UTF-8 nize na standardno napako (`stderr`) za potrebe dnevnikov.

### Ključne zahteve:
- Sporočila MORAJO biti ločena z novimi vrsticami in NE SMEJO vsebovati vključenih novih vrstic
- Strežnik NE SME pisati česarkoli na `stdout`, kar ni veljavno MCP sporočilo
- Klient NE SME pisati česarkoli na `stdin` strežnika, kar ni veljavno MCP sporočilo

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

- Uvažamo razred `Server` in `StdioServerTransport` iz MCP SDK
- Ustvarimo instanco strežnika z osnovno konfiguracijo in zmogljivostmi
- Ustvarimo instanco `StdioServerTransport` in povežemo strežnik z njim, omogočamo komunikacijo preko stdin/stdout

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

- Ustvarimo instanco strežnika z MCP SDK
- Definiramo orodja z dekoratorji
- Uporabljamo kontekstni upravljalec stdio_server za prenos

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
- So zagnani kot podprocesi s strani klienta
- Komunicirajo preko tokov stdin/stdout
- So lažji za implementacijo in odpravljanje napak

## Vaja: Ustvarjanje stdio strežnika

Za ustvarjanje našega strežnika moramo upoštevati dve stvari:

- Za izpostavitev končnih točk za povezavo in sporočila potrebujemo spletni strežnik.
## Lab: Ustvarjanje preprostega MCP stdio strežnika

V tem laboratoriju bomo ustvarili preprost MCP strežnik z uporabo priporočenega stdio prenosa. Ta strežnik bo izpostavil orodja, ki jih lahko kličejo klienti z uporabo standardnega Model Context Protocol.

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

## Ključne razlike od ukinjenega SSE pristopa

**Prenos Stdio (trenutni standard):**
- Preprost model podprocesa - klient zažene strežnik kot otroški proces
- Komunikacija prek stdin/stdout z JSON-RPC sporočili
- Ni potrebne nastavitve HTTP strežnika
- Boljša zmogljivost in varnost
- Lažje odpravljanje napak in razvoj

**Prenos SSE (ukinjen od MCP 2025-06-18):**
- Zahteva HTTP strežnik z SSE končnimi točkami
- Bolj kompleksna nastavitev s spletno infrastrukturo
- Dodatna varnostna vprašanja za HTTP končne točke
- Zamenjan s Streamable HTTP za spletne primere

### Ustvarjanje strežnika z stdio prenosom

Za ustvarjanje našega stdio strežnika moramo:

1. **Uvoziti potrebne knjižnice** - potrebujemo MCP strežniške komponente in stdio prenos
2. **Ustvariti instanco strežnika** - opredeliti strežnik z njegovimi zmogljivostmi
3. **Definirati orodja** - dodati funkcionalnosti, ki jih želimo izpostaviti
4. **Nastaviti prenos** - konfigurirati stdio komunikacijo
5. **Zagnati strežnik** - zagnati strežnik in obdelovati sporočila

Zgradimo to korak za korakom:

### Korak 1: Ustvarite osnovni stdio strežnik

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Nastavite beleženje
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ustvarite strežnik
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

Shrani kodo kot `server.py` in zaženi iz ukazne vrstice:

```bash
python server.py
```

Strežnik se bo zagnal in čakal na vhod iz stdin. Komunicira z uporabo JSON-RPC sporočil preko stdio prenosa.

### Korak 4: Testiranje z Inspektorjem

Strežnik lahko testirate z MCP Inspektorjem:

1. Namestite Inspektor: `npx @modelcontextprotocol/inspector`
2. Zaženite Inspektor in usmerite na vaš strežnik
3. Testirajte orodja, ki ste jih ustvarili

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Odpravljanje napak vašega stdio strežnika

### Uporaba MCP Inspektorja

MCP Inspektor je koristno orodje za odpravljanje napak in testiranje MCP strežnikov. Tako ga uporabite s stdio strežnikom:

1. **Namestite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Zaženite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte strežnik**: Inspektor nudi spletni vmesnik, kjer lahko:
   - Ogledate zmogljivosti strežnika
   - Testirate orodja z različnimi parametri
   - Spremljate JSON-RPC sporočila
   - Odpravljate težave s povezavo

### Uporaba VS Code

MCP strežnik lahko tudi neposredno odpravljate v Visual Studio Code:

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

2. Nastavite točke prekinitve v vaši kodi
3. Zaženite razhroščevalnik in testirajte z Inspektorjem

### Pogosti nasveti za odpravljanje napak

- Uporabljajte `stderr` za dnevniške zapise - nikoli ne pišite na `stdout`, ker je rezerviran za MCP sporočila
- Poskrbite, da so vsa JSON-RPC sporočila ločena z novimi vrsticami
- Najprej testirajte s preprostimi orodji, preden dodate kompleksno funkcionalnost
- Uporabljajte Inspektor za preverjanje oblik sporočil

## Uporaba vašega stdio strežnika v VS Code

Ko ustvarite MCP stdio strežnik, ga lahko integrirate z VS Code za uporabo s Claude ali drugimi MCP združljivimi klienti.

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
   - "Me lahko pozdraviš z orodjem za pozdrav?"
   - "Izračunaj vsoto 15 in 27"
   - "Kakšne so informacije o strežniku?"

### Primer TypeScript stdio strežnika

Tu je popoln TypeScript primer za referenco:

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

V tej posodobljeni lekciji ste se naučili:

- Graditi MCP strežnike z uporabo trenutnega **stdio prenosa** (priporočeni pristop)
- Razumeti, zakaj je bil SSE prenos ukinjen v korist stdio in Streamable HTTP
- Ustvariti orodja, ki jih lahko kličejo MCP klienti
- Odpravljati napake na strežniku z MCP Inspektorjem
- Integrirati stdio strežnik z VS Code in Claude

Prenos stdio omogoča preprostejši, varnejši in zmogljivejši način gradnje MCP strežnikov v primerjavi z ukinjenim pristopom SSE. Je priporočeni prenos za večino implementacij MCP strežnikov po specifikaciji 2025-06-18.


### .NET

1. Najprej ustvarimo nekaj orodij, za to bomo ustvarili datoteko *Tools.cs* z naslednjo vsebino:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vaja: Testiranje vašega stdio strežnika

Zdaj, ko ste zgradili stdio strežnik, ga preizkusimo, da preverimo, ali deluje pravilno.

### Predpogoji

1. Poskrbite, da imate nameščen MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Koda vašega strežnika je shranjena (npr. kot `server.py`)

### Testiranje z Inspektorjem

1. **Zaženite Inspektor z vašim strežnikom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Odprite spletni vmesnik**: Inspektor bo odprl brskalnik in prikazal zmogljivosti strežnika.

3. **Testirajte orodja**:
   - Preizkusite orodje `get_greeting` z različnimi imeni
   - Testirajte orodje `calculate_sum` z raznimi številkami
   - Pokličite orodje `get_server_info` za ogled metapodatkov strežnika

4. **Spremljajte komunikacijo**: Inspektor prikazuje JSON-RPC sporočila, ki se izmenjujejo med klientom in strežnikom.

### Kaj bi morali videti

Ko se strežnik pravilno zažene, bi morali videti:
- Zmogljivosti strežnika navedene v Inspektorju
- Orodja na voljo za testiranje
- Uspešno izmenjavo JSON-RPC sporočil
- Odzive orodij prikazane v vmesniku

### Pogoste težave in rešitve

**Strežnik se ne začne:**
- Preverite, da so vse odvisnosti nameščene: `pip install mcp`
- Preverite Python sintakso in zamike
- Poiščite sporočila o napakah v konzoli

**Orodja se ne pojavijo:**
- Preverite, da so prisotni dekoratorji `@server.tool()`
- Prepričajte se, da so funkcije orodij definirane pred `main()`
- Preverite pravilno konfiguracijo strežnika

**Težave s povezavo:**
- Prepričajte se, da strežnik pravilno uporablja stdio prenos
- Preverite, da noben drug proces ne moti komunikacije
- Preverite sintakso ukaza Inspektorja

## Naloga

Poskusite razširiti svoj strežnik z več zmogljivostmi. Oglejte si [to stran](https://api.chucknorris.io/), da na primer dodate orodje, ki kliče API. Vi odločite, kako naj strežnik izgleda. Zabavajte se :)
## Rešitev

[Rešitev](./solution/README.md) Tukaj je možna rešitev z delujočo kodo.

## Ključni poudarki

Ključne ugotovitve iz tega poglavja so:

- Prenos stdio je priporočen mehanizem za lokalne MCP strežnike.
- Prenos stdio omogoča nemoteno komunikacijo med MCP strežniki in klienti preko standardnih vhodnih in izhodnih tokov.
- Za uporabo stdio strežnikov lahko uporabljate tako Inspektor kot Visual Studio Code, kar poenostavi odpravljanje napak in integracijo.

## Vzorce

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python) 

## Dodatni viri

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kaj sledi

## Naslednji koraki

Zdaj, ko ste se naučili, kako graditi MCP strežnike s stdio prenosom, lahko raziščete naprednejše teme:

- **Naslednje**: [HTTP pretakanje z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Spoznajte drugi podprti prenosni mehanizem za oddaljene strežnike
- **Napredno**: [MCP varnostne najboljše prakse](../../02-Security/README.md) - Vzpostavite varnost v svojih MCP strežnikih
- **Produkcijsko**: [Strategije namestitve](../09-deployment/README.md) - Uvedite svoje strežnike v produkcijsko uporabo

## Dodatni viri

- [Specifikacija MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Uradna specifikacija
- [Dokumentacija MCP SDK](https://github.com/modelcontextprotocol/sdk) - SDK reference za vse jezike
- [Primeri skupnosti](../../06-CommunityContributions/README.md) - Več primerov strežnikov iz skupnosti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->