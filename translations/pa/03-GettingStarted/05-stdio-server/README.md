# MCP ਸਰਵਰ stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ

> **⚠️ ਮਹੱਤਵਪੂਰਨ ਅਪਡੇਟ**: MCP ਵਿਸ਼ੇਸ਼ਤਾ 2025-06-18 ਦੇ ਅਨੁਸਾਰ, ਇੱਕੱਲਾ SSE (Server-Sent Events) ਟਰਾਂਸਪੋਰਟ ਨੂੰ **ਡਿਪ੍ਰੀਕੇਟ** ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਸਦੀ ਥਾਂ "Streamable HTTP" ਟਰਾਂਸਪੋਰਟ ਲਿਆ ਗਿਆ ਹੈ। ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ ਦੋ ਮੁੱਖ ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ_DEFINE_ ਕਰਦੀ ਹੈ:
> 1. **stdio** - ਸਟੈਂਡਰਡ ਇਨਪੁਟ/ਆਉਟਪੁਟ (ਸਥਾਨਕ ਸਰਵਰਾਂ ਲਈ ਸੁਝਾਇਆ ਗਿਆ)
> 2. **Streamable HTTP** - ਉਹਨਾਂ ਦੂਰੇ ਸਰਵਰਾਂ ਲਈ ਜੋ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ SSE ਵਰਤ ਸਕਦੇ ਹਨ
>
> ਇਸ ਪਾਠ ਵਿੱਚ **stdio ਟਰਾਂਸਪੋਰਟ** 'ਤੇ ਧਿਆਨ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਜੋ ਕਿ ਜ਼ਿਆਦਾਤਰ MCP ਸਰਵਰ ਅਮਲਾਂ ਲਈ ਸੁਝਾਇਆ ਗਿਆ ਤਰੀਕਾ ਹੈ।

stdio ਟਰਾਂਸਪੋਰਟ MCP ਸਰਵਰਾਂ ਨੂੰ ਕਲਾਇੰਟਾਂ ਨਾਲ ਸਧਾਰਨ ਇਨਪੁਟ ਅਤੇ ਆਉਟਪੁਟ ਸਟਰੀਮਾਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ ਵਿੱਚ ਸਭ ਤੋਂ ਆਮ ਅਤੇ ਸਿਫਾਰਸ਼ੀ ਟਰਾਂਸਪੋਰਟ ਢਾਂਚਾ ਹੈ, ਜੋ MCP ਸਰਵਰਾਂ ਨੂੰ ਬਿਲਡ ਕਰਨ ਲਈ ਇੱਕ ਸਧਾਰਨ ਅਤੇ ਕੁਸ਼ਲ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਅਨੈਕ ਪ੍ਰਕਾਰ ਦੇ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਇਕੱਠੇ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

## ਓਬਰਵਿਊ

ਇਸ ਪਾਠ ਵਿੱਚ stdio ਟਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਕਿਵੇਂ ਬਣਾਇਆ ਅਤੇ ਵਰਤਿਆ ਜਾਵੇ ਇਸ ਦੀ ਸਮਝ ਦਿੱਤੀ ਗਈ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- stdio ਟਰਾਂਸਪੋਰਟ ਦਾ ਉਪਯੋਗ ਕਰਦਿਆਂ MCP ਸਰਵਰ ਬਣਾਉਣਾ।
- Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨਾ।
- Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨੂੰ ਵਰਤਣਾ।
- ਮੌਜੂਦਾ MCP ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਨੂੰ ਸਮਝਣਾ ਅਤੇ ਕਿਉਂ stdio ਨੂੰ ਸਿਫਾਰਸ਼ੀ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।

## stdio ਟਰਾਂਸਪੋਰਟ - ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

stdio ਟਰਾਂਸਪੋਰਟ ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ (2025-06-18) ਵਿੱਚ ਦੋ ਸਮਰਥਿਤ ਟਰਾਂਸਪੋਰਟ ਕਿਸਮਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ:

- **ਸਧਾਰਨ ਸੰਚਾਰ**: ਸਰਵਰ ਸਟੈਂਡਰਡ ਇਨਪੁਟ (`stdin`) ਤੋਂ JSON-RPC ਸੁਨੇਹੇ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਸਟੈਂਡਰਡ ਆਉਟਪੁਟ (`stdout`) 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਦਾ ਹੈ।
- **ਪ੍ਰੋਸੈਸ-ਆਧਾਰਿਤ**: ਕਲਾਇੰਟ MCP ਸਰਵਰ ਨੂੰ ਇੱਕ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਚਲਾਉਂਦਾ ਹੈ।
- **ਸੁਨੇਹਾ ਫਾਰਮੈਟ**: ਸੁਨੇਹੇ ਵੱਖਰੇ JSON-RPC ਬੇਨਤੀਆਂ, ਸੂਚਨਾਵਾਂ ਜਾਂ ਜਵਾਬਾਂ ਹੁਂਦੇ ਹਨ ਜੋ ਨਿਊਲਾਈਨਾਂ ਨਾਲ ਵੱਖਰੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- **ਲੌਗਿੰਗ**: ਸਰਵਰ `stderr` (`ਸਟੈਂਡਰਡ ਐਰਰ`) 'ਤੇ UTF-8 ਸਟ੍ਰਿੰਗ ਲਿਖ ਸਕਦਾ ਹੈ ਲੌਗਿੰਗ ਲਈ।

### ਮੁੱਖ ਲੋੜਾਂ:
- ਸੁਨੇਹੇ ਨਿਊਲਾਈਨਾਂ ਨਾਲ ਵੱਖਰੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ ਅਤੇ ਅੰਦਰ ਨਿਊਲਾਈਨ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ
- ਸਰਵਰ ਨੂੰ `stdout` 'ਤੇ ਕੋਈ ਵੀ ਅਜਿਹਾ ਕੁਝ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ ਇਕ ਵੈਧ MCP ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ
- ਕਲਾਇੰਟ ਸਰਵਰ ਦੇ `stdin` 'ਤੇ ਕੋਈ ਵੀ ਅਜਿਹਾ ਕੁਝ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ MCP ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ:

- ਅਸੀਂ MCP SDK ਤੋਂ `Server` ਕਲਾਸ ਅਤੇ `StdioServerTransport` ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੇ ਹਾਂ
- ਇੱਕ ਸਰਲ ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਬੇਸਿਕ ਸੰਰਚਨਾ ਅਤੇ ਯੋਗਤਾਵਾਂ ਹਨ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਓ
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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦੇ ਹਾਂ
- ਡੇਕੋਰੇਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੂਲ.define_ ਕਰਦੇ ਹਾਂ
- stdio_server ਸੰਦਰਭ ਪ੍ਰਬੰਧਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟਰਾਂਸਪੋਰਟ ਸੰਭਾਲਦੇ ਹਾਂ

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

SSE ਤੋਂ ਮੁੱਖ ਫਰਕ ਇਹ ਹੈ ਕਿ stdio ਸਰਵਰ:

- ਕਿਸੇ ਵੀ ਵੈੱਬ ਸਰਵਰ ਸੈੱਟਅਪ ਜਾਂ HTTP ਐਂਡਪੋਇੰਟ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ
- ਕਲਾਇੰਟ ਵੱਲੋਂ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਸ਼ੁਰੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ
- stdin/stdout ਸਟਰੀਮਾਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਦੇ ਹਨ
- ਲਾਗੂ ਕਰਨ ਅਤੇ ਡੀਬੱਗ ਕਰਨ ਵਿੱਚ ਆਸਾਨ

## ਕਸਰਤ: stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਸਾਨੂੰ ਦੋ ਗੱਲਾਂ ਦਾ ਧਿਆਨ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ:

- ਸਾਨੂੰ ਕੁਨੈਕਸ਼ਨ ਅਤੇ ਸੁਨੇਹਿਆਂ ਲਈ ਐਂਡਪੋਇੰਟ ਉਜਾਗਰ ਕਰਨ ਲਈ ਵੈੱਬ ਸਰਵਰ ਦੀ ਲੋੜ ਹੈ।

## ਪ੍ਰਯੋਗਸ਼ਾਲਾ: ਇੱਕ ਸਧਾਰਨ MCP stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਪ੍ਰਯੋਗਸ਼ਾਲਾ ਵਿੱਚ ਅਸੀਂ ਸੁਝਾਏ ਗਏ stdio ਟਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੱਕ ਸਧਾਰਨ MCP ਸਰਵਰ ਬਣਾਵਾਂਗੇ। ਇਹ ਸਰਵਰ ਟੂਲ ਉਪਲੱਬਧ ਕਰਾਵੇਗਾ ਜਿਸ ਨੂੰ ਕਲਾਇੰਟ ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕਾਲ ਨੂੰ ਵਰਤ ਕੇ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ।

### ਯੋਗਤਾ

- Python 3.8 ਜਾਂ ਉਸ ਤੋਂ ਬਾਅਦ ਦਾ ਵਰਜਨ
- MCP Python SDK: `pip install mcp`
- ਐਸਿੰਕ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ

ਆਓ ਆਪਣਾ ਪਹਿਲਾ MCP stdio ਸਰਵਰ ਬਣਾਈਏ:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ਲੌਗਿੰਗ ਕਨਫ਼ਿਗਰ ਕਰੋ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ਸਰਵਰ ਬਣਾਓ
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
    # stdio ਟਰਾਂਸਪੋਰਟ ਵਰਤੋਂ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ਡਿਪ੍ਰੀਕੇਟ ਕੀਤੇ SSE ਤਰੀਕੇ ਨਾਲ ਮੁੱਖ ਫਰਕ

**Stdio Transport (ਮੌਜੂਦਾ ਮਿਆਰ):**
- ਸਧਾਰਨ ਸਬਪ੍ਰੋਸੈਸ ਮਾਡਲ - ਕਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਬੱਚਾ ਪ੍ਰੋਸੈਸ ਵਜੋਂ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ
- stdin/stdout ਦੁਆਰਾ JSON-RPC ਸੁਨੇਹਿਆਂ ਨਾਲ ਸੰਚਾਰ
- ਕੋਈ HTTP ਸਰਵਰ ਸੈੱਟਅਪ ਲੋੜੀਂਦਾ ਨਹੀਂ
- ਬਿਹਤਰ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ
- ਡੀਬੱਗ ਅਤੇ ਵਿਕਾਸ ਵਿੱਚ ਬਹੁਤ ਸੌਖਾ

**SSE Transport (MCP 2025-06-18 ਤੋਂ ਡਿਪ੍ਰੀਕੇਟ):**
- SSE ਐਂਡਪੋਇੰਟਾਂ ਨਾਲ HTTP ਸਰਵਰ ਲੋੜੀਂਦਾ
- ਵੈੱਬ ਸਰਵਰ ਇਨਫ੍ਰਾਸਟਰੱਕਚਰ ਨਾਲ ਹੋਰ ਜਟਿਲ ਸੈੱਟਅਪ
- HTTP ਐਂਡਪੋਇੰਟਾਂ ਲਈ ਵਾਧੂ ਸੁਰੱਖਿਆ ਚਿੰਤਾਵਾਂ
- ਹੁਣ ਵੈੱਬ ਆਧਾਰਤ ਸਨਾਰੀਓਜ਼ ਲਈ Streamable HTTP ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਗਿਆ

### stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ ਸਰਵਰ ਬਣਾਉਣੀ

ਸਾਡੇ stdio ਸਰਵਰ ਨੂੰ ਬਣਾਉਣ ਲਈ ਸਾਨੂੰ:

1. **ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕਰਨੀ** - MCP ਸਰਵਰ ਕਮਪੋਨੈਂਟ ਅਤੇ stdio ਟਰਾਂਸਪੋਰਟ
2. **ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ** - ਸਰਵਰ ਦੀ ਸੰਰਚਨਾ ਅਤੇ ਯੋਗਤਾਵਾਂ define ਕਰੋ
3. **ਟੂਲ define ਕਰੋ** - ਉਹ ਫੰਕਸ਼ਨਾਲਿਟੀ ਜੋ ਅਸੀਂ ਉਪਲੱਬਧ ਕਰਵਾਉਣੀ ਹੈ ਜੋੜੋ
4. **ਟਰਾਂਸਪੋਰਟ ਸੈੱਟਅਪ ਕਰਨਾ** - stdio ਸੰਚਾਰ ਦੀ ਸੰਰਚਨਾ ਕਰੋ
5. **ਸਰਵਰ ਚਲਾਉਣਾ** - ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਸੰਭਾਲੋ

ਚਲੋ ਇਸਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਬਣਾਈਏ:

### ਕਦਮ 1: ਇੱਕ ਮੂਲ stdio ਸਰਵਰ ਬਣਾਓ

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ਲਾਗਿੰਗ ਸੰਰਚਿਤ ਕਰੋ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ਸਰਵਰ ਬਣਾਓ
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

### ਕਦਮ 2: ਹੋਰ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰੋ

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

### ਕਦਮ 3: ਸਰਵਰ ਚਲਾਉਣਾ

ਕੋਡ ਨੂੰ `server.py` ਦੇ ਰੂਪ ਵਿੱਚ ਸੇਵ ਕਰੋ ਅਤੇ ਕਮਾਂਡ ਲਾਈਨ ਤੋਂ ਚਲਾਓ:

```bash
python server.py
```

ਸਰਵਰ ਸ਼ੁਰੂ ਹੋ ਜਾਵੇਗਾ ਅਤੇ stdin ਤੋਂ ਇਨਪੁਟ ਦੀ ਉਡੀਕ ਕਰੇਗਾ। ਇਹ stdio ਟਰਾਂਸਪੋਰਟ 'ਤੇ JSON-RPC ਸੁਨੇਹਿਆਂ ਨਾਲ ਸੰਚਾਰ ਕਰਦਾ ਹੈ।

### ਕਦਮ 4: Inspector ਨਾਲ ਟੈਸਟ ਕਰਨਾ

ਤੁਸੀਂ MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਸਰਵਰ ਦੀ ਪੜਤਾਲ ਕਰ ਸਕਦੇ ਹੋ:

1. Inspector ਇੰਸਟਾਲ ਕਰੋ: `npx @modelcontextprotocol/inspector`
2. Inspector ਚਲਾਓ ਅਤੇ ਇਸ ਨੂੰ ਆਪਣੇ ਸਰਵਰ ਨਾਲ ਜੋੜੋ
3. ਬਣਾਏ ਗਏ ਟੂਲਾਂ ਦਾ ਟੈਸਟ ਕਰੋ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨਾ

### MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਨਾ

MCP Inspector MCP ਸਰਵਰਾਂ ਦੀ ਡੀਬੱਗ ਕਰਨ ਅਤੇ ਟੈਸਟ ਕਰਨ ਲਈ ਮਹੱਤਵਪੂਰਨ ਟੂਲ ਹੈ। ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ stdio ਸਰਵਰ ਨਾਲ ਇਸ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੋ:

1. **Inspector ਇੰਸਟਾਲ ਕਰੋ**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ਚਲਾਓ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ਆਪਣੇ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ**: Inspector ਇੱਕ ਵੈੱਬ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿਸ 'ਚ ਤੁਸੀਂ:
   - ਸਰਵਰ ਦੀ ਯੋਗਤਾਵਾਂ ਵੇਖ ਸਕਦੇ ਹੋ
   - ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਟੂਲ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ
   - JSON-RPC ਸੁਨੇਹਿਆਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰ ਸਕਦੇ ਹੋ
   - ਕੁਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਡੀਬੱਗ ਕਰ ਸਕਦੇ ਹੋ

### VS Code ਦੀ ਵਰਤੋਂ ਕਰਨਾ

ਤੁਸੀਂ Visual Studio Code ਵਿੱਚ ਸਿੱਧਾ ਆਪਣੇ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰ ਸਕਦੇ ਹੋ:

1. `.vscode/launch.json` ਵਿੱਚ ਲਾਂਚ ਕਨਫਿਗਰੇਸ਼ਨ ਬਣਾਓ:
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

2. ਆਪਣੇ ਸਰਵਰ ਕੋਡ ਵਿੱਚ ਬ੍ਰੇਕਪਾਇੰਟ ਤੈਅ ਕਰੋ
3. ਡੀਬੱਗਰ ਚਲਾਓ ਅਤੇ Inspector ਨਾਲ ਟੈਸਟ ਕਰੋ

### ਆਮ ਡੀਬੱਗਿੰਗ ਟਿਪਸ

- ਲੌਗਿੰਗ ਲਈ `stderr` ਦੀ ਵਰਤੋਂ ਕਰੋ - ਕਦੇ ਵੀ `stdout` ਵਿੱਚ ਲਿਖੋ ਨਾ ਕਿਉਂਕਿ ਇਹ MCP ਸੁਨੇਹਿਆਂ ਲਈ ਰਾਖੀ ਜਾਂਦੀ ਹੈ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੇ JSON-RPC ਸੁਨੇਹੇ ਨਿਊਲਾਈਨ-ਵੱਖਰੇ ਹਨ
- ਸਧਾਰਨ ਟੂਲਾਂ ਨਾਲ ਪਹਿਲਾਂ ਟੈਸਟ ਕਰੋ, ਫਿਰ ਮੁਸ਼ਕਲ ਫੰਕਸ਼ਨਾਲਿਟੀ ਸ਼ਾਮਿਲ ਕਰੋ
- ਸੁਨੇਹਾ ਫਾਰਮੈਟ ਦੀ ਜਾਂਚ ਲਈ Inspector ਦੀ ਵਰਤੋਂ ਕਰੋ

## VS Code ਵਿੱਚ ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ ਵਰਤਣਾ

ਜਦੋਂ ਤੁਸੀਂ ਆਪਣਾ MCP stdio ਸਰਵਰ ਬਣਾ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਸਨੂੰ VS Code ਨਾਲ ਇੰਟੀਗਰੇਟ ਕਰ ਸਕਦੇ ਹੋ ਤਾਕਿ Claude ਜਾਂ ਹੋਰ MCP-ਕੰਪੈਟਿਬਲ ਕਲਾਇੰਟਾਂ ਨਾਲ ਵਰਤਿਆ ਜਾ ਸਕੇ।

### ਸੰਰਚਨਾ

1. ਇਕ MCP ਸੰਰਚਨਾ ਫਾਈਲ ਬਣਾਓ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ਜਾਂ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) ਤੇ:

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

2. Claude ਨੂੰ ਰੀਸਟਾਰਟ ਕਰੋ: Claude ਨੂੰ ਬੰਦ ਕਰੋ ਅਤੇ ਫਿਰ ਖੋਲ੍ਹੋ ਤਾਂ ਜੋ ਨਵੀਂ ਸਰਵਰ ਸੰਰਚਨਾ ਲੋਡ ਹੋ ਜਾਵੇ।

3. ਕੁਨੈਕਸ਼ਨ ਟੈਸਟ ਕਰੋ: Claude ਨਾਲ ਗੱਲਬਾਤ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਰਵਰ ਦੇ ਟੂਲ ਦਾ ਉਪਯੋਗ ਕਰਕੇ ਦੇਖੋ:
   - "ਕੀ ਤੁਸੀਂ greeting ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮੇਰੀ ਸਲਾਮਤੀ ਕਰ ਸਕਦੇ ਹੋ?"
   - "15 ਅਤੇ 27 ਦਾ ਜੋੜ ਕਿਤਨਾ ਹੈ?"
   - "ਸਰਵਰ ਦੀ ਜਾਣਕਾਰੀ ਕੀ ਹੈ?"

### TypeScript stdio ਸਰਵਰ ਉਦਾਹਰਨ

ਇੱਕ ਪੂਰੀ TypeScript ਉਦਾਹਰਨ ਹਵਾਲੇ ਲਈ:

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

// ਸੰਦ ਜੋੜੋ
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

### .NET stdio ਸਰਵਰ ਉਦਾਹਰਨ

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

## ਸੰਖੇਪ

ਇਸ ਅੱਪਡੇਟ ਕੀਤੇ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖਿਆ ਕਿ:

- ਮੌਜੂਦਾ **stdio ਟਰਾਂਸਪੋਰਟ** ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਕਿਵੇਂ ਬਣਾਏ ਜਾਂਦੇ ਹਨ (ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ)
- ਕਿਉਂ SSE ਟਰਾਂਸਪੋਰਟ ਨੂੰ stdio ਅਤੇ Streamable HTTP ਦੇ ਹਕ ਵਿੱਚ ਖਤਮ ਕਰ ਦਿੱਤਾ ਗਿਆ
- ਉਹ ਟੂਲ ਬਣਾਓ ਜੋ MCP ਕਲਾਇੰਟਾਂ ਦੁਆਰਾ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ
- MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਸਰਵਰ ਨੂੰ ਕਿਵੇਂ ਡੀਬੱਗ ਕਰਨਾ ਹੈ
- VS Code ਅਤੇ Claude ਨਾਲ ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ ਕਿਵੇਂ ਇੰਟੀਗਰੇਟ ਕਰਨਾ ਹੈ

stdio ਟਰਾਂਸਪੋਰਟ ਡਿਪ੍ਰੀਕੇਟ ਕੀਤੇ SSE ਤਰੀਕੇ ਨਾਲ ਤੁਲਨਾਤਮਕ ਤੌਰ 'ਤੇ MCP ਸਰਵਰ ਬਨਾਉਣ ਦਾ ਇੱਕ ਸੂਖਮ, ਜ਼ਿਆਦਾ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨਕਾਰੀ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। 2025-06-18 ਵਿਸ਼ੇਸ਼ਤਾ ਅਨੁਸਾਰ ਇਹ ਜ਼ਿਆਦਾਤਰ MCP ਸਰਵਰ ਲਈ ਸਿਫਾਰਸ਼ੀ ਟਰਾਂਸਪੋਰਟ ਹੈ।

### .NET

1. ਆਓ ਪਹਿਲਾਂ ਕੁਝ ਟੂਲ ਸਿਰਜੀਏ, ਇਸ ਲਈ ਅਸੀਂ ਇਕ ਫਾਈਲ *Tools.cs* ਬਨਾਵਾਂਗੇ ਜਿਸ ਵਿੱਚ ਇਹ ਸਮੱਗਰੀ ਹੋਵੇਗੀ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## ਕਸਰਤ: ਆਪਣੇ stdio ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰਨਾ

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਆਪਣਾ stdio ਸਰਵਰ ਬਣਾ ਲਿਆ ਹੈ, ਆਓ ਇਸਨੂੰ ਟੈਸਟ ਕਰੀਏ ਤਾਂ ਜੋ ਇਹ ਠੀਕ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ ਜਾਂ ਨਹੀਂ।

### ਯੋਗਤਾ

1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ MCP Inspector ਇੰਸਟਾਲ ਕੀਤਾ ਹੈ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. ਤੁਹਾਡਾ ਸਰਵਰ ਕੋਡ ਸੇਵ ਕੀਤਾ ਹੋਇਆ ਹੋਵੇ (ਜਿਵੇਂ ਕਿ `server.py`)

### Inspector ਨਾਲ ਟੈਸਟ ਕਰਨਾ

1. **ਆਪਣੇ ਸਰਵਰ ਦੇ ਨਾਲ Inspector ਚਲਾਓ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ਵੈੱਬ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹੋ**: Inspector ਤੁਹਾਡੇ ਸਰਵਰ ਦੀਆਂ ਯੋਗਤਾਵਾਂ ਵਿਖਾਉਂਦਾ ਬ੍ਰਾਊਜ਼ਰ ਵਿੰਡੋ ਖੋਲ੍ਹੇਗਾ।

3. **ਟੂਲ ਟੈਸਟ ਕਰੋ**:
   - ਵੱਖ-ਵੱਖ ਨਾਮਾਂ ਨਾਲ `get_greeting` ਟੂਲ ਨੂੰ ਵਰਤ ਕੇ ਦੇਖੋ
   - ਵੱਖ-ਵੱਖ ਨੰਬਰਾਂ ਨਾਲ `calculate_sum` ਟੂਲ ਟੈਸਟ ਕਰੋ
   - `get_server_info` ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਕੇ ਸਰਵਰ ਦੀ ਜਾਣਕਾਰੀ ਵੇਖੋ

4. **ਸੰਚਾਰ ਦਾ ਨਿਗਰਾਨੀ ਕਰੋ**: Inspector ਕਲਾਇੰਟ ਅਤੇ ਸਰਵਰ ਦੇ ਵਿਚਕਾਰ ਵਟਦੇ JSON-RPC ਸੁਨੇਹਿਆਂ ਨੂੰ ਦਿਖਾਉਂਦਾ ਹੈ।

### ਤੁਸੀਂ ਕੀ ਵੇਖਣਾ ਚਾਹੀਦਾ ਹੈ

ਜਦੋਂ ਤੁਹਾਡਾ ਸਰਵਰ ਠੀਕ ਤਰ੍ਹਾਂ ਚਲਦਾ ਹੈ, ਤੁਹਾਨੂੰ ਇਹ ਦਿੱਸੇਗਾ:
- Inspector ਵਿੱਚ ਸਰਵਰ ਦੀਆਂ ਯੋਗਤਾਵਾਂ ਦੀ ਲਿਸਟ
- ਟੈਸਟ ਕਰਨ ਲਈ ਟੂਲ ਉਪਲਬਧ
- JSON-RPC ਸੁਨੇਹਿਆਂ ਦਾ ਸਫਲ ਅਦਲਾ-ਬਦਲੀ
- ਇੰਟਰਫੇਸ ਵਿੱਚ ਟੂਲ ਦੇ ਜਵਾਬ

### ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

**ਸਰਵਰ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦਾ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੀਆਂ ਡਿਪੇਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਹਨ: `pip install mcp`
- Python ਸਿੰਟੈਕਸ ਅਤੇ ਇੰਡੈਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ
- ਕਨਸੋਲ ਵਿੱਚ ਕਿਸੇ ਤਰ੍ਹਾਂ ਦੀ ਤਰੁਟੀਆਂ ਲਈ ਦੇਖੋ

**ਟੂਲ ਵੇਖਾਈ ਨਹੀਂ ਦੇ ਰਹੇ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ `@server.tool()` ਡੇਕੋਰੇਟਰ ਹਨ
- ਟੂਲ ਫੰਕਸ਼ਨ `main()` ਤੋਂ ਪਹਿਲਾਂ ਪਰਿਭਾਸ਼ਿਤ ਹਨ
- ਸਰਵਰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸੰਰਚਿਤ ਹੈ ਜਾਂ ਨਹੀਂ ਚੈੱਕ ਕਰੋ

**ਕਨੈਕਸ਼ਨ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਰਵਰ stdio ਟਰਾਂਸਪੋਰਟ ਠੀਕ ਤਰੀਕੇ ਨਾਲ ਵਰਤ ਰਿਹਾ ਹੈ
- ਚੈੱਕ ਕਰੋ ਕਿ ਕੋਈ ਹੋਰ ਪ੍ਰੋਸੈਸ ਰੁਕਾਵਟ ਨਹੀਂ ਪਾ ਰਿਹਾ
- Inspector ਕਮਾਂਡ ਸਿੰਟੈਕਸ ਦੀ ਜਾਂਚ ਕਰੋ

## ਅਸਾਈਨਮੈਂਟ

ਆਪਣਾ ਸਰਵਰ ਵਧੇਰੇ ਯੋਗਤਾਵਾਂ ਨਾਲ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ। [ਇਸ ਪੰਨੇ](https://api.chucknorris.io/) ਨੂੰ ਵੇਖੋ ਉਦਾਹਰਣ ਵੱਜੋਂ ਇੱਕ ਏਪੀ ਆਈ ਕਾਲ ਕਰਨ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਿਲ ਕਰਨ ਲਈ। ਤੁਹਾਨੂੰ ਫੈਸਲਾ ਕਰਨਾ ਹੈ ਕਿ ਸਰਵਰ ਕਿਵੇਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਜ਼ਾ ਲਓ :)

## ਹੱਲ

[ਹੱਲ](./solution/README.md) ਇਹ ਇੱਕ ਸੰਭਵ ਹੱਲ ਹੈ ਜਿਸ ਵਿੱਚ ਕੰਮ ਕਰਨ ਵਾਲਾ ਕੋਡ ਹੈ।

## ਮੁੱਖ ਬਿੰਦੂ

ਇਸ ਅਧਿਆਇ ਤੋਂ ਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ ਹਨ:

- stdio ਟਰਾਂਸਪੋਰਟ ਸਥਾਨਕ MCP ਸਰਵਰਾਂ ਲਈ ਪਰਾਮਰਸ਼ਿਤ ਮਕੈਨਿਜ਼ਮ ਹੈ।
- stdio ਟਰਾਂਸਪੋਰਟ MCP ਸਰਵਰਾਂ ਅਤੇ ਕਲਾਇੰਟਾਂ ਦਰਮਿਆਨ ਸਧਾਰਨ ਇਨਪੁਟ ਅਤੇ ਆਉਟਪੁਟ ਸਟਰੀਮਾਂ ਦੁਆਰਾ ਬਿਨਾ ਰੁਕਾਵਟ ਦੇ ਸੰਚਾਰ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- ਤੁਸੀਂ ਸੀਧਾ Inspector ਅਤੇ Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ stdio ਸਰਵਰਾਂ ਨੂੰ ਵਰਤ ਸਕਦੇ ਹੋ, ਜਿਸ ਨਾਲ ਡੀਬੱਗਿੰਗ ਅਤੇ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਆਸਾਨ ਹੁੰਦਾ ਹੈ।

## ਨਮੂਨਿਆਂ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## ਵਾਧੂ ਸਰੋਤ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ਅਗਲਾ ਕੀ

## ਅਗਲੇ ਕਦਮ

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ MCP ਸਰਵਰ ਬਣਾਉਣਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਤੁਸੀਂ ਹੋਰ ਅਗਲੇ ਵਿਸ਼ਿਆਂ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ:

- **ਅਗਲਾ**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - ਦੂਰੇ ਸਰਵਰਾਂ ਲਈ ਦੂਜਾ ਸਹਿਯੋਗੀ ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਸਿੱਖੋ
- **ਉੱਚ-ਸਤਰ**: [MCP Security Best Practices](../../02-Security/README.md) - ਆਪਣੇ MCP ਸਰਵਰਾਂ ਵਿੱਚ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰੋ
- **ਪ੍ਰੋਡਕਸ਼ਨ**: [Deployment Strategies](../09-deployment/README.md) - ਆਪਣੇ ਸਰਵਰਾਂ ਨੂੰ ਉਤਪਾਦਨ ਲਈ ਤਿਆਰ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ਅਧਿਕਾਰਕ ਵਿਸ਼ੇਸ਼ਤਾ
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - ਸਾਰੇ ਭਾਸ਼ਾਵਾਂ ਲਈ SDK ਹਵਾਲੇ
- [Community Examples](../../06-CommunityContributions/README.md) - ਕਮਿਊਨਿਟੀ ਤੋਂ ਹੋਰ ਸਰਵਰ ਉਦਾਹਰਣ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋक्ति**:  
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਆਰਟੀਫੀਸ਼ਲ ਇੰਟੈਲिजੈਂਸ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੂ ਹੋਵੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ ਹੁੰਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਭੁੱਲਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->