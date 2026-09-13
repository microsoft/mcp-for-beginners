# LLM ဖြင့် client တစ်ခု ဖန်တီးခြင်း

> [!NOTE]
> Java client ဥပမာများသည် legacy HTTP+SSE သယ်ယူပို့ဆောင်မှုမှတဆင့်ချိတ်ဆက်ပြီး
> MCP `2025-11-25` SDK API များကို ရည်ရွယ်ထားပါသည်။ အသစ်သော remote client များအတွက် `2026-07-28`-ကိုက်ညီသော SDK နှင့်
> Streamable HTTP ကို သုံးပါ။

ယခုအထိ server နှင့် client တစ်ခုလုံးဖန်တီးပုံကို ကြည့်ရှုခဲ့ပြီး ဖြစ်သည်။ client မှ server ကို တိုက်ရိုက် ခေါ်ဆို၍ ၎င်း၏ကိရိယာများ၊ အရင်းအမြစ်များနှင့် prompt များကို စာရင်းပြုစုခဲ့သည်။ သို့သော်၊ ၎င်းနည်းလမ်းသည် လက်တွေ့အသုံးပြုရန် မသင့်တော်သေးပါ။ သင့်အသုံးပြုသူများသည် agentic ဒေသအတွင်း နေထိုင်ကြပြီး prompt များကို အသုံးပြု၍ LLM နှင့် ဆက်သွယ်ချင်ကြသည်။ သူတို့သည် MCP နှင့် ကိုယ်ပိုင်စွမ်းရည်များကို သိမ်းဆည်းမည်ကို မသင့်တော်ကြဘူး; ၎င်းတို့ သဘာဝဘာသာစကားဖြင့် ဆက်သွယ်လိုကြသည်။ ဒါဆို ကြုံရသောပြဿနာကို ကျွန်ုပ်တို့ ဘယ်လိုဖြေရှင်းမလဲ? ဖြေရှင်းချက်မှာ client တွင် LLM တစ်ခု ထည့်ခြင်း ဖြစ်သည်။

## အနှစ်ချုပ်

ဒီသင်ခန်းစာတွင် client တွင် LLM တစ်ခု ထည့်သွင်းခြင်းကို အာရုံစိုက်ပြီး အသုံးပြုသူအတွက် ပိုကောင်းမွန်သော အတွေ့အကြုံ ပေးပုံကို ပြသပါမည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးချိန်တွင်၊ သင်သည် အောက်ပါအရာများကို နားလည်နိုင်ပါလိမ့်မည်။

- LLM ပါရှိသော client တစ်ခု ဖန်တီးနိုင်ရန်။
- MCP server ကို LLM သုံး၍ အဆင်ပြေစွာ ဆက်သွယ်နိုင်ရန်။
- Client ဘက်တွင် အသုံးပြုသူအတွက် ပိုကောင်းမွန်သော အတွေ့အကြုံ ပံ့ပိုးနိုင်ရန်။

## နည်းလမ်း

ကျွန်ုပ်တို့ လိုအပ်သော နည်းလမ်းကို ဖော်ထုတ်ကြည့်ရအောင်။ LLM ထည့်သွင်းခြင်းမှာ လွယ်ကူသလို၊ ကျွန်ုပ်တို့ အမှန်တကယ် ဘယ်လိုလုပ်မလဲ?

client မှ server ဆီ ဆက်သွယ်ပုံသည် အောက်ပါအတိုင်း ဖြစ်ပါသည်-

1. Server နှင့် ချိတ်ဆက်မှု တည်ဆောက်ခြင်း။

1. စွမ်းဆောင်ရည်များ၊ prompt များ၊ အရင်းအမြစ်များနှင့် ကိရိယာများကို စာရင်းပြုစုပြီး, ၎င်းတို့၏ schema ကို သိမ်းဆည်းခြင်း။

1. LLM တစ်ခု ထည့်သွင်းပြီး သိမ်းဆည်းထားသော စွမ်းဆောင်ရည်များနှင့် schema များကို LLM နားလည်သော ပုံစံဖြင့် ပေးပို့ခြင်း။

1. အသုံးပြုသူ၏ prompt ကို client မှ စာရင်းပြုစုပေးထားသော ကိရိယာများနှင့်အတူ LLM သို့ ပေးပို့၍ ကိုင်တွယ်ခြင်း။

အရမ်းကောင်းပါတယ်၊ အထက်တွင် ကျွန်ုပ်တို့ လုပ်ဆောင်နိုင်မည့် နည်းလမ်း အဆင့်မြင့်အရည်အချင်း အနေဖြင့် နားလည်သွားပြီ၊ အောက်တွင် စမ်းသပ်ကြည့်မယ်။

## လေ့ကျင့်ခန်း: LLM ပါရှိသော client ဖန်တီးခြင်း

ဒီလေ့ကျင့်ခန်းတွင် ကျွန်ုပ်တို့ client သို့ LLM တစ်ခု ထည့်သွင်းပုံ သင်ယူပါမည်။

### GitHub Personal Access Token ဖြင့် အတည်ပြုခြင်း

GitHub token တစ်ခု ဖန်တီးရာမှာ လွယ်ကူသည်။ ဒီလိုလုပ်နိုင်ပါသည်။

- GitHub Settings သို့ သွားပါ – ပေါ်ခေါက်ညာဘက်ထိပ်မှ မိမိရဲ့ profile ပုံကို နှိပ်ပြီး Settings ကို ရွေးလိုက်ပါ။
- Developer Settings သို့သွားပါ – ရှုပ်ထွေးနေပြီး Developer Settings ကို နှိပ်ပါ။
- Personal Access Tokens ကို ရွေးချယ်ပါ – Fine-grained tokens ကို နှိပ်ပြီး Generate new token ကို နှိပ်ပါ။
- Token ကို စီစဉ်ပါ – မှတ်ချက်တစ်ခုထည့်၍ သက်တမ်းကုန်ဆုံးရက်စွဲထားပြီး လိုအပ်သော scopes (ခွင့်ပြုချက်များ) ကို ရွေးပါ။ ဒီမှာ Models permission ကို ထည့်သွင်းရန် သေချာပါစေ။
- Token ကို Generate လုပ်ပြီး ကူးယူပါ – Generate token ကို နှိပ်ပြီး ပြီးနောက် တစ်ဖန် မမြင်နိုင်တော့ဘဲ Copy ပြုလုပ်ထားပါ။

### -1- Server နှင့် ချိတ်ဆက်ခြင်း

ပထမဦးဆုံး ကျွန်ုပ်တို့ client ကို ဖန်တီးကြပါစို့။

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // စကိမားအတည်ပြုရေးအတွက် zod ကို သွင်းကုဒ်ထည့်ပါ

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

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည် -

- လိုအပ်သော library များကို import ပြုလုပ်ထားသည်
- client နှင့် LLM နှစ်ခုကို စီမံခန့်ခွဲရန် `client` နဲ့ `openai` ဆိုသော member နှစ်ခုပါသော class တစ်ခု ဖန်တီးထားသည်။
- GitHub Models ကို အသုံးပြုရန်အတွက် LLM instance ကို `baseUrl` သတ်မှတ်၍ inference API ကို ပြုလုပ်ထားသည်။

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ချိတ်ဆက်မှုအတွက် server ပါရာမီတာများ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အပြုလုပ်နိုင်သည့်ဖိုင်
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line အချက်အလက်များ
    env=None,  # ရွေးချယ်စရာ ပတ်ဝန်းကျင် အပြောင်းအလဲများ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ချိတ်ဆက်မှုကို စတင်ပါ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

အထက်ပါ ကုဒ်တွင်, ကျွန်ုပ်တို့သည်

- MCP အတွက် လိုအပ်သော library များကို import ပြုလုပ်ထားသည်
- client တစ်ခု ဖန်တီးထားသည်

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

ပထမဦးဆုံး LangChain4j dependency များကို သင့် `pom.xml` ဖိုင်ထဲတွင် ထည့်သွင်းရပါမည်။ MCP integration နှင့် OpenAI-ကိုက်ညီသော MiniMax API အသုံးပြုရန် dependency များဖြည့်ပါ။

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

သင့် MiniMax API key နှင့် (လိုအပ်ပါက) endpoint နှင့် မော်ဒယ်ကို သတ်မှတ်ပါ။
`MINIMAX_MODEL_ID` သည် `MiniMax-M3` နှင့် `MiniMax-M2.7` ကို ထောက်ပံ့သည်။ 
`OPENAI_BASE_URL` မသတ်မှတ်ပါက `MINIMAX_REGION` သည် `global_en` နှင့် `cn_zh` ကို ထောက်ပံ့သည်။

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

ဒေသအလိုက် endpoint ရွေးချယ်ရန် `OPENAI_BASE_URL` မသတ်မှတ်ပါက

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

ပြီးနောက် Java client class ကို ဖန်တီးပါ -

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

        // ဆာဗာနှင့်ချိတ်ဆက်ရန် MCP သယ်ယူပို့ဆောင်မှုဖန်တီးပါ
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // MCP ဖောက်သည်ဖန်တီးပါ
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

အထက်ပါ ကုဒ်တွင် ကျွန်ုပ်တို့သည်

- **LangChain4j dependencies** ထည့်သွင်းခဲ့သည်။ MCP integration နှင့် OpenAI-compatible MiniMax API အတွက် လိုအပ်သည်
- **LangChain4j libraries** ကို import ပြုလုပ်ခဲ့သည်။ MCP integration နှင့် OpenAI chat model အလုပ်လုပ်ရန်
- **`ChatLanguageModel`** ဖန်တီးထားသည်။ MiniMax နှင့် သင့် MiniMax API key, endpoint, ထောက်ပံ့သော မော်ဒယ် ID ဖြင့် ပြင်ဆင်ထားသည်
- **HTTP သယ်ယူပို့ဆောင်မှု စနစ်** သတ်မှတ်ထားသည်။ MCP server နှင့် ချိတ်ဆက်ရန် Server-Sent Events (SSE) အသုံးပြုသည်
- **MCP client တစ်ခု ဖန်တီးထားသည်။** Server အတွက် ဆက်သွယ်မှု ကိုင်တွယ်ရန်
- **LangChain4j Built-in MCP Support ကို အသုံးပြုသည်။** LLM နှင့် MCP server များအကြား အထောက်အကူဖြစ်စေသည်

#### Rust

ဤဥပမာသည် Rust အခြေခံ MCP server ရှိကြောင်း ဆိုလိုသည်။ မရှိပါက [01-first-server](../01-first-server/README.md) သင်ခန်းစာသို့ ပြန်သွား server ဖန်တီးပါ။

Rust MCP server ရှိပါက terminal များဖွင့်ပြီး server နှင့် ထပ်တူ တည်ရှိသော directory သို့ သွားပါ။ ထို့နောက် အောက်ပါ command ဖြင့် LLM client project အသစ်တစ်ခု ဖန်တီးပါ။

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

သင်၏ `Cargo.toml` ဖိုင်တွင် အောက်ပါ dependency များ ထည့်ပါ။

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> OpenAI အတွက် official Rust library မရှိသော်လည်း `async-openai` crate သည် [အဖွဲ့အစည်း ထိန်းသိမ်းသော library](https://platform.openai.com/docs/libraries/rust#rust) ဖြစ်ပြီး လူသုံးများသည် ၎င်းကို အသုံးပြုကြသည်။

`src/main.rs` ဖိုင်တွင် ဖော်ပြပါကုဒ်ဖြင့် အစားထိုးပါ။

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
    // အစပြုမက်ဆေ့ခ်ျ
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI client ကိုဆက်တင်လုပ်ရန်
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP client ကိုဆက်တင်လုပ်ရန်
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

    // ပြုလုပ်ရန်: MCP ကိရိယာစာရင်းထုတ်ရန်

    // ပြုလုပ်ရန်: ကိရိယာခေါ်ဆိုမှုများနှင့်အတူ LLM စကားပြောဆိုမှုရေးရန်

    Ok(())
}
```

ဤကုဒ်သည် MCP server နှင့် GitHub Models နှင့် ဆက်သွယ်မှု ပြုလုပ်သော ဆန်းသစ်သော Rust application တစ်ခု သတ်မှတ်သည်။

> [!IMPORTANT]
> အပလီကေးရှင်းကို run မပြုမီ `OPENAI_API_KEY` အပြင်ပတ်ဝန်းကျင် အလားတူ GitHub token ကို သတ်မှတ်ထားပါ။

ကောင်းပါပြီ၊ နောက်ဆုံးအဆင့်အနေဖြင့် server ၏ စွမ်းဆောင်ရည်များကို စာရင်းပြုစုကြပါစို့။

### -2- Server ၏ စွမ်းဆောင်ရည်များ စာရင်းပြုစုခြင်း

ယခု server နှင့် ချိတ်ဆက်ပြီး ၎င်း၏ စွမ်းဆောင်ရည်များကို မေးမြန်းပါမည်။

#### Typescript

တူညီသော class တွင် အောက်ပါ method များထည့်ပါ -

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ကိရိယာများစာရင်းပြတ်ခြင်း
    const toolsResult = await this.client.listTools();
}
```

အထက်ပါကုဒ်တွင် ကျွန်ုပ်တို့သည်

- Server ဆီ ချိတ်ဆက်ရန် `connectToServer` ကုဒ် ထည့်သွင်းထားသည်။
- ကျွန်ုပ်တို့၏ app flow ကို ကိုင်တွယ်ရန် `run` method ကို ဖန်တီးထားသည်။ လက်ရှိအထိ ကိရိယာများသာ စာရင်းပြုစုထားပြီး မကြာမီ အခြားအရာများလည်း ထည့်သွင်းရန်ရှိသည်။

#### Python

```python
# အသုံးပြုနိုင်သော အရင်းအမြစ်များကို စာရင်းပြုစုပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# အသုံးပြုနိုင်သော ကိရိယာများကို စာရင်းပြုစုပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

ကျွန်ုပ်တို့ ထည့်သွင်းထားသော အရာများမှာ -

- အရင်းအမြစ်များနှင့် ကိရိယာများကို စာရင်းပြုစုပြီး ထုတ်ပြန်ထားသည်။ ကိရိယာများအတွက် `inputSchema` ကိုလည်း စာရင်းပြုစုထားပြီး၊ နောက်တွင် အသုံးပြုမည်။

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


အထက်ပါကုဒ်မှာကျွန်တော်တို့သည် -

- MCP ဆာဗာပေါ်တွင်ရရှိနိုင်သောကိရိယာများကို စာရင်းပြုစုထားသည်
- ကိရိယာတိုင်းအတွက် နာမည်၊ ဖေါ်ပြချက်နှင့် ၎င်း၏ schema ကိုစာရင်းပြုစုထားသည်။ နောက်က တွေအားပိတ်ပြီးကုဒ်အနေဖြင့် ကိရိယာများကိုခေါ်ရန် အသုံးပြုမည်ဖြစ်သည်။

#### Java

```java
// MCP ကိရိယာများကို အလိုအလြောင့် ရှာဖွေသည့် ကိရိယာပံ့ပိုးသူတစ်ဦးကို ဖန်တီးပါ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ကိရိယာပံ့ပိုးသူသည် အလိုအလြောင့် စီမံခန့်ခွဲပါသည် -
// - MCP ဆာဗာမှ ရနိုင်သော ကိရိယာများ စာရင်းပြုစုခြင်း
// - MCP ကိရိယာ schema များကို LangChain4j ပုံစံသို့ ပြောင်းလဲခြင်း
// - ကိရိယာ အသုံးပြုမှုနှင့် တုံ့ပြန်ချက်များကို စီမံခန့်ခွဲခြင်း
```

အထက်ပါကုဒ်မှာကျွန်တော်တို့သည် -

- MCP ဆာဗာမှ ကိရိယာအားလုံးကို အလိုအလျောက်ရှာဖွေရန်နှင့် စာရင်းသွင်းရန် `McpToolProvider` ကိုဖန်တီးခဲ့သည်
- ကိရိယာပံ့ပိုးသူသည် MCP ကိရိယာ schema နှင့် LangChain4j ၏ ကိရိယာဖော်မတ်များအကြား လက်တွေ့ပြောင်းလဲမှုကို ကိုင်တွယ်ပေးသည်
- ဤနည်းလမ်းက ဖောင်မှတ်တမ်းနှင့် ပြောင်းလဲခြင်းလုပ်ငန်းစဉ်ကို ဖြုတ်ထားသည်

#### Rust

MCP ဆာဗာမှ ကိရိယာများကို ရယူခြင်းမှာ `list_tools` နည်းလမ်းကို သုံးသည်။ သင့်ရဲ့ `main` function ၌ MCP client ကို စီစဉ်ပြီးနောက် အောက်ပါကုဒ်ကို ထည့်သွင်းပါ-

```rust
// MCP ကိရိယာ စာရင်းရယူပါ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- ဆာဗာ၏ စွမ်းဆောင်ရည်များအား LLM ကိရိယာများသို့ ပြောင်းလဲခြင်း

ဆာဗာ၏ စွမ်းဆောင်ရည်များစာရင်းပြီးနောက် လိုအပ်ပါက LLM က သိရှိနိုင်သော ဖော်မတ်အားသို့ ပြောင်းလဲရမည်။ ပြီးလျှင် ဤစွမ်းဆောင်မှုများကို LLM အတွက် ကိရိယာများအဖြစ် ပေးပို့နိုင်မည်။

#### TypeScript

1. MCP ဆာဗာမှ တုံ့ပြန်မှုကို LLM သုံးနိုင်သော ကိရိယာဖော်မတ်သို့ ပြောင်းရန် အောက်ပါကုဒ်ကို ထည့်ပါ-

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema အခြေခံပြီး zod schema တစ်ခု ဖန်တီးပါ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // အတိအကျ type ကို "function" ဟု သတ်မှတ်ပါ
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

    အထက်ပါကုဒ်သည် MCP ဆာဗာမှ တုံ့ပြန်မှုကို ယူပြီး LLM သတိထားနိုင်သော ကိရိယာသတ်မှတ်ချက် ဖော်မတ်သို့ပြောင်းသည်။

2. နောက်တစ်ဆင့်အဖြစ် `run` နည်းလမ်းအား အပ်ဒိတ်လုပ်ကြမည်-

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

    အထက်ပါကုဒ်တွင် `run` နည်းလမ်းကို ရလဒ်များအား မြေပုံဆွဲကာ entry တစ်ခုစီအတွက် `openAiToolAdapter` ကို ခေါ်ဆိုထားသည်။

#### Python

1. ပထမဦးစွာ အောက်ပါပြောင်းလဲလိုင်းကိုဖန်တီးပါ-

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

    အထက်ပါ `convert_to_llm_tools` function တွင် MCP ကိရိယာ တုံ့ပြန်မှုကို ယူ၍ LLM သတိထားနိုင်သော ဖော်မတ်သို့ ပြောင်းလဲသည်။

2. နောက်တစ်ဆင့် client ကုဒ်ကို ဤ function ကိုအသုံးချရန် ရေးဆွဲမည်-

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    ဤနေရာတွင် MCP ကိရိယာ တုံ့ပြန်မှုကို LLM သုံးနိုင်သော ဖော်မတ်သို့ ပြောင်းရန် `convert_to_llm_tool` ကိုခေါ်ဆိုထားသည်။

#### .NET

1. MCP ကိရိယာ တုံ့ပြန်မှုကို LLM နားလည်နိုင်သော ဖော်မတ်သို့ ပြောင်းရန် ကုဒ်ထည့်ပါ-

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

အထက်ပါကုဒ်များမှာ-

- နာမည်၊ ဖော်ပြချက်နှင့် input schema ကိုယူသည့် `ConvertFrom` function ကိုဖန်တီးထားသည်။
- LLM နားလည်နိုင်သော ChatCompletionsDefinition ချိတ်ဆက်ပေးသော FunctionDefinition ကို ဖန်တီးစေသည်။

2. အခုတော့ အထက်ပါ function ကို အသုံးပြုရန် ပါရှိသောကုဒ်များအား ပြုပြင်မည်-

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
// သဘာဝဘာသာစကား ဆက်သွယ်ရေးအတွက် Bot အင်တာဖေ့စ် တည်ဆောက်ပါ
public interface Bot {
    String chat(String prompt);
}

// LLM နှင့် MCP အရည်အချင်းများဖြင့် AI ဝန်ဆောင်မှုကို ဖွဲ့စည်းပါ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

အထက်ပါကုဒ်မှာ-

- သဘာဝဘာသာစကားနဲ့ ဆက်သွယ်ရန် `Bot` interface ကို သတ်မှတ်ထားသည်
- LangChain4j ၏ `AiServices` ကို အသုံးပြု၍ LLM နှင့် MCP ကိရိယာပံ့ပိုးသူကို အလိုအလျောက်ချိတ်ဆက်ထားသည်
- ဖောင်ခွဲခြားမှု နှင့် function ခေါ်ဆိုမှုအား Framework များက နောက်ကွယ်မှ ကိုင်တွယ်ပေးသည်
- ဤနည်းလမ်းက လက်တွေ့ကိရိယာ ဖော်ပြနည်းကို ဖယ်ရှားပြီး MCP ကိရိယာများနှင့် LLM အညီရဲ အချက်အလက်ပြောင်းလဲမှုအား LangChain4j ပြုလုပ်ပေးသည်

#### Rust

MCP ကိရိယာတုံ့ပြန်မှု ကို LLM နားလည်နိုင်သော ဖော်မတ်သို့ ပြောင်းရန် ကူညီပေးမည့် function တစ်ခုကို `main.rs` မှာ `main` function အောက်မှာ ထည့်သွင်းပါ။ LLM အတွက် ကမ်းလှမ်းရန် အခါသုံးမည်ဖြစ်သည်-

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

ကောင်းပြီ၊ အသုံးပြုသူမေးခွန်းများကို ကိုင်တွယ်ရန် အဆင်သင့်မရှိသေးပါ၊ ဒါကြောင့် အောက်ကို ဆက်လက်လုပ်ဆောင်ကြမည်။

### -4- အသုံးပြုသူ အသုံးအကြံ မေးမြန်းချက်များကို ကိုင်တွယ်ခြင်း

အပိုင်းဤတွင် အသုံးပြုသူ မေးမြန်းမှုများကို ကိုင်တွယ်မည်။

#### TypeScript

1. LLM ကို ခေါ်ရန် အသုံးပြုမည့် method ကို ထည့်ပါ-

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

        // ၃။ ရလဒ်နဲ့အလုပ်လုပ်ပါ
        // လုပ်ရန်

        }
    }
    ```

    အထက်ပါကုဒ်တွင်-

    - `callTools` method ကို ထည့်သွင်းထားသည်-
    - မရပါက LLM တုံ့ပြန်မှုကို စစ်ဆေးကာ ဘယ်ကိရိယာများ ခေါ်ထားသည်ဟု တုံ့ပြန်ချက်တွင် စစ်ဆေးလျက်ရှိသည်။

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ကိရိယာကို ခေါ်ပါ။
        }
        ```

    - LLM က ခေါ်ဆိုရန် ဖော်ပြထားလျှင် ကိရိယာကို ခေါ်ဆိုသည်။

        ```typescript
        // ၂။ ဆာဗာ၏ကိရိယာကို ဖုန်းခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလာဒ်နှင့်အတူ တစ်စုံတစ်ခုလုပ်ဆောင်ပါ
        // လုပ်ရန်ရှိသည်
        ```

2. LLM ကိုခေါ်ခြင်းနှင့် `callTools` ကိုခေါ်သည့်အတွက် `run` method ကို အပ်ဒိတ်လုပ်ပါ-

    ```typescript

    // 1. LLM အတွက် input ဖြစ်မယ့် စာပိုဒ်တွေ ဖန်တီးပါ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ကို ခေါ်ယူခြင်း
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ရဲ့ ဖြေချက်ကို လျှောက်ပါ၊ ရွေးချယ်စရာ တစ်ခုချင်းစီအတွက် tool call ရှိမရှိ စစ်ဆေးပါ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ကောင်းပြီ၊ ဒါဆို အကုန်လုံးပြည့်စုံသည့်ကုဒ်ကို ကြည့်လိုက်ကြရအောင်-

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema စစ်ဆေးမှုအတွက် zod ကိုအတင်သွင်းပါ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // အနာဂတ်တွင်ဤ URL သို့ ပြောင်းလဲရန် လိုအပ်နိုင်သည်: https://models.github.ai/inference
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
          // input_schema အပေါ်မှာ zod schema တစ်ခု ဖန်တီးပါ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // အသွင်အပြင်ကို "function" ဟု တိတိကျကျ သတ်မှတ်ပါ
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
    
    
          // 2. ဆာဗာ၏ ကိရိယာကို ခေါ်ဆောင်ပါ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. ရလဒ်နှင့်အတူ အတောအတွင်းလုပ်ဆောင်ပါ
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
    
        // 3. LLM ရလဒ်ဖြတ်သန်းပါ၊ ရွေးချယ်မှုတိုင်းအတွက် ကိရိယာခေါ်ဆိုမှုရှိမရှိ စစ်ဆေးပါ
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

1. LLM ကို ခေါ်ရန် လိုအပ်သော import များကို ထည့်လိုက်ပါ-

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. နောက်တစ်ဆင့် LLM ကို ခေါ်မည့် function ကို ထည့်ပါ-

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
            # ရွေးချယ်နိုင်သော ပါရာမီတာများ
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

    အထက်ပါကုဒ်တွင်-

    - MCP ဆာဗာတွင် ရှာဖွေ၍ ပြောင်းလဲထားသော function များအား LLM သို့ ပေးပို့ထားသည်။
    - ထို့နောက် အဆိုပါ function များနဲ့ LLM ကို ခေါ်ဆိုခဲ့သည်။
    - နောက်ဆုံးတွင် ရလဒ်အပေါ် သုံးသပ်ကာ ဘာ function များကို ခေါ်ရန်ရှိသည်စစ်ဆေးသည်။
    - နောက်ဆုံး function များကို ခေါ်ရန် array ပေးပို့သည်။

3. နောက်ဆုံးအဆင့်အဖြစ် ကျွန်တော်တို့၏ main ကုဒ်ကို အပ်ဒိတ်လုပ်မည်-

    ```python
    prompt = "Add 2 to 20"

    # LLM ကို မည်သည့်ကိရိယာများရှိကြောင်း မေးပါ၊ ရှိပါက
    functions_to_call = call_llm(prompt, functions)

    # အကြံပြုထားသော function များကို ခေါ်ပါ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    အထက်ပါကုဒ်တွင် နောက်ဆုံးအဆင့်ကတော့-

    - LLM ၏ prompt အရခေါ်ရန်လိုသည့် function ဖြင့် `call_tool` မှတဆင့် MCP tool ကို ခေါ်ဆိုသည်။
    - MCP ဆာဗာသို့ ကိရိယာခေါ်ဆိုမှုရလဒ်ကို ပရင့်ထုတ်ပြသသည်။

#### .NET

1. LLM prompt မေးမြန်းချက်မောင်းနှင်ရန် အောက်ပါကုဒ်ရှင်းပြပါ-

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

    အထက်ပါကုဒ်တွင်-

    - MCP ဆာဗာမှ ကိရိယာများရယူထားသည်၊ `var tools = await GetMcpTools()`။
    - အသုံးပြုသူ prompt `userMessage` ကိုသတ်မှတ်ထားသည်။
    - မော်ဒယ်နှင့် ကိရိယာများကိုထည့်သွင်းထားသော option object ဖန်တီးထားသည်။
    - LLM ရှေ့သို့ အမိန့်တောင်းဆိုမှု ပြုလုပ်ခဲ့သည်။

2. နောက်ဆုံးအဆင့်အနေဖြင့် LLM မှ function call ဖေါ်ပြမှုရှိမရှိ စစ်ဆေးပါ-

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

    အထက်ပါကုဒ်တွင်-

    - function call များ စာရင်းအတိုင်း loop တွက်၏
    - tool call တစ်ခုစီအတွက် နာမည်နဲ့ arguments ကို ဖယ်ထုတ်ပြီး MCP client ဖြင့် MCP ဆာဗာ၏ tool ကိုခေါ်ဆိုသည်။ နောက်ဆုံး အဖြေဖြင့် ပရင့်ထုတ်ပြသသည်။

ဒီမှာ ကုဒ်ပြည့်စုံပါ-

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
    // MCP ကိရိယာများကိုအလိုအလျောက် အသုံးပြုသော သဘာဝဘာသာစကား မှတောင်းဆိုမှုများကို ဆောင်ရွက်ပါ
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

အထက်ပါကုဒ်မှာ-

- MCP ဆာဗာ tool များနှင့် သဘာဝဘာသာစကား prompt များကို ရိုးရှင်းစွာ အသုံးပြုသည်
- LangChain4j framework သည် အလိုအလျောက် ကိုင်တွယ်သည်-
  - အသုံးပြုသူ prompt များကို လိုအပ်သောအခါ tool call များသို့ ပြောင်းလဲခြင်း
  - LLM ၏ဆုံးဖြတ်ချက်အရ MCP tool များကို သတ်မှတ်၍ ခေါ်ဆိုခြင်း
  - LLM နှင့် MCP ဆာဗာအကြား ဆက်သွယ်မှုစီမံခန့်ခွဲမှု
- `bot.chat()` method သည် MCP tool run အကြောင်းအရာဖြင့် သဘာဝဘာသာစကား ပြန်ကြားချက်များ ဖန်တီးပေးသည်
- ဤနည်းလမ်းက အသုံးပြုသူများအား MCP ၏အောက်ခံရေးဆွဲမှု မလေ့လာဘဲ ကောင်းမွန်သော အသုံးပြုချက်ကို ပေးစွမ်းပေးသည်

အပြည့်အစုံကုဒ် ဥပမာ-

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


ဒီမှာအလုပ်အများစုဖြစ်ပွားပါတယ်။ ကျွန်ုပ်တို့သည် ပထမဆုံးအသုံးပြုသူ၏ prompt ဖြင့် LLM ကိုခေါ်ဆိုမည်ဖြစ်ပြီး၊ မည်သည့်ကိရိယာများကိုခေါ်ရန်လိုအပ်သည်ကိုကြည့်ရှုပြီး အကြောင်းပြန်ချက်ကိုစီမံမှာဖြစ်သည်။ လိုအပ်ပါက အဲဒီကိရိယာများကိုခေါ်ပြီး၊ Tool အခေါ်များမလိုအပ်နိုင်သောအထိနှင့် နောက်ဆုံးတုံ့ပြန်ချက်ရရှိသည်အထိ LLM နှင့်စကားပြောဆက်လက်မည်ဖြစ်သည်။

ကျွန်ုပ်တို့သည် LLM ကိုအကြိမ်ရေများစွာခေါ်ဆိုသွားမည်ဖြစ်လို့ LLM ခေါ်ဆိုမှုကို ကိုင်တွယ်မည့် function တစ်ခု ကိုသတ်မှတ်ကြရအောင်။ သင်၏ `main.rs` ဖိုင်ထဲသို့ အောက်ပါ function ကိုထည့်ပါ။

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

ဤ function သည် LLM client၊ မက်ဆေ့ချ်စာရင်း (အသုံးပြုသူ prompt အပါအဝင်)၊ MCP server မှ ကိရိယာများကိုယူပြီး LLM ထံတောင်းဆိုချက်ပို့ပြီး တုံ့ပြန်ချက်ကိုပြန်ပေးသည်။

LLM မှ ရလာသော တုံ့ပြန်ချက်တွင် `choices` ဆိုသော array ပါဝင်မည်။ ဤတွင်ပေါ်လာသော ရလဒ်ကို ဆန်းစစ်ပြီး `tool_calls` ရှိမရှိစစ်ဆေးရန်လိုအပ်သည်။ ဒါက LLM က အထူးသတ်မှတ်ထားသော ကိရိယာကို arguments တွေနဲ့ခေါ်ရန် တောင်းဆိုနေတယ်ဆိုတာကို သိအောင်လုပ်ပေးသည်။ သင့် `main.rs` ဖိုင်အောက်ခြေမှာ အောက်ပါ function ကိုသတ်မှတ်ရန် ကုဒ်ကိုထည့်ပါ။

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

    // ရနိုင်ပါက အကြောင်းအရာကို မျှဝေပါ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ကိရိယာခေါ်ဆိုမှုများကို ကိုင်တွယ်ပါ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // အကူအညီပေးစာတမ်း ထည့်ပါ

        // တစ်ခုချင်းစီသော ကိရိယာခေါ်ဆိုမှုကို စနစ်တကျ ဆောင်ရွက်ပါ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ကိရိယာရလဒ်ကို စကားများထဲ သွင်းပါ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ကိရိယာရလဒ်များဖြင့် စကားပြော ဆက်လုပ်ပါ
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

`tool_calls` ရှိပါက ကိရိယာအချက်အလက်ကိုထုတ်ယူပြီး MCP server ထံကိရိယာတောင်းဆိုမှုပို့၍ ရလဒ်များကိုစကားပြောအကြောင်းပြန်စာများထဲထည့်သည်။ ပြီးနောက် LLM နှင့်စကားပြောဆက်လက်ပြီး မက်ဆေ့ခ််စာများက assistant ၏ တုံ့ပြန်ချက်နှင့် ကိရိယာခေါ်ယူမှုရလဒ်များဖြင့် update လုပ်သည်။

LLM မှ MCP ခေါ်ယူမှုအတွက် ပြန်လည်ထုတ်ပေးသည့် tool call အချက်အလက်ကို ယူရန်အတွက် နောက်ထပ်အကူအညီ function တစ်ခုကို ထည့်မည်။ သင်၏ `main.rs` ဖိုင်အောက်ခြေတွင် အောက်ပါကုဒ်ကိုထည့်ပါ။

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

အစိတ်အပိုင်းများအားလုံးရှိသွားပြီဖြစ်၍ ပထမဆုံးအသုံးပြုသူ prompt ကို ကိုင်တွယ်ပြီး LLM ကိုခေါ်နိုင်ပြီဖြစ်သည်။ သင်၏ `main` function ကို အောက်ပါကုဒ်ဖြင့် update လုပ်ပါ။

```rust
// ကိရိယာခေါ်ဆိုမှုများနှင့်အတူ LLM စကားပြောဆိုခြင်း
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

ဒါဟာ ပထမဆုံးအသုံးပြုသူ prompt ဖြင့် LLM ကိုတောင်းဆိုကာ စုစုပေါင်းနှစ်ခုကို တွက်ချက်ပေးရန်တောင်းဆိုပြီး တုံ့ပြန်ချက်ကို process လုပ်ကာ tool calls ကို dynamic အနေနဲ့ ကိုင်တွယ်မည်ဖြစ်သည်။

အရမ်းကောင်းပါတယ်၊ သင်လုပ်နိုင်လိုက်ပြီ!

## လေ့ကျင့်မှု

လေ့ကျင့်မှုပုံမှန်အလုပ်အတွက်ရှိသည့်ကုဒ်မှ သင့် server ကို ကိရိယာများနည်းနည်းပိုများသွားအောင် တည်ဆောက်ပါ။ ပြီးနောက် ဥပမာကိုလိုက်ပြီး LLM တစ်ခုပါဝင်သည့် client တစ်ခုဖန်တီးပြီး မတူညီသော prompt များဖြင့် စမ်းသပ်ကြည့်ပါ၊ MCP server ကိုခေါ်ကြောင်းကို dynamic အဖြစ်သေချာစေရန်။ Client ဖန်တီးရာတွင် ဒီနည်းလမ်းသည် အဆုံးသတ်အသုံးပြုသူအဖို့ prompt များကိုသုံး၍ တိကျသည့် client အမိန့်များမလိုအပ်ဘဲ MCP server မည်သည်ကိုမှ သိသွားခြင်းမရှိဘဲ ကောင်းမွန်သောအသုံးပြုသူအတွေ့အကြုံပေးနိုင်သည်။

## ဖြေရှင်းချက်

[Solution](./solution/README.md)

## အဓိကယူဆချက်များ

- LLM ကို သင့် client ထဲသို့ ထည့်သွင်းခြင်းက MCP Server များနှင့် အသုံးပြုသူများ လိုက်ဖက်စွာဆက်ဆံနိုင်မှုပိုဆန်းစေသည်။
- MCP Server မှ တုံ့ပြန်ချက်ကို LLM အကြောင်းအရာသဘောနားလည်နိုင်အောင် ပြောင်းလဲပေးရန် လိုအပ်သည်။

## အပျက်အနည်းငယ်

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ထပ်ဆောင်းအရင်းအမြစ်များ

## နောက်မှာဘာလုပ်မလဲ

- နောက်ထပ်: [Visual Studio Code အသုံးပြုပြီး server ကို အသုံးပြုခြင်း](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->