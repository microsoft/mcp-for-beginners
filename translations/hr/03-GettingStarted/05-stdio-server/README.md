# MCP poslužitelj sa stdio transportom

> **⚠️ Važna nadopuna**: Od specifikacije MCP 2025-06-18, samostalni SSE (Server-Sent Events) transport je **zastarjeli** i zamijenjen "Streamable HTTP" transportom. Trenutna MCP specifikacija definira dva primarna mehanizma transporta:
> 1. **stdio** - Standardni ulaz/izlaz (preporučeno za lokalne poslužitelje)
> 2. **Streamable HTTP** - Za udaljene poslužitelje koji mogu interno koristiti SSE
>
> Ova lekcija je ažurirana da se fokusira na **stdio transport**, što je preporučeni pristup za većinu implementacija MCP poslužitelja.

stdio transport omogućuje MCP poslužiteljima komunikaciju s klijentima putem standardnih ulaznih i izlaznih tokova. Ovo je najčešće korišten i preporučen mehanizam transporta u trenutnoj MCP specifikaciji, pružajući jednostavan i učinkovit način gradnje MCP poslužitelja koji se lako mogu integrirati s raznim klijentskim aplikacijama.

## Pregled

Ova lekcija pokriva kako izgraditi i koristiti MCP poslužitelje koristeći stdio transport.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Izgraditi MCP poslužitelj koristeći stdio transport.
- Otkloniti pogreške MCP poslužitelja koristeći Inspector.
- Koristiti MCP poslužitelj u Visual Studio Code-u.
- Razumjeti trenutačne mehanizme MCP transporta i zašto je stdio preporučen.

## stdio transport - Kako radi

stdio transport je jedan od dva podržana tipa transporta u trenutnoj MCP specifikaciji (2025-06-18). Evo kako radi:

- **Jednostavna komunikacija**: Poslužitelj čita JSON-RPC poruke sa standardnog ulaza (`stdin`) i šalje poruke na standardni izlaz (`stdout`).
- **Temeljeno na procesima**: Klijent pokreće MCP poslužitelj kao podproces.
- **Format poruka**: Poruke su pojedinačni JSON-RPC zahtjevi, notifikacije ili odgovori, razdvojeni novim redovima.
- **Logiranje**: Poslužitelj MOŽE zapisivati UTF-8 stringove na standardnu pogrešku (`stderr`) u svrhu logiranja.

### Ključni zahtjevi:
- Poruke MORAJU biti razdvojene novim redovima i NE SMIJU sadržavati ugrađene nove redove
- Poslužitelj NE SMIJE zapisivati ništa u `stdout` što nije važeća MCP poruka
- Klijent NE SMIJE zapisivati ništa u `stdin` poslužitelja što nije važeća MCP poruka

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

U prethodnom kodu:

- Uvozimo klasu `Server` i `StdioServerTransport` iz MCP SDK-a
- Kreiramo instancu poslužitelja s osnovnom konfiguracijom i mogućnostima
- Kreiramo instancu `StdioServerTransport` i povezujemo poslužitelj s njim, omogućujući komunikaciju preko stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Kreiraj instancu poslužitelja
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

U prethodnom kodu:

- Kreiramo instancu poslužitelja koristeći MCP SDK
- Definiramo alate koristeći dekoratore
- Koristimo stdio_server context manager za upravljanje transportom

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

Ključna razlika u odnosu na SSE je da stdio poslužitelji:

- Ne zahtijevaju postavljanje web poslužitelja niti HTTP krajnjih točaka
- Pokreću se kao podprocesi od strane klijenta
- Komuniciraju preko stdin/stdout tokova
- Jednostavniji su za implementaciju i otklanjanje pogrešaka

## Vježba: Kreiranje stdio poslužitelja

Za kreiranje našeg poslužitelja trebamo imati na umu dvije stvari:

- Potreban nam je web poslužitelj za izlaganje krajnjih točaka za povezivanje i poruke.

## Laboratorij: Kreiranje jednostavnog MCP stdio poslužitelja

U ovom laboratoriju napravit ćemo jednostavan MCP poslužitelj koristeći preporučeni stdio transport. Ovaj poslužitelj će izložiti alate koje klijenti mogu pozivati koristeći standardni Model Context Protocol.

### Preduvjeti

- Python 3.8 ili noviji
- MCP Python SDK: `pip install mcp`
- Osnovno razumijevanje asinhronog programiranja

Počnimo tako da kreiramo naš prvi MCP stdio poslužitelj:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfiguriraj zapisivanje događaja
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kreiraj poslužitelj
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
    # Koristi stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Ključne razlike u odnosu na zastarjeli SSE pristup

**Stdio transport (trenutni standard):**
- Jednostavan model podprocesa - klijent pokreće poslužitelj kao dijete procesa
- Komunikacija putem stdin/stdout koristeći JSON-RPC poruke
- Nema potrebe za postavljanjem HTTP poslužitelja
- Bolja izvedba i sigurnost
- Jednostavnije otklanjanje pogrešaka i razvoj

**SSE transport (zastarjeli od MCP 2025-06-18):**
- Zahtijevao HTTP poslužitelj s SSE krajnjim točkama
- Složenija postava s web server infrastrukturom
- Dodatne sigurnosne mjere za HTTP krajnje točke
- Sada zamijenjen Streamable HTTP-om za web scenarije

### Kreiranje poslužitelja sa stdio transportom

Za kreiranje našeg stdio poslužitelja potrebno je:

1. **Uvesti potrebne biblioteke** - Trebaju nam MCP server komponente i stdio transport
2. **Kreirati instancu poslužitelja** - Definirati poslužitelj sa njegovim mogućnostima
3. **Definirati alate** - Dodati funkcionalnosti koje želimo izložiti
4. **Postaviti transport** - Konfigurirati stdio komunikaciju
5. **Pokrenuti poslužitelj** - Pokrenuti poslužitelj i obraditi poruke

Krećemo korak po korak:

### Korak 1: Kreirajte osnovni stdio poslužitelj

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigurirajte zapisivanje dnevnika
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kreirajte poslužitelj
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

### Korak 2: Dodajte više alata

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

### Korak 3: Pokretanje poslužitelja

Spremite kod kao `server.py` i pokrenite ga iz komandne linije:

```bash
python server.py
```

Poslužitelj će se pokrenuti i čekat će unos iz stdin. Komunicira se koristeći JSON-RPC poruke preko stdio transporta.

### Korak 4: Testiranje sa Inspectorom

Možete testirati svoj poslužitelj koristeći MCP Inspector:

1. Instalirajte Inspector: `npx @modelcontextprotocol/inspector`
2. Pokrenite Inspector i usmjerite ga prema svom poslužitelju
3. Testirajte alate koje ste kreirali

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Otklanjanje pogrešaka vašeg stdio poslužitelja

### Korištenje MCP Inspectora

MCP Inspector je vrijedan alat za otklanjanje pogrešaka i testiranje MCP poslužitelja. Evo kako ga koristiti sa vašim stdio poslužiteljem:

1. **Instalirajte Inspectora**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pokrenite Inspectora**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte svoj poslužitelj**: Inspector pruža web sučelje gdje možete:
   - Pregledati mogućnosti poslužitelja
   - Testirati alate s različitim parametrima
   - Pratiti JSON-RPC poruke
   - Otkloniti probleme s povezivanjem

### Korištenje VS Code-a

Također možete otklanjati pogreške MCP poslužitelja direktno u VS Code-u:

1. Kreirajte konfiguraciju pokretanja u `.vscode/launch.json`:
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

2. Postavite prekide u kodu poslužitelja
3. Pokrenite debugger i testirajte s Inspectorom

### Uobičajeni savjeti za otklanjanje pogrešaka

- Koristite `stderr` za logiranje - nikada ne pišite u `stdout` jer je rezerviran za MCP poruke
- Osigurajte da su sve JSON-RPC poruke razdvojene novim redom
- Testirajte prvo s jednostavnim alatima prije dodavanja složenih funkcionalnosti
- Koristite Inspectora za provjeru formata poruka

## Korištenje vašeg stdio poslužitelja u VS Code-u

Nakon što izgradite svoj MCP stdio poslužitelj, možete ga integrirati s VS Code-om za korištenje s Claudeom ili drugim MCP-kompatibilnim klijentima.

### Konfiguracija

1. **Kreirajte MCP konfiguracijsku datoteku** na `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ili `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Ponovno pokrenite Claude**: Zatvorite i ponovno otvorite Claude da učitate novu konfiguraciju poslužitelja.

3. **Testirajte vezu**: Pokrenite razgovor s Claudeom i isprobajte alate vašeg poslužitelja:
   - "Možeš li me pozdraviti koristeći alat za pozdrav?"
   - "Izračunaj zbroj od 15 i 27"
   - "Koje su informacije o poslužitelju?"

### Primjer TypeScript stdio poslužitelja

Evo cjelovitog TypeScript primjera za referencu:

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

// Dodaj alate
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

### Primjer .NET stdio poslužitelja

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

## Sažetak

U ovoj ažuriranoj lekciji naučili ste kako:

- Izgraditi MCP poslužitelje koristeći trenutačni **stdio transport** (preporučeni pristup)
- Razumjeti zašto je SSE transport zastario u korist stdio i Streamable HTTP transporta
- Kreirati alate koje mogu pozivati MCP klijenti
- Otklanjati pogreške poslužitelja koristeći MCP Inspector
- Integrirati svoj stdio poslužitelj s VS Code-om i Claudeom

stdio transport pruža jednostavniji, sigurniji i učinkovitiji način gradnje MCP poslužitelja u odnosu na zastarjeli SSE pristup. To je preporučeni transport za većinu MCP implementacija poslužitelja od specifikacije 2025-06-18.

### .NET

1. Prvo kreirajmo neke alate, za to ćemo kreirati datoteku *Tools.cs* sa sljedećim sadržajem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vježba: Testiranje vašeg stdio poslužitelja

Sada kada ste izgradili svoj stdio poslužitelj, testirajmo ga da provjerimo radi li ispravno.

### Preduvjeti

1. Provjerite imate li instaliran MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaš kod poslužitelja treba biti spremljen (npr. kao `server.py`)

### Testiranje sa Inspectorom

1. **Pokrenite Inspectora sa svojim poslužiteljem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorite web sučelje**: Inspector će otvoriti prozor preglednika koji prikazuje mogućnosti vašeg poslužitelja.

3. **Testirajte alate**:
   - Isprobajte alat `get_greeting` sa različitim imenima
   - Testirajte alat `calculate_sum` s raznim brojevima
   - Pozovite alat `get_server_info` da vidite metapodatke poslužitelja

4. **Pratite komunikaciju**: Inspector prikazuje JSON-RPC poruke koje se razmjenjuju između klijenta i poslužitelja.

### Što biste trebali vidjeti

Kada se vaš poslužitelj ispravno pokrene, trebali biste vidjeti:
- Mogućnosti poslužitelja navedene u Inspectoru
- Alate dostupne za testiranje
- Uspješne razmjene JSON-RPC poruka
- Odgovore alata prikazane u sučelju

### Uobičajeni problemi i rješenja

**Poslužitelj se ne pokreće:**
- Provjerite jesu li sve ovisnosti instalirane: `pip install mcp`
- Provjerite Python sintaksu i uvlačenje
- Potražite poruke o pogreškama u konzoli

**Alati se ne pojavljuju:**
- Osigurajte da su prisutni dekoratori `@server.tool()`
- Provjerite jesu li funkcije alata definirane prije `main()`
- Provjerite je li poslužitelj ispravno konfiguriran

**Problemi s vezom:**
- Provjerite koristi li poslužitelj ispravno stdio transport
- Provjerite da drugi procesi ne ometaju komunikaciju
- Provjerite sintaksu naredbe Inspectora

## Zadatak

Pokušajte proširiti svoj poslužitelj s više mogućnosti. Pogledajte [ovu stranicu](https://api.chucknorris.io/) kako biste, na primjer, dodali alat koji poziva API. Vi odlučujete kako poslužitelj treba izgledati. Zabavite se :)

## Rješenje

[Rješenje](./solution/README.md) Evo mogućeg rješenja s radnim kodom.

## Ključne pouke

Ključne pouke iz ovog poglavlja su:

- stdio transport je preporučeni mehanizam za lokalne MCP poslužitelje.
- stdio transport omogućuje neometanu komunikaciju između MCP poslužitelja i klijenata koristeći standardne ulazne i izlazne tokove.
- Možete koristiti i Inspector i Visual Studio Code za direktnu potrošnju stdio poslužitelja, što olakšava otklanjanje pogrešaka i integraciju.

## Primjeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python)

## Dodatni resursi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Što dalje

## Sljedeći koraci

Sada kada znate kako izgraditi MCP poslužitelje sa stdio transportom, možete istražiti naprednije teme:

- **Sljedeće**: [HTTP Streaming s MCP-om (Streamable HTTP)](../06-http-streaming/README.md) - Naučite o drugom podržanom mehanizmu transporta za udaljene poslužitelje
- **Napredno**: [MCP sigurnosne najbolje prakse](../../02-Security/README.md) - Implementirajte sigurnost u svoje MCP poslužitelje
- **Proizvodnja**: [Strategije postavljanja](../09-deployment/README.md) - Postavite svoje poslužitelje za produkcijsku upotrebu

## Dodatni resursi

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Službena specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za sve jezike
- [Primjeri iz zajednice](../../06-CommunityContributions/README.md) - Više primjera poslužitelja iz zajednice

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakva nesporazuma ili krive interpretacije nastale uporabom ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->