# MCP Server gamit ang stdio Transport

> **⚠️ Mahalagang Update**: Simula sa MCP Specification 2025-06-18, ang standalone SSE (Server-Sent Events) transport ay **tinanggal na** at pinalitan ng "Streamable HTTP" transport. Ang kasalukuyang MCP specification ay nagtatakda ng dalawang pangunahing mekanismo ng transport:
> 1. **stdio** - Standard input/output (inirerekumenda para sa lokal na mga server)
> 2. **Streamable HTTP** - Para sa mga remote na server na maaaring gumamit ng SSE nang internal
>
> Ang araling ito ay na-update upang tumutok sa **stdio transport**, na siyang inirerekumendang paraan para sa karamihan ng mga implementasyon ng MCP server.

Pinahihintulutan ng stdio transport ang mga MCP server na makipag-ugnayan sa mga client sa pamamagitan ng standard input at output streams. Ito ang pinakakaraniwang ginagamit at inirerekomendang mekanismo ng transport sa kasalukuyang MCP specification, na nagbibigay ng isang simple at episyenteng paraan upang bumuo ng mga MCP server na madaling mai-integrate sa iba't ibang aplikasyon ng client.

## Pangkalahatang Tanaw

Tinutukoy ng araling ito kung paano bumuo at gumamit ng MCP Servers gamit ang stdio transport.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, kaya mong:

- Bumuo ng MCP Server gamit ang stdio transport.
- Mag-debug ng MCP Server gamit ang Inspector.
- Gumamit ng MCP Server gamit ang Visual Studio Code.
- Maunawaan ang kasalukuyang mga mekanismo ng MCP transport at kung bakit inirerekomenda ang stdio.


## stdio Transport - Paano Ito Gumagana

Ang stdio transport ay isa sa dalawang standard na transport sa MCP Specification
`2026-07-28`. Ganito ito gumagana:

- **Simpleng Komunikasyon**: Binabasa ng server ang mga JSON-RPC message mula sa standard input (`stdin`) at nagpapadala ng mga mensahe sa standard output (`stdout`).
- **Batay sa Proseso**: Ina-activate ng client ang MCP server bilang isang subprocess.
- **Format ng Mensahe**: Ang mga mensahe ay mga indibidwal na JSON-RPC request, notification, o response, na hinati-hati gamit ang mga newline.
- **Pag-log**: Maaaring magsulat ang server ng UTF-8 string sa standard error (`stderr`) para sa layunin ng pag-log.

### Mga Pangunahing Kailangan:
- Ang mga mensahe AY DAPAT hatiin gamit ang mga newline at HINDI DAPAT magkaroon ng nakapaloob na newline
- HINDI DAPAT magsulat ang server ng anuman sa `stdout` na hindi isang valid na mensahe ng MCP
- HINDI DAPAT magsulat ang client ng anuman sa `stdin` ng server na hindi isang valid na mensahe ng MCP

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

Sa code na nasa itaas:

- Iniluluwas natin ang klase na `Server` at ang `StdioServerTransport` mula sa MCP SDK
- Gumagawa tayo ng isang server instance na may batayang configuration at kakayahan
- Gumagawa tayo ng isang `StdioServerTransport` instance at kinokonekta ang server dito, pinapagana ang komunikasyon sa stdin/stdout

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

Sa code na nasa itaas:

- Gumawa ng isang server instance gamit ang MCP SDK
- Nagdeklara ng mga tools gamit ang decorators
- Gumamit ng stdio_server context manager para hawakan ang transport

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

Ang pangunahing pagkakaiba mula sa SSE ay:

- Hindi nangangailangan ng setup ng web server o HTTP endpoints
- Pinapalabas bilang mga subprocesses ng client
- Nakikipag-ugnayan sa pamamagitan ng stdin/stdout streams
- Mas simple i-implement at i-debug

## Pagsasanay: Paglikha ng stdio Server

Para gumawa ng server, kailangang tandaan natin ang dalawang bagay:

- Kailangan nating gumamit ng web server para ipakita ang mga endpoints para sa koneksyon at mga mensahe.
## Lab: Paglikha ng simpleng MCP stdio server

Sa lab na ito, gagawa tayo ng simpleng MCP server gamit ang inirerekomendang stdio transport. Ilalantad ng server na ito ang mga tool na pwedeng tawagan ng mga client gamit ang standard Model Context Protocol.

### Mga Kinakailangan

- Python 3.8 o mas bago
- MCP Python SDK: `pip install mcp`
- Batayang kaalaman sa async programming

Simulan natin sa paggawa ng unang MCP stdio server:

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

## Pangunahing Pagkakaiba mula sa tinanggal na SSE approach

**Stdio Transport (Kasalukuyang Pamantayan):**
- Simpleng modelo ng subprocess - ang client ang nagpapalabas ng server bilang child process
- Komunikasyon sa pamamagitan ng stdin/stdout gamit ang JSON-RPC messages
- Walang HTTP server setup na kailangan
- Mas mahusay na pagganap at seguridad
- Mas madali sa pag-debug at pag-develop

**SSE Transport (Tinanggal simula sa MCP 2025-06-18):**
- Kailangan ng HTTP server na may SSE endpoints
- Mas komplikadong setup kasama ang web server infrastructure
- Karagdagang konsiderasyon sa seguridad para sa mga HTTP endpoints
- Pinalitan na ng Streamable HTTP para sa mga web-based na senaryo

### Paglikha ng server gamit ang stdio transport

Para gumawa ng stdio server, kailangan nating:

1. **I-import ang kinakailangang mga library** - Kailangan natin ang mga MCP server components at stdio transport
2. **Gumawa ng server instance** - Tukuyin ang server gamit ang mga kakayahan nito
3. **Magdefine ng mga tools** - Idagdag ang mga functionality na nais ipakita
4. **I-set up ang transport** - I-configure ang stdio communication
5. **Patakbuhin ang server** - Simulan ang server at hawakan ang mga mensahe

Gawin natin ito nang hakbang-hakbang:

### Hakbang 1: Gumawa ng simpleng stdio server

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

Magsisimula ang server at maghihintay ng input mula sa stdin. Nakikipag-ugnayan ito gamit ang mga JSON-RPC message sa stdio transport.

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

Ang MCP Inspector ay isang mahalagang tool para sa pag-debug at pagsubok ng MCP servers. Narito kung paano ito gamitin sa iyong stdio server:

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
   - Subukan ang mga tool gamit ang iba't ibang mga parameter
   - I-monitor ang mga JSON-RPC message
   - Mag-debug ng mga isyu sa koneksyon

### Paggamit ng VS Code

Maaari mo ring direktang i-debug ang iyong MCP server sa VS Code:

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

2. Mag-set ng breakpoints sa iyong server code
3. Patakbuhin ang debugger at subukan gamit ang Inspector

### Mga Karaniwang Tips sa Pag-debug

- Gumamit ng `stderr` para sa pag-log - huwag kailanman magsulat sa `stdout` dahil ito ay nakalaan para sa mga MCP message
- Siguraduhin na lahat ng JSON-RPC message ay hati sa newline
- Subukan muna gamit ang simpleng mga tool bago magdagdag ng mas kumplikadong mga functionality
- Gumamit ng Inspector upang tiyakin ang tamang format ng mga mensahe

## Paggamit ng iyong stdio server sa VS Code

Kapag nakabuo ka na ng iyong MCP stdio server, maaari mo itong i-integrate sa VS Code upang magamit ito kasama si Claude o iba pang MCP-compatible na mga client.

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

2. **I-restart si Claude**: Isara at buksan muli si Claude upang i-load ang bagong configuration ng server.

3. **Subukan ang koneksyon**: Simulan ang pag-uusap kay Claude at subukan ang mga tool ng iyong server:
   - "Maaari mo ba akong batiin gamit ang greeting tool?"
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

- Bumuo ng mga MCP server gamit ang kasalukuyang **stdio transport** (inirerekomendang paraan)
- Maunawaan kung bakit tinanggal ang SSE transport pabor sa stdio at Streamable HTTP
- Gumawa ng mga tool na maaaring tawagin ng mga MCP client
- Mag-debug ng iyong server gamit ang MCP Inspector
- I-integrate ang iyong stdio server sa VS Code at Claude

Ang stdio transport ay nagbibigay ng mas simple, mas ligtas, at mas mabilis na paraan upang bumuo ng mga MCP server kumpara sa tinanggal na SSE approach. Ito ang inirerekomendang transport para sa karamihan ng mga implementasyon ng MCP server simula sa 2025-06-18 na specification.


### .NET

1. Gumawa muna tayo ng ilang tool, para dito gagawa tayo ng file *Tools.cs* na may sumusunod na nilalaman:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Pagsasanay: Pagsubok ng iyong stdio server

Ngayon na nakabuo ka ng iyong stdio server, subukan natin ito upang masigurong gumagana ito nang maayos.

### Mga Kinakailangan

1. Siguraduhing naka-install ang MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Dapat naka-save ang iyong server code (hal., bilang `server.py`)

### Pagsubok gamit ang Inspector

1. **Simulan ang Inspector kasama ng iyong server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Buksan ang web interface**: Magbubukas ang Inspector ng browser window na nagpapakita ng mga kakayahan ng iyong server.

3. **Subukan ang mga tool**: 
   - Subukan ang `get_greeting` tool gamit ang iba't ibang pangalan
   - Subukan ang `calculate_sum` tool gamit ang iba't ibang numero
   - Tawagin ang `get_server_info` tool upang makita ang metadata ng server

4. **I-monitor ang komunikasyon**: Ipinapakita ng Inspector ang mga JSON-RPC message na ipinagpapalitan ng client at server.

### Ano ang dapat mong makita

Kapag tama ang pagsisimula ng iyong server, makikita mo:
- Nakalista ang mga kakayahan ng server sa Inspector
- Mga tool na magagamit para sa pagsubok
- Tagumpay na pagpapalitan ng JSON-RPC message
- Mga sagot ng tool na ipinapakita sa interface

### Mga Karaniwang Problema at Solusyon

**Hindi nagsisimula ang server:**
- Suriin na lahat ng dependencies ay naka-install: `pip install mcp`
- I-verify ang syntax at indentation ng Python
- Tingnan ang mga error message sa console

**Hindi lumalabas ang mga tool:**
- Siguraduhing naroon ang mga `@server.tool()` decorators
- Suriing tama ang pagkakadeklara ng mga tool function bago ang `main()`
- I-verify na tama ang configuration ng server

**Problema sa koneksyon:**
- Siguraduhing ginamit ng server nang tama ang stdio transport
- Tiyaking walang ibang proseso na nakakaabala
- I-verify ang syntax ng Inspector command

## Takdang Aralin

Subukang dagdagan ang kakayahan ng iyong server. Tingnan ang [pahina na ito](https://api.chucknorris.io/) para halimbawa, para magdagdag ng tool na tumatawag sa isang API. Ikaw ang magdedesisyon kung ano ang magiging anyo ng server. Mag-enjoy :)
## Solusyon

[Solusyon](./solution/README.md) Narito ang isang posibleng solusyon na may gumaganang code.

## Pangunahing Aral

Ang mga pangunahing aral mula sa kabanatang ito ay ang mga sumusunod:

- Ang stdio transport ang inirerekomendang mekanismo para sa lokal na mga MCP server.
- Pinahihintulutan ng stdio transport ang tuloy-tuloy na komunikasyon sa pagitan ng MCP server at client gamit ang standard input at output streams.
- Maaari mong gamitin ang parehong Inspector at Visual Studio Code upang direktang gamitan ng stdio servers, na ginagawang madali ang pag-debug at integrasyon.

## Mga Halimbawa 

- [Java Calculator](../samples/java/calculator/README.md)
- [.NET Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## Karagdagang Mga Sanggunian

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Ano ang Susunod

## Mga Susunod na Hakbang

Ngayon na natutunan mo na kung paano bumuo ng MCP server gamit ang stdio transport, maaari mong tuklasin ang mga mas advanced na paksa:

- **Susunod**: [HTTP Streaming gamit ang MCP (Streamable HTTP)](../06-http-streaming/README.md) - Matutunan ang isa pang suportadong mekanismo ng transport para sa mga remote na server
- **Advanced**: [Pinakamahusay na Praktis sa Seguridad ng MCP](../../02-Security/README.md) - Ipatupad ang seguridad sa iyong mga MCP server
- **Para sa Produksyon**: [Mga Estratehiya sa Deployment](../09-deployment/README.md) - I-deploy ang iyong mga server para sa produksyon

## Karagdagang Mga Sanggunian

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Kasalukuyang specification
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - Mga sanggunian ng SDK para sa lahat ng wika
- [Community Examples](../../06-CommunityContributions/README.md) - Higit pang mga halimbawa ng server mula sa komunidad

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->