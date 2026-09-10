# ការបង្កើតអតិថិជនជាមួយ LLM

> [!NOTE]
> ឧទាហរណ៍អតិថិជន Java កំពុងភ្ជាប់តាមរយៈការដឹកជញ្ជូន HTTP+SSE បុរាណ និង
> គោលដៅមក MCP `2025-11-25` SDK APIs។ សូមប្រើ SDK ដែលត្រូវសមនឹង `2026-07-28` និង
> Streamable HTTP សម្រាប់អតិថិជនទាំងថ្មីពីចម្ងាយ។

ដល់ពេលនេះ អ្នកបានឃើញរបៀបបង្កើតម៉ាស៊ីនបម្រើនិងអតិថិជន។ អតិថិជនអាចហៅម៉ាស៊ីនបម្រើដោយច្បាស់លាស់ដើម្បីបញ្ជីឧបករណ៍ ប្រភពធនធាន និងការជំរុញរបស់វា។ ទោះយ៉ាងណា វាមិនមែនជាវិធីប្រើប្រាស់អនុវត្ត្ន៍បានល្អទេ។ អ្នកប្រើប្រាស់របស់អ្នករស់នៅសម័យភ្នាក់ងារហើយរំពឹងទុកប្រើការជំរុញ និងទំនាក់ទំនងជាមួយ LLM ជាក់លាក់វិញ។ ពួកគេមិនថានៅពេលណាអ្នកប្រើ MCP ដើម្បីផ្ទុកសមត្ថភាពរបស់អ្នកឡើយ ពួកគែងទុកចិត្តថានឹងអាចទាក់ទងតាមភាសាធម្មជាតិ។ តើតើយើងដោះស្រាយបញ្ហានេះយ៉ាងដូចម្តេច? ដំណោះស្រាយគឺបន្ថែម LLM ចូលទៅក្នុងអតិថិជន។

## ទិដ្ឋភាពទូទៅ

ក្នុងមេរៀននេះ យើងផ្តោតលើការបន្ថែម LLM ដើម្បីធ្វើអតិថិជនរបស់អ្នក ហើយបង្ហាញថាវាបន្ថែមបទពិសោធន៍ល្អជាងសម្រាប់អ្នកប្រើប្រាស់របស់អ្នកយ៉ាងដូចម្តេច។

## គោលបំណងរៀន

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាចធ្វើបាន៖

- បង្កើតអតិថិជនជាមួយ LLM។
- ទំនាក់ទំនងបានដោយរលូនជាមួយម៉ាស៊ីនបម្រើ MCP ប្រើប្រាស់ LLM។
- ផ្តល់បទពិសោធន៍អ្នកប្រើដែលល្អជាងនៅផ្នែកអតិថិជន។

## វិធីសាស្រ្ត

យើងខំយល់យ៉ាងណានូវវិធីសាស្រ្តដែលយើងត្រូវអនុវត្ត។ ការបន្ថែម LLM សូម្បីតែហាក់ដូចសាមញ្ញ ប៉ុន្តែតើយើងនៅពិតធ្វើបែបនេះមែនទេ?

នេះជារបៀបដែលអតិថិជននឹងទំនាក់ទំនងជាមួយម៉ាស៊ីនបម្រើ៖

1. ស្ថាបនាការតភ្ជាប់ជាមួយម៉ាស៊ីនបម្រើ។

1. បញ្ជីសមត្ថភាព ការជំរុញ ធនធាន និងឧបករណ៍ រួចរក្សាទុកស្កីម៉ារបស់ពួកវាទុក។

1. បន្ថែម LLM ហើយផ្ទុកសមត្ថភាពដែលបានរក្សាទុក និងស្កីម៉ារបស់ពួកវា ដោយប្រើទ្រង់ទ្រាយដែល LLM យល់ដឹង។

1. គ្រប់គ្រងការជំរុញអ្នកប្រើដោយផ្ញើវាទៅកាន់ LLM ជាមួយឧបករណ៍ដែលបានបញ្ជីដោយអតិថិជន។

អស្ចារ្យ​ហើយ​ឥឡូវ​យើង​យល់​ថា​យើង​អាច​ធ្វើ​របៀប​នេះ​នៅ​លម្អិតខ្ពស់ តោះ​សាកល្បង​ដំណើរការ​នៅ​ក្នុង​អនុវត្តខាងក្រោម។

## កំណាត់ហាត់ការណ៍៖ ការបង្កើតអតិថិជនជាមួយ LLM

នៅក្នុងហាត់ការណ៍នេះ យើងនឹងរៀនបន្ថែម LLM ទៅក្នុងអតិថិជនរបស់យើង។

### ការផ្ទៀងផ្ទាត់ដោយប្រើ GitHub Personal Access Token

ការបង្កើតសំបុត្រ GitHub គឺជាដំណើរការងាយស្រួល។ នេះគឺរបៀបអ្នកអាចធ្វើបាន៖

- ទៅកាន់ GitHub Settings – ចុចលើរូបភាពប្រវត្តិរូបរបស់អ្នកនៅខាងស្តាំលើហើយជ្រើសទំរង់ Settings។
- នាវ្ប្រឹង់ទៅ Developer Settings – ស្ពScrollឡើងក្រោមហើយចុច Developer Settings។
- ជ្រើស Personal Access Tokens – ចុចលើ Fine-grained tokens រួច Generate new token។
- កំណត់សំបុត្ររបស់អ្នក – បញ្ចូលសម្គាល់សម្រាប់អោយយល់ច្បាស់ កំណត់ថ្ងៃផុតកំណត់ និងជ្រើសពិទ្ធិការដែលត្រូវ (សិទ្ធិ)。 ក្នុងករណីនេះសូមធ្វើឱ្យប្រាកដថាបានបន្ថែមសិទ្ធិ Models។
- បង្កើតនិងចម្លងសំបុត្រ – ចុច Generate token ហើយប្រាកដថាចម្លងវាទុកភ្លាមៗ ព្រោះអ្នកមិនអាចមើលវាឡើងវិញទៀតទេ។

### -1- ភ្ជាប់ទៅម៉ាស៊ីនបម្រើ

យើងចាប់ផ្តើមបង្កើតអតិថិជនរបស់យើងជាលើកដំបូង៖

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // នាំចូល zod សម្រាប់បញ្ជាក់វិញ្ញាសាសមាសភាព

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

ក្នុងកូដមុននេះ យើងបាន៖

- នាំចូលបណ្ណាល័យដែលត្រូវការនៅក្នុងកម្មវិធី
- បង្កើតថ្នាក់ជាមួយសមាជិកពីរដែលគឺ `client` និង `openai` ដែលជួយគ្រប់គ្រងអតិថិជន និងទំនាក់ទំនងជាមួយ LLM ផ្ទាល់
- កំណត់រចនាសម្ព័ន្ធអនុកូល LLM របស់យើងប្រើបណ្ណាល័យ GitHub Models ដោយកំណត់ `baseUrl` ទៅកាន់ API inference

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# បង្កើតប៉ារ៉ាម៉ែត្រម៉ាស៊ីនបម្រើសម្រាប់ការតភ្ជាប់ stdio
server_params = StdioServerParameters(
    command="mcp",  # អាចអនុវត្តបាន
    args=["run", "server.py"],  # អក្ខរកម្មបញ្ជា ជាជម្រើស
    env=None,  # អថេរព័ន្ធបរិស្ថាន ជាជម្រើស
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ចាប់ផ្តើមការតភ្ជាប់
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

ក្នុងកូដមុននេះ យើងបាន៖

- នាំចូលបណ្ណាល័យដែលត្រូវការសម្រាប់ MCP
- បង្កើតអតិថិជន

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

ចាប់ផ្តើមអ្នកត្រូវបន្ថែមការទំនាក់ទំនង LangChain4j ទៅឯកសារ `pom.xml` របស់អ្នក។ បន្ថែមការទាក់ទងទាំងនេះដើម្បីអនុញ្ញាតឱ្យមានការរួមបញ្ចូល MCP និង API MiniMax ដែលត្រូវគ្នា OpenAI៖

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

កំណត់កូនសោ MiniMax API របស់អ្នក និងជាជម្រើស ពីរបៀបផ្អែកសញ្ញាព្រមទាំងម៉ូដែល។
`MINIMAX_MODEL_ID` គាំទ្រ `MiniMax-M3` និង `MiniMax-M2.7`។ ប្រសិនបើ
មិនបានកំណត់ `OPENAI_BASE_URL` នោះ `MINIMAX_REGION` គាំទ្រ `global_en` និង `cn_zh`។

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ដើម្បីជ្រើសរើសទីតាំងបន្ថែមតាមតំបន់ សូមលុប `OPENAI_BASE_URL` ចេញ៖

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

បន្ទាប់មកបង្កើតថ្នាក់អតិថិជន Java របស់អ្នក៖

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

        // បង្កើតការដឹកជញ្ជូន MCP សម្រាប់ភ្ជាប់ទៅម៉ាស៊ីនមេ
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

ក្នុងកូដមុននេះ យើងបាន៖

- **បន្ថែមការទំនាក់ទំនង LangChain4j**: តម្រូវសម្រាប់ការរួមបញ្ចូល MCP និង API MiniMax ដែលត្រូវអំពី OpenAI
- **នាំចូលបណ្ណាល័យ LangChain4j**: សម្រាប់ការរួមបញ្ចូល MCP និងមុខងារ OpenAI chat
- **បង្កើត `ChatLanguageModel`**: កំណត់ប្រើ MiniMax ជាមួយកូនសោ MiniMax API របស់អ្នក ទីតាំង និងម៉ូដែលដែលគាំទ្រ
- **ដំណើរការដឹកជញ្ជូន HTTP**: ប្រើ Server-Sent Events (SSE) ដើម្បីភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP
- **បង្កើតអតិថិជន MCP**: ដែលបម្រើអ្នកក្នុងការទំនាក់ទំនងជាមួយម៉ាស៊ីនបម្រើ
- **ប្រើគាំទ្ររបស់ LangChain4j សម្រាប់ MCP**: ដែលធ្វើឱ្យរួមបញ្ចូលរវាង LLMs និងម៉ាស៊ីនបម្រើ MCP ងាយស្រួលឡើង

#### Rust

ឧទាហរណ៍នេះគិតថាអ្នកមានម៉ាស៊ីនបម្រើ MCP ហើយប្រើ Rust ដំណើរការ។ ប្រសិនបើអ្នកមិនមានទេ សូមយោងតាមមេរៀន [01-first-server](../01-first-server/README.md) ដើម្បីបង្កើតម៉ាស៊ីនបម្រើ។

ពេលអ្នកមានម៉ាស៊ីនបម្រើ MCP របស់ Rust រួចបើក-terminal ហើយទៅក្នុងថតដូចគ្នានឹងម៉ាស៊ីនបម្រើ។ បន្ទាប់មករត់ពាក្យបញ្ជាដូចខាងក្រោមដើម្បីបង្កើតគម្រោងអតិថិជន LLM ថ្មី៖

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

បន្ថែមការទំនាក់ទំនងខាងក្រោមទៅក្នុងឯកសារ `Cargo.toml` របស់អ្នក៖

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> មិនមានបណ្ណាល័យ Rust ផ្លូវការសម្រាប់ OpenAI ប៉ុន្តែក្រាត `async-openai` គឺជាបណ្ណាល័យដែលគ្រប់គ្រងដោយសហគមន៍ ([community maintained library](https://platform.openai.com/docs/libraries/rust#rust)) ដែលភាគច្រើនត្រូវបានប្រើប្រាស់។

បើកឯកសារ `src/main.rs` ហើយជំនួសមាតិកាដែលមានជាមួយកូដខាងក្រោម៖

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
    // សារស្ដាប់ដំបូង
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // ការតំឡើងអ្នកប្រើ OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ការតំឡើងអ្នកប្រើ MCP
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

    // TODO: ការពិភាក្សា LLM ជាមួយការហៅឧបករណ៍

    Ok(())
}
```

កូដនេះកំណត់កម្មវិធី Rust មូលដ្ឋានដែលនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP និង GitHub Models សម្រាប់ប្រតិបត្តិការជាមួយ LLM។

> [!IMPORTANT]
> សូមប្រាកដថា​បានកំណត់អថេរ​បរិស្ថាន `OPENAI_API_KEY` ជាមួយសំបុត្រ GitHub របស់អ្នក មុនដំណើរការកម្មវិធី។

អស្ចារ្យ ជំហានបន្ទាប់របស់យើង គឺចុះបញ្ជីសមត្ថភាពនៅលើម៉ាស៊ីនបម្រើ។

### -2- ចុះបញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ

ឥឡូវនេះ យើងនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ ហើយសួរពីសមត្ថភាពរបស់វា៖

#### Typescript

ក្នុងថ្នាក់ដូចគ្នា បន្ថែមមុខងារខាងក្រោម៖

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

Dalam kode sebelumnya kami telah:

- បន្ថែមកូដសម្រាប់ភ្ជាប់ទៅម៉ាស៊ីនបម្រើ `connectToServer`។
- បង្កើតមុខងារ `run` ដែលមានភារកិច្ចគ្រប់គ្រងចរន្តកម្មវិធី។ ដល់ពេលនេះ វាបង្ហាញតែបញ្ជីឧបករណ៍ ប៉ុន្តែយើងនឹងបន្ថែមទៀតក្នុងពេលឆាប់ខាងមុខ។

#### Python

```python
# បញ្ចីធនធានដែលមាន
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# បញ្ចីឧបករណ៍ដែលមាន
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

នេះជាចំណុចដែលយើងបានបន្ថែម៖

- បញ្ជីធនធាន និងឧបករណ៍រួចបោះពុម្ពពួកវា។ សម្រាប់ឧបករណ៍យើងក៏បញ្ជី `inputSchema` ដែលយើងប្រើក្រោយ។

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


នៅក្នុងកូដមុននេះ យើងបាន៖

- រាយបញ្ជីឧបករណ៍ដែលអាចប្រើបាននៅលើម៉ាស៊ីនមេ MCP
- សម្រាប់ឧបករណ៍នីមួយៗ រាយបញ្ជីឈ្មោះ ការពិពណ៌នា និងស្កីម៉ារបស់វា។ អ្វីខាងក្រោយគឺជាអ្វីដែលយើងនឹងប្រើដើម្បីហៅឧបករណ៍នៅពេលខាងមុខ។

#### Java

```java
// បង្កើតអ្នកផ្គត់ផ្គង់ឧបករណ៍ដែលរកឃើញឧបករណ៍ MCP ដោយស្វ័យប្រវត្តិ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// អ្នកផ្គត់ផ្គង់ឧបករណ៍ MCP ហៅប្រើប្រាស់ដោយស្វ័យប្រវត្តិ:
// - រាយនាមឧបករណ៍ដែលមានពីម៉ាស៊ីនមេ MCP
// - បម្លែងស្កីម៉ា​ឧបករណ៍ MCP ទៅទ្រង់ទ្រាយ LangChain4j
// - គ្រប់គ្រងការប្រតិបត្ដិឧបករណ៍ និងចម្លើយ
```

នៅក្នុងកូដមុននេះ យើងបាន៖

- បង្កើត `McpToolProvider` ដែលស្វែងរក និងចុះបញ្ជីសម្ភារៈទាំងអស់ពីម៉ាស៊ីនមេ MCP ដោយស្វ័យប្រវត្តិ
- ជួសជុលផ្ទាល់ខ្លួនរវាងការផ្លាស់ប្តូរស្កីម៉ាឧបករណ៍ MCP និងទ្រង់ទ្រាយឧបករណ៍ LangChain4j's នៅខាងក្នុង
- វិធីសាស្រ្តនេះសំដែងការចំរូងបន្ទុកចេញពីការរាយបញ្ជី និងដំណើរការផ្លាស់ប្តូរឧបករណ៍ដោយដៃ

#### Rust

ការទាញយកឧបករណ៍ពីម៉ាស៊ីនមេ MCP ត្រូវបានអនុវត្តដោយប្រើវិធីសាស្រ្ត `list_tools`។ នៅក្នុងមុខងារ `main` របស់អ្នក បន្ទាប់ពីកំណត់ឡើងអ្នកអតិថិជន MCP សូមបន្ថែមកូដដូចខាងក្រោម៖

```rust
// ទទួលបានបញ្ជីឧបករណ៍ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- បម្លែងសមត្ថភាពម៉ាស៊ីនមេទៅជាឧបករណ៍ LLM

ជំហានបន្ទាប់បន្ទាប់ពីរាយបញ្ជីសមត្ថភាពម៉ាស៊ីនមេគឺបម្លែងវាទៅជាទ្រង់ទ្រាយដែល LLM យល់ដឹង។ ពេលដែលយើងបានធ្វើវា យើងអាចផ្ដល់សមត្ថភាពទាំងនេះជាឧបករណ៍ដល់ LLM របស់យើង។

#### TypeScript

1. បន្ថែមកូដខាងក្រោមដើម្បីបម្លែងការឆ្លើយតបពីម៉ាស៊ីនមេ MCP ទៅទ្រង់ទ្រាយឧបករណ៍ដែល LLM អាចប្រើបាន៖

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // បង្កើតស្គីម៉ា zod ពិចារណាតាម input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // កំណត់ប្រភេទជាប្រភេទ "function" อย่างชัดเจน
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

    កូដខាងលើយកការឆ្លើយតបពីម៉ាស៊ីនមេ MCP ហើយបម្លែងវាទៅជាទ្រង់ទ្រាយកំណត់ឧបករណ៍ដែល LLM អាចយល់បាន។

2. អ្នកកំណត់ធ្វើបច្ចុប្បន្នភាពមុខងារ `run` ដើម្បីរាយបញ្ជីសមត្ថភាពម៉ាស៊ីនមេ:

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

    នៅក្នុងកូដមុននេះ យើងបានធ្វើបច្ចុប្បន្នភាពមុខងារ `run` ដើម្បីម៉ាប់តាមលទ្ធផល ហើយសម្រាប់ចំណុចនីមួយៗហៅ `openAiToolAdapter`។

#### Python

1. ជំហានដំបូង បង្កើតមុខងារបម្លែងដូចខាងក្រោម

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

    នៅក្នុងមុខងារខាងលើ `convert_to_llm_tools` យើងយកចម្លើយរបស់ឧបករណ៍ MCP ហើយបម្លែងវាទៅជាទ្រង់ទ្រាយដែល LLM អាចយល់។

2. បន្ទាប់មក អ្នកកំណត់ប្រតិបត្តិការ client របស់យើងដើម្បីប្រើមុខងារនេះដូចខាងក្រោម:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    នៅទីនេះ យើងបានបន្ថែមការហៅទៅ `convert_to_llm_tool` ដើម្បីបម្លែងចម្លើយឧបករណ៍ MCP ទៅអ្វីដែលអាចផ្ដល់ទៅ LLM ក្រោយ។

#### .NET

1. បន្ថែមកូដដើម្បីបម្លែងចម្លើយឧបករណ៍ MCP ទៅអ្វីដែល LLM អាចយល់បាន

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

នៅក្នុងកូដមុននេះ យើងបាន៖

- បង្កើតមុខងារ `ConvertFrom` ដែលទទួលឈ្មោះ ការពិពណ៌នា និងស្កីម៉ាចូល
- កំណត់មុខងារកំណត់ដែលបង្កើត FunctionDefinition ដែលត្រូវផ្ញើទៅ ChatCompletionsDefinition។ អ្វីខាងក្រោយគឺជាអ្វីដែល LLM អាចយល់បាន។

2. យើងមកមើលពីរបៀបកំណត់កូដដែលមានស្រាប់ឲ្យប្រើប្រាស់មុខងារខាងលើនេះ៖

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
// បង្កើតចំណុចប្រទាក់ Bot សម្រាប់ការប្រាស្រ័យទាក់ទងភាសាធម្មជាតិ
public interface Bot {
    String chat(String prompt);
}

// កំណត់រចនាសម្ព័ន្ធសេវា AI ជាមួយឧបករណ៍ LLM និង MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

នៅក្នុងកូដមុននេះ យើងបាន៖

- កំណត់អ៊ីនធើហ្វេស `Bot` ងាយស្រួលសម្រាប់អន្តរកម្មភាសាប្រកបដោយធម្មជាតិ
- ប្រើ LangChain4j's `AiServices` ដើម្បីភ្ជាប់ LLM ជាមួយអ្នកផ្គត់ផ្គង់ឧបករណ៍ MCP ដោយស្វ័យប្រវត្តិ
- បណ្តាញ ធ្វើដំណើរការផ្លាស់ប្តូរស្កីម៉ាឧបករណ៍ និងហៅមុខងារខាងក្រោយដោយស្វ័យប្រវត្តិ
- វិធីសាស្រ្តនេះ លុបបំបាត់ការផ្លាស់ប្តូរឧបករណ៍ដោយដៃ - LangChain4j ជួយគ្រប់គ្រងភាពស្មុគស្មាញទាំងអស់ក្នុងការបម្លែងឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែលអាចប្រើបានជាមួយ LLM

#### Rust

ដើម្បីបម្លែងចម្លើយឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែល LLM អាចយល់បាន យើងនឹងបន្ថែមមុខងារជំនួយមួយដែលរៀបចំការរាយបញ្ជីឧបករណ៍។ សូមបន្ថែមកូដខាងក្រោមទៅក្នុងឯកសារ `main.rs` របស់អ្នកក្រោមមុខងារ `main`។ នេះនឹងត្រូវហៅនៅពេលធ្វើសំណើទៅ LLM៖

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

ល្អមែន យើងមិនទាន់រៀបចំឲ្យដំណើរការសំណើរអ្នកប្រើបានទេ ដូច្នេះយើងនឹងដោះស្រាយវាក្រោយ។

### -4- គ្រប់គ្រងសំណើបញ្ញាតម្លៃរបស់អ្នកប្រើ

នៅផ្នែកនេះនៃកូដ យើងនឹងគ្រប់គ្រងសំណើររបស់អ្នកប្រើ។

#### TypeScript

1. បញ្ចូលមុខងារមួយដែលនឹងត្រូវប្រើសម្រាប់ហៅ LLM របស់យើង៖

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. ហៅឧបករណ៍របស់ម៉ាស៊ីនបម្រើ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. ធ្វើអ្វីមួយជាមួយលទ្ធផល
        // ត្រូវធ្វើ

        }
    }
    ```

    នៅក្នុងកូដមុននេះ យើងបាន៖

    - បន្ថែមមុខងារ `callTools`។
    - មុខងារនេះទទួលបានចម្លើយ LLM ហើយពិនិត្យមើលថាតើមានឧបករណ៍ណាដែលត្រូវហៅដែរ ប្រសិនបើមាន៖

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ហៅឧបករណ៍
        }
        ```

    - ហៅឧបករណ៍ មួយប្រសិនបើ LLM បង្ហាញថាត្រូវហៅវា៖

        ```typescript
        // ២។ ហៅឧបករណ៍របស់ម៉ាស៊ីនបម្រើ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ៣។ ធ្វើបច្ចុប្បន្នភាពមួយជាមួយលទ្ធផល
        // ត្រូវធ្វើសកម្មភាព
        ```

2. បច្ចុប្បន្នភាពមុខងារ `run` ដើម្បីរួមបញ្ចូលការហៅទៅ LLM និងហៅ `callTools`:

    ```typescript

    // 1. បង្កើតសារដែលជាការបញ្ចូលសម្រាប់ LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. ហៅ LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. ឆ្លើយតបនឹង LLM សម្រាប់ជម្រើសនីមួយៗ ពិនិត្យមើលថាតើមានហៅឧបករណ៍ឬទេ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ល្អ មករាយបញ្ជីកូដទាំងមូល៖

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // នាំចូល zod សម្រាប់ការផ្ទៀងផ្ទាត់ schema

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ប្រហែលជាត្រូវការផ្លាស់ប្តូរទៅ URL នេះនៅអនាគត: https://models.github.ai/inference
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
          // បង្កើត schema zod dựa trên input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // កំណត់ប្រភេទឲ្យច្បាស់ទៅ "function"
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
    
    
          // 2. ហៅឧបករណ៍របស់ម៉ាស៊ីនបម្រើ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ធ្វើបរិយាកាសជាមួយលទ្ធផល
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
    
        // 3. ឆ្លងកាត់ចម្លើយ LLM, សម្រាប់ជម្រើសនីមួយៗ ពិនិត្យមើលថាតើវាមានការហៅឧបករណ៍ឬអត់
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

1. បន្ថែមការនាំចូលខ្លះៗដែលត្រូវការសម្រាប់ហៅ LLM

    ```python
    # llm
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

    នៅក្នុងកូដមុននេះ យើងបាន៖

    - ផ្ដល់មុខងាររបស់យើង ដែលយើងបានរកឃើញនៅលើម៉ាស៊ីនមេ MCP និងបានបម្លែងទៅ LLM។
    - បន្ទាប់មកយើងហៅ LLM ជាមួយមុខងារនោះ។
    - បន្ទាប់មក យើងពិនិត្យលទ្ធផលមើលថាមុខងារណាដែលយើងគួរហៅ ប្រសិនបើមាន។
    - ចុងក្រោយ យើងផ្ដល់មើលអារេមុខងារដែលត្រូវហៅ។

3. ជំហានចុងក្រោយ អ្នកកំណត់កូដ `main` របស់យើង៖

    ```python
    prompt = "Add 2 to 20"

    # សួរអោយ LLM ថាជា​ឧបករណ៍​អ្វី​ដែល​គ្រប់គ្នា ប្រសិនបើ​មាន
    functions_to_call = call_llm(prompt, functions)

    # ហៅ​មុខងារ​ដែល​បានស្នើ​​​ផ្តល់អនុសាសន៍
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    នៅទីនោះ គឺជាជំហានចុងក្រោយ ក្នុងកូដខាងលើនេះ យើងបាន៖

    - ហៅឧបករណ៍ MCP តាមរយៈ `call_tool` ដោយប្រើមុខងារដែល LLM គិតថាយើងគួរហៅដោយផ្អែកលើបញ្ញាតិរបស់យើង។
    - បោះពុម្ពលទ្ធផលនៃការហៅឧបករណ៍ទៅម៉ាស៊ីនមេ MCP។

#### .NET

1. មកមើលកូដខ្លះសម្រាប់ធ្វើសំណើបញ្ញាតម្លៃ LLM៖

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

    នៅក្នុងកូដមុននេះ យើងបាន៖

    - ទាញយកឧបករណ៍ពីម៉ាស៊ីនមេ MCP, `var tools = await GetMcpTools()`
    - កំណត់បញ្ញាតម្លៃអ្នកប្រើ `userMessage`
    - បង្កើតអ объект options កំណត់ម៉ូឌែល និងឧបករណ៍
    - ដាក់សំណើទៅ LLM

2. ជំហានចុងក្រោយ មកមើលថាតើ LLM គិតថាយើងគួរហៅមុខងារមួយឬទេ:

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

    នៅក្នុងកូដមុននេះ យើងបាន៖

    - លូបតាមបញ្ជីហៅមុខងារ
    - សម្រាប់ការហៅឧបករណ៍នីមួយៗ បំបែកឈ្មោះ និងអាគុយម៉ង់ ហើយហៅឧបករណ៍នៅម៉ាស៊ីនមេ MCP ការប្រើ MCP client។ ចុងក្រោយយើងបោះពុម្ពលទ្ធផល។

នេះគឺជាកូដទាំងមូល៖

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
    // ប្រតិបត្តិការសំណើភាសាប្រើប្រាស់ធម្មជាតិនាដោយស្វ័យប្រវត្តិដែលប្រើឧបករណ៍ MCP
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

នៅក្នុងកូដមុននេះ យើងបាន៖

- ប្រើបញ្ញាតម្លៃភាសាប្រកបដោយធម្មជាតិដ៏ងាយស្រួលដើម្បីអន្តរកម្មជាមួយឧបករណ៍ម៉ាស៊ីនមេ MCP
- ស៊ុមបន្ទាត់ LangChain4j ធ្វើដំណើរការខាងក្រោយដោយស្វ័យប្រវត្តិ៖
  - បម្លែងបញ្ញាតម្លៃអ្នកប្រើទៅជាការហៅឧបករណ៍នៅពេលទាមទារ
  - ហៅឧបករណ៍ MCP ដែលសមស្របទៅតាមសេចក្តីសម្រេចរបស់ LLM
  - គ្រប់គ្រងដំណើរការសន្ទនារវាង LLM និងម៉ាស៊ីនមេ MCP
- មុខងារ `bot.chat()` បញ្ជូនចម្លើយភាសាប្រកបដោយធម្មជាតិនិងខ្លះអាចរួមបញ្ចូលលទ្ធផលពីការប្រតិបត្តិឧបករណ៍ MCP
- វិធីសាស្រ្តនេះផ្ដល់បទពិសោធន៍អ្នកប្រើប្រាស់ដ៏រលូន ដូច្នេះអ្នកប្រើមិនចាំបាច់ដឹងអំពីការអនុវត្ត MCP ខាងក្រោមទេ

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


នេះគឺជាកន្លែងដែលការងារ​ចម្បង​ត្រូវបាន​ដំណើរការ។ យើងនឹងហៅ LLM ជាមួយសំណើដំបូង​របស់អ្នកប្រើ បន្ទាប់មកដំណើរការឆ្លើយតប ដើម្បីពិនិត្យមើលថាតើត្រូវហៅ​ឧបករណ៍ណាមួយទេឬអត់។ បើពិត ត្រូវហៅឧបករណ៍ទាំងនោះ ហើយបន្តការសន្ទនាជាមួយ LLM រហូតដល់គ្មានការហៅឧបករណ៍បន្ថែម ហើយយើងបានឆ្លើយតបទូទៅ។

យើងនឹងហៅ LLM ជាច្រើនដង ដូច្នេះត្រូវកំណត់មុខងារមួយដើម្បីគ្រប់គ្រងការហៅ LLM។ បន្ថែមមុខងារ​ខាងក្រោមទៅឯកសារ `main.rs` របស់អ្នក៖

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

មុខងារនេះទទួលយក client LLM បញ្ជីសារជាមួយសំណើប្រើ អ្នករចនាគ្រឿងចក្រ MCP server ហើយផ្ញើសំណើទៅ LLM បន្ទាប់មកតបស្នើ។

ផលបត់តបពី LLM នឹងមាន​អារេ​នៃ `choices`។ យើងត្រូវដំណើរការភាពលទ្ធផល ដើម្បីមើលថាតើមាន `tool_calls` ឬអត់។ វាបញ្ជាក់ថា LLM កំពុងស្នើឲ្យហៅឧបករណ៍ពិសេសមួយជាមួយអាគុយម៉ង់។ បន្ថែមកូដខាងក្រោមទៅចុងឯកសារ `main.rs` របស់អ្នក ដើម្បីកំណត់មុខងារដែលគ្រប់គ្រងការឆ្លើយតប LLM៖

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

    // បង្ហាញមាតិកាប្រសិនបើមាន
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // គ្រប់គ្រងការហៅឧបករណ៍
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // បន្ថែមសារជំនួយការ

        // ប្រតិបត្តិការហៅឧបករណ៍នីមួយៗ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // បន្ថែមលទ្ធផលឧបករណ៍ទៅក្នុងសារទាំងអស់
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // បន្តការពិភាក្សាជាមួយលទ្ធផលឧបករណ៍
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

ប្រសិនបើមាន `tool_calls` វាដកយកព័ត៌មានឧបករណ៍ ហៅ MCP server ជាមួយសំណើឧបករណ៍ ក៏ដាក់លទ្ធផលទៅសារសន្ទនា។ បន្ទាប់មកបន្តសន្ទនាជាមួយ LLM ហើយប្រសាសន៍ត្រូវបានបន្តដោយការឆ្លើយតបរបស់ជំនួយការនិងលទ្ធផលរបស់ការហៅឧបករណ៍។

ដើម្បីដកយកព័ត៌មានហៅឧបករណ៍ដែល LLM តបសម្រាប់ករណីហៅ MCP យើងនឹងបន្ថែមមុខងារជំនួយមួយទៀត ដើម្បីដកយកអ្វីដែលចាំបាច់សម្រាប់ហៅ។ បន្ថែមកូដខាងក្រោមទៅចុងឯកសារ `main.rs` របស់អ្នក៖

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

ជាមួយការតំឡើងគ្រប់ផ្នែកទាំងអស់នេះ ឥឡូវនេះយើងអាចគ្រប់គ្រងសំណើដំបូងរបស់អ្នកប្រើ ហើយហៅ LLM បាន។ បន្តកែលម្អមុខងារ `main` របស់អ្នក ដើម្បីរួមបញ្ចូលកូដខាងក្រោម៖

```rust
// ពីរបាំ LLM ជាមួយការហៅឧបករណ៍
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

វានឹងសួរ LLM ជាមួយសំណើដំបូងរបស់អ្នកប្រើសុំបន្ថែមគ្នារវាងលេខពីរមុខ ហើយវានឹងដំណើរការឆ្លើយតបទាំងស្រុងដើម្បីគ្រប់គ្រងការហៅឧបករណ៍យ៉ាងវាយតម្លៃ។

អស្ចារ្យ អ្នកបានធ្វើវាសម្រេច!

## កិច្ចការនៃការសិក្សា

ត្រូវយកកូដពីលំហាត់ហើយបង្កើតម៉ាស៊ីនបម្រើជាមួយឧបករណ៍បន្ថែមផ្សេងទៀត។ បន្ទាប់មកបង្កើត client ជាមួយ LLM ដូចក្នុងលំហាត់ ហើយសាកល្បងជាមួយសំណើដែកផ្សេងៗ ដើម្បីធានាថា​ឧបករណ៍ម៉ាស៊ីនបម្រើទាំងអស់ត្រូវបានហៅដោយមានសុីវិល័យ។ វិធីសាស្រ្តបង្កើត client នេះអោយអ្នកប្រើមានបទពិសោធន៍ល្អ ដោយអាចប្រើសំណើរម៉ូតា ផ្ទុយពីការបញ្ជា client រឹងគ្មានការយល់ដឹងពី MCP server ដែលត្រូវហៅ។

## ដំណោះស្រាយ

[ដំណោះស្រាយ](./solution/README.md)

## ចំណុចសំខាន់ដែលទទួលបាន

- ការបន្ថែម LLM ទៅ client របស់អ្នកផ្តល់វិធីល្អសម្រាប់អ្នកប្រើក្នុងការប្រើប្រាស់ MCP Servers។
- អ្នកត្រូវបម្លែងចម្លើយពី MCP Server ទៅបែបដែល LLM អាចយល់បាន។

## ឧទាហរណ៍

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ប្រភពព័ត៍មានបន្ថែម

## ជំហានបន្ទាប់

- បន្ទាប់៖ [ប្រើម៉ាស៊ីនបម្រើជាមួយ Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->