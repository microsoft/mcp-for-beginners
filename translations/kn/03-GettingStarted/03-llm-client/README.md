# LLM ನೊಂದಿಗೆ ಕ್ಲೈಯಂಟ್ ಸೃಜನಶೀಲತೆ

ಈವರೆಗೆ, ನೀವು ಹೇಗೆ ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಯಂಟ್ ಅನ್ನು ಸೃಷ್ಟಿಸುವುದನ್ನು ನೋಡಿದ್ದೀರಿ. ಕ್ಲೈಯಂಟ್ ಸರ್ವರ್ ಅನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಕರೆಸಬಹುದಾಗಿದೆ ಅದರ ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು. ಆದಾಗ್ಯೂ, ಇದು ಬಹಳ ಪ್ರಾಯೋಗಿಕ ವಿಧಾನವಲ್ಲ. ನಿಮ್ಮ ಬಳಕೆದಾರರು ಏಜೆಂಟಿಕ್ ಯುಗದಲ್ಲಿ ಜೀವಿಸುತ್ತಾರೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಲು ಮತ್ತು LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಅವರು ನೀವು ನಿಮ್ಮ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಂಗ್ರಹಿಸಲು MCP ಅನ್ನು ಬಳಸುತ್ತೀರಾ ಎಂಬುದನ್ನು ಪರಿಗಣಿಸುವುದಿಲ್ಲ; ಅವರು ಸಹಜ ಭಾಷೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸಂವಹನ ಮಾಡೋಣ ಎಂದು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಹೀಗಾಗಿ ನಾವು ಇದನ್ನು ಹೇಗೆ ಪರಿಹರಿಸೋಣ? ಪರಿಹಾರ ಎನ್ನುವುದು ಕ್ಲೈಯಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದಾಗಿದೆ.

## ಅವಲೋಕನ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ನಿಮ್ಮ ಕ್ಲೈಯಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದರ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತೇವೆ ಮತ್ತು ಇದು ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ಹೇಗೆ ಒದಗಿಸುತ್ತದೆ ಎಂದು ತೋರಿಸುತ್ತೇವೆ.

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಕೊನೆಯಲ್ಲಿ, ನೀವು ಆಗರಬಹುದಾಗಿದೆ:

- LLM ಸೇರಿದಂತೆ ಕ್ಲೈಯಂಟ್ ಅನ್ನು ಸೃಷ್ಟಿಸುವುದು.
- LLM ಬಳಸಿಕೊಂಡು MCP ಸರ್ವರ್ ಜೊತೆ ನಿರಂತರವಾಗಿ ಸಂವಹನ ಮಾಡುವುದು.
- ಕ್ಲೈಯಂಟ್ ಬದಿಯಲ್ಲಿ ಹೆಚ್ಚುವರಿ ಅಂತಿಮ ಬಳಕೆದಾರ ಅನುಭವ ಒದಗಿಸುವುದು.

## ವಿಧಾನ

ನಾವು ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ. LLM ಸೇರಿಸುವುದು ಸರಳವಾಗಿ ತೋರುತ್ತದೆ, ನಾವು ನಿಜವಾಗಿಯೂ ಇದನ್ನು ಮಾಡುತ್ತೇವೇ?

ಇದು ಕ್ಲೈಯಂಟ್ ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನ ಮಾಡುವ ರೀತಿ:

1. ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂಪರ್ಕ ಸ್ಥಾಪಿಸುವುದು.

1. ಸಾಮರ್ಥ್ಯಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ, ಅವುಗಳ ಸ್ಕೆಮಾ ನುಡಿಸಿ ಉಳಿಸುವುದು.

1. LLM ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು ಉಳಿಸಿದ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಮತ್ತು ಸ್ಕೀಮಾಗೆ LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಫಾರ್ಮ್ಯಾಟ್ ನಲ್ಲಿ ಪಾಸ್ ಮಾಡುವುದು.

1. ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಗೆ ಹಾಗೂ ಕ್ಲೈಯಂಟ್ ಪಟ್ಟಿ ಮಾಡಿದ ಸಾಧನಗಳ ಜೊತೆ ನೀಡುವ ಮೂಲಕ ಸಂವಹನ ಮಾಡುವುದು.

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಇದನ್ನು ಎಷ್ಟು ಮಟ್ಟಿಗೆ ಮಾಡಬಹುದು ಎಂದು ಅರ್ಥ ಮಾಡಿಕೊಂಡಿದ್ದೇವೆ, ಕೆಳಗಿನ ವ್ಯಾಯಾಮದಲ್ಲಿ ಇದನ್ನು ಪ್ರಯತ್ನಿಸೋಣ.

## ವ್ಯಾಯಾಮ: LLM ಹೊಂದಿರುವ ಕ್ಲೈಯಂಟ್ ಸೃಷ್ಟಿಸುವುದು

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನಾವು ನಮ್ಮ ಕ್ಲೈಯಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದನ್ನು ಕಲಿಯೋಣ.

### GitHub ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ ಬಳಸಿ ಪ್ರಾಮಾಣೀಕರಣ

GitHub ಟೋಕನ್ ಸೃಷ್ಟಿಸುವುದು ಸರಳ ಪ್ರಕ್ರಿಯೆ. ಇದನ್ನು ನೀವು ಹೇಗೆ ಮಾಡಬಹುದು:

- GitHub ಸೆಟ್ಟಿಂಗ್ಗಳಿಗೆ ಹೋಗಿ – ಮೇಲಿನ ಬಲಭಾಗದಲ್ಲಿರುವ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಗಳನ್ನು ಆರಿಸಿ.
- ಡೆ್ವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಗಳಿಗೆ ಸಾಗಿರಿ – ಕೆಳಗೆ ಸ್ಕ್ರೋಲ್ ಮಾಡಿ ಡೆ್ವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ.
- ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ಸ್ ಆಯ್ಕೆ ಮಾಡಿ – ಫೈನ್-ಗ್ರೇನ್ಡ್ ಟೋಕನ್ಸ್ ಅನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ, ನಂತರ ಹೊಸ ಟೋಕನನ್ನು ರಚಿಸಿ.
- ನಿಮ್ಮ ಟೋಕನಿಗೆ ಕಾನ್ಫಿಗರ್ ಮಾಡಿ – ಉಲ್ಲೇಖಕ್ಕಾಗಿ ನೋಟನ್ನು ಸೇರಿಸಿ, ಅವಧಿಯನ್ನು ನಿಗದಿಪಡಿಸಿ ಮತ್ತು ಅಗತ್ಯವಿರುವ ಪರವಾನಗಿಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ (ಈ ಪ್ರಕರಣದಲ್ಲಿ Models ಅನುಮತಿಯನ್ನು ಸೇರಿಸಬೇಕು).
- ಟೋಕನನ್ನು ರಚಿಸಿ ಮತ್ತು ನಕಲಿ ಮಾಡಿ – ಜನರೇಟ್ ಟೋಕನ್ ಕ್ಲಿಕ್ ಮಾಡಿ, ಮತ್ತು ಅದನ್ನು ತಕ್ಷಣ ನಕಲಿಸಿಕೊಳ್ಳಿ, ಏಕೆಂದರೆ ನೀವು ಅದನ್ನು ಮತ್ತೆ ನೋಡಲು ಸಾಧ್ಯವಿರುವುದಿಲ್ಲ.

### -1- ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಮಾಡುವುದು

ನಾವು ಮೊದಲು ನಮ್ಮ ಕ್ಲೈಯಂಟ್ ಅನ್ನು ಸೃಷ್ಟಿಸೋಣ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ ಜಾಡ್ ಅನ್ನು ಆಮದುಮಾಡಿ

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಬೇಕಾದ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- `client` ಮತ್ತು `openai` ಎಂಬ ಎರಡು ಸದಸ್ಯರೊಂದಿಗೆ ಒಂದು ಕ್ಲಾಸ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ, ಇದು ಕ್ರಮವಾಗಿ ಕ್ಲೈಯಂಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಲು ಮತ್ತು LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- ನಮ್ಮ LLM ಉದಾಹರಣೆಯನ್ನು GitHub Models ಬಳಸಲು `baseUrl` ಅನ್ನು ಇನ್ಫರೆನ್ಸ್ API ತಲುಪುವಂತೆ ಸೆಟ್ಟಿಂಗ್ ಮಾಡಿದ್ದೇವೆ.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪ್ಯಾರامیಟರ್ಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯಗತಗೊಳಿಸಬಹುದಾದ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ 参数ಗಳು
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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಗಾಗಿ ಅಗತ್ಯವಾದ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- ಕ್ಲೈಯಂಟ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ

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

ಮೊದಲು, ನೀವು ನಿಮ್ಮ `pom.xml` ಫೈಲಿಗೆ LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸುವ ಅಗತ್ಯವಿದೆ. MCP ಸಂಮೊ۱۸ೕದರಿಗಾಗಿ ಮತ್ತು GitHub Models ಬೆಂಬಲಕ್ಕಾಗಿ ಈ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

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

ನಂತರ ನಿಮ್ಮ Java ಕ್ಲೈಯಂಟ್ ಕ್ಲಾಸ್ ಅನ್ನು ಸೃಷ್ಟಿಸಿ:

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
    
    public static void main(String[] args) throws Exception {        // LLM ಅನ್ನು GitHub ಮಾದರಿಗಳನ್ನು ಬಳಸಲು ಸಂರಚಿಸು
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕ ಸಾಧಿಸಲು MCP ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್ ರಚನೆ ಮಾಡು
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ಗ್ರಾಹಕ ರಚಿಸು
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- **LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿದ್ದೇವೆ**: MCP ಸಂಮೊ۱۸ೕದನೆ, OpenAI ಅಧಿಕೃತ ಕ್ಲೈಯಂಟ್, ಹಾಗೂ GitHub Models ಬೆಂಬಲಕ್ಕಾಗಿ
- **LangChain4j ಗ್ರಂಥಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ**: MCP ಸಂಮೋಧನೆ ಮತ್ತು OpenAI ಚಾಟ್ ಮಾದರಿಗಾಗಿ
- **`ChatLanguageModel` ಸೃಷ್ಟಿಸಿದ್ದೇವೆ**: ನಿಮ್ಮ GitHub ಟೋಕನ್ ಉಪಯೋಗಿಸಿ GitHub Models ಬಳಸಲು ಸಂರಚಿಸಲಾಗಿದೆ
- **HTTP ಸಂಚಾರವನ್ನು ಸೆಟ್ ಮಾಡಿದ್ದೇವೆ**: MCP ಸರ್ವರ್‌ಗಗೆ ಸಂಪರ್ಕಿಸಲು Server-Sent Events (SSE) ಮೂಲಕ
- **MCP ಕ್ಲೈಯಂಟ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ**: ಇದು ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ
- **LangChain4j ಯಲ್ಲಿರುವ MCP ಬೆಂಬಲವನ್ನು ಉಪಯೋಗಿಸಿದ್ದೇವೆ**: ಇದು LLM ಮತ್ತು MCP ಸರ್ವರ್‌ಗಳ ಮಧ್ಯೆ ಸಂಮೋಧನೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ

#### Rust

ಈ ಉದಾಹರಣೆ ನಿಮ್ಮ ಬಳಿ ರಸ್ಟ್ ಆಧಾರಿತ MCP ಸರ್ವರ್ ಚಾಲನೆ ಹೊಂದಿದ್ದು ಎಂದು فرضಿಸುತ್ತದೆ. ಹೊಂದಿಲ್ಲದಿದ್ದರೆ, ಸರ್ವರ್ ಸೃಷ್ಟಿಸುವುದಕ್ಕೆ [01-first-server](../01-first-server/README.md) ಪಾಠಕ್ಕೆ ಹಿಂತಿರುಗಿ.

ನಿಮ್ಮ ರಸ್ಟ್ MCP ಸರ್ವರ್ ಇದ್ದಾಗ, ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಸರ್ವರ್ ಇರುವ ಫೋಲ್ಡರ್‌ಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ. ನಂತರ ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ ಒಂದು ಹೊಸ LLM ಕ್ಲೈಯಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ನಿಮ್ಮ `Cargo.toml` ಫೈಲಿಗೆ ಕೆಳಗಿನ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ಅಧಿಕೃತ ರಸ್ಟ್ ಲೈಬ್ರರಿ OpenAI ಕ್ಕೆ ಲಭ್ಯವಿಲ್ಲ, ಆದಾಗ್ಯೂ `async-openai` ಕ್ರೇಟ್ ಒಂದು [ಸಮುದಾಯ ನಿರ್ವಹಿಸಲಾದ ಗ್ರಂಥಾಲಯ](https://platform.openai.com/docs/libraries/rust#rust) ಆಗಿದ್ದು ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ.

`src/main.rs` ಫೈಲನ್ನು ತೆರೆಯಿರಿ ಮತ್ತು ಅದರ ವಿಷಯವನ್ನು ಕೆಳಗಿನ ಕೋಡಿನಿಂದ ಬದಲಾಯಿಸಿ:

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

    // OpenAI ಕ್ಲೈಂಟ್ ఏర్పాటు ಮಾಡು
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ಕ್ಲೈಂಟ್ ಸೆಟ್ ಅಪ್ ಮಾಡಿ
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

    // TODO: ಸಾಧನ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂಭಾಷಣೆ

    Ok(())
}
```

ಈ ಕೋಡ್ ಒಂದು ಮೂಲಭೂತ ರಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ, ಇದು MCP ಸರ್ವರ್ ಮತ್ತು GitHub Models ಗೆ LLM ಸಂವಹನಕ್ಕಾಗಿ ಸಂಪರ್ಕ ಹೊಂದುತ್ತದೆ.

> [!IMPORTANT]
> ಅಪ್ಲಿಕೇಶನ್ ಚಾಲನೆಗೆ ಮೊದಲು ನಿಮ್ಮ GitHub ಟೋಕನನ್ನು `OPENAI_API_KEY` ಪರಿಸರ ಚರದಲ್ಲಿ ಸೆಟ್ ಮಾಡಿಕೊಳ್ಳಿ.

ಚೆನ್ನಾಗಿದೆ, ಮುಂದೆ ನಾವು ಸರ್ವರ್‌ನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋಣ.

### -2- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು

ಈಗ ನಾವು ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದಿ ಅದರ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಕೇಳೋಣ:

#### Typescript

ಅವದೇ ಕ್ಲಾಸ್‌ನಲ್ಲಿ, ಕೆಳಗಿನ ಮಿಥಗಳನ್ನು ಸೇರಿಸಿ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ಸಲಕರಣೆಗಳ ಪಟ್ಟಿ ಮಾಡುವುದು
    const toolsResult = await this.client.listTools();
}
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್‌ಗೂ ಸಂಪರ್ಕ ಮಾಡುವುದು `connectToServer` ಎಂಬ ಮೆತೋಡನ್ನು ಸೇರಿಸಿದ್ದೇವೆ.
- ನಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ನ ಚಲನೆ ನಿರ್ವಹಿಸುವ `run` ಮೆತೋಡ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ. ಇದುವರೆಗೆ ಇದು ಸಾಧನಗಳನ್ನು ಮಾತ್ರ ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ ಆದರೆ ಮುಂದಿನ ಕಾಲದಲ್ಲಿ ಅದಕ್ಕೆ ಹೆಚ್ಚು ಕಾರ್ಯಗಳನ್ನು ಸೇರಿಸುವೆವು.

#### Python

```python
# ಲಭ್ಯವಿರುವ ಸಂಪನ್ಮೂಲಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ನಾವು ಸೇರಿಸಿದವು:

- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮುದ್ರಿಸಿದ್ದೇವೆ. ಸಾಧನಗಳಿಗಾಗಿ `inputSchema` ಕೂಡ ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ, ಅವರು ಮುಂದಿನ ಕಾರ್ಯದಲ್ಲಿ ಉಪಯೋಗಿಸುವುದು.

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ
- ಪ್ರತಿ ಸಾಧನದ ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಅದರ ಸ್ಕೆಮಾ ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ. ಇದು ಸಾದನಗಳನ್ನು ಬರುವ ಕಾಲದಲ್ಲಿ ಉಪಯೋಗಿಸೋದು.

#### Java

```java
// ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಸಾಧನಗಳನ್ನು ಕಂಡುಕೊಳ್ಳುವ ಟೂಲ್ ಪ್ರೊವೈಡರನ್ನು ರಚಿಸಿ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ಟೂಲ್ ಪ್ರೊವೈಡர் ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಹೀಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ:
// - MCP ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
// - MCP ಟೂಲ್ ಸ್ಕೀಮಾಗಳನ್ನು LangChain4j ಫಾರ್ಮಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವುದು
// - ಸಾಧನ ಕಾರ್ಯನಿರ್ವಹಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಂಡುಹಿಡಿದು ನೋಂದಾಯಿಸುವ `McpToolProvider` ಅನ್ನು ಸೃಷ್ಟಿಸಿದ್ದೇವೆ
- ಸಾಧನ ಸ್ಕೆಮಾ ಮತ್ತು LangChain4j ಸಾಧನ ಫಾರ್ಮ್ಯಾಟ್ ನಡುವಿನ ಪರಿವರ್ತನೆಯನ್ನು ಸಾಧನ ಒದಗಿಸುವವರು ಒಳಗೆ ನಿರ್ವಹಿಸುತ್ತಾರೆ
- ಈ ವಿಧಾನದ ಮೂಲಕ ಕೈಯೊಂದು ಸಾಧನ ಪಟ್ಟಿ ಮಾಡುವ ಮತ್ತು ಪರಿವರ್ತಿಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅವಳೆಖ ಮಾಡಲಾಗಿದೆ

#### Rust

MCP ಸರ್ವರ್‌ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆಯಲು `list_tools` ವಿಧಾನ ಬಳಸಲಾಗುತ್ತದೆ. ನಿಮ್ಮ `main` ಕಾರ್ಯದಲ್ಲಿ, MCP ಕ್ಲೈಯಂಟ್ ಸಿದ್ಧಪಡಿಸಿದ ಆದ ಬಳಿಕ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

```rust
// MCP ಉಪಕರಣ ಪಟ್ಟಿ ಪಡೆಯಿರಿ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು LLM ಸಾಧನಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು

ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ ನಂತರದ ಹಂತವೆಂದರೆ ಅವುಗಳನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವುದು. ಇದಾದಾಗ ನಾವು ಈ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನಮ್ಮ LLM ಗೆ ಸಾಧನಗಳಾಗಿ ಒದಗಿಸಬಹುದು.

#### TypeScript

1. MCP ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಉಪಯೋಗಿಸಬಹುದಾದ ಸಾಧನ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ಇನ್‌ಪುಟ್_ಸ್ಕೀಮಾ ಆಧಾರದ ಮೇಲೆ ಒಂದು ಜೋಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ಪ್ರಕಾರವನ್ನು "function" ಎಂದು ಸ್ಪಷ್ಟವಾಗಿ ಹೊಂದಿಸಿ
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

ರೀತಿ, ಮೇಲಿನ ಕೋಡ್ MCP ಸರ್‍ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸಾಧನ ವ್ಯಾಖ್ಯಾನ ಫಾರ್ಮ್ಯಾಟ್ ಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

1. ನಂತರ `run` ಮಿಥೋಡ್ ಅನ್ನು ಹೊಸದಾಗಿ ಅಪ್ಡೇಟ್ ಮಾಡಿ ಕೆಳಗಿನಂತೆ ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋಣ:

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು `run` ಮೆತೋಡ್ ಅನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿದ್ದು, ಫಲಿತಾಂಶದ ಮೂಲಕ ಮ್ಯಾಪ್ ಮಾಡಿ ಪ್ರತಿ ಪ್ರವೇಶಕ್ಕೆ `openAiToolAdapter` ಅನ್ನು ಕರೆಸುವುದು.

#### Python

1. ಮೊದಲು ಕೆಳಗಿನ ಪರಿವರ್ತಕ ಕಾರ್ಯವನ್ನು ರಚಿಸೋಣ

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

ಈ `convert_to_llm_tools` ಫಂಕ್ಷನ್‌ನಲ್ಲಿ, MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಬಗೆಯ ಫಾರ್ಮ್ಯಾಟ್ ಗೆ ಪರಿವರ್ತಿಸುತ್ತೇವೆ.

1. ನಂತರ, ಈ ಕಾರ್ಯವನ್ನು ಉಪಯೋಗಿಸಲು ನಮ್ಮ ಕ್ಲೈಯಂಟ್ ಕೋಡ್ ಅನ್ನು ಹೀಗೆ ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

ಇಲ್ಲಿ, MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ಹುರಿಯಲು `convert_to_llm_tool` ಕರೆಯುವ ಸಂಭಾವನೆ ಸೇರಿಸಲಾಗಿದೆ.

#### .NET

1. MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ರೀತಿಗೆ ಪರಿವರ್ತಿಸುವುದಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- `ConvertFrom` ಎಂಬ ಫಂಕ್ಷನ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ, ಇದು ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ಕೆಮಾ ಪಡೆಯುತ್ತದೆ.
- ಇದು ಒಂದು `FunctionDefinition` ರಚಿಸುವ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಅದನ್ನು `ChatCompletionsDefinition`ಗೆ ಪಾಸ್ ಮಾಡುತ್ತದೆ. ಇದು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಫಾರ್ಮ್ಯಾಟ್ ಆಗಿದೆ.

1. ಈಗ ಈ ಫಂಕ್ಷನ್ ಒದಗಿಸುವಂತೆ ಕೆಲವು ಲಭ್ಯವಿರುವ ಕೋಡ್‍ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

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
// ಪ್ರಕೃತ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಬಾಟ್ ಇಂಟರ್ಫೇಸ್ ರಚಿಸಿ
public interface Bot {
    String chat(String prompt);
}

// LLM ಮತ್ತು MCP ಸಾಧನಗಳೊಂದಿಗೆ AI ಸೇವೆಯನ್ನು ಸಂರಚಿಸಿ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸಹಜ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಸರಳ `Bot` ಇಂಟರ್ಫೇಸ್ ಅನ್ನುนิ\ಾㅏತ ಮಾಡಿದ್ದೇವೆ
- LangChain4j ನ `AiServices` ಬಳಸಿ LLM ನ್ನು MCP ಸಾಧನ ಒದಗಿಸುವವರೊಂದಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬೈಂಡ್ ಮಾಡಿದ್ದೇವೆ
- ಫ್ರೆಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಾಧನ ಸ್ಕೆಮಾ ಪರಿವರ್ತನೆ ಮತ್ತು ಫಂಕ್ಷನ್ ಕರೆಗಳನ್ನು ಹಿಂಭಾಗದಲ್ಲಿ ನಿರ್ವಹಿಸುತ್ತದೆ
- ಈ ವಿಧಾನ ಕೈಯೊಂದು ಸಾಧನ ಪರಿವರ್ತನೆಯನ್ನು ತೆಗೆದುಹಾಕುತ್ತದೆ - LangChain4j ಎಲ್ಲಾ ಸಂಕೀರ್ಣತೆಯನ್ನು ನಿಭಾಯಿಸುತ್ತದೆ ಮತ್ತು MCP ಸಾಧನಗಳನ್ನು LLM ಗೆ ಹೊಂದಿಕೆಯಾಗುವ ಫಾರ್ಮ್ಯಾಟ್ ಗೆ ಪರಿವರ್ತಿಸುತ್ತದೆ

#### Rust

MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ರೀತಿಗೆ ಪರಿವರ್ತಿಸಲು, ಸಾಧನಗಳ ಪಟ್ಟಿ ಮಾಡುವ ಸಹಾಯಕ ಕಾರ್ಯವನ್ನು `main.rs` ಫೈಲಿನ `main` ಕಾರ್ಯದ ಕೆಳಗೆ ಸೇರಿಸಿ. ಇದು LLM ಗೆ ವಿನಂತಿ ಮಾಡುವಾಗ ಕರೆಸಲಾಗುವುದು:

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

ಚೆನ್ನಾಗಿದೆ, ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ನೋಡಿಕೊಳ್ಳಲು ಸಿದ್ಧರಾಗಿರುತ್ತೇವೆ, ಹೀಗಾಗಿ ಮುಂದಿನ ಹಂತಕ್ಕೆ ಹೋಗೋಣ.

### -4- ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡುವುದು

ಈ ಭಾಗದಲ್ಲಿ, ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುವುದನ್ನು ನೋಡುತ್ತೇವೆ.

#### TypeScript

1. ನಮ್ಮ LLM ಅನ್ನು ಕರೆಸಲು ಉಪಯೋಗಿಸುವ ಒಂದು ಮಿಥೋಡ್ ಸೇರಿಸಿ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ಸರ್ವರ್‌ನ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
        // ಮಾಡಲು ಬಾಕಿ

        }
    }
    ```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- `callTools` ಎಂಬ ಮಿಥೋಡ್ ಸೇರಿಸಿದ್ದೇವೆ.
- ಈ ಮಿಥೋಡ್ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆದು ಯಾವ ಸಾಧನಗಳನ್ನು ಕರೆಸಲಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಿ
        }
        ```

- LLM ಸೂಚಿಸಿದರೆ ಸಾಧನವನ್ನು ಕರೆಸುತ್ತದೆ:

        ```typescript
        // 2. ಸರ್ವರ್‌ನ ಟೂಲ್ ಅನ್ನು ಕರೆ ಮಾಡು
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶವನ್ನು ಬಳಸಿಕೊಂಡು ಏನೋ ಮಾಡು
        // ಮಾಡಲು ಬಾಕಿ ಇದೆ
        ```

1. `run` ಮಿಥೋಡ್ ಅನ್ನು LLM ಕರೆ ಮತ್ತು `callTools` ನ ಕರೆಗಳನ್ನು ಸೇರಿಸಲು ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```typescript

    // ೧. LLM ಗೆ ಇನ್ಪುಟ್ ಆಗುವ ಸಂದೇಶಗಳನ್ನು ರಚಿಸಿ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ೨. LLM ಅನ್ನು ಕರೆ ಮಾಡುವುದು
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ೩. ಪ್ರತಿಯೊಂದು ಆಯ್ಕೆಯೂ ಉಪಕರಣ ಕರೆಗಳನ್ನು ಹೊಂದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಲು LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ಚೆನ್ನಾಗಿದೆ, ಸಂಪೂರ್ಣ ಕೋಡ್ ಹೀಗಿದೆ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗೆ zod ಅನ್ನು ಆಮದು ಮಾಡಿ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ಭವಿಷ್ಯದಲ್ಲಿ ಈ URL ಗೆ ಬದಲಾಯಿಸುವ ಅಗತ್ಯವಿದೆಯಾದರೂ: https://models.github.ai/inference
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
          // input_schema ಆಧರಿಸಿ zod ಸ್ಕೀಮಾ ರಚಿಸಿ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರಕಾರವನ್ನು "function" ಎಂದು ಸ್ಥಾಪಿಸಿ
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
    
    
          // 2. ಸರ್ವರ್‌ನ ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
          // TODO
    
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
    
        // 1. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮೂಲಕ ಹೋಗಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ, ಇದು ಸಾಧನ ಕರೆಗಳಿವೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
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

1. LLM ಕರೆ ಮಾಡಲು ಬೇಕಾದ ಕೆಲವು ಆಮದುಗಳನ್ನು ಸೇರಿಸೋಣ

    ```python
    # ಎಲ್ಎಲ್‌ಎಮ್
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ನಂತರ, LLM ನ್ನು ಕರೆ ಮಾಡುವ ಕಾರ್ಯವನ್ನು ಸೇರಿಸಿ:

    ```python
    # ಎಲ್‌ಎಲ್ಎಂ

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
            # ವೈಕಲ್ಯಪೂರ್ಣ ಅಡ್ಡರೇಖೆಗಳು
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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಕಂಡುಹಿಡಿದ ಮತ್ತು ಪರಿವರ್ತಿಸಿದ ನಮ್ಮ ಫಂಕ್ಷನ್‌ಗಳನ್ನು LLM ಗೆ ಪಾಸ್ ಮಾಡಿದ್ದೇವೆ.
- ನಂತರ, ಆ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಬಳಸಿ LLM ನ್ನು ಕರೆಮಾಡಿದ್ದೇವೆ.
- ನಂತರ ಫಲಿತಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾವ ಫಂಕ್ಷನ್ ಗಳನ್ನು ಕರೆಸಬೇಕಾಗಿವೆ ಎಂದು ನೋಡುತ್ತಿದ್ದೇವೆ.
- ಕೊನೆಗೆ, ಕರೆ ಮಾಡಬೇಕಾದ ಫಂಕ್ಷನ್‌ಗಳ ಅರೇ ಅನ್ನು ಪಾಸ್ ಮಾಡಿದ್ದೇವೆ.

1. ಕೊನೆ ಹಂತವಾಗಿ, ನಮ್ಮ ಮುಖ್ಯ ಕೋಡ್ ಅನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```python
    prompt = "Add 2 to 20"

    # ಎಲ್ಲಕ್ಕೆ ಯಾವ ಸಾಧನಗಳನ್ನು ಬಳಸಬೇಕೆಂದು LLM ಗೆ ಕೇಳಿ, ಇದ್ದರೆ
    functions_to_call = call_llm(prompt, functions)

    # ಶಿಫಾರಸು ಮಾಡಲಾದ ಕಾರ್ಯಗಳನ್ನು ಕರೆಮಾಡಿ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

ಅಲ್ಲಿ, ಆಗಿನ ಎಲ್ಲ ಹಂತಗಳು ಈ ಕೆಳಗಿನಂತೆ:

- MCP ಸಾಧನ‌ವನ್ನು `call_tool` ಮೂಲಕ ಕರೆ ಮಾಡುತ್ತಿದ್ದೇವೆ, ಇದು LLM ನ್ನು ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದ ಮೇಲೆ ಕರೆ ಮಾಡಲು ಸೂಚಿಸಿದೆ.
- ಸಾಧನದ ಕರೆ ಫಲಿತಾಂಶವನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಮುದ್ರಿಸುತ್ತೇವೆ.

#### .NET

1. LLM ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ಮಾಡೋದಿ ಕೆಳಗಿನ ಕೋಡ್ ನೋಡಿ:

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- MCP ಸರ್ವರ್‌ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆದಿದ್ದೇವೆ, `var tools = await GetMcpTools()`.
- ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ `userMessage` ಅಂದರೆ.
- ಮಾದರಿ ಮತ್ತು ಸಾಧನಗಳನ್ನು ಸೂಚಿಸುವ ಆಯ್ಕೆಯ ವಸ್ತು ರಚಿಸಿದ್ದೇವೆ.
- LLM ಕಡೆಗೆ ವಿನಂತಿ ಮಾಡಿದ್ದೇವೆ.

1. ಕೊನೆ ಹಂತ, LLM ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡಲು ಹೌದು ಎಂದು ಬಿಂಬಿಸಿದರೆ ನೋಡೋಣ:

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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- ಫಂಕ್ಷನ್ ಕರೆಯುವ ಪಟ್ಟಿ ಮೂಲಕ ಲೂಪ್ ಮಾಡುತ್ತಿದ್ದೇವೆ.
- ಪ್ರತಿ ಸಾಧನ ಕರೆಗೆ ಹೆಸರು ಮತ್ತು ಆರ್ಗುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಸಾಧನವನ್ನು MCP ಕ್ಲೈಯಂಟ್ ಉಪಯೋಗಿಸಿ ಕರೆ ಮಾಡುತ್ತಿದ್ದೇವೆ. ಕೊನೆಗೆ ಫಲಿತಾಂಶ ಮುದ್ರಿಸುತ್ತೇವೆ.

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
    // MCP ಉಪಕರಣಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬಳಸುವ ಸ್ವಾಭಾವಿಕ ಭಾಷಾ ವಿನಂತಿಗಳನ್ನು ಕಾರ್ಯನಿರ್ವಹಿಸಿ
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

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ:

- MCP ಸರ್ವರ್ ಸಾಧನಗಳೊಂದಿಗೆ ಸರಳ ಸಹಜ ಭಾಷೆ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಿದ್ದೇವೆ
- LangChain4j ಫ್ರೆಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
  - ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಸಾಧನ ಕರೆಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು
  - LLM ನ ನಿರ್ಣಯ ಆಧಾರದ ಮೇಲೆ ಸರಿಯಾದ MCP ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡುವುದು
  - LLM ಮತ್ತು MCP ಸರ್ವರ್ ಮಧ್ಯೆ ಸಂವಾದ ಹರಿವನ್ನು ನಿರ್ವಹಿಸುವುದು
- `bot.chat()` ವಿಧಾನ ಸಹಜ ಭಾಷೆ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡುತ್ತದೆ, ಇದರಲ್ಲಿ MCP ಸಾಧನ ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಫಲಿತಾಂಶ ಇರಬಹುದು
- ಈ ವಿಧಾನ ಬಳಕೆದಾರರಿಗೆ ಅಡಿಗಲ್ಲಿನ MCP ಅನುಷ್ಠಾನದ ಬಗ್ಗೆ ತಿಳಿಯದೇ ವಿಶ್ರಾಂತಿ ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ

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

ಇಲ್ಲಿ ಹೆಚ್ಚಿನ ಕೆಲಸ ನಡೆಯುತ್ತದೆ. ನಾವು ಮೊದಲ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ನೊಂದಿಗೆ LLM ನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ, ನಂತರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾವುದಾದರೂ ಸಾಧನಗಳನ್ನು ಕರೆಸಬೇಕಿದೆ ಎಂಬುದನ್ನು ನೋಡುತ್ತೇವೆ. ಬೇಕಾದರೆ, ಆ ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡಿ, ನಂತರ ಮತ್ತೆ LLM ಜೊತೆಗೆ ಸಂಗ್ರಹಣೆ ಮುಂದುವರಿಸುತ್ತೇವೆ ಇಲ್ಲಿ ಹೆಚ್ಚಿನ ಸಾಧನ ಕರೆಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೊನೆಗೂ ಉತ್ತರ ಸಿಗುವ ತನಕ.

ನಾವು LLM ಗೆ ಹಲವಾರು ಸಲ ಕರೆ ಮಾಡುತ್ತಿರುವುದರಿಂದ, LLM ಕರೆ ನಿರ್ವಹಿಸುವ ಒಂದಿಷ್ಟು ಫಂಕ್ಷನ್ ಅನ್ನು ಹೊಂದಿಸೋಣ. ಈ ಕೆಳಗಿನ ಕಾರ್ಯವನ್ನು ನಿಮ್ಮ `main.rs` ಫೈಲಿಗೆ ಸೇರಿಸಿ:

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

ಈ ಕಾರ್ಯವು LLM ಕ್ಲೈಯಂಟ್, ಸಂದೇಶಗಳ ಪಟ್ಟಿ (ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಸೇರಿ), MCP ಸರ್ವರ್ ಸಾಧನಗಳನ್ನು ತೆಗೆದುಕೊಂಡು LLM ಗೆ ವಿನಂತி ಕಳುಹಿಸಿ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.
LLM ರಿಂದ ಪ್ರತಿಕ್ರಿಯೆಯಲ್ಲಿ `choices` ಎಂಬ ಸರಣಿಯನ್ನು ಹೊಂದಿರುತ್ತದೆ. ಯಾವುದೇ `tool_calls` ಇದ್ದರೆ ಯಾಕೆಂದರೆ ಆಗ ಲ್ಲಿಎಂ ನಿರ್ದಿಷ್ಟವಾದ ಉಪಕರಣವನ್ನು ಅಭ್ಯರ್ಥಿಸುತ್ತಿದ್ದು ಅದರೊಂದಿಗೆ_arguments_ ಕರೆ ಮಾಡಬೇಕು ಎಂದು ತಿಳಿದುಕೊಳ್ಳಲು ಫಲಿತಾಂಶವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬೇಕಾಗುತ್ತದೆ. `main.rs` ಫೈಲ್‌ನ ಕೆಳಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿಭಾಯಿಸುವ ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲು:

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

    // ವಿಷಯ ಲಭ್ಯವಿದ್ದರೆ ಆನು ಪ್ರಿಂಟ್ ಮಾಡಿ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ಸಹಾಯಕ ಸಂದೇಶವನ್ನು ಸೇರಿಸಿ

        // ಪ್ರತಿಯೊಂದು ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ
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

        // ಉಪಕರಣ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸಿ
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

`tool_calls` ಇದ್ದರೆ ಅದು ಉಪಕರಣ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದು, ಉಪಕರಣ ವಿನಂತಿಯೊಂದಿಗೆ MCP ಸರ್ವರ್ ಅನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಭಾಷಣೆ ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸುತ್ತದೆ. ನಂತರ LLM ಜೊತೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸುತ್ತದೆ ಮತ್ತು ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಉಪಕರಣ ಕರೆ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಸಂದೇಶಗಳನ್ನು ನವಿಕರಿಸುತ್ತದೆ.

LLM MCP ಕರೆಗಳಿಗೆ ತಲುಪಿಸುವ ಉಪಕರಣ ಕರೆ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು, ನಾವು ಇನ್ನೊಂದು ಸಹಾಯಕ ಫಂಕ್ಷನ್ ಸೇರಿಸುತ್ತೇವೆ ಎಲ್ಲವೂ ಕರೆ ಮಾಡಲು ಅಗತ್ಯವಿದೆ ಅದನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು. `main.rs` ಫೈಲ್‌ನ ಕೆಳಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

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

ಎಲ್ಲಾ ಭಾಗಗಳು ಸ್ಥಳದಲ್ಲಿದ್ದು, ನಾವು ಈಗ ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ನಿಭಾಯಿಸಿ LLM ಅನ್ನು ಕರೆ ಮಾಡಬಹುದು. ಕೆಳಗಿನ ಕೋಡ್ ಬಳಸಲು ನಿಮ್ಮ `main` ಫಂಕ್ಷನ್ ಅನ್ನು ನವೀಕರಿಸಿ:

```rust
// ಉಪಕರಣಗಳು ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂವಹನ
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

ಇದು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಜೊತೆ LLM ಅನ್ನು ಪ್ರಶ್ನಿಸಿ ಎರಡು ಸಂಖ್ಯೆಗಳ ಮೊತ್ತ ಕೇಳುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ ಡೈನಾಮಿಕ್ ಉಪಕರಣ ಕರೆಗಳನ್ನು ನಿಭಾಯಿಸುತ್ತದೆ.

ಚೆನ್ನಾಗಿದೆ, ನೀವು bunu ಮಾಡಿದ್ದೀರಿ!

## ಅಸೈನ್ಮೆಂಟ್

ಅಭ್ಯಾಸದಿಂದ ಕೋಡ್ ತೆಗೆದುಕೊಂಡು ಸರ್ವರ್ ಅನ್ನು ಕೆಲವು ಹೆಚ್ಚಿನ ಉಪಕರಣಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸಿ. ನಂತರ LLM ಇರುವ ಕ್ಲೈಂಟ್ ಅನ್ನು ತಯಾರಿಸಿ, ಅಭ್ಯಾಸದಂತೆ, ಮತ್ತು ವಿವಿಧ ಪ್ರಾಂಪ್ಟ್‌ಗಳಿಂದ ಪರೀಕ್ಷಿಸಿ ನಿಮ್ಮ ಸರ್ವರ್ ಉಪಕರಣಗಳು ಡೈನಾಮಿಕ್‌గా ಕರೆಮಾಡುತ್ತಿದ್ದವೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಈ ರೀತಿಯ ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಣದಿಂದ ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವ ಸಿಗುತ್ತದೆ ಏಕೆಂದರೆ ಅವರು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಬಹುದಾಗಿದೆ, ನಿಖರ ಕ್ಲೈಂಟ್ ಆಜ್ಞೆಗಳನ್ನು ಅಲ್ಲ, ಮತ್ತು ಯಾವುದೇ MCP ಸರ್ವರ್ ಕರೆ ಮಾಡಲಾಗುತ್ತಿದೆಯೆಂದು ಅರಿತುಕೊಳ್ಳಲಾರರು.

## ಪರಿಹಾರ

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ಪ್ರಮುಖ ಅಂಶಗಳು

- ನಿಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದು MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಬಳಕೆದಾರರ ಸಂವಹನದ ಉತ್ತಮ ವಿಧಾನವನ್ನು ಒದಗಿಸುತ್ತದೆ.
- MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ಅರ್ಥವಾಗುವಂತೆ ಪರಿವರ್ತಿಸಲು ನೀವು ಬೇಕಾಗುತ್ತದೆ.

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
**պրత్యೇಕ ಸೂಚನೆ**:  
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಭಾಷಾಂತರ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದಾದದನ್ನು ತಿಳಿದುಕೊಳ್ಳಿ. ಮೂಲ ಭಾಷೆಯ ದಾಖಲೆಯನ್ನು ಅಧಿಕಾರಿಕ ಮೂಲವಾಗೆ ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಕಲ್ಪನೆಗಳಿಗೆ ಅಥವಾ ತಪ್ಪಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರಿಗಳಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->