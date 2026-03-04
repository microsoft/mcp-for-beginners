# MCP Server a stdio Transporttal

> **⚠️ Fontos frissítés**: Az MCP Specification 2025-06-18 óta a különálló SSE (Server-Sent Events) transport **elavulttá vált**, és helyette a "Streamable HTTP" transport lépett életbe. A jelenlegi MCP specifikáció két fő transzport mechanizmust definiál:
> 1. **stdio** - Szabványos bemenet/kimenet (helyi szerverekhez ajánlott)
> 2. **Streamable HTTP** - Távoli szerverekhez, amelyek belsőleg SSE-t használhatnak
>
> Ez a lecke frissítve lett, hogy a **stdio transzportra** koncentráljon, mely a legtöbb MCP szerver implementáció számára ajánlott megközelítés.

A stdio transport lehetővé teszi az MCP szerverek számára, hogy a klienssel a szabványos bemeneti és kimeneti adatfolyamokon keresztül kommunikáljanak. Ez a leggyakrabban használt és ajánlott transzport mechanizmus a jelenlegi MCP specifikációban, mely egy egyszerű és hatékony módszert kínál MCP szerverek építésére, amelyek könnyen integrálhatók különféle kliens alkalmazásokkal.

## Áttekintés

Ebben a leckében azt tanuljuk meg, hogyan kell MCP szervereket építeni és használni a stdio transport segítségével.

## Tanulási célok

A lecke végére képes leszel:

- MCP szervert készíteni stdio transzport használatával.
- Hibakeresni egy MCP szervert a Inspector használatával.
- Használni egy MCP szervert Visual Studio Code-ból.
- Megérteni a jelenlegi MCP transzport mechanizmusokat, és hogy miért ajánlott a stdio.

## stdio Transport - Működése

A stdio transport a jelenlegi MCP specifikációban (2025-06-18) támogatott két transzport típus egyike. Íme, hogyan működik:

- **Egyszerű kommunikáció**: A szerver a JSON-RPC üzeneteket a szabványos bemenetről (`stdin`) olvassa, és a szabványos kimenetre (`stdout`) küldi az üzeneteket.
- **Folyamat alapú**: A kliens alfolyamatként indítja az MCP szervert.
- **Üzenetformátum**: Az üzenetek egyenként JSON-RPC kérések, értesítések vagy válaszok, amelyek új sorral vannak elválasztva.
- **Naplózás**: A szerver LEHET, hogy UTF-8 stringeket ír a szabványos hibakimenetre (`stderr`) naplózási célból.

### Fő követelmények:
- Az üzenetek ÚJ SORRAL kell hogy el legyenek választva, és NEM tartalmazhatnak beágyazott új sorokat
- A szerver NEM ÍRHAT a `stdout`-ra semmit, ami nem érvényes MCP üzenet
- A kliens NEM ÍRHAT a szerver `stdin`-jére semmit, ami nem érvényes MCP üzenet

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

- Importáljuk a `Server` osztályt és a `StdioServerTransport`-ot az MCP SDK-ból
- Létrehozunk egy szerver példányt alap konfigurációval és képességekkel

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

- Az MCP SDK használatával létrehozunk egy szerver példányt
- Dekorátorokat használunk az eszközök definiálásához
- A stdio_server kontextusmenedzsert használjuk a transzport kezelésére

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
- A kliens indítja őket alfolyamatként
- A stdin/stdout adatfolyamokon keresztül kommunikálnak
- Egyszerűbbek megvalósításban és hibakeresésben

## Gyakorlat: stdio szerver létrehozása

Ahhoz, hogy létrehozzuk a szerverünket, két dolgot kell szem előtt tartanunk:

- Webszervert kell használnunk a kapcsolat és az üzenetek végpontjainak kitetésére.

## Labor: Egyszerű MCP stdio szerver létrehozása

Ebben a laborban egy egyszerű MCP szervert készítünk a javasolt stdio transzporttal. Ez a szerver eszközöket fog nyújtani, amelyeket a kliensek a szabványos Model Context Protocol segítségével hívhatnak meg.

### Előfeltételek

- Python 3.8 vagy újabb
- MCP Python SDK: `pip install mcp`
- Aszinkron programozás alapjai

Kezdjük az első MCP stdio szerverünk létrehozásával:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Naplózás beállítása
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
  
## Fő különbségek a megszűnt SSE megközelítéssel szemben

**Stdio Transzport (Jelenlegi szabvány):**
- Egyszerű alfolyamat modell - a kliens indul a szerver alfolyamatként
- Kommunikáció stdin/stdout-on JSON-RPC üzenetekkel
- Nincs szükség HTTP szerver beállításra
- Jobb teljesítmény és biztonság
- Könnyebb hibakeresés és fejlesztés

**SSE Transzport (Amely 2025-06-18-tól elavult):**
- HTTP szervert igényelt SSE végpontokkal
- Bonyolultabb web szerver infrastruktúra beállítása
- További biztonsági megfontolások HTTP végpontokra vonatkozóan
- Most már helyettesíti a Streamable HTTP a web alapú szcenáriókhoz

### stdio transzporttal szerver létrehozása

A stdio szerver létrehozásához:

1. **Szükséges könyvtárak importálása** - Szükségünk van az MCP szerver komponenseire és a stdio transzportra
2. **Szerver példány létrehozása** - Definiáljuk a szervert a képességeivel
3. **Eszközök definiálása** - Hozzáadjuk a kitettségként kívánt funkciókat
4. **Transzport beállítása** - Konfiguráljuk a stdio kommunikációt
5. **Szerver futtatása** - Elindítjuk a szervert és kezeljük az üzeneteket

Építsük fel lépésről lépésre:

### 1. lépés: Egyszerű stdio szerver létrehozása

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Naplózás beállítása
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
  
A szerver elindul és várja a bemenetet a stdin-ről. JSON-RPC üzeneteket használ a stdio transporton keresztül.

### 4. lépés: Tesztelés az Inspectorrall

Tesztelheti a szerverét az MCP Inspectorral:

1. Telepítse az Inspectort: `npx @modelcontextprotocol/inspector`
2. Indítsa el az Inspectort, és irányítsa a szerverére
3. Tesztelje a létrehozott eszközöket

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
  
## Hibakeresés stdio szerverrel

### MCP Inspector használata

Az MCP Inspector hasznos eszköz az MCP szerverek hibakeresésére és tesztelésére. Így használhatja stdio szerverével:

1. **Inspector telepítése**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **Inspector futtatása**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **Szerver tesztelése**: Az Inspector webes felületet biztosít, ahol megteheti a következőket:
   - Megtekintheti a szerver képességeit
   - Tesztelheti az eszközöket különböző paraméterekkel
   - Figyelheti a JSON-RPC üzeneteket
   - Hibakeresheti a kapcsolódási problémákat

### VS Code használata

Szerverét közvetlenül VS Code-ban is hibakeresheti:

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
3. Futtassa a hibakeresőt és teszteljen az Inspectorral

### Gyakori hibakeresési tippek

- Használja a `stderr`-t naplózásra - soha ne írjon a `stdout`-ra, mert az MCP üzeneteket tartalmaz
- Győződjön meg róla, hogy minden JSON-RPC üzenet új sorral van elválasztva
- Először egyszerű eszközökkel teszteljen, mielőtt bonyolult funkciókat adna hozzá
- Ellenőrizze az Inspectorral az üzenet formátumokat

## stdio szerver használata VS Code-ban

Miután elkészítette MCP stdio szerverét, integrálhatja azt VS Code-dal, hogy Claude-dal vagy más MCP-kompatibilis klienssel használhassa.

### Beállítás

1. **Hozzon létre egy MCP konfigurációs fájlt** a `%APPDATA%\Claude\claude_desktop_config.json` (Windows) vagy `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) útvonalra:

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
  
2. **Indítsa újra Claudet**: Zárja be és nyissa meg újra Claude-ot az új szerverkonfiguráció betöltéséhez.

3. **Tesztelje a kapcsolatot**: Kezdjen beszélgetést Claude-dal, és próbálja ki a szerver eszközeit:
   - „Tudnál üdvözölni az üdvözlő eszköz használatával?”
   - „Számold ki 15 és 27 összegét”
   - „Mi az információ a szerverről?”

### TypeScript stdio szerver példa

Íme egy teljes TypeScript példa referencia céljából:

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
  
## Összegzés

Ebben a frissített leckében megtanultad, hogyan:

- Építs MCP szervereket a jelenlegi **stdio transzporttal** (ajánlott megközelítés)
- Megértsd, miért lett az SSE transzport elavult a stdio és a Streamable HTTP javára
- Készíts eszközöket, amelyeket MCP kliensek hívhatnak
- Hibakeress a szervereden az MCP Inspectorral
- Integráld a stdio szervered VS Code-dal és Claudéval

A stdio transport egyszerűbb, biztonságosabb és jobb teljesítményű módot kínál MCP szerver építésére, mint a megszűnt SSE megközelítés. Ez a javasolt transzport a legtöbb MCP szerver implementáció számára a 2025-06-18-as specifikáció szerint.

### .NET

1. Először készítsünk néhány eszközt, ehhez létrehozunk egy *Tools.cs* fájlt a következő tartalommal:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## Gyakorlat: stdio szerver tesztelése

Most, hogy elkészítetted a stdio szerveredet, teszteljük le, hogy helyesen működik-e.

### Előfeltételek

1. Győződj meg róla, hogy telepítve van az MCP Inspector:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. A szerver kódja legyen elmentve (pl. `server.py`)

### Tesztelés az Inspectorral

1. **Indítsd el az Inspectort a szervereddel**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **Nyisd meg a webes felületet**: Az Inspector megnyit egy böngészőablakot, amely megjeleníti a szerver képességeit.

3. **Teszteld az eszközöket**:  
   - Próbáld ki a `get_greeting` eszközt különböző nevekkel  
   - Teszteld a `calculate_sum` eszközt különféle számokkal  
   - Hívd meg a `get_server_info` eszközt a szerver metaadata megtekintéséhez

4. **Figyeld a kommunikációt**: Az Inspector mutatja a kliens és a szerver közötti JSON-RPC üzenetváltást.

### Amit látnod kell

Ha a szerver helyesen indul el, a következőket kell látnod:
- A szerver képességeinek listáját az Inspectorban
- Elérhető eszközök a teszthez
- Sikeres JSON-RPC üzenetváltásokat
- Az eszköz válaszainak megjelenítését az interfészen

### Gyakori problémák és megoldások

**A szerver nem indul el:**
- Ellenőrizd, hogy minden függőség telepítve van: `pip install mcp`
- Ellenőrizd a Python szintaxist és a behúzást
- Nézz hibakódokat a konzolon

**Nem jelennek meg az eszközök:**
- Győződj meg róla, hogy az `@server.tool()` dekorátorok jelen vannak
- Ellenőrizd, hogy a tool funkciók a `main()` előtt vannak definiálva
- Ellenőrizd a szerver helyes konfigurációját

**Kapcsolódási problémák:**
- Bizonyosodj meg róla, hogy a stdio transzportot helyesen használja a szerver
- Ellenőrizd, hogy más folyamatok nem zavarják
- Ellenőrizd az Inspector parancssori szintaxisát

## Feladat

Próbálj meg további képességeket hozzáadni a szerveredhez. Nézd meg [ezt az oldalt](https://api.chucknorris.io/), például készíts egy olyan eszközt, ami egy API-t hív meg. Te döntöd el, hogyan nézzen ki a szerver. Jó szórakozást :)

## Megoldás

[Megoldás](./solution/README.md) Itt egy lehetséges megoldás működő kóddal.

## Főbb tanulságok

A fejezet legfontosabb tanulságai:

- A stdio transport az ajánlott megoldás a helyi MCP szerverekhez.
- A stdio transzport zökkenőmentes kommunikációt biztosít az MCP szerverek és kliensek között a szabványos bemenet és kimenet adatfolyamokon keresztül.
- Az Inspector és a Visual Studio Code is használható stdio szerverek közvetlen elérésére, megkönnyítve ezzel a hibakeresést és az integrációt.

## Minták

- [Java Számológép](../samples/java/calculator/README.md)
- [.Net Számológép](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Számológép](../samples/javascript/README.md)
- [TypeScript Számológép](../samples/typescript/README.md)
- [Python Számológép](../../../../03-GettingStarted/samples/python)

## További források

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Mi következik

## Következő lépések

Most, hogy megtanultad, hogyan kell MCP szervereket építeni stdio transzporttal, továbbléphetsz fejlettebb témák felé:

- **Következő**: [HTTP Streaming az MCP-vel (Streamable HTTP)](../06-http-streaming/README.md) - Ismerd meg a másik támogatott transzport mechanizmust távoli szerverekhez
- **Haladó**: [MCP Biztonsági legjobb gyakorlatok](../../02-Security/README.md) - Biztonság megvalósítása MCP szervereken
- **Éles üzem**: [Kiszolgáló telepítési stratégiák](../09-deployment/README.md) - Szervereid éles környezetbe való telepítése

## További források

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Hivatalos specifikáció
- [MCP SDK Dokumentáció](https://github.com/modelcontextprotocol/sdk) - SDK dokumentáció minden nyelvhez
- [Közösségi példák](../../06-CommunityContributions/README.md) - További szerver példák a közösségtől

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ez a dokumentum a [Co-op Translator](https://github.com/Azure/co-op-translator) nevű mesterséges intelligencia fordító szolgáltatás segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum, annak eredeti nyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->