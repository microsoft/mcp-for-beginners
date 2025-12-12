<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d846ebb88fbb0f00549e2ff8cc3f746",
  "translation_date": "2025-12-11T11:48:05+00:00",
  "source_file": "03-GettingStarted/03-llm-client/README.md",
  "language_code": "kn"
}
-->
# LLM ಜೊತೆಗೆ ಕ್ಲೈಂಟ್ ರಚನೆ

ಇದುವರೆಗೆ, ನೀವು ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೇಗೆ ರಚಿಸುವುದನ್ನು ನೋಡಿದ್ದೀರಿ. ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಕರೆಮಾಡಿ ಅದರ ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬಹುದು. ಆದಾಗ್ಯೂ, ಇದು ಬಹಳ ಪ್ರಾಯೋಗಿಕ ವಿಧಾನವಲ್ಲ. ನಿಮ್ಮ ಬಳಕೆದಾರರು ಏಜೆಂಟಿಕ್ ಯುಗದಲ್ಲಿ ವಾಸಿಸುತ್ತಿದ್ದಾರೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಲು ಮತ್ತು LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ನೀವು MCP ಬಳಸಿದೀರಾ ಅಥವಾ ಇಲ್ಲವೇ ಎಂಬುದಕ್ಕೆ ತಾಳ್ಮೆ ಇಲ್ಲ, ಆದರೆ ಅವರು ಸಹಜ ಭಾಷೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಹಾಗಾದರೆ ನಾವು ಇದನ್ನು ಹೇಗೆ ಪರಿಹರಿಸಬಹುದು? ಪರಿಹಾರವೆಂದರೆ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಅನ್ನು ಸೇರಿಸುವುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ನಿಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಅನ್ನು ಸೇರಿಸುವುದರ ಮೇಲೆ ಗಮನಹರಿಸುತ್ತೇವೆ ಮತ್ತು ಇದು ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಹೇಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ ಎಂಬುದನ್ನು ತೋರಿಸುತ್ತೇವೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ, ನೀವು ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- LLM ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ರಚಿಸುವುದು.
- LLM ಬಳಸಿ MCP ಸರ್ವರ್ ಜೊತೆಗೆ ನಿರಂತರ ಸಂವಹನ ಮಾಡುವುದು.
- ಕ್ಲೈಂಟ್ ಬದಿಯಲ್ಲಿ ಉತ್ತಮ ಅಂತಿಮ ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಒದಗಿಸುವುದು.

## ವಿಧಾನ

ನಾವು ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ. LLM ಸೇರಿಸುವುದು ಸರಳವಾಗಿ ಕೇಳುತ್ತದೆ, ಆದರೆ ನಾವು ನಿಜವಾಗಿಯೂ ಇದನ್ನು ಮಾಡುತ್ತೇವೇ?

ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಜೊತೆಗೆ ಹೇಗೆ ಸಂವಹನ ಮಾಡುತ್ತದೆ ಎಂಬುದು ಹೀಗಿದೆ:

1. ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂಪರ್ಕ ಸ್ಥಾಪಿಸಿ.

1. ಸಾಮರ್ಥ್ಯಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ, ಮತ್ತು ಅವುಗಳ ಸ್ಕೀಮಾವನ್ನು ಉಳಿಸಿ.

1. LLM ಸೇರಿಸಿ ಮತ್ತು ಉಳಿಸಿದ ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಅವುಗಳ ಸ್ಕೀಮಾವನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪದಲ್ಲಿ ಪಾಸ್ ಮಾಡಿ.

1. ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಗೆ ಮತ್ತು ಕ್ಲೈಂಟ್ ಪಟ್ಟಿ ಮಾಡಿದ ಸಾಧನಗಳೊಂದಿಗೆ ಹ್ಯಾಂಡಲ್ ಮಾಡಿ.

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಇದನ್ನು ಉನ್ನತ ಮಟ್ಟದಲ್ಲಿ ಹೇಗೆ ಮಾಡಬಹುದು ಎಂದು ಅರ್ಥಮಾಡಿಕೊಂಡಿದ್ದೇವೆ, ಕೆಳಗಿನ ವ್ಯಾಯಾಮದಲ್ಲಿ ಇದನ್ನು ಪ್ರಯತ್ನಿಸೋಣ.

## ವ್ಯಾಯಾಮ: LLM ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ರಚನೆ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನಾವು ನಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದನ್ನು ಕಲಿಯೋಣ.

### GitHub ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ ಬಳಸಿ ಪ್ರಾಮಾಣೀಕರಣ

GitHub ಟೋಕನ್ ರಚಿಸುವುದು ಸರಳ ಪ್ರಕ್ರಿಯೆ. ನೀವು ಇದನ್ನು ಹೀಗೆ ಮಾಡಬಹುದು:

- GitHub ಸೆಟ್ಟಿಂಗ್ಸ್‌ಗೆ ಹೋಗಿ – ಮೇಲ್ಭಾಗದ ಬಲಭಾಗದಲ್ಲಿ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಸ್ ಆಯ್ಕೆಮಾಡಿ.
- ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಸ್‌ಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ – ಕೆಳಗೆ ಸ್ಕ್ರೋಲ್ ಮಾಡಿ ಮತ್ತು ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
- ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್‌ಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ – ಫೈನ್-ಗ್ರೇನ್ಡ್ ಟೋಕನ್‌ಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ನಂತರ ಹೊಸ ಟೋಕನ್ ರಚಿಸಿ.
- ನಿಮ್ಮ ಟೋಕನ್ ಅನ್ನು ಸಂರಚಿಸಿ – ಉಲ್ಲೇಖಕ್ಕಾಗಿ ಟಿಪ್ಪಣಿ ಸೇರಿಸಿ, ಅವಧಿ ನಿಗದಿ ಮಾಡಿ ಮತ್ತು ಅಗತ್ಯವಿರುವ ಪರವಾನಗಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ. ಈ ಸಂದರ್ಭದಲ್ಲಿ Models ಪರವಾನಗಿಯನ್ನು ಸೇರಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
- ಟೋಕನ್ ರಚಿಸಿ ಮತ್ತು ನಕಲಿಸಿ – ರಚಿಸಿ ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ತಕ್ಷಣ ನಕಲಿಸಿ, ಏಕೆಂದರೆ ನೀವು ಅದನ್ನು ಮತ್ತೆ ನೋಡಲು ಸಾಧ್ಯವಿಲ್ಲ.

### -1- ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ

ಮೊದಲು ನಮ್ಮ ಕ್ಲೈಂಟ್ ರಚಿಸೋಣ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ zod ಅನ್ನು ಆಮದುಮಾಡಿ

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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- `client` ಮತ್ತು `openai` ಎಂಬ ಎರಡು ಸದಸ್ಯರೊಂದಿಗೆ ಕ್ಲಾಸ್ ರಚಿಸಿದ್ದೇವೆ, ಇದು ನಮ್ಮ ಕ್ಲೈಂಟ್ ನಿರ್ವಹಣೆ ಮತ್ತು LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- ನಮ್ಮ LLM ಉದಾಹರಣೆಯನ್ನು GitHub Models ಬಳಸಲು `baseUrl` ಅನ್ನು ಇನ್ಫರೆನ್ಸ್ API ಗೆ ಸೂಚಿಸುವಂತೆ ಸಂರಚಿಸಿದ್ದೇವೆ.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪರಿಮಾಣಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯನಿರ್ವಹಣೀಯ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ ಆರ್ಗ್ಯುಮೆಂಟ್ಸ್
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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಗೆ ಅಗತ್ಯವಿರುವ ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- ಕ್ಲೈಂಟ್ ರಚಿಸಿದ್ದೇವೆ

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

#### Java

ಮೊದಲು, ನಿಮ್ಮ `pom.xml` ಫೈಲ್‌ಗೆ LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಬೇಕು. MCP ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು GitHub Models ಬೆಂಬಲವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು ಈ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

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

ನಂತರ ನಿಮ್ಮ Java ಕ್ಲೈಂಟ್ ಕ್ಲಾಸ್ ರಚಿಸಿ:

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
    
    public static void main(String[] args) throws Exception {        // GitHub ಮಾದರಿಗಳನ್ನು ಬಳಸಲು LLM ಅನ್ನು ಸಂರಚಿಸಿ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು MCP ಸಾರಿಗೆ ರಚಿಸಿ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿ
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- **LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿದ್ದೇವೆ**: MCP ಇಂಟಿಗ್ರೇಶನ್, OpenAI ಅಧಿಕೃತ ಕ್ಲೈಂಟ್ ಮತ್ತು GitHub Models ಬೆಂಬಲಕ್ಕಾಗಿ
- **LangChain4j ಲೈಬ್ರರಿಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ**: MCP ಇಂಟಿಗ್ರೇಶನ್ ಮತ್ತು OpenAI ಚಾಟ್ ಮಾದರಿ ಕಾರ್ಯಕ್ಷಮತೆಗಾಗಿ
- **`ChatLanguageModel` ರಚಿಸಿದ್ದೇವೆ**: GitHub Models ಬಳಸಲು ನಿಮ್ಮ GitHub ಟೋಕನ್ ಜೊತೆಗೆ ಸಂರಚಿಸಲಾಗಿದೆ
- **HTTP ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್ ಸೆಟ್ ಮಾಡಿದ್ದೇವೆ**: MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು Server-Sent Events (SSE) ಬಳಸಿ
- **MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿದ್ದೇವೆ**: ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂವಹನ ನಿರ್ವಹಿಸಲು
- **LangChain4j ನ ನಿರ್ಮಿತ MCP ಬೆಂಬಲವನ್ನು ಬಳಸಿದ್ದೇವೆ**: ಇದು LLM ಮತ್ತು MCP ಸರ್ವರ್‌ಗಳ ನಡುವಿನ ಇಂಟಿಗ್ರೇಶನ್ ಸರಳಗೊಳಿಸುತ್ತದೆ

#### Rust

ಈ ಉದಾಹರಣೆ ನಿಮ್ಮ ಬಳಿ Rust ಆಧಾರಿತ MCP ಸರ್ವರ್ ಇದ್ದರೆ ಎಂದು ಊಹಿಸುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ, ಸರ್ವರ್ ರಚಿಸಲು [01-first-server](../01-first-server/README.md) ಪಾಠವನ್ನು ನೋಡಿ.

ನಿಮ್ಮ Rust MCP ಸರ್ವರ್ ಇದ್ದ ಮೇಲೆ, ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಸರ್ವರ್ ಇರುವ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿಗೆ ಹೋಗಿ. ನಂತರ ಹೊಸ LLM ಕ್ಲೈಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ರನ್ ಮಾಡಿ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ನಿಮ್ಮ `Cargo.toml` ಫೈಲ್‌ಗೆ ಕೆಳಗಿನ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ಗೆ ಅಧಿಕೃತ Rust ಲೈಬ್ರರಿ ಇಲ್ಲ, ಆದರೆ `async-openai` ಕ್ರೇಟ್ ಒಂದು [ಸಮುದಾಯ ನಿರ್ವಹಿತ ಲೈಬ್ರರಿ](https://platform.openai.com/docs/libraries/rust#rust) ಆಗಿದ್ದು ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ.

`src/main.rs` ಫೈಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಅದರ ವಿಷಯವನ್ನು ಕೆಳಗಿನ ಕೋಡ್‌ನೊಂದಿಗೆ ಬದಲಾಯಿಸಿ:

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
    // ಪ್ರಾಥಮಿಕ ಸಂದೇಶ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ
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

    // TODO: MCP ಸಾಧನ ಪಟ್ಟಿ ಪಡೆಯಿರಿ

    // TODO: ಸಾಧನ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂಭಾಷಣೆ

    Ok(())
}
```

ಈ ಕೋಡ್ ಮೂಲಭೂತ Rust ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತದೆ, ಇದು MCP ಸರ್ವರ್ ಮತ್ತು GitHub Models ಜೊತೆಗೆ LLM ಸಂವಹನ ಮಾಡಲು ಸಂಪರ್ಕಿಸುತ್ತದೆ.

> [!IMPORTANT]
> ಅಪ್ಲಿಕೇಶನ್ ರನ್ ಮಾಡುವ ಮೊದಲು ನಿಮ್ಮ GitHub ಟೋಕನ್ ಬಳಸಿ `OPENAI_API_KEY` ಪರಿಸರ ಚರವನ್ನು ನಿಗದಿಪಡಿಸಬೇಕು.

ಚೆನ್ನಾಗಿದೆ, ಮುಂದಿನ ಹಂತಕ್ಕೆ, ಸರ್ವರ್‌ನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋಣ.

### -2- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು

ಈಗ ನಾವು ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಿ ಅದರ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಕೇಳುತ್ತೇವೆ:

#### Typescript

ಅದೇ ಕ್ಲಾಸ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ವಿಧಾನಗಳನ್ನು ಸೇರಿಸಿ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲಾಗುತ್ತಿದೆ
    const toolsResult = await this.client.listTools();
}
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವ ಕೋಡ್ `connectToServer` ಸೇರಿಸಿದ್ದೇವೆ.
- ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಫ್ಲೋ ನಿರ್ವಹಿಸುವ `run` ವಿಧಾನ ರಚಿಸಿದ್ದೇವೆ. ಇದುವರೆಗೆ ಇದು ಸಾಧನಗಳನ್ನು ಮಾತ್ರ ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ, ಆದರೆ ನಾವು ಶೀಘ್ರದಲ್ಲೇ ಇನ್ನಷ್ಟು ಸೇರಿಸುವೆವು.

#### Python

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
    print("Tool", tool.inputSchema["properties"])
```

ನಾವು ಸೇರಿಸಿದ್ದದ್ದು:

- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮುದ್ರಿಸಿದ್ದೇವೆ. ಸಾಧನಗಳಿಗಾಗಿ ನಾವು ನಂತರ ಬಳಸುವ `inputSchema` ಕೂಡ ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ.

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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ
- ಪ್ರತಿ ಸಾಧನದ ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಅದರ ಸ್ಕೀಮಾವನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ. ಇದನ್ನು ನಾವು ಶೀಘ್ರದಲ್ಲೇ ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡಲು ಬಳಸುತ್ತೇವೆ.

#### Java

```java
// ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಸಾಧನಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವ ಸಾಧನ ಪೂರೈಕೆದಾರರನ್ನು ರಚಿಸಿ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ಸಾಧನ ಪೂರೈಕೆದಾರರು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತಾರೆ:
// - MCP ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
// - MCP ಸಾಧನ ಸ್ಕೀಮಾಗಳನ್ನು LangChain4j ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವುದು
// - ಸಾಧನ ಕಾರ್ಯಾಚರಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಂಡುಹಿಡಿದು ನೋಂದಾಯಿಸುವ `McpToolProvider` ರಚಿಸಿದ್ದೇವೆ
- ಸಾಧನದ ಸ್ಕೀಮಾ ಮತ್ತು LangChain4j ಸಾಧನ ಸ್ವರೂಪದ ನಡುವಿನ ಪರಿವರ್ತನೆಯನ್ನು ಸಾಧನ ಪೂರೈಕೆದಾರ ಆಂತರಿಕವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ
- ಈ ವಿಧಾನವು ಕೈಯಿಂದ ಸಾಧನ ಪಟ್ಟಿ ಮತ್ತು ಪರಿವರ್ತನೆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅಡಗಿಸುತ್ತದೆ

#### Rust

MCP ಸರ್ವರ್‌ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆಯಲು `list_tools` ವಿಧಾನವನ್ನು ಬಳಸಲಾಗುತ್ತದೆ. ನಿಮ್ಮ `main` ಫಂಕ್ಷನ್‌ನಲ್ಲಿ MCP ಕ್ಲೈಂಟ್ ಸಿದ್ಧಪಡಿಸಿದ ನಂತರ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

```rust
// MCP ಸಾಧನ ಪಟ್ಟಿ ಪಡೆಯಿರಿ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು LLM ಸಾಧನಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು

ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ ನಂತರದ ಹಂತವೆಂದರೆ ಅವುಗಳನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವುದು. ಇದಾದ ಮೇಲೆ, ನಾವು ಈ ಸಾಮರ್ಥ್ಯಗಳನ್ನು LLM ಗೆ ಸಾಧನಗಳಾಗಿ ಒದಗಿಸಬಹುದು.

#### TypeScript

1. MCP ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಬಳಸಬಹುದಾದ ಸಾಧನ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ಇನ್‌ಪುಟ್_ಸ್ಕೀಮಾ ಆಧರಿಸಿ ಜೋಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ಪ್ರಕಾರವನ್ನು ಸ್ಪಷ್ಟವಾಗಿ "ಫಂಕ್ಷನ್" ಎಂದು ಸೆಟ್ ಮಾಡಿ
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

    ಮೇಲಿನ ಕೋಡ್ MCP ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು ಅದನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸಾಧನ ವ್ಯಾಖ್ಯಾನ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

1. ನಂತರ, ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು `run` ವಿಧಾನವನ್ನು ನವೀಕರಿಸೋಣ:

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, ನಾವು `run` ವಿಧಾನವನ್ನು ನವೀಕರಿಸಿ ಫಲಿತಾಂಶದ ಮೂಲಕ ನಕ್ಷೆ ಹಾಕಿ ಪ್ರತಿ ಎಂಟ್ರಿಗೆ `openAiToolAdapter` ಅನ್ನು ಕರೆಮಾಡಿದ್ದೇವೆ.

#### Python

1. ಮೊದಲು, ಕೆಳಗಿನ ಪರಿವರ್ತಕ ಫಂಕ್ಷನ್ ರಚಿಸೋಣ

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

    ಮೇಲಿನ `convert_to_llm_tools` ಫಂಕ್ಷನ್‌ನಲ್ಲಿ ನಾವು MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತೇವೆ.

1. ನಂತರ, ಈ ಫಂಕ್ಷನ್ ಅನ್ನು ಬಳಸಲು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡ್ ನವೀಕರಿಸೋಣ:

    ```python
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ಇಲ್ಲಿ, ನಾವು MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ನೀಡಲು ಪರಿವರ್ತಿಸಲು `convert_to_llm_tool` ಅನ್ನು ಕರೆಮಾಡುತ್ತಿದ್ದೇವೆ.

#### .NET

1. MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ಕೋಡ್ ಸೇರಿಸೋಣ

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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾ ತೆಗೆದುಕೊಳ್ಳುವ `ConvertFrom` ಫಂಕ್ಷನ್ ರಚಿಸಿದ್ದೇವೆ.
- ಇದು `FunctionDefinition` ರಚಿಸುವ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಹೊಂದಿದೆ, ಇದು ನಂತರ `ChatCompletionsDefinition` ಗೆ ಪಾಸ್ ಆಗುತ್ತದೆ. ಇದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪ.

1. ಈ ಫಂಕ್ಷನ್ ಉಪಯೋಗಿಸಲು ಕೆಲವು ಇತ್ತೀಚಿನ ಕೋಡ್ ನವೀಕರಿಸೋಣ:

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
// ಸಹಜ ಭಾಷಾ ಸಂವಹನಕ್ಕಾಗಿ ಬಾಟ್ ಇಂಟರ್ಫೇಸ್ ರಚಿಸಿ
public interface Bot {
    String chat(String prompt);
}

// LLM ಮತ್ತು MCP ಸಾಧನಗಳೊಂದಿಗೆ AI ಸೇವೆಯನ್ನು ಸಂರಚಿಸಿ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸಹಜ ಭಾಷಾ ಸಂವಹನಕ್ಕಾಗಿ ಸರಳ `Bot` ಇಂಟರ್ಫೇಸ್ ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ
- LangChain4j ನ `AiServices` ಬಳಸಿ LLM ಮತ್ತು MCP ಸಾಧನ ಪೂರೈಕೆದಾರವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬಂಧಿಸಿದ್ದೇವೆ
- ಫ್ರೇಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಾಧನ ಸ್ಕೀಮಾ ಪರಿವರ್ತನೆ ಮತ್ತು ಫಂಕ್ಷನ್ ಕರೆಗಳನ್ನು ಹಿಂಬಾಲಿಸುತ್ತದೆ
- ಈ ವಿಧಾನ ಕೈಯಿಂದ ಸಾಧನ ಪರಿವರ್ತನೆಯನ್ನು ತೆಗೆದುಹಾಕುತ್ತದೆ - LangChain4j MCP ಸಾಧನಗಳನ್ನು LLM-ಸಂಗತ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವ ಎಲ್ಲಾ ಸಂಕೀರ್ಣತೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ

#### Rust

MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು, ನಾವು ಸಾಧನ ಪಟ್ಟಿ ಸ್ವರೂಪಗೊಳಿಸುವ ಸಹಾಯಕ ಫಂಕ್ಷನ್ ಸೇರಿಸುವೆವು. ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ನಲ್ಲಿ `main` ಫಂಕ್ಷನ್ ಕೆಳಗೆ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ. ಇದು LLM ಗೆ ವಿನಂತಿ ಮಾಡುವಾಗ ಕರೆಮಾಡಲಾಗುತ್ತದೆ:

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

ಚೆನ್ನಾಗಿದೆ, ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡಲು ಸಿದ್ಧರಾಗಿದ್ದೇವೆ, ಆದ್ದರಿಂದ ಮುಂದಿನ ಹಂತಕ್ಕೆ ಹೋಗೋಣ.

### -4- ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡುವುದು

ಈ ಭಾಗದಲ್ಲಿ, ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡುತ್ತೇವೆ.

#### TypeScript

1. ನಮ್ಮ LLM ಅನ್ನು ಕರೆಮಾಡಲು ಬಳಸುವ ವಿಧಾನ ಸೇರಿಸೋಣ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ಸರ್ವರ್‌ನ ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - `callTools` ಎಂಬ ವಿಧಾನ ಸೇರಿಸಿದ್ದೇವೆ.
    - ಈ ವಿಧಾನ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು ಯಾವ ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡಲಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ, ಇದ್ದರೆ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
        }
        ```

    - LLM ಸೂಚಿಸಿದರೆ ಸಾಧನವನ್ನು ಕರೆಮಾಡುತ್ತದೆ:

        ```typescript
        // 2. ಸರ್ವರ್‌ನ ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
        // ಮಾಡಬೇಕಿದೆ
        ```

1. `run` ವಿಧಾನವನ್ನು ನವೀಕರಿಸಿ LLM ಕರೆ ಮತ್ತು `callTools` ಅನ್ನು ಸೇರಿಸೋಣ:

    ```typescript

    // 1. LLM ಗೆ ಇನ್ಪುಟ್ ಆಗುವ ಸಂದೇಶಗಳನ್ನು ರಚಿಸಿ
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
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ, ಅದು ಟೂಲ್ ಕರೆಗಳನ್ನು ಹೊಂದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ಚೆನ್ನಾಗಿದೆ, ಸಂಪೂರ್ಣ ಕೋಡ್ ಪಟ್ಟಿ ಮಾಡೋಣ:

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
            baseURL: "https://models.inference.ai.azure.com", // ಭವಿಷ್ಯದಲ್ಲಿ ಈ URL ಗೆ ಬದಲಾಯಿಸಬೇಕಾಗಬಹುದು: https://models.github.ai/inference
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
          // ಇನ್‌ಪುಟ್_ಸ್ಕೀಮಾ ಆಧರಿಸಿ zod ಸ್ಕೀಮಾ ರಚಿಸಿ
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
    
    
          // 2. ಸರ್ವರ್‌ನ ಟೂಲ್ ಅನ್ನು ಕರೆಮಾಡಿ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
          // ಮಾಡಬೇಕಿದೆ
    
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ ಟೂಲ್ ಕರೆಗಳಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
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

1. LLM ಕರೆ ಮಾಡಲು ಅಗತ್ಯವಿರುವ ಕೆಲವು ಆಮದುಗಳನ್ನು ಸೇರಿಸೋಣ

    ```python
    # ಎಲ್‌ಎಲ್‌ಎಂ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ನಂತರ, LLM ಅನ್ನು ಕರೆಮಾಡುವ ಫಂಕ್ಷನ್ ಸೇರಿಸೋಣ:

    ```python
    # ಎಲ್‌ಎಲ್‌ಎಂ

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಕಂಡುಹಿಡಿದ ಮತ್ತು ಪರಿವರ್ತಿಸಿದ ಫಂಕ್ಷನ್‌ಗಳನ್ನು LLM ಗೆ ಪಾಸ್ ಮಾಡಿದ್ದೇವೆ.
    - ನಂತರ ಆ ಫಂಕ್ಷನ್‌ಗಳೊಂದಿಗೆ LLM ಅನ್ನು ಕರೆಮಾಡಿದ್ದೇವೆ.
    - ಫಲಿತಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾವ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಕರೆಮಾಡಬೇಕೆಂದು ನೋಡುತ್ತಿದ್ದೇವೆ.
    - ಕೊನೆಗೆ, ಕರೆಮಾಡಬೇಕಾದ ಫಂಕ್ಷನ್‌ಗಳ ಸರಣಿಯನ್ನು ಪಾಸ್ ಮಾಡುತ್ತಿದ್ದೇವೆ.

1. ಕೊನೆಯ ಹಂತ, ನಮ್ಮ ಮುಖ್ಯ ಕೋಡ್ ನವೀಕರಿಸೋಣ:

    ```python
    prompt = "Add 2 to 20"

    # ಎಲ್ಲಕ್ಕೆ ಯಾವ ಸಾಧನಗಳನ್ನು ಬಳಸಬೇಕು ಎಂದು LLMಗೆ ಕೇಳಿ, ಇದ್ದರೆ
    functions_to_call = call_llm(prompt, functions)

    # ಸೂಚಿಸಲಾದ ಕಾರ್ಯಗಳನ್ನು ಕರೆಮಾಡಿ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - LLM ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತವಾಗಿ ಕರೆಮಾಡಬೇಕಾದ MCP ಸಾಧನವನ್ನು `call_tool` ಮೂಲಕ ಕರೆಮಾಡುತ್ತಿದ್ದೇವೆ.
    - ಸಾಧನ ಕರೆ ಫಲಿತಾಂಶವನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಮುದ್ರಿಸುತ್ತಿದ್ದೇವೆ.

#### .NET

1. LLM ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಗಾಗಿ ಕೆಲವು ಕೋಡ್ ತೋರಿಸೋಣ:

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
        Model = "gpt-4o-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - MCP ಸರ್ವರ್‌ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆದುಕೊಂಡಿದ್ದೇವೆ, `var tools = await GetMcpTools()`.
    - ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ `userMessage` ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ.
    - ಮಾದರಿ ಮತ್ತು ಸಾಧನಗಳನ್ನು ಸೂಚಿಸುವ ಆಯ್ಕೆಗಳು ಹೊಂದಿರುವ ವಸ್ತುವನ್ನು ರಚಿಸಿದ್ದೇವೆ.
    - LLM ಗೆ ವಿನಂತಿ ಮಾಡಿದ್ದೇವೆ.

1. ಕೊನೆಯ ಹಂತ, LLM ಯಾವ ಫಂಕ್ಷನ್ ಕರೆಮಾಡಬೇಕೆಂದು ಯೋಚಿಸುತ್ತಿದೆಯೇ ಎಂದು ನೋಡೋಣ:

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - ಫಂಕ್ಷನ್ ಕರೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ ಲೂಪ್ ಮಾಡುತ್ತಿದ್ದೇವೆ.
    - ಪ್ರತಿ ಸಾಧನ ಕರೆಗಾಗಿ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ MCP ಕ್ಲೈಂಟ್ ಬಳಸಿ MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಸಾಧನವನ್ನು ಕರೆಮಾಡುತ್ತಿದ್ದೇವೆ. ಕೊನೆಗೆ ಫಲಿತಾಂಶ ಮುದ್ರಿಸುತ್ತಿದ್ದೇವೆ.

ಸಂಪೂರ್ಣ ಕೋಡ್ ಇಲ್ಲಿದೆ:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
using System.Text.Json;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);

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
    Model = "gpt-4o-mini",
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

    Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಸಾಧನಗಳನ್ನು ಬಳಸುವ ನೈಸರ್ಗಿಕ ಭಾಷಾ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಿ
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

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್ ಸಾಧನಗಳೊಂದಿಗೆ ಸಹಜ ಭಾಷಾ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಸಂವಹನ ಮಾಡಿದ್ದೇವೆ
- LangChain4j ಫ್ರೇಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
  - ಅಗತ್ಯವಿದ್ದಾಗ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸಾಧನ ಕರೆಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು
  - LLM ನಿರ್ಧಾರ ಆಧಾರಿತವಾಗಿ ಸೂಕ್ತ MCP ಸಾಧನಗಳನ್ನು ಕರೆಮಾಡುವುದು
  - LLM ಮತ್ತು MCP ಸರ್ವರ್ ನಡುವಿನ ಸಂಭಾಷಣಾ ಹರಿವನ್ನು ನಿರ್ವಹಿಸುವುದು
- `bot.chat()` ವಿಧಾನವು ಸಹಜ ಭಾಷಾ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡುತ್ತದೆ, ಇದರಲ್ಲಿ MCP ಸಾಧನ ಕಾರ್ಯಾಚರಣೆಗಳ ಫಲಿತಾಂಶಗಳು ಸೇರಿರಬಹುದು
- ಈ ವಿಧಾನ ಬಳಕೆದಾರರಿಗೆ MCP ಅಡಿಯಲ್ಲಿ ಇರುವ ಜಟಿಲತೆಯನ್ನು ತಿಳಿಯಬೇಕಾಗದೆ ಸೌಕರ್ಯಕರ ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ

ಸಂಪೂರ್ಣ ಕೋಡ್ ಉದಾಹರಣೆ:

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

ಇಲ್ಲಿ ಬಹುಮಟ್ಟಿನ ಕೆಲಸ ನಡೆಯುತ್ತದೆ. ನಾವು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಜೊತೆಗೆ LLM ಅನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ, ನಂತರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಯಾವ ಸಾಧನಗಳನ್ನು ಕರೆಮ
LLM ನಿಂದ ಪ್ರತಿಕ್ರಿಯೆಯಲ್ಲಿ `choices` ಎಂಬ ಸರಣಿಯನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಯಾವುದೇ `tool_calls` ಇದ್ದರೆ ಅದನ್ನು ಪರಿಶೀಲಿಸಲು ಫಲಿತಾಂಶವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬೇಕಾಗುತ್ತದೆ. ಇದು ನಮಗೆ ತಿಳಿಸುತ್ತದೆ LLM ನಿರ್ದಿಷ್ಟ ಸಾಧನವನ್ನು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಕರೆಮಾಡಬೇಕೆಂದು ಕೇಳುತ್ತಿದೆ. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸಲು ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ನ ಕೆಳಭಾಗಕ್ಕೆ ಸೇರಿಸಿ:

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

    // ಲಭ್ಯವಿದ್ದರೆ ವಿಷಯವನ್ನು ಮುದ್ರಿಸಿ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ಸಹಾಯಕ ಸಂದೇಶವನ್ನು ಸೇರಿಸಿ

        // ಪ್ರತಿ ಉಪಕರಣ ಕರೆಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ಉಪಕರಣ ಫಲಿತಾಂಶವನ್ನು ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸಿ
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

`tool_calls` ಇದ್ದರೆ, ಅದು ಸಾಧನ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದು, MCP ಸರ್ವರ್‌ಗೆ ಸಾಧನ ವಿನಂತಿಯನ್ನು ಕರೆದೊಯ್ಯುತ್ತದೆ ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಭಾಷಣೆ ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸುತ್ತದೆ. ನಂತರ LLM ಜೊತೆಗೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸುತ್ತದೆ ಮತ್ತು ಸಂದೇಶಗಳು ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಸಾಧನ ಕರೆ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ನವೀಕರಿಸಲಾಗುತ್ತವೆ.

LLM MCP ಕರೆಗಳಿಗೆ ನೀಡುವ ಸಾಧನ ಕರೆ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು, ನಾವು ಇನ್ನೊಂದು ಸಹಾಯಕ ಕಾರ್ಯವನ್ನು ಸೇರಿಸುವೆವು, ಇದು ಕರೆ ಮಾಡಲು ಅಗತ್ಯವಿರುವ ಎಲ್ಲವನ್ನೂ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ. ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ನ ಕೆಳಭಾಗಕ್ಕೆ ಸೇರಿಸಿ:

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

ಎಲ್ಲಾ ಭಾಗಗಳು ಸಿದ್ಧವಾಗಿರುವುದರಿಂದ, ನಾವು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಿ LLM ಅನ್ನು ಕರೆಮಾಡಬಹುದು. ನಿಮ್ಮ `main` ಕಾರ್ಯವನ್ನು ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ ನವೀಕರಿಸಿ:

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

ಇದು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್‌ನೊಂದಿಗೆ LLM ಅನ್ನು ಪ್ರಶ್ನಿಸುತ್ತದೆ, ಎರಡು ಸಂಖ್ಯೆಗಳ ಮೊತ್ತವನ್ನು ಕೇಳುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ ಸಾಧನ ಕರೆಗಳನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ.

ಚೆನ್ನಾಗಿದೆ, ನೀವು ಅದನ್ನು ಮಾಡಿದ್ದೀರಿ!

## ನಿಯೋಜನೆ

ಅಭ್ಯಾಸದಿಂದ ಕೋಡ್ ತೆಗೆದುಕೊಂಡು ಸರ್ವರ್‌ಗೆ ಇನ್ನಷ್ಟು ಸಾಧನಗಳನ್ನು ಸೇರಿಸಿ. ನಂತರ LLM ಇರುವ ಕ್ಲೈಂಟ್ ಅನ್ನು ರಚಿಸಿ, ಅಭ್ಯಾಸದಂತೆ, ಮತ್ತು ವಿಭಿನ್ನ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ ನಿಮ್ಮ ಸರ್ವರ್‌ನ ಎಲ್ಲಾ ಸಾಧನಗಳು ಡೈನಾಮಿಕ್ ಆಗಿ ಕರೆಮಾಡಲ್ಪಡುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಈ ರೀತಿಯ ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಣವು ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ನೀಡುತ್ತದೆ ಏಕೆಂದರೆ ಅವರು ನಿಖರ ಕ್ಲೈಂಟ್ ಆಜ್ಞೆಗಳ ಬದಲು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಬಹುದು ಮತ್ತು ಯಾವುದೇ MCP ಸರ್ವರ್ ಕರೆಮಾಡಲಾಗುತ್ತಿರುವುದನ್ನು ಗಮನಿಸದೆ ಇರಬಹುದು.

## ಪರಿಹಾರ

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ಪ್ರಮುಖ ಅಂಶಗಳು

- ನಿಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದು ಬಳಕೆದಾರರಿಗೆ MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಉತ್ತಮ ಸಂವಹನದ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.
- MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ರೀತಿಗೆ ಪರಿವರ್ತಿಸಬೇಕಾಗುತ್ತದೆ.

## ಮಾದರಿಗಳು

- [Java ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.Net ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [JavaScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [TypeScript ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [Python ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)
- [Rust ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

## ಮುಂದೇನು

- ಮುಂದಿನದು: [Visual Studio Code ಬಳಸಿ ಸರ್ವರ್ ಅನ್ನು ಉಪಯೋಗಿಸುವುದು](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->