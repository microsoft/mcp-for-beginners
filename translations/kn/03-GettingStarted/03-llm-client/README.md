# LLM ಆದಾನೊಂದಿಗೆ ಕ್ಲೈಂಟ್ ರಚನೆ ಮಾಡುವುದು

> [!NOTE]
> ಜಾವಾ ಕ್ಲೈಂಟ್ ಉದಾಹರಣೆಗಳು ಹಳೆಯ HTTP+SSE ಸಂಚಾರದ ಮೂಲಕ ಸಂಪರ್ಕಿಸುತ್ತದೆ ಮತ್ತು
> MCP `2025-11-25` SDK APIs ಗುರಿಯಾಗಿವೆ. ಹೊಸ ರಿಮೋಟ್ ಕ್ಲೈಂಟ್ಗಾಗಿ `2026-07-28`-ಅನುಕೂಲಿತ SDK ಮತ್ತು
> ಸ್ಟ್ರೀಮಬಲ್ HTTP ಅನ್ನು ಬಳಸಿ.

ಇದುವರೆಗಿನವರೆಗೂ ನೀವು ಹೇಗೆ ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸುವುದನ್ನು ನೋಡಿ ಬಂದಿದ್ದೀರಿ. ಕ್ಲೈಂಟ್ ತೆರಮೆಗೆ ಸ್ಪಷ್ಟವಾಗಿ ಕರೆಮಾಡಿ ಅದರ ಸಾಧನಗಳು, ಸಂಪನ್ಮೂಲಗಳು, ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಬಹುದಾಗಿ ಅನುಮತಿಸಿದೆ. ಆದರೆ, ಇದು ಬಹುಪಯೋಗದ ವಿಧಾನವಲ್ಲ. ನಿಮ್ಮ ಬಳಕೆದಾರರು ಏಜೆಂಟಿಕ್ ಯುಗದಲ್ಲಿ ನೆಲೆಸಿದ್ದಾರೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಲು ಮತ್ತು LLM ಜೊತೆ ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಅವರು ನಿಮ್ಮ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸಂಗ್ರಹಿಸಲು MCP ಬಳಸುವುದನ್ನು ಗಮನಿಸುವುದಿಲ್ಲ; ಅವರು ಸರಳವಾಗಿ ನೈಸರ್ಗಿಕ ಭಾಷೆಯನ್ನು ಉಪಯೋಗಿಸಿ ಸಂವಹನ ಮಾಡಲು ಬಯಸುತ್ತಾರೆ. ಹಾಗಾದರೆ ಇದನ್ನು ನೀವು ಹೇಗೆ ಪರಿಹರಿಸುತ್ತೀರಿ? ಪರಿಹಾರವೆಂದರೆ LLM ಅನ್ನು ಕ್ಲೈಂಟ್‌ಗೆ ಸೇರಿಸುವುದು.

## ಅವಲೋಕನ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಕ್ಲೈಂಟ್‌ಗೆ LLM ಅನ್ನು ಸೇರಿಸುವ ಮೇಲೆ ಗುರಿಯಾಗುತ್ತೇವೆ ಮತ್ತು ಇದು ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಹೇಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ನೀಡುತ್ತದೆ ಎಂದು ತೋರಿಸುತ್ತೇವೆ.

## ಕಲಿಕಾ ಗುರಿಗಳು

ಈ ಪಾಠದ ಕೊನೆಗೆ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- LLM ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ರಚಿಸಲು.
- LLM ಬಳಸಿ MCP ಸರ್ವರ್ ಜೊತೆ ಸೌಕರ್ಯದಿಂದ ಸಂವಹನ ಮಾಡಲು.
- ಕ್ಲೈಂಟ್ ಪರವಾಗಿ ಉತ್ತಮ ಅಂತಿಮ ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಒದಗಿಸಲು.

## ವಿಧಾನ

ನಾವು ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳೋಣ. LLM ಸೇರಿಸುವುದು ಸರಳವಾಗಿ ಕೇಳುತ್ತದೆ, ಆದರೆ ನಾವು ನಿಜವಾಗಿಯೂ ಇದನ್ನು ಮಾಡುವೇವೋ?

ಇಲ್ಲಿದೆ ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನ ಮಾಡುವ ರೀತಿಯ ವಿವರಣೆ:

1. ಸರ್ವರ್ ಜೊತೆಗೆ ಸಂಪರ್ಕ ಸ್ಥಾಪಿಸು.

1. ಸಾಮರ್ಥ್ಯಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ, ಅವುಗಳ ಸ್ಕೀಮಾವನ್ನು ಉಳಿಸಿ.

1. LLM ಸೇರಿಸಿ ಮತ್ತು ಉಳಿಸಿಕೊಂಡ ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಆ ಶಾಲೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಫಾರ್ಮ್ಯಾಟ್ ನಲ್ಲಿ ಪಾಸ್ ಮಾಡಿ.

1. ಬಳಕೆದಾರನ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಗೆ ತುಂಬಿಸಿ ಮತ್ತು ಕ್ಲೈಂಟ್ ಪಟ್ಟಿ ಮಾಡಿದ ಸಾಧನಗಳೊಂದಿಗೆ ನಿರ್ವಹಿಸು.

ಚೆನ್ನಾಗಿದೆ, ಈಗ ನಾವು ಮೇಲ್ನೋಟದಲ್ಲಿ ಇದನ್ನು ಹೇಗೆ ಮಾಡಬಹುದು ಎಂದು ಅರ್ಥ ಮಾಡಿಕೊಂಡಿದ್ದೇವೆ, ಕೆಳಗಿನ ವ್ಯಾಯಾಮದಲ್ಲಿ ಇದನ್ನು ಪ್ರಯತ್ನಿಸೋಣ.

## ವ್ಯಾಯಾಮ: LLM ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ರಚನೆ

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ, ನಾವು ನಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದನ್ನು ಕಲಿಯುವೆವು.

### ಗಿಥಬ್ ಪರ್ಸನಲ್ ಆಕ್ಸೆಸ್ ಟೋಕನ್ ಬಳಸಿ ಪ್ರಮಾಣೀಕರಣ

ಗಿಥಬ್ ಟೋಕನ್ ರಚಿಸುವುದು ಸರಳ ಪ್ರಕ್ರಿಯೆಯಾಗಿದೆ. ಇಲ್ಲಿದೆ ನೀವು ಇದನ್ನು ಹೇಗೆ ಮಾಡಬೇಕು:

- ಗಿಥಬ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಗೆ ಹೋಗಿ – ಮೇಲ್ಭಾಗದ ಬಲತಿರುವಿನಲ್ಲಿ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಚಿತ್ರದಲ್ಲಿ ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಸ್ ಆಯ್ಕೆಮಾಡಿ.
- ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಗೆ ಸಾಗು – ಕೆಳಗೆ ಸ್ವೈಪ್ ಮಾಡಿ ಮತ್ತು ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
- ಪರ್ಸನಲ್ ಆಕ್ಸೆಸ್ ಟೋಕನ್ಸ್ ಆಯ್ಕೆ ಮಾಡು – ಫೈನ್-ಗ್ರೇನ್ಡ್ ಟೋಕನ್ಸ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಹೊಸ ಟೋಕನ್ ತಯಾರಿಸಿ.
- ನಿಮ್ಮ ಟೋಕನನ್ನು ಹೊಂದಿಸಿ – ಉಲ್ಲೇಖಕ್ಕಾಗಿ ಟಿಪ್ಪಣಿ ಸೇರಿಸಿ, ಅವಧಿ ಅಂತ್ಯವನ್ನು ಹೊಂದಿಸಿ, ಮತ್ತು ಅಗತ್ಯ ಅನುಮತಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ. ಈ ಸಂದರ್ಭದಲ್ಲಿ, ಮಾದರಿಗಳ ಅನುಮತಿಯನ್ನು ಸೇರಿಸುವುದಾಗಿ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
- ಟೋಕನ್ ತಯಾರಿಸಿ ಮತ್ತು ನಕಲಿಸಿ – ಟೋಕನ್ ತಯಾರಿಸಿ ಕ್ಲಿಕ್ ಮಾಡಿ, ಮತ್ತು ಅದನ್ನು ತಕ್ಷಣ ನಕಲಿಸಿ, ಏಕೆಂದರೆ ನೀವು ಮತ್ತೆ ನೋಡಲು ಸಾಧ್ಯವಾಗುವುದಿಲ್ಲ.

### -1- ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕ ಮಾಡುವುದು

ಮೊದಲು ನಾವು ನಮ್ಮ ಕ್ಲೈಂಟ್ ರಚಿಸೋಣ:

#### ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಪರಿಶೀಲನೆಯಿಗಾಗಿ zod ಅನ್ನು ಆಮದುಮಾಡಿ

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

ಮೇಲಿನ ಕಡೆಯಲ್ಲಿರುವ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಅಗತ್ಯ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಇಮ್ಮದುಮಾಡಿದೆವು
- `client` ಮತ್ತು `openai` ಎಂಬ ಎರಡು ಸದಸ್ಯರೊಂದಿಗೆ ಕ್ಲಾಸನ್ನು ರಚಿಸಿದೆವು, ಇವು ಸಮನ್ವಯದಂತೆ LLM ಜೊತೆ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- GitHub ಮಾದರಿಗಳನ್ನು ಬಳಸಲು LLM ಘಟಕವನ್ನು `baseUrl` ಅನ್ನು ಇನ್ಫರೆನ್ಸ್ API ಗೆ ಸೂಚಿಸುವ ಮೂಲಕ ಹೊಂದಿಸಿದೆವು.

#### ಪೈಥಾನ್

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪರಿಮಾಣಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯಾಚರಿಪಡಬಹುದಾದ
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ ಆರ್ಗ್ಯೂಮೆಂಟ್ಗಳು
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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಗೆ ಅಗತ್ಯ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಇಮ್ಪೋರ್ಟ್ ಮಾಡಿದೆವು
- ಒಂದು ಕ್ಲೈಂಟ್ ರಚಿಸಿದೆವು

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

#### ಜಾವಾ

ಮೊದಲು, ನಿಮ್ಮ `pom.xml` ಕಡತದಲ್ಲಿ LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಬೇಕು. MCP ಎಸ್ ಇಂಟಿಗ್ರೇಶನ್ಗೆ ಮತ್ತು OpenAI-ಅನುಕೂಲ MiniMax API ಗೆ ಈ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

ನಿಮ್ಮ MiniMax API ಕೀ ಮತ್ತು ಐಚ್ಛಿಕವಾಗಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಮಾದರಿಯನ್ನು ಸೆಟ್ ಮಾಡಿ.
`MINIMAX_MODEL_ID` `MiniMax-M3` ಮತ್ತು `MiniMax-M2.7` ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. 
`OPENAI_BASE_URL` ಸಜ್ಜುಗೊಂಡಿಲ್ಲದಿದ್ದರೆ, `MINIMAX_REGION` `global_en` ಮತ್ತು `cn_zh` ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ಇಲ್ಲವಾದರೆ, ಪ್ರಾಂತ್ಯ ಆಧಾರಿತ ಎಂಡ್ಪಾಯಿಂಟ್ ಆಯ್ಕೆ ಮಾಡಲು, `OPENAI_BASE_URL` ಅನ್ನು ಬಿಡಿ:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ನಂತರ, ನಿಮ್ಮ Java ಕ್ಲೈಂಟ್ ಕ್ಲಾಸನ್ನು ರಚಿಸಿ:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- **LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿದೆವು**: MCP ಎಂಟಿಗ್ರೇಶನ್ ಮತ್ತು OpenAI-ಅನುಕೂಲ MiniMax API ಗಾಗಿ ಅಗತ್ಯ
- **LangChain4j ಗ್ರಂಥಾಲಯಗಳನ್ನು ಇಂಪೋರ್ಟ್ ಮಾಡಿದೆವು**: MCP ಎಂಟಿಗ್ರೇಶನ್ ಮತ್ತು OpenAI ಚಾಟ್ ಮಾದರಿ ಕಾರ್ಯಾಚರಣೆಗೆ
- **`ChatLanguageModel` ರಚಿಸಿದೆವು**: MiniMax ಬಳಸಿ ನಿಮ್ಮ MiniMax API ಕೀ, ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು ಬೆಂಬಲಿತ ಮಾದರಿ ಐಡಿ ಹೊಂದಿಸಿರುವ
- **HTTP ಸಂಚಾರ ಸಿದ್ಧಪಡಿಸಿದೆವು**: ಸರ್ವರ್-ಸೆಂಟ್ ಇವೆಂಟ್ಸ್ (SSE) ಬಳಸಿ MCP ಸರ್ವರ್ ಸಂಪರ್ಕಿಸಲು
- **MCP ಕ್ಲೈಂಟ್ ರಚಿಸಿದೆವು**: ಸರ್ವರ್‍ಸಂದೇಶ ವಿವರಣೆ ನಿರ್ವಹಿಸಲು
- **LangChain4j ಸಜ್ಜುಗೊಂಡ MCP ಬೆಂಬಲ ಬಳಿದೆವು**: ಇದು LLM ಮತ್ತು MCP ಸರ್ವರ್ಗಳ ನಡುವಣ ಇಂಟಿಗ್ರೇಶನ್ ಸರಳಗೊಳಿಸುತ್ತದೆ

#### ರಸ್ಟು

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ನೀವು ರಸ್ಟು ಆಧಾರಿತ MCP ಸರ್ವರ್ ಇದ್ದೀರಿ ಎಂದು ಊಹಿಸಲಾಗಿದೆ. ನೀವು ಇದನ್ನು ಹೊಂದಿಲ್ಲದಿದ್ದರೆ, ಸರ್ವರ್ ರಚಿಸಲು [01-first-server](../01-first-server/README.md) ಪಾಠವನ್ನು ನೋಡಿ.

ನಿಮ್ಮ ರಸ್ಟು MCP ಸರ್ವರ್ ಇದ್ದಂತೆ, ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಸರ್ವರ್ ಅಪ್ಲಿಕೇಶನ್ ಇರುವ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ ಹೋಗಿ. ನಂತರ ಹೊಸ LLM ಕ್ಲೈಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು ಈ ಆದೇಶವನ್ನು ನಡಿಸಿ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ನಿಮ್ಮ `Cargo.toml` ಕಡತದಲ್ಲಿ ಕೆಳಗಿನ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ಅಧಿಕೃತ ರಸ್ಟು ಲೈಬ್ರರಿ OpenAI ಗಾಗಿ ಇಲ್ಲ, ಆದರೆ `async-openai` ಕ್ರೇಟ್ ಒಂದು [ಸಮುದಾಯ ನಿರ್ವಹಿತ ಗ್ರಂಥಾಲಯ](https://platform.openai.com/docs/libraries/rust#rust) ಆಗಿದ್ದು ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ.

`src/main.rs` ಕಡತವನ್ನು ತೆರೆಯಿರಿ ಮತ್ತು ಅದರ ವಿಷಯವನ್ನು ಈ ಕೆಳಗಿನ ಕೋಡ್‌ನೊಂದಿಗೆ ಬದಲಿಸಿರಿ:

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
    // ಪ್ರಾರಂಭ ಸಂದೇಶ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ಕ್ಲಯಿಂಟ್ ಸೆಟಪ್ ಮಾಡು
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ಕ್ಲಯಿಂಟ್ ಸೆಟಪ್ ಮಾಡು
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

ಈ ಕೋಡ್ ಒಂದು ಮೂಲ ರಸ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಸಜ್ಜುಗೊಳಿಸುತ್ತದೆ, ಇದು MCP ಸರ್ವರ್ ಮತ್ತು GitHub ಮಾದರಿಗಳೊಂದಿಗೆ LLM ಸಂವಹನಕ್ಕೆ ಸಂಪರ್ಕ ಹೊಂದುತ್ತದೆ.

> [!IMPORTANT]
> ಅಪ್ಲಿಕೇಶನ್ ಸ್ಟಾರ್ಟ್ ಮಾಡುವ ಮುನ್ನ ನಿಮ್ಮ GitHub ಟೋಕನ್ `OPENAI_API_KEY` ಪರಿಸರಚರ ನಿಯಂತ್ರಣವನ್ನು ಹೊಂದಿಸಿಕೊಳ್ಳಿ.

ಚೆನ್ನಾಗಿದೆ, ನಾವು ಮುಂದಿನ ಹಂತವಾಗಿ ಸರ್ವರ್‌ನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡೋಣ.

### -2- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡು

ಈಗ ನಾವು ಸರ್ವರ್‍ಗೆ ಸಂಪರ್ಕಿಸಿ ಅದರ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಕೇಳುತ್ತೇವೆ:

#### ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್

ಅದೇ ಕ್ಲಾಸಿನಲ್ಲಿ, ಕೆಳಗಿನ ವಿಧಾನಗಳನ್ನು ಸೇರಿಸಿ:

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್ ಸಂಪರ್ಕ ಕೋಡ್ ಸೇರಿಸಿದೆವು, `connectToServer`.
- ಅಪ್ಲಿಕೇಶನ್ ಫ್ಲೋ ನಿರ್ವಹಿಸುವ `run` ವಿಧಾನ ನಿರ್ಮಿಸಿದೆವು. ಇದುವರೆಗೆ ಮಾತ್ರ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ ಆದರೆ ನಾವು ಶೀಘ್ರದಲ್ಲೇ ಇದಕ್ಕೆ ಹೆಚ್ಚು ಸೇರಿಸಲಿದ್ದೇವೆ.

#### ಪೈಥಾನ್

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

- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮುದ್ರಣ ಮಾಡಿದೆವು. ಸಾಧನಗಳಿಗೆ ನಾವು ನಂತರ ಬಳಸುವ `inputSchema` ಕೂಡ ಪಟ್ಟಿ ಮಾಡಿದೆವು.

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


ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ
- ಪ್ರತಿ ಸಾಧನಕ್ಕೆ ಅದರ ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಅದರ ಸ್ಕೀಮಾವನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ್ದೇವೆ. ಈ ಕೊನೆಯದು ನಾವು Shortly ಸಾಧನಗಳನ್ನು ಕರೆ ಮಾಡಲು ಬಳಸುವದ್ದು.

#### ಜಾವಾ

```java
// MCP ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಂಡುಹಿಡಿಯುವ ಸಾಧನ ಪೂರೈಕೆದಾರ ರಚಿಸಿ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ಸಾಧನ ಪೂರೈಕೆದಾರ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
// - MCP ಸರ್ವರ್‌ನಿಂದ ಲಭ್ಯವಿರುವ ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
// - MCP ಸಾಧನ ಸ್ಕೀಮಾಗಳನ್ನು LangChain4j ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವುದು
// - ಸಾಧನ ಕಾರ್ಯಾಚರಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳ ನಿರ್ವಹಣೆ
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಎಲ್ಲಾ ಸಾಧನಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಹುಡುಕಿ ನೋಂದಣಿ ಮಾಡಲು `McpToolProvider` ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ
- ಸಾಧನ ಒದಗಿಸುವವರು MCP ಸಾಧನ ಸ್ಕೀಮಾಗಳ ಮತ್ತು LangChain4j ನ ಸಾಧನ ಸ್ವರೂಪದ ಮಧ್ಯೆ ಇರುವ ಪರಿವರ್ತನೆಯನ್ನು ಒಳಗೂ ನಿಭಾಯಿಸುತ್ತಾರೆ
- ಈ ಕ್ರಮವು ಕೈಯಿಂದ ಸಾಧನಗಳ ಪಟ್ಟಿ ಹಾಗೂ ಪರಿವರ್ತನೆ ಪ್ರಕ್ರಿಯೆಯನ್ನು abstraction ಮಾಡುತ್ತದೆ

#### ರಸ್ಟ್

MCP ಸರ್ವರ್‌ನಿಂದ ಸಾಧನಗಳನ್ನು ಪಡೆಯುವುದು `list_tools` ವಿಧಾನವನ್ನು ಬಳಸಿ ನಡೆಯುತ್ತದೆ. ನಿಮ್ಮ `main` ಕಾರ್ಯದಲ್ಲಿ, MCP ಕ್ಲೈಂಟ್ ಸೆಟ್‌ಅಪ್ ಮಾಡಿದ ನಂತರ, ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

```rust
// MCP ಉಪಕರಣ ಪಟ್ಟಿ ಪಡೆದುಕೊಳ್ಳಿ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು LLM ಸಾಧನಗಳಿಗೆ ಪರಿವರ್ತಿಸು

ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿದ ನಂತರದ ಹಂತವು ಅವುಗಳನ್ನು LLM ಗೆ ಅರ್ಥವಾಗುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವುದಾಗಿದೆ. ಅದಾದ ಮೇಲೆ ನಾವು ಈ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನಮ್ಮ LLM ಗೆ ಸಾಧನಗಳಾಗಿ ಒದಗಿಸಬಹುದು.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

1. MCP ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಬಳಸಬಹುದಾದ ಸಾಧನ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ಇನ್ಪುಟ್‌_ಸ್ಕೀಮಾ ಅವಲಂಬಿಸಿ ಓಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರಕಾರವನ್ನು "ಫಂಕ್ಷನ್" ಎಂದು ಹೊಂದಿಸಿ
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

    ಮೇಲಿನ ಕೋಡ್ MCP ಸರ್ವರ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು ಅದನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳಬಹುದಾದ ಸಾಧನ ವ್ಯಾಖ್ಯಾನದ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

2. ನಂತರ, ಸರ್ವರ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಲು `run` ವಿಧಾನವನ್ನು ನವೀಕರಿಸೋಣ:

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

    ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ, ನಾವು `run` ವಿಧಾನವನ್ನು ಫಲಿತಾಂಶದ ಮೂಲಕ ನಕ್ಷೆ ಮಾಡುತ್ತೇವೆ ಮತ್ತು ಪ್ರತಿ ಎಂಟ್ರಿಗೆ `openAiToolAdapter` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತೇವೆ.

#### ಪೈಥಾನ್

1. ಮೊದಲು, ಕೆಳಗಿನ ಪರಿವರ್ತಕ ಕಾರ್ಯವನ್ನು ರಚಿಸೋಣ

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

    ಮೇಲಿನ `convert_to_llm_tools` ಕಾರ್ಯದಲ್ಲಿ ನಾವು MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು ಅದನ್ನು LLM ಅರ್ಥ ಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತೇವೆ.

2. ನಂತರ, ಈ ಕಾರ್ಯವನ್ನು ಉಪಯೋಗಿಸಲು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡ್ ಅನ್ನು ನವೀಕರಿಸೋಣ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ಇಲ್ಲಿ, ನಾವು `convert_to_llm_tool` ಅನ್ನು ಕರೆ ಮಾಡುತ್ತಿರುವೆವು MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ನೀಡಲು ಪರಿವರ್ತಿಸಲು.

#### .NET

1. MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ಕೋಡ್ ಸೇರಿಸಲಾಗುವುದು

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

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್ಪುಟ್ ಸ್ಕೀಮಾ ತೆಗೆದುಕೊಳ್ಳುವ `ConvertFrom` ಕಾರ್ಯವನ್ನು ಸೃಷ್ಟಿಸಿದ್ದೇವೆ.
- FunctionDefinition ರಚಿಸುವ ಕಾರ್ಯನಿರ್ವಹಣೆ ನಿರ್ದಿಷ್ಟಪಡಿಸಲಾಗಿದೆ, ಅದು ChatCompletionsDefinition ಗೆ ಪಾಸಾಗುತ್ತದೆ. ಇದು LLM ಗೆ ಅರ್ಥವಾಗುವವಷ್ಟರಲ್ಲಿದೆ.

2. ಮೇಲಿನ ಕಾರ್ಯವನ್ನು ಬಳಸಲು ಇದ್ದ ಕೋಡ್ ಅನ್ನು ನವೀಕರಿಸುವ ವಿಧಾನ:

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

#### ಜಾವಾ

```java
// ಸಹಜ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಬಾಟ್ ಇಂಟರ್ಫೇಸ್ ರಚಿಸಿ
public interface Bot {
    String chat(String prompt);
}

// LLM ಮತ್ತು MCP ಸಾಧನಗಳೊಂದಿಗೆ AI ಸೇವೆಯನ್ನು ಸಂರಚಿಸಿ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನಾವು:

- ಸಹಜ ಭಾಷಾ ಸಂವಹನಗಳಿಗೆ ಸರಳ `Bot` ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಗಟ್ಟುಮಾಡಿದ್ದೇವೆ
- LangChain4j ನ `AiServices` ಬಳಸಿ MCP ಸಾಧನ ಒದಗಿಸುವವರೊಂದಿಗೆ LLM ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬಾಂಧಿಸಿ ಮಾಡಲಾಗಿದೆ
- ಫ್ರೇಮ್ವರ್ಕ್ ಸಾಧನ ಸ್ಕೀಮಾ ಪರಿವರ್ತನೆ ಮತ್ತು ವಿಧಾನ ಕರೆಗಳನ್ನು ಹಿನ್ನೆಲೆಗಳಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿಭಾಯಿಸುತ್ತದೆ
- ಈ ವಿಧಾನದಿಂದ ಕೈಯಿಂದ ಸಾಧನ ಪರಿವರ್ತನೆ ಅಗತ್ಯವಿಲ್ಲ - LangChain4j MCP ಸಾಧನಗಳನ್ನು LLM-ಸಹಜ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುವ ಜಟಿಲತೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ

#### ರಸ್ಟ್

MCP ಸಾಧನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು ನಾವು ಸಹಾಯಕ ಕಾರ್ಯವನ್ನು ಸೇರಿಸುವೆವು, ಅದು ಸಾಧನಗಳ ಪಟ್ಟಿ ಸ್ವರೂಪಗೊಳಿಸುತ್ತದೆ. `main.rs` ಫೈಲ್‌ನ `main` ಕಾರ್ಯದ ಕೆಳಗೆ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ. ಇದು LLM ಗೆ ವಿನಂತಿ ಮಾಡುವಾಗ ಕರೆಯಲಾಗುತ್ತದೆ:

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


ಚೆನ್ನಾಗಿದೆ, ನಾವು ಯಾವುದೇ ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಜ್ಜಾಗಿಲ್ಲ, ಆದ್ದರಿಂದ ಅದನ್ನು ಮುಂದಿನದಾಗಿ ನೋಡೋಣ.

### -4- ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ನಿರ್ವಹಿಸಿ

ಈ ಭಾಗದಲ್ಲಿ ನಾವು ಬಳಕೆದಾರ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುವೆವು.

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

1. ನಮ್ಮ LLM ಅನ್ನು ಕರೆಯಲು ಉಪಯೋಗಿಸುವ ವಿಧಾನವನ್ನು ಸೇರಿಸಿ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ಸರ್ವರ್‌ನ ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನೋ ಮಾಡಿ
        // ಮಾಡಲು ಬಾಕಿ

        }
    }
    ```

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - `callTools` ಎಂಬ ವಿಧಾನವನ್ನು ಸೇರಿಸಿದೆವು.
    - ಆ ವಿಧಾನವು LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಯಾವ ಉಪಕರಣಗಳನ್ನು ಕರೆಮಾಡಲಾಗಿದೆ ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ, ಇದ್ದರೆ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ಉಪಕರಣವನ್ನು ಕರೆಯಿರಿ
        }
        ```

    - LLM ಕರೆ ಮಾಡುವುದಾಗಿ ಸೂಚಿಸಿದರೆ ಉಪಕರಣವನ್ನು ಕರೆಯುತ್ತದೆ:

        ```typescript
        // 2. ಸರ್ವರ್‌ನ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನೋ ಮಾಡಿ
        // TODO
        ```

2. ಲ್ಲೋಡ್ ವಿಧಾನವನ್ನು LLM ಅನ್ನು ಕರೆಮಾಡಲು ಮತ್ತು `callTools` ಅನ್ನು ಕರೆಮಾಡಲು ಅಪ್ಡೇಟ್ ಮಾಡಿ:

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

    // 2. LLM ಅನ್ನು ಕರೆಸುವುದು
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಆಯ್ಕೆಯನ್ನು, ಇದರಲ್ಲಿоборಟುಗಳನ್ನು ಕರೆಸಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ಚೆನ್ನಾಗಿದೆ, ಸಂಪೂರ್ಣ ಕೋಡ್ ಅನ್ನು ಪಟ್ಟಿಮಾಡೋಣ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ ಜೋಡ್ ಅನ್ನು ಆಮದುಮಾಡಿ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ಭವಿಷ್ಯದಲ್ಲಿ ಈ URL ಗೆ ಬದಲಾವಣೆ ಅಗತ್ಯವಿರಬಹುದು: https://models.github.ai/inference
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
          // ಇನ್ಪುಟ್ ಸ್ಕೀಮಾ ಆಧರಿಸಿ ಜೋಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ಪ್ರಕಾರವನ್ನು ಸ್ಪಷ್ಟವಾಗಿ "function" ಎಂದು ಸೆಟ್ ಮಾಡಿ
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
    
    
          // 2. ಸರ್ವರಿನ ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
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
    
        // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯ ಮೂಲಕ ಹೋಗಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ, ಅದು ಸಾಧನ ಕರೆದಿರುತ್ತದೆಯೆ ಎಂದು ಪರಿಶೀಲಿಸಿ
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

#### ಪೈಥಾನ್

1. LLM ಅನ್ನು ಕರೆಮಾಡಲು ಬೇಕಾಗುವ ಕೆಲವು ಇಂಪೋರ್ಟ್‌ಗಳನ್ನು ಸೇರಿಸೋಣ

    ```python
    # ಎಲ್‌ಎಲ್‌ಎಂ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. ಇದೀಗ, LLM ಅನ್ನು ಕರೆಮಾಡುವ ಫಂಕ್ಷನ್ ಅನ್ನು ಸೇರಿಸೋಣ:

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
            # ೖಕಂಸ್ಥ್ರೀಯ ಪದಾರ್ಥಗಳು
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

    - MCP ಸರ್ವರ್‌ನ ಮೇಲೆ ಕಂಡುಹಿಡಿದ ಮತ್ತು ಪರಿವರ್ತಿಸಿದ ನಮ್ಮ ಫಂಕ್ಷನ್ಗಳನ್ನು LLM ಗೆ ಹಂಚಿಹೋಗಿದ್ದೇವೆ.
    - ನಂತರ, ಆ ಫಂಕ್ಷನ್ಗಳೊಂದಿಗೆ LLM ಅನ್ನು ಕರೆಮಾಡಿದೆವು.
    - ನಂತರ, ಫಲಿತಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾವ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಕರೆಮಾಡಬೇಕು ಎಂಬುದನ್ನು ನೋಡುತ್ತಿದ್ದೇವೆ.
    - ಕೊನೆಗೆ, ಕರೆಮಾಡಬೇಕಾದ ಫಂಕ್ಷನ್ಗಳ ಪ್ರತ್ಯೇಕ ಆರೆ ಹಂಚಬಹುದು.

3. ಕೊನೆಯ ಹಂತ, ನಿಮ್ಮ ಮುಖ್ಯ ಕೋಡ್ ಅನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡೋಣ:

    ```python
    prompt = "Add 2 to 20"

    # ಎಲ್ಲದಕ್ಕೂ ಯಾವ ಸಾಧನಗಳನ್ನು ಬಳಸಬೇಕು ಎಂದು LLMಿಗೆ ಕೇಳಿ, ಇದ್ದರೆವೇನಾದರೂ
    functions_to_call = call_llm(prompt, functions)

    # ಸೂಚಿಸಲಾದ ಕಾರ್ಯಗಳನ್ನು ಕರೆ ಮಾಡಿ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ಆ, ಅದು ಕೊನೆಯ ಹಂತ, ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - LLM ಪ್ರಾಂಪ್ಟ್ ಆಧಾರಿತವಾಗಿ ಕರೆಮಾಡಬೇಕಾದ ಫಂಕ್ಷನ್ ಅನ್ನು `call_tool` ಮೂಲಕ MCP ಉಪಕರಣಕ್ಕೆ ಕರೆಮಾಡುತ್ತಿದ್ದೇವೆ.
    - ಉಪಕರಣ ಕರೆಮಾದ ಫಲಿತಾಂಶವನ್ನು MCP ಸರ್ವರ್‌ಗೆ ಮುದ್ರಣ ಮಾಡುತ್ತಿದ್ದೇವೆ.

#### . ನೆಟ್

1. LLM ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ಮಾಡುವ ಕೆಲವು ಕೋಡ್ ತೋರಿಸೋಣ:

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - MCP ಸರ್ವರ್‌ನಿಂದ ಉಪಕರಣಗಳನ್ನು ಪಡೆದುಕೊಂಡಿದ್ದೇವೆ, `var tools = await GetMcpTools()`.
    - ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ `userMessage` ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ.
    - ಮಾದರಿ ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ವಿವರಿಸುವ ಆಯ್ಕೆಗಳು ಆಬ್ಜೆಕ್ಟ್ ಅನ್ನು ರಚಿಸಿದ್ದೇವೆ.
    - LLM ಕಡೆಗೆ ವಿನಂತಿ ಮಾಡಿದ್ದೇವೆ.

2. ಕೊನೆಯ ಹಂತ, LLM ನಾವು ಫಂಕ್ಷನ್ ಅನ್ನು ಕರೆಮಾಡೋಣವೆಂದು ಭಾವಿಸುವುದೇನೋ ನೋಡೋಣ:

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

    - ಫಂಕ್ಷನ್ ಕರೆಗಳ ಪಟ್ಟಿಯ ಮೂಲಕ ಲೂಪ್ ಮಾಡುತ್ತಿದ್ದೇವೆ.
    - ಪ್ರತಿ ಉಪಕರಣ ಕರೆಗಾಗಿ, ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ ಮತ್ತು MCP ಕ್ಲೈಂಟ್ ಬಳಸಿ MCP ಸರ್ವರ್‌ನ ಮೇಲೆ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ. ಕೊನೆಗೆ ಫಲಿತಾಂಶಗಳನ್ನು ಮುದ್ರಣ ಮಾಡುತ್ತೇವೆ.

ಇಲ್ಲಿದೆ ಸಂಪೂರ್ಣ ಕೋಡ್:

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

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### ಜಾವಾ

```java
try {
    // ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಸಾಧನಗಳನ್ನು ಬಳಸುವ ಸಹಜ ಭಾಷಾ ವಿನಂತಿಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರಳ ಸ್ವಭಾವದ ಭಾಷೆ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಿ MCP ಸರ್ವರ್ ಉಪಕರಣಗಳೊಂದಿಗಿನ ಸಂವಹನ ಮಾಡಿದೆವು
- LangChain4j ಫ್ರೇಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
  - ಬೇಡಿಕೆಯ ಪ್ರಕಾರ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಉಪಕರಣ ಕರೆಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದು
  - LLM ನ ತೀರ್ಮಾನ ಆಧಾರಿತವಾಗಿ ಸರಿಯಾದ MCP ಉಪಕರಣಗಳನ್ನು ಕರೆಮಾಡುವುದು
  - LLM ಮತ್ತು MCP ಸರ್ವರ್ ನಡುವಣ ಸಂಭಾಷಣಾ ಸರಣಿಯನ್ನು ನಿರ್ವಹಿಸುವುದು
- `bot.chat()` ವಿಧಾನವು ಸಹಜ ಭಾಷೆಯ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೀಡುತ್ತದೆ, ಅದು MCP ಉಪಕರಣಗಳ ಕಾರ್ಯಾಚರಣೆ ಫಲಿತಾಂಶಗಳನ್ನು ಒಳಗೊಂಡಿರಬಹುದು
- ಇದು ಬಳಕೆದಾರರಿಗೆ ಅಡಿಗಲ್ಲಿನ MCP ಅನುಷ್ಠಾನವನ್ನು ತಿಳಿಯದಷ್ಟು ಸುಗಮ ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ

ಸಂಪೂರ್ಣ ಕೋಡ್ ಉದಾಹರಣೆ:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### ರಸ್ಟ


ಇಲ್ಲಿ ಹೆಚ್ಚಿನ ಭಾಗದ ಕೆಲಸ ನಡೆಯುತ್ತದೆ. ನಾವು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ನೊಂದಿಗೆ LLM ಅನ್ನು ಕರೆಸುತ್ತೇವೆ, ನಂತರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ ಯಾವುದಾದರೂ ಟೂಲ್ಸ್ ಅನ್ನು ಕರೆಸಬೇಕಾದರೆ ಪರಿಶೀಲಿಸಲಾಗುತ್ತದೆ. ಹಾಗಿದ್ದರೆ, ಆ ಟೂಲ್ಸ್ ಅನ್ನು ಕರೆಸಿ LLM ಜೊತೆಗೆ ಸಂವಾದವನ್ನು ಮುಂದುವರೆಸುತ್ತೇವೆ ಮತ್ತು ಯಾವುದೇ ಹೆಚ್ಚಿನ ಟೂಲ್ ಕರೆಗಳು ಅವಶ್ಯಕತೆ ಇಲ್ಲದವರೆಗೆ ಮತ್ತು ನಮಗೆ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆ ದೊರಕುವವರೆಗೆ ಮುಂದುವರೆಸುತ್ತೇವೆ.

ನಾವು LLM ಗೆ ಬಹಳಷ್ಟು ಕರೆ ಮಾಡಲಿದ್ದೇವೆ, ಆದ್ದರಿಂದ LLM ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಒಂದು ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸೋಣ. ನಿಮ್ಮ `main.rs` ಫೈಲಿಗೆ ಕೆಳಗಿನ ಫಂಕ್ಷನ್ ಅನ್ನು ಸೇರಿಸಿ:

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

ಈ ಫಂಕ್ಷನ್ LLM ಕ್ಲೈಂಟ್, ಸಂದೇಶಗಳ ಪಟ್ಟಿ (ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಸೇರಿದಂತೆ), MCP ಸರ್ವರ್‌ನಿಂದ ಟೂಲ್ಸ್ ಅನ್ನು ಸ್ವೀಕರಿಸಿ, LLM ಗೆ ವಿನಂತಿ ಕಳುಹಿಸಿ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

LLM ನಿಂದ ಪ್ರತಿಕ್ರಿಯೆ `choices` ಎಂಬ ಅರೆ ಹೊಂದಿರುತ್ತದೆ. ನಾವು ಫಲಿತಾಂಶವನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಯಾವುದೇ `tool_calls` ಇದ್ದರೆ ನೋಡಬೇಕು. ಇದು LLM ಒಂದು ವಿಧಿ-ನಿರ್ದಿಷ್ಟ ಟೂಲನ್ನು ಆರ್ಗ್ಯುಮೆಂಟ್ಗಳೊಂದಿಗೆ ಕರೆಸಬೇಕೆಂದು ಕೇಳುತ್ತಿದೆ ಎಂದು ತಿಳಿಸುತ್ತದೆ. ನಿಮ್ಮ `main.rs` ಫೈಲಿನ ತಗ್ಗಿನಲ್ಲಿ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸುವ ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ:

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

    // ಟೂಲ್ ಕರೆಗಳನ್ನು ನಿಭಾಯಿಸಿ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ಸಹಾಯಕ ಸಂದೇಶ ಸೇರಿಸಿ

        // ಪ್ರತಿ ಟೂಲ್ ಕರೆ ಜಾರಿಗೆ ತರಬೇಕು
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ಸಂವಹನಗಳಿಗೆ ಟೂಲ್ ಫಲಿತಾಂಶ ಸೇರಿಸಿ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ಟೂಲ್ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸಿ
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

`tool_calls` ಇದ್ದರೆ, ಅದು ಟೂಲ್ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆದು, ಟೂಲ್ ವಿನಂತಿಯೊಂದಿಗೆ MCP ಸರ್ವರ್ ಅನ್ನು ಕರೆಸಿ, ನಂತರ ಫಲಿತಾಂಶಗಳನ್ನು ಸಂವಾದ ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸುತ್ತದೆ. ನಂತರ LLM ಜೊತೆಗೆ ಸಂವಾದ ಮುಂದುವರೆಸುತ್ತದೆ ಮತ್ತು ಸಂದೇಶಗಳನ್ನು ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಟೂಲ್ ಕಾಲ್ ಫಲಿತಾಂಶಗಳಿಂದ ನವೀಕರಿಸಲಾಗುತ್ತದೆ.

MCP ಕಾಲ್ಗಳಿಗಾಗಿ LLM ನೀಡುವ ಟೂಲ್ ಕಾಲ್ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆದುಕೊಳ್ಳಲು ಮತ್ತೊಂದು ಸಹಾಯಕ ಫಂಕ್ಷನ್ ಅನ್ನು ಸೇರಿಸುತ್ತೇವೆ. ನಿಮ್ಮ `main.rs` ಫೈಲಿನ ತಗ್ಗಿನಲ್ಲಿ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ:

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

ಎಲ್ಲಾ ಭಾಗಗಳೊಂದಿಗೆ, ನಾವು ಈಗ ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಿ LLM ಅನ್ನು ಕರೆ ಮಾಡಬಹುದು. ನಿಮ್ಮ `main` ಫಂಕ್ಷನ್ ಅನ್ನು ಕೆಳಗಿನ ಕೋಡ್‌ನೊಂದಿಗೆ ನವೀಕರಿಸಿ:

```rust
// ಸಾಧನ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂಭಾಷಣೆ
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

ಇದು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ನೊಂದಿಗೆ LLM ಅನ್ನು ವಿನಂತಿ ಮಾಡುತ್ತದೆ, ಎರಡು ಸಂಖ್ಯೆಗಳ ಮೊತ್ತಕ್ಕಾಗಿ ಕೇಳಿ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ ಡೈನಾಮಿಕ್ ಆಗಿ ಟೂಲ್ ಕಾಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

ಶುಭಕಾಮನೆಗಳು, ನೀವು ಅದನ್ನು ಸಾಧಿಸಿದ್ದೀರಿ!

## ನಿಯೋಜನೆ

ವ್ಯಾಯಾಮದ ಕೋಡ್ ಅನ್ನು ತೆಗೆದುಕೊಂಡು ಸರ್ವರ್‌ಗೆ ಇನ್ನಷ್ಟು ಟೂಲ್ಸ್ ಸೇರಿಸಿ ನಿರ್ಮಿಸಿ. ನಂತರ ವ್ಯಾಯಾಮದಲ್ಲಿರುವಂತೆ LLM ಒಳಗೊಂಡ ಕ್ಲೈಂಟ್ ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ವಿಭಿನ್ನ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಅದನ್ನು ಪರೀಕ್ಷಿಸಿ, ನಿಮ್ಮ ಎಲ್ಲಾ ಸರ್ವರ್ ಟೂಲ್ಸ್ ಡೈನಾಮಿಕ್ ಆಗಿ ಕರೆಸಲಾಗುತ್ತಾ ಎಂದು ಒಮ್ಮೆ ಖಚಿತಪಡಿಸಿ. ಈ ರೀತಿಯ ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಣದಿಂದ ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವ ದೊರೆಯುತ್ತದೆ ಏಕೆಂದರೆ ಅವರು ನಿಖರವಾದ ಕ್ಲೈಂಟ್ ಕಮ್ಯಾಂಡ್‌ಗಳ ಬದಲು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಬಹುದು ಮತ್ತು ಯಾವುದೇ MCP ಸರ್ವರ್ ಕರೆಗಳಿರುವುದನ್ನು ಗಮನದಲ್ಲಿಟ್ಟುಕೊಳ್ಳದೇ ಇರುತ್ತಾರೆ.

## ಪರಿಹಾರ

[ಪರಿಹಾರ](./solution/README.md)

## ಪ್ರಮುಖ ಅಂಶಗಳು

- ನಿಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದು ಬಳಕೆದಾರರಿಗೆ MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಉತ್ತಮ ಸಂವಹನವನ್ನು ನೀಡುತ್ತದೆ.
- MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ರೀತಿಗೆ ಪರಿವರ್ತಿಸಲು ನಿಮಗೆ ಬೇಕಾಗುತ್ತದೆ.

## ಉದಾಹರಣೆಗಳು

- [ಜಾವಾ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.ನೆಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [ಜಾವಾಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [పైಥಾನ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)
- [ರಸ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

## ಮುಂದಿನ ಹಂತ

- ಮುಂದಿನದು: [ವಿಜುಯಲ್ ಸ್ಟುಡಿಯೋ ಕೋಡ್ ಬಳಸಿ ಸರ್ವರ್ ಉಪಭೋಗಿಸುವುದು](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->