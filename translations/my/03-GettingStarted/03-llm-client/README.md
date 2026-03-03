# LLM နှင့် client တစ်ခု တည်ဆောက်ခြင်း

ယခုအထိ server နှင့် client တစ်ခု ဘယ်လိုတည်ဆောက်ရသည်ကို ကြည့်ရှုထားသည်။ client သည် ပစ္စည်းကိရိယာများ၊ အရင်းအမြစ်များနှင့် prompts များကို စာရင်းပြုလုပ်ရန် အဓိကမှ server ကို ဖုန်းခေါ်နိုင်ခဲ့သည်။ သို့သော်၊ ၎င်းအနည်းငယ် အသုံးချရလွယ်ကူမှု မရှိသော နည်းလမ်းဖြစ်သည်။ သင့်အသုံးပြုသူများသည် အေးဂျင့်အဆင့် အသက်မွေးဝမ်းကြောင်းကာလတွင် နေထိုင်ကြပြီး prompts များအသုံးပြုခြင်းနှင့် LLM နှင့် ဆက်သွယ်ဆက်ဆံမှုကို မျှော်လင့်ကြသည်။ ၎င်းတို့သည် သင်သည် MCP ကို သင်၏ စွမ်းရည်များ သိမ်းဆည်းရန် အသုံးပြုထားသည်ဟု စိုးရိမ်မှာ မဟုတ်ပါ၊ သာမန္ဘာသာစကားဖြင့် ဆက်သွယ်နိုင်ရန်သာ မျှော်လင့်ကြသည်။ ထို့ကြောင့် ဒီပြဿနာကို ဘယ်လိုဖြေရှင်းမလဲ? ဖြေရှင်းချက်မှာ client တွင် LLM တစ်ခု ထည့်သွင်းခြင်းဖြစ်သည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာတွင် client များတွင် LLM တစ်ခု ထည့်သွင်းခြင်းကို ဦးစားပေး၍ သင့်အသုံးပြုသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံကို မည်သို့ပေးနိုင်သည်ကို ပြသပါမည်။

## သင်ယူရမည့် အချက်များ

ဤသင်ခန်းစာ ပြီးဆုံးလျှင် သင်သည် အောက်ပါများကို ကောင်းစွာ ဆောင်ရွက်နိုင်မည်ဖြစ်သည် -

- LLM ပါသော client တစ်ခု တည်ဆောက်ခြင်း။
- LLM အသုံးပြု၍ MCP server နှင့် ထိရောက်စွာ ဆက်သွယ်ခြင်း။
- client ဘက်၌ သုံးစွဲသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံ ပံ့ပိုးပေးခြင်း။

## နည်းလမ်း

မည်သို့ ယခင်နည်းလမ်းကို နားလည်ကြမည်နည်း ကြိုးစားကြည့်ကြရအောင်။ LLM တစ်ခု ထည့်သွင်းခြင်းသည် ရိုးရှင်းသည်ဟု ထင်ရပေမယ့် တကယ်လုပ်မလား?

client သည် server နှင့် ယင်းနည်းဖြင့် ဆက်သွယ်မည် ဖြစ်သည် -

1. Server နှင့် ချိတ်ဆက် တည်ဆောက်ခြင်း။

1. စွမ်းရည်များ၊ prompts များ၊ အရင်းအမြစ်များနှင့် ပစ္စည်းကိရိယာများကို စာရင်းပြုလုပ်၍ ၎င်းတို့၏ schema များကို သိမ်းဆည်းမှု။

1. LLM တစ်ခု ထည့်သွင်းပြီး သိမ်းဆည်းထားသော စွမ်းရည်များနှင့် schema များကို LLM နားလည်နိုင်သည့် ပုံစံဖြင့် ပေးပို့ခြင်း။

1. အသုံးပြုသူ prompt ကို LLM သို့ ပေးပို့ခြင်းနှင့် client မှာ စာရင်းပြုလုပ်ထားသော ပစ္စည်းကိရိယာများနှင့်အတူ ကိုင်တွယ်ခြင်း။

အဆင်ပြေပါပြီ၊ အထက်ပါ အဆင့်မြင့်မှာ ဒီလိုလုပ်ရတယ်ဆိုတာ နားလည်သွားပြီ၊ အောက်ပါလေ့ကျင့်ခန်းတွင် ကြိုးစားကြည့်ပါစို့။

## လေ့ကျင့်ခန်း: LLM ပါသော client တစ်ခု တည်ဆောက်ခြင်း

ဤလေ့ကျင့်ခန်းတွင် LLM တစ်ခုကို client တွင် ထည့်သွင်းခြင်းကို သင်ယူပါမည်။

### GitHub Personal Access Token သုံးပြီး အတည်ပြုခြင်း

GitHub Token တစ်ခု ဖန်တီးခြင်းသည် လွယ်ကူသောလုပ်ငန်းစဉ်တစ်ခု ဖြစ်သည်။ ဤသို့ဆောင်ရွက်နိုင်သည် -

- GitHub Settings သို့သွားရန် – ကိုယ်ပိုင်ပရိုဖိုင် ဓာတ်ပုံကို ညာထောင့်အပေါ်တွင်နှိပ်ပြီး Settings ရွေးချယ်ပါ။
- Developer Settings သို့ သွားရန် – အောက်သို့ ဆွဲချပြီး Developer Settings ကိုနှိပ်ပါ။
- Personal Access Tokens ကို ရွေးချယ်ရန် – Fine-grained tokens ကိုနှိပ်ပြီး Generate new token ကိုနှိပ်ပါ။
- သင့် token ကို ပြင်ဆင်ရန် – မှတ်ချက်ထည့်ပြီး သက်တမ်းကုန်ဆုံးသည့်နေ့သတ်မှတ်၍ လိုအပ်သည့် scopes (ခွင့်ပြုချက်များ) များရွေးချယ်ပါ။ ဤသို့ Models permission ကို မမေ့ပါနှင့်။
- Token ကို ရှာဖွေပြီး ကူးယူပါ – Generate token ကိုနှိပ်ပြီး ခဏ်အလိုလို့ ကူးယူပါ၊ ထပ်မပါဝင်ကြည့်နိုင်ပါ။

### -1- Server နှင့် ချိတ်ဆက်ခြင်း

client ကို အရင်ဆုံး တည်ဆောက်ကြည့်ရအောင်။

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema သက်သေပြုရန်အတွက် zod ကိုတင်သွင်းပါ။

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

အထက်ပါ ကုဒ်တွင် -

- လိုအပ်သော 라이ေဘရယ်များကို import ပြုလုပ်ထားသည်။
- `client` နှင့် `openai` ဆိုသည့် အဖွဲ့ဝင်နှစ်ဦးပါသော class တစ်ခု ဖန်တီးပြီး client ကို စီမံရန်နှင့် LLM နှင့် ဆက်သွယ်ရန် အသုံးပြုသည်။
- `baseUrl` ကို inference API သို့ညွှန်ပြရန် သတ်မှတ်ပြီး GitHub Models အသုံးပြုသည့် LLM instance တစ်ခုကို ပြင်ဆင်ထားသည်။

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ချိတ်ဆက်မှုအတွက် ဆာဗာ ပါရာမီတာများ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အကောင်ပြုနိုင်သော ဖိုင်
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line အချက်အလက်များ
    env=None,  # ရွေးချယ်စရာ ပတ်ဝန်းကျင် အပြောင်းအလဲများ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ချိတ်ဆက်မှုကို စတင်လုပ်ဆောင်ပါ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

အထက်ပါ ကုဒ်တွင် -

- MCP အတွက် လိုအပ်သောライေဘရယ် များ import ပြုလုပ်ထားသည်။
- client တစ်ခု ဖန်တီးထားသည်။

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

ပထမဆုံး `pom.xml` ဖိုင်တွင် LangChain4j dependencies များ ထည့်ရန်လိုအပ်သည်။ MCP ပေါင်းစည်းမှုနှင့် GitHub Models ထောက်ပံ့မှု အတွက် ဤ dependencies များ ထည့်သွင်းပါ -

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

ထို့နောက် Java client class ကို ဖန်တီးပါ -

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
    
    public static void main(String[] args) throws Exception {        // GitHub မော်ဒယ်များအသုံးပြုရန် LLM ကိုချိန်ညှိပါ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ဆာဗာနှင့်ချိတ်ဆက်ရန် MCP သယ်ယူပို့ဆောင်မှုကိုဖန်တီးပါ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP client ကိုဖန်တီးပါ
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

အထက်ပါ ကုဒ်တွင် -

- **LangChain4j dependencies များ ထည့်သွင်းထားသည်** - MCP ပေါင်းစည်းမှုနှင့် OpenAI official client၊ GitHub Models ထောက်ပံ့မှုအတွက်
- **LangChain4j 라이ေဘရယ်များ import ပြုလုပ်ထားသည်** - MCP ပေါင်းစည်းမှုနှင့် OpenAI chat model လုပ်ဆောင်မှုအတွက်
- **`ChatLanguageModel` တည်ဆောက်ထားသည်** - သင့် GitHub token ဖြင့် GitHub Models အသုံးပြုရန် ပြင်ဆင်ထားသည်
- **HTTP သယ်ဆောင်မှု သတ်မှတ်ထားသည်** - Server-Sent Events (SSE) ဖြင့် MCP server သို့ ချိတ်ဆက်ခြင်း
- **MCP client တစ်ခု ဖန်တီးထားသည်** - server နှင့် ဆက်သွယ်မှုကို ကိုင်တွယ်ရန်
- **LangChain4j ၏ build-in MCP အထောက်အကူ ပြုမှုအသုံးပြုထားသည်** - LLM နှင့် MCP server များ ကြား ပေါင်းစည်းမှုကို လွယ်ကူစေသည်

#### Rust

ယခု၌ Rust အခြေပြု MCP server တစ်ခု ရှိကြောင်း ထားပြီး ဖြစ်ပါသည်။ မရှိပါက [01-first-server](../01-first-server/README.md) သင်ခန်းစာသို့ ပြန်လည်သွား၍ server တည်ဆောက်ရန် လမ်းညွှန်ချက် ရယူပါ။

Rust MCP server ရရှိလျှင် terminal တစ်ခု ဖွင့်ပြီး server directory နှင့် ထပ်စီပြီး အောက်ပါ command ဖြင့် LLM client project အသစ် တည်ဆောက်ပါ -

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

ပြီးနောက် `Cargo.toml` ဖိုင်တွင် အောက်ပါ dependencies များ ထည့်ပါ -

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI အတွက် တရားဝင်သော Rust 라이ေဘရယ် မရှိပါ၊ သို့သော် `async-openai` crate သည် [အသိုင်းအဝိုင်း ထိန်းသိမ်းသော 라이ေဘရယ်](https://platform.openai.com/docs/libraries/rust#rust) ဖြစ်ပြီး အများအားဖြင့် အသုံးပြုကြသည်။

`src/main.rs` ဖိုင်ကိုဖွင့်ပြီး အောက်ပါကုဒ်များဖြင့် အစားထိုးလိုက်ပါ -

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
    // အစပိုင်းစာသား
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ဖောက်သည်ကို တပ်ဆင်ပါ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ဖောက်သည်ကို တပ်ဆင်ပါ
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

    // TODO: MCP ကိရိယာ စာရင်းယူပါ

    // TODO: ကိရိယာ ခေါ်ဆိုချက်များနှင့် LLM စကားပြောချက်

    Ok(())
}
```

ဤကုဒ်သည် MCP server နှင့် GitHub Models မှ LLM ဆက်သွယ်မှုအတွက် အခြေခံ Rust application တစ်ခုဖြစ်သည်။

> [!IMPORTANT]
> အက်ပ်လိကေးရှင်း ပြေးကိုင်ရန်မတိုင်မီ `OPENAI_API_KEY` ပတ်ဝန်းကျင် အမျိုးအစားကို သင့် GitHub token ဖြင့် သတ်မှတ်ထားရန် သေချာပါစေ။

အဆင်ပြေပါပြီ၊ နောက်အဆင့်အနေဖြင့် server ၏ စွမ်းရည်များကို စာရင်းပြုလုပ်ကြည့်ရအောင်။

### -2- Server ၏ စွမ်းရည်များ စာရင်းပြုလုပ်ခြင်း

ယခု server နှင့် ချိတ်ဆက်ပြီး စွမ်းရည်များကို မေးမြန်းမည်။

#### Typescript

အတူတူ class တွင် အောက်ပါ method များ ထည့်ပါ -

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

အထက်ပါ ကုဒ်တွင် -

- server နှင့် ချိတ်ဆက်ရန် `connectToServer` ကို ထည့်သွင်းသည်။
- `run` method တစ်ခု ဖန်တီးထားပြီး လက်ရှိတွင် ပစ္စည်းကိရိယာစာရင်း ပြုလုပ်ခြင်းသာ ပါဝင်သည်၊ ထိုနောက် ပိုမိုလုပ်ဆောင်မှု ထည့်သွင်းမည်ဖြစ်သည်။

#### Python

```python
# ရရှိနိုင်သောအရင်းအမြစ်များကို စာရင်းပြုစုပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# ရရှိနိုင်သောကိရိယာများကို စာရင်းပြုစုပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ထည့်သွင်းခဲ့သည်များ -

- အရင်းအမြစ်များနှင့် ပစ္စည်းကိရိယာများ စာရင်းပြုလုပ်ပြီး ထုတ်ပေးသည်။ ပစ္စည်းကိရိယာများအတွက် `inputSchema` ကိုလည်း စာရင်းပြုလုပ်ထားပြီး အနောက်ပိုင်းတွင် အသုံးပြုမည်။

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

အထက်ပါ ကုဒ်တွင် -

- MCP Server တွင် ရနိုင်သည့် ပစ္စည်းကိရိယာများကို စာရင်းပြုလုပ်ထားသည်။
- ပစ္စည်းကိရိယာ တစ်ခုချင်းစီအတွက် နာမည်၊ ဖော်ပြချက် နှင့် schema ကို စာရင်းပြုလုပ်ထားသည်။ နောက်ပိုင်း၌ ပစ္စည်းကိရိယာခေါ်သုံးရာတွင် အသုံးပြုမည့် အချက်အလက်ဖြစ်သည်။

#### Java

```java
// MCP ကိရိယာများကို အလိုအလျောက် ရှာဖွေ ပေးသော ကိရိယာ ပေးသူကို ဖန်တီးပါ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ကိရိယာ ပေးသူသည် အလိုအလျောက် ကိုင်တွယ်ပေးသည် -
// - MCP ဆာဗာမှ အသုံးပြုနိုင်သော ကိရိယာများ စာရင်းပြုစုခြင်း
// - MCP ကိရိယာ စည်းမျဉ်းများကို LangChain4j ပုံစံသို့ ပြောင်းလဲခြင်း
// - ကိရိယာ အလုပ်လုပ်ခြင်းနှင့် အဖြေများကို စီမံခန့်ခွဲခြင်း
```

အထက်ပါ ကုဒ်တွင် -

- MCP server မှ ပစ္စည်းကိရိယာများအား အလိုအလျောက် ရှာဖွေ မှတ်ပုံတင်ပေးသော `McpToolProvider` ကို ဖန်တီးထားသည်။
- ပစ္စည်းကိရိယာ ပေးပို့မှုနှင့် LangChain4j tool ပုံစံတို့အကြား ပြောင်းလဲပေးထားသည်။
- ဤနည်းလမ်းသည် လက်ဖြင့် ပစ္စည်းကိရိယာ စာရင်းပြုလုပ်ခြင်းနှင့် ပြောင်းလဲခြင်းကို ဖယ်ရှားပေးသည်။

#### Rust

MCP server မှ tools ခေါ်ယူခြင်းသည် `list_tools` method ဖြင့်ပြုလုပ်သည်။ `main` function ထဲတွင် MCP client ထည့်သွင်းပြီးနောက်အောက်ပါကုဒ် ထည့်ပါ -

```rust
// MCP ကိရိယာစာရင်းကို ရယူပါ။
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server ၏ စွမ်းရည်များကို LLM tool များသို့ ပြောင်းလဲခြင်း

Server ၏ စွမ်းရည်စာရင်းပြုလုပ်ပြီးနောက် အဆင့်မှာ ယင်းကို LLM နားလည်နိုင်သည့် ပုံစံအဖြစ် ပြောင်းလဲခြင်းဖြစ်သည်။ အဲ့အခါ ယင်းစွမ်းရည်များအား LLM အတွက် ကိရိယာအဖြစ်ပေးအပ်နိုင်မည်။

#### TypeScript

1. MCP Server ၏ အဖြေကို LLM အသုံးပြုနိုင်သည့် tool ပုံစံသို့ ပြောင်းရန် အောက်ပါကုဒ် ထည့်ပါ -

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema အပေါ်အခြေခံ၍ zod schema တစ်ခု ဖန်တီးပါ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // အတိအကျ "function" အမျိုးအစားအဖြစ် သတ်မှတ်ပါ
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

    အထက်ပါ ကုဒ်သည် MCP Server ၏ အဖြေကို LLM နားလည်နိုင်သော tool ဖော်ပြချက် ပုံစံသို့ ပြောင်းသည်။

1. `run` method ကို မျက်နှာစာတို့တွင် စ server စွမ်းရည်များ စာရင်းပြုလုပ်ရန် ပြင်ဆင်ပါ -

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

    အထက်ပါ ကုဒ်တွင် `run` method ကို ပြင်ဆင်ပြီး ပြန်လည်ရရှိသော အချက်များအတွင်း ကိုယ်စားပြု `openAiToolAdapter` ကို ခေါ်သုံးသည်။

#### Python

1. ပထမရန် ပြောင်းလဲမည့် function ကို ဖန်တီးပါ -

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

    `convert_to_llm_tools` function တွင် MCP tool တစ်ခု၏ အဖြေကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲသည်။

1. client ကို ပြင်ဆင်ရန် အောက်ပါအတိုင်း -

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    MCP tool အဖြေကို LLM အတွက် အစားထိုးနိုင်ရန် `convert_to_llm_tool` ကို ခေါ်သုံးထားသည်။

#### .NET

1. MCP tool ၏ အဖြေကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းရန် ကုဒ် ထည့်ပါ -

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

အထက်ပါ ကုဒ်တွင် -

- `ConvertFrom` function တစ်ခု ဖန်တီးပြီး နာမည်၊ ဖော်ပြချက်နှင့် input schema ကို လက်ခံသည်။
- `FunctionDefinition` ကို ဖန်တီးပြီး `ChatCompletionsDefinition` သို့ ပေးပို့သည်၊ ၎င်းသည် LLM နားလည်နိုင်သည်။

1. ၎င်း function ကို အသုံးပြုရန် ရှိသည့်ကုဒ်များ ပြင်ဆင်သည် -

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
// သဘာဝဘာသာစကား ပြောဆိုဆက်သွယ်မှုအတွက် Bot အင်တာဖေ့စ် တည်ဆောက်ပါ
public interface Bot {
    String chat(String prompt);
}

// LLM နှင့် MCP ကိရိယာများဖြင့် AI ဝန်ဆောင်မှုကို ဖွဲ့စည်းပါ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

အထက်ပါ ကုဒ်တွင် -

- သဘာဝဘာသာဖြင့် ဆက်သွယ်နိုင်ရန် ရိုးရှင်းသော `Bot` interface သတ်မှတ်ထားသည်။
- LangChain4j ၏ `AiServices` ကိုအသုံးပြုပြီး LLM နှင့် MCP tool provider ကို အလိုအလျောက် ပေါင်းစည်းထားသည်။
- framework သည် tool schema ပြောင်းလဲခြင်းနှင့် function ခေါ်ကြားမှုကို မှန်ကန်စွာ ကိုင်တွယ်ပေးသည်။
- လက်ဖြင့် စစ်ဆေးခြင်းမလိုတော့ဘဲ LangChain4j က MCP tools များကို LLM စနစ်နှင့် လက်မျက်စုံ ပြောင်းလဲပေးသည်။

#### Rust

MCP tool ၏ အဖြေကို LLM နားလည်နိုင်ရန် tool စာရင်းကို ပုံဖော်သည့် helper function တစ်ခု ထည့်ပါ။ `main` function အောက်တွင် အောက်ပါ function ကို ထည့်ပါ။ LLM ရဲ့ တောင်းဆိုမှုများတွင် အသုံးပြုမည်။

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

အဆင်ပြေပြီ၊ အသုံးပြုသူတောင်းဆိုမှုများ ကိုင်တွယ်ရန် ထပ်မံ စီစဉ်ကြရအောင်။

### -4- အသုံးပြုသူ prompt တောင်းဆိုမှု ကိုင်တွယ်ခြင်း

ကုဒ်၌ အသုံးပြုသူမှ တောင်းဆိုချက်များကို တွန်းအားထုတ် လုပ်ဆောင်ပါမည်။

#### TypeScript

1. LLM ကို ခေါ်ရန် အသုံးပြုမည့် method များ ထည့်ပါ -

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ၂။ ဆာဗာရဲ့ ကိရိယာကိုခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့အတူ အဘယ်သူမျှဆောင်ရွက်ပါ
        // လုပ်ရမည့်အရာ

        }
    }
    ```

အထက်ပါ ကုဒ်၌ -

- `callTools` method တစ်ခု ထည့်သွင်းသည်။
- method သည် LLM ၏ အဖြေကို စစ်ဆေးကာ ဘယ် tool များခေါ်ထားသည်ကို ကြည့်သည် -

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ကိရိယာကိုခေါ်ပါ
        }
        ```

- LLM အတွက် ခေါ်ရန် ပြောကြားထားလျှင် tool ကို ခေါ်သည် -

        ```typescript
        // ၂။ ဆာဗာရဲ့ကိရိယာကို ခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့ တစ်ခုခုလုပ်ပါ
        // လုပ်ရန်ရှိသည်
        ```

1. `run` method ကို LLM က ခေါ်သည့် function များနှင့် `callTools` သုံးရန် ပြင်ဆင်ပါ -

    ```typescript

    // ၁။ LLM အတွက် input ဖြစ်မယ့် မက်ဆေ့ချ်တွေ ဖန်တီးပါ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // ၂။ LLM ကို ခေါ်ဆိုခြင်း
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // ၃။ LLM ရဲ့ ဖြေကြားချက်ကိုကြည့်ပြီး၊ ရွေးချယ်စရာတိုင်းမှာ tool ခေါ်ဆိုမှုရှိမရှိ စစ်ဆေးပါ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

အဆင်ပြေပါပြီ၊ ကုဒ်လုံးဝကို စုစည်းပြီး ပြပါမည် -

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
            baseURL: "https://models.inference.ai.azure.com", // နောက်တွင် ဒီ url ကို ပြောင်းလဲရန် လိုအပ်နိုင်သည်: https://models.github.ai/inference
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
          // input_schema အပေါ်အခြေပြီး zod schema ဖန်တီးပါ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // type ကို "function" အဖြစ် ထုတ်ဖော် သတ်မှတ်ပါ
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
    
    
          // 2. ဆာဗာ၏ ကိရိယာကို ခေါ်ယူပါ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ရလာဒ်နှင့် ပတ်သက်၍ အလုပ်လုပ်ပါ
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
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. LLM အဖြေကို လမ်းလျှောက်ပါ၊ ရွေးချယ်မှုတိုင်းအတွက် ကိရိယာခေါ်ဆိုမှုရှိမရှိ စစ်ဆေးပါ
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

1. LLM ခေါ်ရန် လိုအပ်သည့် import များ ထည့်ပါ -

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM ခေါ်ရန် function ထည့်ပါ -

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
            # ရွေးချယ်နိုင်သော ပါရမီတာများ
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

အထက်ဖော်ပြသည့် ကုဒ်တွင် -

- MCP server တွင်ရှာဖွေနိုင်သည့် function များကို LLM သို့ ပေးပို့ထားသည်။
- အဆိုပါ function များနှင့် LLM ကို ခေါ်သည်။
- ရလဒ်ကို စိစစ်ကာ ဘယ် function များ ခေါ်ရန်ရှိသည်ကို ကြည့်သည်။
- နောက်ဆုံးတွင် ခေါ်ရန် function များ array ဖြစ်သည်ကို pass ပေးသည်။

1. အဆင့်သတ်မှတ်ပြီး တာဝန်နှင့် client code ကို ပြင်ဆင်ပါ -

    ```python
    prompt = "Add 2 to 20"

    # LLM ကို မည်သည့်ကိရိယာများ ရှိခဲ့သည်ဆိုလျှင် မေးပါ
    functions_to_call = call_llm(prompt, functions)

    # အကြံပြုသောလုပ်ဆောင်ချက်များကိုခေါ်ပါ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

အထက်ပါ ကုဒ်တွင် -

- LLM မှ အဆိုပြုသည့် function ကို `call_tool` ဖြင့် MCP tool ခေါ်ခြင်း။
- MCP Server မှ tool ခေါ်ခြင်းရလဒ် မွာပုံနှိပ်ခြင်း။

#### .NET

1. LLM prompt တောင်းဆိုမှုကို ပြုလုပ်သည့် ကုဒ် -

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

အထက်ပါ ကုဒ်၌ -

- MCP server မှ tool များ ကောက်ယူခြင်း `var tools = await GetMcpTools()`။
- အသုံးပြုသူ prompt တစ်ခု `userMessage` သတ်မှတ်ထားသည်။
- model နှင့် tool များ ပါဝင်သော options object ထူထောင်ထားသည်။
- LLM သို့ တောင်းဆိုမှု လုပ်ဆောင်ထားသည်။

1. နောက်ဆုံးအဆင့်၌ LLM သည် function ခေါ်ရန် ထင်မြင်ပါက -

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

အထက်ပါ ကုဒ်၌ -

- function call များ စစ်ဆေးရန် loop ချထားသည်။
- အောက်ဆုံးတွင် tool ပစ္စည်း များတွင် နာမည်နှင့် arguments ထုတ်ယူပြီး MCP server တွင် tool ခေါ်၍ ရလဒ်က ထုတ်ပြခြင်း။

ကုဒ် အပြည့်အစုံ -

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
    // MCP ကိရိယာများကို အလိုအလျောက် အသုံးပြု၍ သဘာဝဘာသာစကား အမိန့်များကို အကောင်အထည်ဖော်ပါ။
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

အထက်ပါ ကုဒ်၌ -

- MCP server tools များနှင့် သဘာဝဘာသာ prompt များ ဖြင့် ဆက်သွယ်ထားသည်။
- LangChain4j framework သည်
  - အသုံးပြုသူ prompt များအား tool ခေါ်ခြင်းအဖြစ် ဖော်ပြသည့်
  - LLM အမြင်ဖြင့် MCP tools များကို ခေါ်သော
  - LLM နှင့် MCP server ကြား ဆက်စပ်ပုံစံကို ကိုင်တွယ်သော
- `bot.chat()` method သည် MCP tools ဆောင်ရွက်မှု ရလဒ်ဖြင့် သဘာဝဘာသာ ဖြေကြားမှုများ ပြန်ပေးသည်။
- ၎င်းနည်း ပေါင်းစပ်မှုဖြင့် အသုံးပြုသူများသည် MCP အောက်ခံပုံစံကို မသိဘဲ အဆက်အသွယ်ပြုနိုင်သည်။

ပြည့်စုံသော ကုဒ် နမူနာ -

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

အဓိကအလုပ်များမှာ ဒီနေရာတွင် ဖြစ်သည်။ အရင်ဆုံး အသုံးပြုသူ prompt ဖြင့် LLM ကို ခေါ်ပြီး ရလဒ်ခံယူပါမည်။ ထို့နောက် ပြန်လည် စစ်ဆေး၍ tool ခေါ်ရန် လိုအပ်ပါက များကို ခေါ်တယ်။ ထိုနည်းဖြင့် LLM နှင့် ဆက်သွယ်မှုကို ဆက်လက်ပြုလုပ်ပြီး နောက်ဆုံးတွင် အဆုံးသတ်သော စကားဝိုင်း ရရှိပါသည်။

LLM အတိုးအကျယ် တောင်းဆိုမှုများ ဖြစ်လိမ့်မည်ဖြစ်သောကြောင့် LLM ကို ခေါ်သည့် function တစ်ခု ဖန်တီးပါ။ `main.rs` ဖိုင်တွင် အောက်ပါ function ထည့်ပါ -

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

ဤ function သည် LLM client, message များ (အသုံးပြုသူ prompt အပါအဝင်), MCP server မှ tools များ အား ယူ၍ LLM သို့ တောင်းဆိုမှု ပေးပို့ပြီး ပြန်လည် ရရှိသည့် အဖြေကို ပြန်ပေးပါသည်။
LLM မှပြန်လာသောတုံ့ပြန်ချက်တွင် `choices` အစုအဝေးတစ်ခု ပါဝင်လိမ့်မည်။ `tool_calls` တစ်ခုခုပါရှိမရှိ စစ်ဆေးရန်အတွက် ရလဒ်ကို ပြန်လည်လုပ်ဆောင်ရန်လိုအပ်ပါသည်။ ၎င်းသည် LLM မှ ကျွန်ုပ်တို့အား အထူးသတ်မှတ်ထားသော tool တစ်ခုကို arguments နှင့်အတူ ခေါ်ရန်တောင်းဆိုနေသည်ကို အသိပေးပါသည်။ LLM ၏ တုံ့ပြန်ချက်ကို ကိုင်တွယ်ရန် ဖန်တီးထားသော function ကို သင့် `main.rs` ဖိုင် အောက်ဆုံးတွင် ထည့်ရန် အောက်ပါကုဒ်ကို ထည့်ပါ-

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
        messages.push(message.clone()); // အကူအညီပေးသူစာသား ထည့်သွင်းပါ

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

            // ကိရိယာရလဒ်ကို စကားပြောစဉ်များထဲသို့ ထည့်သွင်းပါ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ကိရိယာရလဒ်များဖြင့် ဆက်လက်စကားပြောပါ
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

`tool_calls` ရှိပါက၊ tool အချက်အလက်များကို ရှာထုတ်ပြီး MCP server သို့ tool request ဖြင့်ခေါ်ဆိုကာ ရလဒ်များကို စကားဝိုင်း message များထဲသို့ ထည့်သွင်းသည်။ ထို့နောက် စကားဝိုင်းကို LLM ဖြင့် ဆက်လက်လုပ်ဆောင်ပြီး message များသည် assistant ၏ တုံ့ပြန်ချက်နှင့် tool ခေါ်စဉ်ရလဒ်များဖြင့် update ခြင်းခံရသည်။

LLM မှ MCP ခေါ်ယူမှုများအတွက် ပြန်လာသော tool call အချက်အလက်များကို ထုတ်ယူရန် အကူအညီ function နောက်ထပ်တစ်ခုကို `main.rs` ဖိုင် အောက်ဆုံးတွင် ထည့်သွင်းမည်-

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

အပိုင်းအားလုံး ကျင့်သုံးပြီးဖြစ်သောကြောင့်၊ ပထမဆုံး အသုံးပြုသူ prompt ကို ကိုင်တွယ်ပြီး LLM ကို ခေါ်ယူနိုင်ပါပြီ။ `main` function ကို အောက်ပါကုဒ်ဖြင့် update ခြင်း-

```rust
// စက်ကိရိယာခေါ်ဆိုမှုများနှင့် LLM စကားပြောခြင်း
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

ဤသည်က LLM ကို ပထမဆုံး အသုံးပြုသူ prompt ဖြင့် ၂ နှစ်ခွဲ၏ ပေါင်းချိတ် ရှာဖွေစေပြီး တုံ့ပြန်ချက်ကို dynamic tool calls ကို လုပ်ဆောင်ရန် စစ်ဆေးပေးပါမည်။

အလွန်ကောင်းပါပြီ၊ သင်လုပ်နိုင်ခဲ့ပြီ!

## တာဝန်

လေ့ကျင့်ခန်းမှ ကုဒ်ကိုယူပြီး server ကို တခြား tools များဖြင့် တိုးချဲ့ဆောက်လုပ်ပါ။ ထို့နောက် exercise ကဲ့သို့ client တစ်ခုကို LLM နှင့်ဖန်တီးပြီး မတူညီသော prompts များဖြင့် စမ်းသပ်၍ server tools များအားလုံး dynamic လုပ်ဆောင်သည့်အတိုင်း စစ်ဆေးပါ။ ဒီ client ဖန်တီးနည်းသည် end user ကို ကြိုတင် client command တွေမလိုဘဲ prompt များ အသုံးပြု၍ MCP server ကို ခေါ်စရာမလိုဘဲ အထူးကောင်းမွန်သော အသုံးပြုသူ အတွေ့အကြုံ ပေးနိုင်သည်။

## ဖြေရှင်းချက်

[Solution](/03-GettingStarted/03-llm-client/solution/README.md)

## အဓိက သင်ခန်းစာများ

- LLM ကို client တွင် ထည့်သွင်းခြင်းသည် MCP Servers နှင့် အသုံးပြုသူများ ၏ ထိတွေ့မှုကို ကောင်းမွန်စေသည်။
- MCP Server ၏ တုံ့ပြန်ချက်ကို LLM သိရှိနိုင်သည့် ပုံစံသို့ ပြောင်းလဲပေးရန် လိုအပ်ပါသည်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## နောက်ထပ် အရင်းအမြစ်များ

## နောက်ဆုံး သွားရန်

- နောက်တစ်ဆင့်: [Visual Studio Code ဖြင့် server ကို သုံးခြင်း](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ကျူးကပ်ချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဆိုင်ရာဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) မှ အသုံးပြုပြီး ဘာသာပြန်ထားပါသည်။ တိကျမှန်ကန်မှုကို ကြိုးစားထားပေမယ့်၊ ဆက်တိုက်လုပ်သော ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သိရှိပါရန် အရေးကြီးသည်။ မူရင်းစာရွက်စာတမ်း သီးသန့်ဘာသာစကားဖြင့် ရေးသားထားသည့်ပုံစံကိုသာ အတည်ပြုရမည့် အရင်းအမြစ်အဖြစ် ယူဆရမည်ဖြစ်သည်။ အရေးပါသော သတင်းအချက်အလက်များအတွက် ကိုယ်ပိုင်အရည်အချင်းရှိ လူသား ဘာသာပြန်ဆရာတစ်ဦးမှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်နိုင်သည့် နားလည်မှုမှားယွင်းမှုများ သို့မဟုတ် မွားယွင်းစွာ အဓိပ္ပာယ်ဖွင့်ဆိုမှုများအတွက် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->