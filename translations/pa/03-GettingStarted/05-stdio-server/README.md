# MCP ਸਰਵਰ stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ

> **⚠️ ਜਰੂਰੀ ਅੱਪਡੇਟ**: MCP ਵਿਸ਼ੇਸ਼ਤਾ 2025-06-18 ਤੋਂ, ਸਵਤੰਤਰ SSE (ਸਰਵਰ-ਸੈਂਟ ਇਵੈਂਟਸ) ਟਰਾਂਸਪੋਰਟ ਨੂੰ **ਡਿਪ੍ਰੀਕੇਟ** ਕਰ ਦਿੱਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਸਦੀ ਥਾਂ "Streamable HTTP" ਟਰਾਂਸਪੋਰਟ ਨੂੰ ਲਿਆ ਗਿਆ ਹੈ। ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ ਦੋ ਮੁੱਖ ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦੀ ਹੈ:
> 1. **stdio** - ਸਟੈਂਡਰਡ ਇਨਪੁਟ/ਆਉਟਪੁੱਟ (ਸਥਾਨਕ ਸਰਵਰਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ)
> 2. **Streamable HTTP** - ਉਹਨਾਂ ਰਿਮੋਟ ਸਰਵਰਾਂ ਲਈ ਜੋ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ SSE ਵਰਤ ਸਕਦੇ ਹਨ
>
> ਇਸ ਪਾਠ ਨੂੰ **stdio ਟਰਾਂਸਪੋਰਟ** 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਨ ਲਈ ਅੱਪਡੇਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਜੋ ਕਿ ਅਧਿਕਤਮ MCP ਸਰਵਰ ਲਾਗੂ ਕਰਨ ਲਈ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਹੈ।

stdio ਟਰਾਂਸਪੋਰਟ MCP ਸਰਵਰਾਂ ਨੂੰ ਗਾਹਕਾਂ ਨਾਲ ਸਟੈਂਡਰਡ ਇਨਪੁੱਟ ਅਤੇ ਆਉਟਪੁੱਟ ਸਟਰੀਮਾਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ ਵਿੱਚ ਸਭ ਤੋਂ ਆਮ ਅਤੇ ਸਿਫਾਰਸ਼ੀ ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਹੈ, ਜੋ MCP ਸਰਵਰਾਂ ਨੂੰ ਬਣਾਉਣ ਲਈ ਇੱਕ ਸਧਾਰਣ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਵੱਖ-ਵੱਖ ਗਾਹਕ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ ਆਸਾਨੀ ਨਾਲ ਇੰਟੀਗਰੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਝਲਕ

ਇਹ ਪਾਠ stdio ਟਰਾਂਸਪੋਰਟ ਵਰਤ ਕੇ MCP ਸਰਵਰਾਂ ਨੂੰ ਕਿਵੇਂ ਬਣਾਉਣਾ ਅਤੇ ਵਰਤਣਾ ਸਿਖਾਉਂਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਵਿੱਚ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- stdio ਟਰਾਂਸਪੋਰਟ ਵਰਤ ਕੇ MCP ਸਰਵਰ ਬਣਾਉਣਾ।
- Inspector ਵਰਤ ਕੇ MCP ਸਰਵਰ ਨੂੰ ਡਿਬੱਗ ਕਰਨਾ।
- Visual Studio Code ਰਾਹੀਂ MCP ਸਰਵਰ ਨੂੰ ਵਰਤਣਾ।
- ਮੌਜੂਦਾ MCP ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮਾਂ ਨੂੰ ਸਮਝਣਾ ਅਤੇ ਕਿਉਂ stdio ਸਿਫਾਰਸ਼ੀ ਹੈ ਇਹ ਜਾਣਨਾ।

## stdio ਟਰਾਂਸਪੋਰਟ - ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ

stdio ਟਰਾਂਸਪੋਰਟ ਮੌਜੂਦਾ MCP ਵਿਸ਼ੇਸ਼ਤਾ (2025-06-18) ਵਿੱਚ ਸਮਰਥਿਤ ਦੋ ਟਰਾਂਸਪੋਰਟ ਕਿਸਮਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦਾ ਹੈ:

- **ਸਧਾਰਣ ਸੰਚਾਰ**: ਸਰਵਰ ਸਟੈਂਡਰਡ ਇਨਪੁੱਟ (`stdin`) ਤੋਂ JSON-RPC ਸੁਨੇਹੇ ਪੜ੍ਹਦਾ ਹੈ ਅਤੇ ਸਟੈਂਡਰਡ ਆਉਟਪੁੱਟ (`stdout`) 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਦਾ ਹੈ।
- **ਪ੍ਰੋਸੈਸ-ਆਧਾਰਿਤ**: ਗਾਹਕ MCP ਸਰਵਰ ਨੂੰ ਇੱਕ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।
- **ਸੁਨੇਹਾ ਫਾਰਮੈਟ**: ਸੁਨੇਹੇ ਵਿਅਕਤੀਗਤ JSON-RPC ਬੇਨਤੀਆਂ, ਸੂਚਨਾਵਾਂ ਜਾਂ ਪ੍ਰਤੀਕ੍ਰਿਆਵਾਂ ਹੁੰਦੇ ਹਨ ਜੋ ਨਿਊਲਾਈਨਾਂ ਨਾਲ ਵੱਖਰੇ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- **ਲੌਗਿੰਗ**: ਸਰਵਰ ਲੌਗਿੰਗ ਲਈ ਸਟੈਂਡਰਡ ਐਰਰ (`stderr`) 'ਤੇ UTF-8 ਸਟਰਿੰਗ ਲਿਖ ਸਕਦਾ ਹੈ।

### ਮੁੱਖ ਲੋੜਾਂ:
- ਸੁਨੇਹੇ ਨਿਊਲਾਈਨਾਂ ਨਾਲ ਵੱਖਰੇ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ ਅਤੇ ਇਹਨਾਂ ਵਿੱਚ ਇੰਬੈੱਡਡ ਨਿਊਲਾਈਨਾਂ ਨਹੀਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ
- ਸਰਵਰ ਨੂੰ `stdout` 'ਤੇ ਕੁਝ ਵੀ ਐਸਾ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ ਮਾਨਕ MCP ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ
- ਗਾਹਕ ਨੂੰ ਸਰਵਰ ਦੀ `stdin` 'ਤੇ ਕੁਝ ਵੀ ਐਸਾ ਨਹੀਂ ਲਿਖਣਾ ਚਾਹੀਦਾ ਜੋ ਮਾਨਕ MCP ਸੁਨੇਹਾ ਨਾ ਹੋਵੇ

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

ਉਪਰ ਦਿੱਖੀ ਕੋਡ ਵਿੱਚ:

- ਅਸੀਂ MCP SDK ਤੋਂ `Server` ਕਲਾਸ ਅਤੇ `StdioServerTransport` ਨੂੰ ਆਯਾਤ ਕਰਦੇ ਹਾਂ
- ਅਸੀਂ ਮੂਲ ਸੰਰਚਨਾ ਅਤੇ ਯੋਗਤਾਵਾਂ ਨਾਲ ਸਰਵਰ ਉਦਾਹਰਣ ਬਣਾਉਂਦੇ ਹਾਂ
- ਅਸੀਂ `StdioServerTransport` ਦੀ ਉਪਕਰਨ ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਸਰਵਰ ਨੂੰ ਇਸ ਨਾਲ ਜੋੜਦੇ ਹਾਂ, stdin/stdout ਰਾਹੀਂ ਸੰਚਾਰ ਯੋਗ ਬਣਾਉਂਦੇ ਹੋਏ

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

ਉਪਰ ਦਿੱਖੀ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP SDK ਵਰਤ ਕੇ ਸਰਵਰ ਬਣਾਉਂਦੇ ਹਾਂ
- ਡਿਕੋਰੇਟਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਔਜ਼ਾਰ ਪਰਿਭਾਸ਼ਤ ਕਰਦੇ ਹਾਂ
- ਟਰਾਂਸਪੋਰਟ ਸੰਭਾਲਣ ਲਈ stdio_server ਕੰਟੈਕਸਟ ਮੈਨੇਜਰ ਵਰਤਦੇ ਹਾਂ

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

SSE ਨਾਲ ਮੁੱਖ ਫਰਕ ਇਹ ਹੈ ਕਿ stdio ਸਰਵਰ:

- ਵੈੱਬ ਸਰਵਰ ਸੈਟਅੱਪ ਜਾਂ HTTP ਐਂਡਪੌਇੰਟ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ
- ਗਾਹਕ ਵੱਲੋਂ ਸਬਪ੍ਰੋਸੈਸ ਵਜੋਂ ਸ਼ੁਰੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ
- stdin/stdout ਸਟਰੀਮਾਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਦੇ ਹਨ
- ਕਾਰਗੁਜ਼ਾਰੀ ਅਤੇ ਡਿਬੱਗਿੰਗ ਇੱਕਸਾਰ ਅਤੇ ਆਸਾਨ ਹਨ

## ਅਭਿਆਸ: stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਸਾਡੇ ਸਰਵਰ ਨੂੰ ਬਣਾਉਣ ਲਈ ਸਾਨੂੰ ਦੋ ਗੱਲਾਂ ਦਾ ਧਿਆਨ ਰੱਖਣਾ ਹੈ:

- ਸਾਨੂੰ ਕਨੈਕਸ਼ਨ ਅਤੇ ਸੁਨੇਹਿਆਂ ਲਈ ਏਂਡਪੌਇੰਟ ਨੂੰ ਪ੍ਰਦਰਸ਼ਤ ਕਰਨ ਲਈ ਵੈੱਬ ਸਰਵਰ ਦੀ ਲੋੜ ਹੈ।

## ਲੈਬ: ਇੱਕ ਸਧਾਰਣ MCP stdio ਸਰਵਰ ਬਣਾਉਣਾ

ਇਸ ਲੈਬ ਵਿੱਚ, ਅਸੀਂ ਮਸ਼ਵਰਾ ਕੀਤਾ stdio ਟਰਾਂਸਪੋਰਟ ਵਰਤ ਕੇ ਇੱਕ ਸਧਾਰਣ MCP ਸਰਵਰ ਬਣਾਵਾਂਗੇ। ਇਹ ਸਰਵਰ ਔਜ਼ਾਰ ਪਰਦਾਨ ਕਰੇਗਾ ਜੋ ਗਾਹਕ ਸਧਾਰਣ Model Context Protocol ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਾਲ ਕਰ ਸਕਦੇ ਹਨ।

### ਜ਼ਰੂਰੀਆਂ ਸ਼ਰਤਾਂ

- Python 3.8 ਜਾਂ ਵੱਧ
- MCP Python SDK: `pip install mcp`
- ਐਸਿੰਕ ਪ੍ਰੋਗਰਾਮਿੰਗ ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ

ਆਓ ਸਾਡੇ ਪਹਿਲੇ MCP stdio ਸਰਵਰ ਬਣਾਉਣਾ ਸ਼ੁਰੂ ਕਰੀਏ:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ਲੌਗਿੰਗ ਸੰਰਚਨਾ ਕਰੋ
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
    # stdio ਪਰਿਵਹਨ ਦੀ ਵਰਤੋਂ ਕਰੋ
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ਡਿਪ੍ਰੀਕੇਟ ਕੀਤੇ ਗਏ SSE ਤਰੀਕੇ ਤੋਂ ਅਹੰਕਾਰਕ ਫਰਕ

**Stdio ਟਰਾਂਸਪੋਰਟ (ਮੌਜੂਦਾ ਮਿਆਰ):**
- ਸਧਾਰਣ subprocess ਮਾਡਲ - ਗਾਹਕ ਸਰਵਰ ਨੂੰ ਮੌਲ ਪ੍ਰਕਿਰਿਆ ਵਜੋਂ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ
- stdin/stdout ਰਾਹੀਂ JSON-RPC ਸੁਨੇਹਿਆਂ ਨਾਲ ਸੰਚਾਰ
- ਕੋਈ HTTP ਸਰਵਰ ਸੈਟਅੱਪ ਦੀ ਲੋੜ ਨਹੀਂ
- ਵਧੀਆ ਕਾਰਗੁਜ਼ਾਰੀ ਅਤੇ ਸੁਰੱਖਿਆ
- ਆਸਾਨ ਡਿਬੱਗਿੰਗ ਅਤੇ ਵਿਕਾਸ

**SSE ਟਰਾਂਸਪੋਰਟ (MCP 2025-06-18 ਤੋਂ ਡਿਪ੍ਰੀਕੇਟ):**
- SSE ਐਂਡਪੌਇੰਟ ਵਾਲੇ HTTP ਸਰਵਰ ਦੀ ਲੋੜ ਸੀ
- ਵੈੱਬ ਸਰਵਰ ਢਾਂਚਾ ਨਾਲ ਜ਼ਿਆਦਾ ਜਟਿਲ ਸੈਟਅੱਪ
- HTTP ਐਂਡਪੌਇੰਟ ਲਈ ਵਾਧੂ ਸੁਰੱਖਿਆ ਚਿੰਤਾਵਾਂ
- ਹੁਣ ਵੈੱਬ ਅਧਾਰਿਤ ਸਥਿਤੀਆਂ ਲਈ Streamable HTTP ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਗਿਆ

### stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ ਸਰਵਰ ਬਣਾਉਣਾ

ਸਾਡੇ stdio ਸਰਵਰ ਨੂੰ ਬਣਾਉਣ ਲਈ ਸਾਨੂੰ:

1. **ਜ਼ਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਆਯਾਤ ਕਰਨਾ** - ਸਾਨੂੰ MCP ਸਰਵਰ ਕੰਪੋਨੈਂਟ ਅਤੇ stdio ਟਰਾਂਸਪੋਰਟ ਦੀ ਲੋੜ ਹੈ
2. **ਸਰਵਰ ਉਦਾਹਰਣ ਬਣਾਉਣਾ** - ਸਰਵਰ ਦੀ ਯੋਗਤਾਵਾਂ ਨਾਲ ਪਰਿਭਾਸ਼ਾ ਕਰਨਾ
3. **ਔਜ਼ਾਰ ਪਰਿਭਾਸ਼ਤ ਕਰਨਾ** - ਉਹ ਫੰਕਸ਼ਨਾਲਿਟੀ ਜੋ ਅਸੀਂ ਪ੍ਰਦਾਨ ਕਰਨੀ ਹੈ
4. **ਟਰਾਂਸਪੋਰਟ ਸੈਟਅੱਪ ਕਰਨਾ** - stdio ਸੰਚਾਰ ਸੰਰਚਿਤ ਕਰਨਾ
5. **ਸਰਵਰ ਚਲਾਉਣਾ** - ਸਰਵਰ ਸ਼ੁਰੂ ਕਰਨਾ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਸੰਭਾਲਣਾ

ਆਓ ਇੱਕ-ਇੱਕ ਕਰ ਕੇ ਇਹ ਬਣਾਈਏ:

### ਕਦਮ 1: ਇੱਕ ਮੁੱਢਲਾ stdio ਸਰਵਰ ਬਣਾਉਣਾ

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ਲਾਗਿੰਗ ਕਨਫਿਗਰ ਕਰੋ
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

### ਕਦਮ 2: ਵੱਧ ਔਜ਼ਾਰ ਜੋੜਨਾ

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

ਸਰਵਰ ਸ਼ੁਰੂ ਹੋਏਗਾ ਅਤੇ stdin ਤੋਂ ਇਨਪੁਟ ਦੀ ਉਡੀਕ ਕਰੇਗਾ। ਇਹ stdio ਟਰਾਂਸਪੋਰਟ ਰਾਹੀਂ JSON-RPC ਸੁਨੇਹਿਆਂ ਦਾ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।

### ਕਦਮ 4: Inspector ਨਾਲ ਟੈਸਟਿੰਗ

ਤੁਸੀਂ MCP Inspector ਵਰਤ ਕੇ ਆਪਣੇ ਸਰਵਰ ਦੀ ਪਰਖ ਕਰ ਸਕਦੇ ਹੋ:

1. Inspector ਇੰਸਟਾਲ ਕਰੋ: `npx @modelcontextprotocol/inspector`
2. Inspector ਚਲਾਓ ਅਤੇ ਆਪਣੇ ਸਰਵਰ ਲਈ ਪੋਇੰਟ ਕਰੋ
3. ਤੁਸੀਂ ਬਣਾਏ ਹੋਏ ਔਜ਼ਾਰ ਦੀ ਲੜੀ ਜਾਂਚੋ

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## ਤੁਹਾਡੇ stdio ਸਰਵਰ ਦਾ ਡਿਬੱਗਿੰਗ

### MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ

MCP Inspector MCP ਸਰਵਰਾਂ ਦੇ ਡਿਬੱਗ ਅਤੇ ਟੈਸਟਿੰਗ ਲਈ ਇੱਕ ਕੀਮਤੀ ਜੰਤਰ ਹੈ। ਆਪਣੇ stdio ਸਰਵਰ ਨਾਲ ਇਸ ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ, ਇਹ ਰਿਹਾ:

1. **Inspector ਇੰਸਟਾਲ ਕਰੋ**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector ਚਲਾਓ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **ਆਪਣਾ ਸਰਵਰ ਟੈਸਟ ਕਰੋ**: Inspector ਇੱਕ ਵੈੱਬ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ:
   - ਸਰਵਰ ਯੋਗਤਾਵਾਂ ਵੇਖ ਸਕਦੇ ਹੋ
   - ਵੱਖ-ਵੱਖ ਪੈਰਾਮੀਟਰਾਂ ਨਾਲ ਔਜ਼ਾਰ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ
   - JSON-RPC ਸੁਨੇਹਿਆਂ ਦੀ ਮਾਨੀਟਰਿੰਗ ਕਰ ਸਕਦੇ ਹੋ
   - ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ ਦਾ ਡਿਬੱਗ ਕਰ ਸਕਦੇ ਹੋ

### VS Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ

ਤੁਸੀਂ ਆਪਣੇ MCP ਸਰਵਰ ਨੂੰ Visual Studio Code ਵਿੱਚ ਸਿੱਧਾ ਡਿਬੱਗ ਵੀ ਕਰ ਸਕਦੇ ਹੋ:

1. `.vscode/launch.json` ਵਿੱਚ ਲਾਂਚ ਸੰਰਚਨਾ ਬਣਾਓ:
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

2. ਆਪਣੇ ਸਰਵਰ ਕੋਡ 'ਚ ਬ੍ਰੇਕਪോയਿੰਟ ਲਗਾਓ
3. ਡਿਬੱਗਰ ਚਲਾਓ ਅਤੇ Inspector ਨਾਲ ਟੈਸਟ ਕਰੋ

### ਆਮ ਡਿਬੱਗਿੰਗ ਸੁਝਾਅ

- ਲੌਗਿੰਗ ਲਈ `stderr` ਵਰਤੋਂ - MCP ਸੁਨੇਹਿਆਂ ਲਈ `stdout` ਨੂੰ ਕਦੇ ਵੀ ਨਾ ਲਿਖੋ
- ਸਾਰੇ JSON-RPC ਸੁਨੇਹੇ ਨਿਊਲਾਈਨ-ਡੈਲੀਮੀਟਡ ਸੀਧੇ ਹੋਣ
- ਜਟਿਲ ਫੰਕਸ਼ਨਾਲਿਟੀ ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਸਧਾਰਣ ਔਜ਼ਾਰ ਨਾਲ ਟੈਸਟ ਕਰੋ
- ਸੁਨੇਹਾ ਫਾਰਮੈਟਾਂ ਦੀ ਪੱਕੀ ਜਾਂਚ ਲਈ Inspector ਵਰਤੋਂ

## VS Code ਵਿਚ ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ ਵਰਤਣਾ

ਜਦੋਂ ਤੁਸੀਂ MCP stdio ਸਰਵਰ ਬਣਾਲਿਆ, ਤਾਂ ਤੁਸੀਂ ਇਸਨੂੰ VS Code ਨਾਲ ਇੰਟੀਗਰੇਟ ਕਰਕੇ Claude ਜਾਂ ਹੋਰ MCP-ਅਨੁਕੂਲ ਗਾਹਕਾਂ ਨਾਲ ਵਰਤ ਸਕਦੇ ਹੋ।

### ਸੰਰਚਨਾ

1. `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ਜਾਂ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) ਵਿੱਚ MCP ਸੰਰਚਨਾ ਫਾਈਲ ਬਣਾਓ:

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

2. Claude ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰੋ: Claude ਨੂੰ ਬੰਦ ਅਤੇ ਮੁੜ ਖੋਲ੍ਹੋ ਤਾਂ ਜੋ ਨਵੀਂ ਸਰਵਰ ਸੰਰਚਨਾ ਲੋਡ ਹੋ ਜਾਵੇ।

3. ਕਨੈਕਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ: Claude ਨਾਲ ਗੱਲਬਾਤ ਸ਼ੁਰੂ ਕਰੋ ਅਤੇ ਆਪਣੇ ਸਰਵਰ ਦੇ ਔਜ਼ਾਰ ਵਰਤ ਕੇ ਕੋਸ਼ਿਸ਼ ਕਰੋ:
   - "ਕੀ ਤੁਸੀਂ ਗ੍ਰੀਟਿੰਗ ਟੂਲ ਵਰਤ ਕੇ ਮੈਨੂੰ ਸਤਸ੍ਰੀਅਕਾਲ ਕਹਿ ਸਕਦੇ ਹੋ?"
   - "15 ਅਤੇ 27 ਦਾ ਜੋੜ ਕਿਣਾ ਹੈ?"
   - "ਸਰਵਰ ਜਾਣਕਾਰੀ ਕੀ ਹੈ?"

### TypeScript stdio ਸਰਵਰ ਉਦਾਹਰਣ

ਇੱਥੇ ਸਾਨੂੰ ਇੱਕ ਪੂਰਾ TypeScript ਉਦਾਹਰਣ ਦਿੱਤਾ ਹੈ:

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

### .NET stdio ਸਰਵਰ ਉਦਾਹਰਣ

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

## ਸਾਰांश

ਇਸ ਅੱਪਡੇਟ ਕੀਤੇ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖਿਆ:

- ਆਧੁਨਿਕ **stdio ਟਰਾਂਸਪੋਰਟ** (ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ) ਨਾਲ MCP ਸਰਵਰ ਬਨਾਉਣਾ
- SSE ਟਰਾਂਸਪੋਰਟ ਕਿਉਂ ਡਿਪ੍ਰੀਕੇਟ ਹੋਇਆ ਅਤੇ ਇਸ ਦੀ ਥਾਂ stdio ਅਤੇ Streamable HTTP ਨੇ ਲਈ
- ਐਸੇ ਔਜ਼ਾਰ ਬਣਾਉਣਾ ਜੋ MCP ਗਾਹਕਾਂ ਵੱਲੋਂ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ
- MCP Inspector ਰਾਹੀਂ ਆਪਣੇ ਸਰਵਰ ਨੂੰ ਡਿਬੱਗ ਕਰਨਾ
- ਆਪਣੇ stdio ਸਰਵਰ ਨੂੰ VS Code ਅਤੇ Claude ਨਾਲ ਇੰਟੀਗਰੇਟ ਕਰਨਾ

stdio ਟਰਾਂਸਪੋਰਟ ਡਿਪ੍ਰੀਕੇਟ ਕੀਤੇ ਗਏ SSE ਤਰੀਕੇ ਨਾਲੋਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਬਣਾਉਣ ਦਾ ਇੱਕ ਸਧਾਰਣ, ਜ਼ਿਆਦਾ ਸੁਰੱਖਿਅਤ ਅਤੇ ਤੇਜ਼ ਤਰੀਕਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਹ 2025-06-18 ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ ਅਨੁਸਾਰ ਸਾਰਿਆਂ MCP ਸਰਵਰ ਲਾਗੂ ਕਰਨ ਲਈ ਸਿਫਾਰਸ਼ੀ ਟਰਾਂਸਪੋਰਟ ਹੈ।

### .NET

1. ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਕੁਝ ਔਜ਼ਾਰ ਬਣਾਈਏ, ਇਸ ਲਈ ਅਸੀਂ ਇੱਕ ਫਾਈਲ *Tools.cs* ਬਣਾਉਂਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੈ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## ਅਭਿਆਸ: ਆਪਣੇ stdio ਸਰਵਰ ਦੀ ਜਾਂਚ

ਹੁਣ ਜਦੋਂ ਕਿ ਤੁਸੀਂ ਆਪਣਾ stdio ਸਰਵਰ ਬਣਾਲਿਆ ਹੈ, ਆਓ ਇਸ ਦੀ ਕਾਰੀਗਿਰੀ ਨੂੰ ਪ੍ਰਮਾਣਿਤ ਕਰਨ ਲਈ ਟੈਸਟ ਕਰੀਏ।

### ਜ਼ਰੂਰੀਆਂ ਸ਼ਰਤਾਂ

1. ਯਕੀਨ ਕਰੋ ਕਿ MCP Inspector ਤੁਹਾਡੇ ਕੋਲ ਇੰਸਟਾਲ ਹੈ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. ਤੁਹਾਡਾ ਸਰਵਰ ਕੋਡ ਸੁਰੱਖਿਅਤ ਹੈ (ਉਦਾਹਰਨ ਵਜੋਂ `server.py` ਵਜੋਂ)

### Inspector ਨਾਲ ਟੈਸਟਿੰਗ

1. **ਆਪਣੇ ਸਰਵਰ ਨਾਲ Inspector ਸ਼ੁਰੂ ਕਰੋ**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **ਵੈੱਬ ਇੰਟਰਫੇਸ ਖੋਲ੍ਹੋ**: Inspector ਤੁਹਾਡੇ ਸਰਵਰ ਦੀ ਯੋਗਤਾਵਾਂ ਦਿਖਾਉਂਦਾ ਬ੍ਰਾਊਜ਼ਰ ਵਿੰਡੋ ਖੋਲ੍ਹੇਗਾ।

3. **ਔਜ਼ਾਰ ਟੈਸਟ ਕਰੋ**:
   - ਵੱਧ ਨਾਂਵਾਂ ਨਾਲ `get_greeting` ਟੂਲ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ
   - ਵੱਖ-ਵੱਖ ਅੰਕਾਂ ਨਾਲ `calculate_sum` ਟੂਲ ਟੈਸਟ ਕਰੋ
   - ਸਰਵਰ ਮੈਟਾ ਡਾਟਾ ਵੇਖਣ ਲਈ `get_server_info` ਟੂਲ ਕਾਲ ਕਰੋ

4. **ਸੰਚਾਰ ਦੀ ਮਾਨੀਟਰਿੰਗ ਕਰੋ**: Inspector JSON-RPC ਸੁਨੇਹਿਆਂ ਦੀ ਤਬਾਦਲਾ ਦਰਸਾਉਂਦਾ ਹੈ ਜੋ ਗਾਹਕ ਅਤੇ ਸਰਵਰ ਵਿਚਕਾਰ ਹੁੰਦਾ ਹੈ।

### ਤੁਹਾਨੂੰ ਕੀ ਦੇਖਣਾ ਚਾਹੀਦਾ

ਜਦੋਂ ਤੁਹਾਡੇ ਸਰਵਰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ, ਤਾਂ ਤੁਹਾਨੂੰ ਇਹ ਵੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:
- Inspector ਵਿੱਚ ਸਰਵਰ ਦੀਆਂ ਯੋਗਤਾਵਾਂ ਦੀ ਸੂਚੀ
- ਪਰਖ ਲਈ ਉਪਲਬਧ ਔਜ਼ਾਰ
- ਸਫਲ JSON-RPC ਸੁਨੇਹੇ ਦੀ ਲਿਨਦੀਂ
- ਇੰਟਰਫੇਸ ਵਿੱਚ ਟੂਲ ਦੀਆਂ ਪ੍ਰਤੀਕ੍ਰਿਆਵਾਂ

### ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਹੱਲ

**ਸਰਵਰ ਸ਼ੁਰੂ ਨਹੀਂ ਹੁੰਦਾ:**
- ਸਾਰੇ ਨਿਰਭਰਤਾ ਇੰਸਟਾਲ ਹਨ ਜਾਂ ਨਹੀਂ ਚੈੱਕ ਕਰੋ: `pip install mcp`
- Python ਸਿੰਟੈਕਸ ਅਤੇ ਇੰਡੇਂਟੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ
- ਕੰਨਸੋਲ ਵਿੱਚ ਐਰਰ ਸੁਨੇਹੇ ਦੇਖੋ

**ਔਜ਼ਾਰ ਪ੍ਰਗਟ ਨਹੀਂ ਹੁੰਦੇ:**
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ `@server.tool()` ਡਿਕੋਰੇਟਰ ਮੌਜੂਦ ਹਨ
- ਯਕੀਨੀ ਕਰੋ ਕਿ ਟੂਲ ਫੰਕਸ਼ਨ `main()` ਤੋਂ ਪਹਿਲਾਂ ਪਰਿਭਾਸ਼ਿਤ ਹਨ
- ਸਰਵਰ ਢੰਗ ਨਾਲ ਸੰਰਚਿਤ ਹੈ ਜਾਂ ਨਹੀਂ ਜਾਂਚੋ

**ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ:**
- ਸਤੰਦਾ ਰਹੋ ਕਿ ਸਰਵਰ stdio ਟਰਾਂਸਪੋਰਟ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਵਰਤ ਰਿਹਾ ਹੈ
- ਇਹ ਸੁਨਿਸ਼ਚਿਤ ਕਰੋ ਕਿ ਕੋਈ ਹੋਰ ਪ੍ਰਕਿਰਿਆ ਮਦਖਲ اندازੀ ਨਹੀਂ ਕਰ ਰਹੀ
- Inspector ਕਮਾਂਡ ਸਿੰਟੈਕਸ ਨੂੰ ਸਹੀ ਚੈੱਕ ਕਰੋ

## ਅਸਾਈਨਮੈਂਟ

ਆਪਣੇ ਸਰਵਰ ਨੂੰ ਜ਼ਿਆਦਾ ਯੋਗਤਾਵਾਂ ਨਾਲ ਵਿਸਥਾਰਿਤ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ। [ਇਸ ਪੰਨੇ](https://api.chucknorris.io/) ਨੂੰ ਵੇਖੋ, ਉਦਾਹਰਨ ਵਜੋਂ, ਇੱਕ ਐਸਾ ਟੂਲ ਜੋ API ਕਾਲ ਕਰਦਾ ਹੈ, ਸ਼ਾਮਲ ਕਰਨ ਲਈ। ਤੁਸੀਂ ਖੁਦ ਨਿਰਧਾਰਿਤ ਕਰੋ ਕਿ ਸਰਵਰ ਕਿਵੇਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਜ਼ੇ ਕਰੋ :)

## ਹੱਲ

[ਹੱਲ](./solution/README.md) ਇਹ ਇੱਕ ਸੰਭਵ ਹੱਲ ਹੈ ਜਿਸ ਵਿੱਚ ਚਲਦੇ ਕੋਡ ਹਨ।

## ਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ

ਇਸ ਅਧਿਆਇ ਤੋਂ ਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ ਇਹ ਹਨ:

- stdio ਟਰਾਂਸਪੋਰਟ ਸਥਾਨਕ MCP ਸਰਵਰਾਂ ਲਈ ਸਿਫਾਰਸ਼ੀ ਮਕੈਨਿਜ਼ਮ ਹੈ।
- stdio ਟਰਾਂਸਪੋਰਟ MCP ਸਰਵਰਾਂ ਅਤੇ ਗਾਹਕਾਂ ਵਿਚਕਾਰ ਸਟੈਂਡਰਡ ਇਨਪੁੱਟ ਅਤੇ ਆਉਟਪੁੱਟ ਸਟਰੀਮਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਿਨਾਂ ਰੁਕਾਵਟ ਸੰਚਾਰ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- ਤੁਸੀਂ Inspector ਅਤੇ Visual Studio Code ਦੋਹਾਂ ਦਾ ਸਿੱਧਾ ਵਰਤੋਂ ਕਰਕੇ stdio ਸਰਵਰਾਂ ਨੂੰ ਵਰਤ ਸਕਦੇ ਹੋ, ਜਿਹੜਾ ਡਿਬੱਗਿੰਗ ਅਤੇ ਇੰਟੀਗਰੇਸ਼ਨ ਨੂੰ ਸੌਖਾ ਬਣਾਂਦਾ ਹੈ।

## ਨਮੂਨੇ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## ਵਾਧੂ ਸਰੋਤ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## ਅਗਲਾ ਕੀ ਹੈ

## ਅਗਲੇ ਕਦਮ

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ stdio ਟਰਾਂਸਪੋਰਟ ਨਾਲ MCP ਸਰਵਰਾਂ ਬਨਾਉਣਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਤੁਸੀਂ ਹੋਰ ਅੱਗੇ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦਾ ਪਤਾ ਲਗਾ ਸਕਦੇ ਹੋ:

- **ਅਗਲਾ**: [MCP ਨਾਲ HTTP Streaming (Streamable HTTP)](../06-http-streaming/README.md) - ਰਿਮੋਟ ਸਰਵਰਾਂ ਲਈ ਹੋਰ ਸਮਰਥਿਤ ਟਰਾਂਸਪੋਰਟ ਮਕੈਨਿਜ਼ਮ ਬਾਰੇ ਜਾਣੋ
- **ਉੱਚ ਸਤਰ**: [MCP ਸੁਰੱਖਿਆ ਸਭ ਤੋਂ ਵਧੀਆ ਅਭਿਆਸ](../../02-Security/README.md) - MCP ਸਰਵਰਾਂ ਵਿੱਚ ਸੁਰੱਖਿਆ ਲਾਗੂ ਕਰੋ
- ** ਉਤਪਾਦਨ**: [ਤਾਇਨਾਤੀ ਰਣਨੀਤੀਆਂ](../09-deployment/README.md) - ਆਪਣੇ ਸਰਵਰਾਂ ਨੂੰ ਉਤਪਾਦਨ ਲਈ ਤਾਇਨਾਤ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

- [MCP ਵਿਸ਼ੇਸ਼ਤਾ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ਅਧਿਕਾਰਕ ਵਿਸ਼ੇਸ਼ਤਾ
- [MCP SDK ਦਸਤਾਵੇਜ਼](https://github.com/modelcontextprotocol/sdk) - ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ SDK ਸੰਦਰਭ
- [ਕਮਿਊਨਿਟੀ ਉਦਾਹਰਨ](../../06-CommunityContributions/README.md) - ਕਮਿਊਨਿਟੀ ਵੱਲੋਂ ਹੋਰ ਸਰਵਰ ਉਦਾਹਰਨ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਤਰ**:  
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ ਪੇਸ਼ਾਵਰ ਮਾਨਵੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->