# MCP Server stdio transzporttal

> **⚠️ Fontos frissítés**: Az MCP specifikáció 2025-06-18 időpontjától az önálló SSE (Server-Sent Events) transzport **elavulttá vált**, és helyette a "Streamable HTTP" transzport lett bevezetve. A jelenlegi MCP specifikáció két elsődleges transzport mechanizmust határoz meg:
> 1. **stdio** - Standard bemenet/kimenet (helyi szerverekhez ajánlott)
> 2. **Streamable HTTP** - Távoli szerverekhez, amelyek belsőleg SSE-t használhatnak
>
> Ez a lecke a **stdio transzportra** fókuszál, amely a legtöbb MCP szerver implementáció számára ajánlott megoldás.

A stdio transzport lehetővé teszi, hogy az MCP szerverek szabványos bemeneti és kimeneti adatfolyamokon keresztül kommunikáljanak a kliensekkel. Ez a legtöbbet használt és ajánlott transzport mechanizmus a jelenlegi MCP specifikációban, egyszerű és hatékony módot biztosít az MCP szerverek építésére, amelyek egyszerűen integrálhatók különböző kliens alkalmazásokkal.

## Áttekintés

Ez a lecke megtanítja, hogyan lehet MCP szervert építeni és használni a stdio transzportot alkalmazva.

## Tanulási célok

A lecke végére képes leszel:

- MCP szervert építeni a stdio transzport használatával.
- Hibakeresni egy MCP szervert az Inspector segítségével.
- MCP szervert használni Visual Studio Code-on keresztül.
- Megérteni a jelenlegi MCP transzport mechanizmusokat és az stdio ajánlásának okait.

## stdio transzport - Hogyan működik

A stdio transzport a jelenlegi MCP specifikáció (2025-06-18) két támogatott transzporttípusa közül az egyik. Íme, hogyan működik:

- **Egyszerű kommunikáció**: A szerver JSON-RPC üzeneteket olvas a standard bemenetről (`stdin`) és üzeneteket küld a standard kimenetre (`stdout`).
- **Folyamat alapú**: A kliens alfolyamatként indítja el az MCP szervert.
- **Üzenet formátum**: Az üzenetek egyedi JSON-RPC kérések, értesítések vagy válaszok, amelyek új sorral vannak elválasztva.
- **Naplózás**: A szerver LEHETŐSÉG SZERINT írhat UTF-8 karakterláncokat a standard hibakimenetre (`stderr`) naplózáshoz.

### Fő követelmények:
- Az üzeneteknek új sorral kell elválasztva lenniük, és nem tartalmazhatnak beágyazott új sorokat.
- A szerver NEM írhat a `stdout`-ra olyan tartalmat, ami nem érvényes MCP üzenet.
- A kliens NEM írhat a szerver `stdin`-jára olyan tartalmat, ami nem érvényes MCP üzenet.

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

A fenti kódban:

- Importáljuk a `Server` osztályt és a `StdioServerTransport`-ot az MCP SDK-ból
- Létrehozunk egy szerver példányt alapkonfigurációval és képességekkel
- Létrehozunk egy `StdioServerTransport` példányt, és összekapcsoljuk a szervert vele, engedélyezve a kommunikációt stdin/stdout-on keresztül

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Szerver példány létrehozása
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

- Létrehozunk egy szerver példányt az MCP SDK használatával
- Dekorátorokat használva definiálunk eszközöket
- A stdio_server kontextuskezelőt használjuk a transzport kezelésére

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

Az SSE-vel szemben a stdio szerverek:

- Nem igényelnek webszerver beállítást vagy HTTP végpontokat
- A kliens indítja őket alfolyamathoz hasonlóan
- stdin/stdout adatfolyamokon keresztül kommunikálnak
- Egyszerűbbek megvalósítani és hibakeresni

## Gyakorlat: stdio szerver létrehozása

A szerver létrehozásakor két dolgot kell szem előtt tartanunk:

- Webszervert kell használnunk a csatlakozási és üzenetküldési végpontok biztosítására.

## Labor: Egyszerű MCP stdio szerver készítése

Ebben a laborban egy egyszerű MCP szervert hozunk létre az ajánlott stdio transzporttal. Ez a szerver olyan eszközöket tesz elérhetővé, amelyeket a kliensek a szabványos Model Context Protocol használatával hívhatnak meg.

### Előfeltételek

- Python 3.8 vagy újabb
- MCP Python SDK: `pip install mcp`
- Alapvető aszinkron programozási ismeretek

Kezdjük az első MCP stdio szerverünk létrehozásával:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Naplózás konfigurálása
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# A szerver létrehozása
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
    # stdio átvitel használata
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Fontos különbségek a megszűnt SSE megközelítéssel szemben

**Stdio transzport (jelenleg ajánlott szabvány):**
- Egyszerű alfolyamat modell - a kliens gyermekfolyamatként indítja a szervert
- Kommunikáció stdin/stdout-on keresztül JSON-RPC üzenetekkel
- HTTP szerver beállítása nem szükséges
- Jobb teljesítmény és biztonság
- Könnyebb hibakeresés és fejlesztés

**SSE transzport (2025-06-18-tól elavult):**
- HTTP szerver szükséges SSE végpontokkal
- Bonyolultabb webes szerver infrastruktúra
- További biztonsági szempontok HTTP végpontokra
- A webes esetekre most a Streamable HTTP váltotta fel

### Szerver létrehozása stdio transzporttal

A stdio szerver létrehozásához:

1. **Importáljuk a szükséges könyvtárakat** - Meg kell szereznünk az MCP szerver komponenseket és a stdio transzportot
2. **Létrehozunk egy szerver példányt** - Meghatározzuk a szerver képességeit
3. **Definiálunk eszközöket** - Hozzáadjuk a kívánt funkciókat
4. **Beállítjuk a transzportot** - Konfiguráljuk a stdio kommunikációt
5. **Elindítjuk a szervert** - Indítjuk a szervert és kezeljük az üzeneteket

Lépésről lépésre építjük fel:

### 1. lépés: Alap stdio szerver létrehozása

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Naplózás konfigurálása
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# A szerver létrehozása
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

### 2. lépés: Több eszköz hozzáadása

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

Mentse el a kódot `server.py` néven, és futtassa parancssorból:

```bash
python server.py
```

A szerver elindul és várja a bemenetet stdin-ről. JSON-RPC üzeneteket használva kommunikál a stdio transzporton keresztül.

### 4. lépés: Tesztelés az Inspectorral

Tesztelheti szerverét az MCP Inspector segítségével:

1. Telepítse az Inspectort: `npx @modelcontextprotocol/inspector`
2. Indítsa el az Inspectort, és irányítsa a szerver felé
3. Tesztelje a létrehozott eszközöket

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Hibakeresés stdio szerverén

### MCP Inspector használata

Az MCP Inspector értékes eszköz az MCP szerverek hibakereséséhez és teszteléséhez. Íme, hogyan használhatja stdio szerverével:

1. **Telepítse az Inspectort**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Indítsa el az Inspectort**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Tesztelje a szervert**: Az Inspector egy webes felületet kínál, ahol:
   - Megtekintheti a szerver képességeit
   - Tesztelheti az eszközöket különböző paraméterekkel
   - Figyelheti a JSON-RPC üzeneteket
   - Hibakeresheti a kapcsolódási problémákat

### VS Code használata

Közvetlenül VS Code-ban is hibakeresheti MCP szerverét:

1. Hozzon létre egy indítási konfigurációt a `.vscode/launch.json` fájlban:
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

2. Állítson be töréspontokat a szerver kódjában
3. Indítsa el a hibakeresőt és teszteljen az Inspectorral

### Gyakori hibakeresési tippek

- Használja a `stderr`-t naplózásra - soha ne írjon a `stdout`-ra, mert az MCP üzeneteké
- Győződjön meg róla, hogy minden JSON-RPC üzenet új sorral elválasztott
- Először egyszerű eszközökkel teszteljen, mielőtt összetett funkciókat ad hozzá
- Az Inspector segítségével ellenőrizze az üzenetformátumokat

## stdio szerver használata VS Code-ban

Miután elkészítette MCP stdio szerverét, integrálhatja azt VS Code-dal, hogy Claude-dal vagy más MCP-kompatibilis klienssel használhassa.

### Konfiguráció

1. **Hozzon létre egy MCP konfigurációs fájlt** a `%APPDATA%\Claude\claude_desktop_config.json` (Windows) vagy `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) útvonalon:

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

2. **Indítsa újra Claudet**: Zárja be és nyissa meg újra Claudet az új szerver konfiguráció betöltéséhez.

3. **Tesztelje a kapcsolatot**: Kezdjen beszélgetést Claudéval, és próbálja ki a szerver eszközeit:
   - "Meg tudsz köszönni a köszönő eszközzel?"
   - "Számold ki a 15 és 27 összegét"
   - "Mi a szerver információ?"

### TypeScript stdio szerver példa

Íme egy teljes TypeScript példa hivatkozásként:

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

// Eszközök hozzáadása
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

## Összefoglalás

Ebben a frissített leckében megtanultad, hogyan lehet:

- MCP szervereket építeni a jelenlegi **stdio transzport** használatával (ajánlott megközelítés)
- Megérteni, miért váltotta fel az SSE transzportot az stdio és Streamable HTTP
- Olyan eszközöket létrehozni, amelyeket MCP kliensek hívhatnak
- Hibakeresni a szervert az MCP Inspectorral
- Integrálni a stdio szervert VS Code-dal és Claudéval

A stdio transzport egyszerűbb, biztonságosabb és jobb teljesítményt nyújt MCP szerverek építéséhez, mint az elavult SSE megoldás. A 2025-06-18-as specifikációtól kezdve ez az ajánlott transzport a legtöbb MCP szerver implementációhoz.

### .NET

1. Először készítsünk néhány eszközt, ehhez hozzunk létre egy *Tools.cs* fájlt a következő tartalommal:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Gyakorlat: stdio szerver tesztelése

Most, hogy elkészítetted a stdio szerveredet, teszteljük, hogy helyesen működik-e.

### Előfeltételek

1. Győződj meg róla, hogy telepítve van az MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. A szerverkód mentve van (pl. `server.py`)

### Tesztelés az Inspectorral

1. **Indítsd el az Inspectort a szerverrel**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Nyisd meg a webes felületet**: Az Inspector megnyit egy böngészőablakot, amely mutatja a szerver képességeit.

3. **Teszteld az eszközöket**: 
   - Próbáld ki a `get_greeting` eszközt különböző nevekkel
   - Teszteld a `calculate_sum` eszközt különféle számokkal
   - Hívd meg a `get_server_info` eszközt a szerver metaadatainak megtekintéséhez

4. **Figyeld a kommunikációt**: Az Inspector mutatja a kliens és szerver közötti JSON-RPC üzeneteket.

### Amit látnod kell

Ha a szerver helyesen indul el, a következőket látod:
- A szerver képességei listázva az Inspectorban
- Elérhető eszközök tesztelésre
- Sikeres JSON-RPC üzenetváltások
- Az eszközök válaszai megjelennek a felületen

### Gyakori problémák és megoldások

**A szerver nem indul el:**
- Ellenőrizd, hogy minden függőség telepítve van: `pip install mcp`
- Ellenőrizd a Python szintaxist és behúzásokat
- Nézd meg a konzol hibajelzéseit

**Eszközök nem jelennek meg:**
- Győződj meg róla, hogy jelen vannak az `@server.tool()` dekorátorok
- Ellenőrizd, hogy az eszközfüggvények definiálva vannak-e a `main()` előtt
- Ellenőrizd, hogy a szerver helyesen konfigurált-e

**Kapcsolati problémák:**
- Biztosítsd, hogy a szerver stdio transzportot használ helyesen
- Ellenőrizd, hogy nincs-e más folyamat, ami zavarhatja
- Vizsgáld meg az Inspector parancs szintaxisát

## Feladat

Próbáld meg bővíteni a szerveredet további képességekkel. Nézd meg [ezt az oldalt](https://api.chucknorris.io/) például, hogy egy olyan eszközt adhass hozzá, amely egy API-t hív meg. Te döntöd el, milyen legyen a szerver. Jó szórakozást :)

## Megoldás

[Megoldás](./solution/README.md) Itt egy lehetséges megoldás működő kóddal.

## Fő tanulságok

E fejezetből a legfontosabb tanulságok a következők:

- A stdio transzport az ajánlott mechanizmus helyi MCP szerverekhez.
- A stdio transzport zökkenőmentes kommunikációt tesz lehetővé MCP szerverek és kliensek között a szabványos bemeneti és kimeneti adatfolyamok használatával.
- Mind az Inspector, mind a Visual Studio Code használható stdio szerverek közvetlen fogyasztására, megkönnyítve ezzel a hibakeresést és integrációt.

## Minták 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## További források

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mi következik

## Következő lépések

Most, hogy megtanultad, hogyan lehet MCP szervereket építeni stdio transzporttal, felfedezheted a haladóbb témákat:

- **Következő**: [HTTP Streaming MCP-vel (Streamable HTTP)](../06-http-streaming/README.md) - Tanulmányozd a másik támogatott transzport mechanizmust távoli szerverekhez
- **Haladó**: [MCP Biztonsági legjobb gyakorlatok](../../02-Security/README.md) - Biztonság megvalósítása az MCP szervereidben
- **Éles környezet**: [Kiszolgálási stratégiák](../09-deployment/README.md) - Szerverek éles üzembe helyezése

## További források

- [MCP Specifikáció 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Hivatalos specifikáció
- [MCP SDK Dokumentáció](https://github.com/modelcontextprotocol/sdk) - SDK hivatkozások minden nyelven
- [Közösségi példák](../../06-CommunityContributions/README.md) - További szerver példák a közösségtől

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ezt a dokumentumot az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítószolgáltatás segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén javasolt szakmai emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->