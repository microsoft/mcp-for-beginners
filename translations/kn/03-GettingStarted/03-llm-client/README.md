# LLM ಬಳಸಿ ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸುವುದು

ಇದುವರೆಗೂ, ನೀವು ಸರ್ವರ್ ಮತ್ತು ಕ್ಲೈಂಟ್ ಅನ್ನು ಹೇಗೆ ಸೃಷ್ಟಿಸುವುದನ್ನು ನೋಡಿದ್ದೀರಿ. ಕ್ಲೈಂಟ್ ಸ್ಪಷ್ಟವಾಗಿ ಸರ್ವರ್ ಅನ್ನು ಕರೆ ಮಾಡಿ, ಅದರ ಮೌಕುಲೆಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆದಿದೆ. ಆದರೆ, ಇದು ಬಹಳ ಪ್ರಾಯೋಗಿಕ ವಿಧಾನವಲ್ಲ. ನಿಮ್ಮ ಬಳಕೆದಾರರು ಏಜೆಂಟಿಕ್ ಯುಗದಲ್ಲಿ ಬದುಕುತ್ತಿದ್ದಾರೆ ಮತ್ತು ಪ್ರಾಂಪ್ಟ್‌ಗಳನ್ನು ಬಳಸಲು ಮತ್ತು LLM ಜೊತೆ ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಅವರು ನಿಮ್ಮ ಶಕ್ತಿಗಳನ್ನು ಸಂಗ್ರಹಿಸಲು MCP ಅನ್ನು ಬಳಸಿದೀರಾ ಎಂಬುದನ್ನು ಪರಿಗಣಿಸುವುದಿಲ್ಲ; ಅವರು ಸೌಹಾರ್ದಭಾಷೆಯ ಬಳಕೆಯಿಂದ ಸಂವಹನ ಮಾಡಲು ನಿರೀಕ್ಷಿಸುತ್ತಾರೆ. ಹಾಗಿದ್ದರೆ ನಾವು ಇದನ್ನು ಹೇಗೆ ಪರಿಹರಿಸೋಣ? ಪರಿಹಾರವೆಂದರೆ ಕ್ಲೈಂಟ್‌ಗೆ ಒಂದು LLM ಅನ್ನು ಸೇರಿಸುವುದು.

## ಅವಲೋಕನ

ಈ ಅಧ್ಯಾಯದಲ್ಲಿ ನಾವು ನಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಅನ್ನು ಸೇರಿಸುವದನ್ನು ಗಮನಿಸುತ್ತೇವೆ ಮತ್ತು ಇದು ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ನೀಡುವುದನ್ನು ತೋರಿಸುತ್ತೇವೆ.

## ಕಲಿಕಾ ಗುರಿಗಳು

ಈ ಅಧ್ಯಾಯದ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಇದನ್ನು ಮಾಡಲು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- LLM ಹೊಂದಿದ ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸುವುದು.
- MCP ಸರ್ವರ್‌ ಜೊತೆ LLM ಬಳಸಿ ಸುಗಮವಾಗಿ ಸಂವಹನ ಮಾಡುವುದು.
- ಕ್ಲೈಂಟ್ ಬದಿಯಲ್ಲಿಯೇ ಉತ್ತಮ ಅಂತಿಮ ಬಳಕೆದಾರ ಅನುಭವ ಒದಗಿಸುವುದು.

## ವಿಧಾನ

ನಾವು ತೆಗೆದುಕೊಳ್ಳಬೇಕಾದ ಕ್ರಮವನ್ನು ತಿಳಿದುಕೊಳ್ಳೋಣ. LLM ಸೇರಿಸುವುದು ಸರಳದೋ ಅಂತ ನೋಡೋಣ, ನಾವು ಸತ್ಯದಲ್ಲಿ ಇದನ್ನು ಮಾಡಬಲ್ಲೋಣವೇ?

ಇದಾಗಿರುತ್ತದೆ ಕ್ಲೈಂಟ್ ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನ ಮಾಡುವ ವಿಧಾನ:

1. ಸರ್ವರ್ ಜೊತೆ ಸಂಪರ್ಕ ಸ್ಥಾಪಿಸಿ.

1. ಶಕ್ತಿಗಳು, ಪ್ರಾಂಪ್ಟ್‌ಗಳು, ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ಮಾಡಿ ಮತ್ತು ಅವುಗಳ ಸ್ಕೀಮಾವನ್ನು ಉಳಿಸಿ.

1. LLM ಸೇರಿಸಿ ಮತ್ತು ಉಳಿಸಿದ ಶಕ್ತಿಗಳು ಮತ್ತು ಅವುಗಳ ಸ್ಕೀಮಾವನ್ನು LLM ಗೆ ಅರ್ಥವಾಗುವ ರೂಪದಲ್ಲಿ ಪಾಸ್ ಮಾಡಿ.

1. ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು LLM ಗೆ ಪಾಸ್ ಮಾಡಿ, ಕ್ಲೈಂಟ್ ನೀಡಿದ ಉಪಕರಣಗಳೊಡನೆ.

ಚೆನ್ನಾಗಿದೆ, ಈಗ մենք ಏನು ಮಾಡುವುದನ್ನು ಮೇಲ್ಮಟ್ಟದಲ್ಲಿ ಅರ್ಥಮಾಡಿಕೊಂಡೆವು, ಕೆಳಗಿನ ವ್ಯಾಯಾಮದಲ್ಲಿ ಈ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಪ್ರಯತ್ನಿಸೋಣ.

## ವ್ಯಾಯಾಮ: LLM ಹೊಂದಿದ ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸುವುದು

ಈ ವ್ಯಾಯಾಮದಲ್ಲಿ ನಾವು ನಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಅನ್ನು ಸೇರಿಸುವುದನ್ನು ಕಲಿಯೋಣ.

### GitHub ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕೆನ್ನೊಂದಿಗೆ ದೃಢೀಕರಣ

GitHub ಟೋಕನನ್ನು ಸೃಷ್ಟಿಸುವುದು ಸರಳ ಪ್ರಕ್ರಿಯೆಯಾಗಿದೆ. ನೀವು ಹೀಗೆ ಮಾಡಬಹುದು:

- GitHub ಸೆಟ್ಟಿಂಗ್ಗೆ ಹೋಗಿ – ಮೇಲ್ವಾಯ್ದ ಕೊನೆಯಲ್ಲಿ ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್ಸ್ ಆಯ್ಕೆಮಾಡಿ.
- ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಗೆ ಹೋಗಿ – ಕೆಳಗೆ ಸ್ಕ್ರೋಲ್ ಮಾಡಿ ಮತ್ತು ಡೆವಲಪರ್ ಸೆಟ್ಟಿಂಗ್ಸ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
- ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ಗಳನ್ನು ಆಯ್ಕೆಮಾಡಿ – ಫೈನ್- ಗ್ರೇನ್ಡ್ ಟೋಕನ್ಗಳನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಹೊಸ ಟೋಕನ್ ರಚಿಸಿ.
- ನಿಮ್ಮ ಟೋಕನನ್ನು ಸಂರಚಿಸಿ – ಉಲ್ಲೇಖಕ್ಕಾಗಿ ಟಿಪ್ಪಣಿ ಸೇರಿಸಿ, ಅವಧಿ ನಿಗದಿ ಮಾಡಿ ಮತ್ತು ಅಗತ್ಯ ಸ್ಕೋಪ್‌ಗಳನ್ನು (ಅನುಮತಿಗಳನ್ನು) ಆರಿಸಿ. ಈ ಸಂದರ್ಭದಲ್ಲಿ Models ಅನುಮತಿಯನ್ನು ಸೇರಿಸಬೇಕಾಗಿದೆ.
- ಟೋಕನನ್ನು ರಚಿಸಿ ಮತ್ತು ನಕಲಿಸಿ – ಟೋಕನ್ ರಚಿಸಿ ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಮತ್ತು ಅದನ್ನು ತಕ್ಷಣ ನಕಲಿಸಿ, ಏಕೆಂದರೆ ಅದನ್ನು ಮತ್ತೆ ನೋಡಲು ಸಾಧ್ಯವಿಲ್ಲ.

### -1- ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕ

ಮೊದಲು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸೋಣ:

#### ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ವಾಲಿಡೇಷನ್ ಪರಿಸರ ಸ್ವೀಕಾರಕ್ಕೆ zod ಅನ್ನು ಆಮದುಮಾಡಿ

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಅಗತ್ಯ ಪುಸ್ತಕಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- `client` ಮತ್ತು `openai` ಎಂಬ ಎರಡು ಸದಸ್ಯರೊಂದಿಗೆ ಕ್ಲಾಸ್ ಸೃಷ್ಟಿಸಿ, ಇದು ನಮ್ಮ ಕ್ಲೈಂಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಲು ಮತ್ತು LLM ಜೊತೆಗೆ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯಮಾಡುತ್ತದೆ.
- GitHub Models ಬಳಸಲು baseUrl ಅನ್ನು ಇನ್ಫರೆನ್ಸ್ API ಗೆ ಸೆಟ್ ಮಾಡುವ ಮೂಲಕ ನಮ್ಮ LLM ಇನ್‌ಸ್ಟೇನ್ಸ್ ಅನ್ನು ಸಂರಚಿಸಿದ್ದೇವೆ.

#### ಪೈಥಾನ್

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ಸಂಪರ್ಕಕ್ಕಾಗಿ ಸರ್ವರ್ ಪರಿಮಿತಿಗಳನ್ನು ರಚಿಸಿ
server_params = StdioServerParameters(
    command="mcp",  # ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಫೈಲ್
    args=["run", "server.py"],  # ಐಚ್ಛಿಕ ಕಮಾಂಡ್ ಲೈನ್ argument ಗಳು
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

- MCP ಗಾಗಿ ಅಗತ್ಯ ಪುಸ್ತಕಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ
- ಕ್ಲೈಂಟ್ ಅನ್ನು ಸೃಷ್ಟಿಸಿದ್ದೇವೆ

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

#### ಜава

ಮೊದಲಿಗೆ, ನಿಮ್ಮ `pom.xml` ಫೈಲ್‌ಗೆ LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸುವುದು ಅಗತ್ಯ. MCP ಸಂಯೋಜನೆ ಮತ್ತು OpenAI ಹೊಂದಿಕೆಯಾಗುವ MiniMax API ಗಳನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಲು ಈ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ:

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

ನಿಮ್ಮ MiniMax API ಕೀ ಮತ್ತು ಆಯ್ಕೆಮಾಡಬಹುದಾದ ಆದ್ರೆ ಆವಶ್ಯಕ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಮಾದರಿಯನ್ನು ಸೆಟ್ ಮಾಡಿಕೊಳ್ಳಿ.
`MINIMAX_MODEL_ID` `MiniMax-M3` ಮತ್ತು `MiniMax-M2.7` ನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. 
`OPENAI_BASE_URL` ಸೇರ್ಪಡೆ ಇಲ್ಲದಿದ್ದರೆ, `MINIMAX_REGION` `global_en` ಮತ್ತು `cn_zh` ನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ಪ್ರದೇಶದಿಂದ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಆಯ್ಕೆಯನ್ನು ಮಾಡಲು, `OPENAI_BASE_URL` ಅನ್ನು ತೆಗೆದುಹಾಕಿ:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ನಂತರ ನಿಮ್ಮ ಜಾವಾ ಕ್ಲೈಂಟ್ ಕ್ಲಾಸ್ ಅನ್ನು ಸೃಷ್ಟಿಸಿ:

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

        // MCP ಕ್ಲಯಿಂಟ್ ರಚಿಸಿ
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

- **LangChain4j ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿದ್ದೇವೆ**: MCP ಸಂಯೋಜನೆ ಮತ್ತು OpenAI ಹೊಂದಿಕೆಯಾಗುವ MiniMax API ಗಾಗಿ
- **LangChain4j ಪುಸ್ತಕಾಲಯಗಳನ್ನು ಆಮದು ಮಾಡಿದ್ದೇವೆ**: MCP ಸಂಯೋಜನೆ ಮತ್ತು OpenAI ಚಾಟ್ ಮಾದರಿ ಕಾರ್ಯಕ್ಷಮತೆಗೆ
- **`ChatLanguageModel` ಸೃಷ್ಟಿಸಿದೆವು**: ನಿಮ್ಮ MiniMax API ಕೀ, ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಬೆಂಬಲಿತ ಮಾದರಿ ಐಡಿ ಹೊಂದಿಸಿ MiniMax ಬಳಸಲು ಸಂರಚಿಸಲಾಗಿದೆ
- **HTTP ಸಾರಿಗೆ ನಿಗದಿ ಮಾಡಿದೆವು**: MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು Server-Sent Events (SSE) ಉಪಯೋಗಿಸಲಾಗಿದೆ
- **MCP ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸಿದೆವು**: ಇದು ಸರ್ವರ್ ಜೊತೆ ಸಂವಹನ ನಿರ್ವಹಿಸುತ್ತದೆ
- **LangChain4j ನ್ನು ಒಳಗೊಂಡ MCP ಬೆಂಬಲ ಬಳಸದನ್ನು ಉಪಯೋಗಿಸಿದೆವು**: ಇದು LLM ಮತ್ತು MCP ಸರ್ವರ್‌ಗಳ ನಡುವಿನ ಸಂಯೋಜನೆಯನ್ನು ಸರ್ಪಣ ಮಾಡುತ್ತದೆ

#### ರಸ್ಟ್

ಈ ಉದಾಹರಣೆ ನಿಮ್ಮ ಬಳಿ ರಸ್ಟ್ ಆಧಾರಿತ MCP ಸರ್ವರ್ ಇದ್ದದ್ದು ಅನಿಸಿದ್ದು. ಇಲ್ಲದಿದ್ದರೆ, [01-first-server](../01-first-server/README.md) ಅಧ್ಯಾಯವನ್ನು ಮತ್ತೆ ನೋಡಿ ಸರ್ವರ್ ಸೃಷ್ಟಿಸಿ.

ನಿಮ್ಮ ರಸ್ಟ್ MCP ಸರ್ವರ್ ಸಿದ್ಧವಾಗಿದ್ದ ಮೇಲೆ, ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಸರ್ವರ್ ಇದ್ದ ಫೋಲ್ಡರ್‌ಗೆ ಹೋಗಿ. ನಂತರ ಹೊಸ LLM ಕ್ಲೈಂಟ್ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ನಿರ್ವಹಿಸಿ:

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
> ಅಧಿಕೃತವಾಗಿ OpenAI ಗಾಗಿ ರಸ್ಟ್ ಪುಸ್ತಕಾಲಯ ಇಲ್ಲ, ಆದರೆ `async-openai` ಕ್ರೇಟ್ ಒಂದು [ಸಮುದಾಯ ನಿರ್ವಹಿಸಲಾದ ಪುಸ್ತಕಾಲಯ](https://platform.openai.com/docs/libraries/rust#rust) ಆಗಿದ್ದು ಸಾಮಾನ್ಯವಾಗಿ ಉಪಯೋಗದಲ್ಲಿದೆ.

`src/main.rs` ಫೈಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಅದರ ಒಳಗಿನ ವಿಷಯವನ್ನು ಕೆಳಗಿನ ಕೋಡ್ಗೆ ಬದಲಿಸಿ:

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
    // ಪ್ರಾಥಮಿಕ შეტೆ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ಕ್ಲೈಂಟ್ ಸೆಟ್ ಅಪ್ ಮಾಡಿ
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

    // ಮಾಡಬೇಕಿದೆ: MCP ಸಾಧನ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯಿರಿ

    // ಮಾಡಬೇಕಿದೆ: ಉಪಕರಣ ಕರೆಗಳೊಂದಿಗೆ LLM ಸಂಭಾಷಣೆ

    Ok(())
}
```

ಈ ಕೋಡ್ ಮೂಲಭೂತ ರಸ್ಟ್ ಅಪ್ಲಿಕೇಶನ್ ಸಿದ್ಧಪಡಿಸುತ್ತದೆ, ಇದು MCP ಸರ್ವರ್ ಮತ್ತು GitHub Models ಒದಗಿಸುವ LLM ಸಂವಹನಕ್ಕೆ ಸಂಪರ್ಕಿಸುತ್ತದೆ.

> [!IMPORTANT]
> ಅಪ್ಲಿಕೇಶನ್ ನಡೆಯುವ ಮೊದಲು ನಿಮ್ಮ GitHub ಟೋಕನ್ ಜೊತೆ `OPENAI_API_KEY` ಪರಿಸರ ವ್ಯತ್ಯಯವನ್ನು ತಯಾರು ಮಾಡಿ.

ಚೆನ್ನಾಗಿದೆ, ಮುಂದಿನ ಹಂತಕ್ಕೆ ನಾವು ಸರ್ವರ್‌ನಲ್ಲಿ ಶಕ್ತಿಗಳ ಪಟ್ಟಿಯನ್ನು ತೋರಿಸುವುದನ್ನು ಮಾಡೋಣ.

### -2- ಸರ್ವರ್ ಶಕ್ತಿಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು

ಈಗ ನಾವು ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕ ಸಾಧಿಸಿ ಅದರ ಶಕ್ತಿಗಳನ್ನು ಕೇಳೋಣ:

#### ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್

ಅದೇ ಕ್ಲಾಸಿನಲ್ಲಿ ಕೆಳಗಿನ ವಿಧಾನಗಳನ್ನು ಸೇರಿಸಿ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ಸಾಧನಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತಿದೆ
    const toolsResult = await this.client.listTools();
}
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರ್ವರ್ ಗೆ ಸಂಪರ್ಕ ಮಾಡುವ ಕೋಡ್ `connectToServer` ಸೇರಿಸಿದ್ದೇವೆ.
- ನಮ್ಮ ಆಪ್ಲಿಕೇಶನ್ ಫ್ಲೋ ನಿರ್ವಹಿಸುವ `run` ವಿಧಾನವನ್ನು ಸೃಷ್ಟಿಸಿದ್ದೇವೆ. ಇದುವರೆಗೂ ಅದು ಉಪಕರಣಗಳ ಪಟ್ಟಿ ಮಾತ್ರ ಮಾಡುತ್ತದೆ, ಆದರೆ ನಾವು ಹೆಚ್ಚು ಸೇರಿಸುವೆವು.

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
    print("Tool", tool.inputSchema["properties"])
```

ಸೇರಿಸಿದ್ದದೆಂಬುದು:

- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ಮಾಡಿ ಅವುಗಳನ್ನು ಮುದ್ರಿಸಿದ್ದೇವೆ. ಉಪಕರಣಗಳಿಗೆ ಸಹ `inputSchema` ಪಟ್ಟಿಮಾಡಿದ್ದೇವೆ, ಇದು ನಂತರ ಉಪಯೋಗಿಸಲಾಗುತ್ತದೆ.

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ಮಾಡಿದ್ದೇವೆ
- ಪ್ರತಿಯೊಂದು ಉಪಕರಣಕ್ಕೆ, ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಸ್ಕೀಮಾವನ್ನು ಪಟ್ಟಿಮಾಡಿದ್ದೇವೆ. ಇದು ನಂತರ ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡಲು ಉಪಯೋಗವಾಗುತ್ತದೆ.

#### ಜава

```java
// ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವ ಉಪಕರಣ ಪೂರೈಕೆದಾರರನ್ನು ಸೃಷ್ಟಿಸಿರಿ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ಉಪಕರಣ ಪೂರೈಕೆದಾರನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
// - MCP ಸರ್ವರಿನಿಂದ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುವುದು
// - MCP ಉಪಕರಣchemasಗಳನ್ನು LangChain4j ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸುವುದು
// - ಉಪಕರಣ ಕಾರ್ಯಾಚರಣೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- MCP ಸರ್ವರ್‌ನಿಂದ ಎಲ್ಲಾ ಉಪಕರಣಗಳನ್ನು ತಪಾಸಣೆ ಮಾಡಿ ನೋಂದಾಯಿಸುವ `McpToolProvider` ಅನ್ನು ಸೃಷ್ಟಿಸಿದ್ದೇವೆ
- ಉಪಕರಣದ ಪೂರೈಕೆದಾರವು MCP ಉಪಕರಣ ಸ್ಕೀಮಾ ಮತ್ತು LangChain4j ಉಪಕರಣಾ ರೂಪಗಳನ್ನು ಒಳಗ್ತೊಳ್ನುಮಾಡುವ ಪರಿವರ್ತನೆ ನಿರ್ವಹಿಸುತ್ತದೆ
- ಈ ವಿಧಾನವು ಕೈಯಾರೆ ಉಪಕರಣ ಪಟ್ಟಿಮಾಡುವ ಮತ್ತು ಪರಿವರ್ತಿಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಒಡನ್ನಾಗಿ ಮಾಡುತ್ತದೆ

#### ರಸ್ಟ್

MCP ಸರ್ವರ್‌ನಿಂದ ಉಪಕರಣಗಳನ್ನು ಪಡೆಯುವುದು `list_tools` ವಿಧಾನ ಬಳಸಿ ಮಾಡಲಾಗಿದೆ. ನಿಮ್ಮ `main` ಫಂಕ್ಷನ್ ನಂತರ MCP ಕ್ಲೈಂಟ್ ಸಿದ್ಧಪಡಿಸಿ ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ:

```rust
// MCP ಸಾಧನ ಪಟ್ಟಿ ಪಡೆಯಿರಿ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ಸರ್ವರ್ ಶಕ್ತಿಗಳನ್ನು LLM ಉಪಕರಣಗಳಲ್ಲಿ ಪರಿವರ್ತಿಸೋಣ

ಸರ್ವರ್ ಶಕ್ತಿಗಳನ್ನು ಪಟ್ಟಿಮಾಡಿ ನಂತರ, ಅವುಗಳನ್ನು LLM ಗೆ ಅರ್ಥವಾಗುವ ರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಬೇಕು. ನಾವು ಇವುಗಳನ್ನು LLM ಗೆ ಉಪಕರಣಗಳಾಗಿ ಒದಗಿಸಬಹುದು.

#### ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್

1. ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಉಪಕರಣಾ ರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಲು:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ಇನ್‌ಪುಟ್_ಸ್ಕೀಮಾದ ಆಧಾರವಾಗಿ ಜೋಡ್ ಸ್ಕೀಮಾ ರಚಿಸಿ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರಕಾರವನ್ನು "ಕಾರ್ಯ" ಎಂದು 설정 ಮಾಡಿ
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

    ಮೇಲ್ಪಟ್ಟ ಕೋಡ್ MCP ಸರ್ವರ್‌ನಿಂದ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು LLM ಗೆ ಅರ್ಥವಾಗುವ ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನ ರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

2. `run` ವಿಧಾನವನ್ನು ಮುಂದಿನಂತೆಯೇ ಅಪ್‌ಡೇಟ್ ಮಾಡೋಣ, ಸರ್ವರ್ ಶಕ್ತಿಗಳನ್ನು ಸೂಚಿಸಲು:

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, `run` ವಿಧಾನವನ್ನು ಫಲಿತಾಂಶದ ಮೂಲಕ ಹೋಗುವಂತೆ ಮತ್ತು ಪ್ರತಿಯೊಂದು ಪ್ರವೇಶಕ್ಕೆ `openAiToolAdapter` ಕರೆಗೆ ಕರೆಮಾಡಲು ನವೀಕರಿಸಿದ್ದೇವೆ.

#### ಪೈಥಾನ್

1. ಮೊದಲು, ಕೆಳಗಿನ ಪರಿವರ್ತಕ ಫಂಕ್ಷನ್ ಸೃಷ್ಟಿಸೋಣ:

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

    ಮೇಲಿನ `convert_to_llm_tools` ಫಂಕ್ಷನ್ MCP ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು LLM ಗೆ ಅರ್ಥವಾಗುವ ರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸುತ್ತದೆ.

2. ನಂತರ ನಮ್ಮ ಕ್ಲೈಂಟ್ ಕೋಡಿನಲ್ಲಿ ಈ ಫಂಕ್ಷನ್ ಬಳಸಲು ಕೆಳಗಿನಂತೆಯೇ ನವೀಕರಿಸೋಣ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ಇಲ್ಲಿ, ನಾವು MCP ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ನೀಡಲು ಪರಿವರ್ತಿಸಲು `convert_to_llm_tool` ಕರೆಯನ್ನು ಸೇರಿಸಿದ್ದೇವೆ.

#### .NET

1. MCP ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಪರಿವರ್ತನೆ ಮಾಡಲು ಕೋಡ್ ಸೇರಿಸೋಣ:

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

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- `ConvertFrom` ಎಂಬ ಫಂಕ್ಷನ್ ಸೃಷ್ಟಿಸಿದ್ದೇವೆ, ಇದು ಹೆಸರು, ವಿವರಣೆ ಮತ್ತು ಇನ್‌ಪುಟ್ ಸ್ಕೀಮಾವನ್ನು ಪಡೆದು ಕಾರ್ಯಾಚರಣೆ ಮಾಡುತ್ತದೆ.
- ಇದು `FunctionDefinition` ಸೃಷ್ಟಿಸುವ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ಅದನ್ನು `ChatCompletionsDefinition` ಗೆ ಪಾಸ್ ಮಾಡುತ್ತದೆ. ಇವು LLM ಗೆ ಅರ್ಥವಾಗುವ ಸಾಮಗ್ರಿ.

2. ಈ ಮೇಲಿನ ಫಂಕ್ಷನ್ ಉಪಯೋಗಿಸುವಂತೆ ಕೆಲವು ಇರುವ ಕೋಡ್ಗೆ ಬದಲಾವಣೆ ಮಾಡೋಣ:

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

#### ಜава

```java
// ಸ್ವಭಾವಿಕ ಭಾಷೆ ಸಂವಹನಕ್ಕಾಗಿ ಬಾಟ್ ಇಂಟರ್ಫೇಸ್ ರಚಿಸಿ
public interface Bot {
    String chat(String prompt);
}

// LLM ಮತ್ತು MCP ಸಾಧನಗಳೊಂದಿಗೆ AI ಸೇವೆಯನ್ನು ಸಂರಚಿಸಿ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

- ಸರಳ `Bot` ಇಂಟರ್ಫೇಸ್ ಸ್ವಭಾವ ಭಾಷೆಯ ಸಂವಾದಗಳಿಗಾಗಿ ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ
- LangChain4j ನಿಂದ `AiServices` ಬಳಸಿ LLM ಅನ್ನು MCP ಉಪಕರಣ ಪೂರೈಕೆದಾರನೊಂದಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಹೊಂದಿಸಿದ್ದೇವೆ
- ಫ್ರೆ임್‌ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಉಪಕರಣ ಸ್ಕೀಮಾ ಪರಿವರ್ತನೆ ಮತ್ತು ಫಂಕ್ಷನ್ ಕರೆಗಳನ್ನು ಹಿಂಡುತ್ತದೆ
- ಈ ವಿಧಾನವು ಕೈಯಾರೆ ಉಪಕರಣ ಪರಿವರ್ತನೆಯನ್ನು ತಡೆಯುತ್ತದೆ - LangChain4j MCP ಉಪಕರಣಗಳನ್ನು LLM ಹೊಂದಿಕೆಯಾಗುವ ರೂಪಕ್ಕೆ ಪರಿವರ್ತನೆ ಮಾಡುವ ಜಟಿಲತೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ

#### ರಸ್ಟ್

MCP ಉಪಕರಣ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ರೂಮಕ್ಕೆ ಪರಿವರ್ತಿಸಲು, ನಾವು ಉಪಕರಣಗಳ ಪಟ್ಟಿಯನ್ನು ರೂಪಿಸುವ ಸಹಾಯಕರ ಫಂಕ್ಷನ್ ಸೇರಿಸುವೆವು. ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ನಲ್ಲಿ `main` ಫಂಕ್ಷನ್ ಕೆಳಗೆ ಈ ಕೋಡ್ ಸೇರಿಸಿ. ಇದು LLM ಗೆ ವಿನಂತಿ ಮಾಡುವಾಗ ಕರೆಯಲ್ಪಡುವುದು:

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

ಚೆನ್ನಾಗಿದೆ, ಬಳಕೆದಾರರ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸಲು ನಾವು ಸಿದ್ಧರಾಗಿದ್ದೇವೆ, ಅದನ್ನು ಮುಂದಿನ ಹಂತವಾಗಿ ಮಾಡೋಣ.

### -4- ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ನಿರ್ವಹಿಸುವುದು

ಈ ಭಾಗದಲ್ಲಿ ನಾವು ಬಳಕೆದಾರರ ವಿನಂತಿಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತೇವೆ.

#### ಟೈಪ್ಸ್ಕ್ರಿಪ್ಟ್

1. ನಮ್ಮ LLM ಅನ್ನು ಕರೆ ಮಾಡಲು ಉಪಯೋಗಿಸುವ ವಿಧಾನ ಸೇರಿಸೋಣ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ಸರ್ವರ್‌ನ ಸಾಧನವನ್ನು ಕರೆ ಮಾಡು
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡು
        // ಅನಗತ್ಯ ಕೆಲಸ

        }
    }
    ```

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ನಾವು:

    - `callTools` ಎಂಬ ವಿಧಾನ ಸೇರಿಸಿದ್ದೇವೆ.
    - ಈ ವಿಧಾನ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ತೆಗೆದು ಯಾವ ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡಲಾಗಿದೆ ಎಂದು ತರುವುದು.

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ಸಾಧನವನ್ನು ಕರೆಮಾಡಿ
        }
        ```

    - LLM ಕರೆಯಬೇಕು ಎಂದರೆ ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡುತ್ತದೆ.

        ```typescript
        // 2. ಸರ್ವರ್‌ನ ಉಪಕರಣವನ್ನು ಕರೆಮಾಡಿ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
        // ಮಾಡಲು ಬಾಕಿ
        ```

2. `run` ವಿಧಾನವನ್ನು LLM ಕರೆಯುವುದಕ್ಕೆ ಮತ್ತು `callTools` ಅನ್ನು ಕರೆ ಮಾಡಲು ನವೀಕರಿಸೋಣ:

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

    // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪರಿಶೀಲಿಸಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ ಟೂಲ್ ಕಾಲ್‌ಗಳಿದ್ದವೆಯೇ ಎಂದು ಕಾಣಿಕೊಳ್ಳಿ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ಚೆನ್ನಾಗಿದೆ, ಪೂರ್ಣ ಕೋಡ್ ಇದಿದೆ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ಸ್ಕೀಮಾ ಮಾನ್ಯತೆಗಾಗಿ zod ಆಮದುಮಾಡಿ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ಭವಿಷ್ಯದಲ್ಲಿ ಈ URL ಗೆ ಬದಲಾಯಿಸುವ ಅಗತ್ಯವಿರುವಂತೆ ಕಾಣಬಹುದು: https://models.github.ai/inference
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
          // ಇನ್‌ಪುಟ್_ಸ್ಕೀಮಾದ ಆಧಾರದ ಮೇಲೆ zod ಸ್ಕೀಮಾ ರಚಿಸಿ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ವಿಧವನ್ನು ಸ್ಪಷ್ಟವಾಗಿ "function" ಗೆ ಸೆಟ್ ಮಾಡಿ
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
    
    
          // 2. ಸರ್ವರ್‌ನ ಯಂತ್ರವನ್ನು ಕರೆಯಿರಿ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ಫಲಿತಾಂಶದೊಂದಿಗೆ ಏನಾದರೂ ಮಾಡಿ
          // ಮಾಡಬೇಕಾಗಿದೆ
    
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
    
        // 3. LLM ಪ್ರತಿಕ್ರಿಯೆಯ ಮೂಲಕ ಹೋಗಿ, ಪ್ರತಿ ಆಯ್ಕೆಗೆ, ಅದು ಯಾವ ಯಂತ್ರ ಕರೆಗಳನ್ನು ಹೊಂದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
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

1. LLM ಕರೆಯಲು ಅಗತ್ಯವಿರುವ ಕೆಲವು ಆಮದುಗಳನ್ನು ಸೇರಿಸೋಣ

    ```python
    # ಎಲ್‌ಎಲ್‌ಎಂ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. ನಂತರ, LLM_CALL ಮಾಡುವ ಫಂಕ್ಷನ್ ಸೇರಿಸೋಣ:

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
            # ಐಚ್ಛಿಕ ಪರಿಮಿತಿಗಳು
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

    - MCP ಸರ್ವರ್ ನಲ್ಲಿ ಕಂಡುಹಿಡಿದ ಫಂಕ್ಷನ್‌ಗಳನ್ನು LLM ಗೆ ಪಾಸ್ ಮಾಡಿದ್ದೇವೆ.
    - ನಂತರ ನೀವೇಳಿಸಿಕೊಂಡವನು LLM ಅನ್ನು ಫಂಕ್ಷನ್‌ಗಳೊಂದಿಗೆ ಕರೆಮಾಡಿಲ್ಲ.
    - ನಂತರ ಫಲಿತಾಂಶವನ್ನು ಪರಿಶೀಲಿಸಿ ಯಾವ ಫಂಕ್ಷನ್‌ಗಳನ್ನು ಕರೆ ಮಾಡಬೇಕು ಎಂಬುದನ್ನು ನೋಡುತ್ತೇವೆ.
    - ಕೊನೆಗೆ ನಾವು ಕರೆ ಮಾಡಬೇಕಾದ ಫಂಕ್ಷನ್ ಗಳ ಪಟ್ಟಿಯನ್ನು ಪಾಸ್ ಮಾಡುತ್ತೇವೆ.

3. ಕೊನೆಯ ಹಂತ, ನಮ್ಮ ಮುಖ್ಯ ಕೋಡನ್ನು ನವೀಕರಿಸೋಣ:

    ```python
    prompt = "Add 2 to 20"

    # ಎಲ್ಲಿಗೆ ಬೇಕಾದರೂ ಮಾನವ ಭಾಷೆ ಮಾದರಿಯನ್ನು ಯಾವ ಸಾಧನಗಳಿವೆ ಎಂದು ಕೇಳಿ, ಇದ್ದರೆ
    functions_to_call = call_llm(prompt, functions)

    # ಸುಪಾರಿಗೆ ಸೂಚಿಸಿದ ಕಾರ್ಯಗಳನ್ನು ಕರೆಮಾಡಿ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ಇದು ಕೊನೆಯ ಹಂತ, ಮೇಲ್ಪಟ್ಟ ಕೋಡಿನಲ್ಲಿ ನಾವು:

    - ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಆಧಾರದಲ್ಲಿ LLM ಪಟ್ಟಿತ ಯೋಗ್ಯತೆಯಿಂದ MCP ಉಪಕರಣದ ಒಬ್ಬರನ್ನು ಸಂಪರ್ಕಿಸುತ್ತಿದ್ದೇವೆ.
    - ಮುಂದಿನ MCP ಸರ್ವರ್ಗೆ ಉಪಕರಣದ ಕರೆಯ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುತ್ತಿದ್ದೇವೆ.

#### .NET

1. LLM ಪ್ರಾಂಪ್ಟ್ ವಿನಂತಿಯನ್ನು ಮಾಡಲು ಕೆಲವು ಕೋಡ್ ತೋರಿಸೋಣ:

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

    - MCP ಸರ್ವರ್‌ನಿಂದ ಉಪಕರಣಗಳನ್ನು ಪಡೆದಿದ್ದೇವೆ, `var tools = await GetMcpTools()`.
    - ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿದ್ದೇವೆ `userMessage`.
    - ಮಾದರಿ ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ವಿವರಿಸುವ ಆಯ್ಕೆಗಳ ಆಬ್ಜೆಕ್ಟ್ ರಚಿಸಿದ್ದೇವೆ.
    - LLM ಗೆ ವಿನಂತಿ ಕಳುಹಿಸಿದ್ದೇವೆ.

2. ಕೊನೆಯ ಹಂತ, LLM ಯಾವುದಾದರೂ ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡಬೇಕಾ ನೋಡೋಣ:

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

    - ಫಂಕ್ಷನ್ ಕರೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ ಲೂಪ್ ಮಾಡುತ್ತೇವೆ.
    - ಪ್ರತಿಯೊಂದು ಉಪಕರಣ ಕರೆಯಲು ಹೆಸರು ಮತ್ತು ಆರ್ಗುಮೆಂಟ್‌ಗಳನ್ನು ಪಾರ್ಸ್ ಮಾಡಿ MCP ಸರ್ವರ್ ಮೂಲಕ ಕರೆ ಮಾಡುತ್ತೇವೆ. ಕೊನೆಗೆ ಫಲಿತಾಂಶವನ್ನು ಮುದ್ರಿಸುತ್ತೇವೆ.

ಪೂರ್ಣ ಕೋಡ್ ಇದಾಗಿದೆ:

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
    // ಸ್ವಯಂಚಾಲಿತವಾಗಿ MCP ಉಪಕರಣಗಳನ್ನು ಬಳಸುವ ಸ್ವಭಾವಿಕ ಭಾಷೆ ವಿನಂತಿಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಿ
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

- MCP ಸರ್ವರ್ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸರಳ ಸ್ವಭಾವ ಭಾಷಾ ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಸಂವಾದ ನಡೆಸಿದ್ದೇವೆ
- LangChain4j ಫ್ರೆ임್‌ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ:
  - ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಅಗತ್ಯವಿದ್ದಾಗ ಉಪಕರಣ ಕರೆಗಳಿಗೆ ಪರಿವರ್ತಿಸುವುದನ್ನು
  - LLM ನಿರ್ಧಾರ ಆಧಾರಿತವಾಗಿ ಸೂಕ್ತ MCP ಉಪಕರಣಗಳನ್ನು ಕರೆ ಮಾಡುವುದನ್ನು
  - LLM ಮತ್ತು MCP ಸರ್ವರ್ ನಡುವಿನ ಸಂವಾದದ ಪ್ರವರ್ತನೆಯನ್ನು ನಿರ್ವಹಿಸುವುದನ್ನು
- `bot.chat()` ವಿಧಾನ ಸ್ವಭಾವ ಭಾಷೆಯ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನೆಲ್ಲಾ ನೀಡುತ್ತದೆ, ಇವು MCP ಉಪಕರಣಗಳ ಫಲಿತಾಂಶ ಹೊಂದಿರಬಹುದು
- ಈ ವಿಧಾನದಿಂದ ಬಳಕೆದಾರನು MCP ಅಡಿಯಲ್ಲಿ ನಡೆಯುವ ಸಂವಿಧಾನವನ್ನು ತಿಳಿಯುವ ಅಗತ್ಯವಿಲ್ಲದೆ ಸಡಿಲ ಅನುಭವ ಪಡೆಯುತ್ತಾರೆ

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

#### ರಸ್ಟ್

ಇಲ್ಲಿ ಹೆಚ್ಚು ಭಾಗ ಕೆಲಸ ನಡೆದಾಗುತ್ತದೆ. ನಾವು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರರ ಪ್ರಾಂಪ್ಟ್ ಜೊತೆ LLM ಕರೆಮಾಡುತ್ತೇವೆ, ನಂತರ ಫಲಿತಾಂಶದಲ್ಲಿ ಯಾವ ಉಪಕರಣಗಳನ್ನ ಕರೆಯಬೇಕೋ ನೋಡುತ್ತೇವೆ. ಹಾಗಿದ್ದರೆ, ಅವುಗಳನ್ನು ಕರೆಮಾಡುತ್ತೇವೆ ಮತ್ತು LLM ಜೊತೆ ಸಂವಾದ ಮುಂದುವರಿಸುತ್ತೇವೆ, ಇನ್ನಷ್ಟು ಉಪಕರಣ ಕರೆ ಬೇಕಾಗದವರೆಗೆ ಮತ್ತು ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯುವವರೆಗೆ.


ನಾವು LLM ಗೆ ಬಹುಮಾನ ಕರೆಗಳನ್ನು ಮಾಡಲಿದ್ದೇವೆ, ಆದ್ದರಿಂದ LLM ಕರೆ ನಿರ್ವಹಿಸುವ ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸೋಣ. ಕೆಳಗಿನ ಫಂಕ್ಷನ್ ಅನ್ನು ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ:

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

ಈ ಫಂಕ್ಷನ್ LLM ಕ್ಲೈಂಟ್, ಸಂದೇಶಗಳ ಪಟ್ಟಿ (ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಸೇರಿದಂತೆ), MCP ಸರ್ವರ್‌ನ ಸಲಕರಣೆಗಳನ್ನು ತೆಗೆದು LLM ಗೆ ವಿನಂತಿ ಕಳುಹಿಸಿ, ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮರಳಿಸುತ್ತದೆ.

LLM ನಿಂದ ಪ್ರತ್ಯುತ್ತರವು `choices` ಎಂಬ ಅರೆ ಬಗ್ಗೆ ಹೊಂದಿರುತ್ತದೆ. ನಾವು ಫಲಿತಾಂಶವನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬೇಕಾಗುತ್ತದೆ ಯಾವ `tool_calls` ಅಸ್ತಿತ್ವದಲ್ಲಿರುತ್ತದೆಯೇ ತೋರಿಸಲು. ಇದು ನಮಗೆ ತಿಳಿಸುತ್ತದೆ LLM ನಿರ್ದಿಷ್ಟ ಸಲಕರಣೆಯನ್ನುArgument ಗಳೊಂದಿಗೆ ಕರೆಯಲು ವಿನಂತಿಸುತ್ತಿದೆ. ನಿಮ್ಮ `main.rs` ಫೈಲ್‍ನ ಕೆಳಭಾಗಕ್ಕೆ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ LLM ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸುವ ಫಂಕ್ಷನ್ ವ್ಯಾಖ್ಯಾನ ಮಾಡಲು:

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

    // ಉಪಕರಣ ಕರೆಯುವಿಕೆಗಳನ್ನು ಅನ್ವಯಿಸಿ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ಸಹಾಯಕ ಸಂದೇಶವನ್ನು ಸೇರಿಸಿ

        // ಪ್ರತಿಯೊಂದು ಉಪಕರಣ ಕರೆಯುವಿಕೆಯನ್ನು ನಿಭಾಯಿಸಿ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ಸಂದೇಶಗಳಿಗೆ ಉಪಕರಣ ಫಲಿತಾಂಶವನ್ನು ಸೇರಿಸಿ
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

`tool_calls` ಗಳಿದ್ದರೆ, ಅದು ಸಲಕರಣೆ ಮಾಹಿತಿಯನ್ನು ತೆಗಿದು, MCP ಸರ್ವರ್‌ಗೆ ಸಲಕರಣೆ ವಿನಂತಿಯನ್ನು ಕರೆ ಮಾಡಿ, ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಭಾಷಣೆ ಸಂದೇಶಗಳಿಗೆ ಸೇರಿಸುತ್ತದೆ. ನಂತರ LLM ಜೊತೆಗೆ ಸಂಭಾಷಣೆಯನ್ನು ಮುಂದುವರೆಸುತ್ತದೆ ಮತ್ತು ಸಂದೇಶಗಳು ಸಹಾಯಕನ ಪ್ರತಿಕ್ರಿಯೆ ಮತ್ತು ಸಲಕರಣೆ ಕರೆ ಫಲಿತಾಂಶಗಳಿಂದ ನವೀಕರಿಸಲಾಗುತ್ತವೆ.

MCP ಕರೆಗಳಿಗೆ LLM ಮರಳಿಸುವ ಸಲಕರಣೆ ಕರೆ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆಯಲು, ನಾವು ಮತ್ತೊಂದು ಸಹಾಯಕ ಫಂಕ್ಷನ್ ಅನ್ನು ಸೇರಿಸಲಿದ್ದೇವೆ ಕರೆ ಮಾಡಲು ಬೇಕಾದ ಎಲ್ಲವನ್ನೂ ಹೊರತೆಗೆಯಲು. ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ನಿಮ್ಮ `main.rs` ಫೈಲ್‌ನ ತುದಿಗೆ ಸೇರಿಸಿ:

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

ಎಲ್ಲಾ ಭಾಗಗಳು ಸಿದ್ಧವಾಗಿದೆ, ನಾವು ಈಗ ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ನಿರ್ವಹಿಸಿ LLM ಅನ್ನು ಕರೆ ಮಾಡಬಹುದು. ನಿಮ್ಮ `main` ಫಂಕ್ಷನ್ ಅನ್ನು ಕೆಳಗಿನ ಕೋಡ್ ಸೇರಿಸಿ ಅಪ್‌ಡೇಟ್ ಮಾಡಿ:

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

ಇದು ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಮೂಲಕ ಎರಡು ಸಂಖ್ಯೆಗಳ ಮೊತ್ತವನ್ನು ಕೇಳಿ LLM ಅನ್ನು ಪ್ರಶ್ನಿಸುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ డೈನಾಮಿಕ್‌గా ಸಲಕರಣೆ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ.

ಚೆನ್ನಾಗಿದೆ, ನೀವು ಯಶಸ್ವಿಯಾಗಿ ಮಾಡಿದ್ದಾರೆ!

## ನಿಯೋಜನೆ

ಅಭ್ಯಾಸದಿಂದ ಕೋಡ್ ತೆಗೆದುಕೊಂಡು ಸರ್ವರ್ ಅನ್ನು ಹೆಚ್ಚು ಸಲಕರಣೆಗಳೊಂದಿಗೆ ನಿರ್ಮಿಸಿ. ನಂತರ LLM ಹೊಂದಿರುವ ಕ್ಲೈಂಟ್ ರಚಿಸಿ, ಅಭ್ಯಾಸದಂತೆ, ಮತ್ತು ಬಗೆಬಗೆಯ ಪ್ರಾಂಪ್ಟ್‌ಗಳೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ ನಿಮ್ಮ ಎಲ್ಲಾ ಸರ್ವರ್ ಸಲಕರಣೆಗಳು డೈನామಿಕ್‌గా ಕರೆ ಹೊಂದುವಂತೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಈ ರೀತಿಯ ಕ್ಲೈಂಟ್ ನಿರ್ಮಾಣ ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ ಉತ್ತಮ ಅನುಭವವನ್ನು ಒದಗಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಅವರು ನಿಖರ ಕ್ಲೈಂಟ್ ಆರ್ಡರ್ ಗಳ ಬದಲು ಪ್ರಾಂಪ್ಟ್ ಬಳಸಬಹುದು ಮತ್ತು ಯಾರಿಗೂ MCP ಸರ್ವರ್ ಕರೆ ಆಗುತ್ತಿರುವುದು ಗೊತ್ತಾಗುವುದಿಲ್ಲ.

## ಪರಿಹಾರ

[ಪರಿಹಾರ](./solution/README.md)

## ಪ್ರಮುಖ ಪಾಠಗಳು

- ನಿಮ್ಮ ಕ್ಲೈಂಟ್‌ಗೆ LLM ಸೇರಿಸುವುದು MCP ಸರ್ವರ್‌ಗಳೊಂದಿಗೆ ಬಳಕೆದಾರರ ಸಂವಹನ ಅತ್ಯುತ್ತಮವಾಗುತ್ತದೆ.
- MCP ಸರ್ವರ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ವಿಧಕ್ಕೆ ಪರಿವರ್ತನೆ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

## ಮಾದರಿಗಳು

- [ಜಾವಾ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/java/calculator/README.md)
- [.ನೆಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/csharp)
- [ಜಾವಾಸ್ಕೋಡ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/javascript/README.md)
- [ಟೈಪ್‌ಸ್ಕ್ರಿಪ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../samples/typescript/README.md)
- [ಪೈಥಾನ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/python)
- [ರಸ್ಟ್ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್](../../../../03-GettingStarted/samples/rust)

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

## ಮುಂದಿನದೆಯೇನು

- ಮುಂದಿನದು: [ವಿಸುಯಲ್ ಸ್ಟುಡಿಯೋ ಕೋಡ್ ಬಳಸಿ ಸರ್ವರ್ ಗ್ರಹಿಕೆ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->