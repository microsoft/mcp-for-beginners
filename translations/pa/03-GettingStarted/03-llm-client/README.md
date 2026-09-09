# LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਹੈ ਕਿ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਕਿਵੇਂ ਬਣਾਉਣਾ ਹੈ। ਕਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਖੁਦ-ਮੁਖਤਿਆਰ ਤੌਰ 'ਤੇ ਕਾਲ ਕਰਦਾ ਆਇਆ ਹੈ ਜਿਸ ਨਾਲ ਉਹ ਆਪਣੇ ਟੂਲ, ਸਰੋਤ, ਅਤੇ ਪ੍ਰਾਂਪਟ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ। ਪਰ ਇਹ ਇੱਕ ਬਹੁਤ ਪ੍ਰਯੋਗਕਾਰੀ ਤਰੀਕਾ ਨਹੀਂ ਹੈ। ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਏਜੈਂਟਿਕ ਯੁੱਗ ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਉਹ ਪ੍ਰਾਂਪਟ ਵਰਤਣਾ ਅਤੇ LLM ਨਾਲ ਸੰਚਾਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਨ। ਉਹ ਇਹ ਨਹੀਂ ਦੇਖਦੇ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਸਮਰਥਨਾਂ ਨੂੰ ਭੰਡਾਰਿਤ ਕਰਨ ਲਈ MCP ਵਰਤਦੇ ਹੋ; ਉਹ ਸਿਰਫ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਰਤ ਕੇ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਉਮੀਦ ਰੱਖਦੇ ਹਨ। ਹੁਣ ਅਸੀਂ ਇਸ ਨੂੰ ਕਿਵੇਂ ਹੱਲ ਕਰਾਂਗੇ? ਹੱਲ ਇਹ ਹੈ ਕਿ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਜੋੜਿਆ ਜਾਵੇ।

## ਜਾਇਜ਼ਾ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਾਂਗੇ ਕਿ ਕਿਵੇਂ ਕਿਸੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਜੋੜਿਆ ਜਾਏ ਅਤੇ ਦਿਖਾਇਆ ਜਾਵੇ ਕਿ ਇਹ ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਲਈ ਬਿਹਤਰ ਅਨੁਭਵ ਕਿਵੇਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਯੋਗ ਹੋਵੋਗੇ:

- LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ।
- LLM ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ ਇਕ MCP ਸਰਵਰ ਨਾਲ ਬਿਨਾ ਰੁਕਾਵਟ ਇੰਟਰੈਕਟ ਕਰਨਾ।
- ਕਲਾਇੰਟ ਪਾਸੇ ਉਪਭੋਗਤਾ ਲਈ ਬਿਹਤਰ ਅਨੁਭਵ ਮੁਹੱਈਆ ਕਰਵਾਉਣਾ।

## ਤਰੀਕਾ

ਚਲੋ ਇਹ ਸਮਝਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ ਕਿ ਸਾਨੂੰ ਕਿਹੜਾ ਤਰੀਕਾ ਅਪਣਾੳਣਾ ਚਾਹੀਦਾ ਹੈ। LLM ਜੋੜਨਾ ਆਸਾਨ ਲੱਗਦਾ ਹੈ, ਪਰ ਕੀ ਅਸੀਂ ਸੱਚ-ਮੁੱਚ ਇਹ ਕਰਾਂਗੇ?

ਇੱਥੇ ਹੈ ਕਿ ਕਲਾਇੰਟ ਸਰਵਰ ਨਾਲ ਕਿਵੇਂ ਸੰਚਾਰ ਕਰੇਗਾ:

1. ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰਨਾ।

2. ਸਮਰਥਨਾਵਾਂ, ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾ ਕੇ ਉਨ੍ਹਾਂ ਦਾ ਸਕੀਮਾ ਸੰਭਾਲਣਾ।

3. ਇੱਕ LLM ਸ਼ਾਮਿਲ ਕਰਨਾ ਅਤੇ ਸੰਭਾਲੀ ਗਈ ਸਮਰਥਨਾਵਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦਾ ਸਕੀਮਾ ਕਿਸੇ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ LLM ਨੂੰ ਪਾਸ ਕਰਨਾ ਜੋ ਉਹ ਸਮਝ ਸਕਦਾ ਹੈ।

4. ਉਪਭੋਗਤਾ ਦੇ ਪ੍ਰਾਂਪਟ ਨੂੰ LLM ਨੂੰ ਹਥਿਆਰਾਂ ਨਾਲ ਜੋੜ ਕੇ ਸੰਭਾਲਣਾ ਜੋ ਕਲਾਇੰਟ ਵੱਲੋਂ ਸੂਚੀਬੱਧ ਹਨ।

ਬਹੁਤ ਵਧੀਆ, ਹੁਣ ਸਾਨੂੰ ਉੱਚ ਸਤਰ 'ਤੇ ਸਮਝ ਆ ਗਈ ਹੈ ਕਿ ਅਸੀਂ ਇਸ ਨੂੰ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਆਓ ਇਸਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਅਭਿਆਸ ਵਿੱਚ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ।

## ਅਭਿਆਸ: LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਸਿੱਖਾਂਗੇ ਕਿ ਕਿਵੇਂ ਸਾਡੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਿਲ ਕਰਨਾ ਹੈ।

### GitHub Personal Access Token ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਕਤਾ

GitHub ਟੋਕਨ ਬਣਾਉਣਾ ਇੱਕ ਸਿੱਧਾ ਪਰਕਿਰਿਆ ਹੈ। ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਇਹ ਕਰ ਸਕਦੇ ਹੋ:

- GitHub ਸੈਟਿੰਗਾਂ 'ਤੇ ਜਾਓ – ਟੌਪ ਸੱਜੇ ਕੋਨੇ 'ਚ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ Settings ਚੁਣੋ।
- Developer Settings 'ਤੇ ਜਾਓ – ਹੇਠਾਂ ਸਕ੍ਰੋਲ ਕਰੋ ਅਤੇ Developer Settings 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
- Personal Access Tokens ਚੁਣੋ – Fine-grained tokens 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫਿਰ Generate new token।
- ਆਪਣਾ ਟੋਕਨ ਸੈੱਟ ਕਰੋ – ਇਕ ਹਵਾਲਾ ਪੱਤਰ ਸ਼ਾਮਿਲ ਕਰੋ, ਮਿਆਦ ਸੈੱਟ ਕਰੋ, ਅਤੇ ਲੋੜੀਂਦੇ scopes (ਅਧਿਕਾਰ) ਚੁਣੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ Models ਅਧਿਕਾਰ ਜਰੂਰੀ ਹੈ।
- ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਕਾਪੀ ਕਰੋ – Generate token 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫੌਰਨ ਹੀ ਕਾਪੀ ਕਰੋ, ਕਿਉਂਕਿ ਤੁਹਾਨੂੰ ਫਿਰ ਇਹ ਨਹੀਂ ਮਿਲੇਗਾ।

### -1- ਸਰਵਰ ਨਾਲ ਜੁੜੋ

ਆਓ ਪਹਿਲਾਂ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਈਏ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਦੀ ਵੈਧਤਾ ਲਈ ਜ਼ੋਡ ਨੂੰ ਆਯਾਤ ਕਰੋ

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

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ ਹੈ:

- ਜ਼ਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਸ ਬਣਾਈ ਜਿਸ ਵਿੱਚ ਦੋ ਮੈਂਬਰ ਹਨ, `client` ਅਤੇ `openai`, ਜੋ ਸਾਡੇ ਲਈ ਕਲਾਇੰਟ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਅਤੇ LLM ਨਾਲ ਸੰਵਾਦ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।
- ਆਪਣੀ LLM ਇੰਸਟੈਂਸ ਨੂੰ GitHub Models ਵਰਤਣ ਲਈ ਬਨਾਇਆ, ਜਿਸ ਵਿੱਚ `baseUrl` ਨੂੰ ਇੰਫਰੰਸ API ਵੱਲ ਸੈੱਟ ਕੀਤਾ ਗਿਆ।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਚਲਾਉਣ ਯੋਗ
    args=["run", "server.py"],  # ਵਿਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਆਰਗੁਮੈਂਟ
    env=None,  # ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ
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

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ:

- MCP ਲਈ ਜ਼ਰੂਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
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

ਤੁਹਾਨੂੰ ਪਹਿਲਾਂ ਆਪਣੇ `pom.xml` ਫਾਈਲ ਵਿੱਚ LangChain4j dependencies ਸ਼ਾਮਿਲ ਕਰਨੀ ਹੋਣਗੀਆਂ। ਇਹ dependencies MCP ਇੰਟੇਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI-ਕੰਪੈਟਿਬਲ MiniMax API ਨੂੰ ਯੋਗ ਬਣਾਉਣ ਲਈ ਹਨ:

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

ਆਪਣਾ MiniMax API key ਸੈੱਟ ਕਰੋ ਅਤੇ ਚਾਹੇ ਤਾਂ endpoint ਅਤੇ ਮਾਡਲ ਵੀ।
`MINIMAX_MODEL_ID` `MiniMax-M3` ਅਤੇ `MiniMax-M2.7` ਨੂੰ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ। ਜੇ
`OPENAI_BASE_URL` ਸੈੱਟ ਨਹੀਂ ਹੈ, ਤਾਂ `MINIMAX_REGION` `global_en` ਅਤੇ `cn_zh` ਦਾ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ਇਲਾਕੇ ਤੱਕ ਸੰਕੇਤਕ ਨੂੰ ਚੁਣਨ ਲਈ, `OPENAI_BASE_URL` ਨਾ ਸੈੱਟ ਕਰੋ:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ਫਿਰ ਆਪਣਾ ਜਾਵਾ ਕਲਾਇੰਟ ਕਲਾਸ ਬਣਾਓ:

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

        // ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ MCP ਸੰਚਾਰ ਤਿਆਰ ਕਰੋ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ਕਲਾਇਟ ਬਣਾਓ
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

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ ਹੈ:

- **LangChain4j dependencies ਸ਼ਾਮਿਲ ਕੀਤੀਆਂ**: MCP ਇੰਟੇਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI-ਕੰਪੈਟਿਬਲ MiniMax API ਲਈ ਲੋੜੀਂਦੀਆਂ
- **LangChain4j ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ**: MCP ਅਤੇ OpenAI ਚੈਟ ਮਾਡਲ ਫੰਕਸ਼ਨਾਲਿਟੀ ਲਈ
- **`ChatLanguageModel` ਬਣਾਇਆ**: MiniMax ਨਾਲ ਕਨਫਿਗਰ ਕੀਤਾ, ਤੁਹਾਡੇ MiniMax API key, endpoint, ਅਤੇ ਸਮਰਥਿਤ ਮਾਡਲ ID ਨਾਲ
- **HTTP ਟਰਾਂਸਪੋਰਟ ਸੈੱਟ ਕੀਤਾ**: Server-Sent Events (SSE) ਦੀ ਵਰਤੋਂ ਕਰਦਿਆਂ MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਲਈ
- **MCP ਕਲਾਇੰਟ ਬਣਾਇਆ**: ਜੋ ਸਰਵਰ ਨਾਲ ਸੰਵਾਦ ਦਾ ਗੁਆਚਾ ਸ਼ੀਲਤ ਕਰੇਗਾ
- **LangChain4j ਦਾ ਬਿਲਟ-ਇਨ MCP ਸਹਿਯੋਗ ਵਰਤਿਆ**: ਜੋ LLMs ਅਤੇ MCP ਸਰਵਰਾਂ ਦੇ ਵਿਚਕਾਰ ਇੰਟੇਗ੍ਰੇਸ਼ਨ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ

#### Rust

ਇਹ ਉਦਾਹਰਣ ਮੰਨਦੀ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Rust ਆਧਾਰਿਤ MCP ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਸਰਵਰ ਬਣਾਉਣ ਲਈ ਮੁੜ [01-first-server](../01-first-server/README.md) ਪਾਠ ਨੂੰ ਦੇਖੋ।

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਆਪਣਾ Rust MCP ਸਰਵਰ ਹੋਵੇ, ਤਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਸਰਵਰ ਨਾਲੋਂ ਵਾਪਰਦੀ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ। ਫਿਰ ਨਵਾਂ LLM ਕਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਹੁਕਮ ਚਲਾਓ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ਆਪਣੀ `Cargo.toml` ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ dependencies ਸ਼ਾਮਿਲ ਕਰੋ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ਲਈ ਕੋਈ ਅਧਿਕਾਰਿਕ Rust ਲਾਇਬ੍ਰੇਰੀ ਨਹੀਂ ਹੈ, ਪਰ `async-openai` crate ਇੱਕ [ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਸੰਭਾਲੀ ਜਾਣ ਵਾਲੀ ਲਾਇਬ੍ਰੇਰੀ](https://platform.openai.com/docs/libraries/rust#rust) ਹੈ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

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
    // ਪ੍ਰਾਰੰਭਿਕ ਸੁਨੇਹਾ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ਕਲਾਇੰਟ ਸੈੱਟਅੱਪ ਕਰੋ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ਕਲਾਇੰਟ ਸੈੱਟਅੱਪ ਕਰੋ
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

ਇਹ ਕੋਡ ਇੱਕ ਮੁਢਲਾ ਰੱਸਟ ਐਪਲੀਕੇਸ਼ਨ ਸੈੱਟ ਕਰਦਾ ਹੈ ਜੋ MCP ਸਰਵਰ ਅਤੇ GitHub Models ਨਾਲ LLM ਸੰਵਾਦ ਲਈ ਜੁੜੇਗਾ।

> [!IMPORTANT]
> ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ `OPENAI_API_KEY` ਐਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ ਦੇ ਵਿੱਚ ਤੁਹਾਡਾ GitHub ਟੋਕਨ ਹੈ।

ਵਧੀਆ, ਅਗਲੇ ਕਦਮ ਲਈ, ਆਓ ਸਰਵਰ ਉੱਤੇ ਸਮਰਥਨਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈਏ।

### -2- ਸਰਵਰ ਸਮਰਥਨਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ

ਹੁਣ ਅਸੀਂ ਸਰਵਰ ਨਾਲ ਜੁੜ ਕੇ ਉਸ ਦੀਆਂ ਸਮਰਥਨਾਵਾਂ ਬਾਰੇ ਪੁੱਛਾਂਗੇ:

#### Typescript

ਉਸੇ ਕਲਾਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਮੈਥਡ ਜੋੜੋ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ਸੋਧ ਅਜ਼ਮਾਇਸ਼ਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ
    const toolsResult = await this.client.listTools();
}
```

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ:

- ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ ਕੋਡ ਸ਼ਾਮਿਲ ਕੀਤਾ, `connectToServer`.
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਇਆ ਜੋ ਸਾਡੇ ਐਪ ਫਲੋ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਇਸ ਸਮੇਂ ਇਹ ਸਿਰਫ ਟੂਲ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ ਪਰ ਅਸੀਂ ਚਲਦੇ ਚਲਦੇ ਹੋਰ ਚੀਜ਼ਾਂ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ।

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

ਅਸੀਂ ਜੋ ਸ਼ਾਮਿਲ ਕੀਤਾ ਹੈ:

- ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਅਤੇ ਪ੍ਰਿੰਟ ਕੀਤਾ। ਟੂਲਾਂ ਲਈ ਅਸੀਂ `inputSchema` ਵੀ ਸੂਚੀਬੱਧ ਕੀਤਾ ਜੋ ਬਾਅਦ ਵਿੱਚ ਵਰਤਾਂਗੇ।

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

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ:

- MCP ਸਰਵਰ ਉੱਤੇ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ
- ਹਰ ਟੂਲ ਲਈ, ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਉਸ ਦਾ ਸਕੀਮਾ ਸੂਚੀਬੱਧ ਕੀਤਾ। ਇਹ ਅਗਲੇ ਪੜਾਅ ਵਿੱਚ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ।

#### Java

```java
// ਇੱਕ ਟੂਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ਟੂਲ ਪ੍ਰਦਾਤਾ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
// - MCP ਸਰਵਰ ਤੋਂ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾ ਰਿਹਾ ਹੈ
// - MCP ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ LangChain4j ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ
// - ਟੂਲ ਚਲਾਉਣਾ ਅਤੇ ਜਵਾਬਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
```

ਮੂਲ ਕੋਡ ਵਿੱਚ ਅਸੀਂ ਕੀ ਕੀਤਾ ਹੈ:


- ਇੱਕ `McpToolProvider` ਬਣਾਇਆ ਜੋ ਆਪਣੇ ਆਪ MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਟੂਲਾਂ ਦੀ ਖੋਜ ਅਤੇ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ
- ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ MCP ਟੂਲ ਸਕੀਮਾਂ ਅਤੇ LangChain4j ਦੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿਚ ਬਦਲਾਅ ਸੰਭਾਲਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੁਅਲ ਟੂਲ ਲਿਸਟਿੰਗ ਅਤੇ ਕਨਵਰਜ਼ਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਛੁਪਾ ਲੈਂਦਾ ਹੈ

#### ਰੱਸਟ

MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕਰਨਾ `list_tools` ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਨਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਵਿੱਚ, MCP ਕਲਾਇੰਟ ਸੈੱਟਅਪ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

```rust
// MCP ਟੂਲ ਲਿਸਟ ਪ੍ਰਾਪਤ ਕਰੋ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਨੂੰ LLM ਟੂਲਾਂ ਵਿੱਚ ਬਦਲੋ

ਸਰਵਰ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਦੀ ਲਿਸਟਿੰਗ ਦੇ ਬਾਅਦ ਅਗਲਾ ਕਦਮ ਉਹਨਾਂ ਨੂੰ ਇੱਕ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ ਹੈ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ। ਜਦੋਂ ਅਸੀਂ ਇਹ ਕਰ ਲੈਣਾਂ, ਤਾਂ ਅਸੀਂ ਇਹ ਸਮਰੱਥਾਵਾਂ LLM ਨੂੰ ਟੂਲ ਵਜੋਂ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦੇ ਹਾਂ।

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

1. MCP ਸਰਵਰ ਤੋਂ ਪ੍ਰਤਿਕਿਰਿਆ ਨੂੰ ਐਸੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ ਜੋ LLM ਇਸਤੇਮਾਲ ਕਰ ਸਕਦਾ ਹੈ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ਇਨਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ ਤੇ ਇੱਕ ਜ਼ੋਡ ਸਕੀਮਾ ਬਣਾਓ
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

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ MCP ਸਰਵਰ ਤੋਂ ਇਕ ਪ੍ਰਤਿਕਿਰਿਆ ਲੈਂਦਾ ਹੈ ਅਤੇ ਉਸ ਨੂੰ ਟੂਲ ਡਿਫੀਨੀਸ਼ਨ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ।

2. ਅਗਲਾ, `run` ਮੈਥਡ ਨੂੰ ਅੱਪਡੇਟ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਲਿਸਟ ਕਰ ਸਕੀਏ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ `run` ਮੈਥਡ ਨੂੰ ਅੱਪਡੇਟ ਕੀਤਾ ਹੈ ਜੋ ਨਤੀਜੇ ਤੋਂ ਮੈਪ ਕਰਦਾ ਹੈ ਅਤੇ ਹਰ ਐਂਟਰੀ ਲਈ `openAiToolAdapter` ਕਾਲ ਕਰਦਾ ਹੈ।

#### ਪਾਇਥਨ

1. ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤਾ ਕਨਵਰਟਰ ਫੰਕਸ਼ਨ ਬਣਾਈਏ

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

    ਉਪਰ ਦਿੱਤੇ ਫੰਕਸ਼ਨ `convert_to_llm_tools` ਵਿੱਚ ਅਸੀਂ MCP ਟੂਲ ਪ੍ਰਤਿਕਿਰਿਆ ਲੈਂਦੇ ਹਾਂ ਅਤੇ ਉਸਨੂੰ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਾਂ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ।

2. ਅਗਲਾ, ਆਪਣੇ ਕਲਾਇੰਟ ਕੋਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਲਈ ਅਪਡੇਟ ਕਰੀਏ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ਇੱਥੇ ਅਸੀਂ MCP ਟੂਲ ਪ੍ਰਤਿਕਿਰਿਆ ਨੂੰ LLM ਲਈ ਫੀਡ ਕਰਨ ਲਈ `convert_to_llm_tool` ਕਾਲ ਸ਼ਾਮਲ ਕਰ ਰਹੇ ਹਾਂ।

#### .NET

1. MCP ਟੂਲ ਪ੍ਰਤਿਕਿਰਿਆ ਨੂੰ ਐਸੇ ਕਿਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਕੋਡ ਸ਼ਾਮਲ ਕਰੀਏ ਜੋ LLM ਸਮਝ ਸਕੇ

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

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `ConvertFrom` ਫੰਕਸ਼ਨ ਬਣਾਇਆ ਜੋ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾ ਲੈਂਦਾ ਹੈ।
- ਫੰਕਸ਼ਨਲਿਟੀ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ ਜੋ ਇੱਕ FunctionDefinition ਬਣਾਉਂਦਾ ਹੈ ਜੋ ChatCompletionsDefinition ਦੇ ਨਾਲ ਪਾਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਦੂਜਾ ਐਸਾ ਹੈ ਜੋ LLM ਸਮਝਦਾ ਹੈ।

2. ਹੁਣ ਦੇਖੀਏ ਕਿ ਉਪਰ ਦਿੱਤੇ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਲਈ ਕੁਝ ਮੌਜੂਦਾ ਕੋਡ ਕਿਵੇਂ ਅਪਡੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ:

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
// ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੇਕਸ਼ਨ ਲਈ ਬੋਟ ਇੰਟਰਫੇਸ ਬਣਾਓ
public interface Bot {
    String chat(String prompt);
}

// LLM ਅਤੇ MCP ਟੂਲਜ਼ ਨਾਲ AI ਸੇਵਾ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੈਕਸ਼ਨਾਂ ਲਈ ਇੱਕ ਸਧਾਰਣ `Bot` ਇੰਟਰਫੇਸ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ
- LangChain4j ਦੇ `AiServices` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਤਾਂ ਜੋ LLM ਨੂੰ MCP ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਨਾਲ ਆਪਣ آپੇ ਬਾਈਂਡ ਕੀਤਾ ਜਾ ਸਕੇ
- ਫਰੇਮਵਰਕ автомੈਟਿਕ ਤੌਰ ਤੇ ਟੂਲ ਸਕੀਮਾ ਬਦਲਾਅ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਦਾ ਸੰਭਾਲ ਕਰਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੁਅਲ ਟੂਲ ਬਦਲਾਅ ਨੂੰ ਮਿਟਾ ਦਿੰਦਾ ਹੈ - LangChain4j MCP ਟੂਲਾਂ ਨੂੰ LLM-ਅਨੁਕੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਾਰੀ ਜਟਿਲਤਾ ਸੰਭਾਲਦਾ ਹੈ

#### ਰੱਸਟ

MCP ਟੂਲ ਦੀ ਪ੍ਰਤਿਕਿਰਿਆ ਨੂੰ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ, ਅਸੀਂ ਇੱਕ ਹੈਲਪਰ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਟੂਲਾਂ ਦੀ ਲਿਸਟਿੰਗ ਨੂੰ ਫਾਰਮੈਟ ਕਰਦਾ ਹੈ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਆਪਣੇ `main.rs` ਫਾਇਲ ਵਿੱਚ `main` ਫੰਕਸ਼ਨ ਹੇਠਾਂ ਸ਼ਾਮਲ ਕਰੋ। ਇਹ LLM ਨੂੰ ਬੇਨਤੀ ਕਰਨ ਸਮੇਂ ਕਾਲ ਕੀਤਾ ਜਾਵੇਗਾ:

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

ਵਧੀਆ, ਅਸੀਂ ਕਿਸੇ ਵੀ ਉਪਭੋਗਤਾ ਬੇਨਤੀ ਨੂੰ ਹੈਂਡਲ ਕਰਨ ਲਈ ਤਿਆਰ ਹਾਂ, ਤਾਂ ਆਓ ਹੁਣ ਉਸਨੂੰ ਸੰਭਾਲੀਏ।

### -4- ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ ਬੇਨਤੀ ਹੈਂਡਲ ਕਰੋ

ਇਸ ਹਿੱਸੇ ਵਿੱਚ ਅਸੀਂ ਉਪਭੋਗਤਾ ਦੀਆਂ ਬੇਨਤੀਆਂ ਹੈਂਡਲ ਕਰਾਂਗੇ।

#### ਟਾਈਪਸਕ੍ਰਿਪਟ

1. ਇੱਕ ਮੈਥਡ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਸਾਡੇ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ:

    ```typescript
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
        // ਕਰਨ ਦੀ ਲੋੜ ਹੈ

        }
    }
    ```

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਇੱਕ ਮੈਥਡ `callTools` ਸ਼ਾਮਲ ਕੀਤਾ।
    - ਇਹ ਮੈਥਡ LLM ਪ੍ਰਤਿਕਿਰਿਆ ਲੈਂਦਾ ਹੈ ਅਤੇ ਜਾਂਚਦਾ ਹੈ ਕਿ ਕਿਹੜੇ ਟੂਲ ਕਾਲ ਕੀਤੇ ਗਏ ਹਨ, ਜੇ ਹੋਣ ਤਾਂ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ਯੰਤਰ ਨੂੰ ਕਾਲ ਕਰੋ
        }
        ```

    - ਟੂਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਜੇ LLM ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਇਸ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ:

        ```typescript
        // 2. ਸਰਵਰ ਦੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ਨਤੀਜੇ ਨਾਲ ਕੁਝ ਕਰੋ
        // ਕਰਨ ਲਈ
        ```

2. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਅਤੇ `callTools` ਕਾਲ ਸ਼ਾਮਲ ਹੋਵੇ:

    ```typescript

    // 1. LLM ਲਈ ਇਨਪੁਟ ਵਜੋਂ ਸੁਨੇਹੇ ਬਣਾਓ
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

    // 3. LLM ਦੇ ਜਵਾਬ ਨੂੰ ਦੇਖੋ, ਹਰ ਵਿਕਲਪ ਲਈ ਵੇਖੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲਾਂ ਹਨ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ਵਧੀਆ, ਆਓ ਪੂਰਾ ਕੋਡ ਲਿਸਟ ਕਰੀਏ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ ਜ਼ੋਡ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ਭਵਿੱਖ ਵਿੱਚ ਇਸ URL ਨੂੰ ਬਦਲਣ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ: https://models.github.ai/inference
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
          // ਇਨਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਜ਼ੋਡ ਸਕੀਮਾ ਬਣਾਓ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ਪ੍ਰਕਾਰ ਨੂੰ ਖੁਲ੍ਹ ਕੇ "function" ਸੈੱਟ ਕਰੋ
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
          // ਕਰਨ ਵਾਲਾ ਕੰਮ
    
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
    
        // 3. LLM ਜਵਾਬ 'ਚੋਂ ਹਰ ਚੋਣ ਲਈ ਜਾਓ, ਜਾਂਚ ਕਰੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
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

#### ਪਾਇਥਨ

1. LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਕੁਝ ਇੰਪੋਰਟ ਸ਼ਾਮਲ ਕਰੀਏ

    ```python
    # ਐਲਐਲਐਮ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. ਅਗਲਾ, ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੀਏ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰੇਗਾ:

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
            # ਵਿਕਲਪੀ ਪੈਰਾਮੀਟਰ
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

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਉਹ ਸਾਰੇ ਫੰਕਸ਼ਨ ਜੋ MCP ਸਰਵਰ 'ਤੇ ਮਿਲੇ ਅਤੇ ਬਦਲੇ ਗਏ, LLM ਨੂੰ ਦਿੱਤੇ।
    - ਫਿਰ ਅਸੀਂ ਇਹਨਾਂ ਫੰਕਸ਼ਨਾਂ ਨਾਲ LLM ਨੂੰ ਕਾਲ ਕੀਤਾ।
    - ਬਾਅਦ ਵਿੱਚ ਅਸੀਂ ਨਤੀਜੇ ਦੀ ਜਾਂਚ ਕਰਦੇ ਹਾਂ ਦੇਖਣ ਲਈ ਕਿ ਕਿਹੜੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਜ਼ਰੂਰਤ ਹੈ, ਜੇ ਕੋਈ ਹੋਣ।
    - ਅੰਤ ਵਿੱਚ, ਅਸੀਂ ਫੰਕਸ਼ਨਾਂ ਦੀ ਇੱਕ ਲੜੀ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਭੇਜਦੇ ਹਾਂ।

3. ਅਖੀਰਲਾ ਕਦਮ, ਆਪਣੇ ਮੁੱਖ ਕੋਡ ਨੂੰ ਅੱਪਡੇਟ ਕਰੀਏ:

    ```python
    prompt = "Add 2 to 20"

    # LLM ਨੂੰ ਪੁੱਛੋ ਕਿ ਕਿਹੜੇ ਸਾਧਨ ਸਾਰੇ ਲਈ ਹਨ, ਜੇ ਕੋਈ ਹੋਣ
    functions_to_call = call_llm(prompt, functions)

    # ਸੁਝਾਏ ਗਏ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰੋ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ਹੋ ਗਿਆ, ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਟੂਲ ਨੂੰ `call_tool` ਰਾਹੀਂ ਕਾਲ ਕਰਦੇ ਹਾਂ ਉਨ੍ਹਾਂ ਫੰਕਸ਼ਨਾਂ ਦਾ ਜੋ LLM ਨੇ ਸੋਚਿਆ ਕਿ ਸਾਨੂੰ ਸਾਡੇ ਪ੍ਰੰਪਟ ਦੇ ਅਧਾਰ ਤੇ ਕਾਲ ਕਰਣੇ ਚਾਹੀਦੇ ਹਨ।
    - MCP ਸਰਵਰ ਦੇ ਉਤਰ ਦਾ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

#### .NET

1. LLM ਪ੍ਰੰਪਟ ਬੇਨਤੀ ਕਰਨ ਲਈ ਕੁਝ ਕੋਡ ਦਿਖਾਈਏ:

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

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕੀਤੇ, `var tools = await GetMcpTools()`.
    - ਇਕ ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ `userMessage` ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ।
    - ਮਾਡਲ ਅਤੇ ਟੂਲ ਦੱਸਦੇ ਹੋਏ ਅਪਸ਼ਨਜ਼ ਓਬਜੈਕਟ ਬਣਾਇਆ।
    - LLM ਵੱਲ ਬੇਨਤੀ ਕੀਤੀ।

2. ਆਖਰੀ ਕਦਮ, ਦੇਖੀਏ ਕਿ LLM ਸੋਚਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਕੋਈ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ:

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

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਦੀ ਲਿਸਟ ਵਿੱਚ ਲੂਪ ਕੀਤਾ।
    - ਹਰ ਟੂਲ ਕਾਲ ਲਈ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਨੂੰ ਪਾਰਸ ਕਰਕੇ MCP ਕਲਾਇੰਟ ਨਾਲ MCP ਸਰਵਰ 'ਤੇ ਟੂਲ ਕਾਲ ਕੀਤਾ। ਆਖਿਰ ਵਿੱਚ ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕੀਤੇ।

ਪੂਰਾ ਕੋਡ ਇੱਥੇ:

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

#### ਜਾਵਾ

```java
try {
    // ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਚਲਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ
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

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਧਾਰਣ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰੰਪਟਾਂ ਨਾਲ MCP ਸਰਵਰ ਟੂਲਾਂ ਨੂੰ ਇੰਟਰੈਕਟ ਕੀਤਾ
- LangChain4j ਫਰੇਮਵਰਕ ਆਪੇ ਬਾਰੇ ਸੰਭਾਲਦਾ ਹੈ:
  - ਜਦੋਂ ਲੋੜ ਹੋਵੇ, ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟਾਂ ਨੂੰ ਟੂਲ ਕਾਲਾਂ ਵਿੱਚ ਬਦਲਣਾ
  - LLM ਦੇ ਫੈਸਲੇ ਅਨੁਸਾਰ ਉਚਿਤ MCP ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ
  - LLM ਤੇ MCP ਸਰਵਰ ਦਰਮਿਆਨ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
- `bot.chat()` ਮੈਥਡ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰਤਿਕਿਰਿਆਵਾਂ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ MCP ਟੂਲ ਪ੍ਰਚਾਲਨ ਦੇ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ
- ਇਹ ਤਰੀਕਾ ਇੱਕ ਬਿਨਾਂ ਰੁਕਾਵਟ ਵਾਲਾ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ ਅਧੀਨ MCP ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਬਾਰੇ ਜਾਣਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ

ਪੂਰਾ ਕੋਡ ਉਦਾਹਰਨ:

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

#### ਰੱਸਟ

ਇੱਥੇ ਜ਼ਿਆਦਾਤਰ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਉਪਭੋਗਤਾ ਪ੍ਰੰਪਟ ਨਾਲ LLM ਨੂੰ ਕਾਲ ਕਰਾਂਗੇ, ਫਿਰ ਜਵਾਬ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਕੇ ਦੇਖਾਂਗੇ ਕਿ ਕੋਈ ਟੂਲ ਕਾਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ ਕਿ ਨਹੀਂ। ਜੇ ਹਾਂ, ਤਾਂ ਉਹ ਟੂਲ ਕਾਲ ਕਰਾਂਗੇ ਅਤੇ ਸੰਵਾਦ ਜਾਰੀ ਰੱਖਾਂਗੇ ਜਦ ਤਕ ਹੋਰ ਟੂਲ ਕਾਲਜ਼ ਦੀ ਲੋੜ ਨਾ ਰਹਿਣ ਅਤੇ ਸਾਨੂੰ ਅਖੀਰਲਾ ਜਵਾਬ ਮਿਲ ਜਾਵੇ।


ਅਸੀਂ LLM ਨੂੰ ਕਈ ਵਾਰੀ ਕਾਲ ਕਰਨ ਵਾਲੇ ਹਾਂ, ਇਸ ਲਈ ਆਓ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਪਰਿਭਾਸ਼ਿਤ ਕਰੀਏ ਜੋ LLM ਕਾਲ ਨੂੰ ਸੰਭਾਲੇਗਾ। ਆਪਣੀ `main.rs` ਫਾਇਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ:

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

ਇਹ ਫੰਕਸ਼ਨ LLM ਕਲਾਇੰਟ, ਸੁਨੇਹਿਆਂ ਦੀ ਲਿਸਟ (ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਪ੍ਰੌਂਪਟ ਸ਼ਾਮਲ ਹੈ), MCP ਸਰਵਰ ਤੋਂ ਟੂਲਸ ਲੈਂਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਵਾਪਸ ਕਰਦਾ ਹੈ।

LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਵਿੱਚ `choices` ਦੀ ਲੜੀ ਹੋਵੇਗੀ। ਅਸੀਂ ਨਤੀਜੇ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਨੀ ਹੋਵੇਗੀ ਤਾਂ ਕਿ ਵੇਖਿਆ ਜਾ ਸਕੇ ਕਿ ਕੋਈ `tool_calls` ਹਨ ਜਾਂ ਨਹੀਂ। ਇਹ ਸਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ LLM ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਟੂਲ ਨੂੰ ਉਹਦੇ ਅਰਗੁਮੈਂਟਸ ਨਾਲ ਕਾਲ ਕਰਨਾ ਚਾਹੁੰਦਾ ਹੈ। ਆਪਣੀ `main.rs` ਫਾਇਲ ਦੇ ਨੀਵੇਂ ਹਿੱਸੇ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ ਜੋ LLM ਪ੍ਰਤੀਕਿਰਿਆ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੇ:

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

    // ਸਮੱਗਰੀ ਉਪਲਬਧ ਹੋਣ ਤੇ ਪ੍ਰਿੰਟ ਕਰੋ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲੋ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ਸਹਾਇਕ ਸੁਨੇਹਾ ਸ਼ਾਮਲ ਕਰੋ

        // ਹਰ ਟੂਲ ਕਾਲ ਨੂੰ ਚਲਾਓ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਟੂਲ ਪਰਿਣਾਮ ਸ਼ਾਮਲ ਕਰੋ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ਟੂਲ ਪਰਿਣਾਮਾਂ ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖੋ
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

ਜੇਕਰ `tool_calls` ਹਨ, ਤਾਂ ਇਹ ਟੂਲ ਜਾਣਕਾਰੀ ਨਿਕਾਲਦਾ ਹੈ, MCP ਸਰਵਰ ਨੂੰ ਟੂਲ ਕਾਲ ਦੀ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ ਅਤੇ ਨਤੀਜੇ ਗੱਲਬਾਤ ਦੇ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰ ਦਿੰਦਾ ਹੈ। ਫਿਰ ਇਹ LLM ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹੇ ਸਹਾਇਕ ਦੀ ਜਵਾਬ ਅਤੇ ਟੂਲ ਕਾਲ ਦੇ ਨਤੀਜਿਆਂ ਨਾਲ ਅਪਡੇਟ ਹੁੰਦੇ ਹਨ।

LLM ਤੋਂ MCP ਕਾਲਾਂ ਲਈ ਪ੍ਰਾਪਤ ਟੂਲ ਕਾਲ ਜਾਣਕਾਰੀ ਨੂੰ ਨਿਕਾਲਣ ਲਈ ਅਸੀਂ ਹੋਰ ਇੱਕ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਕਾਲ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਸਾਰਾ ਡੇਟਾ ਨਿਕਾਲੇਗਾ। ਆਪਣੀ `main.rs` ਫਾਇਲ ਦੇ ਨੀਵੇਂ ਹਿੱਸੇ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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

ਸਾਰੇ ਹਿੱਸੇ ਜੁੜ ਜਾਣ ਤੋਂ ਬਾਅਦ, ਹੁਣ ਅਸੀਂ ਮੁੱਢਲੇ ਯੂਜ਼ਰ ਪ੍ਰੌਂਪਟ ਨੂੰ ਸੰਭਾਲ ਸਕਦੇ ਹਾਂ ਅਤੇ LLM ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਨੂੰ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰਕੇ ਅਪਡੇਟ ਕਰੋ:

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

ਇਹ ਮੁੱਢਲੇ ਯੂਜ਼ਰ ਪ੍ਰੌਂਪਟ ਨਾਲ LLM ਨੂੰ ਕੂਐਰੀ ਕਰੇਗਾ ਜੋ ਦੋ ਨੰਬਰਾਂ ਦੇ ਜੋੜ ਲਈ ਪੁੱਛਦਾ ਹੈ, ਅਤੇ ਜਵਾਬ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਕੇ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਡਾਇਨਾਮਿਕ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲੇਗਾ।

ਬਹੁਤ ਵਧੀਆ, ਤੁਸੀਂ ਕਰ ਲਿਆ!

## ਅਸਾਈਨਮੈਂਟ

ਅਭਿਆਸ ਤੋਂ ਕੋਡ ਲਓ ਅਤੇ ਕੁਝ ਹੋਰ ਟੂਲਸ ਦੇ ਨਾਲ ਸਰਵਰ ਦਾ ਨਿਰਮਾਣ ਕਰੋ। ਫਿਰ ਇੱਕ LLM ਵਾਲਾ ਕਲਾਇੰਟ ਬਣਾਓ, ਜਿਵੇਂ ਅਭਿਆਸ ਵਿੱਚ ਹੈ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰੌਂਪਟਾਂ ਨਾਲ ਇਸਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਸਮੂਹ ਸਰਵਰ ਟੂਲਜ਼ ਡਾਇਨਾਮਿਕ ਤਰੀਕੇ ਨਾਲ ਕਾਲ ਹੋ ਰਹੇ ਹਨ। ਇਹ ਕਿਸਮ ਦਾ ਕਲਾਇੰਟ ਨਿਰਮਾਣ ਅੰਤ ਉਪਭੋਗਤਾ ਲਈ ਸ਼ਾਨਦਾਰ ਵਰਤੋਂਕਾਰ ਅਨੁਭਵ ਦੇਵੇਗਾ ਕਿਉਂਕਿ ਉਹ ਪ੍ਰੌਂਪਟਾਂ ਨਾਲ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ, ਬਜਾਏ ਕਿ ਸਹੀ ਕਲਾਇੰਟ ਕਮਾਂਡਾਂ ਦੇ, ਅਤੇ ਕਿਸੇ ਵੀ MCP ਸਰਵਰ ਨੂੰ ਕਾਲ ਕਰਨ ਤੋਂ ਬੇਖਬਰ ਰਹਿੰਦੇ ਹਨ।

## ਹੱਲ

[Solution](./solution/README.md)

## ਮੁੱਖ ਮੁੱਦੇ

- ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਲ ਕਰਨ ਨਾਲ ਯੂਜ਼ਰਾਂ ਲਈ MCP ਸਰਵਰਾਂ ਨਾਲ ਸੰਵਾਦ ਕਰਨ ਦਾ ਇੱਕ ਬਿਹਤਰ ਤਰੀਕਾ ਮਿਲਦਾ ਹੈ।
- ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਦੀ ਪ੍ਰਤੀਕਿਰਿਆ ਨੂੰ ਕੁਝ ਐਸਾ ਬਦਲਣਾ ਪਵੇਗਾ ਜੋ LLM ਨੂੰ ਸਮਝ ਆ ਸਕੇ।

## ਨਮੂਨੇ

- [ਜਾਵਾ ਕੈਲਕੁਲੇਟਰ](../samples/java/calculator/README.md)
- [.Net ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/javascript/README.md)
- [ਟਾਈਪਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/typescript/README.md)
- [ਪਾਈਥਨ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/python)
- [ਰਸਟ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/rust)

## ਵਾਧੂ ਸਰੋਤ

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [Visual Studio Code ਦੀ ਵਰਤੋਂ ਨਾਲ ਸਰਵਰ ਦਾ ਉਪਭੋਗ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->