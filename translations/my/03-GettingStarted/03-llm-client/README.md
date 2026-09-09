# LLM အသုံးပြု၍ client တစ်ခု ဖန်တီးခြင်း

လွန်ခဲ့သည့်အချိန်အထိ server တစ်ခုနှင့် client တစ်ခု ဖန်တီးနည်းကိုကြည့်ရှုခဲ့ပါသည်။ client သည် server ကို ထိရောက်စွာ ခေါ်တယ့်အဖြစ် tools, resources နှင့် prompts များ ဖော်ပြနိုင်ခဲ့သည်။ သို့သော် ယင်းသည် အလွန်လေ့လာသင့်သော နည်းလမ်းမဟုုတ်ပါ။ သင့်အသုံးပြုသူများသည် agentic ယူနစ်ကာလတွင် နေထိုင်ကြပြီး prompts များကို အသုံးပြုပြီး LLM နှင့် ဆက်သွယ်လိုကြပါသည်။ သူတို့သည် သင် MCP ကို သင့်ရဲ့ တိုင်းတာမှုသေတ္တာများ သိမ်းဆည်းရန် အသုံးပြုပါကြောင်း စိုးစမ်းမေးမြန်းခြင်း မရှိပါဘူး။ သူတို့သည် သဘာဝဘာသာစကား အသုံးပြုပြီး ဆက်သွယ်နိုင်ရန်မျှော်လင့်ကြသည်။ ဒါဆို ကျွန်ုပ်တို့ ဘယ်လို ဖြေရှင်းမလဲ? ဖြေရှင်းခွင့်မှာ client တွင် LLM တစ်ခု ထည့်သွင်းခြင်း ဖြစ်သည်။

## တခုချင်းအမြင်

ဒီသင်ခန်းစာတွင် သင့် client တွင် LLM တစ်ခု ထည့်သွင်းခြင်း ပေါ်ထားပြီး အသုံးပြုသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံကို ပေးနိုင်မှုကို ပြသထားသည်။

## သင်ယူလိုသည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာ အဆုံးခံရင်သိရမှာက -

- LLM ပါသော client တစ်ခု ဖန်တီးနိုင်ခြင်း။
- LLM အသုံးပြုပြီး MCP server နဲ့ ကြိုးပမ်းစွာ ဆက်သွယ်နိုင်ခြင်း။
- client ဘက်တွင် အသုံးပြုသူအတွက် ပိုကောင်းမွန်သော အတွေ့အကြုံ ပေးနိုင်ခြင်း။

## နည်းလမ်း

ကျွန်ုပ်တို့ လိုအပ်သော နည်းလမ်းကို နားလည်ကြည့်ကြစို့။ LLM တစ်ခု ထည့်သွင်းရခြင်း ခပ်သိမ်းရိုးရှင်းသော်လည်း၊ ပုံမှန်အားဖြင့် ဘယ်လို လုပ်ရမည်နည်း?

client သည် server နှင့် အောက်ပါပုံစံအတိုင်း ဆက်သွယ်မည်ဖြစ်သည်။

၁။ server နဲ့ ချိတ်ဆက်မှု တည်ဆောက်မည်။

၁။ စွမ်းရည်များ၊ prompts, resources နှင့် tools များကို စာရင်းပေးပြီး schema ကို သိမ်းဆည်းမည်။

၁။ LLM တစ်ခု ထည့်သွင်းပြီး သိမ်းဆည်းထားသည့် စွမ်းရည်များနှင့် schema များကို LLM နားလည်နိုင်သော ပုံစံဖြင့် ပေးပို့မည်။

၁။ user prompt ကို LLM ဆီသို့ ပေးပို့ပြီး client မှ စာရင်းပြထားသည့် tools များကို အသုံးပြုမည်။

ကောင်းပြီ၊ အခု ကျွန်ုပ်တို့ အခြေခံနည်းလမ်းကို နားလည်လိုက်ပြီ၊ အောက်ဖြစ်ထွန်းမှုဖြင့် စမ်းသပ်ကြည့်ကြစို့။

## လေ့ကျင့်ခန်း: LLM ပါသော client ဖန်တီးခြင်း

ဒီလေ့ကျင့်ခန်းတွင် ကျွန်ုပ်တို့ client တွင် LLM တစ်ခု ထည့်သွင်းနည်းကို သင်ယူပါမည်။

### GitHub ပုဂ္ဂလိက 접근နံပါတ် အသုံးပြု၍ အတည်ပြုခြင်း

GitHub တိုကင်တစ်ခု ဖန်တီးခြင်း သည် ရိုးရှင်းသော လုပ်ငန်းစဉ်ဖြစ်ပါသည်။ ဘယ်လို လုပ်နိုင်မလဲ:

- GitHub Settings သို့ သွားရန် – ညာဘက်အပေါ်က ကိုယ်ရေးပုံကို နှိပ်ပြီး Settings ရွေးပါ။
- Developer Settings တွင် ဝင်ရောက်ရန် – အောက်ဘက်သို့ ဆင်းပြီး Developer Settings ကို နှိပ်ပါ။
- Personal Access Tokens ရွေးချယ်ရန် – Fine-grained tokens ကိုနှိပ်ပြီး Generate new token ကိုနှိပ်ပါ။
- Token ကို ပြင်ဆင်ရန် – မှတ်ချက် ထည့်၍ သက်တမ်းကုန်ဆုံးသည့်ရက်ချိန် သတ်မှတ်၍ လိုအပ်သော scopes (ခွင့်ပြုချက်များ) ရွေးပါ။ ဒီမှာ Models permission ထည့်သွင်းရန် သေချာပါစေ။
- Token ကို ဖန်တီးပြီး ကူးယူရန် – Generate token ကိုနှိပ်ပြီး ဖန်တီးပြီးနောက် ခဏချက်အတွင်း ကူးယူထားပါ၊ ထပ်ပြီး မမြင်နိုင်ပါ။

### -1- server နဲ့ ချိတ်ဆက်ခြင်း

ရှေ့ စတင်ပြီး client ကို ဖန်တီးကြစို့။

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // စကီမာအတည်ပြုမှုအတွက် zod ကို आयातပါ။

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

အထက်ပါ ကုဒ်တွင်ကျွန်ုပ်တို့သည် -

- လိုအပ်သော libraries များ ပေါင်းထည့်ပြီး
- Client နှင့် LLM တို့ကို စီမံခန့်ခွဲနိုင်ရန် client နှင့် openai ဆိုသော members နှစ်ခုပါသော class တစ်ခု ဖန်တီးခဲ့သည်။
- inference API ကို ရည်ညွှန်းရန် baseUrl ကို သတ်မှတ်ပြီး GitHub Models ကို အသုံးပြုရန် LLM instance အတွက် ပေးထားသည်။

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ဆက်သွယ်မှုအတွက် ဆာဗာအချက်အလက်များ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အကောင်အထည်ဖော်နိုင်သော
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line အတိုင်းအတာများ
    env=None,  # ရွေးချယ်စရာ ပတ်ဝန်းကျင်အပြောင်းအလဲများ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ဆက်သွယ်မှုကို စတင်ပြီး သတ်မှတ်ပါ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

အထက်ပါ ကုဒ်တွင် -

- MCP အတွက် လိုအပ်သော libraries များ ကိုတင်သွင်းခဲ့သည်။
- Client တစ်ခု ဖန်တီးခဲ့သည်။

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

ပထမဦးစွာ LangChain4j dependencies များကို `pom.xml` တွင် ထည့်သွင်းရန် လိုအပ်သည်။ MCP integration နှင့် OpenAI-compatible MiniMax API ကို အသုံးပြုရန်အတွက် dependencies များကို ထည့်သွင်းပါ။

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

သင့် MiniMax API key နှင့် ရွေးချယ်ချင်သည့် endpoint နှင့် model ကို သတ်မှတ်ပါ။
`MINIMAX_MODEL_ID` သည် `MiniMax-M3` နှင့် `MiniMax-M2.7` ကို ထောက်ပံ့သည်။ 
`OPENAI_BASE_URL` မသတ်မှတ်ပါက, `MINIMAX_REGION` သည် `global_en` နှင့် `cn_zh` ကို ထောက်ပံ့သည်။

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

နိုင်ငံတစ်ခုကို အခြေခံပြီး endpoint ရွေးချယ်ချင်ပါက `OPENAI_BASE_URL` ကို ထည့်သွင်းရန် မလိုပါ။

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

အဲဒီနောက် Java client class ကို ဖန်တီးပါ။

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

        // ဆာဗာနှင့် ချိတ်ဆက်ရန် MCP သယ်ယူပို့ဆောင်မှု တည်ဆောက်ပါ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ဖောက်သည် တည်ဆောက်ပါ
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

အထက်ပါ ကုဒ်တွင် -

- **LangChain4j dependencies များ ထည့်သွင်းထားသည်** - MCP integration နှင့် OpenAI-compatible MiniMax API အတွက်လိုအပ်သည်။
- **LangChain4j libraries များကို တင်သွင်းထားသည်** - MCP integration နှင့် OpenAI chat model အလုပ်လုပ်မှုအတွက်။
- **`ChatLanguageModel` တစ်ခု ဖန်တီးထားသည်** - MiniMax ကိုသုံးပြီး MiniMax API key, endpoint, နှင့် ထောက်ပံ့ထားသော model ID များ သတ်မှတ်ထားသည်။
- **HTTP တို့ကို Server-Sent Events (SSE) ဖြင့် MCP server နှင့် ချိတ်ဆက်ရန် သတ်မှတ်ထားသည်**။
- **MCP client တစ်ခု ဖန်တီးထားသည်** - server နှင့် ဆက်သွယ်ရန်။
- **LangChain4j ၏ built-in MCP support ကို အသုံးပြုပြီး** - LLM နှင့် MCP servers များ အချင်းချင်း ပေါင်းပြီး လုပ်ဆောင်မှုကို လွယ်ကူစေသည်။

#### Rust

ဤဥပမာတွင် Rust အခြေခံ MCP server တစ်ခု ရပ်တည်ထားသည်ဟု အစီရင်ခံသည်။ မရှိသေးပါက [01-first-server](../01-first-server/README.md) သင်ခန်းစာသို့ ပြန်သွား၍ server တစ်ခု ဖန်တီးပါ။

သင့် Rust MCP server ရပါက terminal ဖွင့်ပြီး server ဟာရှိတဲ့ directory သို့ သွားပါ။ အောက်ပါ command ဖြင့် LLM client project အသစ်တစ်ခု ဖန်တီးပါ။

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

သင့် `Cargo.toml` ဖိုင်တွင် အောက်ပါ dependencies များ ထည့်သွင်းပါ။

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI အတွက် 공식 Rust library မရှိသော်လည်း `async-openai` crate သည် [အဖွဲ့အစည်း ထိန်းသိမ်းသော library ဖြစ်](https://platform.openai.com/docs/libraries/rust#rust) ပြည်သူများအကြိုက်အနှစ်သာရရှိသော library ဖြစ်သည်။

`src/main.rs` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ ကုဒ်ဖြင့် အစားထိုးပါ။

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
    // စတင်စာတိုက်ချက်
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI ဝန်ဆောင်မှုကို တပ်ဆင်ပါ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ဝန်ဆောင်မှုကို တပ်ဆင်ပါ
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

    // လုပ်ရန်: MCP ကိရိယာစာရင်း ရယူပါ

    // လုပ်ရန်: ကိရိယာခေါ်ယူမှုဖြင့် LLM စကားပြောချက်

    Ok(())
}
```

ဤကုဒ်သည် MCP server နှင့် GitHub Models ဆက်သွယ်ရန် ရိုးရှင်းသော Rust app တစ်ခုကို ပြင်ဆင်ထားသည်။

> [!IMPORTANT]
> GitHub token ဖြင့် `OPENAI_API_KEY` environment variable ကို သတ်မှတ်ကာ app ကို run လိုက်ပါ။

ကောင်းပြီ၊ နောက်တစ်ဆင့်အနေဖြင့် server ၏ စွမ်းရည်များ စာရင်း ပြုလုပ်ကြရအောင်။

### -2- Server စွမ်းရည်များ စာရင်းပြုလုပ်ခြင်း

အခု server နှင့် ချိတ်ဆက်ပြီး ၎င်း၏ စွမ်းရည်များကို မေးမြန်းပါမည်။

#### TypeScript

အဲဒီ class ထဲမှာ အောက်ပါ method များ ထည့်လိုက်ပါ။

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // စနစ်ပစ္စည်းများစာရင်းပြုစုခြင်း
    const toolsResult = await this.client.listTools();
}
```

အထက်ပါကုဒ်တွင် -

- server နဲ့ ချိတ်ဆက်ရန် `connectToServer` method ထည့်သွင်းထားသည်။
- app flow ကို စီမံခန့်ခွဲရန် `run` method တစ်ခု ဖန်တီးထားသည်။ အခုအထိ tools များ စာရင်းပေးရန်သာ ရေးသားထားသော်လည်း နောက်ပိုင်း ပိုများမြောက်အောင် ထပ်ထည့်ပါမည်။

#### Python

```python
# အသုံးပြုနိုင်သော အရင်းအမြစ်များ စာရင်းပြုလုပ်ပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# အသုံးပြုနိုင်သော ကိရိယာများ စာရင်းပြုလုပ်ပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ထည့်သွင်းထားသည်မှာ -

- resources နှင့် tools များကို စာရင်းပြုစုပြီး ပုံမှန် output ပေးထားသည်။ tools အတွက် `inputSchema` ကိုလည်း ပြန်လည်စာရင်းပြုစုပြီး နောက်မှာ အသုံးပြုမှာဖြစ်သည်။

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

- MCP Server တွင် အသုံးပြုနိုင်သည့် tools များကို စာရင်းပြုစုထားသည်။
- သာတူတူ tools တစ်ခုချင်းစီ၏ name၊ description နှင့် schema ကို စာရင်းပြုထားသည်။ schema ကို tools call မပြုခင် ယူအသုံးပြုမည်။

#### Java

```java
// MCP ကိရိယာများကို အလိုအလျောက် ရှာဖွေသော ကိရိယာပေးသွင်းသူ တစ်ဦး ဖန်တီးပါ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ကိရိယာပေးသွင်းသူသည် အလိုအလျောက် ကိုင်တွယ်ပေးသည်-
// - MCP server မှ ရနိုင်သော ကိရိယာများစာရင်းပြုလုပ်ခြင်း
// - MCP ကိရိယာ၏ စခရင်များကို LangChain4j ဖော်မတ်သို့ ပြောင်းလဲခြင်း
// - ကိရိယာ အကောင်အထည်ဖော်ခြင်းနှင့် တုံ့ပြန်မှုများကို စီမံခန့်ခွဲခြင်း
```

အထက်ပါ ကုဒ်တွင် -

- MCP server မှ tools များအားလုံး ကိုယ်တိုင် ရှာဖွေရန်နှင့် မှတ်ပုံတင်ရန် `McpToolProvider` တစ်ခု ဖန်တီးထားသည်။
- tool provider သည် MCP tool schema များ နှင့် LangChain4j tool format အကြား ပြောင်းလဲမှုများကို အတွင်းရေးအဝတ်ကြိုက် ချပြုထားသည်။
- ဒီနည်းလမ်းသည် လက်တွေ့ tools စာရင်းပြုစုခြင်း နှင့် ပြောင်းလဲခြင်း လုပ်ငန်းစဉ်ကို ပိုမို လွယ်ကူစေသည်။

#### Rust

MCP server မှ tools များ ရယူရန် `list_tools` method ကို အသုံးပြုပါသည်။ `main` function တွင် MCP client ဖန်တီးပြီးနောက် အောက်ပါ ကုဒ်ကို ထည့်ပါ။

```rust
// MCP ကိရိယာ စာရင်းယူပါ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server စွမ်းရည်များကို LLM tool များအဖြစ် ပြောင်းလဲခြင်း

Server စွမ်းရည်များကို စာရင်းပြုလုပ်ပြီးနောက် LLM နားလည်နိုင်သည့် ပုံစံသို့ ပြောင်းလဲရမည်။ ပြောင်းလဲပြီးနောက် ဒီတိုးတက်မှုများကို LLM အတွက် tools အဖြစ် ပေးနိုင်သည်။

#### TypeScript

၁။ MCP server response အား LLM အသုံးပြုနိုင်သော tool format သို့ ပြောင်းလဲရန် အောက်ပါ code ထည့်ပါ။

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema ကိုအခြေခံပြီး zod schema ဖြစ်အောင် ပြုလုပ်ပါ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // အမျိုးအစားကို "function" ဟု တိတိကျကျ သတ်မှတ်ပါ
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

    အထက်ပါ code သည် MCP server response ကို ယူပြီး LLM နားလည်နိုင်သော tool definition ပုံစံသို့ ပြောင်းလဲသည်။

၂။ နောက်တစ်ချိန်တွင် `run` method ကို update လုပ်၍ server စွမ်းရည်များ စာရင်းပြုလုပ်စေ မည်။

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

    အထက်ပါ code တွင် `run` method ကို update လုပ်ပြီး အရင်းအမြစ်အားလုံးကို ကြည့်ပြီး, entry တစ်ခုစီတွင် `openAiToolAdapter` ကို ခေါ်ယူထားသည်။

#### Python

၁။ အရင်ဆုံး အောက်ပါ converter function ကို ဖန်တီးပါ။

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

    အထက်ပါ function `convert_to_llm_tools` သည် MCP tool response ကို LLM နားလည်ရမည့် ပုံစံသို့ ပြောင်းလဲသည်။

၂။ အောက်တွင် function ကို အသုံးပြု၍ client code ကို update လုပ်ပါ။

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ဒီနေရာမှာ MCP tool response ကို `convert_to_llm_tool` ဖြင့် LLM ရဲ့ input အတွက် ဖြည့်ဆည်းထားသည်။

#### .NET

၁။ MCP tool response ကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် ကုဒ်ကို ထည့်ပါ။

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

- `ConvertFrom` function တစ်ခု ဖန်တီးထားပြီး၊ name, description နှင့် input schema ကို ယူသုံးသည်။
- အဆိုပါ function သည် FunctionDefinition တစ်ခု ဖန်တီးကာ ChatCompletionsDefinition သို့ ပေးပို့သည်။ ChatCompletionsDefinition သည် LLM နားလည်နိုင်သော ပုံစံ ဖြစ်သည်။

၂။ နောက်ပိုင်းတွင် ဒီ function ကို အသုံးပြုပြီး ရှိပြီးသား code ကို update လုပ်နိုင်စေခြင်း။

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
// သဘာဝဘာသာစကား ဆက်သွယ်မှုအတွက် Bot အင်တာဖေ့စ် တည်ဆောက်ပါ
public interface Bot {
    String chat(String prompt);
}

// LLM နှင့် MCP ကိရိယာများဖြင့် AI ဝန်ဆောင်မှုကို ကွန်ဖစ်ဂျာလုပ်ပါ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

အထက်ပါ ကုဒ်တွင် -

- သဘာဝဘာသာစကား ဖြင့် ဆက်သွယ်ရန် `Bot` interface ရိုးရှင်းတစ်ခု သတ်မှတ်ထားသည်။
- LangChain4j ၏ `AiServices` ကို အသုံးပြုပြီး LLM နှင့် MCP tool provider ကို အလိုအလျောက် ချိတ်ဆက်ထားသည်။
- လက်တွေ့မှာ framework သည် tool schema ပြောင်းလဲခြင်းနှင့် function ခေါ်ခြင်း များကို အလိုအလျောက် စီမံခန့်ခွဲသည်။
- ဒီနည်းလမ်းသည် MCP tools များကို LLM နှင့် ကိုက်ညီသော ပုံစံသို့ ပြောင်းလဲခြင်းကို လက်ဖြင့် ပြုလုပ်စရာ မလိုတော့ သည်။

#### Rust

MCP tool response ကို LLM နားလည်နိုင်သည့် ပုံစံသို့ ပြောင်းရန် helper function တစ်ခု ထည့်သွင်းပါမည်။ main function အောက်တွင် အောက်ပါကုဒ် ထည့်ပါ။ ဒီဖိုင်ကို LLM ကို request တင်ချင်သော အခါ ခေါ်မည်။

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

ကောင်းပြီ၊ အသုံးပြုသူ၏ အမေးအျမားများ ကိုင်တွယ်ဖို့ အဆင်သင့် ဖြစ်လာပါပြီ။

### -4- အသုံးပြုသူ၏ prompt လိုအပ်ချက်ကို ကိုင်တွယ်ခြင်း

ဒီအစိတ်အပိုင်းတွင် အသုံးပြုသူ၏ တောင်းဆိုမှုများကို ကိုင်တွယ်ပါမည်။

#### TypeScript

၁။ LLM ကို ခေါ်ရန် method တစ်ခု ထည့်ပါ။

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ၂။ ဆာဗာရဲ့ ကိရိယာကို ခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့ တစ်ခုခုလုပ်ပါ
        // လုပ်ရန်

        }
    }
    ```

    အထက်ပါ code တွင် ကျွန်ုပ်တို့ -

    - `callTools` method ကို ထည့်သွင်းထားသည်။
    - ဤ method တစ်ခုသည် LLM response ကို နားလည်ပြီး၊ ခေါ်ရန်လိုသော tools များကို စစ်ဆေးသည်။

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ကိရိယာ ခေါ်ပါ
        }
        ```

    - LLM မှ tool ခေါ်ရန် လိုအပ်ကြောင်း ပြောထားလျှင် tool ကို ခေါ်တယ်။

        ```typescript
        // ၂။ ဆာဗာ၏ကိရိယာကို ခေါ်ဆိုပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နှင့် အချို့လုပ်ဆောင်ပါ
        // လုပ်ရန် ပြင်ဆင်中
        ```

၂။ `run` method ကို LLM ကို ခေါ်ရန် နှင့် `callTools` ကို ခေါ်ရန် အသစ်ထည့်ပါ။

    ```typescript

    // 1. LLM အတွက် input ဖြစ်သော စာသားများဖန်တီးပါ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ကို ခေါ်ဆောင်ခြင်း
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM အဖြေအားလုံးကို ပြန်လည်ကြည့်ခြင်း၊ ရွေးချယ်မှု တစ်ခုချင်းစီအတွက် tool calls ရှိမရှိ စစ်ဆေးပါ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ကောင်းပြီ၊ အပြည့်အစုံကို ပြပါ။

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema သတ်မှတ်ခြင်းအတွက် zod ကို Import လုပ်ပါ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // အနာဂတ်တွင် url ကို https://models.github.ai/inference သို့ပြောင်းရန် လိုအပ်နိုင်သည်
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
          // input_schema အပေါ်မှ အခြေခံကာ zod schema တစ်ခု ဖန်တီးပါ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // type ကို "function" ဟု ဖေါ်ပြချက်ဖြင့် သတ်မှတ်ပါ
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
    
    
          // 2. ဆာဗာ၏ ကိရိယာကို ခေါ်ဆိုပါ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ရလာဒ်နှင့် အတူ တစ်စုံတစ်ရာ ပြုလုပ်ပါ
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
    
        // 3. LLM တုံ့ပြန်မှုအား ဖြတ်သန်းပြီး ရွေးချယ်မှုတိုင်းတွင် tool calls ရှိမရှိ စစ်ဆေးပါ
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

၁။ LLM ခေါ်ရန် လိုအပ်သော imports များ ထည့်ပါ။

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

၂။ LLM ကို ခေါ်ရန် function ကို ထည့်ပါ။

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

    အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည် -

    - MCP server တွင် ရှာဖွေတွေ့ရှိပြီး convert လုပ်ထားသော functions များကို LLM ဖြင့် ဆက်သွယ်သည်။
    - ထို functions များဖြင့် LLM ကို ခေါ်သည်။
    - ပြီးဆုံးမှုရှိသည့် function များကို စစ်ဆေးသည်။
    - နောက်ဆုံးတွင် ခေါ်ရမည့် function များကို စာရင်းပေးသည်။

၃။ နောက်ဆုံး အဆင့်တွင် မူလ code ကို update လုပ်ပါ။

    ```python
    prompt = "Add 2 to 20"

    # အသုံးပြုရန် ကိရိယာများရှိပါက LLM ကို မေးမြန်းပါ
    functions_to_call = call_llm(prompt, functions)

    # အကြံပြုထားသော function များကို ခေါ်ပါ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    အောက်ပါ code သည် နောက်ဆုံးအဆင့်ဖြစ်ပြီး -

    - LLM ၏ အဆိုအရ MP tool တစ်ခုကို `call_tool` ဖြင့် ခေါ်ယူသည်။
    - MCP Server ထံမှ tool ခေါ်ယူမှု ရလဒ်ကို print ထုတ်ပြသည်။

#### .NET

၁။ LLM prompt တောင်းဆိုမှုအတွက် ကိုယ်အမှုလုပ်နည်း code တစ်ပိုင်း ပြပါမည်။

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

    အထက်ပါ code တွင် -

    - MCP server (var tools = await GetMcpTools()) မှ tools များ ရယူသည်။
    - user prompt တစ်ခု သတ်မှတ်သည်။
    - model နှင့် tools များကို options object တစ်ခု အဖြစ် ဖန်တီးသည်။
    - LLM ကို တောင်းဆိုသည်။

၂။ နောက်ဆုံးအဆင့်အနေဖြင့် LLM သည် function လုပ်ဆောင်ရန် ဆုံးဖြတ်ပါက အောက်ပါအတိုင်း ပြုလုပ်သည်။

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

    အထက်ပါ code တွင် -

    - function call များစာရင်းကို loop ဖြင့်ကြည့်ပြီး
    -  တစ်ခုချင်း name နှင့် arguments ကို ခွဲထုတ်၍ MCP client အသုံးပြုပြီး MCP server တွင် tool ကို ခေါ်သည်။ နောက်ဆုံးတွင် ရလဒ်များကို print ထုတ်သည်။

အပြည့်အစုံ code -

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
    // MCP ကိရိယာများကို အလိုအလျောက် အသုံးပြု၍ သဘာဝဘာသာစကား တောင်းဆိုချက်များကို လုပ်ဆောင်ပါ။
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

အထက်ပါ code တွင် -

- MCP server tools များနှင့် သဘာဝဘာသာ prompt ဖြင့် အလွယ်တကူ ဆက်သွယ်သည်။ 
- LangChain4j framework သည် အလိုအလျောက်
  - အသုံးပြုသူ prompt များကို 필요ရင် tool call များသို့ ပြောင်းလဲသည်။
  - LLM ဆုံးဖြတ်ချက်အရ MCP tools များကို ခေါ်သည်။
  - LLM နှင့် MCP server အကြား စကားဝိုင်းကို စီမံခန့်ခွဲသည်။
- `bot.chat()` method သည် MCP tool များ လုပ်ဆောင်မှုရလဒ်ပါဝင်သည့် သဘာဝဘာသာတုံ့ပြန်မှုများ ပြန်သွားသည်။
- ဒီနည်းလမ်းသည် အသုံးပြုသူများကို MCP ၏ ရှေ့အကျိုးအစားများကို မသိချင်ပဲ တိကျ ချောမွေ့သော အတွေ့အကြုံ ပေးသည်။

ပုံမှန် code ဥပမာ -

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

အဓိကအလုပ်များသည် ဒီနေရာမှာ ဖြစ်ပါသည်။ ပထမဆုံး user prompt ကို LLM ဆီသို့ ခေါ်၍ ထုတ်လာသော ဖြေကြားချက်ကို စုပ်ယူ၍ tool call လိုအပ်မရှိချင်း ထိ တုံ့ပြန်ချက် ရရှိသည်အထိ ဆက်လက် ဆက်သွယ် ဆောင်ရွက်သည်။


LLM ကို မကြာခဏ ခေါ်ယူရမယ့်အတွက် LLM ခေါ်ယူမှုကို ကိုင်တွယ်ပေးမယ့် function တစ်ခု သတ်မှတ်ကြပါစို့။ `main.rs` ဖိုင်ထဲမှာ အောက်ပါ function ကို ထည့်ပေးပါ။

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

ဒီ function က LLM client, message အဖွဲ့လေး (အသုံးပြုသူရဲ့ prompt ပါဝင်ပြီး), MCP server မှ tools တွေကို ယူပြီး LLM ကို request ပို့ပြီး အဖြေကို ပြန်ထုတ်ပေးပါလိမ့်မယ်။

LLM ကresponse မှာ `choices` ဆိုတဲ့ array ပါလာမယ်။ ဒီရလဒ်ကို စစ်ပြီး `tool_calls` တစ်ခုခု ရှိမရှိ ကြည့်ဖို့ လိုပါမယ်။ ဒီမှာ LLM က သတ်မှတ်ထားတဲ့ tool တစ်ခုကို မည်သည့် arguments တွေနဲ့ ခေါ်သင့်ကြောင်း ပြောပြနေတယ်ဆိုတာ သိစေတယ်။ `main.rs` ဖိုင်အနိမ့်ဆုံးမှာ အောက်ပါ code ကို ထည့်ပြီး LLM response ကို ကိုင်တွယ်မယ့် function ကို သတ်မှတ်ပါ။

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
        messages.push(message.clone()); // အကူအညီပေးသူ မက်ဆေ့ဂျ် ထည့်ပါ

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

            // ကိရိယာရလဒ်ကို မက်ဆေ့ဂျ်များထဲထည့်ပါ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ကိရိယာရလဒ်များဖြင့် စကားပြောဆက်ပါ
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

`tool_calls` ရှိနေခဲ့ရင် tool အချက်အလက်တွေ ထုတ်ယူပြီး MCP server ကို အဲဒီ tool request နဲ့ ခေါ်ဆောင်ပြီး conversation messages ကို tool result တွေ နဲ့ update ပြုလုပ်ပါလိမ့်မယ်။ ဒါနဲ့ LLM နဲ့ ဆက်လက် စကားပြောခြင်း ဆက်လုပ်ပြီး assistant ရဲ့ အဖြေ နဲ့ tool call result တွေ နဲ့ messages တွေကို အသစ်ပြင်ဆင်လိမ့်မယ်။

LLM က MCP call တွေအတွက် ပြန်ထုတ်ပေးတဲ့ tool call အချက်အလက်တွေကို ထုတ်ယူဖို့ helper function တစ်ခု ထပ်ထည့်ဖို့ လိုအပ်နေပါပြီ။ `main.rs` ဖိုင်အောက်ဆုံးပိုင်းမှာ အောက်ပါ code ကို ထည့်ပေးပါ။

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

အပိုင်းအားလုံး ပြင်ဆင်ပြီးနောက်မှာ user ရဲ့ မူလ prompt ကို ကိုင်တွယ်ပြီး LLM ကိုခေါ်ယူနိုင်ပါပြီ။ `main` function ကို အောက်ပါအတိုင်း update ပြုလုပ်ပါ။

```rust
// ကိရိယာခေါ်ဆိုမှုများနှင့် LLM စကားပြောဆိုခြင်း။
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

ဒါက user ရဲ့ မူလ prompt နဲ့ LLM ကို ရှေ့ပြေးမေးခွန်းထုတ်ပြီး နှစ်ခု့နံပါတ်တို့၏ စုစုပေါင်းကို မေးမြန်းပေးတာ၊ ထို့အပြင် tool call တွေကို dynamic တွေ့တွက်ခိုင်းတာ ဖြစ်ပါတယ်။

ဒါဆို အရမ်းကောင်းပါပြီ၊ ချီးမြှင့်ပါတယ်!

## တာဝန်

လေ့ကျင့်ခန်းကနေ ကုဒ်တွေကို ယူပြီး server ကို နည်းနည်း tools တွေ များများထည့်တိုးပြီး ဖန်တီးပါ။ ပြီးရင် LLM ပါရှိတဲ့ client တစ်ခု ပြုလုပ်လိုက်ပါ၊ ပြီးကလို့ မတူညီ prompt တွေနဲ့ စမ်းသပ်ကြည့်လိုက်ပါ၊ သင့် server tools များက dynamic ဝေါဟာရကြည့်လက်ခံခံရမှု လုပ်ကိုင်နေလားဆိုတာ စစ်ဆေးနိုင်ပါပြီ။ ဒီလို client ဖန်တီးခြင်းက အသုံးပြုသူအတွက် အကောင်းမွန်ဆုံး အသုံးပြုမှုအတွေ့အကြုံလည်း ပေးနိုင်မှာဖြစ်ပြီး အသုံးပြုသူက တိကျတဲ့ client command မဟုတ်ပဲ prompt တွေနဲ့သာ အသုံးပြုလို့ရပြီး MCP server ခေါ်ဆောင်မှုကို မသိဖြစ်မှာဖြစ်ပါမယ်။

## ဖြေရှင်းချက်

[ဖြေရှင်းချက်](./solution/README.md)

## အဓိကသင်ခန်းစာများ

- LLM ကိုသင့် client ထဲ ထည့်ခြင်းက MCP Server နှင့် အသုံးပြုသူ သံသယလွတ်စွာ ဆက်သွယ်နိုင်စေတယ်။
- MCP Server ရဲ့ အဖြေကို LLM နားလည်နိုင်သည့် format ပြောင်းပေးရမှာ ဖြစ်တယ်။

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## နှီးနွယ်ရန် အရင်းအမြစ်များ

## နောက်တစ်ဆင့်

- နောက်တစ်ဆင့်: [Visual Studio Code ကို သုံးပြီး server ကို အသုံးပြုခြင်း](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->