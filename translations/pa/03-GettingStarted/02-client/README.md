# ਇੱਕ ਕਲਾਇਂਟ ਬਣਾਉਣਾ

ਕਲਾਇਂਟ ਕੁਸਟਮ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਸਕ੍ਰਿਪਟਾਂ ਹੁੰਦੀਆਂ ਹਨ ਜੋ ਸਿੱਧਾ MCP ਸਰਵਰ ਨਾਲ ਸਾਂਝਾ ਕਰਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰੋਮਪਟ ਮੰਗ ਸਕਣ। ਇੰਸਪੈਕਟਰ ਟੂਲ ਵਰਤਣ ਦੇ ਵੱਖਰੇ, ਜੋ ਸਰਵਰ ਨਾਲ ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦਾ ਹੈ, ਆਪਣਾ ਕਲਾਇਂਟ ਲਿਖਣਾ ਪ੍ਰੋਗਰਾਮੈਟਿਕ ਅਤੇ ਆਟੋਮੈਟਿਕ ਇੰਟਰਐਕਸ਼ਨਾਂ ਲਈ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ MCPਦੀ ਸਮਰੱਥਾ ਆਪਣੇ ਵਰਕਫਲੋ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨ, ਟਾਸਕਾਂ ਨੂੰ ਆਟੋਮੈਟ ਕਰਨ ਅਤੇ ਖਾਸ ਜਰੂਰਤਾਂ ਲਈ ਕੁਸਟਮ ਹੱਲ ਬਣਾਉਣ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ।

## ਸਰਵੇਖਣ

ਇਸ ਸਬਕ ਵਿੱਚ ਤੁਸੀ MCP ਪੱਧਰ ਵਿੱਚ ਕਲਾਇਂਟਸ ਦੀ ਧਾਰਣਾ ਨੂੰ ਜਾਣੋਗੇ। ਤੁਸੀ ਆਪਣਾ ਕਲਾਇਂਟ ਕਿਵੇਂ ਲਿਖਣਾ ਹੈ ਅਤੇ ਇਸਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨਾ ਸਿੱਖੋਗੇ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੇ

ਇਸ ਸਬਕ ਦੇ ਅੰਤ ਤੇ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਸਮਝਣਾ ਕਿ ਕਲਾਇਂਟ ਕੀ ਕਰ ਸਕਦਾ ਹੈ।
- ਆਪਣਾ ਕਲਾਇਂਟ ਲਿਖਣਾ।
- MCP ਸਰਵਰ ਨਾਲ ਕਲਾਇਂਟ ਨੂੰ ਕਨੈਕਟ ਕਰ ਕੇ ਜਾਂਚਣਾ ਕਿ ਸਭ ਕੁਝ ਠੀਕ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।

## ਕਲਾਇਂਟ ਲਿਖਣ ਵਿੱਚ ਕੀ ਆਉਂਦਾ ਹੈ?

ਕਲਾਇਂਟ ਲਿਖਣ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਗੱਲਾਂ ਕਰਨੀਆਂ ਪੈਣਗੀਆਂ:

- **ਸਹੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਆਯਾਤ ਕਰੋ**। ਤੁਸੀਂ ਪਹਿਲਾਂ ਵਰਤੀ ਗਈ ਲਾਇਬ੍ਰੇਰੀ ਵਰਤੋਂਗੇ, ਬੱਸ ਵੱਖਰਾ ਸੰਰਚਨਾ।
- **ਇਕ ਕਲਾਇਂਟ ਦੀ ਪ੍ਰਭੂਤਾ ਕਰੋ**। ਇਸਦਾ ਅਰਥ ਹੈ ਕਿ ਕਲਾਇਂਟ ਦਾ ਇੱਕ ਨਮੂਨਾ ਬਣਾਉਣਾ ਅਤੇ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਢੰਗ ਨਾਲ ਐਸ ਨੂੰ ਜੁੜਨਾ।
- **ਰਿਹਾਇਸ਼ਾਂ ਲਿਸਟ ਕਰਨ ਬਾਰੇ ਫੈਸਲਾ ਕਰੋ**। ਤੁਹਾਡੇ MCP ਸਰਵਰ ਕੋਲ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰੋਮਪਟ ਹੁੰਦੀਆਂ ਹਨ, ਤੁਹਾਨੂੰ ਇਹ ਫੈਸਲਾ ਕਰਨਾ ਪਵੇਗਾ ਕਿ ਕਿਸ ਨੂੰ ਲਿਸਟ ਕਰਨਾ ਹੈ।
- **ਕਲਾਇਂਟ ਨੂੰ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਜੋੜੋ**। ਜਦੋਂ ਤੁਹਾਨੂੰ ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਦੀ ਜਾਣਕਾਰੀ ਹੋਵੇ, ਤਾਂ ਇਸਨੂੰ ਆਪਣੇ ਹੋਸਟ ਐਪ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ ਤਾਂ ਜੋ ਕੋਈ ਯੂਜ਼ਰ ਜਦੋਂ ਪ੍ਰੋਮਪਟ ਜਾਂ ਕਮਾਂਡ ਲਿਖੇ ਤਾਂ ਸਰਵਰ ਦੀ ਸਬੰਧਤ ਵਿਸ਼ੇਸ਼ਤਾ ਚੱਲੇ।

ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਉੱਚ-ਪੱਧਰ 'ਤੇ ਸਮਝ ਗਏ ਹਾਂ ਕਿ ਅਸੀਂ ਕੀ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ, ਚਲੋ ਅੱਗੇ ਇੱਕ ਉਦਾਹਰਨ ਦੇਖੀਏ।

### ਇੱਕ ਉਦਾਹਰਨ ਕਲਾਇਂਟ

ਆਓ ਇਸ ਉਦਾਹਰਨ ਕਲਾਇਂਟ ਨੂੰ ਦੇਖੀਏ:

### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// ਪ੍ਰਾਂਪਟ ਸੂਚੀਬੱਧ ਕਰੋ
const prompts = await client.listPrompts();

// ਇੱਕ ਪ੍ਰਾਂਪਟ ਪ੍ਰਾਪਤ ਕਰੋ
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// ਸਾਧਨ ਸੂਚੀਬੱਧ ਕਰੋ
const resources = await client.listResources();

// ਇੱਕ ਸਾਧਨ ਪੜ੍ਹੋ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ਇੱਕ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਇਂਟ ਦਾ ਨਮੂਨਾ ਬਣਾਇਆ ਅਤੇ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਜੁੜਿਆ।
- ਪ੍ਰੋਮਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲ ਲਿਸਟ ਕੀਤੇ ਅਤੇ ਸਾਰੇ ਨੂੰ ਐਨਾਵੋਕ ਕੀਤਾ।

ਲੋ, ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਕਲਾਇਂਟ ਹੈ ਜੋ MCP ਸਰਵਰ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦਾ ਹੈ।

ਅਗਲਾ ਅਭਿਆਸ ਸੈਸ਼ਨ ਵਿੱਚ ਅਸੀਂ ਧੀਰੇ ਧੀਰੇ ਹਰ ਕੋਡ ਹਿੱਸੇ ਦੀ ਵਿਆਖਿਆ ਕਰਾਂਗੇ।

## ਅਭਿਆਸ: ਕਲਾਇਂਟ ਲਿਖਣਾ

ਜਿਵੇਂ ਉਪਰ ਕਿਹਾ ਗਿਆ ਹੈ, ਆਓ ਸਮਾਂ ਲੈ ਕੇ ਕੋਡ ਦੀ ਵਿਆਖਿਆ ਕਰੀਏ, ਅਤੇ ਜੇ ਤਸੀਂ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਸਾਥ ਨਾਲ ਕੋਡ ਕਰੋ।

### -1- ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕਰੋ

ਚਲੋ ਉਹ ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕਰੀਏ ਜਿਹਨਾਂ ਦੀ ਸਾਨੂੰ ਲੋੜ ਹੈ, ਸਾਨੂੰ ਕਲਾਇਂਟ ਅਤੇ ਸਾਡੀ ਚੁਣੀ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ, stdio ਲਈ ਰਿਫਰੰਸ ਚਾਹੀਦੀ ਹੈ। stdio ਇੱਕ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਸਥਾਨਕ ਮਸ਼ੀਨ 'ਤੇ ਚਲਾਉਣ ਵਾਲੀ ਗੱਲਾਂ ਲਈ ਹੈ। SSE ਇੱਕ ਹੋਰ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਅਸੀਂ ਅਗਲੇ ਚੈਪਟਰਨਾਂ ਵਿੱਚ ਦਿਖਾਵਾਂਗੇ ਪਰ ਹੁਣ ਲਈ stdio ਨਾਲ ਜਾਰੀ ਰੱਖੀਏ।

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### ਪਾਇਥਨ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### ਜਾਵਾ

ਜਾਵਾ ਲਈ, ਤੁਸੀਂ ਪਹਿਲਾਂ ਵਾਲੇ ਅਭਿਆਸ ਵਿੱਚ ਦਿੱਤੇ MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਵਾਲਾ ਇੱਕ ਕਲਾਇਂਟ ਬਣਾਓਗੇ। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) ਦੇ ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ ਪ੍ਰਾਜੈਕਟ ਸਾਢੀ ਨਾਲ ਸਭ ਤੋਂ ਪਹਿਲਾਂ `SDKClient` ਨਾਮ ਦਾ ਜਾਵਾ ਕਲਾਸ `src/main/java/com/microsoft/mcp/sample/client/` ਫੋਲਡਰ ਵਿੱਚ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੇ ਆਯਾਤ ਸ਼ਾਮਲ ਕਰੋ:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### ਰਸਟ

ਤੁਹਾਨੂੰ ਆਪਣੇ `Cargo.toml` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

ਇੱਥੋਂ ਤੋਂ, ਤੁਸੀਂ ਆਪਣੇ ਕਲਾਇਂਟ ਕੋਡ ਵਿੱਚ ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕਰ ਸਕਦੇ ਹੋ।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ਆਓ ਹੁਣ ਇੰਸਟੈਂਸ਼ੀਏਸ਼ਨ ਵੱਲ ਵਧੀਏ।

### -2- ਕਲਾਇਂਟ ਅਤੇ ਟ੍ਰਾਂਸਪੋਰਟ ਦਾ ਇੰਸਟੈਂਸ਼ੀਏਸ਼ਨ

ਸਾਨੂੰ ਟ੍ਰਾਂਸਪੋਰਟ ਦਾ ਅਤੇ ਸਾਡੇ ਕਲਾਇਂਟ ਦਾ ਨਮੂਨਾ ਬਣਾਉਣਾ ਪਵੇਗਾ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਦਾ ਨਮੂਨਾ ਬਣਾਇਆ। ਇਸ ਵਿੱਚ ਕਮਾਂਡ ਅਤੇ args ਦਿੱਤੇ ਗਏ ਹਨ ਕਿ ਸਰਵਰ ਕਿਵੇਂ ਲੱਭਣਾ ਅਤੇ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਸਾਡਾ ਹਿੱਸਾ ਹੈ ਜਦੋਂ ਅਸੀਂ ਕਲਾਇਂਟ ਬਣਾਉਂਦੇ ਹਾਂ।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ਕਲਾਇਂਟ ਨੂੰ ਨਾਮ ਅਤੇ ਵਰਜਨ ਦੇ ਕੇ ਇੰਸਟੈਂਸ਼ੀਏਟ ਕੀਤਾ।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ਕਲਾਇਂਟ ਨੂੰ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਜੋੜਿਆ।

    ```typescript
    await client.connect(transport);
    ```

#### ਪਾਇਥਨ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰामीਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਚਲਾਉਣਯੋਗ
    args=["run", "server.py"],  # ਵੈਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਆਰਗਯੂਮੈਂਟ
    env=None,  # ਵੈਕਲਪਿਕ ਵਾਤਾਵਰਣ ਬਦਲਾਅ
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕਰੋ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕੀਤੀਆਂ
- ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਦਾ ਇੱਕ ਆਬਜੈਕਟ ਇੰਸਟੈਂਸ਼ੀਏਟ ਕੀਤਾ ਜਿਹੜਾ ਸਾਨੂੰ ਸਰਵਰ ਚਲਾਉਣ ਲਈ ਅਤੇ ਕਲਾਇਂਟ ਨਾਲ ਜੋੜਨ ਲਈ ਲੋੜੀਂਦਾ ਹੈ।
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਇਆ ਜੋ `stdio_client` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਜੋ ਕਲਾਇਂਟ ਸੈਸ਼ਨ ਸਟਾਰਟ ਕਰਦਾ ਹੈ।
- ਐਂਟਰੀ ਪੇਂਟ ਬਣਾਇਆ ਹੈ ਜਿੱਥੇ ਅਸੀਂ `run` ਮੈਥਡ ਨੂੰ `asyncio.run` ਨੂੰ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ।

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਆਯਾਤ ਕੀਤੀਆਂ।
- ਇੱਕ stdio ਟ੍ਰਾਂਸਪੋਰਟ ਬਣਾਇਆ ਤੇ ਕਲਾਇਂਟ `mcpClient` ਬਣਾਇਆ। ਇਹ ਸਾਡੇ ਲਈ MCP ਸਰਵਰ ਉੱਤੇ ਫੀਚਰ ਯਾਦ ਕਰਨ ਅਤੇ ਚਲਾਉਣ ਲਈ ਵਰਤੋਂਗੇ।

ਨੋਟ ਕਰੋ, "Arguments" ਵਿੱਚ ਤੁਸੀਂ ਜਾਂ ਤਾਂ *.csproj* ਜਾਂ ਐਗਜ਼ੈਕਯੂਟੇਬਲ ਨੂੰ ਪਾਇਂਟ ਕਰ ਸਕਦੇ ਹੋ।

#### ਜਾਵਾ

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // ਤੁਹਾਡੀ ਕਲਾਇੰਟ ਤਰਕ ਇੱਥੇ ਜਾਂਦੀ ਹੈ
    }
}
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਮੈਨ ਮੈਥਡ ਬਣਾਇਆ ਜੋ `http://localhost:8080` ਨੂੰ ਪੁਆਇੰਟ ਕਰਦਾ SSE ਟ੍ਰਾਂਸਪੋਰਟ ਸੈੱਟ ਕਰਦਾ ਹੈ ਜਿੱਥੇ MCP ਸਰਵਰ ਚੱਲੇਗਾ।
- ਇੱਕ ਕਲਾਇਂਟ ਕਲਾਸ ਬਣਾਈ ਜੋ ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ ਕਨਸਟ੍ਰਕਟਰ ਪੈਰਾਮੀਟਰ ਵਜੋਂ ਲੈਂਦਾ ਹੈ।
- `run` ਮੈਥਡ ਵਿੱਚ, ਅਸੀਂ ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਸਿੰਕਰੋਨਸ MCP ਕਲਾਇਂਟ ਬਣਾਇਆ ਅਤੇ ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕੀਤਾ।
- SSE (ਸਰਵਰ-ਸੈਂਟ ਇਵੈਂਟ) ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਿਆ, ਜੋ HTTP-ਆਧਾਰਿਤ ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ MCP ਸਰਵਰਾਂ ਲਈ ਢੁਕਵਾਂ ਹੈ।

#### ਰਸਟ

ਨੋਟ ਕਰੋ ਕਿ ਇਹ ਰਸਟ ਕਲਾਇਂਟ ਮੰਨਦਾ ਹੈ ਕਿ ਸਰਵਰ "calculator-server" ਨਾਮ ਦਾ ਭਾਈ-ਭਤੀਜਾ ਪ੍ਰਾਜੈਕਟ ਹੈ ਇਕੋ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੇਗਾ ਅਤੇ ਇਸਦੇ ਨਾਲ ਜੁੜੇਗਾ।

```rust
async fn main() -> Result<(), RmcpError> {
    // ਸੇਰਵਰ ਨੂੰ ਇੱਕ ਭਰਾ ਪ੍ਰਾਜੈਕਟ ਸਮਝੋ ਜਿਸਦਾ ਨਾਮ "calculator-server" ਹੈ ਅਤੇ ਉਹੀ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹੈ
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: ਸ਼ੁਰੂ ਕਰੋ

    // TODO: ਔਜ਼ਾਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ

    // TODO: add ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ ਜਿਨ੍ਹਾਂ ਦੇ ਆਰਗੂਮੈਂਟ = {"a": 3, "b": 2} ਹਨ

    client.cancel().await?;
    Ok(())
}
```

### -3- ਸਰਵਰ ਫੀਚਰ ਲਿਸਟ ਕਰਨਾ

ਹੁਣ, ਸਾਡੇ ਕੋਲ ਕਲਾਇਂਟ ਹੈ ਜੋ ਪ੍ਰੋਗਰਾਮ ਚਲਣ ਤੇ ਕਨੈਕਟ ਕਰ ਸਕਦਾ ਹੈ। ਪਰ ਇਹ ਫੀਚਰਾਂ ਨੂੰ ਲਿਸਟ ਨਹੀਂ ਕਰਦਾ, ਚਲੋ ਹੁਣ ਇਹ ਕਰੀਏ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
// ਪ੍ਰਾਰੰਭਕ ਸੂਚੀ
const prompts = await client.listPrompts();

// ਸਰੋਤ ਸੂਚੀ
const resources = await client.listResources();

// ਸੰਦ ਸੂਚੀ
const tools = await client.listTools();
```

#### ਪਾਇਥਨ

```python
# ਉਪਲਬਧ ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ਇੱਥੇ ਅਸੀਂ ਉਪਲਬਧ ਸਰੋਤਾਂ, `list_resources()` ਅਤੇ ਟੂਲਾਂ, `list_tools` ਨੂੰ ਲਿਸਟ ਕਰਕੇ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ਉਪਰ ਦਿੱਤਾ ਹੈ ਕਿ ਅਸੀਂ ਸਰਵਰ ਉੱਤੇ ਟੂਲਾਂ ਲਿਸਟ ਕਰ ਸਕਦੇ ਹਾਂ। ਹਰ ਟੂਲ ਲਈ ਅਸੀਂ ਉਸ ਦਾ ਨਾਮ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

#### ਜਾਵਾ

```java
// ਸੰਦਾਂ ਦੀ ਸੂਚੀ ਬਨਾਓ ਅਤੇ ਦਰਸਾਓ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ਤੁਸੀਂ ਕਨੈਕਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਸਰਵਰ ਨੂੰ ਪਿੰਗ ਵੀ ਕਰ ਸਕਦੇ ਹੋ
client.ping();
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਉਪਲਬਧ ਟੂਲਾਂ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ `listTools()` ਕਾਲ ਕੀਤਾ।
- ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਚੱਲ ਰਹੀ ਹੈ ਇਹ ਪਰਖਣ ਲਈ `ping()` ਵਰਤਿਆ।
- `ListToolsResult` ਵਿੱਚ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾ ਸ਼ਾਮਲ ਹਨ।

ਵਧੀਆ, ਅਸੀਂ ਹੁਣ ਸਾਰੇ ਫੀਚਰ ਪ੍ਰਾਪਤ ਕਰ ਲਏ ਹਨ। ਹੁਣ ਸਵਾਲ ਇਹ ਹੈ ਕਿ ਅਸੀਂ ਇਹ ਕਦੋਂ ਵਰਤਣਾ ਹੈ? ਇਹ ਕਲਾਇਂਟ ਬਹੁਤ ਸਧਾਰਣ ਹੈ, ਇਸ ਲਈ ਫੀਚਰਾਂ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ ‘ਤੇ ਕਾਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ। ਅਗਲੇ ਚੈਪਟਰ ਵਿੱਚ ਅਸੀਂ ਇੱਕ ਜਿਆਦਾ ਅੱਗੇ ਵਧਿਆ ਕਲਾਇਂਟ ਬਣਾਵਾਂਗੇ ਜਿਸਦੇ ਕੋਲ ਆਪਣਾ ਵੱਡਾ ਭਾਸ਼ਾ ਮਾਡਲ, LLM, ਹੋਵੇਗਾ। ਪਰ ਹੁਣ ਲਈ, ਆਓ ਦੇਖੀਏ ਕਿ ਅਸੀਂ ਸਰਵਰ ਉੱਤੇ ਕਿਵੇਂ ਫੀਚਰ ਚਲਾ ਸਕਦੇ ਹਾਂ:

#### ਰਸਟ

ਮੁੱਖ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਕਲਾਇਂਟ ਨੂੰ ਇਨੀਸ਼ੀਅਲਾਈਜ਼ ਕਰਨ ਤੋਂ ਬਾਦ ਅਸੀਂ ਸਰਵਰ ਨੂੰ ਇਨੀਸ਼ੀਅਲਾਈਜ਼ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ ਕੁਝ ਫੀਚਰਾਂ ਦੀ ਲਿਸਟ ਕਰ ਸਕਦੇ ਹਾਂ।

```rust
// ਸ਼ੁਰੂ ਕਰੋ
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ਸੰਦਾਂ ਦੀ ਸੂਚੀ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ਫੀਚਰ ਚਲਾਉਣਾ

ਫੀਚਰ ਚਲਾਉਣ ਲਈ ਸਾਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣਾ ਪਵੇਗਾ ਕਿ ਅਸੀਂ ਸਹੀ Arguments ਅਤੇ ਕਈ ਵਾਰ ਜਿਹੜਾ ਨਾਮ ਅਸੀਂ ਚਲਾ ਰਹੇ ਹਾਂ, ਉਹ ਸਹੀ ਦਿੱਤਾ ਹੈ।

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript

// ਇੱਕ ਸਰੋਤ ਪੜ੍ਹੋ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ਇੱਕ ਸੰਦ ਨੂੰ ਕਾਲ ਕਰੋ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ਪ੍ਰੰਪਟ ਨੂੰ ਕਾਲ ਕਰੋ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ਉਪਰ ਦਿੱਤਿਆ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਸਰੋਤ ਨੂੰ ਪੜ੍ਹਿਆ, ਸਾਨੂੰ `readResource()` ਨਾਲ `uri` ਦਿੱਤਾ। ਸਰਵਰ ਪਾਸੇ ਇਸ ਦਾ ਆਮ ਰੂਪ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦਾ ਹੈ:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    ਸਾਡਾ `uri` ਮੁੱਲ `file://example.txt` ਸਰਵਰ ਤੇ `file://{name}` ਨਾਲ ਮਿਲਦਾ ਹੈ। `example.txt` `name` ਨਾਲ ਜੋੜਿਆ ਜਾਵੇਗਾ।

- ਇੱਕ ਟੂਲ ਚਲਾਇਆ, ਇਸਦਾ ਨਾਂ ਅਤੇ Arguments ਦਿੱਤੇ:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ਪ੍ਰੋਮਪਟ ਲਿਆ, `getPrompt()` ਨੂੰ `name` ਅਤੇ Arguments ਨਾਲ ਕਾਲ ਕੀਤਾ। ਸਰਵਰ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਤਾ ਜਾ ਸਕਦਾ ਹੈ:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    ਇਸ ਤਰ੍ਹਾਂ ਤੁਹਾਡਾ ਕਲਾਇਂਟ ਕੋਡ ਸਰਵਰ ਤੇ ਐਲਾਨ ਕੀਤੇ ਤਰੀਕੇ ਨਾਲ ਮਿਲਦਾ ਜੁਲਦਾ ਹੋਵੇਗਾ:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### ਪਾਇਥਨ

```python
# ਇੱਕ ਸਰੋਤ ਪੜ੍ਹੋ
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ਇੱਕ ਟੂਲ ਕਾਲ ਕਰੋ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ਉਪਰ ਦਿੱਤਾ ਕੋਡ ਵਿਚ ਅਸੀਂ:

- `greeting` ਨਾਮ ਦਾ ਸਰੋਤ `read_resource` ਨਾਲ ਕਾਲ ਕੀਤਾ।
- `add` ਨਾਮ ਦੀ ਟੂਲ `call_tool` ਨਾਲ ਚਲਾਇਆ।

#### .NET

1. ਚਲਾਉਣ ਲਈ ਹੁਣ ਕੁਝ ਫੀਚਰਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦਾ ਕੋਡ ਮਿਲਾਓ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਿੰਟ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਹੈ:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ਜਾਵਾ

```java
// ਵੱਖ-ਵੱਖ ਕੈਲਕੂਲੇਟਰ ਟੂਲਜ਼ ਨੂੰ ਕਾਲ ਕਰੋ
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

ਉਪਰ ਦਿੱਤਾ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਬਹੁਤ ਸਾਰੇ ਕੇਲਕुलेਟਰ ਟੂਲ `callTool()` ਮੈਥਡ ਨਾਲ `CallToolRequest` ਆਬਜੈਕਟ ਵਰਤ ਕੇ ਕਾਲ ਕੀਤੇ।
- ਹਰ ਟੂਲ ਕਾਲ ਟੂਲ ਦਾ ਨਾਂ ਅਤੇ ਉਸਦੇ Argument ਦੀ Map ਦਿੰਦਾ ਹੈ।
- ਸਰਵਰ ਟੂਲਾਂ ਨੂੰ ਖਾਸ ਪੈਰਾਮੀਟਰ ਨਾਮ ਜਿਵੇਂ "a", "b" ਦੀ ਉਮੀਦ ਹੁੰਦੀ ਹੈ ਗਣਿਤੀ ਬਾਰੇ ਕੰਮਾਂ ਵਿੱਚ।
- ਨਤੀਜੇ `CallToolResult` ਆਬਜੈਕਟ ਵਜੋਂ ਮਿਲਦੇ ਹਨ ਜੋ ਸਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਹੁੰਦਾ ਹੈ।

#### ਰਸਟ

```rust
// ਆਰਗ yuਮੈਂਟਸ = {"a": 3, "b": 2} ਨਾਲ ਜੋੜ ਯੰਤਰ ਨੂੰ ਕਾਲ ਕਰੋ
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- ਕਲਾਇਂਟ ਚਲਾਉਣਾ

ਕਲਾਇਂਟ ਚਲਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਲਿਖੋ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

ਆਪਣੀ "scripts" ਸੈਕਸ਼ਨ ਵਿੱਚ *package.json* ਫਾਇਲ ਵਿੱਚ ਇਹ ਇੰਟਰੀ ਸ਼ਾਮਲ ਕਰੋ:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### ਪਾਇਥਨ

ਕਲਾਇਂਟ ਨੂੰ ਇਹ ਕਮਾਂਡ ਨਾਲ ਕਾਲ ਕਰੋ:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ਜਾਵਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡਾ MCP ਸਰਵਰ `http://localhost:8080` 'ਤੇ ਚੱਲ ਰਿਹਾ ਹੈ। ਫਿਰ ਕਲਾਇਂਟ ਚਲਾਓ:

```bash
# ਆਪਣਾ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ
./mvnw clean compile

# ਕਲਾਇੰਟ ਨੂੰ ਚਲਾਓ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ਬਦਲ ਵਜੋਂ, ਤੁਸੀਂ ਇਸ ਪੂਰੇ ਕਲਾਇੰਟ ਪ੍ਰਾਜੈਕਟ ਨੂੰ ਵੀ ਚਲਾ ਸਕਦੇ ਹੋ ਜੋ ਹਲ ਫੋਲਡਰ `03-GettingStarted\02-client\solution\java` ਵਿਚ ਦਿੱਤਾ ਹੈ:

```bash
# ਸਾਲਿਊਸ਼ਨ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ
cd 03-GettingStarted/02-client/solution/java

# JAR ਬਿਲਡ ਅਤੇ ਚਲਾਓ
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### ਰਸਟ

```bash
cargo fmt
cargo run
```

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ, ਤੂੰ ਜੋ ਸਿਖਿਆ ਹੈ ਉਸਦੇ ਅਨੁਸਾਰ ਕਲਾਇਂਟ ਬਣਾਵੇਗਾ ਪਰ ਆਪਣਾ ਖ਼ੁਦ ਦਾ ਕਲਾਇਂਟ ਬਣਾਓਗਾ।

ਇੱਥੇ ਇੱਕ ਸਰਵਰ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਕਲਾਇਂਟ ਕੋਡ ਰਾਹੀਂ ਕਾਲ ਕਰਨਗੇ, ਵੇਖੋ ਕੀ ਤੁਸੀਂ ਇਸ ਸਰਵਰ ਵਿੱਚ ਵਧੇਰੇ ਫੀਚਰ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਇਹ ਹੋਰ ਦਿਲਚਸਪ ਬਣੇ।

### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ਇੱਕ ਜੋੜਣ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ਇੱਕ ਗਤੀਸ਼ੀਲ ਸਵਾਗਤ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// stdin 'ਤੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਅਤੇ stdout 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਣਾ ਸ਼ੁਰੂ ਕਰੋ

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### ਪਾਇਥਨ

```python
# server.py
from mcp.server.fastmcp import FastMCP

# ਇੱਕ MCP ਸਰਵਰ ਬਣਾਓ
mcp = FastMCP("Demo")


# ਇੱਕ ਜੋੜਾਂ ਵਾਲਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ਇੱਕ ਗਤਿਸ਼ੀਲ ਸਤਿਕਾਰ ਸਰੋਤ ਜੁੜੋ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

ਇਸ ਪ੍ਰਾਜੈਕਟ ਨੂੰ ਵੇਖੋ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ [prompts ਅਤੇ resources ਜੋੜ ਸਕਦੇ ਹੋ](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

ਇਸ ਲਿੰਕ ਨੂੰ ਵੀ ਦੇਖੋ ਕਿ ਕਿਵੇਂ [prompts ਅਤੇ resources ਚਲਾਉਣੇ ਹਨ](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)।

### ਰਸਟ

ਪਿਛਲੇ ਸੈਕਸ਼ਨ ਵਿੱਚ, ਤੁਸੀਂ ਸਿੱਖਿਆ ਕਿ ਕਿਵੇਂ ਸਧਾਰਣ MCP ਸਰਵਰ ਰਸਟ ਨਾਲ ਬਣਾਇਆ ਜਾਵੇ। ਤੁਸੀਂ ਇਸਨੂੰ ਅੱਗੇ ਵਧਾ ਸਕਦੇ ਹੋ ਜਾਂ ਇਸ ਲਿੰਕ 'ਤੇ ਹੋਰ ਰਸਟ-ਆਧਾਰਿਤ MCP ਸਰਵਰ ਉਦਾਹਰਨਾਂ ਦੇਖੋ: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ਹੱਲ

**ਹੱਲ ਫੋਲਡਰ** ਵਿੱਚ ਪੂਰੀਆਂ, ਚਲਾਉਣਯੋਗ ਕਲਾਇਂਟ ਕਾਰਜਕਾਰੀ ਹਨ ਜੋ ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ ਕਵਰ ਕੀਤੇ ਸਾਰੇ ਧਾਰਣਾ ਦਿਖਾਉਂਦੀਆਂ ਹਨ। ਹਰ ਹੱਲ ਵਿੱਚ ਕਲਾਇਂਟ ਅਤੇ ਸਰਵਰ ਦੋਹਾਂ ਦਾ ਕੋਡ ਸ਼ਾਮਲ ਹੁੰਦਾ ਹੈ ਜੋ ਵੱਖਰੇ ਅਤੇ ਖੁਦਮੁਖ਼ਤਿਆਰ ਪ੍ਰਾਜੈਕਟਾਂ ਵਿੱਚ ਵੰਡਿਆ ਗਿਆ ਹੈ।

### 📁 ਹੱਲ ਦਾ ਸੰਰਚਨਾ

ਹੱਲ ਡਾਇਰੈਕਟਰੀ ਭਾਸ਼ਾ ਅਨੁਸਾਰ ਵੱਖਰੀ ਕੀਤੀ ਗਈ ਹੈ:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 ਹਰ ਹੱਲ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ

ਹਰ ਭਾਸ਼ਾ-ਅਧਾਰਿਤ ਹੱਲ ਇਹ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ:

- **ਪੂਰਾ ਕਲਾਇਂਟ ਕਾਰਜਕਾਰੀ** ਜਿਸ ਵਿੱਚ ਇਸ ਟਿਊਟੋਰਿਯਲ ਦੀਆਂ ਸਾਰੀਆਂ ਫੀਚਰਾਂ ਹਨ
- **ਚੱਲਦਾ ਪ੍ਰਾਜੈਕਟ ਸੰਰਚਨਾ** ਸਹੀ ਡਿਪੈਂਡੈਂਸੀ ਅਤੇ ਵਿਨ्यास ਸਮੇਤ
- **ਬਿਲਡ ਅਤੇ ਚਲਾਉਣ ਵਾਲੀਆਂ ਸਕ੍ਰਿਪਟਾਂ**  
- **ਭਾਸ਼ਾ-ਕੁਸ਼ਲ README** ਹਦਾਇਤਾਂ ਸਮੇਤ
- **ਗਲਤੀ ਸੰਭਾਲ ਅਤੇ ਨਤੀਜਾ ਪ੍ਰਕਿਰਿਆਕਰਨ ਦੇ ਉਦਾਹਰਨ**

### 📖 ਹੱਲ ਦੇ ਵਰਤੋਂ

1. **ਆਪਣੀ ਪਸੰਦੀਦਾ ਭਾਸ਼ਾ ਵਾਲੇ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ**:

   ```bash
   cd solution/typescript/    # ਟਾਈਪਸਕ੍ਰਿਪਟ ਲਈ
   cd solution/java/          # ਜਾਵਾ ਲਈ
   cd solution/python/        # ਪਾਇਥਨ ਲਈ
   cd solution/dotnet/        # .NET ਲਈ
   ```

2. **ਹਰ ਫੋਲਡਰ ਵਿੱਚ README ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ**:
   - ਡਿਪੈਂਡੈਂਸੀ ਇੰਸਟਾਲ ਕਰਨਾ
   - ਪ੍ਰਾਜੈਕਟ ਬਣਾਉਣਾ
   - ਕਲਾਇਂਟ ਚਲਾਉਣਾ

3. **ਤੁਹਾਨੂੰ ਕੁਝ ਐਸਾ ਆਉਟਪੁੱਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ਪੂਰੀ ਦਸਤਾਵੇਜ਼ੀ ਅਤੇ ਕਦਮ-ਦਰ-কਦਮ ਹਦਾਇਤਾਂ ਲਈ, ਵੇਖੋ: **[📖 ਹੱਲ ਦੀ ਦਸਤਾਵੇਜ਼ੀ](./solution/README.md)**

## 🎯 ਪੂਰੇ ਉਦਾਹਰਨ

ਅਸੀਂ ਸਾਰੇ ਪਾਠ ਵਿੱਚ ਕਵਰੇਜ ਕੀਤੇ ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਲਈ ਪੂਰੇ ਅਤੇ ਕੰਮ ਕਰਦੇ ਕਲਾਇਂਟ ਕਾਰਜਕਾਰੀ ਦਿੱਤੇ ਹਨ। ਇਹ ਉਦਾਹਰਨਾਂ ਉਪਰ ਦਿੱਤੀ ਸਮਰਥਾਵਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਝਲਕਦੀਆਂ ਹਨ ਅਤੇ ਤੁਹਾਡੇ ਆਪਣੇ ਪ੍ਰਾਜੈਕਟਾਂ ਲਈ ਸੰਦ ਜਾਂ ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਵਜੋਂ ਵਰਤੇ ਜਾ ਸਕਦੀਆਂ ਹਨ।

### ਉਪਲਬਧ ਪੂਰੇ ਉਦਾਹਰਨ

| ਭਾਸ਼ਾ | ਫਾਇਲ | ਵੇਰਵਾ |
|----------|------|-------------|
| **ਜਾਵਾ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਣ ਵਾਲਾ ਪੂਰਾ ਜਾਵਾ ਕਲਾਇਂਟ ਬਹੁਤ ਧਿਆਨ-ਪੂਰਵਕ ਗਲਤੀ ਸੰਜਮਹਣੀ ਦੇ ਨਾਲ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤ ਕੇ ਪੂਰਾ C# ਕਲਾਇਂਟ ਜੋ ਸਰਵਰ ਆਟੋਮੈਟਿਕ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ |
| **ਟਾਈਪਸਕ੍ਰਿਪਟ** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | ਟਾਈਪਸਕ੍ਰਿਪਟ ਵਿੱਚ MCP ਪ੍ਰੋਟੋਕੋਲ ਦੀ ਪੂਰੀ ਸਹਾਇਤਾ ਵਾਲਾ ਕਲਾਇਂਟ |
| **ਪਾਇਥਨ** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ਪੈਟਰਨ ਵਾਲਾ ਪੂਰਾ ਪਾਇਥਨ ਕਲਾਇਂਟ |
| **ਰਸਟ** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | ਟੋਕੀਓ ਵਰਤ ਕੇ async ਕਾਰਜ ਲਈ ਪੂਰਾ ਰਸਟ ਕਲਾਇਂਟ |

ਹਰ ਇੱਕ ਪੂਰੇ ਉਦਾਹਰਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:

- ✅ **ਕਨੈਕਸ਼ਨ ਸਥਾਪਨਾ ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ**
- ✅ **ਸਰਵਰ ਦੀ ਖੋਜ** (ਜਿੱਥੇ ਲਾਗੂ, ਟੂਲ, ਸਰੋਤ, ਪ੍ਰੋਮਪਟ)
- ✅ **ਕੈਲਕੁਲੇਟਰ ਆਪਰੇਸ਼ਨ** (ਜੋੜ, ਘਟਾਓ, ਗੁਣਾ, ਭਾਗ, ਸਹਾਇਤਾ)
- ✅ **ਨਤੀਜਾ ਪ੍ਰਕਿਰਿਆ ਅਤੇ ਸੁੰਦਰ ਫਾਰਮੈਟ ਕੀਤਾ ਹੋਇਆ ਆਉਟਪੁੱਟ**
- ✅ **ਪੂਰੀ ਗਲਤੀ ਸੰਜਮਹਣੀ**

- ✅ **ਸਾਫ਼, ਦਸਤਾਵੇਜ਼ਬੱਧ ਕੋਡ** ਕਦਮ ਦਰ ਕਦਮ ਟਿੱਪਣੀਆਂ ਦੇ ਨਾਲ

### ਪੂਰੇ ਉਦਾਹਰਨਾਂ ਦੇ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨਾ

1. ਉੱਪਰ ਦਿੱਤੀ ਸੂਚੀ ਵਿਚੋਂ ਆਪਣੀ ਮਨਪਸੰਦ ਭਾਸ਼ਾ ਚੁਣੋ
2. ਪੂਰੀ ਲਾਗੂ ਕਰਨ ਦੀ ਸਮਝ ਲਈ ਪੂਰੇ ਉਦਾਹਰਨ ਫਾਇਲ ਨੂੰ ਸਮੀਖਿਆ ਕਰੋ
3. [`complete_examples.md`](./complete_examples.md) ਵਿੱਚ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਨੂੰ ਫਾਲੋ ਕਰਦਿਆਂ ਉਦਾਹਰਨ ਚਲਾਓ
4. ਆਪਣੇ ਵਿਸ਼ੇਸ਼ ਉਪਯੋਗ ਲਈ ਉਦਾਹਰਨ ਨੂੰ ਸੋਧੋ ਅਤੇ ਵਧਾਓ

ਇਹ ਉਦਾਹਰਨਾਂ ਨੂੰ ਚਲਾਉਣ ਅਤੇ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਬਾਰੇ ਵਿਸਥਾਰ ਨਾਲ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲਈ ਦੇਖੋ: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 ਹੱਲ ਮੁਕਾਬਲੇ ਪੂਰੇ ਉਦਾਹਰਨਾਂ ਦੇ

| **ਸਮਾਧਾਨ ਫੋਲਡਰ** | **ਪੂਰੇ ਉਦਾਹਰਨ** |
|--------------------|--------------------- |
| ਪ੍ਰੋਜੈਕਟ ਦਾ ਪੂਰਾ ਢਾਂਚਾ ਅਤੇ ਬਿਲਡ ਫਾਇਲਾਂ | ਇਕੱਲੀ ਫਾਇਲ ਦੀ ਲਾਗੂ ਕਰਨਾ |
| ਡਿਪੈਂਡੈਂਸੀਜ਼ ਦੇ ਨਾਲ ਤਿਆਰ ਚੱਲਾਉਣ ਲਈ | ਧਿਆਨ ਕੇਂਦਰਿਤ ਕੋਡ ਉਦਾਹਰਨਾਂ |
| ਉਤਪਾਦਨ ਵਰਗੀ ਸੈਟਅਪ | ਸਿਖਲਾਈ ਲਈ ਸੰਦਰਭ |
| ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਟੂਲਿੰਗ | ਭਾਸ਼ਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਤੁਲਨਾ |

ਦੋਵੇਂ ਤਰੀਕੇ ਮੁੱਲਵਾਨ ਹਨ - ਪੂਰੇ ਪ੍ਰੋਜੈਕਟ ਲਈ **ਸਮਾਧਾਨ ਫੋਲਡਰ** ਅਤੇ ਸਿਖਣ ਅਤੇ ਸੰਦਰਭ ਲਈ **ਪੂਰੇ ਉਦਾਹਰਨ** ਵਰਤੋ।

## ਮੁੱਖ ਬਿੰਦੂ

ਇਸ ਅਧਿਆਇ ਲਈ ਮੁੱਖ ਬਿੰਦੂ ਇਹ ਹਨ ਕਿ ਕਲਾਇੰਟਸ ਬਾਰੇ:

- ਸਰਵਰ 'ਤੇ ਖੂਬੀਆਂ ਖੋਜਣ ਅਤੇ ਕਾਲ ਕਰਨ ਦੋਹਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।
- ਉਹ ਆਪਣੇ ਆਪ ਸ਼ੁਰੂਂ ਕਰਦਿਆਂ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਨ (ਜਿਵੇਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ) ਪਰ ਕਲਾਇੰਟਸ ਚੱਲ ਰਹੇ ਸਰਵਰਾਂ ਨਾਲ ਵੀ ਜੁੜ ਸਕਦੇ ਹਨ।
- ਇਹ ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ ਇੱਕ ਵਧੀਆ ਤਰੀਕਾ ਹੈ, ਜਿਵੇਂ ਪਹਿਲੇ ਅਧਿਆਇ ਵਿੱਚ ਇੰਸਪੈਕਟਰ ਵਰਗੀਆਂ ਵਿਕਲਪੀਆਂ ਨਾਲ ਵੇਰਵਾ ਦਿੱਤਾ ਗਿਆ ਹੈ।

## ਵਾਧੂ ਸਰੋਤ

- [MCP ਵਿੱਚ ਕਲਾਇੰਟਸ ਬਣਾਉਣਾ](https://modelcontextprotocol.io/quickstart/client)

## ਨਮੂਨੇ

- [ਜਾਵਾ ਕੈਲਕुलेਟਰ](../samples/java/calculator/README.md)
- [.NET ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੈਲਕੂਲੇਟਰ](../samples/javascript/README.md)
- [ਟਾਈਪਸਕ੍ਰਿਪਟ ਕੈਲਕੂਲੇਟਰ](../samples/typescript/README.md)
- [ਪਾਇਥਨ ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/python)
- [ਰਸਟ ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/rust)

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->