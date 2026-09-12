# একটি ক্লায়েন্ট তৈরি করা

ক্লায়েন্ট হলো কাস্টম অ্যাপ্লিকেশন বা স্ক্রিপ্ট যা সরাসরি একটি MCP সার্ভারের সাথে যোগাযোগ করে রিসোর্স, টুল এবং প্রম্পট অনুরোধ করে। সার্ভারের সাথে যোগাযোগের জন্য গ্রাফিক্যাল ইন্টারফেস প্রদানকারী ইনস্পেক্টর টুল ব্যবহারের পরিবর্তে, নিজস্ব ক্লায়েন্ট লেখা প্রোগ্রাম্যাটিক এবং স্বয়ংক্রিয় ইন্টারঅ্যাকশন সক্ষম করে। এটি ডেভেলপারদের MCP সক্ষমতাগুলি তাদের নিজস্ব ওয়ার্কফ্লোতে সংহত করতে, কাজ গুলো স্বয়ংক্রিয় করতে এবং নির্দিষ্ট চাহিদা অনুযায়ী বিশেষ সমাধান তৈরি করতে সাহায্য করে।

## ওভারভিউ

এই পাঠে MCP ইকোসিস্টেমের মধ্যে ক্লায়েন্ট ধারণাটি পরিচয় করানো হবে। আপনি শিখবেন কিভাবে নিজস্ব ক্লায়েন্ট লিখবেন এবং সেটি MCP সার্ভারের সাথে সংযোগ করবেন।

## শেখার উদ্দেশ্য

এই পাঠের শেষে, আপনি সক্ষম হবেন:

- একটি ক্লায়েন্ট কি করতে পারে তা বুঝতে পারা।
- নিজস্ব ক্লায়েন্ট লেখা।
- একটি MCP সার্ভারের সাথে ক্লায়েন্ট সংযোগ করা এবং পরীক্ষা করে নিশ্চিত হওয়া যে এটি প্রত্যাশিতভাবে কাজ করে।

## একটি ক্লায়েন্ট লেখার জন্য কি লাগে?

একটি ক্লায়েন্ট লেখার জন্য আপনাকে নিচের কাজগুলো করতে হবে:

- **সঠিক লাইব্রেরি ইমপোর্ট করা**। আপনি আগের মত একই লাইব্রেরি ব্যবহার করবেন, তবে আলাদা নির্মাণ উপকরণ।
- **একটি ক্লায়েন্ট ইনস্ট্যান্টিয়েট করা**। এর জন্য ক্লায়েন্টের একটি ইনস্ট্যান্স তৈরি করতে হবে এবং এটি নির্বাচিত ট্রান্সপোর্ট পদ্ধতির সাথে সংযোগ করতে হবে।
- **কোন রিসোর্স তালিকাভুক্ত করবেন তা সিদ্ধান্ত নেওয়া**। আপনার MCP সার্ভারে রয়েছে রিসোর্স, টুল এবং প্রম্পট, আপনাকে নির্ধারণ করতে হবে কোনগুলো তালিকা করবেন।
- **ক্লায়েন্টকে হোস্ট অ্যাপ্লিকেশনে একত্রিত করা**। সার্ভারের সক্ষমতা জানার পর, আপনাকে এটি হোস্ট অ্যাপ্লিকেশনের সঙ্গে সংযুক্ত করতে হবে যাতে কোনও ব্যবহারকারী প্রম্পট বা অন্য কোন কমান্ড টাইপ করলে সম্পর্কিত সার্ভার ফিচারটি চালু হয়।

এখন আমরা উচ্চস্তরে বুঝে গিয়েছি কি করতে হবে, আসুন পরবর্তী ধাপে একটি উদাহরণ দেখি।

### একটি উদাহরণ ক্লায়েন্ট

এই উদাহরণ ক্লায়েন্টটি দেখি:

### টাইপস্ক্রিপ্ট

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

// প্রম্পটের তালিকা
const prompts = await client.listPrompts();

// একটি প্রম্পট পান
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// সম্পদের তালিকা
const resources = await client.listResources();

// একটি সম্পদ পড়ুন
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// একটি টুল কল করুন
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

উপরের কোডে আমরা:

- লাইব্রেরি ইমপোর্ট করেছি
- একটি ক্লায়েন্ট ইনস্ট্যান্ট তৈরি করেছি এবং stdio ট্রান্সপোর্ট ব্যবহার করে সংযোগ করেছি।
- প্রম্পট, রিসোর্স এবং টুল তালিকা করেছি এবং সেগুলোকে সক্রিয় করেছি।

এটাই হলো, একটি ক্লায়েন্ট যা MCP সার্ভারের সাথে কথা বলতে পারে।

আগামী অনুশীলন অংশে আমরা ধীরে ধীরে প্রতিটি কোড স্নিপেট ব্যাখ্যা করব।

## অনুশীলন: একটি ক্লায়েন্ট লেখা

উপরে বলেছি, এবার ধীরে ধীরে কোড ব্যাখ্যা করি, এবং ইচ্ছে করলে সাথে সাথে কোডও করতে পারেন।

### -1- লাইব্রেরি ইমপোর্ট করা

আমরা দরকারি লাইব্রেরি ইমপোর্ট করব, আমাদের ক্লায়েন্ট এবং stdio ট্রান্সপোর্ট প্রোটোকলের রেফারেন্স লাগবে। stdio হলো এমন একটি প্রোটোকল যা স্থানীয় মেশিনে রান করার জন্য তৈরি। SSE আরেকটি ট্রান্সপোর্ট প্রোটোকল আমরা ভবিষ্যতের অধ্যায়ে দেখাবো, কিন্তু এখন stdio নিয়ে এগিয়ে যাই।

#### টাইপস্ক্রিপ্ট

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### পাইথন

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

#### জাভা

জাভার জন্য, আপনি একটি ক্লায়েন্ট তৈরি করবেন যা আগের অনুশীলনের MCP সার্ভারের সাথে সংযোগ করবে। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) থেকে একই জাভা স্প্রিং বুট প্রকল্প কাঠামো ব্যবহার করুন, এবং `src/main/java/com/microsoft/mcp/sample/client/` ফোল্ডারে একটি নতুন জাভা ক্লাস `SDKClient` তৈরি করে নিচের ইমপোর্টগুলি যোগ করুন:

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

#### রাষ্ট

আপনাকে `Cargo.toml` ফাইলে নিচের ডিপেন্ডেন্সিগুলো যোগ করতে হবে।

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

এরপর আপনি ক্লায়েন্ট কোডে প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করতে পারবেন।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

চলুন এখন ইনস্ট্যান্টিয়েশন করি।

### -2- ক্লায়েন্ট ও ট্রান্সপোর্ট ইনস্ট্যান্টিয়েট করা

আমাদের ট্রান্সপোর্ট এবং ক্লায়েন্টের ইনস্ট্যান্স তৈরি করতে হবে:

#### টাইপস্ক্রিপ্ট

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

উপরের কোডে আমরা:

- একটি stdio ট্রান্সপোর্ট ইনস্ট্যান্স তৈরি করেছি। লক্ষ্য করুন এটি কমান্ড এবং আর্গুমেন্ট নির্দিষ্ট করে, যা সার্ভার খুঁজে পাওয়া এবং শুরু করার জন্য দরকার, কারণ ক্লায়েন্ট তৈরির সময় এ কাজগুলো করতে হবে।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- একটি ক্লায়েন্ট ইনস্ট্যান্টিয়েট করেছি নাম এবং সংস্করণ দিয়ে।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ক্লায়েন্টকে নির্বাচিত ট্রান্সপোর্টের সাথে সংযুক্ত করেছি।

    ```typescript
    await client.connect(transport);
    ```

#### পাইথন

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # এক্সিকিউটেবল
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন প্যারামিটার
    env=None,  # ঐচ্ছিক পরিবেশ 변수
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # সংযোগ শুরু করুন
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

উপরের কোডে আমরা:

- প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি
- একটি সার্ভার প্যারামিটার অবজেক্ট তৈরি করেছি যা দিয়ে সার্ভার শুরু করব যাতে ক্লায়েন্ট সংযোগ করে।
- একটি `run` মেথড সংজ্ঞায়িত করেছি যা `stdio_client` কল করে ক্লায়েন্ট সেশন শুরু করে।
- একটি এন্ট্রি পয়েন্ট তৈরি করেছি যেখানে `run` মেথড `asyncio.run`-এ প্রদান করা হয়েছে।

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

উপরের কোডে আমরা:

- প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করেছি।
- একটি stdio ট্রান্সপোর্ট এবং `mcpClient` নামে একটি ক্লায়েন্ট তৈরি করেছি। এটি MCP সার্ভারে টুল তালিকা এবং কল করার জন্য ব্যবহার করব।

লক্ষ্য করুন, "Arguments" এ আপনি বা তো *.csproj* ফাইল নির্দেশ করতে পারেন বা executable নির্দেশ করতে পারেন।

#### জাভা

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
        
        // আপনার ক্লায়েন্ট লজিক এখানে যাবে
    }
}
```

উপরের কোডে আমরা:

- একটি মেইন মেথড তৈরি করেছি যা একটি SSE ট্রান্সপোর্ট সেটআপ করে, যেটি `http://localhost:8080` পয়েন্ট করে যেখানে আমাদের MCP সার্ভার চলবে।
- একটি ক্লায়েন্ট ক্লাস তৈরি করেছি যা কনস্ট্রাক্টরে ট্রান্সপোর্ট নেয়।
- `run` মেথডে, আমরা ট্রান্সপোর্ট ব্যবহার করে একটি synchronous MCP ক্লায়েন্ট তৈরি করেছি এবং সংযোগ শুরু করেছি।
- SSE (Server-Sent Events) ট্রান্সপোর্ট ব্যবহার করেছি যা HTTP-ভিত্তিক যোগাযোগের জন্য উপযুক্ত জাভা স্প্রিং বুট MCP সার্ভারের সাথে।

#### রাষ্ট

লক্ষ্য করুন, এই রাষ্ট ক্লায়েন্ট ধরে নিচ্ছে সার্ভার একই ডিরেক্টরিতে একটি সাইব্লিং প্রকল্প "calculator-server" নামে। নিচের কোড সার্ভার শুরু করে এবং সংযোগ করে।

```rust
async fn main() -> Result<(), RmcpError> {
    // ধরে নিই সার্ভারটি একই ডিরেক্টরিতে "calculator-server" নামক একটি সহোদর প্রকল্প
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

    // TODO: প্রাথমিককরণ

    // TODO: সরঞ্জামগুলি তালিকাভুক্ত করুন

    // TODO: যুক্ত করার সরঞ্জামটি কল করুন পাশের মানগুলি সহ = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- সার্ভার ফিচার তালিকা করা

এখন আমাদের কাছে এমন একটি ক্লায়েন্ট আছে যা সংযোগ করতে পারে যখন প্রোগ্রাম চালু হবে। তবে এটি আসলে ফিচারগুলো তালিকা করে না, চলুন এখন তাই করি:

#### টাইপস্ক্রিপ্ট

```typescript
// তালিকা প্রম্পট
const prompts = await client.listPrompts();

// তালিকা সম্পদ
const resources = await client.listResources();

// তালিকা সরঞ্জামসমূহ
const tools = await client.listTools();
```

#### পাইথন

```python
# উপলব্ধ সম্পদগুলি তালিকাভুক্ত করুন
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# উপলব্ধ সরঞ্জামগুলি তালিকাভুক্ত করুন
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

এখানে আমরা উপলভ্য রিসোর্স `list_resources()` এবং টুল `list_tools()` তালিকা করে প্রিন্ট করেছি।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

উপরে একটি উদাহরণ দেওয়া হয়েছে কিভাবে সার্ভারের টুলগুলো তালিকা করা যায়। প্রতিটি টুলের নাম আমরা প্রিন্টও করেছি।

#### জাভা

```java
// সরঞ্জাম তালিকা এবং প্রদর্শন করুন
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// সংযোগ যাচাই করার জন্য আপনি সার্ভার পিংও করতে পারেন
client.ping();
```

উপরের কোডে আমরা:

- `listTools()` কল করেছি MCP সার্ভার থেকে সব উপলভ্য টুল পেতে।
- সার্ভারের সাথে সংযোগ সঠিক আছে কি না যাচাই করার জন্য `ping()` ব্যবহার করেছি।
- `ListToolsResult` এ সব টুলের নাম, বর্ণনা, ও ইনপুট স্কিমা সংরক্ষিত থাকে।

দারুন, এখন সব ফিচার ধরে নিয়েছি। এখন প্রশ্ন, কখন ব্যবহার করব? এই ক্লায়েন্টটি তুলনামূলক সরল, এর অর্থ হল কখন দরকার তখন স্পষ্টভাবে ফিচারগুলো কল করতে হবে। পরবর্তী অধ্যায়ে আমরা আরও উন্নত ক্লায়েন্ট তৈরি করব যার নিজস্ব বড় ভাষার মডেল (LLM) থাকবে। আপাতত চলুন দেখি কিভাবে সার্ভারের ফিচারগুলিকে কল করতে পারি:

#### রাষ্ট

প্রধান ফাংশনে ক্লায়েন্ট ইনিশিয়ালাইজ করার পর, আমরা সার্ভার ইনিশিয়ালাইজ করে কিছু ফিচার তালিকা করতে পারি।

```rust
// আরম্ভ করুন
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// তালিকা সরঞ্জামসমূহ
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ফিচার কল করা

ফিচার কল করার সময় সঠিক আর্গুমেন্ট এবং কখনও কখনও ফিচারের নাম সঠিকভাবে দিতে হবে।

#### টাইপস্ক্রিপ্ট

```typescript

// একটি রিসোর্স পড়ুন
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// একটি টুল কল করুন
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// প্রম্পট কল করুন
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

উপরের কোডে আমরা:

- একটি রিসোর্স পড়েছি, `readResource()` কল করে `uri` নির্দিষ্ট করেছি। সার্ভার সাইডের কোড এরকম হতে পারে:

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

    আমাদের `uri` মান `file://example.txt` সার্ভারের `file://{name}` এর সাথে মেলে। এখানে `example.txt` মানে `name`।

- একটি টুল কল করেছি, টুলের `name` ও `arguments` নির্দিষ্ট করে:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- একটি প্রম্পট পেতে `getPrompt()` কল করেছি `name` ও `arguments` সহ। সার্ভারের কোড এরকম:

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

    ফলে আপনার ক্লায়েন্ট কোড সার্ভারের ডিক্লেয়ারেশনের সাথে মিলবে:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### পাইথন

```python
# একটি উৎস পড়ুন
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# একটি টুল কল করুন
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

উপরের কোডে আমরা:

- `read_resource` ব্যবহার করে `greeting` রিসোর্স কল করেছি।
- `call_tool` ব্যবহার করে `add` টুল কল করেছি।

#### .NET

1. একটি টুল কল করার কোড যোগ করি:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. ফলাফল প্রিন্ট করার জন্য কোড:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### জাভা

```java
// বিভিন্ন ক্যালকুলেটর সরঞ্জাম কল করুন
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

উপরের কোডে আমরা:

- একাধিক ক্যালকুলেটর টুল `callTool()` মেথড এবং `CallToolRequest` অবজেক্ট দিয়ে কল করেছি।
- প্রতিটি টুল কল টুলের নাম এবং `Map` আর্গুমেন্ট ব্যবহার করে কল করা হয়েছে।
- সার্ভার টুলগুলো নির্দিষ্ট প্যারামিটার নাম আশা করে (যেমন "a", "b" গণিত অপারেশনের জন্য)।
- সার্ভার থেকে পাওয়া ফলাফল `CallToolResult` অবজেক্টে থাকে।

#### রাষ্ট

```rust
// আর্গুমেন্ট সহ add টুল কল করুন = {"a": 3, "b": 2}
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

### -5- ক্লায়েন্ট চালানো

ক্লায়েন্ট চালানোর জন্য টার্মিনালে নিচের কমান্ড দিন:

#### টাইপস্ক্রিপ্ট

*package.json* এর "scripts" অংশে নিম্নলিখিত এন্ট্রি যোগ করুন:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### পাইথন

নিচের কমান্ড দিয়ে ক্লায়েন্ট কল করুন:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### জাভা

প্রথমে নিশ্চিত করুন MCP সার্ভার `http://localhost:8080` এ চলছে। তারপর ক্লায়েন্ট চালান:

```bash
# আপনার প্রকল্প তৈরি করুন
./mvnw clean compile

# ক্লায়েন্ট চালান
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

অথবা, আপনি সমাধান ফোল্ডার `03-GettingStarted\02-client\solution\java` তে পুরো ক্লায়েন্ট প্রকল্প রান করতে পারেন:

```bash
# সলিউশন ডিরেক্টরিতে যান
cd 03-GettingStarted/02-client/solution/java

# JAR তৈরি করুন এবং চালান
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### রাষ্ট

```bash
cargo fmt
cargo run
```

## নিয়োগ

এই নিয়োগে, আপনি যা শিখেছেন তা ব্যবহার করে নিজস্ব একটি ক্লায়েন্ট তৈরি করবেন।

নিচে একটি সার্ভার দেওয়া হয়েছে যা আপনাকে আপনার ক্লায়েন্ট কোড থেকে কল করতে হবে, দেখুন আপনি সার্ভারে আরো ফিচার যোগ করতে পারেন কি না যাতে এটি আরও আকর্ষণীয় হয়।

### টাইপস্ক্রিপ্ট

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// একটি MCP সার্ভার তৈরি করুন
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// একটি যোগ করার টুল যোগ করুন
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// একটি গতিশীল স্বাগত সম্পদ যোগ করুন
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

// stdin থেকে বার্তা গ্রহণ শুরু করুন এবং stdout এ বার্তা পাঠান

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

### পাইথন

```python
# server.py
from mcp.server.fastmcp import FastMCP

# একটি MCP সার্ভার তৈরি করুন
mcp = FastMCP("Demo")


# একটি যোগ করার সরঞ্জাম যোগ করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি গতিশীল স্বাগতম সম্পদ যোগ করুন
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

এই প্রকল্পটি দেখুন কিভাবে [প্রম্পট ও রিসোর্স যোগ করবেন](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

এছাড়াও এই লিংক দেখুন কিভাবে কল করবেন [প্রম্পট ও রিসোর্স](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)।

### রাষ্ট

[আগের অংশে](../../../../03-GettingStarted/01-first-server) আপনি রাষ্ট দিয়ে একটি সরল MCP সার্ভার তৈরি শিখেছেন। আপনি সেটি অব্যাহত রাখতে পারেন অথবা অধিক রাষ্ট ভিত্তিক MCP সার্ভার উদাহরণ দেখতে পারেন এই লিংকে: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## সমাধান

**সমাধান ফোল্ডারে** সম্পূর্ণ, রান করার জন্য প্রস্তুত ক্লায়েন্ট ইমপ্লিমেন্টেশন রয়েছে যা এই টিউটোরিয়ালে কভার করা সব ধারণা প্রদর্শন করে। প্রতিটি সমাধান পৃথক, স্বতন্ত্র প্রকল্প আকারে ক্লায়েন্ট ও সার্ভার কোড অন্তর্ভুক্ত করে।

### 📁 সমাধানের কাঠামো

সমাধান ডিরেক্টরিটি প্রোগ্রামিং ভাষা ভিত্তিকভাবে সাজানো:

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

### 🚀 প্রত্যেক সমাধানে যা থাকে

প্রতিটি ভাষা-নির্দিষ্ট সমাধান অন্তর্ভুক্ত করে:

- **সম্পূর্ণ ক্লায়েন্ট ইমপ্লিমেন্টেশন** টিউটোরিয়ালের সব ফিচারসহ
- **কাজের মতো প্রকল্প কাঠামো** যথাযথ ডিপেন্ডেন্সি ও কনফিগারেশন সহ
- **বিল্ড ও রান স্ক্রিপ্ট** সহজ সজ্জা ও কার্যকর জন্য
- **বিস্তারিত README** ভাষা-নির্দিষ্ট নির্দেশনা সহ
- **এরর হ্যান্ডলিং** ও ফলাফল প্রসেসিং উদাহরণ

### 📖 সমাধান ব্যবহার

1. **আপনার পছন্দের ভাষার ফোল্ডারে প্রবেশ করুন**:

   ```bash
   cd solution/typescript/    # টাইপস্ক্রিপ্টের জন্য
   cd solution/java/          # জাভার জন্য
   cd solution/python/        # পাইথনের জন্য
   cd solution/dotnet/        # .NET এর জন্য
   ```

2. **প্রতিটি ফোল্ডারে README নির্দেশনা অনুসরণ করুন**:
   - ডিপেন্ডেন্সি ইনস্টলেশন
   - প্রকল্প বিল্ড
   - ক্লায়েন্ট চালানো

3. **উদাহরণ আউটপুট যা দেখতে পাবেন**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

সম্পূর্ণ ডকুমেন্টেশন ও ধাপে ধাপে নির্দেশনার জন্য দেখুন: **[📖 সমাধান ডকুমেন্টেশন](./solution/README.md)**

## 🎯 সম্পূর্ণ উদাহরণ

আমরা টিউটোরিয়ালে কভার করা সব প্রোগ্রামিং ভাষার জন্য সম্পূর্ণ, কাজ করা ক্লায়েন্ট ইমপ্লিমেন্টেশন প্রদান করেছি। এই উদাহরণগুলো উপরের সমস্ত কার্যকারিতা প্রদর্শন করে এবং রেফারেন্স বা শুরু করার পয়েন্ট হিসেবে ব্যবহার করা যাবে।

### উপলভ্য সম্পূর্ণ উদাহরণ

| ভাষা | ফাইল | বিবরণ |
|----------|------|-------------|
| **জাভা** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ট্রান্সপোর্ট সহ সম্পূর্ণ জাভা ক্লায়েন্ট যা বিস্তারিত এরর হ্যান্ডলিং করে |
| **সি#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ট্রান্সপোর্ট ব্যবহার করে স্বয়ংক্রিয় সার্ভার স্টার্টআপ সহ সম্পূর্ণ C# ক্লায়েন্ট |
| **টাইপস্ক্রিপ্ট** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP প্রোটোকলের পূর্ণ সমর্থনসহ সম্পূর্ণ টাইপস্ক্রিপ্ট ক্লায়েন্ট |
| **পাইথন** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await প্যাটার্ন ব্যবহার করে সম্পূর্ণ পাইথন ক্লায়েন্ট |
| **রাষ্ট** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio দিয়ে অ্যাসিঙ্ক অপারেশন সহ সম্পূর্ণ রাষ্ট ক্লায়েন্ট |

প্রতিটি সম্পূর্ণ উদাহরণে অন্তর্ভুক্ত:

- ✅ **সংযোগ স্থাপন ও এরর হ্যান্ডলিং**
- ✅ **সার্ভার আবিষ্কার (যেমন টুল, রিসোর্স, প্রম্পট যেগুলো প্রযোজ্য)**
- ✅ **ক্যালকুলেটর অপারেশন (যোগ, বিয়োগ, গুণ, ভাগ, সাহায্য)**
- ✅ **ফলাফল প্রসেসিং ও সজ্জিত আউটপুট**
- ✅ **বিস্তারিত এরর হ্যান্ডলিং**

- ✅ **পরিষ্কার, দস্তাবেজভুক্ত কোড** স্টেপ-বাই-স্টেপ মন্তব্য সহ

### সম্পূর্ণ উদাহরণগুলির সাথে শুরু করা

1. উপরের টেবিল থেকে **আপনার প্রিয় ভাষা নির্বাচন করুন**
2. সম্পূর্ণ বাস্তবায়ন বুঝতে **সম্পূর্ণ উদাহরণ ফাইলটি পর্যালোচনা করুন**
3. [`complete_examples.md`](./complete_examples.md) ফাইলে নির্দেশিকা অনুসরণ করে **উদাহরণ রান করুন**
4. আপনার নির্দিষ্ট ব্যবহার মামলার জন্য উদাহরণটি **পরিবর্তন করুন এবং বাড়ান**

এই উদাহরণগুলি চালানো এবং কাস্টমাইজ করার বিস্তারিত ডকুমেন্টেশনের জন্য দেখুন: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 সমাধান বনাম সম্পূর্ণ উদাহরণসমূহ

| **সমাধান ফোল্ডার** | **সম্পূর্ণ উদাহরণসমূহ** |
|--------------------|--------------------- |
| বিল্ড ফাইলসহ পুরো প্রকল্প কাঠামো | একক-ফাইল বাস্তবায়ন |
| নির্ভরশীলতার সাথে প্রস্তুত-রান | নির্দিষ্ট কোড উদাহরণ |
| প্রোডাকশন-সদৃশ সেটআপ | শিক্ষামূলক রেফারেন্স |
| ভাষা-নির্দিষ্ট সরঞ্জাম | ক্রস-ল্যাঙ্গুয়েজ তুলনা |

উভয় পদ্ধতি মূল্যবান - পুরো প্রকল্পের জন্য **সমাধান ফোল্ডার** ব্যবহার করুন এবং শেখা ও রেফারেন্সের জন্য **সম্পূর্ণ উদাহরণসমূহ** ব্যবহার করুন।

## প্রধান বিষয়সমূহ

এই অধ্যায়ের মূল বিষয়গুলি ক্লায়েন্ট সম্পর্কে নিম্নরূপ:

- সার্ভারে বৈশিষ্ট্য আবিষ্কার এবং আহ্বান উভয়ের জন্য ব্যবহার করা যেতে পারে।
- যখন এটি নিজেই শুরু হয় তখন সার্ভার চালু করতে পারে (এই অধ্যায়ের মতো) তবে ক্লায়েন্টরা চলমান সার্ভারের সাথে সংযোগও করতে পারে।
- পূর্ববর্তী অধ্যায়ে বর্ণিত বিকল্পগুলোর পাশাপাশি যেমন ইন্সপেক্টরের মতো সার্ভারের সক্ষমতা পরীক্ষা করার খুব ভাল উপায়।

## অতিরিক্ত সম্পদ

- [MCP-এ ক্লায়েন্ট তৈরি](https://modelcontextprotocol.io/quickstart/client)

## নমুনাসমূহ

- [জাভা ক্যালকুলেটর](../samples/java/calculator/README.md)
- [.NET ক্যালকুলেটর](../../../../03-GettingStarted/samples/csharp)
- [জাভাস্ক্রিপ্ট ক্যালকুলেটর](../samples/javascript/README.md)
- [টাইপস্ক্রিপ্ট ক্যালকুলেটর](../samples/typescript/README.md)
- [পাইথন ক্যালকুলেটর](../../../../03-GettingStarted/samples/python)
- [রাস্ট ক্যালকুলেটর](../../../../03-GettingStarted/samples/rust)

## পরবর্তী কি

- পরবর্তী: [LLM সহ ক্লায়েন্ট তৈরি](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->