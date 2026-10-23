# MCP poslužitelj sa stdio Transportom

> **⚠️ Važna obavijest**: Od MCP specifikacije 2025-06-18, samostalni SSE (Server-Sent Events) transport je **zastarjelo** i zamijenjen je "Streamable HTTP" transportom. Trenutna MCP specifikacija definira dva glavna mehanizma prijenosa:
> 1. **stdio** - Standardni ulaz/izlaz (preporučeno za lokalne poslužitelje)
> 2. **Streamable HTTP** - Za udaljene poslužitelje koji mogu koristiti SSE interno
>
> Ova lekcija je ažurirana da se fokusira na **stdio transport**, koji je preporučeni pristup za većinu MCP implementacija poslužitelja.

stdio transport omogućuje MCP poslužiteljima komunikaciju s klijentima putem standardnih ulaznih i izlaznih tokova. Ovo je najčešće korišteni i preporučeni mehanizam prijenosa u trenutnoj MCP specifikaciji, pružajući jednostavan i učinkovit način za izgradnju MCP poslužitelja koji se lako mogu integrirati s različitim klijentskim aplikacijama.

## Pregled

Ova lekcija obuhvaća kako izgraditi i koristiti MCP poslužitelje koristeći stdio transport.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Izgraditi MCP poslužitelj koristeći stdio transport.
- Debugirati MCP poslužitelj koristeći Inspektora.
- Koristiti MCP poslužitelj putem Visual Studio Code-a.
- Razumjeti trenutne mehanizme prijenosa MCP-a i zašto je stdio preporučeno.


## stdio Transport - Kako radi

stdio transport je jedan od dva standardna transporta u MCP specifikaciji
`2026-07-28`. Ovako radi:

- **Jednostavna komunikacija**: Poslužitelj čita JSON-RPC poruke sa standardnog ulaza (`stdin`) i šalje poruke na standardni izlaz (`stdout`).
- **Bazirano na procesu**: Klijent pokreće MCP poslužitelj kao podproces.
- **Format poruka**: Poruke su pojedinačni JSON-RPC zahtjevi, obavijesti ili odgovori, razdvojeni novim redovima.
- **Zapisivanje logova**: Poslužitelj MOŽE pisati UTF-8 stringove na standardnu grešku (`stderr`) za potrebe zapisivanja logova.

### Ključni zahtjevi:
- Poruke MORAJU biti razdvojene novim redovima i NE SMIJU sadržavati ugrađene nove redove
- Poslužitelj NE SMIJE pisati ništa na `stdout` što nije valjana MCP poruka
- Klijent NE SMIJE pisati ništa na poslužiteljev `stdin` što nije valjana MCP poruka

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
- Kreiramo instancu `StdioServerTransport` i povezujemo poslužitelj s njom, omogućujući komunikaciju preko stdin/stdout

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

U prethodnom kodu mi:

- Kreiramo instancu poslužitelja koristeći MCP SDK
- Definiramo alate koristeći dekoratore
- Koristimo stdio_server kontekst menadžera za upravljanje transportom

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

- Ne zahtijevaju postavljanje web poslužitelja ili HTTP endpoint-a
- Pokreću se kao podprocesi od strane klijenta
- Komuniciraju kroz stdin/stdout tokove
- Jednostavniji su za implementaciju i otklanjanje poteškoća

## Vježba: Kreiranje stdio poslužitelja

Da bismo kreirali naš poslužitelj, trebamo imati na umu dvije stvari:

- Trebamo koristiti web poslužitelj za izlaganje endpointa za vezu i poruke.
## Laboratorij: Kreiranje jednostavnog MCP stdio poslužitelja

U ovom laboratoriju kreirat ćemo jednostavan MCP poslužitelj koristeći preporučeni stdio transport. Ovaj poslužitelj će izlagati alate koje klijenti mogu pozivati koristeći standardni Model Context Protocol.

### Preduvjeti

- Python 3.8 ili noviji
- MCP Python SDK: `pip install mcp`
- Osnovno razumijevanje asinhronog programiranja

Krenimo s kreiranjem našeg prvog MCP stdio poslužitelja:

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

## Ključne razlike od zastarjelog SSE pristupa

**Stdio Transport (trenutni standard):**
- Jednostavan model podprocesa - klijent pokreće poslužitelj kao podsistem
- Komunikacija putem stdin/stdout koristeći JSON-RPC poruke
- Nije potrebno postavljanje HTTP poslužitelja
- Bolja performansa i sigurnost
- Jednostavnije otklanjanje poteškoća i razvoj

**SSE Transport (zastarjelo od MCP 2025-06-18):**
- Potreban je HTTP poslužitelj s SSE endpointima
- Složenija postavka s infrastrukturom web poslužitelja
- Dodatna sigurnosna razmatranja za HTTP endpoint-e
- Sada zamijenjen Streamable HTTP-om za scenarije zasnovane na webu

### Kreiranje poslužitelja sa stdio transportom

Da bismo kreirali naš stdio poslužitelj, trebamo:

1. **Uvesti potrebne biblioteke** - Trebaju nam MCP poslužiteljski dijelovi i stdio transport
2. **Kreirati instancu poslužitelja** - Definirati poslužitelj s njegovim mogućnostima
3. **Definirati alate** - Dodati funkcionalnosti koje želimo izložiti
4. **Postaviti transport** - Konfigurirati stdio komunikaciju
5. **Pokrenuti poslužitelj** - Pokrenuti poslužitelj i obrađivati poruke

Gradimo ovo korak po korak:

### Korak 1: Kreirajte osnovni stdio poslužitelj

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

Spremite kod kao `server.py` i pokrenite ga iz naredbene linije:

```bash
python server.py
```

Poslužitelj će se pokrenuti i čekati ulaz s stdin-a. Komunicira koristeći JSON-RPC poruke preko stdio transporta.

### Korak 4: Testiranje s Inspektorom

Možete testirati svoj poslužitelj koristeći MCP Inspektor:

1. Instalirajte Inspektora: `npx @modelcontextprotocol/inspector`
2. Pokrenite Inspektora i usmjerite ga na svoj poslužitelj
3. Testirajte alate koje ste kreirali

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Otklanjanje poteškoća na vašem stdio poslužitelju

### Korištenje MCP Inspektora

MCP Inspektor je vrijedan alat za otklanjanje poteškoća i testiranje MCP poslužitelja. Evo kako ga koristiti s vašim stdio poslužiteljem:

1. **Instalirajte Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pokrenite Inspektora**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte poslužitelj**: Inspektor pruža web sučelje gdje možete:
   - Pregledati mogućnosti poslužitelja
   - Testirati alate s različitim parametrima
   - Pratiti JSON-RPC poruke
   - Otklanjati probleme s vezom

### Korištenje VS Code-a

Također možete otklanjati poteškoće MCP poslužitelja direktno u VS Code-u:

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

2. Postavite točke prekida u vašem kodu poslužitelja
3. Pokrenite debugger i testirajte s Inspektorom

### Uobičajeni savjeti za otklanjanje poteškoća

- Koristite `stderr` za zapisivanje logova - nikada nemojte pisati u `stdout` jer je rezervirano za MCP poruke
- Osigurajte da su sve JSON-RPC poruke razdvojene novim redom
- Najprije testirajte jednostavne alate prije dodavanja složenijih funkcionalnosti
- Koristite Inspektor za provjeru formata poruka

## Korištenje vašeg stdio poslužitelja u VS Code-u

Nakon što ste izgradili svoj MCP stdio poslužitelj, možete ga integrirati s VS Code-om da ga koristite s Claude ili drugim MCP-kompatibilnim klijentima.

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

2. **Ponovno pokrenite Claude**: Zatvorite i ponovno otvorite Claude da biste učitali novu konfiguraciju poslužitelja.

3. **Testirajte vezu**: Započnite razgovor s Claude-om i pokušajte koristiti alate vašeg poslužitelja:
   - "Možeš li me pozdraviti koristeći alat za pozdrav?"
   - "Izračunaj zbroj 15 i 27"
   - "Koje su informacije o poslužitelju?"

### Primjer TypeScript stdio poslužitelja

Evo kompletnog primjera u TypeScriptu za referencu:

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

- Izgraditi MCP poslužitelje koristeći trenutni **stdio transport** (preporučeni pristup)
- Razumjeti zašto je SSE transport zastario u korist stdio i Streamable HTTP
- Kreirati alate koje MCP klijenti mogu pozivati
- Otklanjati poteškoće na poslužitelju koristeći MCP Inspektor
- Integrirati vaš stdio poslužitelj s VS Code i Claude

stdio transport pruža jednostavniji, sigurniji i učinkovitiji način za izgradnju MCP poslužitelja u odnosu na zastarjeli SSE pristup. To je preporučeni transport za većinu MCP poslužiteljskih implementacija prema specifikaciji od 2025-06-18.


### .NET

1. Prvo ćemo kreirati neke alate, za to ćemo napraviti datoteku *Tools.cs* sa sljedećim sadržajem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vježba: Testiranje vašeg stdio poslužitelja

Sada kada ste izgradili svoj stdio poslužitelj, testirajmo ga da bismo bili sigurni da radi ispravno.

### Preduvjeti

1. Provjerite imate li instaliran MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaš kod poslužitelja treba biti spremljen (npr. kao `server.py`)

### Testiranje s Inspektorom

1. **Pokrenite Inspektora s vašim poslužiteljem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorite web sučelje**: Inspektor će otvoriti preglednik s prikazom mogućnosti vašeg poslužitelja.

3. **Testirajte alate**:
   - Isprobajte alat `get_greeting` s različitim imenima
   - Testirajte alat `calculate_sum` s različitim brojevima
   - Pozovite alat `get_server_info` da vidite metapodatke poslužitelja

4. **Pratite komunikaciju**: Inspektor prikazuje JSON-RPC poruke koje se razmjenjuju između klijenta i poslužitelja.

### Što biste trebali vidjeti

Kada se vaš poslužitelj pravilno pokrene, trebali biste vidjeti:
- Mogućnosti poslužitelja prikazane u Inspektoru
- Alate dostupne za testiranje
- Uspješne razmjene JSON-RPC poruka
- Odgovori alata prikazani u sučelju

### Uobičajeni problemi i rješenja

**Poslužitelj se neće pokrenuti:**
- Provjerite jesu li sve ovisnosti instalirane: `pip install mcp`
- Provjerite Python sintaksu i uvlačenje
- Tražite poruke o pogreškama u konzoli

**Alati se ne pojavljuju:**
- Provjerite jesu li dekoratori `@server.tool()` prisutni
- Provjerite jesu li funkcije alata definirane prije `main()`
- Provjerite da je poslužitelj ispravno konfiguriran

**Problemi s vezom:**
- Provjerite koristi li se stdio transport ispravno
- Provjerite da drugi procesi ne ometaju proces
- Provjerite sintaksu naredbe Inspektora

## Zadatak

Pokušajte proširiti svoj poslužitelj s više mogućnosti. Pogledajte [ovu stranicu](https://api.chucknorris.io/) kako biste, na primjer, dodali alat koji poziva API. Vi odlučujete kako bi poslužitelj trebao izgledati. Zabavite se :)
## Rješenje

[Rješenje](./solution/README.md) Evo jednog mogućeg rješenja s ispravnim kodom.

## Ključne poruke

Ključne poruke ovog poglavlja su sljedeće:

- stdio transport je preporučeni mehanizam za lokalne MCP poslužitelje.
- stdio transport omogućuje neprimjetnu komunikaciju između MCP poslužitelja i klijenata preko standardnih ulaza i izlaza.
- Možete koristiti i Inspektor i Visual Studio Code za direktno korištenje stdio poslužitelja, što omogućava jednostavno otklanjanje poteškoća i integraciju.

## Primjeri 

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.NET Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python) 

## Dodatni resursi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Što slijedi

## Sljedeći koraci

Sada kada znate kako izgraditi MCP poslužitelje sa stdio transportom, možete istražiti naprednije teme:

- **Sljedeće**: [HTTP Streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučite o drugom podržanom mehanizmu transporta za udaljene poslužitelje
- **Napredno**: [Najbolje prakse MCP sigurnosti](../../02-Security/README.md) - Implementirajte sigurnost u svojim MCP poslužiteljima
- **Proizvodnja**: [Strategije implementacije](../09-deployment/README.md) - Implementirajte svoje poslužitelje za produkcijsku upotrebu

## Dodatni resursi

- [MCP Specifikacija 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutna specifikacija
- [Dokumentacija MCP SDK](https://github.com/modelcontextprotocol/sdk) - SDK reference za sve jezike
- [Primjeri zajednice](../../06-CommunityContributions/README.md) - Još primjera poslužitelja iz zajednice

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->