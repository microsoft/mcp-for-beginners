# LLM सहित क्लाइंट निर्माण

अहिलेसम्म, तपाईंले कसरी सर्भर र क्लाइंट बनाउन सकिन्छ भनेर देख्नुभयो। क्लाइंटले स्पष्ट रूपमा सर्भरलाई कल गरेर यसको उपकरणहरू, स्रोतहरू, र प्रॉम्प्टहरू सूचीबद्ध गर्न सक्षम छ। यद्यपि, यो व्यावहारिक दृष्टिकोण होइन। तपाईंका प्रयोगकर्ताहरू एजेन्टिक युगमा बस्थे र प्रॉम्प्टहरू प्रयोग गर्न र LLM सँग संवाद गर्न चाहन्छन्। तिनीहरूलाई तपाईंले आफ्नो क्षमता भण्डारण गर्न MCP प्रयोग गर्नुभयो कि छैन भन्ने कुरा चासो छैन; तिनीहरू सरल प्राकृतिक भाषाको प्रयोग गरेर अन्तरक्रिया अपेक्षा गर्छन्। त्यसो भए यो कसरी समाधान गर्ने? समाधान हो क्लाइंटमा LLM थप्नु।

## अवलोकन

यस पाठमा हामीले आफ्नो क्लाइंटमा LLM थप्नेमा केन्द्रित गर्दैछौं र यसले तपाईंका प्रयोगकर्ताका लागि कसरी उत्तम अनुभव प्रदान गर्छ भनेर देखाउँछौं।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- LLM सहित क्लाइंट बनाउने।
- LLM प्रयोग गरेर सीमान्त रूपमा MCP सर्भरसँग अन्तरक्रिया गर्न।
- क्लाइंट पक्षमा उत्तम अन्तिम प्रयोगकर्ता अनुभव प्रदान गर्न।

## दृष्टिकोण

हामीले लिनुपर्ने दृष्टिकोण बुझ्ने प्रयास गरौं। LLM थप्नु सरल लाग्छ, तर हामी साँच्चै यसो गर्नेछौं?

क्लाइंटले सर्भर सँग कसरी अन्तरक्रिया गर्नेछ:

१. सर्भर सँग जडान स्थापना गर्नु।

२. क्षमताहरू, प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरू सूचीबद्ध गरी तिनको स्कीमा बचत गर्नु।

३. LLM थप्नु र बचत गरिएका क्षमताहरू र स्कीमालाई LLM बुझ्ने ढाँचामा पास गर्नु।

४. प्रयोगकर्ता प्रॉम्प्टलाई LLM सँग पास गरी क्लाइंटले सूचीबद्ध गरेका उपकरणहरू समेत पास गर्नु।

राम्रो, अब हामीले उच्च स्तरमा कसरी गर्ने बुझ्यौं, तलको अभ्यासमा प्रयास गरौं।

## अभ्यास: LLM सहित क्लाइंट बनाउने

यस अभ्यासमा, हामी आफ्नो क्लाइंटमा LLM थप्न सिक्नेछौं।

### GitHub व्यक्तिगत पहुँच टोकन प्रयोग गरी प्रमाणीकरण

GitHub टोकन बनाउने प्रक्रिया सरल छ। यसरी गर्न सकिन्छ:

- GitHub सेटिङहरूमा जानुहोस् – माथि दायाँ कुनामा प्रोफाइल चित्र क्लिक गरी सेटिङहरू चयन गर्नुहोस्।
- Developer सेटिङहरूमा जानुहोस् – तल स्क्रोल गरी Developer सेटिङहरू क्लिक गर्नुहोस्।
- Personal Access Tokens छान्नुहोस् – Fine-grained tokens क्लिक गरी नयाँ टोकन जेनेरेट गर्नुहोस्।
- आफ्नो टोकन कन्फिगर गर्नुहोस् – सन्दर्भका लागि नोट थप्नुहोस्, समाप्ति मिति सेट गर्नुहोस्, आवश्यक स्कोपहरू चयन गर्नुहोस्। यस अवस्थामा Models अनुमतिले सुनिश्चित गर्नुहोस्।
- टोकन जेनेरेट गरी तुरुन्तै कपी गर्नुहोस् किनभने पुन: हेर्न सकिन्न।

### -1- सर्भर सँग जडान गर्नुहोस्

पहिला आफ्नो क्लाइंट बनाऔं:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा प्रमाणीकरणका लागि zod आयात गर्नुहोस्

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

माथिको कोडमा हामीले:

- आवश्यक पुस्तकालयहरू आयात गर्यौं
- दुई सदस्यहरू भएको वर्ग बनायौं, `client` र `openai` जसले हामीलाई क्लाइंट व्यवस्थापन र LLM सँग अन्तरक्रिया गर्न सहयोग गर्दछ।
- हाम्रो LLM उदाहरणलाई GitHub Models प्रयोग गर्न `baseUrl` सेट गरी इन्फरेन्स API तर्फ संकेत गरियो।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानका लागि सर्भर प्यारामिटरहरू सिर्जना गर्नुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयन योग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन तर्कहरू
    env=None,  # वैकल्पिक वातावरण चरहरू
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # जडान आरम्भ गर्नुहोस्
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

माथिको कोडमा हामीले:

- MCP का लागि आवश्यक पुस्तकालयहरू आयात गर्यौं
- क्लाइंट बनायौं

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

पहिलो, तपाईंले `pom.xml` फाइलमा LangChain4j निर्भरता थप्न आवश्यक छ। यसले MCP एकीकरण र OpenAI-संगत MiniMax API सक्षम पार्छ:

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

आफ्नो MiniMax API कुञ्जी र, वैकल्पिक रूपमा, अन्तबिन्दु र मोडेल सेट गर्नुहोस्।
`MINIMAX_MODEL_ID` ले `MiniMax-M3` र `MiniMax-M2.7` लाई समर्थन गर्छ। यदि
`OPENAI_BASE_URL` सेट नभएमा, `MINIMAX_REGION` ले `global_en` र `cn_zh` लाई समर्थन गर्छ।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

क्षेत्र द्वारा अन्तबिन्दु चयन गर्न `OPENAI_BASE_URL` छोड्नुहोस्:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

त्यसपछि Java क्लाइंट वर्ग बनाउनुहोस्:

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

माथिको कोडमा हामीले:

- **LangChain4j निर्भरता थप्यौं**: MCP एकीकरण र OpenAI-संगत MiniMax API का लागि आवश्यक
- **LangChain4j पुस्तकालय आयात गर्यौं**: MCP एकीकरण र OpenAI च्याट मोडेल कार्यक्षमताका लागि
- **`ChatLanguageModel` बनायौं**: MiniMax प्रयोग गर्न MiniMax API कुञ्जी, अन्तबिन्दु, र मोडेल ID सेट गर्दै
- **HTTP ट्रान्सपोर्ट सेटअप गर्यौं**: Server-Sent Events (SSE) प्रयोग गरी MCP सर्भरसँग जडान गर्न
- **MCP क्लाइंट बनायौं**: सर्भरसँग संवाद सँभाल्न
- **LangChain4j को MCP समर्थन प्रयोग गर्यौं**: जसले LLM र MCP सर्भरबीच एकीकरण सजिलो बनाउँछ

#### Rust

यस उदाहरणले तपाईंले Rust आधारित MCP सर्भर चलाइरहनुभएको छ भनी मानिन्छ। यदि छैन भने, [01-first-server](../01-first-server/README.md) पाठमा फर्केर सर्भर बनाउनुहोस्।

Rust MCP सर्भर भएपछि, टर्मिनल खोल्नुहोस् र सर्भर रहेको फोल्डरमा जानुहोस्। त्यसपछि नयाँ LLM क्लाइंट प्रोजेक्ट बनाउन तलको आदेश चलाउनुहोस्:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

आफ्नो `Cargo.toml` फाइलमा तलका निर्भरता थप्नुहोस्:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI को लागि आधिकारिक Rust पुस्तकालय छैन, यद्यपि `async-openai` क्रेट एक [समुदाय द्वारा संचालित पुस्तकालय](https://platform.openai.com/docs/libraries/rust#rust) हो जुन सामान्य प्रयोगमा छ।

`src/main.rs` फाइल खोल्नुहोस् र यसका सामग्री निम्न कोडले प्रतिस्थापन गर्नुहोस्:

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
    // आरम्भिक सन्देश
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

    // TODO: उपकरण कलहरू सहित LLM संवाद गर्नुहोस्

    Ok(())
}
```

यस कोडले बेसिक Rust अनुप्रयोग सेटअप गर्दछ जुन MCP सर्भर र GitHub Models सँग LLM अन्तरक्रियाका लागि जडान हुनेछ।

> [!IMPORTANT]
> अनुप्रयोग चलाउनु अघि आफ्नो GitHub टोकन सहित `OPENAI_API_KEY` वातावरण चर सेट गर्नुहोस्।

राम्रो, अर्को चरणका लागि, सर्भरमा उपलब्ध क्षमताहरू सूचीबद्ध गरौं।

### -2- सर्भर क्षमताहरू सूचीबद्ध गर्नुहोस्

अब हामी सर्भरसँग जडान गरी यसको क्षमताहरू सोध्नेछौं:

#### Typescript

उही कक्षामा तलको मेथडहरू थप्नुहोस्:

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

माथिको कोडमा हामीले:

- सर्भर सँग जडान गर्ने कोड थप्यौं, `connectToServer`.
- `run` मेथड बनायौं जसले हाम्रो एप फलो ह्यान्डल गर्छ। अहिलेसम्म यो केवल उपकरणहरू सूचीबद्ध गर्छ तर छिट्टै थप्नेछौं।

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

थपेको कुरा:

- स्रोतहरू र उपकरणहरू सूचीबद्ध गर्यौं र तिनलाई प्रिन्ट गर्यौं। उपकरणहरूको लागि हामीले `inputSchema` पनि सूचीबद्ध गर्यौं जुन पछि प्रयोग गर्नेछौं।

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

माथिको कोडमा हामीले:

- MCP सर्भरमा उपलब्ध उपकरणहरू सूचीबद्ध गर्यौं
- प्रत्येक उपकरणको नाम, विवरण र स्कीमा सूचीबद्ध गर्यौं। पछि उपकरण कल गर्न स्कीमा प्रयोग हुनेछ।

#### Java

```java
// एउटा उपकरण प्रदायक सिर्जना गर्नुहोस् जुन स्वतः MCP उपकरणहरू पत्ता लगाउँछ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP उपकरण प्रदायकले स्वचालित रूपमा ह्यान्डल गर्दछ:
// - MCP सर्भरबाट उपलब्ध उपकरणहरूको सूची बनाउने
// - MCP उपकरण स्किमाहरूलाई LangChain4j ढाँचामा रूपान्तरण गर्ने
// - उपकरण सञ्चालन र प्रतिक्रियाहरू व्यवस्थापन गर्ने
```

माथिको कोडमा हामीले:

- `McpToolProvider` बनायौं जसले स्वचालित रूपमा सबै उपकरणहरू पत्ता लगाउने र दर्ता गर्ने MCP सर्भरबाट
- उपकरण प्रदायकले MCP उपकरण स्कीमा र LangChain4j उपकरण ढाँचाबीच रूपान्तरण भित्रै ह्यान्डल गर्छ
- यसले म्यानुअल उपकरण सूचीबद्धता र रूपान्तरण प्रक्रियालाई लुकाउँछ

#### Rust

MCP सर्भरबाट उपकरणहरू लिन `list_tools` मेथड प्रयोग गरिन्छ। `main` फंक्शनमा MCP क्लाइंट सेटअपपछि तलको कोड थप्नुहोस्:

```rust
// MCP टुल सूची प्राप्त गर्नुहोस्
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्भर क्षमताहरूलाई LLM उपकरणहरूमा रूपान्तरण गर्नुहोस्

सर्भर क्षमताहरू सूचीबद्ध गरेपछि, तिनीहरूलाई LLM बुझ्ने ढाँचामा रूपान्तरण गर्नु अर्को कदम हो। त्यसपछि हामी ती क्षमताहरूलाई उपकरणको रूपमा LLM लाई उपलब्ध गराउन सक्छौं।

#### TypeScript

१. MCP सर्भरबाट आएको प्रतिक्रियालाई LLM प्रयोग गर्न सक्ने उपकरण ढाँचामा रूपान्तरण गर्न तलको कोड थप्नुहोस्:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्किमा अनुसार एउटा zod स्किमा सिर्जना गर्नुहोस्
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // प्रकारलाई स्पष्ट रूपले "function" सेट गर्नुहोस्
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

    माथिको कोडले MCP सर्भरको प्रतिक्रिया लिन्छ र LLM ले बुझ्ने उपकरण परिभाषा ढाँचामा रूपान्तरण गर्छ।

२. अब `run` मेथड अपडेट गरौं ताकि सर्भर क्षमताहरू सूचीबद्ध होस:

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

    माथिका कोडमा `run` मेथडलाई परिणामबाट म्याप गरेर प्रत्येक प्रविष्टिमा `openAiToolAdapter` कल गर्ने गरी अपडेट गरिएको छ।

#### Python

१. पहिला, तलको रूपान्तरण गर्ने फंक्शन बनाऔं

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

    माथि रहेको `convert_to_llm_tools` फंक्शनले MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्छ।

२. अब हाम्रो क्लाइंट कोडलाई यस फंक्शन प्रयोग गर्न अपडेट गरौं:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ हामी `convert_to_llm_tool` कल थप्दैछौं जसले MCP उपकरण प्रतिक्रियालाई पछि LLM लाई दिने योग्य बनाउँछ।

#### .NET

१. MCP उपकरण प्रतिक्रियालाई LLM बुझ्ने योग्यमा रूपान्तरण गर्न कोड थपौं

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

माथिको कोडमा हामीले:

- `ConvertFrom` नामक फंक्शन बनायौं जुन नाम, विवरण र इनपुट स्कीमा लिन्छ।
- यस्तो कार्यक्षमता परिभाषित गर्यौं जसले FunctionDefinition तयार गरी ChatCompletionsDefinition मा पठाउँछ। पछिल्लो LLM लाई बुझिन्छ।

२. अब केही अवस्थित कोडलाई माथिको फंक्शन उपयोग गर्न अपडेट गरौं:

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
// प्राकृतिक भाषा अन्तरक्रियाको लागि बोट इन्टरफेस सिर्जना गर्नुहोस्
public interface Bot {
    String chat(String prompt);
}

// LLM र MCP उपकरणहरूसँग AI सेवा कन्फिगर गर्नुहोस्
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

माथिको कोडमा हामीले:

- प्राकृतिक भाषा अन्तरक्रियाका लागि सरल `Bot` अन्तरफलक परिभाषित गर्यौं
- LangChain4j को `AiServices` प्रयोग गरेर LLM लाई MCP उपकरण प्रदायकसँग स्वचालित बाँध गर्यौं
- फ्रेमवर्कले स्वचालित रूपमा उपकरण स्कीमा रूपान्तरण र फंक्शन कल ह्यान्डल गर्छ
- यसले म्यानुअल उपकरण रूपान्तरण हटाउँछ - LangChain4j ले सबै जटिलता ह्यान्डल गर्छ MCP उपकरणहरू LLM-अनुकूल ढाँचामा रूपान्तरणमा

#### Rust

MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने संरचनामा रूपान्तरण गर्न, हामी एउटा सहायक फंक्शन थप्नेछौं जसले उपकरण सूचीकरणलाई ढाँचा बनाउँछ। तल `main` फंक्शनभन्दा तलको कोड `main.rs` फाइलमा थप्नुहोस्। यो LLM अनुरोध गर्दा प्रयोग हुनेछ:

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

राम्रो, अहिले हामीले प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्नु पाएनौं, त्यसो भए अब त्योतर्फ लागौं।

### -4- प्रयोगकर्ता प्रॉम्प्ट अनुरोध ह्यान्डल गर्नुहोस्

कोडको यस भागमा हामी प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्नेछौं।

#### TypeScript

१. हाम्रो LLM कल गर्न प्रयोग हुने मेथड थप्नुहोस्:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // २। सर्भरको उपकरणलाई कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३। परिणामसँग केहि गर्नुहोस्
        // गर्नुपर्ने छ

        }
    }
    ```

माथिको कोडमा हामीले:

- `callTools` मेथड थप्यौं।
- मेथडले LLM प्रतिक्रियालाई लिन्छ र हेर्छ कुन उपकरणहरू कल गरिएको छ, यदि कुनै छ भने:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // उपकरण कल गर्नुहोस्
        }
        ```

- LLM ले कल गर्नुपर्ने भन्यो भने उपकरण कल गर्छ:

        ```typescript
        // २. सर्भरको उपकरणलाई कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. परिणामसँग केही गर्नुहोस्
        // गर्नु पर्ने काम
        ```

२. `run` मेथड अपडेट गरी LLM र `callTools` कल थप्नुहोस्:

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

    // २. LLM लाई कल गर्दैछ
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ३. LLM उत्तरलाई हेरौं, प्रत्येक विकल्पको लागि, जाँच गर्नुहोस् कि यसमा उपकरण कलहरू छन् कि छैनन्
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

राम्रो, पूर्ण कोड यस्तो छ:

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
            baseURL: "https://models.inference.ai.azure.com", // भविष्यमा यो URL मा परिवर्तन गर्न आवश्यक हुन सक्छ: https://models.github.ai/inference
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
          // इनपुट_स्कीमा आधारित zod स्कीमा सिर्जना गर्नुहोस्
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
    
          // 3. नतिजासँग केही गर्नुहोस्
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
    
        // 3. LLM प्रतिक्रिया मार्फत जानुहोस्, प्रत्येक विकल्पको लागि, यदि यसमा उपकरण कलहरू छन् भने जाँच गर्नुहोस्
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

१. LLM कल गर्न आवश्यक आयातहरू थपौं

    ```python
    # ल्ल्म
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

२. LLM कल गर्ने फंक्शन थपौं:

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

माथिको कोडमा हामीले:

- MCP सर्वरमा भेटिएका र रूपान्तरण गरिएका फंक्शनहरूलाई LLM लाई पास गर्यौं।
- त्यसपछि ती फंक्शनहरू सहित LLM कल गर्यौं।
- परिणाम निरीक्षण गर्यौं कुन फंक्शनहरू कल गर्नुपर्छ हेर्न।
- अन्ततः कल गर्नुपर्ने फंक्शनहरूको एरे पास गयौं।

३. मुख्य कोड अपडेट गरौं:

    ```python
    prompt = "Add 2 to 20"

    # सबैलाई कुन उपकरणहरू सोध्न LLM, कुनै भएमा
    functions_to_call = call_llm(prompt, functions)

    # सुझाव गरिएको कार्यहरू कल गर्नुहोस्
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

माथि कोडमा जस्तै हामी:

- LLM ले प्रस्ताव गरेको फंक्शन प्रयोग गरी `call_tool` मार्फत MCP उपकरण कल गर्छौं।
- उपकरण कलको परिणाम MCP सर्भरमा प्रिन्ट गर्छौं।

#### .NET

१. LLM प्रॉम्प्ट अनुरोध गर्ने कोड देखाउँछौं:

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

माथिको कोडमा हामीले:

- MCP सर्भरबाट उपकरण ल्यायौं, `var tools = await GetMcpTools()`.
- प्रयोगकर्ता प्रॉम्प्ट `userMessage` परिभाषित गर्यौं।
- मोडेल र उपकरण निर्दिष्ट गरी विकल्प वस्तु बनायौं।
- LLM तर्फ अनुरोध पठायौं।

२. अन्तिम चरण, LLM ले कुनै फंक्शन कल गर्नुपर्छ कि भनेर जाँचौं:

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

माथिको कोडमा हामीले:

- फंक्शन कलहरूको सूचीमा लूप गर्यौं।
- प्रत्येक उपकरण कलका लागि नाम र तर्क पार्स गरी MCP क्लाइंट प्रयोग गरी उपकरण कल गर्यौं। अन्ततः नतिजा प्रिन्ट गर्यौं।

पूर्ण कोड यसप्रकार छ:

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

माथिको कोडमा हामीले:

- MCP सर्भर उपकरणहरूसँग सरल प्राकृतिक भाषा प्रॉम्प्टले अन्तरक्रिया गर्यौं
- LangChain4j फ्रेमवर्कले स्वचालित रूपमा ह्यान्डल गर्छ:
  - आवश्यक पर्दा प्रयोगकर्ता प्रॉम्प्टलाई उपकरण कलमा रूपान्तरण
  - LLM को निर्णय अनुसार उचित MCP उपकरणहरु कल गर्ने
  - LLM र MCP सर्भरबीच संवाद प्रवाह व्यवस्थापन
- `bot.chat()` मेथडले प्राकृतिक भाषा प्रतिक्रियाहरू फर्काउँछ जसमा MCP उपकरणको परिणाम पनि समावेश हुन सक्छ
- यसले प्रयोगकर्ताका लागि सहज अनुभव प्रदान गर्दछ जहाँ तिनीहरूलाई MCP इम्प्लिमेन्टेशनको ज्ञान आवश्यक पर्दैन

पूर्ण कोड उदाहरण:

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

यहाँ सबैभन्दा धेरै काम हुन्छ। हामी आरम्भिक प्रयोगकर्ता प्रॉम्प्ट LLM लाई कल गर्छौं, त्यसपछि जवाफ प्रक्रियाकरण गरी हेर्छौं कुनै उपकरण कल गर्नु पर्छ कि। यदि हो भने, ती उपकरणहरू कल गर्छौं र LLM सँग संवाद जारी राख्छौं जबसम्म थप उपकरण कल आवश्यक नपरोस् र अन्तिम प्रतिक्रिया प्राप्त नहोस्।


हामी LLM सँग धेरै पटक कल गर्नेछौं, त्यसैले एस्तो फङ्क्सन परिभाषित गरौं जसले LLM कललाई व्यवस्थापन गर्छ। तपाइँको `main.rs` फाइलमा तलको फङ्क्सन थप्नुहोस्:

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

यस फङ्क्सनले LLM क्लाइन्ट, सन्देशहरूको सूची (प्रयोगकर्ताको प्रम्प्ट सहित), MCP सर्भरका उपकरणहरू लिन्छ र LLM लाई अनुरोध पठाउँछ, र जवाफ फर्काउँछ।

LLM बाट आएको जवाफमा `choices` नामक एरे हुने छ। हामीले परिणाम प्रक्रिया गर्नुपर्छ र हेर्नुपर्छ कि कुनै `tool_calls` छन् कि छैनन्। यसले देखाउँछ कि LLM ले खास उपकरणलाई आर्गुमेन्टसहित कल गर्न चाहन्छ। तपाइँको `main.rs` फाइलको तल्लो भागमा तलको कोड थपेर LLM प्रतिक्रिया व्यवस्थापन गर्ने फङ्क्सन परिभाषित गर्नुहोस्:

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

    // उपकरण कलहरू व्यवस्थापन गर्नुहोस्
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

            // सन्देशहरूमा उपकरण नतिजा थप्नुहोस्
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // उपकरण नतिजासँग संवाद जारी राख्नुहोस्
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

यदि `tool_calls` उपस्थित छन् भने, यसले उपकरणको जानकारी निकाल्छ, MCP सर्भरलाई उपकरण अनुरोधसहित कल गर्छ, र परिणामहरूलाई संवाद सन्देशहरूमा थप्छ। त्यसपछि यो LLM सँग संवाद जारी राख्छ र सन्देशहरू सहायकको प्रतिक्रिया र उपकरण कल परिणामहरूसँग अद्यावधिक हुन्छन्।

LLM ले MCP कलहरूका लागि फर्काएको उपकरण कल जानकारी निकाल्न, हामी अर्को सहायक फङ्क्सन थप्नेछौं जसले कल गर्न आवश्यक सबै विवरण निकाल्छ। तलको कोड तपाइँको `main.rs` फाइलको तल्लो भागमा थप्नुहोस्:

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

सबै भागहरू तयार भएपछि, अब हामी प्रारम्भिक प्रयोगकर्ता प्रम्प्टलाई व्यवस्थापन गरी LLM कल गर्न सक्छौं। तपाइँको `main` फङ्क्सनलाई तलको कोडबाट अपडेट गर्नुहोस्:

```rust
// उपकरण कलहरू सहितको LLM संवाद
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

यसले प्रारम्भिक प्रयोगकर्ता प्रम्प्ट सहित दुई संख्याहरूको योग LLM सँग सोध्छ र यसले प्रतिक्रियालाई प्रक्रिया गरी उपकरण कलहरूलाई गतिशील रूपमा व्यवस्थापन गर्छ।

शानदार, तपाइँले यो गर्नुभयो!

## असाइनमेन्ट

अभ्यासबाट कोड लिएर थप केही उपकरणहरू सहित सर्भर बनाउनुहोस्। त्यसपछि LLM सहित क्लाइन्ट बनाउनुहोस्, अभ्यास जस्तै, र विभिन्न प्रम्प्टहरूसँग परीक्षण गर्नुहोस् ताकि तपाइँका सर्भरका सबै उपकरणहरू गतिशील रूपमा कल हुन्छन् भनी निश्चित गर्नुहोस्। यसरी क्लाइन्ट निर्माण गर्दा अन्तिम प्रयोगकर्ताले राम्रो अनुभव पाउनेछन् किनभने उनीहरूलाई विशिष्ट क्लाइन्ट कमाण्डहरूको सट्टा प्रम्प्ट प्रयोग गर्न सक्नेछ र कुनै MCP सर्भर कल भइरहेको बुझ्ने नपाउनेछन्।

## समाधान

[समाधान](./solution/README.md)

## मुख्य सिकाइहरू

- तपाइँको क्लाइन्टमा LLM थप्दा MCP सर्भरसँग प्रयोगकर्ताले राम्रो तरिकाले अन्तरक्रिया गर्न सक्छन्।
- MCP सर्भरको प्रतिक्रिया LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्न आवश्यक हुन्छ।

## नमूनाहरू

- [जाभा क्यालकुलेटर](../samples/java/calculator/README.md)
- [.Net क्यालकुलेटर](../../../../03-GettingStarted/samples/csharp)
- [जाभास्क्रिप्ट क्यालकुलेटर](../samples/javascript/README.md)
- [टाइपस्क्रिप्ट क्यालकुलेटर](../samples/typescript/README.md)
- [पाइथन क्यालकुलेटर](../../../../03-GettingStarted/samples/python)
- [रस्ट क्यालकुलेटर](../../../../03-GettingStarted/samples/rust)

## थप स्रोतहरू

## के हुनेछ अर्को

- अर्को: [Visual Studio Code प्रयोग गरी सर्भर उपभोग गर्ने](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->