# ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਕਲਾਇੰਟ ਉਹ ਕਸਟਮ ਐਪਲੀਕੇਸ਼ਨ ਜਾਂ ਸਕ੍ਰਿਪਟ ਹੁੰਦੇ ਹਨ ਜੋ ਸਿੱਧੇ MCP ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਕਰਦੇ ਹਨ ਤਾਂ ਜੋ ਸਰੋਤਾਂ, ਟੂਲਾਂ ਅਤੇ ਪ੍ਰੋੰਪਟਾਂ ਦੀ ਬੇਨਤੀ ਕੀਤੀ ਜਾ ਸਕੇ। ਇੰਸਪੈਕਟਰ ਟੂਲ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੇ ਵਿਰੁੱਧ, ਜੋ ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਲਈ ਇੱਕ ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਆਪਣਾ ਕਲਾਇੰਟ ਲਿਖਣ ਨਾਲ ਪ੍ਰੋਗਰਾਮਮੈਟਿਕ ਅਤੇ ਆਟੋਮੈਟਿਕ ਸੰਚਾਰ ਸੰਭਵ ਹੁੰਦਾ ਹੈ। ਇਹ ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਆਪਣੇ ਵਰਕਫਲੋ ਵਿੱਚ MCP ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਸ਼ਾਮਲ ਕਰਨ, ਕੰਮਾਂ ਨੂੰ ਆਟੋਮੈਟ ਕਰਨ ਅਤੇ ਵਿਸ਼ੇਸ਼ ਜ਼ਰੂਰਤਾਂ ਲਈ ਕਸਟਮ ਹੱਲ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## ਝਲਕ

ਇਹ ਪਾਠ MCP (ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ) ਪਰਿਵਾਰ ਵਿੱਚ ਕਲਾਇੰਟਾਂ ਦੇ ਅਵਧਾਰਨਾ ਨਾਲ ਜਾਣੂ ਕਰਵਾਉਂਦਾ ਹੈ। ਤੁਸੀਂ ਸਿੱਖੋਗੇ ਕਿ ਆਪਣਾ ਕਲਾਇੰਟ ਕਿਵੇਂ ਲਿਖਣਾ ਹੈ ਅਤੇ ਇਸਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਕਿਵੇਂ ਜੋੜਨਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- ਸਮਝੋ ਕਿ ਕਲਾਇੰਟ ਕੀ ਕਰ ਸਕਦਾ ਹੈ।
- ਆਪਣਾ ਕਲਾਇੰਟ ਲਿਖੋ।
- ਕਲਾਇੰਟ ਨੂੰ MCP ਸਰਵਰ ਨਾਲ ਜੋੜੋ ਅਤੇ ਟੈਸਟ ਕਰੋ ਤਾਂ ਕਿ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਇਹ ਉਮੀਦਾਂ ਦੇ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦਾ ਹੈ।

## ਕਲਾਇੰਟ ਲਿਖਣ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ?

ਕਲਾਇੰਟ ਲਿਖਣ ਲਈ, ਤੁਹਾਨੂੰ ਇਹ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇਗੀ:

- **ਸਹੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ**। ਤੁਸੀਂ ਪਹਿਲਾਂ ਵਰਤੀ ਗਈ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋਗੇ, ਸਿਰਫ਼ ਵੱਖ-ਵੱਖ ਬਣਤਰਾਂ ਨਾਲ।
- **ਕਲਾਇੰਟ ਬਣਾਓ**। ਇਸ ਵਿੱਚ ਇੱਕ ਕਲਾਇੰਟ ਇੰਸਟੈਂਸ ਬਣਾਉਣਾ ਅਤੇ ਇਸਨੂੰ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਮੋਡ ਨਾਲ ਜੋੜਨਾ ਸ਼ਾਮਲ ਹੋਵੇਗਾ।
- **ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਦਾ ਫੈਸਲਾ ਕਰੋ**। ਤੁਹਾਡੇ MCP ਸਰਵਰ ਵਿੱਚ ਸਰੋਤ, ਟੂਲ ਅਤੇ ਪ੍ਰੋੰਪਟ ਹਨ, ਤੁਹਾਨੂੰ ਇਹ ਫੈਸਲਾ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਕਿ ਕਿਹੜਾ ਸੂਚੀਬੱਧ ਕਰਨਾ ਹੈ।
- **ਕਲਾਇੰਟ ਨੂੰ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ**। ਜਦੋਂ ਤੁਹਾਨੂੰ ਸਰਵਰ ਦੀ ਸਮਰੱਥਾਵਾਂ ਦਾ ਪਤਾ ਲੱਗ ਜਾਵੇ, ਤਾਂ ਤੁਹਾਨੂੰ ਇਸਨੂੰ ਆਪਣੇ ਹੋਸਟ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਤਾਂ ਜੋ ਜਦੋਂ ਕੋਈ ਯੂਜ਼ਰ ਪ੍ਰੋੰਪਟ ਜਾਂ ਹੋਰ ਕਮਾਂਡ ਟਾਈਪ ਕਰੇ, ਤਾਂ ਸੰਬੰਧਿਤ ਸਰਵਰ ਫੀਚਰ ਚਾਲੂ ਹੋਵੇ।

ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਉੱਚ ਪੱਧਰ 'ਤੇ ਸਮਝ ਗਏ ਕਿ ਅਸੀਂ ਕੀ ਕਰਨ ਜਾ ਰਹੇ ਹਾਂ, ਆਓ ਅਗਲੇ ਹਿੱਸੇ ਵਿੱਚ ਇੱਕ ਉਦਾਹਰਨ ਦੇਖੀਏ।

### ਇੱਕ ਉਦਾਹਰਨ ਕਲਾਇੰਟ

ਆਓ ਇਸ ਉਦਾਹਰਨ ਕਲਾਇੰਟ ਨੂੰ ਦੇਖੀਏ:

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕੀਤਾ।
- ਇੱਕ ਕਲਾਇੰਟ ਇੰਸਟੈਂਸ ਬਣਾਇਆ ਅਤੇ ਇਸਨੂੰ ਟ੍ਰਾਂਸਪੋਰਟ ਲਈ stdio ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜੋੜਿਆ।
- ਪ੍ਰੋੰਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਚਾਲੂ ਕੀਤਾ।

ਇਹ ਹੈ, ਇੱਕ ਕਲਾਇੰਟ ਜੋ MCP ਸਰਵਰ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦਾ ਹੈ।

ਆਓ ਅਗਲੇ ਅਭਿਆਸ ਹਿੱਸੇ ਵਿੱਚ ਹਰ ਕੋਡ ਸਨਿੱਪਟ ਨੂੰ ਵਿਖੰਡਿਤ ਕਰਕੇ ਸਮਝਣ ਲਈ ਸਮਾਂ ਲਵਾਂ।

## ਅਭਿਆਸ: ਕਲਾਇੰਟ ਲਿਖਣਾ

ਜਿਵੇਂ ਕਿ ਉਪਰੋਕਤ ਕਿਹਾ ਗਿਆ ਹੈ, ਆਓ ਕੋਡ ਨੂੰ ਸਮਝਾਉਣ ਲਈ ਸਮਾਂ ਲਵਾਂ, ਅਤੇ ਜੇ ਤੁਸੀਂ ਚਾਹੋ ਤਾਂ ਕੋਡ ਨਾਲ ਅਭਿਆਸ ਕਰੋ।

### -1- ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ

ਆਓ ਜਿਨ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਜ਼ਰੂਰਤ ਹੈ ਉਹਨਾਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰੀਏ। ਸਾਨੂੰ ਇੱਕ ਕਲਾਇੰਟ ਅਤੇ ਚੁਣੇ ਗਏ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ stdio ਲਈ ਹਵਾਲੇ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇਗੀ। stdio ਉਹ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜੋ ਤੁਹਾਡੇ ਸਥਾਨਕ ਮਸ਼ੀਨ 'ਤੇ ਚਲਾਉਣ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। SSE ਇੱਕ ਹੋਰ ਟ੍ਰਾਂਸਪੋਰਟ ਪ੍ਰੋਟੋਕੋਲ ਹੈ ਜਿਸਨੂੰ ਅਸੀਂ ਭਵਿੱਖ ਦੇ ਅਧਿਆਇ ਵਿੱਚ ਦਿਖਾਵਾਂਗੇ ਪਰ ਇਹ ਤੁਹਾਡਾ ਦੂਜਾ ਵਿਕਲਪ ਹੈ। ਫਿਲਹਾਲ, ਆਓ stdio ਨਾਲ ਜਾਰੀ ਰੱਖੀਏ।

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
using ModelContextProtocol.Protocol.Transport;
```

#### ਜਾਵਾ

ਜਾਵਾ ਲਈ, ਤੁਸੀਂ ਪਿਛਲੇ ਅਭਿਆਸ ਤੋਂ MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਵਾਲਾ ਕਲਾਇੰਟ ਬਣਾਉਗੇ। ਜਾਵਾ ਸਪ੍ਰਿੰਗ ਬੂਟ ਪ੍ਰੋਜੈਕਟ ਸਟ੍ਰਕਚਰ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) ਤੋਂ, `SDKClient` ਨਾਮਕ ਇੱਕ ਨਵੀਂ ਜਾਵਾ ਕਲਾਸ ਬਣਾਓ `src/main/java/com/microsoft/mcp/sample/client/` ਫੋਲਡਰ ਵਿੱਚ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੇ ਇੰਪੋਰਟ ਸ਼ਾਮਲ ਕਰੋ:

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

ਤੁਹਾਨੂੰ ਆਪਣੇ `Cargo.toml` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ Dependencies ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇਗੀ।

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

ਇਸ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਆਪਣੇ ਕਲਾਇੰਟ ਕੋਡ ਵਿੱਚ ਜ਼ਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰ ਸਕਦੇ ਹੋ।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ਆਓ ਇੰਸਟੈਂਸ਼ਨ ਵੱਲ ਵਧੀਏ।

### -2- ਕਲਾਇੰਟ ਅਤੇ ਟ੍ਰਾਂਸਪੋਰਟ ਨੂੰ ਇੰਸਟੈਂਸ਼ੀਏਟ ਕਰਨਾ

ਸਾਨੂੰ ਟ੍ਰਾਂਸਪੋਰਟ ਅਤੇ ਆਪਣੇ ਕਲਾਇੰਟ ਦਾ ਇੱਕ ਇੰਸਟੈਂਸ ਬਣਾਉਣ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇਗੀ:

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- stdio ਟ੍ਰਾਂਸਪੋਰਟ ਇੰਸਟੈਂਸ ਬਣਾਇਆ। ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ ਕਮਾਂਡ ਅਤੇ ਆਰਗਸ ਨੂੰ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਸਰਵਰ ਨੂੰ ਕਿਵੇਂ ਲੱਭਣਾ ਅਤੇ ਸ਼ੁਰੂ ਕਰਨਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਕੁਝ ਹੈ ਜੋ ਅਸੀਂ ਕਲਾਇੰਟ ਬਣਾਉਣ ਸਮੇਂ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇਗੀ।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ਕਲਾਇੰਟ ਨੂੰ ਇੱਕ ਨਾਮ ਅਤੇ ਵਰਜਨ ਦੇ ਕੇ ਇੰਸਟੈਂਸ਼ੀਏਟ ਕੀਤਾ।

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

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

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
        
        // Your client logic goes here
    }
}
```

#### ਰਸਟ

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- ਸਰਵਰ ਫੀਚਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ

ਹੁਣ, ਸਾਡੇ ਕੋਲ ਇੱਕ ਕਲਾਇੰਟ ਹੈ ਜੋ ਕਨੈਕਟ ਕਰ ਸਕਦਾ ਹੈ ਜੇਕਰ ਪ੍ਰੋਗਰਾਮ ਚਲਾਇਆ ਜਾਵੇ। ਹਾਲਾਂਕਿ, ਇਹ ਅਸਲ ਵਿੱਚ ਆਪਣੇ ਫੀਚਰਾਂ ਦੀ ਸੂਚੀ ਨਹੀਂ ਬਣਾਉਂਦਾ, ਇਸ ਲਈ ਆਓ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਇਹ ਕਰੀਏ:

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### ਪਾਇਥਨ

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

#### ਜਾਵਾ

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

#### ਰਸਟ

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ਫੀਚਰਾਂ ਨੂੰ ਚਾਲੂ ਕਰਨਾ

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

#### ਪਾਇਥਨ

```python
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

#### .NET

```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ਜਾਵਾ

```java
// Call various calculator tools
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

#### ਰਸਟ

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

### -5- ਕਲਾਇੰਟ ਚਲਾਉਣਾ

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### ਪਾਇਥਨ

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ਜਾਵਾ

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### ਰਸਟ

```bash
cargo fmt
cargo run
```

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ, ਤੁਸੀਂ ਜੋ ਸਿੱਖਿਆ ਹੈ ਉਸਦਾ ਪ੍ਰਯੋਗ ਕਰਦੇ ਹੋਏ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਉਗੇ।

### ਟਾਈਪਸਕ੍ਰਿਪਟ

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

### ਰਸਟ

## ਹੱਲ

### 📁 ਹੱਲ ਦੀ ਬਣਤਰ

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

### 🚀 ਹਰੇਕ ਹੱਲ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ

### 📖 ਹੱਲ ਦੀ ਵਰਤੋਂ

```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

## 🎯 ਪੂਰੇ ਉਦਾਹਰਨ

### ਉਪਲਬਧ ਪੂਰੇ ਉਦਾਹਰਨ

| ਭਾਸ਼ਾ | ਫਾਇਲ | ਵੇਰਵਾ |
|----------|------|-------------|
| **ਜਾਵਾ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਦੇ ਹੋਏ ਪੂਰਾ ਜਾਵਾ ਕਲਾਇੰਟ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ਟ੍ਰਾਂਸਪੋਰਟ ਵਰਤਦੇ ਹੋਏ ਪੂਰਾ C# ਕਲਾਇੰਟ |
| **ਟਾਈਪਸਕ੍ਰਿਪਟ** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP ਪ੍ਰੋਟੋਕੋਲ ਸਹਾਇਤਾ ਨਾਲ ਪੂਰਾ ਟਾਈਪਸਕ੍ਰਿਪਟ ਕਲਾਇੰਟ |
| **ਪਾਇਥਨ** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ਪੈਟਰਨ ਵਰਤਦੇ ਹੋਏ ਪੂਰਾ ਪਾਇਥਨ ਕਲਾਇੰਟ |
| **ਰਸਟ** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | async ਕਾਰਵਾਈਆਂ ਲਈ Tokio ਵਰਤਦੇ ਹੋਏ ਪੂਰਾ ਰਸਟ ਕਲਾਇੰਟ |
ਹਰ ਪੂਰੇ ਉਦਾਹਰਨ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:

- ✅ **ਕਨੈਕਸ਼ਨ ਸਥਾਪਨਾ** ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ
- ✅ **ਸਰਵਰ ਖੋਜ** (ਟੂਲ, ਸਰੋਤ, ਪ੍ਰੇਰਨਾ ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ)
- ✅ **ਕੈਲਕੂਲੇਟਰ ਕਾਰਵਾਈਆਂ** (ਜੋੜ, ਘਟਾਉ, ਗੁਣਾ, ਭਾਗ, ਮਦਦ)
- ✅ **ਨਤੀਜਾ ਪ੍ਰਕਿਰਿਆ** ਅਤੇ ਫਾਰਮੈਟ ਕੀਤਾ ਆਉਟਪੁੱਟ
- ✅ **ਵਿਆਪਕ ਗਲਤੀ ਸੰਭਾਲ**
- ✅ **ਸਾਫ, ਦਸਤਾਵੇਜ਼ੀਕ੍ਰਿਤ ਕੋਡ** ਸਟੈਪ-ਬਾਈ-ਸਟੈਪ ਟਿੱਪਣੀਆਂ ਨਾਲ

### ਪੂਰੇ ਉਦਾਹਰਨਾਂ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰਨਾ

1. **ਆਪਣੀ ਪਸੰਦੀਦਾ ਭਾਸ਼ਾ ਚੁਣੋ** ਉਪਰੋਕਤ ਸਾਰਣੀ ਵਿੱਚੋਂ
2. **ਪੂਰੇ ਉਦਾਹਰਨ ਫਾਈਲ ਦੀ ਸਮੀਖਿਆ ਕਰੋ** ਪੂਰੀ ਕਾਰਵਾਈ ਨੂੰ ਸਮਝਣ ਲਈ
3. **ਉਦਾਹਰਨ ਚਲਾਓ** ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ [`complete_examples.md`](./complete_examples.md) ਵਿੱਚ ਦਿੱਤੀ ਗਈ
4. **ਉਦਾਹਰਨ ਨੂੰ ਸੋਧੋ ਅਤੇ ਵਧਾਓ** ਆਪਣੇ ਵਿਸ਼ੇਸ਼ ਉਪਯੋਗ ਲਈ

ਇਨ੍ਹਾਂ ਉਦਾਹਰਨਾਂ ਨੂੰ ਚਲਾਉਣ ਅਤੇ ਕਸਟਮਾਈਜ਼ ਕਰਨ ਬਾਰੇ ਵਿਸਤ੍ਰਿਤ ਦਸਤਾਵੇਜ਼ੀਕਰਨ ਲਈ, ਵੇਖੋ: **[📖 ਪੂਰੇ ਉਦਾਹਰਨਾਂ ਦੀ ਦਸਤਾਵੇਜ਼ੀਕਰਨ](./complete_examples.md)**

### 💡 ਹੱਲ ਵਿਰੁੱਧ ਪੂਰੇ ਉਦਾਹਰਨ

| **ਹੱਲ ਫੋਲਡਰ** | **ਪੂਰੇ ਉਦਾਹਰਨ** |
|--------------------|--------------------- |
| ਬਿਲਡ ਫਾਈਲਾਂ ਨਾਲ ਪੂਰੀ ਪ੍ਰੋਜੈਕਟ ਸੰਰਚਨਾ | ਸਿੰਗਲ-ਫਾਈਲ ਕਾਰਵਾਈਆਂ |
| ਨਿਰਭਰਤਾਵਾਂ ਨਾਲ ਤਿਆਰ-ਚਲਾਉਣ ਯੋਗ | ਕੇਵਲ ਕੋਡ ਉਦਾਹਰਨਾਂ |
| ਉਤਪਾਦਨ-ਜੈਸਾ ਸੈਟਅਪ | ਸਿੱਖਣ ਲਈ ਸੰਦਰਭ |
| ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼ ਟੂਲਿੰਗ | ਭਾਸ਼ਾ-ਅਨੁਸਾਰ ਤੁਲਨਾ |

ਦੋਵੇਂ ਪਹੁੰਚਾਂ ਕੀਮਤੀ ਹਨ - **ਹੱਲ ਫੋਲਡਰ** ਨੂੰ ਪੂਰੇ ਪ੍ਰੋਜੈਕਟਾਂ ਲਈ ਵਰਤੋ ਅਤੇ **ਪੂਰੇ ਉਦਾਹਰਨ** ਸਿੱਖਣ ਅਤੇ ਸੰਦਰਭ ਲਈ।

## ਮੁੱਖ ਸਿੱਖਣ

ਇਸ ਅਧਿਆਇ ਲਈ ਮੁੱਖ ਸਿੱਖਣ ਇਹ ਹਨ ਕਿ ਕਲਾਇੰਟ ਬਾਰੇ:

- ਸਰਵਰ 'ਤੇ ਫੀਚਰਾਂ ਦੀ ਖੋਜ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।
- ਜਦੋਂ ਇਹ ਖੁਦ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ ਤਾਂ ਸਰਵਰ ਨੂੰ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹੈ (ਜਿਵੇਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ) ਪਰ ਕਲਾਇੰਟ ਚੱਲ ਰਹੇ ਸਰਵਰਾਂ ਨਾਲ ਵੀ ਜੁੜ ਸਕਦੇ ਹਨ।
- ਸਰਵਰ ਦੀ ਸਮਰਥਾ ਦੀ ਜਾਂਚ ਕਰਨ ਦਾ ਇਹ ਇੱਕ ਸ਼ਾਨਦਾਰ ਤਰੀਕਾ ਹੈ, ਜਿਵੇਂ ਪਿਛਲੇ ਅਧਿਆਇ ਵਿੱਚ ਵਰਣਨ ਕੀਤਾ ਗਿਆ ਸੀ।

## ਵਾਧੂ ਸਰੋਤ

- [MCP ਵਿੱਚ ਕਲਾਇੰਟ ਬਣਾਉਣਾ](https://modelcontextprotocol.io/quickstart/client)

## ਨਮੂਨੇ

- [ਜਾਵਾ ਕੈਲਕੂਲੇਟਰ](../samples/java/calculator/README.md)
- [.Net ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੈਲਕੂਲੇਟਰ](../samples/javascript/README.md)
- [ਟਾਈਪਸਕ੍ਰਿਪਟ ਕੈਲਕੂਲੇਟਰ](../samples/typescript/README.md)
- [ਪਾਇਥਨ ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/python)
- [ਰਸਟ ਕੈਲਕੂਲੇਟਰ](../../../../03-GettingStarted/samples/rust)

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ](../03-llm-client/README.md)

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀਅਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।