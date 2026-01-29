# LLM सँग क्लाइन्ट सिर्जना गर्दै

अहिलेसम्म, तपाईंले कसरी सर्भर र क्लाइन्ट सिर्जना गर्ने देख्नुभएको छ। क्लाइन्टले सर्भरलाई स्पष्ट रूपमा कल गरेर यसको उपकरणहरू, स्रोतहरू र प्रॉम्प्टहरू सूचीबद्ध गर्न सक्षम भएको छ। यद्यपि, यो धेरै व्यावहारिक तरिका होइन। तपाईंको प्रयोगकर्ता एजेन्टिक युगमा बस्छ र प्रॉम्प्टहरू प्रयोग गर्न र LLM सँग संवाद गर्न अपेक्षा गर्दछ। तपाईंको प्रयोगकर्ताका लागि, तपाईंले आफ्नो क्षमता भण्डारण गर्न MCP प्रयोग गर्नुहुन्छ वा हुँदैन भन्ने कुरामा ध्यान दिँदैनन् तर उनीहरूले प्राकृतिक भाषामा अन्तरक्रिया गर्न चाहन्छन्। त्यसैले हामी यसलाई कसरी समाधान गर्ने? समाधान भनेको क्लाइन्टमा LLM थप्नु हो।

## अवलोकन

यस पाठमा हामी क्लाइन्टमा LLM थप्नमा केन्द्रित छौं र देखाउँछौं कि यसले तपाईंको प्रयोगकर्ताका लागि कत्तिको राम्रो अनुभव प्रदान गर्दछ।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- LLM सहित क्लाइन्ट सिर्जना गर्न।
- LLM प्रयोग गरेर MCP सर्भरसँग सहज रूपमा अन्तरक्रिया गर्न।
- क्लाइन्ट पक्षमा राम्रो अन्तिम प्रयोगकर्ता अनुभव प्रदान गर्न।

## दृष्टिकोण

हामीले लिनुपर्ने दृष्टिकोण बुझ्न प्रयास गरौं। LLM थप्नु सरल सुनिन्छ, तर के हामी साँच्चै यसो गर्नेछौं?

क्लाइन्टले सर्भरसँग कसरी अन्तरक्रिया गर्नेछ:

1. सर्भरसँग जडान स्थापना गर्नुहोस्।

1. क्षमता, प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरू सूचीबद्ध गर्नुहोस्, र तिनीहरूको स्कीमा सुरक्षित गर्नुहोस्।

1. LLM थप्नुहोस् र सुरक्षित क्षमताहरू र तिनीहरूको स्कीमा LLM ले बुझ्ने ढाँचामा पास गर्नुहोस्।

1. प्रयोगकर्ता प्रॉम्प्टलाई LLM मा पास गरेर क्लाइन्टले सूचीबद्ध गरेका उपकरणहरूसँग मिलाएर ह्यान्डल गर्नुहोस्।

शानदार, अब हामीले उच्च स्तरमा कसरी गर्न सकिन्छ बुझ्यौं, तलको अभ्यासमा यसलाई प्रयास गरौं।

## अभ्यास: LLM सहित क्लाइन्ट सिर्जना गर्दै

यस अभ्यासमा, हामी हाम्रो क्लाइन्टमा LLM थप्न सिक्नेछौं।

### GitHub व्यक्तिगत पहुँच टोकन प्रयोग गरेर प्रमाणीकरण

GitHub टोकन सिर्जना गर्नु सरल प्रक्रिया हो। यसरी गर्न सकिन्छ:

- GitHub सेटिङहरूमा जानुहोस् – माथिल्लो दायाँ कुनामा आफ्नो प्रोफाइल तस्वीरमा क्लिक गरी सेटिङहरू चयन गर्नुहोस्।
- डेभलपर सेटिङहरूमा जानुहोस् – तल स्क्रोल गरी डेभलपर सेटिङहरूमा क्लिक गर्नुहोस्।
- व्यक्तिगत पहुँच टोकनहरू चयन गर्नुहोस् – फाइन-ग्रेन्डेड टोकनहरूमा क्लिक गरी नयाँ टोकन सिर्जना गर्नुहोस्।
- आफ्नो टोकन कन्फिगर गर्नुहोस् – सन्दर्भका लागि नोट थप्नुहोस्, समाप्ति मिति सेट गर्नुहोस्, र आवश्यक स्कोपहरू (अनुमतिहरू) चयन गर्नुहोस्। यस अवस्थामा, मोडेल अनुमति थप्न निश्चित हुनुहोस्।
- टोकन सिर्जना गरी कपी गर्नुहोस् – Generate token मा क्लिक गर्नुहोस्, र तुरुन्तै कपी गर्नुहोस्, किनकि तपाईंले फेरि हेर्न सक्नुहुने छैन।

### -1- सर्भरसँग जडान गर्नुहोस्

पहिले हाम्रो क्लाइन्ट सिर्जना गरौं:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरणको लागि zod आयात गर्नुहोस्

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

अघिल्लो कोडमा हामीले:

- आवश्यक पुस्तकालयहरू आयात गर्यौं
- दुई सदस्यहरू `client` र `openai` सहित एक क्लास सिर्जना गर्यौं जसले हामीलाई क्लाइन्ट व्यवस्थापन गर्न र LLM सँग अन्तरक्रिया गर्न मद्दत गर्नेछ।
- हाम्रो LLM उदाहरणलाई GitHub मोडेलहरू प्रयोग गर्न कन्फिगर गर्यौं, `baseUrl` लाई inference API तर्फ सेट गरेर।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानका लागि सर्भर प्यारामिटरहरू सिर्जना गर्नुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयनयोग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन तर्कहरू
    env=None,  # वैकल्पिक वातावरण चरहरू
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # जडान सुरु गर्नुहोस्
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

अघिल्लो कोडमा हामीले:

- MCP का लागि आवश्यक पुस्तकालयहरू आयात गर्यौं
- क्लाइन्ट सिर्जना गर्यौं

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

पहिले, तपाईंले आफ्नो `pom.xml` फाइलमा LangChain4j निर्भरता थप्नुपर्नेछ। MCP एकीकरण र GitHub मोडेल समर्थन सक्षम गर्न यी निर्भरता थप्नुहोस्:

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

त्यसपछि आफ्नो Java क्लाइन्ट क्लास सिर्जना गर्नुहोस्:

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
    
    public static void main(String[] args) throws Exception {        // LLM लाई GitHub मोडेलहरू प्रयोग गर्न कन्फिगर गर्नुहोस्
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // सर्भरसँग जडान गर्न MCP ट्रान्सपोर्ट सिर्जना गर्नुहोस्
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP क्लाइन्ट सिर्जना गर्नुहोस्
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

अघिल्लो कोडमा हामीले:

- **LangChain4j निर्भरता थप्यौं**: MCP एकीकरण, OpenAI आधिकारिक क्लाइन्ट, र GitHub मोडेल समर्थनका लागि आवश्यक
- **LangChain4j पुस्तकालयहरू आयात गर्यौं**: MCP एकीकरण र OpenAI च्याट मोडेल कार्यक्षमताका लागि
- **`ChatLanguageModel` सिर्जना गर्यौं**: GitHub मोडेलहरू प्रयोग गर्न कन्फिगर गरिएको तपाईंको GitHub टोकनसहित
- **HTTP ट्रान्सपोर्ट सेटअप गर्यौं**: Server-Sent Events (SSE) प्रयोग गरेर MCP सर्भरसँग जडान गर्न
- **MCP क्लाइन्ट सिर्जना गर्यौं**: जसले सर्भरसँग सञ्चार ह्यान्डल गर्नेछ
- **LangChain4j को बिल्ट-इन MCP समर्थन प्रयोग गर्यौं**: जसले LLM र MCP सर्भरहरू बीच एकीकरण सजिलो बनाउँछ

#### Rust

यो उदाहरणले तपाईंको Rust आधारित MCP सर्भर चलिरहेको छ भनी मान्दछ। यदि छैन भने, सर्भर सिर्जना गर्न [01-first-server](../01-first-server/README.md) पाठमा फर्केर हेर्नुहोस्।

तपाईंको Rust MCP सर्भर भएपछि, टर्मिनल खोल्नुहोस् र सर्भरको समान डाइरेक्टरीमा जानुहोस्। त्यसपछि नयाँ LLM क्लाइन्ट प्रोजेक्ट सिर्जना गर्न तलको आदेश चलाउनुहोस्:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तपाईंको `Cargo.toml` फाइलमा निम्न निर्भरता थप्नुहोस्:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI को लागि आधिकारिक Rust पुस्तकालय छैन, तर `async-openai` क्रेट एक [समुदायले मर्मत गरेको पुस्तकालय](https://platform.openai.com/docs/libraries/rust#rust) हो जुन सामान्यतया प्रयोग गरिन्छ।

`src/main.rs` फाइल खोल्नुहोस् र यसको सामग्री तलको कोडले प्रतिस्थापन गर्नुहोस्:

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
    // प्रारम्भिक सन्देश
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI क्लाइन्ट सेटअप गर्नुहोस्
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP क्लाइन्ट सेटअप गर्नुहोस्
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

    // TODO: MCP उपकरण सूची प्राप्त गर्नुहोस्

    // TODO: उपकरण कलहरूसँग LLM संवाद

    Ok(())
}
```

यो कोडले एक आधारभूत Rust एप्लिकेसन सेटअप गर्दछ जुन MCP सर्भर र GitHub मोडेलहरूमा LLM अन्तरक्रियाका लागि जडान हुनेछ।

> [!IMPORTANT]
> एप्लिकेसन चलाउनु अघि आफ्नो GitHub टोकनसहित `OPENAI_API_KEY` वातावरण चर सेट गर्न निश्चित हुनुहोस्।

शानदार, अब हाम्रो अर्को कदम सर्भरमा क्षमताहरू सूचीबद्ध गर्ने हो।

### -2- सर्भर क्षमताहरू सूचीबद्ध गर्नुहोस्

अब हामी सर्भरसँग जडान गर्नेछौं र यसको क्षमताहरू सोध्नेछौं:

#### Typescript

उही क्लासमा, तलका मेथडहरू थप्नुहोस्:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // उपकरणहरू सूचीबद्ध गर्दै
    const toolsResult = await this.client.listTools();
}
```

अघिल्लो कोडमा हामीले:

- सर्भरसँग जडान गर्ने कोड `connectToServer` थप्यौं।
- हाम्रो एप्लिकेसन फ्लो ह्यान्डल गर्ने `run` मेथड सिर्जना गर्यौं। अहिलेसम्म यसले मात्र उपकरणहरू सूचीबद्ध गर्छ तर हामी चाँडै थप्नेछौं।

#### Python

```python
# उपलब्ध स्रोतहरू सूचीबद्ध गर्नुहोस्
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणहरू सूचीबद्ध गर्नुहोस्
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

यहाँ हामीले थप्यौं:

- स्रोतहरू र उपकरणहरू सूचीबद्ध गर्यौं र प्रिन्ट गर्यौं। उपकरणहरूको लागि हामीले `inputSchema` पनि सूचीबद्ध गर्यौं जुन पछि प्रयोग गर्नेछौं।

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

अघिल्लो कोडमा हामीले:

- MCP सर्भरमा उपलब्ध उपकरणहरू सूचीबद्ध गर्यौं
- प्रत्येक उपकरणको नाम, विवरण र यसको स्कीमा सूचीबद्ध गर्यौं। पछिल्लो कुरा हामी चाँडै उपकरणहरू कल गर्न प्रयोग गर्नेछौं।

#### Java

```java
// स्वचालित रूपमा MCP उपकरणहरू पत्ता लगाउने उपकरण प्रदायक सिर्जना गर्नुहोस्
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP उपकरण प्रदायकले स्वचालित रूपमा ह्यान्डल गर्दछ:
// - MCP सर्भरबाट उपलब्ध उपकरणहरूको सूची बनाउने
// - MCP उपकरण स्किमाहरूलाई LangChain4j ढाँचामा रूपान्तरण गर्ने
// - उपकरण कार्यान्वयन र प्रतिक्रियाहरू व्यवस्थापन गर्ने
```

अघिल्लो कोडमा हामीले:

- `McpToolProvider` सिर्जना गर्यौं जसले स्वचालित रूपमा MCP सर्भरबाट सबै उपकरणहरू पत्ता लगाएर दर्ता गर्छ
- उपकरण प्रदायकले MCP उपकरण स्कीमाहरू र LangChain4j को उपकरण ढाँचाबीच रूपान्तरण आन्तरिक रूपमा ह्यान्डल गर्छ
- यस दृष्टिकोणले म्यानुअल उपकरण सूचीकरण र रूपान्तरण प्रक्रियालाई हटाउँछ

#### Rust

MCP सर्भरबाट उपकरणहरू प्राप्त गर्न `list_tools` मेथड प्रयोग गरिन्छ। तपाईंको `main` फंक्शनमा, MCP क्लाइन्ट सेटअप गरेपछि तलको कोड थप्नुहोस्:

```rust
// MCP उपकरण सूची प्राप्त गर्नुहोस्
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्भर क्षमताहरूलाई LLM उपकरणहरूमा रूपान्तरण गर्नुहोस्

सर्भर क्षमताहरू सूचीबद्ध गरेपछि अर्को कदम ती क्षमताहरूलाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्नु हो। यसपछि हामी यी क्षमताहरूलाई LLM का लागि उपकरणको रूपमा प्रदान गर्न सक्छौं।

#### TypeScript

1. MCP सर्भरबाट प्राप्त प्रतिक्रिया LLM ले प्रयोग गर्न सक्ने उपकरण ढाँचामा रूपान्तरण गर्न तलको कोड थप्नुहोस्:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्कीमामा आधारित एक जोड स्कीमा सिर्जना गर्नुहोस्
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकारलाई स्पष्ट रूपमा "function" मा सेट गर्नुहोस्
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

    माथिको कोडले MCP सर्भरबाट प्रतिक्रिया लिएर LLM ले बुझ्ने उपकरण परिभाषा ढाँचामा रूपान्तरण गर्छ।

1. अब `run` मेथड अपडेट गरौं जसले सर्भर क्षमताहरू सूचीबद्ध गर्छ:

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

    अघिल्लो कोडमा, हामीले `run` मेथड अपडेट गर्यौं जसले परिणाममा म्याप गर्दै प्रत्येक प्रविष्टिमा `openAiToolAdapter` कल गर्छ।

#### Python

1. पहिले, तलको रूपान्तरण फंक्शन सिर्जना गरौं

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

    माथिको `convert_to_llm_tools` फंक्शनले MCP उपकरण प्रतिक्रिया लिएर LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्छ।

1. अब हाम्रो क्लाइन्ट कोड अपडेट गरौं यस फंक्शनलाई प्रयोग गर्न:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ, हामीले `convert_to_llm_tool` कल थप्यौं जसले MCP उपकरण प्रतिक्रियालाई LLM लाई फिड गर्न सकिनेमा रूपान्तरण गर्छ।

#### .NET

1. MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्नेमा रूपान्तरण गर्न कोड थपौं

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

अघिल्लो कोडमा हामीले:

- `ConvertFrom` फंक्शन सिर्जना गर्यौं जसले नाम, विवरण र इनपुट स्कीमा लिन्छ।
- यस्तो कार्यक्षमता परिभाषित गर्यौं जसले FunctionDefinition सिर्जना गर्छ र त्यसलाई ChatCompletionsDefinition मा पास गर्छ। पछिल्लो कुरा LLM ले बुझ्छ।

1. अब केही अवस्थित कोड अपडेट गरौं यो फंक्शनको फाइदा लिन:

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
// प्राकृतिक भाषा अन्तरक्रियाका लागि बोट इन्टरफेस सिर्जना गर्नुहोस्
public interface Bot {
    String chat(String prompt);
}

// LLM र MCP उपकरणहरूसँग AI सेवा कन्फिगर गर्नुहोस्
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

अघिल्लो कोडमा हामीले:

- प्राकृतिक भाषा अन्तरक्रियाका लागि सरल `Bot` इन्टरफेस परिभाषित गर्यौं
- LangChain4j को `AiServices` प्रयोग गर्यौं जसले LLM लाई MCP उपकरण प्रदायकसँग स्वचालित रूपमा बाँध्छ
- फ्रेमवर्कले उपकरण स्कीमा रूपान्तरण र फंक्शन कल स्वचालित रूपमा ह्यान्डल गर्छ
- यस दृष्टिकोणले म्यानुअल उपकरण रूपान्तरण हटाउँछ - LangChain4j ले MCP उपकरणहरूलाई LLM-अनुकूल ढाँचामा रूपान्तरण गर्ने सबै जटिलता ह्यान्डल गर्छ

#### Rust

MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्न, हामी एउटा सहायक फंक्शन थप्नेछौं जसले उपकरणहरूको सूचीलाई ढाँचा दिन्छ। `main` फंक्शन मुनि तलको कोड `main.rs` फाइलमा थप्नुहोस्। यो LLM लाई अनुरोध गर्दा कल गरिनेछ:

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

शानदार, अब हामी प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्न तयार छौं, त्यसो भए अगाडि बढौं।

### -4- प्रयोगकर्ता प्रॉम्प्ट अनुरोध ह्यान्डल गर्नुहोस्

यस भागमा, हामी प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्नेछौं।

#### TypeScript

1. हाम्रो LLM कल गर्न प्रयोग हुने मेथड थपौं:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // २. सर्भरको उपकरण कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. नतिजासँग केही गर्नुहोस्
        // गर्न बाँकी छ

        }
    }
    ```

    अघिल्लो कोडमा हामीले:

    - `callTools` मेथड थप्यौं।
    - मेथडले LLM प्रतिक्रिया लिएर कुन उपकरणहरू कल गरिएको छ जाँच गर्छ, यदि कुनै छ भने:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // उपकरण कल गर्नुहोस्
        }
        ```

    - LLM ले कल गर्नुपर्ने संकेत गरेमा उपकरण कल गर्छ:

        ```typescript
        // २. सर्भरको उपकरण कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. नतिजासँग केही गर्नुहोस्
        // गर्न बाँकी छ
        ```

1. `run` मेथड अपडेट गरौं जसले LLM कल र `callTools` कल समावेश गर्छ:

    ```typescript

    // १. LLM को लागि इनपुट सन्देशहरू सिर्जना गर्नुहोस्
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // २. LLM लाई कल गर्दै
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ३. LLM को प्रतिक्रिया जाँच गर्नुहोस्, प्रत्येक विकल्पका लागि, यदि यसमा उपकरण कलहरू छन् कि छैनन् जाँच गर्नुहोस्
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

शानदार, पूर्ण कोड सूचीबद्ध गरौं:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरणको लागि zod आयात गर्नुहोस्

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्यमा यो URL मा परिवर्तन गर्न आवश्यक पर्न सक्छ: https://models.github.ai/inference
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
          // input_schema मा आधारित zod स्कीमा सिर्जना गर्नुहोस्
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // प्रकारलाई स्पष्ट रूपमा "function" मा सेट गर्नुहोस्
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
    
    
          // 2. सर्भरको उपकरण कल गर्नुहोस्
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. परिणामसँग केहि गर्नुहोस्
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
            model: "gpt-4o-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM प्रतिक्रिया मार्फत जानुहोस्, प्रत्येक विकल्पको लागि, जाँच गर्नुहोस् कि यसमा उपकरण कलहरू छन् कि छैनन्
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

1. LLM कल गर्न आवश्यक केही आयातहरू थपौं

    ```python
    # एलएलएम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. अब, LLM कल गर्ने फंक्शन थपौं:

    ```python
    # एलएलएम

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
            # वैकल्पिक प्यारामिटरहरू
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

    अघिल्लो कोडमा हामीले:

    - MCP सर्भरमा फेला परेका र रूपान्तरण गरिएका फंक्शनहरू LLM लाई पास गर्यौं।
    - त्यसपछि ती फंक्शनहरूसँग LLM कल गर्यौं।
    - परिणाम जाँच्यौं कि कुन फंक्शनहरू कल गर्नुपर्छ, यदि कुनै छ भने।
    - अन्तमा, कल गर्नुपर्ने फंक्शनहरूको एरे पास गर्यौं।

1. अन्तिम चरण, हाम्रो मुख्य कोड अपडेट गरौं:

    ```python
    prompt = "Add 2 to 20"

    # LLM लाई सोध्नुहोस् सबै उपकरणहरू के हुन्, यदि कुनै छन् भने
    functions_to_call = call_llm(prompt, functions)

    # सुझाएका कार्यहरू कल गर्नुहोस्
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    माथिको कोडमा हामीले:

    - LLM ले सुझाव दिएको फंक्शन प्रयोग गरी MCP उपकरण `call_tool` मार्फत कल गर्यौं।
    - उपकरण कलको परिणाम MCP सर्भरमा प्रिन्ट गर्यौं।

#### .NET

1. LLM प्रॉम्प्ट अनुरोध गर्ने कोड देखाउँछौं:

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

    अघिल्लो कोडमा हामीले:

    - MCP सर्भरबाट उपकरणहरू ल्यायौं, `var tools = await GetMcpTools()`।
    - प्रयोगकर्ता प्रॉम्प्ट `userMessage` परिभाषित गर्यौं।
    - मोडेल र उपकरणहरू निर्दिष्ट गर्दै विकल्प वस्तु बनायौं।
    - LLM तर्फ अनुरोध गर्यौं।

1. अन्तिम चरण, LLM ले फंक्शन कल गर्नुपर्ने सोच्छ कि भनेर जाँचौं:

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

    अघिल्लो कोडमा हामीले:

    - फंक्शन कलहरूको सूचीमा लूप गर्यौं।
    - प्रत्येक उपकरण कलका लागि नाम र आर्गुमेन्ट पार्स गरी MCP क्लाइन्ट प्रयोग गरेर उपकरण कल गर्यौं। अन्तमा परिणाम प्रिन्ट गर्यौं।

पूर्ण कोड यहाँ छ:

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
    // स्वचालित रूपमा MCP उपकरणहरू प्रयोग गर्ने प्राकृतिक भाषा अनुरोधहरू कार्यान्वयन गर्नुहोस्
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

अघिल्लो कोडमा हामीले:

- सरल प्राकृतिक भाषा प्रॉम्प्टहरू प्रयोग गरी MCP सर्भर उपकरणहरूसँग अन्तरक्रिया गर्यौं
- LangChain4j फ्रेमवर्कले स्वचालित रूपमा ह्यान्डल गर्छ:
  - आवश्यक पर्दा प्रयोगकर्ता प्रॉम्प्टलाई उपकरण कलमा रूपान्तरण
  - LLM को निर्णय अनुसार उपयुक्त MCP उपकरणहरू कल गर्ने
  - LLM र MCP सर्भर बीच संवाद प्रवाह व्यवस्थापन गर्ने
- `bot.chat()` मेथडले प्राकृतिक भाषा प्रतिक्रिया फर्काउँछ जसमा MCP उपकरण निष्पादनका परिणामहरू समावेश हुन सक्छन्
- यस दृष्टिकोणले प्रयोगकर्तालाई MCP को आधारभूत कार्यान्वयनबारे जान्न आवश्यक नपर्ने सहज अनुभव प्रदान गर्दछ

पूर्ण कोड उदाहरण:

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

यहाँ मुख्य काम हुन्छ। हामीले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टसहित LLM कल गर्नेछौं, त्यसपछि प्रतिक्रिया प्रक्रिया गर्नेछौं कि कुनै उपकरण कल गर्नुपर्छ कि छैन। यदि छ भने, ती उपकरणहरू कल गर्नेछौं र LLM सँग संवाद जारी राख्नेछौं जबसम्म थप उपकरण कल आवश्यक नपरोस् र अन्तिम प्रतिक्रिया प्राप्त नहोस्।

हामी LLM लाई धेरै पटक कल गर्नेछौं, त्यसैले LLM कल ह्यान्डल गर्ने फंक्शन परिभाषित गरौं। तलको फंक्शन `main.rs` फाइलमा थप्नुहोस्:

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

यो फंक्शनले LLM क्लाइन्ट, सन्देशहरूको सूची (प्रयोगकर्ता प्रॉम्प्ट सहित), MCP सर्भरका उपकरणहरू लिन्छ र LLM लाई अनुरोध पठाउँछ, प्रतिक्रिया फर्काउँछ।
LLM बाट आएको प्रतिक्रिया `choices` को एरे समावेश गर्नेछ। हामीले परिणामलाई प्रक्रिया गर्न आवश्यक छ कि कुनै `tool_calls` उपस्थित छन् कि छैनन् भनेर हेर्न। यसले हामीलाई थाहा दिन्छ कि LLM ले कुनै विशेष उपकरणलाई आर्गुमेन्टसहित कल गर्न अनुरोध गरिरहेको छ। LLM प्रतिक्रिया ह्यान्डल गर्नको लागि तपाईँको `main.rs` फाइलको तल निम्न कोड थप्नुहोस्:

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

    // सामग्री उपलब्ध भएमा प्रिन्ट गर्नुहोस्
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // उपकरण कलहरू ह्यान्डल गर्नुहोस्
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // सहायक सन्देश थप्नुहोस्

        // प्रत्येक उपकरण कल कार्यान्वयन गर्नुहोस्
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // सन्देशहरूमा उपकरण परिणाम थप्नुहोस्
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // उपकरण परिणामहरूसँग संवाद जारी राख्नुहोस्
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

यदि `tool_calls` उपस्थित छन् भने, यसले उपकरण जानकारी निकाल्छ, उपकरण अनुरोधसहित MCP सर्भरलाई कल गर्छ, र परिणामहरूलाई संवाद सन्देशहरूमा थप्छ। त्यसपछि यो LLM सँग संवाद जारी राख्छ र सन्देशहरू सहायकको प्रतिक्रिया र उपकरण कल परिणामहरूसँग अपडेट हुन्छन्।

LLM ले MCP कलहरूको लागि फर्काउने उपकरण कल जानकारी निकाल्न, हामी अर्को सहायक फंक्शन थप्नेछौं जसले कल गर्न आवश्यक सबै कुरा निकाल्छ। तपाईँको `main.rs` फाइलको तल निम्न कोड थप्नुहोस्:

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

सबै भागहरू तयार भएपछि, हामीले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्ट ह्यान्डल गर्न र LLM कल गर्न सक्छौं। तपाईँको `main` फंक्शनलाई निम्न कोड समावेश गर्न अपडेट गर्नुहोस्:

```rust
// उपकरण कलहरूसँग LLM संवाद
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

यसले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टसहित LLM लाई सोध्नेछ दुई संख्याको योगको लागि, र प्रतिक्रिया प्रक्रिया गरेर उपकरण कलहरू गतिशील रूपमा ह्यान्डल गर्नेछ।

शानदार, तपाईँले गर्नुभयो!

## असाइनमेन्ट

व्यायामबाट कोड लिएर सर्भरलाई थप उपकरणहरूसँग विस्तार गर्नुहोस्। त्यसपछि व्यायाममा जस्तै LLM सहित क्लाइन्ट सिर्जना गर्नुहोस् र विभिन्न प्रॉम्प्टहरूसँग परीक्षण गर्नुहोस् ताकि तपाईँका सबै सर्भर उपकरणहरू गतिशील रूपमा कल हुन्छन् भनी सुनिश्चित गर्न सकियोस्। यसरी क्लाइन्ट निर्माण गर्दा अन्तिम प्रयोगकर्ताले उत्कृष्ट प्रयोगकर्ता अनुभव पाउनेछ किनकि उनीहरूले प्रॉम्प्टहरू प्रयोग गर्न सक्छन्, ठ्याक्कै क्लाइन्ट कमाण्डहरू होइन, र कुनै MCP सर्भर कल भइरहेको छ भन्ने थाहा नपाउनेछन्।

## समाधान

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## मुख्य सिकाइहरू

- तपाईँको क्लाइन्टमा LLM थप्दा प्रयोगकर्ताहरूलाई MCP सर्भरसँग अन्तरक्रिया गर्ने राम्रो तरिका प्रदान हुन्छ।
- तपाईँले MCP सर्भरको प्रतिक्रिया LLM ले बुझ्ने स्वरूपमा रूपान्तरण गर्न आवश्यक छ।

## नमूनाहरू

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## थप स्रोतहरू

## के छ अर्को

- अर्को: [Visual Studio Code प्रयोग गरेर सर्भर उपभोग गर्ने](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->