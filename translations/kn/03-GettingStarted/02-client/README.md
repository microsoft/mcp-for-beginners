# ಕ್ಲೈಂಟ್ ರಚನೆ

ಕ್ಲೈಂಟ್‌ಗಳು ಕಸ್ಟಮ್ ಅನ್ವಯಿಕೆಗಳು ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳಾಗಿದ್ದು, ಅವು MCP ಸರ್ವರ್‌ನೊಂದಿಗೆ ನೇರವಾಗಿ ಸಂಪರ್ಕ ಸಾಧಿಸಿ ಸಂಪನ್ಮೂಲಗಳು, ಸಾಧನಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಗಾಗಿ ವಿನಂತಿ ಮಾಡುತ್ತವೆ. ಸರ್ವರ್‌ನೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಗ್ರಾಫಿಕಲ್ ಇಂಟರ್ಫೇಸ್ ನೀಡುವ ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಟೂಲ್ ಬಳಕೆ ಮಾಡುವುದರಿಂದ ಭಿನ್ನವಾಗಿ, ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಬರೆಯುವುದರಿಂದ ಪ್ರೋಗ್ರಾಮಾಟಿಕ ಮತ್ತು ಸ್ವಯಂಚಾಲಿತ ಸಂವಹನ ಸಾಧ್ಯವಾಗುತ್ತದೆ. ಇದರಿಂದ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರು MCP యొక్క ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತಮ್ಮದೇ ಕಾರ್ಯಪ್ರವಾಹಗಳಿಗೆ ಸಂಯೋಜಿಸಬಹುದು, ಕಾರ್ಯಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಬಹುದು ಮತ್ತು ವಿಶೇಷ ಅಗತ್ಯಗಳಿಗೆ ಹೊಂದಿಕೊಂಡ ಕಸ್ಟಮ್ ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸಬಹುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠವು ಮಾದರಿ ಪ್ರಾಸಂಗಿಕ ಪ್ರೋಟೊಕಾಲ್ (MCP) ಪರಿಸರದಲ್ಲಿ ಕ್ಲೈಂಟ್​ಗಳ հասկացಿಕೆಯನ್ನು ಪರಿಚಯಿಸುತ್ತದೆ. ನೀವು ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೇಗೆ ರಚಿಸಿ ಅದನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೀರಿ.

## ಕಲಿಕೆ ಗುರಿಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯಕ್ಕೆ ನೀವು:

- ಕ್ಲೈಂಟ್ ಏನು ಮಾಡಬಹುದು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬಹುದು.
- ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಬರೆಯಬಹುದು.
- ಕ್ಲೈಂಟ್ ಅನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಿ ಪರೀಕ್ಷಿಸಿ, ಸರ್ವರ್ ನಿರೀಕ್ಷೆಯಂತೆ ಕೆಲಸ ಮಾಡುತ್ತೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬಹುದು.

## ಕ್ಲೈಂಟ್ ಬರೆಯಲು ಏನು ಬೇಕಾಗುತ್ತದೆ?

ಕ್ಲೈಂಟ್ ಬರೆಯಲು, ನೀವು ಇವುಗಳನ್ನು ಮಾಡಬೇಕಾಗುತ್ತದೆ:

- **ಸರಿ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಿ**. ನೀವು ಹಿಂದೆ ಬಳಸಿದ ಅದೇ ಲೈಬ್ರರಿಯನ್ನು ಬಳಸುತ್ತೀರಿ, ಆದರೆ ವಿಭಿನ್ನ ಘಟಕಗಳೊಂದಿಗೆ.
- **ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆ ಸೃಷ್ಟಿಸು**. ಇದು ಒಂದು ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆ ರಚಿಸಿ ಅದನ್ನು ಆಯ್ಕೆಮಾಡಲಾದ ಸಂಚಾರ ವಿಧಾನದಲ್ಲಿ ಸಂಪರ್ಕಿಸುವುದನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ.
- **ಯಾವ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬೇಕಾದುದಾಗಿ ನಿರ್ಧರಿಸು**. ನಿಮ್ಮ MCP ಸರ್ವರ್ ಸಂಪನ್ಮೂಲಗಳು, ಸಾಧನಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಬರುತ್ತದೆ, ನೀವು ಯಾವುದು ಪಟ್ಟಿ ಮಾಡಬೇಕೆಂದು ತೀರ್ಮಾನಿಸಬೇಕು.
- **ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೋಸ್ಟ್ ಅನ್ವಯಿಕೆಗೆ ಸಂಯೋಜಿಸು**. ಸರ್ವರ್‌ನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತಿಳಿದಿರುವ ನಂತರ, ಬಳಕೆದಾರರು ಪ್ರಾಂಪ್ಟ್ ಅಥವಾ ಇತರ ಆಜ್ಞೆಯನ್ನು ಟೈಪ್ ಮಾಡಿದಾಗ ಸಂಬಂಧಿಸಿದ ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯ ಕಾರ್ಯಗತಗೊಳಿಸಲು ಈ ಕ್ಲೈಂಟ್ ಅನ್ನು ನಿಮ್ಮ ಹೋಸ್ಟ್ ಅನ್ವಯಿಕೆಗೆ ಸಂಯೋಜಿಸಬೇಕು.

ಈಗ ನಾವು ಉನ್ನತ ಮಟ್ಟದಲ್ಲಿ ಏನು ಮಾಡಬೇಕೆಯೋ ತಿಳಿದುಕೊಂಡಿದ್ದೇವೆ, ಮುಂದಿನ ಉದಾಹರಣೆಯ ಕಡೆ ನೋಡೋಣ.

### ಉದಾಹರಣೆಯ ಕ್ಲೈಂಟ್

ಈ ಉದಾಹರಣೆಯ ಕ್ಲೈಂಟ್ ನೋಡೋಣ:

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

// ಪಟ್ಟಿ ಸೂಚನೆಗಳು
const prompts = await client.listPrompts();

// ಒಂದು ಸೂಚನೆಯನ್ನು ಪಡೆಯಿರಿ
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
const resources = await client.listResources();

// ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ಒಂದು ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಿ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಸಿಕೊಂಡೇವೆ
- ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆ ಸೃಷ್ಟಿಸಿ ಅದನ್ನು stdio ಬಳಸಿ ಸಂಪರ್ಕಿಸಿದ್ದೇವೆ.
- ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಅವುಗಳನ್ನು invoke ಮಾಡಿದೇವೆ.

ಇಲ್ಲಿ ನಿಮಗೆ MCP ಸರ್ವರ್ ಮಾತಾಡಬಲ್ಲ ಕ್ಲೈಂಟ್ ಸಿಗುತ್ತದೆ.

ಮುಂದಿನ ವ್ಯಾಯಾಮ ವಿಭಾಗದಲ್ಲಿ ಪ್ರತಿಯೊಂದು ಕೋಡ್ ಸೆಗ್ಮೆಂಟ್ ಅನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಏನಾಗುತ್ತಿದೆಯೋ ವಿವರಿಸಲು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳೋಣ.

## ವ್ಯಾಯಾಮ: ಕ್ಲೈಂಟ್ ಬರೆಯುವುದು

ಮೇಲೆ ಹೇಳಿದಂತೆ, ಕೋಡ್ ಅನ್ನು ಮನಸುನಿರಿಸಿ ವಿವರಿಸೋಣ, ಬೇಕಾದರೆ ಜೊತೆಗೆ ಕೋಡ್ ಮಾಡಬೇಕಾದರೆ ಅದೂ ಮಾಡಬಹುದು.

### -1- ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳುವುದು

ನಾವು ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳೋಣ, ಇದು ಕ್ಲೈಂಟ್ ಮತ್ತು ಆಯ್ದ ಸಂಚಾರ ಪ್ರೋಟೊಕಾಲ್ (stdio) ಗೆ ಸಂಬಂಧಿಸಿದ ನಿರ್ದಿಷ್ಟ ಉಲ್ಲೇಖಗಳನ್ನು ಹೊಂದಿರಬೇಕು. stdio ನಿಮ್ಮ ಸ್ಥಳೀಯ ಯಂತ್ರದಲ್ಲಿ ಓಡುವುದಕ್ಕಾಗಿ ಪ್ರೋಟೊಕಾಲ್. SSE ಮತ್ತೊಂದು ಸಂಚಾರ ಪ್ರೋಟೊಕಾಲ್ ಆಗಿದ್ದು, ಮುಂದಿನ ಅಧ್ಯಾಯಗಳಲ್ಲಿ ತೋರಿಸಲಾಗುತ್ತದೆ ಆದರೆ ಅದು ನಿಮ್ಮ ಇನ್ನೊಂದು ಆಯ್ಕೆ. ಇದುವರೆಗೆ stdio ಯೊಂದಿಗೆ ಮುಂದುವರಿಯೋಣ.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### ಪೈಥಾನ್

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

ಜಾವಾಗಾಗಿ, ನೀವು ಹಿಂದಿನ ವ್ಯಾಯಾಮದಿಂದ MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವ ಕ್ಲೈಂಟ್ ರಚಿಸಬೇಕು. [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) ನಲ್ಲಿ ಬಳಸಿದ ಜावा ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆಯಲ್ಲಿಯೇ `SDKClient` ಎಂಬ ಹೊಸ ಜಾವಾ ಕ್ಲಾಸ್ ಅನ್ನು `src/main/java/com/microsoft/mcp/sample/client/` ಫೋಲ್ಡರ್‌ನಲ್ಲಿ ರಚಿಸಿ ಮತ್ತು ಕೆಳಗಿನ ಆಮದುಗಳನ್ನು ಸೇರಿಸಿ:

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

ನಿಮ್ಮ `Cargo.toml` ಫೈಲಿಗೆ ಈ ಕೆಳಗಿನ ಅನುಪ摇ಸ್‍ಗಳು ಶೇಖರಿಸಬೇಕು.

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

ಆ ನಂತರ, ಕ್ಲೈಂಟ್ ಕೋಡ್ ನಲ್ಲಿ ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಬಹುದು.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ಮುಂದೆ, ಉದಾಹರಣೆ ಮಾಡೋಣ.

### -2- ಕ್ಲೈಂಟ್ ಮತ್ತು ಸಂಚಾರ ಉದಾಹರಣೆ ಸೃಷ್ಟಿಸುವುದು

ನಾವು ಸಂಚಾರದ ಉದಾಹರಣೆ ಮತ್ತು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆಯನ್ನು ರಚಿಸಬೇಕಾಗುತ್ತದೆ:

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

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- stdio ಸಂಚಾರದ ಉದಾಹರಣೆ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ. ಸರ್ವರ್ ಅನ್ನು ಹುಡುಕಿ ಪ್ರಾರಂಭಿಸಲು ವಿಧಾನದ ಹಾಗೂ ಆರ್ಜುಗಳ ಕುರಿತು ಹೇಗೆ ಸೂಚಿಸುತ್ತಿದ್ದದ್ದು ಗಮನಿಸಿ, ಇದನ್ನು ನಾವು ಕ್ಲೈಂಟ್ ರಚಿಸುವಾಗ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- ಕ್ಲೈಂಟ್ ನಿರೂಪಣೆಗಾಗಿ ಹೆಸರು ಮತ್ತು ಆವೃತ್ತಿ ನೀಡಿ ಉದಾಹರಣೆ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ಆಯ್ದ ಸಂಚಾರಕ್ಕೆ ಕ್ಲೈಂಟ್ ಅನ್ನು ಸಂಪರ್ಕಿಸಿದ್ದೇವೆ.

    ```typescript
    await client.connect(transport);
    ```

#### ಪೈಥಾನ್

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಗುರ್ತಿನಾಮಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯನಿರ್ವಹಣাযোগ್ಯ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳು
    env=None,  # ಐಚ್ಛಿಕ ಪರಿಸರ ಚರಗಳು
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ಸಂಪರ್ಕವನ್ನು ಪ್ರಾರಂಭಿಸಿ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿಸಿದ್ದೇವೆ
- ಸರ್ವರ್ ಪರಿಮಾಣಗಳ ವಸ್ತುವನ್ನು ಉದಾಹರಿಸಿಕೊಂಡೆವು, ಇದನ್ನು ಸರ್ವರ್‌ನ್ನು ಚಲಾಯಿಸಲು ಬಳಸಲಾಗುವುದು, ತದನಂತರ ಅದಕ್ಕೆ ನಮ್ಮ ಕ್ಲೈಂಟ್ ಸಂಪರ್ಕ ಸಾಧಿಸುತ್ತದೆ.
- `run` ಎಂಬ ವಿಧಾನವನ್ನು ನಿರೂಪಿಸಿದ್ದೇವೆ, ಇದು `stdio_client` ಅನ್ನು ಕರೆದು ಕ್ಲೈಂಟ್ ಅಧಿವೇಶನ ಪ್ರಾರಂಭಿಸುತ್ತದೆ.
- `asyncio.run` ಗೆ `run` ವಿಧಾನವನ್ನು ನೀಡುವ ಎಂಟ್ರಿ ಪಾಯಿಂಟ್ ರಚಿಸಿದ್ದೇವೆ.

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

ಮುಂಚಿನ ಕೋಡ್‌లో ನಾನು:

- ಬೇಕಾದ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ.
- stdio ಸಂಚಾರವನ್ನು ರಚಿಸಿ, `mcpClient` ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ. ಇದನ್ನು MCP ಸರ್ವರ್‌ನ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು ಮತ್ತು ಕರೆ ಮಾಡಲು ಬಳಸುತ್ತೇವೆ.

ಗಮನಿಸಬೇಕು, "Arguments" ನಲ್ಲಿ ನೀವು *.csproj* ಅಥವಾ ಎಕ್ಸಿಕ್ಯೂಟೇಬಲ್‌ಗೆ ಸೂಚಿಸಬಹುದು.

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
        
        // ನಿಮ್ಮ ಗ್ರಾಹಕ ಲಾಜಿಕ್ ಇಲ್ಲಿಗೆ ಹೋಗುತ್ತದೆ
    }
}
```

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಮೂಲ `http://localhost:8080` ಗೆ SSE ಸಂಚಾರವನ್ನು ಹೊಂದಿಸಿ ಮುಖ್ಯ ವಿಧಾನವನ್ನು ರಚಿಸಿದ್ದೇವೆ, ಅಲ್ಲಿ MCP ಸರ್ವರ್ ಚಾಲಿತವಾಗಿರುತ್ತದೆ.
- ಸಂಚಾರವನ್ನು ಕಾನ್ಸ್ಟ್ರಕ್ಟರ್ ಪಾರಮೀಟರ್ ಆಗಿ ತೆಗೆದುಕೊಳ್ಳುವ ಕ್ಲೈಂಟ್ ಕ್ಲಾಸ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ.
- `run` ವಿಧಾನದಲ್ಲಿ ಸಾಗಣೆಯೊಂದಿಗೆ ಸಮಕಾಲೀನ MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿ ಸಂಪರ್ಕವನ್ನು ಪ್ರಾರಂಭಿಸಿದ್ದೇವೆ.
- ಜಾವಾ ಸ್ಪ್ರಿಂಗ್ ಬೂಟ್ MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ HTTP ಆಧಾರಿತ ಸಂವಹನಕ್ಕಾಗಿ ಸೂಕ್ತವಾಗಿರುವ SSE (ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್‌ಗಳು) ಸಂಚಾರವನ್ನು ಬಳಸಿದ್ದೇವೆ.

#### ರಸ್ಟ್

ಈ ರಸ್ಟ್ ಕ್ಲೈಂಟ್ assumes ಸರ್ವರ್ "calculator-server" ಎಂಬ ಸಹಪಾಠಿ ಯೋಜನೆ ಆಗಿದೆ ಮತ್ತು ಅದೇ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಇದೆ. ಕೆಳಗಿನ ಕೋಡ್ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಅದಕ್ಕೆ ಸಂಪರ್ಕಿಸುವುದು.

```rust
async fn main() -> Result<(), RmcpError> {
    // ಸರ್ವರ್ ಅನ್ನು ಒಂದೇ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿರುವ "calculator-server" ಎಂಬ ಸಹೋದರ ಪ್ರಾಜೆಕ್ಟ್ ಎಂದು ಊಹಿಸಿ
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

    // TODO: ಪ್ರಾರಂಭಿಸಿ

    // TODO: ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ

    // TODO: {"a": 3, "b": 2} ಗುಣಲಬ್ಧArgumentಗಳೊಂದಿಗೆ add tool ಅನ್ನು ಕರೆಮಾಡಿ

    client.cancel().await?;
    Ok(())
}
```

### -3- ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು

ಈಗ, ನಮಗೆ ಸಂಪರ್ಕ ಸಾಧಿಸುವ ಕ್ಲೈಂಟ್ ಇತ್ತು, ಆದರೆ ಅದು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದಿಲ್ಲ, ಅದನ್ನು ನೋಡೋಣ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
// ಸೂಚನೆಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
const prompts = await client.listPrompts();

// ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
const resources = await client.listResources();

// ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
const tools = await client.listTools();
```

#### ಪೈಥಾನ್

```python
# ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ಇಲ್ಲಿ ನಾವು ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳು, `list_resources()` ಮತ್ತು ಸಾಧನಗಳನ್ನು, `list_tools` ಪಟ್ಟಿ ಮಾಡಿ ಪ್ರದರ್ಶಿಸುತ್ತೇವೆ.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ಮೇಲಿನ ಉದಾಹರಣೆಯಲ್ಲಿ ಸರ್ವರ್‌ನ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದನ್ನು ತೋರಿಸಲಾಗಿದೆ. ಪ್ರತಿ ಸಾಧನದ ಹೆಸರು ನಾವು ಅಚಿಕೊಳ್ಳುತ್ತೇವೆ.

#### ಜಾವಾ

```java
// ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮತ್ತು ಪ್ರದರ್ಶಿಸಿ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ಸಂಪರ್ಕವನ್ನು ಪರಿಶೀಲಿಸಲು ನೀವು ಸರ್ವರ್‌ಗೆ ಪಿಂಗ್ ಮಾಡಬಹುದು
client.ping();
```

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಪಡೆಯಲು `listTools()` ಅನ್ನು ಕರೆ ಮಾಡಿದೆವು.
- ಸಂಪರ್ಕ ಕೆಲಸ ಮಾಡಿತೇ ಎಂದು ಪರಿಶೀಲಿಸಿ `ping()` ಮಾಡಿಕೊಂಡಿದ್ದೇವೆ.
- `ListToolsResult` ಎಲ್ಲಾ ಸಾಧನಗಳ ಮಾಹಿತಿ, ಅವುಗಳ ಹೆಸರುಗಳು, ವರ್ಣನೆಗಳು ಮತ್ತು ಇನ್ಪುಟ್ ಸ್ಕೀಮಾ ಗಳು ಒಳಗೊಂಡಿವೆ.

ಚೆನ್ನಾಗಿದೆ, ನಾವು ಎಲ್ಲಾ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪತ್ತೆ ಮಾಡಿದ್ದೇವೆ. ಈಗ ಪ್ರಶ್ನೆ ಏನೆಂದರೆ ನಾವು ಅವುಗಳನ್ನು ಯಾವಾಗ ಬಳಸುತ್ತೀವೋ? ಈ ಕ್ಲೈಂಟ್ ಸರಳವಾಗಿದೆ, ನಾವು ಅವುಗಳನ್ನು ಬೇಕಾಗಿರುವಾಗ ಸ್ಪಷ್ಟವಾಗಿ ಕರೆ ಮಾಡಬೇಕಾಗುತ್ತದೆ. ಮುಂದಿನ ಅಧ್ಯಾಯದಲ್ಲಿ, ತಾವು ತನ್ನದೇ LLM (ಲಾರ್ಜ್ ಭಾಷಾ ಮಾದರಿ) ಹೊಂದಿರುವ ಉನ್ನತ ಕ್ಲೈಂಟ್ ರಚಿಸುತ್ತೇವೆ. ಈಗಾಗಲೇ, ಸರ್ವರ್ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು invoke ಮಾಡುವ ವಿಧಾನ ನೋಡೋಣ:

#### ರಸ್ಟ್

ಮುಖ್ಯ ಕಾರ್ಯದಲ್ಲಿ, ಕ್ಲೈಂಟ್ ಅನ್ನು ಆರಂಭಿಸಿದ ನಂತರ, ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಅದರ ಕೆಲವು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬಹುದು.

```rust
// ಪ್ರಾರಂಭಿಸಿ
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ಸಾಧನಗಳ ಪಟ್ಟಿಯನ್ನು ತೋರಿಸಿ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕರೆ ಮಾಡುವುದು

ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು invoke ಮಾಡಲು ನಮಗೆ ಸರಿಯಾದ аргументы ನೀಡಬೇಕು ಮತ್ತು ಕೆಲವು ಪ್ರಕರಣಗಳಲ್ಲಿ ನಾವು invoke ಮಾಡುತ್ತಿರುವ ವಿಷಯದ ಹೆಸರನ್ನು ಸೂಚಿಸಬೇಕು.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript

// ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ಪ್ರಾಂಪ್ಟ್ ಕರೆಮಾಡಿ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಒಂದು ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿದ್ದೇವೆ, `readResource()` ಕರೆ ಮಾಡಿ `uri` ನೀಡಿದ್ದೇವೆ. ಸರ್ವರ್ ಬದಿಯಲ್ಲಿನ ಕೋಡ್ ಹೀಗೆ ಇರಬಹುದು:

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

    ನಮ್ಮ `uri` ಮೌಲ್ಯ `file://example.txt` ಸರ್ವರ್‌ನಲ್ಲಿ `file://{name}` ಹೊಂದಿಕೆಯಾಗುತ್ತದೆ. `example.txt` ಅನ್ನು `name` ಗೆ ನಕ್ಷೆಮಾಡಲಾಗುತ್ತದೆ.

- ಒಂದು ಸಾಧನವನ್ನು ಕರೆ ಮಾಡುತ್ತೇವೆ, ಅದರ `name` ಮತ್ತು `arguments` ಅನ್ನು ಯಿದ್ದಂತೆ ಸೂಚಿಸುತ್ತೇವೆ:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ಒಂದು ಪ್ರಾಂಪ್ಟ್ ಪಡೆಯಲು, `getPrompt()` ಅನ್ನು `name` ಮತ್ತು `arguments` ಜೊತೆ ಕರೆ ಮಾಡುತ್ತೀರಿ. ಸರ್ವರ್ ಕೋಡ್ ಹೀಗೆ ಇದೆ:

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

    ಮತ್ತು ನಿಮ್ಮ ಫಲಿತಾಂಶದ ಕ್ಲೈಂಟ್ ಕೋಡ್ ಆದ್ದರಿಂದ ಹೀಗೆ ಕಾಣಿಸುತ್ತದೆ ಸರ್ವರ್ ಇಂದ ಘೋಷಿತ ಮೌಲ್ಯಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗಿಸಿ:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### ಪೈಥಾನ್

```python
# ಸಂಪನ್ಮೂಲವನ್ನು ಓದಿ
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಿ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- `greeting` ಎಂಬ ಸಂಪನ್ಮೂಲವನ್ನು `read_resource` ಮೂಲಕ ಕರೆ ಮಾಡಿದ್ದೇವೆ.
- `add` ಎಂಬ ಸಾಧನವನ್ನು `call_tool` ಮೂಲಕ invoke ಮಾಡಿದ್ದೇವೆ.

#### .NET

1. ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಲು ಕೆಲವು ಕೋಡ್ ಸೇರಿಸೋಣ:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸಲು ಈ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಬಳಸಬಹುದು:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### ಜಾವಾ

```java
// ವಿವಿಧ ಗಣಕ ಯಂತ್ರ ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡಿ
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

ಮುಂಚಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರಣಿಯಾಗಿ ಹಲವಾರು ಗಣಕಯಂತ್ರ ಸಾಧನಗಳನ್ನು `callTool()` ವಿಧಾನದಿಂದ `CallToolRequest` ವಸ್ತುಗಳೊಂದಿಗೆ ಕರೆ ಮಾಡಿದ್ದೇವೆ.
- ಪ್ರತಿ ಸಾಧನದ ಕರೆ ಸಾಧನದ ಹೆಸರು ಮತ್ತು ಆ ಸಾಧನಕ್ಕೆ ಬೇಕಾಗುವ `Map` ಆರ್ಜುಗಳನ್ನು ನೀಡುತ್ತದೆ.
- ಸರ್ವರ್ ಸಾಧನಗಳು ನಿಯತ ಪರಿಮಾಣ ಹೆಸರನ್ನು ನಿರೀಕ್ಷಿಸುತ್ತವೆ (ಉದಾ: ಗಣಿತ ಕ್ರಿಯೆಗಳಿಗೆ "a", "b").
- ಫಲಿತಾಂಶಗಳು `CallToolResult` ವಸ್ತುಗಳಾಗಿ ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹೊಂದಿರುತ್ತವೆ.

#### ರಸ್ಟ್

```rust
// ಆರ್ಗ್ಯುమెಂಟ್‌ಗಳು = {"a": 3, "b": 2} ಹೊಂದಿರುವ add ಟೂಲ್ ಅನ್ನು ಕರೆಸಿರಿ
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

### -5- ಕ್ಲೈಂಟ್ ಕಾರ್ಯಗತಗೊಳ್ಳಿಸು

ಕ್ಲೈಂಟ್ ಕಾರ್ಯಗತಗೊಳಿಸಲು, ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಆಜ್ಞೆ ಟೈಪ್ ಮಾಡಿ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

ನಿಮ್ಮ "scripts" ವಿಭಾಗದಲ್ಲಿ *package.json* ಫೈಲಿನಲ್ಲಿ ಕೆಳಗಿನ ಎಂಟ್ರಿಯನ್ನು ಸೇರಿಸಿ:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### ಪೈಥಾನ್

ಕ್ಲೈಂಟ್ ಅನ್ನು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಈ ವಿಧಾನದೊಂದಿಗೆ ಕರೆ ಮಾಡಿ:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### ಜಾವಾ

ಮೊದಲು, ನಿಮ್ಮ MCP ಸರ್ವರ್ `http://localhost:8080` ನಲ್ಲಿ ಚಾಲಿತವಾಗಿರುತ್ತದೆ ಎಂದು ದೃಢಪಡಿಸಿ. ನಂತರ ಕ್ಲೈಂಟ್ ಚಾಲನೆ ಮಾಡಿರಿ:

```bash
# ನಿಮ್ಮ ಯೋಜನೆಯನ್ನು ನಿರ್ಮಿಸಿ
./mvnw clean compile

# ಕ್ಲಯಿಂಟ್ ಅನ್ನು ಚಲಾಯಿಸಿ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ಅಥವಾ, ಸಂಪೂರ್ಣ ಕ್ಲೈಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ಅನ್ನು, ಸ್ನಾಯುವಿಕೆ ಫೋಲ್ಡರ್ `03-GettingStarted\02-client\solution\java` ನಲ್ಲಿ ನೀಡಲಾಗಿದೆ, ಪ್ರಾರಂಭಿಸಿ:

```bash
# ಪರಿಹಾರ ಡೈರೆಕ್ಟರಿಯನ್ನೂ ನಾವಿಗೇಟ್ ಮಾಡಿ
cd 03-GettingStarted/02-client/solution/java

# JAR ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಚಾಲನೆ ಮಾಡಿ
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### ರಸ್ಟ್

```bash
cargo fmt
cargo run
```

## ಕಾರ್ಯ

ಈ ಕಾರ್ಯದಲ್ಲಿ, ನೀವು ಕಲಿತದ್ದನ್ನು ಬಳಸಿಕೊಂಡು ನಿಮ್ಮದೇ ಕ್ಲೈಂಟ್ ಅನ್ನು ರಚಿಸುವಿರಿ.

ಇದೀಗ ನೀವು ಕರೆ ಮಾಡಬೇಕಾದ ಸರ್ವರ್ ಇಲ್ಲಿದೆ, ಸರ್ವರ್‌ಗೆ ಹೆಚ್ಚು ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಸೇರಿಸಲು ಪ್ರಯತ್ನಿಸಿ.

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

// ಒಂದು ಹೆಚ್ಚಿಸುವ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ಒಂದು ಚಲನೆಯ ಸ್ವಾಗತ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

// stdin ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಸ್ವೀಕರಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು stdout ನಲ್ಲಿ ಸಂದೇಶಗಳನ್ನು ಕಳುಹಿಸುವುದನ್ನು ಪ್ರಾರಂಭಿಸಿ

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

### ಪೈಥಾನ್

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP ಸರ್ವರ್ ರಚಿಸಿ
mcp = FastMCP("Demo")


# ಸೇರ್ಪಡೆ ಉಪಕರಣವನ್ನು ಸೇರಿಸಿ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ಧಾರ್ಮಿಕ ಅಭಿನಂದನೆ ಸಂಪನ್ಮೂಲವನ್ನು ಸೇರಿಸಿ
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

ಈ ಪ್ರಾಜೆಕ್ಟ್ ನೋಡಿ ನೀವು ಹೇಗೆ [ಪ್ರಾಂಪ್ಟ್‌ ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳನ್ನು ಸೇರಿಸಬಹುದು](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

ಮತ್ತೊಮ್ಮೆ ಈ ಲಿಂಕ್ ನೋಡಿ [ಪ್ರಾಂಪ್ಟ್‌ ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳ invoke ಸಾಧನವನ್ನು](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### ರಸ್ಟ್

[ಹಿಂದಿನ ವಿಭಾಗದಲ್ಲಿ](../../../../03-GettingStarted/01-first-server) ನೀವು ರಸ್ಟ್ ಬಳಸಿ ಸರಳ MCP ಸರ್ವರ್ ರಚಿಸುವುದನ್ನು ಕಲಿತಿದ್ದೀರಿ. ನೀವು ಇದನ್ನೇ ಮುಂದುವರಿಸಬಹುದು ಅಥವಾ ಈ ಲಿಂಕ್‌ನಲ್ಲಿ ಹೆಚ್ಚಿನ ರಸ್ಟ್ ಆಧಾರಿತ MCP ಸರ್ವರ್ ಉದಾಹರಣೆಗಳಿವೆ: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ಪರಿಹಾರ

**ಪರಿಹಾರ ಫೋಲ್ಡರ್** ಸಂಪೂರ್ಣ, ಚಲಾಯಿಸಲು ಸಿದ್ಧವಾದ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನಗಳನ್ನು ಒಳಗೊಂಡಿದ್ದು, ಈ ಪಾಠದಲ್ಲಿ ಮೂಡಿಬಂದ ಎಲ್ಲಾ ಕನ್ಸೆಪ್ಟ್‌ಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ. ಪ್ರತಿಯೊಂದು ಪರಿಹಾರವೂ ವಿಭಿನ್ನ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಲ್ಲಿ ಕ್ಲೈಂಟ್ ಮತ್ತು ಸರ್ವರ್ ಕೋಡ್ ಅನ್ನು ಸ್ವತಂತ್ರವಾಗಿ ವ್ಯವಸ್ಥಿತ ಪ್ರಾಜೆಕ್ಟ್ ಆಗಿ ಹೊಂದಿದೆ.

### 📁 ಪರಿಹಾರ ವುಯವಸ್ತೆ

ಪರಿಹಾರ ಡೈರೆಕ್ಟರಿ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಯ ಪ್ರಕಾರ ವ್ಯವಸ್ಥಿತವಾಗಿದೆ:

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

### 🚀 ಪ್ರತಿಯೊಂದು ಪರಿಹಾರದಲ್ಲಿ ಒಳಗೊಂಡಿರುವುದು

ಪ್ರತಿಯೊಂದು ಭಾಷೆಯಿಗಿಂತಾದ ಪರಿಹಾರ ಇವುಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ:

- **ಪೂರ್ಣ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನ** ಪಾಠದ ಎಲ್ಲ ವೈಶಿಷ್ಟ್ಯಗಳೊಂದಿಗೆ
- **ಸಹಜವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಪ್ರಾಜೆಕ್ಟ್ ರಚನೆ** ಮತ್ತು ಅವಲಂಬನೆಗಳು, ಕನ್ಫಿಗರೇಶನ್
- **ನಿರ್ಮಾಣ ಮತ್ತು ಚಾಲನೆ ಸ್ಕ್ರಿಪ್ಟುಗಳು** ಸರಳ ಸ್ಥಾಪನೆ ಮತ್ತು ಕಾರ್ಯಗತಗೊಳಿಸಲು
- **ವಿವರವಾದ README** ಆ ಭಾಷೆಗೆ ವಿಶೇಷ ಸೂಚನೆಗಳೊಂದಿಗೆ
- **ದೋಷ ನಿರ್ವಹಣೆ** ಮತ್ತು ಫಲಿತಾಂಶ ಪ್ರಕ್ರಿಯೆ ಆರ್ಟಿಕೆಗಳು

### 📖 ಪರಿಹಾರಗಳನ್ನು ಬಳಸುವುದು

1. **ನಿಮ್ಮ ಇಚ್ಛಿತ ಭಾಷೆಯ ಫೋಲ್ಡರ್‌ಗೆ ಸಾಗಿರಿ**:

   ```bash
   cd solution/typescript/    # ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್‌ಗೆ
   cd solution/java/          # ಜಾವಾಗೆ
   cd solution/python/        # ಪೈಥಾನ್‌ಗೆ
   cd solution/dotnet/        # .ನೆಟ್‌ಗೆ
   ```

2. **ಪ್ರತಿಯೊಂದು ಫೋಲ್ಡರ್‌ನ README ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿರಿ**:
   - ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸುವುದು
   - ಪ್ರಾಜೆಕ್ಟ್ ನಿರ್ಮಿಸುವುದು
   - ಕ್ಲೈಂಟ್ ಚಾಲನೆ ಮಾಡುವುದು

3. **ನೀವು ಕಾಣಬೇಕಾದ ಉದಾಹರಣಾ output**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ಪೂರ್ಣ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಹಾಗೂ ಹಂತ ಹಂತದ ಮಾರ್ಗದರ್ಶಿಯಿಗಾಗಿ ನೋಡಿ: **[📖 ಪರಿಹಾರ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](./solution/README.md)**

## 🎯 ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು

ಈ ಪಾಠದಲ್ಲಿ ಒಳಗೊಂಡ ಎಲ್ಲಾ ಪ್ರೋಗ್ರಾಮಿಂಗ್ ಭಾಷೆಗಳಿಗಾಗಿ ನಾವು ಪೂರ್ಣ, ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಕ್ಲೈಂಟ್ ಅನುಷ್ಠಾನಗಳನ್ನು ಒದಗಿಸಿದ್ದೇವೆ. ಈ ಉದಾಹರಣೆಗಳು ಮೇಲಿದ್ದ ಎಲ್ಲ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ತೋರಿಸುವುವು ಮತ್ತು ಉಲ್ಲೇಖ ರೂಪದಲ್ಲಿ ಅಥವಾ ನಿಮ್ಮದೇ ಪ್ರಾಜೆಕ್ಟ್ ಆರಂಭಿಸುವ ಮೂಲ ಬಿಂದುವಾಗಿ ಬಳಸಬಹುದು.

### ಲಭ್ಯವಿರುವ ಪೂರ್ಣ ಉದಾಹರಣೆಗಳು

| ಭಾಷೆ | ಫೈಲ್ | ವಿವರಣೆ |
|----------|------|-------------|
| **ಜಾವಾ** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ಸಂಚಾರ ಬಳಸಿ ಸಮಗ್ರ ದೋಷ ನಿರ್ವಹಣೆಯೊಂದಿಗೆ ಪೂರ್ಣ ಜಾವಾ ಕ್ಲೈಂಟ್ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ಸಂಚಾರ ಬಳಸಿ ಸ್ವಯಂಕ್ರಿಯ ಸರ್ವರ್ ಪ್ರಾರಂಭದೊಂದಿಗೆ ಪೂರ್ಣ C# ಕ್ಲೈಂಟ್ |
| **ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP ಪ್ರೋಟೊಕಾಲ್ ಸಂಪೂರ್ಣ ಬೆಂಬಲದೊಂದಿಗೆ ಪೂರ್ಣ ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಲೈಂಟ್ |
| **ಪೈಥಾನ್** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ಮಾದರಿಗಳನ್ನು ಬಳಸುವ ಪೂರ್ಣ ಪೈಥಾನ್ ಕ್ಲೈಂಟ್ |
| **ರಸ್ಟ್** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | ಟೋಕಿಯೊ ಬಳಸಿ async ಕಾರ್ಯಗಳಿಗೆ ಪೂರ್ಣ ರಸ್ಟ್ ಕ್ಲೈಂಟ್ |

ಪ್ರತಿ ಪೂರ್ಣ ಉದಾಹರಣೆಯು ಒಳಗೊಂಡಿದೆ:
- ✅ **ಸಂಪರ್ಕ ಸ್ಥಾಪನೆ** ಮತ್ತು ದೋಷ ನಿರ್ವಹಣೆ  
- ✅ **ಸರ್ವರ್ ಅನ್ವೇಷಣೆ** (ಟೂಲ್ಸ್, ಸಂಪನ್ಮೂಲಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು ಹೊಂದಿದ್ದಲ್ಲಿ)  
- ✅ **ಹಿಸಾಬು ಸಾಧನ ಕಾರ್ಯಕ್ರಮಗಳು** (ಸೇರಿಸುವುದು, ಕಡಿಮೆ ಮಾಡುವುದು, ಗುಣಿಸುವುದು, ಭಾಗಿಸುವುದು, ಸಹಾಯ)  
- ✅ **ಫಲಿತಾಂಶ ಸಂಸ್ಕರಣೆ** ಮತ್ತು ವಿಧಾನಬದ್ಧ ಔಟ್‌ಪುಟ್  
- ✅ **ವಿಸ್ತೃತ ದೋಷ ನಿರ್ವಹಣೆ**  
- ✅ **ಶುದ್ಧ, ಡಾಕ್ಯುಮೆಂಟೆಡ್ ಕೋಡ್** ಹೆಜ್ಜೆ ಹೆಜ್ಜೆ ಟಿಪ್ಪಣಿಗಳೊಂದಿಗೆ  

### ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸುವುದು  

1. ಮೇಲಿನ ಪಟ್ಟಿಯಿಂದ **ನಿಮ್ಮ ಇಷ್ಟದ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ**  
2. **ಸಂಪೂರ್ಣ ಉದಾಹರಣಾ ಫೈಲ್ ಪರಿಶೀಲಿಸಿ** ಸಂಪೂರ್ಣ ಅನುಷ್ಠಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು  
3. [`complete_examples.md`](./complete_examples.md) ನಲ್ಲಿ ಸೂಚನೆಗಳು ನಿರ್ದೇಶನ ಮಾಡುವಂತೆ **ಉದಾಹರಣೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ**  
4. ನಿಮ್ಮ ವಿಶೇಷ ಉಪಯೋಗಕ್ಕಾಗಿ ಉದಾಹರಣೆಯನ್ನು **ತಿದ್ದುಪಡಿ ಮಾಡಿ ಮತ್ತು ವಿಸ್ತರಿಸಿ**  

ಈ ಉದಾಹರಣೆಗಳನ್ನು ಚಲಾಯಿಸುವುದು ಮತ್ತು ಕಸ್ಟಮೈಸ್ ಮಾಡುವ ಬಗ್ಗೆ ವಿವರವಾದ ದಾಖಲೆಗಾಗಿ ನೋಡಿ: **[📖 ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳ ದಾಖಲೆ](./complete_examples.md)**  

### 💡 ಪರಿಹಾರ ಮತ್ತು ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು  

| **ಪರಿಹಾರ ಫೋಲ್ಡರ್** | **ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು** |  
|--------------------|--------------------- |  
| ನಿರ್ಮಾಣ ಕಡತಗಳೊಂದಿಗೆ ಪೂರ್ಣ ಪ್ರಾಜೆಕ್ಟಿನ ರಚನೆ | ಒಂದೇ ಫೈಲ್ ಅನುಷ್ಠಾನಗಳು |  
| ಅವಲಂಬನೆಗಳೊಂದಿಗೆ ರೆಡಿ-ಟು-ರನ್ | ಕೇಂದ್ರೀಕೃತ ಕೋಡ್ ಉದಾಹರಣೆಗಳು |  
| ಉತ್ಪಾದನೆಯಂಥ ಸೆಟಪ್ | ಶೈಕ್ಷಣಿಕ ಉಲ್ಲೇಖ |  
| ಭಾಷಾ-ನಿರ್ದಿಷ್ಟ ಸಾಧನಗಳು | ಬಹುಭಾಷಾ ಹೋಲಿಕೆ |  

ಈ ಎರಡೂ ವಿಧಾನಗಳು ಅಮೂಲ್ಯ - ಪೂರ್ಣ ಪ್ರಾಜೆಕ್ಟ್ಗಾಗಿ **ಪರಿಹಾರ ಫೋಲ್ಡರ್** ಬಳಸಿರಿ ಮತ್ತು ಅಧ್ಯಾಯನ ಮತ್ತು ಉಲ್ಲೇಖಕ್ಕಾಗಿ **ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಗಳು** ಬಳಸಿರಿ.  

## ಮುಖ್ಯ ಅರ್ಥಗಳು  

ಈ ಅಧ್ಯಾಯದ ಮುಖ್ಯ ಅರ್ಥಗಳು ಕ್ಲೈಂಟ್‌ಗಳ ಬಗ್ಗೆ ಇವು:  

- ಸರ್ವರ್‌ನಲ್ಲಿ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಕಂಡುಹಿಡಿಯಲು ಮತ್ತು ಆಮಂತ್ರಿಸಲು ಬಳಸಬಹುದು.  
- ಇದು ಸರ್ವರ್ ಅನ್ನು ಸ್ವಯಂ ಪ್ರಾರಂಭಿಸುವಾಗ (ಈ ಅಧ್ಯಾಯದಲ್ಲಿ ಹಾಗೆಯೇ) ಪ್ರಾರಂಭಿಸಬಹುದು, ಆದರೆ ಕ್ಲೈಂಟ್‌ಗಳು ಕಾರ್ಯನಿರತ ಸರ್ವರ್‌ಗಳಿಗೆ ಕೂಡ ಸಂಪರ್ಕ ಸಾಧಿಸಬಹುದು.  
- ಇಂಟಸ್ಪೆಕ್ಟರ್ ಮೊದಲಿನ ಅಧ್ಯಾಯದಲ್ಲಿ ವಿವರಿಸಿದಂತೆ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪರೀಕ್ಷಿಸುವ ಉತ್ತಮ ಮಾರ್ಗವಾಗಿದೆ.  

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು  

- [MCPನಲ್ಲಿ ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಣ](https://modelcontextprotocol.io/quickstart/client)  

## ಮಾದರಿಗಳು  

- [ಜಾವಾ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../samples/java/calculator/README.md)  
- [.ನೆಟ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)  
- [ಜೆಎಸ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../samples/javascript/README.md)  
- [ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../samples/typescript/README.md)  
- [ಪೈಥಾನ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../../../../03-GettingStarted/samples/python)  
- [ರಸ್ಟ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)  

## ಮುಂದೇನು  

- ಮುಂದಿನದು: [LLM ಸಹಾಯದಿಂದ ಕ್ಲೈಂಟ್ ರಚನೆ](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತ್ಯಜನೆ**:  
ಈ ದಾಖಲೆಯನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ದೃಢತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂದು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲ ದಾಖಲೆಯನ್ನು ಅದರ ಸ್ಥಳೀಯ ಭಾಷೆಯಲ್ಲೇ ಪ್ರಾಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆ ಅಥವಾ误interpretationsಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->