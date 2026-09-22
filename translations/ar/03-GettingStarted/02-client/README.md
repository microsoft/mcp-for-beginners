# إنشاء عميل

العملاء هم تطبيقات أو نصوص مخصصة تتواصل مباشرة مع خادم MCP لطلب الموارد، الأدوات، والتنبيهات. بخلاف استخدام أداة المفتش التي توفر واجهة رسومية للتفاعل مع الخادم، فإن كتابة عميل خاص بك يتيح التفاعل البرمجي والآلي. يتيح ذلك للمطورين دمج قدرات MCP في سير عملهم الخاص، وأتمتة المهام، وبناء حلول مخصصة تلبي الاحتياجات المحددة.

## نظرة عامة

تقدم هذه الدرس مفهوم العملاء داخل نظام بروتوكول سياق النموذج (MCP). ستتعلم كيفية كتابة عميل خاص بك وربطه بخادم MCP.

## أهداف التعلم

بحلول نهاية هذا الدرس، ستكون قادرًا على:

- فهم ما يمكن أن يفعله العميل.
- كتابة عميل خاص بك.
- الاتصال باختبار العميل مع خادم MCP لضمان عمل الأخير كما هو متوقع.

## ما الذي يتضمنه كتابة عميل؟

لكتابة عميل، ستحتاج إلى القيام بما يلي:

- **استيراد المكتبات الصحيحة**. ستستخدم نفس المكتبة كما في السابق، ولكن بمكونات مختلفة.
- **إنشاء كائن عميل**. هذا يتطلب إنشاء مثيل للعميل وربطه بطريقة النقل المختارة.
- **اختيار الموارد التي سيتم عرضها**. يأتي خادم MCP مزودًا بموارد وأدوات وتنبيهات، تحتاج إلى تحديد ما ستدرجه.
- **دمج العميل في تطبيق المضيف**. بمجرد معرفة قدرات الخادم، تحتاج إلى دمج ذلك في تطبيق المضيف بحيث عند إدخال المستخدم تنبيه أو أمر آخر يتم استدعاء ميزة الخادم المقابلة.

الآن بعد أن فهمنا على مستوى عالٍ ما سنقوم به، لنلق نظرة على مثال.

### مثال على عميل

لنلق نظرة على هذا المثال للعميل:

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

// قائمة المطالبات
const prompts = await client.listPrompts();

// الحصول على مطالبة
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// قائمة الموارد
const resources = await client.listResources();

// قراءة مورد
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// استدعاء أداة
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

في الكود السابق قمنا بـ:

- استيراد المكتبات
- إنشاء مثيل للعميل وربطه باستخدام stdio للنقل.
- سرد التنبيهات والموارد والأدوات وتنفيذها جميعًا.

ها هو لديك، عميل قادر على التحدث إلى خادم MCP.

لنأخذ وقتنا في قسم التمرين التالي ونفصل كل جزء من الكود ونشرح ما يحدث.

## تمرين: كتابة عميل

كما ذُكر أعلاه، دعنا نأخذ وقتنا في شرح الكود، وبالطبع يمكنك كتابة الكود جنبًا إلى جنب إذا أردت.

### -1- استيراد المكتبات

دعنا نستورد المكتبات التي نحتاجها، سنحتاج مراجع للعميل وبروتوكول النقل المختار لدينا، stdio. stdio هو بروتوكول للأشياء التي من المفترض أن تعمل على جهازك المحلي. SSE هو بروتوكول نقل آخر سنبينه في فصول لاحقة، لكنه خيار آخر. الآن، دعنا نستمر باستخدام stdio.

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

بالنسبة لـ Java، ستنشئ عميلًا يتصل بخادم MCP من التمرين السابق. باستخدام نفس هيكل مشروع Java Spring Boot من [البدء مع MCP Server](../../../../03-GettingStarted/01-first-server/solution/java)، أنشئ صف Java جديد يسمى `SDKClient` في مجلد `src/main/java/com/microsoft/mcp/sample/client/` وأضف الاستيرادات التالية:

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

ستحتاج إلى إضافة التبعيات التالية إلى ملف `Cargo.toml` الخاص بك.

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

من هناك، يمكنك استيراد المكتبات اللازمة في كود العميل الخاص بك.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

لننتقل إلى جزء الإنشاء.

### -2- إنشاء العميل والنقل

سنحتاج إلى إنشاء مثيل للنقل وأيضًا للعميل:

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

في الكود السابق قمنا بـ:

- إنشاء مثيل لنقل stdio. لاحظ كيف يحدد الأمر والمعاملات لكيفية إيجاد وإطلاق الخادم، وهذا شيء نحتاجه عند إنشاء العميل.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- إنشاء مثيل للعميل بإعطائه اسمًا وإصدارًا.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- ربط العميل بالنقل المختار.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# إنشاء معلمات الخادم لاتصال stdio
server_params = StdioServerParameters(
    command="mcp",  # قابل للتنفيذ
    args=["run", "server.py"],  # وسائط سطر أوامر اختيارية
    env=None,  # متغيرات بيئة اختيارية
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # تهيئة الاتصال
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

في الكود السابق قمنا بـ:

- استيراد المكتبات المطلوبة
- إنشاء كائن معلمات للخادم لاستخدامه لتشغيل الخادم حتى نتمكن من الاتصال به بالعميل.
- تعريف طريقة `run` التي تستدعي `stdio_client` التي تبدأ جلسة عميل.
- إنشاء نقطة دخول حيث نوفر طريقة `run` لـ `asyncio.run`.

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

في الكود السابق قمنا بـ:

- استيراد المكتبات المطلوبة.
- إنشاء نقل stdio وإنشاء عميل `mcpClient`. الأخير هو شيء سنستخدمه لسرد وتنفيذ الميزات على خادم MCP.

ملاحظة، في "المعاملات"، يمكنك الإشارة إلى *.csproj* أو إلى الملف التنفيذي.

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
        
        // منطق العميل الخاص بك يذهب هنا
    }
}
```

في الكود السابق قمنا بـ:

- إنشاء طريقة رئيسية تضبط نقل SSE يشير إلى `http://localhost:8080` حيث سيعمل خادم MCP الخاص بنا.
- إنشاء صف العميل الذي يأخذ النقل كمعامل منشئ.
- في طريقة `run`، ننشئ عميل MCP متزامن باستخدام النقل ونهيئ الاتصال.
- استخدمنا نقل SSE (Server-Sent Events) المناسب للاتصال القائم على HTTP مع خوادم MCP لـ Java Spring Boot.

#### Rust

لاحظ أن عميل Rust هذا يفترض أن الخادم مشروع شقيق اسمه "calculator-server" في نفس الدليل. الكود أدناه سيبدأ الخادم ويتصل به.

```rust
async fn main() -> Result<(), RmcpError> {
    // افترض أن الخادم هو مشروع شقيق يُدعى "calculator-server" في نفس الدليل
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

    // مطلوب: التهيئة

    // مطلوب: سرد الأدوات

    // مطلوب: استدعاء أداة الإضافة بالمعاملات = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- سرد ميزات الخادم

لدينا الآن عميل يمكن الاتصال به إذا تم تشغيل البرنامج. ومع ذلك، فهو لا يعرض ميزاته فعليًا، فلنقم بذلك الآن:

#### TypeScript

```typescript
// قائمة المطالبات
const prompts = await client.listPrompts();

// قائمة الموارد
const resources = await client.listResources();

// قائمة الأدوات
const tools = await client.listTools();
```

#### Python

```python
# سرد الموارد المتاحة
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# سرد الأدوات المتاحة
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

هنا نسرد الموارد المتاحة، `list_resources()` والأدوات `list_tools` ونطبعها.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

أعلاه مثال عن كيفية سرد الأدوات على الخادم. لكل أداة، نطبع اسمها.

#### Java

```java
// قائمة وعرض الأدوات
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// يمكنك أيضًا استخدام أمر ping للخادم للتحقق من الاتصال
client.ping();
```

في الكود السابق قمنا بـ:

- استدعاء `listTools()` للحصول على جميع الأدوات المتاحة من خادم MCP.
- استخدام `ping()` للتحقق من أن الاتصال بالخادم يعمل.
- يحتوي `ListToolsResult` على معلومات عن كل الأدوات بما في ذلك أسمائها، أوصافها، ومخططات الإدخال.

رائع، الآن لدينا جميع الميزات. الآن السؤال هو متى نستخدمها؟ حسنًا، هذا العميل بسيط جدًا، بسيط بمعنى أننا سنحتاج لاستدعاء الميزات صراحةً متى أردنا ذلك. في الفصل التالي، سننشئ عميلًا أكثر تقدمًا يملك وصولًا لنموذجه اللغوي الكبير الخاص، LLM. الآن، دعنا نرى كيف يمكننا استدعاء ميزات الخادم:

#### Rust

في الدالة الرئيسية، بعد تهيئة العميل، يمكننا تهيئة الخادم وسرد بعض ميزاته.

```rust
// تهيئة
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// قائمة الأدوات
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- استدعاء الميزات

لاستدعاء الميزات نحتاج إلى التأكد من تحديد المعاملات الصحيحة وفي بعض الحالات اسم ما نحاول استدعاءه.

#### TypeScript

```typescript

// قراءة مورد
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// استدعاء أداة
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// استدعاء موجه
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

في الكود السابق قمنا بـ:

- قراءة مورد، نستدعي المورد بواسطة `readResource()` مع تحديد `uri`. هذا ما قد يبدو عليه على جانب الخادم:

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

    قيمة `uri` لدينا `file://example.txt` تتطابق مع `file://{name}` على الخادم. `example.txt` سيتم ربطها بـ `name`.

- استدعاء أداة، نستدعيها بتحديد اسمها `name` ومعاملاتها `arguments` بهذا الشكل:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- الحصول على تنبيه، لاستدعاء تنبيه، تستدعي `getPrompt()` مع `name` و `arguments`. يبدو كود الخادم كالتالي:

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

    لذا يبدو كود العميل الناتج هكذا ليتطابق مع المعلن في الخادم:

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
# قراءة مورد
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# استدعاء أداة
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

في الكود السابق قمنا بـ:

- استدعاء مورد يسمى `greeting` باستخدام `read_resource`.
- استدعاء أداة اسمها `add` باستخدام `call_tool`.

#### .NET

1. لنضيف بعض الكود لاستدعاء أداة:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. لطباعة النتيجة، إليك بعض الكود للتعامل معها:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// استدعاء أدوات الحاسبة المختلفة
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

في الكود السابق قمنا بـ:

- استدعاء أدوات حاسبة متعددة باستخدام طريقة `callTool()` مع كائنات `CallToolRequest`.
- كل استدعاء أداة يحدد اسم الأداة و `Map` من المعاملات المطلوبة لتلك الأداة.
- تتوقع أدوات الخادم أسماء معلمات محددة (مثل "a"، "b" للعمليات الرياضية).
- تُعاد النتائج ككائنات `CallToolResult` تحتوي على الرد من الخادم.

#### Rust

```rust
// استدعاء أداة الجمع بالمعاملات = {"a": 3, "b": 2}
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

### -5- تشغيل العميل

لتشغيل العميل، اكتب الأمر التالي في الطرفية:

#### TypeScript

أضف الإدخال التالي إلى قسم "scripts" الخاص بك في *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

استدع العميل بالأمر التالي:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

أولاً، تأكد من أن خادم MCP الخاص بك يعمل على `http://localhost:8080`. ثم شغل العميل:

```bash
# بناء مشروعك
./mvnw clean compile

# تشغيل العميل
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

بدلاً من ذلك، يمكنك تشغيل مشروع العميل الكامل الموجود في مجلد الحل `03-GettingStarted\02-client\solution\java`:

```bash
# الانتقال إلى دليل الحل
cd 03-GettingStarted/02-client/solution/java

# بناء وتشغيل ملف JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## المهمة

في هذه المهمة، ستستخدم ما تعلمته في إنشاء عميل لكن عليك إنشاء عميل خاص بك.

إليك خادم يمكنك استخدامه ويجب أن تستدعيه عبر كود العميل الخاص بك، راجع إذا كان بإمكانك إضافة ميزات أخرى إلى الخادم لجعله أكثر إثارة.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// إنشاء خادم MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// إضافة أداة إضافة
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// إضافة مورد ترحيب ديناميكي
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

// بدء استقبال الرسائل على الإدخال القياسي وإرسال الرسائل على الإخراج القياسي

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
# سيرفر.py
from mcp.server.fastmcp import FastMCP

# إنشاء خادم MCP
mcp = FastMCP("Demo")


# إضافة أداة الجمع
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# إضافة مورد ترحيب ديناميكي
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

راجع هذا المشروع لترى كيفية [إضافة تنبيهات وموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

أيضًا، اطلع على هذا الرابط لكيفية استدعاء [التنبيهات والموارد](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

في [القسم السابق](../../../../03-GettingStarted/01-first-server)، تعلمت كيفية إنشاء خادم MCP بسيط باستخدام Rust. يمكنك الاستمرار في البناء عليه أو الاطلاع على هذا الرابط لمزيد من أمثلة خوادم MCP القائمة على Rust: [أمثلة خادم MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## الحل

يحتوي **مجلد الحل** على تطبيقات جاهزة للعمل للعملاء تظهر جميع المفاهيم التي تمت تغطيتها في هذا الدرس. كل حل يشمل كود العميل والخادم منظم في مشاريع منفصلة ومستقلة.

### 📁 هيكل الحل

يتم تنظيم دليل الحل حسب لغة البرمجة:

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

### 🚀 ماذا يتضمن كل حل

كل حل خاص بلغة يقدم:

- **تنفيذ عميل كامل** بكل الميزات من الدرس
- **هيكل مشروع فعال** مع التبعيات والإعداد الصحيح
- **برامج بناء وتشغيل** لتسهيل الإعداد والتنفيذ
- **وثائق README مفصلة** مع تعليمات خاصة باللغة
- **أمثلة على معالجة الأخطاء** ومعالجة النتائج

### 📖 استخدام الحلول

1. **انتقل إلى مجلد اللغة المفضل لديك**:

   ```bash
   cd solution/typescript/    # لـ TypeScript
   cd solution/java/          # لـ Java
   cd solution/python/        # لـ Python
   cd solution/dotnet/        # لـ .NET
   ```

2. **اتبع تعليمات README** في كل مجلد لـ:
   - تثبيت التبعيات
   - بناء المشروع
   - تشغيل العميل

3. **الناتج المتوقع** الذي يجب أن تراه:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

للتوثيقات الكاملة والتعليمات خطوة بخطوة، راجع: **[📖 توثيق الحل](./solution/README.md)**

## 🎯 أمثلة كاملة

قدمنا تطبيقات عميل كاملة وعاملة لكل لغات البرمجة التي تم تغطيتها في هذا الدرس. توضح هذه الأمثلة الوظائف الكاملة الموضحة أعلاه ويمكن استخدامها كنماذج مرجعية أو نقاط انطلاق لمشاريعك الخاصة.

### الأمثلة الكاملة المتاحة

| اللغة | الملف | الوصف |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | عميل Java كامل باستخدام نقل SSE مع معالجة أخطاء شاملة |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | عميل C# كامل باستخدام نقل stdio مع بدء تشغيل تلقائي للخادم |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | عميل TypeScript كامل بدعم كامل لبروتوكول MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | عميل Python كامل يستخدم أنماط async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | عميل Rust كامل يستخدم Tokio للعمليات غير المتزامنة |

تتضمن كل الأمثلة الكاملة:

- ✅ **إقامة الاتصال** ومعالجة الأخطاء
- ✅ **اكتشاف الخادم** (الأدوات، الموارد، التنبيهات حيثما ينطبق)
- ✅ **عمليات الحاسبة** (الجمع، الطرح، الضرب، القسمة، المساعدة)
- ✅ **معالجة النتائج** والإخراج المنسق
- ✅ **معالجة أخطاء شاملة**

- ✅ **شفرة نظيفة وموثقة** مع تعليقات خطوة بخطوة

### البدء مع أمثلة كاملة

1. **اختر اللغة المفضلة لديك** من الجدول أعلاه
2. **راجع ملف المثال الكامل** لفهم التنفيذ الكامل
3. **شغّل المثال** باتباع التعليمات في [`complete_examples.md`](./complete_examples.md)
4. **عدل ووسع** المثال لحالتك الخاصة

لمزيد من التوثيق التفصيلي حول تشغيل وتخصيص هذه الأمثلة، انظر: **[📖 توثيق الأمثلة الكاملة](./complete_examples.md)**

### 💡 الحل مقابل الأمثلة الكاملة

| **مجلد الحل** | **الأمثلة الكاملة** |
|--------------------|--------------------- |
| هيكل المشروع الكامل مع ملفات البناء | تنفيذات ملف واحد |
| جاهز للتشغيل مع التبعيات | أمثلة كود مركزة |
| إعداد يشبه بيئة الإنتاج | مرجع تعليمي |
| أدوات خاصة باللغة | مقارنة بين اللغات |

كلا النهجين ذو قيمة - استخدم **مجلد الحل** للمشاريع الكاملة و**الأمثلة الكاملة** للتعلم والمرجعية.

## النقاط الرئيسية

النقاط الرئيسية لهذا الفصل حول العملاء هي:

- يمكن استخدامها لاكتشاف الميزات واستدعائها على الخادم.
- يمكنها بدء خادم أثناء بدء تشغيلها (كما في هذا الفصل) ولكن يمكن للعملاء الاتصال بالخوادم الجارية أيضًا.
- هي طريقة رائعة لاختبار قدرات الخادم إلى جانب بدائل مثل المفتش كما وُصف في الفصل السابق.

## موارد إضافية

- [بناء العملاء في MCP](https://modelcontextprotocol.io/quickstart/client)

## عينات

- [حاسبة جافا](../samples/java/calculator/README.md)
- [حاسبة .NET](../../../../03-GettingStarted/samples/csharp)
- [حاسبة جافاسكريبت](../samples/javascript/README.md)
- [حاسبة تايبسكريبت](../samples/typescript/README.md)
- [حاسبة بايثون](../../../../03-GettingStarted/samples/python)
- [حاسبة راست](../../../../03-GettingStarted/samples/rust)

## ما التالي

- التالي: [إنشاء عميل مع LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->