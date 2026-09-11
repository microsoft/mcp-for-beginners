# LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

> [!NOTE]
> ਜਾਵਾ ਕਲਾਇੰਟ ਉਦਾਹਰਣਾਂ ਲੈਗੇਸੀ HTTP+SSE ਟਰਾਂਸਪੋਰਟ ਰਾਹੀਂ ਜੁੜਦੀਆਂ ਹਨ ਅਤੇ
> MCP `2025-11-25` SDK APIs ਨੂੰ ਟਾਰਗੇਟ ਕਰਦੀਆਂ ਹਨ। ਨਵੇਂ ਰਿਮੋਟ ਕਲਾਇੰਟਾਂ ਲਈ `2026-07-28`-ਅਨੁਕੂਲ SDK ਅਤੇ
> ਸਟਰੀਮਬਲ HTTP ਵਰਤੋਂ।

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿ ਚੁکے ਹੋ ਕਿ ਕਿਵੇਂ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਬਣਾਈਦਾ ਹੈ। ਕਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ ਤੇ ਕਾਲ ਕਰਕੇ ਆਪਣੇ ਟੂਲ, ਸਰੋਤ ਅਤੇ ਪ੍ਰಾಂਪਟ ਨੂੰ ਲਿਸਟ ਕਰ ਸਕਦਾ ਸੀ। ਪਰ, ਇਹ ਇਕ ਬਹੁਤ ਹੀ ਕਾਰਗਰ ਢੰਗ ਨਹੀਂ ਹੈ। ਤੁਹਾਡੇ ਉਪਭੋਗਤਾ ਏਜੈਂਟਿਕ ਯੁੱਗ ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਉਮੀਦ ਕਰਦੇ ਹਨ ਕਿ ਪ੍ਰਾਂਪਟ ਵਰਗੇ ਹਨ ਅਤੇ ਇੱਕ LLM ਨਾਲ ਸੰਚਾਰ ਕਰ ਸਕਦੇ ਹਨ। ਉਹ ਇਹ ਨਹੀਂ ਸੋਚਦੇ ਕਿ ਤੁਸੀਂ MCP ਵਰਤਦੇ ਹੋ ਜਾਂ ਨਹੀਂ; ਉਹ ਸਿਰਫ਼ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਰਤ ਕੇ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਉਮੀਦ ਕਰਦੇ ਹਨ। ਤਾਂ ਅਸੀਂ ਇਸ ਨੂੰ ਕਿਵੇਂ ਹੱਲ ਕਰੀਏ? ਹੱਲ ਇਹ ਹੈ ਕਿ ਕਲਾਇੰਟ ਵਿੱਚ ਇੱਕ LLM ਜੋੜੀਏ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਾਂਗੇ ਕਿ ਕਿਵੇਂ ਇੱਕ LLM ਜੋੜਕੇ ਤੁਹਾਡੇ ਕਲਾਇੰਟ ਲਈ ਬਿਹਤਰ ਤਜ਼ਰਬਾ ਦਿੱਤਾ ਜਾ ਸਕਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- LLM ਨਾਲ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਉਣਾ।
- MCP ਸਰਵਰ ਨਾਲ LLM ਰਾਹੀਂ ਬਿਨਾਂ ਰੁਕਾਵਟ ਦੇ ਇੰਟਰੈਕਟ ਕਰਨਾ।
- ਕਲਾਇੰਟ ਪਾਸੇ ਉਤਮ ਅੰਤ-ਉਪਭੋਗਤਾ ਤਜ਼ਰਬਾ ਪ੍ਰਦਾਨ ਕਰਨਾ।

## ਢੰਗ

ਆਓ ਸਮਝੀਏ ਕਿ ਸਾਡਾ ਢੰਗ ਕੀ ਹੋਵੇਗਾ। LLM ਜੋੜਨਾ ਅਸਾਨ ਲੱਗਦਾ ਹੈ, ਪਰ ਕੀ ਅਸੀਂ ਇਹ ਅਸਲ ਵਿੱਚ ਕਰਾਂਗੇ?

ਇੱਥੇ ਕਲਾਇੰਟ ਸਰਵਰ ਨਾਲ ਕਿਵੇਂ ਇੰਟਰੈਕਟ ਕਰੇਗਾ:

1. ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰੋ।

1. ਸਮਰੱਥਾਵਾਂ, ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲ ਦੀ ਸੂਚੀ ਬਣਾਓ ਅਤੇ ਉਹਨਾਂ ਦਾ ਸਕੀਮਾ ਸੇਵ ਕਰੋ।

1. ਇੱਕ LLM ਜੋੜੋ ਅਤੇ ਬਚਾਏ ਹੋਏ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਉਹਨਾਂ ਦਾ ਸਕੀਮਾ LLM ਨੂੰ ਸਮਝ ਆਉਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਪਾਸ ਕਰੋ।

1. ਯੂਜ਼ਰ ਦੇ ਪ੍ਰਾਂਪਟ ਨੂੰ ਹੱਲ ਕਰਨ ਲਈ ਉਸਨੂੰ LLM ਨੂੰ ਸਹਿਤ ਕਲਾਇੰਟ ਵੱਲੋਂ ਲਿਸਟ ਕੀਤੇ ਟੂਲ ਸਹਿਤ ਪਾਸ ਕਰੋ।

ਵਧੀਆ, ਹੁਣ ਸਾਨੂੰ ਉੱਚ starਤ੍ਹਾ ’ਤੇ ਸਮਝ ਆ ਗਿਆ ਕਿ ਅਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਅੱਥੇ ਹੇਠਾਂ ਅਭਿਆਸ ਵਿੱਚ ਇਸ ਨੂੰ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ।

## ਅਭਿਆਸ: LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਆਪਣੇ ਕਲਾਇੰਟ ਨਾਲ ਇੱਕ LLM ਜੋੜਨਾ ਸਿੱਖਾਂਗੇ।

### GitHub ਪਰਸਨਲ ਐਕਸੈਸ ਟੋਕਨ ਦੁਆਰਾ ਪ੍ਰਮਾਣਿਕਤਾ

GitHub ਟੋਕਨ ਬਣਾਉਣਾ ਸਿੱਧਾ ਸਾਦਾ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਇੱਥੇ ਦੱਸਿਆ ਗਿਆ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

- GitHub ਸੈਟਿੰਗਜ਼ ‘ਤੇ ਜਾਓ – ਸਿਖਰਲੇ ਸੱਜੇ ਕੋਨੇ ਵਿੱਚ ਆਪਣੀ ਪ੍ਰੋਫ਼ਾਈਲ ਤਸਵੀਰ ‘ਤੇ ਕਲਿੱਕ ਕਰਕੇ ਸੈਟਿੰਗਜ਼ ਚੁਣੋ।
- ਡਿਵੈਲਪਰ ਸੈਟਿੰਗਜ਼ ‘ਤੇ ਜਾਓ – ਹੇਠਾਂ ਸ੍ਕ੍ਰੋਲ ਕਰ ਕੇ ਡਿਵੈਲਪਰ ਸੈਟਿੰਗਜ਼ ‘ਤੇ ਕਲਿੱਕ ਕਰੋ।
- ਪਰਸਨਲ ਐਕਸੈਸ ਟੋਕਨ ਚੁਣੋ – ਫਾਈਨ-ਗ੍ਰੇਨਡ ਟੋਕਨ ‘ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫਿਰ ਨਵਾਂ ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ।
- ਆਪਣਾ ਟੋਕਨ ਸੰਰਚਿਤ ਕਰੋ – ਸਾਰਥਕ ਨੋਟ ਸ਼ਾਮਲ ਕਰੋ, ਸਮਾਪਤੀ ਮਿਤੀ ਤੈਅ ਕਰੋ, ਅਤੇ ਲੋੜੀਂਦੇ ਸਪੈਕ (ਅਧਿਕਾਰ) ਚੁਣੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ ਮਾਡਲ ਅਧਿਕਾਰ ਜਰੂਰੀ ਹਨ।
- ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ ਅਤੇ ਕਾਪੀ ਕਰੋ – ਜਨਰੇਟ ਟੋਕਨ ‘ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਜਲਦੀ ਹੀ ਕਾਪੀ ਕਰ ਲਓ, ਕਿਉਂਕਿ ਦੁਬਾਰਾ ਦੇਖਣ ਦੀ ਸਹੁਲਤ ਨਹੀਂ ਮਿਲੇਗੀ।

### -1- ਸਰਵਰ ਨਾਲ ਜੁੜੋ

ਆਓ ਪਹਿਲਾਂ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਈਏ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ zod ਨੂੰ ਆਯਾਤ ਕਰੋ

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਸ ਬਣਾਈ ਜਿਸ ਵਿੱਚ ਦੋ ਮੈਂਬਰ ਹਨ, `client` ਅਤੇ `openai` ਜੋ ਕਲਾਇੰਟ ਮੈਨੇਜ ਕਰਨ ਅਤੇ LLM ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨਗੇ।
- ਆਪਣੇ LLM ਇੰਸਟੈਂਸ ਨੂੰ GitHub ਮਾਡਲ ਵਰਤ ਕੇ `baseUrl` ਸੈੱਟ ਕਰਕੇ ਇੰਫਰੇਨਸ API ਨਾਲ ਜੋੜਿਆ।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਐਗਜ਼ਿਕਿਊਟੇਬਲ
    args=["run", "server.py"],  # ਵਿਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਆਰਗੁਮੈਂਟ
    env=None,  # ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ
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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਲਈ ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਇਆ

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

ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `pom.xml` ਫਾਈਲ ਵਿੱਚ LangChain4j ਡਿਪੈਂਡੇਸੀਜ਼ ਜੋੜਣੀਆਂ ਹੋਣਗੀਆਂ। MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI-ਅਨੁਕੂਲ MiniMax API ਲਈ ਇਹ ਡਿਪੈਂਡੇਸੀਜ਼ ਜੋੜੋ:

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

ਆਪਣਾ MiniMax API ਕੁੰਜੀ ਸੈੱਟ ਕਰੋ ਅਤੇ ਕੋਈ ਵੈਚਿਕ चरणਵਿੰਨ ਜਾਂ ਮਾਡਲ ਚੁਣੋ।
`MINIMAX_MODEL_ID` `MiniMax-M3` ਅਤੇ `MiniMax-M2.7` ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ। ਜੇ
`OPENAI_BASE_URL` ਸੈੱਟ ਨਹੀਂ ਹੈ, ਤਾਂ `MINIMAX_REGION` `global_en` ਅਤੇ `cn_zh` ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ਇਲਾਕੇ ਦੇ ਅਨੁਸਾਰ ਐਂਡਪੌਇੰਟ ਚੁਣਨ ਲਈ, `OPENAI_BASE_URL` ਛੱਡ ਦਿਓ:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ਫਿਰ ਆਪਣੀ ਜਾਵਾ ਕਲਾਇੰਟ ਕਲਾਸ ਬਣਾਓ:

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

        // ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ MCP ਟ੍ਰਾਂਸਪੋਰਟ ਬਣਾਓ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ਕਲਾਇੰਟ ਬਣਾਓ
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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- **LangChain4j Dependencies ਜੋੜੀਆਂ**: MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI-ਅਨੁਕੂਲ MiniMax API ਲਈ ਜ਼ਰੂਰੀ
- **LangChain4j ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ**: MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI ਚੈਟ ਮਾਡਲ ਫੰਕਸ਼ਨਾਲਟੀ ਲਈ
- **ਇੱਕ `ChatLanguageModel` ਬਣਾਇਆ**: MiniMax ਨੂੰ ਲਾਗੂ ਕੀਤਾ ਤੇ API ਕੁੰਜੀ, ਐਂਡਪੌਇੰਟ, ਅਤੇ ਸਮਰਥਿਤ ਮਾਡਲ ID ਨਾਲ ਕਨਫਿਗਰ ਕੀਤਾ
- **HTTP ਟਰਾਂਸਪੋਰਟ ਸੈੱਟ ਕੀਤਾ**: Server-Sent Events (SSE) ਰਾਹੀਂ MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਲਈ
- **ਇੱਕ MCP ਕਲਾਇੰਟ ਬਣਾਇਆ**: ਜੋ ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਨੂੰ ਸੰਭਾਲੇਗਾ
- **LangChain4j ਦਾ ਇਨਬਿਲਟ MCP ਸਹਿਯੋਗ ਵਰਤਿਆ**: ਜੋ LLM ਅਤੇ MCP ਸਰਵਰਾਂ ਵਿਚਕਾਰ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਨੂੰ ਆਸਾਨ ਬਨਾਉਂਦਾ ਹੈ

#### Rust

ਇਹ ਉਦਾਹਰਣ ਮੰਨਦਾ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ Rust ਬੇਸਡ MCP ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ ਸਰਵਰ ਬਣਾਉਣ ਲਈ [01-first-server](../01-first-server/README.md) ਪਾਠ ਵਾਪਸ ਵੇਖੋ।

ਇੱਕ ਵਾਰੀ ਤੁਹਾਡੇ ਕੋਲ Rust MCP ਸਰਵਰ ਹੋਵੇ, ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਸਰਵਰ ਵਾਲੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ। ਫਿਰ ਨਵਾਂ LLM ਕਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ਆਪਣੀ `Cargo.toml` ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਡਿਪੈਂਡੇਸੀਜ਼ ਸ਼ਾਮਲ ਕਰੋ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> ਸਾਰੇ ਉਪਲਬਧਤਾ ਮੁਤਾਬਕ Rust ਲਈ ਕੋਈ ਅਧਿਕਾਰਤ OpenAI ਲਾਇਬ੍ਰੇਰੀ ਨਹੀਂ ਹੈ, ਪਰ `async-openai` ਕ੍ਰੇਟ ਇੱਕ [ਕਮਿਊਨਿਟੀ ਸੰਭਾਲੀ ਲਾਇਬ੍ਰੇਰੀ](https://platform.openai.com/docs/libraries/rust#rust) ਹੈ ਜੋ ਆਮ ਤੌਰ ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

`src/main.rs` ਫਾਈਲ ਖੋਲ੍ਹੋ ਅਤੇ ਇਸ ਦੀ ਸਮੱਗਰੀ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਬਦਲੋ:

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
    // ਸ਼ੁਰੂਆਤੀ ਸੁਨੇਹਾ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ਕਲਾਇੰਟ ਸੈਟਅਪ ਕਰੋ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ਕਲਾਇੰਟ ਸੈਟਅਪ ਕਰੋ
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

    // TODO: MCP ਟੂਲ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ

    // TODO: ਟੂਲ ਕਾਲਾਂ ਨਾਲ LLM ਗੱਲਬਾਤ

    Ok(())
}
```

ਇਹ ਕੋਡ ਇੱਕ ਬੁਨਿਆਦੀ Rust ਐਪਲੀਕੇਸ਼ਨ ਸੈੱਟਅਪ ਕਰਦਾ ਹੈ ਜੋ MCP ਸਰਵਰ ਅਤੇ GitHub ਮਾਡਲਾਂ ਨਾਲ LLM ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਕਨੈਕਟ ਕਰੇਗਾ।

> [!IMPORTANT]
> ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ `OPENAI_API_KEY` ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਵਿੱਚ ਆਪਣਾ GitHub ਟੋਕਨ ਸੈੱਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

ਵਧੀਆ, ਅੱਗੇ ਦੇ ਕਦਮ ਵੱਜੋਂ, ਅਸੀਂ ਸਰਵਰ ਤੇ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਂਦੇ ਹਾਂ।

### -2- ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ

ਹੁਣ ਅਸੀਂ ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਕੇ ਉਸ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਪੁੱਛਾਂਗੇ:

#### Typescript

ਇਸੇ ਕਲਾਸ ਵਿੱਚ, ਹੇਠਾਂ ਦਿੱਤੇ ਮੈਥਡ ਜੋੜੋ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ਸੰਦ ਸੂਚੀਬੱਧ ਕਰਨਾ
    const toolsResult = await this.client.listTools();
}
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਲਈ ਕੋਡ ਜੋੜਿਆ, `connectToServer`.
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਇਆ ਜੋ ਅਸੀਂ ਪਿਆਰ ਫ਼ਲੋ ਵਰਤੋਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਹੈ। ਹੁਣ ਤੱਕ ਇਹ ਸਿਰਫ ਟੂਲਸ ਦੀ ਲਿਸਟ ਦਿੰਦਾ ਹੈ ਪਰ ਅਸੀਂ ਇਸ ਵਿੱਚ ਹੋਰ ਵੀ ਸ਼ਾਮਲ ਕਰਾਂਗੇ।

#### Python

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
    print("Tool", tool.inputSchema["properties"])
```

ਅਸੀਂ ਜੋੜਿਆ:

- ਸਰੋਤ ਅਤੇ ਟੂਲ ਸੂਚੀਬੱਧ ਕੀਤੇ ਅਤੇ ਛਾਪੇ। ਟੂਲ ਲਈ ਅਸੀਂ `inputSchema` ਵੀ ਲਿਸਟ ਕਰਦੇ ਹਾਂ, ਜੋ ਅੱਗੇ ਵਰਤਾਂਗੇ।

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


ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ 'ਤੇ ਉਪਲਬਧ ਟੂਲ ਦੀ ਸੂਚੀ ਦਿੱਤੀ ਹੈ
- ਹਰ ਟੂਲ ਲਈ, ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਸ ਦਾ ਸਕੀਮਾ ਦੱਸਿਆ ਹੈ। ਆਖਰੀ ਨੂੰ ਅਸੀਂ ਜਲਦੀ ਹੀ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਾਂਗੇ।

#### ਜਾਵਾ

```java
// ਇੱਕ ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਬਣਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
// - MCP ਸਰਵਰ ਤੋਂ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ
// - MCP ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ LangChain4j ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ
// - ਟੂਲ ਦੀ ਚਾਲੂ ਅਤੇ ਪ੍ਰਤਿਕਿਰਿਆਵਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `McpToolProvider` ਬਣਾਇਆ ਹੈ ਜੋ MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਟੂਲ ਆਪ-ਆਪ ਖੋਜ ਕੇ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ
- ਟੂਲ ਪ੍ਰਦਾਇਕ MCP ਟੂਲ ਸਕੀਮਾਂ ਅਤੇ LangChain4j ਦੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿਚ ਅੰਦਰੂਨੀ ਤੌਰ ਤੇ ਤਬਦੀਲੀ ਦਾ ਸੰਭਾਲ ਕਰਦਾ ਹੈ
- ਇਹ ਢੰਗ ਹੱਥੋਂ ਟੂਲ ਦੀ ਸੂਚੀ ਅਤੇ ਤਬਦੀਲੀ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਸਧਾਰਨ ਕਰਦਾ ਹੈ

#### ਰੱਸਟ

MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ `list_tools` ਮੈਥਡ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਤੁਹਾਡੇ `main` ਫੰਕਸ਼ਨ ਵਿੱਚ, MCP ਕਲਾਇਂਟ ਸੈੱਟਅੱਪ ਕਰਨ ਦੇ ਬਾਅਦ, ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ:

```rust
// MCP ਟੂਲ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਨੂੰ LLM ਟੂਲਾਂ ਵਿੱਚ ਤਬਦੀਲ ਕਰਨਾ

ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਅਗਲਾ ਕਦਮ ਉਹਨਾਂ ਨੂੰ ਐਸਾ ਫਾਰਮੈਟ ਵਿੱਚ ਤਬਦੀਲ ਕਰਨਾ ਹੈ ਜੋ LLM ਸਮਝ ਸਕੇ। ਇਤੋ ਬਾਅਦ ਅਸੀਂ ਇਹ ਸਮਰੱਥਾਵਾਂ ਆਪਣੇ LLM ਲਈ ਟੂਲ ਵਜੋਂ ਦਿੰਦੇ ਹਾਂ।

#### ਟਾਇਪਸਕ੍ਰਿਪਟ

1. ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ ਜੋ MCP ਸਰਵਰ ਤੋਂ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਉਪਯੋਗ ਯੋਗ ਟੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਤਬਦੀਲ ਕਰਦਾ ਹੈ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ਇਨਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਜੋਡ ਸਕੀਮਾ ਬਣਾਓ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ਟਾਈਪ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ "ਫੰਕਸ਼ਨ" ਸੈੱਟ ਕਰੋ
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

    ਉੱਪਰ ਦਿੱਤਾ ਕੋਡ MCP ਸਰਵਰ ਤੋਂ ਜਵਾਬ ਲੈ ਕੇ ਉਸਨੂੰ ਐਸਾ ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ।

2. ਅਗਲਾ ਕਦਮ 'run' ਮੈਥਡ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨਾ ਹੈ ਤਾਂ ਜੋ ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਜਾ ਸਕੇ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ `run` ਮੈਥਡ ਨੂੰ ਅੱਪਡੇਟ ਕੀਤਾ ਹੈ ਤਾਂ ਜੋ ਨਤੀਜੇ ਮੈਪ ਕਰਕੇ ਹਰ ਐਂਟਰੀ ਨੂੰ `openAiToolAdapter` ਕਾਲ ਕੀਤਾ ਜਾਵੇ।

#### ਪਾਇਥਨ

1. ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤਾ ਤਬਦੀਲੀਕਾਰ (ਕਨਵਰਟਰ) ਫੰਕਸ਼ਨ ਬਣਾਈਏ

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

    ਉੱਪਰ ਦਿੱਤੇ ਫੰਕਸ਼ਨ `convert_to_llm_tools` ਵਿੱਚ ਅਸੀਂ MCP ਟੂਲ ਦਾ ਜਵਾਬ ਲੈ ਕੇ ਉਸਨੂੰ ਐਸਾ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਾਂ ਜੋ LLM ਸਮਝ ਸਕੇ।

2. ਫਿਰ ਆਪਣਾ ਕਲਾਇੰਟ ਕੋਡ ਅੱਪਡੇਟ ਕਰੀਏ ਤਾਂ ਜੋ ਇਹ ਫੰਕਸ਼ਨ ਵਰਤ ਸਾਰੇ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ਇੱਥੇ, ਅਸੀਂ `convert_to_llm_tool` ਨੂੰ ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ ਤਾਂ ਜੋ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ ਐਸਾ ਬਣਾ ਸਕੀਏ ਜੋ ਬਾਅਦ ਵਿੱਚ LLM ਨੂੰ ਦੇ ਸਕੀਏ।

#### .NET

1. ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ ਐਸਾ ਬਣਾ ਕੇ LLM ਲਈ ਸਮਝਣਯੋਗ ਬਣਾਉਣ ਲਈ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੀਏ

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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਫੰਕਸ਼ਨ `ConvertFrom` ਬਣਾਇਆ ਜੋ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁੱਟ ਸਕੀਮਾ ਲੈਂਦਾ ਹੈ।
- ਇੱਕ ਐਸਾ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜੋ FunctionDefinition ਬਣਾਉਂਦਾ ਹੈ ਜੋ ChatCompletionsDefinition ਨੂੰ ਮਿਲਦਾ ਹੈ। ਇਹ ਅਜਿਹਾ ਕੁਝ ਹੈ ਜੋ LLM ਸਮਝਦਾ ਹੈ।

2. ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਉੱਪਰ ਦਿੱਤੇ ਫੰਕਸ਼ਨ ਦਾ ਲਾਭ ਲੈਣ ਲਈ ਜਿਆਦਾ ਕੋਡ ਕਿਵੇਂ ਅੱਪਡੇਟ ਕਰ ਸਕਦੇ ਹਾਂ:

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

#### ਜਾਵਾ

```java
// ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰਐਕਸ਼ਨ ਲਈ ਬੋਟ ਇੰਟਰਫੇਸ ਬਣਾਓ
public interface Bot {
    String chat(String prompt);
}

// LLM ਅਤੇ MCP ਟੂਲਜ਼ ਨਾਲ AI ਸੇਵਾ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੈਕਸ਼ਨਾਂ ਲਈ ਇੱਕ ਸਧਾਰਣ `Bot` ਇੰਟਰਫੇਸ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ
- LangChain4j ਦੇ `AiServices` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਤਾਂ ਜੋ MCP ਟੂਲ ਪ੍ਰਦਾਇਕ ਨਾਲ LLM ਨੂੰ ਆਪ-ਆਪ ਜੋੜਿਆ ਜਾ ਸਕੇ
- ਫਰੇਮਵਰਕ ਟੂਲ ਸਕੀਮਾ ਤਬਦੀਲੀ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਨੂੰ ਪਿੱਛੇ ਦਰਸ਼ਨ 'ਚ ਆਪ-ਆਪ ਸੰਭਾਲਦਾ ਹੈ
- ਇਹ ਢੰਗ ਹੱਥੋਂ ਟੂਲ ਤਬਦੀਲੀ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ - LangChain4j MCP ਟੂਲਾਂ ਨੂੰ LLM-ਸੰਗਤ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਾਰੀ ਜਟਿਲਤਾ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ

#### ਰੱਸਟ

MCP ਟੂਲ ਜਵਾਬ ਨੂੰ ਐਸਾ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਜੋ LLM ਸਮਝ ਸਕੇ, ਅਸੀਂ ਇੱਕ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ ਜੋ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੇਗਾ। ਆਪਣੀ `main.rs` ਫਾਈਲ ਵਿੱਚ `main` ਫੰਕਸ਼ਨ ਦੇ ਹੇਠਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ। ਇਹ LLM ਨੂੰ ਬੇਨਤੀ ਕਰਨ ਸਮੇਂ ਕਾਲ ਕੀਤਾ ਜਾਵੇਗਾ:

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


ਬਹੁਤ ਵਧੀਆ, ਅਸੀਂ ਕਿਸੇ ਵੀ ਉਪਭੋਗਤਾ ਦੀ ਬੇਨਤੀ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਸੈਟਅਪ ਨਹੀਂ ਹਾਂ, ਇਸ ਲਈ ਅਸੀਂ ਇਹ ਅਗਲੇ ਕਦਮ ਵਜੋਂ ਕਰੀਏ।

### -4- ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ ਬੇਨਤੀ ਨੂੰ ਸੰਭਾਲੋ

ਕੋਡ ਦੇ ਇਸ ਹਿੱਸੇ ਵਿੱਚ, ਅਸੀਂ ਉਪਭੋਗਤਾ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਸੰਭਾਲਾਂਗੇ।

#### TypeScript

1. ਇੱਕ ਮੈਥਡ ਜੋ ਸਾਡੇ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਪਰੀਤ ਕੀਤਾ ਜਾਵੇਗਾ, ਸ਼ਾਮਲ ਕਰੋ:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ਸਰਵਰ ਦੇ ਸਾਧਨ ਨੂੰ ਕਾਲ ਕਰੋ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ਨਤੀਜੇ ਨਾਲ ਕੁਝ ਕਰੋ
        // ਕਰਨਾ ਹੈ

        }
    }
    ```

    ਪਹਿਲਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਇੱਕ ਮੈਥਡ `callTools` ਸ਼ਾਮਲ ਕੀਤਾ।
    - ਇਹ ਮੈਥਡ LLM ਦੇ ਜਵਾਬ ਨੂੰ ਲੈਂਦਾ ਹੈ ਅਤੇ ਦੇਖਦਾ ਹੈ ਕਿ ਕਿਹੜੇ ਟੂਲ ਕਾਲ ਕੀਤੇ ਗਏ ਹਨ, ਜੇ ਕੋਈ ਹਨ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        }
        ```

    - ਜੇ LLM ਦੱਸਦਾ ਹੈ ਕਿ ਟੂਲ ਕਾਲ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਤਾਂ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ:

        ```typescript
        // 2. ਸਰਵਰ ਦੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ਨਤੀਜੇ ਨਾਲ ਕੁਝ ਕਰੋ
        // ਕਰਨ ਵਾਲਾ ਕੰਮ
        ```

2. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾ ਕਿ LLM ਨੂੰ ਕਾਲ ਅਤੇ `callTools` ਕਾਲ ਸੰਮਿਲਿਤ ਹੋਣ:

    ```typescript

    // 1. LLM ਲਈ ਇਨਪੁੱਟ ਮੈਸੇਜ ਬਣਾਓ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ਨੂੰ ਕਾਲ ਕਰਨਾ
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ਦੀ ਜਵਾਬ ਨੂੰ ਪੜ੍ਹੋ, ਹਰ ਚੋਣ ਲਈ, ਜਾਂਚੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ਬਹੁਤ ਵਧੀਆ, ਆਓ ਕੋਡ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਲਿਖੀਏ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ ਜ਼ੋਡ ਇੰਪੋਰਟ ਕਰੋ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ਭਵਿੱਖ ਵਿੱਚ ਇਸ URL ਨੂੰ ਬਦਲਣ ਦੀ ਜਰੂਰਤ ਹੋ ਸਕਦੀ ਹੈ: https://models.github.ai/inference
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
          // ਇਨਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਅਧਾਰ 'ਤੇ ਜ਼ੋਡ ਸਕੀਮਾ ਬਣਾਓ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ਕੁੱਲਤਰ ਤੌਰ 'ਤੇ ਟਾਈਪ "function" ਸੈੱਟ ਕਰੋ
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
    
    
          // 2. ਸਰਵਰ ਦੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ਨਤੀਜੇ ਨਾਲ ਕੁਝ ਕਰੋ
          // ਟੂ ਡੂ
    
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
    
        // 3. LLM ਜਵਾਬ ਵਿਚੋਂ ਹਰ ਚੋਣ ਲਈ ਦੇਖੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
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

1. ਆਓ ਕੋਈ ਆਯਾਤ ਸ਼ਾਮਲ ਕਰੀਏ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਹਨ

    ```python
    # ਐਲਐੱਲਐਮ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. ਅਗਲਾ, ਆਓ ਉਹ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੀਏ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰੇਗਾ:

    ```python
    # ਐਲਐਲਐਮ

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
            # ਵਿਕਲਪਿਕ ਪੈਰਾਮੀਟਰ
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

    ਪਹਿਲਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਉਹ ਫੰਕਸ਼ਨ ਜੋ ਅਸੀਂ MCP ਸਰਵਰ 'ਤੇ ਲੱਭੇ ਅਤੇ ਕਨਵਰਟ ਕੀਤੇ, LLM ਨੂੰ ਦਿੱਤੇ।
    - ਫਿਰ ਅਸੀਂ LLM ਨੂੰ ਉਨ੍ਹਾਂ ਫੰਕਸ਼ਨਾਂ ਦੇ ਨਾਲ ਕਾਲ ਕੀਤਾ।
    - ਫਿਰ ਅਸੀਂ ਨਤੀਜੇ ਦੀ ਜਾਂਚ ਕਰ ਰਹੇ ਹਾਂ ਕਿ ਕਿਸੇ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।
    - ਆਖਿਰਕਾਰ, ਅਸੀਂ ਕਾਲ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨਾਂ ਦੀ ਸੂਚੀ ਦਿੰਦੇ ਹਾਂ।

3. ਅੰਤਿਮ ਕਦਮ, ਆਓ ਆਪਣੇ ਮੁੱਖ ਕੋਡ ਨੂੰ ਅਪਡੇਟ ਕਰੀਏ:

    ```python
    prompt = "Add 2 to 20"

    # LLM ਨੂੰ ਪੁੱਛੋ ਕਿ ਸਰਗਰਮੀਆਂ ਲਈ ਕਿਹੜੇ ਸੰਦ ਹਨ, ਜੇ ਕੋਈ ਹਨ
    functions_to_call = call_llm(prompt, functions)

    # ਸਿਫਾਰਸ਼ੀ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰੋ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ਇਹ, ਉੱਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਟੂਲ ਨੂੰ `call_tool` ਰਾਹੀਂ ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ, ਉਨ੍ਹਾਂ ਫੰਕਸ਼ਨਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਜੋ LLM ਨੇ ਸਾਡੇ ਪ੍ਰੰਪਟ ਅਨੁਸਾਰ ਕਾਲ ਕਰਨ ਦੀ ਸੋਚੀ।
    - MCP ਸਰਵਰ ਨੂੰ ਟੂਲ ਕਾਲ ਦੇ ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕਰ ਰਹੇ ਹਾਂ।

#### .NET

1. ਆਓ LLM ਪ੍ਰੰਪਟ ਬੇਨਤੀ ਕਰਨ ਲਈ ਕੁਝ ਕੋਡ ਵੇਖੀਏ:

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

    ਪਹਿਲਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕੀਤੇ, `var tools = await GetMcpTools()`।
    - ਇੱਕ ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ `userMessage` ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ।
    - ਮਾਡਲ ਅਤੇ ਟੂਲ ਸਪਿਬਧ ਕਰਦੇ ਇੱਕ ਵਿਕਲਪ ਵਸਤੂ ਬਣਾਈ।
    - LLM ਵੱਲ ਬੇਨਤੀ ਕੀਤੀ।

2. ਆਖਰੀ ਕਦਮ, ਆਓ ਵੇਖੀਏ ਕਿ ਕੀ LLM ਸੋਚਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਕੋਈ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ:

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

    ਪਹਿਲਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਲੂਪ ਕੀਤਾ।
    - ਹਰ ਟੂਲ ਕਾਲ ਲਈ, ਨਾਮ ਅਤੇ ਆਰਗੂਮੈਂਟ ਪਾਰਸ ਕਰਕੇ MCP ਸਰਵਰ 'ਤੇ ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਨਾਲ ਟੂਲ ਕਾਲ ਕੀਤਾ। ਆਖਿਰਕਾਰ ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕੀਤੇ।

ਇੱਥੇ ਪੂਰਾ ਕੋਡ ਹੈ:

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

#### Java

```java
try {
    // ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਬੇਨਤੀਆਂ ਨੂੰ ਚਲਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ
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

ਪਹਿਲਾਂ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ ਦੇ ਟੂਲਾਂ ਨਾਲ ਸਰਲ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਵਰਤਿਆ
- LangChain4j ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
  - ਜਦੋਂ ਲੋੜ ਹੋਵੇ, ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ ਨੂੰ ਟੂਲ ਕਾਲਾਂ ਵਿੱਚ ਬਦਲਦਾ ਹੈ
  - LLM ਦੇ ਫੈਸਲੇ ਅਨੁਸਾਰ ਉਚਿਤ MCP ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ
  - LLM ਅਤੇ MCP ਸਰਵਰ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਬੰਧ ਕਰਦਾ ਹੈ
- `bot.chat()` ਮੈਥਡ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ MCP ਟੂਲਾਂ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਤੋਂ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ
- ਇਹ ਤਰੀਕਾ ਇੱਕ ਬੇਹਤਰ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਅੰਦਰੂਨੀ MCP ਲਾਗੂ ਕਰਨ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੋੜੀ ਨਹੀਂ ਹੁੰਦੀ

ਪੂਰਾ ਕੋਡ ਉਦਾਹਰਣ:

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

#### Rust


ਇੱਥੇ ਜ਼ਿਆਦਾਤਰ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਮਪਟ ਨਾਲ LLM ਨੂੰ ਕਾਲ ਕਰਾਂਗੇ, ਫਿਰ ਜਵਾਬ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਾਂਗੇ ਜੇਕਰ ਕਿਸੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੋਵੇ। ਜੇ ਐਸਾ ਹੋਵੇ ਤਾਂ ਅਸੀਂ ਉਹ ਟੂਲਜ਼ ਕਾਲ ਕਰਾਂਗੇ ਅਤੇ ਗੱਲਬਾਤ LLM ਨਾਲ ਜਾਰੀ ਰੱਖਾਂਗੇ ਜਦ ਤੱਕ ਹੋਰ ਕਿਸੇ ਟੂਲ ਕਾਲ ਦੀ ਲੋੜ ਨਾ ਹੋਵੇ ਅਤੇ ਸਾਡੇ ਕੋਲ ਅੰਤਿਮ ਜਵਾਬ ਆ ਜਾਵੇ।

ਅਸੀਂ LLM ਨੂੰ ਕਈ ਵਾਰੀ ਕਾਲ ਕਰਾਂਗੇ, ਇਸ ਲਈ ਆਓ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੀਏ ਜੋ LLM ਕਾਲ ਨੂੰ ਸੰਭਾਲੇਗਾ। ਆਪਣੀ `main.rs` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ:

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

ਇਹ ਫੰਕਸ਼ਨ LLM ਕਲਾਇੰਟ, ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ (ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਪ੍ਰਾਮਪਟ ਵੀ ਸ਼ਾਮਲ ਹੈ), MCP ਸਰਵਰ ਤੋਂ ਟੂਲਜ਼ ਲੈਂਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਵਾਪਸ ਕਰਦਾ ਹੈ।

LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਵਿੱਚ `choices` ਦੀ ਇੱਕ ਐਰੇ ਹੋਵੇਗੀ। ਸਾਨੂੰ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਨੀ ਪਵੇਗੀ ਇਹ ਵੇਖਣ ਲਈ ਕਿ ਕੋਈ `tool_calls` ਮੌਜੂਦ ਹਨ ਜਾਂ ਨਹੀਂ। ਇਹ ਸਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ LLM ਕਿਸੇ ਖਾਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰ ਰਿਹਾ ਹੈ ਜਿੱਥੇ ਦਲੀਲਾਂ ਦਿੱਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਆਪਣੇ `main.rs` ਫਾਇਲ ਦੇ ਤਲ ਦਾ ਹਿੱਸਾ ਬਣਾਓ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋ LLM ਜਵਾਬ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲੇਗਾ:

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

    // ਸਮੱਗਰੀ ਪ੍ਰਿੰਟ ਕਰੋ ਜੇ ਉਪਲਬਧ ਹੋਵੇ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲੋ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ਸਹਾਇਕ ਸੁਨੇਹਾ ਸ਼ਾਮਲ ਕਰੋ

        // ਹਰੇਕ ਟੂਲ ਕਾਲ ਚਲਾਓ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ਸੰਦੇਸ਼ਾਂ ਵਿੱਚ ਟੂਲ ਨਤੀਜੇ ਸ਼ਾਮਲ ਕਰੋ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ਟੂਲ ਨਤੀਜਿਆਂ ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖੋ
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

ਜੇ `tool_calls` ਮੌਜੂਦ ਹਨ, ਇਹ ਟੂਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਦਾ ਹੈ, MCP ਸਰਵਰ ਨੂੰ ਟੂਲ ਬੇਨਤੀ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਗੱਲਬਾਤੀ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਨਤੀਜੇ ਜੋੜਦਾ ਹੈ। ਫਿਰ ਇਹ LLM ਨਾਲ ਗੱਲਬਾਤ ਨੂੰ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਸਹਾਇਕ ਦੇ ਜਵਾਬ ਅਤੇ ਟੂਲ ਕਾਲ ਨਤੀਜਿਆਂ ਨਾਲ ਅਪਡੇਟ ਕਰਦਾ ਹੈ।

MCP ਕਾਲਜ਼ ਲਈ LLM ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੇ ਟੂਲ ਕਾਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਣ ਲਈ, ਅਸੀਂ ਇੱਕ ਹੋਰ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਸਾਰਾ ਡੈਟਾ ਕੱਢੇਗਾ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਆਪਣੀ `main.rs` ਫਾਇਲ ਦੇ ਅਖੀਰ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ:

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

ਸਾਰੇ ਹਿੱਸੇ ਮੌਜੂਦ ਹੋਣ ਨਾਲ, ਹੁਣ ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਮਪਟ ਸੰਭਾਲ ਸਕਦੇ ਹਾਂ ਅਤੇ LLM ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਅਪਡੇਟ ਕਰੋ:

```rust
// ਟੂਲ ਕਾਲਾਂ ਨਾਲ LLM ਗੱਲਬਾਤ
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

ਇਹ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਮਪਟ ਨਾਲ LLM ਨੂੰ ਪੁੱਛੇਗਾ ਕਿ ਦੋ ਨੰਬਰਾਂ ਦਾ ਜੋੜ ਕੀ ਹੈ, ਅਤੇ ਜਵਾਬ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਦਾ ਹੋਇਆ ਟੂਲ ਕਾਲਜ਼ ਨੂੰ ਡਾਇਨਾਮਿਕ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲੇਗਾ।

ਵਧੀਆ, ਤੁਸੀਂ ਕਰ ਲਿਆ!

## ਅਸਾਈਨਮੈਂਟ

ਵਰਕਆਊਟ ਤੋਂ ਕੋਡ ਲਓ ਅਤੇ ਕੁਝ ਹੋਰ ਟੂਲਜ਼ ਨਾਲ ਸਰਵਰ ਬਣਾਓ। ਫਿਰ ਇੱਕ LLM ਵਾਲਾ ਕਲਾਇੰਟ ਬਣਾਓ, ਜਿਵੇਂ ਕਿ ਵਰਕਆਊਟ ਵਿੱਚ ਹੈ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਾਮਪਟ ਨਾਲ ਟੈਸਟ ਕਰੋ ਇਹ ਜਾਂਚਣ ਲਈ ਕਿ ਤੁਹਾਡੇ ਸਾਰੇ ਸਰਵਰ ਟੂਲਜ਼ ਡਾਇਨਾਮਿਕ ਤੌਰ 'ਤੇ ਕਾਲ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਇਸ ਤਰੀਕੇ ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਅੰਤਿਮ ਵਰਤੋਂਕਾਰ ਨੂੰ ਵਧੀਆ ਅਨੁਭਵ ਮਿਲੇਗਾ ਕਿਉਂਕਿ ਉਹ ਪ੍ਰਾਮਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ, ਸਹੀ ਕਲਾਇੰਟ ਕਮਾਂਡ ਦੀ ਬਜਾਏ, ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਵੀ MCP ਸਰਵਰ ਕਾਲ ਹੋਣ ਦਾ ਪਤਾ ਨਹੀਂ ਹੁੰਦਾ।

## ਹੱਲ

[Solution](./solution/README.md)

## ਮੁੱਖ ਗੱਲਾਂ

- ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਲ ਕਰਨਾ MCP ਸਰਵਰਾਂ ਨਾਲ ਉਪਭੋਗਤਾਵਾਂ ਦੀ ਬਿਹਤਰ ਵਰਤੋਂ ਲਈ ਸੋਧ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਦੇ ਜਵਾਬ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਤਬਦੀਲ ਕਰਨਾ ਪਵੇਗਾ ਕਿ LLM ਉਸਨੂੰ ਸਮਝ ਸਕੇ।

## ਨਮੂਨੇ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ਵਾਧੂ ਸਰੋਤ

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [Visual Studio Code ਦੀ ਵਰਤੋਂ ਨਾਲ ਸਰਵਰ ਦੀ ਖਪਤ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->