# MCP Server gamit ang stdio Transport

> **⚠️ Mahalagang Update**: Mula sa MCP Specification 2025-06-18, ang standalone na SSE (Server-Sent Events) transport ay **deprecated** na at pinalitan ng "Streamable HTTP" transport. Ang kasalukuyang MCP specification ay naglalarawan ng dalawang pangunahing mekanismo ng transport:
> 1. **stdio** - Standard input/output (inirerekomenda para sa mga lokal na server)
> 2. **Streamable HTTP** - Para sa mga remote na server na maaaring gumamit ng SSE internally
>
> Ang araling ito ay na-update upang tutukan ang **stdio transport**, na inirerekomendang paraan para sa karamihan ng mga pagsasakatuparan ng MCP server.

Pinapayagan ng stdio transport ang mga MCP server na makipag-ugnayan sa mga kliyente sa pamamagitan ng standard input at output streams. Ito ang pinaka-karaniwang ginagamit at inirerekomendang mekanismo ng transport sa kasalukuyang MCP specification, na nagbibigay ng isang simple at epektibong paraan upang bumuo ng mga MCP server na madaling maisama sa iba't ibang mga aplikasyon ng kliyente.

## Pangkalahatang-ideya

Tatalakayin sa araling ito kung paano bumuo at gumamit ng MCP Servers gamit ang stdio transport.

## Mga Layunin sa Pagkatuto

Pagkatapos ng araling ito, magagawa mong:

- Bumuo ng MCP Server gamit ang stdio transport.
- Mag-debug ng MCP Server gamit ang Inspector.
- Gumamit ng MCP Server gamit ang Visual Studio Code.
- Maunawaan ang kasalukuyang mga mekanismo ng MCP transport at kung bakit inirerekomenda ang stdio.

## stdio Transport - Paano Ito Gumagana

Ang stdio transport ay isa sa dalawang suportadong uri ng transport sa kasalukuyang MCP specification (2025-06-18). Ganito ang paraan ng trabaho nito:

- **Simpleng Komunikasyon**: Binabasa ng server ang mga JSON-RPC na mensahe mula sa standard input (`stdin`) at nagpapadala ng mga mensahe sa standard output (`stdout`).
- **Batay sa Proseso**: Inilulunsad ng kliyente ang MCP server bilang subprocess.
- **Format ng Mensahe**: Ang mga mensahe ay indibidwal na mga JSON-RPC na kahilingan, notipikasyon, o tugon, na hinihiwalay ng mga bagong linya.
- **Pag-logging**: Maaari ang server na magsulat ng UTF-8 na mga string sa standard error (`stderr`) para sa mga layunin ng pag-log.

### Pangunahing Mga Kinakailangan:
- Ang mga mensahe AY DAPAT mahati gamit ang mga bagong linya at HINDI DAPAT maglaman ng mga embedded na bagong linya
- Ang server AY HINDI DAPAT magsulat ng anumang hindi wastong MCP na mensahe sa `stdout`
- Ang kliyente AY HINDI DAPAT magsulat ng anumang hindi wastong MCP na mensahe sa `stdin` ng server

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

Sa naunang code:

- Ina-import namin ang `Server` na klase at `StdioServerTransport` mula sa MCP SDK
- Gumagawa kami ng isang instance ng server na may pangunahing konfigurasyon at kakayahan

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Lumikha ng halimbawa ng server
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

Sa naunang code ay:

- Gumagawa ng isang server instance gamit ang MCP SDK
- Nagtatakda ng mga tool gamit ang mga dekorador
- Ginagamit ang stdio_server context manager upang hawakan ang transport

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

Ang pangunahing pagkakaiba sa SSE ay ang stdio servers:

- Hindi nangangailangan ng setup ng web server o HTTP endpoints
- Inilulunsad bilang mga subprocess ng kliyente
- Nakikipag-ugnayan sa pamamagitan ng stdin/stdout streams
- Mas simple i-implementa at i-debug

## Ehersisyo: Paglikha ng stdio Server

Para gumawa ng aming server, kailangan naming tandaan ang dalawang bagay:

- Kailangan naming gumamit ng web server para i-expose ang mga endpoint para sa koneksyon at mga mensahe.

## Lab: Paglikha ng simpleng MCP stdio server

Sa lab na ito, gagawa tayo ng isang simpleng MCP server gamit ang inirerekomendang stdio transport. I-expose ng server na ito ang mga tool na maaaring tawagin ng mga kliyente gamit ang standard Model Context Protocol.

### Mga Kinakailangan

- Python 3.8 o mas bago
- MCP Python SDK: `pip install mcp`
- Pangunahing kaalaman sa async programming

Simulan natin sa paggawa ng unang MCP stdio server:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# I-configure ang pag-log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gumawa ng server
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
    # Gamitin ang stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Pangunahing Pagkakaiba mula sa deprecated na SSE na paraan

**Stdio Transport (Kasalukuyang Pamantayan):**
- Simpleng subprocess model - inilulunsad ng kliyente ang server bilang child process
- Komunikasyon sa pamamagitan ng stdin/stdout gamit ang mga JSON-RPC na mensahe
- Hindi kailangan ng HTTP server setup
- Mas maganda ang performance at seguridad
- Mas madali ang debugging at development

**SSE Transport (Deprecated mula sa MCP 2025-06-18):**
- Kinakailangan ang HTTP server na may SSE endpoints
- Mas kumplikadong setup gamit ang web server infrastructure
- Karagdagang konsiderasyon sa seguridad para sa mga HTTP endpoints
- Pinalitan na ngayon ng Streamable HTTP para sa mga web-based na senaryo

### Paglikha ng server gamit ang stdio transport

Para gumawa ng aming stdio server, kailangan naming:

1. **I-import ang mga kinakailangang library** - Kailangan namin ang MCP server components at stdio transport
2. **Gumawa ng server instance** - Itakda ang server kasama ang mga kakayahan nito
3. **Tukuyin ang mga tool** - Idagdag ang functionality na nais naming i-expose
4. **I-set up ang transport** - Isaayos ang stdio komunikasyon
5. **Patakbuhin ang server** - Simulan ang server at hawakan ang mga mensahe

Gawin natin ito ng sunud-sunod:

### Hakbang 1: Gumawa ng basic na stdio server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Isaayos ang pag-log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gumawa ng server
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

### Hakbang 2: Magdagdag pa ng mga tool

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

### Hakbang 3: Patakbuhin ang server

I-save ang code bilang `server.py` at patakbuhin ito mula sa command line:

```bash
python server.py
```

Magsisimula ang server at maghihintay ng input mula sa stdin. Nakikipag-usap ito gamit ang mga JSON-RPC na mensahe sa stdio transport.

### Hakbang 4: Pagsubok gamit ang Inspector

Maaari mong subukan ang iyong server gamit ang MCP Inspector:

1. I-install ang Inspector: `npx @modelcontextprotocol/inspector`
2. Patakbuhin ang Inspector at ituro ito sa iyong server
3. Subukan ang mga tool na iyong ginawa

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Pag-debug ng iyong stdio server

### Paggamit ng MCP Inspector

Ang MCP Inspector ay isang mahalagang tool para sa pag-debug at pagsusuri ng MCP servers. Narito kung paano ito gamitin kasama ng iyong stdio server:

1. **I-install ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Patakbuhin ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Subukan ang iyong server**: Nagbibigay ang Inspector ng web interface kung saan maaari mong:
   - Tingnan ang kakayahan ng server
   - Subukan ang mga tool gamit ang iba't ibang mga parametro
   - Bantayan ang mga JSON-RPC na mensahe
   - I-debug ang mga isyu sa koneksyon

### Paggamit ng VS Code

Maaari mo ring i-debug ang iyong MCP server nang direkta sa VS Code:

1. Gumawa ng launch configuration sa `.vscode/launch.json`:
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

2. Maglagay ng breakpoints sa iyong code ng server
3. Patakbuhin ang debugger at subukan gamit ang Inspector

### Karaniwang mga tip para sa pag-debug

- Gamitin ang `stderr` para sa pag-log - huwag magsulat sa `stdout` dahil nakalaan ito para sa MCP na mga mensahe
- Siguraduhing lahat ng mga JSON-RPC na mensahe ay newline-delimited
- Subukan muna gamit ang simpleng mga tool bago magdagdag ng komplikadong functionality
- Gamitin ang Inspector upang siguraduhing tama ang format ng mga mensahe

## Paggamit ng iyong stdio server sa VS Code

Kapag nagawa mo na ang iyong MCP stdio server, maaari mo itong isama sa VS Code upang magamit kasama si Claude o ibang MCP-compatible na mga kliyente.

### Konfigurasyon

1. **Gumawa ng MCP configuration file** sa `%APPDATA%\Claude\claude_desktop_config.json` (Windows) o `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **I-restart si Claude**: Isara at buksan muli si Claude upang ma-load ang bagong konfigurasyon ng server.

3. **Subukan ang koneksyon**: Magsimula ng pag-uusap kay Claude at subukan ang mga tool ng iyong server:
   - "Pwede mo ba akong batiin gamit ang greeting tool?"
   - "Kalkulahin ang suma ng 15 at 27"
   - "Ano ang impormasyon ng server?"

### Halimbawa ng TypeScript stdio server

Narito ang kumpletong halimbawa ng TypeScript para sa sanggunian:

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

// Magdagdag ng mga kasangkapan
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

### Halimbawa ng .NET stdio server

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

## Buod

Sa na-update na araling ito, natutunan mo kung paano:

- Bumuo ng MCP servers gamit ang kasalukuyang **stdio transport** (inirerekomendang paraan)
- Maunawaan kung bakit ang SSE transport ay na-deprecate pabor sa stdio at Streamable HTTP
- Gumawa ng mga tool na maaaring tawagin ng MCP clients
- Mag-debug ng server gamit ang MCP Inspector
- Isama ang iyong stdio server sa VS Code at Claude

Ang stdio transport ay nagbibigay ng mas simple, mas ligtas, at mas mahusay na performance na paraan upang bumuo ng MCP servers kumpara sa deprecated na SSE na paraan. Ito ang inirerekomendang transport para sa karamihan ng mga pagsasakatuparan ng MCP server mula sa 2025-06-18 na specification.

### .NET

1. Unahin nating gumawa ng mga tool, para dito gagawa tayo ng file *Tools.cs* na may sumusunod na nilalaman:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ehersisyo: Pagsubok ng iyong stdio server

Ngayon na nagawa mo na ang iyong stdio server, subukan natin ito upang matiyak na gumagana nang tama.

### Mga Kinakailangan

1. Siguraduhing naka-install ang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ang iyong server code ay dapat naisave (hal., bilang `server.py`)

### Pagsubok gamit ang Inspector

1. **Simulan ang Inspector kasama ang iyong server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buksan ang web interface**: Magbubukas ang Inspector ng browser window na nagpapakita ng kakayahan ng iyong server.

3. **Subukan ang mga tool**: 
   - Subukan ang `get_greeting` tool gamit ang iba't ibang mga pangalan
   - Subukan ang `calculate_sum` tool gamit ang iba't ibang mga numero
   - Tawagin ang `get_server_info` tool upang makita ang metadata ng server

4. **Bantayan ang komunikasyon**: Ipinapakita ng Inspector ang mga JSON-RPC na mensahe na ipinagpapalit sa pagitan ng kliyente at server.

### Ano ang dapat mong makita

Kapag nagsimula nang tama ang iyong server, dapat mong makita:
- Listahan ng kakayahan ng server sa Inspector
- Mga magagamit na tool para sa pagsusuri
- Matagumpay na pagpapalitan ng JSON-RPC na mga mensahe
- Mga tugon ng tool na ipinapakita sa interface

### Karaniwang mga isyu at mga solusyon

**Hindi nagsisimula ang server:**
- Suriin na lahat ng dependencies ay naka-install: `pip install mcp`
- I-verify ang syntax at indentation ng Python
- Hanapin ang mga mensahe ng error sa console

**Hindi lumalabas ang mga tool:**
- Siguraduhing naroroon ang `@server.tool()` decorators
- Suriin na ang mga function ng tool ay tinukoy bago ang `main()`
- I-verify na maayos ang pagkakakonfigure ng server

**Mga isyu sa koneksyon:**
- Siguraduhing tama ang paggamit ng stdio transport ng server
- Suriin kung may ibang proseso na nakakaapekto
- I-verify ang syntax ng command ng Inspector

## Takdang-aralin

Subukan mong palawakin ang iyong server gamit ang mas maraming kakayahan. Tingnan ang [pahina na ito](https://api.chucknorris.io/) upang, halimbawa, magdagdag ng tool na tumatawag ng API. Ikaw ang magpapasya kung paano ang itsura ng server. Mag-enjoy!

## Solusyon

[Solusyon](./solution/README.md) Narito ang isang posibleng solusyon na may gumaganang code.

## Pangunahing Mga Natutunan

Ang pangunahing mga natutunan mula sa kabanatang ito ay ang mga sumusunod:

- Ang stdio transport ay ang inirerekomendang mekanismo para sa mga lokal na MCP server.
- Pinapayagan ng stdio transport ang tuloy-tuloy na komunikasyon sa pagitan ng mga MCP server at kliyente gamit ang standard na input at output streams.
- Maaari mong gamitin parehong Inspector at Visual Studio Code upang direktang gamitin ang mga stdio server, kaya't madali ang pag-debug at pagsasama.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Karagdagang mga Mapagkukunan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Ano ang Susunod

## Mga Susunod na Hakbang

Ngayon na natutunan mo kung paano bumuo ng MCP servers gamit ang stdio transport, maaari mong tuklasin ang mas advanced na mga paksa:

- **Susunod**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Alamin ang isa pang suportadong mekanismo ng transport para sa mga remote na server
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Ipatupad ang seguridad sa iyong mga MCP server
- **Produksyon**: [Deployment Strategies](../09-deployment/README.md) - I-deploy ang iyong mga server para sa paggamit sa produksyon

## Karagdagang mga Mapagkukunan

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Opisyal na specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Mga reference sa SDK para sa lahat ng mga wika
- [Mga Halimbawa mula sa Komunidad](../../06-CommunityContributions/README.md) - Higit pang mga halimbawa ng server mula sa komunidad

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paalala**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapang maging tumpak ang salin, mangyaring maunawaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na bahagi. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->