# MCP szerver stdio transzporttal

> **⚠️ Fontos frissítés**: Az MCP Specifikáció 2025-06-18 óta a különálló SSE (Server-Sent Events) transzport **elavultnak** minősült, és helyette a "Streamable HTTP" transzportot vezették be. Az aktuális MCP specifikáció két elsődleges transzport mechanizmust határoz meg:
> 1. **stdio** - Standard bemenet/kimenet (helyi szerverekhez ajánlott)
> 2. **Streamable HTTP** - Távoli szerverekhez, amelyek belsőleg SSE-t használhatnak
>
> Ez a lecke frissítve lett, hogy a **stdio transzportra** összpontosítson, amely a legtöbb MCP szerver implementációhoz ajánlott megközelítés.

A stdio transzport lehetővé teszi az MCP szerverek számára, hogy standard bemeneti és kimeneti adatfolyamokon keresztül kommunikáljanak a kliensekkel. Ez az MCP specifikáció jelenlegi leggyakrabban használt és ajánlott transzport mechanizmusa, amely egyszerű és hatékony módot kínál MCP szerverek építésére, amelyek könnyen integrálhatók különböző kliens alkalmazásokkal.

## Áttekintés

Ez a lecke bemutatja, hogyan építsünk és használjunk MCP szervereket stdio transzporttal.

## Tanulási célok

A lecke végére képes leszel:

- MCP szervert építeni stdio transzporttal.
- MCP szervert hibakeresni az Inspector segítségével.
- MCP szervert használni a Visual Studio Code-ban.
- Megérteni az aktuális MCP transzport mechanizmusokat, és hogy miért ajánlott a stdio.

## stdio transzport - Hogyan működik

A stdio transzport az MCP specifikáció (2025-06-18) által támogatott két transzport típus egyike. Így működik:

- **Egyszerű kommunikáció**: A szerver JSON-RPC üzeneteket olvas a standard bemenetről (`stdin`), és üzeneteket küld a standard kimenetre (`stdout`).
- **Folyamat-alapú**: A kliens alfolyamatként indítja el az MCP szervert.
- **Üzenetformátum**: Az üzenetek egyedi JSON-RPC kérések, értesítések vagy válaszok, amelyek új sorokkal vannak elválasztva.
- **Naplózás**: A szerver UTF-8 karakterláncokat írhat a standard hibára (`stderr`) naplózási célból.

### Fő követelmények:
- Az üzeneteket ÚJ SOROKKAL kell elválasztani, és NEM tartalmazhatnak beágyazott új sorokat.
- A szerver NEM írhat semmit a `stdout`-ra, ami nem érvényes MCP üzenet.
- A kliens NEM írhat semmit a szerver `stdin`-jára, ami nem érvényes MCP üzenet.

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

A fenti kódban:

- Importáljuk a `Server` osztályt és a `StdioServerTransport`-ot az MCP SDK-ból.
- Létrehozunk egy szerver példányt alapvető konfigurációval és képességekkel.

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

A fenti kódban:

- Létrehozunk egy szerver példányt az MCP SDK használatával.
- Eszközöket definiálunk dekorátorokkal.
- A `stdio_server` kontextuskezelőt használjuk a transzport kezelésére.

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

A fő különbség az SSE-hez képest, hogy a stdio szerverek:

- Nem igényelnek web szerver beállítást vagy HTTP végpontokat.
- A kliens alfolyamatként indítja el őket.
- `stdin`/`stdout` adatfolyamokon keresztül kommunikálnak.
- Egyszerűbbek implementálni és hibakeresni.

## Gyakorlat: stdio szerver létrehozása

Ahhoz, hogy létrehozzuk a szerverünket, két dolgot kell szem előtt tartanunk:

- Web szervert kell használnunk a végpontok kitettségéhez és az üzenetek kezeléséhez.

## Labor: Egyszerű MCP stdio szerver létrehozása

Ebben a laborban létrehozunk egy egyszerű MCP szervert az ajánlott stdio transzporttal. Ez a szerver olyan eszközöket fog biztosítani, amelyeket a kliensek a standard Model Context Protocol segítségével hívhatnak meg.

### Előfeltételek

- Python 3.8 vagy újabb
- MCP Python SDK: `pip install mcp`
- Alapvető ismeretek az aszinkron programozásról

Kezdjük el az első MCP stdio szerverünk létrehozását:

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

## Fő különbségek az elavult SSE megközelítéshez képest

**Stdio transzport (aktuális szabvány):**
- Egyszerű alfolyamat modell - a kliens gyermekfolyamatként indítja a szervert.
- Kommunikáció `stdin`/`stdout`-on keresztül JSON-RPC üzenetekkel.
- Nem igényel HTTP szerver beállítást.
- Jobb teljesítmény és biztonság.
- Könnyebb hibakeresés és fejlesztés.

**SSE transzport (elavult 2025-06-18 óta):**
- HTTP szervert igényelt SSE végpontokkal.
- Bonyolultabb beállítás web szerver infrastruktúrával.
- További biztonsági megfontolások HTTP végpontokhoz.
- Mostantól Streamable HTTP váltja fel web-alapú forgatókönyvekhez.

### stdio szerver létrehozása

Ahhoz, hogy létrehozzuk a stdio szerverünket, a következőket kell tennünk:

1. **Szükséges könyvtárak importálása** - Az MCP szerver komponensek és stdio transzport szükségesek.
2. **Szerver példány létrehozása** - A szerver képességeinek meghatározása.
3. **Eszközök definiálása** - A kívánt funkcionalitás hozzáadása.
4. **Transzport beállítása** - Stdio kommunikáció konfigurálása.
5. **Szerver futtatása** - A szerver indítása és az üzenetek kezelése.

Lépésről lépésre építsük fel:

### 1. lépés: Alap stdio szerver létrehozása

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

### 2. lépés: További eszközök hozzáadása

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

### 3. lépés: A szerver futtatása

Mentsd el a kódot `server.py` néven, és futtasd a parancssorból:

```bash
python server.py
```

A szerver elindul, és várja a bemenetet a `stdin`-ről. JSON-RPC üzenetekkel kommunikál a stdio transzporton keresztül.

### 4. lépés: Tesztelés az Inspectorral

A szerver teszteléséhez használd az MCP Inspectort:

1. Telepítsd az Inspectort: `npx @modelcontextprotocol/inspector`
2. Futtasd az Inspectort, és mutass rá a szerveredre.
3. Teszteld az általad létrehozott eszközöket.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## A stdio szerver hibakeresése

### Az MCP Inspector használata

Az MCP Inspector értékes eszköz az MCP szerverek hibakereséséhez és teszteléséhez. Így használhatod a stdio szervereddel:

1. **Inspector telepítése**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector futtatása**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Szerver tesztelése**: Az Inspector webes felületet biztosít, ahol:
   - Megtekintheted a szerver képességeit.
   - Tesztelheted az eszközöket különböző paraméterekkel.
   - Figyelheted a JSON-RPC üzeneteket.
   - Hibakeresheted a kapcsolódási problémákat.

### Visual Studio Code használata

Az MCP szerveredet közvetlenül a VS Code-ban is hibakeresheted:

1. Hozz létre egy indítási konfigurációt `.vscode/launch.json` fájlban:
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

2. Állíts be töréspontokat a szerver kódjában.
3. Futtasd a hibakeresőt, és teszteld az Inspectorral.

### Gyakori hibakeresési tippek

- Használj `stderr`-t naplózáshoz - soha ne írj a `stdout`-ra, mivel az MCP üzenetek számára van fenntartva.
- Győződj meg róla, hogy minden JSON-RPC üzenet új sorral van elválasztva.
- Először egyszerű eszközökkel tesztelj, mielőtt bonyolult funkcionalitást adsz hozzá.
- Használd az Inspectort az üzenetformátumok ellenőrzésére.

## stdio szerver használata VS Code-ban

Miután elkészítetted az MCP stdio szerveredet, integrálhatod a VS Code-ba, hogy Claude-dal vagy más MCP-kompatibilis kliensekkel használd.

### Konfiguráció

1. **Hozz létre egy MCP konfigurációs fájlt** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) vagy `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Indítsd újra Claude-ot**: Zárd be, majd nyisd meg újra Claude-ot, hogy betöltse az új szerver konfigurációt.

3. **Teszteld a kapcsolatot**: Indíts beszélgetést Claude-dal, és próbáld ki a szervered eszközeit:
   - "Köszönj nekem a köszönési eszköz segítségével!"
   - "Számold ki 15 és 27 összegét!"
   - "Mi a szerver információ?"

### TypeScript stdio szerver példa

Íme egy teljes TypeScript példa referenciaként:

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

### .NET stdio szerver példa

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

## Összefoglalás

Ebben a frissített leckében megtanultad:

- MCP szervereket építeni az aktuális **stdio transzporttal** (ajánlott megközelítés).
- Megérteni, miért vált elavulttá az SSE transzport, és miért részesítik előnyben a stdio-t és a Streamable HTTP-t.
- Eszközöket létrehozni, amelyeket MCP kliensek hívhatnak meg.
- Hibakeresni a szerveredet az MCP Inspector segítségével.
- Integrálni a stdio szerveredet a VS Code-ba és Claude-ba.

A stdio transzport egyszerűbb, biztonságosabb és teljesítményorientáltabb módot kínál MCP szerverek építésére az elavult SSE megközelítéshez képest. Ez az ajánlott transzport a legtöbb MCP szerver implementációhoz a 2025-06-18 specifikáció szerint.

### .NET

1. Először hozzunk létre néhány eszközt, ehhez hozzunk létre egy *Tools.cs* fájlt a következő tartalommal:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Gyakorlat: stdio szerver tesztelése

Most, hogy elkészítetted a stdio szerveredet, teszteljük, hogy megfelelően működik-e.

### Előfeltételek

1. Győződj meg róla, hogy az MCP Inspector telepítve van:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. A szerver kódját mentsd el (pl. `server.py` néven).

### Tesztelés az Inspectorral

1. **Indítsd el az Inspectort a szervereddel**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Nyisd meg a webes felületet**: Az Inspector megnyit egy böngészőablakot, amely megjeleníti a szervered képességeit.

3. **Teszteld az eszközöket**: 
   - Próbáld ki a `get_greeting` eszközt különböző nevekkel.
   - Teszteld a `calculate_sum` eszközt különböző számokkal.
   - Hívd meg a `get_server_info` eszközt, hogy lásd a szerver metaadatait.

4. **Figyeld a kommunikációt**: Az Inspector megjeleníti a JSON-RPC üzeneteket, amelyeket a kliens és a szerver cserél.

### Mit kell látnod

Ha a szervered helyesen indul el, a következőket kell látnod:
- A szerver képességei megjelennek az Inspectorban.
- Az eszközök elérhetők tesztelésre.
- Sikeres JSON-RPC üzenetcserék.
- Az eszközök válaszai megjelennek a felületen.

### Gyakori problémák és megoldások

**A szerver nem indul el:**
- Ellenőrizd, hogy minden függőség telepítve van: `pip install mcp`.
- Ellenőrizd a Python szintaxist és behúzásokat.
- Nézd meg a konzolban megjelenő hibaüzeneteket.

**Az eszközök nem jelennek meg:**
- Győződj meg róla, hogy a `@server.tool()` dekorátorok jelen vannak.
- Ellenőrizd, hogy az eszköz funkciók a `main()` előtt vannak definiálva.
- Győződj meg róla, hogy a szerver megfelelően van konfigurálva.

**Kapcsolódási problémák:**
- Győződj meg róla, hogy a szerver helyesen használja a stdio transzportot.
- Ellenőrizd, hogy más folyamatok nem zavarják-e.
- Ellenőrizd az Inspector parancsszintaxisát.

## Feladat

Próbálj meg több képességet hozzáadni a szerveredhez. Nézd meg [ezt az oldalt](https://api.chucknorris.io/), hogy például hozzáadj egy eszközt, amely API-t hív. Te döntöd el, hogyan nézzen ki a szerver. Jó szórakozást!  
## Megoldás

[Megoldás](./solution/README.md) Itt található egy lehetséges megoldás működő kóddal.

## Fő tanulságok

A fejezet fő tanulságai a következők:

- A stdio transzport az ajánlott mechanizmus helyi MCP szerverekhez.
- A stdio transzport lehetővé teszi az MCP szerverek és kliensek közötti zökkenőmentes kommunikációt standard bemeneti és kimeneti adatfolyamokon keresztül.
- Az Inspectort és a Visual Studio Code-ot is használhatod stdio szerverek közvetlen fogyasztására, ami egyszerűvé teszi a hibakeresést és az integrációt.

## Minták

- [Java Kalkulátor](../samples/java/calculator/README.md)
- [.Net Kalkulátor](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Kalkulátor](../samples/javascript/README.md)
- [TypeScript Kalkulátor](../samples/typescript/README.md)
- [Python Kalkulátor](../../../../03-GettingStarted/samples/python) 

## További források

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mi következik

## Következő lépések

Most, hogy megtanultad, hogyan építs MCP szervereket stdio transzporttal, felfedezhetsz további haladó témákat:

- **Következő**: [HTTP Streaming MCP-vel (Streamable HTTP)](../06-http-streaming/README.md) - Ismerd meg a távoli szerverekhez támogatott másik transzport mechanizmust.
- **Haladó**: [MCP biztonsági legjobb gyakorlatok](../../02-Security/README.md) - Valósíts meg biztonságot az MCP szerverekben.
- **Éles környezet**: [Telepítési stratégiák](../09-deployment/README.md) - Telepítsd a szervereket éles környezetben való használatra.

## További források

- [MCP Specifikáció 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Hivatalos specifikáció.
- [MCP SDK Dokumentáció](https://github.com/modelcontextprotocol/sdk) - SDK referenciák minden nyelvhez.
- [Közösségi példák](../../06-CommunityContributions/README.md) - További szerver példák a közösségtől.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.