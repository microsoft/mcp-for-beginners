# MCP poslužitelj sa stdio transportom

> **⚠️ Važna obavijest**: Od MCP specifikacije 2025-06-18, samostalni SSE (Server-Sent Events) transport je **zastarjeli** i zamijenjen "Streamable HTTP" transportom. Trenutna MCP specifikacija definira dva osnovna transportna mehanizma:
> 1. **stdio** - Standardni ulaz/izlaz (preporučeno za lokalne poslužitelje)
> 2. **Streamable HTTP** - Za udaljene poslužitelje koji mogu interno koristiti SSE
>
> Ova lekcija je ažurirana da se fokusira na **stdio transport**, koji je preporučeni pristup za većinu implementacija MCP poslužitelja.

Stdio transport omogućava MCP poslužiteljima komunikaciju s klijentima putem standardnih ulaznih i izlaznih tokova. To je najčešće korišten i preporučeni transportni mehanizam u trenutnoj MCP specifikaciji, pružajući jednostavan i učinkovit način za izgradnju MCP poslužitelja koji se lako mogu integrirati s raznim klijentskim aplikacijama.

## Pregled

Ova lekcija obuhvaća kako izgraditi i koristiti MCP poslužitelje koristeći stdio transport.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Izgraditi MCP poslužitelj koristeći stdio transport.
- Otkloniti pogreške MCP poslužitelja koristeći Inspektor.
- Koristiti MCP poslužitelj u Visual Studio Code.
- Razumjeti trenutne MCP transportne mehanizme i zašto je stdio preporučen.


## stdio Transport - Kako radi

Stdio transport je jedan od dva standardna transporta u MCP specifikaciji
`2026-07-28`. Evo kako radi:

- **Jednostavna komunikacija**: Poslužitelj čita JSON-RPC poruke sa standardnog ulaza (`stdin`) i šalje poruke na standardni izlaz (`stdout`).
- **Temeljeno na procesu**: Klijent pokreće MCP poslužitelj kao podproces.
- **Format poruke**: Poruke su pojedinačni JSON-RPC zahtjevi, notifikacije ili odgovori, odvojeni novim redovima.
- **Logiranje**: Poslužitelj MOŽE pisati UTF-8 stringove na standardnu grešku (`stderr`) za potrebe logiranja.

### Ključni uvjeti:
- Poruke MORAJU biti odvojene novim redovima i NE SMIJU sadržavati ugrađene nove redove
- Poslužitelj NE SMIJE pisati ništa na `stdout` što nije valjana MCP poruka
- Klijent NE SMIJE pisati ništa u poslužiteljev `stdin` što nije valjana MCP poruka

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

- Uvozimo `Server` klasu i `StdioServerTransport` iz MCP SDK-a
- Kreiramo instancu poslužitelja s osnovnom konfiguracijom i mogućnostima
- Kreiramo instancu `StdioServerTransport` i povezujemo poslužitelja s njim, omogućujući komunikaciju preko stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Kreiraj instancu servera
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
- Koristimo stdio_server kontekstni menadžer za upravljanje transportom

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

Ključna razlika od SSE-a je u tome da stdio poslužitelji:

- Ne zahtijevaju postavljanje web poslužitelja ni HTTP endpointa
- Pokreću se kao podprocesi od strane klijenta
- Komuniciraju preko stdin/stdout tokova
- Jednostavniji su za implementaciju i otklanjanje pogrešaka

## Vježba: Kreiranje stdio poslužitelja

Za kreiranje našeg poslužitelja, moramo imati na umu dvije stvari:

- Trebamo koristiti web poslužitelj da izložimo endpointove za vezu i poruke.
## Laboratorij: Kreiranje jednostavnog MCP stdio poslužitelja

U ovom laboratoriju ćemo kreirati jednostavan MCP poslužitelj koristeći preporučeni stdio transport. Ovaj poslužitelj će izložiti alate koje klijenti mogu pozivati koristeći standardni Model Context Protocol.

### Preduvjeti

- Python 3.8 ili noviji
- MCP Python SDK: `pip install mcp`
- Osnovno razumijevanje asinhronog programiranja

Počnimo s kreiranjem našeg prvog MCP stdio poslužitelja:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfiguriraj zapisivanje dnevnika
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
- Jednostavan model podprocesa - klijent pokreće poslužitelj kao dječji proces
- Komunikacija preko stdin/stdout koristeći JSON-RPC poruke
- Nije potrebno postavljanje HTTP poslužitelja
- Bolje performanse i sigurnost
- Lakše otklanjanje pogrešaka i razvoj

**SSE transport (zastarjelo od MCP 2025-06-18):**
- Potreban HTTP poslužitelj s SSE endpointima
- Složenija konfiguracija s web poslužiteljskom infrastrukturom
- Dodatni sigurnosni izazovi za HTTP endpointove
- Sada zamijenjeno Streamable HTTP-om za web-scenarije

### Kreiranje poslužitelja sa stdio transportom

Za kreiranje našeg stdio poslužitelja, trebamo:

1. **Uvesti potrebne biblioteke** - Trebamo MCP poslužiteljske komponente i stdio transport
2. **Kreirati instancu poslužitelja** - Definirati poslužitelj s njegovim sposobnostima
3. **Definirati alate** - Dodati funkcionalnosti koje želimo izložiti
4. **Postaviti transport** - Konfigurirati stdio komunikaciju
5. **Pokrenuti poslužitelj** - Startati poslužitelj i obrađivati poruke

Izgradimo ovo korak po korak:

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

Poslužitelj će se pokrenuti i čekati unos s stdin. Komunicira koristeći JSON-RPC poruke preko stdio transporta.

### Korak 4: Testiranje s Inspektorom

Možete testirati svoj poslužitelj koristeći MCP Inspektor:

1. Instalirajte Inspektor: `npx @modelcontextprotocol/inspector`
2. Pokrenite Inspektor i usmjerite ga na svoj poslužitelj
3. Testirajte alate koje ste kreirali

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Otklanjanje pogrešaka vašeg stdio poslužitelja

### Korištenje MCP Inspektora

MCP Inspektor je vrijedan alat za otklanjanje pogrešaka i testiranje MCP poslužitelja. Evo kako ga koristiti sa svojim stdio poslužiteljem:

1. **Instalirajte Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pokrenite Inspektor**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte svoj poslužitelj**: Inspektor pruža web sučelje gdje možete:
   - Pregledati sposobnosti poslužitelja
   - Testirati alate s različitim parametrima
   - Pratiti JSON-RPC poruke
   - Otklanjati probleme s vezom

### Korištenje VS Code

Također možete otklanjati pogreške vašeg MCP poslužitelja direktno u VS Code:

1. Kreirajte konfiguraciju za pokretanje u `.vscode/launch.json`:
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

2. Postavite točke za prekid u svom kodu poslužitelja
3. Pokrenite otklanjanje pogrešaka i testirajte s Inspektorom

### Česti savjeti za otklanjanje pogrešaka

- Koristite `stderr` za logiranje - nikada ne pišite na `stdout` jer je rezerviran za MCP poruke
- Osigurajte da su sve JSON-RPC poruke odvojene novim redovima
- Prvo testirajte jednostavne alate prije dodavanja kompleksne funkcionalnosti
- Koristite Inspektor za provjeru formata poruka

## Korištenje vašeg stdio poslužitelja u VS Code

Nakon što ste izgradili svoj MCP stdio poslužitelj, možete ga integrirati s VS Code za korištenje s Claude-om ili drugim MCP-kompatibilnim klijentima.

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

2. **Restartajte Claude**: Zatvorite i ponovno otvorite Claude kako bi se učitala nova konfiguracija poslužitelja.

3. **Testirajte vezu**: Započnite razgovor s Claude-om i pokušajte koristiti alate vašeg poslužitelja:
   - "Možeš li me pozdraviti koristeći alat za pozdrav?"
   - "Izračunaj zbroj 15 i 27"
   - "Koje su informacije o poslužitelju?"

### Primjer stdio poslužitelja u TypeScriptu

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

### Primjer stdio poslužitelja u .NET

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
- Otkloniti pogreške vašeg poslužitelja koristeći MCP Inspektor
- Integrirati vaš stdio poslužitelj s VS Code i Claude-om

Stdio transport pruža jednostavniji, sigurniji i efikasniji način za izgradnju MCP poslužitelja u usporedbi s zastarjelim SSE pristupom. To je preporučeni transport za većinu MCP implementacija od specifikacije 2025-06-18.


### .NET

1. Prvo ćemo kreirati neke alate, za to ćemo kreirati datoteku *Tools.cs* sa sljedećim sadržajem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vježba: Testiranje vašeg stdio poslužitelja

Sada kada ste kreirali svoj stdio poslužitelj, testirat ćemo ga kako bismo provjerili da radi ispravno.

### Preduvjeti

1. Provjerite imate li instaliran MCP Inspektor:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaš kod poslužitelja treba biti spremljen (npr. kao `server.py`)

### Testiranje s Inspektorom

1. **Pokrenite Inspektor s vašim poslužiteljem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorite web sučelje**: Inspektor će otvoriti preglednik koji prikazuje sposobnosti vašeg poslužitelja.

3. **Testirajte alate**: 
   - Isprobajte alat `get_greeting` s različitim imenima
   - Testirajte alat `calculate_sum` s različitim brojevima
   - Pozovite alat `get_server_info` da vidite metapodatke poslužitelja

4. **Pratite komunikaciju**: Inspektor prikazuje JSON-RPC poruke koje se razmjenjuju između klijenta i poslužitelja.

### Što biste trebali vidjeti

Kada se vaš poslužitelj ispravno pokrene, trebali biste vidjeti:
- Sposobnosti poslužitelja navedene u Inspektoru
- Alate dostupne za testiranje
- Uspješne razmjene JSON-RPC poruka
- Prikaz odgovora alata u sučelju

### Česti problemi i rješenja

**Poslužitelj se neće pokrenuti:**
- Provjerite da su sve ovisnosti instalirane: `pip install mcp`
- Provjerite Python sintaksu i uvlačenje
- Potražite poruke o pogreškama u konzoli

**Alati se ne prikazuju:**
- Osigurajte da su dekoratori `@server.tool()` prisutni
- Provjerite da su funkcije alata definirane prije `main()`
- Provjerite da je poslužitelj pravilno konfiguriran

**Problemi s vezom:**
- Provjerite koristi li poslužitelj ispravno stdio transport
- Provjerite da nijedan drugi proces ne ometa
- Provjerite sintaksu naredbe za Inspektor

## Zadatak

Pokušajte proširiti svoj poslužitelj s više funkcionalnosti. Pogledajte [ovu stranicu](https://api.chucknorris.io/) kako biste, na primjer, dodali alat koji poziva API. Vi odlučujete kako vaš poslužitelj treba izgledati. Zabavite se :)
## Rješenje

[Rješenje](./solution/README.md) Evo jednog mogućeg rješenja s radnim kodom.

## Ključne pouke

Ključne pouke iz ovog poglavlja su sljedeće:

- Stdio transport je preporučeni mehanizam za lokalne MCP poslužitelje.
- Stdio transport omogućava neprimjetnu komunikaciju između MCP poslužitelja i klijenata koristeći standardne ulazne i izlazne tokove.
- Možete koristiti i Inspektor i Visual Studio Code za direktnu potrošnju stdio poslužitelja, što olakšava otklanjanje pogrešaka i integraciju.

## Primjeri

- [Java Kalkulator](../samples/java/calculator/README.md)
- [.Net Kalkulator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulator](../samples/javascript/README.md)
- [TypeScript Kalkulator](../samples/typescript/README.md)
- [Python Kalkulator](../../../../03-GettingStarted/samples/python) 

## Dodatni resursi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Što slijedi

## Sljedeći koraci

Sada kada znate kako izgraditi MCP poslužitelje sa stdio transportom, možete istražiti naprednije teme:

- **Sljedeće**: [HTTP streaming s MCP (Streamable HTTP)](../06-http-streaming/README.md) - Naučite o drugom podržanom transportnom mehanizmu za udaljene poslužitelje
- **Napredno**: [MCP sigurnosne najbolje prakse](../../02-Security/README.md) - Implementirajte sigurnost u svoje MCP poslužitelje
- **Produkcija**: [Strategije postavljanja](../09-deployment/README.md) - Postavite svoje poslužitelje za produkcijsko korištenje

## Dodatni resursi

- [MCP specifikacija 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Trenutna specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za sve jezike
- [Primjeri iz zajednice](../../06-CommunityContributions/README.md) - Još primjera poslužitelja iz zajednice

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->