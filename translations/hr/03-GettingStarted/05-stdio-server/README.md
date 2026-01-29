# MCP Server s stdio transportom

> **⚠️ Važna obavijest**: Od MCP specifikacije 2025-06-18, samostalni SSE (Server-Sent Events) transport je **zastarjel** i zamijenjen "Streamable HTTP" transportom. Trenutna MCP specifikacija definira dva glavna transportna mehanizma:
> 1. **stdio** - Standardni ulaz/izlaz (preporučeno za lokalne servere)
> 2. **Streamable HTTP** - Za udaljene servere koji mogu interno koristiti SSE
>
> Ova lekcija je ažurirana kako bi se fokusirala na **stdio transport**, koji je preporučeni pristup za većinu MCP server implementacija.

Stdio transport omogućuje MCP serverima komunikaciju s klijentima putem standardnih ulaznih i izlaznih tokova. Ovo je najčešće korišten i preporučen transportni mehanizam u trenutnoj MCP specifikaciji, pružajući jednostavan i učinkovit način za izgradnju MCP servera koji se lako integriraju s raznim klijentskim aplikacijama.

## Pregled

Ova lekcija pokriva kako izgraditi i koristiti MCP servere koristeći stdio transport.

## Ciljevi učenja

Na kraju ove lekcije, moći ćete:

- Izgraditi MCP server koristeći stdio transport.
- Debugirati MCP server koristeći Inspector.
- Koristiti MCP server u Visual Studio Code-u.
- Razumjeti trenutne MCP transportne mehanizme i zašto je stdio preporučen.

## stdio transport - Kako funkcionira

Stdio transport je jedan od dva podržana transportna tipa u trenutnoj MCP specifikaciji (2025-06-18). Evo kako funkcionira:

- **Jednostavna komunikacija**: Server čita JSON-RPC poruke sa standardnog ulaza (`stdin`) i šalje poruke na standardni izlaz (`stdout`).
- **Procesno baziran**: Klijent pokreće MCP server kao podproces.
- **Format poruka**: Poruke su pojedinačni JSON-RPC zahtjevi, obavijesti ili odgovori, odvojeni novim redovima.
- **Logiranje**: Server MOŽE zapisivati UTF-8 stringove na standardnu grešku (`stderr`) za potrebe logiranja.

### Ključni zahtjevi:
- Poruke MORAJU biti odvojene novim redovima i NE SMIJU sadržavati ugrađene nove redove.
- Server NE SMIJE zapisivati ništa na `stdout` što nije valjana MCP poruka.
- Klijent NE SMIJE zapisivati ništa na `stdin` servera što nije valjana MCP poruka.

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

U prethodnom kodu:

- Importiramo `Server` klasu i `StdioServerTransport` iz MCP SDK-a.
- Kreiramo instancu servera s osnovnom konfiguracijom i mogućnostima.

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

U prethodnom kodu:

- Kreiramo instancu servera koristeći MCP SDK.
- Definiramo alate koristeći dekoratore.
- Koristimo stdio_server context manager za upravljanje transportom.

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

Ključna razlika u odnosu na SSE je da stdio serveri:

- Ne zahtijevaju postavljanje web servera ili HTTP endpointa.
- Pokreću se kao podprocesi od strane klijenta.
- Komuniciraju putem stdin/stdout tokova.
- Jednostavniji su za implementaciju i debugiranje.

## Vježba: Kreiranje stdio servera

Za kreiranje našeg servera, trebamo imati na umu dvije stvari:

- Trebamo koristiti web server za izlaganje endpointa za povezivanje i poruke.

## Laboratorij: Kreiranje jednostavnog MCP stdio servera

U ovom laboratoriju kreirat ćemo jednostavan MCP server koristeći preporučeni stdio transport. Ovaj server će izložiti alate koje klijenti mogu pozivati koristeći standardni Model Context Protocol.

### Preduvjeti

- Python 3.8 ili noviji
- MCP Python SDK: `pip install mcp`
- Osnovno razumijevanje asinhronog programiranja

Započnimo kreiranjem našeg prvog MCP stdio servera:

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

## Ključne razlike u odnosu na zastarjeli SSE pristup

**Stdio transport (trenutni standard):**
- Jednostavan model podprocesa - klijent pokreće server kao child proces.
- Komunikacija putem stdin/stdout koristeći JSON-RPC poruke.
- Nema potrebe za postavljanjem HTTP servera.
- Bolje performanse i sigurnost.
- Lakše debugiranje i razvoj.

**SSE transport (zastarjeli od MCP 2025-06-18):**
- Zahtijevao HTTP server s SSE endpointima.
- Složenije postavljanje s web server infrastrukturom.
- Dodatni sigurnosni izazovi za HTTP endpointe.
- Sada zamijenjen Streamable HTTP-om za web scenarije.

### Kreiranje servera sa stdio transportom

Za kreiranje našeg stdio servera, trebamo:

1. **Importirati potrebne biblioteke** - Trebamo MCP server komponente i stdio transport.
2. **Kreirati instancu servera** - Definirati server s njegovim mogućnostima.
3. **Definirati alate** - Dodati funkcionalnosti koje želimo izložiti.
4. **Postaviti transport** - Konfigurirati stdio komunikaciju.
5. **Pokrenuti server** - Startati server i upravljati porukama.

Krenimo korak po korak:

### Korak 1: Kreiranje osnovnog stdio servera

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

### Korak 2: Dodavanje više alata

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

### Korak 3: Pokretanje servera

Spremite kod kao `server.py` i pokrenite ga iz komandne linije:

```bash
python server.py
```

Server će se pokrenuti i čekati ulaz sa stdin-a. Komunicira koristeći JSON-RPC poruke preko stdio transporta.

### Korak 4: Testiranje s Inspectorom

Možete testirati svoj server koristeći MCP Inspector:

1. Instalirajte Inspector: `npx @modelcontextprotocol/inspector`
2. Pokrenite Inspector i povežite ga sa svojim serverom.
3. Testirajte alate koje ste kreirali.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debugiranje vašeg stdio servera

### Koristeći MCP Inspector

MCP Inspector je vrijedan alat za debugiranje i testiranje MCP servera. Evo kako ga koristiti sa vašim stdio serverom:

1. **Instalirajte Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Pokrenite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testirajte svoj server**: Inspector pruža web sučelje gdje možete:
   - Pregledati mogućnosti servera.
   - Testirati alate s različitim parametrima.
   - Pratiti JSON-RPC poruke.
   - Debugirati probleme s povezivanjem.

### Koristeći VS Code

Možete također debugirati svoj MCP server direktno u VS Code-u:

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

2. Postavite breakpointe u kodu servera.
3. Pokrenite debugger i testirajte s Inspectorom.

### Uobičajeni savjeti za debugiranje

- Koristite `stderr` za logiranje - nikada ne zapisujte na `stdout` jer je rezerviran za MCP poruke.
- Osigurajte da su sve JSON-RPC poruke odvojene novim redovima.
- Testirajte s jednostavnim alatima prije dodavanja složenih funkcionalnosti.
- Koristite Inspector za provjeru formata poruka.

## Korištenje vašeg stdio servera u VS Code-u

Nakon što ste izgradili svoj MCP stdio server, možete ga integrirati s VS Code-om kako biste ga koristili s Claude-om ili drugim MCP-kompatibilnim klijentima.

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

2. **Ponovno pokrenite Claude**: Zatvorite i ponovno otvorite Claude kako bi učitao novu konfiguraciju servera.

3. **Testirajte vezu**: Započnite razgovor s Claude-om i pokušajte koristiti alate vašeg servera:
   - "Možeš li me pozdraviti koristeći alat za pozdrav?"
   - "Izračunaj zbroj 15 i 27."
   - "Koje su informacije o serveru?"

### TypeScript stdio server primjer

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

### .NET stdio server primjer

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

## Sažetak

U ovoj ažuriranoj lekciji naučili ste kako:

- Izgraditi MCP servere koristeći trenutni **stdio transport** (preporučeni pristup).
- Razumjeti zašto je SSE transport zastario u korist stdio i Streamable HTTP-a.
- Kreirati alate koje MCP klijenti mogu pozivati.
- Debugirati svoj server koristeći MCP Inspector.
- Integrirati svoj stdio server s VS Code-om i Claude-om.

Stdio transport pruža jednostavniji, sigurniji i učinkovitiji način za izgradnju MCP servera u usporedbi sa zastarjelim SSE pristupom. To je preporučeni transport za većinu MCP server implementacija prema specifikaciji iz 2025-06-18.

### .NET

1. Prvo kreirajmo alate, za to ćemo kreirati datoteku *Tools.cs* sa sljedećim sadržajem:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Vježba: Testiranje vašeg stdio servera

Sada kada ste izgradili svoj stdio server, testirajmo ga kako bismo bili sigurni da ispravno radi.

### Preduvjeti

1. Osigurajte da imate instaliran MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Vaš kod servera treba biti spremljen (npr. kao `server.py`).

### Testiranje s Inspectorom

1. **Pokrenite Inspector sa svojim serverom**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Otvorite web sučelje**: Inspector će otvoriti prozor preglednika koji prikazuje mogućnosti vašeg servera.

3. **Testirajte alate**: 
   - Isprobajte alat `get_greeting` s različitim imenima.
   - Testirajte alat `calculate_sum` s raznim brojevima.
   - Pozovite alat `get_server_info` za prikaz metapodataka servera.

4. **Pratite komunikaciju**: Inspector prikazuje JSON-RPC poruke koje se razmjenjuju između klijenta i servera.

### Što biste trebali vidjeti

Kada vaš server ispravno radi, trebali biste vidjeti:
- Mogućnosti servera navedene u Inspectoru.
- Alate dostupne za testiranje.
- Uspješne razmjene JSON-RPC poruka.
- Odgovore alata prikazane u sučelju.

### Uobičajeni problemi i rješenja

**Server se ne pokreće:**
- Provjerite jesu li sve ovisnosti instalirane: `pip install mcp`.
- Provjerite Python sintaksu i uvlake.
- Potražite poruke o greškama u konzoli.

**Alati se ne pojavljuju:**
- Osigurajte da su prisutni `@server.tool()` dekoratori.
- Provjerite jesu li funkcije alata definirane prije `main()`.
- Provjerite je li server pravilno konfiguriran.

**Problemi s povezivanjem:**
- Provjerite koristi li server stdio transport ispravno.
- Provjerite da li drugi procesi ne ometaju.
- Provjerite sintaksu naredbe Inspectora.

## Zadatak

Pokušajte proširiti svoj server s više mogućnosti. Pogledajte [ovu stranicu](https://api.chucknorris.io/) kako biste, na primjer, dodali alat koji poziva API. Vi odlučujete kako će server izgledati. Zabavite se :)

## Rješenje

[Rješenje](./solution/README.md) Evo mogućeg rješenja s radnim kodom.

## Ključne točke

Ključne točke iz ovog poglavlja su sljedeće:

- Stdio transport je preporučeni mehanizam za lokalne MCP servere.
- Stdio transport omogućuje neometanu komunikaciju između MCP servera i klijenata koristeći standardne ulazne i izlazne tokove.
- Možete koristiti i Inspector i Visual Studio Code za direktno korištenje stdio servera, što debugiranje i integraciju čini jednostavnim.

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

Sada kada ste naučili kako izgraditi MCP servere sa stdio transportom, možete istražiti naprednije teme:

- **Sljedeće**: [HTTP Streaming s MCP-om (Streamable HTTP)](../06-http-streaming/README.md) - Naučite o drugom podržanom transportnom mehanizmu za udaljene servere.
- **Napredno**: [MCP Sigurnosne najbolje prakse](../../02-Security/README.md) - Implementirajte sigurnost u vašim MCP serverima.
- **Produkcija**: [Strategije implementacije](../09-deployment/README.md) - Implementirajte svoje servere za produkcijsku upotrebu.

## Dodatni resursi

- [MCP Specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Službena specifikacija.
- [MCP SDK Dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK reference za sve jezike.
- [Primjeri zajednice](../../06-CommunityContributions/README.md) - Više primjera servera iz zajednice.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.