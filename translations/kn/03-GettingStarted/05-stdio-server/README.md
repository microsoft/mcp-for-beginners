# MCP ಸರ್ವರ್ stdio ಸಾರಿಗೆೊಂದಿಗೆ

> **⚠️ ಪ್ರಮುಖ ಅಪ್ಡೇಟ್**: MCP ನಿರ್ದಿಷ್ಟಿಕೆ 2025-06-18 ರಿಂದ, ಸ್ವತಂತ್ರ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್ಸ್) ಸಾರಿಗೆ **ನಿಷೇಧಿಸಲಾಗಿದೆ** ಮತ್ತು "Streamable HTTP" ಸಾರಿಗೆಯಿಂದ ಬದಲಿ ಆಗಿದೆ. ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟಿಕೆಯಲ್ಲಿ ಎರಡು ಪ್ರಮುಖ ಸಾರಿಗೆ ವಿಧಾನಗಳು ಇದೆ:
> 1. **stdio** - ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್/ಆuotput (ಸ್ಥಳೀಯ ಸರ್ವರ್‌ಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
> 2. **Streamable HTTP** - SSE ಒಳಗೊಳ್ಳುವ ದೂರ ಸರ್ವರ್‌ಗಳಿಗೆ
>
> ಈ ಪಾಠ stdio ಸಾರಿಗೆಯ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಲು ನವೀಕರಿಸಲಾಗಿದೆ, ಇದು ಹೆಚ್ಚಿನ MCP ಸರ್ವರ್ ಜಾರಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.

stdio ಸಾರಿಗೆ MCP ಸರ್ವರ್‌ಗಳು ಗ್ರಾಹಕರೊಂದಿಗೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ ಮತ್ತು ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ. ಇದು ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟಿಕೆಯಲ್ಲಿ ಅತ್ಯಂತ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸುವ ಮತ್ತು ಶಿಫಾರಸು ಮಾಡಲಾದ ಸಾರಿಗೆ ವಿಧಾನವಾಗಿದೆ, ಇವು ವಿವಿಧ ಗ್ರಾಹಕ ಆಪ್ಲಿಕೇಶನ್‌ಗಳೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಸಂಯೋಜಿಸಲು ಸುಲಭವಾಗುವ ಸರಳ ಮತ್ತು ಪರಿಣಾಮಕಾರಿಯಾದ ಮಾರ್ಗದೊಂದಿಗೆ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

## ಅವಲೋಕನ

ಈ ಪಾಠದಲ್ಲಿ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್‌ಗಳನ್ನು ಹೇಗೆ ನಿರ್ಮಿಸಿ ಬಳಸುವುದು ಎಂಬುದನ್ನು ಕವರ್ ಮಾಡುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ, ನೀವು ಈ القدرة ಗಳಿಸಬಹುದು:

- stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್ ನಿರ್ಮಿಸಲು.
- ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡಲು.
- Visual Studio Code ಬಳಸಿ MCP ಸರ್ವರ್ ಉಪಯೋಗಿಸಲು.
- ಪ್ರಸ್ತುತ MCP ಸಾರಿಗೆ ವಿಧಗಳು ಮತ್ತು stdio ಯು ಏಕೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು.

## stdio ಸಾರಿಗೆ - ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

stdio ಸಾರಿಗೆ ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟಿಕೆ (2025-06-18) ನಲ್ಲಿ ಬೆಂಬಲಿತ ಎರಡು ಸಾರಿಗೆ ವಿಧಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಎಂಬುದನ್ನು ನೋಡೋಣ:

- **ಸರಳ ಸಂವಹನ**: ಸರ್ವರ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ (`stdin`) ರಿಂದ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಓದುತ್ತದೆ ಮತ್ತು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಔಟ್‌ಪುಟ್ (`stdout`) ಗೆ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುತ್ತದೆ.
- **ಪ್ರಕ್ರಿಯೆ ಆಧಾರಿತ**: ಗ್ರಾಹಕ MCP ಸರ್ವರ್ ಅನ್ನು ಉಪಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ.
- **ಸಂದೇಶ ಸ್ವರೂಪ**: ಸಂದೇಶಗಳು ಪ್ರತ್ಯೇಕವಾದ JSON-RPC ವಿನಂತಿಗಳು, ಅಧಿಸೂಚನೆಗಳು ಅಥವಾ ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಹೊಸ ಸಾಲುಗಳಿಂದ ವಿಭಜಿಸಲ್ಪಟ್ಟಿವೆ.
- **ಲಾಗಿಂಗ್**: ಸರ್ವರ್ ಲಾಗಿಂಗ್ ಉದ್ದೇಶಗಳಿಗಾಗಿ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಎರರ್ (`stderr`) ಗೆ UTF-8 ಸ್ಟ್ರಿಂಗ್ ಬರೆಯಬಹುದು.

### ಪ್ರಮುಖ ಅವಶ್ಯಕತೆಗಳು:
- ಸಂದೇಶಗಳು ಹೊಸ ಸಾಲುಗಳಿಂದ ವಿಭಜಿಸುವಂತೆ ಆಗಿರಬೇಕು ಮತ್ತು ಒಳಗೊಳ್ಳದ ಹೊಸ ಸಾಲುಗಳಿರಬಾರದು
- ಸರ್ವರ್ ಮಾನ್ಯವಲ್ಲದ MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ `stdout` ಗೆ ಬರೆಯಬಾರದು
- ಗ್ರಾಹಕ ಮಾನ್ಯವಲ್ಲದ MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ ಸರ್ವರ್ `stdin` ಗೆ ಬರೆಯಬಾರದು

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- ನಾವು MCP SDK ಯಿಂದ `Server` ಕ್ಲಾಸ್ ಮತ್ತು `StdioServerTransport` ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ
- ಪ್ರಾಥಮಿಕ ಕಾನ್ಫಿಗರೇಶನ್ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸುತ್ತೇವೆ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ಸರ್ವರ್ ಇನ್ಸ್ಟಾನ್ಸ್ ರಚಿಸಿ
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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- MCP SDK ಅನ್ನು ಬಳಸಿಕೊಂಡು ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಲಾಗಿದೆ
- ಡೆಕೋರೇಟರ್‌ಗಳನ್ನು ಬಳಸಿ ಸಾಧನಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ
- stdio_server ಕಾಂಟೆಕ್ಸ್ಟ್ ಮ್ಯಾನೇಜರ್ ಅನ್ನು ಸಾರಿಗೆಗಾಗಿ ಹ್ಯಾಂಡಲ್ ಮಾಡಲಾಗುತ್ತದೆ

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

SSE ಯಿಂದ ಮುಖ್ಯ ಭೇದವೆಂದರೆ stdio ಸರ್ವರ್‌ಗಳು:

- ವೆಬ್ ಸರ್ವರ್ ಸೆಟಪ್ ಅಥವಾ HTTP ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಅವಶ್ಯಕತೆ ಮಾಡಿಕೊಳ್ಳುವುದಿಲ್ಲ
- ಗ್ರಾಹಕದಿಂದ ಉಪಪ್ರಕ್ರಿಯೆಗಳಾಗಿ ಪ್ರಾರಂಭಗೊಳ್ಳುತ್ತವೆ
- stdin/stdout ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡುತ್ತವೆ
- ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಮತ್ತು ಡೀಬಗ್ ಮಾಡಲು ಸರಳವಾಗಿದೆ

## ಅಭ್ಯಾಸ: stdio ಸರ್ವರ್ ರಚನೆ

ನಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ರಚಿಸಲು, ನಾವು ಎರಡು ವಿಷಯಗಳನ್ನು ಗಮನಿಸಬೇಕು:

- ಸಂಪರ್ಕ ಮತ್ತು ಸಂದೇಶಗಳ ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಪ್ರದರ್ಶಿಸಲು ನಮಗೆ ವೆಬ್ ಸರ್ವರ್ ಅಗುತ್ತದೆ.

## ಪ್ರಯೋಗ: ಸರಳ MCP stdio ಸರ್ವರ್ ರಚನೆ

ಈ ಪ್ರಯೋಗದಲ್ಲಿ, ನಾವು ಶಿಫಾರಸು ಮಾಡಲಾದ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸರಳ MCP ಸರ್ವರ್ ಅನ್ನು ರಚಿಸುತ್ತೇವೆ. ಈ ಸರ್ವರ್‌ವು ಗ್ರಾಹಕರು ಮಾನಕ Model Context Protocol ಬಳಸಿ ಕರೆ ಮಾಡಬಹುದಾದ ಸಾಧನಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ.

### ಪೂರ್ವಪಯೋಗಗಳು

- Python 3.8 ಅಥವಾ ಅದಕ್ಕೆ ಮೇಲು
- MCP Python SDK: `pip install mcp`
- ಅಸ್ಯಿಂಕ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮೂಲಭೂತ ಜ್ಞಾನ

ನಮ್ಮ ಮೊದಲ MCP stdio ಸರ್ವರ್ ಅನ್ನು ರಚಿಸುವುದರಿಂದ ಪ್ರಾರಂಭಿಸೋಣ:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ಲಾಗಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ಸರ್ವರ್ ಸೃಷ್ಟಿಸಿ
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
    # stdio ಸಾರಿಗೆವನ್ನು ಬಳಸಿರಿ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## ನಿಷೇಧಗೊಂಡ SSE ವಿಧಾನದಿಂದ ಮುಖ್ಯ ಭೇದಗಳು

**Stdio ಸಾರಿಗೆ (ಪ್ರಸ್ತುತ ಮಾನಕ):**
- ಸರಳ ಉಪಪ್ರಕ್ರಿಯೆ ಮಾದರಿ - ಗ್ರಾಹಕ ಸರ್ವರ್ ಅನ್ನು ಚೈಲ್ಡ್ ಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ
- stdin/stdout ಮೂಲಕ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಸಂವಹನ ಮಾಡುತ್ತದೆ
- HTTP ಸರ್ವರ್ ಸೆಟಪ್ ಅಗತ್ಯವಿಲ್ಲ
- ಉತ್ತಮ ಕಾರ್ಯಕ್ಷमता ಮತ್ತು ಭದ್ರತೆ
- ಸುಲಭ ಡೀಬಗ್ ಮತ್ತು ಅಭಿವೃದ್ಧಿ

**SSE ಸಾರಿಗೆ (MCP 2025-06-18 ರಿಂದ ನಿಷೇಧಿತ):**
- SSE ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳಳ್ಳಿರುವ HTTP ಸರ್ವರ್ ಅಗತ್ಯವಿತ್ತು
- ವೆಬ್ ಸರ್ವರ್ ಇನ್ಫ್ರಾಸ್ಟ್ರಕ್ಟರ್ ಜೊತೆಗೆ ಗೊಂದಲಕಾರಿಯಾದ ಸೆಟಪ್
- HTTP ಎಂಡ್ಪಾಯಿಂಟ್‌ಗಳ ಭದ್ರತೆಗಾಗಿ ಹೆಚ್ಚುವರಿ ಪರಿಗಣನೆಗಳು
- ಈಗ Streamable HTTP ಮೂಲಕ ಬದಲಿಸಲಾಗಿದೆ ವೆಬ್ ಆಧಾರಿತ ಪರಿಸ್ಥಿತಿಗಳಿಗಾಗಿ

### stdio ಸಾರಿಗೆಯೊಂದಿಗೆ ಸರ್ವರ್ ಸೃಷ್ಟಿಸುವುದು

ನಮ್ಮ stdio ಸರ್ವರ್ ರಚಿಸಲು ನಾವು ಈ ಕ್ರಮಗಳನ್ನು ಅನುಸರಿಸಬೇಕು:

1. **ಅವಶ್ಯಕ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಿ** - MCP ಸರ್ವರ್ ಕಂಪೋನೆಂಟ್‌ಗಳು ಮತ್ತು stdio ಸಾರಿಗೆ
2. **ಸರ್ವರ್ ಉದಾಹರಣೆ ರಚಿಸಿ** - ಅದರ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
3. **ಸಾಧನಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ** - ನೀಡಲು ಬಯಸುವ ಕಾರ್ಯಗಳನ್ನೊಳಗೊಂಡು
4. **ಸಾರಿಗೆ ಸಂರಚಿಸಿ** - stdio ಸಂವಹನವನ್ನು ಸಂರಚಿಸಿ
5. **ಸರ್ವರ್ ಚಾಲನೆ** - ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಸಂದೇಶಗಳನ್ನು ನಿರ್ವಹಿಸಿ

ನಾವು ಹಂತ ಹಂತವಾಗಿ ಇದನ್ನು ನಿರ್ಮಿಸೋಣ:

### ಹಂತ 1: ಮೂಲ stdio ಸರ್ವರ್ ರಚಿಸಿ

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ಲಾಗಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ಸರ್ವರ್ ರಚಿಸಿ
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


### ಹಂತ 2: ಇನ್ನಷ್ಟು ಸಾಧನಗಳನ್ನು ಸೇರಿಸಿ

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

ಕೋಡ್ ಅನ್ನು `server.py` ಎಂದು ಉಳಿಸಿ, ಮತ್ತು ಕಮಾಂಡ್ ಲೈನ್‌ನಿಂದ ಚಾಲನೆ ಮಾಡಿ:

```bash
python server.py
```


ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗಿ stdin ನಿಂದ ಇನ್ಪುಟ್ ನಿರೀಕ್ಷಿಸುತ್ತದೆ. ಇದು stdio ಸಾರಿಗೆಯಲ್ಲಿ JSON-RPC ಸಂದೇಶಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡುತ್ತದೆ.

### ಹಂತ 4: ಇನ್ಸ್ಪೆಕ್ಟರ್ ಮೂಲಕ ಪರೀಕ್ಷೆ

ನೀವು MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಸರ್ವರ್ ಪರೀಕ್ಷೆ ಮಾಡಬಹುದು:

1. ಇನ್ಸ್ಪೆಕ್ಟರ್ ಅನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ: `npx @modelcontextprotocol/inspector`  
2. ಇನ್ಸ್ಪೆಕ್ಟರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಕಡೆಗೆ ಸೂಚಿಸಿ  
3. ನೀವು ರಚಿಸಿದ ಸಾಧನಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ  

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## ನಿಮ್ಮ stdio ಸರ್ವರ್ ಡೀಬಗ್ ಮಾಡುವದು

### MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಳಕೆ

MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಡೀಬಗ್ ಮತ್ತು ಪರೀಕ್ಷಿಸುವುದಕ್ಕೆ ಅಮೂಲ್ಯ ಸಾಧನವಾಗಿದೆ. ಇದನ್ನು ನಿಮ್ಮ stdio ಸರ್ವರ್ ಜೊತೆ ಹೇಗೆ ಬಳಸುವುದು ಎಂಬುದನ್ನು ನೋಡೋಣ:

1. **ಇನ್ಸ್ಪೆಕ್ಟರ್ ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```
  
2. **ಇನ್ಸ್ಪೆಕ್ಟರ್ ರನ್ಮಾಡಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
3. **ನಿಮ್ಮ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಿ**:  
   - ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವೀಕ್ಷಿಸಿ  
   - ವಿಭಿನ್ನ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ಸಾಧನಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ  
   - JSON-RPC ಸಂದೇಶಗಳನ್ನು ವೀಕ್ಷಿಸಿ  
   - ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳನ್ನು ಡೀಬಗ್ ಮಾಡಿ  

### VS Code ಬಳಕೆ

ನೀವು ನಿಮ್ಮ MCP ಸರ್ವರ್ ಅನ್ನು ನೇರವಾಗಿ VS Code ನಲ್ಲಿ ಡೀಬಗ್ ಮಾಡಬಹುದು:

1. `.vscode/launch.json` ನಲ್ಲಿ ಲಾಂಚ್ ಕಾನ್ಫಿಗರೇಶನ್ ರಚಿಸಿ:  
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
  
2. ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್‌ನಲ್ಲಿ ಬ್ರೇಕ್ ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಹೊಂದಿಸಿ  
3. ಡೀಬಗೆರ್ ಅನ್ನು ರನ್ ಮಾಡಿ ಮತ್ತು ಇನ್ಸ್ಪೆಕ್ಟರ್‌ನೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ  

### ಸಾಮಾನ್ಯ ಡೀಬಗ್ ಟಿಪ್ಸ್

- ಲಾಗ್ಗಿಂಗ್‌ಗಾಗಿ `stderr` ಬಳಸಿರಿ - `stdout` ಗೆ ಬರೆಯಬೇಡಿ, ಅದು MCP ಸಂದೇಶಗಳಿಗೆ ಮೀಸಲಾಗಿದೆ  
- ಎಲ್ಲಾ JSON-RPC ಸಂದೇಶಗಳು ಹೊಸ ಸಾಲಿನಿಂದ ವಿಭಜಿತವಾಗಿರಬೇಕು  
- ಕುಲಾಯಿಸಿದ ಸಾಧನಗಳಿಂದ ಪ್ರಾರಂಭಿಸಿ ಮುಂಚೆ ಸಂಕೀರ್ಣ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸೇರಿಸುವುದಕ್ಕೆ ಮುಂದಾಗಿರಿ  
- ಸಂದೇಶ ರೂಪಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಳಸಿ  

## VS Code ನಲ್ಲಿ ನಿಮ್ಮ stdio ಸರ್ವರ್ ಉಪಯೋಗಿಸುವುದು

ನೀವು MCP stdio ಸರ್ವರ್ ರಚಿಸಿದ ನಂತರ, ಅದನ್ನು VS Code ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ Claude ಅಥವಾ ಇतर MCP-ಹೊಂದಾಣಿಕೆಯ ಗ್ರಾಹಕರೊಂದಿಗೆ ಬಳಸಬಹುದು.

### ಸಂರಚನೆ

1. `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ಅಥವಾ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) ನಲ್ಲಿ MCP ಸಂರಚನಾ ಫೈಲ್ ರಚಿಸಿ:  
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
  
2. Claude ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ: ಹೊಸ ಸರ್ವರ್ ಸಂರಚನೆಯನ್ನು ಲೋಡ್ ಮಾಡಲು Claude ಅನ್ನು ಮುಚ್ಚಿ ಮತ್ತೆ ತೆರೆಯಿರಿ.  

3. ಸಂಪರ್ಕ ಪರೀಕ್ಷಿಸಿ: Claude ಜೊತೆ ಸಂಭಾಷಣೆ ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಸಾಧನಗಳನ್ನು ಪ್ರಯೋಗಿಸಿ:  
   - "ನನಗೆ ಅಭಿನಂದನೆಯ ಸಾಧನವನ್ನು ಬಳಸಿ ಆಗಮಿಸಬಹುದುವೇ?"  
   - "15 ಮತ್ತು 27 ಗಳ ಮೊತ್ತ ಎಣಿಸಿ"  
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
  
## ಸಾರಾಂಶ

ಈ ನವೀಕರಿಸಿದ ಪಾಠದಲ್ಲಿ, ನೀವು ಕಲಿತದ್ದೇನಂದರೆ:

- ಪ್ರಸ್ತುತ **stdio ಸಾರಿಗೆ** (ಶಿಫಾರಸುಮಾಡಲಾದ ವಿಧಾನ) ಬಳಸಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು  
- SSE ಸಾರಿಗೆ stdio ಮತ್ತು Streamable HTTP ಗೆ ಯಾಕೆ ನಿಷೇಧಿಸಲ್ಪಟ್ಟಿತು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು  
- MCP ಗ್ರಾಹಕರು ಕರೆ ಮಾಡಬಹುದಾದ ಸಾಧನಗಳನ್ನು ರಚಿಸುವುದು  
- MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಳಸಿ ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ಡೀಬಗ್ ಮಾಡುವುದು  
- VS Code ಮತ್ತು Claude ಜೊತೆಗೆ ನಿಮ್ಮ stdio ಸರ್ವರ್ ಸಂಯೋಜಿಸುವುದು  

stdio ಸಾರಿಗೆ ನಿಷೇಧಗೊಂಡ SSE ವಿಧಾನಕ್ಕಿಂತ ಸರಳ, ಹೆಚ್ಚು ಭದ್ರ, ಮತ್ತು ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಒದಗಿಸುವ ಮಾರ್ಗವಾಗಿದೆ. 2025-06-18 ನಿರ್ದಿಷ್ಟಿಕೆಯ ಪ್ರಕಾರ ಬಹು MCP ಸರ್ವರ್ ಜಾರಿಗೆ ಶಿಫಾರಸುಮಾಡಲಾದ ಸಾರಿಗೆ ಇದು.

### .NET

1. ಮೊದಲು ಕೆಲವು ಸಾಧನಗಳನ್ನು ರಚಿಸೋಣ, ಇದಕ್ಕಾಗಿ *Tools.cs* ಎಂಬ ಫೈಲ್ ಅನ್ನು ಕೆಳಗಿನ ವಿಷಯೊಟ್ಟಿಗೆ ರಚಿಸಲಾಗುತ್ತದೆ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```
  

## ಅಭ್ಯಾಸ: ನಿಮ್ಮ stdio ಸರ್ವರ್ ಪರೀಕ್ಷೆ

ಈಗ ನೀವು stdio ಸರ್ವರ್ ರಚಿಸಿದ್ದೀರಿ, ಅದನ್ನು ಸರಿಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದಾಗಿ ಪರೀಕ್ಷಿಸೋಣ.

### ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

1. MCP ಇನ್ಸ್ಪೆಕ್ಟರ್ ಇನ್ಸ್ಟಾಲ್ ಆಗಿರಬೇಕು:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್ ಉಳಿಸಲಾಗಿರಬೇಕು (ಉದಾ. `server.py`)

### ಇನ್ಸ್ಪೆಕ್ಟರ್ ಮೂಲಕ ಪರೀಕ್ಷೆ

1. **ನಿಮ್ಮ ಸರ್ವರ್ ಜೊತೆಗೆ ಇನ್ಸ್ಪೆಕ್ಟರ್ ಪ್ರಾರಂಭಿಸಿ**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ತೆರೆದುಕೊಳ್ಳಿ**: ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬ್ರೌಸರ್ ವಿಂಡೋ ತೆರೆದೀಗ ನಿಮ್ಮ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುತ್ತದೆ.

3. **ಸಾಧನಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**:  
   - ವಿಭಿನ್ನ ಹೆಸರುಗಳೊಂದಿಗೆ `get_greeting` ಸಾಧನವನ್ನು ಪ್ರಯೋಗಿಸಿ  
   - ವಿವಿಧ ಸಂಖ್ಯೆಗಳೊಂದಿಗೆ `calculate_sum` ಸಾಧನವನ್ನು ಪರೀಕ್ಷಿಸಿ  
   - `get_server_info` ಸಾಧನವನ್ನು ಕರೆಸಿ ಸರ್ವರ್ ಮೆಟಾಡೇಟಾ ನೋಡಿ  

4. **ಸಂವಹನವನ್ನು ವೀಕ್ಷಿಸಿ**: ಇನ್ಸ್ಪೆಕ್ಟರ್ ಗ್ರಾಹಕ ಮತ್ತು ಸರ್ವರ್ ನಡುವೆ ವಿನಿಮಯವಾಗುವ JSON-RPC ಸಂದೇಶಗಳನ್ನು ತೋರಿಸುತ್ತದೆ.

### ನೀವು ಏನು ನೋಡಬೇಕು

ನಿಮ್ಮ ಸರ್ವರ್ ಸರಿಯಾಗಿ ಪ್ರಾರಂಭವಾದಾಗ ನೀವು ಕಾಣುವುದು:  
- ಇನ್ಸ್ಪೆಕ್ಟರ್‌ನಲ್ಲಿ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳ ಪಟ್ಟಿ  
- ಪರೀಕ್ಷೆಗಾಗಿ ಲಭ್ಯವಾಗಿರುವ ಸಾಧನಗಳು  
- JSON-RPC ಸಂದೇಶ ವಿನಿಮಯ ಸಫಲವಾದುದು  
- ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಇಂಟರ್ಫೇಸ್ನಲ್ಲಿ ಪ್ರದರ್ಶಿತವಾದವು

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳು

**ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗುತ್ತಿಲ್ಲ:**  
- ಎಲ್ಲಾ ಅವಲಂಬನೆಗಳು ಸ್ಥಾಪಿತವಿರುವುದನ್ನು ಪರಿಶೀಲಿಸಿ: `pip install mcp`  
- Python ಸಿಂಟ್ಯಾಕ್ಸ್ ಮತ್ತು ಇಂದೆಂಟೇಷನ್ ಪರಿಶೀಲಿಸಿ  
- ಕಮಾಂಡ್ ಕಾನ್ಸೋಲ್ ನಲ್ಲಿ ದೋಷ ಸಂದೇಶಗಳನ್ನು ನೋಡಿ  

**ಸಾಧನಗಳು ಕಾಣಿಸತಕ್ಕಂತೆ ಇಲ್ಲ:**  
- `@server.tool()` ಡೆಕೋರೇಟರ್‌ಗಳು ಇರಬೇಕಾಗಿವೆ  
- ಸಾಧನ ಫಂಕ್ಷನ್‌ಗಳು `main()` ಹಿಂದೆนิರ್ಧಿಷ್ಟವಾಗಿರಬೇಕು  
- ಸರ್ವರ್ ಸರಿಯಾಗಿ ಸಂರಚಿತವಾಗಿರಬೇಕು  

**ಕನೆಕ್ಷನ್ ಸಮಸ್ಯೆಗಳು:**  
- ಸರ್ವರ್ ಸರಿಯಾಗಿ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಕೆ ಮಾಡುತ್ತಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ  
- ಇತರ ಯಾವುದೇ ಪ್ರಕ್ರಿಯೆಗಳು ಹಸ್ತಕ್ಷೇಪ ಮಾಡುತ್ತಿಲ್ಲವೆಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ  
- ಇನ್ಸ್ಪೆಕ್ಟರ್ ಕಮಾಂಡ್ ಸಿಂಟ್ಯಾಕ್ಸ್ ಪರಿಶೀಲಿಸಿ  

## ಅಸೈನ್ಮೆಂಟ್

ನಿಮ್ಮ ಸರ್ವರ್‌ನಲ್ಲಿ ಹೆಚ್ಚು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಪ್ರಯತ್ನಿಸಿ. [ಈ ಪುಟವನ್ನು](https://api.chucknorris.io/) ನೋಡಿ, ಉದಾಹರಣೆಗೆ, API ಕರೆ ಮಾಡಬಹುದಾದ ಸಾಧನವನ್ನು ಸೇರಿಸಿ. ನಿಮ್ಮ ಸರ್ವರ್ ಹೇಗಿರಬೇಕು ಎಂದು ನೀವು ನಿರ್ಧರಿಸು. ಆನಂದಿಸಿ :)

## ಪರಿಹಾರ

[ಪರಿಹಾರ](./solution/README.md) ಇದು ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್ ಜೊತೆ ಒಂದು ಸಾಧ್ಯ ಪರಿಹಾರವಾಗಿದೆ.

## ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಅಧ್ಯಾಯದಿಂದ ಪ್ರಮುಖ ಪಾಠಗಳು:

- stdio ಸಾರಿಗೆ ಸ್ಥಳೀಯ MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಶಿಫಾರಸುಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.
- stdio ಸಾರಿಗೆಯು MCP ಸರ್ವರ್‌ಗಳು ಮತ್ತು ಗ್ರಾಹಕರ ಮಧ್ಯೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್ಪುಟ್ ಮತ್ತು ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ನಿರಂತರ ಸಂವಹನವನ್ನು ಅನುಮತಿಸುತ್ತದೆ.
- stdio ಸರ್ವರ್‌ಗಳನ್ನು ನೇರವಾಗಿ ಉಪಯೋಗಿಸಲು ನೀವು ಇನ್ಸ್ಪೆಕ್ಟರ್ ಮತ್ತು Visual Studio Code ಎರಡನ್ನೂ ಬಳಸಬಹುದು, ಇದು ಡೀಬಗ್ ಮತ್ತು ಸಂಯೋಜನೆಯನ್ನು ಸುಲಭಗೊಳಿಸುತ್ತದೆ.

## ಮಾದರಿಗಳು

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ಮುಂದೇನು

## ಮುಂದಿನ ಹಂತಗಳು

stdio ಸಾರಿಗೆ ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ನೀವು ಕಲಿತಿದ್ದೀರಿ, ಇದಕ್ಕೆ ಮುಂದುವರೆದು ಅವರಹಿತ ವಿಷಯಗಳನ್ನು ಅನ್ವೇಷಿಸಬಹುದು:

- **ಮುಂದೆ**: [HTTP ಸ್ಟ್ರೀಮಿಂಗ್ MCP (Streamable HTTP)](../06-http-streaming/README.md) - ದೂರಸರ್ವರ್‌ಗಳ үчүн ಅನ್ಯ ಬೆಂಬಲಿತ ಸಾರಿಗೆ ವಿಧಾನವನ್ನು ತಿಳಿದುಕೊಳ್ಳಿ  
- **ಮುಖ್ಯ**: [MCP ಭದ್ರತೆ ಉತ್ತಮ ವಿಧಾನಗಳು](../../02-Security/README.md) - ನಿಮ್ಮ MCP ಸರ್ವರ್‌ಗಳಲ್ಲಿ ಭದ್ರತೆಯನ್ನು ಅನ್ವಯಿಸಿ  
- **ಉತ್ಪಾದನೆ**: [ಪ್ರವೃತ್ತಿ ತಂತ್ರಗಳು](../09-deployment/README.md) - ಉತ್ಪಾದನಾ ಬಳಕೆಗೆ ನಿಮ್ಮ ಸರ್ವರ್‌ಗಳನ್ನು ನಿಯೋಜಿಸಿ  

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [MCP ನಿರ್ದಿಷ್ಟಿಕೆ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ಅಧಿಕೃತ ನಿರ್ದಿಷ್ಟಿಕೆ  
- [MCP SDK ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/modelcontextprotocol/sdk) - ಎಲ್ಲಾ ಭಾಷೆಗಳ SDK ರೆಫರೆನ್ಸ್‌ಗಳು  
- [ಸಮುದಾಯ ಉದಾಹರಣೆಗಳು](../../06-CommunityContributions/README.md) - ಸಮುದಾಯದಿಂದ ಹೆಚ್ಚಿನ ಸರ್ವರ್ ಉದಾಹರಣೆಗಳು

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತಪಾಸಣೆ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಫಲಿತಾಂಶಕ್ಕಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದಾಗಿದೆ ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯ ವಸ್ತುನಿಷ್ಠ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಲಾಗಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದಕಾರರ ಸೇವೆಯನ್ನು ಬಳಸುವುದು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಸಮಜ್ಞಾಪನೆ ತಪ್ಪುಗಳು ಅಥವಾ ಅರ್ಥಮುಖತೆಯ ಹೊಣೆಗಾರಿಕೆ ನಮ್ಮದಲ್ಲಿ ಇಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->