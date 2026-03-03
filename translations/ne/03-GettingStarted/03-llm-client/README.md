# LLM सँग क्लाइन्ट सिर्जना गर्दै

अहिले सम्म, तपाईंले कसरी सर्भर र क्लाइन्ट सिर्जना गर्ने देख्नुभएको छ। क्लाइन्टले सर्भरलाई स्पष्ट रूपमा कल गरेर यसको उपकरणहरू, स्रोतहरू, र प्रॉम्प्टहरूको सूची लिन सक्षम भएको छ। तर, यो धेरै व्यावहारिक तरिका होइन। तपाईंका प्रयोगकर्ताहरू एजेन्टिक युगमा बस्छन् र प्रॉम्प्टहरू प्रयोग गर्न र LLM सँग संवाद गर्न चाहन्छन्। उनीहरूलाई तपाईंले MCP प्रयोग गरेर आफ्नो क्षमता भण्डारण गर्नु भएको छ कि छैन भनी चिन्ता छैन; उनीहरू त सरलै स्वाभाविक भाषाको प्रयोग गरेर अन्तरक्रिया गर्न चाहन्छन्। अब हामीले यो कसरी समाधान गर्ने? समाधान क्लाइन्टमा LLM थप गर्नु हो।

## अवलोकन

यस पाठमा हामी क्लाइन्टमा LLM थप गर्नमा ध्यान केन्द्रित गर्नेछौं र प्रयोगकर्ताका लागि यो कस्तो राम्रो अनुभव प्रदान गर्छ भनेर देखाउनेछौं।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- LLM सहित क्लाइन्ट सिर्जना गर्न।
- LLM प्रयोग गरी MCP सर्भरसँग सहज रूपमा अन्तरक्रिया गर्न।
- क्लाइन्ट पक्षमा राम्रो अन्त प्रयोगकर्ता अनुभव प्रदान गर्न।

## दृष्टिकोण

हामीलाई लिनुपर्ने दृष्टिकोण बुझ्ने प्रयास गरौं। LLM थप गर्नु सजिलो जस्तो लाग्छ, तर के हामी साँच्चिकै यो गर्नेछौं?

क्लाइन्टले सर्भरसँग कसरी अन्तरक्रिया गर्ने:

1. सर्भरसँग जडान स्थापित गर्नुहोस्।

1. क्षमताहरू, प्रॉम्प्टहरू, स्रोतहरू र उपकरणहरूको सूची बनाउनुहोस्, र तिनीहरूको स्किमासँग बचत गर्नुहोस्।

1. LLM थप्नुहोस् र बचत गरिएको क्षमताहरू र स्किमालाई LLM ले बुझ्ने ढाँचामा पठाउनुहोस्।

1. प्रयोगकर्ता प्रॉम्प्टलाई LLM मा पठाएर र क्लाइन्टले सूचीबद्ध उपकरणहरूसँग मिलाएर ह्यान्डल गर्नुहोस्।

उत्कृष्ट, अब हामीले उच्च स्तरमा कसरी गर्ने थाहा पाएँ, तलको अभ्यासमा प्रयास गरौं।

## अभ्यास: LLM सहित क्लाइन्ट सिर्जना गर्दै

यस अभ्यासमा, हामी हाम्रो क्लाइन्टमा LLM थप्न सिक्नेछौं।

### GitHub व्यक्तिगत पहुँच टोकन प्रयोग गरेर प्रमाणिकरण

GitHub टोकन सिर्जना गर्नु सरल प्रक्रिया हो। यसरी गर्न सकिन्छ:

- GitHub सेटिङहरूमा जानुहोस् – माथिल्लो दायाँ कुनामा तपाईंको प्रोफाइल तस्वीर क्लिक गरी सेटिङहरू चयन गर्नुहोस्।
- Developer Settings मा जानुहोस् – तल स्क्रोल गरी Developer Settings क्लिक गर्नुहोस्।
- Personal Access Tokens चयन गर्नुहोस् – Fine-grained tokens मा क्लिक गरी नयाँ टोकन उत्पन्न गर्नुहोस्।
- टोकन कन्फिगर गर्नुहोस् – सन्दर्भका लागि नोट थप्नुहोस्, समाप्ति मिति सेट गर्नुहोस्, र आवश्यक स्कोपहरू (अनुमतिहरू) चयन गर्नुहोस्। यस केसमा Models अनुमति थप्न सुनिश्चित गर्नुहोस्।
- टोकन उत्पादन गरी यसलाई तुरुन्तै कपी गर्नुहोस्, किनकि तपाईंले फेरि यो देख्न पाउने छैन।

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

माथिका कोडमा हामीले:

- आवश्यक लाइब्रेरीहरू आयात गरेका छौं
- दुई सदस्यहरू `client` र `openai` सहित वर्ग सिर्जना गरेका छौं जसले हामीलाई क्लाइन्ट व्यवस्थापन र LLM सँग अन्तरक्रिया गर्न मद्दत गर्छ।
- GitHub Models प्रयोग गर्न `baseUrl` सेट गरेर हाम्रो LLM इन्स्टेन्स कन्फिगर गरेका छौं।

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio जडानको लागि सर्भर प्यारामिटरहरू सिर्जना गर्नुहोस्
server_params = StdioServerParameters(
    command="mcp",  # कार्यान्वयनयोग्य
    args=["run", "server.py"],  # वैकल्पिक कमाण्ड लाइन आर्गुमेन्टहरू
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

माथिका कोडमा हामीले:

- MCP का लागि आवश्यक लाइब्रेरीहरू आयात गरेका छौं
- क्लाइन्ट तयार पारेका छौं

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

पहिले, तपाईंले आफ्नो `pom.xml` फाइलमा LangChain4j निर्भरता थप्नु पर्नेछ। यी निर्भरताहरू MCP एकीकरण र GitHub Models समर्थन सक्षम गर्न थप्नुहोस्:

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

त्यसपछि आफ्नो Java क्लाइन्ट वर्ग सिर्जना गर्नुहोस्:

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
    
    public static void main(String[] args) throws Exception {        // LLM लाई GitHub मोडेलहरू प्रयोग गर्ने गरी कन्फिगर गर्नुहोस्
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

माथिका कोडमा हामीले:

- **LangChain4j निर्भरता थपेका छौं**: MCP एकीकरण, OpenAI आधिकारिक क्लाइन्ट, र GitHub Models समर्थनको लागि आवश्यक
- **LangChain4j लाइब्रेरीहरू आयात गरेका छौं**: MCP एकीकरण र OpenAI च्याट मोडल कार्यक्षमताका लागि
- **`ChatLanguageModel` सिर्जना गरेका छौं**: तपाईँको GitHub टोकनसहित GitHub Models कन्फिगर गरिएको
- **HTTP ट्रान्सपोर्ट सेटअप गरेका छौं**: Server-Sent Events (SSE) प्रयोग गरी MCP सर्भरसँग जडान गर्न
- **MCP क्लाइन्ट तयार पारेका छौं**: जसले सर्भरसँग सञ्चार सञ्चालन गर्नेछ
- **LangChain4j को बिल्ट-इन MCP समर्थन प्रयोग गरेका छौं**: जसले LLM र MCP सर्भरबीचको एकीकरण सरल बनाउँछ

#### Rust

यो उदाहरणले तपाईंको Rust आधारित MCP सर्भर चलिरहेको छ भनी मान्छ। त्यस्तो छैन भने, [01-first-server](../01-first-server/README.md) पाठमा फर्केर सर्भर सिर्जना गर्नुहोस्।

Rust MCP सर्भर भएपछि, टर्मिनल खोल्नुहोस् र सर्भर भएको सोही डाइरेक्टरीमा जानुहोस्। त्यहाँ नयाँ LLM क्लाइन्ट प्रोजेक्ट सिर्जना गर्न तलको आदेश चलाउनुहोस्:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` फाइलमा तलका निर्भरता थप्नुहोस्:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI को लागि आधिकारिक Rust लाइब्रेरी छैन, तर `async-openai` क्रेट एउटा [समुदायले व्यवस्थापन गरेको लाइब्रेरी](https://platform.openai.com/docs/libraries/rust#rust) हो जुन प्रायः प्रयोग गरिन्छ।

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

यो कोडले एक बेसिक Rust एप्लिकेसन सेटअप गर्छ जुन MCP सर्भर र GitHub Models सँग LLM अन्तरक्रियाका लागि जडान गर्छ।

> [!IMPORTANT]
> एप्लिकेसन चलाउनु अघि आफ्नो GitHub टोकनसँग `OPENAI_API_KEY` environment variable सेट गर्न नबिर्सनुहोस्।

उत्कृष्ट, अब अर्को चरणमा, सर्भरमा क्षमताहरूको सूची बनाऔं।

### -2- सर्भर क्षमताहरू सूचीबद्ध गर्नुहोस्

अब हामी सर्भरसँग जडान गर्नेछौं र यसको क्षमताहरू सोध्नेछौं:

#### Typescript

त्यसै वर्गमा, तलका मेथडहरू थप्नुहोस्:

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

- सर्भरसँग जडान गर्न `connectToServer` कोड थपेका छौं।
- `run` मेथड सिर्जना गरेका छौं जुन एप प्रवाह ह्यान्डल गर्छ। अहिलेसम्म मात्र उपकरण सूचीबद्ध गर्छ तर चाँडै बढी थप्नेछौं।

#### Python

```python
# उपलब्ध स्रोतहरूको सूची बनाउनुहोस्
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# उपलब्ध उपकरणहरूको सूची बनाउनुहोस्
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

यहाँ हामीले थपेका छौं:

- स्रोतहरू र उपकरणहरू सूचीबद्ध गरी प्रिन्ट गरेका छौं। उपकरणको लागि हामीले `inputSchema` पनि दिएका छौं जुन पछि प्रयोग गर्नेछौं।

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

- MCP सर्भरमा उपलब्ध उपकरणहरूको सूची बनाएका छौं
- प्रत्येक उपकरणको नाम, विवरण र स्किमा सूचीबद्ध गरेका छौं। पछि उपकरणहरू कल गर्न यो उपयोगी हुन्छ।

#### Java

```java
// एउटा उपकरण प्रदायक सिर्जना गर्नुहोस् जुन स्वचालित रूपमा MCP उपकरणहरू पत्ता लगाउँछ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP उपकरण प्रदायकले स्वचालित रूपमा यसलाई व्यवस्थापन गर्दछ:
// - MCP सर्भरबाट उपलब्ध उपकरणहरूको सूची बनाउँदै
// - MCP उपकरण योजनाहरूलाई LangChain4j ढाँचामा रूपान्तरण गर्दै
// - उपकरण कार्यान्वयन र प्रतिक्रिया व्यवस्थापन गर्दै
```

माथिको कोडमा हामीले:

- `McpToolProvider` सिर्जना गरेका छौं जुन स्वचालित रूपमा सबै उपकरणहरू पत्ता लगाएर MPC सर्भरबाट दर्ता गर्छ
- उपकरण प्रदायकले MCP उपकरण स्किमाहरू र LangChain4j उपकरण ढाँचाबीच रूपान्तरण आन्तरिक रूपमा ह्यान्डल गर्छ
- यो दृष्टिकोणले म्यानुअल उपकरण सूचीबद्धता र रूपान्तरण प्रक्रियालाई लुकाउँछ

#### Rust

MCP सर्भरबाट उपकरणहरू प्राप्त गर्न `list_tools` मेथड प्रयोग हुन्छ। तपाईंको `main` फंक्शनमा, MCP क्लाइन्ट सेटअप पछाडि तलको कोड थप्नुहोस्:

```rust
// MCP उपकरण सूची प्राप्त गर्नुहोस्
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- सर्भर क्षमताहरूलाई LLM उपकरणहरूमा रूपान्तरण गर्नुहोस्

सर्भर क्षमताहरू सूचीबद्ध गरेपछि अर्को चरण ती क्षमताहरूलाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्नु हो। त्यसपछि हामी यी क्षमताहरू हाम्रो LLM लाई उपकरणका रूपमा प्रदान गर्न सक्छौं।

#### TypeScript

1. MCP सर्भरको प्रतिक्रियालाई LLM उपयोग गर्न सक्ने उपकरण ढाँचामा रूपान्तरण गर्न तलको कोड थप्नुहोस्:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema मा आधारित zod स्किमा सिर्जना गर्नुहोस्
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

    माथिको कोडले MCP सर्भरको प्रतिक्रिया लिएर त्यसलाई LLM ले बुझ्ने उपकरण परिभाषा ढाँचामा रूपान्तरण गर्छ।

1. `run` मेथडलाई सर्भर क्षमताहरू सूचीबद्ध गर्न अपडेट गरौं:

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

    माथिको कोडमा, हामीले `run` मेथडलाई परिणाम मार्फत म्याप गरी प्रत्येक entry मा `openAiToolAdapter` कल गर्दैछौं।

#### Python

1. पहिले, तलको रूपान्तरण फंक्शन बनाऔं

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

    `convert_to_llm_tools` फंक्शनले MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने ढाँचामा रूपान्तरण गर्छ।

1. अर्को, हाम्रो क्लाइन्ट कोडलाई यस फंक्शन प्रयोग गर्न अपडेट गरौं:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    यहाँ, हामीले `convert_to_llm_tool` लाई कल गरेर MCP उपकरण प्रतिक्रिया LLM मा पठाउन सकिने स्वरूपमा रूपान्तरण गरिरहेका छौं।

#### .NET

1. MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने स्वरूपमा रूपान्तरण गर्ने कोड थपियो:

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

- `ConvertFrom` नामक फंक्शन बनाएका छौं जुन नाम, विवरण र इनपुट स्किमा लिन्छ।
- फंक्शनले FunctionDefinition सिर्जना गर्छ जुन ChatCompletionsDefinition मा पठाइन्छ। यो LLM ले बुझ्छ।

1. अब अवस्थित कोड कसरी अपडेट गर्ने हेर्नुहोस्:

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
// प्राकृतिक भाषा अन्तरक्रियाका लागि बोट अन्तरफलक सिर्जना गर्नुहोस्
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

- प्राकृतिक भाषा अन्तर्क्रियाका लागि सरल `Bot` इन्टरफेस परिभाषित गरेका छौं
- LangChain4j को `AiServices` प्रयोग गरी LLM र MCP उपकरण प्रदायकलाई स्वचालित रूपमा बाँधेका छौं
- फ्रेमवर्कले उपकरण स्किमा रूपान्तरण र फंक्शन कल स्वचालित रूपमा ह्यान्डल गर्छ
- यसले म्यानुअल उपकरण रूपान्तरणलाई समाप्त पार्छ - LangChain4j सबै जटिलता सम्हाल्छ

#### Rust

MCP उपकरण प्रतिक्रियालाई LLM ले बुझ्ने स्वरूपमा रूपान्तरण गर्न हामीले एउटा हेल्पर फंक्शन थप्नेछौं जुन उपकरण सूचीलाई फारम्याट गर्छ। यो फंक्शन `main` फंक्शनको मुनि `main.rs` फाइलमा थप्नुहोस्। LLM लाई अनुरोध गर्दा यो कल हुनेछ:

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

उत्कृष्ट, अब प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्ने सेटअप गरौं।

### -4- प्रयोगकर्ता प्रॉम्प्ट अनुरोध ह्यान्डल गर्नुहोस्

यस भागमा, हामी प्रयोगकर्ता अनुरोधहरू ह्यान्डल गर्नेछौं।

#### TypeScript

1. LLM कल गर्न प्रयोग हुने मेथड थप्नुहोस्:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // २. सर्भरको उपकरणलाई कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. परिणामसँग केही गर्नुहोस्
        // गर्नु पर्ने कुरा

        }
    }
    ```

    माथिको कोडमा:

    - `callTools` नामक मेथड थपियो।
    - यो मेथडले LLM प्रतिक्रियालाई लिएर कुन उपकरणहरू कल भएको जाँच गर्छ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // उपकरण कल गर्नुहोस्
        }
        ```

    - LLM ले क्याल कल गर्न भन्यो भने उपकरण कल गर्दछ:

        ```typescript
        // २. सर्भरको उपकरण कल गर्नुहोस्
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ३. परिणामसँग केही गर्नुहोस्
        // गर्नु पर्ने काम
        ```

1. `run` मेथड अपडेट गरी LLM कल र `callTools` समावेश गरौं:

    ```typescript

    // 1. LLM को लागि इनपुट सन्देशहरू बनाउनुहोस्
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM कल गर्दै
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM प्रतिक्रिया जाँच गर्नुहोस्, प्रत्येक विकल्पका लागि, यदि यसमा उपकरण कलहरू छन् कि छैनन् जाँच गर्नुहोस्
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

उत्कृष्ट, पूर्ण कोड यस्तो छ:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // स्किमा प्रमाणीकरणको लागि zod आयात गर्नुहोस्

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // भविष्यमा यो URL परिवर्तन गर्न आवश्यक पर्न सक्छ: https://models.github.ai/inference
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
          // इनपुट_स्किमा अनुसार zod स्किमा बनाउनुहोस्
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // स्पष्ट रूपमा प्रकारलाई "function" मा सेट गर्नुहोस्
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
    
    
          // 2. सर्भरको उपकरणलाई कल गर्नुहोस्
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. परिणामसँग केही गर्नुहोस्
          // गर्ने काम
    
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
    
        // 1. LLM प्रतिक्रियामा जानुहोस्, हरेक विकल्पको लागि, हेर्नुहोस् कि के यसमा उपकरण कलहरू छन्
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

1. LLM कल गर्न आवश्यक केही आयात थपौं:

    ```python
    # ल्लम
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM कल गर्ने फंक्शन थपौं:

    ```python
    # llm

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

    - MCP सर्भरमा भेटिएका र रूपान्तरण गरिएका फंक्शनहरू LLM लाई दिएका छौं।
    - LLM लाई ती फंक्शनहरूसँग कल गरेका छौं।
    - नतिजा जाँच्दै कुन फंक्शन कल गर्नु पर्छ हेरेका छौं।
    - अन्ततः कल गर्नुपर्ने फंक्शनहरूको एरे पास गरेका छौं।

1. अन्तिम चरण, हाम्रो मुख्य कोड अपडेट गरौं:

    ```python
    prompt = "Add 2 to 20"

    # कुनै भएमा, LLM लाई सबै उपकरणहरू के हुन् सोध्नुहोस्
    functions_to_call = call_llm(prompt, functions)

    # सुझाव गरिएको कार्यहरू कल गर्नुहोस्
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    माथिको कोडमा हामीले:

    - LLM ले हाम्रो प्रॉम्प्टमा आधारित कल गर्नुपर्ने ठानेको फंक्शन प्रयोग गरी MCP उपकरण कल गरेका छौं।
    - उपकरण कलको नतिजा MCP सर्भरमा प्रिन्ट गरेका छौं।

#### .NET

1. LLM प्रॉम्प्ट अनुरोध गर्ने कोड यसरी हुन्छ:

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

    माथिको कोडमा:

    - MCP सर्भरबाट उपकरणहरू ल्यायौं, `var tools = await GetMcpTools()`।
    - प्रयोगकर्ता प्रॉम्प्ट `userMessage` परिभाषित गर्‍यौं।
    - मोडल तथा उपकरणहरू निर्दिष्ट गरेर अप्सन ऑब्जेक्ट बनायौं।
    - LLM तर्फ अनुरोध पठायौं।

1. अन्तिम चरण, LLM ले फंक्शन कल गर्नु पर्छ भनि सोचेमा त्यसो गरौं:

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

    माथिको कोडमा:

    - फंक्शन कलहरूको सूचीमा लूप गर्‍यौं।
    - प्रत्येक उपकरण कलका लागि नाम र आर्गुमेन्ट पार्स गरी MCP सर्भरमा उपकरण कल गरी नतिजा प्रिन्ट गर्‍यौं।

पूर्ण कोड यस्तो छ:

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

माथिको कोडमा:

- सरल प्राकृतिक भाषा प्रॉम्प्ट प्रयोग गरी MCP सर्भर उपकरणहरूसँग अन्तरक्रिया गरेका छौं
- LangChain4j फ्रेमवर्कले स्वचालित रूपमा ह्यान्डल गर्छ:
  - आवश्यक पर्दा प्रयोगकर्ताको प्रॉम्प्टलाई उपकरण कलमा रूपान्तरण
  - LLM को निर्णय अनुसार उपयुक्त MCP उपकरणहरू कल गर्ने
  - LLM र MCP सर्भरबीच संवाद प्रवाह व्यवस्थापन गर्ने
- `bot.chat()` मेथडले प्राकृतिक भाषा प्रतिक्रियाहरू फर्काउँछ जसमा MCP उपकरण प्रदर्शनका नतिजा हुन सक्छन्
- यो दृष्टिकोणले प्रयोगकर्तालाई MCP को भित्री कार्यान्वयन जान्न नपर्ने सहज अनुभव प्रदान गर्छ

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

यहाँ मुख्य कार्य हुन्छ। हामी शुरुमा प्रयोगकर्ता प्रॉम्प्टसहित LLM लाई कल गर्नेछौं, त्यसपछि प्रतिक्रिया हेर्नेछौं कि कुनै उपकरण कल गर्नुपर्नेछ कि छैन। यदि छ भने, ती उपकरणहरू कल गरेर LLM सँग संवाद जारी राख्नेछौं जबसम्म कुनै थप उपकरण कल आवश्यक नहुने र अन्तिम प्रतिक्रिया नआउने।

हामी धेरै पटक LLM कल गर्नेछौं, त्यसैले त्यस्तो फंक्शन परिभाषित गरौं। तलको फंक्शन `main.rs` फाइलमा थप्नुहोस्:

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

यस फंक्शनले LLM क्लाइन्ट, सन्देशहरूको सूची (प्रयोगकर्ता प्रॉम्प्टसहित), MCP सर्भरबाट उपकरणहरू लिन्छ, र LLM लाई अनुरोध पठाएर प्रतिक्रिया फर्काउँछ।
LLM बाट फर्कने प्रतिक्रिया `choices` को एउटा एर्रे समावेश गर्नेछ। हामीले परिणामलाई प्रक्रिया गर्नुपर्नेछ कि कुनै पनि `tool_calls` छन् कि छैनन् भनेर हेर्न। यसले हामीलाई थाहा दिन्छ कि LLM ले कुनै विशेष उपकरणलाई तर्कहरू सहित कल गर्न आग्रह गरिरहेको छ। LLM प्रतिक्रिया ह्यान्डल गर्नको लागि `main.rs` फाइलको तलको भागमा तलको कोड थप्नुहोस्:

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

        // उपकरण परिणामहरूसँग कुराकानी जारी राख्नुहोस्
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

यदि `tool_calls` उपस्थित छन् भने, यसले उपकरण जानकारी निकाल्छ, उपकरण अनुरोध सहित MCP सर्भरलाई कल गर्छ र परिणामहरूलाई संवाद सन्देशहरूमा थप्छ। त्यसपछि यसले LLM सँग संवाद जारी राख्छ र सन्देशहरू सहायकको प्रतिक्रिया र उपकरण कल परिणामहरू सहित अपडेट हुन्छन्।

MCP कलहरूका लागि LLM ले फर्काउने उपकरण कल जानकारी निकाल्नको लागि, हामी अर्को सहायक फंक्शन थप्नेछौं जुन कल गर्न आवश्यक सबै कुरा निकाल्नेछ। `main.rs` फाइलको तलको भागमा निम्न कोड थप्नुहोस्:

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

सबै भागहरू सेट भएपछि, हामीले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्ट ह्यान्डल गर्न र LLM लाई कल गर्न सक्छौं। तपाईंको `main` फंक्शनलाई निम्न कोड समावेश गर्न अपडेट गर्नुहोस्:

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

यसले प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टसँग LLM लाई सोध्नेछ दुई संख्याको योग के हो भनेर, र यो प्रतिक्रिया प्रक्रिया गरेर उपकरण कलहरू डाइनामिक रूपमा ह्यान्डल गर्नेछ।

सुन्दर, तपाईंले यो गर्नुभयो!

## असाइनमेन्ट

अभ्यासबाट कोड लिएर सर्भरलाई केही थप उपकरणहरू सहित निर्माण गर्नुहोस्। त्यसपछि LLM सहित क्लाइन्ट बनाउनुहोस्, अभ्यास जस्तै, र विभिन्न प्रॉम्प्टहरूसँग परीक्षण गर्नुहोस् ताकि तपाईंको सबै सर्भर उपकरणहरू डाइनामिक रूपमा कल हुने सुनिश्चित होस्। यस तरिकाले क्लाइन्ट निर्माण गर्दा अन्त प्रयोगकर्ताले राम्रो प्रयोगकर्ता अनुभव पाउनेछन् किनकि उनीहरूले प्रॉम्प्ट प्रयोग गर्न सक्छन्, सटीक क्लाइन्ट आदेशहरू होइन, र कुनै MCP सर्भर कल भइरहेको छ भन्ने कुरा थाहा पाउने छैनन्।

## समाधान

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## प्रमुख निष्कर्षहरू

- क्लाइन्टमा LLM थप्दा प्रयोगकर्ताहरूलाई MCP सर्भरहरूसँग अन्तरक्रिया गर्न राम्रो तरिका प्रदान हुन्छ।
- तपाईंले MCP सर्भर प्रतिक्रिया LLM बुझ्न सक्ने स्वरूपमा रूपान्तरण गर्न आवश्यक छ।

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
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अपूर्णता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->