# ক্লায়েন্ট তৈরি করা

ক্লায়েন্টগুলি এমন কাস্টম অ্যাপ্লিকেশন বা স্ক্রিপ্ট যা সরাসরি MCP সার্ভারের সাথে যোগাযোগ করে রিসোর্স, টুল এবং প্রম্পটগুলি অনুরোধ করে। ইন্সপেক্টর টুল ব্যবহারের থেকে ভিন্ন, যা সার্ভারের সাথে ইন্টারঅ্যাক্ট করার জন্য একটি গ্রাফিক্যাল ইন্টারফেস প্রদান করে, নিজস্ব ক্লায়েন্ট লেখার মাধ্যমে আপনি প্রোগ্রাম্যাটিক এবং স্বয়ংক্রিয় ইন্টারঅ্যাকশন করতে পারেন। এটি ডেভেলপারদের MCP ক্ষমতাগুলিকে তাদের নিজস্ব ওয়ার্কফ্লোতে একত্রিত করার, কাজগুলি স্বয়ংক্রিয় করার এবং নির্দিষ্ট প্রয়োজনের জন্য কাস্টম সমাধান তৈরি করার সুযোগ দেয়।

## ওভারভিউ

এই পাঠে Model Context Protocol (MCP) ইকোসিস্টেমের মধ্যে ক্লায়েন্টের ধারণা পরিচয় করানো হয়। আপনি শিখবেন কিভাবে নিজের ক্লায়েন্ট লিখে সেটিকে MCP সার্ভারের সাথে সংযুক্ত করবেন।

## শেখার উদ্দেশ্য

এই পাঠ শেষে আপনি পারবেন:

- একটি ক্লায়েন্ট কী করতে পারে তা বোঝা।
- নিজস্ব ক্লায়েন্ট লেখা।
- একটি MCP সার্ভারের সাথে ক্লায়েন্ট সংযুক্ত করা এবং পরীক্ষণ করা যাতে নিশ্চিত হওয়া যায় এটি প্রত্যাশিতভাবে কাজ করছে।

## একটি ক্লায়েন্ট লেখার জন্য কি দরকার?

একটি ক্লায়েন্ট লেখার জন্য আপনাকে নিম্নলিখিত কাজগুলো করতে হবে:

- **ঠিক লাইব্রেরি আমদানি করা।** আপনি আগের মতো একই লাইব্রেরি ব্যবহার করবেন, শুধু ভিন্ন রচনাসমূহ।
- **একটি ক্লায়েন্ট উদাহরণ তৈরি করা।** একটি ক্লায়েন্ট ইনস্ট্যান্স তৈরি করতে হবে এবং এটি নির্বাচিত ট্রান্সপোর্ট পদ্ধতির সাথে সংযুক্ত করতে হবে।
- **কোন রিসোর্স লিস্ট করতে হবে তা নির্ধারণ করা।** আপনার MCP সার্ভারে রিসোর্স, টুল এবং প্রম্পট রয়েছে, আপনাকে নির্ধারণ করতে হবে কোনগুলো লিস্ট করবেন।
- **ক্লায়েন্টকে হোস্ট অ্যাপ্লিকেশনে একত্রিত করা।** সার্ভারের ক্ষমতা বুঝে আপনি এটি হোস্ট অ্যাপ্লিকেশনে একত্রিত করবেন যাতে ব্যবহারকারী প্রম্পট বা অন্য কোনো কমান্ড টাইপ করলে সংশ্লিষ্ট সার্ভার ফিচারটি আহ্বান করা হয়।

এখন আমরা উচ্চ-স্তরে বুঝে গেছি আমরা কি করতে যাচ্ছি, চলুন পরবর্তী উদাহরণ দেখি।

### একটি উদাহরণ ক্লায়েন্ট

এই উদাহরণ ক্লায়েন্টটি দেখে নিন:

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

// প্রম্পটগুলোর তালিকা
const prompts = await client.listPrompts();

// একটি প্রম্পট পান
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// রিসোর্স তালিকা
const resources = await client.listResources();

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
```

উপরের কোডে আমরা:

- লাইব্রেরি আমদানি করেছি
- একটি ক্লায়েন্ট উদাহরণ তৈরি করে stdio ট্রান্সপোর্ট ব্যবহার করে সংযুক্ত করেছি।
- প্রম্পট, রিসোর্স এবং টুল লিস্ট করে সেগুলো আহ্বান করেছি।

এখানে আছে, একটি ক্লায়েন্ট যা MCP সার্ভারের সাথে কথা বলতে পারে।

পরবর্তী অনুশীলন বিভাগে আমরা প্রতিটি কোড স্নিপেট ধীরে ধীরে ভেঙে দেখে বুঝাব।

## অনুশীলন: একটি ক্লায়েন্ট লেখা

উপরোক্ত মতো কোড বর্ণনা ধীরে ধীরে নেব, এবং চাইলে সাথে সাথে কোড করতেও পারেন।

### -1- লাইব্রেরি আমদানি করা

প্রয়োজনীয় লাইব্রেরি আমদানি করি, আমাদের ক্লায়েন্ট এবং আমাদের নির্বাচিত ট্রান্সপোর্ট প্রোটোকল stdio-র রেফারেন্স লাগবে। stdio হলো আপনার লোকাল মেশিনে চালানোর জন্য প্রোটোকল। SSE আরেকটি ট্রান্সপোর্ট প্রোটোকল যা ভবিষ্যত অধ্যায়ে দেখানো হবে, যা অন্য একটি বিকল্প। আপাতত stdio দিয়ে চালিয়ে যাই।

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

জাভার জন্য, আপনি একটি ক্লায়েন্ট তৈরি করবেন যা পূর্ববর্তী অনুশীলনের MCP সার্ভারের সাথে সংযুক্ত হবে। [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) থেকে একই Java Spring Boot প্রকল্প কাঠামো ব্যবহার করে `src/main/java/com/microsoft/mcp/sample/client/` ফোল্ডারে `SDKClient` নামে একটি নতুন Java ক্লাস তৈরি করুন এবং নিম্নলিখিত আমদানি যোগ করুন:

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

`Cargo.toml` ফাইলে নিম্নলিখিত নির্ভরতাগুলি যোগ করতে হবে।

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

তারপর ক্লায়েন্ট কোডে প্রয়োজনীয় লাইব্রেরি আমদানি করতে পারেন।

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

এখন উদাহরণ তৈরি করি।

### -2- ক্লায়েন্ট এবং ট্রান্সপোর্ট ইনস্ট্যান্টিয়েট করা

ট্রান্সপোর্ট এবং ক্লায়েন্টের ইনস্ট্যান্স তৈরি করতে হবে:

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

উপরের কোডে:

- একটি stdio ট্রান্সপোর্ট উদাহরণ তৈরি করেছি। লক্ষ্য করুন এটি কমান্ড এবং আর্গুমেন্ট নির্দিষ্ট করে কিভাবে সার্ভার খুঁজে পেতে এবং চালু করতে হবে, কারণ এটি আমাদের ক্লায়েন্ট তৈরির সময় করতে হবে।

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- একটি ক্লায়েন্ট উদাহরণ তৈরি করেছি নাম এবং সংস্করণ দিয়ে।

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ক্লায়েন্টটিকে নির্বাচিত ট্রান্সপোর্টের সাথে সংযুক্ত করেছি।

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# stdio সংযোগের জন্য সার্ভার প্যারামিটার তৈরি করুন
server_params = StdioServerParameters(
    command="mcp",  # নির্বাহযোগ্য
    args=["run", "server.py"],  # ঐচ্ছিক কমান্ড লাইন আর্গুমেন্ট
    env=None,  # ঐচ্ছিক পরিবেশগত ভেরিয়েবল
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # সংযোগ আরম্ভ করুন
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

উপরের কোডে:

- প্রয়োজনীয় লাইব্রেরি আমদানি করেছি
- সার্ভার প্যারামিটার অবজেক্ট উদাহরণ তৈরি করেছি যা দিয়ে সার্ভার চালিয়ে ক্লায়েন্ট সংযুক্ত করব।
- একটি `run` মেথড সংজ্ঞায়িত করেছি যা `stdio_client` কল করে ক্লায়েন্ট সেশন শুরু করে।
- `asyncio.run` এ `run` মেথড প্রদান করার জন্য একটি এন্ট্রি পয়েন্ট তৈরি করেছি।

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

উপরের কোডে:

- প্রয়োজনীয় লাইব্রেরি আমদানি করেছি.
- একটি stdio ট্রান্সপোর্ট তৈরি করেছি এবং `mcpClient` নামক একটি ক্লায়েন্ট তৈরি করেছি, যা MCP সার্ভারে ফিচার তালিকা এবং আহ্বানে ব্যবহৃত হবে।

বিঃদ্রঃ, "Arguments" এ আপনি *.csproj* বা এক্সিকিউটেবল পয়েন্ট করতে পারেন।

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
        
        // আপনার ক্লায়েন্ট লজিক এখানে যাবে
    }
}
```

উপরের কোডে:

- একটি মেইন মেথড তৈরি করেছি যা একটি SSE ট্রান্সপোর্ট সেটআপ করে, সেটি `http://localhost:8080` পয়েন্ট করছে, যেখানে MCP সার্ভার চলছে।
- একটি ক্লায়েন্ট ক্লাস তৈরি করেছি যেটা কনস্ট্রাক্টরে ট্রান্সপোর্ট নেয়।
- `run` মেথডে ট্রান্সপোর্ট দিয়ে সিনক্রোনাস MCP ক্লায়েন্ট তৈরি ও কানেকশন ইনিশিয়ালাইজ করেছি।
- SSE (Server-Sent Events) ট্রান্সপোর্ট ব্যবহার করেছি, যা Java Spring Boot MCP সার্ভারের HTTP ভিত্তিক যোগাযোগের জন্য উপযোগী।

#### Rust

এই Rust ক্লায়েন্ট ধরে নিচ্ছে সার্ভার একই ডিরেক্টরির "calculator-server" নামে সিবলিং প্রজেক্ট। নিচের কোড সার্ভার শুরু করে এবং সংযুক্ত করে।

```rust
async fn main() -> Result<(), RmcpError> {
    // ধরে নিন সার্ভার একই ডিরেক্টরির একটি সহোদর প্রকল্প যার নাম "calculator-server"
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

    // TODO: প্রাথমিকরণ করুন

    // TODO: সরঞ্জামগুলি তালিকা করুন

    // TODO: add সরঞ্জাম কল করুন আর্গুমেন্ট সহ = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- সার্ভারের ফিচারগুলোর তালিকা করা

আমাদের এখন একটি ক্লায়েন্ট আছে যা সংযোজিত হতে পারে যদি প্রোগ্রাম চালানো হয়। তবে এটি বৈশিষ্ট্যগুলো তালিকাভুক্ত করে না, তাই এখন সে কাজ করি:

#### TypeScript

```typescript
// তালিকা নির্দেশনা
const prompts = await client.listPrompts();

// তালিকা সম্পদ
const resources = await client.listResources();

// তালিকা সরঞ্জামগুলো
const tools = await client.listTools();
```

#### Python

```python
# উপলব্ধ সম্পদসমূহের তালিকা তৈরি করুন
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# উপলব্ধ সরঞ্জামসমূহের তালিকা তৈরি করুন
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

এখানে আমরা উপলব্ধ রিসোর্স `list_resources()` এবং টুল `list_tools` তালিকা করে প্রিন্ট করছি।

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

উপরে একটি উদাহরণ দেয়া হয়েছে কিভাবে সার্ভারের টুলগুলি তালিকা করতে হয়। প্রতিটি টুলের জন্য আমরা নাম প্রিন্ট করছি।

#### Java

```java
// সরঞ্জামগুলিকে তালিকাভুক্ত করুন এবং প্রদর্শন করুন
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// সংযোগ যাচাই করার জন্য আপনি সার্ভারকে পিংও করতে পারেন
client.ping();
```

উপরের কোডে:

- `listTools()` কল করে MCP সার্ভার থেকে সব উপলব্ধ টুল পেয়েছি।
- `ping()` ব্যবহার করে সার্ভারের সাথে সংযোগ কার্যকর কিনা পরীক্ষা করেছি।
- `ListToolsResult` তে সব টুলের নাম, বর্ণনা এবং ইনপুট স্কিমার তথ্য আছে।

চমৎকার, এখন সব ফিচার ক্যাপচার হয়েছে। কিন্তু প্রশ্ন হল, কখন এগুলো ব্যবহার করবেন? এই ক্লায়েন্টটি বেশ সরল, অর্থাৎ ফিচারগুলি ব্যবহার করতে হলে আপনাকে স্পষ্টভাবে আহ্বান করতে হবে। পরবর্তী অধ্যায়ে আমরা এমন একটি অ্যাডভান্সড ক্লায়েন্ট তৈরি করব যার নিজের একটি বড় ভাষা মডেল (LLM) থাকবে। আপাতত দেখে নিই কিভাবে সার্ভারের ফিচারগুলি আহ্বান করা যায়:

#### Rust

মেইন ফাংশনে ক্লায়েন্ট ইনিশিয়ালাইজ করার পর সার্ভার ইনিশিয়ালাইজ করে কিছু ফিচার তালিকা করতে পারি।

```rust
// প্রাথমিক রূপে প্রস্তুত করা
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// টুলসের তালিকা
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- ফিচার আহ্বান করা

ফিচার আহ্বান করতে হলে সঠিক আর্গুমেন্ট এবং মাঝে মাঝে নাম নির্দিষ্ট করতে হবে যা আপনি আহ্বান করতে চাইছেন।

#### TypeScript

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

উপরের কোডে:

- একটি রিসোর্স পড়া হয়েছে, `readResource()` কল করে `uri` নির্দিষ্ট করা হয়েছে। সার্ভার সাইডে এরকম দেখায়:

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

    আমাদের `uri` মান `file://example.txt` সার্ভারে `file://{name}`-এর সাথে মিলে যায়। `example.txt` `name`-এর সঙ্গে ম্যাপ হবে।

- একটি টুল কল করা হয়েছে, নাম এবং আর্গুমেন্ট দিয়ে:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- প্রম্পট আনা হয়েছে, `getPrompt()` কল করে নাম এবং আর্গুমেন্ট সহ। সার্ভার কোড নিম্নরূপ:

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

    এবং আপনার ক্লায়েন্ট কোড সার্ভারে ঘোষিত এর সাথে মিলবে:

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
# একটি রিসোর্স পড়ুন
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# একটি টুল কল করুন
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

উপরের কোডে:

- `greeting` নামক রিসোর্স `read_resource` দিয়ে কল করা হয়েছে।
- `add` নামক টুল `call_tool` দিয়ে আহ্বান করা হয়েছে।

#### .NET

1. একটি টুল কল করার কোড:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. আউটপুট প্রিন্ট করার কোড:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// বিভিন্ন ক্যালকুলেটর টুল কল করুন
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

উপরের কোডে:

- একাধিক ক্যালকুলেটর টুল `callTool()` পদ্ধতি এবং `CallToolRequest` অবজেক্ট ব্যবহার করে কল করা হয়েছে।
- প্রতিটি টুল কল নির্দিষ্ট টুল নাম এবং টুলের জন্য প্রয়োজনীয় আর্গুমেন্টের `Map` নির্ধারণ করে।
- সার্ভারের টুলগুলি নির্দিষ্ট প্যারামিটার নাম প্রত্যাশা করে (যেমন গণিতিক অপারেশনের জন্য "a", "b")।
- ফলাফল `CallToolResult` অবজেক্ট হিসাবে আসে যা সার্ভারের উত্তর ধারণ করে।

#### Rust

```rust
// যুক্তি সহ add টুল কল করুন = {"a": 3, "b": 2}
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

ক্লায়েন্ট চালাতে টার্মিনালে নিম্নলিখিত কমান্ড টাইপ করুন:

#### TypeScript

*package.json* এর "scripts" সেকশনে নিম্নলিখিত এন্ট্রি যোগ করুন:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

নিম্নলিখিত কমান্ড দিয়ে ক্লায়েন্ট কল করুন:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

প্রথমে নিশ্চিত করুন MCP সার্ভার `http://localhost:8080` এ চলছে। এরপর ক্লায়েন্ট চালান:

```bash
# আপনার প্রকল্প তৈরি করুন
./mvnw clean compile

# ক্লায়েন্ট চালান
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

অথবা, আপনি সমাধান ফোল্ডারে দেওয়া সম্পূর্ণ ক্লায়েন্ট প্রজেক্ট `03-GettingStarted\02-client\solution\java` চালাতে পারেন:

```bash
# সমাধান ডিরেক্টরিতে নেভিগেট করুন
cd 03-GettingStarted/02-client/solution/java

# JAR তৈরি এবং চালনা করুন
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## অ্যাসাইনমেন্ট

এই অ্যাসাইনমেন্টে, আপনি শিখেছেন ক্লায়েন্ট তৈরিতে আপনার আত্মবিশ্বাস পাবেন এবং নিজস্ব ক্লায়েন্ট তৈরি করবেন।

নিচে একটি সার্ভার আছে যা আপনাকে ক্লায়েন্ট কোড দ্বারা কল করতে হবে, দেখুন আপনি কি সার্ভারে আরও ফিচার যোগ করতে পারেন যাতে এটি আরও আকর্ষণীয় হয়।

### TypeScript

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

// একটি গতিশীল অভিবাদন সম্পদ যোগ করুন
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

// stdin এ মেসেজ গ্রহণ শুরু করুন এবং stdout এ মেসেজ পাঠান শুরু করুন

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

# একটি MCP সার্ভার তৈরি করুন
mcp = FastMCP("Demo")


# একটি যোগ করার সরঞ্জাম যুক্ত করুন
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# একটি ডায়নামিক অভ্যর্থনা রিসোর্স যুক্ত করুন
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

এই প্রজেক্টটি দেখুন কিভাবে [প্রম্পট এবং রিসোর্স যোগ করবেন](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)।

এছাড়াও, এই লিঙ্কটি দেখুন কিভাবে [প্রম্পট এবং রিসোর্স আহ্বান করবেন](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)।

### Rust

[আগের অধ্যায়ে](../../../../03-GettingStarted/01-first-server) আপনি শিখেছেন কিভাবে একটি সাদামাটা MCP সার্ভার Rust দিয়ে তৈরি করবেন। আপনি সেটা ভিত্তি করে আরও তৈরি করতে পারেন অথবা এই লিঙ্ক থেকে Rust ভিত্তিক MCP সার্ভারের আরো উদাহরণ দেখতে পারেন: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## সমাধান

**সমাধান ফোল্ডার** গুলো সম্পূর্ণ, কাজ করার মত ক্লায়েন্ট ইমপ্লিমেন্টেশন ধারণ করে যা এই টিউটোরিয়ালে আলোচিত সব ধারণাগুলি প্রদর্শন করে। প্রতিটি সমাধান ক্লায়েন্ট এবং সার্ভার কোড পৃথক, স্বনির্ভর প্রকল্প হিসেবে সংগঠিত।

### 📁 সমাধান কাঠামো

সমাধান ডিরেক্টরি প্রোগ্রামিং ভাষা অনুযায়ী সংগঠিত:

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

### 🚀 প্রতিটি সমাধানে কি আছে

প্রত্যেক ভাষা-নির্দিষ্ট সমাধানে অন্তর্ভুক্ত:

- **পুরো ক্লায়েন্ট ইমপ্লিমেন্টেশন** টিউটোরিয়ালের সব ফিচার সহ
- **কাজ করা প্রকল্প কাঠামো** যথাযথ নির্ভরতাসমূহ এবং কনফিগারেশন সহ
- **বিল্ড ও রান স্ক্রিপ্ট** সহজ সেটআপ ও কার্যকর করার জন্য
- **বিস্তারিত README** ভাষা-নির্দিষ্ট নির্দেশাবলীসহ
- **ত্রুটি পরিচালনা** এবং ফলাফল প্রক্রিয়াকরণের উদাহরণ

### 📖 সমাধান ব্যবহারের নির্দেশনা

1. **আপনার পছন্দের ভাষার ফোল্ডারে যান**:

   ```bash
   cd solution/typescript/    # টাইপস্ক্রিপ্ট-এর জন্য
   cd solution/java/          # জাভার জন্য
   cd solution/python/        # পাইথনের জন্য
   cd solution/dotnet/        # .NET-এর জন্য
   ```

2. **প্রতিটি ফোল্ডারে README নির্দেশাবলী অনুসরণ করুন**:
   - নির্ভরতাগুলি ইনস্টল করা
   - প্রকল্প বিল্ড করা
   - ক্লায়েন্ট চালানো

3. **আপনি যা আউটপুট দেখতে পারেন তার উদাহরণ**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

সম্পূর্ণ ডকুমেন্টেশন এবং ধাপে ধাপে নির্দেশনার জন্য দেখুন: **[📖 Solution Documentation](./solution/README.md)**

## 🎯 সম্পূর্ণ উদাহরণ

আমরা এই টিউটোরিয়ালে আলোচিত সকল প্রোগ্রামিং ভাষার জন্য সম্পূর্ণ কাজ করার মত ক্লায়েন্ট ইমপ্লিমেন্টেশন প্রদান করেছি। এই উদাহরণগুলি সম্পূর্ণ কার্যকারিতা প্রদর্শন করে যা উপরোক্ত বর্ণনা করা হয়েছে এবং আপনার নিজের প্রকল্পের জন্য রেফারেন্স ইমপ্লিমেন্টেশন বা শুরু করা বিন্দু হিসেবে ব্যবহার করতে পারেন।

### উপলব্ধ সম্পূর্ণ উদাহরণ

| ভাষা | ফাইল | বিবরণ |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ট্রান্সপোর্ট ব্যবহার করে বিস্তৃত ত্রুটি পরিচালনার সাথে সম্পূর্ণ Java ক্লায়েন্ট |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ট্রান্সপোর্ট ব্যবহার করে স্বয়ংক্রিয় সার্ভার স্টার্টআপ সহ সম্পূর্ণ C# ক্লায়েন্ট |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | MCP প্রোটোকলের সম্পূর্ণ সমর্থনসহ সম্পূর্ণ TypeScript ক্লায়েন্ট |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await প্যাটার্ন ব্যবহার করে সম্পূর্ণ Python ক্লায়েন্ট |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio ব্যবহার করে অ্যাসিঙ্ক অপারেশন সম্পাদনকারী সম্পূর্ণ Rust ক্লায়েন্ট |

প্রতিটি সম্পূর্ণ উদাহরণ অন্তর্ভুক্ত:
- ✅ **কনেকশন স্থাপন** এবং ত্রুটি পরিচালনা
- ✅ **সার্ভার আবিষ্কার** (যথাস্থানে টুলস, রিসোর্স, প্রম্পট)
- ✅ **ক্যালকুলেটর অপারেশন** (যোগ, বিয়োগ, গুণ, ভাগ, সাহায্য)
- ✅ **ফলাফল প্রক্রিয়াকরণ** এবং ফরম্যাট করা আউটপুট
- ✅ **সম্পূর্ণ ত্রুটি পরিচালনা**
- ✅ **পরিষ্কার, ডকুমেন্টেড কোড** ধাপে ধাপে কমেন্টসহ

### সম্পূর্ণ উদাহরণের মাধ্যমে শুরু করা

1. উপরের টেবিল থেকে আপনার পছন্দসই ভাষা **চয়ন করুন**
2. পূর্ণ বাস্তবায়ন বোঝার জন্য **সম্পূর্ণ উদাহরণ ফাইল পর্যালোচনা করুন**
3. নির্দেশনা অনুযায়ী [`complete_examples.md`](./complete_examples.md) এ থাকা উদাহরণটি **চালান**
4. আপনার নির্দিষ্ট ব্যবহারের জন্য উদাহরণটি **পরিবর্তন এবং প্রসারিত করুন**

এই উদাহরণগুলি চালানো এবং কাস্টমাইজ করার বিস্তারিত ডকুমেন্টেশনের জন্য দেখুন: **[📖 Complete Examples Documentation](./complete_examples.md)**

### 💡 সলিউশন বনাম সম্পূর্ণ উদাহরণ

| **সলিউশন ফোল্ডার** | **সম্পূর্ণ উদাহরণ** |
|---------------------|-------------------- |
| বিল্ড ফাইলসহ পূর্ণ প্রকল্প কাঠামো | একক-ফাইল বাস্তবায়ন |
| নির্ভরশীলতাসহ চলার জন্য প্রস্তুত | কেন্দ্রিভূত কোড উদাহরণ |
| উৎপাদনের মতো সেটআপ | শিক্ষামূলক রেফারেন্স |
| ভাষা-নির্দিষ্ট টুলিং | ভাষা-বিশেষ তুলনা |

উভয়পদ্ধতি মূল্যবান - সম্পূর্ণ প্রকল্পের জন্য **সলিউশন ফোল্ডার** এবং শেখা ও রেফারেন্সের জন্য **সম্পূর্ণ উদাহরণ** ব্যবহার করুন।

## প্রধান বিষয়সমূহ

এই অধ্যায়ে ক্লায়েন্টদের সম্পর্কে প্রধান বিষয়সমূহ হলো:

- সার্ভারে ফিচার আবিষ্কার এবং আহ্বানের জন্য ব্যবহার করা যেতে পারে।
- নিজেকে চালু করার সময় একটি সার্ভার শুরু করতে পারে (যেমন এই অধ্যায়ে) তবে ক্লায়েন্ট চলমান সার্ভারের সাথে সংযোগও করতে পারে।
- সার্ভারের ক্ষমতা পরীক্ষার জন্য Inspector এর মতো বিকল্পের পাশাপাশিও একটি দুর্দান্ত উপায়।

## অতিরিক্ত রিসোর্স

- [MCP তে ক্লায়েন্ট তৈরি](https://modelcontextprotocol.io/quickstart/client)

## নমুনা

- [জাভা ক্যালকুলেটর](../samples/java/calculator/README.md)
- [.Net ক্যালকুলেটর](../../../../03-GettingStarted/samples/csharp)
- [জাভাস্ক্রিপ্ট ক্যালকুলেটর](../samples/javascript/README.md)
- [টাইপস্ক্রিপ্ট ক্যালকুলেটর](../samples/typescript/README.md)
- [পাইথন ক্যালকুলেটর](../../../../03-GettingStarted/samples/python)
- [রাষ্ট ক্যালকুলেটর](../../../../03-GettingStarted/samples/rust)

## পরবর্তী কি

- পরবর্তী: [একটি LLM সহ ক্লায়েন্ট তৈরি](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসত্যতা থাকতে পারে তা মাথায় রাখুন। মূল নথিটি তার নিজস্ব ভাষায় প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ প্রয়োজন। এই অনুবাদের ব্যবহারের কারণে যে কোনো ভুল বোঝাবুঝি বা ভুলব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->