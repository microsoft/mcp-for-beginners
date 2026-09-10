# បង្កើតអ្នកដៃគូជាមួយ LLM

រហូតដល់ពេលនេះ អ្នកបានឃើញពីរបៀបបង្កើតម៉ាស៊ីនបម្រើ និងអ្នកដៃគូមួយ។ អ្នកដៃគូអាចអូសម៉ាស៊ីនបម្រើយ៉ាងច្បាស់ ដើម្បីបញ្ជីឧបករណ៍ ជំនួយ និងស្នើសុំ។ ទោះជាយ៉ាងណា វាមិនមែនជារបៀបដែលមានប្រសិទ្ធភាពណាស់ទេ។ អ្នកប្រើប្រាស់របស់អ្នករស់នៅសម័យកាលជាអ្នកប្រតិបត្តិ ហើយរំពឹងថានឹងប្រើប្រាស់ស្នើសុំ និងទំនាក់ទំនងជាមួយ LLM ជំនួស។ ពួកគេមិនខ្វល់ថាអ្នកប្រើ MCP ដើម្បីរក្សាទុកសមត្ថភាពរបស់អ្នក ឬអត់ទេ; ពួកគេសង្ឃឹមថានឹងអាចប្តូរទំនាក់ទំនងដោយប្រើភាសាបែបធម្មជាតិ។ តើយើងដោះស្រាយបញ្ហានេះដូចម្តេច? ការដោះស្រាយគឺស្វែងរកការបន្ថែម LLM ទៅក្នុងអ្នកដៃគូ។

## ទិដ្ឋភាពទូទៅ

ក្នុងមេរៀននេះ យើងផ្ដោតលើការបន្ថែម LLM ទៅក្នុងអ្នកដៃគូ រួចបង្ហាញពីរបៀបដែលវាចូលរួមផ្តល់បទពិសោធន៍ល្អជាងសម្រាប់អ្នកប្រើរបស់អ្នក។

## គោលបំណងស្វែងយល់

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច:

- បង្កើតអ្នកដៃគូជាមួយ LLM។
- បង្កើតការទំនាក់ទំនងរលូនជាមួយម៉ាស៊ីនបម្រើ MCP ដោយប្រើ LLM។
- ផ្តល់បទពិសោធន៍ដ៏ល្អសម្រាប់អ្នកប្រើនៅផ្នែកអ្នកដៃគូ។

## វិធីសាស្ត្រ

យើងព្យាយាមយល់ពីវិធីសាស្ត្រដែលត្រូវអនុវត្ត។ ការបន្ថែម LLM សំដៅថាសាមញ្ញ ប៉ុន្តែតើយើងពិតជាធ្វើបានដែរឬទេ?

នេះជាវិធីដែលអ្នកដៃគូអាចទំនាក់ទំនងទៅម៉ាស៊ីនបម្រើ:

1. កសាងការតភ្ជាប់ទៅម៉ាស៊ីនបម្រើ។

1. បញ្ជីសមត្ថភាព សំណើ សម្ភារៈ និងឧបករណ៍ ហើយរក្សាទុកស្កីម៉ារបស់ពួកវា។

1. បន្ថែម LLM ហើយផ្ញើសមត្ថភាព និងស្កីម៉ារដែលបានរក្សាទុកទៅជាទ្រង់ទ្រាយដែល LLM អាចយល់បាន។

1. ដោះស្រាយសំណើរបស់អ្នកប្រើ ដោយផ្ញើវាទៅ LLM ព្រមទាំងឧបករណ៍ដែលបានបញ្ជីដោយអ្នកដៃគូ។

ល្អហើយ ឥឡូវយើងបានយល់ពីរបៀបធ្វើការនេះនៅកម្រិតខ្ពស់ តោះយកវាក្នុងលំហាត់ខាងក្រោម។

## លំហាត់៖ បង្កើតអ្នកដៃគូជាមួយ LLM

ក្នុងលំហាត់នេះ យើងនឹងរៀនពីរបៀបបន្ថែម LLM ទៅក្នុងអ្នកដៃគូរបស់យើង។

### ការផ្ទៀងផ្ទាត់ដោយប្រើ GitHub Personal Access Token

ការបង្កើតតោគិន GitHub គឺជាការប្រតិបត្តិដ៏ងាយស្រួល។ វិធីធ្វើមានដូចខាងក្រោម៖

- បើកទៅ GitHub Settings – ចុចរូបភាពរបស់អ្នក នៅខាងលើស្តាំ ហើយជ្រើស Settings។
- ទៅ Developer Settings – រោទ៍ចុះក្រោម ហើយចុច Developer Settings។
- ជ្រើស Personal Access Tokens – ចុច Fine-grained tokens ហើយបន្ទាប់មក Generate new token។
- កំណត់តោគិនរបស់អ្នក – បន្ថែមកំណត់ចំណាំ សំរាប់យោង កំណត់ថ្ងៃផុតកំណត់ និងជ្រើសកាត់បន្ថែមត្រឹមត្រូវ (សិទ្ធិ)។ ក្នុងករណីនេះ គួរតែបន្ថែមសិទ្ធិ Models។
- បង្កើតហើយចម្លងតោគិន – ចុច Generate token ហើយប្រាកដថាចម្លងវាបន្ទាន់ ដូចឥឡូវនេះអ្នកមិនអាចមើលវាបានម្តងទៀតឡើយ។

### -1- តភ្ជាប់ទៅម៉ាស៊ីនបម្រើ

យើងចាប់ផ្តើមបង្កើតអ្នកដៃគូរបស់យើងមុន៖

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // នាំចូល zod សម្រាប់ការផ្ទៀងផ្ទាត់ស្កីម៉ា

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

នៅក្នុងកូដមុននេះ យើងបាន:

- យកប្រើបណ្ណាល័យដែលត្រូវការ
- បង្កើតថ្នាក់មួយជាមួយសមាជិកពីរ `client` និង `openai` ដែលជួយគ្រប់គ្រងអ្នកដៃគូ និងទំនាក់ទំនងជាមួយ LLM ផ្ទាល់។
- កំណត់ជំនួស LLM របស់យើង ដើម្បីប្រើ GitHub Models ដោយកំណត់ `baseUrl` ទៅកាន់ API inference។

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# បង្កើតប៉ារ៉ាម៉ែត្រសម្រាប់ការតភ្ជាប់ stdio
server_params = StdioServerParameters(
    command="mcp",  # ឯកសារអនុវត្ត
    args=["run", "server.py"],  # អាគុយម៉ង់បន្ទាត់បញ្ជាដែលជាជម្រើស
    env=None,  # អថេរបរិស្ថានដែលជាជម្រើស
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ផ្ដើមការតភ្ជាប់
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

នៅក្នុងកូដមុននេះ យើងបាន:

- យកបណ្ណាល័យដែលត្រូវការ សម្រាប់ MCP
- បង្កើតអ្នកដៃគូ

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

ដំបូង អ្នកត្រូវបន្ថែមការពឹងផ្អែក LangChain4j ទៅក្នុងឯកសារ `pom.xml` របស់អ្នក។ បន្ថែមការពឹងផ្អែកទាំងនេះ ដើម្បីអនុញ្ញាតឲ្យមានការតភ្ជាប់ MCP និង MiniMax API ដែលផ្គូរផ្គង OpenAI៖

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

កំណត់កូនសោ MiniMax API របស់អ្នក និង ជម្រើសបន្ថែម ដូចជា endpoint និង ម៉ូដែល។
`MINIMAX_MODEL_ID` គាំទ្រ `MiniMax-M3` និង `MiniMax-M2.7`។ ប្រសិនបើ
មិនបានកំណត់ `OPENAI_BASE_URL` ទេ `MINIMAX_REGION` គាំទ្រ `global_en` និង `cn_zh`។

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ដើម្បីជ្រើស endpoint ផ្អែកលើតំបន់ ជ្រើសលុប `OPENAI_BASE_URL` ៖

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

បន្ទាប់មក បង្កើតថ្នាក់អ្នកដៃគូ Java របស់អ្នក ៖

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

        // បង្កើតការដឹកជញ្ជូន MCP សម្រាប់ការតភ្ជាប់ទៅម៉ោងបម្រើ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // បង្កើតអតិថិជន MCP
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

នៅក្នុងកូដមុននេះ យើងបាន:

- **បន្ថែមការពឹងផ្អែក LangChain4j**៖ ត្រូវការសម្រាប់ការតភ្ជាប់ MCP និង MiniMax API ដែលផ្គូរផ្គង OpenAI
- **យកបណ្ណាល័យ LangChain4j**៖ សម្រាប់ការតភ្ជាប់ MCP និងមុខងារ chat model OpenAI
- **បង្កើត `ChatLanguageModel`**៖ កំណត់ប្រើ MiniMax ជាមួយកូនសោ MiniMax API, endpoint និងម៉ូដែលគាំទ្រ
- **កំណត់ការកោះវិញ HTTP**៖ ប្រើ Server-Sent Events (SSE) ដើម្បីភ្ជាប់ម៉ាស៊ីនបម្រើ MCP
- **បង្កើតអតិថិជន MCP**៖ ដែលនឹងដោះស្រាយទំនាក់ទំនងជាមួយម៉ាស៊ីនបម្រើ
- **ប្រើការគាំទ្រដែលមានរួចរបស់ LangChain4j លើ MCP**៖ ដែលធ្វើឲ្យការបញ្ចូលរវាង LLM និងម៉ាស៊ីនបម្រើ MCP គឺសាមញ្ញ

#### Rust

ឧទាហរណ៍នេះបើកចំហសម្រាប់អ្នកមានម៉ាស៊ីនបម្រើ MCP ដែលផ្អែកលើ Rust។ ប្រសិនបើអ្នកមិនមានទេ សូមយោងទៅមេរៀន [01-first-server](../01-first-server/README.md) ដើម្បីបង្កើតម៉ាស៊ីនបម្រើ។

បន្ទាប់ពីអ្នកមានម៉ាស៊ីនបម្រើ Rust MCP បើក terminal ហើយចូលទៅកាន់ថតដដែលជាមួយម៉ាស៊ីនបម្រើ។ បន្ទាប់មកដំណើរការ អនុប្បទានខាងក្រោម ដើម្បីបង្កើតគម្រោងអតិថិជន LLM ថ្មីមួយ៖

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

បន្ថែមការពឹងផ្អែកខាងក្រោមទៅ​ `Cargo.toml` របស់អ្នក៖

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> មិនមានបណ្ណាល័យផ្លូវការសម្រាប់ OpenAI នៅក្នុង Rust ទេ ទោះជាយ៉ាងណា `async-openai` គឺជាបណ្ណាល័យដែលមានការថែរក្សាដោយសហគមន៍ ដែលតែងតែប្រើប្រាស់នៅបច្ចុប្បន្ន។

បើកឯកសារ `src/main.rs` ហើយប្ដូរកូដខាងក្នុងជាមួយកូដខាងក្រោម៖

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
    // សារដំបូង
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // កំណត់ម៉ាស៊ីនអតិថិជន OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // កំណត់ម៉ាស៊ីនអតិថិជន MCP
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

    // TODO: ទទួលបានបញ្ជីឧបករណ៍ MCP

    // TODO: សន្ទនាទំព័រធំ (LLM) ជាមួយការហៅឧបករណ៍

    Ok(())
}
```

កូដនេះរៀបចំកម្មវិធី Rust មូលដ្ឋាន ដែលនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP និង GitHub Models សម្រាប់ការប្រើប្រាស់ LLM។

> [!IMPORTANT]
> សូមមិនភ្លេចកំណត់អថេរ `OPENAI_API_KEY` ជាមួយតោគិន GitHub របស់អ្នក មុនពេលដំណើរការកម្មវិធី។

ល្អហើយ សម្រាប់ជំហានបន្ទាប់ យើងចុះបញ្ជីសមត្ថភាពនៅលើម៉ាស៊ីនបម្រើ។

### -2- បញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ

ឥឡូវនេះ យើងនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ ហើយស្នើសុំសមត្ថភាពរបស់វា៖

#### Typescript

ក្នុងថ្នាក់ដដែល ផ្ដល់វិធីសាស្ត្រខាងក្រោម៖

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // បញ្ជីឧបករណ៍
    const toolsResult = await this.client.listTools();
}
```

នៅក្នុងកូដមុននេះ យើងបាន:

- បន្ថែមកូដសម្រាប់ភ្ជាប់ទៅម៉ាស៊ីនបម្រើ `connectToServer`។
- បង្កើតវិធីសាស្ត្រ `run` ដែលទទួលខុសត្រូវច្រកបង្ហាញកម្មវិធី។ រហូតដល់ពេលនេះ វាត្រឹមតែបញ្ជីឧបករណ៍ ប៉ុន្តែយើងនឹងបន្ថែមជាច្រើនទៀតភាគខាងមុខ។

#### Python

```python
# បញ្ជីធនធានដែលមាន
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# បញ្ជីឧបករណ៍ដែលមាន
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ខាងក្រោមជារឿងដែលយើងបានបន្ថែម៖

- បញ្ជីធនធាន និងឧបករណ៍ ហើយបោះពុម្ពពួកវា។ សម្រាប់ឧបករណ៍ យើងក៏បញ្ជី `inputSchema` ដែលយើងប្រើបន្តក្រោម។

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

នៅក្នុងកូដមុននេះ យើងបាន:

- បញ្ជីឧបករណ៍ដែលមាននៅលើម៉ាស៊ីនបម្រើ MCP
- សម្រាប់ឧបករណ៍នីមួយៗ បញ្ជីឈ្មោះ ការពិពណ៌នា និងស្កីម៉ារបស់វា។ វាងាយស្រួលសម្រាប់យើងប្រើការហៅឧបករណ៍បន្ថែម។

#### Java

```java
// បង្កើតអ្នកផ្គត់ផ្គង់ឧបករណ៍ដែលស្វ័យប្រវត្តិរកឃើញឧបករណ៍ MCP
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// អ្នកផ្គត់ផ្គង់ឧបករណ៍ MCP ដំណើរការដោយស្វ័យប្រវត្តិ៖
// - បង្ហាញបញ្ជីឧបករណ៍ដែលមានពីម៉ាស៊ីនមេ MCP
// - បម្លែងស្ខេម៉ាស្វ្រិចឧបករណ៍ MCP ទៅជា​ទ្រង់ទ្រាយ LangChain4j
// - គ្រប់គ្រងការប្រតិបត្តិការឧបករណ៍ និងចម្លើយ
```

នៅក្នុងកូដមុននេះ យើងបាន:


- បានបង្កើត `McpToolProvider` ដែលស្វ័យប្រវត្តិក្នុងការស្វែងរកនិងចុះបញ្ជីឧបករណ៍ទាំងអស់ពីម៉ាស៊ីនបម្រើ MCP
- អ្នកផ្គត់ផ្គង់ឧបករណ៍ដំណើរការការបំប្លែងរវាងគំរូឧបករណ៍ MCP និងទ្រង់ទ្រាយឧបករណ៍របស់ LangChain4j ខាងក្នុង
- វិធីនេះរំលាយដំណើរការ​បញ្ជីឧបករណ៍និងការបំប្លែងដោយដៃ

#### Rust

ការយកឧបករណ៍ពីម៉ាស៊ីនបម្រើ MCP ប្រើវិធី `list_tools`។ នៅក្នុងមុខងារ `main` របស់អ្នក បន្ទាប់ពីការតំឡើងអតិថិជន MCP សូមបន្ថែមកូដដូចខាងក្រោម៖

```rust
// ទទួលបានបញ្ជីឧបករណ៍ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- បម្លែងសមត្ថភាពម៉ាស៊ីនបម្រើទៅឧបករណ៍ LLM

ជំហានបន្ទាប់បន្ទាប់ពីបញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើគឺបម្លែងវាទៅទ្រង់ទ្រាយដែល LLM អាចយល់។ បន្ទាប់ពីយើងធ្វើវានេះ អាចផ្តល់សមត្ថភាពទាំងនេះជាឧបករណ៍ទៅ LLM របស់យើង។

#### TypeScript

1. បន្ថែមកូដដូចខាងក្រោមដើម្បីបម្លែងការឆ្លើយតបពីម៉ាស៊ីនបម្រើ MCP ទៅទ្រង់ទ្រាយឧបករណ៍ដែល LLM អាចប្រើបាន៖

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // បង្កើតchema Zod dựa trên input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // កំណត់ប្រភេទជា "function" อย่างชัดเจน
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

    កូដខាងលើយកការឆ្លើយតបពីម៉ាស៊ីនបម្រើ MCP ហើយបម្លែងទៅទ្រង់ទ្រាយកំណត់ឧបករណ៍ដែល LLM អាចយល់។

2. យើងចាប់ផ្តើមបន្ទាន់សម័យវិធី `run` ដើម្បីបញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ៖

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

    ក្នុងកូដមុន ពួកយើងបានបន្ទាន់សម័យវិធី `run` ដើម្បីបដិសេធចូលរួមតាមលទ្ធផល ហើយសម្រាប់រាល់ចំណុចបន្ទាន់ហៅ `openAiToolAdapter`។

#### Python

1. ដំបូង សូមបង្កើតមុខងារ converters ដូចខាងក្រោម

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

    នៅក្នុងមុខងារ `convert_to_llm_tools` ខាងលើ យើងយកការឆ្លើយតបឧបករណ៍ MCP ហើយបម្លែងវាទៅទ្រង់ទ្រាយដែល LLM អាចយល់។

2. បន្ទាប់មក យើងបន្ទាន់សម័យកូដអតិថិជនរបស់យើង ដើម្បីប្រើអនុគមន៍នេះ ដូចខាងក្រោម៖

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    នៅទីនេះ យើងលើកកូដហៅ `convert_to_llm_tool` ដើម្បីបម្លែងការឆ្លើយតបឧបករណ៍ MCP ទៅสิ่งដែលយើងអាចផ្គត់ផ្គង់ទៅ LLM បន្ទាប់។

#### .NET

1. សូមបន្ថែមកូដដើម្បីបម្លែងការឆ្លើយតបឧបករណ៍ MCP ទៅវត្ថុដែល LLM អាចយល់បាន

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

នៅក្នុងកូដមុនហើយបាន៖

- បង្កើតមុខងារ `ConvertFrom` ដែលទទួលបានឈ្មោះ ការពណ៌នា និងគំរូបញ្ចូល។
- កំណត់មុខងារដែលបង្កើត `FunctionDefinition` ដែលត្រូវបានផ្ញើទៅ `ChatCompletionsDefinition`។ បច្ចេកទេសចុងក្រោយនេះគឺជារបស់ដែល LLM អាចយល់។

2.​ មកមើលរបៀបដែលយើងអាចបន្ទាន់សម័យកូដមានស្រាប់ ដើម្បីទទួលផលពីមុខងារខាងលើនេះ៖

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
// បង្កើតចំណុចប្រទាក់បូតសម្រាប់ការប្រាស្រ័យទាក់ទងជាភាសាធម្មតា
public interface Bot {
    String chat(String prompt);
}

// កំណត់ការកំណត់សេវាកម្ម AI ជាមួយឧបករណ៍ LLM និង MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

នៅក្នុងកូដមុនហើយបាន៖

- កំណត់អន្តរាគមន៍ `Bot` ងាយស្រួលសម្រាប់ការប្រាស្រ័យភាសាធម្មជាតិ
- ប្រើប្រាស់ `AiServices` របស់ LangChain4j ដើម្បីភ្ជាប់ LLM ជាមួយ MCP tool provider ដោយស្វ័យប្រវត្តិ
- ស៊ុមផ្នែកបានដំណើរការ ការបំលែងគំរូឧបករណ៍ និងហៅមុខងារវិញក្រោយឆាក
- វិធីនេះបំបាត់ការបំលែងឧបករណ៍ដោយដៃ - LangChain4j គ្រប់គ្រងភាពស្មុគស្មាញនៃការបំលែងឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែលអាចប្រើ LLM

#### Rust

ដើម្បីបម្លែងការឆ្លើយតបឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែល LLM អាចយល់ យើងនឹងបន្ថែមមុខងារជំនួយមួយ ដែលរៀបចំព័ត៌មានបញ្ជីឧបករណ៍។ សូមបន្ថែមកូដខាងក្រោមក្នុងឯកសារ `main.rs` របស់អ្នកនៅក្រោមមុខងារ `main`។ វានឹងត្រូវហៅនៅពេលធ្វើការស្នើសុំទៅ LLM ៖

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

ល្អហើយ ឥឡូវយើងមិនទាន់រៀបចំដើម្បីដោះស្រាយសំណើរអ្នកប្រើនៅឡើយទេ ដូច្នេះយើងនឹងដោះស្រាយវាដំបូង។

### -4- ដោះស្រាយសំណើរបញ្ចេញពាក្យរបស់អ្នកប្រើ

ក្នុងផ្នែកនេះ យើងនឹងដោះស្រាយសំណើរអ្នកប្រើ។

#### TypeScript

1. បន្ថែមមុខងារមួយដែលនឹងប្រើសម្រាប់ហៅ LLM របស់យើង៖

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ហៅឧបករណ៍របស់ម៉ាស៊ីនមេ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ធ្វើអ្វីមួយជាមួយលទ្ធផល
        // TODO

        }
    }
    ```

    ក្នុងកូដមុនយើងបាន៖

    - បន្ថែមមុខងារ `callTools`។
    - មុខងារនៅត្រូវទទួលបានការឆ្លើយតបពី LLM ហើយពិនិត្យមើលថាតើមានឧបករណ៍ណាត្រូវបានហៅដែរឬទេ:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ហៅឧបករណ៍
        }
        ```

    - ហៅឧបករណ៍ ប្រសិនបើ LLM បង្ហាញថាត្រូវហៅ:

        ```typescript
        // 2. ហៅឧបករណ៍របស់ម៉ាស៊ីនបម្រើ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ធ្វើអ្វីមួយជាមួយលទ្ធផល
        // ធ្វើទុក
        ```

2. បន្ទាន់សម័យវិធី `run` ដើម្បីរួមបញ្ចូលការហៅទៅលើ LLM និងហៅ `callTools`៖

    ```typescript

    // ១. បង្កើតសារ​ដែល​ជា​ការ​បញ្ចូល​សម្រាប់ LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ២. អូសហៅ LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ៣. ពិនិត្យចម្លើយ LLM សម្រាប់ជម្រើសនីមួយៗ ពិនិត្យមើលថាតើមានការហៅឧបករណ៍ទេឬអត់
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ល្អ ខ្ញុំទាញយកកូដពេញលេញ៖

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // នាំចូល zod សម្រាប់ផ្ទៀងផ្ទាត់ schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ប្រហែលជាត្រូវបំលែងទៅ url នេះនៅអនាគត: https://models.github.ai/inference
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
          // បង្កើត schema zod បើអាស្រ័យលើ input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // កំណត់ប្រភេទជា "function" ដោយច្បាស់
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
    
    
          // ២. ហៅឧបករណ៍តាមម៉ាស៊ីនមេ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ៣. ធ្វើអ្វីមួយជាមួយលទ្ធផល
          // ត្រូវធ្វើ
    
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
    
        // ៣. ត្រួតពិនិត្យចំលើយ LLM សម្រាប់ជម្រើសនីមួយៗ តើមានការហៅឧបករណ៍ឬអត់
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

1. ចូលនូវមុខងារមួយចំនួនដែលទាមទារសម្រាប់ហៅ LLM

    ```python
    # ឡលម
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. បន្ទាប់មក បន្ថែមមុខងារដែលនឹងហៅ LLM៖

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
            # ប៉ារ៉ាម៉ែត្រជាជម្រើស
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

    ក្នុងកូដមុនយើងបាន៖

    - ផ្ញើមុខងាររបស់យើង ដែលយើងបានរកឃើញលើម៉ាស៊ីនបម្រើ MCP និងបម្លែងរួចពីមុខងារ។
    - បន្ទាប់ហៅ LLM ជាមួយមុខងារទាំងនោះ។
    - បន្ទាប់ ពិនិត្យលទ្ធផលមើលថាតើមានមុខងារណាដែលត្រូវហៅ ប្រសិនបើមាន។
    - ចុងក្រោយ យើងផ្ញើបញ្ជីមុខងារដើម្បីហៅ។

3. ជំហានចុងក្រោយ សូមបន្ទាន់សម័យកូដសំខាន់របស់យើង៖

    ```python
    prompt = "Add 2 to 20"

    # សួរលីអេលអែមពីឧបករណ៍អ្វីខ្លះ សម្រាប់គ្រប់គ្នា ប្រសិនបើមាន
    functions_to_call = call_llm(prompt, functions)

    # ហៅមុខងារដែលបានណែនាំ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    នៅទីនោះ ជាជំហានចុងក្រោយ ក្នុងកូដខាងលើយើងបាន៖

    - ហៅឧបករណ៍ MCP តាម `call_tool` ប្រើមុខងារដែល LLM គិតថាត្រូវហៅដោយផ្អែកលើពាក្យបញ្ចេញរបស់យើង។
    - បោះពុម្ពលទ្ធផលនៃការហៅឧបករណ៍ទៅម៉ាស៊ីនបម្រើ MCP។

#### .NET

1. ចុះបង្ហាញកូដសម្រាប់ធ្វើសំណើរបញ្ចេញពាក្យទៅ LLM៖

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

    ក្នុងកូដមុនយើងបាន៖

    - ទាញយកឧបករណ៍ពីម៉ាស៊ីនបម្រើ MCP, `var tools = await GetMcpTools()`.
    - កំណត់ពាក្យបញ្ចេញអ្នកប្រើ `userMessage`.
    - បង្កើតអភិលិខិតជម្រើសដែលបញ្ជាក់ម៉ូដែល និងឧបករណ៍។
    - ធ្វើសំណើទៅ LLM។

2. ជំហានចុងក្រោយមួយ សូមមើលថាតើ LLM គិតថាត្រូវហៅមុខងារមួយទេ៖

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

    ក្នុងកូដមុនយើងបាន៖

    - ជុំវិញបញ្ជីហៅមុខងារ។
    - សម្រាប់រាល់ការហៅឧបករណ៍ អ្នកវិភាគឈ្មោះ និងអាគុយម៉ង់ ហើយហៅឧបករណ៍នៅលើម៉ាស៊ីនបម្រើ MCP ដោយប្រើអតិថិជន MCP។ ចុងក្រោយបោះពុម្ពលទ្ធផល។

នៅទីនេះជាកូដពេញលេញ៖

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
    // អនុវត្តសេចក្តីស្នើសុំភាសាធម្មជាតិតាមរយៈការប្រើឧបករណ៍ MCP ដោយស្វ័យប្រវត្តិ
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

នៅក្នុងកូដមុនយើងបាន៖

- ប្រើអត្ថបទធម្មជាតិសាមញ្ញសម្រាប់ប្រតិបត្តិការជាមួយឧបករណ៍ម៉ាស៊ីនបម្រើ MCP
- លំហាត់ LangChain4j ដំណើរការដោយស្វ័យប្រវត្តិ៖
  - ការបំលែងសំណួរអ្នកប្រើទៅហៅឧបករណ៍នៅពេលចាំបាច់
  - ហៅឧបករណ៍ MCP ដែលសមស្របដោយសេចក្ដីសម្រេចអ្នក LLM
  - គ្រប់គ្រងផ្លូវការប្រាស្រ័យគ្នារវាង LLM និងម៉ាស៊ីនបម្រើ MCP
- មុខងារ `bot.chat()` បញ្ចេញការឆ្លើយតបភាសាធម្មជាតិដែលអាចរួមបញ្ចូលលទ្ធផលពីការប្រតិបត្តិឧបករណ៍ MCP
- វិធីនេះផ្តល់បទពិសោធន៍ដំណើរការយ៉ាងរលូនដែលអ្នកប្រើមិនចាំបាច់ដឹងអំពីការអនុវត្ត MCP នៅខាងក្រោម

ឧទាហរណ៍កូដពេញលេញ៖

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

នៅទីនេះជាកន្លែងដែលការងារចម្បងកើតឡើង។ យើងនឹងហៅ LLM ជាមួយពាក្យបញ្ចេញដំបូងពីអ្នកប្រើ បន្ទាប់ពីនោះបំលែងការឆ្លើយតបដើម្បីពិនិត្យថាតើមានឧបករណ៍ណាត្រូវហៅ។ ប្រសិនបើមាន យើងនឹងហៅឧបករណ៍ទាំងនោះ ហើយបន្តការសន្ទនាជាមួយ LLM រហូតដល់មិនមានការហៅឧបករណ៍បន្ថែមទៀត ហើយយើងទទួលបានការឆ្លើយតបចុងក្រោយ។


យើងនឹងធ្វើការហៅទៅកាន់ LLM ជាច្រើនដង ដូច្នេះចង់សរសេរមួយមុខងារ ដែលអាចគ្រប់គ្រងការហៅ LLM បាន។ សូមបន្ថែមមុខងារខាងក្រោមទៅក្នុងឯកសារ `main.rs` របស់អ្នក៖

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

មុខងារនេះទទួល LLM client, បញ្ជីសារ (រួមទាំងសំណើរពីអ្នកប្រើប្រាស់), ឧបករណ៍ពីម៉ាស៊ីន MCP server ហើយផ្ញើសំណើទៅ LLM បង្រួមសំណូមពរនេះវិញ។

លទ្ធផលពី LLM នឹងមានអារេនៃ `choices`។ យើងត្រូវដំណើរការវានេះដើម្បីមើលថា មាន `tool_calls` មួយណាត្រូវបានបង្ហាញមកទេ។ វាបង្ហាញថា LLM កំពុងស្នើអោយហៅឧបករណ៍ពិសេសមួយជាមួយអាគុយម៉ង់។ សូមបន្ថែមកូដខាងក្រោមចុងឯកសារ `main.rs` របស់អ្នកដើម្បីកំណត់មុខងារមួយសម្រាប់គ្រប់គ្រងការឆ្លើយតបរបស់ LLM៖

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

    // ព្រីនមាតិកានៅពេលមាន
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ដំណើរការហៅឧបករណ៍
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // បន្ថែមសារជំនួយការ

        // អនុវត្តការហៅឧបករណ៍និមួយៗ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // បន្ថែមលទ្ធផលឧបករណ៍ទៅសារជាសារ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // បន្តសំនួរឆ្លើយតបជាមួយលទ្ធផលឧបករណ៍
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

ប្រសិនបើ `tool_calls` មាន វានឹងដកសេចក្ដីព័ត៌មានឧបករណ៍ ហៅម៉ាស៊ីន MCP ជាមួយសំណើហៅឧបករណ៍ ហើយបន្ថែមលទ្ធផលទៅក្នុងសារហូរហែរនៃការសន្ទនា។ បន្ទាប់មក វានឹងបន្តសន្ទនាជាមួយ LLM ហើយសារៗត្រូវបានធ្វើបច្ចុប្បន្នភាពជាមួយនឹងការឆ្លើយតបរបស់ជំនួយករ និងលទ្ធផលហៅឧបករណ៍។

ដើម្បីដកសេចក្ដីព័ត៌មានហៅឧបករណ៍ដែល LLM ត្រឡប់មកសម្រាប់ការហៅ MCP យើងនឹងបន្ថែមមុខងារជំនួយមួយទៀតសម្រាប់ទាញយកអ្វីៗទាំងអស់ដែលត្រូវការ សម្រាប់ធ្វើការហៅនេះ។ សូមបន្ថែមកូដខាងក្រោមចុងឯកសារ `main.rs` របស់អ្នក៖

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

ជាមួយគ្រប់ការភ្ជាប់មានរួចហើយ យើងអាចគ្រប់គ្រងសំណើដើមពីអ្នកប្រើប្រាស់ និងហៅ LLM បាន។ អាប់ដេតមុខងារ `main` របស់អ្នក ដើម្បីរួមបញ្ចូលកូដខាងក្រោម៖

```rust
// ការពិភាក្សា LLM ជាមួយការហៅឧបករណ៍
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

នេះនឹងសួរទៅកាន់ LLM ជាមួយសំណើដើមរបស់អ្នកប្រើប្រាស់សុំរកផលបូកនៃលេខពីរ ហើយវានឹងដំណើរការឆ្លើយតប ដើម្បីគ្រប់គ្រងការហៅឧបករណ៍អោយមានសកម្មភាព។

ល្អណាស់ អ្នកបានបញ្ចប់វា!

## កិច្ចការ

អូសកូដពីលំហាត់នេះហើយបង្កើតម៉ាស៊ីនមេជាមួយឧបករណ៍បន្ថែមទៀត។ បន្ទាប់មកបង្កើតម៉ាស៊ីនអតិថិជនជាមួយ LLM ដូចក្នុងលំហាត់ ហើយសាកល្បងវាជាមួយសំណើខុសៗគ្នា ដើម្បីធានាថា ឧបករណ៍ម៉ាស៊ីនមេទាំងអស់របស់អ្នកត្រូវបានហៅដោយសកម្ម។ វិធីសាស្រ្តនេះក្នុងការបង្កើតម៉ាស៊ីនអតិថិជន មានន័យថា អ្នកប្រើចុងក្រោយនឹងមានបទពិសោធន៍ល្អ ពីព្រោះពួកគេចំណាស់អាចប្រើសំណើ ជំនួសបញ្ជាលំអិតរបស់កូដអតិថិជន ហើយមិនដឹងថា MCP server កំពុងត្រូវបានហៅនៅខាងក្រោយទេ។

## ដំណោះស្រាយ

[ដំណោះស្រាយ](./solution/README.md)

## ចំណុចសំខាន់ៗ

- ការបន្ថែម LLM ទៅក្នុងម៉ាស៊ីនអតិថិជនរបស់អ្នកផ្តល់វិធីល្អជាងសម្រាប់អ្នកប្រើប្រាស់ក្នុងការប្រាស្រ័យជាមួយ MCP Servers។
- អ្នកត្រូវបម្លែងចម្លើយពីម៉ាស៊ីនមេ MCP ទៅជាអ្វីមួយដែល LLM អាចយល់បាន។

## ឧទាហរណ៍

- [កញ្ចប់គណនាវិជ្ជាជីវៈ Java](../samples/java/calculator/README.md)
- [កញ្ចប់គណនាវិជ្ជាជីវៈ .Net](../../../../03-GettingStarted/samples/csharp)
- [កញ្ចប់គណនាវិជ្ជាជីវៈ JavaScript](../samples/javascript/README.md)
- [កញ្ចប់គណនាវិជ្ជាជីវៈ TypeScript](../samples/typescript/README.md)
- [កញ្ចប់គណនាវិជ្ជាជីវៈ Python](../../../../03-GettingStarted/samples/python)
- [កញ្ចប់គណនាវិជ្ជាជីវៈ Rust](../../../../03-GettingStarted/samples/rust)

## ឯកសារបន្ថែម

## អ្វីខ្លះនៅក្រោយ

- បន្ទាប់: [ការប្រើម៉ាស៊ីនមេជាមួយ Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->