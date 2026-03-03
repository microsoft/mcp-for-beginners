# ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਕਲਾਇੰਟ ਵਿਸ਼ੇਸ਼ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਸਕ੍ਰਿਪਟ ਹੁੰਦੇ ਹਨ ਜੋ ਸਿੱਧਾ MCP ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰਾਂਪਟ ਦੀ ਮੰਗ ਕਰ ਸਕਣ। ਇੰਸਪੈਕਟਰ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਬਜਾਏ, ਜੋ ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਕਰਨ ਲਈ ਇੱਕ ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਆਪਣਾ ਕਲਾਇੰਟ ਲਿਖਣਾ ਪ੍ਰੋਗਰਾਮੈਟਿਕ ਅਤੇ ਆਟੋਮੇਟਿਕ ਇੰਟਰਐਕਸ਼ਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ MCP ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਆਪਣੇ ਕੰਮ ਦੇ ਪ੍ਰਬੰਧ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨ, ਕਾਰਜਾਂ ਆਟੋਮੇਟ ਕਰਨ, ਅਤੇ ਨਿਰਧਾਰਿਤ ਜ਼ਰੂਰਤਾਂ ਲਈ ਕਸਟਮ ਹੱਲ ਬਣਾਉਣ ਦੀ ਸਹੂਲਤ ਦਿੰਦਾ ਹੈ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਪਰਿਵੇਸ਼ ਵਿੱਚ ਕਲਾਇੰਟਾਂ ਦੇ ਸੰਕਲਪ ਨੂੰ ਵੱਖ-ਵੱਖ ਤਰੀਕੇ ਨਾਲ ਪੇਸ਼ ਕੀਤਾ ਗਿਆ ਹੈ। ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਆਪਣਾ ਕਲਾਇੰਟ ਕਿਵੇਂ ਲਿਖਣਾ ਹੈ ਅਤੇ ਉਸ ਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਕਿਵੇਂ ਜੋੜਣਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰਥ ਹੋਵੋਗੇ:

- ਕਲਾਇੰਟ ਕੀ ਕਰ ਸਕਦਾ ਹੈ, ਇਹ ਸਮਝਣਾ।
- ਆਪਣਾ ਕਲਾਇੰਟ ਲਿਖਣਾ।
- ਕਲਾਇੰਟ ਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨਾ ਅਤੇ ਟੈਸਟ ਕਰਨਾ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਸਰਵਰ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।

## ਕਲਾਇੰਟ ਲਿਖਣ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ?

ਕਲਾਇੰਟ ਲਿਖਣ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਨੇ ਹੋਣਗੇ:

- **ਸਹੀ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕਰੋ**। ਤੁਸੀਂ ਪਹਿਲਾਂ ਵਰਤੀ ਗਈ ਲਾਇਬ੍ਰੇਰੀ ਵਰਤ ਰਹੇ ਹੋ, ਸਿਰਫ਼ ਵੱਖ ਵੱਖ ਬਣਾਤਾਂ ਨਾਲ।
- **ਕਲਾਇੰਟ ਬਣਾਓ**। ਇਹ ਵਿੱਚ ਕਲਾਇੰਟ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ ਅਤੇ ਇਸ ਨੂੰ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਵਿਧੀ ਨਾਲ ਜੋੜਨਾ ਸ਼ਾਮਲ ਹੋਵੇਗਾ।
- **ਤਯ ਕਰਨਾ ਕਿ ਕਿਹੜੇ ਸ੍ਰੋਤ ਨੂੰ ਲਿਸਟ ਕਰਨਾ ਹੈ**। ਤੁਹਾਡੇ MCP ਸਰਵਰ ਨਾਲ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰਾਂਪਟ ਹੁੰਦੇ ਹਨ, ਤੁਹਾਨੂੰ ਇਹ ਨਿਰਧਾਰਤ ਕਰਨਾ ਹੈ ਕਿ ਕਿਹੜੇ ਲਿਸਟ ਕਰਨੇ ਹਨ।
- **ਕਲਾਇੰਟ ਨੂੰ ਇੱਕ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਜੋੜਨਾ**। ਜਦੋਂ ਤੁਸੀਂ ਸਰਵਰ ਦੀ ਸਮਰੱਥਾ ਜਾਣ ਲਓ, ਤਾਂ ਇਸਨੂੰ ਆਪਣੇ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਜੋੜੋ ਤਾਂ ਜੋ ਜੇ ਕੋਈ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਜਾਂ ਹੋਰ ਕਮਾਂਡ ਟਾਈਪ ਕਰੇ ਤਾਂ ਉਸ ਅਨੁਸਾਰ ਸਰਵਰ ਫੀਚਰ ਚਲਾਇਆ ਜਾ ਸਕੇ।

ਹੁਣ ਜਦੋਂ ਕਿ ਅਸੀਂ ਉੱਚ ਪੱਧਰ 'ਤੇ ਸਮਝ ਚੁੱਕੇ ਹਾਂ ਕਿ ਅਸੀਂ ਕੀ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ, ਆਓ ਅਗਲੇ ਉਦਾਹਰਨ ਨੂੰ ਵੇਖੀਏ।

### ਇੱਕ ਉਦਾਹਰਨ ਕਲਾਇੰਟ

ਆਓ ਇਸ ਉਦਾਹਰਨ ਕਲਾਇੰਟ ਨੂੰ ਵੇਖੀਏ:

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

// ਪ੍ਰੰਪਟ ਸੂਚੀਬੱਧ ਕਰੋ
const prompts = await client.listPrompts();

// ਇੱਕ ਪ੍ਰੰਪਟ ਪ੍ਰਾਪਤ ਕਰੋ
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// ਸਰੋਤ ਸੂਚੀਬੱਧ ਕਰੋ
const resources = await client.listResources();

// ਇੱਕ ਸਰੋਤ ਪੜ੍ਹੋ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ਇੱਕ ਟੂਲ ਕਾਲ ਕਰੋ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕੀਤੀਆਂ
- stdio ਦਾ ਉਪਯੋਗ ਕਰਦਿਆਂ ਇੱਕ ਕਲਾਇੰਟ ਦਾ ਇੰਸਟੈਂਸ ਬਣਾਇਆ ਅਤੇ ਜੋੜਿਆ।
- ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲ ਲਿਸਟ ਕੀਤੇ ਅਤੇ ਸਾਰੇ ਨਿਰਵਾਹ ਕੀਤੇ।

ਇਹ ਹੈ, ਇੱਕ ਕਲਾਇੰਟ ਜੋ MCP ਸਰਵਰ ਨਾਲ ਗੱਲ ਕਰ ਸਕਦਾ ਹੈ।

ਅਗਲੇ ਅਭਿਆਸ ਸੈਸ਼ਨ ਵਿੱਚ ਅਸੀਂ ਹਰ ਕੋਡ ਟੁਕੜੇ ਨੂੰ ਵਿਚਾਰੇਂਗੇ ਅਤੇ ਸਮਝਾਵਾਂਗੇ ਕਿ ਕੀ ਹੋ ਰਿਹਾ ਹੈ।

## ਅਭਿਆਸ: ਇੱਕ ਕਲਾਇੰਟ ਲਿਖਣਾ

ਜਿਵੇਂ ਉੱਪਰ ਕਿਹਾ ਗਿਆ, ਆਓ ਅਸੀਂ ਸਮਾਂ ਲੈ ਕੇ ਕੋਡ ਨੂੰ ਸਮਝੀਏ, ਅਤੇ ਜੇਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਕੋਡ ਨਾਲ਼ ਵੀ ਚੱਲ ਸਕਦੇ ਹੋ।

### -1- ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕਰੋ

ਆਓ ਜਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕਰੀਏ, ਸਾਨੂੰ ਕਲਾਇੰਟ ਅਤੇ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ stdio ਦਾ ਹਵਾਲਾ ਦੇਣਾ ਪੈਏਗਾ। stdio ਇੱਕ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਤੁਹਾਡੇ ਸਥਾਨਕ ਮਸ਼ੀਨ ਉੱਤੇ ਚੱਲਣ ਵਾਲੀਆਂ ਚੀਜ਼ਾਂ ਲਈ ਹੈ। SSE ਇੱਕ ਹੋਰ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਅਸੀਂ ਆਉਣ ਵਾਲੇ ਅਧਿਆਏ ਵਿੱਚ ਵੇਖਾਂਗੇ ਪਰ ਇਹ ਤੁਹਾਡਾ ਦੂਜਾ ਵਿਕਲਪ ਹੈ। ਇਸ ਵੇਲੇ ਲਈ, ਆਓ stdio ਨਾਲ ਜਾਰੀ ਰੱਖੀਏ।

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

ਜਾਵਾ ਲਈ, ਤੁਸੀਂ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਉਗੇ ਜੋ ਪਿਛਲੇ ਅਭਿਆਸ ਦਾ MCP ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ। ਉਹੀ ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ ਪ੍ਰੋਜੈਕਟ ਢਾਂਚਾ ਵਰਤਦੇ ਹੋਏ ਜੋ [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) ਤੋਂ ਹੈ, `src/main/java/com/microsoft/mcp/sample/client/` ਫੋਲਡਰ ਵਿੱਚ `SDKClient` ਨਾਮਕ ਨਵੀਂ ਜਾਵਾ ਕਲਾਸ ਬਣਾਓ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਆਯਾਤਾਂ ਸ਼ਾਮਲ ਕਰੋ:

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

ਤੁਹਾਨੂੰ ਆਪਣੇ `Cargo.toml` ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਡੀਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕਰਨੀਆਂ ਪੈਣਗੀਆਂ।

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

ਇੱਥੋਂ ਤੋਂ, ਤੁਸੀਂ ਆਪਣੀ ਕਲਾਇੰਟ ਕੋਡ ਵਿੱਚ ਲੋੜੀਂਦੀ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕਰ ਸਕਦੇ ਹੋ।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ਚਲੋ ਅੱਗੇ ਇੰਸਟੈਂਸੀਏਸ਼ਨ ਵੱਲ ਵਧੀਏ।

### -2- ਕਲਾਇੰਟ ਅਤੇ ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਇੰਸਟੈਂਸੀਏਸ਼ਨ

ਸਾਨੂੰ ਇੱਕ ਟ੍ਰਾਂਸਪੋਰਟ ਅਤੇ ਇੱਕ ਕਲਾਇੰਟ ਦਾ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ ਹੋਵੇਗਾ:

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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- stdio ਟ੍ਰਾਂਸਪੋਰਟ ਇੰਸਟੈਂਸ ਬਣਾਇਆ। ਦੇਖੋ ਕਿ ਕਿਵੇਂ ਕਮਾਂਡ ਅਤੇ args ਨੂੰ ਵਿਸ਼ੇਸ਼ਤ ਕੀਤਾ ਗਿਆ ਹੈ ਕਿ ਸਰਵਰ ਕਿਵੇਂ ਲੱਭਣਾ ਅਤੇ ਚਾਲੂ ਕਰਨਾ ਹੈ, ਕਿਉਂਕਿ ਇਹ ਕੁਝ ਅਸੀਂ ਕਲਾਇੰਟ ਬਣਾਉਂਦੇ ਸਮੇਂ ਕਰਨ ਵਾਲੇ ਹਾਂ।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ਕਲਾਇੰਟ ਨੂੰ ਇੱਕ ਨਾਮ ਅਤੇ ਸਮਾਂ ਵਰਜਨ ਦਿੱਤੇ ਬਿਨਾਂ ਇੰਸਟੈਂਸ ਕੀਤਾ।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ਕਲਾਇੰਟ ਨੂੰ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਜੋੜਿਆ।

    ```typescript
    await client.connect(transport);
    ```

#### ਪਾਇਥਨ

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਚਲਾਉਣਯੋਗ
    args=["run", "server.py"],  # ਵਿਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਦਰਜ
    env=None,  # ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲ
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕਰੋ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕੀਤੀਆਂ
- ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਆਬਜੈਕਟ ਇੰਸਟੈਂਸ਼ੀਏਟ ਕੀਤਾ ਜੋ ਅਸੀਂ ਸਰਵਰ ਚਲਾਉਣ ਲਈ ਵਰਤਾਂਗੇ ਤਾਂ ਜੋ ਕਲਾਇੰਟ ਨਾਲ ਜੁੜ ਸਕੀਏ।
- `run` ਨਾਮਕ ਇੱਕ ਮੈਥਡ ਤਿਆਰ ਕੀਤਾ ਜੋ `stdio_client` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ ਜੋ ਕਲਾਇੰਟ ਸੈਸ਼ਨ ਸ਼ੁਰੂ ਕਰਦਾ ਹੈ।
- ਇੱਕ ਐਂਟਰੀ ਪਾਇੰਟ ਬਣਾਈ ਜਿਸ ਵਿੱਚ ਅਸੀਂ `asyncio.run` ਨੂੰ `run` ਮੈਥਡ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ।

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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਜਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਆਯਾਤ ਕੀਤੀਆਂ।
- stdio ਟ੍ਰਾਂਸਪੋਰਟ ਬਣਾਇਆ ਅਤੇ `mcpClient` ਕਲਾਇੰਟ ਬਣਾਇਆ। ਇਹਚੀਜ਼ ਅਸੀਂ MCP ਸਰਵਰ ਉੱਤੇ ਫੀਚਰ ਲਿਸਟ ਕਰਨ ਅਤੇ ਨਿਰਵਾਹ ਕਰਨ ਲਈ ਵਰਤਾਂਗੇ।

ਨੋਟ ਕਰੋ, "Arguments" ਵਿੱਚ ਤੁਸੀਂ ਜਾਂ ਤਾਂ *.csproj* ਜਾਂ ਐਗਜ਼ਿਕਿਊਟੇਬਲ ਨੂੰ ਪੌਇੰਟ ਕਰ ਸਕਦੇ ਹੋ।

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
        
        // ਤੁਹਾਡਾ ਕਲਾਇੰਟ ਤਰਕ ਇੱਥੇ ਜਾਂਦਾ ਹੈ
    }
}
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਮੈਨ ਮੈਥਡ ਬਣਾਇਆ ਜੋ `http://localhost:8080` ਨੂੰ ਪੌਇੰਟ ਕਰਦਾ ਈ SSE ਟ੍ਰਾਂਸਪੋਰਟ ਸੈੱਟ ਕਰਦਾ ਹੈ ਜਿੱਥੇ ਸਾਡੇ MCP ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੋਵੇਗਾ।
- ਇੱਕ ਕਲਾਇੰਟ ਕਲਾਸ ਬਣਾਇਆ ਜੋ ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ ਕੰਸਟ੍ਰਕਟਰ ਪੈਰਾਮੀਟਰ ਵਜੋਂ ਲੈਂਦੀ ਹੈ।
- `run` ਮੈਥਡ ਵਿੱਚ, ਅਸੀਂ ਟ੍ਰਾਂਸਪੋਰਟ ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ ਸਿੰਕ੍ਰੋਨਸ MCP ਕਲਾਇੰਟ ਬਣਾਇਆ ਅਤੇ ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕੀਤਾ।
- SSE (ਸਰਵਰ-ਸੈਂਟ ਈਵੇਂਟ) ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਿਆ ਜੋ ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ MCP ਸਰਵਰਾਂ ਨਾਲ HTTP ਆਧਾਰਿਤ ਸੰਚਾਰ ਲਈ ਮੋਹੱਈਆ ਹੈ।

#### ਰਸਟ

ਜੇਕਰ ਸਰਵਰ ਉਧਵਤਾ "calculator-server" ਨਾਂ ਦੇ ਸਬਲਿੰਗ ਪ੍ਰੋਜੈਕਟ ਵਜੋਂ ਸਮਾਨ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਮੰਨਿਆ ਜਾਵੇ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰੇਗਾ ਅਤੇ ਇਸ ਨਾਲ ਜੁੜੇਗਾ।

```rust
async fn main() -> Result<(), RmcpError> {
    // فرض کرو کہ سرور ایک بھائی پروجیکٹ ہے جس کا نام "calculator-server" ہے اور وہی ڈائریکٹری میں ہے
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

    // TODO: شروعات کرو

    // TODO: آلات کی فہرست بناؤ

    // TODO: add tool کو arguments = {"a": 3, "b": 2} کے ساتھ کال کرو

    client.cancel().await?;
    Ok(())
}
```

### -3- ਸਰਵਰ ਫੀਚਰਲਿਸਟ

ਹੁਣ ਸਾਡੇ ਕੋਲ ਐਸਾ ਕਲਾਇੰਟ ਹੈ ਜੋ ਚਲਣ ਤੇ ਜੋੜ ਸਕਦਾ ਹੈ। ਪਰ ਇਹ ਹਾਲੇ ਆਪਣੇ ਫੀਚਰ ਲਿਸਟ ਨਹੀਂ ਕਰਦਾ, ਆਓ ਹੁਣ ਇਹ ਕਰੀਏ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
// ਪ੍ਰੋਂਪਟਸ ਦੀ ਸੂਚੀ
const prompts = await client.listPrompts();

// ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ
const resources = await client.listResources();

// ਟੂਲਾਂ ਦੀ ਸੂਚੀ
const tools = await client.listTools();
```

#### ਪਾਇਥਨ

```python
# ਉਪਲਬਧ ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ਉਪਲਬਧ ਸੰਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ਅਸੀਂ ਉਪਲਬਧ ਸਰੋਤਾਂ `list_resources()` ਅਤੇ ਟੂਲਾਂ `list_tools` ਨੂੰ ਲਿਸਟ ਕਰਦੇ ਹਾਂ ਅਤੇ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ਉੱਪਰ ਇੱਕ ਉਦਾਹਰਨ ਹੈ ਕਿ ਕਿਵੇਂ ਸਰਵਰ ਉੱਤੇ ਟੂਲਾਂ ਲਿਸਟ ਕਰ ਸਕਦੇ ਹਾਂ। ਹਰ ਟੂਲ ਲਈ ਅਸੀਂ ਉਸ ਦਾ ਨਾਮ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

#### ਜਾਵਾ

```java
// ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ ਅਤੇ ਪ੍ਰਦਰਸ਼ਨ ਕਰੋ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ਤੁਸੀਂ ਕੁਨੈਕਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਸਰਵਰ ਨੂੰ ਪਿੰਗ ਵੀ ਕਰ ਸਕਦੇ ਹੋ
client.ping();
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਉਪਲਬਧ ਟੂਲ ਲੈਣ ਲਈ `listTools()` ਨੂੰ ਕਾਲ ਕੀਤਾ।
- ਸਰਵਰ ਨਾਲ ਸੰਜੋਗ ਸਥਾਪਿਤ ਕਰਨ ਲਈ `ping()` ਵਰਤੀ।
- `ListToolsResult` ਵਿੱਚ ਸਾਰੇ ਟੂਲਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਹੁੰਦੀ ਹੈ ਜਿਵੇਂ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾਵਾਂ।

ਵਧੀਆ, ਹੁਣ ਸਾਡੇ ਕੋਲ ਸਾਰੇ ਫੀਚਰ ਹਨ। ਹੁਣ ਸਵਾਲ ਹੈ ਕਿ ਇਹਨਾਂ ਦੀ ਵਰਤੋਂ ਕਦੋਂ ਕਰੀਏ? ਇਹ ਕਲਾਇੰਟ ਬਹੁਤ ਸਧਾਰਣ ਹੈ, ਇਸ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਸਾਨੂੰ ਫੀਚਰ ਕਾਲ ਕਰਨ ਲਈ ਸਪਸਟ ਤੌਰ 'ਤੇ ਕਾਲ ਕਰਨੀ ਪਵੇਗੀ। ਅਗਲੇ ਅਧਿਆਏ ਵਿੱਚ ਅਸੀਂ ਇੱਕ ਅੱਗੇ ਵਧੇ ਕਲਾਇੰਟ ਬਣਾਵਾਂਗੇ ਜਿਸ ਕੋਲ ਆਪਣੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ, LLM ਦੀ ਪਹੁੰਚ ਹੋਵੇਗੀ। ਫਿਲਹਾਲ, ਆਓ ਵੇਖੀਏ ਕਿ ਸਿਰਫ MCP ਸਰਵਰ ਉੱਤੇ ਫੀਚਰ ਕਿਵੇਂ ਅਮਲ ਕਰਦੇ ਹਾਂ:

#### ਰਸਟ

ਮੁੱਖ ਫੰਕਸ਼ਨ ਵਿੱਚ, ਕਲਾਇੰਟ ਇਨਿਸ਼ੀਅਲਾਈਜ਼ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ ਸਰਵਰ ਨੂੰ ਇਨਿਸ਼ੀਅਲਾਈਜ਼ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ ਕੁਝ ਫੀਚਰ ਲਿਸਟ ਕਰ ਸਕਦੇ ਹਾਂ।

```rust
// ਸ਼ੁਰੂਆਤ ਕਰੋ
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ਟੂਲਸ ਦੀ ਸੂਚੀ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ਫੀਚਰ ਕਾਲ ਕਰੋ

ਫੀਚਰ ਕਾਲ ਕਰਨ ਲਈ ਸਾਨੂੰ ਯਕੀਨੀ ਬਣਾਉਣਾ ਹੈ ਕਿ ਅਸੀਂ ਠੀਕ ਆਰਗੂਮੈਂਟ ਦਿੱਤੇ ਹਨ ਅਤੇ ਕਈ ਵਾਰ ਉਸ ਦਾ ਨਾਮ ਵੀ ਜੋ ਅਸੀਂ ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ।

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript

// ਇੱਕ ਸਰੋਤ ਪੜੋ
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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਸਰੋਤ ਨੂੰ ਪੜ੍ਹਿਆ, ਅਸੀਂ `readResource()` ਨਾਲ `uri` ਦਿੱਤਾ। ਇਹ ਸੰਭਵਤ: ਸਰਵਰ ਉਤੋਂ ਇਸ ਤਰ੍ਹਾਂ ਹੋਵੇਗਾ:

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

    ਸਾਡਾ `uri` ਮੁੱਲ `file://example.txt` ਸਰਵਰ ਉੱਤੇ `file://{name}` ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ। `example.txt` ਨੂੰ `name` ਨਾਲ ਮੈਪ ਕੀਤਾ ਜਾਵੇਗਾ।

- একটা ਟੂਲ ਕਾਲ ਕੀਤਾ, ਅਸੀਂ ਇਸ ਨੂੰ ਉਸ ਦੇ `name` ਅਤੇ `arguments` ਦੇ ਕੇ ਕਾਲ ਕਰਦੇ ਹਾਂ:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ਪ੍ਰਾਂਪਟ ਪ੍ਰਾਪਤ ਕੀਤਾ, `getPrompt()` ਤੋਂ `name` ਅਤੇ `arguments` ਦੇ ਕੇ। ਸਰਵਰ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗਦਾ ਹੈ:

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

    ਅਤੇ ਤੁਹਾਡਾ ਕਲਾਇੰਟ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਹੋਵੇਗਾ ਜੋ ਸਰਵਰ ਉੱਤੇ ਘੋਸ਼ਿਤ ਕੀਤੇ ਗਏ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ:

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
# ਇੱਕ ਸਾਧਨ ਪੜ੍ਹੋ
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ਇੱਕ ਟੂਲ ਕਾਲ ਕਰੋ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਸਰੋਤ `greeting` ਨੂੰ `read_resource` ਨਾਲ ਕਾਲ ਕੀਤਾ।
- ਇੱਕ ਟੂਲ `add` ਨੂੰ `call_tool` ਨਾਲ ਕਾਲ ਕੀਤਾ।

#### .NET

1. ਇੱਕ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

2. ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕਰਨ ਲਈ ਕੋਡ ਇੱਥੇ ਹੈ:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ਜਾਵਾ

```java
// ਵੱਖ-ਵੱਖ ਕੈਲਕुलेਟਰ ਟੂਲਜ਼ ਨੂੰ ਕਾਲ ਕਰੋ
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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਕਈ ਕੈਲਕੂਲੇਟਰ ਟੂਲਾਂ ਨੂੰ `callTool()` ਮੈਥਡ ਨਾਲ `CallToolRequest` ਔਬਜੈਕਟਾਂ ਨੂੰ ਵਰਤ ਕੇ ਕਾਲ ਕੀਤਾ।
- ਹਰ ਟੂਲ ਕਾਲ ਵਿੱਚ ਉਸ ਟੂਲ ਦਾ ਨਾਮ ਅਤੇ ਉਸ ਦੇ ਲੋੜੀਂਦੇ ਆਗਮੈਂਟ ਦਾ `Map` ਦਿੱਤਾ ਗਿਆ।
- ਸਰਵਰ ਟੂਲਾਂ ਖਾਸ ਪੈਰਾਮੀਟਰ ਨਾਮਾਂ ਦੀ ਉਮੀਦ ਕਰਦੇ ਹਨ (ਜਿਵੇਂ "a", "b" ਗਣਿਤੀ ਕੰਮਾਂ ਲਈ)।
- ਨਤੀਜੇ `CallToolResult` ਔਬਜੈਕਟ ਵਜੋਂ ਵਾਪਸ ਮਿਲਦੇ ਹਨ ਜੋ ਸਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਹਨ।

#### ਰਸਟ

```rust
// ਦਰਜ ਕੀਤੇ ਹੋਏ ਤਰਕਾਂ ਨਾਲ ਐਡ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ = {"a": 3, "b": 2}
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

### -5- ਕਲਾਇੰਟ ਚਲਾਓ

ਕਲਾਇੰਟ ਚਲਾਉਣ ਲਈ, ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਲਿਖੋ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

ਆਪਣੇ *package.json* ਦੀ "scripts" ਸੈਕਸ਼ਨ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਐਂਟਰੀ ਸ਼ਾਮਲ ਕਰੋ:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### ਪਾਇਥਨ

ਕਲਾਇੰਟ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਨਾਲ ਕਾਲ ਕਰੋ:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ਜਾਵਾ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨ ਕਰੋ ਕਿ ਤੁਹਾਡਾ MCP ਸਰਵਰ `http://localhost:8080` ਉੱਤੇ ਚੱਲ ਰਿਹਾ ਹੈ। ਫਿਰ ਕਲਾਇੰਟ ਚਲਾਓ:

```bash
# ਆਪਣਾ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ
./mvnw clean compile

# ਕਲਾਇੰਟ ਚਲਾਓ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ਵਿਕਲਪਕ ਤੌਰ ਤੇ, ਤੁਸੀਂ ਸਕੌਲਿਊਸ਼ਨ ਫੋਲਡਰ `03-GettingStarted\02-client\solution\java` ਵਿੱਚ ਦਿੱਤਾ ਹੋਇਆ ਪੂਰਾ ਕਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਚਲਾ ਸਕਦੇ ਹੋ:

```bash
# ਹੱਲ ਡਿਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ
cd 03-GettingStarted/02-client/solution/java

# JAR ਬਣਾਓ ਅਤੇ ਚਲਾਓ
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### ਰਸਟ

```bash
cargo fmt
cargo run
```

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ, ਤੁਸੀਂ ਜੋ ਸਿੱਖਿਆ ਹੈ ਉਸਦਾ ਉਪਯੋਗ ਕਰਦੇ ਹੋਏ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਉਗੇ।

ਇੱਥੇ ਇੱਕ ਸਰਵਰ ਹੈ ਜਿਸਨੂੰ ਤੁਹਾਨੂੰ ਆਪਣੇ ਕਲਾਇੰਟ ਕੋਡ ਰਾਹੀਂ ਕਾਲ ਕਰਨਾ ਹੈ, ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਇਸ ਸਰਵਰ ਵਿੱਚ ਹੋਰ ਫੀਚਰ ਜੋੜ ਕੇ ਇਸਨੂੰ ਹੋਰ ਦਿਲਚਸਪ ਬਣਾ ਸਕਦੇ ਹੋ।

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

// ਇੱਕ ਜੋੜ ਟੂਲ ਜੋੜੋ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ਇੱਕ ਗਤਿਸੀਲ ਸੰਦੇਸ਼ ਸਾਧਨ ਜੋੜੋ
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

// stdin 'ਤੇ ਸੁਨੇਹੇ ਪ੍ਰਾਪਤ ਕਰਨਾ ਅਤੇ stdout 'ਤੇ ਸੁਨੇਹੇ ਭੇਜਣਾ ਸ਼ੁਰੂ ਕਰੋ

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


# ਇਕ ਜੋੜਨ ਦਾ ਟੂਲ ਸ਼ਾਮਲ ਕਰੋ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ਇਕ ਡਾਇਨੇਮਿਕ ਸਲਾਮ ਸੰਸਾਧਨ ਸ਼ਾਮਲ ਕਰੋ
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

ਇਸ ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਵੇਖੋ ਕਿ ਕਿਵੇਂ ਤੁਸੀਂ [ਪ੍ਰਾਂਪਟ ਅਤੇ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

ਇਸ ਲਿੰਕ ਨੂੰ ਵੀ ਚੈੱਕ ਕਰੋ ਕਿ ਕਿਵੇਂ [ਪ੍ਰਾਂਪਟ ਅਤੇ ਸਰੋਤ ਕਾਲ ਕਰਨ](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ਲਈ।

### ਰਸਟ

ਪਿਛਲੇ ਅਧਿਆਏ ਵਿੱਚ ਤੁਸੀਂ ਸਿੱਖਿਆ ਕਿ ਰਸਟ ਨਾਲ ਇੱਕ ਸਧਾਰਣ MCP ਸਰਵਰ ਕਿਵੇਂ ਬਣਾਉਣਾ ਹੈ। ਤੁਸੀਂ ਇਸ ਨੂੰ ਅੱਗੇ ਵੀ ਵਧਾ ਸਕਦੇ ਹੋ ਜਾਂ ਇਸ ਲਿੰਕ ਦੀ ਸਹਾਇਤਾ ਲੈ ਸਕਦੇ ਹੋ ਜਿੱਥੇ ਹੋਰ ਰਸਟ ਆਧਾਰਿਤ MCP ਸਰਵਰ ਉਦਾਹਰਨਾਂ ਹਨ: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ਹੱਲ

**ਸਕੌਲਿਊਸ਼ਨ ਫੋਲਡਰ** ਵਿੱਚ ਪੂਰੇ, ਤਿਆਰ-ਚਲਾਉ ਕਲਾਇੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਹਨ ਜੋ ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ ਕਵਰ ਕੀਤੀਆਂ ਸਾਰੀਆਂ ਧਾਰਣਾਵਾਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਹਰ ਇੱਕ ਹੱਲ ਵਿੱਚ ਕਲਾਇੰਟ ਅਤੇ ਸਰਵਰ ਕੋਡ ਵੱਖ-ਵੱਖ, ਸਵੈ-ਨਿਰਭਰ ਪ੍ਰੋਜੈਕਟਾਂ ਵਿੱਚ ਸੰਯੋਜਿਤ ਹਨ।

### 📁 ਹੱਲ ਢਾਂਚਾ

ਹੱਲ ਡਾਇਰੈਕਟਰੀ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾ ਅਨੁਸਾਰ ਵਿਕਸਤ ਕੀਤੀ ਗਈ ਹੈ:

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

### 🚀 ਹਰ ਹੱਲ ਵਿੱਚ ਕੀ ਹੁੰਦਾ ਹੈ

ਹਰ ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਹੱਲ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:

- **ਪੂਰਾ ਕਲਾਇੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ** ਜਿਸ ਵਿੱਚ ਸਾਰੇ ਟਿਊਟੋਰਿਅਲ ਦੇ ਫੀਚਰ ਸ਼ਾਮਲ ਹਨ
- **ਸਰਗਰਮ ਪ੍ਰੋਜੈਕਟ ਢਾਂਚਾ** ਜਿਸ ਵਿੱਚ ਸਹੀ ਡੀਪੈਂਡੈਸੀਜ਼ ਅਤੇ ਸੰਰਚਨਾ ਹੈ
- **ਬਿਲਡ ਅਤੇ ਚਲਾਉਣ ਵਾਲੇ ਸਕ੍ਰਿਪਟਸ** ਆਸਾਨ ਸੈੱਟਅੱਪ ਅਤੇ ਚਲਾਉਣ ਲਈ
- **ਵਿਸ਼ਤ੍ਰਿਤ README** ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਹੁਕਮਾਂ ਨਾਲ
- **ਤ੍ਰੁੱਟੀ ਸੰਭਾਲਣ** ਅਤੇ ਨਤੀਜੇ ਪ੍ਰਕਿਰਿਆ ਉਦਾਹਰਨਾਂ

### 📖 ਹੱਲਾਂ ਦੀ ਵਰਤੋਂ

1. **ਆਪਣੀ ਮਨਪਸੰਦ ਭਾਸ਼ਾ ਵਾਲੇ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ**:

   ```bash
   cd solution/typescript/    # ਟਾਈਪਸਕ੍ਰਿਪਟ ਲਈ
   cd solution/java/          # ਜਾਵਾ ਲਈ
   cd solution/python/        # ਪਾਇਥਨ ਲਈ
   cd solution/dotnet/        # .NET ਲਈ
   ```

2. **ਹਰ ਫੋਲਡਰ ਵਿੱਚ README ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ**:
   - ਡੀਪੈਂਡੈਸੀਜ਼ ਇੰਸਟਾਲ ਕਰਨਾ
   - ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣਾ
   - ਕਲਾਇੰਟ ਚਲਾਉਣਾ

3. **ਤੁਹਾਨੂੰ ਜੋ ਨਤੀਜਾ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ਪੂਰੀ ਦਸਤਾਵੇਜ਼ੀ ਅਤੇ ਕਦਮ-ਦਰ-ਕਦਮ ਹਦਾਇਤਾਂ ਲਈ ਵੇਖੋ: **[📖 ਹੱਲ ਦਸਤਾਵੇਜ਼ੀ](./solution/README.md)**

## 🎯 ਪੂਰੇ ਉਦਾਹਰਨ

ਅਸੀਂ ਸਾਰੇ ਸਮਾਰਥਿਤ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਲਈ ਪੂਰੇ, ਤੁਲਨਾਤਮਕ ਤੌਰ 'ਤੇ ਕੰਮ ਕਰਨ ਵਾਲੇ ਕਲਾਇੰਟ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਦਿੱਤੇ ਹਨ। ਇਹ ਉਦਾਹਰਨ ਉਪਰ ਦਰਸਾਈਆਂ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਦਿਖਾਉਂਦੇ ਹਨ ਅਤੇ ਰੁਫ਼ੜ ਸੂਤਰ ਜਾਂ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟਾਂ ਲਈ ਸ਼ੁਰੂਆਤ ਵਾਲੇ ਪੁਆਇੰਟ ਵਜੋਂ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।

### ਉਪਲਬਧ ਪੂਰੇ ਉਦਾਹਰਨ

| ਭਾਸ਼ਾ | ਫਾਈਲ | ਵਰਣਨ |
|----------|------|-------------|
| **ਜਾਵਾ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਦਾ ਪੂਰਾ ਜਾਵਾ ਕਲਾਇੰਟ ਜਿਸ ਵਿੱਚ ਵਿਸਤ੍ਰਿਤ ਤ੍ਰੁੱਟੀ ਸੰਭਾਲ ਹੈ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ਟ੍ਰਾਂਸਪੋਰਟ ਨਾਲ ਪੂਰਾ C# ਕਲਾਇੰਟ ਜੋ ਸਵੈਚਾਲਿਤ ਸਰਵਰ ਸ਼ੁਰੂਆਤ ਕਰਦਾ ਹੈ |
| **ਟਾਈਪਸਕ੍ਰਿਪਟ** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | ਪੂਰਾ ਟਾਈਪਸਕ੍ਰਿਪਟ ਕਲਾਇੰਟ MCP ਪ੍ਰੋਟੋਕੋਲ ਸਮਰਥਨ ਨਾਲ |
| **ਪਾਇਥਨ** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ਪੈਟਰਨ ਵਰਤਦਾ ਪੂਰਾ ਪਾਇਥਨ ਕਲਾਇੰਟ |
| **ਰਸਟ** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio ਦੀ ਵਰਤੋਂ ਨਾਲ async ਆਪਰੇਸ਼ਨਾਂ ਲਈ ਪੂਰਾ ਰਸਟ ਕਲਾਇੰਟ |

ਹਰ ਪੂਰੇ ਉਦਾਹਰਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:
- ✅ **ਕਨੈਕਸ਼ਨ ਸਥਾਪਨਾ** ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ  
- ✅ **ਸਰਵਰ ਖੋਜ** (ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ, ਟੂਲ, ਸਰੋਤ, ਪ੍ਰਾਂਪਟ)  
- ✅ **ਕੈਲਕੁਲੇਟਰ ਓਪਰੇਸ਼ਨ** (ਜੋੜਨਾ, ਘਟਾਉਣਾ, ਗੁਣਾ, ਵੰਡਣਾ, ਮਦਦ)  
- ✅ **ਨਤੀਜੇ ਦੀ ਪ੍ਰੋਸੈਸਿੰਗ** ਅਤੇ ਫਾਰਮੈਟ ਕੀਤਾ ਆਉਟਪੁੱਟ  
- ✅ **ਵਿਆਪਕ ਗਲਤੀ ਸੰਭਾਲ**  
- ✅ **ਸਾਫ, ਦਸਤਾਵੇਜ਼ਬੱਧ ਕੋਡ** ਕਦਮ-ਦਰ-ਕਦਮ ਟਿੱਪਣੀਆਂ ਸਮੇਤ  

### ਪੂਰੇ ਉਦਾਹਰਣਾਂ ਨਾਲ ਸ਼ੁਰੂਆਤ

1. ਉੱਪਰ ਦਿੱਤੀ ਸੂਚੀ ਤੋਂ ਆਪਣੀ ਪਸੰਦੀਦਾ ਭਾਸ਼ਾ ਚੁਣੋ  
2. ਪੂਰੇ ਉਦਾਹਰਣ ਫਾਇਲ ਦਾ ਸਮੀਖਿਆ ਕਰੋ ਤਾਂ ਜੋ ਪੂਰੀ ਕਾਰਗੁਜ਼ਾਰੀ ਸਮਝ ਆ ਸਕੇ  
3. [`complete_examples.md`](./complete_examples.md) ਵਿੱਚ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੇ ਅਨੁਸਾਰ ਉਦਾਹਰਣ ਚਲਾਓ  
4. ਆਪਣੀ ਖਾਸ ਲੋੜ ਲਈ ਉਦਾਹਰਣ ਵਿੱਚ ਸੋਧ ਅਤੇ ਵਾਧਾ ਕਰੋ  

ਇਨ੍ਹਾਂ ਉਦਾਹਰਣਾਂ ਨੂੰ ਚਲਾਉਣ ਅਤੇ ਅਨੁਕੂਲਿਤ ਕਰਨ ਬਾਰੇ ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼ ਲਈ ਵੇਖੋ: **[📖 Complete Examples Documentation](./complete_examples.md)**  

### 💡 ਸੁਝਾਅ ਬਨਾਮ ਪੂਰੇ ਉਦਾਹਰਣ

| **ਸੁਝਾਅ ਫੋਲਡਰ** | **ਪੂਰੇ ਉਦਾਹਰਣ** |
|-----------------|-----------------|
| ਪੂਰੇ ਪ੍ਰੋਜੈਕਟ ਦਾ ਢਾਂਚਾ ਅਤੇ ਬਿਲਡ ਫਾਇਲਾਂ | ਸਿਰਫ ਇੱਕ ਫਾਇਲ ਵਾਲੇ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ |  
| ਡਿਪੈਂਡੇੰਸੀਜ਼ ਸਮੇਤ ਤਿਆਰ | ਕੇਂਦਰਿਤ ਕੋਡ ਉਦਾਹਰਣ |  
| ਪ੍ਰੋਡਕਸ਼ਨ ਵਰਗਾ ਸੈਟਅੱਪ | ਸਿੱਖਣ ਲਈ ਰেফਰੈਂਸ |  
| ਭਾਸ਼ਾ ਨਿਰਧਾਰਿਤ ਟੂਲਿੰਗ | ਬਹੁਭਾਸ਼ਾਈ ਤੁਲਨਾ |  

ਦੋਹਾਂ ਤਰੀਕਿਆਂ ਦੀ ਕੀਮਤ ਹੈ - ਪੂਰੇ ਪ੍ਰੋਜੈਕਟਾਂ ਲਈ **ਸੁਝਾਅ ਫੋਲਡਰ** ਅਤੇ ਸਿੱਖਣ ਅਤੇ ਰੁਜੂ ਕਰਨ ਲਈ **ਪੂਰੇ ਉਦਾਹਰਣ** ਦੀ ਵਰਤੋਂ ਕਰੋ।  

## ਮੁੱਖ ਬਿੰਦੂ

ਇਸ ਅਧਿਆਇ ਲਈ ਮੁੱਖ ਬਿੰਦੂ ਇਹ ਹਨ:  

- ਕਲਾਇੰਟ ਸਰਵਰ 'ਤੇ ਖੂਬੀਆਂ ਖੋਜਣ ਅਤੇ ਕਾਲ ਕਰਨ ਦੋਹਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।  
- ਇਹ ਆਪਣੇ ਆਪ ਸੇਵਾ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹਨ (ਇਸ ਅਧਿਆਇ ਵਾਂਗ) ਪਰ ਚੱਲ ਰਹੇ ਸਰਵਰਾਂ ਨਾਲ ਵੀ ਕਨੈਕਟ ਹੋ ਸਕਦੇ ਹਨ।  
- ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦਾ ਟੈਸਟ ਕਰਨ ਲਈ ਇਕ ਵਧੀਆ ਢੰਗ ਹੈ, ਜਿਵੇਂ ਕਿ ਪਿਛਲੇ ਅਧਿਆਇ ਵਿੱਚ ਵਰਣਿਤ ਇੰਸਪੈਕਟਰ ਵਰਗਾ ਵਿਕਲਪ।  

## ਵਾਧੂ ਸਰੋਤ

- [MCP ਵਿਚ ਕਲਾਇੰਟ ਬਣਾਉਣਾ](https://modelcontextprotocol.io/quickstart/client)  

## ਨਮੂਨੇ

- [ਜਾਵਾ ਕੈਲਕੁਲੇਟਰ](../samples/java/calculator/README.md)  
- [.Net ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)  
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/javascript/README.md)  
- [ਟਾਈਪਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/typescript/README.md)  
- [ਪਾਇਥਨ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/python)  
- [ਰਸਟ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/rust)  

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਡਿਸਕਲੇਮਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੇ ਜ਼ਰੀਏ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਪ੍ਰਯਾਸ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰੱਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਸਰਵੋਤਮ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਵਰਣਾਂ ਲਈ ਜਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->