# LLM ਨਾਲ ਕੁਲਾਇੰਟ ਬਣਾਉਣਾ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਵیکھਿਆ ਕਿ ਕਿਵੇਂ ਸਰਵਰ ਅਤੇ ਕੁਲਾਇੰਟ ਬਣਾਏ ਜਾਂਦੇ ਹਨ। ਕੁਲਾਇੰਟ ਸਰਵਰ ਨੂੰ ਖੁਲਾ ਤੌਰ 'ਤੇ ਕਾਲ ਕਰ ਸਕਦਾ ਸੀ ਤਾਂ ਕਿ ਇਸ ਦੇ ਟੂਲ, ਸਰੋਤ ਅਤੇ ਪ੍ਰਾਂਪਟ ਸੂਚੀਬੱਧ ਕੀਤੇ ਜਾਂ। ਪਰ ਇਹ ਬਹੁਤ ਪ੍ਰਯੋਗਿਕ ਤਰੀਕਾ ਨਹੀਂ ਹੈ। ਤੁਹਾਡੇ ਉਪਭੋਗਤਾ ਏਜੰਟਿਕ ਯੁੱਗ ਵਿੱਚ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਪ੍ਰਾਂਪਟ ਵਰਤਣ ਅਤੇ LLM ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਦੀ ਉਮੀਦ ਰੱਖਦੇ ਹਨ। ਉਹਨਾਂ ਨੂੰ ਫਰਕ ਨਹੀਂ ਪੈਂਦਾ ਕਿ ਤੁਸੀਂ MCP ਨੂੰ ਆਪਣੀਆਂ ਸਮਰਥਾਵਾਂ ਸਟੋਰ ਕਰਨ ਲਈ ਵਰਤਦੇ ਹੋ ਜਾਂ ਨਹੀਂ; ਉਹ ਸਿਰਫ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਗੱਲਬਾਤ ਕਰਨ ਦੀ ਉਮੀਦ ਕਰਦੇ ਹਨ। ਤਾਂ ਫਿਰ ਅਸੀਂ ਇਹ ਮਸਲਾ ਕਿਵੇਂ ਹੱਲ ਕਰੀਏ? ਹੱਲ ਇਹ ਹੈ ਕਿ ਕੁਲਾਇੰਟ ਵਿੱਚ ਇੱਕ LLM ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਵੇ।

## ਝਲਕ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ LLM ਨੂੰ ਆਪਣੇ ਕੁਲਾਇੰਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨ ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਾਂਗੇ ਅਤੇ ਵਿਖਾਵਾਂਗੇ ਕਿ ਇਹ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾ ਲਈ ਬਹੁਤ ਬਿਹਤਰ ਅਨੁਭਵ ਕਿਵੇਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਕਰ ਸਕੋਗੇ:

- LLM ਨਾਲ ਕੁਲਾਇੰਟ ਬਣਾਉਣਾ।
- LLM ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨਾਲ ਬਿਨਾ ਰੁਕਾਵਟ ਮੁਲਾਕਾਤ ਕਰਨਾ।
- ਕੁਲਾਇੰਟ ਪਾਸੇ ਬਿਹਤਰ ਅੰਤਮ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਨਾ।

## ਤਰੀਕਾ

ਚਲੋ ਇਸ ਤਰੀਕੇ ਨੂੰ ਸਮਝਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ ਜਿਹੜਾ ਅਸੀਂ ਲੈਣਾ ਹੈ। LLM ਸ਼ਾਮਲ ਕਰਨਾ ਸੌਖਾ ਲੱਗਦਾ ਹੈ, ਪਰ ਕੀ ਅਸੀਂ ਪੱਕੇ ਤੌਰ 'ਤੇ ਇਹ ਕਰਾਂਗੇ?

ਇੱਥੇ ਕੁਲਾਇੰਟ ਕਿਵੇਂ ਸਰਵਰ ਨਾਲ ਸੰਪਰਕ ਕਰੇਗਾ:

1. ਸਰਵਰ ਨਾਲ ਕਨੈਕਸ਼ਨ ਸਥਾਪਿਤ ਕਰਨਾ।

1. ਸਮਰਥਾਵਾਂ, ਪ੍ਰਾਂਪਟ, ਸਰੋਤ ਅਤੇ ਟੂਲ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ ਅਤੇ ਉਹਨਾਂ ਦਾ ਸਕੀਮਾ ਸੁਰੱਖਿਅਤ ਕਰਨਾ।

1. ਇੱਕ LLM ਸ਼ਾਮਲ ਕਰਨਾ ਅਤੇ ਸੁਰੱਖਿਅਤ ਸਮਰਥਾਵਾਂ ਅਤੇ ਉਹਨਾਂ ਦਾ ਸਕੀਮਾ LLM ਨੂੰ ਸਮਝ ਆਉਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਪਾਸ ਕਰਨਾ।

1. ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨੂੰ LLM ਨੂੰ ਪਾਸ ਕਰਨਾ ਅਤੇ ਕੁਲਾਇੰਟ ਦੁਆਰਾ ਸੂਚੀਬੱਧ ਟੂਲ ਨਾਲ ਸਾਂਝਾ ਕਰਨਾ।

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਸਮਝ ਗਏ ਕਿ ਅਸੀਂ ਅੱਧਿਕ ਉੱਚ ਸਤਰ 'ਤੇ ਇਹ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਚਲੋ ਹੇਠਾਂ ਦਿੱਤੀ ਕਸਰਤ ਵਿੱਚ ਇਸ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ।

## ਕਸਰਤ: LLM ਨਾਲ ਕੁਲਾਇੰਟ ਬਣਾਉਣਾ

ਇਸ ਕਸਰਤ ਵਿੱਚ, ਅਸੀਂ ਆਪਣੇ ਕੁਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਲ ਕਰਨਾ ਸਿੱਖਾਂਗੇ।

### GitHub Personal Access Token ਨਾਲ ਪ੍ਰਮਾਣਿਕਤਾ

GitHub ਟੋਕਨ ਬਣਾਉਣਾ ਇੱਕ ਸਧਾਰਣ ਪ੍ਰਕਿਰਿਆ ਹੈ। ਐਵੇਂ ਕਰ ਸਕਦੇ ਹੋ:

- GitHub Settings ਤੇ ਜਾਓ – ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਸਰਵੋਚ ਦਾਹਿਨੇ ਕੋਨੇ ਵਿੱਚ ਅਤੇ Settings ਚੁਣੋ।
- Developer Settings ਤੇ ਜਾਂਚ ਕਰੋ – ਥੱਲੇ ਸਕ੍ਰੋਲ ਕਰੋ ਅਤੇ Developer Settings ਤੇ ਕਲਿੱਕ ਕਰੋ।
- Personal Access Tokens ਚੁਣੋ – Fine-grained tokens ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਫਿਰ Generate new token ਤੇ ਕਲਿੱਕ ਕਰੋ।
- ਆਪਣਾ ਟੋਕਨ ਸੰਰਚਿਤ ਕਰੋ – ਇੱਕ ਨੋਟ ਜੋੜੋ, ਸਮਾਪਤੀ ਮਿਤੀ ਸੈੱਟ ਕਰੋ ਅਤੇ ਜ਼ਰੂਰੀ ਸکوਪ (ਪਰਮੀਸ਼ਨ) ਚੁਣੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ ਮਾਡਲਜ਼ ਦੀ ਪਰਮਿਸ਼ਨ ਜ਼ਰੂਰ ਜੋੜੋ।
- ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਨਾਲੇ ਕਾਪੀ ਕਰੋ – Generate token ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਉਸਦੇ ਬਾਅਦ ਤੁਰੰਤ ਇਸ ਨੂੰ ਕਾਪੀ ਕਰੋ, ਕਿਉਂਕਿ ਦੁਬਾਰਾ ਇਹ ਨਹੀਂ ਵੇਖਿਆ ਜਾ ਸਕਦਾ।

### -1- ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰੋ

ਚਲੋ ਪਹਿਲਾਂ ਆਪਣਾ ਕੁਲਾਇੰਟ ਬਣਾਈਏ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ ਜ਼ੋਡ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ

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

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਲੋੜੀਂਦੇ ਲਾਇਬਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕਲਾਸ ਬਣਾਈ ਜਿਸ ਵਿੱਚ ਦੋ ਮੈਂਬਰ ਹਨ, `client` ਅਤੇ `openai`, ਜੋ ਸਾਨੂੰ ਕੁਲਾਇੰਟ ਨੂੰ ਮੈਨੇਜ ਕਰਨ ਅਤੇ LLM ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਦੇਣਗੇ।
- ਆਪਣੇ LLM ਇੰਸਟੈਂਸ ਨੂੰ GitHub ਮਾਡਲਜ਼ ਵਰਤਣ ਲਈ ਕੰਫਿਗਰ ਕੀਤਾ `baseUrl` ਨੂੰ ਇੰਫਰਨਸ ਏਪੀਆਈ ਵੱਲ ਦਿਖਾ ਕੇ।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ਕਨੈਕਸ਼ਨ ਲਈ ਸਰਵਰ ਪੈਰਾਮੀਟਰ ਬਣਾਓ
server_params = StdioServerParameters(
    command="mcp",  # ਚਲਾਉਣਯੋਗ
    args=["run", "server.py"],  # ਵਿਕਲਪਿਕ ਕਮਾਂਡ ਲਾਈਨ ਜ਼ਰੂਰੀਆਂ
    env=None,  # ਵਿਕਲਪਿਕ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ਕਨੈਕਸ਼ਨ ਸ਼ੁਰੂ ਕਰੋ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਲਈ ਲੋੜੀਂਦੇ ਲਾਇਬਰੇਰੀਜ਼ ਇੰਪੋਰਟ ਕੀਤੀਆਂ
- ਇੱਕ ਕੁਲਾਇੰਟ ਬਣਾਇਆ

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

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `pom.xml` ਫਾਇਲ ਵਿੱਚ LangChain4j ਡੀਪੈਂਡੇੰਸੀਜ਼ ਸ਼ਾਮਲ ਕਰਨੀ ਪਵੇਗੀ। MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ GitHub ਮਾਡਲਜ਼ ਸਹਾਇਤਾ ਲਈ ਇਹਨਾਂ ਡੀਪੈਂਡੇੰਸੀਜ਼ ਨੂੰ ਸ਼ਾਮਲ ਕਰੋ:

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

ਫਿਰ ਆਪਣੀ ਜਾਵਾ ਕੁਲਾਇੰਟ ਕਲਾਸ ਬਣਾਓ:

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
    
    public static void main(String[] args) throws Exception {        // LLM ਨੂੰ GitHub ਮਾਡਲਾਂ ਨੂੰ ਵਰਤਣ ਲਈ ਸੰਰਚਿਤ ਕਰੋ
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

        // MCP ਕਲਾਇਟ ਬਣਾਓ
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- **LangChain4j ਡੀਪੈਂਡੇੰਸੀਜ਼ ਸ਼ਾਮਲ ਕੀਤੀਆਂ**: MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ, OpenAI ਅਧਿਕਾਰਿਕ ਕੁਲਾਇੰਟ ਅਤੇ GitHub ਮਾਡਲਜ਼ ਲਈ
- **LangChain4j ਲਾਇਬਰੇਰੀਜ਼ ਆਯਾਤ ਕੀਤੀਆਂ**: MCP ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਅਤੇ OpenAI ਚੈਟ ਮਾਡਲ ਫੰਕਸ਼ਨਾਲਟੀ ਲਈ
- **`ChatLanguageModel` ਬਣਾਇਆ**: ਜੋ ਤੁਹਾਡੇ GitHub ਟੋਕਨ ਨਾਲ GitHub ਮਾਡਲਜ਼ ਵਰਤਦਾ ਹੈ
- **HTTP ਟਰਾਂਸਪੋਰਟ ਸੈਟ ਕੀਤਾ**: Server-Sent Events (SSE) ਵਰਤ ਕੇ MCP ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਨ ਲਈ
- **MCP ਕੁਲਾਇੰਟ ਬਣਾਇਆ**: ਜੋ ਸਰਵਰ ਨਾਲ ਸਾਂਝਾ ਸੰਚਾਰ ਸੰਭਾਲੇਗਾ
- **LangChain4j ਦੇ ਬਿਲਟ-ਇਨ MCP ਸਪੋਰਟ ਨੂੰ ਵਰਤਿਆ**: ਜੋ LLM ਅਤੇ MCP ਸਰਵਰਾਂ ਵਿਚਕਾਰ ਇੰਟਿਗ੍ਰੇਸ਼ਨ ਸੌਖਾ ਕਰਦਾ ਹੈ

#### Rust

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Rust-ਆਧਾਰਿਤ MCP ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ। ਜੇਕਰ ਨਹੀਂ ਹੈ, ਤਾਂ ਸਰਵਰ ਬਣਾਉਣ ਲਈ [01-first-server](../01-first-server/README.md) ਪਾਠ ਵਾਪਸ ਵੇਖੋ।

ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ Rust MCP ਸਰਵਰ ਹੋਵੇ, ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ ਅਤੇ ਉਸੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ ਜਿੱਥੇ ਸਰਵਰ ਹੈ। ਫਿਰ ਨਵੀਂ LLM ਕੁਲਾਇੰਟ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ਆਪਣੀ `Cargo.toml` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਡੀਪੈਂਡੇੰਸੀਜ਼ ਜੋੜੋ:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI ਲਈ ਕੋਈ ਅਧਿਕਾਰਿਕ Rust ਲਾਇਬਰੇਰੀ ਨਹੀਂ ਹੈ। ਪਰ, `async-openai` ਕਰੇਟ ਇੱਕ [ਕਮਿਊਨਿਟੀ ਦੁਆਰਾ ਸੰਭਾਲੀ ਜਾਣ ਵਾਲੀ ਲਾਇਬਰੇਰੀ](https://platform.openai.com/docs/libraries/rust#rust) ਹੈ ਜੋ ਆਮ ਤੌਰ ਤੇ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।

`src/main.rs` ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਇਸਦਾ ਸਮੱਗਰੀ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਬਦਲ ਦਿਓ:

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

    // ਕਰੋ: MCP ਟੂਲ ਲਿਸਟਿੰਗ ਪ੍ਰਾਪਤ ਕਰੋ

    // ਕਰੋ: ਟੂਲ ਕਾਲਾਂ ਨਾਲ LLM ਗੱਲਬਾਤ

    Ok(())
}
```

ਇਹ ਕੋਡ ਇੱਕ ਮੂਲ Rust ਐਪਲੀਕੇਸ਼ਨ ਸੈੱਟਅੱਪ ਕਰਦਾ ਹੈ ਜੋ MCP ਸਰਵਰ ਅਤੇ GitHub ਮਾਡਲਜ਼ ਨਾਲ LLM ਸੰਪਰਕ ਲਈ ਜੋੜਦਾ ਹੈ।

> [!IMPORTANT]
> ਐਪ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਆਪਣਾ GitHub ਟੋਕਨ ਵਰਦੋਂ `OPENAI_API_KEY` ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਓ।

ਵਧੀਆ, ਅਗਲਾ ਕਦਮ ਹੈ ਸਰਵਰ ਉੱਤੇ ਸਮਰਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ।

### -2- ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ

ਹੁਣ ਅਸੀਂ ਸਰਵਰ ਨਾਲ ਕਨੈਕਟ ਕਰਕੇ ਇਸ ਦੀ ਸਮਰਥਾਵਾਂ ਬਾਰੇ ਪੁੱਛਾਂਗੇ:

#### Typescript

ਉਸੀ ਕਲਾਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੇ ਮੈਥਡ ਸ਼ਾਮਲ ਕਰੋ:

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

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ ਕੋਡ `connectToServer` ਸ਼ਾਮਲ ਕੀਤਾ।
- ਇੱਕ `run` ਮੈਥਡ ਬਣਾਇਆ ਜੋ ਸਾਡੀ ਐਪ ਦੇ ਫ਼ਲੋ ਨੂੰ ਸੰਭਾਲਦਾ ਹੈ। ਹਾਲੇ ਤੱਕ ਇਹ ਸਿਰਫ ਟੂਲ ਸੂਚੀਬੱਧ ਕਰਦਾ ਹੈ ਪਰ ਅਸੀਂ ਇਸ ਵਿੱਚ ਹੋਰ ਸ਼ਾਮਲ ਕਰਾਂਗੇ।

#### Python

```python
# ਉਪਲਬਧ ਸਰੋਤਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ਉਪਲਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ਅਸੀਂ ਇਹ ਜੁੜਿਆ:

- ਸਰੋਤਾਂ ਅਤੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਬਣਾਈ ਅਤੇ ਛਾਪੀ। ਟੂਲਜ਼ ਲਈ ਅਸੀਂ `inputSchema` ਵੀ ਸੂਚੀਬੱਧ ਕਰਦੇ ਹਾਂ ਜੋ ਬਾਅਦ ਵਿੱਚ ਵਰਤਾਂਗੇ।

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

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਸਰਵਰ ਉੱਤੇ ਉਪਲੱਬਧ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਬਣਾਈ
- ਹਰ ਟੂਲ ਲਈ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਸਕੀਮਾ ਦਿੱਤਾ। ਐਹੋ ਜੀਸਾ ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਟੂਲ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤੋਂ ਵਿੱਚ ਲਿਆਉਣਗੇ।

#### Java

```java
// ਇੱਕ ਟੂਲ ਪ੍ਰਦਾਤਾ ਬਣਾਓ ਜੋ ਆਪਣੇ ਆਪ MCP ਟੂਲਾਂ ਨੂੰ ਖੋਜਦਾ ਹੈ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ਟੂਲ ਪ੍ਰਦਾਤਾ ਆਪਣੇ ਆਪ ਇਹ ਕੰਮ ਸੰਭਾਲਦਾ ਹੈ:
// - MCP ਸਰਵਰ ਤੋਂ ਉਪਲੱਬਧ ਟੂਲਾਂ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ
// - MCP ਟੂਲ ਸਕੀਮਾਂ ਨੂੰ LangChain4j ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣਾ
// - ਟੂਲ ਦੀ ਕਾਰਜਕਿਰਤੀ ਅਤੇ ਜਵਾਬਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰਨਾ
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- `McpToolProvider` ਬਣਾਇਆ ਜੋ MCP ਸਰਵਰ ਤੋਂ ਸਾਰੇ ਟੂਲ ਖੋਜ ਕੇ ਰਜਿਸਟਰ ਕਰਦਾ ਹੈ
- ਇਹ ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ MCP ਟੂਲ ਸਕੀਮਾ ਅਤੇ LangChain4j ਦੇ ਟੂਲ ਫਾਰਮੈਟ ਵਿਚਕਾਰ ਬਦਲਾਅ ਸੈਲਫ-ਮੇਨੇਜ ਕਰਦਾ ਹੈ
- ਇਹ ਤਰੀਕਾ ਹੱਥੋਂ-ਹੱਥ ਟੂਲ ਸੂਚੀ ਅਤੇ ਬਦਲਾਅ ਦੀ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਛੁਪਾ ਦਿੰਦਾ ਹੈ

#### Rust

MCP ਸਰਵਰ ਤੋਂ ਟੂਲ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ `list_tools` ਮੈਥਡ ਵਰਤੋਂ ਕਰਦੇ ਹੋ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਵਿੱਚ MCP ਕੁਲਾਇੰਟ ਸੈੱਟਅੱਪ ਤੋਂ ਬਾਅਦ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

```rust
// MCP ਟੂਲ ਸੂਚੀ ਪ੍ਰਾਪਤ ਕਰੋ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਨੂੰ LLM ਟੂਲਜ਼ ਵਿੱਚ ਬਦਲਣਾ

ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਲਿਸਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਅਗਲਾ ਕਦਮ ਇਹ ਹੈ ਕਿ ਉਹਨਾਂ ਨੂੰ ਇਸ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾਵੇ ਜੋ LLM ਨੂੰ ਸਮਝ ਆਵੇ। ਜਦੋਂ ਅਸੀਂ ਐਹੋ ਕਰਾਂਗੇ ਤਾਂ ਅਸੀਂ ਇਹ ਸਮਰਥਾਵਾਂ LLM ਲਈ ਟੂਲਜ਼ ਵਜੋਂ ਪੇਸ਼ ਕਰ ਸਕਾਂਗੇ।

#### TypeScript

1. MCP ਸਰਵਰ ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਸਮਝ ਆਉਣ ਵਾਲੀ ਟੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // ਇਨਪੁਟ_ਸਕੀਮਾ ਅਧਾਰਿਤ ਇੱਕ ਜੋਡ ਸਕੀਮਾ ਬਣਾਓ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // ਜ਼ਰੂਰੀ ਤੌਰ 'ਤੇ ਕਿਸਮ "ਫੰਕਸ਼ਨ" ਸੈੱਟ ਕਰੋ
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

    ਉਪਰ ਦਿੱਤਾ ਕੋਡ MCP ਸਰਵਰ ਤੋਂ ਜਵਾਬ ਲੈਂਦਾ ਹੈ ਅਤੇ ਉਸਨੂੰ LLM ਲਈ ਟੂਲ ਡਿਫਿਨੀਸ਼ਨ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।

1. ਹੁਣ `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੀਏ ਤਾਂ ਜੋ ਸਰਵਰ ਸਮਰਥਾਵਾਂ ਦੀ ਸੂਚੀ ਬਣੇ:

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

    ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ ਹੈ ਜੋ ਨਤੀਜੇ ਵਿੱਚੋਂ ਹਰ ਐਂਟਰੀ ਤੇ `openAiToolAdapter` ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ।

#### Python

1. ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਹੇਠਾਂ ਦਿੱਤਾ ਕਨਵਰਟਰ ਫੰਕਸ਼ਨ ਬਣਾਈਏ

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

    ਇਸ ਫੰਕਸ਼ਨ `convert_to_llm_tools` ਵਿੱਚ ਅਸੀਂ MCP ਟੂਲ ਜਵਾਬ ਲੈ ਕੇ ਇਸਨੂੰ LLM ਲਈ ਸਮਝ ਆਉਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦੇ ਹਾਂ।

1. ਫਿਰ, ਆਪਣੇ ਕੁਲਾਇੰਟ ਕੋਡ ਨੂੰ ਇਸ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਲਈ ਅਪਡੇਟ ਕਰੀਏ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ਇੱਥੇ ਅਸੀਂ `convert_to_llm_tool` ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ MCP ਟੂਲ ਜਵਾਬ ਨੂੰ ਬਾਅਦ ਵਿੱਚ LLM ਨੂੰ ਫੀਡ ਕਰਨ ਯੋਗ ਬਣਾ ਸਕੀਏ।

#### .NET

1. MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਸਮਝ ਆਉਣ ਯੋਗ ਸਮੱਗਰੀ ਵਿੱਚ ਬਦਲਣ ਲਈ ਕੋਡ ਜੋੜੋ:

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

- `ConvertFrom` ਫੰਕਸ਼ਨ ਬਣਾਇਆ ਜੋ ਨਾਮ, ਵੇਰਵਾ ਅਤੇ ਇਨਪੁੱਟ ਸਕੀਮਾ ਲੈਂਦਾ ਹੈ।
- ਕਾਰਜ ਪ੍ਰਵਰਤਨ ਕੀਤਾ ਜੋ ਇੱਕ FunctionDefinition ਬਣਾਉਂਦਾ ਹੈ ਜੋ ChatCompletionsDefinition ਨੂੰ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਆਖਰੀ LLM ਲਈ ਸਮਝਦਾਰ ਹੁੰਦਾ ਹੈ।

1. ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਮੌਜੂਦਾ ਕੋਡ ਨੂੰ ਅਪਡੇਟ ਕਰਾਂਗੇ ਤਾਂ ਜੋ ਇਸ ਫੰਕਸ਼ਨ ਦਾ ਲਾਭ ਲੈ ਸਕੀਏ:

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
// ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰਐਕਸ਼ਨ ਲਈ ਬੋਟ ਇੰਟਰਫੇਸ ਬਣਾਓ
public interface Bot {
    String chat(String prompt);
}

// LLM ਅਤੇ MCP ਟੂਲਜ਼ ਨਾਲ AI ਸੇਵਾ ਕਨਫਿਗਰ ਕਰੋ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਇੰਟਰਐਕਸ਼ਨ ਲਈ ਸਾਦਾ `Bot` ਇੰਟਰਫੇਸ ਵਿਆਖਿਆ ਕੀਤੀ
- LangChain4j ਦੇ `AiServices` ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜੋ ਆਟੋਮੈਟਿਕ ਤੌਰ ਤੇ LLM ਨੂੰ MCP ਟੂਲ ਪ੍ਰੋਵਾਈਡਰ ਨਾਲ ਬਾਈਂਡ ਕਰਦਾ ਹੈ
- ਫ੍ਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਟੂਲ ਸਕੀਮਾ ਬਦਲਾਅ ਅਤੇ ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ ਸੰਭਾਲਦਾ ਹੈ
- ਇਸ ਤਰੀਕੇ ਨਾਲ ਹੱਥੋਂ-ਹੱਥ ਟੂਲ ਬਦਲਣ ਨੂੰ ਖਤਮ ਕਰ ਦਿੱਤਾ - LangChain4j MCP ਟੂਲਜ਼ ਨੂੰ LLM-ਮੈਚਿੰਗ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਦੀ ਸਾਰੀ ਮੁਸ਼ਕਲਾਈ ਸੰਭਾਲਦਾ ਹੈ

#### Rust

MCP ਟੂਲ ਜਵਾਬ ਨੂੰ LLM ਲਈ ਸਮਝ ਆਉਣ ਵਾਲੇ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਣ ਲਈ ਅਸੀਂ ਇਕ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਟੂਲ ਲਿਸਟ ਨੂੰ ਫਾਰਮੈਟ ਕਰੇਗਾ। ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਆਪਣੀ `main.rs` ਫਾਇਲ ਵਿੱਚ `main` ਫੰਕਸ਼ਨ ਦੇ ਹੇਠਾਂ ਜੋੜੋ। ਇਹ LLM ਨੂੰ ਰਿਕਵੈਸਟ ਭੇਜਣ ਵੇਲੇ ਕਾਲ ਕੀਤਾ ਜਾਏਗਾ:

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

ਵਧੀਆ, ਹੁਣ ਅਸੀਂ ਕੋਈ ਯੂਜ਼ਰ ਅਨੁਰੋਧ ਸੰਭਾਲਣ ਲਈ ਤਿਆਰ ਹਾਂ, ਆਓ ਇਹ ਅਗਲਾ ਕੰਮ ਕਰੀਏ।

### -4- ਯੂਜ਼ਰ ਪ੍ਰांਪਟ ਅਨੁਰੋਧ ਸੰਭਾਲੋ

ਇਸ ਭਾਗ ਵਿੱਚ ਅਸੀਂ ਯੂਜ਼ਰ ਦੀਆਂ ਮੰਗਾਂ ਨਿਭਾਵਾਂਗੇ।

#### TypeScript

1. ਇੱਕ ਮੈਥਡ ਜੋ LLM ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ, ਸ਼ਾਮਲ ਕਰੋ:

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
        // ਕਰਨਾ ਹੈ

        }
    }
    ```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- `callTools` ਨਾਮਕ ਮੈਥਡ ਸ਼ਾਮਲ ਕੀਤਾ।
- ਮੈਥਡ LLM ਦੇ ਜਵਾਬ ਨੂੰ ਲੈਂਦਾ ਹੈ ਅਤੇ ਵੇਖਦਾ ਹੈ ਕਿ ਕਿਸ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਣਾ ਚਾਹੀਦਾ ਹੈ, ਜੇ ਕੋਈ ਹੋਵੇ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ਟੂਲ ਨੂੰ ਕਾਲ ਕਰੋ
        }
        ```

- ਜੇ LLM ਦੱਸੇ ਕਿ ਕਿਸੇ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨਾ ਹੋਵੇ ਤਾਂ ਉਸਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ:

        ```typescript
        // 2. ਸਰਵਰ ਦੇ ਸੰਦ ਨੂੰ ਕਾਲ ਕਰੋ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ਨਤੀਜੇ ਨਾਲ ਕੁਝ ਕਰੋ
        // ਕਰਨ ਬਾਕੀ
        ```

1. `run` ਮੈਥਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ LLM ਕਾਲ ਅਤੇ `callTools` ਮੇਥਡ ਸ਼ਾਮਲ ਹੋ ਜਾਣ:

    ```typescript

    // 1. ਐੱਲਐੱਲਐੱਮ ਲਈ ਇਨਪੁਟ ਵਾਲੇ ਸੁਨੇਹੇ ਬਣਾਓ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. ਐੱਲਐੱਲਐੱਮ ਨੂੰ ਕਾਲ ਕਰਨਾ
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. ਐੱਲਐੱਲਐੱਮ ਦੇ ਜਵਾਬ ਨੂੰ ਵੇਖੋ, ਹਰ ਚੋਣ ਲਈ, ਜੱਚੋ ਕਿ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ ਕਿ ਨਹੀਂ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ਵਧੀਆ, ਸਾਰੇ ਕੋਡ ਨੂੰ ਪੂਰੀ ਤਰ੍ਹਾਂ ਵੇਖੋ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // ਸਕੀਮਾ ਦੀਪਿਰੀਖਿਆ ਲਈ zod ਇੰਪੋਰਟ ਕਰੋ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ਭਵਿੱਖ ਵਿੱਚ ਇਸ url ਨੂੰ ਬਦਲਣਾ ਪੈ ਸਕਦਾ ਹੈ: https://models.github.ai/inference
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
          // ਇੰਪੁੱਟ_ਸਕੀਮਾ ਦੇ ਆਧਾਰ ਤੇ ਇੱਕ zod ਸਕੀਮਾ ਬਣਾਓ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ਟਾਈਪ ਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ "function" ਸੈੱਟ ਕਰੋ
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
    
        // 1. LLM ਜਵਾਬ ਵਿੱਚੋਂ ਹਰ ਚੋਣ ਨੂੰ ਦੇਖੋ, ਜਾਂਚੋ ਕਿ ਕੀ ਇਸ ਵਿੱਚ ਟੂਲ ਕਾਲ ਹਨ
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

1. LLM ਕਾਲ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਇੰਪੋਰਟ ਸ਼ਾਮਲ ਕਰੋ

    ```python
    # ਲਲਮ
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
            # ਦਿਲਚਸਪ ਪੈਰਾਮੀਟਰ
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

- MCP ਸਰਵਰ ਤੋਂ ਮਿਲੇ ਫੰਕਸ਼ਨਾਂ ਨੂੰ LLM ਨੂੰ ਦਿੱਤਾ।
- ਫਿਰ LLM ਨੂੰ ਉਨ੍ਹਾਂ ਫੰਕਸ਼ਨਾਂ ਨਾਲ ਕਾਲ ਕੀਤਾ।
- ਫਿਰ ਨਤੀਜਾ ਵੇਖਿਆ ਕਿ ਕਿਸ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ, ਜੇ ਕੋਈ।
- ਅੰਤ ਵਿੱਚ ਕਾਲ ਕਰਨ ਲਈ ਫੰਕਸ਼ਨਾਂ ਦੀ ਲਿਸਟ ਦਿੱਤੀ।

1. ਆਖਰੀ ਕਦਮ, ਆਪਣੇ ਮੁੱਖ ਕੋਡ ਨੂੰ ਅਪਡੇਟ ਕਰੋ:

    ```python
    prompt = "Add 2 to 20"

    # ਐਲਐਲਐਮ ਨੂੰ ਪੁੱਛੋ ਕਿ ਸਭ ਨੂੰ ਕਿਹੜੇ ਸੰਦ, ਜੇ ਕੋਈ ਹੋਣ
    functions_to_call = call_llm(prompt, functions)

    # ਸੁਝਾਏ ਗਏ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਕਾਲ ਕਰੋ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

ਉੱਥੇ, ਇਹ ਅਖੀਰਲਾ ਕਦਮ ਸੀ, ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ ਅਸੀਂ:

- MCP ਟੂਲ ਨੂੰ `call_tool` ਰਾਹੀਂ ਕਾਲ ਕੀਤਾ ਜੋ LLM ਦੇ ਦੇਸ਼ਨਾਂ ਅਨੁਸਾਰ ਦੀ ਫੰਕਸ਼ਨ ਹੈ।
- ਟੂਲ ਕਾਲ ਦਾ ਨਤੀਜਾ MCP ਸਰਵਰ ਉੱਤੇ ਪ੍ਰਿੰਟ ਕੀਤਾ।

#### .NET

1. LLM ਪ੍ਰਾਂਪਟ ਰਿਕਵੈਸਟ ਕਰਨ ਲਈ ਕੁਝ ਕੋਡ ਵੇਖੋ:

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
- ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ `userMessage` ਬਣਾਇਆ।
- ਮਾਡਲ ਅਤੇ ਟੂਲਜ਼ ਦਰਸਾਉਂਦੇ ਵਿੱਕਲਪ ਆਬਜੈਕਟ ਤਿਆਰ ਕੀਤਾ।
- LLM ਵੱਲ ਰਿਕਵੈਸਟ ਕੀਤਾ।

1. ਇੱਕ ਆਖਰੀ ਕਦਮ, ਵੇਖੀਏ ਕਿ ਕੀ LLM ਸੋਚਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਫੰਕਸ਼ਨ ਕਾਲ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ:

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

- ਫੰਕਸ਼ਨ ਕਾਲਾਂ ਦੀ ਸੂਚੀ ਵਿੱਚ ਲੂਪ ਕੀਤਾ।
- ਹਰ ਟੂਲ ਕਾਲ ਦੇ ਲਈ ਨਾਮ ਅਤੇ ਆਰਗੁਮੈਂਟ ਪਾਰਸ ਕੀਤੇ ਅਤੇ MCP ਕਲਾਇੰਟ ਨਾਲ ਟੂਲ ਕਾਲ ਕੀਤਾ। ਆਖਰ ਨੂੰ ਨਤੀਜੇ ਪ੍ਰਿੰਟ ਕੀਤੇ।

ਪੂਰਾ ਕੋਡ ਇਹ ਹੈ:

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
    // ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਬਿਨੈਵਾਂ ਚਲਾਓ ਜੋ ਆਟੋਮੇਟਿਕ ਤੌਰ 'ਤੇ MCP ਸੰਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੀਆਂ ਹਨ
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

- MCP ਸਰਵਰ ਟੂਲਜ਼ ਨਾਲ ਸਧਾਰਨ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਪ੍ਰਾਂਪਟ ਵਰਤੇ
- LangChain4j ਫ੍ਰੇਮਵਰਕ ਆਪਣੇ ਆਪ ਸੰਭਾਲਦਾ ਹੈ:
  - ਜਦੋਂ ਲੋੜ ਹੋਵੇ, ਉਪਭੋਗਤਾ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਟੂਲ ਕਾਲਜ਼ ਵਿੱਚ ਬਦਲਣਾ
  - LLM ਦੇ ਫੈਸਲੇ ਅਨੁਸਾਰ ਸਮੁੱਚੇ MCP ਟੂਲ ਕਾਲ ਕਰਨਾ
  - LLM ਅਤੇ MCP ਸਰਵਰ ਵਿਚਕਾਰ ਗੱਲਬਾਤ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ
- `bot.chat()` ਮੈਥਡ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਵਿੱਚ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ MCP ਟੂਲਜ਼ ਦੇ ਨਤੀਜੇ ਹੋ ਸਕਦੇ ਹਨ
- ਇਹ ਤਰੀਕਾ ਬਿਨਾਂ MCP ਦੇ ਤਹਿ ਸਮਝੇ, ਬਿਨਾਂ ਰੁਕਾਵਟ ਦੇ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ

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

ਇੱਥੇ ਜ਼ਿਆਦਾਤਰ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਅਸੀਂ LLM ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨਾਲ ਕਾਲ ਕਰਾਂਗੇ, ਫਿਰ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰੋਸੈਸ ਕਰਾਂਗੇ ਕਿ ਕੋਈ ਟੂਲ ਕਾਲ ਵਾਂਝੇ ਜਾਂ ਨਹੀਂ। ਜੇ ਹਾਂ, ਤਾਂ ਉਹ ਟੂਲ ਕਾਲ ਕਰਾਂਗੇ ਅਤੇ LLM ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖਾਂਗੇ ਜਦ ਤੱਕ ਹੋਰ ਕਿਸੇ ਟੂਲ ਕਾਲ ਦੀ ਲੋੜ ਨਾ ਰਹਿ ਜਾਵੇ ਅਤੇ ਸਾਨੂੰ ਆਖਰੀ ਜਵਾਬ ਮਿਲ ਜਾਵੇ।

ਅਸੀਂ LLM ਨੂੰ ਕਈ ਵਾਰੀ ਕਾਲ ਕਰਾਂਗੇ, ਇਸ ਲਈ ਇੱਕ ਫੰਕਸ਼ਨ ਬਣਾਈਏ ਜੋ LLM ਕਾਲ ਸੰਭਾਲੇ। ਆਪਣੀ `main.rs` ਫਾਇਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਫੰਕਸ਼ਨ ਜੋੜੋ:

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

ਇਹ ਫੰਕਸ਼ਨ LLM ਕੁਲਾਇੰਟ, ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ (ਜਿਸ ਵਿੱਚ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਲ ਹੈ), MCP ਸਰਵਰ ਤੋਂ ਟੂਲਜ਼ ਲੈਂਦਾ ਹੈ ਅਤੇ LLM ਨੂੰ ਬੇਨਤੀ ਭੇਜਦਾ ਹੈ, ਅਤੇ ਜਵਾਬ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।
LLM ਤੋਂ ਪ੍ਰਾਪਤ ਜਵਾਬ ਵਿੱਚ `choices` ਦਾ ਐਰੇ ਸ਼ਾਮਲ ਹੋਵੇਗਾ। ਸਾਨੂੰ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰਨੀ ਪਵੇਗੀ ਤਾਂ ਜੋ ਦੇਖਿਆ ਜਾ ਸਕੇ ਕਿ ਕੋਈ `tool_calls` ਮੌਜੂਦ ਹਨ ਜਾਂ ਨਹੀਂ। ਇਹ ਸਾਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ LLM ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਟੂਲ ਨੂੰ ਆਰਗੂਮੈਂਟਸ ਦੇ ਨਾਲ ਕਾਲ ਕਰਨ ਦੀ ਬੇਨਤੀ ਕਰ ਰਿਹਾ ਹੈ। ਆਪਣੇ `main.rs` ਫਾਈਲ ਦੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ ਤਾਂ ਜੋ LLM ਜਵਾਬ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਫੰਕਸ਼ਨ ਬਣਾਇਆ ਜਾ ਸਕੇ:

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

    // ਸਮੱਗਰੀ ਪ੍ਰਿੰਟ ਕਰੋ ਜੇ ਉਪਲੱਬਧ ਹੋਵੇ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਸੰਭਾਲੋ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ਸਹਾਇਤਾ ਸਨੇਹਾ ਸ਼ਾਮਲ ਕਰੋ

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

            // ਟੂਲ ਨਤੀਜੇ ਨੂੰ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰੋ
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


ਜੇ `tool_calls` ਮੌਜੂਦ ਹਨ, ਤਾਂ ਇਹ ਟੂਲ ਜਾਣਕਾਰੀ ਨਿਕਾਲਦਾ ਹੈ, ਟੂਲ ਬੇਨਤੀ ਨਾਲ MCP ਸਰਵਰ ਨੂੰ ਕਾਲ ਕਰਦਾ ਹੈ, ਅਤੇ ਨਤੀਜੇ ਗੱਲਬਾਤ ਸੁਨੇਹਿਆਂ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ। ਫਿਰ ਇਹ LLM ਨਾਲ ਗੱਲਬਾਤ ਜਾਰੀ ਰੱਖਦਾ ਹੈ ਅਤੇ ਸੁਨੇਹਿਆਂ ਨੂੰ ਅਸਿਸਟੈਂਟ ਦੇ ਜਵਾਬ ਅਤੇ ਟੂਲ ਕਾਲ ਨਤੀਜਿਆਂ ਨਾਲ ਅਪਡੇਟ ਕਰਦਾ ਹੈ।

MCP ਕਾਲਾਂ ਲਈ LLM ਵੱਲੋਂ ਵਾਪਸ ਕੀਤੀ ਟੂਲ ਕਾਲ ਜਾਣਕਾਰੀ ਨਿਕਾਲਣ ਲਈ, ਅਸੀਂ ਇੱਕ ਹੋਰ ਸਹਾਇਕ ਫੰਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰਾਂਗੇ ਜੋ ਸਾਰੀ ਲੋੜੀਂਦੀ ਜਾਣਕਾਰੀ ਕਾਲ ਕਰਨ ਲਈ ਬਾਹਰ ਕੱਢੇਗਾ। ਆਪਣੇ `main.rs` ਫਾਈਲ ਦੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

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


ਸਾਰੀਆਂ ਜ਼ਰੂਰੀ ਹਿੱਸੇ ਮੌਜੂਦ ਹੋਣ ਮਗਰੋਂ, ਅਸੀਂ ਹੁਣ ਮੁਢਲਾ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਸੰਭਾਲ ਸਕਦੇ ਹਾਂ ਅਤੇ LLM ਨੂੰ ਕਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਆਪਣੇ `main` ਫੰਕਸ਼ਨ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰਕੇ ਅਪਡੇਟ ਕਰੋ:

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


ਇਹ LLM ਨੂੰ ਮੁਢਲੇ ਯੂਜ਼ਰ ਪ੍ਰਾਂਪਟ ਨਾਲ ਪੁੱਛੇਗਾ ਜੋ ਦੋ ਨੰਬਰਾਂ ਦਾ ਜੋੜ ਹੈ, ਅਤੇ ਜਵਾਬ ਨੂੰ ਪ੍ਰਕਿਰਿਆ ਕਰੇਗਾ ਤਾਂ ਜੋ ਟੂਲ ਕਾਲਾਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਸੰਭਾਲਿਆ ਜਾ ਸਕੇ।

ਸ਼ਾਬਾਸ਼, ਤੁਸੀਂ ਇਹ ਕਰ ਲਿਆ!

## ਅਸਾਈਨਮੈਂਟ

ਕਸਰਤ ਤੋਂ ਕੋਡ ਲਓ ਅਤੇ ਸਰਵਰ ਵਿੱਚ ਹੋਰ ਕੁਝ ਟੂਲ ਬਣਾਓ। ਫਿਰ ਕਸਰਤ ਵਾਂਗ ਇੱਕ LLM ਨਾਲ ਕਲਾਇੰਟ ਬਣਾਓ ਅਤੇ ਵੱਖ-ਵੱਖ ਪ੍ਰਾਂਪਟ ਨਾਲ ਟੈਸਟ ਕਰੋ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਸਰਵਰ ਦੇ ਸਾਰੇ ਟੂਲ ਗਤੀਸ਼ੀਲ ਤੌਰ 'ਤੇ ਕਾਲ ਹੋ ਰਹੇ ਹਨ ਇਹ ਯਕੀਨੀ ਬਣੇ। ਇਸ ਤਰ੍ਹਾਂ ਕਲਾਇੰਟ ਬਣਾਉਣ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਅੰਤਮ ਉਪਭੋਕਤਾ ਨੂੰ ਇੱਕ ਵਧੀਆ ਉਪਭੋਗਤਾ ਅਨੁਭਵ ਮਿਲੇਗਾ ਕਿਉਂਕਿ ਉਹ ਸਹੀ ਕਲਾਇੰਟ ਕਮਾਂਡਾਂ ਦੀ ਜਗ੍ਹਾ ਪ੍ਰਾਂਪਟ ਵਰਤ ਸਕਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਵੀ MCP ਸਰਵਰ ਕਾਲ ਤੋਂ ਅਣਜਾਣ ਰਹੇਗਾ।

## ਹੱਲ

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## ਮੁੱਖ ਪੁਆਇੰਟ

- ਆਪਣੇ ਕਲਾਇੰਟ ਵਿੱਚ LLM ਸ਼ਾਮਲ ਕਰਨਾ ਉਪਭੋਗਤਾਵਾਂ ਲਈ MCP ਸਰਵਰਾਂ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਦਾ ਵਧੀਆ ਤਰੀਕਾ ਦਿੰਦਾ ਹੈ।
- ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਦੇ ਜਵਾਬ ਨੂੰ ਕੁਝ ਐਸਾ ਬਦਲਣਾ ਪਵੇਗਾ ਜੋ LLM ਸਮਝ ਸਕੇ।

## ਨਮੂਨੇ

- [Java ਕੈਲਕੁਲੇਟਰ](../samples/java/calculator/README.md)
- [.Net ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/csharp)
- [JavaScript ਕੈਲਕੁਲੇਟਰ](../samples/javascript/README.md)
- [TypeScript ਕੈਲਕੁਲੇਟਰ](../samples/typescript/README.md)
- [Python ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/python)
- [Rust ਕੈਲਕੁਲੇਟਰ](../../../../03-GettingStarted/samples/rust)

## ਵਾਧੂ ਸਰੋਤ

## ਅਗਲਾ ਕੀ ਹੈ

- ਅਗਲਾ: [Visual Studio Code ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਰਵਰ ਦੀ ਖਪਤ](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਰਣ**:
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਜਾਣੋਂ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਅਹਿਮ ਜਾਣਕਾਰੀ ਲਈ ਵਪਾਰਕ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਉਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->