# LLM ਨਾਲ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਅਜੇ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਹੈ ਕਿ ਸੇਰਵਰ ਅਤੇ ਕਲਾਇੰਟ ਕਿਵੇਂ ਬਣਾਏ ਜਾਂਦੇ ਹਨ। ਕਲਾਇੰਟ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਸੇਰਵਰ ਨੂੰ ਕਾਲ ਕਰਨ ਵਿੱਚ ਸਮਰੱਥ ਰਹਿ ਚੁੱਕਾ ਹੈ ਤਾਂ ਜੋ ਉਹ ਆਪਣੇ ਟੂਲ, ਸਰੋਤ, ਅਤੇ ਪ੍ਰਾਂਪਟ ਦੀ ਸੂਚੀ ਬਣਾ ਸਕੇ। ਹਾਲਾਂਕਿ, ਇਹ ਬਹੁਤ ਪ੍ਰਾਇਗਮਿਕ ਤਰੀਕਾ ਨਹੀਂ ਹੈ। ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਏਜੈਂਟਿਕ ਯੁੱਗ ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਉਮੀਦ ਕਰਦੇ ਹਨ ਕਿ ਉਹ ਪ੍ਰਾਂਪਟ ਵਰਤ ਕੇ ਅਤੇ ਇੱਕ LLM ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਣਗੇ। ਉਹ ਨੂੰ ਫ਼ਰਕ ਨਹੀਂ ਪੈਂਦਾ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਸਟੋਰ ਕਰਨ ਲਈ MCP ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ; ਉਹ ਸਹਿਜ ਭਾਸ਼ਾ ਵਿੱਚ ਮੁਹੱਈਆ ਕੀਤੀ ਗਈ ਗੱਲਬਾਤ ਕੀਤਾ ਕਰਨ ਦੀ ਉਮੀਦ ਕਰਦੇ ਹਨ। ਤਾਂ ਇਸ ਦਾ ਹੱਲ ਕੀ ਹੈ? ਹੱਲ ਇਹ ਹੈ ਕਿ ਕਲਾਇੰਟ ਨੂੰ ਇੱਕ LLM ਸ਼ਾਮਿਲ ਕੀਤਾ ਜਾਵੇ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਧਿਆਨ ਕੇਂਦਰਤ ਕਰਦੇ ਹਾਂ ਕਿ ਕਿਵੇਂ ਇੱਕ LLM ਨੂੰ ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨਾ ਹੈ ਅਤੇ ਦਿਖਾਉਂਦੇ ਹਾਂ ਕਿ ਇਹ ਤੁਹਾਡੇ ਯੂਜ਼ਰ ਲਈ ਕਿਵੇਂ ਬਿਹਤਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਇੱਕ LLM ਨਾਲ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਉਣ ਲਈ।
- ਇੱਕ MCP ਸੇਰਵਰ ਨਾਲ ਇੱਕ LLM ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਹਿਜ ਤਰੀਕੇ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ।
- ਕਲਾਇੰਟ ਪਾਸੇ ਬਿਹਤਰ ਅੰਤ ਯੂਜ਼ਰ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ।

## ਤਰੀਕਾ

ਆਓ ਸਮਝਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ ਕਿ ਸਾਨੂੰ ਕਿਹੜਾ ਤਰੀਕਾ ਅਪਣਾ ਚਾਹੀਦਾ ਹੈ। ਇੱਕ LLM ਸ਼ਾਮਿਲ ਕਰਨਾ ਆਸਾਨ ਲੱਗਦਾ ਹੈ, ਪਰ ਕੀ ਅਸੀਂ ਹਕੀਕਤ ਵਿੱਚ ਇਹ ਕਰਾਂਗੇ?

ਇਹ ਹੈ ਕਿਵੇਂ ਕਲਾਇੰਟ ਸੇਰਵਰ ਨਾਲ ਗੱਲਬਾਤ ਕਰੇਗਾ:

1. ਸੇਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰੋ।

1. ਸਮਰੱਥਾਵਾਂ, ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ, ਅਤੇ ਉਹਨਾਂ ਦੇ ਸਕੀਮਾ ਨੂੰ ਸੰਭਾਲਕੇ ਰੱਖੋ।

1. ਇੱਕ LLM ਸ਼ਾਮਿਲ ਕਰੋ ਅਤੇ ਸੰਭਾਲੇ ਗਏ ਸਮਰੱਥਾਵਾਂ ਅਤੇ ਉਹਨਾਂ ਦੇ ਸਕੀਮਾ ਨੂੰ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਪਾਸ ਕਰੋ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ।

1. ਇੱਕ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸੰਭਾਲੋ ਅਤੇ ਇਸਨੂੰ LLM ਨੂੰ ਕਲਾਇੰਟ ਦੁਆਰਾ ਲਿਸਟ ਕੀਤੇ ਟੂਲਾਂ ਦੇ ਨਾਲ ਦਿਓ।

ਵਧੀਆ, ਹੁਣ ਸਾਨੂੰ ਸਮਝ ਆ ਗਈ ਕਿ ਅਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਆਓ ਹੇਠਾਂ ਦਿੱਤੇ ਅਭਿਆਸ ਵਿੱਚ ਇਸਨੂੰ ਟ੍ਰਾਈ ਕਰੀਏ।

## ਅਭਿਆਸ: ਇੱਕ LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਉਣਾ

ਇਸ ਅਭਿਆਸ ਵਿੱਚ, ਅਸੀਂ ਸਿੱਖਾਂਗੇ ਕਿ ਕਿਵੇਂ ਇੱਕ LLM ਨੂੰ ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਨਾ ਹੈ।

### GitHub ਪर्सਨਲ ਐਕਸੈੱਸ ਟੋਕਨ ਦੁਆਰਾ ਪ੍ਰਮਾਣੀਕਰਨ

GitHub ਟੋਕਨ ਬਣਾਉਣਾ ਸਿੱਧਾ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਇੱਥੇ ਹੈ ਕਿ ਤੁਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

- GitHub ਸੈਟਿੰਗਸ 'ਤੇ ਜਾਓ – ਸੱਜੇ ਉੱਪਰ ਕੌਰਨਰ ਵਿਚ ਆਪਣੀ ਪ੍ਰੋਫਾਈਲ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ Settings ਚੁਣੋ।
- Developer Settings ਵੱਲ ਜਾਓ – ਹੇਠਾਂ ਸਕ੍ਰੋਲ ਕਰਕੇ Developer Settings 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
- Personal Access Tokens ਚੁਣੋ – Fine-grained tokens ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫਿਰ Generate new token।
- ਆਪਣੇ ਟੋਕਨ ਨੂੰ ਕਾਨਫ਼ਿਗਰ ਕਰੋ – ਰੇਫਰੈਂਸ ਲਈ ਨੋਟ ਸ਼ਾਮਿਲ ਕਰੋ, ਮਿਆਦ ਨਿਰਧਾਰਿਤ ਕਰੋ, ਅਤੇ ਜਰੂਰੀ scopes (ਇਜਾਜ਼ਤਾਂ) ਚੁਣੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ Models ਦੀ ਇਜਾਜ਼ਤ ਜੋੜੋ।
- ਟੋਕਨ ਜਨਰੇਟ ਕਰੋ ਅਤੇ ਕਾਪੀ ਕਰੋ – Generate token ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਤੁਰੰਤ ਇਸਨੂੰ ਕਾਪੀ ਕਰੋ, ਕਿਉਂਕਿ ਤੁਸੀਂ ਮੁੜ ਇਹ ਨਹੀਂ ਦੇਖ سکੋਗੇ।

### -1- ਸੇਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨਾ

ਆਓ ਸਭ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣਾ ਕਲਾਇੰਟ ਬਣਾਈਏ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਧਤਾ ਲਈ ਜ਼ੋਡ ਆਮਦ ਕਰੋ

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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕੀਤਾ ਹੈ
- ਇੱਕ ਕਲਾਸ ਬਣਾਈ ਹੈ ਜਿਸ ਵਿੱਚ ਦੋ ਮੈਂਬਰ ਹਨ, `client` ਅਤੇ `openai`, ਜੋ ਸਦੱਸਾਂ ਕਲਾਇੰਟ ਨੂੰ ਸੰਭਾਲਣ ਅਤੇ LLM ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨਗੇ।
- ਆਪਣੇ LLM ਇੰਸਟੈਂਸ ਨੂੰ GitHub ਮਾਡਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਕਾਨਫਿਗਰ ਕੀਤਾ ਹੈ ਜਦ ਕਿ `baseUrl` ਨੂੰ ਇੰਫਰੈਂਸ API ਨਾਲ ਜੋੜਿਆ ਗਿਆ ਹੈ।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਐਗਜ਼ੈਕਿਊਟੇਬਲ
    args=["run", "server.py"],  # ਵਿਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਆਰਗੂਮੈਂਟ
    env=None,  # ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਨ ਚਲ
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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਲਈ ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ ਹਨ
- ਇੱਕ ਕਲਾਇੰਟ ਤਿਆਰ ਕੀਤਾ ਹੈ

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

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `pom.xml` ਫਾਈਲ ਵਿੱਚ LangChain4j ਡਿਪੇਂਡੈਂਸੀਜ਼ ਸ਼ਾਮਿਲ ਕਰਨੀ ਪੈਣਗੀਆਂ। MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ GitHub ਮਾਡਲਾਂ ਸਹਾਇਤਾ ਨੂੰ ਯੋਗ ਕਰਨ ਲਈ ਇਹ ਡਿਪੇਂਡੈਂਸੀਜ਼ ਜੋੜੋ:

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
    
    public static void main(String[] args) throws Exception {        // LLM ਨੂੰ GitHub ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਸੰਰਚਿਤ ਕਰੋ
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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- **LangChain4j ਡਿਪੇਂਡੈਂਸੀਜ਼ ਜੋੜੀਆਂ**: MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ, OpenAI ਅਧਿਕਾਰਿਕ ਕਲਾਇੰਟ ਅਤੇ GitHub ਮਾਡਲ ਸਹਾਇਤਾ ਲਈ
- **LangChain4j ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਪੋਰਟ ਕੀਤੀਆਂ**: MCP ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI ਚੈਟ ਮਾਡਲ ਫੰਕਸ਼ਨ ਵਿਕਾਸ ਲਈ
- **`ChatLanguageModel` ਬਣਾਇਆ**: ਆਪਣੇ GitHub ਟੋਕਨ ਨਾਲ GitHub ਮਾਡਲ ਵਰਤਣ ਲਈ ਕਾਫ਼ਿਗਰ ਕੀਤਾ
- **HTTP ਟ੍ਰਾਂਸਪੋਰਟ ਸੈਟਅੱਪ ਕੀਤਾ**: Server-Sent Events (SSE) ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸੇਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ
- **MCP ਕਲਾਇੰਟ ਬਣਾਇਆ**: ਜੋ ਸੇਰਵਰ ਨਾਲ ਸੰਚਾਰ ਸੰਭਾਲੇਗਾ
- **LangChain4j ਦੀ ਬਿਲਟ-ਇਨ MCP ਸਹਾਇਤਾ ਵਰਤੀ**: ਜੋ LLM ਅਤੇ MCP ਸੇਰਵਰਾਂ ਵਿੱਚ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਨੂੰ ਸਾਦਾ ਬਣਾਉਂਦੀ ਹੈ

#### Rust

ਇਹ ਉਦਾਹਰਣ ਸਮਝਦੀ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਰਸਟ-ਆਧਾਰਿਤ MCP ਸੇਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤਾਂ [01-first-server](../01-first-server/README.md) ਪਾਠ ਵਿੱਚ ਵਾਪਸ ਜਾ ਕੇ ਸੇਰਵਰ ਬਣਾਓ।

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਰਸਟ MCP ਸੇਰਵਰ ਹੋਵੇ, ਇੱਕ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਉਸੇ ਫੋਲਡਰ ਵਿੱਚ ਜਾਓ ਜਿੱਥੇ ਸੇਰਵਰ ਹੈ। ਫਿਰ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾ ਕੇ ਨਵਾਂ LLM ਕਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ਆਪਣੀ `Cargo.toml` ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਡਿਪੇਂਡੈਂਸੀਜ਼ ਜੋੜੋ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ਲਈ ਕੋਈ ਅਧਿਕਾਰਿਕ ਰਸਟ ਲਾਇਬ੍ਰੇਰੀ ਨਹੀਂ ਹੈ, ਪਰ `async-openai` crate ਇੱਕ [ਕਮਿਿੂਨਿਟੀ ਦ੍ਵਾਰਾ ਸੰਭਾਲੀ ਜਾਂਦੀ ਲਾਇਬ੍ਰੇਰੀ](https://platform.openai.com/docs/libraries/rust#rust) ਹੈ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

`src/main.rs` ਫਾਈਲ ਖੋਲ੍ਹੋ ਅਤੇ ਇਸਦਾ ਸਮੱਗਰੀ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਬਦਲੋ:

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

    // TODO: MCP ਟੂਲ ਦੀ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ

    // TODO: ਟੂਲ ਕਾਲਾਂ ਨਾਲ LLM ਗੱਲਬਾਤ

    Ok(())
}
```

ਇਹ ਕੋਡ ਇੱਕ ਮੂਲ ਰਸਟ ਐਪਲੀਕੇਸ਼ਨ ਸੈਟਅੱਪ ਕਰਦਾ ਹੈ ਜੋ MCP ਸੇਰਵਰ ਅਤੇ GitHub ਮਾਡਲਾਂ ਨਾਲ LLM ਗੱਲਬਾਤ ਲਈ ਕਨੈਕਟ ਕਰੇਗਾ।

> [!IMPORTANT]
> ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣੇ GitHub ਟੋਕਨ ਨਾਲ `OPENAI_API_KEY` ਵਾਤਾਵਰਣ ਚਲਨਹਾਰ ਵੈਰੀਏਬਲ ਸੈਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

ਵਧੀਆ, ਆਪਣੇ ਅਗਲੇ ਕਦਮ ਲਈ, ਆਓ ਸੇਰਵਰ 'ਤੇ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈਏ।

### -2- ਸੇਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ

ਹੁਣ ਅਸੀਂ ਸੇਰਵਰ ਨਾਲ ਜੁੜ ਕੇ ਉਸ ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਪੂੱਛਾਂਗੇ:

#### TypeScript

ਉਸੇ ਕਲਾਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਮੈਥਡਜ਼ ਜੋੜੋ:

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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸੇਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ ਕੋਡ ਜੋੜਿਆ ਹੈ, `connectToServer`।
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਈ ਹੈ ਜੋ ਐਪ ਦੀ ਪ੍ਰਵਾਹ ਸੰਭਾਲਦੀ ਹੈ। ਹੁਣ ਤੱਕ ਇਹ ਸਿਰਫ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਦਿਖਾਉਂਦੀ ਹੈ ਪਰ ਅਸੀਂ ਇਸ ਵਿੱਚ ਥੋੜਾ ਹੋਰ ਵੀ ਜਲਦੀ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ।

#### Python

```python
# ਉਪਲਬਧ ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ਉਪਲਬਧ ਯੰਤਰਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ਇੱਥੇ ਜੋ ਅਸੀਂ ਸ਼ਾਮਿਲ ਕੀਤਾ ਹੈ:

- ਸਰੋਤ ਅਤੇ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾ ਕੇ ਪ੍ਰਿੰਟ ਕੀਤਾ। ਟੂਲਾਂ ਲਈ ਅਸੀਂ `inputSchema` ਵੀ ਲਿਸਟ ਕਰਦੇ ਹਾਂ ਜੋ ਅੱਗੇ ਵਰਤੀ ਜਾਵੇਗੀ।

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

- MCP ਸੇਰਵਰ ਉੱਤੇ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਹੈ
- ਹਰ ਟੂਲ ਲਈ, ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਉਸ ਦਾ ਸਕੀਮਾ ਲਿਸਟ ਕੀਤਾ। ਇਹ ਤੁਸੀਂ ਜਲਦੀ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤੋਂਗੇ।

#### Java

```java
// ਇੱਕ ਟੂਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ਟੂਲ ਪ੍ਰਦਾਤਾ ਆਪਣੇ ਆਪ ਇਹ ਸੰਭਾਲਦਾ ਹੈ:
// - MCP ਸਰਵਰ ਤੋਂ ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾ ਰਿਹਾ ਹੈ
// - MCP ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ LangChain4j ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ
// - ਟੂਲ ਐਕਜ਼ਿਕਿਊਸ਼ਨ ਅਤੇ ਜਵਾਬਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ `McpToolProvider` ਬਣਾਇਆ ਜੋ ਆਪਣੇ ਆਪ MCP ਸੇਰਵਰ ਤੋਂ ਸਾਰੇ ਟੂਲਾਂ ਨੂੰ ਅਨੁਸੂਚਿਤ ਤੇ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ
- ਟੂਲ ਪ੍ਰੋਵਾਇਡਰ MCP ਟੂਲ ਸਕੀਮਾਂ ਅਤੇ LangChain4j ਦੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿਚ ਧਿਆਨ ਨਾਲ ਬਦਲਾਅ ਕਰਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੂਅਲ ਟੂਲ ਲਿਸਟਿੰਗ ਅਤੇ ਬਦਲਾਅ ਦੀ ਜ਼ਰੂਰਤ ਨੂੰ ਖ਼ਤਮ ਕਰਦਾ ਹੈ

#### Rust

MCP ਸੇਰਵਰ ਤੋਂ ਟੂਲਾਂ ਪ੍ਰਾਪਤ ਕਰਨ ਦੇ ਲਈ `list_tools` ਮੈਥਡ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਵਿੱਚ, MCP ਕਲਾਇੰਟ ਸੈਟਅੱਪ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ:

```rust
// MCP ਟੂਲ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ਸੇਰਵਰ ਸਮਰੱਥਾਵਾਂ ਨੂੰ LLM ਟੂਲਾਂ ਵਿੱਚ ਬਦਲੋ

ਸੇਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਅਗਲਾ ਕਦਮ ਹੈ ਕਿ ਉਹਨਾਂ ਨੂੰ ਇੱਕ ਐਸੇ ਫਾਰਮੇਟ ਵਿੱਚ ਬਦਲਣਾ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ। ਇਸ ਤੋਂ ਬਾਅਦ ਅਸੀਂ ਇਹ ਸਮਰੱਥਾਵਾਂ ਆਪਣੇ LLM ਲਈ ਟੂਲਾਂ ਵਜੋਂ ਪ੍ਰਦਾਨ ਕਰ ਸਕਦੇ ਹਾਂ।

#### TypeScript

1. MCP ਸੇਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਵਰਤਣਯੋਗ ਟੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ਇਨਪੁਟ_schema ਦੇ ਆਧਾਰ ਤੇ ਇੱਕ ਜ਼ਾਡ ਸਕੀਮਾ ਬਣਾਓ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ਕਿਸਮ ਨੂੰ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ "ਫੰਕਸ਼ਨ" ਸੈੱਟ ਕਰੋ
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

    ਉੱਪਰ ਦਿੱਤਾ ਕੋਡ MCP ਸੇਰਵਰ ਤੋਂ ਜਵਾਬ ਲੈਂਦਾ ਹੈ ਅਤੇ ਉਸਨੂੰ LLM ਦੀ ਸਮਝ ਵਾਲੇ ਟੂਲ ਪਰਿਭਾਸ਼ਾ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।

1. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ ਸੇਰਵਰ ਸਮਰੱਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਈ ਜਾਵੇ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ `run` ਮੈਥਡ ਬਦਲਿਆ ਹੈ, ਨਤੀਜੇ ਵਿਚੋਂ ਹਰ ਐਂਟਰੀ ਲਈ `openAiToolAdapter` ਕਾਲ ਕਰਦਾ ਹੈ।

#### Python

1. ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤੀ ਕਨਵਰਟਰ ਫੰਕਸ਼ਨ ਬਣਾਓ

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

    ਇਸ ਫੰਕਸ਼ਨ `convert_to_llm_tools` ਵਿੱਚ ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਲੈਂਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਐਸੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਾਂ ਜੋ LLM ਸਮਝ ਸਕਦਾ ਹੈ।

1. ਫਿਰ ਆਪਣੇ ਕਲਾਇੰਟ ਕੋਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਵਰਤਣ ਲਈ ਅਪਡੇਟ ਕਰੋ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ਇੱਥੇ ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਖੁਰਾਕ ਦੇਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ `convert_to_llm_tool` ਕਾਲ ਕਰ ਰਹੇ ਹਾਂ।

#### .NET

1. MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਸਮਝ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਕੋਡ ਜੋੜੋ

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

- ਇੱਕ ਫੰਕਸ਼ਨ `ConvertFrom` ਬਣਾਇਆ ਜੋ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਇਨਪੁਟ ਸਕੀਮਾ ਲੈਂਦਾ ਹੈ।
- ਇੱਕ ਫੰਕਸ਼ਨ ਤਿਆਰ ਕੀਤਾ ਜੋ ਇੱਕ FunctionDefinition ਬਣਾਉਂਦਾ ਹੈ ਜੋ ChatCompletionsDefinition ਵਿੱਚ ਦਿੰਦਾ ਹੈ। ਪਿਛਲਾ W LLM ਲਈ ਸਮਝ ਦਾ ਹੈ।

1. ਇਸ ਤੋਂ ਬਾਅਦ ਦੇ ਕੂਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਅਪਡੇਟ ਕਰੀਏ:

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
// ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰੈਕਸ਼ਨ ਲਈ ਬੌਟ ਇੰਟਰਫੇਸ ਬਣਾਓ
public interface Bot {
    String chat(String prompt);
}

// LLM ਅਤੇ MCP ਟੂਲਸ ਨਾਲ AI ਸੇਵਾ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਇੱਕ ਸਰਲ `Bot` ਇੰਟਰਫੇਸ ਨੂੰ ਪਾਰਕੀਮੀ ਭਾਸ਼ਾ ਗੱਲਬਾਤ ਲਈ ਡਿਫਾਈਨ ਕੀਤਾ
- LangChain4j ਦੇ `AiServices` ਨੂੰ ਵਰਤਿਆ ਜੋ LLM ਨੂੰ MCP ਟੂਲ ਪ੍ਰੋਵਾਇਡਰ ਨਾਲ ਆਪਣੇ ਆਪ ਜੋੜਦਾ ਹੈ
- ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਟੂਲ ਸਕੀਮਾ ਬਦਲਾਅ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲ ਨੂੰ ਹੈਂਡਲ ਕਰਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਮੈਨੂਅਲ ਟੂਲ ਕਨਵਰਜ਼ਨ ਨੂੰ ਖਤਮ ਕਰਦਾ ਹੈ - LangChain4j MCP ਟੂਲਾਂ ਨੂੰ LLM-ਸਮਝਯੋਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਾਰੀ ਜਟਿਲਤਾ ਸੰਭਾਲਦਾ ਹੈ

#### Rust

MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਸਮਝ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ, ਅਸੀਂ ਇੱਕ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕਰਾਂਗੇ ਜੋ ਟੂਲ ਸੂਚੀ ਨੂੰ ਫਾਰਮੈਟ ਕਰੇਗਾ। ਆਪਣੇ `main.rs` ਫਾਈਲ ਵਿੱਚ `main` ਫੰਕਸ਼ਨ ਤੋਂ ਹੇਠਾਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ। ਇਹ LLM ਕੋਲ ਬੇਨਤੀਆਂ ਕਰਨ ਵੇਲੇ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

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

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਯੂਜ਼ਰ ਦੀਆਂ ਬੇਨਤੀਆਂ ਸੰਭਾਲਣ ਲਈ ਤਿਆਰ ਹਾਂ, ਆਓ ਅੱਗੇ ਵਧੀਏ।

### -4- ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਬੇਨਤੀ ਸੰਭਾਲੋ

ਇਸ ਹਿੱਸੇ ਵਿੱਚ ਅਸੀਂ ਯੂਜ਼ਰ ਦੀਆਂ ਬੇਨਤੀਆਂ ਸੰਭਾਲਾਂਗੇ।

#### TypeScript

1. ਉਹ ਮੈਥਡ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ ਜੋੜੋ:

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
        // ਕਰਨ ਲਈ

        }
    }
    ```

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਇੱਕ ਮੈਥਡ `callTools` ਜੋੜੀ ਹੈ।
    - ਮੈਥਡ LLM ਜਵਾਬ ਨੂੰ ਲੈਂਦੀ ਹੈ ਅਤੇ ਦੇਖਦੀ ਹੈ ਕਿ ਕਿਹੜੇ ਟੂਲ ਕਾਲ ਹੋਏ ਹਨ, ਜੇ ਹੋਏ ਹਨ:

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
        // ਕਰਨਾ ਹੈ
        ```

1. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਕੇ `callTools` ਨੂੰ ਕਾਲ ਕੀਤਾ ਜਾਵੇ:

    ```typescript

    // 1. ਮੈਸੇਜ ਬਣਾਓ ਜੋ LLM ਲਈ ਇਨਪੁਟ ਹਨ
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

    // 3. LLM ਦੇ ਜਵਾਬ ਨੂੰ ਦੇਖੋ, ਹਰ ਇੱਕ ਚੋਣ ਲਈ, ਜਾਂਚੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
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
import { z } from "zod"; // ਸਕੀਮਾ ਸੱਤਿਆਪਨ ਲਈ ਜ਼ੋਡ ਇੰਪੋਰਟ ਕਰੋ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ਭਵਿੱਖ ਵਿੱਚ ਇਸ URL ਨੂੰ ਬਦਲਣਾ ਪੈ ਸਕਦਾ ਹੈ: https://models.github.ai/inference
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
          // ਇਨਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਜ਼ੋਡ ਸਕੀਮਾ ਬਣਾਓ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ਟਾਈਪ ਨੂੰ ਖੁੱਲ੍ਹ ਕੇ "function" ਸੈੱਟ ਕਰੋ
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
          // ਕਰਨਾ ਬਾਕੀ ਹੈ
    
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
    
        // 1. LLM ਜਵਾਬ ਦੁਆਰਾ ਜਾਓ, ਹਰ ਚੋਣ ਲਈ, ਜਾਂਚੋ ਕਿ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ ਕਿ ਨਹੀਂ
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

1. LLM ਕਾਲ ਲਈ ਲੋੜੀਂਦੇ ਇੰਪੋਰਟਸ ਜੋੜੋ

    ```python
    # ਐਲਐਲਐਮ
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. ਫਿਰ ਉਹ ਫੰਕਸ਼ਨ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰੇਗਾ ਜੋੜੋ:

    ```python
    # ਐਲਐੱਲਐਮ

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਸੇਰਵਰ ਤੋਂ ਲੱਭੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ LLM ਨੂੰ ਪਾਸ ਕੀਤਾ।
    - ਫਿਰ LLM ਨੂੰ ਇਹਨਾਂ ਫੰਕਸ਼ਨਾਂ ਨਾਲ ਕਾਲ ਕੀਤਾ।
    - ਨਤੀਜੇ ਦਾ ਜਾਇਜ਼ਾ ਲਿਆ ਕਿ ਕਿਹੜੇ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਣੇ ਹਨ, ਜੇ ਕੋਈ ਹੋਣ।
    - ਆਖਿਰਕਾਰ ਕਾਲ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨਾਂ ਦੀ ਲੜੀ ਪਾਸ ਕੀਤੀ।

1. ਅੰਤਮ ਕਦਮ, ਆਪਣੇ ਮੁੱਖ ਕੋਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ:

    ```python
    prompt = "Add 2 to 20"

    # LLM ਨੂੰ ਪੁੱਛੋ ਕਿ ਸਭ ਲਈ ਕਿਹੜੇ ਟੂਲ ਹਨ, ਜੇ ਕੋਈ ਹਨ
    functions_to_call = call_llm(prompt, functions)

    # ਸੂਝਾਅਤਫ਼ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰੋ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    ਉੱਥੇ, ਇਹ ਆਖਰੀ ਕਦਮ ਸੀ। ਉਪਰਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਟੂਲ ਨੂੰ `call_tool` ਰਾਹੀਂ ਕਾਲ ਕਰਦੇ ਹਾਂ ਜਿਹੜਾ LLM ਸਮਝਦਾ ਹੈ ਕਿ ਸਾਡੀ ਪ੍ਰਾਂਪਟ ਦੇ ਅਧਾਰ ਤੇ ਕਾਲ ਕਰਨ ਦੀ ਲੋੜ ਹੈ।
    - ਟੂਲ ਕਾਲ ਦਾ ਨਤੀਜਾ MCP ਸੇਰਵਰ ਨੂੰ ਛਾਪਦੇ ਹਾਂ।

#### .NET

1. LLM ਪ੍ਰਾਂਪਟ ਬੇਨਤੀ ਕਰਨ ਵਾਲਾ ਕੁਝ ਕੋਡ ਦਿਖਾਉਂਦੇ ਹਾਂ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - MCP ਸੇਰਵਰ ਤੋਂ ਟੂਲ ਲੈ ਕੇ, `var tools = await GetMcpTools()`।
    - ਯੂਜ਼ਰ ਦਾ ਪ੍ਰਾਂਪਟ `userMessage` ਲਿਆ।
    - ਮਾਡਲ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਦਰਸਾਉਂਦਾ ਕੋਈ options ਆਬਜੈਕਟ ਬਣਾਇਆ।
    - LLM ਵੱਲ ਬੇਨਤੀ ਭੇਜੀ।

1. ਆਖਰੀ ਕਦਮ, ਵੇਖੀਏ ਕਿ LLM ਸਮਝਦਾ ਹੈ ਕਿ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ ਜਾਂ ਨਹੀਂ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

    - ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਗੁੰਮ੍ਹੇ।
    - ਹਰ ਟੂਲ ਕਾਲ ਲਈ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਨੂੰ ਪਾਰਸ ਕੀਤਾ ਅਤੇ MCP ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸੇਰਵਰ ਉੱਤੇ ਟੂਲ ਕਾਲ ਕੀਤਾ। ਆਖਿਰਕਾਰ ਨਤੀਜਾ ਛਪਾਇਆ।

ਪੂਰਾ ਕੋਡ:

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
    // ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਬੇਨਤੀਆਂ ਨੂੰ ਚਲਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਸੰਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ
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

ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਰਲ ਪ੍ਰਾਕ੍ਰਿਤਿਕ ਭਾਸ਼ਾ ਪ੍ਰਾਂਪਟਾਂ ਵਰਤੀ MCP ਸੇਰਵਰ ਦੇ ਟੂਲਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ
- LangChain4j ਫਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
  - ਜਦ ਲੋੜ ਹੋਵੇ, ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨੂੰ ਟੂਲ ਕਾਲਾਂ ਵਿੱਚ ਬਦਲਣਾ
  - LLM ਦੇ ਫੈਸਲੇ ਅਨੁਸਾਰ ਯੋਗ MCP ਟੂਲ ਕਾਲ ਕਰਨਾ
  - LLM ਅਤੇ MCP ਸੇਰਵਰ ਦਰਮਿਆਨ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
- `bot.chat()` ਮੈਥਡ ਮੁੜ ਪ੍ਰਾਕ੍ਰਿਤਿਕ ਭਾਸ਼ਾ ਜਵਾਬ ਦਿੰਦਾ ਹੈ, ਜਿਹੜਾ MCP ਟੂਲ ਡੂੰਘਾਈ ਦੇ ਨਤੀਜੇ ਵੀ ਸ਼ਾਮਿਲ ਕਰ ਸਕਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਇਕ ਸੁਚਾਰੂ ਯੂਜ਼ਰ ਅਨੁਭਵ ਦਿੰਦਾ ਹੈ ਜਿੱਥੇ ਯੂਜ਼ਰਾਂ ਨੂੰ ਅੰਦਰਲੇ MCP ਇੰਪਲਿਮੈਂਟੇਸ਼ਨ ਬਾਰੇ ਜਾਣਨ ਦੀ ਲੋੜ ਨਹੀਂ ਰਹਿੰਦੀ

ਪੂਰਾ ਕੋਡ ਉਦਾਹਰਣ:

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

ਇੱਥੇ ਜ਼ਿਆਦਾਤਰ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨਾਲ LLM ਨੂੰ ਕਾਲ ਕਰਾਂਗੇ, ਫਿਰ ਜਵਾਬ ਦਾ ਪ੍ਰੋਸੈਸ ਕਰਾਂਗੇ ਕਿ ਕੀ ਕੋਈ ਟੂਲ ਕਾਲ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਜੇ ਹਾਂ, ਤਾਂ ਅਸੀਂ ਉਹ ਟੂਲ ਕਾਲ ਕਰਾਂਗੇ ਅਤੇ LLM ਨਾਲ ਗੱਲਬਾਤ जारी ਰੱਖਾਂਗੇ ਜੱਥੋਂ ਤੱਕ ਹੋਰ ਟੂਲ ਕਾਲਾਂ ਦੀ ਲੋੜ ਨਾ ਰਹਿ ਜਾਵੇ ਅਤੇ ਸਾਨੂੰ ਅੰਤਿਮ ਜਵਾਬ ਮਿਲ ਜਾਵੇ।

ਅਸੀਂ LLM ਨੂੰ ਕਈ ਵਾਰੀ ਕਾਲ ਕਰਾਂਗੇ, ਇਸ ਲਈ ਅਸੀਂ ਇੱਕ ਫੰਕਸ਼ਨ ਡਿਫ਼ਾਈਨ ਕਰੀਏ ਜੋ LLM ਕਾਲ ਦਾ ਸੰਭਾਲੇਗਾ। ਆਪਣੇ `main.rs` ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਫੰਕਸ਼ਨ ਜੋੜੋ:

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

ਇਹ ਫੰਕਸ਼ਨ LLM ਕਲਾਇੰਟ, ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ (ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਿਲ ਹੈ), MCP ਸਰਵਰ ਤੋਂ ਟੂਲਾਂ ਨੂੰ ਲੈਂਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਵਾਪਸ ਕਰਦਾ ਹੈ।
LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਵਿੱਚ `choices` ਦਾ ਇੱਕ ਐਰੇ ਹੁੰਦਾ ਹੈ। ਸਾਨੂੰ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਕਿਰਿਆਵਦਾਰ ਕਰਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਦੇਖਿਆ ਜਾ ਸਕੇ ਕਿ ਕੋਈ `tool_calls` ਮੌਜੂਦ ਹਨ ਜਾਂ ਨਹੀਂ। ਇਹ ਸਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ LLM ਕਿਸੇ ਖਾਸ ਟੂਲ ਨੂੰ ਬਿਨੈ ਨਾਲ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰ ਰਿਹਾ ਹੈ। LLM ਜਵਾਬ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਆਪਣੀ `main.rs` ਫ਼ਾਇਲ ਦੇ ਨੀਵੇਂ ਹਿੱਸੇ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ:

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

    // ਜੇ ਮੌਜੂਦ ਹੈ ਤਾਂ ਸਮੱਗਰੀ ਛਾਪੋ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲੋ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ਸਹਾਇਕ ਸੁਨੇਹਾ ਸ਼ਾਮਲ ਕਰੋ

        // ਹਰ ਇੱਕ ਟੂਲ ਕਾਲ ਨੂੰ ਚੱਲਾਓ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ਸੰਦ ਦੇ ਨਤੀਜੇ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ਟੂਲ ਦੇ ਨਤੀਜਿਆਂ ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖੋ
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

ਜੇਕਰ `tool_calls` ਮੌਜੂਦ ਹਨ, ਤਾਂ ਇਹ ਟੂਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਦਾ ਹੈ, ਟੂਲ ਬੇਨਤੀ ਦੇ ਨਾਲ MCP ਸਰਵਰ ਨੂੰ ਕੌਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਗੱਲਬਾਤ ਦੇ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰਦਾ ਹੈ। ਫਿਰ ਇਹ LLM ਨਾਲ ਗੱਲਬਾਤ ਨੂੰ جاري ਰੱਖਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਸਹਾਇਕ ਦੇ ਜਵਾਬ ਅਤੇ ਟੂਲ ਕਾਲ ਨਤੀਜਿਆਂ ਨਾਲ ਅਪਡੇਟ ਕਰਦਾ ਹੈ।

MCP ਕਾਲਾਂ ਲਈ LLM ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੇ ਗਏ ਟੂਲ ਕਾਲ ਜਾਣਕਾਰੀ ਨੂੰ ਕੱਢਣ ਲਈ, ਸਾਨੂੰ ਇੱਕ ਹੋਰ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕਰਨਾ ਪਵੇਗਾ ਜੋ ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦੀ ਹਰ ਚੀਜ਼ ਨੂੰ ਕੱਢਦਾ ਹੈ। ਆਪਣੀ `main.rs` ਫ਼ਾਇਲ ਦੇ ਦਰ ਤਹਿਤ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ:

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

ਸਾਰੇ ਹਿੱਸੇ ਠੀਕ ਢੰਗ ਨਾਲ ਜੁੜ ਜਾਣ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ ਹੁਣ ਪਹਿਲਾਂ ਉਪਭੋਗਤਾ ਪ੍ਰਾਰੰਭ訊 ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ LLM ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਅਪਡੇਟ ਕਰੋ:

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

ਇਹ ਸ਼ੁਰੂਆਤੀ ਉਪਭੋਗਤਾ ਪ੍ਰਾਰੰਭ訊 ਨੂੰ ਦੋ ਨੰਬਰਾਂ ਦੇ ਜੋੜ ਲਈ LLM ਨੂੰ ਪੁੱਛੇਗਾ, ਅਤੇ ਜਵਾਬ ਨੂੰ ਪ੍ਰਕਿਰਿਆਵਦਾਰ ਕਰਦੇ ਹੋਏ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤਰੀਕੇ ਨਾਲ ਹੇਠਾਂ ਲਿਆਵੇਗਾ।

ਵਧੀਆ, ਤੁਸੀਂ ਇਹ ਕਰ ਲਿਆ!

## ਕੰਮ

ਅਭਿਆਸ ਤੋਂ ਕੋਡ ਲੈ ਕੇ ਸਰਵਰ ਨੂੰ ਹੋਰ ਕਈ ਟੂਲਾਂ ਨਾਲ ਵਿਕਸਤ ਕਰੋ। ਫਿਰ LLM ਵਾਲਾ ਇੱਕ ਕਲਾਇੰਟ ਬਣਾਓ, ਬਿਲਕੁਲ ਅਭਿਆਸ ਦੀ ਤਰ੍ਹਾਂ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਾਰੰਭ訊ਾਂ ਨਾਲ ਇਸਦੀ ਜਾਂਚ ਕਰੋ ਤਾਂ ਜੋ ਇਹ ਯਕੀਨੀ ਬਣੇ ਕਿ ਤੁਹਾਡਾ ਸਾਰਾ ਸਰਵਰ ਟੂਲ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਕਾਲ ਹੁੰਦਾ ਹੈ। ਕਲਾਇੰਟ ਬਣਾਉਣ ਦਾ ਇਹ ਤਰੀਕਾ ਮਤਲਬ ਹੈ ਕਿ ਅੰਤ ਉਪਭੋਗਤਾ ਦਾ ਸਾਰੇ ਉਪਭੋਗਤਾ ਤਜਰਬਾ ਬਹੁਤ ਵਧੀਆ ਹੋਵੇਗਾ ਕਿਉਂਕਿ ਉਹ ਜੁਸਟ ਕਲਾਇੰਟ ਕਮਾਂਡਾਂ ਦੀ ਥਾਂ ਪ੍ਰਾਰੰਭ訊ਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਵੀ MCP ਸਰਵਰ ਕਾਲ ਹੋਣ ਤੋਂ ਬੇਪੜ੍ਹ ਰਹੇਗਾ।

## ਹੱਲ

[Solution](./solution/README.md)

## ਮੁੱਖ ਸਿਖਲਾਈਆਂ

- ਆਪਣੇ ਕਲਾਈਂਟ ਵਿੱਚ LLM ਦੀ ਸ਼ਾਮਿਲੀਅਤ ਉਪਭੋਗਤਾਵਾਂ ਨੂੰ MCP ਸਰਵਰਾਂ ਨਾਲ ਬਿਹਤਰ ਤਰੀਕੇ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਦਾ ਮੌਕਾ ਦਿੰਦੀ ਹੈ।
- MCP ਸਰਵਰ ਜਵਾਬ ਨੂੰ LLM ਨੂੰ ਸਮਝ ਆਉਣ ਵਾਲੀ ਚੀਜ਼ ਵਿੱਚ ਬਦਲਣਾ ਜਰੂਰੀ ਹੁੰਦਾ ਹੈ।

## ਨਮੂਨੇ

- [ਜਾਵਾ ਕੈਲਕੁਲੇਟਰ](../samples/java/calculator/README.md)
- [.Net ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)
- [ਜਾਵਾਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/javascript/README.md)
- [ਟਾਈਪਸਕ੍ਰਿਪਟ ਕੈਲਕੁਲੇਟਰ](../samples/typescript/README.md)
- [ਪਾਇਥਾਨ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/python)
- [ਰਸਟ ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/rust)

## ਅਤਿਰਿਕਤ ਸਰੋਤ

## ਅਗਲਾ ਕੀ

- ਅਗਲਾ: [Visual Studio Code ਦੀ ਵਰਤੋਂ ਨਾਲ ਇੱਕ ਸਰਵਰ ਨੂੰ ਖਪਤ ਕਰਨਾ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰਾ**:  
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪੈਦਾਂ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤਫ਼ਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->