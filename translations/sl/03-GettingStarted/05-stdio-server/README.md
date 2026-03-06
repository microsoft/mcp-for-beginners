# MCP Strežnik s stdio transportom

> **⚠️ Pomembna posodobitev**: Od MCP specifikacije 2025-06-18 je samostojni SSE (Server-Sent Events) transport **zastarel** in nadomeščen s transportom "Streamable HTTP". Trenutna MCP specifikacija opredeljuje dva glavna transportna mehanizma:
> 1. **stdio** - Standardni vhod/izhod (priporočeno za lokalne strežnike)
> 2. **Streamable HTTP** - Za oddaljene strežnike, ki lahko interno uporabljajo SSE
> 
> Ta lekcija je posodobljena tako, da se osredotoča na **stdio transport**, ki je priporočeni pristop za večino implementacij MCP strežnikov.

stdio transport omogoča MCP strežnikom komunikacijo s klienti prek standardnih vhodnih in izhodnih tokov. To je najpogosteje uporabljen in priporočen transportni mehanizem v trenutni MCP specifikaciji, ki zagotavlja enostaven in učinkovit način za izgradnjo MCP strežnikov, ki jih lahko enostavno integriramo z različnimi klientskimi aplikacijami.

## Pregled

Ta lekcija pokriva, kako zgraditi in uporabljati MCP strežnike z uporabo stdio transporta.

## Cilji učenja

Ob koncu te lekcije boste znali:

- Zgraditi MCP strežnik z uporabo stdio transporta.
- Odpravljati napake MCP strežnika z uporabo Inspectorja.
- Uporabljati MCP strežnik v Visual Studio Code.
- Razumeti trenutne MCP transportne mehanizme in zakaj je stdio priporočeno.

## stdio transport - kako deluje

stdio transport je eden izmed dveh podprtih transportnih tipov v trenutni MCP specifikaciji (2025-06-18). Tako deluje:

- **Preprosta komunikacija**: strežnik prebere JSON-RPC sporočila iz standardnega vhoda (`stdin`) in pošlje sporočila na standardni izhod (`stdout`).
- **Na osnovi procesa**: klient zažene MCP strežnik kot podproces.
- **Format sporočil**: sporočila so posamezni JSON-RPC zahtevki, obvestila ali odgovori, ločeni z novimi vrsticami.
- **Zapisovanje**: strežnik LAHKO zapisuje UTF-8 nize na standardni izhod za napake (`stderr`) za namene zapisovanja dnevnikov.

### Ključne zahteve:
- Sporočila MORAJO biti ločena z novimi vrsticami in NE SMEJO vsebovati vgrajenih novih vrstic
- Strežnik NE SME pisati ničesar na `stdout`, kar ni veljavno MCP sporočilo
- Klient NE SME pisati ničesar na strežnikov `stdin`, kar ni veljavno MCP sporočilo

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

- Uvozimo razred `Server` in `StdioServerTransport` iz MCP SDK
- Ustvarimo instanco strežnika z osnovno konfiguracijo in zmogljivostmi

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
- Definiramo orodja z dekoratorji
- Uporabimo stdio_server kontekstni upravljalec za upravljanje transporta

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

- Ne potrebujejo nastavitev spletnega strežnika ali HTTP končnih točk
- Se zaženejo kot podprocesi s strani klienta
- Komunicirajo preko stdin/stdout tokov
- So enostavnejši za implementacijo in odpravljanje napak

## Vadba: Ustvarjanje stdio strežnika

Da ustvarimo naš strežnik, moramo upoštevati dve stvari:

- Potrebujemo spletni strežnik za izpostavitev končnih točk za povezave in sporočila.

## Laboratorij: Ustvarjanje enostavnega MCP stdio strežnika

V tem laboratoriju bomo ustvarili enostaven MCP strežnik z uporabo priporočenega stdio transporta. Ta strežnik bo izpostavil orodja, ki jih lahko kličemo z uporabo standardnega Model Context Protocola.

### Predpogoji

- Python 3.8 ali novejši
- MCP Python SDK: `pip install mcp`
- Osnovno razumevanje asinhronega programiranja

Začnimo z ustvarjanjem prvega MCP stdio strežnika:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Nastavite beleženje
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ustvarite strežnik
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
    # Uporabite stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ključne razlike glede na zastareli SSE pristop

**Stdio transport (trenutni standard):**
- Preprost model podprocesa - klient zažene strežnik kot otroški proces
- Komunikacija preko stdin/stdout z JSON-RPC sporočili
- Ni potrebe po nastavku HTTP strežnika
- Boljša zmogljivost in varnost
- Lažje odkrivanje napak in razvoj

**SSE transport (zastarel od MCP 2025-06-18):**
- Zahteva HTTP strežnik s SSE končnimi točkami
- Kompleksnejša nastavitev s spletno infrastrukturo
- Dodatni varnostni vidiki za HTTP končne točke
- Zamenjan z Streamable HTTP za spletne scenarije

### Ustvarjanje strežnika z stdio transportom

Za ustvarjanje našega stdio strežnika moramo:

1. **Uvoziti potrebne knjižnice** - potrebujemo MCP strežniške komponente in stdio transport
2. **Ustvariti instanco strežnika** - opredeliti strežnik z njegovimi zmogljivostmi
3. **Definirati orodja** - dodati funkcionalnost, ki jo želimo izpostaviti
4. **Nastaviti transport** - konfigurirati stdio komunikacijo
5. **Zagnati strežnik** - zagnati strežnik in obdelovati sporočila

Gradimo to korak za korakom:

### Korak 1: Ustvaritev osnovnega stdio strežnika

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

### Korak 2: Dodaj več orodij

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

Strežnik se bo zagnal in čakal na vhod iz stdin. Komunicira z uporabo JSON-RPC sporočil preko stdio transporta.

### Korak 4: Testiranje z Inspectorjem

Strežnik lahko preizkusiš z MCP Inspectorjem:

1. Namesti Inspector: `npx @modelcontextprotocol/inspector`
2. Zaženi Inspector in nastavi povezavo na svoj strežnik
3. Testiraj orodja, ki si jih ustvaril

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Odpravljanje napak tvojega stdio strežnika

### Uporaba MCP Inspectorja

MCP Inspector je dragoceno orodje za odpravljanje napak in testiranje MCP strežnikov. Tako ga uporabiš s svojim stdio strežnikom:

1. **Namesti Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Zaženi Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testiraj strežnik**: Inspector ponuja spletni vmesnik, kjer lahko:
   - Ogledaš zmogljivosti strežnika
   - Testiraš orodja z različnimi parametri
   - Spremljaš JSON-RPC sporočila
   - Odpravljaš težave s povezavo

### Uporaba VS Code

MCP strežnik lahko tudi odpraviš neposredno v VS Code:

1. Ustvari konfiguracijo zagona v `.vscode/launch.json`:
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

2. Nastavi točke prekinitve v kodi strežnika
3. Zaženi razhroščevalnik in testiraj z Inspectorjem

### Pogosti nasveti za odpravljanje napak

- Uporabljaj `stderr` za zapisovanje dnevnikov - nikoli ne piši na `stdout`, ker je namenjen MCP sporočilom
- Poskrbi, da so vsa JSON-RPC sporočila ločena z novo vrstico
- Najprej testiraj s preprostimi orodji pred dodajanjem kompleksne funkcionalnosti
- Uporabi Inspector za preverjanje formatov sporočil

## Uporaba tvojega stdio strežnika v VS Code

Ko zgradiš MCP stdio strežnik, ga lahko integriraš z VS Code, da ga uporabljaš s Claude ali drugimi MCP združljivimi klienti.

### Konfiguracija

1. **Ustvari konfiguracijsko datoteko MCP** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ali `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Znova zaženi Claude**: Zapri in ponovno odpri Claude, da naloži novo konfiguracijo strežnika.

3. **Preizkusi povezavo**: Začni pogovor s Claudom in poskusi uporabiti orodja svojega strežnika:
   - "Ali me lahko pozdraviš z orodjem za pozdrav?"
   - "Izračunaj vsoto 15 in 27"
   - "Kakšne so informacije o strežniku?"

### Primer TypeScript stdio strežnika

Tu je popoln primer v TypeScriptu za referenco:

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

- Graditi MCP strežnike z uporabo trenutnega **stdio transporta** (priporočeni pristop)
- Razumeti, zakaj je bil SSE transport zastarel v prid stdio in Streamable HTTP
- Ustvarjati orodja, ki jih lahko kličejo MCP klienti
- Odpravljati napake strežnika z MCP Inspectorjem
- Integrirati stdio strežnik z VS Code in Claude

stdio transport zagotavlja preprostejši, bolj varen in zmogljiv način za gradnjo MCP strežnikov v primerjavi z zastarelim SSE pristopom. Je priporočen transport za večino MCP strežniških implementacij glede na specifikacijo 2025-06-18.

### .NET

1. Najprej ustvarimo nekaj orodij, za to bomo ustvarili datoteko *Tools.cs* z naslednjo vsebino:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vadba: Testiranje tvojega stdio strežnika

Zdaj, ko si zgradil svoj stdio strežnik, ga preizkusimo, da zagotovimo pravilno delovanje.

### Predpogoji

1. Poskrbi, da imaš nameščen MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Tvoja koda strežnika mora biti shranjena (npr. kot `server.py`)

### Testiranje z Inspectorjem

1. **Zaženi Inspector s svojim strežnikom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Odpri spletni vmesnik**: Inspector bo odprl brskalnik s prikazom zmogljivosti tvojega strežnika.

3. **Testiraj orodja**:
   - Preizkusi orodje `get_greeting` z različnimi imeni
   - Testiraj orodje `calculate_sum` z različnimi številkami
   - Pokliči orodje `get_server_info`, da vidiš informacije o strežniku

4. **Nadzoruj komunikacijo**: Inspector prikazuje JSON-RPC sporočila, ki se izmenjujejo med klientom in strežnikom.

### Kaj bi moral videti

Ko se strežnik začne pravilno, bi moral videti:
- Zmogljivosti strežnika naštete v Inspectorju
- Orodja na voljo za testiranje
- Uspešne izmenjave JSON-RPC sporočil
- Odgovore orodij prikazane v vmesniku

### Pogoste težave in rešitve

**Strežnik se ne zažene:**
- Preveri, da so vse odvisnosti nameščene: `pip install mcp`
- Preveri sintakso in zamike v Python kodi
- Preveri sporočila o napakah v konzoli

**Orodja se ne prikažejo:**
- Poskrbi, da so prisotni dekoratorji `@server.tool()`
- Preveri, da so funkcije orodij definirane pred `main()`
- Preveri, da je strežnik pravilno konfiguriran

**Težave s povezavo:**
- Prepričaj se, da strežnik pravilno uporablja stdio transport
- Preveri, da nobeni drugi procesi ne posegajo
- Preveri sintakso ukaza Inspectorja

## Naloga

Poskusi razširiti svoj strežnik z več funkcionalnostmi. Glej [to stran](https://api.chucknorris.io/), da na primer dodaš orodje, ki kliče API. Odloči se, kako želiš, da strežnik izgleda. Zabavaj se :)

## Rešitev

[Rešitev](./solution/README.md) Tukaj je možna rešitev z delujočo kodo.

## Ključne ugotovitve

Ključne ugotovitve iz tega poglavja so naslednje:

- stdio transport je priporočeni mehanizem za lokalne MCP strežnike.
- stdio transport omogoča nemoteno komunikacijo med MCP strežniki in klienti prek standardnih vhodnih in izhodnih tokov.
- Lahko uporabljaš tako Inspector kot Visual Studio Code za neposredno uporabo stdio strežnikov, kar omogoča enostavno odpravljanje napak in integracijo.

## Vzorci

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)

## Dodatni viri

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kaj je naslednje

## Naslednji koraki

Ko si se naučil, kako graditi MCP strežnike s stdio transportom, lahko raziščeš naprednejše teme:

- **Naslednje**: [HTTP Streaming z MCP (Streamable HTTP)](../06-http-streaming/README.md) - Spoznaj drugega podprtega transportnega mehanizma za oddaljene strežnike
- **Napredno**: [MCP varnostne dobre prakse](../../02-Security/README.md) - Implementiraj varnost v svojih MCP strežnikih
- **Proizvodnja**: [Strategije uvajanja](../09-deployment/README.md) - Namesti svoje strežnike za produkcijsko uporabo

## Dodatni viri

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Uradna specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za vse jezike
- [Primeri skupnosti](../../06-CommunityContributions/README.md) - Več primerov strežnikov iz skupnosti

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Opozorilo**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba šteti za avtoritativni vir. Za kritične informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->