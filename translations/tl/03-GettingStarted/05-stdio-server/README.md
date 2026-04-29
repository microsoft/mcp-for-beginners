# MCP Server gamit ang stdio Transport

> **⚠️ Mahalagang Update**: Simula sa MCP Specification 2025-06-18, ang standalone na SSE (Server-Sent Events) transport ay **tinanggal** at pinalitan ng "Streamable HTTP" transport. Ang kasalukuyang MCP specification ay nagtatakda ng dalawang pangunahing mekanismo ng transport:
> 1. **stdio** - Standard input/output (inirerekomenda para sa mga lokal na server)
> 2. **Streamable HTTP** - Para sa mga remote server na maaaring gumamit ng SSE internally
>
> Ang araling ito ay na-update upang tutukan ang **stdio transport**, na ang inirerekomendang paraan para sa karamihan ng mga implementasyon ng MCP server.

Pinapayagan ng stdio transport ang mga MCP server na makipag-ugnayan sa mga client sa pamamagitan ng standard input at output streams. Ito ang pinaka-karaniwang ginagamit at inirerekomendang mekanismo ng transport sa kasalukuyang MCP specification, na nagbibigay ng isang simple at episyenteng paraan upang bumuo ng mga MCP server na madaling maiintegrate sa iba't ibang mga client applications.

## Pangkalahatang-ideya

Sinasaklaw ng araling ito kung paano bumuo at gumamit ng MCP Servers gamit ang stdio transport.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:

- Bumuo ng MCP Server gamit ang stdio transport.
- Mag-debug ng MCP Server gamit ang Inspector.
- Gumamit ng MCP Server gamit ang Visual Studio Code.
- Maunawaan ang kasalukuyang mga mekanismo ng transport sa MCP at bakit inirerekomenda ang stdio.

## stdio Transport - Paano Ito Gumagana

Ang stdio transport ay isa sa dalawang suportadong uri ng transport sa kasalukuyang MCP specification (2025-06-18). Ganito ang paraan ng paggana nito:

- **Simple na Komunikasyon**: Binabasa ng server ang mga mensaheng JSON-RPC mula sa standard input (`stdin`) at nagpapadala ng mga mensahe sa standard output (`stdout`).
- **Process-based**: Inilulunsad ng client ang MCP server bilang isang subprocess.
- **Format ng Mensahe**: Ang mga mensahe ay indibidwal na JSON-RPC requests, notifications, o responses, na pinaghihiwalay ng mga bagong linya.
- **Logging**: Maaaring magsulat ang server ng UTF-8 na mga string sa standard error (`stderr`) para sa mga layunin ng pag-log.

### Mga Pangunahing Kinakailangan:
- Ang mga mensahe ay DAPAT pinaghihiwalay ng mga bagong linya at HINDI DAPAT maglaman ng mga naka-embed na bagong linya
- HINDI DAPAT magsulat ang server ng anumang hindi wastong mensahe ng MCP sa `stdout`
- HINDI DAPAT magsulat ang client sa `stdin` ng server ng anumang hindi wastong mensahe ng MCP

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

- Ina-import namin ang klase na `Server` at `StdioServerTransport` mula sa MCP SDK
- Gumagawa kami ng instance ng server na may basic na configuration at capabilities
- Gumagawa kami ng isang instance ng `StdioServerTransport` at ikinakonekta ang server dito, na nagpapahintulot sa komunikasyon sa stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Gumawa ng server na halimbawa
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

Sa nakaraang code:

- Gumagawa ng instance ng server gamit ang MCP SDK
- Nagdedeklara ng mga tools gamit ang mga decorator
- Ginagamit ang stdio_server context manager para hawakan ang transport

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

Ang pangunahing pagkakaiba sa SSE ay ang mga stdio server:

- Hindi nangangailangan ng setup ng web server o HTTP endpoints
- Inilulunsad bilang mga subprocess ng client
- Nakikipag-ugnayan sa pamamagitan ng stdin/stdout streams
- Mas simple i-implement at i-debug

## Ehersisyo: Paglikha ng stdio Server

Para gumawa ng server, kailangang tandaan ang dalawang bagay:

- Kailangan namin gumamit ng web server para mag-expose ng mga endpoints para sa koneksyon at mga mensahe.

## Lab: Paglikha ng simpleng MCP stdio server

Sa lab na ito, gagagawa tayo ng isang simpleng MCP server gamit ang inirekomendang stdio transport. Ang server na ito ay mag-eexpose ng mga tools na maaaring tawagin ng mga client gamit ang standard Model Context Protocol.

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

# Lumikha ng server
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

## Pangunahing pagkakaiba mula sa deprecated na SSE na paraan

**Stdio Transport (Kasalukuyang Pamantayan):**
- Simpleng subprocess model - pinapalunsad ng client ang server bilang child process
- Komunikasyon sa pamamagitan ng stdin/stdout gamit ang mga mensaheng JSON-RPC
- Hindi kailangan ang HTTP server setup
- Mas mahusay na performance at seguridad
- Mas madali i-debug at i-develop

**SSE Transport (Tinanggal simula sa MCP 2025-06-18):**
- Nangangailangan ng HTTP server na may SSE endpoints
- Mas kumplikadong setup gamit ang web server infrastructure
- Karagdagang considerations sa seguridad para sa HTTP endpoints
- Pinalitan na ng Streamable HTTP para sa web-based na mga senaryo

### Paglikha ng server gamit ang stdio transport

Para gumawa ng stdio server, kailangan nating:

1. **I-import ang kinakailangang mga library** - Kailangan namin ang MCP server components at stdio transport
2. **Gumawa ng instance ng server** - Ideklara ang server kasama ang mga kakayahan nito
3. **Magdefine ng mga tools** - Idagdag ang mga functionality na nais naming i-expose
4. **I-setup ang transport** - I-configure ang stdio komunikasyon
5. **Patakbuhin ang server** - Simulan ang server at hawakan ang mga mensahe

Gawin natin ito ng paunti-unti:

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

### Hakbang 3: Pagpapatakbo ng server

I-save ang code bilang `server.py` at patakbuhin ito mula sa command line:

```bash
python server.py
```

Magsisimula ang server at maghihintay ng input mula sa stdin. Nakikipag-ugnayan ito gamit ang mga JSON-RPC na mensahe sa stdio transport.

### Hakbang 4: Pagsubok gamit ang Inspector

Maaari mong subukan ang iyong server gamit ang MCP Inspector:

1. I-install ang Inspector: `npx @modelcontextprotocol/inspector`
2. Patakbuhin ang Inspector at ituro ito sa iyong server
3. Subukan ang mga tools na iyong ginawa

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Pag-debug ng iyong stdio server

### Paggamit ng MCP Inspector

Ang MCP Inspector ay isang mahalagang kasangkapan para sa pag-debug at pagsubok ng MCP servers. Ganito ito gamitin sa iyong stdio server:

1. **I-install ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Patakbuhin ang Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Subukan ang iyong server**: Ang Inspector ay nagbibigay ng web interface kung saan maaari mong:
   - Tingnan ang mga kakayahan ng server
   - Subukan ang mga tools gamit ang iba't ibang mga parameter
   - I-monitor ang mga JSON-RPC message
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

2. Maglagay ng breakpoints sa iyong server code
3. Patakbuhin ang debugger at subukan gamit ang Inspector

### Mga Karaniwang Tip sa Pag-debug

- Gamitin ang `stderr` para sa pag-log - huwag magsulat sa `stdout` dahil nakalaan ito para sa MCP messages
- Siguraduhing lahat ng JSON-RPC messages ay newline-delimited
- Subukan muna ang mga simpleng tools bago magdagdag ng kumplikadong functionality
- Gamitin ang Inspector para i-verify ang format ng mga mensahe

## Paggamit ng iyong stdio server sa VS Code

Kapag nagawa mo na ang MCP stdio server, maaari mo itong i-integrate sa VS Code upang gamitin ito kasama si Claude o iba pang MCP-compatible clients.

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

2. **I-restart ang Claude**: Isara at buksan muli ang Claude upang i-load ang bagong server configuration.

3. **Subukan ang koneksyon**: Magsimula ng pag-uusap kay Claude at subukan ang mga tools ng iyong server:
   - "Pwede mo ba akong batiin gamit ang greeting tool?"
   - "Kalkulahin ang kabuuan ng 15 at 27"
   - "Ano ang impormasyon ng server?"

### Halimbawa ng TypeScript stdio server

Narito ang kompletong halimbawa ng TypeScript para sa sanggunian:

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
- Unawain kung bakit tinanggal ang SSE transport pabor sa stdio at Streamable HTTP
- Lumikha ng mga tools na maaaring tawagin ng MCP clients
- Mag-debug ng iyong server gamit ang MCP Inspector
- I-integrate ang iyong stdio server sa VS Code at Claude

Nagbibigay ang stdio transport ng mas simple, mas ligtas, at mas mabilis na paraan upang bumuo ng MCP servers kumpara sa deprecated na paraan ng SSE. Ito ang inirerekomendang transport para sa karamihan ng mga implementasyon ng MCP server simula sa 2025-06-18 specification.

### .NET

1. Gumawa muna tayo ng ilang mga tools, para dito gagawa tayo ng file na *Tools.cs* na may sumusunod na nilalaman:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Ehersisyo: Pagsubok ng iyong stdio server

Ngayon na nagawa mo na ang iyong stdio server, subukan natin ito upang matiyak na ito ay gumagana ng maayos.

### Mga Kinakailangan

1. Siguraduhing naka-install ang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Ang iyong server code ay naka-save (halimbawa, bilang `server.py`)

### Pagsubok gamit ang Inspector

1. **Simulan ang Inspector kasama ang iyong server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buksan ang web interface**: Magbubukas ang Inspector ng browser window na nagpapakita ng kakayahan ng iyong server.

3. **Subukan ang mga tools**: 
   - Subukan ang `get_greeting` tool gamit ang iba't ibang pangalan
   - Subukan ang `calculate_sum` tool gamit ang iba't ibang mga numero
   - Tawagin ang `get_server_info` tool upang makita ang metadata ng server

4. **I-monitor ang komunikasyon**: Ipinapakita ng Inspector ang mga JSON-RPC messages na nagpapalitan sa pagitan ng client at server.

### Ano ang dapat mong makita

Kapag nagsimula nang tama ang iyong server, dapat mong makita:
- Mga kakayahan ng server na nakalista sa Inspector
- Mga tool na available para sa pagsubok
- Matagumpay na pagpapalitan ng mga JSON-RPC message
- Mga tugon ng tool na ipinapakita sa interface

### Mga Karaniwang Isyu at Solusyon

**Hindi nagsisimula ang server:**
- Suriin kung lahat ng dependencies ay naka-install: `pip install mcp`
- I-verify ang syntax at indentation ng Python
- Tingnan ang mga error message sa console

**Hindi lumilitaw ang mga tools:**
- Siguraduhing naroroon ang mga `@server.tool()` decorators
- Tingnan kung ang mga tool functions ay nade-define bago ang `main()`
- I-verify na maayos ang configuration ng server

**Mga isyu sa koneksyon:**
- Siguraduhin na tama ang paggamit ng stdio transport sa server
- Suriin kung may ibang proseso na nakakaistorbo
- I-verify ang syntax ng Inspector command

## Takdang-Aralin

Subukang palawakin ang iyong server gamit ang mas maraming capabilities. Tingnan ang [pahina na ito](https://api.chucknorris.io/) para halimbawa, magdagdag ng tool na tumatawag sa isang API. Ikaw ang magdedesisyon kung ano ang anyo ng server. Mag-enjoy :)

## Solusyon

[Solusyon](./solution/README.md) Narito ang isang posibleng solusyon na may gumaganang kodigo.

## Pangunahing Mga Natutunan

Ang mga pangunahing natutunan mula sa kabanatang ito ay ang mga sumusunod:

- Ang stdio transport ang inirerekomendang mekanismo para sa mga lokal na MCP server.
- Pinapayagan ng stdio transport ang tuloy-tuloy na komunikasyon sa pagitan ng mga MCP server at client gamit ang standard input at output streams.
- Maaari mong gamitin ang parehong Inspector at Visual Studio Code upang direktang gamitin ang mga stdio server, na nagpapadali sa pag-debug at integrasyon.

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

Ngayon na natutunan mo na kung paano gumawa ng MCP servers gamit ang stdio transport, maaari kang mag-explore ng mas advanced na mga paksa:

- **Susunod**: [HTTP Streaming gamit ang MCP (Streamable HTTP)](../06-http-streaming/README.md) - Matutunan ang isa pang suportadong mekanismo ng transport para sa mga remote server
- **Advanced**: [MCP Security Best Practices](../../02-Security/README.md) - Ipatupad ang seguridad sa iyong MCP servers
- **Production**: [Deployment Strategies](../09-deployment/README.md) - Mag-deploy ng mga server para sa production use

## Karagdagang Mga Mapagkukunan

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Opisyal na specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Mga reference ng SDK para sa lahat ng wika
- [Community Examples](../../06-CommunityContributions/README.md) - Mas maraming halimbawa ng server mula sa komunidad

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi eksaktong impormasyon. Ang orihinal na dokumento sa pinagmulan nitong wika ang dapat ituring na pinakapinagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling pantao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->