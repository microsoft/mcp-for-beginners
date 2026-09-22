# ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸುವುದು

ಕ್ಲೈಂಟ್‌ಗಳು ಕಸ್ಟಮ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳಾಗಿದ್ದು, MCP ಸರ್ವರ್‌ಗೆ ನೇರವಾಗಿ ಸಂವಹನ ಮಾಡಿ ಸಂಪನ್ಮೂಲಗಳು, ಉಪಕರಣಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ವಿನಂತಿಸುತ್ತವೆ. ಸರ್ವರ್‌ನೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಗ್ರಾಫಿಕಲ್ ಇಂಟರ್ಫೇಸ್ ನೀಡುವ ಇನ್ಸ್pector ಉಪಕರಣವನ್ನು ಬಳಸುವುದನ್ನು ಬಿಟ್ಟು ನಿಮ್ಮತಮ ಕ್ಲೈಂಟ್ ಬರೆಯುವುದರಿಂದ ಪ್ರೋಗ್ರಾಮಾಟಿಕ್ ಮತ್ತು ಸ್ವಯಂಚಾಲಿತ ಸಂವಹನ ಸಾಧ್ಯವಾಗುತ್ತದೆ. ಇದರಿಂದ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರು ತಮ್ಮ ಕಾರ್ಯಪದ್ಯದಲ್ಲಿ MCP ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಂಯೋಜಿಸಬಹುದು, ಕಾರ್ಯಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಬಹುದು, ಮತ್ತು ನಿರ್ದಿಷ್ಟ ಅಗತ್ಯಗಳಿಗೆ ತಕ್ಕಂತೆ ಕಸ್ಟಮ್ ಪರಿಹಾರಗಳನ್ನು ರಚಿಸಬಹುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠವು Model Context Protocol (MCP) ಪರಿಕರ ವ್ಯವಸ್ಥೆಯೊಳಗಿನ ಕ್ಲೈಂಟ್‌ಗಳ ಪರಿಕಲ್ಪನೆಯನ್ನು ಪರಿಚಯಿಸುತ್ತದೆ. ನೀವು ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಅನ್ನು ಬರೆಯುವುದು ಮತ್ತು ಅದನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಗೊಳಿಸುವುದನ್ನು ಕಲಿತೀರಿ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಕ್ಲೈಂಟ್ ಏನು ಮಾಡಲು ಸಾಧ್ಯವೋ ಅದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಬರೆಯುವುದು.
- MCP ಸರ್ವರ್ ಜೊತೆಗೆ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂಪರ್ಕಿಸಿ ಪರೀಕ್ಷಿಸುವುದು, ಸರ್ವರ್ ನಿರೀಕ್ಷೆಯಂತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳುವುದು.

## ಕ್ಲೈಂಟ್ ಬರೆಯಲು ಏನು ಬೇಕು?

ಕ್ಲೈಂಟ್ ಬರೆಯಲು, ನೀವು ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಬೇಕಾಗುತ್ತದೆ:

- **ಸರಿಯಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದುಮಾಡಿಕೊಳ್ಳುವುದು**. ನೀವು ಹಿಂದಿನಂತಹಲೈಬ್ರರಿಯನ್ನು ಬಳಸುತ್ತೀರಿ, ಬೇರೆ ರಚನೆಗಳು ಮಾತ್ರ.
- **ಕ್ಲೈಂಟ್ ಉದ್ದೇಶಿಸುವುದು**. ಇದರಲ್ಲಿ ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆ ರಚಿಸಿ ಆಯ್ಕೆಯಾದ ಸಾರಿಗೆ ವಿಧಾನಕ್ಕೆ ಸಂಪರ್ಕಗೊಳಿಸುವುದು ಒಳಗೊಂಡಿದೆ.
- **ಯಾವ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬೇಕು ಎಂದು ನಿರ್ಧರಿಸುವುದು**. ನಿಮ್ಮ MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಸಂಪನ್ಮೂಲಗಳು, ಉಪಕರಣಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳಿವೆ, ಯಾವುವನ್ನು ಪಟ್ಟಿ ಮಾಡాలో ನಿರ್ಧರಿಸಬೇಕು.
- **ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಸಂಯೋಜಿಸುವುದು**. ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತಿಳಿದುಕೊಂಡ ನಂತರ, ನಿಮ್ಮ ಹೋಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ನಿಗೆ ಇದನ್ನು ಸಂಯೋಜಿಸಬೇಕು ಹಾಗಾಗಿ ಬಳಕೆದಾರರು ಪ್ರಾಂಪ್ಟ್ ಅಥವಾ ಆಜ್ಞೆಗಳನ್ನು ಟೈಪ್ ಮಾಡಿದಾಗ, ಅದರ ಅನುಗುಣವಾಗಿ ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯಗಳು ಕರೆಸಲ್ಪಡುವಂತೆ ಮಾಡಬೇಕು.

ಈಗ ನಾವು ಎತ್ತರ ಮಟ್ಟದಲ್ಲಿ ಏನು ಮಾಡಬೇಕೆಂದು ತಿಳಿದುಕೊಂಡಿದ್ದೇವೆ, ಮುಂದಿನ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ.

### ಒಂದು ಉದಾಹರಣೆಯ ಕ್ಲೈಂಟ್

ಈ ಉದಾಹರಣೆಯ ಕ್ಲೈಂಟ್ ಅನ್ನು ನೋಡೋಣ:

### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

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

// ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಪಟ್ಟಿ
const prompts = await client.listPrompts();

// ಒಂದು ಪ್ರಾಂಪ್ಟ್ ಪಡೆಯಿರಿ
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// ಸಂಪನ್ಮೂಲಗಳ ಪಟ್ಟಿ
const resources = await client.listResources();

// ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಿ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದುಮಾಡಿದೆವು
- ಕ್ಲೈಂಟ್ ಇದರ उदाहरणವನ್ನು ಸೃಷ್ಟಿಸಿ stdio ಸಾರಿಗೆಗೆ ಸಂಪರ್ಕಗೊಳಿಸಿದೆವು.
- ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿಮಾಡಿ ಅವುಗಳನ್ನು ಕರೆಸಿದೆವು.

ಹೀಗಾಗಿ ನೀವು ಕಾಣುತ್ತೀರಿ, ಸಂವಹನಗೊಳ್ಳುವ MCP ಸರ್ವರ್‌ಗೆ ಮಾತನಾಡಬಲ್ಲ ಕ್ಲೈಂಟ್ ಇದೆ.

ಮುಂದಿನ ವ್ಯಾಯಾಮ ವಿಭಾಗದಲ್ಲಿ ನಾವು ಸಮಯ ತೆಗೆದು ಪ್ರತಿ ಕೋಡ್ ತುಣುಕವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ ತಿಳಿಸುವೆವು.

## ವ್ಯಾಯಾಮ: ಕ್ಲೈಂಟ್ ಬರೆಯುವುದು

ಮೇಲ್ಕಂಡದರಂತೆ, ಕೋಡ್ ವಿವರಿಸಲು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳೋಣ ಮತ್ತು ಇಚ್ಛಿಸುವರೆಂದು ಕೋಡ್ ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡಬಹುದು.

### -1- ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುವುದು

ನಾವು ಬೇಕಾಗುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳೋಣ. ನಾವು ಕ್ಲೈಂಟಿಗೂ ಮತ್ತು ನಮ್ಮ ಆಯ್ಕೆಮಾಡಿದ ಸಾರಿಗೆ ಪ್ರೋಟೋಕಾಲ್, stdioಗೆ ಉಲ್ಲೇಖ ಬೇಕಾಗುತ್ತದೆ. stdio ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರದಲ್ಲಿ ಓಡುವುದಕ್ಕಾಗಿ ಸಿದ್ಧಪಡಿಸಿರುವ ಪ್ರೋಟೋಕಾಲ್. SSE ಎಂಬ ಇನ್ನೊಂದು ಸಾರಿಗೆ ಪ್ರೋಟೋಕಾಲ್ ನಾಳೆ ಅಧ್ಯಾಯಗಳಲ್ಲಿ ತೋರಿಸಲಾಗುತ್ತದೆ, ಅದು ನಿಮ್ಮ ಇನ್ನೊಂದು ಆಯ್ಕೆ. ಈಗ though, stdio ಜೊತೆ ಮುಂದುವರಿಯೋಣ.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### ಪೈಥನ್

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

#### ಜಾವಾ

ಜಾವಾ ಗಾಗಿ, ನೀವು ಹಿಂದಿನ ವ್ಯಾಯಾಮದಿಂದ MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವ ಕ್ಲೈಂಟ್ ರಚಿಸುವಿರಿ. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) ನಂತರ ಜಾವಾ ಸ್ಪ್ರಿಂಗ್ ಬುಟ್ ಯೋಜನೆಯ ರಚನೆಯನ್ನು ಉಪಯೋಗಿಸಿ, ಹೊಸ ಜಾವಾ ಕ್ಲಾಸ್ `SDKClient` ಅನ್ನು `src/main/java/com/microsoft/mcp/sample/client/` ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಆಮದುಗಳನ್ನು ಸೇರಿಸಿ:

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

#### ರಸ್ಟ್

ನಿಮ್ಮ `Cargo.toml` ಫೈಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಬೇಕು.

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

ಅಲ್ಲಿ, ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡಿನಲ್ಲಿ ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಬಹುದು.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ಈಗ ನಾವು ಉದ್ಧೇಶಿಸುವುದಕ್ಕೆ ಮುಂದಾಗೋಣ.

### -2- ಕ್ಲೈಂಟ್ ಮತ್ತು ಸಾರಿಗೆ ಉದ್ಧೇಶಿಸುವುದು

ನಾವು ಸಾರಿಗೆ ಮತ್ತು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಎರಡರ ಉದಾಹರಣೆಗಳನ್ನು ರಚಿಸಬೇಕಾಗುತ್ತದೆ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

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

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- stdio ಸಾರಿಗೆ ಉದಾಹರಣೆ ರಚಿಸಿದೆವು. ಇದು ಸರ್ವರ್ ಕಂಡುಹಿಡಿಯುವುದು ಮತ್ತು ಪ್ರಾರಂಭಿಸುವ ನಿಯತಾಂಕಗಳಾದ ಕಮಾಂಡ್ ಮತ್ತು ಆರ್ಗ್ಸ್ ಅನ್ನು ವಿವರಿಸುತ್ತದೆ, ನಾವು ಕ್ಲೈಂಟ್ ರಚಿಸುವಾಗ ಇದನ್ನು ಮಾಡಬೇಕಾಗುತ್ತದೆ.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೆಸರಿನಲ್ಲಿ ಮತ್ತು ಆವೃತ್ತಿಯಲ್ಲಿ ಉದ್ಧೇಶಿಸಿದೆವು.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ಕ್ಲೈಂಟ್ ಆಯ್ಕೆಯಾದ ಸಾರಿಗೆಗೆ ಸಂಪರ್ಕಗೊಳಿಸಿದೆವು.

    ```typescript
    await client.connect(transport);
    ```

#### ಪೈಥನ್

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪರಿಮಾಣಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಚಾಲನೆಯೋಗ್ಯ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ ಅರ್ಗ್ಯೂಮೆಂಟ್ಸ್
    env=None,  # ಐಚ್ಛಿಕ ಪರಿಸರ ಬದಲಾಗುವ ಮಾಪಕಗಳು
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ಸಂಪರ್ಕವನ್ನು ಆರಂಭಿಸಿ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- ಸರ್ವರ್ ನಿಯತಾಂಕಗಳ ವಸ್ತುವನ್ನು ಉದ್ಧೇಶಿಸಿದೆವು, ಇದನ್ನು ಬಳಸಿಕೊಂಡು ನಾವು ಸರ್ವರ್ ಚಾಲನೆ ಮಾಡಿ, ಅದಕ್ಕೆ ನಮ್ಮ ಕ್ಲೈಂಟ್ ಸಂಪರ್ಕಗೊಳಿಸಬಹುದು.
- `run` ಎಂಬ ವಿಧಾನವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದೆವು, ಇದು `stdio_client` ಅವರನ್ನು ಕರೆದು ಕ್ಲೈಂಟ್ ಸೆಷನ್ ಪ್ರಾರಂಭಿಸುತ್ತದೆ.
- `asyncio.run` ಗೆ `run` ವಿಧಾನವನ್ನು ಒದಗಿಸುವ ಪ್ರವೇಶಬಿಂದು ಸೃಷ್ಟಿಸಿದೆವು.

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

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದೆವು.
- stdio ಸಾರಿಗೆ ರಚಿಸಿ `mcpClient` ಎನ್ನುವ ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸಿದೆವು. ಇದರ ಮೂಲಕ ನಾವು MCP ಸರ್ವರ್‌ನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿಮಾಡಿ ಕರೆಸಬಹುದು.

ಗಮನಿಸಿ, "Arguments" ನಲ್ಲಿ ನೀವು *.csproj* ಅಥವಾ ನಿರ್ಗಮನ ಫೈಲನ್ನು ಸೂಚಿಸಬಹುದು.

#### ಜಾವಾ

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
        
        // ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ಲಾಜಿಕ್ ಇಲ್ಲಿ ಹೋಗುತ್ತದೆ
    }
}
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- `http://localhost:8080` ಗೆ ಸೂಚಿಸುತ್ತಿರುವ SSE ಸಾರಿಗೆ ಒದಗಿಸಿ ಮುಖ್ಯ ವಿಧಾನವನ್ನು ರಚಿಸಿದೆವು. ಇಲ್ಲಿ ನಮ್ಮ MCP ಸರ್ವರ್ ಓಡುತ್ತಿದೆ.
- ಸಾರಿಗೆ ಅನ್ನು ನಿರ್ಮಾಪಕ ಪ್ಯಾರಾಮೀಟರ್ ಆಗಿ ತೆಗೆದುಕೊಳ್ಳುವ ಕ್ಲೈಂಟ್ ವರ್ಗವನ್ನು ರಚಿಸಿದೆವು.
- `run` ವಿಧಾನದಲ್ಲಿ, ಸಾರಿಗೆ ಬಳಸಿ ಸಿಂಕ್ರೊನಸ್ MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿ ಸಂಪರ್ಕವನ್ನು ಆರಂಭಿಸಿದೆವು.
- Java Spring Boot MCP ಸರ್ವರ್‌ಗಳಿಗೆ ಹೊಂದಿಕೊಂಡ ಹಿHTTP ಆಧಾರಿತ ಸಂವಹನಕ್ಕೆ ಸೂಕ್ತವಾದ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್‌ಗಳು) ಸಾರಿಗೆ ಬಳಸಿದೆವು.

#### ರಸ್ಟ್

ಈ ರಸ್ಟ್ ಕ್ಲೈಂಟ್ assumes ಸರ್ವರ್ ಸಮಾನಸ್ಥರಿ ಯೋಜನೆಯಾಗಿದೆ, ಅದರ ಹೆಸರು "calculator-server" ಮತ್ತು ಅದೇ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇದೆ. ಕೆಳಗಿನ ಕೋಡ್ ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸಿ ಅದಕ್ಕೆ ಸಂಪರ್ಕಗೊಳಿಸುತ್ತದೆ.

```rust
async fn main() -> Result<(), RmcpError> {
    // ಸರ್ವರ್ ಅದೇ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ "calculator-server" ಎಂಬ ಸಹೋದರ ಪ್ರಾಜೆಕ್ಟ್ ಎಂದು ಊಹಿಸಿ
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

    // TODO: ಪ್ರಾರಂಭಿಸು

    // TODO: ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡು

    // TODO: arguments = {"a": 3, "b": 2} ಆಗಿರುವ add tool ಅನ್ನು ಕರೆಮಾಡು

    client.cancel().await?;
    Ok(())
}
```

### -3- ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿಮಾಡುವುದು

ಈಗ, ನಮ್ಮ ಬಳಿ ಪ್ರೋಗ್ರಾಮ್ ಓಡಿಸಿದಾಗ ಸಂಪರ್ಕಗೊಳ್ಳಬಹುದಾದ ಕ್ಲೈಂಟ್ ಇದೆ. ಆದರೆ ಅದು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ತೋರಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ಅದನ್ನು ಮುಂದುವರೆಸೋಣ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
// ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡು
const prompts = await client.listPrompts();

// ಸಂಪನ್ಮೂಲಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡು
const resources = await client.listResources();

// ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡು
const tools = await client.listTools();
```

#### ಪೈಥನ್

```python
# ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳ ಪಟ್ಟಿಯನ್ನು ತೋರಿಸಿ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ತೋರಿಸಿ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ಇಲ್ಲಿ ನಾವು ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳನ್ನು `list_resources()` ಮತ್ತು ಉಪಕರಣಗಳನ್ನು `list_tools` ಹಾಗೂ ಅತ никогдаintha ಕ್ರಿಯೆಯಲ್ಲೂ ಕೂಡ ಪ್ರಕಟಿಸುತ್ತೇವೆ.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ಮೇಲಿನ ಉದಾಹರಣೆಯು ಸರ್ವರ್‌ನ ಉಪಕರಣಗಳನ್ನು ಹೇಗೆ ಪಟ್ಟಿಮಾಡಬಹುದು ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತದೆ. ಪ್ರತಿ ಉಪಕರಣದ ಹೆಸರನ್ನು ನಾವು ಹೊರತರುತ್ತೇವೆ.

#### ಜಾವಾ

```java
// ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮತ್ತು ಪ್ರದರ್ಶಿಸಿ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ಸಂಪರ್ಕವನ್ನು ಪರಿಶೀಲಿಸಲು ನೀವು ಸರ್ವರ್‌ಗೆ ಪಿಂಗ್ ಮಾಡಲು ಸಹ ಸಾಧ್ಯವಿದೆ
client.ping();
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಎಲ್ಲ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಡೆಯಲು `listTools()` ಅನ್ನು ಕರೆಸಿದೆವು.
- ಸಂಪರ್ಕವು ಸರಿಯಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಲು `ping()` ಅನ್ನು ಉಪಯೋಗಿಸಿದೆವು.
- `ListToolsResult` ನಲ್ಲಿ ಎಲ್ಲಾ ಉಪಕರಣಗಳ ಹೆಸರು, ವಿವರಣೆ, ಮತ್ತು ಇನಪುಟ್ ಸ್ಕೆಮಾ ಮಾಹಿತಿ ಇರುತ್ತದೆ.

ಚೆನ್ನಾಗಿದೆ, ಈಗ ಎಲ್ಲಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಚಿತ್ರಿಸಿದ್ದೇವೆ. ಇದೀಗ ಅವುಗಳನ್ನು ನಾವು ಯಾವಾಗ ಬಳಸೋಣ? ಈ ಕ್ಲೈಂಟ್ ಬಹಳ ಸರಳವಾಗಿದೆ, ಅಂದರೆ ನಾವು ಅಗತ್ಯವಿರುವಾಗ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಕರೆಸಬೇಕಾಗುತ್ತದೆ. ಮುಂದಿನ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಸ್ವಂತ ದೊಡ್ಡ ಭಾಷಾ ಮಾದರಿಯನ್ನು (LLM) ಒಳಗೊಂಡ ಆಧುನಿಕ ಕ್ಲೈಂಟ್ ರಚಿಸುವೆವು. ಈಗ though, ನಾವು ಸರ್ವರ್‌ನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಹೇಗೆ invoke ಮಾಡೋದು ನೋಡೋಣ:

#### ರಸ್ಟ್

ಮುಖ್ಯ ಫಂಕ್ಷನ್‌ನಲ್ಲಿ, ಕ್ಲೈಂಟ್ ಆರಂಭಿಸಿದ ನಂತರ, ನಾವು ಸರ್ವರ್‌ನ್ನು ಆರಂಭಿಸಿ ಅದರ ಕೆಲವು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿಮಾಡಬಹುದು.

```rust
// ಪ್ರಾರಂಭಿಸಿ
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ಸಾಧನಗಳ ಪಟ್ಟಿ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು invoke ಮಾಡುವುದು

ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು invoke ಮಾಡಲು ಸರಿಯಾದ arguments ನೀಡಬೇಕು ಮತ್ತು ಕೆಲವೊಮ್ಮೆ invoke ಮಾಡಲು ಯತ್ನಿಸುವ ಅಂಶದ ಹೆಸರನ್ನು ಸ್ಪಷ್ಟಪಡಿಸಬೇಕು.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript

// ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ಒಂದು ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಕರೆಮಾಡಿ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿದೆವು, `readResource()` ಅನ್ನು `uri` ನೀಡುವುದರ ಮೂಲಕ ಕರೆಯುತ್ತೇವೆ. ಸರ್ವರ್ ಭಾಗದಲ್ಲಿ ಅದು ಹೀಗೆ ಇರಬಹುದು:

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

    ನಮ್ಮ `uri` ಮೌಲ್ಯ `file://example.txt` ಸರ್ವರ್‌ನ `file://{name}` ಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತದೆ. `example.txt` ಅನ್ನು `name` ಗೆ ನಕ್ಷೆ ಮಾಡಲಾಗುತ್ತದೆ.

- ಒಂದು ಉಪಕರಣವನ್ನು ಕರೆಸಿದೆವು, ಅದರ `name` ಮತ್ತು `arguments` ನೊಂದಿಗೆ ಹೀಗೆ ಕರೆಸಲಾಗುತ್ತದೆ:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ಪ್ರಾಂಪ್ಟ್ ಪಡೆಯಲು, `getPrompt()` ಅನ್ನು `name` ಮತ್ತು `arguments` ನೊಂದಿಗೆ ಕರೆಸುತ್ತೇವೆ. ಸರ್ವರ್ ಕೋಡ್ ಹೀಗಿರಬಹುದು:

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

    ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡ್ ಹೀಗಿರುತ್ತದೆ, ಇದು ಸರ್ವರ್‌ನಲ್ಲಿ ಘೋಷಿಸಿದವಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### ಪೈಥನ್

```python
# ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ಒಂದು ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- `greeting` ಎಂಬ ಸಂಪನ್ಮೂಲವನ್ನು `read_resource` ಬಳಸಿ ಕರೆಸಿದೆವು.
- `add` ಎಂಬ ಉಪಕರಣವನ್ನು `call_tool` ಬಳಸಿ invoke ಮಾಡಿದೆವು.

#### .NET

1. ಉಪಕರಣವನ್ನು invoke ಮಾಡುವ ಕೆಲವು ಕೋಡ್ ಸೇರಿಸುವೆವು:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸಲು, ಕೆಳಗಿನ ಕೋಡ್ ಬಳಸಬಹುದು:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ಜಾವಾ

```java
// ವಿವಿಧ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ഉപಕರಣಗಳನ್ನು ಕರೆಮಾಡಿ
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

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- `callTool()` ವಿಧಾನ ಮತ್ತು `CallToolRequest` ವಸ್ತುಗಳಿಂದ ಬಹು ಉಪಕರಣಗಳನ್ನು ಕರೆಸಿದೆವು.
- ಪ್ರತಿ ಉಪಕರಣದ ಕರೆ ಉಪಕರಣದ ಹೆಸರನ್ನು ಮತ್ತು ಆ ಉಪಕರಣಕ್ಕೆ ಬೇಕಾಗುವ ನಿಯತಾಂಕಗಳ `Map` ಅನ್ನು ಸ್ಪಷ್ಟಪಡಿಸುತ್ತದೆ.
- ಸರ್ವರ್ ಉಪಕರಣಗಳು ನಿರ್ದಿಷ್ಟ ನಿಯತಾಂಕ ಹೆಸರನ್ನು (ಉದಾ: ಗಣಿತ ಕ್ರಿಯೆಗಳಿಗೆ "a", "b") ನಿರೀಕ್ಷಿಸುತ್ತವೆ.
- ಫಲಿತಾಂಶಗಳನ್ನು ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆ ಹೊಂದಿರುವ `CallToolResult` ವಸ್ತುಗಳಾಗಿ ಹಿಂತಿರುಗಿಸುತ್ತವೆ.

#### ರಸ್ಟ್

```rust
// ಪರಾಮರ್ಶೆಗಳು = {"a": 3, "b": 2} ಜೊತೆಗೆ add ಟೂಲ್ ಅನ್ನು ಕರೆಮಾಡಿ
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

### -5- ಕ್ಲೈಂಟ್ ಅನ್ನು ಓಡಿಸುವುದು

ಕ್ಲೈಂಟ್ ಓಡಿಸಲು, ಕೆಳಕಂಡ ಆದೇಶವನ್ನು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಟೈಪ್‌ಮಾಡಿ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

*package.json* ನ "scripts" ವಿಭಾಗದಲ್ಲಿ ಕೆಳಕಂಡ ಎಂಟ್ರಿಯನ್ನು ಸೇರಿಸಿ:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### ಪೈಥನ್

ಕೆಳಗಿನ ಆದೇಶದಿಂದ ಕ್ಲೈಂಟ್ ಅನ್ನು ಕರೆಸಿರಿ:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ಜಾವಾ

ಮೊದಲು, ನಿಮ್ಮ MCP ಸರ್ವರ್ `http://localhost:8080` ನಲ್ಲಿ ಓಡುತ್ತಿರಲಿ ಎಂದು ದೃಢಪಡಿಸಿ. ನಂತರ ಕ್ಲೈಂಟ್ ಅನ್ನು ಓಡಿಸಿ:

```bash
# ನಿಮ್ಮ ಯೋಜನೆಯನ್ನು ನಿರ್ಮಿಸಿ
./mvnw clean compile

# ಕ್ಲೈಯಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ಅಥವಾ, ನೀವು ಸಂಪೂರ್ಣ ಕ್ಲೈಂಟ್ ಯೋಜನೆಯನ್ನು λύಣೆ ಫೋಲ್ಡರ್ `03-GettingStarted\02-client\solution\java` ನಲ್ಲಿ ಓಡಿಸಬಹುದು:

```bash
# ಪರಿಹಾರ ಡೈರೆಕ್ಟರಿಗೆ ಸಾಗಿಕೊಳ್ಳಿ
cd 03-GettingStarted/02-client/solution/java

# JAR ರಚಿಸಿ ಮತ್ತು ನಡಿಸು
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### ರಸ್ಟ್

```bash
cargo fmt
cargo run
```

## ನಿಯೋಜನೆ

ಈ ನಿಯೋಜನೆಯಲ್ಲಿ, ನೀವು ಕಲಿತಂಥದ್ದು ಉಪಯೋಗಿಸಿ ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ರಚಿಸಬೇಕು.

ನೀವು ಕೆಳಗಿನ ಸರ್ವರ್ ಅನ್ನು ಬಳಸಿ ನಿಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡ್ ಮೂಲಕ ಅದನ್ನು ಕರೆಸಬಹುದು, ಸರ್ವರ್‌ಗೆ ಹೆಚ್ಚು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸುವ ಪ್ರಯತ್ನ ಮಾಡಿ, ಅದನ್ನು ಹೆಚ್ಚು ಸುಪ್ರಭಾವಿ ಮಾಡಿಕೊಂಡಿರಿ.

### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ಒಂದು MCP ಸರ್ವರ್ ರಚಿಸಿ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ಒಂದು ಸೇರ್ಪಡೆ ಉಪಕರಣ ಸೇರಿಸಿ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ಗತಿಶೀಲ ಸ್ವಾಗತ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

// stdin ಮೇಲೆ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು stdout ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸಿ

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

### ಪೈಥನ್

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP ಸರ್ವರ್ ರಚಿಸಿ
mcp = FastMCP("Demo")


# ಒಂದು ಸೇರ್ಪಡೆ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ಡೈನಾಮಿಕ್ ಗೆಟ್ರಿಂಗ್ನ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

ಈ ಯೋಜನೆಯನ್ನು ನೋಡಿ ನೀವು ಹೇಗೆ [ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸೇರಿಸಬಹುದೋ](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ.

ಈ ಲಿಂಕ್‌ನಲ್ಲಿ ನೀವು ಹೇಗೆ [ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು invoke ಮಾಡಬೇಕೆಂಬುದನ್ನು](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ಪರೀಕ್ಷಿಸಿ.

### ರಸ್ಟ್

[ಹಿಂದಿನ ವಿಭಾಗದಲ್ಲಿ](../../../../03-GettingStarted/01-first-server), ನೀವು ರಸ್ಟ್‌ನಲ್ಲಿ ಸರಳ MCP ಸರ್ವರ್ ರಚಿಸಲು ಕಲಿತೀರಿ. ಅದನ್ನು ಬಳಸಿಕೊಂಡು ಮುಂದುವರೆಸಬಹುದು ಅಥವಾ ಈ ಲಿಂಕ್‌ನಲ್ಲಿ ಇನ್ನಷ್ಟು ರಸ್ಟ್ ಆಧಾರಿತ MCP ಸರ್ವರ್ ಉದಾಹರಣೆಗಳನ್ನು ನೋಡಿ: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## λύಣೆ

**λύಣೆ ಫೋಲ್ಡರ್** ಸಂಪೂರ್ಣ, ತಕ್ಷಣ ಓಡಿಸಲು ಸಿದ್ದವಾಗಿರುವ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನಗಳನ್ನು ಒಳಗೊಂಡಿದ್ದು ಈ ಟ್ಯುಟೋರಿಯಲ್‌ನಲ್ಲಿ ಒಳಗೊಂಡ ಎಲ್ಲ ದೃಷ್ಟಾಂತಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ಪ್ರತಿ λύಣೆ ಪ್ರತ್ಯೇಕ, ಸ್ವತಂತ್ರ ಯೋಜನೆಯಲ್ಲಿ ಕ್ಲೈಂಟ್ ಮತ್ತು ಸರ್ವರ್ ಕೋಡ್ ಅನ್ನು ಹೊಂದಿದೆ.

### 📁 λύಣೆ ಸಂರಚನೆ

λύಣೆ ಡೈರೆಕ್ಟರಿ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಯ ಮೂಲಕ ಸಂಘಟಿತವಾಗಿದೆ:

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

### 🚀 ಪ್ರತಿ λύಣೆ ಯಾವುದು ಒಳಗೊಂಡಿದೆ

ಪ್ರತಿ ಭಾಷಾ-ನಿರ್ದಿಷ್ಟ λύಣೆ ನೀಡುತ್ತದೆ:

- ಟ್ಯುಟೋರಿಯಲ್‌ನ ಎಲ್ಲ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಒಳಗೊಂಡ **ಸಂಪೂರ್ಣ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನ**
- ಸರಿಯಾದ ಅವಲಂಬನೆಗಳು ಮತ್ತು ಸಂರಚನೆಯೊಂದಿಗೆ **ಕಾರ್ಯನಿರ್ವಹಣಾ ಯೋಜನೆ ರಚನೆ**
- ಆಳವಡ್ಡಿಯಾಗಿ ಸ್ಥಾಪನೆ ಮತ್ತು ಕಾರ್ಯಚರಣೆಗೆ **ನಿರ್ಮಿಸಿ ಮತ್ತು ಓಡಿಸುವ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳು**
- ಭಾಷಾ-ನಿರ್ದಿಷ್ಟ ಸೂಚನೆಗಳೊಂದಿಗೆ **ವಿಸ್ತೃತ README**
- **ದೋಷ ನಿರ್ವಹಣೆ** ಮತ್ತು ಫಲಿತಾಂಶ ಪ್ರಕ್ರಿಯೆ ಮಾದರಿಗಳು

### 📖 λύಣೆ ಬಳಸುವುದು

1. **ನಿಮ್ಮ ಇଚ್ಛಿತ ಭಾಷಾ ಫೋಲ್ಡರ್ ಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ:**

   ```bash
   cd solution/typescript/    # ಟೈಪ್ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಾಗಿ
   cd solution/java/          # ಜಾವಾ ಕೈಗೆ
   cd solution/python/        # ಪೈಥಾನ್‌ಗಾಗಿ
   cd solution/dotnet/        # ಡಾಟ್‌ನೆಟ್‌ಗಾಗಿ
   ```

2. **ಪ್ರತಿ ಫೋಲ್ಡರ್‌ನ README ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ:**
   - ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸುವುದು
   - ಯೋಜನೆಯನ್ನು ರಚಿಸುವುದು
   - ಕ್ಲೈಂಟ್ ಓಡಿಸುವುದು

3. **ನೀವು ಕಾಣಬೇಕಾದ ಉದಾಹರಣೆಯ ಔಟ್‌ಪುಟ್:**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ಸಂಪೂರ್ಣ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಮತ್ತು ಕ್ರಮವಾಗಿ ಸೂಚನೆಗಳಿಗೆ ನೋಡಿ: **[📖 λύಣೆ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](./solution/README.md)**

## 🎯 ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು

ಈ ಟ್ಯುಟೋರಿಯಲ್ ಆವರ್ತಿಸಿದ್ದ ಎಲ್ಲಾ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಿಗೆ ಸಂಪೂರ್ಣ, ಕಾರ್ಯನಿರ್ವಹಿಸಬಹುದಾದ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನಗಳನ್ನು ನಾವು ಒದಗಿಸಿದ್ದೇವೆ. ಈ ಉದಾಹರಣೆಗಳು ಮೇಲ್ಕಂಡ ಕಾರ್ಯಕ್ಷಮತೆಗಳನ್ನು ಸಿಕ್ಕಾಪಟ್ಟೆ ತೋರಿಸುತ್ತವೆ ಮತ್ತು ನಿಮ್ಮದೇ ಯೋಜನೆಗಳು ಅಥವಾ ಪ್ರಾರಂಭಿಕ ಬಿಂದುಗಳಾಗಿ ಬಳಸಬಹುದು.

### ಲಭ್ಯವಿರುವ ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು

| ಭಾಷೆ | ಫೈಲ್ | ವಿವರಣೆ |
|----------|------|-------------|
| **ಜಾವಾ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ಸಾರಿಗೆ ಬಳಸಿ ವ್ಯಾಪಕ ದೋಷ ನಿರ್ವಹಣೆ ಸಹಿತ ಸಂಪೂರ್ಣ ಜಾವಾ ಕ್ಲೈಂಟ್ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ಸಾರಿಗೆ ಬಳಸಿ ಸ್ವಯಂಚಾಲಿತ ಸರ್ವರ್ ಪ್ರಾರಂಭಿಸುವ ಸಂಪೂರ್ಣ C# ಕ್ಲೈಂಟ್ |
| **ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP ಪ್ರೋಟೋಕಾಲ್ ಸಂಪೂರ್ಣ ಬೆಂಬಲದ ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಲೈಂಟ್ |
| **ಪೈಥನ್** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | ಅಸಿಂಕ್/ಅವೇಟ್ ಮಾದರಿಗಳು ಬಳಸಿ ಸಂಪೂರ್ಣ ಪೈಥನ್ ಕ್ಲೈಂಟ್ |
| **ರಸ್ಟ್** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | ಅಸಿಂಕ್ ಕಾರ್ಯಗಳಿಗಾಗಿ ಟೋಕಿಯೋ ಬಳಸಿ ಸಂಪೂರ್ಣ ರಸ್ಟ್ ಕ್ಲೈಂಟ್ |

ಪ್ರತಿ ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳಲ್ಲಿ ಇದೆ:

- ✅ **ಸಂಪರ್ಕ ಸ್ಥಾಪನೆ** ಮತ್ತು ದೋಷ ನಿರ್ವಹಣೆ
- ✅ **ಸರ್ವರ್ ಕಂಡುಹಿಡಿಯುವಿಕೆ** (ಪ್ರಯೋಜನಾಕರವಾದಲ್ಲಿ ಉಪಕರಣಗಳು, ಸಂಪನ್ಮೂಲಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು)
- ✅ **ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್ ಕಾರ್ಯಾಚರಣೆಗಳು** ( ಸೇರಿಸುವುದು, ತೆಗೆದುಕೊಳ್ಳುವುದು, ಗುಣಾಕಾರ, ಭಾಗಾಕಾರ, ಸಹಾಯ)
- ✅ **ಫಲಿತಾಂಶ ಪ್ರಕ್ರಿಯೆ** ಮತ್ತು ಸೂಕ್ತ ರೂಪದಲ್ಲಿ ಔಟ್‌ಪುಟ್
- ✅ **ವಿಸ್ತೃತ ದೋಷ ನಿರ್ವಹಣೆ**

- ✅ **ಸ್ವಚ್ಛ, ವರದಿಯಾಗಿರುವ ಕೋಡ್** ಎಲ್ಲ ಹೆಜ್ಜೆ ಹಾದಿಗಳನ್ನು ವಿವರಿಸುವ ಟಿಪ್ಪಣಿಗಳೊಂದಿಗೆ

### ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸುವುದು

1. ಮೇಲಿನ ಟೇಬಲ್‌ನಿಂದ **ನಿಮ್ಮ ಇಷ್ಟದ ಭಾಷೆಯನ್ನು ಆರಿಸಿ**
2. ಸಂಪೂರ್ಣ ಅನುಷ್ಠಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು **ಸಂಪೂರ್ಣ ಉದಾಹರಣೆ ಫೈಲ್ ಪರಿಶೀಲಿಸಿ**
3. [`complete_examples.md`](./complete_examples.md) ನ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ **ಉದಾಹರಣೆಯನ್ನು ರನ್ ಮಾಡಿ**
4. ನಿಮ್ಮ ನಾನಾ ಉದ್ದೇಶಕ್ಕೆ **ಉದಾಹರಣೆತನ್ನು ತಿದ್ದುಪಡಿ ಮತ್ತು ವಿಸ್ತರಿಸಿ**

ಈ ಉದಾಹರಣೆಗಳನ್ನು how to run ಮತ್ತು কাস্টಮೈಸ್ ಮಾಡುವುದು ಬಗ್ಗೆ ಸಂಪೂರ್ಣ ದಾಖಲೆಗಾಗಿ, ನೋಡಿ: **[📖 ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](./complete_examples.md)**

### 💡 ಪರಿಹಾರ ಮತ್ತು ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳ ನಡುವಿನ ವ್ಯತ್ಯಾಸ

| **ಪರಿಹಾರ ಫೋಲ್ಡರ್** | **ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು** |
|--------------------|--------------------- |
| ಕಟ್ಟಡ ಫೈಲ್‌ಗಳೊಂದಿಗೆ ಸಂಪೂರ್ಣ ಯೋಜನೆಯ ರಚನೆ | ಒಂದು ಫೈಲ್‌ಗಳ ಅನುಷ್ಠಾನಗಳು |
| ಅವಲಂಬನೆಗಳೊಂದಿಗೆ ತಯಾರಾಗಿ ಓಡಿಸಲು | ಕೇಂದ್ರೀಯವಾದ ಕೋಡ್ ಉದಾಹರಣೆಗಳು |
| ಉತ್ಪಾದನಾ ಮಟ್ಟದ ವ್ಯವಸ್ಥೆ | ಶೈಕ್ಷಣಿಕ ರೆಫರೆನ್ಸ್ |
| ಭಾಷಾ-ನಿರ್ದಿಷ್ಟ ಟೂಲಿಂಗ್ | ಭಾಷೆಗಳ ನಡುವಿನ ಹೋಲಿಕೆ |

ಎರಡೂ ವಿಧಾನಗಳು ಮೂರು - **ಪರಿಹಾರ ಫೋಲ್ಡರ್** ಸಂಪೂರ್ಣ ಯೋಜನೆಗಳಿಗಾಗಿ, ಮತ್ತು **ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು** ಕಲಿಕೆ ಮತ್ತು ಉಲ್ಲೇಖಕ್ಕಾಗಿ ಉಪಯೋಗಿಸಿ.

## ಮುಖ್ಯ ಪಾಠಗಳು

ಈ ಅಧ್ಯಾಯದ ಮುಖ್ಯ ಪಾಠಗಳು ಗ್ರಾಹಕರ ಬಗ್ಗೆ ಇವುಗಳಾಗಿವೆ:

- ಸರ್ವರ್‌ನ ಪ್ರತ್ಯೇಕತೆ ಮತ್ತು ಕಾರ್ಯಾನುಷ್ಠಾನವನ್ನೂ ಕಾಣಲು ಮತ್ತು ಕರೆ ಮಾಡಲು ಬಳಸಬಹುದು.
- ಸ್ವತಃ ಪ್ರಾರಂಭವಾಗುವಾಗ ಸರ್ವರ್ ಆರಂಭಿಸಬಹುದು (ಈ ಅಧ್ಯಾಯದಂತೆ) ಆದರೆ ಗ್ರಾಹಕರು ಇತರ ಓಡುತ್ತಿರುವ ಸರ್ವರ್‌ಗೆ ಕೂಡ ಸಂಪರ್ಕಿಸಬಹುದು.
- ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಅಥವಾ ಹೀಗೊಂದು ಬದಲಿ ಮಾರ್ಗಗಳ ಹೋಲಿಕೆಯಲ್ಲಿ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಅದ್ಭುತ ಮಾರ್ಗ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- [MCP ನಲ್ಲಿ ಗ್ರಾಹಕರ ನಿರ್ಮಾಣ](https://modelcontextprotocol.io/quickstart/client)

## ಮಾದರಿಗಳು

- [ಜಾವಾ ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.NET ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [ಪೈಥಾನ್ ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)
- [ರಸ್ಟ್ ಕ್ಯಾಲುಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)

## ಮುಂದಿನದು ಏನು

- ಮುಂದಿನದು: [LLM ಜೊತೆ ಗ್ರಾಹಕ ರಚನೆ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->