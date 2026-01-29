# stdio ಸಾರಿಗೆ ಹೊಂದಿರುವ MCP ಸರ್ವರ್

> **⚠️ ಪ್ರಮುಖ ನವೀಕರಣ**: MCP ನಿರ್ದಿಷ್ಟತೆ 2025-06-18 ರಿಂದ, ಸ್ವತಂತ್ರ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್ಸ್) ಸಾರಿಗೆ **ನಿರಾಕರಿಸಲಾಗಿದೆ** ಮತ್ತು "ಸ್ಟ್ರೀಮಬಲ್ HTTP" ಸಾರಿಗೆಯಿಂದ ಬದಲಾಯಿಸಲಾಗಿದೆ. ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟತೆ ಎರಡು ಪ್ರಮುಖ ಸಾರಿಗೆ ವಿಧಾನಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ:
> 1. **stdio** - ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್‌ಪುಟ್/ಔಟ್‌ಪುಟ್ (ಸ್ಥಳೀಯ ಸರ್ವರ್‌ಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
> 2. **Streamable HTTP** - SSE ಅನ್ನು ಆಂತರಿಕವಾಗಿ ಬಳಸಬಹುದಾದ ದೂರದ ಸರ್ವರ್‌ಗಳಿಗೆ
>
> ಈ ಪಾಠವನ್ನು **stdio ಸಾರಿಗೆ** ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸಲು ನವೀಕರಿಸಲಾಗಿದೆ, ಇದು ಬಹುತೇಕ MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.

stdio ಸಾರಿಗೆ MCP ಸರ್ವರ್‌ಗಳು ಗ್ರಾಹಕರೊಂದಿಗೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್‌ಪುಟ್ ಮತ್ತು ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ. ಇದು ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟತೆಯಲ್ಲಿ ಅತ್ಯಂತ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುವ ಮತ್ತು ಶಿಫಾರಸು ಮಾಡಲಾದ ಸಾರಿಗೆ ವಿಧಾನವಾಗಿದ್ದು, ವಿವಿಧ ಗ್ರಾಹಕ ಅಪ್ಲಿಕೇಶನ್‌ಗಳೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಸಂಯೋಜಿಸಬಹುದಾದ ಸರಳ ಮತ್ತು ಪರಿಣಾಮಕಾರಿ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.

## ಅವಲೋಕನ

ಈ ಪಾಠವು stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಮತ್ತು ಉಪಯೋಗಿಸುವ ವಿಧಾನವನ್ನು ಒಳಗೊಂಡಿದೆ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್ ನಿರ್ಮಿಸುವುದು.
- ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ಡಿಬಗ್ ಮಾಡುವುದು.
- Visual Studio Code ಬಳಸಿ MCP ಸರ್ವರ್ ಉಪಯೋಗಿಸುವುದು.
- ಪ್ರಸ್ತುತ MCP ಸಾರಿಗೆ ವಿಧಾನಗಳನ್ನು ಮತ್ತು stdio ಯನ್ನು ಶಿಫಾರಸು ಮಾಡುವ ಕಾರಣಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.

## stdio ಸಾರಿಗೆ - ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ

stdio ಸಾರಿಗೆ ಪ್ರಸ್ತುತ MCP ನಿರ್ದಿಷ್ಟತೆಯಲ್ಲಿ (2025-06-18) ಬೆಂಬಲಿತ ಎರಡು ಸಾರಿಗೆ ಪ್ರಕಾರಗಳಲ್ಲಿ ಒಂದಾಗಿದೆ. ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ:

- **ಸರಳ ಸಂವಹನ**: ಸರ್ವರ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್‌ಪುಟ್ (`stdin`) ನಿಂದ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಓದುತ್ತದೆ ಮತ್ತು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಔಟ್‌ಪುಟ್ (`stdout`) ಗೆ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುತ್ತದೆ.
- **ಪ್ರಕ್ರಿಯೆ ಆಧಾರಿತ**: ಗ್ರಾಹಕ MCP ಸರ್ವರ್ ಅನ್ನು ಉಪಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ.
- **ಸಂದೇಶ ಸ್ವರೂಪ**: ಸಂದೇಶಗಳು ಪ್ರತ್ಯೇಕ JSON-RPC ವಿನಂತಿಗಳು, ಸೂಚನೆಗಳು ಅಥವಾ ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಹೊಸ ಸಾಲುಗಳಿಂದ ವಿಭಜಿಸಲ್ಪಟ್ಟಿವೆ.
- **ಲಾಗಿಂಗ್**: ಸರ್ವರ್ ಲಾಗಿಂಗ್ ಉದ್ದೇಶಗಳಿಗೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಎರರ್ (`stderr`) ಗೆ UTF-8 ಸ್ಟ್ರಿಂಗ್‌ಗಳನ್ನು ಬರೆಯಬಹುದು.

### ಪ್ರಮುಖ ಅಗತ್ಯಗಳು:
- ಸಂದೇಶಗಳು ಹೊಸ ಸಾಲುಗಳಿಂದ ವಿಭಜಿಸಲ್ಪಟ್ಟಿರಬೇಕು ಮತ್ತು ಒಳಗಿರುವ ಹೊಸ ಸಾಲುಗಳನ್ನು ಹೊಂದಿರಬಾರದು
- ಸರ್ವರ್ `stdout` ಗೆ ಮಾನ್ಯ MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ ಬರೆಯಬಾರದು
- ಗ್ರಾಹಕ ಸರ್ವರ್‌ನ `stdin` ಗೆ ಮಾನ್ಯ MCP ಸಂದೇಶವಲ್ಲದ ಯಾವುದನ್ನೂ ಬರೆಯಬಾರದು

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- ನಾವು MCP SDK ನಿಂದ `Server` ವರ್ಗ ಮತ್ತು `StdioServerTransport` ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುತ್ತೇವೆ
- ಮೂಲ ಸಂರಚನೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸುತ್ತೇವೆ

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP SDK ಬಳಸಿ ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸುತ್ತೇವೆ
- ಡೆಕೊರೇಟರ್‌ಗಳನ್ನು ಬಳಸಿ ಉಪಕರಣಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತೇವೆ
- ಸಾರಿಗೆಯನ್ನು ನಿರ್ವಹಿಸಲು stdio_server ಕಾನ್ಟೆಕ್ಸ್ಟ್ ಮ್ಯಾನೇಜರ್ ಅನ್ನು ಬಳಸುತ್ತೇವೆ

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

SSE ನಿಂದ ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸ stdio ಸರ್ವರ್‌ಗಳು:

- ವೆಬ್ ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್ ಅಥವಾ HTTP ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಅಗತ್ಯವಿಲ್ಲ
- ಗ್ರಾಹಕ ಉಪಪ್ರಕ್ರಿಯೆಗಳಾಗಿ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸುತ್ತದೆ
- stdin/stdout ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ಸಂವಹನ ಮಾಡುತ್ತದೆ
- ಅನುಷ್ಠಾನ ಮತ್ತು ಡಿಬಗ್ ಮಾಡಲು ಸರಳ

## ಅಭ್ಯಾಸ: stdio ಸರ್ವರ್ ರಚನೆ

ನಮ್ಮ ಸರ್ವರ್ ರಚಿಸಲು, ನಾವು ಎರಡು ವಿಷಯಗಳನ್ನು ಗಮನದಲ್ಲಿರಿಸಬೇಕು:

- ಸಂಪರ್ಕ ಮತ್ತು ಸಂದೇಶಗಳಿಗಾಗಿ ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸಲು ವೆಬ್ ಸರ್ವರ್ ಬಳಸಬೇಕಾಗುತ್ತದೆ.

## ಪ್ರಯೋಗಶಾಲೆ: ಸರಳ MCP stdio ಸರ್ವರ್ ರಚನೆ

ಈ ಪ್ರಯೋಗಶಾಲೆಯಲ್ಲಿ, ನಾವು ಶಿಫಾರಸು ಮಾಡಲಾದ stdio ಸಾರಿಗೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸರಳ MCP ಸರ್ವರ್ ರಚಿಸುವೆವು. ಈ ಸರ್ವರ್ ಗ್ರಾಹಕರು ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮಾದರಿ ಸಂಧರ್ಭ ಪ್ರೋಟೋಕಾಲ್ ಬಳಸಿ ಕರೆಮಾಡಬಹುದಾದ ಉಪಕರಣಗಳನ್ನು ಬಹಿರಂಗಪಡಿಸುತ್ತದೆ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

- Python 3.8 ಅಥವಾ ನಂತರದ ಆವೃತ್ತಿ
- MCP Python SDK: `pip install mcp`
- ಅಸಿಂಕ್ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಮೂಲಭೂತ ತಿಳಿವು

ನಮ್ಮ ಮೊದಲ MCP stdio ಸರ್ವರ್ ರಚಿಸುವುದರಿಂದ ಪ್ರಾರಂಭಿಸೋಣ:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ಲಾಗಿಂಗ್ ಅನ್ನು ಸಂರಚಿಸಿ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ಸರ್ವರ್ ಅನ್ನು ರಚಿಸಿ
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
    # stdio ಸಾರಿಗೆ ಬಳಸಿ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ನಿರಾಕರಿಸಲಾದ SSE ವಿಧಾನದಿಂದ ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳು

**Stdio ಸಾರಿಗೆ (ಪ್ರಸ್ತುತ ಮಾನದಂಡ):**
- ಸರಳ ಉಪಪ್ರಕ್ರಿಯೆ ಮಾದರಿ - ಗ್ರಾಹಕ ಸರ್ವರ್ ಅನ್ನು ಚೈಲ್ಡ್ ಪ್ರಕ್ರಿಯೆಯಾಗಿ ಪ್ರಾರಂಭಿಸುತ್ತದೆ
- JSON-RPC ಸಂದೇಶಗಳನ್ನು ಬಳಸಿ stdin/stdout ಮೂಲಕ ಸಂವಹನ
- HTTP ಸರ್ವರ್ ಸೆಟ್‌ಅಪ್ ಅಗತ್ಯವಿಲ್ಲ
- ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಭದ್ರತೆ
- ಸುಲಭ ಡಿಬಗ್ ಮತ್ತು ಅಭಿವೃದ್ಧಿ

**SSE ಸಾರಿಗೆ (MCP 2025-06-18 ರಿಂದ ನಿರಾಕರಿಸಲಾಗಿದೆ):**
- SSE ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ HTTP ಸರ್ವರ್ ಅಗತ್ಯವಿತ್ತು
- ವೆಬ್ ಸರ್ವರ್ ಮೂಲಸೌಕರ್ಯದೊಂದಿಗೆ ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ಸೆಟ್‌ಅಪ್
- HTTP ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳಿಗೆ ಹೆಚ್ಚುವರಿ ಭದ್ರತಾ ಪರಿಗಣನೆಗಳು
- ಈಗ ವೆಬ್ ಆಧಾರಿತ ಸಂದರ್ಭಗಳಿಗೆ Streamable HTTP ಮೂಲಕ ಬದಲಾಯಿಸಲಾಗಿದೆ

### stdio ಸಾರಿಗೆಯೊಂದಿಗೆ ಸರ್ವರ್ ರಚನೆ

ನಮ್ಮ stdio ಸರ್ವರ್ ರಚಿಸಲು, ನಾವು:

1. **ಅಗತ್ಯ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಿ** - MCP ಸರ್ವರ್ ಘಟಕಗಳು ಮತ್ತು stdio ಸಾರಿಗೆಯನ್ನು ಬೇಕಾಗುತ್ತದೆ
2. **ಸರ್ವರ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಿ** - ಅದರ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
3. **ಉಪಕರಣಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ** - ಬಹಿರಂಗಪಡಿಸಲು ಬೇಕಾದ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸೇರಿಸಿ
4. **ಸಾರಿಗೆಯನ್ನು ಸೆಟ್‌ಅಪ್ ಮಾಡಿ** - stdio ಸಂವಹನವನ್ನು ಸಂರಚಿಸಿ
5. **ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ** - ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಸಂದೇಶಗಳನ್ನು ನಿರ್ವಹಿಸಿ

ನಾವು ಇದನ್ನು ಹಂತ ಹಂತವಾಗಿ ನಿರ್ಮಿಸೋಣ:

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

### ಹಂತ 2: ಹೆಚ್ಚಿನ ಉಪಕರಣಗಳನ್ನು ಸೇರಿಸಿ

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

ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗಿ stdin ನಿಂದ ಇನ್‌ಪುಟ್‌ಗಾಗಿ ಕಾಯುತ್ತದೆ. ಇದು stdio ಸಾರಿಗೆಯ ಮೂಲಕ JSON-RPC ಸಂದೇಶಗಳನ್ನು ಬಳಸಿ ಸಂವಹನ ಮಾಡುತ್ತದೆ.

### ಹಂತ 4: ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ಪರೀಕ್ಷೆ

ನೀವು ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ಪರೀಕ್ಷಿಸಬಹುದು:

1. ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ: `npx @modelcontextprotocol/inspector`
2. ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್‌ಗೆ ಸೂಚಿಸಿ
3. ನೀವು ರಚಿಸಿದ ಉಪಕರಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## ನಿಮ್ಮ stdio ಸರ್ವರ್ ಡಿಬಗ್ ಮಾಡುವುದು

### MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ

MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ MCP ಸರ್ವರ್‌ಗಳನ್ನು ಡಿಬಗ್ ಮತ್ತು ಪರೀಕ್ಷಿಸಲು ಅಮೂಲ್ಯ ಸಾಧನವಾಗಿದೆ. ನಿಮ್ಮ stdio ಸರ್ವರ್ ಜೊತೆಗೆ ಇದನ್ನು ಹೇಗೆ ಬಳಸುವುದು:

1. **ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ**: ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ಒದಗಿಸುತ್ತದೆ, ಇಲ್ಲಿ ನೀವು:
   - ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ವೀಕ್ಷಿಸಬಹುದು
   - ವಿಭಿನ್ನ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳೊಂದಿಗೆ ಉಪಕರಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಬಹುದು
   - JSON-RPC ಸಂದೇಶಗಳನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಬಹುದು
   - ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳನ್ನು ಡಿಬಗ್ ಮಾಡಬಹುದು

### VS Code ಬಳಸಿ

ನೀವು ನಿಮ್ಮ MCP ಸರ್ವರ್ ಅನ್ನು ನೇರವಾಗಿ VS Code ನಲ್ಲಿ ಡಿಬಗ್ ಮಾಡಬಹುದು:

1. `.vscode/launch.json` ನಲ್ಲಿ ಲಾಂಚ್ ಸಂರಚನೆಯನ್ನು ರಚಿಸಿ:
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

2. ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್‌ನಲ್ಲಿ ಬ್ರೇಕ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸೆಟ್ ಮಾಡಿ
3. ಡಿಬಗರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ಪರೀಕ್ಷಿಸಿ

### ಸಾಮಾನ್ಯ ಡಿಬಗ್ ಸಲಹೆಗಳು

- ಲಾಗಿಂಗ್‌ಗಾಗಿ `stderr` ಬಳಸಿ - `stdout` ಗೆ ಎಂದಿಗೂ ಬರೆಯಬೇಡಿ, ಅದು MCP ಸಂದೇಶಗಳಿಗೆ ಮೀಸಲಿರುತ್ತದೆ
- ಎಲ್ಲಾ JSON-RPC ಸಂದೇಶಗಳು ಹೊಸ ಸಾಲುಗಳಿಂದ ವಿಭಜಿಸಲ್ಪಟ್ಟಿರಬೇಕು
- ಸಂಕೀರ್ಣ ಕಾರ್ಯಕ್ಷಮತೆ ಸೇರಿಸುವ ಮೊದಲು ಸರಳ ಉಪಕರಣಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ
- ಸಂದೇಶ ಸ್ವರೂಪಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ

## VS Code ನಲ್ಲಿ ನಿಮ್ಮ stdio ಸರ್ವರ್ ಉಪಯೋಗಿಸುವುದು

ನೀವು MCP stdio ಸರ್ವರ್ ರಚಿಸಿದ ನಂತರ, ಅದನ್ನು VS Code ಜೊತೆಗೆ ಸಂಯೋಜಿಸಿ Claude ಅಥವಾ ಇತರ MCP-ಸಮ್ಮತ ಗ್ರಾಹಕರೊಂದಿಗೆ ಬಳಸಬಹುದು.

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

2. **Claude ಅನ್ನು ಮರುಪ್ರಾರಂಭಿಸಿ**: ಹೊಸ ಸರ್ವರ್ ಸಂರಚನೆಯನ್ನು ಲೋಡ್ ಮಾಡಲು Claude ಅನ್ನು ಮುಚ್ಚಿ ಮತ್ತೆ ತೆರೆಯಿರಿ.

3. **ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ**: Claude ಜೊತೆ ಸಂಭಾಷಣೆ ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ನಿಮ್ಮ ಸರ್ವರ್ ಉಪಕರಣಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ:
   - "ನೀವು ಸ್ವಾಗತ ಉಪಕರಣ ಬಳಸಿ ನನ್ನನ್ನು ಸ್ವಾಗತಿಸಬಹುದುವೇ?"
   - "15 ಮತ್ತು 27 ರ ಮೊತ್ತವನ್ನು ಲೆಕ್ಕಿಸಿ"
   - "ಸರ್ವರ್ ಮಾಹಿತಿ ಏನು?"

### TypeScript stdio ಸರ್ವರ್ ಉದಾಹರಣೆ

ಇದೀಗ ಪೂರ್ಣ TypeScript ಉದಾಹರಣೆ:

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

// ಸಾಧನಗಳನ್ನು ಸೇರಿಸಿ
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

## ಸಾರಾಂಶ

ಈ ನವೀಕರಿಸಿದ ಪಾಠದಲ್ಲಿ, ನೀವು ಕಲಿತದ್ದು:

- ಪ್ರಸ್ತುತ **stdio ಸಾರಿಗೆ** (ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನ) ಬಳಸಿ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು
- SSE ಸಾರಿಗೆ stdio ಮತ್ತು Streamable HTTP ಗೆ ಏಕೆ ನಿರಾಕರಿಸಲ್ಪಟ್ಟಿತು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು
- MCP ಗ್ರಾಹಕರು ಕರೆಮಾಡಬಹುದಾದ ಉಪಕರಣಗಳನ್ನು ರಚಿಸುವುದು
- MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ಡಿಬಗ್ ಮಾಡುವುದು
- VS Code ಮತ್ತು Claude ಜೊತೆಗೆ ನಿಮ್ಮ stdio ಸರ್ವರ್ ಅನ್ನು ಸಂಯೋಜಿಸುವುದು

stdio ಸಾರಿಗೆ ನಿರಾಕರಿಸಲಾದ SSE ವಿಧಾನಕ್ಕಿಂತ ಸರಳ, ಹೆಚ್ಚು ಭದ್ರತೆ ಮತ್ತು ಉತ್ತಮ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ. 2025-06-18 ನಿರ್ದಿಷ್ಟತೆಯ ಪ್ರಕಾರ, ಇದು ಬಹುತೇಕ MCP ಸರ್ವರ್ ಅನುಷ್ಠಾನಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ಸಾರಿಗೆ ವಿಧಾನವಾಗಿದೆ.

### .NET

1. ಮೊದಲು ಕೆಲವು ಉಪಕರಣಗಳನ್ನು ರಚಿಸೋಣ, ಇದಕ್ಕಾಗಿ ನಾವು *Tools.cs* ಎಂಬ ಫೈಲ್ ಅನ್ನು ಕೆಳಗಿನ ವಿಷಯದೊಂದಿಗೆ ರಚಿಸುವೆವು:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## ಅಭ್ಯಾಸ: ನಿಮ್ಮ stdio ಸರ್ವರ್ ಪರೀಕ್ಷೆ

ನೀವು stdio ಸರ್ವರ್ ರಚಿಸಿದ ನಂತರ, ಅದು ಸರಿಯಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸೋಣ.

### ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

1. MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಸ್ಥಾಪಿತವಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್ ಉಳಿಸಲಾಗಿದೆ (ಉದಾ: `server.py`)

### ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ಪರೀಕ್ಷೆ

1. **ನಿಮ್ಮ ಸರ್ವರ್ ಜೊತೆಗೆ ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಪ್ರಾರಂಭಿಸಿ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ತೆರೆಯಿರಿ**: ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ನಿಮ್ಮ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತೋರಿಸುವ ಬ್ರೌಸರ್ ವಿಂಡೋವನ್ನು ತೆರೆಯುತ್ತದೆ.

3. **ಉಪಕರಣಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ**: 
   - ವಿಭಿನ್ನ ಹೆಸರುಗಳೊಂದಿಗೆ `get_greeting` ಉಪಕರಣವನ್ನು ಪ್ರಯತ್ನಿಸಿ
   - ವಿವಿಧ ಸಂಖ್ಯೆಗಳೊಂದಿಗೆ `calculate_sum` ಉಪಕರಣವನ್ನು ಪರೀಕ್ಷಿಸಿ
   - ಸರ್ವರ್ ಮೆಟಾಡೇಟಾ ನೋಡಲು `get_server_info` ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ

4. **ಸಂವಹನವನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ**: ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಗ್ರಾಹಕ ಮತ್ತು ಸರ್ವರ್ ನಡುವೆ ವಿನಿಮಯವಾಗುತ್ತಿರುವ JSON-RPC ಸಂದೇಶಗಳನ್ನು ತೋರಿಸುತ್ತದೆ.

### ನೀವು ಏನು ನೋಡಬೇಕು

ನಿಮ್ಮ ಸರ್ವರ್ ಸರಿಯಾಗಿ ಪ್ರಾರಂಭವಾದಾಗ, ನೀವು ನೋಡಬೇಕು:
- ಇನ್ಸ್‌ಪೆಕ್ಟರ್‌ನಲ್ಲಿ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳು ಪಟ್ಟಿ ಮಾಡಲ್ಪಟ್ಟಿವೆ
- ಪರೀಕ್ಷೆಗಾಗಿ ಉಪಕರಣಗಳು ಲಭ್ಯವಿವೆ
- ಯಶಸ್ವಿ JSON-RPC ಸಂದೇಶ ವಿನಿಮಯಗಳು
- ಇಂಟರ್ಫೇಸ್‌ನಲ್ಲಿ ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಗಳು ಪ್ರದರ್ಶಿತವಾಗಿವೆ

### ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು ಮತ್ತು ಪರಿಹಾರಗಳು

**ಸರ್ವರ್ ಪ್ರಾರಂಭವಾಗುತ್ತಿಲ್ಲ:**
- ಎಲ್ಲಾ ಅವಲಂಬನೆಗಳು ಸ್ಥಾಪಿತವಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ: `pip install mcp`
- Python ಸಿಂಟ್ಯಾಕ್ಸ್ ಮತ್ತು ಇನ್‌ಡೆಂಟೇಶನ್ ಪರಿಶೀಲಿಸಿ
- ಕಾನ್ಸೋಲ್‌ನಲ್ಲಿ ದೋಷ ಸಂದೇಶಗಳನ್ನು ಹುಡುಕಿ

**ಉಪಕರಣಗಳು ಕಾಣಿಸುವುದಿಲ್ಲ:**
- `@server.tool()` ಡೆಕೊರೇಟರ್‌ಗಳು ಇದ್ದಾರೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
- `main()` ಮೊದಲು ಉಪಕರಣ ಕಾರ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
- ಸರ್ವರ್ ಸರಿಯಾಗಿ ಸಂರಚಿಸಲಾಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ

**ಸಂಪರ್ಕ ಸಮಸ್ಯೆಗಳು:**
- ಸರ್ವರ್ stdio ಸಾರಿಗೆಯನ್ನು ಸರಿಯಾಗಿ ಬಳಸುತ್ತಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
- ಇತರ ಪ್ರಕ್ರಿಯೆಗಳು ಹಸ್ತಕ್ಷೇಪ ಮಾಡುತ್ತಿಲ್ಲ ಎಂದು ಪರಿಶೀಲಿಸಿ
- ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಕಮಾಂಡ್ ಸಿಂಟ್ಯಾಕ್ಸ್ ಪರಿಶೀಲಿಸಿ

## ನಿಯೋಜನೆ

ನಿಮ್ಮ ಸರ್ವರ್ ಅನ್ನು ಹೆಚ್ಚಿನ ಸಾಮರ್ಥ್ಯಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸಲು ಪ್ರಯತ್ನಿಸಿ. ಉದಾಹರಣೆಗೆ, [ಈ ಪುಟ](https://api.chucknorris.io/) ನೋಡಿ, API ಅನ್ನು ಕರೆಮಾಡುವ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ. ಸರ್ವರ್ ಹೇಗಿರಬೇಕು ಎಂದು ನೀವು ನಿರ್ಧರಿಸಿ. ಸವಾಲು ಮಾಡಿ :)

## ಪರಿಹಾರ

[ಪರಿಹಾರ](./solution/README.md) ಇಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕೋಡ್‌ನೊಂದಿಗೆ ಸಾಧ್ಯವಾದ ಪರಿಹಾರವಿದೆ.

## ಪ್ರಮುಖ ಅಂಶಗಳು

ಈ ಅಧ್ಯಾಯದಿಂದ ಪ್ರಮುಖ ಅಂಶಗಳು:

- stdio ಸಾರಿಗೆ ಸ್ಥಳೀಯ MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವಾಗಿದೆ.
- stdio ಸಾರಿಗೆ MCP ಸರ್ವರ್‌ಗಳು ಮತ್ತು ಗ್ರಾಹಕರ ನಡುವೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಇನ್‌ಪುಟ್ ಮತ್ತು ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ಗಳ ಮೂಲಕ ನಿರಂತರ ಸಂವಹನವನ್ನು ಅನುಮತಿಸುತ್ತದೆ.
- ನೀವು ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಮತ್ತು Visual Studio Code ಎರಡನ್ನೂ ನೇರವಾಗಿ stdio ಸರ್ವರ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಲು ಬಳಸಬಹುದು, ಇದರಿಂದ ಡಿಬಗ್ ಮತ್ತು ಸಂಯೋಜನೆ ಸುಲಭವಾಗುತ್ತದೆ.

## ಮಾದರಿಗಳು

- [Java ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.Net ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [JavaScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [TypeScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [Python ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ಮುಂದಿನದು ಏನು

## ಮುಂದಿನ ಹಂತಗಳು

stdio ಸಾರಿಗೆಯೊಂದಿಗೆ MCP ಸರ್ವರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ನೀವು ಕಲಿತಿದ್ದೀರಿ, ಈಗ ನೀವು ಹೆಚ್ಚಿನ ಉನ್ನತ ವಿಷಯಗಳನ್ನು ಅನ್ವೇಷಿಸಬಹುದು:

- **ಮುಂದೆ**: [MCP ಜೊತೆಗೆ HTTP ಸ್ಟ್ರೀಮಿಂಗ್ (Streamable HTTP)](../06-http-streaming/README.md) - ದೂರದ ಸರ್ವರ್‌ಗಳಿಗೆ ಬೆಂಬಲಿತ ಇನ್ನೊಂದು ಸಾರಿಗೆ ವಿಧಾನವನ್ನು ತಿಳಿದುಕೊಳ್ಳಿ
- **ಅತ್ಯಾಧುನಿಕ**: [MCP ಭದ್ರತಾ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](../../02-Security/README.md) - ನಿಮ್ಮ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->