# LLM ဖြင့် client တစ်ခု ဖန်တီးခြင်း

ယခုအထိ သင်သည် server နှင့် client တစ်ခု ဖန်တီးနည်းကို ကြည့်ရှုခဲ့ပြီးဖြစ်သည်။ client သည် server ကို တိုက်ရိုက် ခေါ်ယူ၍ ၎င်း၏ tools, resources နှင့် prompts များကို စာရင်းပြုစုနိုင်ခဲ့သည်။ သို့သော် ၎င်းသည် အလွန်လက်တွေ့ကျသော နည်းလမ်းမဟုတ်ပါ။ သင့်အသုံးပြုသူသည် agentic ယဉ်ကျေးမှုကာလတွင် နေထိုင်ပြီး prompts များကို အသုံးပြု၍ LLM နှင့် ဆက်သွယ်လိုသည်။ သင့်အသုံးပြုသူအတွက် MCP ကို သုံးမသုံးခြင်းမဟုတ်ပဲ သဘာဝဘာသာစကားဖြင့် ဆက်သွယ်နိုင်ရန် မျှော်လင့်သည်။ ထို့ကြောင့် ဤပြဿနာကို မည်သို့ ဖြေရှင်းမည်နည်း? ဖြေရှင်းချက်မှာ client တွင် LLM တစ်ခု ထည့်သွင်းခြင်းဖြစ်သည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာတွင် client တွင် LLM တစ်ခု ထည့်သွင်းခြင်းကို အာရုံစိုက်ပြီး သင့်အသုံးပြုသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံကို မည်သို့ ပေးနိုင်သည်ကို ပြသမည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာအဆုံးတွင် သင်သည်:

- LLM ပါရှိသော client တစ်ခု ဖန်တီးနိုင်မည်။
- LLM ကို အသုံးပြု၍ MCP server နှင့် ချိတ်ဆက် ဆက်သွယ်နိုင်မည်။
- client ဘက်တွင် အသုံးပြုသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံ ပေးနိုင်မည်။

## နည်းလမ်း

လိုအပ်သော နည်းလမ်းကို နားလည်ကြည့်ကြရအောင်။ LLM တစ်ခု ထည့်သွင်းခြင်းသည် ရိုးရှင်းသော်လည်း အမှန်တကယ် လုပ်ဆောင်မည်လား?

client သည် server နှင့် အောက်ပါအတိုင်း ဆက်သွယ်မည်ဖြစ်သည်-

1. server နှင့် ချိတ်ဆက်မှု တည်ဆောက်ခြင်း။

1. စွမ်းရည်များ၊ prompts, resources နှင့် tools များကို စာရင်းပြုစု၍ ၎င်းတို့၏ schema ကို သိမ်းဆည်းခြင်း။

1. LLM တစ်ခု ထည့်သွင်းပြီး သိမ်းဆည်းထားသော စွမ်းရည်များနှင့် schema များကို LLM နားလည်နိုင်သော ပုံစံဖြင့် ပေးပို့ခြင်း။

1. အသုံးပြုသူ prompt ကို LLM သို့ ပေးပို့ပြီး client မှ စာရင်းပြုစုထားသော tools များနှင့်အတူ ကိုင်တွယ်ခြင်း။

အလွန်ကောင်းပြီ၊ အဆင့်မြင့်အဆင့်တွင် မည်သို့ လုပ်ဆောင်မည်ကို နားလည်သွားပြီဖြစ်သောကြောင့် အောက်ပါ လေ့ကျင့်ခန်းတွင် စမ်းသပ်ကြည့်ကြရအောင်။

## လေ့ကျင့်ခန်း: LLM ပါရှိသော client တစ်ခု ဖန်တီးခြင်း

ဤလေ့ကျင့်ခန်းတွင် client တွင် LLM တစ်ခု ထည့်သွင်းနည်းကို သင်ယူမည်။

### GitHub Personal Access Token ဖြင့် အတည်ပြုခြင်း

GitHub token တစ်ခု ဖန်တီးခြင်းသည် ရိုးရှင်းသော လုပ်ငန်းစဉ်ဖြစ်သည်။ အောက်ပါအတိုင်း လုပ်ဆောင်နိုင်သည်-

- GitHub Settings သို့ သွားပါ – ထိပ်ဆုံးညာဘက်မှ သင့်ပရိုဖိုင်ပုံကို နှိပ်ပြီး Settings ကို ရွေးချယ်ပါ။
- Developer Settings သို့ သွားပါ – အောက်သို့ ဆွဲချပြီး Developer Settings ကို နှိပ်ပါ။
- Personal Access Tokens ကို ရွေးချယ်ပါ – Fine-grained tokens ကို နှိပ်ပြီး Generate new token ကို နှိပ်ပါ။
- သင့် Token ကို ပြင်ဆင်ပါ – မှတ်ချက်တစ်ခု ထည့်သွင်းပြီး သက်တမ်းကုန်ဆုံးရက်ကို သတ်မှတ်ပြီး လိုအပ်သော scopes (ခွင့်ပြုချက်များ) ကို ရွေးချယ်ပါ။ ဤအမှုတွင် Models ခွင့်ပြုချက်ကို ထည့်သွင်းရန် သေချာပါစေ။
- Token ကို Generate ပြီး ကူးယူပါ – Generate token ကို နှိပ်ပြီး ချက်ချင်း ကူးယူပါ၊ ထပ်မကြည့်နိုင်တော့ပါ။

### -1- Server နှင့် ချိတ်ဆက်ခြင်း

client ကို ပထမဦးဆုံး ဖန်တီးကြရအောင်-

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema စစ်ဆေးမှုအတွက် zod ကို တင်သွင်းပါ။

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

အထက်ပါ ကုဒ်တွင်-

- လိုအပ်သော စာကြည့်တိုက်များကို import ပြုလုပ်ထားသည်။
- client နှင့် LLM နှင့် ဆက်သွယ်ရန် ကူညီမည့် `client` နှင့် `openai` ဆိုသော members နှစ်ခုပါရှိသည့် class တစ်ခု ဖန်တီးထားသည်။
- GitHub Models ကို အသုံးပြုရန် `baseUrl` ကို inference API သို့ ပြောင်းထားပြီး LLM instance ကို ပြင်ဆင်ထားသည်။

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ချိတ်ဆက်မှုအတွက် ဆာဗာ ပါရာမီတာများ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အလုပ်လုပ်နိုင်သော
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line အချက်အလက်များ
    env=None,  # ရွေးချယ်စရာ ပတ်ဝန်းကျင် အပြောင်းအလဲများ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ချိတ်ဆက်မှုကို စတင်တည်ဆောက်ပါ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

အထက်ပါ ကုဒ်တွင်-

- MCP အတွက် လိုအပ်သော စာကြည့်တိုက်များကို import ပြုလုပ်ထားသည်။
- client တစ်ခု ဖန်တီးထားသည်။

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

ပထမဦးဆုံး LangChain4j dependencies များကို `pom.xml` ဖိုင်တွင် ထည့်သွင်းရမည်။ MCP ပေါင်းစည်းမှုနှင့် GitHub Models ကို ထောက်ပံ့ရန် အောက်ပါ dependencies များ ထည့်သွင်းပါ-

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

ထို့နောက် Java client class ကို ဖန်တီးပါ-

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
    
    public static void main(String[] args) throws Exception {        // GitHub မော်ဒယ်များကို အသုံးပြုရန် LLM ကို ပြင်ဆင်ပါ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ဆာဗာနှင့် ချိတ်ဆက်ရန် MCP သယ်ယူပို့ဆောင်မှုကို ဖန်တီးပါ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP client ကို ဖန်တီးပါ
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

အထက်ပါ ကုဒ်တွင်-

- **LangChain4j dependencies များ ထည့်သွင်းထားသည်** - MCP ပေါင်းစည်းမှု၊ OpenAI official client နှင့် GitHub Models ထောက်ပံ့မှုအတွက်
- **LangChain4j စာကြည့်တိုက်များကို import ပြုလုပ်ထားသည်** - MCP ပေါင်းစည်းမှုနှင့် OpenAI chat model လုပ်ဆောင်ချက်အတွက်
- **`ChatLanguageModel` တစ်ခု ဖန်တီးထားသည်** - GitHub token ဖြင့် GitHub Models ကို အသုံးပြုရန် ပြင်ဆင်ထားသည်
- **HTTP သယ်ယူပို့ဆောင်မှုကို စီစဉ်ထားသည်** - Server-Sent Events (SSE) ကို အသုံးပြု၍ MCP server နှင့် ချိတ်ဆက်ရန်
- **MCP client တစ်ခု ဖန်တီးထားသည်** - server နှင့် ဆက်သွယ်မှုကို ကိုင်တွယ်ရန်
- **LangChain4j ၏ MCP ထောက်ပံ့မှုကို အသုံးပြုထားသည်** - LLM များနှင့် MCP server များအကြား ပေါင်းစည်းမှုကို လွယ်ကူစေသည်

#### Rust

ဤဥပမာသည် Rust အခြေပြု MCP server တစ်ခု ရှိကြောင်း သတ်မှတ်ထားသည်။ မရှိပါက [01-first-server](../01-first-server/README.md) သင်ခန်းစာသို့ ပြန်သွား၍ server ကို ဖန်တီးပါ။

Rust MCP server ရရှိပြီးပါက terminal ကို ဖွင့်၍ server နှင့် တူညီသော directory သို့ သွားပါ။ ထို့နောက် အောက်ပါ command ဖြင့် LLM client project အသစ် တစ်ခု ဖန်တီးပါ-

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` ဖိုင်တွင် အောက်ပါ dependencies များ ထည့်သွင်းပါ-

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI အတွက် official Rust library မရှိသော်လည်း `async-openai` crate သည် [အသိုင်းအဝိုင်းထိန်းသိမ်းသော စာကြည့်တိုက်](https://platform.openai.com/docs/libraries/rust#rust) ဖြစ်ပြီး အများအားဖြင့် အသုံးပြုသည်။

`src/main.rs` ဖိုင်ကို ဖွင့်၍ အောက်ပါကုဒ်ဖြင့် အစားထိုးပါ-

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
    // စတင်မက်ဆေ့ခ်ျ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI client ကို စတင်တပ်ဆင်ခြင်း
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP client ကို စတင်တပ်ဆင်ခြင်း
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

    // TODO: MCP ကိရိယာစာရင်း ရယူရန်

    // TODO: ကိရိယာခေါ်ဆိုမှုများနှင့် LLM စကားပြောခြင်း

    Ok(())
}
```

ဤကုဒ်သည် MCP server နှင့် GitHub Models ကို ချိတ်ဆက်ရန် အခြေခံ Rust application တစ်ခုကို ပြင်ဆင်ထားသည်။

> [!IMPORTANT]
> အပလီကေးရှင်းကို စတင်မပြေးမီ `OPENAI_API_KEY` environment variable ကို သင့် GitHub token ဖြင့် သတ်မှတ်ထားရန် သေချာပါစေ။

ကောင်းပါပြီ၊ နောက်တစ်ဆင့်အနေဖြင့် server ၏ စွမ်းရည်များကို စာရင်းပြုစုကြရအောင်။

### -2- Server စွမ်းရည်များ စာရင်းပြုစုခြင်း

ယခု server နှင့် ချိတ်ဆက်ပြီး ၎င်း၏ စွမ်းရည်များကို မေးမြန်းပါ-

#### Typescript

တူညီသော class တွင် အောက်ပါ method များ ထည့်သွင်းပါ-

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ကိရိယာများ စာရင်းပြုစုခြင်း
    const toolsResult = await this.client.listTools();
}
```

အထက်ပါ ကုဒ်တွင်-

- server နှင့် ချိတ်ဆက်ရန် `connectToServer` ကို ထည့်သွင်းထားသည်။
- app flow ကို ကိုင်တွယ်မည့် `run` method ကို ဖန်တီးထားသည်။ ယခုအချိန်တွင် tools များကိုသာ စာရင်းပြုစုထားသော်လည်း နောက်ပိုင်းတွင် ပိုမိုထည့်သွင်းမည်။

#### Python

```python
# ရနိုင်သော အရင်းအမြစ်များကို စာရင်းပြုစုပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ရနိုင်သော ကိရိယာများကို စာရင်းပြုစုပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ထည့်သွင်းထားသောအရာများမှာ-

- resources နှင့် tools များကို စာရင်းပြုစုပြီး ပုံနှိပ်ထားသည်။ tools များအတွက် `inputSchema` ကိုလည်း စာရင်းပြုစုထားပြီး နောက်ပိုင်းတွင် အသုံးပြုမည်။

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

အထက်ပါ ကုဒ်တွင်-

- MCP Server တွင် ရရှိနိုင်သော tools များကို စာရင်းပြုစုထားသည်။
- tools တစ်ခုချင်းစီအတွက် name, description နှင့် schema ကို စာရင်းပြုစုထားသည်။ schema သည် tools များကို ခေါ်ရန် အသုံးပြုမည့် အချက်အလက်ဖြစ်သည်။

#### Java

```java
// MCP ကိရိယာများကို အလိုအလျောက် ရှာဖွေသည့် ကိရိယာ ပံ့ပိုးသူ တစ်ခု ဖန်တီးပါ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ကိရိယာ ပံ့ပိုးသူသည် အလိုအလျောက် ကိုင်တွယ်ပေးသည် -
// - MCP ဆာဗာမှ ရနိုင်သော ကိရိယာများကို စာရင်းပြုစုခြင်း
// - MCP ကိရိယာ စနစ်များကို LangChain4j ပုံစံသို့ ပြောင်းလဲခြင်း
// - ကိရိယာ အကောင်အထည်ဖော်ခြင်းနှင့် တုံ့ပြန်ချက်များကို စီမံခန့်ခွဲခြင်း
```

အထက်ပါ ကုဒ်တွင်-

- MCP server မှ tools များအား အလိုအလျောက် ရှာဖွေမှတ်ပုံတင်သည့် `McpToolProvider` တစ်ခု ဖန်တီးထားသည်။
- tool provider သည် MCP tool schema များနှင့် LangChain4j tool ပုံစံများအကြား ပြောင်းလဲမှုကို အတွင်းပိုင်းတွင် ကိုင်တွယ်သည်။
- ဤနည်းလမ်းသည် tools များကို လက်ဖြင့် စာရင်းပြုစုခြင်းနှင့် ပြောင်းလဲခြင်းကို ဖယ်ရှားပေးသည်။

#### Rust

MCP server မှ tools များ ရယူရန် `list_tools` method ကို အသုံးပြုသည်။ `main` function တွင် MCP client ကို ပြင်ဆင်ပြီးနောက် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ-

```rust
// MCP ကိရိယာစာရင်းကို ရယူပါ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server စွမ်းရည်များကို LLM tools အဖြစ် ပြောင်းလဲခြင်း

server စွမ်းရည်များ စာရင်းပြုစုပြီးနောက် LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရမည်။ ပြောင်းလဲပြီးနောက် ၎င်းစွမ်းရည်များကို LLM အတွက် tools အဖြစ် ပေးနိုင်မည်။

#### TypeScript

1. MCP Server မှ ရရှိသော response ကို LLM အသုံးပြုနိုင်သော tool ပုံစံသို့ ပြောင်းလဲရန် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ-

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema အပေါ် မူတည်၍ zod schema တစ်ခု ဖန်တီးပါ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // type ကို "function" ဟု ထင်ရှားစွာ သတ်မှတ်ပါ
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

    အထက်ပါကုဒ်သည် MCP Server response ကို ယူ၍ LLM နားလည်နိုင်သော tool definition ပုံစံသို့ ပြောင်းလဲသည်။

1. `run` method ကို server စွမ်းရည်များ စာရင်းပြုစုရန် အောက်ပါအတိုင်း ပြင်ဆင်ပါ-

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

    အထက်ပါ ကုဒ်တွင် `run` method ကို update ပြုလုပ်၍ ရလဒ်အား map ဖြင့် လှမ်းပြီး entry တစ်ခုချင်းစီအတွက် `openAiToolAdapter` ကို ခေါ်သည်။

#### Python

1. ပထမဦးဆုံး အောက်ပါ converter function ကို ဖန်တီးပါ-

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

    `convert_to_llm_tools` function တွင် MCP tool response ကို ယူ၍ LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲသည်။

1. နောက်တစ်ဆင့် client ကုဒ်ကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ-

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ဤနေရာတွင် MCP tool response ကို LLM သို့ ထည့်သွင်းနိုင်ရန် `convert_to_llm_tool` ကို ခေါ်သုံးထားသည်။

#### .NET

1. MCP tool response ကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် ကုဒ် ထည့်သွင်းပါ-

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

အထက်ပါ ကုဒ်တွင်-

- name, description နှင့် input schema ကို လက်ခံသည့် `ConvertFrom` function တစ်ခု ဖန်တီးထားသည်။
- FunctionDefinition တစ်ခု ဖန်တီးပြီး ChatCompletionsDefinition သို့ ပေးပို့သည်။ ၎င်းသည် LLM နားလည်နိုင်သော ပုံစံဖြစ်သည်။

1. အထက်ပါ function ကို အသုံးပြုရန် ရှိပြီးသား ကုဒ်ကို ပြင်ဆင်ပါ-

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
// သဘာဝဘာသာစကားအပြန်အလှန်ဆက်သွယ်မှုအတွက် Bot အင်တာဖေ့စ်တစ်ခု ဖန်တီးပါ
public interface Bot {
    String chat(String prompt);
}

// LLM နှင့် MCP ကိရိယာများဖြင့် AI ဝန်ဆောင်မှုကို ပြင်ဆင်ပါ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

အထက်ပါ ကုဒ်တွင်-

- သဘာဝဘာသာစကားဖြင့် ဆက်သွယ်ရန် ရိုးရှင်းသော `Bot` interface တစ်ခု သတ်မှတ်ထားသည်။
- LangChain4j ၏ `AiServices` ကို အသုံးပြု၍ LLM နှင့် MCP tool provider ကို အလိုအလျောက် ချိတ်ဆက်ထားသည်။
- framework သည် tool schema ပြောင်းလဲခြင်းနှင့် function ခေါ်ဆိုခြင်းကို အလိုအလျောက် ကိုင်တွယ်ပေးသည်။
- ဤနည်းလမ်းသည် လက်ဖြင့် tool ပြောင်းလဲခြင်းကို ဖယ်ရှားပြီး MCP tools များကို LLM သင့်လျော်သော ပုံစံသို့ ပြောင်းလဲခြင်း၏ အခက်အခဲများအား LangChain4j က ကိုင်တွယ်ပေးသည်။

#### Rust

MCP tool response ကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် tools စာရင်းကို ဖော်ပြသည့် helper function တစ်ခု ထည့်သွင်းမည်။ `main` function အောက်တွင် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ။ ၎င်းကို LLM သို့ တောင်းဆိုမှုများ ပြုလုပ်ရာတွင် ခေါ်သုံးမည်-

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

ကောင်းပါပြီ၊ အသုံးပြုသူ တောင်းဆိုမှုများကို ကိုင်တွယ်ရန် ပြင်ဆင်ထားပြီးဖြစ်သောကြောင့် နောက်တစ်ဆင့်ကို ဆက်လုပ်ကြရအောင်။

### -4- အသုံးပြုသူ prompt တောင်းဆိုမှု ကိုင်တွယ်ခြင်း

ဤကုဒ်အပိုင်းတွင် အသုံးပြုသူ တောင်းဆိုမှုများကို ကိုင်တွယ်မည်။

#### TypeScript

1. LLM ကို ခေါ်ရန် အသုံးပြုမည့် method တစ်ခု ထည့်သွင်းပါ-

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ၂။ ဆာဗာရဲ့ကိရိယာကိုခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့တစ်ခုခုလုပ်ပါ
        // လုပ်ရန်ရှိသည်

        }
    }
    ```

    အထက်ပါ ကုဒ်တွင်-

    - `callTools` method ကို ထည့်သွင်းထားသည်။
    - method သည် LLM response ကို လက်ခံပြီး ခေါ်ရန်လိုသော tools များ ရှိမရှိ စစ်ဆေးသည်-

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ကိရိယာကို ခေါ်ပါ
        }
        ```

    - LLM မှ ခေါ်ရန်လိုသည်ဟု ပြောပါက tool ကို ခေါ်သည်-

        ```typescript
        // ၂။ ဆာဗာရဲ့ကိရိယာကိုခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့တစ်ခုခုလုပ်ပါ
        // လုပ်ရန်ရှိသည်
        ```

1. `run` method ကို LLM ခေါ်ဆိုမှုနှင့် `callTools` ခေါ်ဆိုမှုများ ထည့်သွင်းရန် update ပြုလုပ်ပါ-

    ```typescript

    // 1. LLM အတွက် input ဖြစ်တဲ့ မက်ဆေ့ခ်ျတွေ ဖန်တီးပါ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ကို ခေါ်ဆိုခြင်း
    let response = this.openai.chat.completions.create({
        model: "gpt-4o-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ရဲ့ တုံ့ပြန်ချက်ကို ကြည့်ပါ၊ ရွေးချယ်မှုတိုင်းအတွက် tool call ရှိမရှိ စစ်ဆေးပါ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ကောင်းပါပြီ၊ အကုန်လုံးကို ပြန်လည်ကြည့်ကြရအောင်-

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema စစ်ဆေးမှုအတွက် zod ကို တင်သွင်းပါ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // အနာဂတ်တွင် ဒီ url ကို ပြောင်းလဲရန် လိုအပ်နိုင်သည်: https://models.github.ai/inference
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
          // input_schema အပေါ် မူတည်၍ zod schema တစ်ခု ဖန်တီးပါ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // type ကို "function" ဟု ထင်ရှားစွာ သတ်မှတ်ပါ
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
    
    
          // 2. ဆာဗာ၏ ကိရိယာကို ခေါ်ပါ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ရလဒ်နှင့် အလုပ်လုပ်ပါ
          // လုပ်ရန်ရှိသည်
    
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
    
        // 1. LLM တုံ့ပြန်ချက်ကို ဖြတ်သန်းပြီး၊ ရွေးချယ်မှုတိုင်းအတွက် ကိရိယာခေါ်ဆိုမှုရှိမရှိ စစ်ဆေးပါ
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

1. LLM ခေါ်ရန် လိုအပ်သော imports များ ထည့်သွင်းပါ-

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. နောက်တစ်ဆင့် LLM ကို ခေါ်မည့် function ကို ထည့်သွင်းပါ-

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
            # ရွေးချယ်စရာ ပါရာမီတာများ
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

    အထက်ပါ ကုဒ်တွင်-

    - MCP server တွင် ရှာဖွေပြီး ပြောင်းလဲထားသော functions များကို LLM သို့ ပေးပို့ထားသည်။
    - ထို့နောက် functions များနှင့်အတူ LLM ကို ခေါ်ထားသည်။
    - ရလဒ်ကို စစ်ဆေး၍ ခေါ်ရန် function များ ရှိမရှိ ကြည့်သည်။
    - နောက်ဆုံးတွင် ခေါ်ရန် function များ စာရင်းကို ပေးပို့သည်။

1. နောက်ဆုံးအဆင့် client ကုဒ်ကို update ပြုလုပ်ပါ-

    ```python
    prompt = "Add 2 to 20"

    # LLM ကို မည်သည့်ကိရိယာများရှိသည်ကို မေးပါ၊ ရှိပါက
    functions_to_call = call_llm(prompt, functions)

    # အကြံပြုထားသောလုပ်ဆောင်ချက်များကို ခေါ်ပါ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    အထက်ပါ ကုဒ်တွင်-

    - LLM ၏ အဆိုအရ MCP tool တစ်ခုကို `call_tool` ဖြင့် ခေါ်ထားသည်။
    - MCP Server သို့ tool ခေါ်ဆိုမှုရလဒ်ကို ပုံနှိပ်ထားသည်။

#### .NET

1. LLM prompt တောင်းဆိုမှု ပြုလုပ်ရန် ကုဒ်ကို ပြပါ-

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

    အထက်ပါ ကုဒ်တွင်-

    - MCP server မှ tools များ ရယူထားသည်၊ `var tools = await GetMcpTools()`။
    - အသုံးပြုသူ prompt `userMessage` ကို သတ်မှတ်ထားသည်။
    - model နှင့် tools များ သတ်မှတ်ထားသည့် options object တစ်ခု ဖန်တီးထားသည်။
    - LLM သို့ တောင်းဆိုမှု ပြုလုပ်ထားသည်။

1. နောက်ဆုံးအဆင့် LLM သည် function ခေါ်ရန်လိုသည်ဟု ထင်ပါက စစ်ဆေးပါ-

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

    အထက်ပါ ကုဒ်တွင်-

    - function calls စာရင်းကို လည်ပတ်စစ်ဆေးထားသည်။
    - tool call တစ်ခုချင်းစီအတွက် name နှင့် arguments ကို ခွဲထုတ်ပြီး MCP client ဖြင့် MCP server တွင် tool ကို ခေါ်သည်။ နောက်ဆုံးတွင် ရလဒ်များကို ပုံနှိပ်သည်။

ကုဒ်အပြည့်အစုံ-

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
    // MCP ကိရိယာများကို အလိုအလျောက် အသုံးပြု၍ သဘာဝဘာသာစကား တောင်းဆိုချက်များကို အကောင်အထည်ဖော်ပါ။
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

အထက်ပါ ကုဒ်တွင်-

- MCP server tools များနှင့် သဘာဝဘာသာစကား prompt များဖြင့် ရိုးရှင်းစွာ ဆက်သွယ်ထားသည်။
- LangChain4j framework သည် အလိုအလျောက် ကိုင်တွယ်ပေးသည်-
  - အသုံးပြုသူ prompt များကို လိုအပ်သလို tool ခေါ်ဆိုမှုများသို့ ပြောင်းလဲခြင်း
  - LLM ၏ ဆုံးဖြတ်ချက်အရ သင့်တော်သော MCP tools များကို ခေါ်ဆိုခြင်း
  - LLM နှင့် MCP server အကြား စကားဝိုင်းစီမံခန့်ခွဲမှု
- `bot.chat()` method သည် MCP tool အကောင်အထည်ဖော်မှုများ ပါဝင်နိုင်သည့် သဘာဝဘာသာစကားဖြေကြားချက်များ ပြန်လည်ပေးသည်
- ဤနည်းလမ်းသည် အသုံးပြုသူများအနေဖြင့် MCP အတွင်းရေးရာကို မသိဘဲ သဘာဝစကားဖြင့် အဆင်ပြေစွာ အသုံးပြုနိုင်စေသည်။

ကုဒ်နမူနာ အပြည့်အစုံ-

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

ဤနေရာတွင် အလုပ်အများစု ဖြစ်ပေါ်သည်။ ပထမဦးဆုံး အသုံးပြုသူ prompt ဖြင့် LLM ကို ခေါ်ပြီး ထုတ်လွှင့်ချက်ကို စစ်ဆေးကာ tool များ ခေါ်ရန် လိုအပ်ပါက ခေါ်ပြီး LLM နှင့် ဆက်လက် စကားဝိုင်း ပြုလုပ်မည်။ tool ခေါ်ဆိုမှု မလိုအပ်သေးပါက နောက်ဆုံးဖြေကြားချက် ရရှိမည်။

LLM ကို မကြာခဏ ခေါ်ဆိုမည်ဖြစ်သောကြောင့် LLM ခေါ်ဆိုမှုကို ကိုင်တွယ်မည့် function တစ်ခု သတ်မှတ်ပါ။ `main.rs` ဖိုင်တွင် အောက်ပါ function ကို ထည့်သွင်းပါ-

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

ဤ function သည် LLM client, message စာရင်း (အသုံးပြုသူ prompt ပါဝင်သည်), MCP server မှ tools များကို လက်ခံပြီး LLM သို့ တောင်းဆိုမှု ပေးပို့ကာ ပြန်လည်ဖြေကြားချက်ကို ပြန်ပေးသည်။
LLM မှ ပြန်လာသော တုံ့ပြန်ချက်တွင် `choices` ဆိုသော အစုအဝေးတစ်ခု ပါဝင်မည်ဖြစ်သည်။ ကျွန်ုပ်တို့သည် ရလဒ်ကို စစ်ဆေးရန် လိုအပ်သည်၊ `tool_calls` များ ရှိမရှိကို ကြည့်ရန်။ ၎င်းက LLM သည် အတိအကျ တစ်ခုခုသော ကိရိယာတစ်ခုကို အချက်အလက်များနှင့်အတူ ခေါ်ဆိုရန် တောင်းဆိုနေသည်ကို သိရှိစေသည်။ သင့် `main.rs` ဖိုင်၏ အောက်ဆုံးတွင် အောက်ပါကုဒ်ကို ထည့်သွင်း၍ LLM တုံ့ပြန်ချက်ကို ကိုင်တွယ်မည့် function တစ်ခုကို သတ်မှတ်ပါ-

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

    // အကြောင်းအရာရှိပါက ပုံနှိပ်ပါ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ကိရိယာခေါ်ဆိုမှုများကို ကိုင်တွယ်ပါ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // အကူအညီပေးသူ စာတိုက်စာကို ထည့်ပါ

        // ကိရိယာခေါ်ဆိုမှုတိုင်းကို အကောင်အထည်ဖော်ပါ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ကိရိယာရလဒ်ကို စာတိုက်စာများထဲသို့ ထည့်ပါ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ကိရိယာရလဒ်များနှင့် စကားပြောဆက်လက်ပါ
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

`tool_calls` များ ရှိပါက၊ ၎င်းသည် ကိရိယာဆိုင်ရာ အချက်အလက်များကို ထုတ်ယူပြီး MCP ဆာဗာသို့ ကိရိယာတောင်းဆိုမှုဖြင့် ခေါ်ဆိုကာ ရလဒ်များကို စကားပြောဆိုမှု မက်ဆေ့ခ်ျများထဲသို့ ထည့်သွင်းသည်။ ထို့နောက် LLM နှင့် စကားပြောဆိုမှုကို ဆက်လက်လုပ်ဆောင်ပြီး မက်ဆေ့ခ်ျများကို အကူအညီပေးသူ၏ တုံ့ပြန်ချက်နှင့် ကိရိယာခေါ်ဆိုမှုရလဒ်များဖြင့် အပ်ဒိတ်လုပ်သည်။

LLM မှ MCP ခေါ်ဆိုမှုများအတွက် ပြန်လာသော ကိရိယာခေါ်ဆိုမှု အချက်အလက်များကို ထုတ်ယူရန် အကူအညီ function တစ်ခုကို ထပ်မံ ထည့်သွင်းမည်။ သင့် `main.rs` ဖိုင်၏ အောက်ဆုံးတွင် အောက်ပါကုဒ်ကို ထည့်ပါ-

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

အပိုင်းအားလုံး ပြီးစီးသွားသောကြောင့်၊ ကျွန်ုပ်တို့သည် စတင်အသုံးပြုသူ prompt ကို ကိုင်တွယ်ပြီး LLM ကို ခေါ်ဆိုနိုင်ပြီဖြစ်သည်။ သင့် `main` function ကို အောက်ပါကုဒ်ဖြင့် အပ်ဒိတ်လုပ်ပါ-

```rust
// ကိရိယာခေါ်ဆိုမှုများနှင့် LLM စကားပြောခြင်း
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

ဤသည်က LLM ကို စတင်အသုံးပြုသူ prompt ဖြင့် မေးမြန်းကာ နံပါတ်နှစ်ခု၏ စုစုပေါင်းကို မေးမြန်းပြီး တုံ့ပြန်ချက်ကို ကိရိယာခေါ်ဆိုမှုများကို dynamic အနေဖြင့် ကိုင်တွယ်ရန် လုပ်ဆောင်မည်ဖြစ်သည်။

အရမ်းကောင်းပြီ၊ သင်လုပ်နိုင်ပြီ!

## အလုပ်အပ်

လေ့ကျင့်ခန်းမှ ကုဒ်ကို ယူပြီး ဆာဗာကို ကိရိယာများ ပိုမိုထည့်သွင်း၍ တည်ဆောက်ပါ။ ထို့နောက် LLM ပါသော client တစ်ခုကို လေ့ကျင့်ခန်းကဲ့သို့ ဖန်တီးပြီး မတူညီသော prompt များဖြင့် စမ်းသပ်ပါ၊ သင့်ဆာဗာကိရိယာများအားလုံး dynamic အနေဖြင့် ခေါ်ဆိုခံရမည်ဖြစ်သည်ကို သေချာစေရန်။ client တစ်ခုကို ဤနည်းဖြင့် တည်ဆောက်ခြင်းသည် အသုံးပြုသူအတွက် အကောင်းဆုံး အသုံးပြုမှု အတွေ့အကြုံကို ပေးစွမ်းနိုင်သည်၊ အကြောင်းမှာ သူတို့သည် တိကျသော client command များအစား prompt များကို အသုံးပြုနိုင်ပြီး MCP ဆာဗာကို ခေါ်ဆိုခြင်းကို မသိရှိဘဲ အသုံးပြုနိုင်ခြင်း ဖြစ်သည်။

## ဖြေရှင်းချက်

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## အဓိက သင်ခန်းစာများ

- LLM ကို သင့် client တွင် ထည့်သွင်းခြင်းဖြင့် MCP ဆာဗာများနှင့် အသုံးပြုသူများ ပိုမိုကောင်းမွန်စွာ ဆက်သွယ်နိုင်သည်။
- MCP ဆာဗာ၏ တုံ့ပြန်ချက်ကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် လိုအပ်သည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## အပိုဆောင်း အရင်းအမြစ်များ

## နောက်တစ်ဆင့်

- နောက်တစ်ဆင့်: [Visual Studio Code ကို အသုံးပြု၍ ဆာဗာကို စားသုံးခြင်း](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->