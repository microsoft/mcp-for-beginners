# MCP serveris su stdio transportu

> **⚠️ Svarbus atnaujinimas**: Nuo MCP specifikacijos 2025-06-18, atskiras SSE (Server-Sent Events) transportas yra **nutrauktas** ir pakeistas „Streamable HTTP“ transportu. Dabartinė MCP specifikacija apibrėžia du pagrindinius transporto mechanizmus:
> 1. **stdio** - Standartinis įvesties/išvesties srautas (rekomenduojama vietiniams serveriams)
> 2. **Streamable HTTP** - Skirta nuotoliniams serveriams, kurie gali viduje naudoti SSE
>
> Šis pamokos turinys buvo atnaujintas, kad būtų sutelktas dėmesys į **stdio transportą**, kuris yra rekomenduojamas daugumai MCP serverių įgyvendinimų.

Stdio transportas leidžia MCP serveriams bendrauti su klientais per standartinius įvesties ir išvesties srautus. Tai dažniausiai naudojamas ir rekomenduojamas transporto mechanizmas dabartinėje MCP specifikacijoje, suteikiantis paprastą ir efektyvų būdą kurti MCP serverius, kurie gali būti lengvai integruojami su įvairiomis klientų programomis.

## Apžvalga

Šioje pamokoje sužinosite, kaip kurti ir naudoti MCP serverius su stdio transportu.

## Mokymosi tikslai

Pabaigus šią pamoką, galėsite:

- Sukurti MCP serverį naudojant stdio transportą.
- Derinti MCP serverį naudojant Inspector.
- Naudoti MCP serverį su Visual Studio Code.
- Suprasti dabartinius MCP transporto mechanizmus ir kodėl rekomenduojamas stdio.


## stdio transportas - kaip tai veikia

Stdio transportas yra vienas iš dviejų standartinių transportų MCP specifikacijoje
`2026-07-28`. Štai kaip jis veikia:

- **Paprastas bendravimas**: serveris skaito JSON-RPC žinutes iš standartinės įvesties (`stdin`) ir siunčia žinutes į standartinę išvestį (`stdout`).
- **Procesu pagrįstas**: klientas paleidžia MCP serverį kaip po procesą.
- **Žinučių formatas**: žinutės yra atskiri JSON-RPC užklausos, pranešimai arba atsakymai, atskirti naujomis eilutėmis.
- **Registracijos žurnalas**: serveris GALI rašyti UTF-8 eilutes į standartinę klaidų išvestį (`stderr`) registracijai.

### Pagrindiniai reikalavimai:
- Žinutės TURI būti atskirtos naujomis eilutėmis IR NETURI turėti įterptųjų naujų eilučių
- Serveris NETURI rašyti į `stdout` nieko, kas nėra galiojanti MCP žinutė
- Klientas NETURI rašyti į serverio `stdin` nieko, kas nėra galiojanti MCP žinutė

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

Ankstesniame kode:

- Importuojame `Server` klasę ir `StdioServerTransport` iš MCP SDK
- Sukuriame serverio egzempliorių su pagrindine konfigūracija ir galimybėmis
- Sukuriame `StdioServerTransport` egzempliorių ir jungiame serverį prie jo, leidžiant bendravimą per stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sukurti serverio egzempliorių
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

Aukščiau pateiktame kode mes:

- Kuriame serverio egzempliorių naudodami MCP SDK
- Apibrėžiame įrankius pasitelkdami dekoratorius
- Naudojame stdio_server kontekstą transporto valdymui

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

Pagrindinis skirtumas nuo SSE yra tas, kad stdio serveriai:

- Nepareikalauja web serverio ar HTTP galinių taškų
- Paleidžiami kaip klientų po procesai
- Bendrauja per stdin/stdout srautus
- Yra paprastesni įgyvendinti ir derinti

## Užduotis: Stdio serverio kūrimas

Norėdami sukurti mūsų serverį, turime atsiminti du dalykus:

- Turime naudoti web serverį, kad atskleistume galinius taškus prisijungimui ir žinutėms.
## Laboratorija: Paprasto MCP stdio serverio kūrimas

Šioje laboratorijoje sukursime paprastą MCP serverį, naudodami rekomenduojamą stdio transportą. Šis serveris atskleis įrankius, kuriuos klientai galės kviesti naudodami standartinį Model Context Protocol.

### Reikalingos sąlygos

- Python 3.8 arba naujesnė versija
- MCP Python SDK: `pip install mcp`
- Pagrindinės asynchrinos programavimo žinios

Pradėkime kurdami mūsų pirmąjį MCP stdio serverį:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigūruoti žurnalaudavimą
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sukurti serverį
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
    # Naudoti stdio transportą
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Pagrindiniai skirtumai nuo nutraukto SSE požiūrio

**Stdio transportas (dabartinis standartas):**
- Paprastas po procesų modelis - klientas paleidžia serverį kaip vaikų procesą
- Bendravimas per stdin/stdout naudojant JSON-RPC žinutes
- HTTP serverio nustatymas nereikalingas
- Geresnis našumas ir saugumas
- Lengvesnis derinimas ir kūrimas

**SSE transportas (nutrauktas nuo MCP 2025-06-18):**
- Reikalavo HTTP serverio su SSE galiniais taškais
- Sudėtingesnis nustatymas su web serverio infrastruktūra
- Papildomi saugumo reikalavimai HTTP galiniams taškams
- Dabar pakeistas Streamable HTTP web pagrindu veikiančiose scenarijose

### Serverio kūrimas naudojant stdio transportą

Norėdami sukurti mūsų stdio serverį, turime:

1. **Importuoti reikiamas bibliotekas** – mums reikia MCP serverio komponentų ir stdio transporto
2. **Sukurti serverio egzempliorių** – apibrėžti serverį su jo galimybėmis
3. **Apibrėžti įrankius** – pridėti norimą atskleisti funkcionalumą
4. **Sutvarkyti transportą** – konfigūruoti stdio bendravimą
5. **Paleisti serverį** – pradėti serverį ir tvarkyti žinutes

Kurkime žingsnis po žingsnio:

### 1 veiksmas: Sukurkite paprastą stdio serverį

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigūruoti žurnalų įrašymą
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sukurti serverį
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

### 2 veiksmas: Pridėti daugiau įrankių

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

### 3 veiksmas: Serverio paleidimas

Išsaugokite kodą kaip `server.py` ir paleiskite iš komandų eilutės:

```bash
python server.py
```

Serveris pradės veikti ir lauks įvesties iš stdin. Jis bendrauja naudodamas JSON-RPC žinutes per stdio transportą.

### 4 veiksmas: Testavimas su Inspector

Galite testuoti savo serverį naudodami MCP Inspector:

1. Įdiekite Inspector: `npx @modelcontextprotocol/inspector`
2. Paleiskite Inspector ir nukreipkite jį į savo serverį
3. Išbandykite sukurtus įrankius

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Derinimas jūsų stdio serveriui

### Naudojant MCP Inspector

MCP Inspector yra vertingas įrankis MCP serverių derinimui ir testavimui. Štai kaip jį naudoti su jūsų stdio serveriu:

1. **Įdiekite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Paleiskite Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Išbandykite serverį**: Inspector suteikia interneto sąsają, kur galite:
   - Peržiūrėti serverio galimybes
   - Išbandyti įrankius su skirtingais parametrais
   - Stebėti JSON-RPC žinutes
   - Derinti ryšio problemas

### Naudojant VS Code

Taip pat galite derinti savo MCP serverį tiesiogiai VS Code:

1. Sukurkite paleidimo konfigūraciją `.vscode/launch.json`:
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

2. Nustatykite pertraukimus savo serverio kode
3. Paleiskite derintuvą ir testuokite su Inspector

### Dažnos derinimo gairės

- Naudokite `stderr` registracijai – niekada nerašykite į `stdout`, nes jis skirtas MCP žinutėms
- Užtikrinkite, kad visos JSON-RPC žinutės būtų atskirtos naujomis eilutėmis
- Pirmiausiai testuokite su paprastais įrankiais, prieš pridėdami sudėtingesnes funkcijas
- Naudokite Inspector, kad patikrintumėte žinučių formatus

## Jūsų stdio serverio naudojimas VS Code

Sukūrę MCP stdio serverį, jį galite integruoti su VS Code, kad naudotumėte su Claude ar kitais MCP suderinamais klientais.

### Konfigūracija

1. **Sukurkite MCP konfigūracijos failą** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) arba `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Paleiskite iš naujo Claude**: Uždarykite ir vėl atidarykite Claude, kad būtų įkelta nauja serverio konfigūracija.

3. **Išbandykite ryšį**: Pradėkite pokalbį su Claude ir išbandykite savo serverio įrankius:
   - "Ar gali mane pasveikinti naudodamas pasveikinimo įrankį?"
   - "Apskaičiuok 15 ir 27 sumą"
   - "Kokia serverio informacija?"

### TypeScript stdio serverio pavyzdys

Čia pilnas TypeScript pavyzdys žiūrėjimui:

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

// Pridėti įrankius
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

### .NET stdio serverio pavyzdys

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

## Apibendrinimas

Šioje atnaujintoje pamokoje išmokote:

- Kurti MCP serverius naudojant dabartinį **stdio transportą** (rekomenduojamą požiūrį)
- Suprasti, kodėl SSE transportas buvo nutrauktas ir pakeistas stdio bei Streamable HTTP
- Kurti įrankius, kuriuos gali kviesti MCP klientai
- Derinti serverį naudojant MCP Inspector
- Integruoti stdio serverį su VS Code ir Claude

Stdio transportas suteikia paprastesnį, saugesnį ir našesnį būdą kurti MCP serverius, palyginti su nutrauktu SSE požiūriu. Tai yra rekomenduojamas transportas daugumai MCP serverių įgyvendinimų nuo 2025-06-18 specifikacijos.


### .NET

1. Pirmiausia sukurkime keletą įrankių, tam sukursime failą *Tools.cs* su šiuo turiniu:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Užduotis: Jūsų stdio serverio testavimas

Dabar, kai sukūrėte savo stdio serverį, išbandykime, ar jis veikia tinkamai.

### Reikalingos sąlygos

1. Įsitikinkite, kad MCP Inspector įdiegtas:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Jūsų serverio kodas turi būti išsaugotas (pvz., kaip `server.py`)

### Testavimas su Inspector

1. **Paleiskite Inspector kartu su savo serveriu**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Atidarykite interneto sąsają**: Inspector atidarys naršyklės langą, kuriame matysite savo serverio galimybes.

3. **Išbandykite įrankius**: 
   - Išbandykite `get_greeting` įrankį su skirtingais vardais
   - Išbandykite `calculate_sum` įrankį su įvairiais skaičiais
   - Iškvieskite `get_server_info` įrankį, kad matytumėte serverio metaduomenis

4. **Stebėkite ryšį**: Inspector rodo JSON-RPC žinučių mainus tarp kliento ir serverio.

### Ko turėtumėte sulaukti

Jei jūsų serveris pradeda veikti teisingai, turėtumėte matyti:
- Serverio galimybes pateiktas Inspektoriuje
- Įrankius, prieinamus testavimui
- Sėkmingą JSON-RPC žinučių mainą
- Įrankių atsakymus rodomus sąsajoje

### Dažniausios problemos ir sprendimai

**Serveris nepradeda veikti:**
- Patikrinkite, ar visos priklausomybės įdiegtos: `pip install mcp`
- Patikrinkite Python sintaksę ir įtraukimo taisykles
- Ieškokite klaidų pranešimų konsolėje

**Įrankiai nematomi:**
- Įsitikinkite, kad yra `@server.tool()` dekoratoriai
- Patikrinkite, ar įrankių funkcijos apibrėžtos prieš `main()`
- Patikrinkite, ar serveris yra tinkamai sukonfigūruotas

**Ryšio problemos:**
- Įsitikinkite, kad serveris tinkamai naudoja stdio transportą
- Patikrinkite, ar nėra trukdžių iš kitų procesų
- Patikrinkite Inspectoriaus komandos sintaksę

## Užduotis

Pabandykite sukurti savo serverį su daugiau galimybių. Pavyzdžiui, žiūrėkite [šią svetainę](https://api.chucknorris.io/), kad pridėtumėte įrankį, kuris kviečia API. Patys nuspręskite, kaip turi atrodyti serveris. Linkime smagaus :)
## Sprendimas

[Sprendimas](./solution/README.md) Čia pateikiamas galimas sprendimas su veikiančiu kodu.

## Pagrindinės įžvalgos

Šios skyriaus pagrindinės įžvalgos:

- Stdio transportas yra rekomenduojamas vietiniams MCP serveriams.
- Stdio transportas leidžia sklandžiai bendrauti tarp MCP serverių ir klientų naudojant standartinius įvesties ir išvesties srautus.
- Galite naudoti tiek Inspector, tiek Visual Studio Code tiesiogiai naudoti stdio serverius, kas palengvina derinimą ir integraciją.

## Pavyzdžiai 

- [Java skaičiuoklė](../samples/java/calculator/README.md)
- [.Net skaičiuoklė](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuoklė](../samples/javascript/README.md)
- [TypeScript skaičiuoklė](../samples/typescript/README.md)
- [Python skaičiuoklė](../../../../03-GettingStarted/samples/python) 

## Papildomi ištekliai

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kas toliau

## Kiti žingsniai

Dabar, kai išmokote kurti MCP serverius su stdio transportu, galite tyrinėti sudėtingesnes temas:

- **Toliau**: [HTTP srautinimas su MCP (Streamable HTTP)](../06-http-streaming/README.md) - Sužinokite apie kitą palaikomą transporto mechanizmą nuotoliniams serveriams
- **Pažengusiems**: [MCP saugumo geriausios praktikos](../../02-Security/README.md) - Įgyvendinkite saugumą savo MCP serveriuose
- **Produkcijai**: [Diegimo strategijos](../09-deployment/README.md) - Diekite serverius gamybinei aplinkai

## Papildomi ištekliai

- [MCP specifikacija 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Dabartinė specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) - SDK nuorodos visoms programavimo kalboms
- [Bendruomenės pavyzdžiai](../../06-CommunityContributions/README.md) - Daugiau serverių pavyzdžių iš bendruomenės

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->