# کلائنٹ بنانا

کلائنٹس کسٹم ایپلیکیشنز یا اسکرپٹس ہوتی ہیں جو براہ راست ایک MCP سرور سے رابطہ کرتی ہیں تاکہ وسائل، ٹولز، اور پرامپٹس کی درخواست کی جا سکے۔ انسپکٹر ٹول استعمال کرنے کے برعکس، جو سرور کے ساتھ گرافیکل انٹرفیس فراہم کرتا ہے، اپنا کلائنٹ لکھنے سے پروگراماتی اور خودکار تعاملات ممکن ہوتے ہیں۔ اس سے ڈویلپرز کو MCP کی صلاحیتوں کو اپنے ورک فلو میں شامل کرنے، کاموں کو خودکار بنانے، اور مخصوص ضروریات کے مطابق کسٹم حل تیار کرنے کی اجازت ملتی ہے۔

## جائزہ

یہ سبق ماڈل کانٹیکسٹ پروٹوکول (MCP) ایکوسسٹم میں کلائنٹس کے تصور کا تعارف کرواتا ہے۔ آپ سیکھیں گے کہ اپنا کلائنٹ کیسے لکھا جائے اور اسے MCP سرور سے کیسے متصل کیا جائے۔

## تعلیمی مقاصد

اس سبق کے اختتام تک آپ قابل ہوں گے کہ:

- سمجھ سکیں کہ کلائنٹ کیا کر سکتا ہے۔
- اپنا کلائنٹ لکھ سکیں۔
- کلائنٹ کو MCP سرور کے ساتھ جوڑیں اور آزمائیں تاکہ یقینی بنایا جا سکے کہ سرور توقع کے مطابق کام کر رہا ہے۔

## کلائنٹ لکھنے میں کیا شامل ہے؟

کلائنٹ لکھنے کے لیے آپ کو درج ذیل کام کرنے ہوں گے:

- **صحیح لائبریریز درآمد کرنا**۔ آپ وہی لائبریری استعمال کریں گے جو پہلے استعمال کی تھی، بس مختلف ساختیں استعمال کریں گے۔
- **کلائنٹ قائم کرنا**۔ اس میں کلائنٹ کی ایک مثال بنانا اور اسے منتخب کردہ ٹرانسپورٹ میتھڈ سے جوڑنا شامل ہوگا۔
- **یہ فیصلہ کرنا کہ کون سے وسائل کی فہرست دیں**۔ آپ کے MCP سرور کے پاس وسائل، ٹولز، اور پرامپٹس موجود ہیں، آپ کو فیصلہ کرنا ہے کہ ان میں سے کون سی فہرست کرنی ہے۔
- **کلائنٹ کو میزبان ایپلیکیشن میں شامل کرنا**۔ جب آپ سرور کی صلاحیتوں کو سمجھ لیں تو انہیں اپنی میزبان ایپلیکیشن میں ضم کریں تاکہ اگر کوئی صارف پرامپٹ یا کوئی اور کمانڈ ٹائپ کرے تو متعلقہ سرور فیچر کال ہو جائے۔

اب جب کہ ہم نے بلند سطح پر سمجھ لیا کہ ہمیں کیا کرنا ہے، آئیں اگلے مرحلے میں ایک مثال دیکھتے ہیں۔

### ایک مثال کلائنٹ

آئیے اس مثال کلائنٹ پر نظر ڈالتے ہیں:

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

// ترغیبات کی فہرست بنائیں
const prompts = await client.listPrompts();

// ایک ترغیب حاصل کریں
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

// ایک آلہ کال کریں
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

اوپر دیے گئے کوڈ میں ہم نے:

- لائبریریز درآمد کیں۔
- کلائنٹ کی ایک مثال بنائی اور اسے stdio ٹرانسپورٹ کے ذریعے جوڑا۔
- پرامپٹس، وسائل، اور ٹولز کی فہرست دی اور انہیں کال کیا۔

یہ رہا آپ کا کلائنٹ جو MCP سرور سے بات کر سکتا ہے۔

اگلے مشق سیکشن میں ہم ہر کوڈ کے ٹکڑے کو تفصیل سے بیان کریں گے اور سمجھائیں گے کہ کیا ہو رہا ہے۔

## مشق: کلائنٹ لکھنا

جیسا کہ اوپر کہا گیا، آئیے ہم کوڈ کو آرام سے سمجھائیں، اور اگر آپ چاہیں تو ساتھ ساتھ کوڈ بھی کریں۔

### -1- لائبریریز درآمد کرنا

آئیں وہ لائبریریز درآمد کریں جن کی ضرورت ہے، ہمیں کلائنٹ اور منتخب شدہ ٹرانسپورٹ پروٹوکول stdio کے حوالے چاہیے ہوں گے۔ stdio ایسے کاموں کے لیے پروٹوکول ہے جو آپ کے لوکل مشین پر چلنے کے لیے ہوتے ہیں۔ SSE ایک اور ٹرانسپورٹ پروٹوکول ہے جو ہم مستقبل کے ابواب میں دکھائیں گے لیکن یہ آپ کا دوسرا آپشن ہے۔ فی الحال، ہم stdio کے ساتھ جاری رکھیں گے۔

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

جاوا کے لیے، آپ ایسا کلائنٹ بنائیں گے جو پچھلی مشق سے MCP سرور سے جڑتا ہو۔ [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java) میں موجود سا‎м Java Spring Boot پروجیکٹ ڈھانچہ استعمال کرتے ہوئے، `src/main/java/com/microsoft/mcp/sample/client/` فولڈر میں ایک نیا Java کلاس `SDKClient` بنائیں اور درج ذیل امپورٹس شامل کریں:

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

آپ کو اپنی `Cargo.toml` فائل میں درج ذیل dependencies شامل کرنا ہوں گی۔

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

اس کے بعد آپ اپنے کلائنٹ کوڈ میں ضروری لائبریریز درآمد کر سکتے ہیں۔

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

آئیے اب انسٹینشی ایشن پر چلتے ہیں۔

### -2- کلائنٹ اور ٹرانسپورٹ کی مثال بنانا

ہمیں ٹرانسپورٹ اور کلائنٹ دونوں کی ایک مثال بنانی ہوگی:

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

اوپر کے کوڈ میں ہم نے:

- stdio ٹرانسپورٹ کی مثال بنائی۔ نوٹ کریں کہ اس میں سرور کو تلاش کرنے اور شروع کرنے کے لیے کمانڈ اور args دیے گئے ہیں، کیونکہ کلائنٹ بناتے وقت ہمیں یہ کرنا ہوگا۔

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- کلائنٹ کی مثال بنائی، اسے نام اور ورژن دیا۔

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- کلائنٹ کو منتخب شدہ ٹرانسپورٹ سے جوڑا۔

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# سٹڈیئو کنکشن کے لئے سرور پیرا میٹرز بنائیں
server_params = StdioServerParameters(
    command="mcp",  # قابل اجرا
    args=["run", "server.py"],  # اختیاری کمانڈ لائن آرگیومنٹس
    env=None,  # اختیاری ماحول کے متغیرات
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # کنکشن کا آغاز کریں
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

اوپر کے کوڈ میں ہم نے:

- ضروری لائبریریز درآمد کیں۔
- ایک سرور پیرامیٹرز آبجیکٹ بنایا تاکہ سرور چلائیں اور کلائنٹ کے ساتھ اسے جوڑ سکیں۔
- `run` میتھڈ ڈیفائن کی جو `stdio_client` کال کرتا ہے جو کلائنٹ سیشن شروع کرتا ہے۔
- ایک انٹری پوائنٹ بنایا جہاں `run` کو `asyncio.run` کے ساتھ فراہم کیا گیا۔

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

اوپر کے کوڈ میں ہم نے:

- ضروری لائبریریز درآمد کیں۔
- stdio ٹرانسپورٹ بنائی اور `mcpClient` کلائنٹ بنایا۔ یہ وہ کلائنٹ ہے جس سے ہم MCP سرور کی خصوصیات کی فہرست اور کال کریں گے۔

نوٹ کریں، "Arguments" میں آپ *.csproj* یا executable دونوں میں سے کسی ایک کا حوالہ دے سکتے ہیں۔

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
        
        // آپ کا کلائنٹ لاجک یہاں جاتا ہے
    }
}
```

اوپر کے کوڈ میں ہم نے:

- ایک مین میتھڈ بنایا جو SSE ٹرانسپورٹ سیٹ کرتا ہے جو `http://localhost:8080` کی طرف اشارہ کرتا ہے جہاں ہمارا MCP سرور چل رہا ہوگا۔
- ایک کلائنٹ کلاس بنائی جو ٹرانسپورٹ کو کنسٹرکٹر پیرامیٹر کے طور پر لیتی ہے۔
- `run` میتھڈ میں ہم نے ٹرانسپورٹ کے ذریعے synchronous MCP کلائنٹ بنایا اور کنکشن انیشیئلائز کیا۔
- SSE (Server-Sent Events) ٹرانسپورٹ استعمال کیا جو HTTP پر مبنی جاوا Spring Boot MCP سرورز کے لیے موزوں ہے۔

#### Rust

نوٹ کریں یہ Rust کلائنٹ فرض کرتا ہے کہ سرور ایک بھائی پروجیکٹ ہے جس کا نام "calculator-server" ہے اور وہی ڈائریکٹری میں ہے۔ نیچے دیا گیا کوڈ سرور کو شروع کرے گا اور اس سے جڑ جائے گا۔

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

    // TODO: شروع کریں

    // TODO: ٹولز کی فہرست بنائیں

    // TODO: add ٹول کو کال کریں جس کے آرگیومنٹس = {"a": 3, "b": 2} ہوں

    client.cancel().await?;
    Ok(())
}
```

### -3- سرور کی خصوصیات کی فہرست دینا

اب ہمارے پاس ایسا کلائنٹ ہے جو پروگرام چلانے پر جڑ سکتا ہے۔ تاہم، یہ واقعی میں اس کی خصوصیات کی فہرست نہیں دیتا، لہٰذا آئیں یہ اگلا کام کرتے ہیں:

#### TypeScript

```typescript
// پرامپٹس کی فہرست
const prompts = await client.listPrompts();

// وسائل کی فہرست
const resources = await client.listResources();

// ٹولز کی فہرست
const tools = await client.listTools();
```

#### Python

```python
# دستیاب وسائل کی فہرست
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# دستیاب آلات کی فہرست
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

یہاں ہم دستیاب وسائل `list_resources()` اور ٹولز `list_tools` کی فہرست دیتے ہیں اور انہیں پرنٹ کرتے ہیں۔

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

اوپر ایک مثال دی گئی ہے کہ سرور کے ٹولز کی فہرست کیسے لی جائے۔ ہر ٹول کے لیے، ہم اس کا نام پرنٹ کرتے ہیں۔

#### Java

```java
// آلات کی فہرست بنائیں اور مظاہرہ کریں
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// آپ کنکشن کی تصدیق کے لیے سرور کو پنگ بھی کر سکتے ہیں
client.ping();
```

اوپر کے کوڈ میں ہم نے:

- MCP سرور سے تمام دستیاب ٹولز حاصل کرنے کے لیے `listTools()` کال کی۔
- کنکشن کی جانچ کے لیے `ping()` کال کی۔
- `ListToolsResult` میں تمام ٹولز کی معلومات شامل ہیں جیسے نام، وضاحتیں، اور ان پٹ اسکیمات۔

عمدہ، اب ہم نے تمام خصوصیات حاصل کر لی ہیں۔ اب سوال یہ ہے کہ ہم ان کا استعمال کب کریں؟ یہ کلائنٹ بہت سادہ ہے، یعنی ہمیں خصوصیات کو واضح طور پر کال کرنا ہوگا جب بھی ہم انہیں چاہیں۔ اگلے باب میں ہم ایک زیادہ پیشرفتہ کلائنٹ بنائیں گے جس کے پاس اپنا بڑا لسانی ماڈل (LLM) ہوگا۔ فی الحال، آتے ہیں سرور کی خصوصیات کو کال کرنے کا طریقہ:

#### Rust

مین فنکشن میں، کلائنٹ انیشیئلائز کرنے کے بعد، ہم سرور کو شروع کر سکتے ہیں اور اس کی کچھ خصوصیات کی فہرست دے سکتے ہیں۔

```rust
// شروع کریں
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// آلات کی فہرست بنائیں
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- خصوصیات کو کال کرنا

خصوصیات کو کال کرنے کے لیے ضروری ہے کہ صحیح دلائل فراہم کیے جائیں اور بعض اوقات اس چیز کا نام بھی جسے ہم کال کرنا چاہتے ہیں۔

#### TypeScript

```typescript

// ایک ذریعہ پڑھیں
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// ایک آلہ کال کریں
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// پرامٹ کال کریں
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

اوپر کے کوڈ میں ہم نے:

- ایک ریسورس کو پڑھا، ہم `readResource()` کال کر کے `uri` فراہم کرتے ہیں۔ سرور سائیڈ پر اس کا غالباً یہ طرز ہوگا:

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

    ہمارا `uri` ویلیو `file://example.txt` سرور پر `file://{name}` سے مماثل ہے۔ `example.txt` کو `name` میں میپ کیا جائے گا۔

- ایک ٹول کو کال کیا، ہم اسے اس کے `name` اور `arguments` فراہم کر کے کال کرتے ہیں جیسے:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- پرامپٹ حاصل کیا، پرامپٹ حاصل کرنے کے لیے `getPrompt()` کال کرتے ہیں، جس میں `name` اور `arguments` ہوتے ہیں۔ سرور کا کوڈ کچھ یوں ہوگا:

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

    اور آپ کا کلائنٹ کوڈ نتیجتاً کچھ یوں ہوگا تاکہ سرور پر بتائے گئے تعریف سے مماثل ہو:

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
# ایک وسیلہ پڑھیں
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# ایک آلہ کال کریں
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

اوپر کے کوڈ میں ہم نے:

- `greeting` نامی ریسورس کو `read_resource` کے ذریعے کال کیا۔
- `add` نامی ٹول کو `call_tool` کے ذریعے کال کیا۔

#### .NET

1. آئیے کچھ کوڈ شامل کرتے ہیں جو ٹول کو کال کرے:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. نتیجہ پرنٹ کرنے کے لیے، درج ذیل کوڈ استعمال کریں:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// مختلف کیلکولیٹر کے اوزار کو کال کریں
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

اوپر کے کوڈ میں ہم نے:

- `callTool()` میتھڈ اور `CallToolRequest` آبجیکٹس کے ذریعے متعدد کیلکولیٹر ٹولز کال کیے۔
- ہر ٹول کال میں ٹول کا نام اور اس کے لیے ضروری دلائل کا `Map` دیا جاتا ہے۔
- سرور کے ٹولز مخصوص پیرامیٹر ناموں (جیسے "a"، "b" ریاضیاتی عمل کے لیے) کی توقع کرتے ہیں۔
- نتائج `CallToolResult` آبجیکٹ کی صورت میں واپس آتے ہیں جن میں سرور سے جوابی ڈیٹا ہوتا ہے۔

#### Rust

```rust
// کال ایڈ ٹول وِد آرگیومنٹس = {"a": 3, "b": 2}
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

#### TypeScript

*package.json* کی "scripts" سیکشن میں درج ذیل انٹری شامل کریں:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

کلائنٹ کو درج ذیل کمانڈ سے کال کریں:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

یا تو یقین دہانی کریں کہ MCP سرور `http://localhost:8080` پر چل رہا ہے۔ پھر کلائنٹ چلائیں:

```bash
# اپنا پروجیکٹ بنائیں
./mvnw clean compile

# کلائنٹ چلائیں
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

متبادل طور پر، آپ حل فولڈر `03-GettingStarted\02-client\solution\java` میں فراہم کردہ مکمل کلائنٹ پروجیکٹ چلا سکتے ہیں:

```bash
# حل کے فولڈر پر جائیں
cd 03-GettingStarted/02-client/solution/java

# JAR بنائیں اور چلائیں
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## اسائنمنٹ

اس اسائنمنٹ میں، آپ نے جو کچھ سیکھا ہے اسے استعمال کرتے ہوئے اپنا کلائنٹ بنائیں گے۔

یہاں ایک سرور دیا گیا ہے جسے آپ اپنے کلائنٹ کوڈ کے ذریعہ کال کریں، دیکھیں کیا آپ سرور میں مزید خصوصیات شامل کر سکتے ہیں تاکہ اسے مزید دلچسپ بنایا جا سکے۔

### TypeScript

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

// ایک متحرک خوش آمدید وسیلہ شامل کریں
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

// stdin پر پیغامات وصول کرنا شروع کریں اور stdout پر پیغامات بھیجنا شروع کریں

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

# ایک MCP سرور بنائیں
mcp = FastMCP("Demo")


# ایک اضافی ٹول شامل کریں
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# ایک متحرک خوش آمدیدی وسائل شامل کریں
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

اس پروجیکٹ کو دیکھیں تاکہ جان سکیں کہ آپ [پرامپٹس اور وسائل کیسے شامل کریں](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs)۔

اس لنک کو بھی چیک کریں کہ [پرامپٹس اور وسائل کو کیسے کال کیا جائے](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/)۔

### Rust

[پچھلے سیکشن](../../../../03-GettingStarted/01-first-server) میں، آپ نے سیکھا کہ Rust کے ساتھ ایک سادہ MCP سرور کیسے بنایا جاتا ہے۔ آپ اس پر مزید تعمیر کر سکتے ہیں یا مزید Rust پر مبنی MCP سرور مثالوں کے لیے یہ لنک دیکھیں: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## حل

**حل فولڈر** میں مکمل، چلانے کے قابل کلائنٹ امپلیمنٹیشنز شامل ہیں جو اس سبق میں زیر بحث تمام تصورات کو ظاہر کرتے ہیں۔ ہر حل میں کلائنٹ اور سرور دونوں کے کوڈ الگ، خود مختار پروجیکٹس میں منظم ہیں۔

### 📁 حل کا ڈھانچہ

حل ڈائریکٹری پروگرامنگ زبان کے لحاظ سے منظم ہے:

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

ہر زبان مخصوص حل فراہم کرتا ہے:

- **مکمل کلائنٹ امپلیمنٹیشن** جس میں سبق کی تمام خصوصیات شامل ہیں
- **کام کرنے والا پروجیکٹ ڈھانچہ** مناسب dependencies اور کنفیگریشن کے ساتھ
- **بلڈ اور رن اسکرپٹس** آسان سیٹ اپ اور اجرا کے لیے
- **تفصیلی README** زبان مخصوص ہدایات کے ساتھ
- **غلطی کا ہینڈلنگ اور نتیجے کی پروسیسنگ کی مثالیں**

### 📖 حل استعمال کرنا

1. **اپنی پسندیدہ زبان کے فولڈر میں جائیں**:

   ```bash
   cd solution/typescript/    # ٹائپ اسکرپٹ کے لیے
   cd solution/java/          # جاوا کے لیے
   cd solution/python/        # پائتھن کے لیے
   cd solution/dotnet/        # ڈاٹ نیٹ کے لیے
   ```

2. **ہر فولڈر میں README کی ہدایات پر عمل کریں**:
   - dependencies انسٹال کرنا
   - پروجیکٹ تعمیر کرنا
   - کلائنٹ چلانا

3. **مثال کے طور پر آپ کو ایسا آؤٹ پٹ دیکھنا چاہیے**:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

مکمل دستاویزات اور مرحلہ وار ہدایات کے لیے دیکھیں: **[📖 حل کی دستاویزات](./solution/README.md)**

## 🎯 مکمل مثالیں

ہم نے تمام پروگرامنگ زبانوں کے لیے مکمل، کام کرنے والے کلائنٹ امپلیمنٹیشنز فراہم کیے ہیں جو اس سبق میں شامل تمام فعالیت کو دکھاتے ہیں اور آپ کے اپنے پروجیکٹس کے لیے حوالہ یا آغاز نقطہ کے طور پر استعمال ہو سکتے ہیں۔

### دستیاب مکمل مثالیں

| زبان | فائل | وضاحت |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | SSE ٹرانسپورٹ استعمال کرتے ہوئے جامع غلطی ہینڈلنگ کے ساتھ مکمل جاوا کلائنٹ |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | stdio ٹرانسپورٹ استعمال کرتے ہوئے مکمل C# کلائنٹ خودکار سرور اسٹارٹ اپ کے ساتھ |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | مکمل TypeScript کلائنٹ جو MCP پروٹوکول کی مکمل حمایت کرتا ہے |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | مکمل Python کلائنٹ جو async/await پیٹرنز استعمال کرتا ہے |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Tokio کے ساتھ async آپریشنز کے لیے مکمل Rust کلائنٹ |

ہر مکمل مثال میں شامل ہیں:
- ✅ **کنکشن قائم کرنا** اور ایرر ہینڈلنگ  
- ✅ **سرور کی دریافت** (ٹولز، وسائل، پرامپٹس جہاں لاگو ہوں)  
- ✅ **کیلکولیٹر آپریشنز** (جمع، منفی، ضرب، تقسیم، مدد)  
- ✅ **نتیجہ کی پروسیسنگ** اور فارمیٹ شدہ آؤٹ پٹ  
- ✅ **جامع ایرر ہینڈلنگ**  
- ✅ **صاف ستھرا، دستاویزی کوڈ** مرحلہ وار تبصروں کے ساتھ  

### مکمل مثالوں کے ساتھ آغاز کرنا  

1. **مندرجہ بالا جدول سے اپنی پسندیدہ زبان منتخب کریں**  
2. **مکمل مثال فائل کا جائزہ لیں** تاکہ مکمل عملدرآمد کو سمجھ سکیں  
3. **مثال چلائیں** [`complete_examples.md`](./complete_examples.md) میں موجود ہدایات کے مطابق  
4. **مثال میں ترمیم کریں اور اسے اپنے مخصوص استعمال کے لیے بڑھائیں**  

ان مثالوں کو چلانے اور حسب ضرورت بنانے کے بارے میں تفصیلی دستاویزات کے لیے دیکھیں: **[📖 مکمل مثالوں کی دستاویزات](./complete_examples.md)**  

### 💡 حل بمقابلہ مکمل مثالیں  

| **حل کا فولڈر** | **مکمل مثالیں** |  
|----------------|-----------------|  
| مکمل پروجیکٹ ساخت بشمول بلڈ فائلیں | واحد فائل امپلیمینٹیشنز |  
| انحصارات کے ساتھ چلانے کے لیے تیار | مخصوص کوڈ مثالیں |  
| پروڈکشن جیسا سیٹ اپ | تعلیمی حوالہ |  
| زبان مخصوص ٹولنگ | زبانوں کے درمیان موازنہ |  

دونوں طریقے قیمتی ہیں - مکمل پروجیکٹس کے لیے **حل کا فولڈر** استعمال کریں اور سیکھنے اور حوالہ کے لیے **مکمل مثالیں**۔  

## اہم نکات  

اس باب کے کلیدی نکات کلائنٹس کے بارے میں درج ذیل ہیں:  

- انہیں سرور کی خصوصیات دریافت کرنے اور چلانے دونوں کے لیے استعمال کیا جا سکتا ہے۔  
- یہ سرور کو خود شروع کرتے ہوئے شروع کر سکتے ہیں (جیسا کہ اس باب میں ہے) لیکن کلائنٹس چل رہے سرورز سے بھی جڑ سکتے ہیں۔  
- یہ سرور کی صلاحیتوں کو جانچنے کا ایک بہترین طریقہ ہے، جیسے کہ انسپیکٹر جیسا متبادل، جیسا کہ پچھلے باب میں بیان کیا گیا تھا۔  

## اضافی وسائل  

- [MCP میں کلائنٹس کی تعمیر](https://modelcontextprotocol.io/quickstart/client)  

## نمونے  

- [جاوا کیلکولیٹر](../samples/java/calculator/README.md)  
- [.نیٹ کیلکولیٹر](../../../../03-GettingStarted/samples/csharp)  
- [جاوا اسکرپٹ کیلکولیٹر](../samples/javascript/README.md)  
- [ٹائپ اسکرپٹ کیلکولیٹر](../samples/typescript/README.md)  
- [پائتھون کیلکولیٹر](../../../../03-GettingStarted/samples/python)  
- [رسٹ کیلکولیٹر](../../../../03-GettingStarted/samples/rust)  

## آگے کیا ہے  

- اگلا: [LLM کے ساتھ کلائنٹ بنانا](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دریافت نامہ**:
یہ دستاویز AI ترجمہ خدمت [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لئے کوشاں ہیں، براہ کرم خیال رکھیں کہ خودکار تراجم میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لئے پیشہ ورانہ انسانی ترجمہ کرنے کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہم پر نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->