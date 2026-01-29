# ਐਮਸੀਪੀ ਸਰਵਰ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ

> **⚠️ ਮਹੱਤਵਪੂਰਨ ਅੱਪਡੇਟ**: ਐਮਸੀਪੀ ਸਪੈਸਿਫਿਕੇਸ਼ਨ 2025-06-18 ਦੇ ਮੁਤਾਬਕ, ਸਟੈਂਡਅਲੋਨ SSE (ਸਰਵਰ-ਸੈਂਟ ਇਵੈਂਟਸ) ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ **ਡਿਪ੍ਰੀਕੇਟ** ਕਰ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਸਦੀ ਜਗ੍ਹਾ "ਸਟ੍ਰੀਮਏਬਲ HTTP" ਟ੍ਰਾਂਸਪੋਰਟ ਨੇ ਲੈ ਲਈ ਹੈ। ਮੌਜੂਦਾ ਐਮਸੀਪੀ ਸਪੈਸਿਫਿਕੇਸ਼ਨ ਦੋ ਮੁੱਖ ਟ੍ਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮਾਂ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ:
> 1. **stdio** - ਸਟੈਂਡਰਡ ਇਨਪੁਟ/ਆਉਟਪੁੱਟ (ਲੋਕਲ ਸਰਵਰਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ)
> 2. **ਸਟ੍ਰੀਮਏਬਲ HTTP** - ਦੂਰ-ਦਰਾਜ ਦੇ ਸਰਵਰਾਂ ਲਈ ਜੋ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ SSE ਵਰਤ ਸਕਦੇ ਹਨ
>
> ਇਸ ਪਾਠ ਨੂੰ **stdio ਟ੍ਰਾਂਸਪੋਰਟ** 'ਤੇ ਕੇਂਦਰਿਤ ਕਰਨ ਲਈ ਅੱਪਡੇਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ ਕਿ ਜ਼ਿਆਦਾਤਰ ਐਮਸੀਪੀ ਸਰਵਰ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਹੈ।

stdio ਟ੍ਰਾਂਸਪੋਰਟ ਐਮਸੀਪੀ ਸਰਵਰਾਂ ਨੂੰ ਸਟੈਂਡਰਡ ਇਨਪੁਟ ਅਤੇ ਆਉਟਪੁੱਟ ਸਟ੍ਰੀਮਾਂ ਰਾਹੀਂ ਕਲਾਇੰਟਾਂ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਮੌਜੂਦਾ ਐਮਸੀਪੀ ਸਪੈਸਿਫਿਕੇਸ਼ਨ ਵਿੱਚ ਸਭ ਤੋਂ ਵੱਧ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਅਤੇ ਸਿਫਾਰਸ਼ੀ ਟ੍ਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਹੈ, ਜੋ ਸਧਾਰਨ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕੇ ਨਾਲ ਐਮਸੀਪੀ ਸਰਵਰ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਸਿੱਖਿਆ ਜਾਵੇਗਾ ਕਿ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਮਸੀਪੀ ਸਰਵਰ ਕਿਵੇਂ ਬਣਾਉਣਾ ਅਤੇ ਵਰਤਣਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- stdio ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਮਸੀਪੀ ਸਰਵਰ ਬਣਾਉਣਾ।
- ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਮਸੀਪੀ ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨਾ।
- Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਮਸੀਪੀ ਸਰਵਰ ਨੂੰ ਵਰਤਣਾ।
- ਮੌਜੂਦਾ ਐਮਸੀਪੀ ਟ੍ਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮਾਂ ਨੂੰ ਸਮਝਣਾ ਅਤੇ stdio ਨੂੰ ਕਿਉਂ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।

## stdio ਟ੍ਰਾਂਸਪੋਰਟ - ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

stdio ਟ੍ਰਾਂਸਪੋਰਟ ਮੌਜੂਦਾ ਐਮਸੀਪੀ ਸਪੈਸਿਫਿਕੇਸ਼ਨ (2025-06-18) ਵਿੱਚ ਦੋ ਸਹਾਇਕ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰਕਾਰਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ:

- **ਸਧਾਰਨ ਸੰਚਾਰ**: ਸਰਵਰ ਸਟੈਂਡਰਡ ਇਨਪੁਟ (`stdin`) ਤੋਂ JSON-RPC ਸੁਨੇਹੇ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਸਟੈਂਡਰਡ ਆਉਟਪੁੱਟ (`stdout`) 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਦਾ ਹੈ।
- **ਪ੍ਰੋਸੈਸ-ਅਧਾਰਿਤ**: ਕਲਾਇੰਟ ਐਮਸੀਪੀ ਸਰਵਰ ਨੂੰ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਲਾਂਚ ਕਰਦਾ ਹੈ।
- **ਸੁਨੇਹਾ ਫਾਰਮੈਟ**: ਸੁਨੇਹੇ ਵਿਅਕਤੀਗਤ JSON-RPC ਬੇਨਤੀਆਂ, ਸੂਚਨਾਵਾਂ ਜਾਂ ਜਵਾਬ ਹੁੰਦੇ ਹਨ, ਜੋ ਨਿਊਲਾਈਨਾਂ ਦੁਆਰਾ ਵੱਖਰੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- **ਲੌਗਿੰਗ**: ਸਰਵਰ ਲੌਗਿੰਗ ਦੇ ਲਈ ਸਟੈਂਡਰਡ ਐਰਰ (`stderr`) 'ਤੇ UTF-8 ਸਟ੍ਰਿੰਗਾਂ ਲਿਖ ਸਕਦਾ ਹੈ।

### ਮੁੱਖ ਲੋੜਾਂ:
- ਸੁਨੇਹੇ ਨਿਊਲਾਈਨਾਂ ਦੁਆਰਾ ਵੱਖਰੇ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ ਅਤੇ ਉਨ੍ਹਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਨਿਊਲਾਈਨ ਨਹੀਂ ਹੋਣਾ ਚਾਹੀਦਾ।
- ਸਰਵਰ ਨੂੰ `stdout` 'ਤੇ ਕੁਝ ਵੀ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ ਵੈਧ ਐਮਸੀਪੀ ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ।
- ਕਲਾਇੰਟ ਨੂੰ ਸਰਵਰ ਦੇ `stdin` 'ਤੇ ਕੁਝ ਵੀ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ ਵੈਧ ਐਮਸੀਪੀ ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ।

### ਟਾਈਪਸਕ੍ਰਿਪਟ

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

- ਅਸੀਂ ਐਮਸੀਪੀ SDK ਤੋਂ `Server` ਕਲਾਸ ਅਤੇ `StdioServerTransport` ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੇ ਹਾਂ।
- ਅਸੀਂ ਬੁਨਿਆਦੀ ਸੰਰਚਨਾ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਨਾਲ ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦੇ ਹਾਂ।

### ਪਾਇਥਨ

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ:

- ਅਸੀਂ ਐਮਸੀਪੀ SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਉਂਦੇ ਹਾਂ।
- ਡੇਕੋਰੇਟਰਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੂਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੇ ਹਾਂ।
- stdio_server ਸੰਦਰਭ ਪ੍ਰਬੰਧਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ ਸੰਭਾਲਦੇ ਹਾਂ।

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

SSE ਨਾਲ ਮੁੱਖ ਅੰਤਰ ਇਹ ਹਨ ਕਿ stdio ਸਰਵਰ:

- ਵੈੱਬ ਸਰਵਰ ਸੈਟਅੱਪ ਜਾਂ HTTP ਐਂਡਪੌਇੰਟ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ।
- ਕਲਾਇੰਟ ਦੁਆਰਾ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਲਾਂਚ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- stdin/stdout ਸਟ੍ਰੀਮਾਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਦੇ ਹਨ।
- ਲਾਗੂ ਕਰਨ ਅਤੇ ਡੀਬੱਗ ਕਰਨ ਲਈ ਸਧਾਰਨ ਹੁੰਦੇ ਹਨ।

## ਅਭਿਆਸ: stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਸਾਡਾ ਸਰਵਰ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਦੋ ਗੱਲਾਂ ਦਾ ਧਿਆਨ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ:

- ਸਾਨੂੰ ਕਨੈਕਸ਼ਨ ਅਤੇ ਸੁਨੇਹਿਆਂ ਲਈ ਐਂਡਪੌਇੰਟ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਵੈੱਬ ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।
## ਲੈਬ: ਸਧਾਰਨ ਐਮਸੀਪੀ stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਲੈਬ ਵਿੱਚ, ਅਸੀਂ ਸਿਫਾਰਸ਼ੀ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਧਾਰਨ ਐਮਸੀਪੀ ਸਰਵਰ ਬਣਾਵਾਂਗੇ। ਇਹ ਸਰਵਰ ਉਹ ਟੂਲ ਪ੍ਰਦਾਨ ਕਰੇਗਾ ਜਿਨ੍ਹਾਂ ਨੂੰ ਕਲਾਇੰਟ ਸਟੈਂਡਰਡ ਮਾਡਲ ਕਨਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ।

### ਪੂਰਵ ਸ਼ਰਤਾਂ

- ਪਾਇਥਨ 3.8 ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ
- ਐਮਸੀਪੀ ਪਾਇਥਨ SDK: `pip install mcp`
- ਐਸਿੰਕ ਪ੍ਰੋਗਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ

ਆਓ ਆਪਣਾ ਪਹਿਲਾ ਐਮਸੀਪੀ stdio ਸਰਵਰ ਬਣਾਉਣਾ ਸ਼ੁਰੂ ਕਰੀਏ:

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

## ਡਿਪ੍ਰੀਕੇਟ ਕੀਤੇ SSE ਤਰੀਕੇ ਨਾਲ ਮੁੱਖ ਅੰਤਰ

**Stdio ਟ੍ਰਾਂਸਪੋਰਟ (ਮੌਜੂਦਾ ਮਿਆਰ):**
- ਸਧਾਰਨ ਸਬਪ੍ਰੋਸੈਸ ਮਾਡਲ - ਕਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਚਾਈਲਡ ਪ੍ਰੋਸੈਸ ਵਜੋਂ ਲਾਂਚ ਕਰਦਾ ਹੈ।
- stdin/stdout ਰਾਹੀਂ JSON-RPC ਸੁਨੇਹਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਚਾਰ।
- HTTP ਸਰਵਰ ਸੈਟਅੱਪ ਦੀ ਲੋੜ ਨਹੀਂ।
- ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸੁਰੱਖਿਆ।
- ਡੀਬੱਗ ਕਰਨ ਅਤੇ ਵਿਕਾਸ ਲਈ ਆਸਾਨ।

**SSE ਟ੍ਰਾਂਸਪੋਰਟ (MCP 2025-06-18 ਤੋਂ ਡਿਪ੍ਰੀਕੇਟ):**
- SSE ਐਂਡਪੌਇੰਟਾਂ ਨਾਲ HTTP ਸਰਵਰ ਦੀ ਲੋੜ ਸੀ।
- ਵੈੱਬ ਸਰਵਰ ਢਾਂਚੇ ਨਾਲ ਵਧੇਰੇ ਜਟਿਲ ਸੈਟਅੱਪ।
- HTTP ਐਂਡਪੌਇੰਟਾਂ ਲਈ ਵਾਧੂ ਸੁਰੱਖਿਆ ਵਿਚਾਰ।
- ਹੁਣ ਵੈੱਬ-ਅਧਾਰਿਤ ਸਥਿਤੀਆਂ ਲਈ ਸਟ੍ਰੀਮਏਬਲ HTTP ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਗਿਆ।

### stdio ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਸਰਵਰ ਬਣਾਉਣਾ

stdio ਸਰਵਰ ਬਣਾਉਣ ਲਈ, ਸਾਨੂੰ ਇਹ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

1. **ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕਰੋ** - ਐਮਸੀਪੀ ਸਰਵਰ ਕੰਪੋਨੈਂਟ ਅਤੇ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਲੋੜ ਹੈ।
2. **ਸਰਵਰ ਇੰਸਟੈਂਸ ਬਣਾਓ** - ਸਰਵਰ ਨੂੰ ਇਸ ਦੀ ਸਮਰੱਥਾਵਾਂ ਨਾਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ।
3. **ਟੂਲ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ** - ਉਹ ਕਾਰਜਸ਼ੀਲਤਾ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਤੁਸੀਂ ਪ੍ਰਦਾਨ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ।
4. **ਟ੍ਰਾਂਸਪੋਰਟ ਸੈਟਅੱਪ ਕਰੋ** - stdio ਸੰਚਾਰ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ।
5. **ਸਰਵਰ ਚਲਾਓ** - ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਸੰਭਾਲੋ।

ਆਓ ਇਸਨੂੰ ਕਦਮ ਦਰ ਕਦਮ ਬਣਾਈਏ:

### ਕਦਮ 1: ਸਧਾਰਨ stdio ਸਰਵਰ ਬਣਾਓ

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

### ਕਦਮ 2: ਹੋਰ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ

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

ਕੋਡ ਨੂੰ `server.py` ਵਜੋਂ ਸੇਵ ਕਰੋ ਅਤੇ ਕਮਾਂਡ ਲਾਈਨ ਤੋਂ ਚਲਾਓ:

```bash
python server.py
```

ਸਰਵਰ ਸ਼ੁਰੂ ਹੋਵੇਗਾ ਅਤੇ stdin ਤੋਂ ਇਨਪੁਟ ਦੀ ਉਡੀਕ ਕਰੇਗਾ। ਇਹ stdio ਟ੍ਰਾਂਸਪੋਰਟ 'ਤੇ JSON-RPC ਸੁਨੇਹਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਚਾਰ ਕਰਦਾ ਹੈ।

### ਕਦਮ 4: ਇੰਸਪੈਕਟਰ ਨਾਲ ਟੈਸਟਿੰਗ

ਤੁਸੀਂ ਆਪਣੇ ਸਰਵਰ ਨੂੰ ਐਮਸੀਪੀ ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ:

1. ਇੰਸਪੈਕਟਰ ਇੰਸਟਾਲ ਕਰੋ: `npx @modelcontextprotocol/inspector`
2. ਇੰਸਪੈਕਟਰ ਚਲਾਓ ਅਤੇ ਇਸਨੂੰ ਆਪਣੇ ਸਰਵਰ ਨਾਲ ਜੋੜੋ।
3. ਆਪਣੇ ਬਣਾਏ ਟੂਲਾਂ ਨੂੰ ਟੈਸਟ ਕਰੋ।

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨਾ

### ਐਮਸੀਪੀ ਇੰਸਪੈਕਟਰ ਦੀ ਵਰਤੋਂ

ਐਮਸੀਪੀ ਇੰਸਪੈਕਟਰ stdio ਸਰਵਰਾਂ ਨੂੰ ਡੀਬੱਗ ਅਤੇ ਟੈਸਟ ਕਰਨ ਲਈ ਇੱਕ ਕੀਮਤੀ ਟੂਲ ਹੈ। 

...

---

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।