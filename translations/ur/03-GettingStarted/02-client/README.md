# کلائنٹ بنانا

کلائنٹ حسب ضرورت ایپلیکیشنز یا اسکرپٹس ہوتے ہیں جو MCP سرور سے براہ راست رابطہ کرتے ہیں تاکہ وسائل، ٹولز، اور پرامپٹس کی درخواست کی جا سکے۔ انسپکٹر ٹول کے ذریعہ جو سرور کے ساتھ گرافیکل انٹرفیس فراہم کرتا ہے کے برعکس، اپنا کلائنٹ لکھنے سے پروگراماتی اور خودکار تعاملات ممکن ہوتے ہیں۔ اس سے ڈیولپرز کو MCP کی صلاحیتوں کو اپنے کام کے بہاؤ میں شامل کرنے، کام کو خودکار بنانے، اور مخصوص ضروریات کے مطابق حسب ضرورت حل تیار کرنے کی اجازت ملتی ہے۔

## جائزہ

یہ سبق ماڈل کانٹیکسٹ پروٹوکول (MCP) ماحولیاتی نظام میں کلائنٹس کے تصور کا تعارف کراتا ہے۔ آپ سیکھیں گے کہ اپنا کلائنٹ کیسے لکھیں اور اسے MCP سرور سے کیسے جوڑیں۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ درج ذیل کر سکیں گے:

- سمجھنا کہ کلائنٹ کیا کر سکتا ہے۔
- اپنا کلائنٹ لکھنا۔
- کلائنٹ کو MCP سرور سے جوڑنا اور ٹیسٹ کرنا تاکہ اس بات کو یقینی بنایا جا سکے کہ وہ توقع کے مطابق کام کر رہا ہے۔

## کلائنٹ لکھنے میں کیا آتا ہے؟

کلائنٹ لکھنے کے لیے، آپ کو درج ذیل کرنے کی ضرورت ہوگی:

- **درست لائبریریاں امپورٹ کریں**۔ آپ وہی لائبریری استعمال کریں گے جو پہلے استعمال کی تھی، بس مختلف کنسٹرکٹس کے ساتھ۔
- **کلائنٹ کا ایک مثال بنائیں**۔ اس میں ایک کلائنٹ کی مثال بنانا اور منتخب کردہ ٹرانسپورٹ میتھڈ سے اسے جوڑنا شامل ہوگا۔
- **یہ فیصلہ کریں کہ کون سے وسائل کی فہرست بنانی ہے**۔ آپ کے MCP سرور میں وسائل، ٹولز اور پرامپٹس شامل ہیں، آپ کو فیصلہ کرنا ہوگا کہ کونسی فہرست بنانی ہے۔
- **کلائنٹ کو ہوسٹ ایپلیکیشن کے ساتھ ضم کریں**۔ جب آپ کو سرور کی صلاحیتوں کا پتہ چل جائے تو آپ کو اسے اپنی ہوسٹ ایپلیکیشن میں شامل کرنا ہوگا تاکہ اگر کوئی صارف کوئی پرامپٹ یا دوسرا کمانڈ ٹائپ کرے تو متعلقہ سرور کی خصوصیت چلائی جائے۔

اب جب کہ ہم نے اعلی سطح پر سمجھ لیا ہے کہ ہمیں کیا کرنا ہے، آئیں اگلے حصے میں ایک مثال دیکھتے ہیں۔

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

// پرامپٹس کی فہرست بنائیں
const prompts = await client.listPrompts();

// ایک پرامپٹ حاصل کریں
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// وسائل کی فہرست بنائیں
const resources = await client.listResources();

// ایک وسیلہ پڑھیں
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ایک ٹول کال کریں
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

پچھلے کوڈ میں ہم نے:

- لائبریریاں امپورٹ کیں
- کلائنٹ کی ایک مثال بنائی اور stdio کو ٹرانسپورٹ کے طور پر استعمال کرتے ہوئے اسے جوڑا۔
- پرامپٹس، وسائل اور ٹولز کی فہرست بنائی اور ان سب کو چلایا۔

تو یہ رہا، ایک کلائنٹ جو MCP سرور سے بات کر سکتا ہے۔

آئیں اگلے مشق حصے میں وقت لے کر ہر کوڈ کے ٹکڑے کو توڑ کر سمجھتے ہیں کہ کیا ہو رہا ہے۔

## مشق: کلائنٹ لکھنا

جیسا کہ اوپر کہا گیا، آئیے وقت لے کر کوڈ کی وضاحت کرتے ہیں، اور اگر چاہیں تو ساتھ ساتھ کوڈ بھی کریں۔

### -1- لائبریریاں امپورٹ کرنا

آئیے وہ لائبریریاں امپورٹ کریں جو ہمیں چاہیے، ہمیں کلائنٹ اور ہمارے منتخب کردہ ٹرانسپورٹ پروٹوکول stdio کا حوالہ درکار ہوگا۔ stdio ایک پروٹوکول ہے جو آپ کے لوکل مشین پر چلنے والی چیزوں کے لیے ہے۔ SSE ایک اور ٹرانسپورٹ پروٹوکول ہے جسے ہم آئندہ ابواب میں دکھائیں گے لیکن یہ آپ کا دوسرا آپشن ہے۔ ابھی کے لیے، ہم stdio کے ساتھ جاری رکھتے ہیں۔

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

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### جاوا

جاوا کے لیے، آپ ایک ایسا کلائنٹ بنائیں گے جو پچھلی مشق کے MCP سرور سے جُڑتا ہے۔ اسی Java Spring Boot پروجیکٹ کی ساخت استعمال کرتے ہوئے جیسا کہ [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) میں ہے، `src/main/java/com/microsoft/mcp/sample/client/` فولڈر میں ایک نئی Java کلاس `SDKClient` بنائیں اور درج ذیل امپورٹس شامل کریں:

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

آپ کو اپنی `Cargo.toml` فائل میں درج ذیل ڈیپنڈنسیز شامل کرنی ہوں گی۔

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

اس کے بعد، آپ اپنی کلائنٹ کوڈ میں ضروری لائبریریاں امپورٹ کر سکتے ہیں۔

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

اب انسٹینشی ایشن کی طرف چلتے ہیں۔

### -2- کلائنٹ اور ٹرانسپورٹ کو انسٹینشی ایٹ کرنا

ہمیں ٹرانسپورٹ کی ایک مثال اور اپنے کلائنٹ کی ایک مثال بنانی ہوگی:

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

پچھلے کوڈ میں ہم نے:

- stdio ٹرانسپورٹ کی ایک مثال بنائی۔ نوٹ کریں کہ یہ کمانڈ اور دلیلیں مخصوص کرتا ہے تاکہ سرور کو تلاش کیا جا سکے اور شروع کیا جا سکے کیونکہ ہمیں کلائنٹ بناتے وقت یہ کرنا ہوگا۔

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- کلائنٹ کا ایک مثال بنایا گیا، جسے نام اور ورژن دیا گیا۔

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- کلائنٹ کو منتخب کردہ ٹرانسپورٹ سے جوڑا گیا۔

    ```typescript
    await client.connect(transport);
    ```

#### پائتھون

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# سٹیڈیو کنکشن کے لیے سرور کے پیرامیٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابلِ اجرا
    args=["run", "server.py"],  # اختیاری کمانڈ لائن دلائل
    env=None,  # اختیاری ماحول کے متغیرات
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # کنکشن کو ابتدائیہ بنائیں
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

پچھلے کوڈ میں ہم نے:

- مطلوبہ لائبریریاں امپورٹ کیں
- ایک سرور پیرامیٹرز آبجیکٹ بنایا کیونکہ ہم اسے سرور چلانے کے لیے استعمال کریں گے تاکہ ہم کلائنٹ کے ساتھ جڑ سکیں۔
- ایک `run` میتھڈ ڈیفائن کی جو `stdio_client` کو کال کرتا ہے جو کلائنٹ سیشن شروع کرتا ہے۔
- ایک انٹری پوائنٹ بنایا جہاں ہم `run` میتھڈ کو `asyncio.run` میں فراہم کرتے ہیں۔

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

پچھلے کوڈ میں ہم نے:

- مطلوبہ لائبریریاں امپورٹ کیں۔
- stdio ٹرانسپورٹ بنایا اور `mcpClient` نامی کلائنٹ بنایا۔ اس کا استعمال MCP سرور پر فیچرز کی فہرست اور کال کے لیے ہوگا۔

نوٹ کریں، "Arguments" میں آپ *.csproj* فائل یا executable کو پوائنٹ کر سکتے ہیں۔

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
        
        // آپ کا کلائنٹ منطقی یہاں جاتا ہے
    }
}
```

پچھلے کوڈ میں ہم نے:

- ایک مین میتھڈ بنایا جو SSE ٹرانسپورٹ سیٹ اپ کرتا ہے جو `http://localhost:8080` کی طرف اشارہ کرتا ہے جہاں ہمارا MCP سرور چل رہا ہوگا۔
- ایک کلائنٹ کلاس بنایا جو ٹرانسپورٹ کو کنسٹرکٹر پیرامیٹر کے طور پر لیتا ہے۔
- `run` میتھڈ میں، ہم synchronous MCP کلائنٹ بناتے ہیں جو ٹرانسپورٹ استعمال کرتا ہے اور کنکشن کو انیشیلائز کرتا ہے۔
- SSE (سرور بھیجے گئے ایونٹس) ٹرانسپورٹ استعمال کیا جو Java Spring Boot MCP سرورز کے ساتھ HTTP بیسڈ مواصلات کے لیے موزوں ہے۔

#### رسٹ

نوٹ کریں یہ رسٹ کلائنٹ فرض کرتا ہے کہ سرور اسی ڈائریکٹری میں ایک sibling پروجیکٹ ہے جس کا نام "calculator-server" ہے۔ نیچے دیا گیا کوڈ سرور کو شروع کرے گا اور اس سے جڑ جائے گا۔

```rust
async fn main() -> Result<(), RmcpError> {
    // فرض کریں کہ سرور ایک بہن پروجیکٹ ہے جس کا نام "calculator-server" ہے اور وہ اسی ڈائریکٹری میں ہے
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

    // کرنا ہے: ابتدائیہ کاری

    // کرنا ہے: آلات کی فہرست بنائیں

    // کرنا ہے: add ٹول کو دلائل کے ساتھ کال کریں = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- سرور کی خصوصیات کی فہرست بنانا

اب ہمارے پاس ایک کلائنٹ ہے جو پروگرام چلنے پر جڑ سکتا ہے۔ تاہم، یہ اپنی خصوصیات کی فہرست نہیں بناتا، تو آئیں یہ کرتے ہیں:

#### ٹائپ اسکرپٹ

```typescript
// پرامپٹس کی فہرست
const prompts = await client.listPrompts();

// وسائل کی فہرست
const resources = await client.listResources();

// اوزاروں کی فہرست
const tools = await client.listTools();
```

#### پائتھون

```python
# دستیاب وسائل کی فہرست بنائیں
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# دستیاب آلات کی فہرست بنائیں
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

یہاں ہم دستیاب وسائل، `list_resources()` اور ٹولز، `list_tools` کی فہرست بناتے ہیں اور انھیں پرنٹ کرتے ہیں۔

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

اوپر ایک مثال ہے کہ ہم سرور پر موجود ٹولز کی فہرست کیسے بنا سکتے ہیں۔ ہر ٹول کا نام پرنٹ کرتے ہیں۔

#### جاوا

```java
// آلات کی فہرست بنائیں اور نمائش کریں
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// آپ کنکشن کی تصدیق کے لیے سرور کو بھی پنگ کر سکتے ہیں
client.ping();
```

پچھلے کوڈ میں ہم نے:

- `listTools()` کو کال کیا تاکہ MCP سرور سے تمام دستیاب ٹولز حاصل کیے جا سکیں۔
- `ping()` استعمال کیا تاکہ سرور سے کنکشن کام کر رہا ہے یہ تصدیق کی جا سکے۔
- `ListToolsResult` میں تمام ٹولز کی معلومات شامل ہوتی ہے جس میں ان کے نام، وضاحتیں، اور ان پٹ اسکیمے شامل ہیں۔

بہت خوب، اب ہم نے تمام خصوصیات کو حاصل کر لیا ہے۔ اب سوال یہ ہے کہ ہم انہیں کب استعمال کریں؟ یہ کلائنٹ بالکل سادہ ہے، یعنی ہمیں فیچرز کو واضح طور پر کال کرنا ہوگا جب ہم انہیں چاہتے ہیں۔ اگلے باب میں، ہم ایک زیادہ ترقی یافتہ کلائنٹ بنائیں گے جس کے پاس اپنا بڑا زبان ماڈل، LLM، ہوگا۔ ابھی کے لیے، دیکھتے ہیں کہ ہم سرور پر خصوصیات کو کیسے چلائیں:

#### رسٹ

مین فنکشن میں، کلائنٹ کی انیشیلائزیشن کے بعد، ہم سرور کو انیشیلائز کر سکتے ہیں اور اس کی کچھ خصوصیات کی فہرست بنا سکتے ہیں۔

```rust
// ابتدائیہ کریں
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// آلات کی فہرست بنائیں
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- خصوصیات کو چلانا

خصوصیات کو چلانے کے لیے ہمیں یقینی بنانا ہوگا کہ ہم درست دلائل فراہم کریں اور کچھ معاملات میں جس چیز کو کال کر رہے ہیں اس کا نام بھی بتائیں۔

#### ٹائپ اسکرپٹ

```typescript

// ایک ذریعہ پڑھیں
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ایک آلہ کو کال کریں
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// پرامپٹ کو کال کریں
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

پچھلے کوڈ میں ہم نے:

- ایک وسیلہ پڑھا، ہم `readResource()` کال کرتے ہیں اور `uri` مہیا کرتے ہیں۔ یہاں سرور کی طرف سے یہ ممکنہ طور پر کیسا لگتا ہے:

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

    ہمارا `uri` ویلیو `file://example.txt` سرور پر `file://{name}` سے میل کھاتا ہے۔ `example.txt` کو `name` کے ساتھ میپ کیا جائے گا۔

- ایک ٹول کال کیا، ہم اسے اس کے `name` اور `arguments` کے ساتھ کال کرتے ہیں مثلاً:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- پرامپٹ حاصل کیا، `getPrompt()` کو `name` اور `arguments` کے ساتھ کال کیا۔ سرور کوڈ یوں دکھتا ہے:

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

    اور نتیجتاً آپ کا کلائنٹ کوڈ سرور کے اعلان کے مطابق یوں دکھتا ہے:

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
# ایک وسیلہ پڑھیں
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ایک آلہ کال کریں
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

پچھلے کوڈ میں ہم نے:

- `greeting` نامی وسائل کو `read_resource` کے ذریعے کال کیا۔
- `add` نامی ٹول کو `call_tool` کے ذریعے چلایا۔

#### .NET

1. آئیے کچھ کوڈ شامل کریں جو ایک ٹول کال کرے:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. نتیجہ پرنٹ کرنے کے لیے، یہ کوڈ استعمال کریں:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### جاوا

```java
// مختلف کیلکولیٹر ٹولز کو کال کریں
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

پچھلے کوڈ میں ہم نے:

- مختلف کیلکولیٹر ٹولز کو `callTool()` میتھڈ کے ذریعے `CallToolRequest` آبجیکٹس کے ساتھ کال کیا۔
- ہر ٹول کال میں ٹول کا نام اور اس کے لیے درکار دلائل کا `Map` شامل ہے۔
- سرور کے ٹولز مخصوص پیرامیٹر ناموں کی توقع کرتے ہیں (جیسے "a"، "b" ریاضیاتی عملیات کے لیے)۔
- نتائج کو `CallToolResult` آبجیکٹس کی صورت میں واپس کیا جاتا ہے جن میں سرور کی طرف سے جواب ہوتا ہے۔

#### رسٹ

```rust
// آرجومنٹس = {"a": 3, "b": 2} کے ساتھ ایڈ ٹول کال کریں
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

### -5- کلائنٹ چلانا

کلائنٹ چلانے کے لیے، ٹرمینل میں درج ذیل کمانڈ ٹائپ کریں:

#### ٹائپ اسکرپٹ

*package.json* میں "scripts" سیکشن میں درج ذیل انٹری شامل کریں:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### پائتھون

کلائنٹ کو درج ذیل کمانڈ سے کال کریں:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### جاوا

سب سے پہلے، یقینی بنائیں کہ آپ کا MCP سرور `http://localhost:8080` پر چل رہا ہے۔ پھر کلائنٹ چلائیں:

```bash
# اپنا منصوبہ بنائیں
./mvnw clean compile

# کلائنٹ چلائیں
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

آپ مکمل کلائنٹ پروجیکٹ بھی چلا سکتے ہیں جو حل فولڈر `03-GettingStarted\02-client\solution\java` میں موجود ہے:

```bash
# حل کی ڈائریکٹری پر جائیں
cd 03-GettingStarted/02-client/solution/java

# JAR بنائیں اور چلائیں
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### رسٹ

```bash
cargo fmt
cargo run
```

## اسائنمنٹ

اس اسائنمنٹ میں، آپ نے جو کچھ کلائنٹ بنانے میں سیکھا ہے اسے استعمال کریں گے لیکن اپنا کلائنٹ بنائیں گے۔

یہاں ایک سرور ہے جسے آپ استعمال کر سکتے ہیں جو آپ کو اپنے کلائنٹ کوڈ کے ذریعے کال کرنا ہوگا، دیکھیں کہ کیا آپ سرور میں مزید خصوصیات شامل کر سکتے ہیں تاکہ یہ مزید دلچسپ ہو جائے۔

### ٹائپ اسکرپٹ

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ایک MCP سرور بنائیں
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// ایک اضافی آلہ شامل کریں
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// ایک متحرک خیرمقدم وسیلہ شامل کریں
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

// stdin پر پیغامات وصول کرنا شروع کریں اور stdout پر پیغامات بھیجیں

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

# ایک MCP سرور بنائیں
mcp = FastMCP("Demo")


# ایک اضافتی آلہ شامل کریں
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ایک متحرک خوش آمدیدی وسیلہ شامل کریں
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

اس پروجیکٹ کو دیکھیں تاکہ یہ معلوم ہو کہ آپ [پرامپٹس اور وسائل](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs) کیسے شامل کر سکتے ہیں۔

اس لنک کو بھی چیک کریں کہ آپ [پرامپٹس اور وسائل کو کیسے کال کر سکتے ہیں](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)۔

### رسٹ

[پچھلے حصے](../../../../03-GettingStarted/01-first-server) میں، آپ نے سیکھا کہ رسٹ کے ساتھ ایک سادہ MCP سرور کیسے بنایا جاتا ہے۔ آپ اس پر مزید تعمیر کر سکتے ہیں یا اس لنک پر مزید رسٹ بیسڈ MCP سرور مثالیں دیکھ سکتے ہیں: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## حل

**حل فولڈر** مکمل، چلانے کے لیے تیار کلائنٹ امپلیمینٹیشنز پر مشتمل ہے جو اس ٹیوٹوریل میں شامل تمام تصورات کو ظاہر کرتی ہیں۔ ہر حل میں کلائنٹ اور سرور دونوں کے کوڈ الگ، خود مختار پروجیکٹس میں منظم ہیں۔

### 📁 حل کی ساخت

حل کی ڈائریکٹری پروگرامنگ زبان کی بنیاد پر منظم ہے:

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

### 🚀 ہر حل میں کیا شامل ہے

ہر زبان کے مخصوص حل میں شامل ہے:

- **مکمل کلائنٹ امپلیمینٹیشن** جس میں ٹیوٹوریل کی تمام خصوصیات شامل ہیں
- **کام کرنے والا پروجیکٹ سٹرکچر** مناسب ڈیپنڈنسیز اور ترتیبات کے ساتھ
- **بلڈ اور رن اسکرپٹس** آسان سیٹ اپ اور عمل درآمد کے لیے
- **تفصیلی README** مخصوص زبان کی ہدایات کے ساتھ
- **ایرر ہینڈلنگ** اور نتائج کی پروسیسنگ کی مثالیں

### 📖 حل استعمال کرنا

1. **اپنی پسندیدہ زبان کے فولڈر میں جائیں**:

   ```bash
   cd solution/typescript/    # ٹائپ اسکرپٹ کے لیے
   cd solution/java/          # جاوا کے لیے
   cd solution/python/        # پائتھن کے لیے
   cd solution/dotnet/        # .NET کے لیے
   ```

2. **ہر فولڈر میں README کی ہدایات پر عمل کریں**:
   - ڈیپنڈنسیز انسٹال کرنا
   - پروجیکٹ بنانا
   - کلائنٹ چلانا

3. **نمونہ آؤٹ پٹ** جو آپ کو دیکھنی چاہیے:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

مکمل دستاویزات اور مرحلہ وار ہدایات کے لیے دیکھیں: **[📖 حل کی دستاویزات](./solution/README.md)**

## 🎯 مکمل مثالیں

ہم نے اس ٹیوٹوریل میں شامل تمام پروگرامنگ زبانوں کے لیے مکمل، کام کرنے والے کلائنٹ امپلیمینٹیشن مہیا کیے ہیں۔ یہ مثالیں اوپر بیان کردہ مکمل فنکشنالٹی دکھاتی ہیں اور آپ کے اپنے پروجیکٹس کے حوالے یا نقطہ آغاز کے طور پر استعمال کی جا سکتی ہیں۔

### دستیاب مکمل مثالیں

| زبان | فائل | وضاحت |
|----------|------|-------------|
| **جاوا** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ٹرانسپورٹ کے ساتھ مکمل جاوا کلائنٹ، مکمل ایرر ہینڈلنگ کے ساتھ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ٹرانسپورٹ کا استعمال کرنے والا مکمل C# کلائنٹ، خودکار سرور اسٹارٹ اپ کے ساتھ |
| **ٹائپ اسکرپٹ** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | مکمل ٹائپ اسکرپٹ کلائنٹ، MCP پروٹوکول کی مکمل حمایت کے ساتھ |
| **پائتھون** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | async/await پیٹرنز کے ساتھ مکمل پائتھون کلائنٹ |
| **رسٹ** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio کا استعمال کرتے ہوئے async آپریشنز کا مکمل رسٹ کلائنٹ |

ہر مکمل مثال میں شامل ہے:

- ✅ **کنکشن کی اسٹیبلشمنٹ** اور ایرر ہینڈلنگ
- ✅ **سرور دریافت** (جہاں قابل اطلاق ہو، ٹولز، وسائل، پرامپٹس)
- ✅ **کیلکولیٹر آپریشنز** (جمع، تفریق، ضرب، تقسیم، مدد)
- ✅ **نتائج کی پروسیسنگ** اور منظم آؤٹ پٹ
- ✅ **مکمل ایرر ہینڈلنگ**

- ✅ **صاف، دستاویزی کوڈ** مرحلہ وار تبصروں کے ساتھ

### مکمل مثالوں کے ساتھ شروع کرنا

1. اوپر دی گئی جدول سے **اپنی پسندیدہ زبان منتخب کریں**
2. **مکمل مثال فائل کا جائزہ لیں** تاکہ پوری عمل درآمد کو سمجھ سکیں
3. [`complete_examples.md`](./complete_examples.md) میں دی گئی ہدایات کے مطابق **مثال چلائیں**
4. اپنی مخصوص استعمال کے لیے **مثال میں ترمیم کریں اور اسے بڑھائیں**

ان مثالوں کو چلانے اور حسب ضرورت بنانے کے بارے میں تفصیلی دستاویز کے لیے دیکھیں: **[📖 مکمل مثالوں کی دستاویزات](./complete_examples.md)**

### 💡 حل بمقابلہ مکمل مثالیں

| **حل فولڈر** | **مکمل مثالیں** |
|--------------------|--------------------- |
| مکمل پروجیکٹ کا ڈھانچہ بلڈ فائلوں کے ساتھ | ایک فائل میں عمل درآمد |
| انحصار کے ساتھ چلانے کے لیے تیار | مرکزی کوڈ مثالیں |
| پیداوار جیسا سیٹ اپ | تعلیمی حوالہ |
| زبان مخصوص ٹولنگ | زبانوں کے مابین موازنہ |

دونوں طریقے قیمتی ہیں - مکمل پروجیکٹس کے لیے **حل فولڈر** استعمال کریں اور سیکھنے اور حوالہ کے لیے **مکمل مثالیں** استعمال کریں۔

## اہم نکات

اس باب کے کلیدی نکات کلائنٹس کے بارے میں درج ذیل ہیں:

- سرور پر خصوصیات دریافت کرنے اور ان کو چلانے دونوں کے لیے استعمال ہو سکتے ہیں۔
- خود کو شروع کرتے ہوئے سرور شروع کر سکتے ہیں (جیسے اس باب میں) لیکن کلائنٹس چلتے ہوئے سرورز سے بھی جڑ سکتے ہیں۔
- سرور کی صلاحیتوں کو جانچنے کا بہترین طریقہ ہیں، جیسے پچھلے باب میں Inspector کے متبادل کے طور پر بیان کیا گیا تھا۔

## اضافی وسائل

- [MCP میں کلائنٹس بنانا](https://modelcontextprotocol.io/quickstart/client)

## نمونے

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)
- [.NET کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)
- [پائتھون کیلکولیٹر](../../../../03-GettingStarted/samples/python)
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)

## آگے کیا ہے

- اگلا: [ایک LLM کے ساتھ کلائنٹ بنانا](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->