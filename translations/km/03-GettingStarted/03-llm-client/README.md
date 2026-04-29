# បង្កើត client ជាមួយ LLM

ដូចដែលអ្នកបានឃើញរហូតមកនេះ អ្នកបានឃើញពីរបៀបបង្កើតម៉ាស៊ីនបម្រើ និង client ។ Client បានអាចហៅម៉ាស៊ីនបម្រើជាតំណាងដើម្បីបង្ហាញបញ្ជីឧបករណ៍ វត្ថុធនធាន និងស្នើសុំ។ ទោះជាយ៉ាងណាក៏ដោយ វាគឺមិនមែនជាវិធីដែលមានប្រយោជន៍ខ្លាំងទេ។ អ្នកប្រើប្រាស់របស់អ្នករស់នៅក្នុងយុគសម័យភ្នាក់ងារ agentic ហើយរំពឹងថានឹងប្រើស្នើសុំ និងទំនាក់ទំនងជាមួយ LLM ជំនួស។ ពួកគេមិនខ្វល់ថាតើអ្នកប្រើ MCP ដើម្បីផ្ទុកសមត្ថភាពរបស់អ្នក ឬពុំមែនទេ ពួកគេខំរង់ចាំក្នុងការតភ្ជាប់ប្រើភាសាធម្មជាតិរបស់មនុស្ស។ តើយើងត្រូវដោះស្រាយដូចម្តេច? ដំណោះស្រាយគឺបន្ថែម LLM ទៅ client។

## ទិដ្ឋភាពទូទៅ

ក្នុងមេរៀននេះយើងផ្តោតលើការបន្ថែម LLM ទៅ client របស់អ្នក និងបង្ហាញពីរបៀបដែលវាផ្តល់បទពិសោធដោយប្រសើរជាងសម្រាប់អ្នកប្រើប្រាស់។

## គោលបំណងរៀន

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- បង្កើត client ជាមួយ LLM។
- ទំនាក់ទំនងដោយរលូនជាមួយម៉ាស៊ីនបម្រើ MCP ដោយប្រើ LLM។
- ផ្តល់បទពិសោធន៍ប្រើប្រាស់ល្អជាងសម្រាប់អ្នកប្រើក្រោយ client។

## វិធីសាស្ត្រ

សូមយល់ដឹងវិធីសាស្ត្រដែលយើងត្រូវយក។ ការបន្ថែម LLM សម្លេងមើលទៅសាមញ្ញ ប៉ុន្តើយើងពិតៗត្រូវធ្វើដូចនេះឬ? 

នេះជារបៀប client នឹងទំនាក់ទំនងជាមួយម៉ាស៊ីនបម្រើ៖

1. បង្កើតការតភ្ជាប់ជាមួយម៉ាស៊ីនបម្រើ។

1. បញ្ជីសមត្ថភាព ស្នើសុំ វត្ថុធនធាន និងឧបករណ៍ ហើយរក្សាទុកផែនទីរបស់ពួកវា។

1. បន្ថែម LLM ហើយផ្តល់សមត្ថភាពដែលបានរក្សាទុក និងផែនទីរបស់ពួកវាជារបៀបដែល LLM យល់។

1. ឆ្លើយតបទៅនឹងស្នើសុំអ្នកប្រើដោយបញ្ជូនវាទៅ LLM រួមជាមួយឧបករណ៍ដែលបានបញ្ជីដោយ client។

ល្អ ប៉ុន្តែនៅពេលយើងយល់រួចទេពីរបៀបទូទៅ ប្រសិនចង់ចាប់ផ្តើមសាកល្បងនោះមកសាកល្បងនៅលើហាត់ប្រាណខាងក្រោម។

## ហាត់ប្រាណ៖ បង្កើត client ជាមួយ LLM

ក្នុងហាត់ប្រាណនេះយើង​នឹងរៀនបន្ថែម LLM ទៅ client របស់យើង។

### អះអាងភាពតាមរយៈ Token ផ្ទាល់ខ្លួន GitHub

ការបង្កើត token GitHub គឺជាដំណើរការងាយស្រួល។ នេះជារបៀបដែលអ្នកអាចធ្វើបាន៖

- ទៅកាន់ GitHub Settings – ចុចរូបតំណាងប្រវត្តិរូបនៅកំពូលកែងស្ដាំ រួចជ្រើស Settings។
- ទៅកាន់ Developer Settings – រំកិលចុះក្រោម ហើយចុច Developer Settings។
- ជ្រើស Personal Access Tokens – ចុច Fine-grained tokens រួចចុច Generate new token។
- កំណត់ Token របស់អ្នក – បន្ថែមសម្គាល់សម្រាប់យោង កំណត់កាលបរិច្ឆេទផុតកំណត់ ហើយជ្រើសរើសសិទ្ធិដែលចាំបាច់ (permissions)។ ក្នុងករណីនេះ ត្រូវប្រាកដថាបន្ថែមសិទ្ធិ Models។
- បង្កើត ហើយចម្លង Token – ចុច Generate token ហើយប្រាកដចម្លងភ្លាម ព្រោះអ្នកមិនអាចមើលវាម្តងទៀតបានទេ។

### -1- តភ្ជាប់ទៅម៉ាស៊ីនបម្រើ

សូមបង្កើត client របស់យើងជាមុន៖

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // នាំចូល zod សម្រាប់ផ្ទៀងផ្ទាត់សណ្ឋាន

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

ក្នុងកូដខាងលើ យើងបាន៖

- យកបណ្ណាល័យដែលចាំបាច់
- បង្កើតថ្នាក់មួយមានសមាសភាគពីរគឺ `client` និង `openai` ដែលជួយគ្រប់គ្រង client និងទំនាក់ទំនងជាមួយ LLM យ៉ាងស្រួល។
- កំណត់ instance របស់ LLM ដើម្បីប្រើ GitHub Models ដោយកំណត់ `baseUrl` តាម API inference។

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# បង្កើតប៉ារ៉ាម៉ែត IV សម្រាប់ការតភ្ជាប់ stdio
server_params = StdioServerParameters(
    command="mcp",  # ឯកសារដំណើរការ
    args=["run", "server.py"],  # ប៉ារ៉ាម៉ែតបញ្ជាកម្មបន្ទាត់បន្ថែម
    env=None,  # ខណៈការបរិបទបរិយាកាសជាជម្រើស
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

ក្នុងកូដខាងលើ យើងបាន៖

- យកបណ្ណាល័យដែលចាំបាច់សម្រាប់ MCP
- បង្កើត client មួយ

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

ជាពិសេស អ្នកត្រូវបន្ថែម LangChain4j dependencies ទៅក្នុង `pom.xml` របស់អ្នក។ បន្ថែម dependencies ទាំងនេះដើម្បីអាចធ្វើ MCP integration និងគាំទ្រ GitHub Models៖

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

បន្ទាប់មក បង្កើតថ្នាក់ client Java របស់អ្នក៖

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
    
    public static void main(String[] args) throws Exception {        // កំណត់រចនាសម្ព័ន្ធ LLM ដើម្បីប្រើម៉ូឌែល GitHub
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // បង្កើតការដឹកជញ្ជូន MCP សម្រាប់ភ្ជាប់ទៅម៉ាស៊ីនបម្រើ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // បង្កើតអ្នកប្រើ MCP
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

ក្នុងកូដខាងលើ យើងបាន៖

- **បន្ថែម LangChain4j dependencies**៖ ជាចាំបាច់សម្រាប់ MCP integration, client ផ្លូវការរបស់ OpenAI, និងគាំទ្រ GitHub Models
- **យកបណ្ណាល័យ LangChain4j**៖ សម្រាប់ការបញ្ចូល MCP និងមូឌែលសន្ទនារ OpenAI
- **បង្កើត ChatLanguageModel**៖ កំណត់ឱ្យប្រើ GitHub Models ជាមួយសំបុត្ររបស់ GitHub របស់អ្នក
- **កំណត់ការដឹកជញ្ជូន HTTP**៖ ប្រើ Server-Sent Events (SSE) ដើម្បីភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP
- **បង្កើត MCP client**៖ ដែលគ្រប់គ្រងការទំនាក់ទំនងជាមួយម៉ាស៊ីនបម្រើ
- **ប្រើគាំទ្រលំនាំដើមរបស់ LangChain4j សម្រាប់ MCP**៖ ដែលធ្វើឱ្យការរួមបញ្ចូលរវាង LLM និងម៉ាស៊ីនបម្រើ MCP រលូនជាងមុន

#### Rust

ឧទាហរណ៍នេះសន្មតថាអ្នកមានម៉ាស៊ីនបម្រើ MCP ដែលផ្ដល់សេវាលើ Rust រួចហើយ។ ប្រសិនបើមិនមាន សូមយោងត្រលប់ទៅមេរៀន [01-first-server](../01-first-server/README.md) ដើម្បីបង្កើតម៉ាស៊ីនបម្រើ។

ពេលដែលមានម៉ាស៊ីនបម្រើ MCP Rust រួចហើយ បើក terminal ហើយចូលទៅថតដូចម៉ាស៊ីនបម្រើ រួចបញ្ចូលពាក្យបញ្ជាខាងក្រោមដើម្បីបង្កើត project client LLM ថ្មី៖

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

បន្ថែម dependencies ខាងក្រោមទៅក្នុងឯកសារ `Cargo.toml` របស់អ្នក៖

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> មិនមានបណ្ណាល័យផ្លូវការរបស់ Rust សម្រាប់ OpenAI ទេ ទោះជាយ៉ាងណា `async-openai` crate គឺជាបណ្ណាល័យដែលគ្រប់គ្រងដោយសហគមន៍ ([community maintained library](https://platform.openai.com/docs/libraries/rust#rust)) ដែលត្រូវបានប្រើជាញឹកញាប់។

បើកឯកសារ `src/main.rs` ហើយជំនួសខ្លឹមសាររបស់វាដោយកូដខាងក្រោម៖

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

    // ការតំឡើងអតិថិជន OpenAI
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // ការតំឡើងអតិថិជន MCP
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

    // TODO: ទទួលយកបញ្ជីឧបករណ៍ MCP

    // TODO: ការសន្ទនាដោយ LLM ជាមួយការហៅឧបករណ៍

    Ok(())
}
```

កូដនេះកំណត់កម្មវិធី Rust សាមញ្ញមួយដែលនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP និង GitHub Models សម្រាប់ទំនាក់ទំនង LLM។

> [!IMPORTANT]
> សូមប្រាកដថាត្រូវកំណត់ environment variable `OPENAI_API_KEY` ជាមួយសំបុត្ររបស់ GitHub មុនចាប់ផ្តើមកម្មវិធី។

ល្អ សម្រាប់ជំហានបន្ទាប់ យើងត្រូវបញ្ជីសមត្ថភាពនៅលើម៉ាស៊ីនបម្រើ។

### -2- បញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ

ឥឡូវនេះ យើងនឹងភ្ជាប់ទៅម៉ាស៊ីនបម្រើ ហើយស្នើរសុំសមត្ថភាពរបស់វា៖

#### Typescript

ក្នុងថ្នាក់ដដែលនេះ បន្ថែមវិធីសាស្ត្រខាងក្រោម៖

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // រាយបញ្ជីឧបករណ៍
    const toolsResult = await this.client.listTools();
}
```

ក្នុងកូដខាងលើ យើងបាន៖

- បន្ថែមកូដសម្រាប់ភ្ជាប់ទៅម៉ាស៊ីនបម្រើ `connectToServer`
- បង្កើតវិធីសាស្ត្រ `run` ដែលទទួលបន្ទុកលំហូរកម្មវិធី។ ដល់ពេលនេះ វាទើបតែបញ្ជីឧបករណ៍ ប៉ុន្តាយើងនឹងបន្ថែមទៀតនៅពេលក្រោយ។

#### Python

```python
# បញ្ជីធនធានដែលមានស្រាប់
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# បញ្ជីឧបករណ៍ដែលមានស្រាប់
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

នេះគឺជារឿងដែលយើងបានបន្ថែម៖

- បញ្ជីវត្ថុធនធាន និងឧបករណ៍ ហើយបោះពុម្ពវាទៅ។ សម្រាប់ឧបករណ៍ យើងក៏បញ្ជី `inputSchema` ដែលយើងប្រើក្រោយ។

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

ក្នុងកូដខាងលើ យើងបាន៖

- បញ្ជីឧបករណ៍ដែលមាននៅលើម៉ាស៊ីនបម្រើ MCP
- សម្រាប់ឧបករណ៍នីមួយៗ បញ្ជីឈ្មោះ ការពិពណ៌នា និងផែនទីរបស់វា។ ពួកនេះគឺអ្វីដែលយើងនឹងប្រើដើម្បីហៅឧបករណ៍ភ្លាមៗ។

#### Java

```java
// បង្កើតអ្នកផ្តល់ឧបករណ៍ដែលស្វែងរកឧបករណ៍ MCP ដោយស្វayani
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// អ្នកផ្តល់ឧបករណ៍ MCP ដឹកនាំដោយស្វ័យប្រវត្តិ៖
// - បញ្ជីឧបករណ៍ដែលមានពីម៉ាស៊ីនមេ MCP
// - បម្លែងគ្រោងសchemaឧបករណ៍ MCP ទៅទ្រង់ទ្រាយ LangChain4j
// - គ្រប់គ្រងការប្រតិបត្តិឧបករណ៍ និងចម្លើយ
```

ក្នុងកូដខាងលើ យើងបាន៖

- បង្កើត `McpToolProvider` ដែលស្វ័យប្រវត្តិស្វែងរក និងចុះបញ្ជីឧបករណ៍ទាំងអស់ពីម៉ាស៊ីនបម្រើ MCP
- កម្មវិធីផ្គត់ផ្គង់ឧបករណ៍គ្រប់គ្រងការបម្លែងគ្នារវាងផែនទីឧបករណ៍ MCP និងលំនាំឧបករណ៍ LangChain4j ក្រៅផ្ទៃ
- វិធីសាស្ត្រនេះគឺបិទខ្ទប់ពីការបញ្ជី និងបម្លែងឧបករណ៍ដោយដៃ

#### Rust

ការទាញយកឧបករណ៍ពីម៉ាស៊ីនបម្រើ MCP ត្រូវបានបំពេញដោយវិធីសាស្ត្រ `list_tools`។ ក្នុងមុខងារ `main` របស់អ្នក បន្ទាប់ពីកំណត់ MCP client សូមបន្ថែមកូដខាងក្រោម៖

```rust
// ទទួលបានបញ្ជីឧបករណ៍ MCP
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- បម្លែងសមត្ថភាពម៉ាស៊ីនបម្រើទៅឧបករណ៍ LLM

ជំហានបន្ទាប់ បន្ទាប់ពីបញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ គឺបម្លែងវាទៅទ្រង់ទ្រាយដែល LLM យល់។ បន្ទាប់ពីធ្វើបច្ចុប្បន្នភាព យើងអាចផ្តល់សមត្ថភាពទាំងនេះជាឧបករណ៍ទៅ LLM របស់យើងបាន។

#### TypeScript

1. បន្ថែមកូដខាងក្រោមសម្រាប់បម្លែងចម្លើយពីម៉ាស៊ីនបម្រើ MCP ទៅទ្រង់ទ្រាយឧបករណ៍ដែល LLM អាចប្រើបាន៖

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // បង្កើតស្គីម zod ដោយផ្អែកលើ input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // កំណត់ប្រភេទជាក់លាក់ទៅ "function"
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

    កូដខាងលើ ពីមួយចម្លើយមកពីម៉ាស៊ីនបម្រើ MCP នេះ បម្លែងវាទៅជាកំណត់ឧបករណ៍ដែល LLM យល់។

1. ឥឡូវសុំធ្វើបច្ចុប្បន្នភាពវិធីសាស្រ្ត `run` ដើម្បីបញ្ជីសមត្ថភាពម៉ាស៊ីនបម្រើ៖

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

    ក្នុងកូដនេះ យើងបានធ្វើបច្ចុប្បន្នភាព `run` ដើម្បីផ្លាស់ប្តូរដំណើរការដំណើរការ និងសម្រាប់គ្រប់ចំណុចហៅ `openAiToolAdapter`។

#### Python

1. ជាដំបូង សូមបង្កើតមុខងារបម្លែងនេះ ៖

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

    ក្នុងមុខងារ `convert_to_llm_tools` ខាងលើ យើងយកចម្លើយឧបករណ៍ MCP ហើយបម្លែងវាទៅទ្រង់ទ្រាយដែល LLM យល់។

1. បន្ទាប់មក សូមធ្វើបច្ចុប្បន្នភាពកូដ client របស់យើង ដូចរបៀបខាងក្រោម៖

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    នៅទីនេះ យើងបន្ថែមហៅមុខងារ `convert_to_llm_tool` ដើម្បីបម្លែងចម្លើយឧបករណ៍ MCP ទៅអ្វីដែលយើងអាចផ្តល់ឲ្យ LLM នៅពេលក្រោយ។

#### .NET

1. សូមបន្ថែមកូដសម្រាប់បម្លែងចម្លើយឧបករណ៍ MCP ទៅអ្វីដែល LLM អាចយល់៖

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

ក្នុងកូដខាងលើ យើងបាន៖

- បង្កើតមុខងារ `ConvertFrom` ដែលទទួលបាន ឈ្មោះ ការពិពណ៌នា និងផែនទីបញ្ចូល។
- កំណត់មុខងារដែលបង្កើត `FunctionDefinition` ដែលផ្ញើទៅ `ChatCompletionsDefinition`។ ដែលអត្ថន័យថាជាអ្វីដែល LLM អាចយល់បាន។

1. យើងមកមើលវិធីធ្វើបច្ចុប្បន្នភាពកូដដែលមានស្រាប់ ដើម្បីប្រើប្រាស់មុខងារខាងលើ៖

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
// បង្កើតផ្ទៃចុះBotសម្រាប់ការប្រាស្រ័យទាក់ទងភាសា​ធម្មជាតិ
public interface Bot {
    String chat(String prompt);
}

// កំណត់សេវាកម្មAIជាមួយឧបករណ៍LLM និង MCP
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

ក្នុងកូដខាងលើ យើងបាន៖

- កំណត់ `Bot` interface សាមញ្ញសម្រាប់ការប្រាស្រ័យភាសាធម្មជាតិ
- ប្រើសេវាកម្ម AiServices របស់ LangChain4j ដើម្បីភ្ជាប់ LLM ជាស្វ័យប្រវត្តិ ជាមួយអ្នកផ្គត់ផ្គង់ឧបករណ៍ MCP
- ស៊ុមភាគស្វ័យប្រវត្តិគ្រប់គ្រងការបម្លែងផែនទីឧបករណ៍ និងការហៅមុខងារខាងក្រោយ
- វិធីសាស្រ្តនេះដោះស្រាយការបម្លែងឧបករណ៍ដោយដៃ - LangChain4j គ្រប់គ្រងភាពស្មុគស្មាញទាំងអស់ក្នុងការបម្លែងឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែលសមរភាពជាមួយ LLM

#### Rust

ដើម្បីបម្លែងចម្លើយឧបករណ៍ MCP ទៅទ្រង់ទ្រាយដែល LLM យល់ យើងនឹងបន្ថែមមុខងារជំនួយមួយដែលរៀបចំបញ្ជីឧបករណ៍។ សូមបន្ថែមកូដខាងក្រោមទៅក្នុងឯកសារ `main.rs` របស់អ្នកក្រោមមុខងារ `main`។ វានឹងត្រូវហៅពេលធ្វើសំណើទៅ LLM៖

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

ល្អណាស់ យើងបានរៀបចំសម្រាប់ដោះស្រាយសំណើរអ្នកប្រើរួចហើយ យើងត្រូវចាប់ផ្តើមផ្នែកនោះនៅជំហានបន្ទាប់។

### -4- ដោះស្រាយសំណើរអ្នកប្រើ

ក្នុងផ្នែកនេះនៃកូដ យើងនឹងដោះស្រាយសំណើរពីអ្នកប្រើ។

#### TypeScript

1. បន្ថែមមុខងារដែលនឹងប្រើសម្រាប់ហៅ LLM៖

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
        // ត្រូវធ្វើ

        }
    }
    ```

    ក្នុងកូដខាងលើ យើងបាន៖

    - បន្ថែមមុខងារ `callTools`។
    - មុខងារនេះទទួលបញ្ជាលទ្ធផល LLM ហើយពិនិត្យថាតើមានឧបករណ៍ណាដែលត្រូវហៅ ឬបើមិនមាន:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ហៅឧបករណ៍
        }
        ```

    - ហៅឧបករណ៍ ប្រសិនបើ LLM បង្ហាញថាត្រូវហៅវា៖

        ```typescript
        // ២. ហៅឧបករណ៍ម៉ាស៊ីនមេ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ៣. អនុវត្តអ្វីមួយជាមួយលទ្ធផល
        // ត្រូវធ្វើ
        ```

1. បច្ចុប្បន្នភាពមុខងារ `run` ដើម្បីរួមបញ្ចូលការហៅទៅ LLM និងហៅ `callTools`:

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

    // 3. ឆែកឆែកចម្លើយពី LLM សម្រាប់ជម្រើសមួយៗ ត្រួតពិនិត្យថាតើមានការហៅឧបករណ៍ទេ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ល្អ សូមបង្ហាញកូដពេញលេញ៖

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
            baseURL: "https://models.inference.ai.azure.com", // អាចត្រូវការផ្លាស់ប្តូរទៅ url នេះនៅអនាគត: https://models.github.ai/inference
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
          // បង្កើត schema zod អាស្រ័យលើ input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // កំណត់ប្រភេទជាផ្សាយថា "function"
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
    
          // 3. ធ្វើអ្វីមួយជាមួយលទ្ធផល
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
    
        // 1. ឆ្លងកាត់ចំលើយ LLM សម្រាប់ជម្រើសមួយៗ បញ្ចាក់ថាមានការហៅឧបករណ៍ឬអត់
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

1. សូមបន្ថែមការនាំចូលដែលចាំបាច់ដើម្បីហៅ LLM៖

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. បន្ទាប់មក បន្ថែមមុខងារដែលនឹងហៅ LLM៖

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

    ក្នុងកូដខាងលើ យើងបាន៖

    - ផ្ញើមុខងាររបស់យើង ដែលបានស្វែងរកលើម៉ាស៊ីនបម្រើ MCP ហើយបានបម្លែងទៅ LLM។
    - បន្ទាប់ហៅ LLM ជាមួយមុខងារដែលបានផ្ញើ។
    - ពិនិត្យផលបញ្ជាលទផលដើម្បីមើលថាមុខងារណាដែលត្រូវហៅ បើមាន។
    - ចុងក្រោយ យើងបញ្ជូនសំណុំមុខងារដើម្បីហៅ។

1. ជំហានចុងក្រោយ សូមបច្ចុប្បន្នភាពកូដដើមរបស់យើង៖

    ```python
    prompt = "Add 2 to 20"

    # សួរទៅកាន់ LLM ថា ឧបករណ៍អ្វីខ្លះដែលអាចប្រើបាន ប្រសិនបើមាន
    functions_to_call = call_llm(prompt, functions)

    # ហៅមុខងារដែលបានស្នើបន្ទាន់
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    នេះជាជំហានចុងក្រោយ ក្នុងកូដខាងលើ យើង៖

    - ហៅឧបករណ៍ MCP តាម `call_tool` ប្រើមុខងារដែល LLM គិតថាចាំបាច់ហៅដោយផ្អែកលើស្នើសុំរបស់យើង។
    - បោះពុម្ពលទ្ធផលការហៅឧបករណ៍ទៅម៉ាស៊ីនបម្រើ MCP។

#### .NET

1. សូមបង្ហាញកូដសម្រាប់ធ្វើសំណើ LLM prompt៖

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

    ក្នុងកូដខាងលើ យើងបាន៖

    - ទាញយកឧបករណ៍ពីម៉ាស៊ីនបម្រើ MCP, `var tools = await GetMcpTools()`
    - កំណត់សំណើអ្នកប្រើ `userMessage`
    - បង្កើតអុបសិនប្រ៉ាប់ specifying model និងឧបករណ៍
    - បំពេញសំណើទៅ LLM

1. ជំហានចុងក្រោយ ត្រូវមើលថាតើ LLM គិតថាត្រូវហៅមុខងារមួយ៖

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

    ក្នុងកូដខាងលើ យើងបាន៖

    - ដំណើរការលើបញ្ជីការហៅមុខងារ
    - សម្រាប់រាល់ការហៅឧបករណ៍ នាំឈ្មោះ និងបរិមាណ ហើយហៅឧបករណ៍លើម៉ាស៊ីនបម្រើ MCP ដោយប្រើ MCP client។ ចុងក្រោយបោះពុម្ពលទ្ធផល។

នេះគឺជាកូដពេញលេញ៖

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
    // បំពេញការស្នើសុំភាសาธรรมชาติដែលប្រើឧបករណ៍ MCP អូតូម៉ាទិច
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

ក្នុងកូដខាងលើ យើងបាន៖

- ប្រើស្នើសុំភាសាធម្មជាតិសាមញ្ញ សម្រាប់ទំនាក់ទំនងជាមួយឧបករណ៍ MCP server
- បណ្ដុំគ្រប់គ្រង LangChain4j ធ្វើស្វ័យប្រវត្តិក្នុង៖
  - បម្លែងស្នើសុំអ្នកប្រើទៅហៅឧបករណ៍ពេលចាំបាច់
  - ហៅឧបករណ៍ MCP ដែលសមរភាព ដោយផ្អែកលើការសម្រេចចិត្តរបស់ LLM
  - គ្រប់គ្រងលំហូរសន្ទនារវាង LLM និងម៉ាស៊ីនបម្រើ MCP
- វិធីសាស្រ្ត `bot.chat()` បញ្ចូនចម្លើយភាសាធម្មជាតិក្នុងនោះអាចមានលទ្ធផលពីការប្រតិបត្តិឧបករណ៍ MCP
- វិធីសាស្រ្តនេះផ្តល់បទពិសោធន៍អ្នកប្រើដោយរលូន ដែលអ្នកប្រើមិនចាំបាច់ដឹងអំពីការអនុវត្ត MCP ជាឯកតាជាក់លាក់ទេ

ឧទាហរណ៍កូដពេញលេញ៖

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

ទីនេះគឺជាកន្លែងដែលការងារច្រើនកើតមាន។ យើងនឹងហៅ LLM ជាមួយស្នើសុំដំបូងពីអ្នកប្រើ បន្ទាប់មកដោះស្រាយចម្លើយ ដើម្បីមើលថាតើមានឧបករណ៍ណាត្រូវហៅទេ។ បើមាន អ្នកនឹងហៅឧបករណ៍ទាំងនេះ ហើយបន្តសន្ទនាជាមួយ LLM រហូតដល់មិនចាំបាច់ហៅឧបករណ៍បន្ថែមទៀត ហើយយើងមានចម្លើយចុងក្រោយ។

យើងនឹងធ្វើការហៅច្រើនដងទៅ LLM ដូច្នេះសូមកំណត់មុខងារមួយដែលគ្រប់គ្រងការហៅ LLM។ បន្ថែមមុខងារខាងក្រោមទៅក្នុងឯកសារ `main.rs` របស់អ្នក៖

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

មុខងារនេះទទួល client LLM បញ្ជីសារផ្សេងៗ (រួមទាំងស្នើសុំអ្នកប្រើ) ឧបករណ៍ពីម៉ាស៊ីនបម្រើ MCP ហើយបញ្ជូនសំណើទៅ LLM ហើយបញ្ចូនតបស្នូលត្រឡប់វិញ។
ការឆ្លើយតបពី LLM នឹងមានអារេមួយនៃ `choices`។ យើងត្រូវតែដំណើរការកាលបរិច្ឆេទដើម្បីឃើញថា មាន `tool_calls` មួយណាមានអវត្តមានឬអត់។ វាឲ្យដឹងថា LLM កំពុងស្នើសុំឲ្យហៅឧបករណ៍ជាក់លាក់មួយជាមួយនឹងអាគុយម៉ង់។ បន្ថែមកូដខាងក្រោមនៅចុងឯកសារ `main.rs` របស់អ្នក ដើម្បីកំណត់មុខងារមួយដើម្បីដោះស្រាយការឆ្លើយតបពី LLM៖

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

    // បោះពុម្ពមាតិកាប្រសិនបើមាន
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // គ្រប់គ្រងការហៅឧបករណ៍
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // បន្ថែមសាររបស់ជំនួយការ

        // បញ្ចូលការហៅឧបករណ៍នីមួយៗ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // បន្ថែមលទ្ធផលឧបករណ៍ទៅសារនានា
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

បើមាន `tool_calls` វានឹងដកសេចក្ដីព័ត៌មានឧបករណ៍ដោយហៅម៉ាសុីន MCP ជាមួយសំណើឧបករណ៍ ហើយបន្ថែមលទ្ធផលទៅក្នុងសារសន្ទនានោះ។ បន្ទាប់មកវាត្រូវបន្តសន្ទនាជាមួយ LLM ហើយសារត្រូវបានអាប់ដេតជាមួយនឹងការឆ្លើយតបពីជំនួយការនិងលទ្ធផលហៅឧបករណ៍។

ដើម្បីដកសេចក្ដីព័ត៌មានហៅឧបករណ៍ដែល LLM ឆ្លើយតបសម្រាប់ការហៅ MCP មិញ ត្រូវបន្ថែមមុខងារជួយមួយទៀត ដើម្បីដកយកអ្វីៗទាំងអស់ដែលត្រូវបានប្រើឲ្យសម្រេចការហៅ។ បន្ថែមកូដខាងក្រោមនៅចុងឯកសារ `main.rs` របស់អ្នក៖

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

ជាមួយនឹងផ្នែកគ្រប់យ៉ាង ក្នុងកន្លែង យើងអាចដោះស្រាយសំណើផ្ដើមពីអ្នកប្រើ និងហៅ LLM។ អាប់ដេតមុខងារ `main` របស់អ្នក ដោយបញ្ចូលកូដដូចខាងក្រោម៖

```rust
// ការសន្ទនារបស់ LLM ជាមួយការហៅឧបករណ៍
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

នេះនឹងស្នើសុំ LLM ជាមួយសំណើផ្ដើមរបស់អ្នកប្រើសួរនូវផលបូកនៃលេខពីរមួយ ហើយវានឹងដំណើរការឆ្លើយតបដើម្បីគ្រប់គ្រងការហៅឧបករណ៍ឲ្យមានលំនាំ។

ល្អមែន អ្នកបានធ្វើបានទៀតហើយ!

## កិច្ចតំណែង

យកកូដពីលំហាត់ហើយបង្កើតម៉ាសុីនមួយជាមួយឧបករណ៍បន្ថែមច្រើនទៀត។ បន្ទាប់មកបង្កើតអតិថិជនមួយជាមួយ LLM ដូចក្នុងលំហាត់ហើយសាកល្បងវាជាមួយសំណួរផ្សេងៗ ដើម្បីធ្វើឲ្យប្រាកដថាឧបករណ៍ម៉ាសុីនរបស់អ្នកទាំងអស់ត្រូវបានហៅដោយឌីណាមិច។ វិធីសាស្រ្តបង្កើតអតិថិជននេះមានន័យថា អ្នកប្រើចុងក្រោយនឹងទទួលបានបទពិសោធន៍ល្អ ពីព្រោះពួកគេអាចប្រើសំណួរ ជំនួសការបញ្ជាទិញអតិថិជនច្បាស់លាស់ ហើយមិនដឹងថាមានម៉ាសុីន MCP ត្រូវបានហៅឡើយ។

## ដំណោះស្រាយ

[ដំណោះស្រាយ](./solution/README.md)

## ចំណុចសំខាន់ៗ

- ការបន្ថែម LLM ទៅអតិថិជនរបស់អ្នកផ្តល់អនុសាសន៍ល្អសម្រាប់អ្នកប្រើក្នុងការប្រាស្រ័យទាក់ទងជាមួយម៉ាសុីន MCP។
- អ្នកត្រូវបំលែងចម្លើយពីម៉ាសុីន MCP ទៅជា​រូបមន្តមួយដែល LLM អាចយល់បាន។

## គំរូ

- [ម៉ាសុីនគណនា Java](../samples/java/calculator/README.md)
- [ម៉ាសុីនគណនា .Net](../../../../03-GettingStarted/samples/csharp)
- [ម៉ាសុីនគណនា JavaScript](../samples/javascript/README.md)
- [ម៉ាសុីនគណនា TypeScript](../samples/typescript/README.md)
- [ម៉ាសុីនគណនា Python](../../../../03-GettingStarted/samples/python)
- [ម៉ាសុីនគណនា Rust](../../../../03-GettingStarted/samples/rust)

## កំណត់ហេតុបន្ថែម

## តើមានអ្វីបន្ទាប់

- បន្ទាប់: [ការប្រើម៉ាសុីនដោយប្រើ Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**ៈ  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយប្រព័ន្ធ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខិតខំបំពេញភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិក៏អាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមOwnត្រាជាដើមគួរត្រូវបានគិតថាជាដើមកំណែតែមួយដែលមានសម្បទាន៍។ សម្រាប់ព័ត៌មានសំខាន់ យើងផ្ញើផ្តល់អនុសាសន៍ឱ្យបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសផ្សេងណាមួយដូចដែលបានកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->