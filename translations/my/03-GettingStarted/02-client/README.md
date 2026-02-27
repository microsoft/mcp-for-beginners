# Client တစ်ခုဖန်တီးခြင်း

Client များသည် MCP Server နှင့်တိုက်ရိုက်ဆက်သွယ်၍ အရင်းအမြစ်များ၊ ကိရိယာများနှင့် prompt များကို တောင်းဆိုသော စိတ်ကြိုက် application များ သို့မဟုတ် script များဖြစ်သည်။ Server နှင့်ဆက်သွယ်ရန် graphical interface ပေးသော inspector tool ကို အသုံးပြုခြင်းနှင့်မတူဘဲ သင်၏ client ကို ကိုယ်တိုင်ရေးခြင်းဖြင့် အလိုအလျောက်လုပ်ဆောင်မှုများနှင့် အစီအစဉ်အဟန်အမခံ ဆက်သွယ်နိုင်သည်။ ၎င်းက developer များကို MCP ၏စွမ်းရည်များကို သူတို့၏ workflow များတွင် ပေါင်းစည်းအသုံးပြုရန်၊ တာဝန်များကို အလိုအလျောက်လုပ်ရန်နှင့် သီးသန့်လိုအပ်ချက်များအတွက် အထူးပြုဖြေရှင်းနည်းများ ဖန်တီးရန် အခွင့်အရေးပေးသည်။

## အနှစ်ချုပ်

ဤသင်ခန်းစာသည် Model Context Protocol (MCP) စနစ်အတွင်း client အကြောင်းကို မိတ်ဆက်ပေးသည်။ သင်သည် ကိုယ်ပိုင် client ရေးသားပြီး MCP Server နှင့် ဆက်သွယ်ခြင်းကို သင်ယူနိုင်ပါလိမ့်မည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာအဆုံးတွင် သင်သည် -

- client ဟာ ဘာလုပ်နိုင်သလဲကို နားလည်နိုင်ပါလိမ့်မည်။
- ကိုယ်ပိုင် client ကို ရေးသားနိုင်ပါလိမ့်မည်။
- MCP server နှင့် ဆက်သွယ်စမ်းသပ်ပြီး server က အလုပ်လုပ်မှုမှန်ကန်ခြင်းကို သေချာစွာ စစ်ဆေးနိုင်ပါလိမ့်မည်။

## Client ရေးသားရာတွင် လိုအပ်သည့်အချက်များ

Client ရေးသားဖို့အတွက် အောက်ပါအချက်များ လိုအပ်ပါသည် -

- **မှန်ကန်သော 라이ဘရရီများကို import လုပ်ပါ**။ သင်သည် ယခင်ကအသုံးပြုပြီးသား 라이ဘရရီကို အသုံးပြုမည်ဖြစ်သော်လည်း ကွဲပြားသော ကွန်စမြဲများကို သုံးပါမည်။
- **Client instance တစ်ခုဖန်တီးပါ**။ Client တစ်ခု ဖန်တီးပြီး ခုနှစ်ောင်းထားသော ထုတ်ပို့ပုံကို အသုံးပြု၍ ဆက်သွယ်ပါမည်။
- **ဘာလက်ရှိ server အရင်းအမြစ်များကို စစ်ဆေးမည်ဆိုတာဆုံးဖြတ်ပါ**။ MCP server တွင် အရင်းအမြစ်များ၊ ကိရိယာများနှင့် prompt များ ပါဝင်ပြီး၊ စာရင်းပြုမည့်အရာကိုရွေးချယ်ပါ။
- **Client ကို host application တစ်ခုတွင် ပေါင်းစည်းပါ**။ Server ၏ စွမ်းဆောင်ရည်ကို သိရှိပြီးနောက်၊ သင့် host application တွင် ပေါင်းစည်းပါ။ အသုံးပြုသူက prompt သို့မဟုတ် အမိန့်တစ်ခုရိုက်ထည့်သောအခါ server ၏ အကြောင်းဆိုင်ရာ feature ကို ခေါ်ယူစေပါ။

အထက်ပါ အကြောင်းအရာများကို နားလည်ပြီးနောက်၊ နမူနာတစ်ခုကို ကြည့်လိုက်ပါ။

### နမူနာ Client

ဒီနမူနာ client ကိုကြည့်လိုက်ရအောင် -

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

// မေးခွန်းများစာရင်း
const prompts = await client.listPrompts();

// မေးခွန်းတစ်ခုရယူပါ
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// အရင်းအမြစ်များစာရင်း
const resources = await client.listResources();

// အရင်းအမြစ်တစ်ခုကိုဖတ်ပါ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ကိရိယာတစ်ခုကိုခေါ်ပါ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ယခင် ကုဒ်တွင် -

- 라이ဘရရီများကို import လုပ်ထားသည်။
- client instance တစ်ခု ဖန်တီးပြီး stdio မှတစ်ဆင့် ဆက်သွယ်ထားသည်။
- prompt ၊ resource များနှင့် tool များကို စာရင်းပြု၍ အားလုံးခေါ်ယူထားသည်။

ဒါပေမယ့် MCP Server နှင့် ဆက်သွယ်နိုင်သည့် client တစ်ခု ရှိပါပြီ။

နောက် တစ်ခုပြုလုပ်မည့်အခန်းတွင် ကုဒ်ပစ္စည်းအပိုင်းတိုင်းကို ခွဲခြမ်းလုပ်ဆောင်ပြီး ရှင်းပြပါမည်။

## လေ့ကျင့်ခန်း - Client ရေးသားခြင်း

အထက်တွင် ပြောခဲ့သလို၊ ကုဒ်ကို ရှင်းပြရန် အချိန်ယူပြီး လိုလျှင် နောက်ကျောလှမ်းလက်တွေ့ လေ့ကျင့်ပါ။

### -1- 라이ဘရရီများ import လုပ်ခြင်း

လိုအပ်သည့် 라이ဘရရီများကို import လုပ်ပါ။ client နဲ့ stdio transport protocol ကို ကိုးကားရန်လိုသည်။ stdio သည် သင့်ကိုယ်ပိုင်စက်ပေါ်တွင် အလုပ်လုပ်ရန် ဖြစ်သော protocol ဖြစ်သည်။ SSE သည် နောက်ပိုင်းအခန်းများတွင် ဖော်ပြမည့် transport protocol တစ်ခု ဖြစ်ပြီး အခြားရွေးချယ်စရာဖြစ်သည်။ ယခုအချိန်မှာတော့ stdio ဖြင့် ဆက်လက်လုပ်ဆောင်ပါမည်။

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

Java အတွက်တော့ ယခင်လေ့ကျင့်ခန်းမှ MCP server နှင့် ချိတ်ဆက်သော client ကို Java Spring Boot project ဖွဲ့စည်းမှုအတိုင်း [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) မှာ ရှိသော structure နှင့် ကိုက်ညီစွာ `SDKClient` ဆိုတဲ့ Java class အသစ်ကို `src/main/java/com/microsoft/mcp/sample/client/` ဖိုဒါတွင် ဖန်တီးပြီး အောက်ပါ imports များထည့်ပါ။

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

`Cargo.toml` ဖိုင်တွင် အောက်ပါ dependencies များထည့်ရန်လိုအပ်သည်။

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

ထို့နောက် client ကုဒ်တွင်လိုအပ်သည့် 라이ဘရရီများကို import လုပ်နိုင်ပါသည်။

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

အခုတော့ instance ဖန်တီးခြင်းဆီသို့ ရောက်ရှိကြပါစို့။

### -2- Client နှင့် transport instance ဖန်တီးခြင်း

transport instance နှင့် client instance တို့ကို ဖန်တီးရမည်ဖြစ်သည်။

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

ယခင်ကုဒ်တွင် -

- stdio transport instance တစ်ခု ဖန်တီးထားသည်။ Server ကို ရှာဖွေစတင်နိုင်ရန် command နှင့် args များသတ်မှတ်ထားသည်။

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- client ကို name နှင့် version ဖြင့် instance ဖန်တီးထားသည်။

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- client ကိုရွေးချယ်ထားသော transport နှင့် ဆက်သွယ်ထားသည်။

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio ချိတ်ဆက်မှုအတွက် ဆာဗာပါတီမီတာများ ဖန်တီးပါ
server_params = StdioServerParameters(
    command="mcp",  # လည်ပတ်နိုင်သော
    args=["run", "server.py"],  # ရွေးချယ်နိုင်သည့် command line အချက်အလက်များ
    env=None,  # ရွေးချယ်နိုင်သည့် ပတ်ဝန်းကျင်ချိန်ညှိများ
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ချိတ်ဆက်မှုကို စတင်အလုပ်လုပ်အောင် ပြုလုပ်ပါ
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

ယခင်ကုဒ်တွင် -

- လိုအပ်သည့် 라이ဘရရီများ import လုပ်ထားသည်။
- Server ကို run ဖို့ အသုံးပြုမည့် parameters object တစ်ခု ဖန်တီးထားသည်။
- `stdio_client` ကိုခေါ်သည့် `run` method တစ်ခု သတ်မှတ်ထားသည်။
- `asyncio.run` မှတစ်ဆင့် `run` method ကို မောင်းပေးသော entry point ဖန်တီးထားသည်။

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

ယခင်ကုဒ်တွင် -

- လိုအပ်သည့် 라이ဘရရီများ import လုပ်ထားသည်။
- stdio transport တစ်ခု ဖန်တီးပြီး `mcpClient` client ကို ဖန်တီးထားသည်။ ၎င်းသည် MCP Server ၏ feature များကို စာရင်းပြုခြင်းနှင့် ခေါ်ရန် အသုံးပြုမည့် client ဖြစ်သည်။

"Arguments" တွင် *.csproj* သို့မဟုတ် executable ဖိုင်ကို ရည်ညွှန်းနိုင်သည်။

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
        
        // သင့် client logic ကို ဒီနေရာမှာရေးပါ
    }
}
```

ယခင်ကုဒ်တွင် -

- MCP Server တည်နေရာဖြစ်သော `http://localhost:8080` ကို ရည်ညွှန်း၍ SSE transport ကို ဖန်တီးထားသည်။
- Transport ကို constructor parameter အဖြစ် ယူသည့် client class တစ်ခု ဖန်တီးထားသည်။
- `run` method တွင် transport ကို အသုံးပြု၍ synchronous MCP client တစ်ခု ဖန်တီးပြီး ဆက်သွယ်မှုကို စတင်ထားသည်။
- Java Spring Boot MCP server များနှင့် HTTP-based ဆက်သွယ်မှုအတွက် SSE (Server-Sent Events) transport ကို အသုံးပြုထားသည်။

#### Rust

Rust client သည် server ကို "calculator-server" ဆိုသော အဖွဲ့အစည်းတစ်ခု အဖြစ် တူညီသော ဖိုင်လမ်းကြောင်းတွင် တည်ရှိသည်ဟုယူဆထားသည်။ အောက်ပါကုဒ်သည် server ကို စတင်ပြီး ဆက်သွယ်ပါမည်။

```rust
async fn main() -> Result<(), RmcpError> {
    // ဆာဗာကို "calculator-server" ဟုအမည်ရသော ညီအစ်ကိုပရောဂျက်တစ်ခု ဖြစ်ပြီး အတူတူ ဒိုင်रेकတရီထဲမှာရှိတာလိုယူဆပါ
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

    // လုပ်ဆောင်ရမည့်အချက် - စတင်လိုက်ပါ

    // လုပ်ဆောင်ရမည့်အချက် - ကိရိယာများစာရင်းပြုစုပါ

    // လုပ်ဆောင်ရမည့်အချက် - arguments = {"a": 3, "b": 2} ဖြင့် add tool ကိုခေါ်ပါ

    client.cancel().await?;
    Ok(())
}
```

### -3- Server features များစာရင်းပြုစုခြင်း

ယခု client သည် ဆက်သွယ်နိုင်ပြီ ဖြစ်သော်လည်း feature များကို စာရင်းပြုစုခြင်း မရှိသေးပါ။ ထို့ကြောင့် ခြေလှမ်းချင်းစီကို ချပြပါမည် -

#### TypeScript

```typescript
// အကြောင်းအရာများစာရင်း
const prompts = await client.listPrompts();

// အရင်းအမြစ်များစာရင်း
const resources = await client.listResources();

// ကိရိယာများစာရင်း
const tools = await client.listTools();
```

#### Python

```python
# အသုံးပြုနိုင်သော အရင်းအမြစ်များ စာရင်း
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# အသုံးပြုနိုင်သော ကိရိယာများ စာရင်း
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ဒီမှာ available resources (`list_resources()`) နှင့် tools (`list_tools`) များကို စာရင်းပြုစုပြီး ပရင့်ထုတ်ထားသည်။

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

အထက်ပါ ဥပမာသည် server တွင်ရှိသော tools များကို စာရင်းပြုရာပုံဖြစ်သည်။ tools တစ်ခုချင်းစီအတွက် name ကို ပရင့်ထုတ်ထားသည်။

#### Java

```java
// စာရင်းပြုစုပါ နှင့် ကိရိယာများကို ပြသပါ
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// ချိတ်ဆက်မှုကို ထောက်လှမ်းရန် ဆာဗာကို ping လဲ ပေးနိုင်သည်။
client.ping();
```

ယခင်ကုဒ်တွင် -

- MCP server မှ available tools များကို `listTools()` ဖြင့် ခေါ်ယူထားသည်။
- Server နှင့် ဆက်သွယ်မှုမှန်ကန်ပုံကို `ping()` ဖြင့် စစ်ဆေးထားသည်။
- `ListToolsResult` တွင် tool name, ဖော်ပြချက်နှင့် input schema များ ပါဝင်သည်။

အံ့သြဖြစ်စရာကောင်းသည်။ အားလုံး feature များကို သိရှိထားပါပြီ။ ထို့နောက် လုပ်ဆောင်မှုများကို ဘယ်အချိန်တွင် အသုံးပြုမလဲဆိုတာ ဖြစ်လာသည်။ ဤ client သည် feature များကို အကြိုပြောကြားခေါ်ယူရမည့် အလွန်ရိုးရှင်းသော client ဖြစ်သည်။ နောက်ဆုံးပိုင်းတွင် ကိုယ်ပိုင် LLM (large language model) ပါသော client တစ်ခု ဖန်တီးမည် ဖြစ်သည်။ ယခုလည်း server တွင် feature များခေါ်ယူနည်းကို ကြည့်ရအောင် -

#### Rust

main function တွင် client ကို initialize ပြီးနောက် server ကို initialize လုပ်ပြီး အချို့ feature များကို စာရင်းပြုစုနိုင်သည်။

```rust
// စတင်ပြင်ဆင်ခြင်း
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// ကိရိယာများစာရင်း
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Feature များ ခေါ်ယူခြင်း

feature များခေါ်ယူရန် လိုအပ်သည့် arguments များနှင့် အခါအားလျော်စွာ ခေါ်ယူမည့် feature ၏အမည်များကို မှန်ကန်စွာ သတ်မှတ်ရမည်။

#### TypeScript

```typescript

// အရင်းအမြစ်ကိုဖတ်ပါ
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ကိရိယာတစ်ခုကိုခေါ်ပါ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// prompt ကိုခေါ်ပါ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

အထက်ပါကုဒ်တွင် -

- resource တစ်ခုကို ဖတ်ရှုမည့်အခါ `readResource()` ကို `uri` နဲ့ခေါ်သည်။ server ဘက်ရာမှာ အောက်ပါအတိုင်းဖြစ်နိုင်သည် -

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

    server အတွက် `uri` တန်ဖိုး `file://example.txt` သည် `file://{name}` နဲ့ ကိုက်ညီပြီး `example.txt` ကို `name` တွင် map လုပ်သုံးသည်။

- tool ကို `name` နှင့် `arguments` သတ်မှတ်ပြီး ခေါ်ယူသည်။

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- prompt ပေးရန် `getPrompt()` ကို `name` နှင့် `arguments` ဖြင့် ခေါ်သည်။ Server ဘက်နမူနာ -

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

    လူတွေ့ client code သည် server တွင် သတ်မှတ်ထားသည့်အတိုင်း ဖြစ်သည်။

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
# အရင်းအမြစ်ကို ဖတ်ပါ
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ကိရိယာတစ်ခုကို ခေါ်ပါ
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

အထက်ပါကုဒ်တွင် -

- `greeting` resource ကို `read_resource` ဖြင့် ခေါ်ယူထားသည်။
- `add` tool ကို `call_tool` ဖြင့် ခေါ်ယူထားသည်။

#### .NET

1. tool ကို ခေါ်ရန် အောက်ပါကုဒ်ထည့်ပါ။

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ရလဒ်ကို ပရင့်ထုတ်ရန် အောက်ပါကုဒ်ကို သုံးပါ။

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// ကိန်းတွက်စက်ကိရိယာအမျိုးမျိုးကို ခေါ်ဆိုပါ။
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

ယခင်ကုဒ်တွင် -

- `callTool()` method ဖြင့် calculator tool များစွာကို `CallToolRequest` object များဖြင့် ခေါ်ယူခဲ့သည်။
- တစ်ခုချင်း ဆက်သွယ်ရာ tool ၏ အမည်နှင့် ပေးရမည့် arguments များကို Map အဖြစ် ထည့်သွင်းထားသည်။
- server tools များသည် "a", "b" စသည်ဖြင့် parameter များအလိုက်တိတိကျကျ အသုံးပြုခြင်းကို မျှော်မွန်းသည်။
- ရလဒ်များကို `CallToolResult` object များအဖြစ် ပြန်လာသည်။

#### Rust

```rust
// ပရိုဂရမ် add ကို argument = {"a": 3, "b": 2} ဖြင့်ခေါ်ပါ။
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

### -5- Client run ခြင်း

Client run ချင်လျှင် terminal တွင် အောက်ပါ command ကို ရိုက်ထည့်ပါ။

#### TypeScript

*package.json* ၏ "scripts" အပိုင်းတွင် အောက်ပါ entry ကို ထည့်ပါ။

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

အောက်ပါ command ဖြင့် client ကို run ပါ။

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

MCP server ကို `http://localhost:8080` တွင် run ထားရှိထားခြင်းကို သေချာစေရန်၊ ထိုပြီးနောက် client run ပါ။

```bash
# သင်၏ပရောဂျက်ကို ဖန်တီးပါ
./mvnw clean compile

# က라이언့ကို ပြေးပါ
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

alternatively၊ solution folder `03-GettingStarted\02-client\solution\java` တွင်ပေးထားသော complete client project ကို run နိုင်သည်။

```bash
# ဖြေရှင်းချက် directory သို့ navigation လုပ်ပါ
cd 03-GettingStarted/02-client/solution/java

# JAR ကို တည်ဆောက်ပြီး ပြေးပါ
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## အလုပ်ပေးစာ

ဤအလုပ်တွင် သင် သင်ယူထားသော client ဖန်တီးခြင်း၊ သင်၏ကိုယ်ပိုင် client တစ်ခုဖန်တီးပြီး ဘာသာရပ်ပြည့်စုံစွာ အသုံးပြုပါ။

သင်၏ client ကို ခေါ်ယူရန် သုံးနိုင်သော server တစ်ခုရှိသည်၊ ထို့ဟာ လူစိတ်ဝင်စားစရာ feature များ သုံးစွဲရန် ပိုမိုထည့်သွင်းပါ။

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

// ပေါင်းထည့်ရန် ကိရိယာတစ်ခု ထည့်ပါ
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// လှေကားမှုအား အသစ်ပြောင်းလဲနိုင်သော အရင်းမြစ်တစ်ခု ထည့်ပါ
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

// stdin တွင် မက်ဆေ့ခ််များ လက်ခံယူခြင်းနှင့် stdout တွင် မက်ဆေ့ခ််များ ပို့ခြင်း စတင်ပါ။

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

# MCP ဆာဗာတစ်ခု ဖန်တီးပါ
mcp = FastMCP("Demo")


# ချိန်ထည့်ရေးကိရိယာတစ်ခု ပေါင်းထည့်ပါ
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# အပြောင်းအလဲ ရှိသောခင်တွယ်ကြိုဆိုမှုအရင်းအမြစ်ကို ပေါင်းထည့်ပါ
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

ဤ project ကို ကြည့်၍ [prompts နှင့် resources ထည့်သွင်းနည်း](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) ကို လေ့လာနိုင်သည်။

ထို့အပြင် [prompts နှင့် resources ခေါ်ယူနည်း](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ကိုလည်း စစ်ဆေးကြည့်ပါ။

### Rust

[ယခင်အပိုင်း](../../../../03-GettingStarted/01-first-server) တွင် Rust ဖြင့် တိုင်းတာသော MCP server ကို ဖန်တီးခြင်းကို သင်ယူခဲ့သည်။ ထိုအခြေခံ server ပေါ်၌ ဆက်လက်တိုးချဲ့နိုင်သလို MCP server ရဲ့ Rust-based နမူနာများကို [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers) တွင်ကြည့်ရှုနိုင်သည်။

## ဖြေရှင်းနည်း

**solution folder** တွင် ဤဒေါ်ကမြမ်းစာတမ်းတွင် ဖော်ပြခဲ့သည့် အကြောင်းအရာအားလုံးကို သေချာပြသသည့် လုပ်ဆောင်နိုင်သော client နမူနာများ ပါဝင်သည့် အပြည့်အစုံ client implementations တို့နှင့် server ကုဒ်များကို project အလိုက် ခွဲထုတ်ထားသည်။

### 📁 Solution ဖိုင်တွဲ ဖွဲ့စည်းမှု

solution directory ကို အောက်ပါ programming language အလိုက် ကွဲပြားစီတင်ထားသည် -

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

### 🚀 Solution တစ်ခုစီတွင် ပါဝင်သည့်အရာများ

ဘာသာစကားအလိုက် Solution များသည် -

- သင်ခန်းစာအတွင်း စီမံခန့်ခွဲမှုအားလုံး ပါဝင်သည့် အပြည့်အစုံ client implementation
- အလုပ်လုပ်နိုင်သည့် project ဖွဲ့စည်းမှု များနှင့် မှန်ကန်သော dependencies များ၊ configuration များ
- လွယ်ကူစွာ setup ပြီး run နိုင်ရန် build နှင့် run script များ
- ဘာသာစကားအလိုက် အသေးစိတ် README များ
- error handling နှင့် result processing ဥပမာများ

### 📖 Solution များအသုံးပြုခြင်း

1. ကြိုက်နှစ်သက်ရာ ဘာသာစကား folder ကိုသွားပါ -

   ```bash
   cd solution/typescript/    # TypeScript အတွက်
   cd solution/java/          # Java အတွက်
   cd solution/python/        # Python အတွက်
   cd solution/dotnet/        # .NET အတွက်
   ```

2. folder တစ်ခုချင်းစီ၏ README လမ်းညွှန်ချက်များကို အသေးစိတ် လိုက်နာပါ -
   - dependencies installation
   - project build
   - client run

3. မျှော်မှန်းရမည့် output ဥပမာ -

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

ပြည့်စုံသောစာတမ်းများနှင့် လမ်းညွှန်ချက်များအတွက် **[📖 Solution Documentation](./solution/README.md)** ကို ကြည့်ရှုပါ။

## 🎯 ပြည့်စုံသော နမူနာများ

ဤသင်ခန်းစာကို ဖော်ပြထားသည့် programming language တစ်ခုချင်းစီအတွက် အပြည့်အစုံ client implementation များ ပေးထားသည်။ ထိုနမူနာများတွင် ဖော်ပြထားသည့် စွမ်းဆောင်ရည်များအားလုံး ပါဝင်ပြီး အညွှန်းဆိုင်ရာ implementation များ သို့မဟုတ် ကိုယ်ပိုင် project များအတွက် စတင်အသုံးပြုနိုင်သည်။

### ရရှိနိုင်သော ပြည့်စုံနမူနာများ

| ဘာသာစကား | ဖိုင် | ဖော်ပြချက် |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE transport အသုံးပြုသော Java client အပြည့်အစုံ၊ error handling ကောင်းစွာပါဝင်သည် |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio transport အသုံးပြုသည့် C# client အပြည့်အစုံ၊ server ကို အလိုအလျောက်စတင်နိုင်သည် |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP protocol အပြည့်အစုံ ထောက်ပံ့သည့် TypeScript client |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await pattern ရှိ Python client အပြည့်အစုံ |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio ကို async လုပ်ဆောင်ချက်အတွက် အသုံးပြုသော Rust client |

ပြည့်စုံသော နမူနာတစ်ခုချင်းစီတွင် -
- ✅ **ဆက်သွယ်မှုတည်ဆောက်ခြင်း** နှင့် အမှားများကိုစီမံခန့်ခွဲခြင်း  
- ✅ **ဆားဗာရှာဖွေရေး** (ကိရိယာများ၊ အရင်းအမြစ်များ၊ လမ်းညွှန်ချက်များ လိုအပ်ပါက)  
- ✅ **ကိန်းဂဏန်းတွက်ချက်မှု လုပ်ငန်းစဉ်များ** (ပေါင်းခြင်း၊ လျော့ခြင်း၊ မြှောက်ခြင်း၊ ခွဲခြင်း၊ အကူအညီ)  
- ✅ **ရလဒ်ကို စီမံခန့်ခွဲခြင်း** နှင့် ပုံစံမှန်ကန်သော 출력  
- ✅ **အပြည့်အစုံ အမှားစီမံခန့်ခွဲမှု**  
- ✅ **သန့်ရှင်းပြီး စာတမ်းရေးသားထားသော ကုဒ်** နှင့် အဆင့်လိုက် မှတ်ချက်များ  

### စပြီး လေ့လာရန် အပြည့်အစုံ နမူနာများနှင့်အတူ

1. အထက်တွင်ဖော်ပြထားသော ဇယားမှ **သင့်နှစ်သက်ရာ ဘာသာစကားကို ရွေးချယ်ပါ**  
2. **အပြည့်အစုံ နမူနာဖိုင်ကို ပြန်လည်သုံးသပ်ပြီး** အပြည့်အစုံ အကောင်အထည်ဖော်မှုကို နားလည်ပါ  
3. [`complete_examples.md`](./complete_examples.md) တွင် နေရာယူထားသည့် ညွှန်ကြားချက်များ အတိုင်း **နမူနာကို ထားဆောင်ပါ**  
4. သင်၏ အထူးလိုအပ်ချက်နှင့်ကိုက်ညီအောင် **နမူနာကို ပြင်ဆင် နှင့် တိုးချဲ့ပါ**  

ဒီနမူနာများနှင့် ပတ်သက်သော အသေးစိတ်စာတမ်းများကို ကြည့်ပါ - **[📖 အပြည့်အစုံ နမူနာ စာတမ်း](./complete_examples.md)**  

### 💡 ဖြေရှင်းချက် နှင့် အပြည့်အစုံ နမူနာများ

| **ဖြေရှင်းချက် ဖိုလ်ဒါ** | **အပြည့်အစုံ နမူနာများ** |
|-------------------------|----------------------------|
| အဆောက်အအုံနှင့် build ဖိုင်များပါရှိသော ထူထောင်မှုပြည့်စုံ | တစ်ဖိုင်တည်းဖြင့် အကောင်အထည်ဖော်မှုပြီးဆုံးမှုများ |  
| dependencies များအပြည့်စုံဖြင့် အသင့်ပြေးနိုင် | အာရုံစိုက်ထားသည့် ကုဒ်နမူနာများ |  
| ထုတ်လုပ်မှုအဆင့်ကဲ့သို့အခြေခံ၍ ပြင်ဆင်ထားခြင်း | ပညာရေးအရ အညွှန်းဖြစ်သော နမူနာများ |  
| ဘာသာစကားအလိုက် ကိရိယာများအသုံးပြုထားခြင်း | ဘာသာစကားများရဲ့ နှိုင်းယှဉ်ချက် |  

နှစ်ခုစလုံး အရေးကြီးပြီး - အပြည့်အစုံ စီမံကိန်းများအတွက် **ဖြေရှင်းချက် ဖိုလ်ဒါ** ကို အသုံးပြုနိုင်ပြီး၊ အတတ်ပညာ လေ့လာရန်နှင့် ကိုးကားရန်အတွက် **အပြည့်အစုံ နမူနာများ** ကို အသုံးပြုနိုင်ပါသည်။  

## အဓိကအချက်များ

ဒီအခန်းအတွက် အဓိက သိမ်းဆည်းချက်များမှာ client များအကြောင်း:

- ဆားဗာပေါ်ရှိ features များကို ရှာဖွေဖော်ထုတ်ခြင်းနှင့် ခေါ်ယူဆောင်ရွက်ခြင်း လုပ်ဆောင်နိုင်သည်။  
- သူ့ကိုယ်သူ စတင်တည်ဆောက်ရာတွင် ဆားဗာကိုပါ စတင်နိုင်သလို (ဒီအခန်းအတိုင်း)၊ client များကတော့ လက်ရှိ ရှိသော ဆားဗာများနှင့် ဆက်သွယ်နိုင်ပါသည်။  
- Inspectors ကဲ့သို့ အခြားရွေးချယ်စရာ နည်းလမ်းများနှင့်နှိုင်းယှဉ်ကြည့်ရာတွင် ဆားဗာ၏စွမ်းရည်များကို စမ်းသပ်ရန် အရေးကြီးသော နည်းလမ်းတစ်ခုဖြစ်သည်။  

## နောက်ထပ် အရင်းအမြစ်များ

- [MCP တွင် client များ တည်ဆောက်ခြင်း](https://modelcontextprotocol.io/quickstart/client)  

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)  
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)  

## နောက်တစ်ခုက ဘာလဲ

- နောက်တစ်ဆင့်: [LLM အသုံးပြု၍ client တည်ဆောက်ခြင်း](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**တိကျမှန်ကန်မှု မမှန်ကန်မှု အတွက် ဝေဖန်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဆာဗာစ် [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေပြီးဖြစ်သော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူရင်းစာတမ်းကို သက်ဆိုင်ရာ ဘာသာစကားဖြင့်သာ အတိအကျကိုးကားရန် မျှော်လင့်ရပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူမှုပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုအသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖတ်ခြင်းများအတွက် ကျွန်ုပ်တို့၏ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->