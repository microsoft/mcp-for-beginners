# Client တစ်ခု ဖန်တီးခြင်း

Client များသည် MCP Server နှင့်တိုက်ရိုက်ဆက်သွယ်ပြီး အရင်းအမြစ်များ၊ ကိရိယာများနှင့် prompts များကို တောင်းဆိုနိုင်သော အထူးပြုအက်ပ်များ သို့မဟုတ် script များဖြစ်သည်။ Server နှင့်အတူ အပြန်အလှန်လုပ်ဆောင်ရန် ဂရပ်ဖစ်အင်တာဖေ့စ်ပေးသော inspector tool ကို အသုံးပြုခြင်းနှင့်မတူဘဲ၊ သင့်ကိုယ်ပိုင် client ကိုရေးသားခြင်းဖြင့် အလိုအလျောက်လုပ်ဆောင်မှုများနှင့် သီးသန့်လိုအပ်ချက်များအတွက် အထူးပြုဖြေရှင်းချက်များကို ဖန်တီးနိုင်သည်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာတွင် Model Context Protocol (MCP) ecosystem အတွင်း client များ၏ အယူအဆကို မိတ်ဆက်ပေးမည်ဖြစ်သည်။ သင်၏ကိုယ်ပိုင် client ကိုရေးသားပြီး MCP Server နှင့်ဆက်သွယ်ပုံကို သင်လေ့လာနိုင်မည်ဖြစ်သည်။

## သင်ခန်းစာ၏ ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးတွင် သင်သည် အောက်ပါအရာများကို နားလည်နိုင်မည်ဖြစ်သည်-

- Client တစ်ခုက ဘာလုပ်ဆောင်နိုင်သည်ကို နားလည်ခြင်း။
- ကိုယ်ပိုင် client တစ်ခုရေးသားခြင်း။
- MCP Server နှင့် client ကို ဆက်သွယ်ပြီး စမ်းသပ်ခြင်း။

## Client တစ်ခုရေးသားရန် ဘာတွေလိုအပ်သလဲ?

Client တစ်ခုရေးသားရန် အောက်ပါအဆင့်များကို လိုက်နာရမည်-

- **လိုအပ်သော library များကို import လုပ်ပါ**။ ယခင်က အသုံးပြုခဲ့သော library ကိုပင် အသုံးပြုမည်ဖြစ်ပြီး၊ ကွဲပြားသော constructs များကိုသာ အသုံးပြုမည်။
- **Client တစ်ခုကို instantiate လုပ်ပါ**။ Client instance တစ်ခုဖန်တီးပြီး ရွေးချယ်ထားသော transport method နှင့်ဆက်သွယ်ရမည်။
- **List ပြုလုပ်ရန်အရင်းအမြစ်များကိုဆုံးဖြတ်ပါ**။ သင့် MCP Server တွင် အရင်းအမြစ်များ၊ ကိရိယာများနှင့် prompts များပါဝင်ပြီး၊ သင်သည် မည်သည့်အရာကို list ပြုလုပ်မည်ကိုဆုံးဖြတ်ရမည်။
- **Client ကို host application နှင့်ပေါင်းစည်းပါ**။ Server ၏စွမ်းဆောင်ရည်များကို သိရှိပြီးနောက်၊ host application နှင့်ပေါင်းစည်းပြီး အသုံးပြုသူက prompt သို့မဟုတ် အခြား command များရိုက်ထည့်သောအခါ၊ သက်ဆိုင်ရာ server feature ကို ခေါ်ဆောင်နိုင်ရန် စီစဉ်ရမည်။

အထက်ပါအကြောင်းအရာများကို နားလည်ပြီးနောက်၊ နောက်တစ်ဆင့်တွင် ဥပမာတစ်ခုကို ကြည့်ရှုကြမည်။

### Client ဥပမာတစ်ခု

အောက်တွင် client ဥပမာတစ်ခုကို ကြည့်ရှုပါ-

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

အထက်ပါ code တွင်-

- Library များကို import လုပ်သည်။
- Client instance တစ်ခုဖန်တီးပြီး stdio ကို transport အဖြစ်အသုံးပြု၍ ဆက်သွယ်သည်။
- Prompts, resources, tools များကို list ပြုလုပ်ပြီး အားလုံးကို invoke လုပ်သည်။

ဒါဆို MCP Server နှင့် ဆက်သွယ်နိုင်သော client တစ်ခုရရှိပါပြီ။

နောက်ထပ် exercise အပိုင်းတွင် code snippet တစ်ခုချင်းစီကို ခွဲခြမ်းရှင်းလင်းပြီး ဘာတွေဖြစ်နေသည်ကို ရှင်းပြပါမည်။

## လေ့ကျင့်မှု: Client တစ်ခုရေးသားခြင်း

အထက်တွင်ဖော်ပြခဲ့သလို၊ code ကိုရှင်းပြသည့်အခါ သင်လည်း code ကိုအတူတူရေးနိုင်ပါသည်။

### -1- Library များ Import လုပ်ခြင်း

လိုအပ်သော library များကို import လုပ်ပါ။ Client နှင့် ရွေးချယ်ထားသော transport protocol (stdio) ကို reference လုပ်ရန်လိုအပ်ပါမည်။ stdio သည် သင့် local machine ပေါ်တွင် run လုပ်ရန်ရည်ရွယ်ထားသော protocol တစ်ခုဖြစ်သည်။ SSE သည် နောက်ပိုင်း chapter များတွင် ပြသမည့် transport protocol တစ်ခုဖြစ်ပြီး၊ ဒါဟာ သင့်အခြားရွေးချယ်စရာတစ်ခုဖြစ်သည်။ ယခုအချိန်တွင် stdio ဖြင့် ဆက်လက်လုပ်ဆောင်ကြပါစို့။

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Java အတွက် [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) မှ Java Spring Boot project structure ကို အသုံးပြု၍ `SDKClient` ဟုခေါ်သော Java class တစ်ခုကို `src/main/java/com/microsoft/mcp/sample/client/` folder တွင် ဖန်တီးပြီး အောက်ပါ imports များထည့်ပါ-

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

သင့် `Cargo.toml` ဖိုင်တွင် အောက်ပါ dependencies များထည့်ရန်လိုအပ်ပါမည်။

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

ထို့နောက် သင့် client code တွင် လိုအပ်သော library များကို import လုပ်နိုင်ပါသည်။

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

အခုတော့ instantiation ဆီသို့ ရောက်ကြပါစို့။

### -2- Client နှင့် Transport ကို Instantiate လုပ်ခြင်း

Transport နှင့် Client တစ်ခုစီကို instantiate လုပ်ရန်လိုအပ်ပါမည်-

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

အထက်ပါ code တွင်-

- stdio transport instance တစ်ခုဖန်တီးသည်။ Command နှင့် args ကို သတ်မှတ်ထားသည်ကို သတိပြုပါ၊ ဒါဟာ server ကိုရှာဖွေပြီး start လုပ်ရန်လိုအပ်သည်။

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Client တစ်ခုကို name နှင့် version ဖြင့် instantiate လုပ်သည်။

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Client ကို ရွေးချယ်ထားသော transport နှင့်ဆက်သွယ်သည်။

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

အထက်ပါ code တွင်-

- လိုအပ်သော library များကို import လုပ်သည်။
- Server parameters object တစ်ခု instantiate လုပ်သည်၊ ဒါကို server ကို run လုပ်ရန်အသုံးပြုမည်။
- `stdio_client` ကိုခေါ်သည့် `run` method တစ်ခုသတ်မှတ်သည်၊ ဒါဟာ client session တစ်ခုစတင်ရန်အသုံးပြုမည်။
- `asyncio.run` ကို အသုံးပြု၍ `run` method ကို provide လုပ်သည်။

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

အထက်ပါ code တွင်-

- လိုအပ်သော library များကို import လုပ်သည်။
- stdio transport တစ်ခုဖန်တီးပြီး `mcpClient` ဟုခေါ်သော client တစ်ခုဖန်တီးသည်။ ဒါဟာ MCP Server ပေါ်ရှိ features များကို list ပြုလုပ်ပြီး invoke လုပ်ရန်အသုံးပြုမည်။

"Arguments" တွင် *.csproj* သို့မဟုတ် executable ကို ရည်ညွှန်းနိုင်သည်။

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
        
        // Your client logic goes here
    }
}
```

အထက်ပါ code တွင်-

- `http://localhost:8080` တွင် run လုပ်မည့် MCP server ကို ရည်ညွှန်းသော SSE transport တစ်ခုကို setup လုပ်သည်။
- Transport ကို constructor parameter အဖြစ်ယူသော client class တစ်ခုဖန်တီးသည်။
- `run` method တွင် synchronous MCP client တစ်ခုဖန်တီးပြီး connection ကို initialize လုပ်သည်။
- SSE (Server-Sent Events) transport ကို အသုံးပြုသည်၊ ဒါဟာ Java Spring Boot MCP servers နှင့် HTTP-based ဆက်သွယ်မှုအတွက် သင့်လျော်သည်။

#### Rust

Main function တွင် client ကို initialize ပြီးနောက် server ကို initialize လုပ်ပြီး features များကို list ပြုလုပ်နိုင်သည်။

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Server Features များကို List ပြုလုပ်ခြင်း

Client ကို run လုပ်သည့်အခါ server features များကို list ပြုလုပ်ရန်လိုအပ်သည်။

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

ဒီမှာ `list_resources()` နှင့် `list_tools` ကို အသုံးပြု၍ ရရှိနိုင်သော resources နှင့် tools များကို print ထုတ်သည်။

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

အထက်ပါ code တွင် server ပေါ်ရှိ tools များကို list ပြုလုပ်သည်။ Tool တစ်ခုစီအတွက် name ကို print ထုတ်သည်။

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

အထက်ပါ code တွင်-

- MCP server မှရရှိနိုင်သော tools များအားလုံးကို `listTools()` ဖြင့်ရယူသည်။
- Server နှင့် connection အလုပ်လုပ်နေကြောင်းစစ်ဆေးရန် `ping()` ကို အသုံးပြုသည်။
- `ListToolsResult` တွင် tools များ၏ name, description, input schema စသည့်အချက်အလက်များပါဝင်သည်။

### -4- Features များကို Invoke လုပ်ခြင်း

Features များကို invoke လုပ်ရန် argument များနှင့် invoke လုပ်လိုသည့်အရာ၏ name ကို သေချာစွာသတ်မှတ်ရမည်။

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

အထက်ပါ code တွင်-

- Resource တစ်ခုကို `readResource()` ဖြင့် `uri` သတ်မှတ်ပြီးခေါ်သည်။

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

    Server ပေါ်တွင် `uri` value `file://example.txt` သည် `file://{name}` နှင့်ကိုက်ညီသည်။ `example.txt` ကို `name` သို့ mapping လုပ်မည်။

- Tool တစ်ခုကို `name` နှင့် `arguments` သတ်မှတ်ပြီးခေါ်သည်။

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Prompt တစ်ခုရယူရန် `getPrompt()` ကို `name` နှင့် `arguments` ဖြင့်ခေါ်သည်။

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

    Server code သည် အောက်ပါအတိုင်းဖြစ်မည်-

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

အထက်ပါ code တွင်-

- `read_resource` ကို အသုံးပြု၍ `greeting` ဟုခေါ်သော resource တစ်ခုကိုခေါ်သည်။
- `call_tool` ကို အသုံးပြု၍ `add` ဟုခေါ်သော tool တစ်ခုကို invoke လုပ်သည်။

#### .NET

1. Tool တစ်ခုကို call လုပ်ရန် code ထည့်ပါ-

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Result ကို print ထုတ်ရန် code ထည့်ပါ-

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

အထက်ပါ code တွင်-

- `CallToolRequest` objects များဖြင့် `callTool()` method ကို အသုံးပြု၍ calculator tools များကိုခေါ်သည်။
- Tool တစ်ခုစီသည် tool name နှင့် tool အတွက်လိုအပ်သော arguments များပါဝင်သည့် `Map` တစ်ခုကို သတ်မှတ်ထားသည်။
- Server tools များသည် အထူးသတ်မှတ်ထားသော parameter names (ဥပမာ- "a", "b" သို့မဟုတ် သင်္ချာဆိုင်ရာ operations များအတွက်) ကို မျှော်မှန်းထားသည်။
- Results များကို server မှပြန်လာသော `CallToolResult` objects အဖြစ်ရရှိသည်။

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

### -5- Client ကို Run လုပ်ခြင်း

Client ကို run လုပ်ရန် terminal တွင် အောက်ပါ command ကိုရိုက်ထည့်ပါ-

#### TypeScript

*package.json* တွင် "scripts" အပိုင်းတွင် အောက်ပါ entry ကိုထည့်ပါ-

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Client ကို အောက်ပါ command ဖြင့်ခေါ်ပါ-

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

MCP server ကို `http://localhost:8080` တွင် run လုပ်ထားကြောင်းသေချာပါစေ။ ထို့နောက် client ကို run လုပ်ပါ-

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

မဟုတ်ရင် `03-GettingStarted\02-client\solution\java` folder တွင်ပါဝင်သော အပြည့်အစုံ client project ကို run လုပ်နိုင်သည်-

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## လုပ်ငန်းတာဝန်

ဒီလုပ်ငန်းတာဝန်တွင် သင်လေ့လာခဲ့သည့်အတိုင်း client တစ်ခုဖန်တီးပြီး သင့်ကိုယ်ပိုင် client တစ်ခုရေးသားပါ။

သင်၏ client code မှတစ်ဆင့်ခေါ်ရန်အောက်ပါ server ကိုအသုံးပြုပါ၊ server ကို ပိုမိုစိတ်ဝင်စားစေရန် features များထည့်သွင်းနိုင်မည်ဖြစ်သည်။

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

ဒီ project ကိုကြည့်ပါ [add prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) ပြုလုပ်ပုံကိုလေ့လာရန်။

ထို့အပြင် [prompts and resources](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/) ကို invoke ပြုလုပ်ပုံကိုလည်းကြည့်ပါ။

### Rust

[ယခင်အပိုင်း](../../../../03-GettingStarted/01-first-server) တွင် Rust ဖြင့် MCP server တစ်ခုဖန်တီးပုံကို သင်လေ့လာခဲ့ပါသည်။ ထိုအပေါ်ဆက်လက်တည်ဆောက်နိုင်သလို MCP server examples များကိုလည်းကြည့်နိုင်သည်- [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ဖြေရှင်းချက်

**solution folder** တွင် ဒီသင်ခန်းစာတွင်ဖော်ပြထားသည့် concept များအားလုံးကို ပြသထားသည့် client implementation များပါဝင်သည်။ Solution တစ်ခုစီတွင် client နှင့် server code များကို သီးခြားစီ self-contained projects အဖြစ်ဖော်ပြထားသည်။

### 📁 Solution Structure

Solution directory ကို programming language အလိုက် စီစဉ်ထားသည်-

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

### 🚀 Solution တစ်ခုစီတွင် ပါဝင်သောအရာများ

Language-specific solution တစ်ခုစီတွင်-

- **Client implementation အပြည့်အစုံ** (tutorial တွင်ဖော်ပြထားသည့် features များအားလုံးပါဝင်သည်)
- **Project structure အလုပ်လုပ်နိုင်သောပုံစံ** (dependencies နှင့် configuration များပါဝင်သည်)
- **Build နှင့် run scripts** (setup နှင့် execution ကိုလွယ်ကူစေရန်)
- **README အသေးစိတ်** (language-specific လမ်းညွှန်ချက်များပါဝင်သည်)
- **Error handling** နှင့် result processing ဥပမာများ

### 📖 Solution များကို အသုံးပြုခြင်း

1. **သင့်နှစ်သက်သော language folder သို့သွားပါ**-

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Folder တစ်ခုစီတွင်ပါဝင်သော README လမ်းညွှန်ချက်များကိုလိုက်နာပါ**-
   - Dependencies များ install လုပ်ခြင်း
   - Project ကို build လုပ်ခြင်း
   - Client ကို run လုပ်ခြင်း

3. **Output ဥပမာ** သင်မြင်ရမည့်အရာ-

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Documentation အပြည့်အစုံနှင့် အဆင့်ဆင့်လမ်းညွှန်ချက်များအတွက်- **[📖 Solution Documentation](./solution/README.md)** ကိုကြည့်ပါ။

## 🎯 အပြည့်အစုံသော ဥပမာများ

ဒီ tutorial တွင်ဖော်ပြထားသည့် functionality အပြည့်အစုံကို ပြသထားသည့် client implementation များကို language အလိုက်ပေးထားပါသည်။ ဤဥပမာများကို reference implementation များအဖြစ် သို့မဟုတ် သင့်ကိုယ်ပိုင် project များအတွက် starting point အဖြစ် အသုံးပြုနိုင်သည်။

### ရရှိနိုင်သော အပြည့်အစုံသော ဥပမာများ

| Language | File | Description |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE transport ကိုအသုံးပြုသည့် Java client အပြည့်အစုံ (error handling ပါဝင်သည်) |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio transport ကိုအသုံးပြုသည့် C# client အပြည့်အစုံ (server ကိုအလိုအလျောက် start လုပ်သည်) |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP protocol အပြည့်အစုံကို support ပြုလုပ်သည့် TypeScript client |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await patterns ကိုအသုံးပြုသည့် Python client |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Async operations များအတွက် Tokio ကိုအသုံးပြုသည့် Rust client |
တစ်ခုချင်းစီသော နမူနာများတွင် ပါဝင်သည်မှာ -

- ✅ **ချိတ်ဆက်မှု တည်ဆောက်ခြင်း** နှင့် အမှားကိုင်တွယ်မှု
- ✅ **ဆာဗာ ရှာဖွေမှု** (ကိရိယာများ၊ အရင်းအမြစ်များ၊ လိုအပ်သော အကြံပြုချက်များ)
- ✅ **ကိန်းဂဏန်းတွက်ချက်မှု လုပ်ဆောင်ချက်များ** (ပေါင်း, နုတ်, များ, ခွဲ, အကူအညီ)
- ✅ **ရလဒ်ကို ကိုင်တွယ်ခြင်း** နှင့် ပုံစံတူ အထွက်
- ✅ **ကျယ်ကျယ်ပြန့်ပြန့် အမှားကိုင်တွယ်မှု**
- ✅ **သန့်ရှင်းပြီး မှတ်ချက်ထည့်ထားသော ကုဒ်များ** (အဆင့်ဆင့် အကြောင်းပြချက်များနှင့်အတူ)

### ပြည့်စုံသော နမူနာများဖြင့် စတင်ခြင်း

1. အထက်တွင် ဖော်ပြထားသော ဇယားမှ **သင့်နှစ်သက်ရာ ဘာသာစကား** ကို ရွေးပါ  
2. **ပြည့်စုံသော နမူနာဖိုင်ကို ပြန်လည်ကြည့်ရှုပါ** - အကောင်အထည်ဖော်မှု အပြည့်အစုံကို နားလည်ရန်  
3. [`complete_examples.md`](./complete_examples.md) တွင် ဖော်ပြထားသော လမ်းညွှန်ချက်များအတိုင်း **နမူနာကို အကောင်အထည်ဖော်ပါ**  
4. သင့်ရည်ရွယ်ချက်အတွက် အထူးပြု၍ **နမူနာကို ပြင်ဆင်ပြီး တိုးချဲ့ပါ**  

ဒီနမူနာများကို အကောင်အထည်ဖော်ခြင်းနှင့် ပြင်ဆင်မှုအတွက် အသေးစိတ် လမ်းညွှန်ချက်များကို ဖတ်ရန် - **[📖 ပြည့်စုံသော နမူနာများ လမ်းညွှန်ချက်](./complete_examples.md)** ကို ကြည့်ပါ။

### 💡 ဖြေရှင်းချက်နှင့် ပြည့်စုံသော နမူနာများ၏ ကွာခြားချက်

| **ဖြေရှင်းချက် ဖိုလ်ဒါ** | **ပြည့်စုံသော နမူနာများ** |
|--------------------|--------------------- |
| Build ဖိုင်များပါဝင်သော စီမံကိန်းဖွဲ့စည်းမှု အပြည့်အစုံ | တစ်ဖိုင်တည်းဖြင့် အကောင်အထည်ဖော်မှု |
| Dependencies များနှင့် အဆင်သင့် | အဓိကထားသော ကုဒ်နမူနာများ |
| ထုတ်လုပ်မှုဆိုင်ရာ အခြေအနေတူ စီမံကိန်း | ပညာရေးဆိုင်ရာ ရည်ညွှန်းချက် |
| ဘာသာစကားအလိုက် ကိရိယာများ | ဘာသာစကားများနှင့် နှိုင်းယှဉ်မှု |

နှစ်မျိုးစလုံး အဖိုးတန်ဖြစ်သည် - **ဖြေရှင်းချက် ဖိုလ်ဒါ** ကို ပြည့်စုံသော စီမံကိန်းများအတွက် အသုံးပြုပါ၊ **ပြည့်စုံသော နမူနာများ** ကို သင်ယူမှုနှင့် ရည်ညွှန်းချက်အတွက် အသုံးပြုပါ။

## အဓိက အချက်များ

ဒီအခန်းအတွက် အဓိက အချက်များမှာ -

- Client များသည် ဆာဗာပေါ်တွင် လုပ်ဆောင်ချက်များကို ရှာဖွေခြင်းနှင့် အကောင်အထည်ဖော်ခြင်းနှစ်မျိုးလုံးအတွက် အသုံးပြုနိုင်သည်။
- Client များသည် (ဒီအခန်းတွင် ဖော်ပြထားသကဲ့သို့) ကိုယ်တိုင် စတင်စဉ် ဆာဗာကို စတင်နိုင်သလို၊ ရှိပြီးသား ဆာဗာများနှင့်လည်း ချိတ်ဆက်နိုင်သည်။
- Inspector ကဲ့သို့သော အခြားရွေးချယ်စရာများနှင့် နှိုင်းယှဉ်ပါက ဆာဗာ၏ စွမ်းဆောင်ရည်များကို စမ်းသပ်ရန် Client သည် အလွန်ကောင်းမွန်သော နည်းလမ်းတစ်ခုဖြစ်သည်။

## ထပ်မံသော အရင်းအမြစ်များ

- [MCP တွင် Client များ တည်ဆောက်ခြင်း](https://modelcontextprotocol.io/quickstart/client)

## နမူနာများ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## နောက်တစ်ဆင့်

- နောက်တစ်ဆင့်: [LLM ဖြင့် Client တစ်ခု ဖန်တီးခြင်း](../03-llm-client/README.md)

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်ကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။ 