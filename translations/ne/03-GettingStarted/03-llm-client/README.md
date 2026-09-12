# LLM संग क्लाइन्ट सिर्जना गर्दै

> [!NOTE]
> Java क्लाइन्ट उदाहरणहरू पूर्व HTTP+SSE यातायातमार्फत जडान हुन्छन् र
> लक्षित MCP `2025-11-25` SDK API हरू। नयाँ रिमोट क्लाइन्टहरूको लागि `2026-07-28`-अनुकूल SDK र
> Streamable HTTP प्रयोग गर्नुहोस्।

अहिलेसम्म, तपाईंले कसरी एउटा सर्भर र क्लाइन्ट सिर्जना गर्ने देख्नुभयो। क्लाइन्टले सर्भरलाई स्पष्ट रूपमा कल गरेर यसको उपकरणहरू, स्रोतहरू, र प्रॉम्प्टहरू सूचीबद्ध गर्न सक्षम थियो। तथापि, यो धेरै व्यावहारिक दृष्टिकोण होइन। तपाईंका प्रयोगकर्ताहरू एजेन्टिक युगमा बाँचिरहेका छन् र प्रॉम्प्टहरू प्रयोग गर्न र LLM सँग संवाद गर्न अपेक्षा गर्दछन्। उनीहरूलाई तपाईंले आफ्नो क्षमताहरू स्टोर गर्न MCP प्रयोग गर्नु भएको छ कि छैन भन्ने चिन्ता छैन; उनीहरू केवल प्राकृतिक भाषाको प्रयोग गरेर अन्तरक्रिया गर्ने अपेक्षा गर्दछन्। त्यसो भए हामी यसलाई कसरी समाधान गर्ने? समाधान हो क्लाइन्टमा LLM थप्नु।

## अवलोकन

यस पाठमा हामी आफ्नो क्लाइन्टमा LLM थप्ने र यसले तपाईंका प्रयोगकर्ताका लागि कसरी धेरै राम्रो अनुभव प्रदान गर्छ भन्नेमा ध्यान केन्द्रित गर्नेछौं।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यमा, तपाईं सक्षम हुनुहुनेछ:

- LLM सहित क्लाइन्ट सिर्जना गर्न।
- LLM प्रयोग गरेर सहज रूपमा MCP सर्भरसँग अन्तरक्रिया गर्न।
- क्लाइन्ट साइडमा राम्रो अन्तिम प्रयोगकर्ता अनुभव प्रदान गर्न।

## दृष्टिकोण

हामीले लिनुपर्ने दृष्टिकोण बुझ्ने प्रयास गरौँ। LLM थप्न सरल सुनिन्छ, तर के हामी साँच्चै यसो गर्नेछौं?

यहाँ क्लाइन्टले सर्भरसँग कसरी अन्तरक्रिया गर्नेछ:

1. सर्भरसँग जडान स्थापना गर्नुहोस्।

1. क्षमताहरू, प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरूको सूची बनाउनुहोस् र तिनीहरूको स्किमालाई बचत गर्नुहोस्।

1. एक LLM जोड्नुहोस् र तिनीहरूलाई LLM समझ्ने ढाँचामा बचत गरिएको क्षमताहरू र स्किमाहरू पास गर्नुहोस्।

1. प्रयोगकर्ता प्रॉम्प्टलाई LLM सँग क्लाइन्टले सूचीबद्ध गरेको उपकरणहरूसँग पास गरी व्यवस्थापन गर्नुहोस्।

राम्रो, अब हामी उच्च तहमा यो कसरी गर्ने थाहा पाए, तलको अभ्यासमा प्रयास गरौं।

## अभ्यास: LLM सहित क्लाइन्ट सिर्जना गर्दै

यस अभ्यासमा, हामी आफ्नो क्लाइन्टमा LLM थप्न सिक्नेछौं।

### GitHub व्यक्तिगत पहुँच टोकन प्रयोग गरेर प्रमाणीकरण

GitHub टोकन सिर्जना गर्न सजिलो प्रक्रिया हो। यसो गर्न सक्नुहुन्छ:

- GitHub सेटिङ्समा जानुहोस् – माथि दायाँ कुनामा आफ्नो प्रोफाइल चित्रमा क्लिक गरी सेटिङ्स चयन गर्नुहोस्।
- डेभलपर सेटिङ्समा जानुहोस् – तल स्क्रोल गरी डेभलपर सेटिङ्समा क्लिक गर्नुहोस्।
- व्यक्तिगत पहुँच टोकनहरू चयन गर्नुहोस् – फाइन-ग्रेन्ड टोकनहरूमा क्लिक गरी नयाँ टोकन उत्पन्न गर्नुहोस्।
- आफ्नो टोकन कन्फिगर गर्नुहोस् – सन्दर्भको लागि नोट थप्नुहोस्, समाप्ति मिति सेट गर्नुहोस्, र आवश्यक स्कोपहरू (अनुमतिहरू) चयन गर्नुहोस्। यस अवस्थामा मोडेल अनुमतिहरू थप्न निश्चित हुनुहोस्।
- टोकन उत्पन्न गर्नुहोस् र प्रतिलिपि गर्नुहोस् – टोकन उत्पन्नमा क्लिक गर्नुहोस्, र तुरुन्तै प्रतिलिपि गर्नुहोस्, किनकि यो फेरि देख्न सकिँदैन।

### -1- सर्भरसँग जडान गर्नुहोस्

पहिले हाम्रो क्लाइन्ट सिर्जना गरौँ:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्कीमा मान्यताका लागि zod आयात गर्नुहोस्

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

- आवश्यक पुस्तकालयहरू इम्पोर्ट गर्‍यौं
- दुई सदस्यहरूको क्लास बनायो, `client` र `openai` जसले हामीलाई क्लाइन्ट व्यवस्थापन गर्न र LLM सँग अन्तरक्रिया गर्न मद्दत गर्छ।
- हाम्रो LLM उदाहरणलाई GitHub मोडेलहरू प्रयोग गर्न कन्फिगर गर्‍यौं, `baseUrl` लाई इनफरेन्स API मा सेट गरी।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानको लागि सर्भर प्यारामिटरहरू सिर्जना गर्नुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयन योग्य
    args=["run", "server.py"],  # वैकल्पिक आदेश पङ्क्ति तर्कहरू
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

माथिको कोडमा हामीले:

- MCP का लागि आवश्यक पुस्तकालयहरू इम्पोर्ट गर्‍यौं
- क्लाइन्ट सिर्जना गर्‍यौं

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

पहिले, तपाईंले आफ्नो `pom.xml` फाइलमा LangChain4j निर्भरता थप्नुपर्नेछ। MCP एकीकरण र OpenAI-अनुकूल MiniMax API सक्षम गर्न यी निर्भरताहरू थप्नुहोस्:

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
`MINIMAX_MODEL_ID` ले `MiniMax-M3` र `MiniMax-M2.7` समर्थन गर्दछ। यदि
`OPENAI_BASE_URL` सेट गरिएको छैन भने, `MINIMAX_REGION` ले `global_en` र `cn_zh` समर्थन गर्दछ।

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

क्षेत्र अनुसार अन्तबिन्दु चयन गर्न, `OPENAI_BASE_URL` छोड्नुहोस्:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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

        // सर्भरसँग जडान गर्न MCP यातायात सिर्जना गर्नुहोस्
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

- **LangChain4j निर्भरता थप्यौं**: MCP एकीकरण र OpenAI-अनुकूल MiniMax API को लागि आवश्यक
- **LangChain4j पुस्तकालयहरू इम्पोर्ट गर्‍यौं**: MCP एकीकरण र OpenAI च्याट मोडेल कार्यक्षमताको लागि
- **`ChatLanguageModel` सिर्जना गर्‍यौं**: MiniMax र तपाईंको MiniMax API कुञ्जी, अन्तबिन्दु, र समर्थित मोडेल ID सहित कन्फिगर गरिएको
- **HTTP ट्रान्सपोर्ट सेट अप गर्‍यौं**: MCP सर्भरसँग जडान गर्न Server-Sent Events (SSE) प्रयोग गर्दै
- **एक MCP क्लाइन्ट सिर्जना गर्‍यौं**: जसले सर्भरसँग संचार व्यवस्थापन गर्नेछ
- **LangChain4j को निर्मित MCP समर्थन प्रयोग गर्‍यौं**: जुन LLM र MCP सर्भरहरू बीच एकीकरणलाई सरल बनाउँछ

#### Rust

यो उदाहरणले मान्दछ कि तपाईंसँग Rust आधारित MCP सर्भर चलिरहेको छ। यदि छैन भने, [01-first-server](../01-first-server/README.md) पाठमा फर्केर सर्भर सिर्जना गर्नुहोस्।

आफ्नो Rust MCP सर्भर भएपछि, टर्मिनल खोल्नुहोस् र सर्भरसँग उही डिरेक्टरीमा जानुहोस्। त्यसपछि नयाँ LLM क्लाइन्ट प्रोजेक्ट सिर्जना गर्न तलको आदेश चलाउनुहोस्:

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
> OpenAI को लागि आधिकारिक Rust पुस्तकालय छैन, तथापि, `async-openai` क्रेट एक [समुदाय द्वारा मर्मत गरिएको पुस्तकालय](https://platform.openai.com/docs/libraries/rust#rust) हो जुन सामान्यतया प्रयोग गरिन्छ।

`src/main.rs` फाइल खोल्नुहोस् र यसको सामग्री निम्न कोडसहित प्रतिस्थापित गर्नुहोस्:

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

    // OpenAI क्लाइन्ट सेटअप
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP क्लाइन्ट सेटअप
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

यस कोडले एक आधारभूत Rust एप्लिकेशन सेटअप गर्दछ जुन MCP सर्भर र GitHub मोडेलहरूसँग LLM अन्तरक्रियाको लागि जडान हुनेछ।

> [!IMPORTANT]
> एप्लिकेसन चलाउनु अघि आफ्नो GitHub टोकन सहित `OPENAI_API_KEY` वातावरण चर सेट गर्न निश्चित गर्नुहोस्।

राम्रो, अर्को कदमका लागि, सर्भरमा क्षमताहरू सूचीबद्ध गरौं।

### -2- सर्भर क्षमताहरू सूचीबद्ध गर्नुहोस्

अब हामी सर्भरसँग जडान भएर यसको क्षमताहरू सोध्नेछौं:

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

माथिको कोडमा हामीले:

- सर्भरसँग जडान गर्नको लागि कोड थपेका छौँ, `connectToServer`।
- हाम्रो एप फ्लोको जिम्मेवारी लिएको `run` मेथड सिर्जना गर्‍यौं। अहिलेसम्म यसले उपकरणहरू मात्र सूचीबद्ध गर्दछ तर छिट्टै थप्नेछौं।

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

हामीले थपेका कुराहरू:

- स्रोतहरू र उपकरणहरू सूचीबद्ध गर्‍यौं र तिनीहरूलाई मुद्रण गर्‍यौं। उपकरणहरूको लागि हामीले `inputSchema` पनि सूचीबद्ध गर्‍यौं जुन हामी पछि प्रयोग गर्छौं।

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

- MCP सर्भरमा उपलब्ध उपकरणहरूको सूची बनायो
- हरेक उपकरणका लागि नाम, विवरण र यसको स्कीमा सूचीबद्ध गर्यौं। पछिल्लो चीज हामीले चाँडै उपकरणहरू कल गर्न प्रयोग गर्नेछौं।

#### Java

```java
// एउटा उपकरण प्रदायक बनाउनुहोस् जसले स्वचालित रूपमा MCP उपकरणहरू पत्ता लगाउँछ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP उपकरण प्रदायकले स्वचालित रूपमा ह्यान्डल गर्दछ:
// - MCP सर्भरबाट उपलब्ध उपकरणहरूको सूची बनाउने
// - MCP उपकरण स्कीमाहरूलाई LangChain4j ढाँचामा रुपान्तरण गर्ने
// - उपकरण कार्यान्वयन र प्रतिक्रिया व्यवस्थापन गर्ने
```

अघिल्लो कोडमा हामीले:

- एउटा `McpToolProvider` बनायौं जसले स्वतः MCP सर्भरबाट सबै उपकरणहरू पत्ता लगाएर दर्ता गर्छ
- उपकरण प्रदायकले MCP उपकरण स्कीमाहरू र LangChain4j को उपकरण ढाँचाबीच रूपान्तरण भित्रै गर्दछ
- यो दृष्टिकोणले म्यानुअल उपकरण सूचीकरण र रूपान्तरण प्रक्रियालाई लुकाउँछ

#### Rust

MCP सर्भरबाट उपकरणहरू प्राप्त गर्न `list_tools` विधि प्रयोग गरिन्छ। तपाईंको `main` function मा, MCP क्लाइन्ट सेटअप गरेपछि, तलको कोड थप्नुहोस्:

```rust
// MCP उपकरण सूची प्राप्त गर्नुहोस्
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्भर क्षमताहरूलाई LLM उपकरणहरूमा रूपान्तरण गर्नुहोस्

सर्भर क्षमताहरू सूचीबद्ध गरेपछि, अर्को चरण हो तीलाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्नु। यसपछि हामी यी क्षमताहरूलाई हाम्रो LLM लाई उपकरणको रूपमा प्रदान गर्न सक्छौं।

#### TypeScript

1. MCP सर्भरबाट प्राप्त प्रतिक्रियालाई LLM ले प्रयोग गर्न सक्ने उपकरण ढाँचामा रूपान्तरण गर्न तलको कोड थप्नुहोस्:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // इनपुट_स्किमा आधारित जॉड स्किमा बनाउनुहोस्
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

    माथि कोडले MCP सर्भरबाट प्रतिक्रियालाई लिएर LLM ले बुझ्ने उपकरण परिभाषा ढाँचामा रूपान्तरण गर्छ।

2. अब `run` विधि अपडेट गरौं जसले सर्भर क्षमताहरू सूचीबद्ध गर्छ:

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

    अघिल्लो कोडमा, हामीले `run` विधिलाई परिणाममा म्याप गर्न अपडेट गर्यौं र प्रत्येक प्रविष्टिका लागि `openAiToolAdapter` कल गर्ने।

#### Python

1. पहिले, तलको रूपान्तरण गर्ने फङ्क्शन बनाऔं

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

    माथि फङ्क्शन `convert_to_llm_tools` मा हामीले MCP उपकरण प्रतिक्रिया लिएर LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्छौं।

2. अर्को, हाम्रो क्लाइन्ट कोड अपडेट गरौं जसले यो फङ्क्शन प्रयोग गर्छ:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ, हामी `convert_to_llm_tool` कल थप्दैछौं जसले MCP उपकरण प्रतिक्रिया LLM लाई दिने योग्य केहीमा रूपान्तरण गर्छ।

#### .NET

1. MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने तरिकामा रूपान्तरण गर्न कोड थपौं

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

- `ConvertFrom` नामक फङ्क्शन सिर्जना गर्यौं जसले नाम, विवरण र इनपुट स्कीमा लिन्छ।
- यस्तो कार्यक्षमता परिभाषित गर्यौं जसले FunctionDefinition सिर्जना गर्छ जुन ChatCompletionsDefinition मा पठाइन्छ। यो LLM ले बुझ्ने कुरा हो।

2. अब हेर्नुस् कसरी हामी माथि फङ्क्शन प्रयोग गरेर केही विद्यमान कोड अपडेट गर्न सक्छौं:

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
// प्राकृतिक भाषा अन्तर्क्रियाको लागि बोट इन्टरफेस सिर्जना गर्नुहोस्
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

- प्राकृतिक भाषा अन्तरक्रियाका लागि सादा `Bot` इन्टरफेस परिभाषित गर्यौं
- LangChain4j को `AiServices` प्रयोग गरेर LLM लाई MCP उपकरण प्रदायकसँग स्वतः बाँध्यौं
- फ्रेमवर्कले स्वतः उपकरण स्कीमा रूपान्तरण र फङ्क्शन कललाई पृष्ठभूमिमा ह्यान्डल गर्छ
- यसले म्यानुअल उपकरण रूपान्तरणलाई हटाउँदै - LangChain4j ले MCP उपकरणलाई LLM-अनुकूल ढाँचामा रूपान्तरणको जटिलता सबै ह्यान्डल गर्छ

#### Rust

MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्न हामी एउटा सहयोगी फङ्क्शन थप्नेछौं जुन उपकरण सूचीकरणलाई फर्म्याट गर्छ। तपाईंको `main.rs` फाइलमा `main` function पछि तलको कोड थप्नुहोस्। LLM लाई अनुरोध गर्दा यो कल हुनेछ:

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

राम्रो छ, हामीले प्रयोगकर्ताका अनुरोधहरू ह्यान्डल गर्न तयार पारेका छैनौं, त्यसपछि हामी त्यसलाई सम्हाल्नेछौं।

### -4- प्रयोगकर्ताको प्रॉम्प्ट अनुरोध ह्यान्डल गर्नुहोस्

यस भागमा, हामी प्रयोगकर्ताका अनुरोधहरू ह्यान्डल गर्ने छौं।

#### TypeScript

1. एउटा विधि थप्नुहोस् जुन हाम्रो LLM कल गर्न प्रयोग हुनेछ:

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
        // गर्न बाँकी

        }
    }
    ```

    अघिल्लो कोडमा हामीले:

    - `callTools` नामक विधि थप्यौं।
    - विधिले LLM प्रतिक्रिया लिन्छ र जाँच्दछ कुन उपकरणहरू कल गरिएको छ, यदि कुनै छन् भने:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // टूल कल गर्नुहोस्
        }
        ```

    - LLM ले कल गर्नुपर्ने संकेत गर्दा उपकरण कल गर्दछ:

        ```typescript
        // २. सर्भरको उपकरण कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. परिणामसँग केही गर्नुहोस्
        // गर्नु बाँकी
        ```

2. `run` विधि अपडेट गरेर LLM कल र `callTools` कल समावेश गरौं:

    ```typescript

    // 1. LLM को लागि इनपुट सन्देशहरू बनाउँदै
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM मा कल गर्दै
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिकृयामा जानुहोस्, प्रत्येक विकल्पको लागि, जाँच गर्नुस् कि यसमा उपकरण कलहरू छन् कि छैनन्
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

राम्रो छ, पूरा कोड सूची यो हो:

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
            baseURL: "https://models.inference.ai.azure.com", // भविष्यमा यो URL मा परिवर्तन गर्नुपर्ने हुन सक्छ: https://models.github.ai/inference
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
          // इनपुट_स्कीमा आधारित zod स्कीमा बनाउनुहोस्
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // स्पष्ट रूपमा प्रकार "function" मा सेट गर्नुहोस्
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
    
          // ३. परिणामसँग केही गर्नुहोस्
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
    
        // ३. LLM जवाफमार्फत जानुहोस्, प्रत्येक विकल्पका लागि जाँच गर्नुहोस् कि यसमा उपकरण कलहरू छन् कि छैनन्
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

2. अब त्यो function थपौं जसले LLM कल गर्नेछ:

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

    - हाम्रा फङ्क्शनहरू, जुन हामीले MCP सर्भरमा पायौं र रूपान्तरण गर्यौं, LLM लाई दिएका छौं।
    - तब हामीले उक्त फङ्क्शनहरूसँग LLM कल गर्यौं।
    - त्यसपछि, हामी परिणाम जाँच्दैछौं कुन फङ्क्शनहरू कल गर्नुपर्छ भनेर।
    - अन्तमा, हामी फङ्क्शनहरूको एरे पास गर्छौं कल गर्न।

3. अन्तिम चरण, हाम्रो मुख्य कोड अपडेट गरौं:

    ```python
    prompt = "Add 2 to 20"

    # सबैलाई कुन उपकरणहरू प्रयोग गर्ने भन्न LLM लाई सोध्नुहोस्, यदि कुनै छ भने
    functions_to_call = call_llm(prompt, functions)

    # प्रस्तावित कार्यहरू कल गर्नुहोस्
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    त्यहाँ, त्यो अन्तिम चरण थियो, माथि कोडमा हामीले:

    - `call_tool` मार्फत MCP उपकरण कल गर्यौं जुन LLM ले हाम्रो प्रॉम्प्ट अनुसार कल गर्नुपर्ने ठानेको थियो।
    - MCP सर्भरमा उपकरण कलको परिणाम मुद्रण गर्यौं।

#### .NET

1. LLM प्रॉम्प्ट अनुरोध गर्ने केही कोड देखाऔं:

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

    अघिल्लो कोडमा हामीले:

    - MCP सर्भरबाट उपकरणहरू प्राप्त गर्यौं, `var tools = await GetMcpTools()`।
    - प्रयोगकर्ताको प्रॉम्प्ट `userMessage` परिभाषित गर्यौं।
    - मोडेल र उपकरणहरू निर्दिष्ट गर्ने विकल्प वस्तु बनायौं।
    - LLM तर्फ अनुरोध गर्यौं।

2. अन्तिम चरण, हेर्नुस् LLM ले फङ्क्शन कल गर्ने सोच्दछ कि होइन:

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

    - फङ्क्शन कलहरूको सूचीमा लूप गर्यौं।
    - हरेक उपकरण कलको लागि नाम र तर्कहरू पार्स गरी MCP सर्भरमा उपकरण कल गर्यौं र अन्तिममा परिणामहरू मुद्रण गर्यौं।

पूरा कोड यहाँ छ:

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
    // स्वचालित रूपमा MCP उपकरणहरू प्रयोग गर्ने स्वाभाविक भाषा अनुरोधहरू कार्यान्वयन गर्नुहोस्
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

- MCP सर्भर उपकरणहरू सँग अन्तरक्रिया गर्न सादगीपूर्ण प्राकृतिक भाषा प्रॉम्प्टहरू प्रयोग गर्यौं
- LangChain4j फ्रेमवर्कले स्वतः ह्यान्डल गर्दछ:
  - आवश्यक पर्दा प्रयोगकर्ताको प्रॉम्प्टलाई उपकरण कलमा रूपान्तरण गर्नु
  - LLM को निर्णय अनुसार उचित MCP उपकरणहरू कल गर्नु
  - LLM र MCP सर्भर बीच संवाद प्रवाह व्यवस्थापन गर्नु
- `bot.chat()` विधिले प्राकृतिक भाषा प्रतिक्रियाहरू फर्काउँछ जसमा MCP उपकरण कार्यान्वयनबाट परिणामहरू पनि समावेश हुन सक्छ
- यस दृष्टिकोणले प्रयोगकर्तालाई सहज अनुभव दिन्छ जहाँ उनीहरूले अन्तर्निहित MCP कार्यान्वयन बारे जान्न आवश्यक पर्दैन

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


यहाँ ठूलो भाग काम हुन्छ। हामी LLM लाई सुरुको प्रयोगकर्ता प्रॉम्प्टसँग कल गर्नेछौं, त्यसपछि प्रतिक्रियालाई प्रक्रिया गर्नेछौं कि कुनै उपकरणहरू कल गर्न आवश्यक छ कि छैन। यदि छ भने, ती उपकरणहरू कल गर्नेछौं र LLM सँग संवाद जारी राख्नेछौं जबसम्म थप उपकरण कल गर्न आवश्यक नपर्ला र हामीसँग अन्तिम प्रतिक्रिया नआउँदासम्म।

हामीले धेरै पटक LLM लाई कल गर्ने छौं, त्यसैले एउटा कार्यलाई परिभाषित गरौं जसले LLM कललाई सम्हाल्नेछ। आफ्नो `main.rs` फाइलमा तलको कार्य थप्नुहोस्:

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

यो कार्यले LLM क्लाइन्ट, सन्देशहरूको सूची (प्रयोगकर्ता प्रॉम्प्ट सहित), MCP सर्भरबाट उपकरणहरू लिन्छ, र LLM लाई अनुरोध पठाउँछ, अनि प्रतिक्रिया फर्काउँछ।

LLM बाट प्रतिक्रिया एक `choices` को एर्रे हुनेछ। हामीले परिणाम प्रक्रियामा हेर्नुपर्नेछ कि कुनै `tool_calls` छन् कि छैनन्। यसले हामीलाई थाहा दिन्छ कि LLM ले विशेष उपकरण कल गर्न अनुरोध गरिरहेको छ तदनुसार तर्कसहित। आफ्नो `main.rs` फाइलको तलमा निम्न कोड थप्नुहोस् जसले LLM प्रतिक्रिया सम्हाल्नको लागि कार्य परिभाषित गर्छ:

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

    // उपकरण कलहरू व्यवस्थित गर्नुहोस्
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

यदि `tool_calls` छन् भने, यसले उपकरण जानकारी निकाल्छ, MCP सर्भरलाई उपकरण अनुरोध सहित कल गर्छ, र नतिजा संवाद सन्देशहरूमा थप्छ। त्यसपछि संवाद LLM सँग जारी राखिन्छ र सन्देशहरू सहायकको प्रतिक्रिया र उपकरण कलको नतिजा अनुसार अपडेट हुन्छ।

LLM ले MCP कलहरूको लागि फिर्ता गर्ने उपकरण कल जानकारी निकाल्न, अर्को सहायक कार्य थप्नेछौं जुन कल गर्न आवश्यक सबै कुरा निकाल्छ। आफ्नो `main.rs` फाइलको तल निम्न कोड थप्नुहोस्:

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

सबै टुक्रा राखिसकेपछि, हामीले सुरुको प्रयोगकर्ता प्रॉम्प्ट सम्हाल्न र LLM लाई कल गर्न सक्दछौं। आफ्नो `main` कार्यलाई निम्न कोडमा अपडेट गर्नुहोस्:

```rust
// उपकरण कलहरू सहित LLM वार्तालाप
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

यसले सुरुको प्रयोगकर्ता प्रॉम्प्टसँग LLM लाई सोध्नेछ दुई संख्याको योगको लागि, र प्रतिक्रिया प्रक्रियामा उपकरण कललाई गतिशील रूपमा सम्हाल्नेछ।

राम्रो भयो, तपाईंले गर्नुभयो!

## कार्य

अभ्यासबाट कोड लिएर थप उपकरणहरूसहित सर्भर बनाउनुहोस्। त्यसपछि LLM सहित एक क्लाइन्ट सिर्जना गर्नुहोस्, अभ्यास जस्तै, र विभिन्न प्रॉम्प्टहरूमा परीक्षण गर्नुहोस् जसले तपाईंको सर्भरका सबै उपकरणहरू गतिशील रूपमा कल हुन्छन् भनेर सुनिश्चित गर्छ। यसरी क्लाइन्ट बनाउँदा अन्तिम प्रयोगकर्ताले उत्तम प्रयोगकर्ता अनुभव पाउँछन् किनकि उनीहरूले वास्तविक क्लाइन्ट आदेशको सट्टा प्रॉम्प्टहरू प्रयोग गर्न सक्दछन् र MCP सर्भर कल भएको थाहा पाउँदैनन्।

## समाधान

[Solution](./solution/README.md)

## मुख्य सिकाइहरू

- आफ्नो क्लाइन्टमा LLM थप्दा MCP सर्भरसँग प्रयोगकर्ताहरूको अन्तरक्रिया राम्रो हुन्छ।
- तपाईंले MCP सर्भरको प्रतिक्रिया यस्तो कुरामा रूपान्तरण गर्न आवश्यक पर्छ जुन LLM बुझ्न सक्छ।

## नमुना

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## थप स्रोतहरू

## के हुनेछ पछि

- Next: [Consuming a server using Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->