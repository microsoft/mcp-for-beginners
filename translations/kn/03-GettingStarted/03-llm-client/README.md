# LLM ಯೊಂದಿಗೆ ಕ್ಲಯಂಟ್ ರಚಿಸುವುದು

ಈವರೆಗೆ, ನೀವು ಸರ್ವರ್ ಮತ್ತು ಕ್ಲಯಂಟ್ ಅನ್ನು ಹೇಗೆ ರಚಿಸುವುದನ್ನು ನೋಡುತ್ತಿದ್ದೀರಿ. ಕ್ಲಯಂಟ್ ಸ್ಪಷ್ಟವಾಗಿ ಸರ್ವರ್ ಅನ್ನು ಕರೆಮಾಡಿ ಅದರ ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬಹುದಾಗಿದೆ. ಆದರೆ ಇದು ತುಂಬಾ ಪ್ರಾಯೋಗಿಕ ವಿಧಾನವಲ್ಲ. ನಿಮ್ಮ ಬಳಕೆದಾರರು ಏಜೆಂಟಿಕ್ ಯುಗದಲ್ಲಿ ವಾಸಿಸುತ್ತಿದ್ದಾರೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸುತ್ತಾ LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಬೇಕೆಂದು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಅವರು MCP ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಂಗ್ರಹಿಸುವುದು ಅಥವಾ ಇಲ್ಲದಿರುವುದು ಬಗ್ಗೆ ಚಿಂತಿಸುವುದಿಲ್ಲ; ಅವರು ಸಹಜ ಭಾಷೆ ಬಳಸಿ ಸಂವಹನ ಮಾಡಬೇಕೆಂದು ಬಯಸುತ್ತಾರೆ. ಅದನ್ನು ನಾವು ಹೇಗೆ ಪರಿಹರಿಸುವ ಸಮಾಧಾನ? ಪರಿಹಾರವೆಂದರೆ LLM ನ್ನು ಕ್ಲಯಂಟ್ ಗೆ ಸೇರಿಸುವುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ನಿಮಗೆ LLM ಅನ್ನು ಕ್ಲಯಂಟ್ ಗೆ ಸೇರಿಸುವ ಕುರಿತು ಗಮನಹರಿಸುವೆವು ಮತ್ತು ಇದು ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಹೇಗೆ ಉತ್ತಮ ಅನುಭವ ಒದಗಿಸುತ್ತದೆ ಎಂಬುದನ್ನು ತೋರಿಸುವೆವು.

## ಕಲಿಕೆ ಗುರಿಗಳು

ಈ ಪಾಠದ ಅಂತ್ಯದಲ್ಲಿ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- LLM ಜೊತೆಗೆ ಕ್ಲಯಂಟ್ ರಚಿಸುವುದು.
- MCP ಸರ್ವರ್ ಜೊತೆ LLM ಬಳಸಿ ನಿರಂತರ ಸಂವಹನ ಮಾಡುವುದು.
- ಕ್ಲಯಂಟ್ ಬದಿಯ ಅಂತಿಮ ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಉತ್ತಮಗೊಳಿಸುವುದು.

## ವಿಧಾನ

ನಾವು ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಂಡೋಣ. LLM ಸೇರಿಸುವುದು ಸರಳವಾಗಿ ತೋರುತ್ತದೆ, ಆದರೆ ನಿಜವಾಗಿಯೂ ನಾವು ಇದನ್ನು ಮಾಡುತ್ತೇವೆವೇ?

ಇಗೆ ಕ್ಲಯಂಟ್ ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡುವ ವಿಧಾನ:

1. ಸರ್ವರ್ ಜೊತೆ ಸಂಪರ್ಕ ಸ್ಥಾಪನೆ.

1. ಸಾಮರ್ಥ್ಯಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳ ಪಟ್ಟಿ ಮಾಡಿ, ಅವುಗಳ ಸ್ವರೂಪವನ್ನು ಉಳಿಸಿ.

1. LLM ಸೇರಿಸಿ ಮತ್ತು ಅವುಗಳ ಸಾಮರ್ಥ್ಯಗಳು ಹಾಗೂ ಸ್ವರೂಪವನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಫಾರ್ಮ್ಯಾಟ್ ನಲ್ಲಿ ಪಾಸ್ ಮಾಡಿ.

1. ಬಳಕೆದಾರನ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಗೆ ಸಾಗಿಸಿ ಮತ್ತು ಕ್ಲಯಂಟ್ ಪಟ್ಟಿ ಮಾಡಿದ ಸಾಧನಗಳೊಂದಿಗೆ ಹ್ಯಾಂಡಲ್ ಮಾಡುವುದು.

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಉಕ್ಕೇರಿ ಹೇಗೆ ಮಾಡಬೇಕು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇವೆ. ಕೆಳಗಿನ ವ್ಯಾಯಾಮದಲ್ಲಿ ಪ್ರಯತ್ನಿಸೋಣ.

## ವ್ಯಾಯಾಮ: LLM ಜೊತೆ ಕ್ಲಯಂಟ್ ರಚಿಸುವುದು

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನಾವು ನಮ್ಮ ಕ್ಲಯಂಟ್ ಗೆ LLM ಸೇರಿಸಬೇಕು.

### GitHub ಪರ್ಸನಲ್ ಆಕ್ಸೆಸ್ ಟೋಕನ್ ಬಳಸಿ ಪ್ರಾಮಾಣೀಕರಣ

GitHub ಟೋಕನ್ ಸೃಷ್ಟಿಸುವುದು ಸರಳ ಪ್ರಕ್ರಿಯೆ. ನೀವು ಈ ರೀತಿಯಾಗಿ ಮಾಡಬಹುದು:

- GitHub ಸೆಟ್ಟಿಂಗ್‌ಗಳಿಗೆ ಹೋಗಿ – ಮೇಲ್ಭಾಗದ ಬಲಭಾಗದಲ್ಲಿ ಪ್ರೊಫೈಲ್ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ.
- ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳಿಗೆ ನವಿಗೇಟ್ ಮಾಡಿ – ಕೆಳಗೆ ಸ್ಕ್ರಾಲ್ ಮಾಡಿ ಮತ್ತು ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ.
- ಪರ್ಸನಲ್ ಆಕ್ಸೆಸ್ ಟೋಕನ್ಸ್ ಆಯ್ಕೆ ಮಾಡಿ – ಫೈನ್-ಗ್ರೇನ್ಡ್ ಟೋಕನ್ಸ್ ಕ್ಲಿಕ್ ಮಾಡಿ ನಂತರ ನೂತನ ಟೋಕನ್ ರಚಿಸಿ.
- ನಿಮ್ಮ ಟೋಕನ್ ಸಂರಚಿಸಿ – ಸ್ಪಷ್ಟನೆಗಾಗಿ ಟಿಪ್ಪಣಿ ಸೇರಿಸಿ, ಅವಧಿ ನಿಗದಿ ಮಾಡಿ, ಮತ್ತು ಅಗತ್ಯ ಪರವಾನಗಿಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ. ಇಲ್ಲಿ Models ಪರವಾನಗಿಯನ್ನು ಸೇರಿಸುವುದು ಖಚಿತಗೊಳಿಸಿ.
- ಟೋಕನ್ ರಚಿಸಿ ಮತ್ತು ಪ್ರತಿಯನ್ನು ನಕಲಿಸಿ – Generate token ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಕೂಡಲೇ ನಕಲಿಸಿ, ಇದನ್ನು ಮತ್ತೊಮ್ಮೆ ನೋಡಲು ಸಾಧ್ಯವಿಲ್ಲ.

### -1- ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕಿಸಿ

ನಾವು ಮೊದಲಿಗೆ ನಮ್ಮ ಕ್ಲಯಂಟ್ ರಚಿಸೋಣ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ ಜೋಡ್ ಅನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಿ

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- ಅಗತ್ಯಲೈಬ್ರರಿಗಳನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಿದೆವು
- `client` ಮತ್ತು `openai` ಎಂಬ ಎರಡು ಸದಸ್ಯರುಳ್ಳ ಕ್ಲಾಸ್ ರಚಿಸಿದೆವು; ಅವು ನಮ್ಮ ಕ್ಲಯಂಟ್ ನಿರ್ವಹಣೆ ಮತ್ತು LLM ಸಂವಹನಕ್ಕೆ ಸಹಾಯ ಮಾಡುತ್ತವೆ
- GitHub Models ಬಳಕೆಗಾಗಿ LLM ಇನ್‌ಸ್ಟಾನ್ಸ್ ಅನ್ನು `baseUrl` ಅನ್ನು ಇನ್ಫರೆನ್ಸ್ API ನ ಕಡೆ ಸೂಚಿಸುವಂತೆ ಸಂರಚಿಸಿದೆವು

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# ಸ್ಟ್ಡಿಯೋ ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪರಿಮಾಣಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯಾಚರಣೀಯ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ ಆರ್ಗ್ಯೂಮೆಂಟ್ಸ್
    env=None,  # ಐಚ್ಛಿಕ ಪರಿಸರ ಚರಗಳು
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

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- MCP ಗೆ ಅಗತ್ಯಲೈಬ್ರರಿಗಳನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಿದೆವು
- ಕ್ಲಯಂಟ್ ರಚಿಸಿದೆವು

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

ಮೊದಲಿಗೆ, ನಿಮ್ಮ `pom.xml` ಫೈಲ್ ಗೆ LangChain4j ಅವಶ್ಯಕತೆಗಳನ್ನು ಸೇರಿಸಬೇಕು. MCP ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು GitHub Models ಸಹಾಯಕ್ಕಾಗಿ ಈ ಅವಶ್ಯಕತೆಗಳನ್ನು ಸೇರಿಸಿ:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

ಆಮೇಲೆ ನಿಮ್ಮ Java ಕ್ಲಯಂಟ್ ಕ್ಲಾಸ್ ರಚಿಸಿ:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // GitHub ಮಾದರಿಗಳನ್ನು ಬಳಿಸಲು LLM ಅನ್ನು ಸಂರಚಿತ ಮಾಡಿರಿ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವುದಕ್ಕೆ MCP ಸಾರಿಗೆ ರಚಿಸು
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ಗ್ರಾಹಕ ರಚಿಸಿ
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- **LangChain4j ಅವಶ್ಯಕತೆಗಳನ್ನು ಸೇರಿಸಿದ್ದು**: MCP ಇಂಟಿಗ್ರೇಶನ್, OpenAI ಅಧಿಕೃತ ಕ್ಲಯಂಟ್ ಮತ್ತು GitHub Models ಬೆಂಬಲದಿಗಾಗಿ
- **LangChain4j ಲೈಬ್ರರಿಗಳನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಿದ್ದು**: MCP ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು OpenAI ಚಾಟ್ ಮಾಡೆಲ್ ಕಾರ್ಯಾಚರಣೆಗೆ
- **`ChatLanguageModel` ರಚನೆ**: GitHub Models ಬಳಸಿ ನಿಮ್ಮ GitHub ಟೋಕನ್ ಜೊತೆಗೆ ಸಂರಚಿಸಲಾಯಿತು
- **HTTP ಸಂಚಾರವನ್ನು ಸಿದ್ಧಪಡಿಸಿದ್ದು**: SSE ಬಳಸಿ MCP ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕಿಗೊಳಿಸಲು
- **MCP ಕ್ಲಯಂಟ್ ರಚಿಸಲಾಗಿದೆ**: ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂವಹನ ನಿರ್ವಹಿಸಲು
- **LangChain4j ರಚನೆಯ MCP ಬೆಂಬಲವನ್ನು ಉಪಯೋಗಿಸಿದ್ದು**: ಇದು LLM ಮತ್ತು MCP ನಡುವಿನ ಸಂಯೋಜನೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ

#### Rust

ಈ ಉದಾಹರಣೆ ನಿಮಗೆ Rust ಆಧಾರಿತ MCP ಸರ್ವರ್ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆ ಎಂದು فرضಿಸುತ್ತದೆ. ನೀವು ಇನ್ನೊಂದು ಸರ್ವರ್ ಇಲ್ಲದಿದ್ದರೆ, [01-first-server](../01-first-server/README.md) ಪಾಠವನ್ನು ನೋಡಿ ಸರ್ವರ್ ರಚಿಸುವುದನ್ನು ಕಲಿಯಿರಿ.

ನಿಮ್ಮ Rust MCP ಸರ್ವರ್ ರನ್ ಆಗುತ್ತಿರುವ ಡೈರೆಕ್ಟರಿಗೆ ತೆರಳಿ, ಹೊಸ LLM ಕ್ಲಯಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ನಿರ್ವಹಿಸಿ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ನಿಮ್ಮ `Cargo.toml` ಫೈಲ್ ಗೆ ಕೆಳಗಿನ ಅವಶ್ಯಕತೆಗಳನ್ನು ಸೇರಿಸಿ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ಗೆ ಅಧಿಕೃತ Rust ಗ್ರಂಥಾಲಯವಿಲ್ಲ, ಆದಾಗ್ಯೂ, `async-openai` ಕ್ರೇಟ್ ಒಂದು [ಸಮುದಾಯ ನಿರ್ಗಮಿತ ಗ್ರಂಥಾಲಯ](https://platform.openai.com/docs/libraries/rust#rust) ಆಗಿದ್ದು ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ.

`src/main.rs` ಫೈಲ್ ಹೊರೆ ತೆರೆದು, ಅದರಲ್ಲಿ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಬದಲಿಸಿ:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // ಪ್ರಾರಂಭಿಕ ಸಂದೇಶ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ಗ್ರಾಹಕವನ್ನು ಸೆಟ್‌ಅಪ್ ಮಾಡಿ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ಗ್ರಾಹಕವನ್ನು ಸೆಟ್‌ಅಪ್ ಮಾಡಿ
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: MCP ಸಾಧನ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ

    // TODO: ಸಾಧನ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂವಾದ

    Ok(())
}
```

ಈ ಕೋಡ್ ಮೂಲಭೂತ Rust ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತದೆ, ಇದು MCP ಸರ್ವರ್ ಮತ್ತು GitHub Models ನೊಂದಿಗೆ LLM ಸಂವಹನ ಮಾಡಲು ಗ್ರಂಥಾಲಯಗಳನ್ನು ಹೊಂದಿದೆ.

> [!IMPORTANT]
> ಅಪ್ಲಿಕೇಶನ್ ಚಾಲನೆ ಗೆ ಮುಂಚೆ `OPENAI_API_KEY` ಪರಿಸರ変数ವನ್ನು ನಿಮ್ಮ GitHub ಟೋಕನ್‌ನಿಂದ ಸೆಟ್ ಮಾಡಬೇಕಾಗಿದೆ.

ಚೆನ್ನಾಗಿದೆ, ಮುಂದಿನ ಹಂತಕ್ಕೆ, ಸರ್ವರ್ ನಲ್ಲಿ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋಣ.

### -2- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ

ಈಗ ನಾವು ಸರ್ವರ್ ಜೊತೆ ಸಂಪರ್ಕ ಸ್ಥಾಪಿಸಿ ಅದರ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಕೇಳುತ್ತೇವೆ:

#### Typescript

ಅದೇ ಕ್ಲಾಸ್ ನಲ್ಲಿ ಕೆಳಗಿನ ವಿಧಾನಗಳನ್ನು ಸೇರಿಸಿ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲಾಗುತ್ತಿದೆ
    const toolsResult = await this.client.listTools();
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕಿಸಲು `connectToServer` ಕೋಡ್ ಸೇರಿಸಿದ್ದೇವೆ.
- `run` ಎಂಬ ವಿಧಾನ ರಚಿಸಿದ್ದು, ಅದು ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಪ್ರವಾಹವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಧರೆವರೆಗೆ ಇದು ಸಾಧನಗಳನ್ನು ಮಾತ್ರ ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ ಆದರೆ ಮುಂದೆ ಇನ್ನಷ್ಟು ಸೇರಿಸಲಿದ್ದೇವೆ.

#### Python

```python
# ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡು
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡು
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ನಾವು ಸೇರಿಸಿದವು:

- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮುದ್ರಣ ಮಾಡಿದ್ದಾರೆ. ಸಾಧನಗಳಿಗಾಗಿ ನಾವು ನಂತರ ಉಪಯೋಗಿಸುವ `inputSchema` ಸಹ ಪಟ್ಟಿ ಮಾಡಿದೆವು.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್ ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ
- ಪ್ರತಿ ಸಾಧನದ ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಅದರ ಸ್ವರೂಪವನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ. ಈ ಸ್ವರೂಪವನ್ನು ಹೆಚ್ಚಿನಳಿಗೆ ಸಾಧನಗಳನ್ನು ಕರೆಯಲು ಬಳಸುತ್ತೇವೆ.

#### Java

```java
// ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವ ಉಪಕರಣ ಪೂರೈಕೆದಾರರನ್ನು ರಚಿಸಿ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ಉಪಕರಣ ಪೂರೈಕೆದಾರನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
// - MCP ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
// - MCP ಉಪಕರಣ ಛಾಪೆಗಳನ್ನು LangChain4j ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವುದು
// - ಉಪಕರಣ ನಿರ್ವಹಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಂಡುಹಿಡಿಯುವ ಮತ್ತು ನೋಂದಾಯಿಸುವ `McpToolProvider` ರಚಿಸಿದೆವು
- ಸಾಧನ ಪ್ರೊವೈಡರ್ MCP ಸಾಧನ ಸ್ವರೂಪಗಳನ್ನು LangChain4j ಸಾಧನ ಸ್ವರೂಪಕ್ಕೆ ಒಳಗೆ ಹಸ್ತಾಂತರಿಸುತ್ತದೆ
- ಈ ವಿಧಾನದಿಂದ ಸಾಧನ ಪಟ್ಟಿ ಮಾಡುವುದು ಮತ್ತು ಹಸ್ತಾಂತರಣೆಯನ್ನು ಕೈಯಿಂದ ಮಾಡಬೇಕಾಗುವುದಿಲ್ಲ

#### Rust

MCP ಸರ್ವರ್ ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆಯಲು `list_tools` ವಿಧಾನ ಬಳಾಸು ಮಾಡಬಹುದು. `main` ಫಂಕ್ಷನ್ ನಲ್ಲಿ MCP ಕ್ಲಯಂಟ್ ಸೆಟ್ ಅಪ್ ಮಾಡಿಕೊಂಡ ಬಳಿಕ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

```rust
// MCP ಸಾಧನ ಲಿಸ್ಟಿಂಗ್ ಪಡೆಯಿರಿ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು LLM ಸಾಧನಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು

ಸಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ ಮೇಲೆ ಅವುಗಳನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಬೇಕಾಗಿದೆ. ಈ ಪರಿವರ್ತನೆಯಾದ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನಾವು LLM ಗೆ ಸಾಧನಗಳಾಗಿ ಒದಗಿಸುತ್ತೇವೆ.

#### TypeScript

1. MCP ಸರ್ವರ್ ನ ಉತ್ತರವನ್ನು LLM ಬಳಸಬಹುದಾದ ಸಾಧನ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ಇನ್‌ಪುಟ್_schema ಆಧಾರಿತವಾಗಿ ಜೋಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ಟೈಪ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ "ಕಾರ್ಯ"ವಾಗಿ ಸೆಟ್ ಮಾಡಿ
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    ಮೇಲಿನ ಕೋಡ್ MCP ಸರ್ವರ್ ನ ಉತ್ತರವನ್ನು ತೆಗೆದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸಾಧನ ನಿರೂಪಣೆಯಾಗಿ ಪರಿವರ್ತಿಸುತ್ತದೆ.

1. ಮುಂದಾಗಿ `run` ವಿಧಾನವನ್ನು ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವಂತೆ ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ, ನಾವು `run` ವಿಧಾನದಲ್ಲಿ ಫಲಿತಾಂಶ ದಿಂದ ಪ್ರತಿಯೊಂದು ಎಂಟ್ರಿಗೆ `openAiToolAdapter` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತೇವೆ.

#### Python

1. ಮೊದಲು ಕೆಳಗಿನ ಪರಿವರ್ತಕ ಕಾರ್ಯವನ್ನು ರಚಿಸೋಣ:

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    ಮೇಲಿನ `convert_to_llm_tools` ಕಾರ್ಯದಲ್ಲಿ MCP ಸಾಧನ ಪ್ರತಿಕ್ರೀಯೆಯನ್ನು ತೆಗೆದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲಾಗುತ್ತದೆ.

1. ನಂತರ, ನಾವು ನಮ್ಮ ಕ್ಲಯಂಟ್ ಕೋಡ್ ಅನ್ನು ಈ ಕಾರ್ಯವನ್ನು ಬಳಸುವಂತೆ ತಿದ್ದುಪಡಿ ಮಾಡೋಣ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ಇಲ್ಲಿ, ನಾವು MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ನಿಗೆ ನೀಡುವಂತೆ ಪರಿವರ್ತಿಸಲು `convert_to_llm_tool` ಕರೆ ಸೇರಿಸಿದ್ದೇವೆ.

#### .NET

1. MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವ ಕೋಡ್ ಸೇರಿಸೋಣ

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- `ConvertFrom` ಎಂಬ ಕಾರ್ಯವನ್ನು ರಚಿಸಿದ್ದು, ಅದು ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ವರೂಪವನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ.
- ಈ ಕಾರ್ಯ `FunctionDefinition` ರಚಿಸುವ ಮುಖಾಂತರ, ಅದು `ChatCompletionsDefinition` ಗೆ ಪಾಸ್ ಆಗುತ್ತದೆ; ಇದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪ.

1. ಈಗ ಈ ಕಾರ್ಯವನ್ನು ಬಳಸಲು ಕೆಲವು ಇರುವ ಕೋಡ್ ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// ನೈಸರ್ಗಿಕ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಬಾಟ್ ಇಂಟರ್ಫೇಸ್ ರಚಿಸಿ
public interface Bot {
    String chat(String prompt);
}

// LLM ಮತ್ತು MCP ಸಾಧನಗಳೊಂದಿಗೆ AI ಸೇವೆಯನ್ನು ಸಂರಚಿಸಿ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ ನಾವು:

- సహಜ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಸರಳ `Bot` ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ
- LangChain4j ನ `AiServices` ಬಳಸಿ LLM ಹಾಗೂ MCP ಸಾಧನ ಪ್ರೊವೈಡರ್ ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬಂಧಿಸಿದೆವು
- ಫ್ರೇಮ್‌ವರ್ಕ್ ಸಾಧನ ಸ್ವರೂಪ ಪರಿವರ್ತನೆ ಮತ್ತು ಕಾರ್ಯಪಾಲನೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ
- ಈ ವಿಧಾನದಿಂದ MCP ಸಾಧನಗಳ ಕೈಯಿಂದ ಪರಿವರ್ತನೆ ಅಗತ್ಯವಿಲ್ಲ - LangChain4j ಸಕಲದರ ಸುದೀರ್ಢಗೆತುಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ

#### Rust

MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ಸಹಾಯಕ ಕಾರ್ಯವನ್ನು ಸೇರಿಸೋಣ. ನಿಮ್ಮ `main.rs` ನಲ್ಲಿ `main` функцияನ ಕೆಳಗೆ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ. ಇದು LLM ಪ್ರಶ್ನೆಗಳಿಗೆ ಹಕ್ಕುಮಾಡುವಾಗ ಕರೆಮಾಡಲಾಗುತ್ತದೆ:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಬಳಕೆದಾರರ ವಿನಂತಿಗಳನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡಲು ಸಿದ್ಧರಾಗಿದ್ದೇವೆ. ಮುಂದುವರಿಯೋಣ.

### -4- ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿ ಹ್ಯಾಂಡಲ್ ಮಾಡುವುದು

ಈ ಭಾಗದಲ್ಲಿ, ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ಸಂವಹನ ಮಾಡೋಣ.

#### TypeScript

1. LLM ಅನ್ನು ಕರೆಮಾಡಲು ಬಳಸದಂತಹ ವಿಧಾನ ಸೇರಿಸೋಣ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ಸರ್ವರ್‌ನ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
        // ಮಾಡಬೇಕಿದೆ

        }
    }
    ```

    ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

    - `callTools` ಎಂಬ ವಿಧಾನ ಸೇರಿಸಲಾಗಿದೆ.
    - LLM ಉತ್ತರಗೊಳ್ಳುವ ಮೂಲಕ ಯಾವ ಸಾಧನಗಳನ್ನು ಕರೆಯಬೇಕಾಗುತ್ತದೆ ಎಂದು ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ಉಪಕರಣವನ್ನು ಕರೆಯಿರಿ
        }
        ```

    - LLM ಸೂಚಿಸಿದರೆ ಸಾಧನವನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ:

        ```typescript
        // 2. ಸರ್ವರ್ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
        // ಮಾಡಬೇಕಿದೆ
        ```

1. `run` ವಿಧಾನವನ್ನು LLM ಕರೆ ಮತ್ತು `callTools` ಅನ್ನು ಸೇರಿಸಲು ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```typescript

    // 1. LLMಗೆ ಇನ್‌ಪುಟ್ ಆಗುವ ಸಂದೇಶಗಳನ್ನು ರಚಿಸಿ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ಅನ್ನು ಕರೆಮಾಡುವುದು
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, pratyeka ಆಯ್ಕೆಗಾಗಿ, ಅದು ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ಹೊಂದಿದೆಯೇ ಎಂದು പരിശോധಿಸಿ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ಚೆನ್ನಾಗಿದೆ, ಸಂಪೂರ್ಣ ಕೋಡ್ ಇಲ್ಲಿದೆ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ zod ಅನ್ನು ಆಮದುಮಾಡಿ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ಭವಿಷ್ಯದಲ್ಲಿ ಈ URL ಗೆ ಬದಲಾಗಬೇಕಾಗಬಹುದು: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // input_schema ಆಧಾರದ ಮೇಲೆ zod ಸ್ಕೀಮಾ ರಚಿಸಿ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರಕಾರವನ್ನು "function" ಎಂದು ಸೆಟ್ ಮಾಡಿ
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. ಸರ್ವರ್‌ನ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
          // ಮಾಡಲು ಇರುವುದು
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ ಉಪಕರಣ ಕರೆಗಳಿರುವುದರ ಪರಿಶೀಲನೆ ಮಾಡಿ
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. LLM ಕರೆ ಮಾಡಲು ಅಗತ್ಯವಿರುವ ಇಂಪೋರ್ಟ್‌ಗಳು ಸೇರಿಸೋಣ:

    ```python
    # ಎಲ್‌ಎಲ್ಎಂ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ನಂತರ, LLM ಗೆ ಕರೆಮಾಡುವ ಕಾರ್ಯ ಸೇರಿಸೋಣ:

    ```python
    # ಎಲ್‌ಎಲ್‌ಎಮ್

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # ಐಚ್ಛಿಕ ಪರಿಮಾಣಗಳು
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

    - MCP ಸರ್ವರ್ ನಿಂದ ಕಂಡುಹಿಡಿದ ಕಾರ್ಯಗಳನ್ನೂ ಅಪ್‌ಡೇಟ್ ಮಾಡಿ, ಅವುಗಳನ್ನು LLM ಗೆ ನೀಡಲಾಗಿದೆ.
    - ಆ ಬಳಿಕ ಆ ಕಾರ್ಯಗಳೊಂದಿಗೆ LLMನ್ನು ಕರೆಮಾಡಲಾಗಿದೆ.
    - ಫಲಿತಾಂಶವನ್ನು ತಪಾಸಣೆಮಾಡಿ ಯಾವ ಕಾರ್ಯಗಳನ್ನು ಕರೆಮಾಡಬೇಕೆಂದು ನೋಡಿ.
    - ಕೊನೆಗೆ ಕರೆಯಬೇಕಾದ ಕಾರ್ಯಗಳ ಪಟ್ಟಿಯನ್ನು ಭೇದಿಸಿದೆ.

1. ಕೊನೆಯಲ್ಲಿ, ಮುಖ್ಯ ಕೋಡ್ ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```python
    prompt = "Add 2 to 20"

    # LLM ಅನ್ನು ಕೇಳಿ ಎಲ್ಲಾ ಉಪಕರಣಗಳನ್ನು, ಇದ್ದರೆ ಏನೇನಾದರೂ
    functions_to_call = call_llm(prompt, functions)

    # ಸೂಚಿಸಿದ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಕರೆಸಿಕೊಳ್ಳಿ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ಕೊನೆಯ ಹಂತ; ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

    - LLM ಸೂಚಿಸಿರುವಂತೆ ಕಾರ್ಯವನ್ನು `call_tool` ಮೂಲಕ MCP ಸಾಧನಕ್ಕೆ ಕರೆ ಮಾಡಿ.
    - ಸಾಧನದ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುತ್ತಿದೆ.

#### .NET

1. LLM ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿ ಮಾಡಲು ಕೆಲವು ಕೋಡ್ ನೋಡೋಣ:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

    - MCP ಸರ್ವರ್ ನಿಂದ ಸಾಧನಗಳನ್ನು ತರಲಾಗಿದೆ, `var tools = await GetMcpTools()`.
    - ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ `userMessage` ಆಗಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿದೆ.
    - ಮಾಡೆಲ್ ಮತ್ತು ಸಾಧನಗಳ ಸೂಚನೆಗಳೊಂದಿಗೆ ಆಯ್ಕೆಗಳನ್ನು ತಯಾರಿಸಿ.
    - LLM ಗೆ ವಿನಂತಿ ಮಾಡಲಾಗಿದೆ.

1. ಕೊನೆಗೆ, LLM ಕಾರ್ಯವಿನಂತಿ ಮಾಡಬೇಕೆಂದು ನೀವು ತೀರ್ಮಾನಿಸಿದೆಯೇಂದು ನೋಡೋಣ:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

    - ಕಾರ್ಯಗಳ ಪಟ್ಟಿಯನ್ನು ಲೂಪ್ ಮಾಡಿದ್ರೆ.
    - ಪ್ರತಿ ಕಾರ್ಯದ ಹೆಸರು ಮತ್ತು ಅರ್ಗುಮೆಂಟ್ಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ, MCP ಸರ್ವರ್ ನಲ್ಲಿ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಿ. ಫಲಿತಾಂಶ ಮುದ್ರಿಸಲಾಗಿದೆ.

ಸಂಪೂರ್ಣ ಕೋಡ್ ಇಲ್ಲಿದೆ:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ ಸಹಜ ಭಾಷಾ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಿ
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

ಮೇಲಿನ ಕೋಡ್ ನಲ್ಲಿ:

- ಸರಳ ಸಹಜ ಭಾಷೆ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ MCP ಸರ್ವರ್ ಸಾಧನಗಳ ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲಾಗಿದೆ
- LangChain4j ಫ್ರೇಮ್‌ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
  - ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸಾಧನ ಕರೆಗೆ ಪರಿವರ್ತಿಸುವುದು
  - LLM ನ ನಿರ್ಧಾರದಿಂದ ಸೂಕ್ತ MCP ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವುದು
  - LLM ಮತ್ತು MCP ನಡುವೆ ಸಂಭಾಷಣೆ ಪ್ರವಾಹವನ್ನು ನಿರ್ವಹಿಸುವುದು
- `bot.chat()` ವಿಧಾನ MCP ಸಾಧನಗಳ ಫಲಿತಾಂಶಗಳನ್ನು ಸಹ ಒಳಗೊಂಡ ಸಹಜ ಭಾಷೆ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡುತ್ತದೆ
- ಬಳಕೆದಾರರು MCP ಅನುಷ್ಠಾನವನ್ನು ತಿಳಿಯದೇ ಸಹಜ ಅನುಭವ ಪಡೆಯುತ್ತಾರೆ

ಸಂಪೂರ್ಣ ಉದಾಹರಣೆಯ ಕೋಡ್:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

ಇಲ್ಲಿ ಮುಖ್ಯ ಕೆಲಸಗಳು ನಡೆಯುತ್ತವೆ. ನಾವು ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ನೊಂದಿಗೆ LLM ನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ, ನಂತರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾರಾದರೂ ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡಬೇಕಿದೆಯೆಂದು ನೋಡುತ್ತೇವೆ. ಹಾಗಿದ್ದರೆ, ನಾವು ಆ ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡಿ, LLM ಜೊತೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸುತ್ತೇವೆ, ಮತ್ತಷ್ಟು ಸಾಧನ ಕರೆಗಳ ಅಗತ್ಯವಿಲ್ಲದವರೆಗೆ ಮತ್ತು ಕೊನೆಗೆ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆ ಸಿಗುವವರೆಗೆ.

ನಾವು LLM ಗೆ ಹಲವು ಬಾರಿ ಕರೆಮಾಡಲಿದ್ದೇವೆ, ಆದ್ದರಿಂದ LLM ಕರೆ ನಿರ್ವಹಿಸುವ ಕಾರ್ಯವೊಂದನ್ನು ವ್ಯಾಖ್ಯಾನಿಸೋಣ. `main.rs` ಗೆ ಕೆಳಗಿನ ಕಾರ್ಯ ಸೇರಿಸಿ:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

ಈ ಕಾರ್ಯ LLM ಕ್ಲಯಂಟ್, ಸಂದೇಶಗಳ ಪಟ್ಟಿಯನ್ನು (ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಸೇರಿ), MCP ಸರ್ವರ್‌ನ ಸಾಧನಗಳನ್ನು ತೆಗೆದು LLM ಗೆ ವಿನಂತಿ ಕಳುಹಿಸಿ ಪ್ರತಿಕ್ರಿಯೆ ನೀಡುತ್ತದೆ.
LLM ನಿಂದ ಬಂದಿರುವ ಪ್ರತಿಕ್ರಿಯೆಯಲ್ಲಿ `choices` ಎಂಬ ತರತಂಜಿಯೊಂದಿದೆ. ಯಾವುದೇ `tool_calls` ಇದ್ದರೆ ಅದರ نتیಜೆಗಳನ್ನು ನಾವು ಪ್ರಕ್ರಿಯೆ ಮಾಡಬೇಕಾಗುತ್ತದೆ. ಇದು ನಮಗೆ ತಿಳಿಸುತ್ತದೆ LLM ವಿಶೇಷ ಸಾಧನವನ್ನು ಕರೆಯಲು ಅರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಕೇಳುತ್ತಿದೆ. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸಲು `main.rs` ಫೈಲ್‌ನ ತಳಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡನ್ನು ಸೇರಿಸಿ:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // ವಿಷಯ ಲಭ್ಯವಿದ್ದರೆ ಮುದ್ರಿಸಿ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ಉಪಕರಣ ಕರೆಗೆಲೆನ್ನು ಕಾರ್ಯನಿರ್ವಹಿಸಿ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ಸಹಾಯಕ ಸಂದೇಶವನ್ನು ಸೇರಿಸಿ

        // ಪ್ರತಿ ಉಪಕರಣ ಕರೆನಡಿಸುವುದು
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ಸಂದೇಶಗಳಿಗೆ ಉಪಕರಣ ಫಲಿತಾಂಶ ಸೇರಿಸಿ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ಉಪಕರಣ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರಿಸಿ
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```

`tool_calls` ಇದ್ದರೆ, ಅದು ಸಾಧನ ಮಾಹಿತಿ ತೆಗೆದುಹಾಕುತ್ತದೆ, MCP ಸರ್ವರ್‌ನೊಂದಿಗೆ ಸಾಧನ ವಿನಂತಿಯನ್ನು ಕರೆದರೆ, ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಭಾಷಣಾ ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸುತ್ತದೆ. ನಂತರ LLM ಜೊತೆಗೆ ಸಂಭಾಷಣೆ ಮುಂದುವರಿ, ಮತ್ತು ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಸಾಧನ ಕರೆ ಫಲಿತಾಂಶಗಳಿಂದ ಸಂದೇಶಗಳು ನವೀಕರಿಸಲ್ಪಡುತ್ತವೆ.

LLM MCP ಕರೆಗಳಿಗೆ ತಲುಪಿಸಿದ ಸಾಧನ ಕರೆ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದುಹಾಕಲು ಇನ್ನೊಂದು ಸಹಾಯಕರ ಕಾರ್ಯನಿರ್ವಹಣೆಯನ್ನು ಸೇರಿಸೋಣ. `main.rs` ಫೈಲ್‌ನ ತಳಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡನ್ನು ಸೇರಿಸಿ:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```

ಎಲ್ಲಾ ಭಾಗಗಳು ಸಿದ್ಧವಾದ ಮೇಲೆ, ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ കൈಗಾರಿಕೆ ಮಾಡೋಣ ಮತ್ತು LLM ಅನ್ನು ಕರೆಮಾಡೋಣ. ನಿಮ್ಮ `main` ಕಾರ್ಯವನ್ನು ಕೆಳಗಿನ ಕೋಡಿನಿಂದ ನವೀಕರಿಸಿ:

```rust
// ಉಪಕರಣ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂಭಾಷಣೆ
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```

ಇದು LLM ಗೆ ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಮೂಲಕ ಎರಡು ಸಂಖ್ಯೆಗಳಲ್ಲಿ ಮೊತ್ತ ಕೇಳುವುದು, ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಸಾಧನ ಕರೆಗಳನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ.

ಶ್ರೇಷ್ಠ, ನೀವು ಯಶಸ್ವಿಯಾಗಿ ಮಾಡಿದ್ದೀರಿ!

## ನಿಯೋಜನೆ

ಅಭ್ಯಾಸದಿಂದ ಕೋಡನ್ನು ತೆಗೆದು, ಸ್ವಲ್ಪ ಹೆಚ್ಚು ಸಾಧನಗಳೊಂದಿಗೆ ಸರ್ವರ್ ಅನ್ನು ನಿರ್ಮಿಸಿ. ನಂತರ LLM ಇದ್ದ ಕ್ಲಯಿಂಟ್ ಅನ್ನು ನಿರ್ಮಿಸಿ, ಮತ್ತು ವಿವಿಧ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ ಎಲ್ಲಾ ಸರ್ವರ್ ಸಾಧನಗಳು ಡೈನಾಮಿಕ್ ಆಗಿ ಕರೆಮಾಡುತ್ತವೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಇಂತಹ ಕ್ಲಯಿಂಟ್ ನಿರ್ಮಾಣ ವಿಧಾನವು ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವ ನೀಡುತ್ತದೆ ಏಕೆಂದರೆ ಅವರು ನಿಖರ ಕ್ಲಯಿಂಟ್ ಆಜ್ಞೆಗಳ ಬದಲಿ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ ಮತ್ತು ಯಾವುದೇ MCP ಸರ್ವರ್ ಕರೆಗಳು ನಡೆದಿರುವುದನ್ನು ಗಮನಿಸದಿರುತ್ತಾರೆ.

## ಪರಿಹಾರ

[Solution](./solution/README.md)

## ಪ್ರಮುಖ ಪಾಠಗಳು

- ನಿಮ್ಮ ಕ್ಲಯಿಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದು ಬಳಕೆದಾರರಿಗೆ MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಉತ್ತಮ ವಿರೂಪಣೆ ಕೊಡುತ್ತದೆ.
- MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಆಯ್ಕೆಮಾಡಬಹುದಾದ ರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವ ಅಗತ್ಯವಿದೆ.

## ಉದಾಹರಣೆಗಳು

- [ಜಾವಾ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.ನೆಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [ಪೈಥಾನ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)
- [ರಸ್ಟು ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

## ಮುಂದೇನು

- ಮುಂದಿನದು: [ವಿಶುಯಲ್ ಸ್ಟುಡಿಯೋ ಕೋಡ್ ಬಳಸಿ ಸರ್ವರ್ ಉಪಯೋಗಿಸುವುದು](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರವು**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿರ್ವಹಿಸುವ ಯತ್ನವೂAccuracyಗಾಗಿ ಆದರೆ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು. ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅದರ مادರ ಜೀವಿತ ಭಾಷೆಯಲ್ಲಿ ಅಧಿಕಾರಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದ ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಗೊಂದಲಗಳು ಅಥವಾ ತಪ್ಪು ಅರ್ಥಗಳ ಕುರಿತು ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->