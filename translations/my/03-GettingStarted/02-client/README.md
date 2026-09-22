# client တစ်ခု ဖန်တီးခြင်း

Clients ဆိုတာ MCP Server နဲ့ တိုက်ရိုက် ဆက်သွယ်ပြီး ရင်းမြစ်များ၊ ကိရိယာများ၊ နှင့် ဆွဲဆောင်ချက်များကို တောင်းယူသော စိတ်ကြိုက်လျှောက်လွှာများ သို့မဟုတ် စကရစ်တွေပါ။ သင့်ကိုယ်ပိုင် client ကိုရေးသားခြင်းသည် เซာဗာနှင့် တွဲဖက်ဆက်သွယ်ရန် ဂရပ်ဖစ်နည်းလမ်းများပေးသော inspector ကိရိယာအသုံးပြုခြင်းနှင့် မတူပဲ၊ အစီအစဉ်ဖန်တီးနိုင်သော၊ အလိုအလျောက်လုပ်ဆောင်နိုင်သော ဆက်သွယ်မှုများကို ခွင့်ပြုသည်။ ၎င်းက ဖွံ့ဖြိုးရေးသူများအား MCP ၏ စွမ်းဆောင်ရည်များကို သူတို့ရဲ့ လုပ်ငန်းစဉ်များထဲ ထည့်သွင်းနိုင်စေပြီး တာဝန်များကို အလိုအလျောက်လုပ်ဆောင်ခြင်းနှင့် သီးသန့်လိုအပ်ချက်များကို ကိုက်ညီသည့် စိတ်ကြိုက် ဖြေရှင်းချက်များ တည်ဆောက်နိုင်စေပါသည်။

## အကျဥ်းချုပ်

ဒီသင်ခန်းစာမှာ Model Context Protocol (MCP) နယ်ပယ်ထဲရှိ clients စိတ်ကူးကို မိတ်ဆက်ပေးပါမည်။ သင့်ကိုယ်ပိုင် client ကို ဘယ်လိုရေးရမလဲ၊ MCP Server မှာ ဘယ်လိုဆက်သွယ်ရမလဲ ဆိုတာ သင်လေ့လာသွားပါလိမ့်မယ်။

## သင်ယူရမည့် ရည်ရွယ်ချက်များ

ဒီသင်ခန်းစာ အဆုံးသတ်မှ ကွာလတီရှိသော client ကို သိရှိနားလည်နိုင်မှာဖြစ်ပါတယ်:

- Client တစ်ခု ဘာလုပ်နိုင်သည်ကို နားလည်ပါ။
- ကိုယ်ပိုင် client ကို ရေးသားပါ။
- MCP server နှင့် client ဆက်သွယ်စမ်းသပ်၍ server ဖြစ်နိုင်သောအတိုင်း အလုပ်လုပ်မှုကို သေချာစေပါ။

## Client ရေးသားခြင်းတွင် ဘာတွေ ပါဝင်သင့်လဲ?

Client ကိုရေးသားရန်အတွက် ကျွန်ုပ်တို့ လိုအပ်တယ်သော အချက်များမှာ:

- **မှန်ကန်သော ဖြည့်စွက်ချက်များကို သွင်းယူပါ။** ယခင်ကအသုံးပြုခဲ့သည့် စာကြည့်တိုက် နှင့် အတူသုံးသည်မှာ တူညီသော်လည်း ကွဲပြားသော ဖော်ပြချက်များဖြစ်ပါသည်။
- **Client တစ်ခု အထွက်ဦးတည်ပါ။** ၎င်းသည် client instance တစ်ခုဖန်တီးပြီး ရွေးချယ်ထားသည့် သယ်ယူပို့ဆောင်မှုနည်းလမ်းနှင့် ဆက်သွယ်ရန်ပါဝင်ပါသည်။
- **ရင်းမြစ်များ ဘာအများကြီး ပြသမလဲ ဆုံးဖြတ်ပါ။** သင့် MCP server အတွက် ရင်းမြစ်များ၊ ကိရိယာများနှင့် ဆွဲဆောင်ချက်များ ပါရှိပြီး မည်သည့်အရာကို ပြသမည်ကို ဆုံးဖြတ်ပေးပါ။
- **Client ကို အိမ်ရှင်လျှောက်လွှာနှင့် ပေါင်းစည်းပါ။** Server ၏ စွမ်းဆောင်မှုများကို သိရှိပြီးနောက်၊ အသုံးပြုသူတစ်ဦးသည် prompt သို့မဟုတ် အမိန့်တစ်ခု ရိုက်ထည့်ပါက အဆိုပါ server တွင်သက်ဆိုင်ရာ အင်္ဂါရပ်ကို ခေါ်ယူစေရန် အိမ်ရှင်လျှောက်လွှာနှင့် ပေါင်းစည်းထားရပါမည်။

အထက်ပါ အဆင့်ကြီးတွေကို နားလည်ပြီးနောက်၊ နမူနာတစ်ခုကို ကြည့်ကြပါစို့။

### နမူနာ Client တစ်ခု

ဒီနမူနာ client ကို ကြည့်ကြပါစို့။

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// ပရိုမ့်များ စာရင်းပြုစုခြင်း
const prompts = await client.listPrompts();

// ပရိုမ့်တစ်ခု ရယူရန်
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// အရင်းအမြစ်များ စာရင်းပြုစုခြင်း
const resources = await client.listResources();

// အရင်းအမြစ်တစ်ခု ဖတ်ရှုခြင်း
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ကိရိယာတစ်ခု ခေါ်ယူခြင်း
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ယခင်ကုဒ်တွင် ကျွန်ုပ်တို့လုပ်သော အရာများမှာ-

- စာကြည့်တိုက်များကို သွင်းယူခြင်း
- Client instance တစ်ခု ဖန်တီးပြီး stdio သယ်ယူပို့ဆောင်မှုထားနဲ့ ဆက်သွယ်ထားခြင်း။
- prompts, resources, tools များကို စာရင်းပြုစု၍ လုပ်ဆောင်ခြင်း။

ဒီလိုနဲ့ MCP Server နဲ့ စကားပြောနိုင်တဲ့ client တစ်ခု ရှိပါတယ်။

နောက်တစ်ခု လေ့ကျင့်ခန်းတွင် ကိုးဒ်ပုံစံ တစ်ခုစီကို အသေးစိတ်ဖေါ်ပြ သဘောပေါက်စေကြမယ်။

## လေ့ကျင့်ခန်း - Client ရေးခြင်း

အထက်ဖော်ပြခဲ့သလို ကိုးဒ်ကို ရှင်းပြပြီး စိတ်တိုင်းကျ ရေးသားကြပါစို့။

### -1- စာကြည့်တိုက်များ သွင်းယူခြင်း

လိုအပ်တဲ့ စာကြည့်တိုက်များကို သွင်းယူကြပါစို့။ client နှင့် ရွေးချယ်ထားသော သယ်ယူပို့ဆောင်မှု protocol stdio ကို ကြည့်ညွှန်းပါ။ stdio သည် သင့်ကွန်ပျူတာတွင် လည်ပတ်မည့် protocol အမျိုးအစားဖြစ်သည်။ SSE သည် နောက်ပိုင်းအခန်းတွင် ပြသပေးမည့် သယ်ယူပို့ဆောင်မှု protocol အမျိုးအစားတစ်ခုဖြစ်သည်။ ဒီအချိန်တွင်တော့ stdio နဲ့သာ ဆက်လုပ်ကြပါစို့။

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Java အတွက် MCP server မှာ ဆက်သွယ်နိုင်တဲ့ client ကို [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) မှာ အသုံးပြုထားသော Java Spring Boot စီမံကိန်း ဖွဲ့စည်းမှုဖြင့် `src/main/java/com/microsoft/mcp/sample/client/` ဖိုလ်ဒါအတွင်း `SDKClient` ဆိုတဲ့ class အသစ်ကို ဖန်တီးပြီး အောက်ပါ imports တွေ မျော်သမျှထည့်သွင်းပါ။

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

`Cargo.toml` ဖိုင်အတွက် အောက်ပါ dependencies များ ထည့်သွင်းရန် လိုပါသည်။

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

ထိုနေရာက client ကိုးဒ်တွင်လိုအပ်သည့် စာကြည့်တိုက်များကို သွင်းယူနိုင်သည်။

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

ဒီမှာ client ထုတ်လုပ်ခြင်းကို ဆက်လက်လုပ်ဆောင်ကြပါစို့။

### -2- Client နှင့် သယ်ယူပို့ဆောင်မှု အထွက်ဦးတည်မှုဖန်တီးခြင်း

သယ်ယူပို့ဆောင်မှုနှင့် client instance များဖန်တီးရန် လိုအပ်ပါသည်။

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

ယခင်ကုဒ်တွင် ကျွန်တော်တို့-

- stdio transport instance တစ်ခုဖန်တီးထားသည်။ Command နှင့် args ကို server ကိုရှာဖွေနေစဉ်လှုပ်ရှားမှုအတွက် သတ်မှတ်ထားသည်၊ ၎င်းကို client ဖန်တီးရာတွင် လိုအပ်သည်။

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Client ကို name နှင့် version ဖြင့် အသစ်ဖန်တီးထားသည်။

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Client ကို သတ်မှတ်ထားသည့် သယ်ယူပို့ဆောင်မှုနှင့် ဆက်သွယ်ထားသည်။

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ချိတ်ဆက်မှုအတွက်ဆာဗာပါရာမီတာများဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # အထ 실행နိုင်သော
    args=["run", "server.py"],  # ရွေးချယ်စရာ command line argument များ
    env=None,  # ရွေးချယ်စရာပတ်ဝန်းကျင်အသားအရစ်များ
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ချိတ်ဆက်မှုကိုစတင်ပြင်ဆင်ပါ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ယခင်ကုဒ်တွင် ကျွန်ုပ်တို့-

- လိုအပ်သော စာကြည့်တိုက်များကို သွင်းယူထားသည်။
- server parameters object တစ်ခုဖန်တီးထားသည်။ ဤ server ကို run ဖို့သုံးပြီး client နဲ့ ဆက်သွယ်ရန် ဖြစ်သည်။
- `run` ဆိုသော method တစ်ခု သတ်မှတ်ထားပြီး အဲဒါက `stdio_client` ကို ခေါ်ပြီး client session စတင်သည်။
- `asyncio.run` ထဲမှ `run` method ကိုစာရင်းဝင်နေရာအဖြစ် ဖော်ပြထားသည်။

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

ယခင်ကုဒ်တွင် ကျွန်ုပ်တို့-

- လိုအပ်သော စာကြည့်တိုက်များ သွင်းယူထားသည်။
- stdio transport ဖန်တီးပြီး client `mcpClient` ကိုဖန်တီးထားသည်။ ၎င်းကို MCP Server မှာ function များ စာရင်းပြုစု၍ ခေါ်ယူဖို့ အသုံးပြုမည်။

မှတ်ချက်- "Arguments" တွင် *.csproj* သို့မဟုတ် executable ကို ရည်ညွှန်းနိုင်သည်။

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // သင့်ဖောက်သည်လိုဂစ်ကို ဒီမှာရေးပါ
    }
}
```

ယခင်ကုဒ်တွင်ကျွန်ုပ်တို့-

- Main method ဖန်တီးပြီး MCP server လည်ပတ်နေမည့် `http://localhost:8080` ကို SSE transport ဖြင့် ပြုလုပ်ထားသည်။
- Transport ကို constructor parameter အနေနဲ့ ရယူသော client class ဖန်တီးထားသည်။
- `run` method တွင် transport သုံးပြီး synchronous MCP client တစ်ခု ဖန်တီးပြီး အဆက်အသွယ် စတင်ထားသည်။
- SSE (Server-Sent Events) transport ကို အသုံးပြုပြီး Java Spring Boot MCP servers နှင့် HTTP-based ဆက်သွယ်မှုအတွက် သင့်လျော်သည်။

#### Rust

ယခု Rust client သည် "calculator-server" နှင့် အတူ directory တည်နေရာတွင် ရှိသော sibling project အဖြစ် server ကို ယူဆမည်ဖြစ်သည်။ အောက်ပါကုဒ်သည် server ကိုစတင်ပြီး၊ ဆက်သွယ်ပေးလိမ့်မည်။

```rust
async fn main() -> Result<(), RmcpError> {
    // ဆာဗာကို မိသားစုစီမံကိန်းတစ်ခုဖြစ်တဲ့ "calculator-server" ဟုအမည်ပေးထားသော အတူတူဖိုင်ထဲရှိစီမံကိန်းဟုယူဆပါ
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: စတင်တည်ဆောက်ရန်

    // TODO: ကိရိယာများ စာရင်းပြုစုရန်

    // TODO: add tool ကို အချက်အလက်များ {"a": 3, "b": 2} ဖြင့် ခေါ်ရန်

    client.cancel().await?;
    Ok(())
}
```

### -3- Server features များစာရင်းပြုစုခြင်း

အခု client တစ်ခု ရှိနေပြီး ဖွင့်လှစ်နိုင်သော်လည်း server feature များ စာရင်း မပြသသေးပါ၊ အခုဆက်လုပ်ကြပါစို့။

#### TypeScript

```typescript
// ဖော်ပြချက်များစာရင်း
const prompts = await client.listPrompts();

// အရင်းအမြစ်များစာရင်း
const resources = await client.listResources();

// စက်ပစ္စည်းများစာရင်း
const tools = await client.listTools();
```

#### Python

```python
# အသုံးပြုနိုင်သော အရင်းအမြစ်များ စာရင်းပြပါ
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# အသုံးပြုနိုင်သော ကိရိယာများ စာရင်းပြပါ
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ဒီမှာ ရနိုင်သော resources `list_resources()` နှင့် tools `list_tools` ကို စာရင်းပြုစုပြီး ပုံနှိပ်ထုတ်ပြပါသည်။

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

အထက်မှာ server အတွက် tools များကို စာရင်းပြုစုနည်း ဥပမာဖြစ်သည်။ tool များစီအတွက် အမည်ကို ဖော်ပြပါသည်။

#### Java

```java
// ကိရိယာများကို စာရင်းပြုစု၍ ပြသပါ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ချိတ်ဆက်မှုကို စစ်ဆေးရန် ဆာဗာကို ဗွီပ်လုပ်နိုင်ပါသည်
client.ping();
```

ယခင်ကုဒ်တွင်ကျွန်ုပ်တို့-

- MCP server မှရရှိနိုင်သည့် 모든 tools များကို `listTools()` ဖြင့် ခေါ်ယူခဲ့သည်။
- server နှင့် ဆက်သွယ်မှု အခြေအနေနှင့် စစ်ဆေးရန် `ping()` ကိုအသုံးပြုသည်။
- `ListToolsResult` တွင် tools များအမည်၊ ဖော်ပြချက်နှင့် input schema စသည့် အချက်အလက်များ ထည့်သွင်းထားသည်။

အလွန်ကောင်းမွန်ပါပြီ၊ features တွေ စုဆောင်းထားပါပြီ။ ဝင်စားမည့် အချိန်မှာ မည်နှစ်သည့်အခါအသုံးပြုမလဲ? ဒီ client သည် features များကို စိတ်ကြိုက်ခေါ်ခိုင်းရမည့် ရိုးရှင်းသော client ဖြစ်သည်။ နောက်တစ်အခန်းတွင် ၎င်း၏ကိုယ်ပိုင် LLM (large language model) ကို အသုံးပြုသော အဆင့်မြင့် client တစ်ခု ဖန်တီးမည်။ ယခုအချိန်မှာ server features များကို ဘယ်လိုခေါ်မလဲဆိုတာကြည့်ပါစို့။

#### Rust

Main function တွင် client ကို initialize ပြုလုပ်ပြီးနောက် server ကို စတင်၍ အချို့ feature များ စာရင်းပြုစုနိုင်သည်။

```rust
// စတင်ပြုလုပ်ခြင်း
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// စက်ပစ္စည်းများစာရင်း
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Features များ ခေါ်ယူခြင်း

မလိုအပ်သော arguments များ နှင့် အမည်များကို တိကျစွာ ဖော်ပြသေချာရန် လိုအပ်ပါသည်။

#### TypeScript

```typescript

// အရင်းအမြစ်တစ်ခုကို ဖတ်ပါ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ကိရိယာတစ်ခုအား ခေါ်ဆိုပါ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// prompt ကို ခေါ်ဆိုပါ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ယခင်ကုဒ်တွင် ကျွန်တော်တို့-

- resource တစ်ခုဖတ်ခြင်း၊ `readResource()` ကို `uri` ဖြင့် ခေါ်ယူသည်။ server ဘက်မှာ အောက်ပါအတိုင်း ဖြစ်နိုင်သည်။

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    ကျွန်ုပ်တို့၏ `uri` တန်ဖိုး `file://example.txt` သည် server မှာရှိသည့် `file://{name}` နှင့် ကိုက်ညီသည်။ `example.txt` ကို `name` ဟု mapping လုပ်သည်။

- tool ကို ခေါ်ကြောင်း, tool ၏ `name` နှင့် `arguments` ကို အောက်ပါအတိုင်းဖော်ပြသည်။

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- prompt ကို ရယူရန် `getPrompt()` ကို `name` နှင့် `arguments` ဖြင့် ခေါ်သည်။ Server ကုဒ်မှာ အောက်ပါအတိုင်းဖြစ်သည်။

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    ထို့ကြောင့် client ကုဒ်ကို server ပေါ်တွင် ကြေညာထားသည့် အတိုင်း အောက်ပါအတိုင်း ရေးသားရမည်ဖြစ်သည်။

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# ရင်းမြစ်ကိုဖတ်ရန်
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ကိရိယာတစ်ခုကိုခေါ်ရန်
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ယခင်ကုဒ်တွင် ကျွန်ုပ်တို့-

- `greeting` ဆိုတဲ့ resource ကို `read_resource` ဖြင့် ခေါ်ယူခဲ့သည်။
- `add` ဆိုသော tool ကို `call_tool` ဖြင့် ခေါ်ယူခဲ့သည်။

#### .NET

1. tool ခေါ်ရန်အတွက် ကုဒ်ထည့်ပါ။

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ရလဒ်ကို ပုံနှိပ်ရန် ကုဒ်ကို ခဲထုတ်ပါ။

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// ကေယ်လ်ကူရေးတာကိရိယာအမျိုးမျိုးကို ခေါ်ယူပါ
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

ယခင်ကုဒ်တွင် ကျွန်ုပ်တို့-

- `callTool()` method နှင့် `CallToolRequest` objects များ အသုံးပြု၍ အနည်းငယ် calculator tools များ ခေါ်ယူခဲ့သည်။
- tool အမည်နှင့် tool လိုအပ်သော arguments များ `Map` အဖြစ် ပေးထားသည်။
- Server tools အတွက် သတ်မှတ် parameter များ (ဥပမာ- "a", "b" စသည့် သင်္ကေတများ) လိုအပ်သည်။
- ရလဒ်များကို server မှ ပြန်ပေးသော `CallToolResult` objects အဖြစ် လက်ခံရရှိသည်။

#### Rust

```rust
// arguments = {"a": 3, "b": 2} နဲ့ add tool ကို ခေါ်ပါ။
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Client ကို run ရန်

Client ကို run ဖို့ terminal တွင် အောက်ပါ command များထည့်ပါ။

#### TypeScript

*package.json* ဖိုင်က "scripts" အပိုင်းမှာ အောက်တွင်ပြထားသည့် ကိုးဒ် ထည့်ပါ။

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Client ကို အောက်ပါ command ဖြင့် ခေါ်ပါ။

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

MCP server ကို `http://localhost:8080` ပေါ်တွင် စတင်ထားသည်ဟုတ်မဟုတ် စစ်ဆေးပြီး client ကိုသုံးပါ။

```bash
# သင်၏ပရောဂျက်ကို တည်ဆောက်ပါ
./mvnw clean compile

# ဖောက်သည်ကို လည်ပတ်ပါ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

သို့မဟုတ် solution folder `03-GettingStarted\02-client\solution\java` မှ client စီမံကိန်း ပြည့်စုံကို run လုပ်နိုင်ပါသည်။

```bash
# ဖြေရှင်းမှု directory သို့ သွားပါ
cd 03-GettingStarted/02-client/solution/java

# JAR ကို တည်ဆောက်ပြီး အလှည့်အပြောင်းပြေးပါ
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## လုပ်ငန်းတာဝန်

ဒီလုပ်ငန်းတာဝန်ကြောင့် သင် client စတင်ဖန်တီးခြင်းတွင် သင်ယူခဲ့သည့် အရာများကို အသုံးပြုသည့် ကိုယ်ပိုင် client တစ်ခု ဖန်တီးပါ။

သင့်ကို client ကနေ ခေါ်ရမည့် server တစ်ခု ရှိပါတယ်၊ သင့် client ကုဒ်မှပစ်သွားပြီး server ကို ပိုစိတ်ဝင်စားဖို့ အပြောင်းအလဲ feature များ ထပ်ထည့်နိုင်ပါစေ။

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// MCP ဆာဗာတစ်ခု ဖန်တီးပါ
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ပေါင်းစပ်မှုကိရိယာတစ်ခု ထည့်သွင်းပါ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ဒိုင်နမစ်ကြိုဆိုမှု အရင်းအမြစ်တစ်ခု ထည့်ပါ
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// stdin တွင် စာတိုများ လက်ခံရယူခြင်းနှင့် stdout တွင် စာတိုများ ပို့ခြင်း စတင်ပါ

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# MCP ဆာဗာ တစ်ခု ဖန်တီးပါ
mcp = FastMCP("Demo")


# တွက်ချက်မှု ကိရိယာ တစ်ခုပေါင်းထည့်ပါ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ပိတ်သတ်နိုင်သော ကြိုဆိုမှု အရင်းအမြစ် တစ်ခု ပေါင်းထည့်ပါ
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

ဒီ project ကို ကြည့်ခြင်းဖြင့် [prompts နှင့် resources ထည့်သွင်းနည်း](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) ကို သိရှိနိုင်ပါသည်။

ဒီလင့်ခ်ကိုလည်း ကြည့်ကာ [prompts နှင့် resources ခေါ်ယူနည်း](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ကို လေ့လာပါ။

### Rust

[ယခင်အခန်း](../../../../03-GettingStarted/01-first-server) တွင် Rust သုံးပြီး MCP server ရိုးရှင်းဖန်တီးနည်း သင်ယူခဲ့သည်။ ဆက်လက်တည်ဆောက်ခြင်း သို့မဟုတ် Rust-based MCP server ဥပမာများဟာ ဒီလင့်ခ်မှာ ရှိပါတယ်-[MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ဖြေရှင်းချက်

**solution folder** တွင် ထည့်သွင်းထားသော client အကောင်အထည်ဖော်မှုများသည် ဤသင်ခန်းစာအတွင်းပါရှိသည့် မူကြမ်းများအားလုံးကို ပြသရန် အသင့်ဖြစ်ပြီး run လုပ်နိုင်သော ပရောဂျက်များဖြစ်ကြသည်။ Solution တစ်ခုစီတွင် client နှင့် server ကို ကိုယ်ပိုင် project များအဖြစ် စနစ်တကျ စုစည်းထားသည်။

### 📁 ဖြေရှင်းချက်ဖွဲ့စည်းပုံ

Solution directory ကို programming language မျိုးအလိုက် ဖွဲ့စည်းထားသည်။

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 ဖြေရှင်းချက်တစ်ခုစီတွင် ပါဝင်သော အရာများ

သင်ဘာသာစကားအလိုက် solution တစ်ခုစီသည် အောက်ပါအကြောင်းအရာများ ပါဝင်သည် -

- **သင်ခန်းစာလမ်းညွှန်မှ လက်တွေ့ client တည်ဆောက်မှုအပြည့်အစုံ**
- **တည်ဆောက်မှုစံနှုန်းရှိပြီး အသေးစိတ် ရေးဆွဲထားသော project structure**
- **ရိုးရှင်းသော build နှင့် run scripts များ**
- **ဘာသာစကားအလိုက် အသုံးပြုနည်းများ ပါဝင်သည့် README အသေးစိတ်**
- **အမှားကိုင်တွယ်ခြင်းနှင့် ရလဒ် လက်ခံ နမူနာများ**

### 📖 ဖြေရှင်းချက်များကို အသုံးပြုခြင်း

1. **သင်နှစ်သက်သော ဘာသာစကား folder ကို သွားပါ**။

   ```bash
   cd solution/typescript/    # TypeScript အတွက်
   cd solution/java/          # Java အတွက်
   cd solution/python/        # Python အတွက်
   cd solution/dotnet/        # .NET အတွက်
   ```

2. **အစီအစဉ်အား စတင်ခြင်းနှင့် အသုံးပြုပုံ အချက်အလက်များအတွက် README အတိုင်းလိုက်နာပါ**။
   - အတွက်လို အခိုင်အမာထည့်သွင်းခြင်း
   - စီမံကိန်း တည်ဆောက်ခြင်း
   - client ကို run လုပ်ခြင်း

3. **သင်မြင်ရမည့် ဥပမာ output**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ဤ tutorial အတွက် ပြည့်စုံသော အရာများနှင့် အဆင့်လိုက် လမ်းညွှန်များကို ကြည့်ရန်- **[📖 Solution Documentation](./solution/README.md)**

## 🎯 ပြည့်စုံသော နမူနာများ

သေချာသော မူကြမ်းများနှင့် ပြည့်စုံသော client အကောင်အထည်ဖော်မှုများကို ဘာသာစကားအားလုံးအတွက် ပေးထားပြီး ဤနမူနာများမှာ ဖေါ်ပြထားသော အလုပ်လုပ်နိုင်မှုအတိုင်း လုပ်ဆောင်သက်သေပြသည်။ သင့်ကိုယ်ပိုင် ပြန်လည်ဖန်တီးမှုအတွက် နှင့် စတင်ရေးဆွဲရန် အရင်းအမြစ်များအဖြစ် အသုံးပြုနိုင်သည်။

### ရနိုင်သော ပြည့်စုံနိုင်သော ဥပမာများ

| ဘာသာစကား | ဖိုင်အမည် | ဖော်ပြချက် |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE transport ဖြင့် အပြည့်အစုံပါဝင်သည့် Java client နှင့် error handling ပြည့်စုံခြင်း |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio transport အသုံးပြုသော C# client ပေါ်တွင် server ကို အလိုအလျောက် စတင်ခြင်းပါဝင်သည် |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP protocol အပြည့်အစုံ ထောက်ပံ့သည့် TypeScript client ဖြစ်သည် |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await ပုံစံများ သုံးသော Python client |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | async လုပ်ငန်းဆောင်တာများအတွက် Tokio သုံးသော Rust client |

ပြည့်စုံသော နမူနာတစ်ခုစီတွင် ပါဝင်သည့် အရာများ-

- ✅ **ဆက်သွယ်မှု တည်ဆောက်ခြင်းနှင့် အမှားကိုင်တွယ်ခြင်း**
- ✅ **Server တွင် ရရှိနိုင်သည့်အရာများ ရှာဖွေရေး (tools, resources, prompts)**
- ✅ **Calculator လုပ်ဆောင်ချက်များ (ပေါင်း, ခွဲ, မြှောက်, မျှ, ကူညီ)**
- ✅ **ရလဒ် ထုတ်ယူခြင်းနှင့် ဖော်ပြချက် ပုံဖော်ခြင်း**
- ✅ **အပြည့်အစုံ error handling လုပ်ဆောင်ချက်များ**

- ✅ **သန့်ရှင်းပြီး မှတ်တမ်းတင်ထားသော ကုတ်** ကို အဆင့်ဆင့် မှတ်ချက်များနှင့်အတူ  

### နမူနာများဖြင့် စတင်အသုံးပြုခြင်း  

1. အထက်ပါ စာရင်းမှ **သင်ဆုံးဖြတ်ထားသော ဘာသာစကားကို ရွေးချယ်ပါ**  
2. **ပြည့်စုံသော နမူနာဖိုင်ကို သုံးသပ်လိုက်ပါ** ၊ အကောင်အထည်ဖော်မှုကို သိရှိရန်  
3. [`complete_examples.md`](./complete_examples.md) သို့ပါတဲ့ လမ်းညွှန်ချက်များအတိုင်း **နမူနာကို ပြေးကြည့်ပါ**  
4. သင်၏ အထူးရည်ရွယ်ချက်များအတွက် နမူနာကို **ပြင်ဆင်ပြီး တိုးချဲ့ပါ**  

အကြောင်းအရာအသေးစိတ်များအတွက် ဤနမူနာများကို လည်ပတ်ခြင်းနှင့် ပြင်ဆင်ခြင်းစာရွက်ကို ကြည့်ပါ - **[📖 ပြည့်စုံသော နမူနာစာရွက်](./complete_examples.md)**  

### 💡 Solution နှင့် ပြည့်စုံသော နမူနာများ  

| **Solution ဖိုလ်ဒါ** | **ပြည့်စုံသော နမူနာများ** |
|--------------------|--------------------- |
| ပြည့်စုံသော စီမံကိန်း လုပ်ငန်းစဉ်များနှင့် ဘီလ်ဖိုင်များ | တစ်ဖိုင်သာဖြစ်သော အကောင်အထည်ဖော်ချက်များ |
| အခြားပစ္စည်းများလိုအပ်ချက်နှင့် ပြေးနိုင်သည့် | အာရုံစိုက်သော ကုတ်နမူနာများ |
| ထုတ်လုပ်မှုဆန်သော စီမံချက် | ပညာသင်ယူရေး ကျမ်း reference |
| ဘာသာစကားအလိုက် မိမိထိန်းချုပ်နိုင်ရေးကိရိယာများ | ဘာသာစကားများအလိုက် နှိုင်းယှဉ်ခြင်း |

နည်းလမ်းနှစ်ခုလုံးမှာ အဖိုးတန်ပါတယ် - ပြည့်စုံသော စီမံကိန်းများအတွက် **solution ဖိုလ်ဒါကို** အသုံးပြုပါ၊ ပညာသင်ယူခြင်းနှင့် ညီလာခံများအတွက် **ပြည့်စုံသော နမူနာများ** ကို အသုံးပြုပါ။  

## အဓိက သင်ခန်းစာများ  

ဤသင်ခန်းစာတွင် client များအကြောင်း အဓိကသင်ခန်းစာများမှာ အောက်ပါအတိုင်းဖြစ်သည် -  

- server ပေါ်ရှိ လုပ်ဆောင်ချက်များကို ရှာဖွေခြင်းနှင့် ခေါ်ယူနိုင်သည်။  
- မိမိကိုယ်ကို စတင်ကာ server တစ်ခုကို စတင်နိုင်သလို (ဤသင်ခန်းစာအတိုင်း) client များသည် လည်ပတ်နေသော server များကို ချိတ်ဆက်နိုင်သည်။  
- Inspector ကဲ့သို့သော အခြားနည်းလမ်းများနှင့် နှိုင်းယှဉ်၍ server အား စမ်းသပ်ရန် အကောင်းဆုံးနည်းလမ်းတစ်ခုဖြစ်သည်။  

## အပို ရင်းမြစ်များ  

- [MCP တွင် client များတည်ဆောက်ခြင်း](https://modelcontextprotocol.io/quickstart/client)  

## နမူနာများ  

- [Java ကိန်းဂဏန်းတွက်စက်](../samples/java/calculator/README.md)  
- [.NET ကိန်းဂဏန်းတွက်စက်](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript ကိန်းဂဏန်းတွက်စက်](../samples/javascript/README.md)  
- [TypeScript ကိန်းဂဏန်းတွက်စက်](../samples/typescript/README.md)  
- [Python ကိန်းဂဏန်းတွက်စက်](../../../../03-GettingStarted/samples/python)  
- [Rust ကိန်းဂဏန်းတွက်စက်](../../../../03-GettingStarted/samples/rust)  

## နောက်ထပ် ဘာဖြစ်မလဲ  

- နောက်တစ်ခု - [LLM တွင် client တည်ဆောက်ခြင်း](../03-llm-client/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->