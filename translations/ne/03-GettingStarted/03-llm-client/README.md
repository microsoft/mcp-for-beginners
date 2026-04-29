# LLM सँग क्लाइन्ट सिर्जना गर्दै

अहिलेसम्म, तपाईंले कसरी सर्भर र क्लाइन्ट सिर्जना गर्ने देख्नुभएको छ। क्लाईन्टले स्पष्ट रूपमा सर्भरलाई यसका उपकरणहरू, स्रोतहरू, र प्रम्प्टहरू सूचीबद्ध गर्न कल गर्न सक्षम थियो। तर, यो धेरै व्यावहारिक तरिका होइन। तपाईंका प्रयोगकर्ताहरू एजेन्टिक युगमा बस्छन् र प्रम्प्टहरू प्रयोग गर्न र LLM सँग संवाद गर्न आशा गर्दछन्। उनीहरूलाई तपाईं MCP प्रयोग गरेर तपाईंका क्षमता भण्डारण गर्नुहुन्छ वा हुँदैन, यसमा चासो नलाग्नेछ; उनीहरू सरल प्राकृतिक भाषामा अन्तरक्रिया गर्न अपेक्षा गर्दछन्। त्यसोभए हामीले यो कसरी समाधान गर्ने? समाधान हो क्लाइन्टमा LLM थप्नु।

## अवलोकन

यस पाठमा हामी हाम्रो क्लाइन्टमा LLM थप्न केन्द्रित हुनेछौं र यसले तपाईंका प्रयोगकर्ताका लागि कतिको राम्रो अनुभव प्रदान गर्दछ भन्ने देखाउनेछौं।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- LLM सहित क्लाइन्ट सिर्जना गर्न।
- LLM प्रयोग गरेर सहज रूपमा MCP सर्भरसँग अन्तरक्रिया गर्न।
- क्लाइन्ट पक्षमा प्रयोगकर्तालाई अझ राम्रो अन्तिम अनुभव प्रदान गर्न।

## दृष्टिकोण

हामीले लिनुपर्ने दृष्टिकोणलाई बुझ्न प्रयास गरौं। LLM थप्नु सरल लाग्छ, तर के हामी साँच्चै यसलाई गर्नेछौं?

क्लाइन्टले सर्भरसँग यसरी अन्तरक्रिया गर्नेछ:

1. सर्भरसँग जडान स्थापित गर्नुहोस्।

1. क्षमता, प्रम्प्ट, स्रोतहरू र उपकरणहरू सूचीबद्ध गर्नुहोस् र तिनीहरूको स्कीमा सुरक्षित गर्नुहोस्।

1. LLM थप्नुहोस् र सुरक्षित गरेका क्षमता र तिनीहरूको स्कीमा LLM ले बुझ्ने ढाँचामा पास गर्नुहोस्।

1. प्रयोगकर्ताको प्रम्प्ट ह्यान्डल गर्नुहोस् र यसलाई क्लाइन्टले सूचीबद्ध गरेका उपकरणहरूसँग LLM लाई पास गर्नुहोस्।

शानदार, अब हामीले उच्च स्तरमा यो कसरी गर्न सकिन्छ बुझ्यौं, तलको अभ्यासमा यसलाई प्रयास गरौं।

## अभ्यास: LLM सहित क्लाइन्ट सिर्जना गर्दै

यस अभ्यासमा, हामी हाम्रो क्लाइन्टमा LLM थप्न सिक्नेछौं।

### GitHub Personal Access Token प्रयोग गरेर प्रमाणीकरण

GitHub टोकन सिर्जना गर्नु सरल प्रक्रिया हो। यसरी गर्न सकिन्छ:

- GitHub सेटिङहरूमा जानुहोस् – माथिल्लो दाहिने कुनामा आफ्नो प्रोफाइल चित्रमा क्लिक गर्नुहोस् र सेटिङहरू चयन गर्नुहोस्।
- Developer Settings मा जानुहोस् – तल स्क्रोल गरेर Developer Settings क्लिक गर्नुहोस्।
- Personal Access Tokens छान्नुहोस् – Fine-grained tokens क्लिक गर्नुहोस् र नयाँ टोकन जनरेट गर्नुहोस्।
- आफ्नो टोकन कन्फिगर गर्नुहोस् – सन्दर्भका लागि नोट थप्नुहोस्, समाप्ति मिति सेट गर्नुहोस्, र आवश्यक स्कोपहरू (अनुमतिहरू) चयन गर्नुहोस्। यस अवस्थामा Models अनुमति थप्न निश्चित हुनुहोस्।
- टोकन जनरेट गर्नुहोस् र त्यसलाई तुरुन्तै कपी गर्नुहोस्, किनकि पछि तपाईंले फेरि हेर्न सक्नुहुने छैन।

### -1- सर्भरसँग जडान गर्नुहोस्

पहिले हाम्रो क्लाइन्ट सिर्जना गरौं:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्किमा मान्यकरणका लागि zod आयात गर्नुहोस्

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

माथिल्लो कोडमा हामीले:

- आवश्यक पुस्तकालयहरू इम्पोर्ट गरेका छौं
- दुई सदस्यहरू `client` र `openai` भएको क्लास सिर्जना गरेका छौं, जसले क्लाइन्ट व्यवस्थापन गर्न र LLM सँग अन्तरक्रिया गर्न मद्दत गर्नेछ।
- हाम्रो LLM उदाहरणलाई GitHub Models प्रयोग गर्न कन्फिगर गरेका छौं, `baseUrl` सेट गरेर inference API मा संकेत गर्दै।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio कनेक्सनको लागि सर्भर प्यारामिटरहरू बनाउनुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयन योग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन आर्गुमेन्टहरू
    env=None,  # वैकल्पिक वातावरण भेरिएबलहरू
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # कनेक्सन सुरु गर्नुहोस्
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

माथिल्लो कोडमा हामीले:

- MCP को लागि आवश्यक पुस्तकालयहरू आयात गरेका छौं
- क्लाइन्ट सिर्जना गरेका छौं

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

पहिले, तपाईंले आफ्नो `pom.xml` फाइलमा LangChain4j निर्भरताहरू थप्नु पर्नेछ। MCP इंटिग्रेशन र GitHub Models समर्थन सक्षम गर्न यी निर्भरताहरू थप्नुहोस्:

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

त्यसपछि तपाईंको Java क्लाइन्ट क्लास सिर्जना गर्नुहोस्:

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

        // MCP ग्राहक सिर्जना गर्नुहोस्
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

माथिल्लो कोडमा हामीले:

- **LangChain4j निर्भरताहरू थपेका छौं**: MCP इंटिग्रेशन, OpenAI आधिकारिक क्लाइन्ट, र GitHub Models समर्थनको लागि आवश्यक
- **LangChain4j पुस्तकालयहरू आयात गरेका छौं**: MCP इंटिग्रेशन र OpenAI च्याट मोडेल कार्यक्षमता को लागी
- **`ChatLanguageModel` सिर्जना गरेका छौं**: जुन GitHub Models प्रयोग गर्न कन्फिगर गरिएको छ तपाईंको GitHub टोकनसँग
- **HTTP ट्रान्सपोर्ट सेट अप गरेका छौं**: Server-Sent Events (SSE) प्रयोग गरेर MCP सर्भरसँग जडान गर्न
- **MCP क्लाइन्ट सिर्जना गरेका छौं**: जसले सर्भरसँगको सञ्चार सम्हाल्ने छ
- **LangChain4j को बिल्ट-इन MCP समर्थन प्रयोग गरेका छौं**: जसले LLM र MCP सर्भरहरूको बीचको एकीकरणलाई सरल बनाउँछ

#### Rust

यो उदाहरणले Rust आधारित MCP सर्भर चलिरहेको छ भन्ने मान्छ। यदि तपाईंंसँग छैन भने, [01-first-server](../01-first-server/README.md) पाठमा फर्केर सर्भर सिर्जना गर्नुहोस्।

तपाईंको Rust MCP सर्भर भएपछि, टर्मिनल खोल्नुहोस् र सर्भरको समान निर्देशिकामा जानुहोस्। त्यसपछि नयाँ LLM क्लाइन्ट प्रोजेक्ट सिर्जना गर्न निम्न कमाण्ड चलाउनुहोस्:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

तपाईंको `Cargo.toml` फाइलमा निम्न निर्भरताहरू थप्नुहोस्:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI का लागि आधिकारिक Rust पुस्तकालय छैन, तर `async-openai` क्रेट एक [समुदायद्वारा मर्मत गरिएको पुस्तकालय](https://platform.openai.com/docs/libraries/rust#rust) हो जुन सामान्य रूपमा प्रयोग गरिन्छ।

`src/main.rs` फाइल खोल्नुहोस् र यसको सामग्री तलको कोडसँग प्रतिस्थापन गर्नुहोस्:

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

यो कोडले एक आधारभूत Rust एप्लिकेशन सेटअप गर्दछ जसले MCP सर्भर र GitHub Models सँग LLM अन्तरक्रिया गर्नेछ।

> [!IMPORTANT]
> एप्लिकेशन चलाउनु अघि आफ्नो GitHub टोकनको साथ `OPENAI_API_KEY` वातावरण चर सेट गर्न निश्चित गर्नुहोस्।

शानदार, हाम्रो अर्को कदमको लागि, अब सर्भरमा क्षमताहरू सूचीबद्ध गरौं।

### -2- सर्भर क्षमताहरू सूचीबद्ध गर्नुहोस्

अब हामी सर्भरसँग जडान गर्नेछौं र यसको क्षमता सोध्नेछौं:

#### Typescript

उस्तै क्लासमा तलका मेथडहरू थप्नुहोस्:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // उपकरणहरूको सूचीकरण
    const toolsResult = await this.client.listTools();
}
```

माथिल्लो कोडमा हामीले:

- सर्भरसँग जडान गर्ने कोड `connectToServer` थपेका छौं।
- `run` मेथड सिर्जना गरेका छौं जुन हाम्रो एप फ्लो ह्यान्डल गर्ने जिम्मेवार छ। अहिलेसम्म यसले मात्र उपकरणहरू सूचीबद्ध गरिरहेको छ तर हामी छिट्टै थप गर्नेछौं।

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

यहाँ हामीले थपेका छौं:

- स्रोतहरू र उपकरणहरू सूचीबद्ध गरेर प्रिन्ट गरेका छौं। उपकरणहरूका लागि हामीले `inputSchema` पनि सूचीबद्ध गरेका छौं जुन पछि प्रयोग गर्नेछौं।

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

माथिल्लो कोडमा हामीले:

- MCP सर्भरमा उपलब्ध उपकरणहरू सूचीबद्ध गरेका छौं
- प्रत्येक उपकरणको नाम, विवरण र स्कीमा सूचीबद्ध गरेका छौं। पछि उपकरणलाई कल गर्न यो प्रयोग हुनेछ।

#### Java

```java
// यस्तो उपकरण प्रदायक बनाउनुहोस् जुन स्वतः MCP उपकरणहरू पत्ता लगाउँछ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP उपकरण प्रदायक स्वचालित रूपमा ह्यान्डल गर्दछ:
// - MCP सर्भरबाट उपलब्ध उपकरणहरूको सूची तयार गर्ने
// - MCP उपकरण स्कीमाहरूलाई LangChain4j ढाँचामा रूपान्तरण गर्ने
// - उपकरण कार्यान्वयन र प्रतिक्रियाहरू व्यवस्थापन गर्ने
```

माथिल्लो कोडमा हामीले:

- `McpToolProvider` सिर्जना गरेका छौं जसले MCP सर्भरबाट सबै उपकरणहरू स्वचालित रूपमा पत्ता लगाउँछ र रजिस्टर गर्दछ
- उपकरण प्रदायकले MCP उपकरण स्कीमाहरू र LangChain4j को उपकरण ढाँचाबीच रूपान्तरण आन्तरिक रूपमा सम्हाल्छ
- यस दृष्टिकोणले म्यानुअल उपकरण सूचीकरण र रूपान्तरण प्रक्रिया हटाउँछ

#### Rust

MCP सर्भरबाट उपकरणहरू प्राप्त गर्न `list_tools` मेथड प्रयोग गरिन्छ। `main` फङ्क्शनमा, MCP क्लाइन्ट सेटअप पछि तल कोड थप्नुहोस्:

```rust
// MCP उपकरण सूची प्राप्त गर्नुहोस्
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्भर क्षमताहरू LLM उपकरणमा रूपान्तरण गर्नुहोस्

सर्भर क्षमताहरू सूचीबद्ध गरेपछि, अब तिनीहरूलाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्ने कुरा आउँछ। यसपछि, हामी यी क्षमताहरूलाई LLM का लागि उपकरणहरूका रूपमा प्रदान गर्न सक्छौं।

#### TypeScript

1. MCP सर्भरबाट प्राप्त प्रतिक्रियालाई LLM ले प्रयोग गर्नसक्ने उपकरण ढाँचामा रूपान्तरण गर्न तलको कोड थप्नुहोस्:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema आधारित एक zod schema बनाउनुहोस्
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकारलाई स्पष्ट रूपमा "function" सेट गर्नुहोस्
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

    माथिको कोडले MCP सर्भरको प्रतिक्रिया लिये तापनि LLM ले बुझ्ने उपकरण परिभाषा ढाँचामा परिवर्तित गर्दछ।

1. `run` मेथड अपडेट गरेर सर्भर क्षमताहरू सूचीबद्ध गरौं:

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

    माथिल्लो कोडमा, हामीले `run` मेथडलाई परिणाममा म्याप गरेर प्रत्येक प्रविष्टिमा `openAiToolAdapter` कल गरेका छौं।

#### Python

1. पहिला तलको कन्वर्टर फङ्क्शन बनाऔँ:

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

    माथिको `convert_to_llm_tools` फङ्क्शनमा, हामीले MCP उपकरणको प्रतिक्रिया लिएर त्यसलाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्छौं।

1. त्यसपछि, हाम्रो क्लाइन्ट कोडलाई यस फङ्क्शन प्रयोग गर्न अपडेट गरौं:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ, हामीले MCP उपकरणको प्रतिक्रियालाई LLM लाई पठाउनसक्ने रूपमा रूपान्तरण गर्न `convert_to_llm_tool` कल थपेका छौं।

#### .NET

1. MCP उपकरण प्रतिक्रिया LLM ले बुझ्ने रूपमा रूपान्तरण गर्न कोड थपौं:

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

माथिल्लो कोडमा हामीले:

- `ConvertFrom` नामक फङ्क्शन बनाएका छौं जसले नाम, विवरण र इनपुट स्कीमा लिन्छ।
- यसले एक `FunctionDefinition` सिर्जना गर्ने कार्यक्षमता परिभाषित गर्छ जुन `ChatCompletionsDefinition` मा पास हुन्छ। यो LLM ले बुझ्ने कुरा हो।

1. अब कसरी पुरानो कोडलाई यस फङ्क्शनको प्रयोग गर्ने गरी अपडेट गर्ने हेर्नुहोस्:

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
// स्वाभाविक भाषा अन्तर्क्रियाका लागि बोट इंटरफेस बनाउनुहोस्
public interface Bot {
    String chat(String prompt);
}

// LLM र MCP उपकरणहरूसँग AI सेवा कन्फिगर गर्नुहोस्
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

माथिल्लो कोडमा हामीले:

- प्राकृतिक भाषाका अन्तरक्रियाका लागि सरल `Bot` इन्टरफेस परिभाषित गरेका छौं
- LangChain4j को `AiServices` प्रयोग गरेर LLM लाई MCP उपकरण प्रदायकसँग स्वचालित रूपमा बाँध्ने गरेका छौं
- फ्रेमवर्कले स्वचालित रूपमा उपकरण स्कीमा रूपान्तरण र फङ्क्शन कल व्यबस्थापन गर्छ
- यसले म्यानुअल उपकरण रूपान्तरण हटाउँछ - LangChain4j ले MCP उपकरणहरूलाई LLM अनुकूल ढाँचामा रूपान्तरण गर्ने सबै जटिलता सम्हाल्छ

#### Rust

MCP उपकरण प्रतिक्रियालाई LLM बुझ्ने ढाँचामा रूपान्तरण गर्न, हामी एक सहायक फङ्क्शन थप्नेछौं जसले उपकरण सूचीकरणलाई ढाँचा दिनेछ। `main` फङ्क्शन तल तपाईंको `main.rs` फाइलमा तलको कोड थप्नुहोस्। यसलाई LLM अनुरोध गर्दा कल गरिनेछ:

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

शानदार, अब हामी कुनै प्रयोगकर्ता अनुरोध ह्यान्डल गर्न तयार छौं, त्यसपछि त्यसलाई अगाडि बढाऔं।

### -4- प्रयोगकर्ताको प्रम्प्ट अनुरोध ह्यान्डल गर्नुहोस्

यस भागमा हामी प्रयोगकर्ताहरूका अनुरोधहरू ह्यान्डल गर्नेछौं।

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
        // गर्ने कुरा

        }
    }
    ```

    माथिल्लो कोडमा हामीले:

    - `callTools` नामक मेथड थपेका छौं।
    - मेथडले LLM प्रतिक्रिया लिएर कुन उपकरणहरू कल भएका छन् हेर्छ, यदि कुनै छन् भने:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // उपकरण कल गर्नुहोस्
        }
        ```

    - उपकरण कल गर्छ, यदि LLM ले कल गर्नु उपयुक्त ठाने भने:

        ```typescript
        // २. सर्भरको उपकरण कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. परिणामसँग केही गर्नुहोस्
        // TODO
        ```

1. `run` मेथड अपडेट गरेर LLM कल र `callTools` समावेश गरौं:

    ```typescript

    // 1. LLM को लागि इनपुट सन्देशहरू तयार पार्नुहोस्
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM लाई कल गर्दै
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM को प्रतिक्रिया जाँच्नुहोस्, प्रत्येक विकल्पको लागि, यसमा उपकरण कलहरू छन् कि छैन जाँच गर्नुहोस्
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

शानदार, सम्पूर्ण कोड तल सूचीबद्ध गरौं:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्किमा मान्यताको लागि zod इम्पोर्ट गर्नुहोस्

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्यमा यो URL मा परिवर्तन गर्न हुन सक्छ: https://models.github.ai/inference
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
          // इनपुट_स्किमा आधारित zod स्किमा बनाउनुहोस्
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
    
    
          // २. सर्भरको उपकरण कल गर्नुहोस्
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ३. नतिजासँग केहि गर्नुहोस्
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
    
        // १. LLM प्रतिक्रियामा हिँड्नुहोस्, प्रत्येक विकल्पको लागि, उपकरण कल छ कि छैन जाँच गर्नुहोस्
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

1. LLM कल गर्न आवश्यक इम्पोर्टहरू थपौं:

    ```python
    # एलएलएम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM कल गर्ने फङ्क्शन थपौं:

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

    माथिल्लो कोडमा हामीले:

    - फङ्क्शनहरू (जो MCP सर्भरमा भेटेका छौं र रूपान्तरण गरेका छौं) LLM लाई पास गरेका छौं।
    - त्यसपछि LLM लाई ती फङ्क्शनहरूका साथ कल गरेका छौं।
    - परिणामलाई निरीक्षण गरेर कुन फङ्क्शन कल गर्ने निर्णय लिन्छौं।
    - अन्ततः फङ्क्शनहरूको array पास गर्छौं।

1. अन्तिम चरण, मुख्य कोड अपडेट गरौं:

    ```python
    prompt = "Add 2 to 20"

    # LLM लाई सोध्नुहोस् कि सबैका लागि कुन उपकरणहरू छन्, यदि कुनै छन् भने
    functions_to_call = call_llm(prompt, functions)

    # सुझाव गरिएको कार्यहरू कल गर्नुहोस्
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    माथिल्लो कोडमा:

    - LLM ले जुन फङ्क्शन कल गर्नुपर्ने ठानेको छ, त्यसलाई `call_tool` बाट MCP उपकरणमा कल गर्छौं।
    - उपकरण कल सीम्यूले प्राप्त परिणाम प्रिन्ट गर्छौं।

#### .NET

1. LLM प्रम्प्ट अनुरोधका लागि केही कोड हेरौं:

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

    माथिल्लो कोडमा हामीले:

    - MCP सर्भरबाट उपकरणहरू प्राप्त गरेका छौं, `var tools = await GetMcpTools()`।
    - प्रयोगकर्ताको प्रम्प्ट `userMessage` परिभाषित गरेका छौं।
    - मोडेल र उपकरणहरू निर्दिष्ट गरेर अप्सन वस्तु तयार पारेका छौं।
    - LLM तर्फ अनुरोध गरेका छौं।

1. अन्तिम चरण, LLM ले फङ्क्शन कल गर्नुपर्ने छ कि छैन जाँचौं:

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

    माथिल्लो कोडमा हामीले:

    - फङ्क्शन कलहरूको सूचीमा लूप गरेका छौं।
    - हरेक उपकरण कलको लागि नाम र आर्गुमेन्ट्स पार्स गरेर MCP सर्भरमा MCP क्लाइन्ट प्रयोग गरी उपकरण कल गरेका छौं। अन्ततः परिणाम प्रिन्ट गरेका छौं।

यहाँ सम्पूर्ण कोड छ:

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
    // MCP उपकरणहरू स्वचालित रूपमा प्रयोग गर्ने प्राकृतिक भाषा अनुरोधहरू कार्यान्वयन गर्नुहोस्
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

माथिल्लो कोडमा हामीले:

- सरल प्राकृतिक भाषा प्रम्प्ट प्रयोग गरेर MCP सर्भर उपकरणहरूसँग अन्तरक्रिया गरेका छौं
- LangChain4j फ्रेमवर्कले स्वचालित रूपमा सम्हाल्छ:
  - आवश्यकता अनुसार प्रयोगकर्ताको प्रम्प्टलाई उपकरण कलमा रूपान्तरण गर्नु
  - LLM को निर्णय अनुसार उपयुक्त MCP उपकरणहरू कल गर्नु
  - LLM र MCP सर्भर बीच संवाद प्रवाह व्यवस्थापन गर्नु
- `bot.chat()` मेथडले प्राकृतिक भाषा प्रतिक्रियाहरू फर्काउँछ जसमा MCP उपकरण निष्पादनका परिणामहरू समावेश हुन सक्छन्
- यसले प्रयोगकर्ताहरूलाई MCP को आधारभूत कार्यान्वयन थाहा नहुँदै सहज प्रयोगकर्ता अनुभव प्रदान गर्दछ

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

यहाँ मुख्य काम हुन्छ। हामीले प्रारम्भिक प्रयोगकर्ता प्रम्प्ट सहित LLM कल गर्नेछौं, त्यसपछि प्रतिक्रिया प्रक्रिया गरेर कुन उपकरण कल गर्नुपर्ने हो हेर्नेछौं। आवश्यक भए ती उपकरणहरू कल गरेर LLM सँग संवाद जारी राख्नेछौं जबसम्म थप उपकरण कल आवश्यक नहुने र अन्तिम प्रतिक्रिया नआउञ्जेल।

हामी LLM लाई धेरै पटक कल गर्नेछौं, त्यसैले हामी एक फङ्क्शन परिभाषित गर्नेछौं जुन LLM कल ह्यान्डल गर्नेछ। तलको फङ्क्शन `main.rs` फाइलमा थप्नुहोस्:

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

यो फङ्क्शनले LLM क्लाइन्ट, सन्देशहरूको सूची (प्रयोगकर्ता प्रम्प्ट सहित), MCP सर्भरका उपकरणहरू लिन्छ र LLM लाई अनुरोध पठाउँछ, प्रतिक्रिया फर्काउँछ।
LLM बाट आएको प्रतिक्रिया `choices` को एउटा एरे समावेश गर्नेछ। हामीले परिणामलाई प्रक्रिया गर्नुपर्नेछ कि कुनै `tool_calls` छन् कि छैनन्। यसले हामीलाई थाहा हुन्छ कि LLM ले विशिष्ट उपकरणलाई तर्कहरू सहित बोलाउन अनुरोध गरेको छ। LLM प्रतिक्रिया ह्यान्डल गर्न तलको कोडलाई आफ्नो `main.rs` फाइलको अन्त्यमा थप्नुहोस्:

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

    // सामग्री उपलब्ध भएमा छाप्नुहोस्
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // उपकरण कलहरू सम्हाल्नुहोस्
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

        // उपकरण परिणामहरूसँग कुरा जारी राख्नुहोस्
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

यदि `tool_calls` हरू उपस्थित छन् भने, यसले उपकरण जानकारी निकाल्छ, उपकरण अनुरोध सहित MCP सर्भरलाई कल गर्छ, र परिणामहरूलाई कुराकानी सन्देशहरूमा थप्छ। त्यसपछि यो LLM सँग कुराकानी जारी राख्छ र सन्देशहरू सहायकको प्रतिक्रिया र उपकरण कल परिणामहरूसँग अद्यावधिक गरिन्छ।

LLM ले MCP कलहरूको लागि फिर्ता गर्ने उपकरण कल जानकारी निकाल्न हामी अर्को हेल्पर फङ्क्शन थप्नेछौं जसले कल गर्न आवश्यक सबै कुरा निकाल्छ। तलको कोडलाई आफ्नो `main.rs` फाइलको अन्त्यमा थप्नुहोस्:

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

सबै भागहरू तयार भएपछि, हामीले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टलाई ह्यान्डल गरी LLMलाई कल गर्न सक्छौं। आफ्नो `main` फङ्क्शनलाई तलको कोड समावेश गर्न अपडेट गर्नुहोस्:

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

यसले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टसँग LLM लाई प्रश्न गर्नेछ जुन दुई संख्याको योग फर्माउँछ, र प्रतिक्रिया प्रक्रियागर्न उपकरण कलहरू गतिशील रूपमा ह्यान्डल गर्नेछ।

शानदार, तपाईंले यो गर्नुभयो!

## असाइन्मेन्ट

कसरतबाट कोड लिएर सर्भरमा केही थप उपकरणहरू निर्माण गर्नुहोस्। त्यसपछि कसरतमा भएको जस्तै LLM सहित क्लाइन्ट सिर्जना गरेर विभिन्न प्रॉम्प्टहरूसँग परीक्षण गर्नुहोस् ताकि तपाईंको सबै सर्भर उपकरणहरू गतिशील रूपमा कल हुन्छन् भनी सुनिश्चित गर्न सकियोस्। यसरी क्लाइन्ट बनाउनुले अन्तिम प्रयोगकर्तालाई राम्रो प्रयोगकर्ता अनुभव दिनेछ किनकि उनीहरूले ठीक क्लाइन्ट कमाण्डहरूबाट नभई प्रॉम्प्टहरू प्रयोग गर्न सक्नेछन् र कुनै MCP सर्भर कल भइरहेको हुनुको बारेमा थाहा नपाउनेछन्।

## समाधान

[Solution](./solution/README.md)

## मुख्य निष्कर्षहरू

- आफ्नो क्लाइन्टमा LLM थप्दा MCP सर्भरहरूसँग प्रयोगकर्ताहरूले अन्तरक्रिया गर्न राम्रो तरिका प्रदान गर्छ।
- तपाईंले MCP सर्भर प्रतिक्रियालाई LLM लाई बुझ्न सक्ने स्वरूपमा रूपान्तरण गर्नुपर्ने हुन्छ।

## नमूनाहरू

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## थप स्रोतहरू

## अर्को के छ

- अर्को: [Visual Studio Code प्रयोग गरी सर्भर उपभोग गर्ने](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको प्रयास गर्छौं, तर कृपया सचेत हुनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा गलतफहमीहरू हुन सक्छन्। मूल दस्तावेज यसको स्वदेशी भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->