# MCP poslužitelj sa stdio transportom

> **⚠️ Važna obavijest**: Od specifikacije MCP 2025-06-18, samostalni SSE (Server-Sent Events) transport je **zastarjeli** i zamijenjen je "Streamable HTTP" transportom. Trenutna MCP specifikacija definira dva primarna transportna mehanizma:
> 1. **stdio** - Standardni ulaz/izlaz (preporučeno za lokalne poslužitelje)
> 2. **Streamable HTTP** - Za udaljene poslužitelje koji mogu interno koristiti SSE
>
> Ova lekcija je ažurirana da se fokusira na **stdio transport**, koji je preporučeni pristup za većinu implementacija MCP poslužitelja.

Stdio transport omogućuje MCP poslužiteljima komunikaciju s klijentima putem standardnih ulaznih i izlaznih tokova. Ovo je najčešće korišten i preporučeni transportni mehanizam u trenutnoj MCP specifikaciji, pružajući jednostavan i učinkovit način za izgradnju MCP poslužitelja koji se lako mogu integrirati s različitim klijentskim aplikacijama.

## Pregled

Ova lekcija pokriva kako izgraditi i koristiti MCP poslužitelje pomoću stdio transporta.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:

- Izgraditi MCP poslužitelj koristeći stdio transport.
- Debugirati MCP poslužitelj koristeći Inspector.
- Koristiti MCP poslužitelj u Visual Studio Code-u.
- Razumjeti trenutne MCP transportne mehanizme i zašto se preporučuje stdio.

## stdio transport - Kako radi

Stdio transport je jedan od dva podržana tipa transporta u trenutnoj MCP specifikaciji (2025-06-18). Evo kako radi:

- **Jednostavna komunikacija**: poslužitelj čita JSON-RPC poruke sa standardnog ulaza (`stdin`) i šalje poruke na standardni izlaz (`stdout`).
- **Temeljen na procesu**: klijent pokreće MCP poslužitelj kao podproces.
- **Format poruka**: poruke su pojedinačni JSON-RPC zahtjevi, notifikacije ili odgovori, odvojeni novim redom.
- **Dnevnički zapisi** (logging): poslužitelj MOŽE pisati UTF-8 stringove na standardnu grešku (`stderr`) za potrebe zapisivanja.

### Ključni zahtjevi:
- Poruke MORAJU biti razdvojene novim redom i NE SMIJU sadržavati ugrađene nove redove.
- Poslužitelj NE SMIJE pisati ništa na `stdout` što nije valjana MCP poruka.
- Klijent NE SMIJE pisati ništa na `stdin` poslužitelja što nije valjana MCP poruka.

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

U gornjem kodu:

- Uvozimo klasu `Server` i `StdioServerTransport` iz MCP SDK-a
- Kreiramo instancu poslužitelja s osnovnom konfiguracijom i mogućnostima

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

U gornjem kodu:

- Kreiramo instancu poslužitelja koristeći MCP SDK
- Definiramo alate pomoću dekoratora
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

Ključna razlika u odnosu na SSE je da stdio poslužitelji:

- Ne zahtijevaju postavljanje web poslužitelja ni HTTP krajnjih točaka
- Pokreću se kao podprocesi od strane klijenta
- Komuniciraju putem stdin/stdout tokova
- Jednostavniji su za implementaciju i debugiranje

## Vježba: Kreiranje stdio poslužitelja

Za kreiranje našeg poslužitelja trebamo imati na umu dvije stvari:

- Trebamo koristiti web poslužitelj za izlaganje krajnjih točaka za povezivanje i poruke.
## Laboratorij: Kreiranje jednostavnog MCP stdio poslužitelja

U ovom laboratoriju kreirat ćemo jednostavan MCP poslužitelj koristeći preporučeni stdio transport. Ovaj poslužitelj će izlagati alate koje klijenti mogu pozivati koristeći standardni Model Context Protocol.

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
- Jednostavan model podprocesa - klijent pokreće poslužitelj kao podproces
- Komunikacija putem stdin/stdout koristeći JSON-RPC poruke
- Nije potrebno postavljanje HTTP poslužitelja
- Bolje performanse i sigurnost
- Jednostavnije debugiranje i razvoj

**SSE transport (zastarjelo od MCP 2025-06-18):**
- Zahtijevao je HTTP poslužitelj s SSE krajnjim točkama
- Složenija postavka s infrastrukturom web poslužitelja
- Dodatni sigurnosni zahtjevi za HTTP krajnje točke
- Sada je zamijenjen Streamable HTTP za scenarije bazirane na webu

### Kreiranje poslužitelja sa stdio transportom

Za kreiranje našeg stdio poslužitelja potrebno je:

1. **Uvoziti potrebne biblioteke** - Trebamo MCP komponente poslužitelja i stdio transport
2. **Kreirati instancu poslužitelja** - Definirati poslužitelj sa svojim mogućnostima
3. **Definirati alate** - Dodati funkcionalnosti koje želimo izložiti
4. **Postaviti transport** - Konfigurirati stdio komunikaciju
5. **Pokrenuti poslužitelj** - Startati poslužitelj i obrađivati poruke

Izgradimo to korak po korak:

### Korak 1: Kreiraj osnovni stdio poslužitelj

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfiguriraj zapisivanje dnevnika
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kreiraj poslužitelj
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

### Korak 2: Dodaj više alata

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

Spremi kôd kao `server.py` i pokreni ga iz naredbenog retka:

```bash
python server.py
```

Poslužitelj će se pokrenuti i čekati unos sa stdin. Komunicira pomoću JSON-RPC poruka preko stdio transporta.

### Korak 4: Testiranje s Inspectorom

Možete testirati svoj poslužitelj koristeći MCP Inspector:

1. Instalirajte Inspector: `npx @modelcontextprotocol/inspector`
2. Pokrenite Inspector i usmjerite ga na svoj poslužitelj
3. Testirajte alate koje ste kreirali

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debugiranje vašeg stdio poslužitelja

### Korištenje MCP Inspectora

MCP Inspector je vrijedan alat za debugiranje i testiranje MCP poslužitelja. Evo kako ga koristiti sa vašim stdio poslužiteljem:

1. **Instalirajte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pokrenite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte poslužitelj**: Inspector pruža web sučelje u kojem možete:
   - Pregledati mogućnosti poslužitelja
   - Testirati alate s različitim parametrima
   - Pratiti JSON-RPC poruke
   - Debugirati probleme s vezom

### Korištenje VS Code-a

MCP poslužitelj možete debugirati i izravno u VS Code-u:

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
3. Pokrenite debugger i testirajte s Inspectorom

### Česti savjeti za debugiranje

- Koristite `stderr` za logiranje - nikada ne pišite na `stdout` jer je rezerviran za MCP poruke
- Osigurajte da su sve JSON-RPC poruke odvojene novim redom
- Prvo testirajte s jednostavnim alatima prije dodavanja složenih funkcionalnosti
- Koristite Inspector za provjeru formata poruka

## Korištenje vašeg stdio poslužitelja u VS Code-u

Nakon što ste izgradili svoj MCP stdio poslužitelj, možete ga integrirati s VS Code-om da biste ga koristili s Claudeom ili drugim MCP-kompatibilnim klijentima.

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

2. **Restartajte Claude**: Zatvorite i ponovno otvorite Claude da bi učitao novu konfiguraciju poslužitelja.

3. **Testirajte vezu**: Pokrenite razgovor s Claudeom i pokušajte koristiti vaše alate:
   - "Možeš li me pozdraviti koristeći alat za pozdrav?"
   - "Izračunaj zbroj 15 i 27"
   - "Koje su informacije o poslužitelju?"

### Primjer TypeScript stdio poslužitelja

Evo kompletnog TypeScript primjera za referencu:

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

// Dodajte alate
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

U ovoj ažuriranoj lekciji ste naučili kako:

- Izgraditi MCP poslužitelje koristeći trenutni **stdio transport** (preporučeni pristup)
- Razumjeti zašto je SSE transport zastario u korist stdio i Streamable HTTP
- Kreirati alate koje MCP klijenti mogu pozivati
- Debugirati poslužitelj koristeći MCP Inspector
- Integrirati svoj stdio poslužitelj s VS Code-om i Claudeom

Stdio transport pruža jednostavniji, sigurniji i učinkovitiji način za izgradnju MCP poslužitelja u odnosu na zastarjeli SSE pristup. To je preporučeni transport za većinu MCP implementacija od specifikacije 2025-06-18.

### .NET

1. Prvo kreirajmo neke alate, za to ćemo kreirati datoteku *Tools.cs* sa sljedećim sadržajem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vježba: Testiranje vašeg stdio poslužitelja

Sada kad ste izgradili svoj stdio poslužitelj, testirajmo ga da budemo sigurni da radi ispravno.

### Preduvjeti

1. Provjerite imate li instaliran MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaš poslužiteljski kôd treba biti spremljen (npr. kao `server.py`)

### Testiranje s Inspectorom

1. **Pokrenite Inspector s vašim poslužiteljem**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorite web sučelje**: Inspector će otvoriti prozor preglednika sa prikazom mogućnosti vašeg poslužitelja.

3. **Testirajte alate**: 
   - Isprobajte alat `get_greeting` s različitim imenima
   - Testirajte alat `calculate_sum` s raznim brojevima
   - Pozovite alat `get_server_info` za prikaz metapodataka poslužitelja

4. **Pratite komunikaciju**: Inspector prikazuje JSON-RPC poruke koje se razmjenjuju između klijenta i poslužitelja.

### Što biste trebali vidjeti

Kada se vaš poslužitelj uspješno pokrene, trebali biste vidjeti:
- Popis mogućnosti poslužitelja u Inspectoru
- Alate dostupne za testiranje
- Uspješne razmjene JSON-RPC poruka
- Odgovore alata prikazane u sučelju

### Česti problemi i rješenja

**Poslužitelj se ne pokreće:**
- Provjerite jesu li sve ovisnosti instalirane: `pip install mcp`
- Provjerite Python sintaksu i uvlačenje
- Potražite poruke o pogreškama u konzoli

**Alati se ne pojavljuju:**
- Provjerite da su prisutni `@server.tool()` dekoratori
- Provjerite da su funkcije alata definirane prije `main()`
- Provjerite je li poslužitelj ispravno konfiguriran

**Problemi s vezom:**
- Provjerite koristi li poslužitelj ispravno stdio transport
- Provjerite da nisu drugi procesi u konfliktu
- Provjerite ispravnost sintakse naredbi Inspectora

## Zadatak

Pokušajte dodatno razviti svoj poslužitelj s više mogućnosti. Pogledajte [ovu stranicu](https://api.chucknorris.io/) kako biste, primjerice, dodali alat koji poziva API. Vi odlučujete kako treba izgledati poslužitelj. Zabavite se :)

## Rješenje

[Rješenje](./solution/README.md) Evo mogućeg rješenja s radnim kodom.

## Ključne pouke

Ključne pouke iz ovog poglavlja su sljedeće:

- Stdio transport je preporučeni mehanizam za lokalne MCP poslužitelje.
- Stdio transport omogućava neprimjetnu komunikaciju između MCP poslužitelja i klijenata koristeći standardne ulazne i izlazne tokove.
- Možete koristiti i Inspector i Visual Studio Code za korištenje stdio poslužitelja izravno, što olakšava debugiranje i integraciju.

## Primjeri

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## Dodatni resursi

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Što slijedi

## Sljedeći koraci

Sada kad ste naučili kako izgraditi MCP poslužitelje sa stdio transportom, možete istražiti naprednije teme:

- **Sljedeće**: [HTTP streaming s MCP-om (Streamable HTTP)](../06-http-streaming/README.md) - Saznajte o drugom podržanom transportnom mehanizmu za udaljene poslužitelje
- **Napredno**: [MCP sigurnosne najbolje prakse](../../02-Security/README.md) - Implementirajte sigurnost u svoje MCP poslužitelje
- **Produkcija**: [Strategije implementacije](../09-deployment/README.md) - Implementirajte svoje poslužitelje za produkcijsku upotrebu

## Dodatni resursi

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Službena specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za sve jezike
- [Primjeri iz zajednice](../../06-CommunityContributions/README.md) - Više primjera poslužitelja iz zajednice

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku smatra se službenim i autoritativnim. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili kriva tumačenja nastala korištenjem ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->