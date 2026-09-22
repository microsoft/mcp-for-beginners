# MCP szerver stdio transzporttal

> **⚠️ Fontos frissítés**: Az MCP specifikáció 2025-06-18-as verziója óta az önálló SSE (Server-Sent Events) transzport **elavulttá vált**, és a "Streamable HTTP" transzport váltotta fel. A jelenlegi MCP specifikáció két fő transzport-mechanizmust definiál:
> 1. **stdio** - standard bemenet/kimenet (ajánlott helyi szerverekhez)
> 2. **Streamable HTTP** - távoli szerverekhez, melyek esetleg belsőleg SSE-t használnak
>
> Ez a lecke frissítve lett, hogy a **stdio transzportra** fókuszáljon, amely a legtöbb MCP szerver implementáció esetén ajánlott megközelítés.

A stdio transzport lehetővé teszi, hogy az MCP szerverek standard bemenet és kimenet csatornákon keresztül kommunikáljanak a klienssel. Ez jelenleg a leggyakrabban használt és ajánlott transzport-mechanizmus az MCP specifikációban, egyszerű és hatékony módot nyújtva MCP szerverek építésére, melyek könnyen integrálhatók különböző kliens alkalmazásokkal.

## Áttekintés

Ez a lecke azt mutatja be, hogyan kell MCP szervereket építeni és használni a stdio transzporttal.

## Tanulási célok

A lecke végére képes leszel:

- MCP szervert építeni stdio transzport használatával.
- MCP szervert hibakeresni az Inspector segítségével.
- MCP szervert használni Visual Studio Code-ban.
- Megérteni a jelenlegi MCP transzport mechanizmusokat, és hogy miért ajánlott a stdio.


## stdio transzport – Működése

A stdio transzport az MCP specifikáció
`2026-07-28` két szabványos transzportja közül az egyik. Íme, hogyan működik:

- **Egyszerű kommunikáció**: A szerver JSON-RPC üzeneteket olvas a standard bemenetről (`stdin`) és üzeneteket küld a standard kimenetre (`stdout`).
- **Folyamat alapú**: A kliens a MCP szervert alfolyamként indítja.
- **Üzenet formátum**: Az üzenetek egyedi JSON-RPC kérések, értesítések vagy válaszok, sorvégekkel elválasztva.
- **Naplózás**: A szerver írhathat UTF-8 szövegeket a standard hibakimenetre (`stderr`) naplózási célból.

### Fő követelmények:
- Az üzeneteket sorvégeknek kell elválasztaniuk, és nem tartalmazhatnak beágyazott sortöréseket
- A szerver NEM írhat a `stdout`-ra olyan tartalmat, ami nem érvényes MCP üzenet
- A kliens NEM írhat a szerver `stdin`-jére olyan tartalmat, ami nem érvényes MCP üzenet

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

Az előző kódban:

- A MCP SDK-ból importáljuk a `Server` osztályt és a `StdioServerTransport`-ot
- Létrehozunk egy szerver példányt alap konfigurációval és képességekkel
- Létrehozunk egy `StdioServerTransport` példányt, és hozzákapcsoljuk a szervert, lehetővé téve a kommunikációt stdin/stdout-on keresztül

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

Az előző kódban:

- Létrehozunk egy szerver példányt az MCP SDK-val
- Eszközöket definiálunk dekorátorokkal
- A stdio_server kontextus-kezelőt használjuk a transzport kezelésére

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

A fő különbség az SSE-hez képest, hogy a stdio szerverek:

- Nem igényelnek webszerver beállítást vagy HTTP végpontokat
- A kliens alfolyamként indítja őket
- stdin/stdout csatornákon kommunikálnak
- Egyszerűbb őket megvalósítani és hibakeresni

## Gyakorlat: stdio szerver készítése

A szerver létrehozásakor két dolgot kell szem előtt tartanunk:

- Használnunk kell egy webszervert a kapcsolódási és üzenetküldési végpontok nyitásához.
## Labor: Egyszerű MCP stdio szerver készítése


Ebben a laborban létrehozunk egy egyszerű MCP szervert a javasolt stdio transzport használatával. Ez a szerver eszközöket fog elérhetővé tenni, amelyeket az ügyfelek a szabványos Model Context Protocol használatával hívhatnak meg.

### Előfeltételek

- Python 3.8 vagy újabb
- MCP Python SDK: `pip install mcp`
- Alapvető ismeretek az aszinkron programozásról

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

# Szerver létrehozása
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
    # stdio szállítás használata
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Fontos különbségek a már elavult SSE megközelítéshez képest

**Stdio transzport (Jelenlegi szabvány):**
- Egyszerű alfolyamat-modell – az ügyfél gyermekfolyamatként indítja a szervert
- Kommunikáció stdin/stdout-on keresztül JSON-RPC üzenetek használatával
- Nem szükséges HTTP szerver beállítása
- Jobb teljesítmény és biztonság
- Egyszerűbb hibakeresés és fejlesztés

**SSE transzport (Elavult 2025-06-18-tól MCP-ben):**
- HTTP szerver szükséges SSE végpontokkal
- Összetettebb beállítás web szerver infrastruktúrával
- További biztonsági megfontolások a HTTP végpontoknál
- Most a web alapú forgatókönyvekhez Streamable HTTP váltotta fel

### Szerver létrehozása stdio transzporttal

Ahhoz, hogy létrehozzuk a stdio szerverünket, a következőket kell tennünk:

1. **Importáljuk a szükséges könyvtárakat** – szükségünk van az MCP szerver komponensekre és a stdio transzportra
2. **Hozzuk létre a szerver példányt** – definiáljuk a szervert a képességeivel együtt
3. **Határozzuk meg az eszközöket** – adjuk hozzá a kívánt funkcionalitást
4. **Állítsuk be a transzportot** – konfiguráljuk az stdio kommunikációt
5. **Futtassuk a szervert** – indítsuk el a szervert és kezeljük az üzeneteket

Építsük meg lépésről lépésre:

### 1. lépés: Hozzunk létre egy alap stdio szervert

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

### 2. lépés: Adjuk hozzá további eszközöket

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

Mentsük el a kódot `server.py` néven, majd futtassuk a parancssorból:

```bash
python server.py
```

A szerver elindul és várja a bemenetet a stdin-ről. JSON-RPC üzenetekkel kommunikál az stdio transzport alatt.

### 4. lépés: Tesztelés az Inspectorral

Tesztelheted a szerveredet az MCP Inspector segítségével:

1. Telepítsd az Inspectort: `npx @modelcontextprotocol/inspector`
2. Futtasd az Inspectort, és irányítsd a szerveredre
3. Teszteld a létrehozott eszközöket

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Hibakeresés az stdio szerverednél

### Az MCP Inspector használata

Az MCP Inspector értékes eszköz az MCP szerverek hibakereséséhez és teszteléséhez. Íme, hogyan használd az stdio szervereddel:

1. **Telepítsd az Inspectort**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Futtasd az Inspectort**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Teszteld a szerveredet**: Az Inspector egy webes felületet biztosít, ahol:
   - Megtekintheted a szerver képességeit
   - Tesztelheted az eszközöket különböző paraméterekkel
   - Figyelheted a JSON-RPC üzeneteket
   - Hibakeresheted a kapcsolódási problémákat

### VS Code használata

Az MCP szerveredet közvetlenül a VS Code-ban is hibakeresheted:

1. Hozz létre egy indítási konfigurációt a `.vscode/launch.json` fájlban:
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

2. Állíts be töréspontokat a szerverkódodban
3. Futtasd a hibakeresőt és teszteld az Inspectornál

### Gyakori hibakeresési tippek

- Használd a `stderr`-t a naplózáshoz – soha ne írj a `stdout`-ra, mert az MCP üzeneteknek van fenntartva
- Győződj meg róla, hogy minden JSON-RPC üzenet sorvégekkel el van választva
- Először tesztelj egyszerű eszközökkel, mielőtt bonyolult funkcionalitást adnál hozzá

- Használd az Inspektort az üzenetformátumok ellenőrzésére

## A stdio szerver használata a VS Code-ban


Miután elkészítetted az MCP stdio szerveredet, integrálhatod azt a VS Code-dal, hogy Claude-dal vagy más MCP-kompatibilis klienssel használd.

### Konfiguráció

1. **Hozz létre egy MCP konfigurációs fájlt** a `%APPDATA%\Claude\claude_desktop_config.json` helyen (Windows) vagy `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Indítsd újra Claude-ot**: Zárd be és nyisd meg újra Claude-ot az új szerverkonfiguráció betöltéséhez.

3. **Teszteld a kapcsolatot**: Kezdj egy beszélgetést Claude-dal és próbáld ki a szervered eszközeit:
   - "Tudsz üdvözölni az üdvözlő eszközzel?"
   - "Számold ki a 15 és 27 összegét"
   - "Milyen információk vannak a szerverről?"

### TypeScript stdio szerver példa

Íme egy teljes TypeScript példa referencia célból:

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

## Összefoglaló

Ebben a frissített leckében megtanultad, hogyan lehet:

- MCP szervereket építeni a jelenlegi **stdio transport** használatával (ajánlott megközelítés)
- Megérteni, miért lett az SSE transport elavult a stdio és a Streamable HTTP javára
- Olyan eszközöket létrehozni, melyeket MCP kliensek hívhatnak meg
- Hibakeresni a szerveredet az MCP Inspectorral
- Integrálni a stdio szerveredet VS Code-dal és Claude-dal

A stdio transport egyszerűbb, biztonságosabb és hatékonyabb módot biztosít MCP szerverek építésére az elavult SSE megközelítéshez képest. Ez a javasolt transport a legtöbb MCP szerverimplementáció esetén a 2025-06-18 specifikáció alapján.


### .NET

1. Először hozzunk létre néhány eszközt, ehhez készítsünk egy *Tools.cs* fájlt a következő tartalommal:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Gyakorlat: A stdio szerver tesztelése

Most, hogy elkészítetted a stdio szerveredet, teszteld le, hogy helyesen működik-e.

### Előfeltételek

1. Győződj meg róla, hogy telepítve van az MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. A szerverkódod mentve legyen (pl. `server.py` néven)

### Tesztelés az Inspectorral

1. **Indítsd el az Inspectort a szervereddel**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Nyisd meg a webes felületet**: Az Inspector megnyit egy böngészőablakot, amely megjeleníti a szerver képességeit.

3. **Teszteld az eszközöket**: 
   - Próbáld ki a `get_greeting` eszközt különböző nevekkel
   - Teszteld a `calculate_sum` eszközt különböző számokkal
   - Hívd meg a `get_server_info` eszközt a szerver metaadatainak megtekintéséhez

4. **Figyeld a kommunikációt**: Az Inspector mutatja a kliens és a szerver között cserélt JSON-RPC üzeneteket.

### Amit látnod kell

Ha a szerver megfelelően indul el, akkor a következőket kell látnod:
- A szerver képességei felsorolva az Inspectorban
- Elérhető eszközök a teszteléshez
- Sikeres JSON-RPC üzenetcserék
- Az eszközválaszok megjelenítve a felületen

### Gyakori problémák és megoldások

**A szerver nem indul el:**
- Ellenőrizd, hogy minden függőség telepítve van-e: `pip install mcp`
- Ellenőrizd a Python szintaxisát és behúzásokat
- Nézd meg a konzolban az esetleges hibákat

**Nincs megjelenő eszköz:**
- Győződj meg arról, hogy a `@server.tool()` dekorátorok megvannak
- Ellenőrizd, hogy az eszközfüggvények definiálva vannak a `main()` előtt
- Győződj meg, hogy a szerver helyesen van konfigurálva

**Kapcsolati problémák:**
- Győződj meg arról, hogy a szerver helyesen használja a stdio transportot
- Ellenőrizd, hogy más folyamatok nem zavarják-e
- Ellenőrizd az Inspector parancssori szintaxisát

## Feladat

Próbálj meg több képességgel bővíteni a szerveredet. Nézd meg [ezt az oldalt](https://api.chucknorris.io/) például egy olyan eszköz hozzáadásához, amely API-t hív meg. Te döntöd el, hogyan nézzen ki a szerver. Jó szórakozást :)
## Megoldás

[Megoldás](./solution/README.md) Itt található egy lehetséges megoldás működő kóddal.

## Főbb tanulságok

A fejezet főbb tanulságai a következők:

- A stdio transport a javasolt mechanizmus helyi MCP szerverekhez.
- A stdio transport lehetővé teszi az MCP szerverek és kliensek közötti zökkenőmentes kommunikációt a standard bemeneti és kimeneti folyamok használatával.
- Használhatod az Inspectort és a Visual Studio Code-ot is stdio szerverek közvetlen fogyasztására, megkönnyítve a hibakeresést és az integrációt.

## Minták

- [Java számológép](../samples/java/calculator/README.md)
- [.Net számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript számológép](../samples/javascript/README.md)
- [TypeScript számológép](../samples/typescript/README.md)
- [Python számológép](../../../../03-GettingStarted/samples/python) 

## További források

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mi következik

## Következő lépések

Most, hogy megtanultad, hogyan lehet MCP szervereket építeni a stdio transporttal, felfedezhetsz fejlettebb témákat:

- **Következő**: [HTTP Streaming az MCP-vel (Streamable HTTP)](../06-http-streaming/README.md) - Ismerd meg a távoli szerverek másik támogatott transzport mechanizmusát
- **Haladó**: [MCP biztonsági legjobb gyakorlatok](../../02-Security/README.md) - Biztonság implementálása az MCP szervereidben
- **Termelési**: [Telepítési stratégiák](../09-deployment/README.md) - Szervereid telepítése éles használatra

## További források

- [MCP specifikáció 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Aktualis specifikáció
- [MCP SDK dokumentáció](https://github.com/modelcontextprotocol/sdk) - SDK referencia minden nyelvhez
- [Közösségi példák](../../06-CommunityContributions/README.md) - Több szerver példa a közösségtől

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->