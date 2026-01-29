# MCP serveris su stdio transportu

> **⚠️ Svarbus atnaujinimas**: Nuo MCP specifikacijos 2025-06-18, atskiras SSE (Server-Sent Events) transportas buvo **pašalintas** ir pakeistas „Streamable HTTP“ transportu. Dabartinė MCP specifikacija apibrėžia du pagrindinius transporto mechanizmus:
> 1. **stdio** - Standartinis įvesties/išvesties srautas (rekomenduojama vietiniams serveriams)
> 2. **Streamable HTTP** - Nuotoliniams serveriams, kurie viduje gali naudoti SSE
>
> Ši pamoka buvo atnaujinta, kad būtų sutelkta į **stdio transportą**, kuris yra rekomenduojamas daugumai MCP serverių įgyvendinimų.

Stdio transportas leidžia MCP serveriams bendrauti su klientais per standartinius įvesties ir išvesties srautus. Tai yra dažniausiai naudojamas ir rekomenduojamas transporto mechanizmas dabartinėje MCP specifikacijoje, suteikiantis paprastą ir efektyvų būdą kurti MCP serverius, kuriuos lengva integruoti su įvairiomis klientų programomis.

## Apžvalga

Šioje pamokoje aptariama, kaip kurti ir naudoti MCP serverius naudojant stdio transportą.

## Mokymosi tikslai

Pamokos pabaigoje galėsite:

- Sukurti MCP serverį naudojant stdio transportą.
- Derinti MCP serverį naudojant „Inspector“.
- Naudoti MCP serverį su Visual Studio Code.
- Suprasti dabartinius MCP transporto mechanizmus ir kodėl stdio yra rekomenduojamas.

## stdio transportas – kaip jis veikia

Stdio transportas yra vienas iš dviejų palaikomų transporto tipų dabartinėje MCP specifikacijoje (2025-06-18). Štai kaip jis veikia:

- **Paprastas bendravimas**: Serveris skaito JSON-RPC pranešimus iš standartinės įvesties (`stdin`) ir siunčia pranešimus į standartinę išvestį (`stdout`).
- **Procesų pagrindu**: Klientas paleidžia MCP serverį kaip subprocesą.
- **Pranešimų formatas**: Pranešimai yra atskiri JSON-RPC užklausos, pranešimai arba atsakymai, atskirti naujomis eilutėmis.
- **Žurnalavimas**: Serveris GALI rašyti UTF-8 eilutes į standartinę klaidą (`stderr`) žurnalavimo tikslais.

### Pagrindiniai reikalavimai:
- Pranešimai PRIVALO būti atskirti naujomis eilutėmis ir NEGALI turėti įterptų naujų eilučių.
- Serveris NEGALI rašyti nieko į `stdout`, kas nėra galiojantis MCP pranešimas.
- Klientas NEGALI rašyti nieko į serverio `stdin`, kas nėra galiojantis MCP pranešimas.

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

Ankstesniame kode:

- Importuojame `Server` klasę ir `StdioServerTransport` iš MCP SDK.
- Sukuriame serverio egzempliorių su pagrindine konfigūracija ir galimybėmis.

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

Ankstesniame kode:

- Sukuriame serverio egzempliorių naudodami MCP SDK.
- Apibrėžiame įrankius naudodami dekoratorius.
- Naudojame `stdio_server` kontekstų valdytoją transportui valdyti.

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

Pagrindinis skirtumas nuo SSE yra tas, kad stdio serveriai:

- Nereikalauja žiniatinklio serverio nustatymo ar HTTP galinių taškų.
- Paleidžiami kaip subprocesai klientui.
- Bendrauja per stdin/stdout srautus.
- Yra paprastesni įgyvendinti ir derinti.

## Užduotis: Sukurti stdio serverį

Norėdami sukurti serverį, turime atsižvelgti į du dalykus:

- Turime naudoti žiniatinklio serverį, kad atskleistume galinius taškus ryšiui ir pranešimams.

## Laboratorija: Paprasto MCP stdio serverio kūrimas

Šioje laboratorijoje sukursime paprastą MCP serverį, naudodami rekomenduojamą stdio transportą. Šis serveris atskleis įrankius, kuriuos klientai galės iškviesti naudodami standartinį Model Context Protocol.

### Reikalavimai

- Python 3.8 ar naujesnė versija.
- MCP Python SDK: `pip install mcp`.
- Pagrindinės žinios apie asinchroninį programavimą.

Pradėkime kurti pirmąjį MCP stdio serverį:

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

## Pagrindiniai skirtumai nuo pašalinto SSE metodo

**Stdio transportas (dabartinis standartas):**
- Paprastas subprocesų modelis – klientas paleidžia serverį kaip vaiko procesą.
- Bendravimas per stdin/stdout naudojant JSON-RPC pranešimus.
- Nereikia HTTP serverio nustatymo.
- Geresnis našumas ir saugumas.
- Lengvesnis derinimas ir kūrimas.

**SSE transportas (pašalintas nuo MCP 2025-06-18):**
- Reikėjo HTTP serverio su SSE galiniais taškais.
- Sudėtingesnis nustatymas su žiniatinklio serverio infrastruktūra.
- Papildomi saugumo aspektai HTTP galiniams taškams.
- Dabar pakeistas „Streamable HTTP“ žiniatinklio scenarijams.

### Serverio kūrimas su stdio transportu

Norėdami sukurti stdio serverį, turime:

1. **Importuoti reikalingas bibliotekas** – mums reikės MCP serverio komponentų ir stdio transporto.
2. **Sukurti serverio egzempliorių** – apibrėžti serverį su jo galimybėmis.
3. **Apibrėžti įrankius** – pridėti funkcionalumą, kurį norime atskleisti.
4. **Nustatyti transportą** – konfigūruoti stdio bendravimą.
5. **Paleisti serverį** – pradėti serverį ir tvarkyti pranešimus.

Sukurkime tai žingsnis po žingsnio:

### 1 žingsnis: Sukurti pagrindinį stdio serverį

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

### 2 žingsnis: Pridėti daugiau įrankių

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

### 3 žingsnis: Paleisti serverį

Išsaugokite kodą kaip `server.py` ir paleiskite jį iš komandinės eilutės:

```bash
python server.py
```

Serveris pradės veikti ir lauks įvesties iš stdin. Jis bendrauja naudodamas JSON-RPC pranešimus per stdio transportą.

### 4 žingsnis: Testavimas su „Inspector“

Galite išbandyti savo serverį naudodami MCP „Inspector“:

1. Įdiekite „Inspector“: `npx @modelcontextprotocol/inspector`.
2. Paleiskite „Inspector“ ir nukreipkite jį į savo serverį.
3. Išbandykite sukurtus įrankius.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Derinimas jūsų stdio serveriui

### Naudojant MCP „Inspector“

MCP „Inspector“ yra vertingas įrankis MCP serverių derinimui ir testavimui. Štai kaip jį naudoti su jūsų stdio serveriu:

1. **Įdiekite „Inspector“**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Paleiskite „Inspector“**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testuokite savo serverį**: „Inspector“ suteikia žiniatinklio sąsają, kurioje galite:
   - Peržiūrėti serverio galimybes.
   - Testuoti įrankius su skirtingais parametrais.
   - Stebėti JSON-RPC pranešimus.
   - Derinti ryšio problemas.

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

2. Nustatykite pertraukos taškus savo serverio kode.
3. Paleiskite derintuvą ir testuokite su „Inspector“.

### Bendri derinimo patarimai

- Naudokite `stderr` žurnalavimui – niekada nerašykite į `stdout`, nes jis skirtas MCP pranešimams.
- Įsitikinkite, kad visi JSON-RPC pranešimai yra atskirti naujomis eilutėmis.
- Pirmiausia testuokite paprastus įrankius, prieš pridėdami sudėtingą funkcionalumą.
- Naudokite „Inspector“, kad patikrintumėte pranešimų formatus.

## Naudojimas jūsų stdio serverio su VS Code

Kai sukursite savo MCP stdio serverį, galite jį integruoti su VS Code, kad naudotumėte jį su Claude ar kitais MCP suderinamais klientais.

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

2. **Paleiskite Claude iš naujo**: Uždarykite ir vėl atidarykite Claude, kad įkeltumėte naują serverio konfigūraciją.

3. **Testuokite ryšį**: Pradėkite pokalbį su Claude ir pabandykite naudoti savo serverio įrankius:
   - „Ar gali pasveikinti mane naudodamas pasveikinimo įrankį?“
   - „Apskaičiuok 15 ir 27 sumą.“
   - „Kokia serverio informacija?“

### TypeScript stdio serverio pavyzdys

Štai pilnas TypeScript pavyzdys:

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

## Santrauka

Šioje atnaujintoje pamokoje išmokote:

- Kurti MCP serverius naudojant dabartinį **stdio transportą** (rekomenduojamas metodas).
- Suprasti, kodėl SSE transportas buvo pašalintas ir pakeistas stdio bei „Streamable HTTP“.
- Kurti įrankius, kuriuos gali iškviesti MCP klientai.
- Derinti savo serverį naudojant MCP „Inspector“.
- Integruoti savo stdio serverį su VS Code ir Claude.

Stdio transportas suteikia paprastesnį, saugesnį ir našesnį būdą kurti MCP serverius, palyginti su pašalintu SSE metodu. Tai yra rekomenduojamas transportas daugumai MCP serverių įgyvendinimų pagal 2025-06-18 specifikaciją.

### .NET

1. Pirmiausia sukurkime keletą įrankių, tam sukursime failą *Tools.cs* su šiuo turiniu:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Užduotis: Testuoti savo stdio serverį

Dabar, kai sukūrėte savo stdio serverį, išbandykime jį, kad įsitikintume, jog jis veikia tinkamai.

### Reikalavimai

1. Įsitikinkite, kad MCP „Inspector“ yra įdiegtas:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Jūsų serverio kodas turėtų būti išsaugotas (pvz., kaip `server.py`).

### Testavimas su „Inspector“

1. **Paleiskite „Inspector“ su savo serveriu**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Atidarykite žiniatinklio sąsają**: „Inspector“ atidarys naršyklės langą, kuriame bus rodomos jūsų serverio galimybės.

3. **Testuokite įrankius**: 
   - Išbandykite `get_greeting` įrankį su skirtingais vardais.
   - Testuokite `calculate_sum` įrankį su įvairiais skaičiais.
   - Iškvieskite `get_server_info` įrankį, kad pamatytumėte serverio metaduomenis.

4. **Stebėkite bendravimą**: „Inspector“ rodo JSON-RPC pranešimus, keičiamus tarp kliento ir serverio.

### Ką turėtumėte matyti

Kai jūsų serveris paleidžiamas teisingai, turėtumėte matyti:
- Serverio galimybes, rodomas „Inspector“.
- Įrankius, prieinamus testavimui.
- Sėkmingus JSON-RPC pranešimų mainus.
- Įrankių atsakymus, rodomus sąsajoje.

### Dažnos problemos ir sprendimai

**Serveris nepaleidžiamas:**
- Patikrinkite, ar visos priklausomybės yra įdiegtos: `pip install mcp`.
- Patikrinkite Python sintaksę ir įtrauką.
- Ieškokite klaidų pranešimų konsolėje.

**Įrankiai nerodomi:**
- Įsitikinkite, kad yra `@server.tool()` dekoratoriai.
- Patikrinkite, ar įrankių funkcijos apibrėžtos prieš `main()`.
- Įsitikinkite, kad serveris tinkamai sukonfigūruotas.

**Ryšio problemos:**
- Įsitikinkite, kad serveris teisingai naudoja stdio transportą.
- Patikrinkite, ar kiti procesai netrukdo.
- Patikrinkite „Inspector“ komandos sintaksę.

## Užduotis

Pabandykite išplėsti savo serverį su daugiau galimybių. Žr. [šį puslapį](https://api.chucknorris.io/), kad, pavyzdžiui, pridėtumėte įrankį, kuris kviečia API. Jūs nusprendžiate, kaip turėtų atrodyti serveris. Smagaus kūrimo :)

## Sprendimas

[Sprendimas](./solution/README.md) Štai galimas sprendimas su veikiančiu kodu.

## Pagrindinės mintys

Pagrindinės šio skyriaus mintys yra šios:

- Stdio transportas yra rekomenduojamas mechanizmas vietiniams MCP serveriams.
- Stdio transportas leidžia sklandų bendravimą tarp MCP serverių ir klientų naudojant standartinius įvesties ir išvesties srautus.
- Galite tiesiogiai naudoti „Inspector“ ir Visual Studio Code, kad naudotumėte stdio serverius, todėl derinimas ir integracija yra paprasti.

## Pavyzdžiai

- [Java skaičiuotuvas](../samples/java/calculator/README.md)
- [.Net skaičiuotuvas](../../../../03-GettingStarted/samples/csharp)
- [JavaScript skaičiuotuvas](../samples/javascript/README.md)
- [TypeScript skaičiuotuvas](../samples/typescript/README.md)
- [Python skaičiuotuvas](../../../../03-GettingStarted/samples/python) 

## Papildomi ištekliai

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Kas toliau

## Kiti žingsniai

Dabar, kai išmokote kurti MCP serverius su stdio transportu, galite tyrinėti sudėtingesnes temas:

- **Toliau**: [HTTP srautinė peržiūra su MCP („Streamable HTTP“)](../06-http-streaming/README.md) – Sužinokite apie kitą palaikomą transporto mechanizmą nuotoliniams serveriams.
- **Pažangiai**: [MCP saugumo geriausios praktikos](../../02-Security/README.md) – Įgyvendinkite saugumą savo MCP serveriuose.
- **Produkcijai**: [Diegimo strategijos](../09-deployment/README.md) – Diegkite savo serverius produkciniam naudojimui.

## Papildomi ištekliai

- [MCP specifikacija 2025-06-18](https://spec.modelcontextprotocol.io/specification/) – Oficiali specifikacija.
- [MCP SDK dokumentacija](https://github.com/modelcontextprotocol/sdk) – SDK nuorodos visoms kalboms.
- [Bendruomenės pavyzdžiai](../../06-CommunityContributions/README.md) – Daugiau serverių pavyzdžių iš bendruomenės.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.