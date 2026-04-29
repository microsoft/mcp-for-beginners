# ការបង្កើតអតិថិជន

អតិថិជនគឺជាកម្មវិធីឆ្នោត ឬស្គ្រីបដែលតភ្ជាប់ដោយផ្ទាល់ទៅកាន់ម៉ាស៊ីនបម្រើ MCP ដើម្បីស្នើសុំធនធាន ឧបករណ៍ និងការជំរុញ។ ខុសពីការប្រើប្រាស់ឧបករណ៍ inspector ដែលផ្តល់ចំណុចប្រទាក់ក្រាហ្វិចសម្រាប់គ្រប់គ្រងម៉ាស៊ីនបម្រើ ការសរសេរអតិថិជនផ្ទាល់ជាការតភ្ជាប់ប្រព្រឹត្តតាមកម្មវិធីនិងស្វ័យប្រវត្តិ។ វាអនុញ្ញាតឲ្យអ្នកអភិវឌ្ឍន៍បញ្ចូលសមត្ថភាព MCP ក្នុងល្បងរបស់ខ្លួន ដំណើរការតាមស្វ័យប្រវត្តិ ហើយកសាងដំណោះស្រាយប្ដូរតាមតម្រូវការពិសេស។

## សង្ខេប

មេរៀននេះណែនាំពីគំនិតអតិថិជនក្នុងប្រព័ន្ធ Model Context Protocol (MCP)។ អ្នកនឹងរៀនពីរបៀបសរសេរអតិថិជនផ្ទាល់ខ្លួន ហើយធ្វើឲ្យវាតភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP។

## គោលបំណងការសិក្សា

នៅចុងបញ្ចប់នៃមេរៀននេះ អ្នកនឹងអាច:

- យល់ពីអ្វីដែលអតិថិជនអាចធ្វើបាន។
- សរសេរអតិថិជនផ្ទាល់ខ្លួន។
- តភ្ជាប់ និងសាកល្បងអតិថិជនជាមួយម៉ាស៊ីនបម្រើ MCP ដើម្បីធានាថាអាចដំណើរការដូចបានរំពឹង។

## តើមានអ្វីក្នុងការសរសេរអតិថិជន?

ដើម្បីសរសេរអតិថិជន អ្នកគួរតែក្នុងការធ្វើដូចខាងក្រោម៖

- **ធ្វើការនាំចូលបណ្ណាល័យត្រឹមត្រូវ**។ អ្នកនឹងប្រើបណ្ណាល័យដដែលស្ទើរតែចាស់ តែមុខងារផ្សេងៗ។
- **បង្កើតអតិថិជនមួយ**។ នេះជាការបង្កើតអតិថិជនមួយហើយតភ្ជាប់វាជាមួយវិធីសាស្រ្តផ្ទេរដែលបានជ្រើសរើស។
- **សម្រេចចិត្តទៅលើធនធានដែលត្រូវបញ្ជី**។ ម៉ាស៊ីនបម្រើ MCP របស់អ្នកមានធនធាន ឧបករណ៍ និងការជំរុញ អ្នកត្រូវសម្រេចចិត្តថាអ្វីខ្លះត្រូវបញ្ជី។
- **បញ្ចូលអតិថិជនទៅកម្មវិធីមេភ្ញៀវ**។ នៅពេលដែលអ្នកដឹងពីសមត្ថភាពម៉ាស៊ីនបម្រើ អ្នកត្រូវបញ្ចូលវាទៅកម្មវិធីមេភ្ញៀវ ដើម្បីបើអ្នកប្រើវាយជំរុញ ឬបញ្ជាដទៃទៀត អនុគមន៍ម៉ាស៊ីនបម្រើនោះនឹងត្រូវហៅ។

ឥឡូវនេះដែលយើងយល់ជារបៀបទូលំទូលាយ អ្នកអាចមើលឧទាហរណ៍ខាងក្រោម។

### ឧទាហរណ៍អតិថិជន

មកពិនិត្យមើលឧទាហរណ៍អតិថិជននេះ៖

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

// បញ្ជីចំលើយបន្តិចៗ
const prompts = await client.listPrompts();

// ទទួលបានចំលើយបន្តិច
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// បញ្ជីធនធាន
const resources = await client.listResources();

// អានធនធាន
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ហៅឧបករណ៍
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

ក្នុងកូដខាងលើ យើងបាន:

- នាំចូលបណ្ណាល័យ
- បង្កើតអតិថិជនមួយ ហើយតភ្ជាប់វា ដោយប្រើ stdio ជាវិធីផ្ទេរ។
- បញ្ជីការជំរុញ ធនធាន និងឧបករណ៍ ហើយហៅពួកវាទាំងអស់។

ដូច្នេះ អ្នកមានអតិថិជនដែលអាចនិយាយជាមួយម៉ាស៊ីនបម្រើ MCP ។

ចូរយើងចំណាយពេលនៅផ្នែកហាត់ប្រាណបន្ទាប់ ហើយវែងវង់ចែកងាកក្នុងកូដនីមួយៗនិងពន្យល់អំពីអ្វីកំពុងកើតឡើង។

## ហាត់ប្រាណ៖ សរសេរអតិថិជន

ដូចបាននិយាយខាងលើ មកចំណាយពេលនិយាយអំពីកូដ ហើយអាចសរសេរតាម បើអ្នកចង់។

### -1- នាំចូលបណ្ណាល័យ

សូមនាំចូលបណ្ណាល័យដែលអាចជួយបាន។ យើងនឹងត្រូវយោងទៅអតិថិជន និងព_PROTO_ transport ដែលបានជ្រើសរើស stdio។ stdio ជាព_PROTO_សម្រាប់រឿងដែលនឹងដំណើរការលើម៉ាស៊ីនបង្កើត។ SSE គឺជា transport protocol មួយទៀតដែលយើងនឹងបង្ហាញនៅជំពូកក្រោយ ប៉ុន្តែនេះជាជម្រើសផ្សេងទៀត។ ឥឡូវ មកបន្តជាមួយ stdio។

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

សម្រាប់ Java អ្នកនឹងបង្កើតអតិថិជនមួយ ដែលតភ្ជាប់ទៅម៉ាស៊ីនបម្រើ MCP ពីលំហាត់បណ្ដាំមុន។ ប្រើរចនាសម្ព័ន្ធគម្រោង Java Spring Boot ដដែលពី [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) បង្កើតថ្នាក់ Java ថ្មីឈ្មោះ `SDKClient` នៅក្នុងថត `src/main/java/com/microsoft/mcp/sample/client/` ហើយបន្ថែមការនាំចូលដូចខាងក្រោម៖

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

អ្នកត្រូវបន្ថែមអាសន្នកម្មខាងក្រោមទៅក្នុងឯកសារ `Cargo.toml` របស់អ្នក។

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

ពីទីនោះ អ្នកអាចនាំចូលបណ្ណាល័យដែលត្រូវការនៅឯកសារកូដអតិថិជនរបស់អ្នក។

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

មកបន្តការបង្កើត instance ។

### -2- បង្កើតអតិថិជន និង transport

យើងត្រូវបង្កើត instance សម្រាប់ transport និងអតិថិជនរបស់យើង៖

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

ក្នុងកូដខាងលើ យើងបាន៖

- បង្កើតឧបករណ៍ផ្ទេរព៌ត៍ stdio មួយ។ សូមចំណាំថាវាកំណត់បញ្ជារនិងអាគុយម៉ង់សម្រាប់រកនិងចាប់ផ្តើមម៉ាស៊ីនបម្រើ ដូចជារឿងដែលយើងត្រូវធ្វើខណៈបង្កើតអតិថិជន។

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- បង្កើតអតិថិជនដោយផ្ដល់ឈ្មោះ និងកំណែ។

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- តភ្ជាប់អតិថិជនទៅ transport ដែលបានជ្រើសរើស។

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# បង្កើតប៉ារ៉ាម៉ែត្រ​ម៉ាស៊ីនបម្រើ​សម្រាប់ការតភ្ជាប់ stdio
server_params = StdioServerParameters(
    command="mcp",  # កម្មវិធីអាចប اجرا បាន
    args=["run", "server.py"],  # អនុគ្រោះ​បញ្ជាលបញ្ជា ជាជម្រើស
    env=None,  # អថេរបរិស្ថានជាជម្រើស
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

ក្នុងកូដខាងលើ យើងបាន：

- នាំចូលបណ្ណាល័យដែលត្រូវការ
- បង្កើតអង្គភាពប៉ារ៉ាម៉ែត្រម៉ាស៊ីនបម្រើមួយ ដើម្បីប្រើដើម្បីរត់ម៉ាស៊ីនបម្រើ ហើយតភ្ជាប់ទៅវាជាមួយអតិថិជន។
- សរសេរប្រភេទមេធដ៍ `run` ដែលហៅទៅ `stdio_client` ដែលចាប់ផ្តើមសម័យអតិថិជន។
- បង្កើតចំណុចចូល ដែលផ្ដល់មេធដ៍ `run` ទៅ `asyncio.run`។

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

ក្នុងកូដខាងលើ យើងបាន:

- នាំចូលបណ្ណាល័យដែលត្រូវការ។
- បង្កើត transport stdio និងបង្កើតអតិថិជន `mcpClient`។ អាតិថិជននេះយើងនឹងប្រើដើម្បីបញ្ជីនិងហៅមុខងារ លើម៉ាស៊ីនបម្រើ MCP។

សូមចំណាំ នៅ "Arguments" អ្នកអាចបញ្ជាក់ទៅកាន់ *.csproj* ឬឯកសារបញ្ចូល។

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
        
        // ឡូជិចភ្ញ៉ៀវរបស់អ្នកស្ថិតនៅទីនេះ
    }
}
```

ក្នុងកូដខាងលើ យើងបាន:

- បង្កើតមេធដ៍មួយដែលកំណត់ SSE transport បញ្ជូនទៅ `http://localhost:8080` ដែលម៉ាស៊ីនបម្រើ MCP នឹងដំណើរការ។
- បង្កើតថ្នាក់អតិថិជន មួយ ទទួល transport ជាព៉ារ៉ាម៉ែត្រនៅពេលបង្កើត។
- នៅក្នុងមេធដ៍ `run` យើងបង្កើតអតិថិជន MCP សម័យវិញដោយប្រើ transport ហើយបញ្ចូលតភ្ជាប់។
- ប្រើ SSE (Server-Sent Events) transport ដែលសមស្របសម្រាប់ការទំនាក់ទំនង HTTP ជាមួយម៉ាស៊ីនបម្រើ MCP Java Spring Boot។

#### Rust

សូមចំណាំអតិថិជន Rust នេះអនុញ្ញាតថាម៉ាស៊ីនបម្រើគឺជាគំរោងជាប់នាម "calculator-server" នៅក្នុងថតដូចគ្នា។ កូដខាងក្រោមនឹងចាប់ផ្តើមម៉ាស៊ីនបម្រើ ហើយតភ្ជាប់ទៅវា។

```rust
async fn main() -> Result<(), RmcpError> {
    // សន្មត់ថាគេហទំព័រជាគម្រោងបងប្អូនដែលមានឈ្មោះថា "calculator-server" នៅក្នុងថតដូចគ្នា
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

    // TODO: ចាប់ផ្តើម

    // TODO: បង្ហាញបញ្ជីឧបករណ៍

    // TODO: ហៅឧបករណ៍បន្ថែមជាមួយអាគុយម៉ង់ = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- បញ្ជីមុខងារម៉ាស៊ីនបម្រើ

ឥឡូវនេះ យើងមានអតិថិជន ដែលអាចភ្ជាប់បានបើគម្រោងដំណើរការ។ ទោះយ៉ាងណា វាមិនបានបញ្ជីមុខងាររបស់វាទេ ដូច្នេះយើងនឹងធ្វើវាបន្ទាប់៖

#### TypeScript

```typescript
// បញ្ជីសំណើ
const prompts = await client.listPrompts();

// បញ្ជីធនធាន
const resources = await client.listResources();

// បញ្ជីឧបករណ៍
const tools = await client.listTools();
```

#### Python

```python
# បញ្ជីធនធានដែលអាចប្រើបាន
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# បញ្ជីឧបករណ៍ដែលអាចប្រើបាន
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

នៅទីនេះ យើងបញ្ជីធនធាន `list_resources()` និងឧបករណ៍ `list_tools` ហើយបោះពុម្ភវា។

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ខាងលើគឺជាគំរូនៃរបៀបបញ្ជីឧបករណ៍នៅលើម៉ាស៊ីនបម្រើ។ សម្រាប់ឧបករណ៍នីមួយៗ យើងបោះពុម្ភឈ្មោះវា។

#### Java

```java
// បញ្ជី និងបង្ហាញឧបករណ៍
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// អ្នកអាចផ្ញើសញ្ញាថ្មីទៅម៉ាស៊ីនបម្រើដើម្បីផ្ទៀងផ្ទាត់ការតភ្ជាប់បានផងដែរ
client.ping();
```

ក្នុងកូដខាងលើ យើងបាន:

- ហៅ `listTools()` ដើម្បីទទួលឧបករណ៍ដែលមានពីម៉ាស៊ីនបម្រើ MCP។
- ប្រើ `ping()` ដើម្បីផ្ទៀងផ្ទាត់តភ្ជាប់ទៅម៉ាស៊ីនបម្រើឲ្យដំណើរការ។
- `ListToolsResult` មានព័ត៌មានអំពីឧបករណ៍ទាំងអស់ រួមមានឈ្មោះ វិធាន និងស្គីមាតំណើបញ្ចូល។

អស្ចារ្យ ឥឡូវយើងបានចាប់យកគ្រប់មុខងារ។ តើពេលណាដែលយើងប្រើវាទេ? អតិថិជននេះសាមញ្ញ ព្រោះយើងត្រូវហៅមុខងារដោយ explcitly នៅពេលដែលយើងត្រូវការ។ នៅជំពូកក្រោយ អ្នកនឹងបង្កើតអតិថិជនមួយកាន់តែលំអិតដែលមានម៉ូដែលភាសាធំនៃខ្លួនឯង LLM។ ឥឡូវតែបើកនិយមកើតហៅមុខងារម៉ាស៊ីនបម្រើ៖

#### Rust

នៅមុខងារចម្បង បន្ទាប់ពីចាប់ផ្តើមអតិថិជន យើងអាចចាប់ផ្តើមម៉ាស៊ីនបម្រើ និងបញ្ជីមុខងារមួយចំនួនរបស់វា។

```rust
// ចាប់ផ្ដើម
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// បញ្ជីឧបករណ៍
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ហៅមុខងារ

ដើម្បីហៅមុខងារ យើងត្រូវប្រាកដថាយើងបានបញ្ជាក់អាគុយម៉ង់ត្រឹមត្រូវ ហើយនៅខ្លះអាចត្រូវបញ្ជាក់ឈ្មោះអ្វីដែលត្រូវហៅ។

#### TypeScript

```typescript

// អានធនធាន
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ហៅឧបករណ៍មួយ
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// ហៅស្នើសុំ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

ក្នុងកូដខាងលើ យើងបាន:

- អានធនធានមួយ យើងហៅធនធានដោយហៅ `readResource()` បញ្ជាក់ `uri`។ នេះជាមើលទៅម៉ាស៊ីនបម្រើ:

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

    តម្លៃ `uri` របស់យើង `file://example.txt` ត្រូវគ្នា `file://{name}` នៅម៉ាស៊ីនបម្រើ។ `example.txt` នឹងតំណាងឲ្យ `name`។

- ហៅឧបករណ៍មួយ យើងហៅវាដោយបញ្ជាក់ `name` និង `arguments` ដូចខាងក្រោម:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ទទួលបានជំរុញ ដើម្បីទទួលជំរុញ អ្នកហៅ `getPrompt()` ជាមួយ `name` និង `arguments`។ កូដម៉ាស៊ីនបម្រើមើលដូចខាងក្រោម៖

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

    ហើយកូដអតិថិជនរបស់អ្នកក៏មើលដូចខាងក្រោមដើម្បីត្រូវនឹងអ្វីបានប្រកាសនៅម៉ាស៊ីនបម្រើ៖

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
# អានធនធាន
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ហៅឧបករណ៍
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

ក្នុងកូដខាងលើ យើងបាន:

- ហៅធនធានមួយដែលមានឈ្មោះ `greeting` ដោយប្រើ `read_resource`។
- ហៅឧបករណ៍មួយដែលមានឈ្មោះ `add` ដោយប្រើ `call_tool`។

#### .NET

1. មកបន្ថែមកូដហៅឧបករណ៍៖

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ដើម្បីបោះពុម្ភលទ្ធផល នេះជាកូដដើម្បីដោះស្រាយវា៖

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// ហៅឧបករណ៍គណនាផ្សេងៗ
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

ក្នុងកូដខាងលើ យើងបាន:

- ហៅឧបករណ៍គណនាច្រើន ដោយប្រើវិធីសាស្រ្ត `callTool()` ជាមួយវត្ថុ `CallToolRequest`។
- ការហៅរាល់ឧបករណ៍បញ្ជាក់ឈ្មោះឧបករណ៍ និង `Map` នៃអាគុយម៉ង់ដែលត្រូវការដោយឧបករណ៍នោះ។
- ឧបករណ៍ម៉ាស៊ីនបម្រើចង់បានឈ្មោះប៉ារ៉ាម៉ែត្រពិសេស (ដូចជា "a", "b" សម្រាប់ប្រតិបត្តិការគណនា)។
- លទ្ធផលត្រូវបានត្រឡប់ជាវត្ថុ `CallToolResult` ដែលមានចម្លើយពីម៉ាស៊ីនបម្រើ។

#### Rust

```rust
// ហៅឧបករណ៍បូកជាមួយអាគុយម៉ង់ = {"a": 3, "b": 2}
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

### -5- ដំណើរការអតិថិជន

ដើម្បីដំណើរការអតិថិជន សូមវាយពាក្យបញ្ជាខាងក្រោមនៅក្នុងបន្ទាត់បញ្ជា:

#### TypeScript

បន្ថែមចំណុចចូលខាងក្រោមទៅផ្នែក "scripts" នៅក្នុង *package.json* របស់អ្នក៖

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

ហៅអតិថិជនជាមួយពាក្យបញ្ជាខាងក្រោម៖

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ជាមុន សូមធានាថាម៉ាស៊ីនបម្រើ MCP របស់អ្នកកំពុងដំណើរការ នៅលើ `http://localhost:8080`។ បន្ទាប់មកដំណើរការអតិថិជន៖

```bash
# សាងសង់គម្រោងរបស់អ្នក
./mvnw clean compile

# នៅរត់កម្មវិធីអតិថិជន
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ជាជម្រើសផ្សេង អ្នកអាចដំណើរការគម្រោងអតិថិជនពេញលេញដែលផ្ដល់នៅថតដំណោះស្រាយ `03-GettingStarted\02-client\solution\java`៖

```bash
# ធ្វើការ ទៅកាន់ថតដោះស្រាយ
cd 03-GettingStarted/02-client/solution/java

# បង្កើត និងរត់ JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## កិច្ចការផ្ទាល់ខ្លួន

នៅក្នុងកិច្ចការនេះ អ្នកនឹងប្រើចំណេះដឹងដែលអង្គុយក្នុងការបង្កើតអតិថិជន ប៉ុន្តែបង្កើតអតិថិជនផ្ទាល់ខ្លួន។

នេះជាម៉ាស៊ីនបម្រើមួយដែលអ្នកអាចប្រើ ហើយត្រូវហៅតាមកូដអតិថិជនរបស់អ្នក ដើម្បីបន្ថែមមុខងារបន្ថែមធ្វើឲ្យវាមានចំណាប់អារម្មណ៍។

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// បង្កើតម៉ាស៊ីនបម្រើ MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// បន្ថែមឧបករណ៍បូកបន្ថែម
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// បន្ថែមធនធានស្វាគមន៍ឌីណាមិច
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

// ចាប់ផ្តើមទទួលសារនៅលើ stdin និងផ្ញើសារនៅលើ stdout

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

# បង្កើតម៉ាស៊ីនបម្រើ MCP
mcp = FastMCP("Demo")


# បញ្ចូលឧបករណ៍បូក
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# បន្ថែមធនធានស្វាគមន៍ដYNAMIC
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

មើលគម្រោងនេះ ដើម្បីមើលរបៀប [បន្ថែមជំរុញ និងធនធាន](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)។

ផងដែរ សូមពិនិត្យតំណភ្ជាប់នេះ សម្រាប់របៀបហៅ [ជំរុញ និងធនធាន](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)។

### Rust

នៅក្នុង [ផ្នែកមុន](../../../../03-GettingStarted/01-first-server) អ្នកបានរៀនរបៀបបង្កើតម៉ាស៊ីនបម្រើ MCP មួយងាយស្រួលជាមួយ Rust។ អ្នកអាចបន្តកសាងលើវា ឬពិនិត្យតំណភ្ជាប់នេះ សម្រាប់ឧទាហរណ៍ម៉ាស៊ីនបម្រើ MCP បែប Rust៖ [ឧទាហរណ៍ម៉ាស៊ីនបម្រើ MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ដំណោះស្រាយ

**ថតដំណោះស្រាយ** មានការអនុវត្តអតិថិជនពេញលេញ ដែលអាចដំណើរការបានទាំងស្រុង បង្ហាញគំនិតទាំងអស់ដែលបានរៀនក្នុងមេរៀននេះ។ រាល់ដំណោះស្រាយមានកូដអតិថិជន និងម៉ាស៊ីនបម្រើរៀបចំក្នុងគំរោងដាច់ដោយឡែក។

### 📁 រចនាសម្ព័ន្ធដំណោះស្រាយ

ថតដំណោះស្រាយត្រូវបានរៀបចំដោយភាសាកម្មវិធី៖

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

### 🚀 អ្វីដែលរាល់ដំណោះស្រាយមាន

រាល់ដំណោះស្រាយបែបភាសា ផ្តល់:

- **អនុវត្តអតិថិជនពេញលេញ** ជាមួយមុខងារទាំងអស់ពីមេរៀន
- **រចនាសម្ព័ន្ធគម្រោងដំណើរការបាន** ជាមួយការព្យាយាមនិងការកំណត់ត្រឹមត្រូវ
- **ស្គ្រីបកសាង និងដំណើរការ** សម្រាប់ការតំឡើង និងដំណើរការ ងាយស្រួល
- **README ពិស្តារ** ជាមួយការណែនាំជាក់លាក់ផ្អែកលើភាសា
- **ការដោះស្រាយកំហុស និងគំរូដំណោះស្រាយលទ្ធផល**

### 📖 ការប្រើប្រាស់ដំណោះស្រាយ

1. **ចូលទៅថតភាសាដែលអ្នកចូលចិត្ត**៖

   ```bash
   cd solution/typescript/    # សម្រាប់ TypeScript
   cd solution/java/          # សម្រាប់ Java
   cd solution/python/        # សម្រាប់ Python
   cd solution/dotnet/        # សម្រាប់ .NET
   ```

2. **អនុវត្តតាមការណែនាំ README** របស់រាល់ថតសម្រាប់៖
   - តំឡើងការពឹងផ្អែក
   - កសាងគម្រោង
   - ដំណើរការ​អតិថិជន

3. **លទ្ធផលគំរូដែលអ្នកគួរមើលឃើញ៖**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

សម្រាប់ឯកសារពេញលេញ និងការណែនាំជាប្រយោជន៍ សូមមើល៖ **[📖 Solution Documentation](./solution/README.md)**

## 🎯 ឧទាហរណ៍ពេញលេញ

យើងបានផ្ដល់អនុវត្តអតិថិជនទាំងស្រុង សម្រាប់ភាសាកម្មវិធីទាំងអស់ដែលបានរៀបរាប់ក្នុងមេរៀននេះ។ ឧទាហរណ៍ទាំងនេះបង្ហាញមុខងារពេញលេញ និងអាចប្រើជាគំរូហើយចាប់ផ្តើមសម្រាប់គម្រោងរបស់អ្នក។

### អនុវត្តទាំងស្រុងដែលមាន

| ភាសា | ឯកសារ | ការពិពណ៌នា |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | អតិថិជន Java ពេញលេញប្រើ SSE transport ជាមួយការគ្រប់គ្រងកំហុសយ៉ាងពេញលេញ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | អតិថិជន C# ពេញលេញប្រើ stdio transport ជាមួយការចាប់ផ្តើមម៉ាស៊ីនបម្រើដោយស្វ័យប្រវត្តិ |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | អតិថិជន TypeScript ពេញលេញជាមួយគាំទ្រព_PROTOCOL MCP ពេញលេញ |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | អតិថិជន Python ពេញលេញប្រើគំរូ async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | អតិថិជន Rust ពេញលេញប្រើ Tokio សម្រាប់ប្រតិបត្តិការពហុកាល |

រាល់ឧទាហរណ៍ពេញលេញរួមមាន:
- ✅ **ការតភ្ជាប់និងការដោះស្រាយកំហុស**
- ✅ **ការស្វែងរកម៉ាស៊ីនបម្រើ** (ឧបករណ៍, ធនធាន, សំណួរដែលអាចអនុវត្តបាន)
- ✅ **ប្រតិបត្តិការជាាគណនី** (បូក, ដក, គុណ, ចែក, ជំនួយ)
- ✅ **ការតម្រៀបលទ្ធផល** និងការបញ្ចេញលទ្ធផលដែលមានទ្រង់ទ្រាយ
- ✅ **ការដោះស្រាយកំហុសដោយទូលំទូលាយ**
- ✅ **កូដស្អាត, មានឯកសារ** ជាមួយមតិយោបល់ជាដំណាក់កាលៗ

### ចាប់ផ្តើមជាមួយឧទាហរណ៍ពេញលេញ

1. **ជ្រើសរើសភាសាដែលអ្នកចូលចិត្ត** ពីតារាងខាងលើ
2. **ពិនិត្យឯកសារឧទាហរណ៍ពេញលេញ** ដើម្បីយល់ពីការអនុវត្តពេញលេញ
3. **រត់ឧទាហរណ៍** តាមការណែនាំនៅក្នុង [`complete_examples.md`](./complete_examples.md)
4. **កែប្រែ និងបន្ថែម** ឧទាហរណ៍សម្រាប់ករណីប្រើប្រាស់របស់អ្នក

សម្រាប់ឯកសារពីលម្អិតអំពីរបៀបរត់ និងប្តូរការវឺនឧទាហរណ៍ទាំងនេះ ពិនិត្យមើល: **[📖 ឯកសារឧទាហរណ៍ពេញលេញ](./complete_examples.md)**

### 💡 ដំណោះស្រាយប្រៀបធៀបនឹងឧទាហរណ៍ពេញលេញ

| **ថតដំណោះស្រាយ**          | **ឧទាហរណ៍ពេញលេញ**          |
|----------------------------|-----------------------------|
| រចនាសម្ព័ន្ធគម្រោងពេញលេញជាមួយឯកសារសង់សម្រាប់    | ការអនុវត្តឯកសារតែមួយ          |
| រៀបចំរួចរាល់ជាមួយការពឹងផ្អែក       | ឧទាហរណ៍កូដផ្តោតតែមួយ         |
| ការតំឡើងសម្រាប់ផលិតកម្ម         | ឯកសារយោងសិក្សា                    |
| ឧបករណ៍ជាភាសា             | ការប្រៀបធៀបជាភាសាច្រើនដូចគ្នា   |

វិធីទាំងពីរនេះមានតម្លៃ - ប្រើ **ថតដំណោះស្រាយ** សម្រាប់គម្រោងពេញលេញ និង **ឧទាហរណ៍ពេញលេញ** សម្រាប់ការសិក្សា និងយោង។

## ចំនុចសំខាន់

ចំនុចសំខាន់សម្រាប់ជំពូកនេះស្ដីពីអតិថិជនមានដូចជា៖

- អាចប្រើសម្រាប់ស្វែងរក និងហៅមុខងារលើម៉ាស៊ីនបម្រើ។
- អាចចាប់ផ្តើមម៉ាស៊ីនបម្រើខ្លួនឯងក្នុងពេលវាចាប់ផ្តើម (ដូចជាជំពូកនេះ) ប៉ុន្តែអតិថិជនអាចភ្ជាប់ទៅម៉ាស៊ីនបម្រើដែលកំពុងរត់បានផងដែរ។
- ជាវិធីដ៏ល្អក្នុងការប្រមោលសមត្ថភាពម៉ាស៊ីនបម្រើជាមួយជម្រើសផ្សេងៗដូចជា Inspector ដែលបានពិពណ៌នានៅជំពូកមុន។

## ធនធានបន្ថែម

- [ការសាងសង់អតិថិជននៅ MCP](https://modelcontextprotocol.io/quickstart/client)

## ឧទាហរណ៍

- [កម្មវិធីគណនាភាសា Java](../samples/java/calculator/README.md)
- [កម្មវិធីគណនាភាសា .Net](../../../../03-GettingStarted/samples/csharp)
- [កម្មវិធីគណនាភាសា JavaScript](../samples/javascript/README.md)
- [កម្មវិធីគណនាភាសា TypeScript](../samples/typescript/README.md)
- [កម្មវិធីគណនាភាសា Python](../../../../03-GettingStarted/samples/python)
- [កម្មវិធីគណนាភាសា Rust](../../../../03-GettingStarted/samples/rust)

## អ្វីដែលនៅខាងក្រោយ

- បន្ទាប់: [ការបង្កើតអតិថិជនជាមួយ LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈដែលយើងខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាមូលដ្ឋានគួរត្រូវបានត្រូវបានពិចារណារបស់ផ្លូវការជាដើម។ សម្រាប់ព័ត៌មានសំខាន់ៗ យើងណែនាំឱ្យប្រើការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំឬការបកប្រែខុសណាមួយដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->