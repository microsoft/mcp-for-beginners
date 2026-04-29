# MCP ಸರ್ವರ್ stdio ಸಾರಿಗೆಯೊಂದಿಗೆ

> **⚠️ ಪ್ರಮುಖ تازهлисಿಸುವಿಕೆ**: MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ 2025-06-18 ರ ಪ್ರಕಾರ, ಸ್ವತಂತ್ರ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್ಸ್) ಸಾರಿಗೆ **ಅಪ್ರಚಲಿತವಾಗಿದೆ** ಮತ್ತು "Streams ಮತ್ತು HTTP" ಸಾರಿಗೆಯಿಂದ ಬದಲಿ ಮಾಡಲಾಗಿದೆ. ಪ್ರಸ್ತುತ MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಎರಡು ಪ್ರಮುಖ ಸಾರಿಗೆ ವಿಧಾನಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:  
> 1. **stdio** - ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್/ಔಟ್ಪುಟ್ (ಸ್ಥಳೀಯ ಸರ್ವರ್‌ಗಳುಗಾಗಿ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)  
> 2. **Streams ಮತ್ತು HTTP** - SSE ಅನ್ನು ಆಂತರಿಕವಾಗಿ ಬಳಸಬಹುದಾದ ದೂರದ ಸರ್ವರ್‌ಗಳಿಗೆ  
>  
> ಈ ಪಾಠ stdio ಸಾರಿಗೆಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುವಂತೆ ನವೀಕರಿಸಲಾಗಿದೆ, ಇದು ಹೆಚ್ಚು MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.

stdio ಸಾರಿಗೆ MCP ಸರ್ವರ್‌ಗಳು ಕ್ಲೈಂಟ್‌ಗಳೊಂದಿಗೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ ಮತ್ತು ಔಟ್ಪುಟ್ ಸ್ಟ್ರೀಂಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ. ಇದು ಪ್ರಸ್ತುತ MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್‌ನಲ್ಲಿ ಅತಿ ಹೆಚ್ಚಿನವಾಗಿ ಬಳಕೆಯಾದ ಹಾಗೂ ಶಿಫಾರಸು ಮಾಡಲಾದ ಸಾರಿಗೆ ವಿಧಾನವಾಗಿದ್ದು, ವಿವಿಧ ಕ್ಲೈಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಅನುಕೂಲಪಡಿಸಬಹುದಾದ ಸರಳ ಮತ್ತು ಪರಿಣಾಮಕಾರಿಯಾದ ವಿಧಾನವನ್ನು ಒದಗಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

ಈ ಪಾಠ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್‌ಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಿ ಉಪಯೋಗಿಸುವುದೆಂದು ವಿವರಿಸುತ್ತದೆ.

## ಕಲಿಕೆ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ ನೀವು ನೀಡಬಹುದಾದವುಗಳು:

- stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿ MCP ಸರ್ವರ್ ಅನ್ನು ನಿರ್ಮಿಸುವುದು.
- Inspector ಅನ್ನು ಉಪಯೋಗಿಸಿಕೊಂಡು MCP ಸರ್ವರ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡುವುದು.
- Visual Studio Code ಬಳಸಿ MCP ಸರ್ವರ್ ಅನ್ನು ಉಪಯೋಗಿಸುವುದು.
- ಪ್ರಸ್ತುತ MCP ಸಾರಿಗೆ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಹಾಗೂ stdio ಯನ್ನು ಏಕೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.

## stdio ಸಾರಿಗೆ - ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

stdio ಸಾರಿಗೆ ಪ್ರಸ್ತುತ MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ (2025-06-18) ನಲ್ಲಿ ಬೆಂಬಲಿತ ಎರಡು ಸಾರಿಗೆ ವಿಧಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇದನ್ನು ಹೀಗಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ:

- **ಸರಳ ಸಂವಹನ**: ಸರ್ವರ್ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ (`stdin`) ನಿಂದ ಓದಿ, ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಔಟ್ಪುಟ್ (`stdout`) ಗೆ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುತ್ತದೆ.
- **ಪ್ರಕ್ರಿಯೆಯ ಆಧಾರಿತ**: ಕ್ಲೈಂಟ್ MCP ಸರ್ವರ್ ಅನ್ನು ಸಹಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ.
- **ಸಂದೇಶ ರೂಪ**: ಸಂದೇಶಗಳು ತಲಾ ಒಂದು JSON-RPC ವಿನಂತಿ, ಅಧಿಸೂಚನೆ ಅಥವಾ ಪ್ರತಿಕ್ರಿಯೆಗಳಾಗಿದ್ದು, ನ್ಯೂಲೈನ್‌ಗಳಿಂದ ವಿಭಜಿಸಲಾಗುತ್ತದೆ.
- **ಲಾಗಿಂಗ್**: ಸರ್ವರ್ ಲಾಗ್‌ಗಾಗಿ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಏರರ್ (`stderr`) ಗೆ UTF-8 ಸರಣಿಗಳನ್ನು ಬರೆಯಬಹುದು.

### ಪ್ರಮುಖ ಅವಶ್ಯಕತೆಗಳು:  
- ಸಂದೇಶಗಳು ನ್ಯೂಲೈನ್‌ಗಳಿಂದ ವಿಭಜಿತವಾಗಿರಬೇಕು ಮತ್ತು ಒಳಗೊಳ್ಳುವ ನ್ಯೂಲೈನ್‌ಗಳನ್ನು ಹೊಂದಿರಕೂಡದು  
- ಸರ್ವರ್ ತಪ್ಪು MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ `stdout` ಗೆ ಬರೆಯಬಾರದು  
- ಕ್ಲೈಂಟ್ ತಪ್ಪು MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ ಸರ್ವರ್‌ನ `stdin` ಗೆ ಬರೆಯಬಾರದು  

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
  
ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ:  

- MCP SDK ನಿಂದ `Server` ವರ್ಗ ಮತ್ತು `StdioServerTransport` ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಲಾಗುತ್ತದೆ  
- ಮೂಲಭೂತ ಸಂರಚನೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಲಾಗುತ್ತದೆ  
- `StdioServerTransport` ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ ಸರ್ವರ್ ಅನ್ನು ಅದಕ್ಕೆ ಸಂಪರ್ಕಿಸಿ stdin/stdout ಮುಖಾಂತರ ಸಂವಹನ ಸಕ್ರಿಯಗೊಳಿಸಲಾಗುತ್ತದೆ  

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ಸರ್ವರ್ ಉದಾಹರಣೆ ರಚಿಸಿ
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
  
ಈ ಹಿಂದೆ ನೀಡಲಾದ ಕೋಡ್‌ನಲ್ಲಿ:  

- MCP SDK ಬಳಸಿ ಸರ್ವರ್ ಉದಾಹರಣೆ ರಚಿಸಲಾಗುತ್ತದೆ  
- ಡೆಕೊರೇಟರ್‌ಗಳ ಮೂಲಕ ಟೂಲ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ  
- stdio_server ಕಾನ್ಟೆಕ್ಸ್ಟ್ ಮ್ಯಾನೇಜರ್ ಬಳಸಿ ಸಾರಿಗೆಯನ್ನು ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ  

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
  
SSE ಯಿಂದ ಪ್ರಮುಖ ಭೇದವೇನೆಂದರೆ stdio ಸರ್ವರ್‌ಗಳು:  

- ವೆಬ್ ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್ ಅಥವಾ HTTP ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳ ಅಗತ್ಯವಿಲ್ಲ  
- ಕ್ಲೈಂಟ್ ಸಹಪ್ರಕ್ರಿಯೆಯಾಗಿ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ  
- stdin/stdout ಸ್ಟ್ರೀಂಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡುತ್ತವೆ  
- ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಮತ್ತು ಡೀಬಗ್ ಮಾಡಲು ಸರಳವಾಗಿವೆ  

## ಅಭ್ಯಾಸ: stdio ಸರ್ವರ್ ಸೃಷ್ಟಿಸುವುದು

ನಮ್ಮ ಸರ್ವರ್ ರಚಿಸಲು ನಾವು ಎರಡು ವಿಷಯಗಳನ್ನು ಗಮನದಲ್ಲಿರಿಸಬೇಕು:  

- ಸಂಪರ್ಕ ಮತ್ತು ಸಂದೇಶಗಳಿಗಾಗಿ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಹೊರತರುವ ವೆಬ್ ಸರ್ವರ್ ಅನ್ನು ಉಪಯೋಗಿಸುವ ಅಗತ್ಯವಿದೆ.

## ಪ್ರಯೋಗಶಾಲೆ: ಸರಳ MCP stdio ಸರ್ವರ್ ರಚನೆ

ಈ ಪ್ರಯೋಗಶಾಲೆಯಲ್ಲಿ, ನಾವು ಶಿಫಾರಸು ಮಾಡಲಾದ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿ ಸರಳ MCP ಸರ್ವರ್ ಅನ್ನು ನಿರ್ಮಿಸುತ್ತೇವೆ. ಈ ಸರ್ವರ್ ಕ್ಲೈಂಟ್‌ಗಳು Model Context Protocol ಮೂಲಕ ಕರೆ ಮಾಡಬಹುದಾದ ಟೂಲ್ಗಳನ್ನು ಅನಾವರಣಗೊಳಿಸುತ್ತದೆ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

- Python 3.8 ಅಥವಾ ಹೆಚ್ಚು  
- MCP Python SDK: `pip install mcp`  
- ಅಸಿಂಕ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮೂಲಭೂತ ಅರಿವು  

ನಮ್ಮೆಲೋ stdio MCP ಸರ್ವರ್ನ್ನು ನಿರ್ಮಿಸುವುದರಿಂದ ಪ್ರಾರಂಭಿಸೋಣ:  

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ಲಾಗಿಂಗ್ ಅನ್ನು ಆಕಾರಗೊಳಿಸಿ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ಸರವರವನ್ನು ಸೃಷ್ಟಿಸಿ
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
    # stdio ಸಾರಿಗೆ ಬಳಸಿರಿ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```
  
## ಅಪ್ರಚಲಿತ SSE ವಿಧಾನದಿಂದ ಪ್ರಮುಖ ಭೇದಗಳು

**Stdio ಸಾರಿಗೆ (ಪ್ರಸ್ತುತ ನಿಯಮಿತ)**:  
- ಸರಳ subprocess ಮಾದರಿ - ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಅನ್ನು ಸಬ್ ಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ  
- JSON-RPC ಸಂದೇಶಗಳ ಮೂಲಕ stdin/stdout ನಲ್ಲಿ ಸಂವಹನ  
- ಯಾವುದೇ HTTP ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್ ಅಗತ್ಯವಿಲ್ಲ  
- ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಭದ್ರತೆ  
- ಸುಲಭ ಡೀಬಗ್ಗಿಂಗ್ ಮತ್ತು ಅಭಿವೃದ್ಧಿ  

**SSE ಸಾರಿಗೆ (MCP 2025-06-18 ರಿಂದ ಅಪ್ರಚಲಿತ)**:  
- SSE ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ HTTP ಸರ್ವರ್ ಅಗತ್ಯವಿತ್ತು  
- ವೆಬ್ ಸರ್ವರ್ ಮೂಲಸೌಕರ್ಯ ಜತೆಗೆ ಜಟಿಲ ಸೆಟ್‌ಅಪ್  
- HTTP ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳಿಗೆ ಹೆಚ್ಚುವರಿ ಭದ್ರತಾ ವಿಚಾರಣೆಗಳು  
- ವೆಬ್ ಆಧಾರಿತ ಸಂದರ್ಭಗಳಿಗೆ ಈಗ Streams ಮತ್ತು HTTP ಮೂಲಕ ಬದಲಿ ಮಾಡಲಾಗಿದೆ  

### stdio ಸಾರಿಗೆಯಿಂದ ಸರ್ವರ್ ರಚಿಸುವುದು

ನಮ್ಮ stdio ಸರ್ವರ್ ರಚಿಸಲು, ನಾವು:  

1. **ಆವಶ್ಯಕ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಿ** - MCP ಸರ್ವರ್ ಕಾಂಪೋನೆಂಟ್‌ಗಳು ಮತ್ತು stdio ಸಾರಿಗೆಯ  
2. **ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ** - ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ  
3. **ಟೂಲ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ** - ಬಹಿರಂಗಪಡಿಸಲು ಇಚ್ಛಿಸುವ ಕಾರ್ಯಕ್ಷಮತೆ  
4. **ಸಾರಿಗೆಯನ್ನು ಸೆಟ್‌ಅಪ್ ಮಾಡಿ** - stdio ಸಂವಹನವನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ  
5. **ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ** - ಸಂದೇಶಗಳನ್ನು ನಿರ್ವಹಿಸಿ  

ಹಾಗಾದರೆ ಹಂತ ಹಂತವಾಗಿ ನಿರ್ಮಿಸಲು ಶುರು ಮಾಡೋಣ:

### ಹಂತ 1: ಮೂಲ stdio ಸರ್ವರ್ ರಚನೆ

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ಲಾಗಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ಸರ್ವರ್ ಅನ್ನು ರಚಿಸಿ
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
  
### ಹಂತ 2: ಹೆಚ್ಚುವರಿ ಟೂಲ್ಗಳನ್ನು ಸೇರಿಸು

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
  
### ಹಂತ 3: ಸರ್ವರ್ ಚಾಲನೆ

ಕೋಡ್ ಅನ್ನು `server.py` ಎಂದು ಉಳಿಸಿ ಮತ್ತು ಕಮಾಂಡ್ ಲೈನ್‌ನಿಂದ ಚಾಲನೆ ಮಾಡಿ:

```bash
python server.py
```
  
ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ ಮತ್ತು stdin ನಿಂದ ಇನ್ಪುಟ್‌ಗಾಗಿ ನಿರೀಕ್ಷಿಸುತ್ತದೆ. ಇದು stdio ಸಾರಿಗೆಯ ಮೂಲಕ JSON-RPC ಸಂದೇಶಗಳನ್ನು ವಿನಿಮಯ ಮಾಡುತ್ತದೆ.

### ಹಂತ 4: Inspector ಬಳಸಿ ಪರೀಕ್ಷೆ

ನೀವು ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು MCP Inspector ಬಳಸಿ ಪರೀಕ್ಷಿಸಬಹುದು:  

1. Inspector ಅನ್ನು ಇನ್ಸ್ಟ್‌ಲ್ ಮಾಡಿ: `npx @modelcontextprotocol/inspector`  
2. Inspector ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಸೂಚಿಸಿ  
3. ನೀವು ರಚಿಸಿದ ಟೂಲ್ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ  

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
  
## ನಿಮ್ಮ stdio ಸರ್ವರ್ ಡೀಬಗ್ ಮಾಡುವುದು

### MCP Inspector ಬಳસದು

MCP Inspector MCP ಸರ್ವರ್‌ಗಳ ಡೀಬಗ್ಗಿಂಗ್ ಮತ್ತು ಪರೀಕ್ಷೆಗೆ ಮುಖ್ಯ ಉಪಕರಣವಾಗಿದೆ. ಇದನ್ನು ನಿಮ್ಮ stdio ಸರ್ವರ್ ಜೊತೆಗೆ ಉಪಯೋಗಿಸುವ ವಿಧಾನ:  

1. **Inspector ಇನ್ಸ್ಟ್‌ಲ್ ಮಾಡಿರಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **Inspector ಚಾಲನೆ ಮಾಡಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **ನಿಮ್ಮ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಿ**: Inspector ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ಒದಗಿಸುತ್ತದೆ, ಅಲ್ಲಿ ನೀವು:  
   - ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೋಡಬಹುದು  
   - ವಿಭಿನ್ನ ಪ್ಯಾರಾಮೀಟರ್ಗಳೊಂದಿಗೆ ಟೂಲ್ಗಳನ್ನು ಪರೀಕ್ಷಿಸಬಹುದು  
   - JSON-RPC ಸಂದೇಶಗಳನ್ನು ಜನಾಯಿಸಬಹುದು  
   - ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳನ್ನು ಡೀಬಗ್ ಮಾಡಬಹುದು  

### VS Code ಬಳಸಿ ಡೀಬಗ್ಗಿಂಗ್

ನೀವು ನೀವು MCP ಸರ್ವರ್ ಅನ್ನು ನೇರವಾಗಿ VS Code ನಲ್ಲಿ ಡೀಬಗ್ ಮಾಡಬಹುದು:  

1. `.vscode/launch.json` ನಲ್ಲಿ ಲಂಚ್ ಕಾನ್ಫಿಗರೇಶನ್ ರಚಿಸಿ:  
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
  
2. ಸರ್ವರ್ ಕೋಡ್ ನಲ್ಲಿ ಬ್ರೇಕ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ  
3. ಡೀಬಗ್ಗರ್ ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು Inspector ಬಳಸಿ ಪರೀಕ್ಷೆ ಮಾಡಿ  

### ಸಾಮಾನ್ಯ ಡೀಬಗ್ಗಿಂಗ್ ಸಲಹೆಗಳು

- ಲಾಗ್ ಮಾಡಲು `stderr` ಬಳಸಿ - MCP ಸಂದೇಶಗಳು ಮಾತ್ರ `stdout` ಗೆ ಬರೆಯಿರಿ  
- ಎಲ್ಲಾ JSON-RPC ಸಂದೇಶಗಳು ನ್ಯೂಲೈನ್‌ಗಳಿಂದ ವಿಭಜಿತವಾಗಿರಲಿ  
- ಮೊದಲು ಸರಳ ಟೂಲ್ಗಳಿಂದ ಪರೀಕ್ಷಿಸಿ, ನಂತರ ಸಂಕೀರ್ಣ ಕಾರ್ಯಕ್ಷಮತೆ ಸೇರಿಸಿ  
- ಸಂದೇಶ ಸ್ವರೂಪಗಳ ಪರಿಶೀಲನೆಗಾಗಿ Inspector ಬಳಸಿ  

## VS Code ನಲ್ಲಿ ನಿಮ್ಮ stdio ಸರ್ವರ್ ಉಪಯೋಗಿಸುವುದು

ನೀವು MCP stdio ಸರ್ವರ್ ನಿರ್ಮಿಸಿದ ನಂತರ, ಅದನ್ನು Claude ಅಥವಾ ಇತರ MCP-ಸಂಬಂಧಿತ ಕ್ಲೈಂಟ್‌ಗಳೊಂದಿಗೆ ಉಪಯೋಗಿಸಲು VS Code ಗೆ ಒಂದಾಗಿ ಮಾಡಬಹುದು.

### ಸಂರಚನೆ

1. **MCP ಸಂರಚನಾ ಕಡತವನ್ನು ರಚಿಸಿ** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ಅಥವಾ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):  

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
  
2. **Claude ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ**: ಹೊಸ ಸರ್ವರ್ ಸಂರಚನೆಯನ್ನು ಲೋಡ್ ಮಾಡಲು Claude ಅನ್ನು ಮುಚ್ಚಿ ಮತ್ತೆ ತೆರೆಯಿರಿ.  

3. **ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ**: Claude ಜೊತೆ ಸಂಭಾಷಣೆ ಆರಂಭಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಟೂಲ್ಗಳನ್ನು ಬಳಸಿ ಪರಿಶೀಲಿಸಿ:  
   - "ದಯವಿಟ್ಟು ಹೈಗೆಟಿಂಗ್ ಟೂಲ್ ಬಳಸಿ ನನ್ನನ್ನು ಹಸೆಳಿಸು?"  
   - "15 ಮತ್ತು 27 ಇಣುಕುಗಳ ಮೊತ್ತವನ್ನು ಲೆಕ್ಕಿಸಿ"  
   - "ಸರ್ವರ್ ಮಾಹಿತಿ ಏನು?"  

### TypeScript stdio ಸರ್ವರ್ ಉದಾಹರಣೆ

ಇಲ್ಲಿ ಪೂರ್ಣ TypeScript ಉದಾಹರಣೆ ಇದೆ:  

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

// ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸಿ
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
  
### .NET stdio ಸರ್ವರ್ ಉದಾಹರಣೆ

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
  
## ಸಂಕ್ಷಿಪ್ತ

ಈ ನವೀಕರಿಸಿದ ಪಾಠದಲ್ಲಿ ನೀವು ಕಲಿತದ್ದು:  

- ಪ್ರಸ್ತುತ **stdio ಸಾರಿಗೆ** (ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನ) ಬಳಸಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು  
- SSE ಸಾರಿಗೆ stdio ಮತ್ತು Streams ಮತ್ತು HTTP ಅವತರಣಿಕೆಗಾಗಿ ಅಪ್ರಚಲಿತವಾಗಲಾದ ಕಾರಣ ತಿಳಿದುಕೊಳ್ಳುವುದು  
- MCP ಕ್ಲೈಂಟ್‌ಗಳು ಕರೆ ಮಾಡಬಹುದಾದ ಟೂಲ್ಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು  
- MCP Inspector ಬಳಸಿ ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡುವುದು  
- ನಿಮ್ಮ stdio ಸರ್ವರ್ ಅನ್ನು VS Code ಮತ್ತು Claude ಜತೆ ಏಕೀಕರಿಸುವುದು  

stdio ಸಾರಿಗೆ ಅಪ್ರಚಲಿತ SSE ವಿಧಾನಕ್ಕಿಂತ ಸರಳ, ಭದ್ರತೆಯುತ ಮತ್ತು ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯ ಮೂಲಕ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ. 2025-06-18 ಸ್ಪೆಸಿಫಿಕೇಶನ್ ಪ್ರಕಾರ ಅತಿ ಹೆಚ್ಚಿನ MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನಗಳಿಗೆ ಇದು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ.

### .NET

1. ಮೊದಲು ಕೆಲವು ಟೂಲ್ಗಳನ್ನು ರಚಿಸೋಣ, ಇದಕ್ಕಾಗಿ *Tools.cs* ಎಂಬ ಫೈಲ್ ರಚಿಸಿ, ಕೆಳಗಿನ ವಿಷಯವನ್ನೊಳಗೊಂಡಂತೆ:  

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  
## ಅಭ್ಯಾಸ: ನಿಮ್ಮ stdio ಸರ್ವರ್ ತನಿಖೆ

ನೀವು stdio ಸರ್ವರ್ ನಿರ್ಮಿಸಿದ್ದೀರಿ, ಈಗ ಅದು ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸೋಣ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

1. ನೀವು MCP Inspector ಇನ್ಸ್ಟ್‌ಲ್ ಮಾಡಿರಬೇಕು:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್ ಸಂರಕ್ಷಿಸಲಾಗಿದೆ (ಉದಾ: `server.py`)

### Inspector ಜೊತೆ ಪರೀಕ್ಷೆ

1. **ನಿಮ್ಮ ಸರ್ವರ್ ಮೂಲಕ Inspector ಪ್ರಾರಂಭಿಸಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ತೆರೆಯಿರಿ**: Inspector ನಿಮ್ಮ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುವ ಬ್ರೌಸರ್ ವಿಂಡೋವನ್ನು ತೆರುತ್ತದೆ.  

3. **ಟೂಲ್ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**:  
   - ವಿಭಿನ್ನ ಹೆಸರುಗಳಿಂದ `get_greeting` ಟೂಲ್ ಪ್ರಯತ್ನಿಸಿ  
   - ವಿವಿಧ ಸಂಖ್ಯೆಗಳೊಂದಿಗೆ `calculate_sum` ಟೂಲ್ ಪರೀಕ್ಷಿಸಿ  
   - `get_server_info` ಟೂಲ್ ಕರೆ ಮಾಡಿ ಸರ್ವರ್ ಮೆಟಾಡೇಟಾವನ್ನು ನೋಡಿ  

4. **ಸಂವಹನವನ್ನು ಮಾನಿಟರ್ ಮಾಡಿ**: Inspector ಕ್ಲೈಂಟ್ ಮತ್ತು ಸರ್ವರ್ ನಡುವೆ ವಿನಿಮಯವಾಗುವ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.  

### ನೀವು ನೋಡಬೇಕಾದವು

ನಿಮ್ಮ ಸರ್ವರ್ ಸರಿ ಪ್ರಾರಂಭವಾದಾಗ, ನೀವು ನೋಡಬೇಕಾದವುಗಳು:  
- ಸರ್ಕಾರೆ ಸಮಯದ ಸಾಮರ್ಥ್ಯಗಳು Inspector ನಲ್ಲಿ  
- ಪರೀಕ್ಷಿಸಲು ಲಭ್ಯವಿರುವ ಟೂಲ್ಗಳು  
- ಯಶಸ್ವಿ JSON-RPC ಸಂದೇಶ ವಿನಿಮಯಗಳು  
- ಇಂಟರ್ಫೇಸ್‌ನಲ್ಲಿ ಟೂಲ್ ಪ್ರತಿಕ್ರಿಯೆಗಳು  

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳು

**ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗುವುದಿಲ್ಲ:**  
- ಎಲ್ಲ ಅವಲಂಬನೆಗಳು ಇನ್ಸ್ಟ್‌ಲ್ ಆಗಿವೆಯೇ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ: `pip install mcp`  
- Python ವಾಕ್ಯರಚನೆ ಮತ್ತು ಜಾಗಮಾನ (indentation) ಪರಿಶೀಲಿಸಿ  
- ಕಮಾಂಡ್ ಲೈನ್‌ನಲ್ಲಿ ದೋಷ ಸಂದೇಶಗಳಿಗೆ ಗಮನ ನೀಡಿ  

**ಟೂಲ್ಗಳು ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತಿಲ್ಲ:**  
- `@server.tool()` ಡೆಕೊರೇಟರ್‌ಗಳು ಇದ್ದವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ  
- `main()` ಗಿಂತ ಮುಂಚೆ ಟೂಲ್ ಫಂಕ್ಷನ್‌ಗಳು ವ್ಯಾಖ್ಯಾನಗೊಂಡಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ  
- ಸರ್ವರ್ ಸರಿಯಾಗಿ ಕಾನ್ಫಿಗರ್ ಆಗಿದೆ ಎಂದು ದೃಢೀಕರಿಸಿ  

**ಸಂಪರ್ಕದ ಸಮಸ್ಯೆಗಳು:**  
- ಸರ್ವರ್ stdio ಸಾರಿಗೆಯನ್ನು ಸರಿಯಾಗಿ ಬಳಸಿ ಎಂದು ಪರಿಶೀಲಿಸಿ  
- ಬೇರೆ ಪ್ರಕ್ರಿಯೆಗಳು ಹಸ್ತಕ್ಷೇಪ ಮಾಡುತ್ತಿಲ್ಲದೆಯೇ ನೋಡಿಕೊಳ್ಳಿ  
- Inspector ಕಮಾಂಡ್ ನಿರಾಕರಣೆಯನ್ನು ತಪಾಸಣೆ ಮಾಡಿ  

## ಸರ್ಕಾರಿ ಕೆಲಸ

ನಿಮ್ಮ ಸರ್ವರ್‌ಗೆ ಹೆಚ್ಚು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಪ್ರಯತ್ನಿಸಿ. ಉದಾಹರಣೆಗೆ [ಈ ಪುಟ](https://api.chucknorris.io/) ಅನ್ನು ನೋಡಿ ಒಂದು API ಕರೆ ಮಾಡಬಹುದಾದ ಟೂಲ್ ಸೇರಿಸಿ. ನೀವು ಸರ್ವರ್ ಹೇಗಿರಬೇಕು ಎಂದು ತೀರ್ಮಾನಿಸಿ. ಸಂತೋಷ ಉಳ್ಳמיתು :)

## ಪರಿಹಾರ

[ಪರಿಹಾರ](./solution/README.md) ಇಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್ ಜೊತೆಗೆ ಸಾಧ್ಯವಾದ ಪರಿಹಾರ ಇದಾಗಿದೆ.

## ಪ್ರಮುಖ ಅಂಶಗಳು

ಈ ಅಧ್ಯಾಯದ ಪ್ರಮುಖ ಅಂಶಗಳು:

- stdio ಸಾರಿಗೆ ಸ್ಥಳೀಯ MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.  
- ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ ಹಾಗೂ ಔಟ್ಪುಟ್ ಸ್ಟ್ರೀಂಗಳ ಮೂಲಕ MCP ಸರ್ವರ್‌ಗಳು ಮತ್ತು ಕ್ಲೈಂಟ್‌ಗಳು ಸತತ ಸಂವಹನ ಮಾಡಬಹುದು.  
- Inspector ಮತ್ತು Visual Studio Code ಎರಡೂ stdio ಸರ್ವರ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಉಪಯೋಗಿಸಲು ಹಾಗೂ ಡೀಬಗ್ ಮಾಡಲು ಅನುಕೂಲಕರ.  

## ಮಾದರಿಗಳು 

- [Java ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)  
- [.Net ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)  
- [TypeScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)  
- [Python ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)  

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ಮುಂದಿನ ಹಂತಗಳು

## ಮುಂದಿನ ಹಂತಗಳು

stdio ಸಾರಿಗೆಯಲ್ಲಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ನೀವು ಕಲಿತಿದ್ದೀರಿ, ಹಾಗಾದರೆ ನೀವು ಹೆಚ್ಚಿನ ಉನ್ನತ ವಿಷಯಗಳನ್ನು ಅನ್ವೇಷಿಸಬಹುದು:  

- **ಮುಂದೆ**: [MCP ನೊಂದಿಗೆ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ (Streams ಮತ್ತು HTTP)](../06-http-streaming/README.md) - ದೂರಸೇವಕರಿಗೆ ಇನ್ನೊಂದು ಬೆಂಬಲಿತ ಸಾರಿಗೆ ವ್ಯವಸ್ಥೆಯನ್ನು ತಿಳಿದುಕೊಳ್ಳಿ  
- **ಉನ್ನತ**: [MCP ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](../../02-Security/README.md) - ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗಳಲ್ಲಿ ಭದ್ರತೆಯನ್ನು ಜಾರಿಗೆ ತರಲು  
- **ಉತ್ಪಾದನಾ**: [ನಿಯೋಜನೆ ತಂತ್ರಗಳು](../09-deployment/README.md) - ಉತ್ಪಾದನೆಗೆ ನಿಮ್ಮ ಸರ್ವರ್‌ಗಳನ್ನು ನಿಯೋಜಿಸುವುದು  

## ಹೆಚ್ಚಿನ ಸಂಪನ್ಮೂಲಗಳು

- [MCP ಸ್ಪೆಸಿಫಿಕೇಶನ್ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ಅಧಿಕೃತ ಸ್ಪೆಸಿಫಿಕೇಶನ್  
- [MCP SDK ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/modelcontextprotocol/sdk) - ಎಲ್ಲಾ ಭಾಷೆಗಳ SDK ರೆಫರನ್ಸ್  
- [ಸಮುದಾಯ ಉದಾಹರಣೆಗಳು](../../06-CommunityContributions/README.md) - ಸಮುದಾಯದಿಂದ ಹೆಚ್ಚಿನ ಸರ್ವರ್ ಉದಾಹರಣೆಗಳು

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ನಿರಾಕರಣೆ**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದೆಂದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಅತ್ಯಾವಶ್ಯಕ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದಾದರೂ ಗೊಂದಲಗಳು ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರಿಯಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->