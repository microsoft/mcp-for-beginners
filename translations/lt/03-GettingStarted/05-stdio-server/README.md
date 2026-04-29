# MCP serveris su stdio transportu

> **⚠️ Svarbus atnaujinimas**: Nuo MCP specifikacijos 2025-06-18 atskiras SSE (Server-Sent Events) transportas yra **atsisakytas** ir pakeistas „Streamable HTTP“ transportu. Dabartinė MCP specifikacija apibrėžia du pagrindinius transporto mechanizmus:
> 1. **stdio** – standartinis įvesties/išvesties srautas (rekomenduojamas vietiniams serveriams)
> 2. **Streamable HTTP** – nuotoliniams serveriams, kurie gali naudoti SSE viduje
>
> Šis pamoka atnaujinta, kad būtų sutelktas dėmesys į **stdio transportą**, kuris yra rekomenduojamas daugumai MCP serverių įgyvendinimų.

Stdio transportas leidžia MCP serveriams bendrauti su klientais per standartinius įvesties ir išvesties srautus. Tai labiausiai paplitęs ir rekomenduojamas transporto mechanizmas dabartinėje MCP specifikacijoje, suteikiantis paprastą ir efektyvų būdą kurti MCP serverius, kuriuos lengva integruoti su įvairiomis kliento programomis.

## Apžvalga

Šioje pamokoje aptarsime, kaip sukurti ir naudoti MCP serverius naudodami stdio transportą.

## Mokymosi tikslai

Pamokos pabaigoje mokėsite:

- Kurti MCP serverį naudojant stdio transportą.
- Derinti MCP serverį naudojant Inspector.
- Naudoti MCP serverį Visual Studio Code aplinkoje.
- Suprasti dabartinius MCP transporto mechanizmus ir kodėl rekomenduojamas stdio transportas.

## stdio transportas – kaip tai veikia

Stdio transportas yra vienas iš dviejų palaikomų transporto tipų dabartinėje MCP specifikacijoje (2025-06-18). Štai kaip tai veikia:

- **Paprasta komunikacija**: serveris skaito JSON-RPC žinutes iš standartinės įvesties (`stdin`) ir siunčia žinutes į standartinę išvestį (`stdout`).
- **Procesų pagrindu**: klientas paleidžia MCP serverį kaip posubordinatą procesą.
- **Žinučių formatas**: žinutės yra atskiros JSON-RPC užklausos, pranešimai arba atsakymai, atskirti naujomis eilutėmis.
- **Žurnalavimas**: serveris GALI rašyti UTF-8 eilutes į standartinę klaidų išvestį (`stderr`) žurnalų tikslams.

### Svarbiausios sąlygos:
- Žinutės TURI būti atskirtos naujomis eilutėmis ir NETURI turėti įdėtų naujų eilučių
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

Aukščiau pateiktame kode:

- Importuojame `Server` klasę ir `StdioServerTransport` iš MCP SDK
- Sukuriame serverio egzempliorių su pagrindine konfigūracija ir galimybėmis
- Sukuriame `StdioServerTransport` egzempliorių ir prijungiame serverį prie jo, leidžiant bendrauti per stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Sukurkite serverio egzempliorių
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

Aukščiau pateiktame kode:

- Sukuriame serverio egzempliorių naudojant MCP SDK
- Apibrėžiame įrankius naudodami dekoratorius
- Naudojame stdio_server kontekstinį valdiklį transportui tvarkyti

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

- Nereikalauja interneto serverio nustatymo ar HTTP galinių taškų
- Paleidžiami kaip posubordinatai procesai klientų
- Bendrauja per stdin/stdout srautus
- Paprastesni įgyvendinimui ir derinimui

## Užduotis: stdio serverio kūrimas

Kad sukurtume serverį, turime atsiminti du dalykus:

- Turime naudoti interneto serverį, kad atvertume galinius taškus prisijungimui ir žinutėms.
## Laboratorija: paprasto MCP stdio serverio kūrimas

Šioje laboratorijoje sukursime paprastą MCP serverį naudodami rekomenduojamą stdio transportą. Šis serveris atvers įrankius, kuriuos klientai gali kviesti naudodami standartinį Model Context Protocol.

### Reikalavimai

- Python 3.8 arba naujesnis
- MCP Python SDK: `pip install mcp`
- Pagrindinės asinchroninio programavimo žinios

Pradėkime kurdami pirmąjį MCP stdio serverį:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Konfigūruoti žurnalo įrašymą
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

## Pagrindiniai skirtumai nuo atsisakyto SSE metodo

**Stdio transportas (dabartinė standarto versija):**
- Paprastas posubordinato modelis – klientas paleidžia serverį kaip vaikų procesą
- Komunikacija per stdin/stdout naudojant JSON-RPC žinutes
- Nereikia HTTP serverio nustatymo
- Geresnis našumas ir saugumas
- Lengvesnis derinimas ir vystymas

**SSE transportas (atsisakytas nuo MCP 2025-06-18):**
- Reikalavo HTTP serverio su SSE galiniais taškais
- Sudėtingesnis nustatymas su interneto serverio infrastruktūra
- Papildomos saugumo priemonės HTTP galiniams taškams
- Dabar pakeistas Streamable HTTP bei interneto scenarijams

### Serverio kūrimas su stdio transportu

Norėdami sukurti stdio serverį, turime:

1. **Importuoti reikalingas bibliotekas** – mums reikalingi MCP serverio komponentai ir stdio transportas
2. **Sukurti serverio egzempliorių** – apibrėžti serverį su jo galimybėmis
3. **Apibrėžti įrankius** – pridėti funkcionalumą, kurį norime atskleisti
4. **Sukurti transportą** – sukonfigūruoti stdio komunikaciją
5. **Paleisti serverį** – pradėti serverį ir tvarkyti žinutes

Sukurkime tai žingsnis po žingsnio:

### 1 žingsnis: Sukurkite paprastą stdio serverį

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigūruoti žurnalo įrašymą
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

### 2 žingsnis: Pridėkite daugiau įrankių

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

### 3 žingsnis: Paleiskite serverį

Išsaugokite kodą kaip `server.py` ir paleiskite komandinėje eilutėje:

```bash
python server.py
```

Serveris pradės veikti ir lauks įvesties iš stdin. Jis bendrauja naudodamas JSON-RPC žinutes per stdio transportą.

### 4 žingsnis: Testavimas su Inspector

Galite išbandyti serverį naudodami MCP Inspector:

1. Įdiekite Inspector: `npx @modelcontextprotocol/inspector`
2. Paleiskite Inspector ir nukreipkite jį į savo serverį
3. Išbandykite sukurtus įrankius

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Savo stdio serverio derinimas

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

3. **Išbandykite savo serverį**: Inspector teikia interneto sąsają, kur galite:
   - Peržiūrėti serverio galimybes
   - Išbandyti įrankius su skirtingais parametrais
   - Stebėti JSON-RPC žinutes
   - Derinti ryšio problemas

### Naudojant VS Code

Taip pat galite derinti MCP serverį tiesiogiai VS Code aplinkoje:

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

2. Nustatykite pertraukas serverio kode
3. Paleiskite derintuvą ir testuokite su Inspector

### Dažniausios derinimo rekomendacijos

- Naudokite `stderr` žurnaluoti – niekada nerašykite į `stdout`, nes jis skirtas MCP žinutėms
- Užtikrinkite, kad visos JSON-RPC žinutės būtų atskirtos naujomis eilutėmis
- Iš pradžių testuokite su paprastais įrankiais, prieš pridėdami sudėtingesnes funkcijas
- Naudokitės Inspector žinučių formatų patikrai

## Kaip naudoti savo stdio serverį VS Code

Kai sukursite MCP stdio serverį, galėsite integruoti jį su VS Code, kad naudotumėte Claude ar kitus MCP suderinamus klientus.

### Konfigūracija

1. **Sukurkite MCP konfigūracijos failą** adresu `%APPDATA%\Claude\claude_desktop_config.json` (Windows) arba `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Perkraukite Claude**: Uždarykite ir vėl atidarykite Claude, kad įkeltumėte naują serverio konfigūraciją.

3. **Patikrinkite ryšį**: Pradėkite pokalbį su Claude ir išbandykite savo serverio įrankius:
   - „Ar gali mane pasveikinti naudodamas greeting įrankį?“
   - „Apskaičiuok 15 ir 27 sumą“
   - „Kokia yra serverio informacija?“

### TypeScript stdio serverio pavyzdys

Pilnas TypeScript pavyzdys suteikiamas kaip nuoroda:

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

## Santrauka

Šioje atnaujintoje pamokoje išmokote:

- Kurti MCP serverius naudojant dabartinį **stdio transportą** (rekomenduojamą būdą)
- Suprasti, kodėl SSE transportas buvo atsisakytas vietoje stdio ir Streamable HTTP
- Kurti įrankius, kuriuos gali kviesti MCP klientai
- Derinti serverį naudojant MCP Inspector
- Integruoti savo stdio serverį su VS Code ir Claude

Stdio transportas suteikia paprastesnį, saugesnį ir našesnį būdą kurti MCP serverius, palyginti su atsisakytu SSE metodu. Tai rekomenduojamas transportas daugumai MCP serverių įgyvendinimų nuo 2025-06-18 specifikacijos.

### .NET

1. Pirmiausia sukurkime keletą įrankių, tam sukursime failą *Tools.cs* su tokiu turiniu:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Užduotis: savo stdio serverio testavimas

Dabar, kai sukūrėte stdio serverį, išbandykime jį, kad įsitikintume, jog veikia tinkamai.

### Reikalavimai

1. Įsitikinkite, kad MCP Inspector įdiegtas:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Jūsų serverio kodas išsaugotas (pvz., `server.py`)

### Testavimas su Inspector

1. **Pradėkite Inspector kartu su serveriu**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Atidarykite interneto sąsają**: Inspector atidarys naršyklės langą, rodantį jūsų serverio galimybes.

3. **Išbandykite įrankius**: 
   - Išbandykite `get_greeting` įrankį su skirtingais vardais
   - Išbandykite `calculate_sum` įrankį su įvairiais skaičiais
   - Iškvieskite `get_server_info` įrankį, norėdami pamatyti serverio metaduomenis

4. **Stebėkite komunikaciją**: Inspector rodo JSON-RPC žinutes, kurios keičiasi tarp kliento ir serverio.

### Ką turėtumėte matyti

Kai serveris paleidžiamas teisingai, turėtumėte matyti:
- Serverio galimybių sąrašą Inspectoriaus lange
- Įrankius, prieinamus testavimui
- Sėkmingus JSON-RPC žinučių mainus
- Įrankių atsakymus sąsajoje

### Dažnos problemos ir sprendimai

**Serveris nepaleidžiamas:**
- Patikrinkite, ar įdiegti visi priklausomybės: `pip install mcp`
- Patikrinkite Python sintaksę ir įtraukimus
- Peržiūrėkite klaidų pranešimus konsolėje

**Įrankiai nerodomi:**
- Patikrinkite, ar yra `@server.tool()` dekoratoriai
- Įsitikinkite, kad įrankių funkcijos apibrėžtos prieš `main()`
- Patikrinkite, ar serveris tinkamai sukonfigūruotas

**Ryšio problemos:**
- Įsitikinkite, kad serveris tinkamai naudoja stdio transportą
- Patikrinkite, ar kiti procesai netrukdo
- Patikrinkite Inspector komandos sintaksę

## Užduotis

Pabandykite pridėti daugiau galimybių savo serveriui. Peržiūrėkite [šią puslapį](https://api.chucknorris.io/) ir, pavyzdžiui, pridėkite įrankį, kuris kviečia API. Spręskite, kaip turėtų atrodyti serveris. Sėkmės :)
## Sprendimas

[Sprendimas](./solution/README.md) Čia pateikiamas galimas veikiantis sprendimas su kodu.

## Svarbiausios išvados

Pagrindinės įžvalgos iš šio skyriaus:

- Stdio transportas yra rekomenduojamas mechanizmas vietiniams MCP serveriams.
- Stdio transportas leidžia sklandžiai komunikuoti tarp MCP serverių ir klientų naudojant standartinius įvesties ir išvesties srautus.
- Galite naudoti tiek Inspector, tiek Visual Studio Code tiesiogiai sąveikauti su stdio serveriais, kas palengvina derinimą ir integraciją.

## Pavyzdžiai

- [Java kalkuliatorius](../samples/java/calculator/README.md)
- [.Net kalkuliatorius](../../../../03-GettingStarted/samples/csharp)
- [JavaScript kalkuliatorius](../samples/javascript/README.md)
- [TypeScript kalkuliatorius](../samples/typescript/README.md)
- [Python kalkuliatorius](../../../../03-GettingStarted/samples/python)

## Papildomi ištekliai

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kas toliau

## Tolesni žingsniai

Dabar, kai išmokote kurti MCP serverius su stdio transportu, galite gilintis į sudėtingesnes temas:

- **Toliau**: [HTTP srautas su MCP (Streamable HTTP)](../06-http-streaming/README.md) – sužinokite apie kitą palaikomą transporto mechanizmą nuotoliniams serveriams
- **Pažengusiems**: [MCP saugumo gerosios praktikos](../../02-Security/README.md) – įgyvendinkite saugumą savo MCP serveriuose
- **Gaminiui**: [Diegimo strategijos](../09-deployment/README.md) – diegkite savo serverius gamybai

## Papildomi ištekliai

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – oficiali specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) – SDK nuorodos visoms kalboms
- [Bendruomenės pavyzdžiai](../../06-CommunityContributions/README.md) – daugiau serverių pavyzdžių iš bendruomenės

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Dėl svarbios informacijos rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingas išvadas, kilusias naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->