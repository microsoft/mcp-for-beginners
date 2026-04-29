# LLM နှင့် Client တစ်ခု ဖန်တီးခြင်း

ယခုအချိန်ထိ Server နှင့် Client တို့ကို ဘယ်လိုဖန်တီးရမည်ကို ကြည့်ရှုရပြီး ဖြစ်ပါသည်။ Client သည် Server ကို အသုံးပြုနိုင်ပြီး Tools၊ Resources နှင့် Prompts များကို အထက်တွင် ဖော်ပြထားသလို ခေါ်ယူနိုင်ခဲ့သည်။ သို့သော် ၎င်းသည် အလွန်သုံးစွဲရ အဆင်ပြေသော နည်းလမ်းမဟုတ်ပါ။ မိမိအသုံးပြုသူများမှာ Agentic ကာလတစ်ခုတွင် နေထိုင်ကြပြီး Prompts များကို အသုံးပြု၍ LLM နှင့် ဆက်သွယ်ချင်ကြသည်။ ၎င်းတို့သည် MCP ကို မိမိတွေ့ရှိထားသော စွမ်းရည်များ ချထားသည်ကို ဩပေမဲ့ သဘာဝဘာသာဖြင့် ဆက်ဆံလိုကြပါသည်။ ထို့ကြောင့် ဤပြဿနာကို မည်သို့ ဖြေရှင်းနိုင်မည်သနည်း? ဖြေရှင်းချက်မှာ Client တွင် LLM ကို ထည့်သွင်းခြင်းဖြစ်သည်။

## အကြောင်းအရာအကျဉ်း

ဤသင်ခန်းစာတွင် Client တွင် LLM ထည့်သွင်းခြင်းကို အာရုံစိုက်ပြီး အသုံးပြုသူအတွက် ပိုမိုကောင်းမွန်သော အတွေ့အကြုံ များပေးနိုင်မည်ကို ဖော်ပြပါမည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာကုန်ဆုံးချိန်တွင် သင်သည် -

- LLM ဖြင့် Client တစ်ခု ဖန်တီးနိုင်မည်။
- MCP Server နှင့် LLM ဖြင့် ထိတွေ့ဆက်သွယ်နိုင်မည်။
- Client ဆိုဒ်တွင် ထောက်ပံ့မှုကောင်းမွန်သော အသုံးပြုသူအတွေ့အကြုံ ပံ့ပိုးနိုင်မည်။

## နည်းလမ်း

ကျွန်ုပ်တို့ စနစ်တကျ နားလည်ရမည့် နည်းလမ်းကို ကြေငြာလိုက်ရအောင်။ LLM ထည့်သွင်းရတာရိုးရှင်းပေမယ့် စစ်မှန်တော့ မည်သို့လုပ်မလဲ?

Client သည် Server နှင့် အောက်ပါနည်းဖြင့် ဆက်သွယ်ပါလိမ့်မည်။

1. Server နှင့် ချိတ်ဆက်မှုတည်ဆောက်ပါ။

1. Server မှ စွမ်းရည်များ၊ Prompts များ၊ Resources နှင့် Tools များကို စာရင်းပေးပို့ပြီး ဒါဇုံ၏ Schema ကို သိမ်းဆည်းပါ။

1. LLM ထည့်သွင်းပြီး သိမ်းဆည်းထားသော စွမ်းရည်များနှင့် Schema များကို LLM နားလည်နိုင်သည့် ပုံစံဖြင့် ပေးပါ။

1. User ၏ Prompt ကို LLM သို့ ပေးပို့ပြီး Client ရဲ့ Tool များနှင့်အတူ ကိုင်တွယ်ပါ။

ကောင်းပြီ၊ အထက်တွင် အခြေခံအဆင့်ကို နားလည်သွားပြီ ဖြစ်လို့ အောက်မှာ လေ့ကျင့်မှုလေးကို ပြုလုပ်ကြမယ်။

## လေ့ကျင့်မှု - LLM ဖြင့် Client တစ်ခု ဖန်တီးခြင်း

ဤလေ့ကျင့်မှုတွင် Client တွင် LLM ထည့်သွင်းလုပ်ခြင်းကို သင်ယူပါမည်။

### GitHub Personal Access Token ဖြင့် ကိုယ်ပိုင်အတည်ပြုခြင်း

GitHub Token တစ်ခု ဖန်တီးခြင်းသည် လွယ်ကူသည့်လုပ်ငန်းစဉ်တစ်ခုဖြစ်သည်။ အောက်ပါ နည်းလမ်းဖြင့် ပြုလုပ်နိုင်ပါသည် -

- GitHub Settings သို့သွားရန် - ထိပ်ဆုံးညာဘက် ခုံရုံးပုံကို နှိပ်၍ Settings ကို ရွေးချယ်ပါ။
- Developer Settings သို့ ရွှေ့သွားရန် - အောက်သို့ ဆွဲချ၍ Developer Settings ကို နှိပ်ပါ။
- Personal Access Tokens ရွေးချယ်၍ Fine-grained tokens ကို နှိပ်ပြီး Generate new token ကို ရွေးပါ။
- Token ကို မှတ်သားပေးရန် Note ထည့်သွင်းခြင်း၊ သက်တမ်းကုန်ဆုံးစေနေ့ သတ်မှတ်ခြင်း၊ လိုအပ်သော Scope များ (ခွင့်ပြုချက်များ) ကို ရွေးချယ်ပါ။ ဤနောက်ဆုံးတွင် Models permission ထည့်သွင်းရမည်။
- Generate token ကို နှိပ်၍ ထွက်လာသော Token ကို ချက်ချင်း ကူးယူပါ၊ ထပ်မကြည့်နိုင်တော့ပါ။

### -1- Server နှင့် ချိတ်ဆက်ခြင်း

ပထမဦးဆုံး Client ကို ဖန်တီးကြရအောင် -

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema စစ်ဆေးမှုအတွက် zod ကိုတင်သွင်းပါ။

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

အောက်က code တွင် -

- လိုအပ်သော library များကို import လုပ်ထားသည်။
- Client နှင့် LLM ကို စီမံခန့်ခွဲရန် `client` နှင့် `openai` ဟူသော member ၂ ယောက်ပါပြီး class တစ်ခု ဖန်တီးထားသည်။
- GitHub Models ကို အောက်ခံ inference API သို့ `baseUrl` ဖြင့် ဆက်သွယ်စေရန် LLM instance ကို သတ်မှတ်ထားသည်။

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ဆက်သွယ်မှုအတွက် ဆာဗာမီတာတွေ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အကောင်အထည်ဖော်နိုင်သော
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line အချက်များ
    env=None,  # ရွေးချယ်စရာ ပတ်ဝန်းကျင် အပြောင်းအလဲများ
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ဆက်သွယ်မှု စတင်တည်ဆောက်ပါ
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

အောက်က code တွင် -

- MCP အတွက် လိုအပ်သော library များကို import လုပ်ထားသည်။
- Client တစ်ခု ဖန်တီးထားသည်။

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

ပထမဦးဆုံး `pom.xml` တွင် LangChain4j dependencies များ ထည့်သွင်းရမည်။ MCP ပေါင်းစည်းမှုနှင့် GitHub Models ကို Support ပြုလုပ်ရန် အောက်ပါ dependency များ ထည့်သွင်းပါ။

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

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // GitHub မော်ဒယ်များကို အသုံးပြုရန် LLM ကို ဆက်တင်ပြုလုပ်ပါ
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // ဆာဗာနှင့် ချိတ်ဆက်ရန် MCP ပို့ဆောင်ရေးကို ဖန်တီးပါ
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

အောက်ပါ အချက်အလက်များဖြင့် -

- LangChain4j dependencies များ ထည့်သွင်းပြီး MCP ပေါင်းစည်းမှု၊ OpenAI client နှင့် GitHub Models ကို စီမံသည်။
- LangChain4j library များကို import လုပ်ပြီး MCP လုပ်ဆောင်ချက်များနှင့် OpenAI chat model ကို အသုံးပြုသည်။
- GitHub token ဖြင့် GitHub Models ကို သတ်မှတ်ထားသော ChatLanguageModel တစ်ခု ဖန်တီးသည်။
- Server Sent Events (SSE) ကို အသုံးပြု၍ MCP server နှင့် HTTP transport တည်ဆောက်ထားသည်။
- MCP client ကို ဖန်တီးပြီး Server နှင့် ဆက်သွယ်ခြင်းများ စီမံထားသည်။
- LangChain4j built-in MCP support ကို အသုံးပြု၍ LLM နှင့် MCP server ပေါင်းစည်းမှု လွယ်ကူစေသည်။

#### Rust

ဤဥပမာသည် Rust မူရင်း MCP server တစ်ခု ရှိတဲ့ အခြေအနေကို အခြေခံသည်။ မရှိသေးပါက [01-first-server](../01-first-server/README.md) သို့ ပြန်သွားဖတ်ရယူပြီး Server ဖန်တီးပါ။

Rust MCP server ရှိသည့် ဒိုင်ရက်ထရီကို Terminal ဖြင့် ဖွင့်ပြီး အောက်ပါ command ဖြင့် LLM Client Project အသစ်တစ်ခု ဖန်တီးပါ။

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

`Cargo.toml` တွင် အောက်ပါ dependency များ ထည့်ပါ။

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]  
> OpenAI အတွက် အတည်ပြု Rust library မရှိသေးပေမယ့် `async-openai` crate သည် [အသိုင်းအဝိုင်းထိန်းသိမ်းထားသော library](https://platform.openai.com/docs/libraries/rust#rust) တစ်ခုဖြစ်သည်။

`src/main.rs` ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ code ဖြင့် အစားထိုးပါ။

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

    // OpenAI ဖောက်သည်ကို ပြင်ဆင်ပါ
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP ဖောက်သည်ကို ပြင်ဆင်ပါ
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

    // TODO: MCP ကိရိယာစာရင်းရယူပါ

    // TODO: ကိရိယာခေါ်ဆိုမှုများနှင့် LLM စကားပြောခြင်း

    Ok(())
}
```

ဤ code သည် Rust application မျိုးဆိုးတစ်ခုဖြစ်ပြီး MCP server နှင့် GitHub Models ကို ပေါင်းသုံးသော LLM ဆက်သွယ်မှုကို ပြုလုပ်သည်။

> [!IMPORTANT]  
> application ရွှေ့ရန် မတိုင်မီ `OPENAI_API_KEY` environment variable ကို GitHub token ဖြင့် သတ်မှတ်ထားရန် သေချာစေပါ။

ကောင်းပြီ၊ နောက်တစ်ဆင့်အနေဖြင့် Server ၏ စွမ်းရည်များကို စာရင်းတင်ကြမယ်။

### -2- Server စွမ်းရည်များ စာရင်းပေးပို့ခြင်း

ယခု MP Server နှင့် ချိတ်ဆက်၍ Server ၏ စွမ်းရည်များကို မေးမြန်းပါမည်။

#### TypeScript

အဆိုပါ Class ထဲတွင် အောက်ပါ method များ ထည့်သွင်းပါ။

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // ကိရိယာများကို စာရင်းပြုစုခြင်း
    const toolsResult = await this.client.listTools();
}
```

အောက်ပါ code တွင် -

- Server နှင့် ချိတ်ဆက်ရန် `connectToServer` method ထည့်သွင်းသည်။
- Application flow ကို စီမံရန် `run` method တစ်ခု ဖန်တီးထားသည်။ ယခုအချိန်တွင် Tools များစာရင်းပေးထားပေမယ့် လာမယ့်အချိန်တွင် အခြားအရာများထည့်မည်။

#### Python

```python
# အသုံးပြုနိုင်သော အရင်းအမြစ်များ ကို စာရင်းပြုစုပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# အသုံးပြုနိုင်သော စက်ပစ္စည်းများ ကို စာရင်းပြုစုပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

အောက်ပါအချက်အလက်များ ထည့်သွင်းထားသည် -

- Resources နှင့် Tools များ စာရင်းပေးပြီး 출력ထားသည်။ Tools များအတွက် `inputSchema` ကိုလည်း ထည့်သွင်းထားသည်။

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

အောက်ပါ code တွင် -

- MCP Server တွင် ရရှိနိုင်သော Tools များ စာရင်းပေးထားသည်။
- Tools တစ်ခုချင်းစီတွင် နာမည်၊ ဖော်ပြချက်နှင့် schema ကို စာရင်းပေးထားသည်။ Schema သည် လာမည့်အချိန်တွင် Tools ခေါ်ယူရာတွင် အသုံးပြုမည့် အချက်အလက်ဖြစ်သည်။

#### Java

```java
// MCP စက်များကို အလိုအလျောက် ရှာဖွေသော ကိရိယာ ပံ့ပိုးသူကို ဖန်တီးပါ
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP ကိရိယာ ပံ့ပိုးသူသည် အလိုအလျောက် ကိုင်တွယ်သည် -
// - MCP ဆာဗာမှ ရနိုင်သော ကိရိယာများ စာရင်းပြုစုခြင်း
// - MCP ကိရိယာ schemas များကို LangChain4j ပုံစံသို့ ပြောင်းလဲခြင်း
// - ကိရိယာ အလုပ်အမှု နှင့် တုံ့ပြန်မှုများကို စီမံခန့်ခွဲခြင်း
```

အောက်ပါနေရာတွင် -

- MCP Server မှ စက်တင်ထုတ်ပြီး Tools များကို ခွေ့စိတ်စစ်ဆေး၍ အလိုအလျောက် register လုပ်သော `McpToolProvider` ဖန်တီးထားသည်။
- Tool provider သည် MCP tool schema များကို LangChain4j tool ပုံစံသို့ ပြောင်းလဲခြင်းကို အတွင်းတွင် စီမံတယ်။
- ဤနည်းမှာ Tools ဘာသာပြန်ခြင်းနှင့် စာရင်းပေးပို့ခြင်းကို လက်ဖြင့် မလုပ်ပဲ ကျော်လွှားသည်။

#### Rust

MCP Server မှ Tools ရယူမှုအတွက် `list_tools` method ကို အသုံးပြုသည်။ `main` function ထဲတွင် MCP client တည်ဆောက်ပြီးနောက် အောက်ပါ code ကို ထည့်ပါ။

```rust
// MCP ကိရိယာစာရင်းကို ရယူပါ
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server စွမ်းရည်များကို LLM Tools သို့ ပြောင်းလဲခြင်း

Server စွမ်းရည်များ စာရင်းဖြင့် ရလာပြီးနောက် လုပ်ဆောင်ရမည့် နောက်တစ်ဆင့်မှာ LLM နားလည်သော ပုံစံသို့ ပြောင်းပေးခြင်းဖြစ်သည်။ ထို tools များကို LLM အတွက် အသုံးပြုနိုင်ရန် ပေးနိုင်မည်ဖြစ်သည်။

#### TypeScript

1. MCP Server response ကို LLM သုံးနိုင်သည့် Tool ပုံစံသို့ ပြောင်းလဲရန် အောက်ပါ code ကို ထည့်ပါ။

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // input_schema အပေါ်အခြေခံ၍ zod schema တစ်ခု တည်ဆောက်ပါ
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // type ကို "function" အဖြစ် ထောက်ပံ့သတ်မှတ်ပါ
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

    အထက် code တွင် MCP Server မှ ပြန်လည်ရရှိသော response ကို LLM နားလည်နိုင်သည့် Tool ပြောင်းလဲပုံသို့ ပြောင်းထားသည်။

1. `run` method ကို Server စွမ်းရည်များ စာရင်းထုတ်ရန် ပြင်ဆင်ပါ။

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

    ဤ code တွင် `run` method ကို ပြင်ဆင်ပြီး ရလာသည့် Results တစ်ခုချင်းစီအတွက် `openAiToolAdapter` ကို ခေါ်သုံးထားသည်။

#### Python

1. အရင်ဆုံး Converter function အောက်ပါအတိုင်း ဖန်တီးပါ။

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

    `convert_to_llm_tools` function တွင် MCP Tool response ကို LLM နားလည်နိုင်သည့် ပုံစံသို့ ပြောင်းပေးထားသည်။

1. Client code ကို အောက်ပါအတိုင်း ပြင်ဆင်ပါ။

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    MCP Tool response ကို LLM သိုမှတ်ပေးရန် `convert_to_llm_tool` function ကို ခေါ်သွားထားသည်။

#### .NET

1. MCP Tool response ကို LLM နားလည်နိုင်သည့် ပုံစံသို့ ပြောင်းရန် code ထည့်ပါ။

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

အောက်ပါအချက်အလက်များပါဝင်သည် -

- `ConvertFrom` function ကို name, description နှင့် input schema ဖြင့် ဖန်တီးထားသည်။
- FunctionDefinition ဖြင့် ChatCompletionsDefinition ပုံစံသို့ ပြောင်းလဲသည်။

1. ရှိပြီးသား code ကို ဒီ function ဖြင့် အသုံးချခြင်း -

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
// သဘာဝဘာသာစကားအပြန်အလှန်ဆက်သွယ်မှုအတွက် Bot မျက်နှာပြင်တစ်ခု ဖန်တီးပါ
public interface Bot {
    String chat(String prompt);
}

// LLM နှင့် MCP ကိရိယာများ ဖြင့် AI ဝန်ဆောင်မှုကို တပ်ဆင်ပါ
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

အောက်ပါအချက်အလက်များ ပါဝင်သည် -

- သဘာဝဘာသာဖြင့် ဆက်ဆံမှုအတွက် `Bot` interface သတ်မှတ်ထားသည်။
- LangChain4j `AiServices` ကို ထိတွေ့မှုအလိုက် LLM နှင့် MCP tool provider ကို အလိုအလျောက် ဆက်သွယ်ကြသည်။
- Framework မှ MCP Tool schema ပြောင်းခြင်းနှင့် Function call ကို အလိုအလျောက် စီမံသည်။
- သုံးစွဲသူအား MCP ဝန်ဆောင်မှုအကြောင်းသိရှိစေခြင်းမလိုပဲ လုပ်ငန်းစဉ်အားလုံးကို LangChain4j က တာဝန်ယူပါသည်။

#### Rust

MCP Tool response ကို LLM နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် စက်ကရိတ် function အောက်ပါပုံစံထည့်ပါ။ `main.rs` အတွင်း `main` function အောက်တွင် ထည့်သွင်းပါ။ LLM သို့ ခေါ်ယူမှုများတွင် အသုံးပြုမည်။

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

ကောင်းပြီ၊ ယခု User ၏ request များကို ကိုင်တွယ်သော ဆက်လက်လုပ်ဆောင်ချက်ကို လုပ်ကြရအောင်။

### -4- User Prompt ကို ကိုင်တွယ်ခြင်း

ဤအပိုင်းတွင် User ၏ Request များကို ကိုင်တွယ်မည်။

#### TypeScript

1. LLM ကို ခေါ်ရန် သုံးမည့် method ကို ထည့်ပါ။

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // ၂။  ဆာဗာရဲ့ ကိရိယာကိုခေါ်ပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။  ရလဒ်နဲ့အချ some လုပ်ပါ
        // လုပ်ရန် ကျန်နေသည်

        }
    }
    ```

    အောက်က code တွင် -

    - `callTools` method ထည့်သွင်းသည်။
    - LLM response ကို စစ်ဆေး၍ ကွဲပြားသော tools များ ကုန်ကျဆုံးသွားမလား စစ်ဆေးသည်။

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // ကိရိယာကို ခေါ်ပါ
        }
        ```

    - LLM မှ tool ခေါ်ရန် အဆိုရှိပါက ခေါ်ယူသည်။

        ```typescript
        // ၂။ ဆာဗာရဲ့ ကိရိယာကို ခေါ်ယူပါ
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // ၃။ ရလဒ်နဲ့ အလုပ်လုပ်ပါ
        // ပြင်ဆင်ရန်
        ```

1. `run` method ကို LLM ခေါ်ယူခြင်းနှင့် `callTools` သုံးခြင်း ပါအောင် ပြင်ဆင်ပါ။

    ```typescript

    // 1. LLM အတွက် input ဖြစ်မဲ့ message များဖန်တီးပါ
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. LLM ကိုခေါ်ဆိုခြင်း
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. LLM ရဲ့တုံ့ပြန်မှုကို စစ်ဆေးပါ၊ ရွေးချယ်မှုတိုင်းမှာ tool calls တွေရှိတာကို စစ်ဆေးပါ
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

ကောင်းပါပြီ၊ အကုန်လုံး code ကို ပြန်လည်ရှုကြည့်ပါ။

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // schema မွန္သက္ခ်က္အတြက္ zod ကို ျဖည့္သြင္းပါ

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // ေနာက္လာမည့္အခါ ဤ url ကို ေျပာင္းလဲႏိုင္သည္: https://models.github.ai/inference
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
          // input_schema ကိုေျခခံ၍ zod schema ကို တည္ေဆာက္ပါ
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // ေတာင္းဆိုခ်က္ကို ေဖာ္ျပရာတြင္ "function" အျဖစ္ သတ္မွတ္ပါ
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
    
    
          // ၂။ ဆာဗာ၏ ကိရိယာကို ခ်ိတ္ဆက္ေခၚယူပါ
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // ၃။ ရလဒ္ႏွင့္အတူ တစ္စုံတစ္ရာ ျပဳလုပ္ပါ
          // လုပ္ေပးရန္ရွိေသာ အေရးႀကီးအလုပ္
    
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
    
        // ၁။ LLM အၿပန္အလွန္ကို ဖြတ္သန္းၿပီး၊ တစ္ခုခ်င္းစီအတြက္ ကိရိယာခ့ံခ်ိတ္မှု ရွိမရွိ စစ္ေဆးပါ
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

1. LLM ခေါ်ရန် လိုအပ်သော import များ ထည့်ပါ။

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. LLM ခေါ်မည့် function ကို ထည့်ပါ။

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
            # ရွေးချယ်နိုင်သောပါရာမီတာများ
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

    အောက်က code တွင် -

    - MCP server ၌ ရှိသော functions များကို LLM သို့ ပေးပို့ပြီး
    - LLM ကို functions နှင့်အတူ ခေါ်ယူသည်။
    - ရလဒ်ကို လေ့လာ၍ Function အမည်များ ရှိပါက ခေါ်ယူရန် စစ်ဆေးသည်။
    - Function များကို မေးခွန်းအဖြေများအဖြစ် ဖြေနိုင်သည်။

1. နောက်ဆုံးအဆင့် Client ရဲ့ main code ကို ပြင်ဆင်ပါ။

    ```python
    prompt = "Add 2 to 20"

    # LLM ကိုမှာပါ၊ အကယ်၍ ရှိလျှင် စက္ကန့်တူကိရိယာတွေ ဘာတွေရှိလဲဆိုတာ
    functions_to_call = call_llm(prompt, functions)

    # အကြံပြုထားသော function များကိုခေါ်ပါ
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    အထက်ပါ code တွင် -

    - LLM ၏ ခေါ်ထုတ်ရန် ထင်ရှားသည့် function ဖြင့် MCP Tool ကို `call_tool` ဖြင့် ခေါ်ယူသည်။
    - MCP Server မှ Tool call ရလဒ်ကို 출력သည်။

#### .NET

1. LLM prompt request ပြုလုပ်ခြင်းအတွက် code များ -

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

    အောက်ပါအချက်အလက်များ ပါဝင်သည် -

    - MCP Server မှ tools များ ရယူသည်၊ `var tools = await GetMcpTools()`။
    - User prompt `userMessage` တည်ဆောက်သည်။
    - Model နှင့် Tools သတ်မှတ်ထားသည့် options object တစ်ခု ဖန်တီးသည်။
    - LLM သို့ request တင်သည်။

1. နောက်ဆုံးအဆင့် LLM မှ function call ထားသလား စစ်ဆေးခြင်း -

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

    အောက်ပါအချက်များ ပါဝင်သည် -

    - Function call များအားလုံး loop ဖြင့် စစ်ဆေးသည်။
    - Tool တစ်ခုချင်း call များတွင် name နှင့် arguments ကို ဖြိုခွဲ၍ MCP Server တွင် Tool ကို ခေါ်ယူပြီး ရလဒ် output ပြုလုပ်သည်။

အောက်တွင် အားလုံး code ထည့်ထားသည် -

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
    // MCP ကိရိယာများကို အလိုအလျောက် အသုံးပြု၍ သဘာဝဘာသာစကား တောင်းဆိုမှုများကို ဖြစ်စေပါ။
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

အောက်ပါအချက်များ ပါဝင်သည် -

- MCP Server Tools များနှင့် သဘာဝဘာသာ ဖြင့် အလွယ်တကူ ပြောဆိုနိုင်ရန် အသုံးပြုပြီး
- LangChain4j Framework မှ -

  - အသုံးပြုသူ prompt ကို လိုအပ်သလို Tool call များသို့ ပြောင်းလဲခြင်း
  - LLM ရွေးခဲ့သည့် MCP Tools ကို ခေါ်ယူခြင်း
  - LLM နှင့် MCP Server အကြား ဆွေးနွေးမှုကို စီမံခန့်ခွဲခြင်း

- `bot.chat()` မှ သဘာဝဘာသာဖြင့် ဖြေဆိုချက် ပြန်လာပြီး MCP Tool လုပ်ဆောင်ချက်များလည်း ပါနိုင်သည်။
- ၎င်းနည်းလမ်းသည် အသုံးပြုသူအား MCP backend အကြောင်း မသိပဲ အသုံးပြုခွင့်ပေးသည်။

နမူနာကုဒ်အပြည့်အစုံ -

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

အလုပ်အများဆုံး လုပ်ဆောင်မှုလည်း ဒီမှာ ဖြစ်ပါသည်။ စတင် user prompt ဖြင့် LLM ကို ခေါ်ပြီး နောက်ဆုံး LLM မှ Tool call လုပ်ရန်ရှိ/မရှိ စစ်ဆေးကာ Tool များကို ခေါ်၍ ဆက်သွယ်မှုကို ဆက်လက်လုပ်ဆောင်ပါလိမ့်မည်။

LLM ကို များစွာ ခေါ်မည့်အတွက် `main.rs` ဖိုင်၌ အောက်ပါ function ကို ထည့်ပါ။

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

ဤ function သည် LLM client, Messages (user prompt ပါဝင်), MCP Server Tools များကို လက်ခံကာ LLM သို့ Request ပို့ပြီး Response ကို ပြန်ပေးသည်။
LLM မှ ရရှိသော တုံ့ပြန်ချက်တွင် `choices` စုစည်းမှုပါရှိမည် ဖြစ်သည်။ ထိုအဖြေကို မည်သည့် `tool_calls` များ ရှိမရှိ ကြည့်ရှုရန် လိုအပ်ပါသည်။ ၎င်းသည် LLM မှ ပေးသော အချက်အလက်ဖြစ်ပြီး သတ်မှတ်ထားသော tool ကို arguments များနှင့် အသုံးပြုရန် တောင်းဆိုနေကြောင်း သိရှိရနိုင်ပါသည်။ LLM တုံ့ပြန်ချက်ကို ကိုင်တွယ်ရန် ဖိုင် `main.rs` ၏အောက်ဆုံးတွင် အောက်ပါ ကိုဒ်ကို ထည့်သွင်းပါ။

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

    // ရနိုင်ပါက မိတ္ကြိုစာတန်းပုံနှိပ်ပါ
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // ကိရိယာခေါ်ဆိုမှုများကို ကိုင်တွယ်ပါ
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // ကူညီသူစကားပို့စ် ထည့်ပါ

        // ကိရိယာခေါ်ဆိုမှုနှင့်တိုက်ရိုက်ဆောင်ရွက်ပါ
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // ကိရိယာရလဒ်ကို စကားပို့စ်များထဲ ထည့်ပါ
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // ကိရိယာရလဒ်များနှင့် စကားဝိုင်းကို ဆက်လက်ပြုလုပ်ပါ
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

`tool_calls` များရှိပါက၊ ၎င်းတွင် ပါဝင်သည့် tool အချက်အလက်ကို ကိုင်တွယ်ခြင်း၊ MCP ဆာဗာကို tool တောင်းဆိုချက်ဖြင့် ခေါ်ဆိုခြင်းနှင့် အဖြေများကို ဆက်သွယ်မှု ဆာဗာပြင်ဆင်ချက်များအား ထည့်သွင်းခြင်းတို့ ပြုလုပ်မည်ဖြစ်သည်။ ထို့နောက် LLM နှင့် ဆက်သွယ်မှု ဆက်လုပ်ပြီး သုံးစွဲသူ၏ တုံ့ပြန်ချက်နှင့် tool ခေါ်ဆိုမှု ရလဒ်များဖြင့် ဆက်သွယ်မှုများ ဖြည့်တင်းပါသည်။

LLM မှ MCP ခေါ်ဆိုမှုများအတွက် ပြန်လာသော tool call အချက်အလက်အား ထုတ်ယူရန် အကူအညီ အလုပ်လုပ်မည့် 함수များထပ်တစ်ခု ထည့်သွင်းပါမည်။ `main.rs` ဖိုင်၏ အောက်ဆုံးတွင် အောက်ပါ ကိုဒ်ကို ထည့်ပါ။

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

လိုအပ်သည့် အစိတ်အပိုင်းများအားလုံးဖြည့်စွက်ပြီးနောက်ပိုင်း၊ ပထမဆုံး သုံးစွဲသူ စကားပုံကို ကိုင်တွယ်ပြီး LLM ကို ခေါ်ဆိုနိုင်ပါပြီ။ `main` function ကို အောက်ပါ အတိုင်း အပ်ဒိတ်လုပ်ပါ။

```rust
// ကိရိယာခေါ်ဆိုမှုများပါသော LLM စကားပြောခြင်း
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

ဤအရာသည် ပထမ ဦးဆုံး သုံးစွဲသူ စကားပုံဖြင့် အဆက်အသွယ်တောင်းဆို၍ LLM ကို မေးမြန်းခြင်း ဖြစ်ပြီး၊ tool call များကို dynamic အဖြစ် ကိုင်တွယ်ပေးမည် ဖြစ်သည်။

ကောင်းပါပြီ၊ သင်ပြုလုပ်နိုင်ခဲ့ပါပြီ!

## လက်တွေ့လုပ်ဆောင်ရန်

လေ့ကျင့်ခန်းမှ ကုဒ်ကို ရယူပြီး ဆာဗာအတွက် အသုံးပြုသော tool များကို ပိုမိုတိုးချဲ့ပါ။ ထို့နောက် LLM ပါသည့် ကလိုင်း( client ) တစ်ခုကို မူလ လေ့ကျင့်ခန်းအတိုင်း ဖန်တီးပြီး အမျိုးမျိုးသော စကားပုံများဖြင့် စမ်းသပ်ပါ၊ တကယ်လည်း သင့်ဆာဗာ tool များအားလုံး dynamic အတိုင်း ခေါ်ယူနိုင်ခြင်းကို သေချာပါစေ။ ဒီလို client တည်ဆောက်ခြင်းက သုံးစွဲသူများအတွက် ပိုမိုကောင်းမွန်သည့် အသုံးပြုမှုအတွေ့အကြုံပေးနိုင်ပါသည်၊ လျှောက်လွှာ ကြောင်းအတိုင်း MCP ဆာဗာကို တိုက်ရိုက် ခေါ်ဆိုခြင်း မလိုအပ်တော့ဘဲ စကားပုံများကို အသုံးပြု၍ လွယ်ကူစွာ တိုးချဲ့နိုင်ပါသည်။

## ဖြေရှင်းချက်

[Solution](./solution/README.md)

## အဓိကယူဆချက်များ

- LLM ကို သင့် client တွင် ပေါင်းထည့်ခြင်းသည် MCP ဆာဗာများနှင့် သုံးစွဲသူများ၏ ဆက်သွယ်မှု အတွက် ပိုမိုကောင်းမွန်သော နည်းလမ်းဖြစ်သည်။
- MCP ဆာဗာဖြေရှင်းချက်ကို LLM အတွက် နားလည်နိုင်သော ပုံစံသို့ ပြောင်းလဲရန် လိုအပ်သည်။

## စမ်းသပ်မှုများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## ထပ်ဆောင်း အရင်းအမြစ်များ

## နောက်တစ်ဆင့်

- နောက်တစ်ဆင့်: [Visual Studio Code ကို အသုံးပြု၍ ဆာဗာ အသုံးပြုခြင်း](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**မှတ်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှန်ကန်မှုမရှိမှုများ ဖြစ်ပေါ်နိုင်သည်ကို သိရှိပါ။ မူရင်း စာတမ်းကို မိရိုးဘာသာဖြင့် အဓိကအရင်းအမြစ်အဖြစ် သတ်မှတ်ရမည်ဖြစ်သည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူကြီးမင်းတို့သည် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းအတွက် ဖြစ်ပေါ်လာသည့် အနားမလွတ်ဘဲ နားလည်မှုမှားမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->