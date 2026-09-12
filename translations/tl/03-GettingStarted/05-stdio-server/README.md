# MCP Server gamit ang stdio Transport

> **⚠️ Mahalagang Update**: Simula sa MCP Specification 2025-06-18, ang standalone SSE (Server-Sent Events) transport ay **deprecated** na at pinalitan ng "Streamable HTTP" transport. Ang kasalukuyang MCP specification ay naglalarawan ng dalawang pangunahing mekanismo ng transport:
> 1. **stdio** - Standard input/output (inirerekomenda para sa mga lokal na server)
> 2. **Streamable HTTP** - Para sa mga remote na server na maaaring gumamit ng SSE nang panloob
>
> Ang araling ito ay na-update upang tumutok sa **stdio transport**, na inirerekomenda para sa karamihan ng mga implementasyon ng MCP server.

Pinapayagan ng stdio transport ang mga MCP server na makipag-ugnayan sa mga kliyente sa pamamagitan ng standard input at output streams. Ito ang pinakaginagamit at inirerekomendang mekanismo ng transport sa kasalukuyang MCP specification, na nagbibigay ng isang simple at mahusay na paraan upang bumuo ng MCP servers na madaling maisama sa iba't ibang aplikasyon ng kliyente.

## Pangkalahatang Pagsusuri

Tinuturo sa araling ito kung paano bumuo at gamitin ang MCP Servers gamit ang stdio transport.

## Mga Layunin ng Pag-aaral

Sa pagtatapos ng araling ito, magagawa mong:

- Bumuo ng MCP Server gamit ang stdio transport.
- Mag-debug ng MCP Server gamit ang Inspector.
- Gumamit ng MCP Server gamit ang Visual Studio Code.
- Maunawaan ang kasalukuyang MCP transport mechanisms at kung bakit inirerekomenda ang stdio.


## stdio Transport - Paano Ito Gumagana

Ang stdio transport ay isa sa dalawang standard na transport sa MCP Specification
`2026-07-28`. Ganito ang pag-andar nito:

- **Simple na Komunikasyon**: Binabasa ng server ang mga mensaheng JSON-RPC mula sa standard input (`stdin`) at nagpapadala ng mga mensahe sa standard output (`stdout`).
- **Batay sa Proseso**: Pinapaandar ng kliyente ang MCP server bilang subprocess.
- **Format ng Mensahe**: Ang mga mensahe ay hiwalay na JSON-RPC requests, notifications, o responses, na hinahati ng bagong linya.
- **Pag-log**: Maaaring magsulat ang server ng UTF-8 na mga string sa standard error (`stderr`) para sa layunin ng pag-log.

### Pangunahing Mga Kinakailangan:
- DAPAT ang mga mensahe ay hinati ng mga bagong linya at HINDI DAPAT maglaman ng mga naka-embed na bagong linya
- HINDI DAPAT magsulat ang server ng anumang bagay sa `stdout` na hindi valid na mensahe ng MCP
- HINDI DAPAT magsulat ang kliyente ng anumang bagay sa `stdin` ng server na hindi valid na mensahe ng MCP

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

Sa nakaraang code:

- Nag-import tayo ng `Server` class at `StdioServerTransport` mula sa MCP SDK
- Gumawa tayo ng server instance na may basic na configuration at capabilities
- Gumawa tayo ng `StdioServerTransport` instance at ikinonekta ang server dito, na nagpapahintulot ng komunikasyon sa stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Gumawa ng instance ng server
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

Sa nakaraang code ginawa natin:

- Gumawa ng server instance gamit ang MCP SDK
- Nagdeklara ng mga tools gamit ang mga decorators
- Ginamit ang stdio_server context manager upang pangasiwaan ang transport

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

Ang pangunahing kaibahan sa SSE ay ang mga stdio server ay:

- Hindi nangangailangan ng web server setup o HTTP endpoints
- Pinapaandar bilang subprocesses ng kliyente
- Nakikipagkomunika sa pamamagitan ng stdin/stdout streams
- Mas simple i-implement at i-debug

## Ehersisyo: Paglikha ng stdio Server

Para gumawa ng ating server, kailangan nating tandaan ang dalawang bagay:

- Kailangan nating gumamit ng web server upang i-expose ang mga endpoints para sa koneksyon at mga mensahe.
## Lab: Paglikha ng simple MCP stdio server

Sa lab na ito, gagawa tayo ng simpleng MCP server gamit ang inirerekomendang stdio transport. Ipapakita ng server na ito ang mga tools na maaaring tawagin ng mga kliyente gamit ang standard Model Context Protocol.

### Mga Kinakailangan

- Python 3.8 o mas bago
- MCP Python SDK: `pip install mcp`
- Batayang kaalaman sa async programming

Magsimula tayo sa paggawa ng unang MCP stdio server:

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

## Mga Pangunahing Kaibahan mula sa deprecated SSE approach

**Stdio Transport (Kasalukuyang Standard):**
- Simple na subprocess model - ang kliyente ang nagpapalay ng server bilang child process
- Komunikasyon gamit ang stdin/stdout na may JSON-RPC na mga mensahe
- Hindi kailangan ng HTTP server setup
- Mas mahusay sa performance at seguridad
- Mas madaling i-debug at i-develop

**SSE Transport (Deprecated simula MCP 2025-06-18):**
- Kinakailangang HTTP server na may SSE endpoints
- Mas kumplikadong setup kasama ang web server infrastructure
- May dagdag seguridad na mga konsiderasyon para sa HTTP endpoints
- Pinalitan na ngayon ng Streamable HTTP para sa web-based na mga scenario

### Paglikha ng server gamit ang stdio transport

Para gumawa ng stdio server, kailangan nating:

1. **I-import ang mga kinakailangang library** - Kailangan natin ang MCP server components at stdio transport
2. **Gumawa ng server instance** - Tukuyin ang server kasama ang mga kakayahan nito
3. **Magdeklara ng mga tools** - Idagdag ang mga functionality na nais nating i-expose
4. **I-setup ang transport** - I-configure ang stdio communication
5. **Patakbuhin ang server** - Simulan ang server at pangasiwaan ang mga mensahe

Gawin natin ito ng hakbang-hakbang:

### Hakbang 1: Gumawa ng basic na stdio server

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# I-configure ang pag-log
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

### Hakbang 2: Magdagdag ng mga tools

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

Magsisimula ang server at maghihintay ng input mula sa stdin. Nakikipagkomunika ito gamit ang JSON-RPC messages sa stdio transport.

### Hakbang 4: Subukan gamit ang Inspector

Maaari mong subukan ang iyong server gamit ang MCP Inspector:

1. I-install ang Inspector: `npx @modelcontextprotocol/inspector`
2. Patakbuhin ang Inspector at itutok ito sa iyong server
3. Subukan ang mga tools na ginawa mo

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Pag-debug ng iyong stdio server

### Paggamit ng MCP Inspector

Mahalaga ang MCP Inspector para sa pag-debug at pagsubok ng MCP servers. Ganito ito gamitin sa iyong stdio server:

1. **I-install ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Patakbuhin ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Subukan ang iyong server**: Nagbibigay ang Inspector ng web interface kung saan maaari mong:
   - Tingnan ang mga kakayahan ng server
   - Subukan ang mga tools gamit ang iba't ibang parameters
   - Bantayan ang mga JSON-RPC messages
   - I-debug ang mga problema sa koneksyon

### Paggamit ng VS Code

Maaari mo ring i-debug nang direkta ang iyong MCP server sa VS Code:

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

2. Maglagay ng mga breakpoint sa iyong server code
3. Patakbuhin ang debugger at subukan gamit ang Inspector

### Mga karaniwang tips sa pag-debug

- Gamitin ang `stderr` para sa pag-log - huwag magsulat sa `stdout` dahil nakalaan ito para sa mga MCP message
- Siguraduhing ang lahat ng JSON-RPC messages ay hinati sa linya (newline-delimited)
- Subukan muna gamit ang simpleng tools bago magdagdag ng komplikadong functionality
- Gamitin ang Inspector para i-verify ang format ng mga mensahe

## Paggamit ng iyong stdio server sa VS Code

Kapag naitayo mo na ang iyong MCP stdio server, maaari mo itong isama sa VS Code para magamit ito kasama si Claude o iba pang MCP-compatible na mga kliyente.

### Configuration

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

2. **I-restart ang Claude**: Isara at buksan muli ang Claude upang ma-load ang bagong server configuration.

3. **Subukan ang koneksyon**: Simulan ang isang pag-uusap kay Claude at subukan ang mga tools ng iyong server:
   - "Pwede mo ba akong batiin gamit ang greeting tool?"
   - "Kalkulahin ang suma ng 15 at 27"
   - "Ano ang impormasyon ng server?"

### Halimbawa ng TypeScript stdio server

Narito ang isang kumpletong halimbawa ng TypeScript para sa sanggunian:

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
- Maunawaan kung bakit na-deprecate ang SSE transport pabor sa stdio at Streamable HTTP
- Gumawa ng mga tools na maaaring tawagin ng MCP clients
- I-debug ang iyong server gamit ang MCP Inspector
- Isama ang iyong stdio server sa VS Code at Claude

Ang stdio transport ay nagbibigay ng mas simple, mas secure, at mas mahusay na paraan upang bumuo ng MCP servers kumpara sa deprecated na SSE approach. Ito ang inirerekomendang transport para sa karamihan ng mga implementasyon ng MCP server simula sa 2025-06-18 na specification.


### .NET

1. Gumawa muna tayo ng ilang tools, kaya gagawa tayo ng file na *Tools.cs* na may sumusunod na nilalaman:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ehersisyo: Pagsusuri ng iyong stdio server

Ngayong naitayo mo na ang iyong stdio server, subukan natin ito para masiguro na maayos itong gumagana.

### Mga Kinakailangan

1. Siguraduhin na naka-install ang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Dapat nakasave ang iyong server code (halimbawa, bilang `server.py`)

### Pagsusuri gamit ang Inspector

1. **Simulan ang Inspector kasama ang iyong server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buksan ang web interface**: Magbubukas ang Inspector ng browser window na nagpapakita ng kakayahan ng iyong server.

3. **Subukan ang mga tools**: 
   - Subukan ang `get_greeting` tool gamit ang iba't ibang pangalan
   - Subukan ang `calculate_sum` tool gamit ang iba't ibang numero
   - Tawagin ang `get_server_info` tool para makita ang metadata ng server

4. **Bantayan ang komunikasyon**: Ipinapakita ng Inspector ang mga JSON-RPC messages na ipinagpapalitan ng client at server.

### Ano ang dapat mong makita

Kapag nagsimula nang maayos ang iyong server, makikita mo:
- Mga kakayahan ng server na nakalista sa Inspector
- Mga tools na available para sa pagsusuri
- Matagumpay na pagpapalitan ng mga JSON-RPC message
- Mga sagot mula sa tool na ipinapakita sa interface

### Mga karaniwang problema at solusyon

**Hindi nagsisimula ang server:**
- Suriin na lahat ng dependencies ay naka-install: `pip install mcp`
- Tiyakin ang tamang syntax at indentation ng Python
- Tingnan ang mga mensahe ng error sa console

**Hindi lumalabas ang mga tools:**
- Siguraduhing nandun ang `@server.tool()` decorators
- Tiyakin na ang mga tool function ay nadefine bago ang `main()`
- Siguraduhing tama ang configuration ng server

**Mga isyu sa koneksyon:**
- Siguraduhin na ginagamit nang tama ang stdio transport ng server
- Suriin kung may ibang proseso na nakakaistorbo
- I-verify ang syntax ng Inspector command

## Takdang Aralin

Subukang palawakin ang iyong server na may mas maraming kakayahan. Tingnan ang [pahina](https://api.chucknorris.io/) para, halimbawa, magdagdag ng tool na tumatawag ng API. Sa iyo ang desisyon kung ano ang anyo ng server. Mag-enjoy :)
## Solusyon

[Solusyon](./solution/README.md) Narito ang isang posibleng solusyon na may gumaganang code.

## Pangunahing Mga Natutunan

Ang mga pangunahing natutunan mula sa kabanatang ito ay ang mga sumusunod:

- Ang stdio transport ang inirerekomendang mekanismo para sa mga lokal na MCP server.
- Pinapahintulutan ng stdio transport ang seamless na komunikasyon sa pagitan ng MCP servers at clients gamit ang standard input at output streams.
- Maaari mong gamitin ang parehong Inspector at Visual Studio Code para direktang gamitin ang stdio servers, na nagpapadali sa pag-debug at integrasyon.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Karagdagang Mga Mapagkukunan

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Ano ang Susunod

## Mga Susunod na Hakbang

Ngayong natutunan mo na kung paano bumuo ng MCP servers gamit ang stdio transport, maaari kang mag-explore ng mas advanced na mga paksa:

- **Susunod**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Matuto tungkol sa isa pang suportadong mekanismo ng transport para sa remote servers
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Magpatupad ng seguridad sa iyong MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - I-deploy ang iyong mga server para sa production use

## Karagdagang Mga Mapagkukunan

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Kasalukuyang specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Mga reference ng SDK para sa lahat ng wika
- [Community Examples](../../06-CommunityContributions/README.md) - Maraming halimbawa ng server mula sa komunidad

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->