# MCP serveris su stdio transportu

> **⚠️ Svarbus atnaujinimas**: Nuo MCP specifikacijos 2025-06-18 atskiro SSE (Server-Sent Events) transporto naudojimas buvo **nutrauktas** ir pakeistas "Streamable HTTP" transportu. Dabartinė MCP specifikacija apibrėžia du pagrindinius transporto mechanizmus:
> 1. **stdio** - standartinis įvesties/išvesties srautas (rekomenduojama vietiniams serveriams)
> 2. **Streamable HTTP** - nuotoliniams serveriams, kurie gali naudoti SSE viduje
>
> Šis pamokas atnaujintas, kad sutelktų dėmesį į **stdio transportą**, kuris yra rekomenduojamas daugumai MCP serverių įgyvendinimų.

stdio transportas leidžia MCP serveriams bendrauti su klientais per standartinius įvesties ir išvesties srautus. Tai dažniausiai naudojamas ir rekomenduojamas transporto mechanizmas dabartinėje MCP specifikacijoje, suteikiantis paprastą ir efektyvų būdą kurti MCP serverius, kurie lengvai integruojami su įvairiomis kliento programomis.

## Apžvalga

Ši pamoka aptaria, kaip kurti ir naudoti MCP serverius naudojant stdio transportą.

## Mokymosi tikslai

Pasibaigus šiai pamokai, galėsite:

- Sukurti MCP serverį naudojant stdio transportą.
- Derinti MCP serverį naudojant Inspector.
- Naudoti MCP serverį Visual Studio Code aplinkoje.
- Suprasti dabartinius MCP transporto mechanizmus ir kodėl rekomenduojamas stdio.

## stdio transportas – kaip tai veikia

stdio transportas yra vienas iš dviejų palaikomų transporto tipų dabartinėje MCP specifikacijoje (2025-06-18). Štai kaip jis veikia:

- **Paprasta komunikacija**: serveris skaito JSON-RPC žinutes iš standartinės įvesties (`stdin`) ir siunčia žinutes į standartinę išvestį (`stdout`).
- **Procesų pagrindu**: klientas paleidžia MCP serverį kaip subprocess.
- **Žinučių formatas**: žinutės yra atskiros JSON-RPC užklausos, pranešimai ar atsakymai, atskirti naujomis eilutėmis.
- **Žurnalo rašymas**: serveris GALĖTŲ rašyti UTF-8 eilutes į standartinę klaidų išvestį (`stderr`) žurnalo reikmėms.

### Pagrindiniai reikalavimai:
- Žinutės TURI būti atskirtos naujomis eilutėmis ir NETURI turėti įterptų naujų eilučių
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
```

Anksčiau pateiktame kode:

- Importuojame `Server` klasę ir `StdioServerTransport` iš MCP SDK
- Sukuriame serverio egzempliorių su pagrindine konfigūracija ir galimybėmis

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

Anksčiau pateiktame kode:

- Kuriame serverio egzempliorių naudojant MCP SDK
- Apibrėžiame įrankius naudojant dekoratorius
- Naudojamės `stdio_server` konteksto valdytoju transporto valdymui

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

- Nereikalauja interneto serverio ar HTTP galinių taškų
- Yra paleidžiami kaip subprocess'ai klientų
- Komunikuoja per stdin/stdout srautus
- Lengviau įgyvendinami ir derinami

## Pratybos: stdio serverio kūrimas

Kurdami serverį turime turėti omenyje dvi svarbias dalis:

- Naudojame interneto serverį, kad atskleistume galinius taškus prisijungimui ir žinutėms.

## Laboratorija: paprasto MCP stdio serverio kūrimas

Šioje laboratorijoje sukursime paprastą MCP serverį naudodami rekomenduojamą stdio transportą. Šis serveris išskleis įrankius, kuriuos klientai galės kviesti naudodami standartinį Model Context Protocol.

### Reikalavimai

- Python 3.8 ar naujesnė versija
- MCP Python SDK: `pip install mcp`
- Pagrindinės asinchroninio programavimo žinios

Pradėkime kurti savo pirmą MCP stdio serverį:

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

## Pagrindiniai skirtumai nuo nutraukto SSE metodo

**Stdio transportas (dabartinis standartas):**
- Paprasta subprocess modelis – klientas paleidžia serverį kaip vaiko procesą
- Komunikacija per stdin/stdout naudojant JSON-RPC žinutes
- Nereikia HTTP serverio nustatymo
- Gera našumo ir saugumo kokybė
- Lengvesnis derinimas ir plėtra

**SSE transportas (nutrauktas nuo MCP 2025-06-18):**
- Reikėjo HTTP serverio su SSE galiniais taškais
- Sudėtingesnis nustatymas su interneto serverio infrastruktūra
- Didesni saugumo reikalavimai HTTP galiniams taškams
- Dabar pakeistas Streamable HTTP interneto situacijoms

### Serverio kūrimas su stdio transportu

Norėdami sukurti savo stdio serverį, turime:

1. **Importuoti reikiamas bibliotekas** – mums reikia MCP serverio komponentų ir stdio transporto
2. **Sukurti serverio egzempliorių** – apibrėžti serverį su jo galimybėmis
3. **Apibrėžti įrankius** – pridėti funkcionalumą, kurį norime atskleisti
4. **Sutvarkyti transportą** – sukonfigūruoti stdio komunikaciją
5. **Paleisti serverį** – pradėti serverį ir tvarkyti žinutes

Sukurkime tai žingsnis po žingsnio:

### 1 žingsnis: paprasto stdio serverio kūrimas

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Konfigūruoti žurnalavimą
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

### 2 žingsnis: daugiau įrankių pridėjimas

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

### 3 žingsnis: serverio paleidimas

Išsaugokite kodą kaip `server.py` ir paleiskite komandų eilutėje:

```bash
python server.py
```

Serveris pradės veikti ir lauks įvesties iš stdin. Jis bendrauja naudodamas JSON-RPC žinutes per stdio transportą.

### 4 žingsnis: testavimas su Inspector

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
## Derinimas jūsų stdio serveryje

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

3. **Testuokite savo serverį**: Inspector suteikia interneto sąsają, kur galite:
   - Peržiūrėti serverio galimybes
   - Testuoti įrankius su įvairiais parametrais
   - Stebėti JSON-RPC žinutes
   - Derinti ryšio problemas

### Naudojant VS Code

Taip pat galite derinti savo MCP serverį tiesiogiai VS Code aplinkoje:

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

2. Užstatykite sutrikimų taškus (breakpoints) jūsų serverio kode
3. Paleiskite derintuvą ir testuokite su Inspector

### Dažnos derinimo rekomendacijos

- Naudokite `stderr` žurnalavimui – niekada nerinkite į `stdout`, nes jis skirtas MCP žinutėms
- Užtikrinkite, kad visos JSON-RPC žinutės būtų atskirtos naujomis eilutėmis
- Išbandykite paprastus įrankius prieš pridedant sudėtingą funkcionalumą
- Naudokite Inspector patvirtinti žinučių formatą

## Kaip naudoti savo stdio serverį VS Code aplinkoje

Kai sukursite savo MCP stdio serverį, galite jį integruoti su VS Code naudodami Claude arba kitus MCP palaikančius klientus.

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

2. **Paleiskite Claude iš naujo**: uždarykite ir vėl atidarykite Claude, kad įkeltumėte naują serverio konfigūraciją.

3. **Patikrinkite ryšį**: pradėkite pokalbį su Claude ir bandykite naudoti serverio įrankius:
   - „Ar gali mane pasveikinti naudodamas sveikinimo įrankį?“
   - „Apskaičiuok sumą 15 ir 27“
   - „Kokia serverio informacija?“

### TypeScript stdio serverio pavyzdys

Čia pateiktas pilnas TypeScript pavyzdys:

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

## Santrauką

Šioje atnaujintoje pamokoje jūs išmokote:

- Kurti MCP serverius naudojant dabartinį **stdio transportą** (rekomenduojamą metodą)
- Suprasti, kodėl SSE transportas buvo nutrauktas ir pakeistas stdio bei Streamable HTTP
- Kurti įrankius, kuriuos gali kviesti MCP klientai
- Derinti serverį naudojant MCP Inspector
- Integruoti savo stdio serverį su VS Code ir Claude

Stdio transportas suteikia paprastesnį, saugesnį ir našesnį būdą kurti MCP serverius palyginti su nutrauktu SSE metodu. Tai rekomenduojamas transportas daugumai MCP serverių įgyvendinimų pagal 2025-06-18 specifikaciją.

### .NET

1. Pirmiausia sukurkime keletą įrankių, tam sukursime failą *Tools.cs* su šiuo turiniu:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Pratybos: testuojame jūsų stdio serverį

Dabar, kai sukūrėte savo stdio serverį, patikrinkime, ar jis veikia tinkamai.

### Reikalavimai

1. Įsitikinkite, kad MCP Inspector įdiegtas:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Jūsų serverio kodas turi būti įrašytas (pvz., `server.py`)

### Testavimas su Inspector

1. **Paleiskite Inspector su savo serveriu**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Atidarykite interneto sąsają**: Inspector atidarys naršyklės langą, rodantį jūsų serverio galimybes.

3. **Išbandykite įrankius**:
   - Išbandykite `get_greeting` įrankį su skirtingais vardais
   - Išbandykite `calculate_sum` įrankį su įvairiais skaičiais
   - Paskambinkite `get_server_info` įrankiui, kad pamatytumėte serverio metaduomenis

4. **Stebėkite komunikaciją**: Inspector rodo JSON-RPC žinutės, keičiamos tarp kliento ir serverio.

### Ką turėtumėte matyti

Kai jūsų serveris sėkmingai startuos, turėtumėte matyti:
- Serverio galimybės išvardytos Inspectore
- Įrankiai paruošti testavimui
- Sėkmingas JSON-RPC žinučių mainai
- Įrankių atsakymai rodomi sąsajoje

### Dažniausios problemos ir sprendimai

**Serveris nesikrauna:**
- Patikrinkite, ar visos priklausomybės įdiegtos: `pip install mcp`
- Patikrinkite Python sintaksę ir įtraukų teisingumą
- Ieškokite klaidų pranešimų konsolėje

**Įrankiai nerodomi:**
- Įsitikinkite, kad yra `@server.tool()` dekoratoriai
- Patikrinkite, kad įrankių funkcijos apibrėžtos prieš `main()`
- Įsitikinkite, kad serveris tinkamai sukonfigūruotas

**Ryšio problemos:**
- Patikrinkite, ar serveris naudoja stdio transportą teisingai
- Įsitikinkite, kad nėra kitų trukdžių procesų
- Patvirtinkite Inspectoro komandos sintaksę

## Užduotis

Pabandykite papildyti savo serverį daugiau galimybių. Peržiūrėkite [šią puslapį](https://api.chucknorris.io/), kad, pavyzdžiui, pridėtumėte įrankį, kuris kviečia API. Jūs patys nuspręskite, kaip serveris turėtų atrodyti. Linkime smagiai :)

## Sprendimas

[Sprendimas](./solution/README.md) Štai galimas sprendimas su veikiančiu kodu.

## Pagrindinės išvados

Šio skyriaus pagrindinės išvados yra šios:

- stdio transportas yra rekomenduojamas mechanizmas vietiniams MCP serveriams.
- Stdio transportas leidžia sklandžiai komunikuoti tarp MCP serverių ir klientų naudojant standartinius įvesties ir išvesties srautus.
- Galite naudoti tiek Inspector, tiek Visual Studio Code tiesiogiai naudoti stdio serverius, todėl derinimas ir integracija yra paprasti.

## Pavyzdžiai

- [Java Skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net Skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript Skaičiuotuvas](../samples/typescript/README.md)
- [Python Skaičiuotuvas](../../../../03-GettingStarted/samples/python)

## Papildomi šaltiniai

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kas toliau

## Kiti žingsniai

Dabar, kai išmokote kurti MCP serverius naudodami stdio transportą, galite gilintis į pažangesnes temas:

- **Toliau**: [HTTP srautinimas su MCP (Streamable HTTP)](../06-http-streaming/README.md) – sužinokite apie kitą palaikomą transporto mechanizmą nuotoliniams serveriams
- **Pažengusiems**: [MCP saugumo gerosios praktikos](../../02-Security/README.md) – įgyvendinkite saugumą savo MCP serveriuose
- **Gamybai**: [Diegimo strategijos](../09-deployment/README.md) – diegkite savo serverius gamybai

## Papildomi šaltiniai

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – oficiali specifikacija
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) – SDK nuorodos visoms kalboms
- [Bendruomenės pavyzdžiai](../../06-CommunityContributions/README.md) – daugiau serverių pavyzdžių iš bendruomenės

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turi būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretavimą, kylančius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->