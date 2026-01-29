# MCP Server gamit ang stdio Transport

> **⚠️ Mahalagang Update**: Simula sa MCP Specification 2025-06-18, ang standalone SSE (Server-Sent Events) transport ay **hindi na ginagamit** at pinalitan ng "Streamable HTTP" transport. Ang kasalukuyang MCP specification ay nagtatakda ng dalawang pangunahing mekanismo ng transport:
> 1. **stdio** - Standard input/output (inirerekomenda para sa mga lokal na server)
> 2. **Streamable HTTP** - Para sa mga remote server na maaaring gumamit ng SSE sa loob
>
> Ang araling ito ay na-update upang mag-focus sa **stdio transport**, na siyang inirerekomendang paraan para sa karamihan ng mga MCP server implementation.

Ang stdio transport ay nagbibigay-daan sa mga MCP server na makipag-ugnayan sa mga kliyente gamit ang standard input at output streams. Ito ang pinakakaraniwang ginagamit at inirerekomendang mekanismo ng transport sa kasalukuyang MCP specification, na nagbibigay ng simple at epektibong paraan upang bumuo ng MCP servers na madaling ma-integrate sa iba't ibang client applications.

## Pangkalahatang-ideya

Ang araling ito ay tumatalakay kung paano bumuo at gumamit ng MCP Servers gamit ang stdio transport.

## Mga Layunin sa Pag-aaral

Sa pagtatapos ng araling ito, magagawa mo ang sumusunod:

- Bumuo ng MCP Server gamit ang stdio transport.
- I-debug ang MCP Server gamit ang Inspector.
- Gumamit ng MCP Server sa Visual Studio Code.
- Maunawaan ang kasalukuyang mga mekanismo ng MCP transport at kung bakit inirerekomenda ang stdio.

## stdio Transport - Paano Ito Gumagana

Ang stdio transport ay isa sa dalawang suportadong uri ng transport sa kasalukuyang MCP specification (2025-06-18). Ganito ito gumagana:

- **Simpleng Komunikasyon**: Binabasa ng server ang mga JSON-RPC na mensahe mula sa standard input (`stdin`) at nagpapadala ng mga mensahe sa standard output (`stdout`).
- **Batay sa Proseso**: Ang client ay naglulunsad ng MCP server bilang subprocess.
- **Format ng Mensahe**: Ang mga mensahe ay indibidwal na JSON-RPC requests, notifications, o responses, na pinaghihiwalay ng mga newline.
- **Pag-log**: Ang server AY maaaring magsulat ng UTF-8 strings sa standard error (`stderr`) para sa pag-log.

### Mga Pangunahing Kinakailangan:
- Ang mga mensahe AY DAPAT na pinaghihiwalay ng mga newline at HINDI DAPAT maglaman ng embedded newlines.
- Ang server AY HINDI DAPAT magsulat ng kahit ano sa `stdout` na hindi valid na MCP message.
- Ang client AY HINDI DAPAT magsulat ng kahit ano sa `stdin` ng server na hindi valid na MCP message.

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

Sa code na ito:

- Ini-import natin ang `Server` class at `StdioServerTransport` mula sa MCP SDK.
- Gumagawa tayo ng server instance na may basic configuration at capabilities.

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

Sa code na ito:

- Gumagawa tayo ng server instance gamit ang MCP SDK.
- Nagde-define tayo ng tools gamit ang decorators.
- Ginagamit ang stdio_server context manager para sa transport.

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

Ang pangunahing pagkakaiba mula sa SSE ay ang stdio servers:

- Hindi nangangailangan ng web server setup o HTTP endpoints.
- Nilulunsad bilang subprocesses ng client.
- Nakikipag-ugnayan gamit ang stdin/stdout streams.
- Mas simple i-implement at i-debug.

## Ehersisyo: Paglikha ng stdio Server

Para makagawa ng server, kailangan nating tandaan ang dalawang bagay:

- Kailangan nating gumamit ng web server para mag-expose ng endpoints para sa koneksyon at mga mensahe.

## Lab: Paglikha ng simpleng MCP stdio server

Sa lab na ito, gagawa tayo ng simpleng MCP server gamit ang inirerekomendang stdio transport. Ang server na ito ay mag-e-expose ng tools na maaaring tawagin ng mga kliyente gamit ang standard Model Context Protocol.

### Mga Kinakailangan

- Python 3.8 o mas bago.
- MCP Python SDK: `pip install mcp`.
- Pangunahing kaalaman sa async programming.

Simulan natin ang paggawa ng unang MCP stdio server:

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

## Pangunahing Pagkakaiba mula sa Deprecated SSE Approach

**Stdio Transport (Kasalukuyang Standard):**
- Simpleng subprocess model - nilulunsad ng client ang server bilang child process.
- Komunikasyon sa pamamagitan ng stdin/stdout gamit ang JSON-RPC messages.
- Walang kinakailangang HTTP server setup.
- Mas mahusay na performance at seguridad.
- Mas madaling i-debug at i-develop.

**SSE Transport (Hindi na ginagamit simula MCP 2025-06-18):**
- Nangangailangan ng HTTP server na may SSE endpoints.
- Mas komplikadong setup gamit ang web server infrastructure.
- Karagdagang konsiderasyon sa seguridad para sa HTTP endpoints.
- Pinalitan na ng Streamable HTTP para sa web-based scenarios.

### Paglikha ng server gamit ang stdio transport

Para makagawa ng stdio server, kailangan nating:

1. **I-import ang kinakailangang mga library** - Kailangan natin ang MCP server components at stdio transport.
2. **Gumawa ng server instance** - I-define ang server gamit ang capabilities nito.
3. **Mag-define ng tools** - Idagdag ang functionality na gusto nating i-expose.
4. **I-set up ang transport** - I-configure ang stdio communication.
5. **Patakbuhin ang server** - Simulan ang server at i-handle ang mga mensahe.

Gawin natin ito step-by-step:

### Hakbang 1: Gumawa ng basic stdio server

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

### Hakbang 2: Magdagdag ng mas maraming tools

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

Ang server ay magsisimula at maghihintay ng input mula sa stdin. Nakikipag-ugnayan ito gamit ang JSON-RPC messages sa stdio transport.

### Hakbang 4: Testing gamit ang Inspector

Pwede mong i-test ang server gamit ang MCP Inspector:

1. I-install ang Inspector: `npx @modelcontextprotocol/inspector`.
2. Patakbuhin ang Inspector at ituro ito sa iyong server.
3. I-test ang mga tools na ginawa mo.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Pag-debug ng iyong stdio server

### Gamit ang MCP Inspector

Ang MCP Inspector ay mahalagang tool para sa pag-debug at pag-test ng MCP servers. Ganito ito gamitin sa iyong stdio server:

1. **I-install ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Patakbuhin ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **I-test ang iyong server**: Ang Inspector ay nagbibigay ng web interface kung saan maaari mong:
   - Tingnan ang server capabilities.
   - I-test ang tools gamit ang iba't ibang parameters.
   - I-monitor ang JSON-RPC messages.
   - I-debug ang mga isyu sa koneksyon.

### Gamit ang VS Code

Pwede mo ring i-debug ang MCP server mo direkta sa VS Code:

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

2. Maglagay ng breakpoints sa server code mo.
3. Patakbuhin ang debugger at i-test gamit ang Inspector.

### Mga Karaniwang Tips sa Pag-debug

- Gumamit ng `stderr` para sa pag-log - huwag magsulat sa `stdout` dahil ito ay nakalaan para sa MCP messages.
- Siguraduhing lahat ng JSON-RPC messages ay newline-delimited.
- I-test muna ang simpleng tools bago magdagdag ng mas komplikadong functionality.
- Gamitin ang Inspector para i-verify ang format ng mga mensahe.

## Paggamit ng iyong stdio server sa VS Code

Kapag nagawa mo na ang MCP stdio server mo, pwede mo itong i-integrate sa VS Code para magamit ito sa Claude o iba pang MCP-compatible clients.

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

2. **I-restart ang Claude**: Isara at muling buksan ang Claude para ma-load ang bagong server configuration.

3. **I-test ang koneksyon**: Simulan ang pag-uusap sa Claude at subukan ang tools ng server mo:
   - "Pwede mo ba akong batiin gamit ang greeting tool?"
   - "I-calculate ang sum ng 15 at 27."
   - "Ano ang server info?"

### TypeScript stdio server example

Narito ang kumpletong TypeScript example para sa reference:

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

### .NET stdio server example

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

## Buod

Sa updated na araling ito, natutunan mo kung paano:

- Bumuo ng MCP servers gamit ang kasalukuyang **stdio transport** (inirerekomendang paraan).
- Maunawaan kung bakit ang SSE transport ay hindi na ginagamit at pinalitan ng stdio at Streamable HTTP.
- Gumawa ng tools na maaaring tawagin ng MCP clients.
- I-debug ang server gamit ang MCP Inspector.
- I-integrate ang stdio server mo sa VS Code at Claude.

Ang stdio transport ay nagbibigay ng mas simple, mas secure, at mas mahusay na paraan para bumuo ng MCP servers kumpara sa deprecated SSE approach. Ito ang inirerekomendang transport para sa karamihan ng MCP server implementations simula sa 2025-06-18 specification.

### .NET

1. Gumawa muna tayo ng ilang tools, para dito gagawa tayo ng file na *Tools.cs* na may ganitong nilalaman:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ehersisyo: Testing ng iyong stdio server

Ngayon na nagawa mo na ang stdio server mo, subukan natin ito para masiguradong gumagana ito nang tama.

### Mga Kinakailangan

1. Siguraduhing naka-install ang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ang server code mo ay dapat naka-save (hal., bilang `server.py`).

### Testing gamit ang Inspector

1. **Patakbuhin ang Inspector kasama ang iyong server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buksan ang web interface**: Magbubukas ang Inspector ng browser window na nagpapakita ng capabilities ng server mo.

3. **I-test ang tools**: 
   - Subukan ang `get_greeting` tool gamit ang iba't ibang pangalan.
   - I-test ang `calculate_sum` tool gamit ang iba't ibang numero.
   - Tawagin ang `get_server_info` tool para makita ang metadata ng server.

4. **I-monitor ang komunikasyon**: Ipinapakita ng Inspector ang JSON-RPC messages na ipinapadala sa pagitan ng client at server.

### Ano ang dapat mong makita

Kapag tama ang pagsisimula ng server mo, dapat mong makita:
- Ang server capabilities na nakalista sa Inspector.
- Mga tools na available para sa testing.
- Matagumpay na JSON-RPC message exchanges.
- Mga response ng tools na ipinapakita sa interface.

### Karaniwang mga isyu at solusyon

**Hindi magsimula ang server:**
- Siguraduhing naka-install ang lahat ng dependencies: `pip install mcp`.
- I-verify ang Python syntax at indentation.
- Tingnan ang error messages sa console.

**Hindi lumalabas ang tools:**
- Siguraduhing may `@server.tool()` decorators.
- Siguraduhing ang tool functions ay naka-define bago ang `main()`.
- I-verify na tama ang configuration ng server.

**Mga isyu sa koneksyon:**
- Siguraduhing tama ang paggamit ng stdio transport sa server.
- Tingnan kung may ibang proseso na nakakaabala.
- I-verify ang syntax ng Inspector command.

## Assignment

Subukan mong palawakin ang server mo gamit ang mas maraming capabilities. Tingnan ang [page na ito](https://api.chucknorris.io/) para, halimbawa, magdagdag ng tool na tumatawag sa isang API. Ikaw ang magdesisyon kung ano ang magiging hitsura ng server. Mag-enjoy! :)

## Solusyon

[Solusyon](./solution/README.md) Narito ang posibleng solusyon na may working code.

## Mga Pangunahing Puntos

Ang mga pangunahing puntos mula sa kabanatang ito ay ang mga sumusunod:

- Ang stdio transport ang inirerekomendang mekanismo para sa mga lokal na MCP servers.
- Ang stdio transport ay nagbibigay ng seamless na komunikasyon sa pagitan ng MCP servers at clients gamit ang standard input at output streams.
- Pwede mong gamitin ang Inspector at Visual Studio Code para direktang gamitin ang stdio servers, na ginagawang simple ang debugging at integration.

## Mga Halimbawa

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Karagdagang Resources

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Ano ang Susunod

## Mga Susunod na Hakbang

Ngayon na natutunan mo kung paano bumuo ng MCP servers gamit ang stdio transport, maaari mong tuklasin ang mas advanced na mga paksa:

- **Susunod**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - Alamin ang iba pang suportadong mekanismo ng transport para sa remote servers.
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Mag-implement ng seguridad sa iyong MCP servers.
- **Production**: [Deployment Strategies](../09-deployment/README.md) - I-deploy ang iyong servers para sa production use.

## Karagdagang Resources

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Opisyal na specification.
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Mga reference ng SDK para sa lahat ng wika.
- [Community Examples](../../06-CommunityContributions/README.md) - Mas maraming halimbawa ng server mula sa komunidad.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.