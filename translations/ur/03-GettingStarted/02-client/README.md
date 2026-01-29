# کلائنٹ بنانا

کلائنٹس وہ کسٹم ایپلیکیشنز یا اسکرپٹس ہیں جو براہ راست ایک MCP سرور کے ساتھ بات چیت کرتے ہیں تاکہ وسائل، ٹولز، اور پرامپٹس کی درخواست کی جا سکے۔ انسپکٹر ٹول کے استعمال کے برعکس، جو سرور کے ساتھ تعامل کے لیے ایک گرافیکل انٹرفیس فراہم کرتا ہے، اپنا کلائنٹ لکھنے سے پروگراماتی اور خودکار تعاملات ممکن ہوتے ہیں۔ یہ ڈویلپرز کو MCP کی صلاحیتوں کو اپنے ورک فلو میں ضم کرنے، کاموں کو خودکار کرنے، اور مخصوص ضروریات کے مطابق کسٹم حل تیار کرنے کی اجازت دیتا ہے۔

## جائزہ

یہ سبق ماڈل کانٹیکسٹ پروٹوکول (MCP) ایکو سسٹم میں کلائنٹس کے تصور کو متعارف کراتا ہے۔ آپ سیکھیں گے کہ اپنا کلائنٹ کیسے لکھیں اور اسے MCP سرور سے کیسے جوڑیں۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ یہ کرنے کے قابل ہوں گے:

- سمجھ سکیں کہ کلائنٹ کیا کر سکتا ہے۔
- اپنا کلائنٹ لکھ سکیں۔
- کلائنٹ کو MCP سرور سے جوڑ کر ٹیسٹ کریں تاکہ یہ یقینی بنایا جا سکے کہ سرور توقع کے مطابق کام کر رہا ہے۔

## کلائنٹ لکھنے میں کیا شامل ہے؟

کلائنٹ لکھنے کے لیے، آپ کو درج ذیل کام کرنے ہوں گے:

- **صحیح لائبریریاں درآمد کریں**۔ آپ وہی لائبریری استعمال کریں گے جو پہلے استعمال کی گئی تھی، بس مختلف کنسٹرکٹس کے ساتھ۔
- **کلائنٹ کو انسٹیٹیوٹ کریں**۔ اس میں کلائنٹ کی ایک انسٹینس بنانا اور اسے منتخب کردہ ٹرانسپورٹ میتھڈ سے جوڑنا شامل ہوگا۔
- **یہ فیصلہ کریں کہ کون سے وسائل کی فہرست بنانی ہے**۔ آپ کے MCP سرور میں وسائل، ٹولز، اور پرامپٹس شامل ہیں، آپ کو فیصلہ کرنا ہوگا کہ کون سا ظاہر کرنا ہے۔
- **کلائنٹ کو میزبان ایپلیکیشن میں ضم کریں**۔ ایک بار جب آپ سرور کی صلاحیتوں کو جان لیں، تو آپ کو اسے اپنی میزبان ایپلیکیشن میں ضم کرنا ہوگا تاکہ اگر کوئی صارف پرامپٹ یا کوئی اور کمانڈ ٹائپ کرے تو متعلقہ سرور فیچر فعال ہو جائے۔

اب جب کہ ہم نے اعلیٰ سطح پر سمجھ لیا ہے کہ ہم کیا کرنے جا رہے ہیں، آئیے اگلی مثال پر نظر ڈالیں۔

### ایک مثال کلائنٹ

آئیے اس مثال کلائنٹ کو دیکھتے ہیں:

### ٹائپ اسکرپٹ

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

اوپر دیے گئے کوڈ میں ہم نے:

- لائبریریاں درآمد کیں۔
- کلائنٹ کی ایک انسٹینس بنائی اور اسے stdio کے ذریعے ٹرانسپورٹ کے لیے جوڑا۔
- پرامپٹس، وسائل، اور ٹولز کی فہرست بنائی اور ان سب کو فعال کیا۔

یہ رہا، ایک کلائنٹ جو MCP سرور سے بات کر سکتا ہے۔

آئیے اگلے مشق کے سیکشن میں وقت نکال کر ہر کوڈ اسنیپٹ کو توڑ کر سمجھتے ہیں کہ کیا ہو رہا ہے۔

## مشق: کلائنٹ لکھنا

جیسا کہ اوپر کہا گیا، آئیے کوڈ کی وضاحت کرتے ہوئے وقت نکالتے ہیں، اور اگر آپ چاہیں تو ساتھ ساتھ کوڈ کریں۔

### -1- لائبریریاں درآمد کریں

آئیے وہ لائبریریاں درآمد کریں جن کی ہمیں ضرورت ہے۔ ہمیں کلائنٹ اور اپنے منتخب کردہ ٹرانسپورٹ پروٹوکول، stdio، کے حوالہ جات کی ضرورت ہوگی۔ stdio ایک پروٹوکول ہے جو آپ کی مقامی مشین پر چلنے والی چیزوں کے لیے ہے۔ SSE ایک اور ٹرانسپورٹ پروٹوکول ہے جسے ہم آئندہ ابواب میں دکھائیں گے، لیکن یہ آپ کا دوسرا آپشن ہے۔ فی الحال، آئیے stdio کے ساتھ جاری رکھیں۔

#### ٹائپ اسکرپٹ

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### پائتھون

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .نیٹ

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;
```

#### جاوا

جاوا کے لیے، آپ ایک کلائنٹ بنائیں گے جو پچھلی مشق کے MCP سرور سے جڑتا ہے۔ جاوا اسپرنگ بوٹ پروجیکٹ اسٹرکچر کا استعمال کرتے ہوئے [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) سے ایک نئی جاوا کلاس `SDKClient` بنائیں اور درج ذیل درآمدات شامل کریں:

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

#### رسٹ

آپ کو اپنے `Cargo.toml` فائل میں درج ذیل ڈیپینڈنسیز شامل کرنے کی ضرورت ہوگی۔

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

اس کے بعد، آپ اپنی کلائنٹ کوڈ میں ضروری لائبریریاں درآمد کر سکتے ہیں۔

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

آئیے انسٹیٹیوشن کی طرف بڑھتے ہیں۔

### -2- کلائنٹ اور ٹرانسپورٹ کو انسٹیٹیوٹ کرنا

ہمیں ٹرانسپورٹ اور اپنے کلائنٹ کی ایک انسٹینس بنانی ہوگی:

#### ٹائپ اسکرپٹ

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

اوپر دیے گئے کوڈ میں ہم نے:

- stdio ٹرانسپورٹ انسٹینس بنائی۔ نوٹ کریں کہ یہ سرور کو تلاش کرنے اور شروع کرنے کے لیے کمانڈ اور آرگس کو کیسے مخصوص کرتا ہے، کیونکہ یہ وہ چیز ہے جو ہمیں کلائنٹ بناتے وقت کرنی ہوگی۔

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- کلائنٹ کو ایک نام اور ورژن دے کر انسٹیٹیوٹ کیا۔

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- کلائنٹ کو منتخب کردہ ٹرانسپورٹ سے جوڑا۔

    ```typescript
    await client.connect(transport);
    ```

#### پائتھون

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

اوپر دیے گئے کوڈ میں ہم نے:

- ضروری لائبریریاں درآمد کیں۔
- سرور پیرامیٹرز آبجیکٹ انسٹیٹیوٹ کیا کیونکہ ہم اسے سرور چلانے کے لیے استعمال کریں گے تاکہ ہم اپنے کلائنٹ کے ساتھ اس سے جڑ سکیں۔
- ایک `run` میتھڈ ڈیفائن کیا جو `stdio_client` کو کال کرتا ہے، جو کلائنٹ سیشن شروع کرتا ہے۔
- ایک انٹری پوائنٹ بنایا جہاں ہم `run` میتھڈ کو `asyncio.run` فراہم کرتے ہیں۔

#### .نیٹ

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

اوپر دیے گئے کوڈ میں ہم نے:

- ضروری لائبریریاں درآمد کیں۔
- stdio ٹرانسپورٹ بنائی اور ایک کلائنٹ `mcpClient` بنایا۔ یہ وہ چیز ہے جسے ہم MCP سرور پر فیچرز کی فہرست بنانے اور فعال کرنے کے لیے استعمال کریں گے۔

نوٹ کریں، "Arguments" میں، آپ یا تو *.csproj* یا ایگزیکیوٹیبل کی طرف اشارہ کر سکتے ہیں۔

#### جاوا

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

اوپر دیے گئے کوڈ میں ہم نے:

- ایک مین میتھڈ بنایا جو `http://localhost:8080` پر چلنے والے MCP سرور کی طرف اشارہ کرتے ہوئے ایک SSE ٹرانسپورٹ سیٹ کرتا ہے۔
- ایک کلائنٹ کلاس بنائی جو کنسٹرکٹر پیرامیٹر کے طور پر ٹرانسپورٹ لیتی ہے۔
- `run` میتھڈ میں، ہم ٹرانسپورٹ کا استعمال کرتے ہوئے ایک سنکرونس MCP کلائنٹ بناتے ہیں اور کنکشن کو انیشیٹ کرتے ہیں۔
- SSE (سرور-سینٹ ایونٹس) ٹرانسپورٹ استعمال کیا جو جاوا اسپرنگ بوٹ MCP سرورز کے ساتھ HTTP پر مبنی کمیونیکیشن کے لیے موزوں ہے۔

#### رسٹ

یہ رسٹ کلائنٹ فرض کرتا ہے کہ سرور ایک بہن پروجیکٹ ہے جس کا نام "calculator-server" ہے اور وہ اسی ڈائریکٹری میں موجود ہے۔ نیچے دیا گیا کوڈ سرور کو شروع کرے گا اور اس سے جڑے گا۔

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

### -3- سرور فیچرز کی فہرست بنانا

اب، ہمارے پاس ایک کلائنٹ ہے جو پروگرام چلائے جانے پر جڑ سکتا ہے۔ تاہم، یہ دراصل اس کی فیچرز کی فہرست نہیں بناتا، تو آئیے یہ کام کریں:

#### ٹائپ اسکرپٹ

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### پائتھون

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

یہاں ہم دستیاب وسائل `list_resources()` اور ٹولز `list_tools` کی فہرست بناتے ہیں اور انہیں پرنٹ کرتے ہیں۔

#### .نیٹ

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

اوپر ایک مثال ہے کہ ہم سرور پر موجود ٹولز کی فہرست کیسے بنا سکتے ہیں۔ ہر ٹول کے لیے، ہم اس کا نام پرنٹ کرتے ہیں۔

#### جاوا

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

اوپر دیے گئے کوڈ میں ہم نے:

- `listTools()` کو کال کیا تاکہ MCP سرور سے تمام دستیاب ٹولز حاصل کیے جا سکیں۔
- `ping()` کا استعمال کیا تاکہ یہ تصدیق کی جا سکے کہ سرور سے کنکشن کام کر رہا ہے۔
- `ListToolsResult` میں تمام ٹولز کی معلومات شامل ہوتی ہیں، جیسے ان کے نام، وضاحتیں، اور ان پٹ اسکیمے۔

زبردست، اب ہم نے تمام فیچرز کو کیپچر کر لیا ہے۔ اب سوال یہ ہے کہ ہم انہیں کب استعمال کریں؟ یہ کلائنٹ کافی سادہ ہے، اس لحاظ سے کہ ہمیں فیچرز کو فعال کرنے کے لیے انہیں واضح طور پر کال کرنا ہوگا۔ اگلے باب میں، ہم ایک زیادہ جدید کلائنٹ بنائیں گے جس کے پاس اپنا بڑا لینگویج ماڈل (LLM) ہوگا۔ فی الحال، آئیے دیکھتے ہیں کہ ہم سرور پر فیچرز کو کیسے فعال کر سکتے ہیں:

#### رسٹ

مین فنکشن میں، کلائنٹ کو انیشیٹ کرنے کے بعد، ہم سرور کو انیشیٹ کر سکتے ہیں اور اس کی کچھ فیچرز کی فہرست بنا سکتے ہیں۔

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- فیچرز کو فعال کرنا

فیچرز کو فعال کرنے کے لیے ہمیں یہ یقینی بنانا ہوگا کہ ہم درست آرگومنٹس اور بعض اوقات اس چیز کا نام فراہم کریں جسے ہم فعال کرنے کی کوشش کر رہے ہیں۔

#### ٹائپ اسکرپٹ

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

اوپر دیے گئے کوڈ میں ہم نے:

- ایک ریسورس پڑھا، ہم ریسورس کو `readResource()` کال کر کے اور `uri` فراہم کر کے کال کرتے ہیں۔ یہ سرور سائیڈ پر کچھ اس طرح نظر آئے گا:

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

    ہمارا `uri` ویلیو `file://example.txt` سرور پر `file://{name}` سے میچ کرتا ہے۔ `example.txt` کو `name` پر میپ کیا جائے گا۔

- ایک ٹول کو کال کیا، ہم اسے اس کے `name` اور اس کے `arguments` کو مخصوص کر کے کال کرتے ہیں:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- پرامپٹ حاصل کریں، پرامپٹ حاصل کرنے کے لیے، آپ `getPrompt()` کو `name` اور `arguments` کے ساتھ کال کرتے ہیں۔ سرور کوڈ کچھ اس طرح نظر آتا ہے:

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

    اور آپ کا نتیجہ کلائنٹ کوڈ اس طرح نظر آتا ہے تاکہ سرور پر ڈکلیئر کردہ چیز سے میچ کرے:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### پائتھون

```python
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

اوپر دیے گئے کوڈ میں ہم نے:

- `read_resource` کا استعمال کرتے ہوئے ایک ریسورس `greeting` کو کال کیا۔
- `call_tool` کا استعمال کرتے ہوئے ایک ٹول `add` کو فعال کیا۔

#### .نیٹ

1. ایک ٹول کو کال کرنے کے لیے کچھ کوڈ شامل کریں:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. نتیجہ پرنٹ کرنے کے لیے، یہاں کچھ کوڈ ہے جو اس کو ہینڈل کرے گا:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### جاوا

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

اوپر دیے گئے کوڈ میں ہم نے:

- `callTool()` میتھڈ کا استعمال کرتے ہوئے کئی کیلکولیٹر ٹولز کو کال کیا، جس میں `CallToolRequest` آبجیکٹس شامل ہیں۔
- ہر ٹول کال میں اس ٹول کا نام اور ایک `Map` شامل ہے جو اس ٹول کے لیے درکار آرگومنٹس کو فراہم کرتا ہے۔
- سرور ٹولز مخصوص پیرامیٹر ناموں (جیسے "a"، "b" ریاضیاتی آپریشنز کے لیے) کی توقع کرتے ہیں۔
- نتائج `CallToolResult` آبجیکٹس کے طور پر واپس کیے جاتے ہیں جن میں سرور سے جواب شامل ہوتا ہے۔

#### رسٹ

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

### -5- کلائنٹ چلائیں

کلائنٹ کو چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں:

#### ٹائپ اسکرپٹ

اپنے "scripts" سیکشن میں *package.json* میں درج ذیل اندراج شامل کریں:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### پائتھون

درج ذیل کمانڈ کے ساتھ کلائنٹ کو کال کریں:

```sh
python client.py
```

#### .نیٹ

```sh
dotnet run
```

#### جاوا

پہلے، یہ یقینی بنائیں کہ آپ کا MCP سرور `http://localhost:8080` پر چل رہا ہے۔ پھر کلائنٹ کو چلائیں:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

متبادل طور پر، آپ مکمل کلائنٹ پروجیکٹ کو `03-GettingStarted\02-client\solution\java` فولڈر میں فراہم کردہ حل میں چلا سکتے ہیں:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### رسٹ

```bash
cargo fmt
cargo run
```

## اسائنمنٹ

اس اسائنمنٹ میں، آپ وہ سب کچھ استعمال کریں گے جو آپ نے کلائنٹ بنانے میں سیکھا ہے، لیکن اپنا کلائنٹ بنائیں گے۔

یہاں ایک سرور ہے جسے آپ کو اپنے کلائنٹ کوڈ کے ذریعے کال کرنا ہوگا، دیکھیں کہ کیا آپ سرور میں مزید فیچرز شامل کر سکتے ہیں تاکہ یہ زیادہ دلچسپ ہو۔

### ٹائپ اسکرپٹ

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

### پائتھون

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

### .نیٹ

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

اس پروجیکٹ کو دیکھیں تاکہ آپ دیکھ سکیں کہ [پرامپٹس اور وسائل کیسے شامل کریں](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)۔

یہ لنک بھی چیک کریں کہ [پرامپٹس اور وسائل کو کیسے فعال کریں](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)۔

### رسٹ

پچھلے سیکشن میں، آپ نے سیکھا کہ رسٹ کے ساتھ ایک سادہ MCP سرور کیسے بنایا جائے۔ آپ اس پر مزید کام کر سکتے ہیں یا رسٹ پر مبنی MCP سرور کی مزید مثالوں کے لیے یہ لنک چیک کریں: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## حل

**حل فولڈر** میں مکمل، چلنے کے لیے تیار کلائنٹ امپلیمنٹیشنز شامل ہیں جو اس ٹیوٹوریل میں شامل تمام تصورات کو ظاہر کرتی ہیں۔ ہر حل میں کلائنٹ اور سرور کوڈ شامل ہے جو الگ الگ، خود مختار پروجیکٹس میں منظم ہیں۔

### 📁 حل کا ڈھانچہ

حل کی ڈائریکٹری پروگرامنگ زبان کے لحاظ سے منظم ہے:

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

### 🚀 ہر حل میں کیا شامل ہے؟

ہر زبان کے مخصوص حل میں شامل ہے:

- **مکمل کلائنٹ امپلیمنٹیشن** جس میں ٹیوٹوریل کے تمام فیچرز شامل ہیں۔
- **کام کرنے والا پروجیکٹ ڈھانچہ** جس میں مناسب ڈیپینڈنسیز اور کنفیگریشن شامل ہیں۔
- **بلڈ اور رن اسکرپٹس** آسان سیٹ اپ اور عمل درآمد کے لیے۔
- **تفصیلی README** زبان کے لحاظ سے مخصوص ہدایات کے ساتھ۔
- **ایرر ہینڈلنگ** اور نتیجہ پروسیسنگ کی مثالیں۔

### 📖 حل کا استعمال

1. **اپنی پسندیدہ زبان کے فولڈر پر جائیں**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **ہر فولڈر میں README ہدایات پر عمل کریں**:
   - ڈیپینڈنسیز انسٹال کرنا
   - پروجیکٹ کو بلڈ کرنا
   - کلائنٹ کو چلانا

3. **مثال آؤٹ پٹ** جو آپ کو دیکھنا چاہیے:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

مکمل دستاویزات اور مرحلہ وار ہدایات کے لیے، دیکھیں: **[📖 حل کی دستاویزات](./solution/README.md)**

## 🎯 مکمل مثالیں

ہم نے اس ٹیوٹوریل میں شامل تمام پروگرامنگ زبانوں کے لیے مکمل، کام کرنے والے کلائنٹ امپلیمنٹیشنز فراہم کی ہیں۔ یہ مثالیں اوپر بیان کردہ مکمل فعالیت کو ظاہر کرتی ہیں اور آپ کے اپنے پروجیکٹس کے لیے حوالہ امپلیمنٹیشنز یا آغاز کے پوائنٹس کے طور پر استعمال کی جا سکتی ہیں۔

### دستیاب مکمل مثالیں

| زبان | فائل | وضاحت |
|----------|------|-------------|
| **جاوا** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | مکمل جاوا کلائنٹ جو SSE ٹرانسپورٹ استعمال کرتا ہے اور جامع ایرر ہینڈلنگ فراہم کرتا ہے |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | مکمل C# کلائنٹ جو stdio ٹرانسپورٹ استعمال کرتا ہے اور خودکار سرور اسٹارٹ اپ فراہم کرتا ہے |
| **ٹائپ اسکرپٹ** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | مکمل ٹائپ اسکرپٹ کلائنٹ جو مکمل MCP پروٹوکول سپورٹ فراہم کرتا ہے |
| **پائتھون** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | مکمل پائتھون کلائنٹ جو async/
ہر مکمل مثال میں شامل ہے:

- ✅ **کنکشن قائم کرنا** اور خرابیوں کا ازالہ  
- ✅ **سرور کی دریافت** (اوزار، وسائل، اور جہاں ضروری ہو وہاں پرامپٹس)  
- ✅ **کیلکولیٹر کے آپریشنز** (جمع، تفریق، ضرب، تقسیم، مدد)  
- ✅ **نتائج کی پروسیسنگ** اور فارمیٹ شدہ آؤٹ پٹ  
- ✅ **جامع خرابیوں کا ازالہ**  
- ✅ **صاف اور دستاویزی کوڈ** مرحلہ وار تبصروں کے ساتھ  

### مکمل مثالوں کے ساتھ شروعات کریں

1. **اپنی پسندیدہ زبان منتخب کریں** اوپر دی گئی جدول سے  
2. **مکمل مثال کی فائل کا جائزہ لیں** تاکہ مکمل عمل کو سمجھ سکیں  
3. **مثال کو چلائیں** [`complete_examples.md`](./complete_examples.md) میں دی گئی ہدایات کے مطابق  
4. **مثال میں ترمیم کریں اور اسے اپنے مخصوص استعمال کے لیے بڑھائیں**  

ان مثالوں کو چلانے اور اپنی مرضی کے مطابق بنانے کے بارے میں تفصیلی دستاویزات کے لیے دیکھیں: **[📖 مکمل مثالوں کی دستاویزات](./complete_examples.md)**  

### 💡 حل بمقابلہ مکمل مثالیں

| **حل کا فولڈر** | **مکمل مثالیں** |
|--------------------|--------------------- |
| مکمل پروجیکٹ کا ڈھانچہ بلڈ فائلز کے ساتھ | سنگل فائل پر مبنی عمل درآمد |
| ڈیپینڈنسیز کے ساتھ فوری چلنے کے لیے تیار | مرکوز کوڈ کی مثالیں |
| پروڈکشن جیسا سیٹ اپ | تعلیمی حوالہ |
| زبان کے لحاظ سے مخصوص اوزار | زبانوں کے درمیان موازنہ |

دونوں طریقے قیمتی ہیں - **حل کے فولڈر** کو مکمل پروجیکٹس کے لیے استعمال کریں اور **مکمل مثالوں** کو سیکھنے اور حوالہ کے لیے۔

## اہم نکات

اس باب کے اہم نکات کلائنٹس کے بارے میں درج ذیل ہیں:

- کلائنٹس سرور پر فیچرز دریافت کرنے اور انہیں استعمال کرنے دونوں کے لیے استعمال کیے جا سکتے ہیں۔  
- کلائنٹس خود کو شروع کرتے وقت سرور کو بھی شروع کر سکتے ہیں (جیسا کہ اس باب میں بیان کیا گیا ہے) لیکن کلائنٹس چلتے ہوئے سرورز سے بھی جڑ سکتے ہیں۔  
- سرور کی صلاحیتوں کو جانچنے کا ایک بہترین طریقہ ہے، متبادل جیسے انسپکٹر کے ساتھ، جیسا کہ پچھلے باب میں بیان کیا گیا تھا۔  

## اضافی وسائل

- [MCP میں کلائنٹس بنانا](https://modelcontextprotocol.io/quickstart/client)

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)  
- [.Net کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)  
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)  
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)  
- [پائتھون کیلکولیٹر](../../../../03-GettingStarted/samples/python)  
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)  

## آگے کیا ہے

- اگلا: [ایک LLM کے ساتھ کلائنٹ بنانا](../03-llm-client/README.md)  

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔