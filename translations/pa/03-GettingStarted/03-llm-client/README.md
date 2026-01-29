# LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਵੇਖਿਆ ਹੈ ਕਿ ਸਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਕਿਵੇਂ ਬਣਾਉਣੇ ਹਨ। ਕਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਖੁੱਲ੍ਹ ਕੇ ਉਸਦੇ ਟੂਲ, ਸਰੋਤ ਅਤੇ ਪ੍ਰਾਂਪਟ ਸੂਚੀਬੱਧ ਕਰਨ ਲਈ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ। ਪਰ ਇਹ ਬਹੁਤ ਪ੍ਰਯੋਗਕਾਰੀ ਤਰੀਕਾ ਨਹੀਂ ਹੈ। ਤੁਹਾਡਾ ਯੂਜ਼ਰ ਏਜੈਂਟਿਕ ਯੁੱਗ ਵਿੱਚ ਰਹਿੰਦਾ ਹੈ ਅਤੇ ਉਮੀਦ ਕਰਦਾ ਹੈ ਕਿ ਉਹ ਪ੍ਰਾਂਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਤੇ LLM ਨਾਲ ਸੰਚਾਰ ਕਰਕੇ ਇਹ ਕਰੇਗਾ। ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਲਈ ਇਹ ਮਾਇਨੇ ਨਹੀਂ ਰੱਖਦਾ ਕਿ ਤੁਸੀਂ ਆਪਣੀਆਂ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ MCP ਵਰਤਦੇ ਹੋ ਜਾਂ ਨਹੀਂ, ਪਰ ਉਹ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਉਮੀਦ ਕਰਦਾ ਹੈ। ਤਾਂ ਅਸੀਂ ਇਹ ਕਿਵੇਂ ਹੱਲ ਕਰੀਏ? ਹੱਲ ਇਹ ਹੈ ਕਿ ਕਲਾਇੰਟ ਵਿੱਚ ਇੱਕ LLM ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਵੇ।

## ਓਵਰਵਿਊ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ ਇੱਕ LLM ਸ਼ਾਮਲ ਕਰਨ 'ਤੇ ਧਿਆਨ ਦੇਵਾਂਗੇ ਅਤੇ ਵੇਖਾਂਗੇ ਕਿ ਇਹ ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਲਈ ਕਿਵੇਂ ਬਿਹਤਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਇੱਕ LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ।
- MCP ਸਰਵਰ ਨਾਲ LLM ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਬਿਨਾਂ ਰੁਕਾਵਟ ਇੰਟਰੈਕਟ ਕਰਨਾ।
- ਕਲਾਇੰਟ ਪਾਸੇ ਬਿਹਤਰ ਅੰਤਮ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਨਾ।

## ਤਰੀਕਾ

ਆਓ ਸਮਝੀਏ ਕਿ ਸਾਨੂੰ ਕਿਹੜਾ ਤਰੀਕਾ ਅਪਣਾਉਣਾ ਹੈ। ਇੱਕ LLM ਸ਼ਾਮਲ ਕਰਨਾ ਆਸਾਨ ਲੱਗਦਾ ਹੈ, ਪਰ ਕੀ ਅਸੀਂ ਇਹ ਅਸਲ ਵਿੱਚ ਕਰਾਂਗੇ?

ਇਹ ਹੈ ਕਲਾਇੰਟ ਦਾ ਸਰਵਰ ਨਾਲ ਇੰਟਰੈਕਸ਼ਨ ਕਰਨ ਦਾ ਤਰੀਕਾ:

1. ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰੋ।

1. ਸਮਰੱਥਾਵਾਂ, ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ ਅਤੇ ਉਨ੍ਹਾਂ ਦਾ ਸਕੀਮਾ ਸੇਵ ਕਰੋ।

1. ਇੱਕ LLM ਸ਼ਾਮਲ ਕਰੋ ਅਤੇ ਸੇਵ ਕੀਤੀਆਂ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦਾ ਸਕੀਮਾ LLM ਨੂੰ ਸਮਝ ਆਉਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਪਾਸ ਕਰੋ।

1. ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨੂੰ LLM ਨੂੰ ਪਾਸ ਕਰਕੇ ਅਤੇ ਕਲਾਇੰਟ ਵੱਲੋਂ ਸੂਚੀਬੱਧ ਟੂਲਾਂ ਨਾਲ ਮਿਲਾ ਕੇ ਹੈਂਡਲ ਕਰੋ।

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਉੱਚ ਸਤਰ 'ਤੇ ਸਮਝ ਗਏ ਹਾਂ ਕਿ ਅਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਆਓ ਹੇਠਾਂ ਦਿੱਤੇ ਅਭਿਆਸ ਵਿੱਚ ਇਸਨੂੰ ਅਜ਼ਮਾਈਏ।

## ਅਭਿਆਸ: LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ ਇੱਕ LLM ਸ਼ਾਮਲ ਕਰਨਾ ਸਿੱਖਾਂਗੇ।

### GitHub Personal Access Token ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਕਤਾ

GitHub ਟੋਕਨ ਬਣਾਉਣਾ ਸਿੱਧਾ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

- GitHub ਸੈਟਿੰਗਜ਼ 'ਤੇ ਜਾਓ – ਸਿਖਰਲੇ ਸੱਜੇ ਕੋਨੇ ਵਿੱਚ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਸੈਟਿੰਗਜ਼ ਚੁਣੋ।
- Developer Settings 'ਤੇ ਜਾਓ – ਹੇਠਾਂ ਸਕ੍ਰੋਲ ਕਰੋ ਅਤੇ Developer Settings 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
- Personal Access Tokens ਚੁਣੋ – Fine-grained tokens 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫਿਰ Generate new token 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
- ਆਪਣਾ ਟੋਕਨ ਸੰਰਚਿਤ ਕਰੋ – ਸੰਦਰਭ ਲਈ ਇੱਕ ਨੋਟ ਸ਼ਾਮਲ ਕਰੋ, ਮਿਆਦ ਨਿਰਧਾਰਤ ਕਰੋ, ਅਤੇ ਜ਼ਰੂਰੀ ਸਕੋਪ (ਅਧਿਕਾਰ) ਚੁਣੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ Models ਅਧਿਕਾਰ ਸ਼ਾਮਲ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।
- ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਕਾਪੀ ਕਰੋ – Generate token 'ਤੇ ਕਲਿੱਕ ਕਰੋ, ਅਤੇ ਤੁਰੰਤ ਕਾਪੀ ਕਰ ਲਵੋ, ਕਿਉਂਕਿ ਤੁਸੀਂ ਇਸਨੂੰ ਮੁੜ ਨਹੀਂ ਦੇਖ ਸਕੋਗੇ।

### -1- ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰੋ

ਆਓ ਪਹਿਲਾਂ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਈਏ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ zod ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ

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

- ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਸ ਬਣਾਈ ਜਿਸ ਵਿੱਚ ਦੋ ਮੈਂਬਰ ਹਨ, `client` ਅਤੇ `openai`, ਜੋ ਸਾਨੂੰ ਕਲਾਇੰਟ ਨੂੰ ਮੈਨੇਜ ਕਰਨ ਅਤੇ LLM ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨਗੇ।
- ਆਪਣੇ LLM ਇੰਸਟੈਂਸ ਨੂੰ GitHub Models ਵਰਤਣ ਲਈ ਸੰਰਚਿਤ ਕੀਤਾ, `baseUrl` ਨੂੰ inference API ਵੱਲ ਸੈੱਟ ਕਰਕੇ।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਚਲਾਉਣ ਯੋਗ
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

- MCP ਲਈ ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਇਆ

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

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `pom.xml` ਫਾਇਲ ਵਿੱਚ LangChain4j ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕਰਨੀਆਂ ਪੈਣਗੀਆਂ। MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ GitHub Models ਸਹਾਇਤਾ ਲਈ ਇਹ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕਰੋ:

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // LLM ਨੂੰ GitHub ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਲਈ ਸੰਰਚਿਤ ਕਰੋ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ MCP ਟ੍ਰਾਂਸਪੋਰਟ ਬਣਾਓ
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
}
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- **LangChain4j ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕੀਤੀਆਂ**: MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ, OpenAI ਅਧਿਕਾਰਤ ਕਲਾਇੰਟ, ਅਤੇ GitHub Models ਸਹਾਇਤਾ ਲਈ
- **LangChain4j ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ**: MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI ਚੈਟ ਮਾਡਲ ਫੰਕਸ਼ਨਾਲਿਟੀ ਲਈ
- **`ChatLanguageModel` ਬਣਾਇਆ**: GitHub Models ਨੂੰ ਤੁਹਾਡੇ GitHub ਟੋਕਨ ਨਾਲ ਵਰਤਣ ਲਈ ਸੰਰਚਿਤ
- **HTTP ਟ੍ਰਾਂਸਪੋਰਟ ਸੈੱਟ ਕੀਤਾ**: Server-Sent Events (SSE) ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ
- **MCP ਕਲਾਇੰਟ ਬਣਾਇਆ**: ਜੋ ਸਰਵਰ ਨਾਲ ਸੰਚਾਰ ਸੰਭਾਲੇਗਾ
- **LangChain4j ਦੀ ਬਿਲਟ-ਇਨ MCP ਸਹਾਇਤਾ ਵਰਤੀ**: ਜੋ LLMs ਅਤੇ MCP ਸਰਵਰਾਂ ਵਿਚਕਾਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਸੌਖਾ ਬਣਾਉਂਦੀ ਹੈ

#### Rust

ਇਹ ਉਦਾਹਰਨ ਮੰਨਦੀ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Rust ਅਧਾਰਿਤ MCP ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਸਰਵਰ ਬਣਾਉਣ ਲਈ [01-first-server](../01-first-server/README.md) ਪਾਠ ਨੂੰ ਵੇਖੋ।

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ Rust MCP ਸਰਵਰ ਹੋਵੇ, ਇੱਕ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਸਰਵਰ ਵਾਲੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ। ਫਿਰ ਨਵਾਂ LLM ਕਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ਆਪਣੇ `Cargo.toml` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਲ ਕਰੋ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ਲਈ ਕੋਈ ਅਧਿਕਾਰਤ Rust ਲਾਇਬ੍ਰੇਰੀ ਨਹੀਂ ਹੈ, ਪਰ `async-openai` crate ਇੱਕ [ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਸੰਭਾਲੀ ਜਾਣ ਵਾਲੀ ਲਾਇਬ੍ਰੇਰੀ](https://platform.openai.com/docs/libraries/rust#rust) ਹੈ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

`src/main.rs` ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਇਸਦਾ ਸਮੱਗਰੀ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਬਦਲੋ:

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
    // ਸ਼ੁਰੂਆਤੀ ਸੁਨੇਹਾ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ਕਲਾਇੰਟ ਸੈੱਟਅਪ ਕਰੋ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ਕਲਾਇੰਟ ਸੈੱਟਅਪ ਕਰੋ
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

ਇਹ ਕੋਡ ਇੱਕ ਬੁਨਿਆਦੀ Rust ਐਪਲੀਕੇਸ਼ਨ ਸੈੱਟਅਪ ਕਰਦਾ ਹੈ ਜੋ MCP ਸਰਵਰ ਅਤੇ GitHub Models ਨਾਲ LLM ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਕਨੈਕਟ ਕਰੇਗਾ।

> [!IMPORTANT]
> ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ GitHub ਟੋਕਨ ਨਾਲ `OPENAI_API_KEY` ਵਾਤਾਵਰਣ ਚਲਕ (environment variable) ਸੈੱਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

ਵਧੀਆ, ਅਗਲੇ ਕਦਮ ਲਈ, ਆਓ ਸਰਵਰ 'ਤੇ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈਏ।

### -2- ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ

ਹੁਣ ਅਸੀਂ ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਾਂਗੇ ਅਤੇ ਉਸ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਮੰਗਾਂਗੇ:

#### Typescript

ਉਸੇ ਕਲਾਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਮੈਥਡ ਸ਼ਾਮਲ ਕਰੋ:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ਸੰਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ
    const toolsResult = await this.client.listTools();
}
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ ਕੋਡ ਸ਼ਾਮਲ ਕੀਤਾ, `connectToServer`।
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਇਆ ਜੋ ਐਪ ਫਲੋ ਸੰਭਾਲਦਾ ਹੈ। ਹੁਣ ਤੱਕ ਇਹ ਸਿਰਫ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦਾ ਹੈ ਪਰ ਅਸੀਂ ਇਸ ਵਿੱਚ ਜਲਦੀ ਹੋਰ ਸ਼ਾਮਲ ਕਰਾਂਗੇ।

#### Python

```python
# ਉਪਲਬਧ ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ਉਪਲਬਧ ਸੰਦਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ਇਹ ਹੈ ਜੋ ਅਸੀਂ ਸ਼ਾਮਲ ਕੀਤਾ:

- ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਅਤੇ ਪ੍ਰਿੰਟ ਕੀਤੀ। ਟੂਲਾਂ ਲਈ ਅਸੀਂ `inputSchema` ਵੀ ਸੂਚੀਬੱਧ ਕੀਤਾ ਜੋ ਅਸੀਂ ਬਾਅਦ ਵਿੱਚ ਵਰਤਾਂਗੇ।

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ 'ਤੇ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ
- ਹਰ ਟੂਲ ਲਈ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਉਸਦਾ ਸਕੀਮਾ ਸੂਚੀਬੱਧ ਕੀਤਾ। ਇਹ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਵੇਗਾ।

#### Java

```java
// ਇੱਕ ਟੂਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ਟੂਲ ਪ੍ਰਦਾਤਾ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
// - MCP ਸਰਵਰ ਤੋਂ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ
// - MCP ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ LangChain4j ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ
// - ਟੂਲ ਚਲਾਉਣ ਅਤੇ ਜਵਾਬਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `McpToolProvider` ਬਣਾਇਆ ਜੋ MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਆਪਣੇ ਆਪ ਖੋਜਦਾ ਅਤੇ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ
- ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ MCP ਟੂਲ ਸਕੀਮਾਂ ਅਤੇ LangChain4j ਦੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿਚਕਾਰ ਕਨਵਰਜ਼ਨ ਅੰਦਰੂਨੀ ਤੌਰ 'ਤੇ ਸੰਭਾਲਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੂਅਲ ਟੂਲ ਸੂਚੀਬੱਧ ਕਰਨ ਅਤੇ ਕਨਵਰਜ਼ਨ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਛੁਪਾ ਦਿੰਦਾ ਹੈ

#### Rust

MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ `list_tools` ਮੈਥਡ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਵਿੱਚ, MCP ਕਲਾਇੰਟ ਸੈੱਟਅਪ ਕਰਨ ਤੋਂ ਬਾਅਦ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

```rust
// MCP ਟੂਲ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਨੂੰ LLM ਟੂਲਾਂ ਵਿੱਚ ਬਦਲੋ

ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਅਗਲਾ ਕਦਮ ਇਹ ਹੈ ਕਿ ਉਨ੍ਹਾਂ ਨੂੰ LLM ਲਈ ਸਮਝਣਯੋਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾਵੇ। ਜਦੋਂ ਅਸੀਂ ਇਹ ਕਰ ਲੈਂਦੇ ਹਾਂ, ਤਾਂ ਅਸੀਂ ਇਹ ਸਮਰੱਥਾਵਾਂ ਆਪਣੇ LLM ਨੂੰ ਟੂਲਾਂ ਵਜੋਂ ਦੇ ਸਕਦੇ ਹਾਂ।

#### TypeScript

1. MCP ਸਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਵਰਤਣਯੋਗ ਟੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ਇਨਪੁਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਜੋਡ ਸਕੀਮਾ ਬਣਾਓ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ਕਿਸਮ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ "ਫੰਕਸ਼ਨ" ਸੈੱਟ ਕਰੋ
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

    ਉਪਰੋਕਤ ਕੋਡ MCP ਸਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ LLM ਸਮਝਣਯੋਗ ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।

1. ਅਗਲਾ, `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੀਏ ਤਾਂ ਜੋ ਸਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਜਾਵੇ:

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

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ ਹੈ ਜੋ ਨਤੀਜੇ ਵਿੱਚੋਂ ਹਰ ਐਂਟਰੀ ਲਈ `openAiToolAdapter` ਕਾਲ ਕਰਦਾ ਹੈ।

#### Python

1. ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤੀ ਕਨਵਰਟਰ ਫੰਕਸ਼ਨ ਬਣਾਈਏ:

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

    ਉਪਰੋਕਤ `convert_to_llm_tools` ਫੰਕਸ਼ਨ ਵਿੱਚ ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਸਮਝਣਯੋਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਾਂ।

1. ਫਿਰ, ਆਪਣੇ ਕਲਾਇੰਟ ਕੋਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਲਈ ਅਪਡੇਟ ਕਰੋ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ਇੱਥੇ ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਨੂੰ ਫੀਡ ਕਰਨ ਲਈ `convert_to_llm_tool` ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ।

#### .NET

1. MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਸਮਝਣਯੋਗ ਬਣਾਉਣ ਲਈ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `ConvertFrom` ਫੰਕਸ਼ਨ ਬਣਾਇਆ ਜੋ ਨਾਮ, ਵਰਣਨ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾ ਲੈਂਦਾ ਹੈ।
- ਇੱਕ ਫੰਕਸ਼ਨਲਿਟੀ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੀ ਜੋ `FunctionDefinition` ਬਣਾਉਂਦੀ ਹੈ ਜੋ `ChatCompletionsDefinition` ਨੂੰ ਪਾਸ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ LLM ਲਈ ਸਮਝਣਯੋਗ ਹੁੰਦੀ ਹੈ।

1. ਹੁਣ ਦੇਖੀਏ ਕਿ ਅਸੀਂ ਮੌਜੂਦਾ ਕੋਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਲਈ ਕਿਵੇਂ ਅਪਡੇਟ ਕਰ ਸਕਦੇ ਹਾਂ:

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
// ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਬੋਟ ਇੰਟਰਫੇਸ ਬਣਾਓ
public interface Bot {
    String chat(String prompt);
}

// LLM ਅਤੇ MCP ਟੂਲਜ਼ ਨਾਲ AI ਸੇਵਾ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਇੱਕ ਸਧਾਰਣ `Bot` ਇੰਟਰਫੇਸ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ
- LangChain4j ਦੇ `AiServices` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜੋ LLM ਨੂੰ MCP ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਨਾਲ ਆਪਣੇ ਆਪ ਬਾਈਂਡ ਕਰਦਾ ਹੈ
- ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਟੂਲ ਸਕੀਮਾ ਕਨਵਰਜ਼ਨ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੰਭਾਲਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੂਅਲ ਟੂਲ ਕਨਵਰਜ਼ਨ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ - LangChain4j MCP ਟੂਲਾਂ ਨੂੰ LLM-ਅਨੁਕੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਾਰੀ ਜਟਿਲਤਾ ਸੰਭਾਲਦਾ ਹੈ

#### Rust

MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਸਮਝਣਯੋਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ, ਅਸੀਂ ਇੱਕ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰਦਾ ਹੈ। ਆਪਣੇ `main.rs` ਫਾਇਲ ਵਿੱਚ `main` ਫੰਕਸ਼ਨ ਦੇ ਹੇਠਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ। ਇਹ LLM ਨੂੰ ਬੇਨਤੀ ਕਰਨ ਸਮੇਂ ਕਾਲ ਕੀਤਾ ਜਾਵੇਗਾ:

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

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਕਿਸੇ ਵੀ ਯੂਜ਼ਰ ਬੇਨਤੀ ਨੂੰ ਹੈਂਡਲ ਕਰਨ ਲਈ ਤਿਆਰ ਹਾਂ, ਤਾਂ ਆਓ ਅਗਲਾ ਕਦਮ ਕਰੀਏ।

### -4- ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਬੇਨਤੀ ਹੈਂਡਲ ਕਰੋ

ਇਸ ਹਿੱਸੇ ਵਿੱਚ ਅਸੀਂ ਯੂਜ਼ਰ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਹੈਂਡਲ ਕਰਾਂਗੇ।

#### TypeScript

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
        // ਕਰਨ ਵਾਲਾ

        }
    }
    ```

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਇੱਕ `callTools` ਮੈਥਡ ਸ਼ਾਮਲ ਕੀਤਾ।
    - ਇਹ ਮੈਥਡ LLM ਜਵਾਬ ਲੈਂਦਾ ਹੈ ਅਤੇ ਦੇਖਦਾ ਹੈ ਕਿ ਕਿਹੜੇ ਟੂਲ ਕਾਲ ਕੀਤੇ ਗਏ ਹਨ, ਜੇ ਕੋਈ ਹਨ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        }
        ```

    - ਜੇ LLM ਦੱਸਦਾ ਹੈ ਕਿ ਕਿਸੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਤਾਂ ਉਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ:

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

1. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਨਾ ਅਤੇ `callTools` ਕਾਲ ਸ਼ਾਮਲ ਹੋਵੇ:

    ```typescript

    // 1. ਐਲਐਲਐਮ ਲਈ ਇਨਪੁੱਟ ਵਜੋਂ ਸੁਨੇਹੇ ਬਣਾਓ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. ਐਲਐਲਐਮ ਨੂੰ ਕਾਲ ਕਰਨਾ
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. ਐਲਐਲਐਮ ਦੇ ਜਵਾਬ ਨੂੰ ਵੇਖੋ, ਹਰ ਚੋਣ ਲਈ, ਜਾਂਚੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ਵਧੀਆ, ਪੂਰਾ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਹੈ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ zod ਇੰਪੋਰਟ ਕਰੋ

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
          // ਇਨਪੁਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ zod ਸਕੀਮਾ ਬਣਾਓ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ਕਿਸਮ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ "function" ਸੈੱਟ ਕਰੋ
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM ਜਵਾਬ ਵਿੱਚੋਂ ਹਰ ਚੋਣ ਲਈ ਜਾਂਚ ਕਰੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
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

1. LLM ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਇੰਪੋਰਟ ਸ਼ਾਮਲ ਕਰੋ:

    ```python
    # ਐਲਐਲਐਮ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ਫਿਰ, ਉਹ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰੇਗਾ:

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

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਆਪਣੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ, ਜੋ MCP ਸਰਵਰ ਤੋਂ ਮਿਲੇ ਅਤੇ ਬਦਲੇ ਗਏ, LLM ਨੂੰ ਪਾਸ ਕੀਤਾ।
    - ਫਿਰ LLM ਨੂੰ ਕਾਲ ਕੀਤਾ।
    - ਨਤੀਜੇ ਦੀ ਜਾਂਚ ਕੀਤੀ ਕਿ ਕਿਹੜੇ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨੇ ਹਨ, ਜੇ ਕੋਈ ਹਨ।
    - ਆਖਿਰਕਾਰ ਕਾਲ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨਾਂ ਦੀ ਲਿਸਟ ਪਾਸ ਕੀਤੀ।

1. ਆਖਰੀ ਕਦਮ, ਆਪਣੇ ਮੁੱਖ ਕੋਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ:

    ```python
    prompt = "Add 2 to 20"

    # LLM ਨੂੰ ਪੁੱਛੋ ਕਿ ਸਾਰੇ ਟੂਲ ਕਿਹੜੇ ਹਨ, ਜੇ ਕੋਈ ਹਨ
    functions_to_call = call_llm(prompt, functions)

    # ਸੁਝਾਏ ਗਏ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰੋ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - `call_tool` ਰਾਹੀਂ MCP ਟੂਲ ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ ਜੋ LLM ਨੇ ਸੂਚਿਤ ਕੀਤਾ ਕਿ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।
    - MCP ਸਰਵਰ ਨੂੰ ਟੂਲ ਕਾਲ ਦਾ ਨਤੀਜਾ ਪ੍ਰਿੰਟ ਕਰ ਰਹੇ ਹਾਂ।

#### .NET

1. LLM ਪ੍ਰਾਂਪਟ ਬੇਨਤੀ ਕਰਨ ਲਈ ਕੁਝ ਕੋਡ ਦਿਖਾਈਏ:

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

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕੀਤੇ, `var tools = await GetMcpTools()`।
    - ਇੱਕ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ `userMessage` ਪਰਿਭਾਸ਼ਿਤ ਕੀਤਾ।
    - ਮਾਡਲ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਇੱਕ ਵਿਕਲਪ ਆਬਜੈਕਟ ਬਣਾਇਆ।
    - LLM ਵੱਲ ਬੇਨਤੀ ਕੀਤੀ।

1. ਆਖਰੀ ਕਦਮ, ਦੇਖੀਏ ਕਿ LLM ਸੋਚਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਕਿਸੇ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ:

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

    ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਲੂਪ ਕੀਤਾ।
    - ਹਰ ਟੂਲ ਕਾਲ ਲਈ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਪਾਰਸ ਕਰਕੇ MCP ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਨਾਲ ਟੂਲ ਕਾਲ ਕੀਤਾ। ਆਖਿਰਕਾਰ ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕੀਤੇ।

ਪੂਰਾ ਕੋਡ ਇੱਥੇ ਹੈ:

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
    // ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀਆਂ ਬੇਨਤੀਆਂ ਨੂੰ ਚਲਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ
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

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ ਟੂਲਾਂ ਨਾਲ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰਾਂਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕੀਤੀ
- LangChain4j ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
  - ਜਦੋਂ ਲੋੜ ਹੋਵੇ ਤਾਂ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਟੂਲ ਕਾਲਾਂ ਵਿੱਚ ਬਦਲਣਾ
  - LLM ਦੇ ਫੈਸਲੇ ਅਨੁਸਾਰ MCP ਟੂਲਾਂ ਨੂੰ ਕਾਲ ਕਰਨਾ
  - LLM ਅਤੇ MCP ਸਰਵਰ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਬੰਧਨ
- `bot.chat()` ਮੈਥਡ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ MCP ਟੂਲਾਂ ਦੇ ਨਤੀਜੇ ਸ਼ਾਮਲ ਹੋ ਸਕਦੇ ਹਨ
- ਇਹ ਤਰੀਕਾ ਇੱਕ ਬਿਨਾਂ ਰੁਕਾਵਟ ਵਾਲਾ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰਾਂ ਨੂੰ MCP ਦੀ ਅੰਦਰੂਨੀ ਕਾਰਗੁਜ਼ਾਰੀ ਬਾਰੇ ਜਾਣਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ

ਪੂਰਾ ਕੋਡ ਉਦਾਹਰਨ:

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

ਇੱਥੇ ਜ਼ਿਆਦਾਤਰ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨਾਲ LLM ਨੂੰ ਕਾਲ ਕਰਾਂਗੇ, ਫਿਰ ਜਵਾਬ ਦੀ ਪ੍ਰਕਿਰਿਆ ਕਰਾਂਗੇ ਕਿ ਕੀ ਕਿਸੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਜੇ ਹਾਂ, ਤਾਂ ਅਸੀਂ ਉਹ ਟੂਲ ਕਾਲ ਕਰਾਂਗੇ ਅਤੇ ਗੱਲਬਾਤ LLM ਨਾਲ ਜਾਰੀ ਰੱਖਾਂਗੇ ਜਦ ਤੱਕ ਹੋਰ ਟੂਲ ਕਾਲਾਂ ਦੀ ਲੋੜ ਨਾ ਰਹਿ ਜਾਵੇ ਅਤੇ ਸਾਡੇ ਕੋਲ ਅੰਤਿਮ ਜਵਾਬ ਹੋਵੇ।

ਅਸੀਂ LLM ਨੂੰ ਕਈ ਵਾਰੀ ਕਾਲ ਕਰਾਂਗੇ, ਇਸ ਲਈ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰੀਏ ਜੋ LLM ਕਾਲ ਨੂੰ ਸੰਭਾਲੇ। ਆਪਣੇ `main.rs` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ:

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

ਇਹ ਫੰਕਸ਼ਨ LLM ਕਲਾਇੰਟ, ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ (ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਲ ਹੈ), MCP ਸਰਵਰ ਤੋਂ ਟੂਲਾਂ ਨੂੰ ਲੈਂਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ, ਜਵਾਬ ਵਾਪਸ ਕਰਦਾ ਹੈ।
LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਵਿੱਚ `choices` ਦੀ ਇੱਕ ਐਰੇ ਸ਼ਾਮਲ ਹੋਵੇਗੀ। ਸਾਨੂੰ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਨੀ ਪਵੇਗੀ ਤਾਂ ਜੋ ਦੇਖਿਆ ਜਾ ਸਕੇ ਕਿ ਕੋਈ `tool_calls` ਮੌਜੂਦ ਹਨ ਜਾਂ ਨਹੀਂ। ਇਹ ਸਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ LLM ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਦੀ ਮੰਗ ਕਰ ਰਿਹਾ ਹੈ ਜਿਸ ਵਿੱਚ ਦਲੀਲਾਂ ਹਨ। LLM ਜਵਾਬ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਇੱਕ ਫੰਕਸ਼ਨ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨ ਲਈ ਆਪਣੇ `main.rs` ਫਾਇਲ ਦੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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

            // ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਟੂਲ ਨਤੀਜਾ ਸ਼ਾਮਲ ਕਰੋ
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

ਜੇ `tool_calls` ਮੌਜੂਦ ਹਨ, ਤਾਂ ਇਹ ਟੂਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਦਾ ਹੈ, MCP ਸਰਵਰ ਨੂੰ ਟੂਲ ਬੇਨਤੀ ਨਾਲ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਗੱਲਬਾਤ ਦੇ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਫਿਰ ਇਹ LLM ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹੇ ਸਹਾਇਕ ਦੇ ਜਵਾਬ ਅਤੇ ਟੂਲ ਕਾਲ ਨਤੀਜਿਆਂ ਨਾਲ ਅਪਡੇਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

MCP ਕਾਲਾਂ ਲਈ LLM ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੀ ਟੂਲ ਕਾਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਣ ਲਈ, ਅਸੀਂ ਇੱਕ ਹੋਰ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦਾ ਸਾਰਾ ਕੁਝ ਕੱਢੇਗਾ। ਆਪਣੇ `main.rs` ਫਾਇਲ ਦੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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

ਸਾਰੇ ਹਿੱਸੇ ਠੀਕ ਢੰਗ ਨਾਲ ਜੁੜ ਗਏ ਹਨ, ਹੁਣ ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸੰਭਾਲ ਸਕਦੇ ਹਾਂ ਅਤੇ LLM ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਹੋਵੇ:

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

ਇਹ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨਾਲ LLM ਨੂੰ ਪੁੱਛੇਗਾ ਕਿ ਦੋ ਨੰਬਰਾਂ ਦਾ ਜੋੜ ਕੀ ਹੈ, ਅਤੇ ਜਵਾਬ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਕੇ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਸੰਭਾਲੇਗਾ।

ਸ਼ਾਬਾਸ਼, ਤੁਸੀਂ ਇਹ ਕਰ ਲਿਆ!

## ਅਸਾਈਨਮੈਂਟ

ਵਿਆਯਾਮ ਤੋਂ ਕੋਡ ਲਵੋ ਅਤੇ ਕੁਝ ਹੋਰ ਟੂਲਾਂ ਨਾਲ ਸਰਵਰ ਬਣਾਓ। ਫਿਰ ਇੱਕ LLM ਵਾਲਾ ਕਲਾਇੰਟ ਬਣਾਓ, ਜਿਵੇਂ ਕਿ ਵਿਆਯਾਮ ਵਿੱਚ ਹੈ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਾਂਪਟਾਂ ਨਾਲ ਇਸ ਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣਾਇਆ ਜਾ ਸਕੇ ਕਿ ਤੁਹਾਡੇ ਸਾਰੇ ਸਰਵਰ ਟੂਲ ਗਤੀਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਕਾਲ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ। ਇਸ ਤਰੀਕੇ ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਅੰਤਮ ਉਪਭੋਗਤਾ ਨੂੰ ਵਧੀਆ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਮਿਲੇਗਾ ਕਿਉਂਕਿ ਉਹ ਪ੍ਰਾਂਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ, ਬਜਾਏ ਸਹੀ ਕਲਾਇੰਟ ਕਮਾਂਡਾਂ ਦੇ, ਅਤੇ ਕਿਸੇ ਵੀ MCP ਸਰਵਰ ਕਾਲ ਹੋਣ ਤੋਂ ਅਣਜਾਣ ਰਹੇਗਾ।

## ਹੱਲ

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ਮੁੱਖ ਸਿੱਖਣ ਵਾਲੀਆਂ ਗੱਲਾਂ

- ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਲ ਕਰਨ ਨਾਲ ਉਪਭੋਗਤਾਵਾਂ ਲਈ MCP ਸਰਵਰਾਂ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਦਾ ਬਿਹਤਰ ਤਰੀਕਾ ਮਿਲਦਾ ਹੈ।
- ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਦੇ ਜਵਾਬ ਨੂੰ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਬਦਲਣਾ ਪੈਂਦਾ ਹੈ ਜੋ LLM ਸਮਝ ਸਕੇ।

## ਨਮੂਨੇ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ਵਾਧੂ ਸਰੋਤ

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਨੂੰ ਕਨਜ਼ਿਊਮ ਕਰਨਾ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->