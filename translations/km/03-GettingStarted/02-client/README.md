# ការបង្កើតមួយកាន់តែម្ដង

កាន់តែម្ដង គឺជាកម្មវិធីឯកជន ឬស្គ្រីបដែល​ទំនាក់ទំនងដោយផ្ទាល់ជាមួយម៉ាស៊ីនមើល MCP ដើម្បីស្នើរសុំធនធាន ឧបករណ៍ និងបម្ដៅ។ ផ្ទុយពីការប្រើឧបករណ៍ inspector ដែលផ្តល់អ៊ីនធ័រផ្សារដែកសម្រាប់អន្តរកម្មជាមួយម៉ាស៊ីនមើល ការសរសេរកាន់តែម្ដងរបស់អ្នកឲ្យអាចធ្វើបានការអន្តរកម្មតាមរយៈកម្មវិធី និងស្វ័យកាល។ នេះអនុញ្ញាតឲ្យអ្នកអភិវឌ្ឍបញ្ចូលសមត្ថភាព MCP ទៅក្នុងចំណោមការងាររបស់ពួកគេ រៀបចំកិច្ចការជាស្វ័យប្រវត្តិ និងបង្កើតដំណោះស្រាយតាមការទាមទារពិសេស។

## ទិដ្ឋភាពទូទៅ

មេរៀននេះណែនាំអំពីគំនិតអតិថិជននៅក្នុងប្រព័ន្ធ Model Context Protocol (MCP)។ អ្នកនឹងបានរៀនពីរបៀបសរសេរកាន់តែម្ដងរបស់អ្នក និងធ្វើឲ្យវាតភ្ជាប់ទៅម៉ាស៊ីនមើល MCP។

## គោលបំណងរៀន

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- យល់ដឹងថាកាន់តែម្ដងអាចធ្វើអ្វីបានខ្លះ។
- សរសេរកាន់តែម្ដងជារបស់អ្នក។
- ភ្ជាប់ និងសាកល្បងកាន់តែម្ដងជាមួយម៉ាស៊ីនមើល MCP ដើម្បីធានាថាវាធ្វើការត្រឹមត្រូវ។

## តើមានអ្វីនៅក្នុងការសរសេរកាន់តែម្ដង?

ដើម្បីសរសេរកាន់តែម្ដង អ្នកនឹងត្រូវធ្វើដូចខាងក្រោម៖

- ** នាំយកបណ្ណាល័យត្រឹមត្រូវ **។ អ្នកនឹងប្រើបណ្ណាល័យដូចគ្នាថ្មីដូចមុន ប៉ុន្តែជាសំណុំផ្សេងគ្នា។
- ** បង្កើតតំណាងអតិថិជន **។ នេះនឹងពាក់ព័ន្ធនឹងការបង្កើតបំណលាងអតិថិជន និងភ្ជាប់វានឹងវិធីសាស្រ្តផ្ទេរដែលបានជ្រើសរើស។
- ** សំរេចចិត្តពីធនធានត្រូវបញ្ជី **។ ម៉ាស៊ីនមើល MCP របស់អ្នកមានធនធាន ឧបករណ៍ និងបម្ដៅ អ្នកត្រូវសំរេចចិត្តពីអ្វីដែលត្រូវបញ្ជី។
- ** បញ្ចូលអតិថិជនទៅកម្មវិធីម៉ាស៊ីនម៉ាស៊ីនចាស់ **។ ពេលដែលអាចដឹងពីសមត្ថភាពនៃម៉ាស៊ីនមើល អ្នកត្រូវបញ្ចូលវាទៅកម្មវិធីម៉ាស៊ីនម៉ាស៊ីនចាស់របស់អ្នក ដូច្នេះបើអ្នកប្រើប្រាស់វាយបម្ដៅ ឬបញ្ជា មុខងារម៉ាស៊ីនមើលដែលពាក់ព័ន្ធនឹងត្រូវបានហៅ។

ឥឡូវនេះយើងបានយល់នៅកម្រិតខ្ពស់ពីអ្វីដែលយើងត្រូវធ្វើ តោះមើលឧទាហរណ៍ខាងក្រោម។

### អតិថិជនឧទាហរណ៍

តោះមើលអតិថិជនឧទាហរណ៍នេះ៖

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

// បញ្ជីពាក្យបង្ហាញ
const prompts = await client.listPrompts();

// ទទួលបានពាក្យបង្ហាញ
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

នៅក្នុងកូដខាងលើ យើងបាន:

- នាំយកបណ្ណាល័យ
- បង្កើតធាតុអតិថិជន និងភ្ជាប់វា​ប្រើ stdio ជាវិធីផ្ទេរ។
- បញ្ជីបម្ដៅធនធាន និងឧបករណ៍ និងហៅពួកវាទាំងអស់។

នេះហើយជាកាន់តែម្ដងដែលអាចនិយាយទៅម៉ាស៊ីនមើល MCP។

តោះយើងយកពេលវេលារបស់យើងនៅក្នុងផ្នែកហាត់ប្រាណបន្ទាប់ ហើយបំបែករៀបរាប់កូដនីតិវិធីនីមួយ និងពន្យល់អំពីអ្វីដែលកើតឡើង។

## ហាត់ប្រាណ៖ សរសេរកាន់តែម្ដង

ដូចបាននិយាយខាងលើ តោះយើងយកពេលវេលារយៈពេលពន្យល់កូដ ហើយបើចង់អាចសរសេរជាមួយគ្នា។

### -1- នាំយកបណ្ណាល័យ

តោះនាំយកបណ្ណាល័យដែលយើងត្រូវការ អ្នកនឹងត្រូវការតំណភ្ជាប់ទៅអតិថិជន និងរបៀបផ្ទេរដែលបានជ្រើសរើស stdio។ stdio ជាប្រព័ន្ធផ្ទេរដើម្បីបដិសណ្ឋារកម្មនៅលើម៉ាស៊ីនរបស់អ្នក។ SSE គឺជាប្រព័ន្ធផ្ទេរផ្សេងមួយដែលយើងនឹងបង្ហាញនៅជំពូកខាងក្រោយ ប៉ុន្តេសម្រាប់ឥឡូវនេះ តោះបន្តជាមួយ stdio។

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

សម្រាប់ Java អ្នកនឹងបង្កើតអតិថិជនដែលភ្ជាប់ទៅម៉ាស៊ីនមើល MCP ពីហាត់ប្រាណមុន។ ប្រើរចនាសម្ព័ន្ធគម្រោង Java Spring Boot ដូចក្នុង [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) បង្កើតថ្នាក់ Java ថ្មីឈ្មោះ `SDKClient` ក្នុងថត `src/main/java/com/microsoft/mcp/sample/client/` ហើយបន្ថែមការនាំចូលដូចខាងក្រោម៖

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

អ្នកនឹងត្រូវបន្ថែមការគាំទ្រខាងក្រោមទៅឯកសារ `Cargo.toml` របស់អ្នក។

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

ពីទីនេះ អ្នកអាចនាំយកបណ្ណាល័យចាំបាច់នៅក្នុងកូដអតិថិជនរបស់អ្នក។

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

តោះបន្តទៅកាន់ការបង្កើត។

### -2- បង្កើតអតិថិជន និងការផ្ទេរ

យើងត្រូវបង្កើតធាតុផ្ទេរ និងអតិថិជនរបស់យើង៖

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

នៅក្នុងកូដខាងលើ យើងបាន:

- បង្កើតធាតុផ្ទេរ stdio។ ចំណាំថាវាចែងបញ្ជា និងអាគុយម៉ង់ចំពោះរបៀបរកនិងចាប់ផ្ដើមម៉ាស៊ីនមើល ដូចជា។ វាជាអ្វីដែលយើងត្រូវធ្វើក្នុងការបង្កើតអតិថិជន។

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

- ភ្ជាប់អតិថិជនទៅវិធីផ្ទេរដែលបានជ្រើសរើស។

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# បង្កើតប៉ារ៉ាម៉ែត្រប្រតិបត្តិការសម្រាប់ការតភ្ជាប់ stdio
server_params = StdioServerParameters(
    command="mcp",  # ឯកសារអាចបញ្ជាលើច
    args=["run", "server.py"],  # ពាក្យបញ្ជាជម្រើស
    env=None,  # បំលែងបរិស្ថានជម្រើស
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # ដំណើរការការតភ្ជាប់
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

នៅក្នុងកូដខាងលើ យើងបាន:

- នាំយកបណ្ណាល័យចាំបាច់
- បង្កើតវត្ថុប៉ារ៉ាម៉ែត្រម៉ាស៊ីនមើល ដែលយើងនឹងប្រើដើម្បីបើកម៉ាស៊ីនមើល ដើម្បីភ្ជាប់វាជាមួយអតិថិជនរបស់យើង។
- កំណត់វិធីសាស្រ្ត `run` ដែលហៅ `stdio_client` ដែលចាប់ផ្ដើមសម័យអតិថិជន។
- បង្កើតចំណុចចូលដែលផ្ដល់វិធីសាស្រ្ត `run` ទៅ `asyncio.run`។

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

នៅក្នុងកូដខាងលើ យើងបាន:

- នាំយកបណ្ណាល័យចាំបាច់។
- បង្កើតផ្ទេរប្រភេទ stdio និងបង្កើតអតិថិជន `mcpClient`។ វាជាអ្វីដែលយើងប្រើសម្រាប់បញ្ជីនិងហៅមុខងារនៅលើម៉ាស៊ីនមើល MCP។

ចំណាំ នៅក្នុង "Arguments" អ្នកអាចបញ្ជូនទៅ *.csproj* ឬទៅឯកសារប្រតិបត្តិការណ៍។

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
        
        // តារាជីវិតអតិថិជនរបស់អ្នកនៅទីនេះ
    }
}
```

នៅក្នុងកូដខាងលើ យើងបាន:

- បង្កើតវិធីសាស្រ្ត main ដែលកំណត់ផ្ទេរ SSE វាយសម្លេងទៅ `http://localhost:8080` ដែលម៉ាស៊ីនមើល MCP របស់យើងនឹងដំណើរការ។
- បង្កើតថ្នាក់អតិថិជន ដែលទទួលផ្ទេរ ជាពារពាស់ដើម្បីគេន់ក្នុងការសាងសង់។
- ក្នុងវិធី run យើងបង្កើតអតិថិជន MCP ប្រើផ្ទេរ និងចាប់ផ្ដើមការភ្ជាប់។
- ប្រើផ្ទេរប្រភេទ SSE (Server-Sent Events) ដែលសមស្របសម្រាប់ការទំនាក់ទំនង HTTP ជាមួយម៉ាស៊ីនមើល MCP Spring Boot Java។

#### Rust

ចំណាំថា អតិថិជន Rust នេះសន្មតថាម៉ាស៊ីនមើលគឺជាគម្រោងបងប្អូនឈ្មោះ "calculator-server" នៅក្នុងថតតែមួយ។ កូដខាងក្រោមនឹងចាប់ផ្ដើមម៉ាស៊ីនមើល និងភ្ជាប់ទៅវា។

```rust
async fn main() -> Result<(), RmcpError> {
    // សន្មត់ថា server គឺជា​គម្រោង​ប្អូនប្រុស​ដែល​មានឈ្មោះ "calculator-server" នៅ​ក្នុងថតដដែលគ្នា
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

    // TODO: បញ្ជីឧបករណ៍

    // TODO: ហៅឧបករណ៍បន្ថែមជាមួយអា​រ៉ឺមិន = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- បញ្ជីមុខងារម៉ាស៊ីនមើល

ឥឡូវនេះ យើងមានអតិថិជនដែលអាចភ្ជាប់បានបើកម្មវិធីត្រូវបានដំណើរការ។ ទោះជាយ៉ាងណា វាមិនបញ្ជីមុខងាររបស់វានោះទេ ដូច្នេះតោះធ្វើទៅឲ្យវា៖

#### TypeScript

```typescript
// បញ្ជីប្រធានបទ
const prompts = await client.listPrompts();

// បញ្ជីធនធាន
const resources = await client.listResources();

// បញ្ជីឧបករណ៍
const tools = await client.listTools();
```

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
```

នៅទីនេះយើងបញ្ជីធនធានដែលអាចប្រើបាន `list_resources()` និងឧបករណ៍ `list_tools` ហើយបោះពុម្ពអោយឃើញ។

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

ខាងលើគឺជាឧទាហរណ៍ពីរបៀបយើងអាចបញ្ជីឧបករណ៍នៅលើម៉ាស៊ីនមើល។ សម្រាប់ឧបករណ៍មួយៗ យើងបោះពុម្ពឈ្មោះវា។

#### Java

```java
// បញ្ជី និងបង្ហាញឧបករណ៍
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// អ្នកអាចផ្ញើ ping ទៅម៉ាស៊ីនשרת ដើម្បីផ្ទៀងផ្ទាត់ការតភ្ជាប់បានដែរ
client.ping();
```

នៅក្នុងកូដខាងលើ យើងបាន:

- ហៅ `listTools()` ដើម្បីទទួលបានឧបករណ៍ទាំងអស់ដែលអាចប្រើបានពីម៉ាស៊ីនមើល MCP។
- ប្រើ `ping()` ដើម្បីបញ្ជាក់ថាការភ្ជាប់ទៅម៉ាស៊ីនមើលកំពុងដំណើរការ។
- `ListToolsResult` រួមមានព័ត៌មានអំពីឧបករណ៍ទាំងអស់ រួមទាំងឈ្មោះ ការពិពណ៌នា និងស្គីមទិន្នន័យបញ្ចូល។

ល្អណាស់ ឥឡូវនេះយើងបានចាប់យកមុខងារទាំងអស់ហើយ។ ពេលណាអ្នកប្រើវា? អតិថិជននេះគឺសាមញ្ញ ខ្លះៗគួរតែហៅមុខងារដោយច្បាស់នៅពេលចង់បានវា។ ក្នុងជំពូកបន្ទាប់ យើងនឹងបង្កើតអតិថិជនដ៏បច្ចេកវិទ្យាដែលមានការចូលដំណើរការទៅម៉ូដែលភាសាធំនៅក្នុងខ្លួនវា (LLM)។ ចំពោះពេលនេះ តោះមើលរបៀបហៅមុខងារនៅលើម៉ាស៊ីនមើល៖

#### Rust

ក្នុងមុខងារសំខាន់បន្ទាប់ពីចាប់ផ្តើមអតិថិជន អ្នកអាចចាប់ផ្តើមម៉ាស៊ីនមើល និងបញ្ជីមុខងារមួយចំនួនរបស់វា។

```rust
// ចាប់ផ្តើម
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// បញ្ជីឧបករណ៍
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ហៅមុខងារ

ដើម្បីហៅមុខងារ អ្នកត្រូវធានាថា បានបញ្ជាក់អាគុយម៉ង់ត្រឹមត្រូវ ហើយនៅខ្លះករណីមានត្រូវនិយាយឈ្មោះម៉ុខងារដែលត្រូវហៅ។

#### TypeScript

```typescript

// អានធនធានមួយ
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

// ហៅបញ្ហាសំណួរ
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

នៅក្នុងកូដខាងលើ យើងបាន:

- អានធនធាន មកហៅធនធានដោយហៅ `readResource()` បញ្ជាក់ `uri`។ នេះហាក់ដូចជា​នៅផ្នែកម៉ាស៊ីនមើល៖

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

    តម្លៃ `uri` របស់យើង `file://example.txt` ត្រូវគ្នាជាមួយ `file://{name}` នៅលើម៉ាស៊ីនមើល។ `example.txt` នឹងត្រូវផែនទីទៅ `name`។

- ហៅឧបករណ៍ យើងហៅវាដោយបញ្ជាក់ `name` និង `arguments` ដូចខាងក្រោម៖

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- ទទួលបម្ដៅ ដើម្បីទទួលបម្ដៅ អ្នកហៅ `getPrompt()` ជាមួយ `name` និង `arguments`។ កូដម៉ាស៊ីនមើលដូចខាងក្រោម៖

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

    ហើយក្នុងកូដអតិថិជន ផលប៉ះពាល់ដូចខាងក្រោមដើម្បីឆ្លៀងទៅនឹងអ្វីដែលបានប្រកាសនៅលើម៉ាស៊ីនមើល។

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

នៅក្នុងកូដខាងលើ យើងបាន:

- ហៅធនធានឈ្មោះ `greeting` ប្រើ `read_resource`.
- ហៅឧបករណ៍ឈ្មោះ `add` ប្រើ `call_tool`.

#### .NET

1. តោះបន្ថែមកូដសម្រាប់ហៅឧបករណ៍៖

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ដើម្បីបោះពុម្ពលទ្ធផល បន្ទាប់មានកូដដើម្បីដោះស្រាយវា៖

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// ហៅឧបករណ៍គណនាផ្សេងទៀត
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

នៅក្នុងកូដខាងលើ យើងបាន:

- ហៅឧបករណ៍គណនាផ្សេងៗប្រើវិធីសាស្រ្ត `callTool()` ជាមួយវត្ថុ `CallToolRequest`។
- ឧបករណ៍មួយៗហៅបញ្ជាក់ឈ្មោះឧបករណ៍ និង `Map` នៃអាគុយម៉ង់ដែលត្រូវបានទាមទារ។
- ឧបករណ៍ម៉ាស៊ីនមើលរំពឹងថាមានឈ្មោះប៉ារ៉ាម៉ែត្រជាក់លាក់ (ដូចជា "a", "b" សម្រាប់ប្រតិបត្តិការជាគណិតវិទ្យា)។
- លទ្ធផលត្រឡប់មកជាជាតិកម្មវិធី `CallToolResult` ដែលមានតបស្នងពីម៉ាស៊ីនមើល។

#### Rust

```rust
// ហៅឧបករណ៍បូកជាមួយអាគុយម៉ង់ទាំងនេះ = {"a": 3, "b": 2}
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

### -5- រំពឹងអតិថិជន

ដើម្បីរត់អតិថិជន សរសេរបញ្ជាខាងក្រោមនៅក្នុង Terminal៖

#### TypeScript

បន្ថែមការចូលបន្ទាត់ខាងក្រោមទៅផ្នែក "scripts" នៅក្នុង *package.json*៖

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

ហៅអតិថិជនជាមួយបញ្ជាខាងក្រោម៖

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

ជាទីមួយ សូមធានាថាម៉ាស៊ីនមើល MCP របស់អ្នកកំពុងដំណើរការ នៅ `http://localhost:8080`។ បន្ទាប់មករត់អតិថិជន៖

```bash
# សាងសង់គម្រោងរបស់អ្នក
./mvnw clean compile

# រត់កម្មវិធីអតិថិជន
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

ជំហានមួយផ្សេងទៀត អ្នកអាចរត់គម្រោងអតិថិជនពេញលេញដែលបានផ្ដល់នៅក្នុងថតដោះសោ `03-GettingStarted\02-client\solution\java`៖

```bash
# នាវិកទៅកាន់ថតដំណោះស្រាយ
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

## កិច្ចការជម្រាប

ក្នុងកិច្ចការនេះ អ្នកនឹងប្រើអ្វីដែលបានរៀនក្នុងការបង្កើតអតិថិជន ប៉ុន្តែបង្កើតអតិថិជនរបស់អ្នកផ្ទាល់។

នេះជាម៉ាស៊ីនមើលដែលអ្នកអាចប្រើបានជាមួយកូដអតិថិជនរបស់អ្នក មើលថាអ្នកអាចបន្ថែមមុខងារបន្ថែមទៅម៉ាស៊ីនមើលដើម្បីធ្វើឲ្យវាគួរឱកាសបំផុត។

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// បង្កើតម៉ាស៊ីនមេ MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// បន្ថែមឧបករណ៍បូក
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// បន្ថែមធនធានស្វាគមន៍មានលក្ខណៈអូតូ
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

# បង្កើតម៉ាស៊ីនមេ MCP
mcp = FastMCP("Demo")


# បន្ថែមឧបករណ៍បូក
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# បន្ថែមធនធានអារម្មណ៍ស្វាគមន៍ឌីណាមិច
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

មើលគម្រោងនេះដើម្បីមើលរបៀប [បន្ថែមបម្ដៅ និងធនធាន](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)។

ក្រៅពីនេះ សូមពិនិត្យតំណនេះសម្រាប់របៀបហៅ [បម្ដៅ និងធនធាន](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)។

### Rust

នៅក្នុង [ផ្នែកពីមុន](../../../../03-GettingStarted/01-first-server) អ្នកបានរៀនពីរបៀបបង្កើតម៉ាស៊ីនមើល MCP មួយសាមញ្ញជាមួយ Rust។ អ្នកអាចបន្តបង្កើតលើវា ឬមើលតំណនេះសម្រាប់ឧទាហរណ៍ម៉ាស៊ីនមើល MCP ជាមួយ Rust បន្ថែម៖ [ឧទាហរណ៍ម៉ាស៊ីនមើល MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## ដំណោះស្រាយ

ថត **ដំណោះស្រាយ** មានការអនុវត្តអតិថិជនដែលពេញលេញ និងអាចដំណើរការបានដែលបង្ហាញគ្រប់គំនិតដែលបានពិភាក្សានៅក្នុងមេរៀននេះ។ ដំណោះស្រាយនីមួយៗរួមមានកូដទាំងអតិថិជន និងម៉ាស៊ីនមើលដែលបានរៀបចំបំបែកជាគម្រោងឯករាជ្យ។

### 📁 រចនាសម្ព័ន្ធដំណោះស្រាយ

ថតដំណោះស្រាយត្រូវបានរៀបចំតាមភាសាកម្មវិធី៖

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

### 🚀 អ្វីដែលក្នុងការដំណោះស្រាយនីមួយៗ

ការដំណោះស្រាយជាភាសាមួយៗផ្ដល់ជូន៖

- ** ការអនុវត្តអតិថិជន​ពេញលេញ ** ជាមួយគ្រប់មុខងារពីមេរៀន
- ** រចនាសម្ព័ន្ធគម្រោងដំណើរការ ** មានការពឹងផ្អែកនិងការកំណត់ត្រឹមត្រូវ
- ** ស្គ្រីបសាងសង់ និងបើកបរពេញលេញ ** សម្រាប់ការរៀបចំ និងប្រតិបត្តិការងារងាយស្រួល
- ** README ថ្លវិលលម្អិត ** ជាមួយសេចក្ដីណែនាំនិមួយៗ
- ** ការដោះស្រាយកំហុស ** និងឧទាហរណ៍ដំណើរការវិលតប

### 📖 ការប្រើប្រាស់ដំណោះស្រាយ

1. ** សូមចូលទៅក្នុងថតភាសាដែលអ្នកចូលចិត្ត៖**

   ```bash
   cd solution/typescript/    # សម្រាប់ TypeScript
   cd solution/java/          # សម្រាប់ Java
   cd solution/python/        # សម្រាប់ Python
   cd solution/dotnet/        # សម្រាប់ .NET
   ```

2. ** អនុវត្តតាមការណែនាំ README ក្នុងថតនីមួយៗ សម្រាប់៖**
   - ការដំឡើងការពឹងផ្អែក
   - ការសាងសង់គម្រោង
   - ការរត់អតិថិជន

3. ** លទ្ធផលឧទាហរណ៍ ដែលអ្នកគួរមើលឃើញ៖**

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

សម្រាប់ឯកសារពេញលេញ និងសេចក្តីណែនាំជម្រេីស​សូមមើលៈ **[📖 ឯកសារដំណោះស្រាយ](./solution/README.md)**

## 🎯 ឧទាហរណ៍ពេញលេញ

យើងបានផ្ដល់អនុវត្តអតិថិជនពេញលេញ ដែលដំណើរការបានសម្រាប់ភាសាកម្មវិធីទាំងអស់ដែលបង្រៀនក្នុងមេរៀននេះ។ ឧទាហរណ៍ទាំងនេះបង្ហាញមុខងារពេញលេញដែលបានពិពណ៌នាខាងលើ ហើយអាចប្រើជាការយោង ឬចំណុចចាប់ផ្តើមសម្រាប់គម្រោងរបស់អ្នក។

### ឧទាហរណ៍ពេញលេញដែលអាចប្រើបាន

| ភាសា | ឯកសារ | ការពិពណ៌នា |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | អតិថិជន Java ពេញលេញ ប្រើផ្ទេរ SSE ជាមួយការដោះស្រាយកំហុសលម្អិត |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | អតិថិជន C# ពេញលេញ ប្រើផ្ទេរ stdio ជាមួយការចាប់ផ្តើមម៉ាស៊ីនមើលដោយស្វ័យប្រវត្តិ |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | អតិថិជន TypeScript ពេញលេញ ជាមួយការគាំទ្រ MCP protocol ពេញលេញ |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | អតិថិជន Python ពេញលេញ ប្រើរបៀប async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | អតិថិជន Rust ពេញលេញ ប្រើ Tokio សម្រាប់ប្រតិបត្តិការពហុទំនាក់ទំនង |

អ្នកប្រាកដថាឧទាហរណ៍ពេញលេញណាមួយរួមមាន៖

- ✅ ** ការបង្កើតការភ្ជាប់ ** និងដោះស្រាយកំហុស
- ✅ ** ការរកឃើញម៉ាស៊ីនមើល ** (ឧបករណ៍, ធនធាន, បម្ដៅ នៅកន្លែងអាចប្រើ)
- ✅ ** ប្រតិបត្តិការគណនា ** (បូក, ខ្វះ, គុណ, ចែក, ជំនួយ)
- ✅ ** ការដោះស្រាយលទ្ធផល និងបោះពុម្ពឲ្យមានទ្រង់ទ្រាយល្អ**
- ✅ ** ការដោះស្រាយកំហុសលម្អិត **

- ✅ **កូដស្អាត និងមានឯកសារ** ជាមួយនឹងការពណ៌នាជំហានបន្តបន្ទាប់

### ការចាប់ផ្តើមជាមួយឧទាហរណ៍ពេញលេញ

1. **ជ្រើសរើសភាសាដែលអ្នកចូលចិត្ត** ពីតារាងខាងលើ
2. **ពិនិត្យឯកសារឧទាហរណ៍ពេញលេញ** ដើម្បីយល់ពីការអនុវត្តពេញលេញ
3. **រត់ឧទាហរណ៍** ដោយតាមការណែនាំនៅក្នុង [`complete_examples.md`](./complete_examples.md)
4. **កែប្រែលនិងពង្រីក** ឧទាហរណ៍សម្រាប់ករណីប្រើប្រាស់របស់អ្នក

សម្រាប់ឯកសារពិស្តារពីការរត់និងប្តូរតាមបំណងឧទាហរណ៍ទាំងនេះ, មើលៈ **[📖 ឯកសារឧទាហរណ៍ពេញលេញ](./complete_examples.md)**

### 💡 ដំណោះស្រាយ និងឧទាហរណ៍ពេញលេញ

| **ថតដំណោះស្រាយ** | **ឧទាហរណ៍ពេញលេញ** |
|--------------------|--------------------- |
| រចនាសម្ព័ន្ធគម្រោងពេញលេញជាមួយឯកសារការសាងសង់ | ការអនុវត្តជា​ឯកសារតែមួយ |
| ផ្ទៀងផ្ទាត់រួចជាមួយការពឹងផ្អែក | ឧទាហរណ៍កូដផ្តោតលើយ៉ាងត្រឹមត្រូវ |
| ការតំរៀបដូចផលិតកម្ម | ឯកសារយោងសម្រាប់ការអប់រំ |
| ឧបករណ៍ជាក់លាក់សម្រាប់ភាសា | ការប្រៀបធៀបឆ្លងភាសា |

ទាំងពីរយុទ្ធសាស្ត្រមានតម្លៃ - ប្រើ **ថតដំណោះស្រាយ** សម្រាប់គម្រោងពេញលេញ និង **ឧទាហរណ៍ពេញលេញ** សម្រាប់ការបង្រៀននិងយោង។

## ចំណុចសំខាន់

ចំណុចសំខាន់សម្រាប់ជំពូកនេះគឺអំពីអតិថិជន៖

- អាចប្រើសម្រាប់រកឃើញនិងហៅមុខងារនៅលើម៉ាស៊ីនបម្រើទាំងពីរ។
- អាចចាប់ផ្តើមម៉ាស៊ីនបម្រើខ្លួនវាផ្ទាល់ (ដូចនៅក្នុងជំពូកនេះ) ប៉ុន្តែអតិថិជនអាចភ្ជាប់ទៅម៉ាស៊ីនបម្រើដែលកំពុងដំណើរការបានផងដែរ។
- ជាវិធីល្អសម្រាប់សាកល្បងសមត្ថភាពម៉ាស៊ីនបម្រើ យ៉ាងជាប់ជួយជបអោលជាមួយជម្រើសផ្សេងៗដូចជា Inspector ដូចដែលបានពិពណ៌នានៅជំពូកមុន។

## ធនធានបន្ថែម

- [ការបង្កើតអតិថិជនក្នុង MCP](https://modelcontextprotocol.io/quickstart/client)

## គំរូ

- [កម្មវិធីគណនា Java](../samples/java/calculator/README.md)
- [កម្មវិធីគណនា .NET](../../../../03-GettingStarted/samples/csharp)
- [កម្មវិធីគណនា JavaScript](../samples/javascript/README.md)
- [កម្មវិធីគណនា TypeScript](../samples/typescript/README.md)
- [កម្មវិធីគណនា Python](../../../../03-GettingStarted/samples/python)
- [កម្មវិធីគណនា Rust](../../../../03-GettingStarted/samples/rust)

## ចុងក្រោយ

- បន្ទាប់: [បង្កើតអតិថិជនជាមួយ LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->